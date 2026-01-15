"""
Shared analytics helpers.
Used by Analytics page and other modules to record usage events.
"""

from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


ANALYTICS_FILE = Path("analytics_data.json")


def load_analytics() -> Dict[str, Any]:
    """Load analytics data from JSON file."""
    try:
        if ANALYTICS_FILE.exists():
            with open(ANALYTICS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except (OSError, IOError, json.JSONDecodeError):
        # Return default structure if file cannot be read
        pass
    return {
        "page_views": {},
        "feature_usage": {},
        "search_queries": [],
        "user_sessions": [],
        "errors": [],
    }


def save_analytics(data: Dict[str, Any]) -> None:
    """Persist analytics data to JSON file."""
    try:
        with open(ANALYTICS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except (OSError, IOError):
        # Silently fail if file cannot be written (e.g., read-only filesystem)
        pass


def track_page_view(page_name: str) -> None:
    """Increment view counter for a page."""
    try:
        analytics = load_analytics()
        analytics.setdefault("page_views", {})
        analytics["page_views"][page_name] = analytics["page_views"].get(page_name, 0) + 1
        save_analytics(analytics)
    except Exception:
        # Silently fail if tracking cannot be saved
        pass


def track_feature_usage(feature_name: str) -> None:
    """Increment usage counter for a feature."""
    try:
        analytics = load_analytics()
        analytics.setdefault("feature_usage", {})
        analytics["feature_usage"][feature_name] = analytics["feature_usage"].get(
            feature_name, 0
        ) + 1
        save_analytics(analytics)
    except Exception:
        # Silently fail if tracking cannot be saved
        pass


def track_search(query: str) -> None:
    """Append a search query event."""
    try:
        analytics = load_analytics()
        analytics.setdefault("search_queries", [])
        analytics["search_queries"].append(
            {"query": query, "timestamp": datetime.now().isoformat()}
        )
        # Keep only last 1000 searches
        analytics["search_queries"] = analytics["search_queries"][-1000:]
        save_analytics(analytics)
    except Exception:
        # Silently fail if tracking cannot be saved
        pass


__all__ = ["load_analytics", "save_analytics", "track_page_view", "track_feature_usage", "track_search"]

