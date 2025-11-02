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
                    st.markdown(f"""
                    <div class="favorite-card">
                        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                            <span style="font-size: 1.5rem;">{calc_info['icon']}</span>
                            <strong style="font-size: 0.95rem; color: #212121;">{calc_info['name']}</strong>
                        </div>
                        <div style="font-size: 0.8rem; color: #757575;">
                            {calc_info['category']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col_remove, col_open = st.columns([1, 3])
                    with col_remove:
                        if st.button("🗑️", key=f"remove_fav_{calc_id}", help="Xóa khỏi yêu thích"):
                            remove_from_favorites(calc_id)
                            st.success("Đã xóa khỏi yêu thích")
                            st.rerun()
                    
                    with col_open:
                        if st.button("▶️ Mở", key=f"open_fav_{calc_id}", type="primary", use_container_width=True):
                            from .recently_used import add_to_recently_used
                            add_to_recently_used(calc_id)
                            st.switch_page(calc_info['page'])
        
        if num_favs > 12:
            st.caption(f"... và {num_favs - 12} calculator khác")
    else:
        st.info("""
        **💡 Chưa có calculator yêu thích**
        
        Nhấn **⭐** khi tìm kiếm hoặc xem calculator để thêm vào danh sách yêu thích!
        """)
    
    st.markdown("---")

