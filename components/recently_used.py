"""
Recently Used Component
Track and display recently used calculators
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS


def add_to_recently_used(calc_id):
    """Add calculator to recently used (max 10)"""
    if calc_id in st.session_state.recently_used:
        st.session_state.recently_used.remove(calc_id)
    st.session_state.recently_used.insert(0, calc_id)
    st.session_state.recently_used = st.session_state.recently_used[:10]  # Keep only last 10


def render_recently_used():
    """Render recently used section"""
    st.markdown("### 🕐 Sử Dụng Gần Đây")
    
    if st.session_state.recently_used:
        cols = st.columns(min(5, len(st.session_state.recently_used)))
        for idx, calc_id in enumerate(st.session_state.recently_used[:5]):  # Show max 5
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx]:
                    is_fav = calc_id in st.session_state.favorites
                    fav_icon = "⭐" if is_fav else "☆"
                    
                    st.markdown(f"""
                    **{calc_info['icon']} {calc_info['name']}**  
                    {calc_info['category']}
                    """)
                    
                    col_fav, col_open = st.columns([1, 2])
                    with col_fav:
                        if st.button(fav_icon, key=f"fav_recent_{calc_id}"):
                            if is_fav:
                                from .favorites import remove_from_favorites
                                remove_from_favorites(calc_id)
                            else:
                                from .favorites import add_to_favorites
                                add_to_favorites(calc_id)
                            st.rerun()
                    
                    with col_open:
                        if st.button("Mở", key=f"open_recent_{calc_id}", type="secondary"):
                            st.info(f"Mở {calc_info['name']}...")
    else:
        st.info("💡 Chưa có lịch sử sử dụng. Bắt đầu dùng calculator để xem lịch sử ở đây!")
    
    st.markdown("---")

