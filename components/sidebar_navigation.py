"""
Sidebar Navigation Component
Collapsible navigation menu with grouped items and sub-items
Mobile-optimized with touch-friendly controls
"""

import streamlit as st
from typing import Dict, List, Optional
from config.navigation_config import (
    get_all_categories,
    get_navigation_items_for_category,
    NAVIGATION_CATEGORIES,
    NAVIGATION_SUB_ITEMS
)
from config.app_config import get_module_info

# Mobile-optimized CSS
MOBILE_NAV_CSS = """
<style>
/* Mobile-optimized navigation */
@media (max-width: 768px) {
    /* Larger touch targets */
    .stButton > button {
        min-height: 48px;
        padding: 12px 16px;
        font-size: 1rem;
    }
    
    /* Larger expander headers */
    .streamlit-expanderHeader {
        min-height: 48px;
        padding: 12px 16px;
        font-size: 1rem;
    }
    
    /* Better spacing for sub-items */
    .sub-item-button {
        padding-left: 32px !important;
    }
    
    /* Hamburger menu indicator */
    .nav-hamburger {
        display: block;
        position: fixed;
        top: 10px;
        left: 10px;
        z-index: 1000;
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 8px;
        padding: 8px;
        cursor: pointer;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
}

/* Desktop: Normal size */
@media (min-width: 769px) {
    .nav-hamburger {
        display: none;
    }
}

/* Smooth transitions */
.streamlit-expanderHeader,
.stButton > button {
    transition: all 0.2s ease;
}

/* Active state highlighting */
.nav-item-active {
    background-color: #e3f2fd !important;
    border-left: 4px solid #1976d2 !important;
    font-weight: 600;
}
</style>
"""


def get_current_page_id() -> Optional[str]:
    """Get current page ID from Streamlit query params or page name"""
    try:
        # Try to get from query params first
        query_params = st.query_params
        if 'page' in query_params:
            return query_params['page']
    except:
        pass
    
    # Fallback: try to infer from page name
    try:
        import os
        page_name = os.path.basename(st.runtime.get_instance()._session_state.get('_pages', {}).get('current_page', ''))
        if page_name:
            # Extract module ID from page name
            # e.g., "01_📊_Scores.py" -> "scores"
            page_name = page_name.replace('.py', '').split('_')[-1].lower()
            return page_name
    except:
        pass
    
    return None


def is_page_active(page_path: str) -> bool:
    """Check if a page is currently active"""
    try:
        # Get current page from Streamlit
        current_page = st.runtime.get_instance()._session_state.get('_pages', {}).get('current_page', '')
        if current_page:
            return page_path in current_page or current_page in page_path
    except:
        pass
    
    # Fallback: check query params
    try:
        query_params = st.query_params
        if 'page' in query_params:
            return page_path in query_params['page'] or query_params['page'] in page_path
    except:
        pass
    
    return False


def render_navigation_item(item, is_sub_item: bool = False, parent_id: Optional[str] = None):
    """Render a single navigation item"""
    active = is_page_active(item.page_path)
    
    # Style for active item
    active_style = "background-color: #e3f2fd; border-left: 4px solid #1976d2; padding-left: 8px;" if active else ""
    sub_item_style = "padding-left: 24px; font-size: 0.9em; color: #666;" if is_sub_item else ""
    
    # Combine styles
    item_style = f"{active_style} {sub_item_style}"
    
    # Defensive check: ensure icon and title are strings
    item_icon = str(item.icon) if item.icon is not None else "📄"
    item_title = str(item.title) if item.title is not None else item.id
    
    # Button or link
    button_text = f"{item_icon} {item_title}"
    
    if st.button(
        button_text,
        key=f"nav_{item.id}",
        use_container_width=True,
        type="primary" if active else "secondary"
    ):
        st.switch_page(item.page_path)


def render_sidebar_navigation():
    """Render the main sidebar navigation with collapsible groups"""
    
    # Get all categories
    categories = get_all_categories()
    
    # Get current page to determine which category should be expanded
    current_page_id = get_current_page_id()
    active_category_id = None
    
    # Find which category contains the current page
    if current_page_id:
        for cat_id, category in categories.items():
            if current_page_id in category.module_ids:
                active_category_id = cat_id
                break
    
    # Render each category as collapsible group
    for cat_id, category in categories.items():
        # Determine if this category should be expanded
        # Default: first 3 categories expanded, or if it contains active page
        should_expand = (
            category.default_expanded or 
            (active_category_id == cat_id) or
            (cat_id in ["home_search", "drugs_dosing", "calculators_scores"])
        )
        
        # Get navigation items for this category
        nav_items = get_navigation_items_for_category(cat_id)
        
        if not nav_items:
            # Fallback: use module_ids directly
            nav_items = []
            for module_id in category.module_ids:
                module_info = get_module_info(module_id)
                if module_info:
                    from config.navigation_config import NavigationItem
                    nav_items.append(NavigationItem(
                        id=module_id,
                        title=module_info.title,
                        icon=module_info.icon,
                        page_path=module_info.page_path,
                        is_sub_item=False
                    ))
        
        # Group items by parent
        main_items = []
        sub_items_map = {}
        
        for item in nav_items:
            if item.is_sub_item and item.parent_id:
                if item.parent_id not in sub_items_map:
                    sub_items_map[item.parent_id] = []
                sub_items_map[item.parent_id].append(item)
            else:
                main_items.append(item)
        
        # Defensive check: ensure icon and title are strings
        icon = str(category.icon) if category.icon is not None else "📁"
        title = str(category.title) if category.title is not None else "Category"
        
        # Safely format the expander label
        expander_label = f"{icon} **{title}**"
        
        # Render category with expander
        with st.expander(
            expander_label,
            expanded=should_expand,
            key=f"nav_cat_{cat_id}"
        ):
            # Render main items
            for item in main_items:
                render_navigation_item(item, is_sub_item=False)
                
                # Render sub-items if any
                if item.id in sub_items_map:
                    for sub_item in sub_items_map[item.id]:
                        render_navigation_item(sub_item, is_sub_item=True, parent_id=item.id)


def render_sidebar_navigation_simple():
    """
    Simplified version for compatibility
    Uses module_ids directly without sub-item structure
    Mobile-optimized with touch-friendly controls
    """
    # Inject mobile CSS
    st.markdown(MOBILE_NAV_CSS, unsafe_allow_html=True)
    
    categories = get_all_categories()
    
    for cat_id, category in categories.items():
        # Defensive check: ensure icon and title are strings
        icon = str(category.icon) if category.icon is not None else "📁"
        title = str(category.title) if category.title is not None else "Category"
        
        should_expand = (
            category.default_expanded or 
            (cat_id in ["home_search", "drugs_dosing", "calculators_scores"])
        )
        
        # Safely format the expander label
        expander_label = f"{icon} **{title}**"
        
        with st.expander(
            expander_label,
            expanded=should_expand,
            key=f"nav_cat_{cat_id}"
        ):
            for module_id in category.module_ids:
                # Skip sub-items (they'll be handled in main items)
                if module_id in NAVIGATION_SUB_ITEMS:
                    continue
                
                module_info = get_module_info(module_id)
                if module_info:
                    active = is_page_active(module_info.page_path)
                    
                    # Defensive check: ensure icon and title are strings
                    module_icon = str(module_info.icon) if module_info.icon is not None else "📄"
                    module_title = str(module_info.title) if module_info.title is not None else module_id
                    
                    # Add active class styling
                    button_class = "nav-item-active" if active else ""
                    
                    if st.button(
                        f"{module_icon} {module_title}",
                        key=f"nav_{module_id}",
                        use_container_width=True,
                        type="primary" if active else "secondary"
                    ):
                        st.switch_page(module_info.page_path)
                    
                    # Show sub-items if any (with indentation)
                    sub_items = [sid for sid, pid in NAVIGATION_SUB_ITEMS.items() if pid == module_id]
                    if sub_items:
                        for sub_id in sub_items:
                            sub_info = get_module_info(sub_id)
                            if sub_info:
                                sub_active = is_page_active(sub_info.page_path)
                                
                                # Defensive check: ensure icon and title are strings
                                sub_icon = str(sub_info.icon) if sub_info.icon is not None else "📄"
                                sub_title = str(sub_info.title) if sub_info.title is not None else sub_id
                                
                                # Use HTML for better indentation on mobile
                                st.markdown(
                                    f'<div class="sub-item-button" style="padding-left: 24px;">',
                                    unsafe_allow_html=True
                                )
                                if st.button(
                                    f"└ {sub_icon} {sub_title}",
                                    key=f"nav_{sub_id}",
                                    use_container_width=True,
                                    type="primary" if sub_active else "secondary"
                                ):
                                    st.switch_page(sub_info.page_path)
                                st.markdown('</div>', unsafe_allow_html=True)
