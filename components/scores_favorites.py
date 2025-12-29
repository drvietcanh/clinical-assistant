"""
Scores Favorites Component
Manage and display favorite scores/calculators
"""

import streamlit as st
from typing import List, Tuple, Optional


def get_favorite_scores() -> List[Tuple[str, str]]:
    """
    Get list of favorite scores from session state.
    Returns list of (specialty, score_id) tuples.
    """
    if 'favorite_scores' not in st.session_state:
        st.session_state['favorite_scores'] = []
    return st.session_state['favorite_scores']


def add_to_favorites(specialty: str, score_id: str):
    """Add score to favorites"""
    if 'favorite_scores' not in st.session_state:
        st.session_state['favorite_scores'] = []
    
    fav_key = (specialty, score_id)
    if fav_key not in st.session_state['favorite_scores']:
        st.session_state['favorite_scores'].append(fav_key)


def remove_from_favorites(specialty: str, score_id: str):
    """Remove score from favorites"""
    if 'favorite_scores' in st.session_state:
        fav_key = (specialty, score_id)
        if fav_key in st.session_state['favorite_scores']:
            st.session_state['favorite_scores'].remove(fav_key)


def is_favorite(specialty: str, score_id: str) -> bool:
    """Check if score is in favorites"""
    favorites = get_favorite_scores()
    return (specialty, score_id) in favorites


def render_favorite_button(specialty: str, score_id: str, score_name: str, key_suffix: str = ""):
    """
    Render favorite toggle button.
    
    Returns:
        True if clicked and toggled, False otherwise
    """
    is_fav = is_favorite(specialty, score_id)
    button_label = "⭐ Bỏ đánh dấu" if is_fav else "⭐ Đánh dấu"
    button_type = "secondary" if is_fav else "primary"
    
    key = f"fav_btn_{specialty}_{score_id}_{key_suffix}".replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
    
    if st.button(button_label, key=key, use_container_width=True, type=button_type):
        if is_fav:
            remove_from_favorites(specialty, score_id)
            st.success(f"✅ Đã bỏ đánh dấu: {score_name}")
        else:
            add_to_favorites(specialty, score_id)
            st.success(f"⭐ Đã đánh dấu: {score_name}")
        st.rerun()
        return True
    return False


def render_favorites_section_in_sidebar(SCORES_BY_SPECIALTY: dict):
    """
    Render favorites section in sidebar.
    Shows favorite scores with quick access.
    """
    favorites = get_favorite_scores()
    
    if favorites:
        st.markdown("### ⭐ Calculators Yêu Thích")
        
        # Filter to only show favorites that still exist
        valid_favorites = []
        for specialty, score_id in favorites:
            if specialty in SCORES_BY_SPECIALTY and score_id in SCORES_BY_SPECIALTY[specialty]:
                valid_favorites.append((specialty, score_id))
        
        if valid_favorites:
            for specialty, score_id in valid_favorites[:10]:  # Show max 10
                score_info = SCORES_BY_SPECIALTY[specialty][score_id]
                score_name = score_info['name']
                
                # Truncate long names
                display_name = score_name
                if len(display_name) > 35:
                    display_name = display_name[:32] + "..."
                
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"**{display_name}**")
                    st.caption(f"{specialty.split('(')[0].strip()}")
                
                with col2:
                    if st.button("❌", key=f"remove_fav_{specialty}_{score_id}".replace(" ", "_").replace("/", "_").replace("(", "").replace(")", ""), 
                                help="Bỏ đánh dấu"):
                        remove_from_favorites(specialty, score_id)
                        st.rerun()
            
            if len(valid_favorites) > 10:
                st.caption(f"... và {len(valid_favorites) - 10} calculator khác")
            
            st.markdown("---")
        else:
            st.info("💡 Chưa có calculator yêu thích hợp lệ.")
    else:
        st.info("💡 Chưa có calculator yêu thích. Nhấn ⭐ để đánh dấu!")


def render_favorites_page(SCORES_BY_SPECIALTY: dict):
    """
    Render full favorites page.
    Shows all favorite scores organized by specialty.
    """
    favorites = get_favorite_scores()
    
    st.header("⭐ Calculators Yêu Thích")
    
    if not favorites:
        st.info("""
        **💡 Chưa có calculator yêu thích**
        
        Nhấn **⭐ Đánh dấu** khi xem calculator để thêm vào danh sách yêu thích!
        
        Favorites giúp bạn truy cập nhanh các calculator thường dùng nhất.
        """)
        return
    
    # Filter to only show favorites that still exist
    valid_favorites = {}
    for specialty, score_id in favorites:
        if specialty in SCORES_BY_SPECIALTY and score_id in SCORES_BY_SPECIALTY[specialty]:
            if specialty not in valid_favorites:
                valid_favorites[specialty] = []
            valid_favorites[specialty].append(score_id)
    
    if not valid_favorites:
        st.warning("Không có calculator yêu thích hợp lệ.")
        return
    
    st.success(f"Bạn có **{sum(len(scores) for scores in valid_favorites.values())}** calculator yêu thích")
    st.markdown("---")
    
    # Group by specialty
    for specialty, score_ids in valid_favorites.items():
        st.subheader(f"{specialty}")
        
        for score_id in score_ids:
            score_info = SCORES_BY_SPECIALTY[specialty][score_id]
            
            col1, col2, col3 = st.columns([6, 2, 1])
            with col1:
                st.markdown(f"**{score_info['name']}**")
                st.caption(score_info.get('desc', ''))
            
            with col2:
                if st.button("📊 Mở", key=f"open_{specialty}_{score_id}".replace(" ", "_"), use_container_width=True):
                    # Set session state to navigate
                    st.session_state['navigate_to_specialty'] = specialty
                    st.session_state['navigate_to_score'] = score_id
                    st.rerun()
            
            with col3:
                if st.button("❌", key=f"remove_{specialty}_{score_id}".replace(" ", "_"), 
                            help="Bỏ đánh dấu"):
                    remove_from_favorites(specialty, score_id)
                    st.rerun()
        
        st.markdown("---")

