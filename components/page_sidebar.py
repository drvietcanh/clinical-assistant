"""
Standard Page Sidebar Component
Unified sidebar structure for all pages
"""

import streamlit as st
from typing import List, Dict, Optional, Callable


def render_standard_sidebar(
    title: str,
    icon: str,
    description: str = None,
    module_group: str = None,
    quick_links: List[Dict] = None,
    filters: Dict = None,
    info_text: str = None,
    custom_content: Callable = None
):
    """
    Render standardized sidebar for pages.
    
    Args:
        title: Sidebar title
        icon: Icon emoji
        description: Description text
        module_group: Module group name (for categorization)
        quick_links: List of {label, page, icon} dicts for quick navigation
        filters: Filter configuration dict
        info_text: Info text to display
        custom_content: Custom function to render additional content
    
    Returns:
        Dict of filter values (if filters provided)
    """
    with st.sidebar:
        # Header
        st.header(f"{icon} {title}")
        if description:
            st.caption(description)
        if module_group:
            st.caption(f"Thuộc nhóm *{module_group}*")
        
        st.markdown("---")
        
        # Quick links
        if quick_links:
            with st.expander("🔗 Liên kết nhanh", expanded=False):
                cols = st.columns(min(len(quick_links), 2))
                for idx, link in enumerate(quick_links):
                    with cols[idx % 2]:
                        label = link.get("label", "")
                        page = link.get("page", "")
                        link_icon = link.get("icon", "")
                        if st.button(
                            f"{link_icon} {label}",
                            key=f"quick_link_{idx}",
                            use_container_width=True
                        ):
                            st.switch_page(page)
        
        # Filters
        filter_values = {}
        if filters:
            st.subheader("🔍 Bộ lọc")
            for filter_name, filter_config in filters.items():
                # Check conditional display
                conditional = filter_config.get("conditional")
                if conditional:
                    # Simple conditional check (e.g., "view_mode == 'Theo chuyên khoa'")
                    # For now, we'll handle it in the calling page
                    continue
                
                filter_type = filter_config.get("type", "selectbox")
                options = filter_config.get("options", [])
                default = filter_config.get("default", options[0] if options else None)
                key = filter_config.get("key", f"filter_{filter_name}")
                
                if filter_type == "selectbox":
                    value = st.selectbox(
                        filter_config.get("label", filter_name),
                        options,
                        index=options.index(default) if default in options else 0,
                        key=key
                    )
                elif filter_type == "multiselect":
                    value = st.multiselect(
                        filter_config.get("label", filter_name),
                        options,
                        default=filter_config.get("default", []),
                        key=key
                    )
                elif filter_type == "radio":
                    value = st.radio(
                        filter_config.get("label", filter_name),
                        options,
                        index=options.index(default) if default in options else 0,
                        key=key
                    )
                else:
                    value = default
                
                filter_values[filter_name] = value
            
            # Handle conditional filters after main filters
            for filter_name, filter_config in filters.items():
                conditional = filter_config.get("conditional")
                if conditional and "view_mode" in conditional:
                    # Check if condition is met
                    view_mode_value = filter_values.get("view_mode", "")
                    if "Theo chuyên khoa" in conditional and view_mode_value == "Theo chuyên khoa":
                        filter_type = filter_config.get("type", "selectbox")
                        options = filter_config.get("options", [])
                        default = filter_config.get("default", options[0] if options else None)
                        key = filter_config.get("key", f"filter_{filter_name}")
                        
                        value = st.selectbox(
                            filter_config.get("label", filter_name),
                            options,
                            index=options.index(default) if default in options else 0,
                            key=key
                        )
                        filter_values[filter_name] = value
            
            st.markdown("---")
        
        # Custom content
        if custom_content:
            custom_content()
            st.markdown("---")
        
        # Info text
        if info_text:
            st.info(info_text)
    
    return filter_values

