"""
Recently Used Component
Track and display recently used calculators
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS
from utils.state import add_to_recently_used as add_recent


def add_to_recently_used(calc_id):
    """Add calculator to recently used"""
    add_recent(calc_id)


def render_recently_used(max_items=5):
    """Render recently used section"""
    st.markdown("### 🕐 Sử dụng Gần Đây")
    
    recently_used = st.session_state.get('recently_used', [])
    if recently_used:
        display_items = recently_used[:max_items]
        cols = st.columns(min(max_items, len(display_items)))
        for idx, calc_id in enumerate(display_items):
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx]:
                    is_fav = calc_id in st.session_state.get('favorites', [])
                    
                    # Use calculator card component
                    from .ui.cards import render_calculator_card
                    render_calculator_card(
                        calc_id=calc_id,
                        name=calc_info['name'],
                        category=calc_info.get('category', ''),
                        icon=calc_info.get('icon', '📊'),
                        page=calc_info.get('page', 'Scores'),
                        is_favorite=is_fav,
                        is_recent=True,
                        show_favorite_button=True,
                        show_open_button=True
                    )
    else:
        st.info("💡 Chưa có lịch sử sử dụng. Bắt đầu dùng calculator để xem lịch sử ở đây!")
    
    st.markdown("---")

