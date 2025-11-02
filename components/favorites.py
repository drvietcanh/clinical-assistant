"""
Favorites Component
Manage and display favorite calculators
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS


def add_to_favorites(calc_id):
    """Add calculator to favorites"""
    if calc_id not in st.session_state.favorites:
        st.session_state.favorites.append(calc_id)


def remove_from_favorites(calc_id):
    """Remove calculator from favorites"""
    if calc_id in st.session_state.favorites:
        st.session_state.favorites.remove(calc_id)


def render_favorites():
    """Render favorites section"""
    st.markdown("### ⭐ Yêu Thích")
    
    if st.session_state.favorites:
        cols = st.columns(min(4, len(st.session_state.favorites)))
        for idx, calc_id in enumerate(st.session_state.favorites[:8]):  # Show max 8
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx % 4]:
                    with st.container():
                        st.markdown(f"""
                        **{calc_info['icon']} {calc_info['name']}**  
                        {calc_info['category']}
                        """)
                        
                        col_remove, col_open = st.columns([1, 2])
                        with col_remove:
                            if st.button("🗑️", key=f"remove_fav_{calc_id}", help="Xóa khỏi yêu thích"):
                                remove_from_favorites(calc_id)
                                st.rerun()
                        
                        with col_open:
                            if st.button("Mở", key=f"open_fav_{calc_id}", type="primary"):
                                from .recently_used import add_to_recently_used
                                add_to_recently_used(calc_id)
                                st.info(f"Mở {calc_info['name']} từ {calc_info['page']}...")
                        
                        st.markdown("---")
    else:
        st.info("💡 Chưa có calculator yêu thích. Nhấn ⭐ khi tìm kiếm để thêm vào danh sách!")
    
    st.markdown("---")

