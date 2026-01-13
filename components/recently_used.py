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


def render_recently_used(max_items=5, show_empty_state=True):
    """Render enhanced recently used section with visual cards"""
    st.markdown("### 🕐 Sử dụng Gần Đây")
    
    recently_used = st.session_state.get('recently_used', [])
    if recently_used:
        display_items = recently_used[:max_items]
        num_cols = min(max_items, len(display_items))
        if num_cols == 0:
            num_cols = 1
        cols = st.columns(num_cols)
        
        for idx, calc_id in enumerate(display_items):
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx]:
                    is_fav = calc_id in st.session_state.get('favorites', [])
                    star_icon = "⭐" if is_fav else "☆"
                    
                    # Enhanced card design
                    st.markdown(
                        f"""
                        <div class="calculator-card" style="text-align: center; padding: 20px; margin-bottom: 12px;">
                            <div style="font-size: 3rem; margin-bottom: 8px;">{calc_info.get('icon', '📊')}</div>
                            <div style="font-weight: 600; font-size: 1rem; margin-bottom: 4px; color: var(--text-primary);">
                                {calc_info['name']}
                            </div>
                            <div style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 12px;">
                                {calc_info.get('category', '')}
                            </div>
                            <div style="font-size: 1.2rem; opacity: 0.6;">{star_icon}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # Action buttons
                    btn_col1, btn_col2 = st.columns(2)
                    with btn_col1:
                        page_path_map = {
                            'Scores': 'pages/01_📊_Scores.py',
                            'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                            'Drugs': 'pages/07_💊_Drug_Database.py',
                            'Protocols': 'pages/04_📋_Protocols.py',
                        }
                        page_path = page_path_map.get(calc_info.get('page', 'Scores'), 'pages/01_📊_Scores.py')
                        if st.button("Mở", key=f"recent_open_{calc_id}", use_container_width=True, type="primary"):
                            st.session_state['preset_calculator'] = calc_id
                            st.session_state['switch_to_scores'] = True
                            st.rerun()
                    with btn_col2:
                        from utils.state import add_to_favorites, remove_from_favorites
                        if st.button(star_icon, key=f"recent_fav_{calc_id}", use_container_width=True, help="Thêm/bỏ yêu thích"):
                            if is_fav:
                                remove_from_favorites(calc_id)
                            else:
                                add_to_favorites(calc_id)
                            st.rerun()
    else:
        if show_empty_state:
            st.markdown(
                """
                <div class="empty-state">
                    <div class="empty-state-icon">🕐</div>
                    <div class="empty-state-message">Chưa có lịch sử sử dụng</div>
                    <div class="empty-state-hint">
                        Bắt đầu dùng calculator để xem lịch sử ở đây!
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    st.markdown("---")

