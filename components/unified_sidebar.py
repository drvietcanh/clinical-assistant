"""
Unified Sidebar Component
Standard sidebar for all pages
"""

import streamlit as st
from typing import List, Dict, Optional, Callable
from config.navigation_config import NAVIGATION_CATEGORIES


def render_standard_page_sidebar(
    title: str,
    icon: str,
    description: str,
    module_group: str,
    quick_links: Optional[List[Dict]] = None,
    filters: Optional[Dict] = None,
    info_text: Optional[str] = None,
    show_category_links: bool = True
) -> None:
    """
    Standard sidebar for all pages
    
    Args:
        title: Page title
        icon: Page icon
        description: Page description
        module_group: Module group/category
        quick_links: List of quick link dicts with 'label', 'page', 'icon'
        filters: Filter configuration dict
        info_text: Additional info text
        show_category_links: Show links to other modules in same category
    """
    with st.sidebar:
        # Header
        st.markdown(f"### {icon} {title}")
        if description:
            st.caption(description)
        
        st.markdown("---")
        
        # Category links
        if show_category_links:
            # Find category for this module
            current_category = None
            for cat_id, cat_data in NAVIGATION_CATEGORIES.items():
                # Support both old dict format and new NavigationCategory dataclass
                module_ids = cat_data.module_ids if hasattr(cat_data, 'module_ids') else cat_data.get("modules", [])
                if module_group in module_ids:
                    current_category = cat_id
                    break
            
            if current_category:
                cat_info = NAVIGATION_CATEGORIES[current_category]
                cat_title = cat_info.title if hasattr(cat_info, 'title') else str(current_category)
                st.markdown(f"**📁 Nhóm:** {cat_title}")
                with st.expander("🔗 Liên kết trong nhóm", expanded=False):
                    cat_data = NAVIGATION_CATEGORIES[current_category]
                    # Support both old dict format and new NavigationCategory dataclass
                    module_ids = cat_data.module_ids if hasattr(cat_data, 'module_ids') else cat_data.get("modules", [])
                    for module_id in module_ids:
                        if module_id != module_group:
                            # Get module info
                            try:
                                from config.app_config import get_module_info
                                from config.navigation_config import NAVIGATION_SUB_ITEMS
                                # Skip sub-items in category links (they're accessible from parent page)
                                if module_id not in NAVIGATION_SUB_ITEMS:
                                    module_info = get_module_info(module_id)
                                    if module_info:
                                        if st.button(
                                            f"{module_info.icon} {module_info.title}",
                                            key=f"sidebar_link_{module_id}",
                                            use_container_width=True
                                        ):
                                            st.switch_page(module_info.page_path)
                            except ImportError:
                                pass
                st.markdown("---")
        
        # Quick links
        if quick_links:
            st.markdown("**⚡ Truy cập nhanh**")
            for link in quick_links:
                label = link.get('label', '')
                page = link.get('page', '')
                icon = link.get('icon', '🔗')
                
                if st.button(
                    f"{icon} {label}",
                    key=f"quick_link_{label}",
                    use_container_width=True
                ):
                    st.switch_page(page)
            st.markdown("---")
        
        # Filters
        if filters:
            st.markdown("**🔍 Lọc**")
            for filter_name, filter_config in filters.items():
                filter_type = filter_config.get('type', 'selectbox')
                
                if filter_type == 'selectbox':
                    st.selectbox(
                        filter_config.get('label', filter_name),
                        options=filter_config.get('options', []),
                        key=f"filter_{filter_name}"
                    )
                elif filter_type == 'multiselect':
                    st.multiselect(
                        filter_config.get('label', filter_name),
                        options=filter_config.get('options', []),
                        key=f"filter_{filter_name}"
                    )
                elif filter_type == 'slider':
                    st.slider(
                        filter_config.get('label', filter_name),
                        min_value=filter_config.get('min', 0),
                        max_value=filter_config.get('max', 100),
                        value=filter_config.get('default', 50),
                        key=f"filter_{filter_name}"
                    )
            st.markdown("---")
        
        # Info text
        if info_text:
            st.info(info_text)


def render_module_sidebar(
    module_id: str,
    quick_links: Optional[List[Dict]] = None,
    filters: Optional[Dict] = None,
    info_text: Optional[str] = None
) -> None:
    """
    Render sidebar for a module using module config
    
    Args:
        module_id: Module ID
        quick_links: Quick links
        filters: Filters
        info_text: Info text
    """
    try:
        from config.app_config import get_module_info
        module_info = get_module_info(module_id)
        
        if module_info:
            render_standard_page_sidebar(
                title=module_info.title,
                icon=module_info.icon,
                description=module_info.description,
                module_group=module_id,
                quick_links=quick_links,
                filters=filters,
                info_text=info_text
            )
    except ImportError:
        # Fallback
        st.sidebar.markdown(f"### {module_id}")


__all__ = [
    'render_standard_page_sidebar',
    'render_module_sidebar',
]

