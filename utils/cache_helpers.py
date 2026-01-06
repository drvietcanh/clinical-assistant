"""
Cache helper functions for common patterns used across the app.
"""

from typing import Dict, Iterable, List, Tuple, Optional

import streamlit as st


@st.cache_data(ttl=600)
def get_popular_calculators(default_ids: Tuple[str, ...]) -> List[str]:
    """
    Get list of popular calculators.

    For now, this simply returns the provided default IDs but is cached so
    we can later plug in analytics-based ranking without touching callers.
    """
    return list(default_ids)


@st.cache_data(ttl=60)
def compute_usage_stats_snapshot(
    total_calculations: int,
    most_used_id: Optional[str],
    category_counts: Tuple[Tuple[str, int], ...],
) -> Dict[str, object]:
    """
    Compute a stable snapshot of usage stats for display on dashboards.

    Accepts only hashable inputs so it can be safely cached.
    """
    top_category = "Chưa có"
    if category_counts:
        top_category = max(category_counts, key=lambda x: x[1])[0]

    return {
        "total_calculations": total_calculations,
        "most_used_id": most_used_id,
        "top_category": top_category,
    }


@st.cache_data(ttl=3600)
def get_module_list_for_navigation_cached():
    """
    Cached wrapper around get_module_list_for_navigation.

    This avoids recomputing the module list on every app rerun.
    """
    from config.app_config import get_module_list_for_navigation

    return get_module_list_for_navigation()

