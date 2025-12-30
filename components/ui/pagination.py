"""
Pagination Component
Standardized pagination for list views
"""

import streamlit as st


def render_pagination(
    total_items: int,
    items_per_page: int = 20,
    page_key: str = "page",
    show_info: bool = True
) -> tuple:
    """
    Render pagination controls and return current page range.
    
    Args:
        total_items: Total number of items
        items_per_page: Items per page
        page_key: Unique key for page state
        show_info: Show item count info
    
    Returns:
        Tuple of (start_idx, end_idx, current_page, total_pages)
    """
    total_pages = (total_items + items_per_page - 1) // items_per_page if total_items > 0 else 1
    
    if total_pages <= 1:
        return (0, total_items, 1, 1)
    
    # Get current page from session state
    current_page = st.session_state.get(page_key, 1)
    
    # Page selector
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        page_num = st.number_input(
            f"Trang",
            min_value=1,
            max_value=total_pages,
            value=current_page,
            key=page_key,
            label_visibility="collapsed"
        )
        st.session_state[page_key] = page_num
    
    # Calculate indices
    start_idx = (page_num - 1) * items_per_page
    end_idx = min(start_idx + items_per_page, total_items)
    
    # Show info
    if show_info:
        st.caption(f"📄 Hiển thị {start_idx + 1}-{end_idx} / {total_items} items")
        st.markdown("---")
    
    return (start_idx, end_idx, page_num, total_pages)


def get_paginated_items(items: list, items_per_page: int = 20, page_key: str = "page") -> list:
    """
    Get paginated items for current page.
    
    Args:
        items: Full list of items
        items_per_page: Items per page
        page_key: Unique key for page state
    
    Returns:
        Paginated list of items
    """
    start_idx, end_idx, _, _ = render_pagination(
        len(items),
        items_per_page,
        page_key,
        show_info=True
    )
    
    return items[start_idx:end_idx]

