"""
App Updates / Changelog

Provides a simple, file-backed update feed for in-app announcements
distinct from external "Medical News" RSS.

Design goals:
- Works offline (local JSON file)
- Allows "seen" tracking per user/device via local JSON
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from config.user_profile import get_current_profile


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
UPDATES_FILE = DATA_DIR / "app_updates.json"
SEEN_FILE = DATA_DIR / "app_updates_seen.json"


@dataclass(frozen=True)
class AppUpdate:
    id: str
    date: str  # ISO date (YYYY-MM-DD)
    title: str
    content: str
    type: str = "update"  # feature | update | improvement | bugfix | announcement


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _read_json(path: Path, default: Any) -> Any:
    try:
        if not path.exists():
            return default
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def load_updates() -> List[AppUpdate]:
    """Load updates from data/app_updates.json (newest first)."""
    _ensure_data_dir()
    raw = _read_json(UPDATES_FILE, default={"updates": []})
    items = raw.get("updates", []) if isinstance(raw, dict) else []

    updates: List[AppUpdate] = []
    for it in items:
        if not isinstance(it, dict):
            continue
        if not it.get("id") or not it.get("title") or not it.get("date"):
            continue
        updates.append(
            AppUpdate(
                id=str(it["id"]),
                date=str(it["date"]),
                title=str(it.get("title", "")),
                content=str(it.get("content", "")),
                type=str(it.get("type", "update")),
            )
        )

    def _sort_key(u: AppUpdate):
        try:
            return datetime.fromisoformat(u.date)
        except Exception:
            return datetime.min

    updates.sort(key=_sort_key, reverse=True)
    return updates


def load_seen_update_ids() -> Set[str]:
    _ensure_data_dir()
    # Backward compatible:
    # - new format: {"profiles": {"noi": [...], "icu": [...]}, ...}
    # - legacy format: {"seen_ids": [...]}
    raw = _read_json(SEEN_FILE, default={"profiles": {}})
    if not isinstance(raw, dict):
        raw = {"profiles": {}}

    # Legacy: single global list
    if "seen_ids" in raw and "profiles" not in raw:
        seen_legacy = raw.get("seen_ids", [])
        if isinstance(seen_legacy, list):
            return {str(x) for x in seen_legacy}

    profiles = raw.get("profiles", {})
    if not isinstance(profiles, dict):
        profiles = {}

    profile = get_current_profile()
    seen = profiles.get(profile, [])
    if not isinstance(seen, list):
        seen = []
    return {str(x) for x in seen}


def mark_updates_seen(update_ids: List[str]) -> None:
    _ensure_data_dir()
    # Load raw file to preserve other profiles
    raw = _read_json(SEEN_FILE, default={"profiles": {}})
    if not isinstance(raw, dict):
        raw = {"profiles": {}}
    # If legacy exists, migrate into current profile on first write
    if "seen_ids" in raw and "profiles" not in raw:
        raw = {"profiles": {get_current_profile(): raw.get("seen_ids", [])}}
    profiles = raw.get("profiles", {})
    if not isinstance(profiles, dict):
        profiles = {}

    profile = get_current_profile()
    current_seen = profiles.get(profile, [])
    if not isinstance(current_seen, list):
        current_seen = []

    seen = {str(x) for x in current_seen}
    seen.update(str(x) for x in update_ids)

    profiles[profile] = sorted(seen)
    payload = {"profiles": profiles, "updated_at": datetime.now().isoformat()}
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def get_unseen_updates(limit: int = 3) -> List[AppUpdate]:
    updates = load_updates()
    seen = load_seen_update_ids()
    unseen = [u for u in updates if u.id not in seen]
    return unseen[: max(0, limit)]


def save_updates(updates: List[AppUpdate]) -> None:
    """Persist updates to data/app_updates.json (sorted newest first)."""
    _ensure_data_dir()

    def _sort_key(u: AppUpdate):
        try:
            return datetime.fromisoformat(u.date)
        except Exception:
            return datetime.min

    updates_sorted = sorted(updates, key=_sort_key, reverse=True)
    payload = {
        "updates": [
            {
                "id": u.id,
                "date": u.date,
                "title": u.title,
                "content": u.content,
                "type": u.type,
            }
            for u in updates_sorted
        ]
    }
    with open(UPDATES_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def upsert_update(update: AppUpdate) -> None:
    """Insert or update by id."""
    updates = load_updates()
    by_id = {u.id: u for u in updates}
    by_id[update.id] = update
    save_updates(list(by_id.values()))


def delete_update(update_id: str) -> None:
    updates = [u for u in load_updates() if u.id != update_id]
    save_updates(updates)

