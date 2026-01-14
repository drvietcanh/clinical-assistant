"""
Update notification system (lightweight, in-app)

Design goals:
- No database required
- Works with Streamlit session_state
- Safe defaults (no spam)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Set

import streamlit as st


@dataclass(frozen=True)
class UpdateItem:
    """A single update note shown to the user."""

    id: str  # stable unique id, e.g. "2026-01-14-phase1-antibiogram"
    date: str  # ISO-ish string: YYYY-MM-DD
    title: str
    details_md: str
    severity: str = "info"  # "info" | "minor" | "major"
    area: Optional[str] = None  # e.g. "Antibiogram", "Dosing", "IV Compatibility"


def get_antibiotics_updates() -> List[UpdateItem]:
    """
    Registry of Antibiotics module updates.
    Keep this curated and short. Add new entries at the top.
    """
    return [
        UpdateItem(
            id="2026-01-14-phase1-antibiogram-rrt-ecmo",
            date="2026-01-14",
            title="Phase 1: Antibiogram + CRRT/ECMO dosing notes",
            area="Phase 1",
            severity="major",
            details_md=(
                "- 🧫 **Antibiogram**: xem kháng thuốc theo bệnh viện (demo) và upload dữ liệu.\n"
                "- 🫁 **CRRT/ECMO**: thêm ghi chú điều chỉnh liều theo RRT/ECMO trong dosing.\n"
                "- 💊 **Database**: bổ sung thuốc ICU/XDR (ví dụ Cefiderocol).\n"
            ),
        ),
        UpdateItem(
            id="2026-01-10-visual-compare-export-evidence",
            date="2026-01-10",
            title="So sánh trực quan + Export + Evidence badges",
            area="Comparison/Export",
            severity="major",
            details_md=(
                "- 📊 **So sánh trực quan**: spectrum/dosing/cost/side effects.\n"
                "- 📤 **Export**: PDF/Excel/Copy cho kết quả tính liều và bảng so sánh.\n"
                "- 🏷️ **Evidence level**: badge A/B/C/D trên regimen.\n"
            ),
        ),
    ]


def _get_seen_set(key: str) -> Set[str]:
    seen = st.session_state.get(key)
    if not isinstance(seen, set):
        seen = set(seen) if isinstance(seen, (list, tuple)) else set()
        st.session_state[key] = seen
    return seen


def get_unread_updates_count(scope_key: str = "antibiotics_updates_seen") -> int:
    updates = get_antibiotics_updates()
    seen = _get_seen_set(scope_key)
    return sum(1 for u in updates if u.id not in seen)


def mark_all_updates_as_seen(scope_key: str = "antibiotics_updates_seen") -> None:
    updates = get_antibiotics_updates()
    seen = _get_seen_set(scope_key)
    for u in updates:
        seen.add(u.id)
    st.session_state[scope_key] = seen


def render_whats_new(scope_key: str = "antibiotics_updates_seen") -> None:
    """
    Render an in-app "What's new" panel.
    """
    updates = get_antibiotics_updates()
    seen = _get_seen_set(scope_key)
    unread = [u for u in updates if u.id not in seen]

    st.markdown("### 🆕 Có gì mới")
    if not updates:
        st.caption("Chưa có cập nhật nào.")
        return

    if unread:
        st.info(f"Bạn có **{len(unread)}** cập nhật chưa đọc.")
    else:
        st.success("Bạn đã đọc tất cả cập nhật.")

    col1, col2 = st.columns([2, 1])
    with col1:
        if st.button("✅ Đánh dấu đã đọc tất cả", key="antibiotics_mark_all_updates_seen", use_container_width=True):
            mark_all_updates_as_seen(scope_key=scope_key)
            st.rerun()
    with col2:
        show_all = st.toggle("Hiện tất cả", value=True, key="antibiotics_show_all_updates")

    items = updates if show_all else unread
    for u in items:
        is_unread = u.id not in seen
        status_prefix = "🟦" if u.severity == "info" else ("🟨" if u.severity == "minor" else "🟥")
        unread_prefix = "**(NEW)** " if is_unread else ""
        header = f"{status_prefix} {unread_prefix}{u.title}"
        with st.expander(header, expanded=is_unread):
            meta = f"**Ngày:** {u.date}"
            if u.area:
                meta += f"  \n**Khu vực:** {u.area}"
            st.markdown(meta)
            st.markdown(u.details_md)
            if is_unread:
                if st.button("Đánh dấu đã đọc", key=f"antibiotics_mark_seen_{u.id}", use_container_width=True):
                    seen.add(u.id)
                    st.session_state[scope_key] = seen
                    st.rerun()

