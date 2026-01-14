"""
App Updates / Changelog
"""

import streamlit as st

from utils.page_helper import setup_page, render_standard_footer
from utils.analytics_events import track_page_view, track_feature_usage

from components.app_updates import load_updates, get_unseen_updates, mark_updates_seen


setup_page(
    page_title="Updates / Changelog",
    page_icon="🆕",
    description="Cập nhật tính năng, sửa lỗi và thay đổi quan trọng trong ứng dụng",
    mobile_header=True,
)

track_page_view("Updates / Changelog")
track_feature_usage("updates_page_open")

st.title("🆕 Updates / Changelog")
st.caption("Danh sách cập nhật nội bộ của ứng dụng (khác với Tin tức y khoa).")

unseen = get_unseen_updates(limit=20)
if unseen:
    st.success(f"✨ Bạn có {len(unseen)} cập nhật chưa xem")
    if st.button("Đánh dấu tất cả là đã xem", type="primary", use_container_width=True):
        mark_updates_seen([u.id for u in unseen])
        track_feature_usage("updates_mark_all_seen")
        st.rerun()
else:
    st.info("Bạn đã xem hết các cập nhật gần đây.")

st.markdown("---")

updates = load_updates()
if not updates:
    st.warning("Chưa có dữ liệu cập nhật. (data/app_updates.json)")
else:
    # Filters
    type_filter = st.multiselect(
        "Lọc theo loại:",
        options=["feature", "update", "improvement", "bugfix", "announcement"],
        default=["feature", "update", "improvement", "bugfix", "announcement"],
    )
    search = st.text_input("🔍 Tìm trong cập nhật", placeholder="Nhập từ khóa...")

    filtered = [
        u for u in updates
        if (u.type in type_filter)
        and (search.lower() in (u.title + " " + u.content).lower() if search else True)
    ]

    for u in filtered:
        with st.expander(f"{u.title} • {u.date}", expanded=False):
            st.markdown(u.content)
            st.caption(f"Type: `{u.type}` • ID: `{u.id}`")

render_standard_footer()

