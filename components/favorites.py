"""
Favorites Component
Manage and display favorite calculators
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS
from utils.state import add_to_favorites as add_fav, remove_from_favorites as remove_fav


def add_to_favorites(calc_id):
    """Add calculator to favorites"""
    add_fav(calc_id)


def remove_from_favorites(calc_id):
    """Remove calculator from favorites"""
    remove_fav(calc_id)


def render_favorites():
    """Render enhanced favorites section"""
    st.markdown("### ⭐ Yêu Thích")
    
    if st.session_state.favorites:
        num_favs = len(st.session_state.favorites)
        st.caption(f"Bạn có **{num_favs}** calculator yêu thích")
        
        num_cols = min(4, num_favs)
        cols = st.columns(num_cols)
        
        for idx, calc_id in enumerate(st.session_state.favorites[:12]):  # Show max 12
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx % num_cols]:
                    # Use calculator card component for consistency
                    from .ui.cards import render_calculator_card
                    render_calculator_card(
                        calc_id=calc_id,
                        name=calc_info['name'],
                        category=calc_info.get('category', ''),
                        icon=calc_info.get('icon', '📊'),
                        page=calc_info.get('page', 'Scores'),
                        is_favorite=True,
                        is_recent=False,
                        show_favorite_button=True,
                        show_open_button=True
                    )
        
        if num_favs > 12:
            st.info(f"💡 Có thêm **{num_favs - 12}** calculator khác trong danh sách yêu thích")
    else:
        st.info("""
        **💡 Chưa có calculator yêu thích**
        
        Nhấn **⭐** khi tìm kiếm hoặc xem calculator để thêm vào danh sách yêu thích!
        
        Favorites giúp bạn truy cập nhanh các calculator thường dùng nhất.
        """)
    
    st.markdown("---")

