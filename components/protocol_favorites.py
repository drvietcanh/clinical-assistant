"""
Protocol Favorites Component
Manage favorite/bookmarked protocols
"""

import streamlit as st
from typing import List


def get_favorite_protocols() -> List[str]:
    """
    Get list of favorite protocols from session state.
    
    Returns:
        List of favorite protocol names
    """
    return st.session_state.get('favorite_protocols', [])


def add_to_favorites(protocol_name: str):
    """
    Add protocol to favorites.
    
    Args:
        protocol_name: Name of protocol to add
    """
    if 'favorite_protocols' not in st.session_state:
        st.session_state['favorite_protocols'] = []
    
    if protocol_name not in st.session_state['favorite_protocols']:
        st.session_state['favorite_protocols'].append(protocol_name)
        st.session_state['favorite_protocols'] = sorted(st.session_state['favorite_protocols'])


def remove_from_favorites(protocol_name: str):
    """
    Remove protocol from favorites.
    
    Args:
        protocol_name: Name of protocol to remove
    """
    if 'favorite_protocols' in st.session_state:
        if protocol_name in st.session_state['favorite_protocols']:
            st.session_state['favorite_protocols'].remove(protocol_name)


def is_favorite(protocol_name: str) -> bool:
    """
    Check if protocol is in favorites.
    
    Args:
        protocol_name: Name of protocol to check
        
    Returns:
        True if protocol is favorite, False otherwise
    """
    favorites = get_favorite_protocols()
    return protocol_name in favorites


def render_favorite_button(protocol_name: str, key_suffix: str = ""):
    """
    Render favorite toggle button.
    
    Args:
        protocol_name: Name of protocol
        key_suffix: Optional suffix for unique key
        
    Returns:
        True if clicked and toggled, False otherwise
    """
    is_fav = is_favorite(protocol_name)
    button_label = "⭐ Bỏ đánh dấu" if is_fav else "⭐ Đánh dấu"
    button_type = "secondary" if is_fav else "primary"
    
    key = f"fav_button_{protocol_name}_{key_suffix}".replace(" ", "_").replace("/", "_")
    
    if st.button(button_label, key=key, use_container_width=True, type=button_type):
        if is_fav:
            remove_from_favorites(protocol_name)
            st.success(f"✅ Đã bỏ đánh dấu: {protocol_name}")
        else:
            add_to_favorites(protocol_name)
            st.success(f"⭐ Đã đánh dấu: {protocol_name}")
        st.rerun()
        return True
    return False


def render_favorites_section(all_protocols: List[str] = None):
    """
    Render favorites section in sidebar.
    
    Args:
        all_protocols: Optional list of all available protocols for filtering
    """
    favorites = get_favorite_protocols()
    
    if favorites:
        # Filter to only show favorites that exist in current protocol list
        if all_protocols:
            favorites = [f for f in favorites if f in all_protocols]
        
        if favorites:
            st.markdown("### ⭐ Protocols Yêu Thích")
            
            for protocol_name in favorites:
                # Create a compact display with remove button
                col1, col2 = st.columns([4, 1])
                with col1:
                    # Truncate long names for display
                    display_name = protocol_name.split(' ', 1)[-1] if ' ' in protocol_name else protocol_name
                    if len(display_name) > 30:
                        display_name = display_name[:27] + "..."
                    st.markdown(f"📋 {display_name}")
                
                with col2:
                    if st.button("❌", key=f"remove_fav_{protocol_name}".replace(" ", "_"), 
                                help="Bỏ đánh dấu"):
                        remove_from_favorites(protocol_name)
                        st.rerun()
            
            st.markdown("---")
        else:
            # No favorites in current specialty
            st.info("💡 Chưa có protocol yêu thích trong chuyên khoa này.")
    else:
        # No favorites at all
        st.info("💡 Chưa có protocol yêu thích. Nhấn ⭐ để đánh dấu protocol bạn thường dùng!")

