"""
Collaboration helpers: export/import local user state.

This is a pragmatic "share via file" approach:
- Export: download a JSON snapshot of selected session_state keys
- Import: upload JSON to restore/merge state
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st


EXPORT_VERSION = 1

# Keys we consider "shareable" across devices
STATE_KEYS = [
    "favorites",
    "recently_used",
    "search_history",
    "user_preferences",
    "favorite_protocols",
    "drug_saved_searches",
    "saved_searches",
    "recent_searches",
    "drug_comparison_list",
]


def export_state_payload(extra: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "schema": "clinical-assistant.user-state",
        "version": EXPORT_VERSION,
        "exported_at": datetime.now().isoformat(),
        "state": {},
    }
    state: Dict[str, Any] = {}
    for k in STATE_KEYS:
        if k in st.session_state:
            state[k] = st.session_state.get(k)
    payload["state"] = state
    if extra:
        payload["extra"] = extra
    return payload


def _safe_list(value: Any) -> List[Any]:
    return value if isinstance(value, list) else []


def _safe_dict(value: Any) -> Dict[str, Any]:
    return value if isinstance(value, dict) else {}


def import_state_payload(payload: Dict[str, Any], mode: str = "merge") -> Tuple[bool, str]:
    """
    Import user state from payload.

    mode:
    - "replace": overwrite keys
    - "merge": merge lists (unique) and dicts (shallow update)
    """
    if not isinstance(payload, dict):
        return False, "Payload không hợp lệ."
    if payload.get("schema") != "clinical-assistant.user-state":
        return False, "Không đúng định dạng export."
    state = payload.get("state")
    if not isinstance(state, dict):
        return False, "Thiếu trường state."

    for k, v in state.items():
        if k not in STATE_KEYS:
            continue
        if mode == "replace":
            st.session_state[k] = v
            continue

        # merge
        current = st.session_state.get(k)
        if isinstance(current, list) or isinstance(v, list):
            merged = list(dict.fromkeys(_safe_list(current) + _safe_list(v)))
            st.session_state[k] = merged
        elif isinstance(current, dict) or isinstance(v, dict):
            merged = _safe_dict(current)
            merged.update(_safe_dict(v))
            st.session_state[k] = merged
        else:
            # scalar fallback
            st.session_state[k] = v

    return True, "Import thành công."


def payload_to_json_bytes(payload: Dict[str, Any]) -> bytes:
    return json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")

