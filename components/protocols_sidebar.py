"""
Protocols Sidebar Components
Helper functions for rendering protocol sidebar
"""

import streamlit as st
from typing import Optional, Tuple
from config.protocol_lists import SPECIALTY_LIST, get_protocol_list
from components.protocol_favorites import (
    render_favorites_section,
    is_favorite,
    render_favorite_button
)
from components.protocol_dark_mode import render_theme_toggle


def get_default_protocol_index(protocol_list: list, deep_link: str) -> int:
    """
    Find protocol index in list based on deep link.
    
    Args:
        protocol_list: List of protocol names
        deep_link: Deep link protocol name to match
        
    Returns:
        Index of matching protocol, or 0 if not found
    """
    if not deep_link:
        return 0
    # Try exact match first (most reliable)
    for idx, p in enumerate(protocol_list):
        if deep_link == p:
            return idx
    # Try partial match (more flexible)
    for idx, p in enumerate(protocol_list):
        # Remove emoji and compare text
        p_text = p.split(' ', 1)[-1] if ' ' in p else p
        deep_link_text = deep_link.split(' ', 1)[-1] if ' ' in deep_link else deep_link
        if deep_link_text.lower() in p_text.lower() or p_text.lower() in deep_link_text.lower():
            return idx
    return 0


def render_protocol_selector(
    protocol_list: list, 
    use_deep_link: bool = False, 
    deep_link_protocol: Optional[str] = None
) -> str:
    """
    Render protocol radio selector with deep link support.
    
    Args:
        protocol_list: List of protocol names
        use_deep_link: Whether to use deep link for default selection
        deep_link_protocol: Protocol name from deep link
        
    Returns:
        Selected protocol name
    """
    default_idx = get_default_protocol_index(protocol_list, deep_link_protocol) if use_deep_link else 0
    return st.radio(
        "Phác đồ:",
        protocol_list,
        index=default_idx,
        label_visibility="collapsed"
    )


def render_protocols_sidebar() -> Tuple[str, str, bool]:
    """
    Render the complete protocols sidebar.
    
    Returns:
        Tuple of (specialty, protocol, use_deep_link)
    """
    st.header("📋 Phác đồ điều trị")
    st.caption("Tra cứu nhanh phác đồ và hướng dẫn xử trí lâm sàng.")
    
    # Check for deep link from Articles page
    deep_link_specialty = st.session_state.get('protocol_specialty')
    deep_link_protocol = st.session_state.get('protocol_to_open')
    deep_link_function = st.session_state.get('protocol_function')
    
    # Set default index based on deep link
    default_specialty_index = 0
    if deep_link_specialty:
        try:
            default_specialty_index = SPECIALTY_LIST.index(deep_link_specialty)
        except ValueError:
            pass
    
    specialty = st.selectbox(
        "Chuyên khoa:",
        SPECIALTY_LIST,
        index=default_specialty_index
    )
    
    # Store deep link info temporarily (will be cleared after routing)
    use_deep_link = bool(deep_link_protocol and deep_link_function)
    
    st.markdown("---")
    
    # ========== FAVORITES SECTION ==========
    render_favorites_section()
    
    st.markdown("---")
    
    # Liên kết nhanh về module Hồi sức
    with st.expander("Liên kết nhanh", expanded=False):
        if st.button("🫁 Mở Hồi sức (ICU Tools)", use_container_width=True):
            st.switch_page("pages/09_🫁_Critical_Care.py")
        if st.button("📊 Mở Thang điểm & Công thức", use_container_width=True):
            st.switch_page("pages/01_📊_Scores.py")
    
    st.markdown("---")
    
    # Get protocol list for selected specialty
    protocol_list = get_protocol_list(specialty)
    
    # ========== SEARCH/FILTER PROTOCOL - ENHANCED UI ==========
    # ========== SEARCH/FILTER PROTOCOL - ENHANCED UI ==========
    if protocol_list:
        search_term = st.text_input(
            "🔍 Tìm protocol...",
            key=f"protocol_search_{specialty}",
            placeholder="Nhập tên protocol...",
            help="Tìm kiếm nhanh trong danh sách protocols"
        )
        
        # Filter protocols based on search
        if search_term:
            search_lower = search_term.lower()
            # Remove emoji and search in text
            filtered_list = [
                p for p in protocol_list
                if search_lower in p.lower() or 
                   (search_lower in p.split(' ', 1)[-1].lower() if ' ' in p else False)
            ]
            
            if filtered_list:
                protocol_list = filtered_list
                st.caption(f"✅ Tìm thấy **{len(filtered_list)}** kết quả")
            else:
                st.warning(f"Không có protocol nào khớp với '{search_term}'")
                protocol_list = []  # Show empty list
        else:
            # Simple count
            st.caption(f"📊 **{len(protocol_list)}** protocols trong chuyên khoa này")
    
    if protocol_list:
        # Use helper function for consistency
        protocol = render_protocol_selector(protocol_list, use_deep_link, deep_link_protocol)
        
        # Show favorite button for selected protocol
        if protocol and protocol != "Không có protocol nào":
            st.markdown("---")
            col_fav1, col_fav2 = st.columns([1, 4])
            with col_fav1:
                render_favorite_button(protocol, key_suffix=specialty)
            with col_fav2:
                # Show protocol info
                protocol_display = protocol.split(' ', 1)[-1] if ' ' in protocol else protocol
                st.caption(f"**{protocol_display}**")
    else:
        # Fallback: show empty selector
        protocol = st.radio(
            "Phác đồ:",
            ["Không có protocol nào"],
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    
    # ========== THEME TOGGLE ==========
    render_theme_toggle()
    
    st.markdown("---")
    
    from components.ui import render_info_box
    render_info_box(
        """
        **Nguồn dữ liệu:**
        - Hướng dẫn Bộ Y tế
        - AHA/ACC, ESC, IDSA
        - UpToDate & Medscape
        """,
        title="Thông tin",
        type="info",
        icon="📚"
    )
    
    return specialty, protocol, use_deep_link

