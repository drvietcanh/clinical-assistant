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


def render_favorites(max_items=None, show_empty_state=True):
    """Render enhanced favorites section with visual cards"""
    st.markdown("### ⭐ Yêu Thích")
    
    favorites = st.session_state.get('favorites', [])
    
    if favorites:
        num_favs = len(favorites)
        st.caption(f"Bạn có **{num_favs}** calculator yêu thích")
        
        # Determine display items
        if max_items:
            display_items = favorites[:max_items]
        else:
            display_items = favorites[:12]
        
        # Responsive grid
        num_cols = min(4, len(display_items))
        if num_cols == 0:
            num_cols = 1
        cols = st.columns(num_cols)
        
        for idx, calc_id in enumerate(display_items):
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx % num_cols]:
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
                            <div style="font-size: 1.5rem;">⭐</div>
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
                        if st.button("Mở", key=f"fav_open_{calc_id}", use_container_width=True, type="primary"):
                            st.session_state['preset_calculator'] = calc_id
                            st.session_state['switch_to_scores'] = True
                            st.rerun()
                    with btn_col2:
                        if st.button("⭐", key=f"fav_remove_{calc_id}", use_container_width=True, help="Bỏ yêu thích"):
                            remove_from_favorites(calc_id)
                            st.rerun()
        
        if num_favs > (max_items or 12):
            st.info(f"💡 Có thêm **{num_favs - (max_items or 12)}** calculator khác trong danh sách yêu thích")
    else:
        if show_empty_state:
            st.markdown(
                """
                <div class="empty-state">
                    <div class="empty-state-icon">⭐</div>
                    <div class="empty-state-message">Chưa có calculator yêu thích</div>
                    <div class="empty-state-hint">
                        Nhấn <strong>⭐</strong> khi tìm kiếm hoặc xem calculator để thêm vào danh sách yêu thích!
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
    
    st.markdown("---")

