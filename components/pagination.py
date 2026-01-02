"""
Pagination Component
Standard pagination for list views
"""

import streamlit as st
from typing import List, Any, Callable, Optional
from math import ceil


def render_pagination(
    items: List[Any],
    items_per_page: int = 10,
    page_key: str = "page",
    show_info: bool = True,
    show_jump: bool = True
) -> tuple[List[Any], int, int]:
    """
    Render pagination controls and return paginated items
    
    Args:
        items: List of items to paginate
        items_per_page: Number of items per page
        page_key: Session state key for current page
        show_info: Show pagination info (e.g., "Showing 1-10 of 100")
        show_jump: Show jump to page input
    
    Returns:
        Tuple of (paginated_items, current_page, total_pages)
    """
    if not items:
        return [], 1, 1
    
    total_items = len(items)
    total_pages = ceil(total_items / items_per_page)
    
    # Get current page from session state
    if page_key not in st.session_state:
        st.session_state[page_key] = 1
    
    current_page = st.session_state[page_key]
    
    # Validate page number
    if current_page < 1:
        current_page = 1
    elif current_page > total_pages:
        current_page = total_pages
        st.session_state[page_key] = current_page
    
    # Calculate pagination
    start_idx = (current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    paginated_items = items[start_idx:end_idx]
    
    # Render pagination controls
    if total_pages > 1:
        col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
        
        with col1:
            if st.button("⏮️ Đầu", key=f"{page_key}_first", disabled=(current_page == 1)):
                st.session_state[page_key] = 1
                st.rerun()
        
        with col2:
            if st.button("◀️ Trước", key=f"{page_key}_prev", disabled=(current_page == 1)):
                st.session_state[page_key] = current_page - 1
                st.rerun()
        
        with col3:
            if show_info:
                st.markdown(
                    f"""
                    <div style="text-align: center; padding: 8px;">
                        <span style="color: #666; font-size: 0.9em;">
                            Trang <strong>{current_page}</strong> / {total_pages} 
                            ({start_idx + 1}-{min(end_idx, total_items)} / {total_items})
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="text-align: center; padding: 8px;">
                        <span style="color: #666; font-size: 0.9em;">
                            Trang <strong>{current_page}</strong> / {total_pages}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        with col4:
            if st.button("Tiếp ▶️", key=f"{page_key}_next", disabled=(current_page == total_pages)):
                st.session_state[page_key] = current_page + 1
                st.rerun()
        
        with col5:
            if st.button("Cuối ⏭️", key=f"{page_key}_last", disabled=(current_page == total_pages)):
                st.session_state[page_key] = total_pages
                st.rerun()
        
        # Jump to page
        if show_jump and total_pages > 5:
            with st.expander("🔢 Chuyển đến trang", expanded=False):
                jump_col1, jump_col2 = st.columns([2, 1])
                with jump_col1:
                    jump_page = st.number_input(
                        "Số trang:",
                        min_value=1,
                        max_value=total_pages,
                        value=current_page,
                        key=f"{page_key}_jump"
                    )
                with jump_col2:
                    if st.button("Chuyển", key=f"{page_key}_jump_btn"):
                        st.session_state[page_key] = int(jump_page)
                        st.rerun()
    
    return paginated_items, current_page, total_pages


def render_simple_pagination(
    items: List[Any],
    items_per_page: int = 10,
    page_key: str = "page"
) -> List[Any]:
    """
    Simple pagination without controls (just returns paginated items)
    
    Args:
        items: List of items to paginate
        items_per_page: Number of items per page
        page_key: Session state key for current page
    
    Returns:
        Paginated items
    """
    if not items:
        return []
    
    total_pages = ceil(len(items) / items_per_page)
    
    if page_key not in st.session_state:
        st.session_state[page_key] = 1
    
    current_page = st.session_state[page_key]
    
    if current_page < 1:
        current_page = 1
    elif current_page > total_pages:
        current_page = total_pages
        st.session_state[page_key] = current_page
    
    start_idx = (current_page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    
    return items[start_idx:end_idx]


__all__ = [
    'render_pagination',
    'render_simple_pagination',
]

