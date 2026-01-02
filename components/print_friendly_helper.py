"""
Print-Friendly Helper
Easy integration of print-friendly features into pages
"""

import streamlit as st
from components.print_friendly import render_print_button, inject_print_styles


def setup_print_friendly_page(
    page_title: str = None,
    show_button: bool = True,
    button_position: str = "top"
) -> None:
    """
    Setup print-friendly styles and button for a page
    
    Args:
        page_title: Title for print (optional)
        show_button: Whether to show print button
        button_position: "top" or "bottom"
    """
    # Inject print styles
    inject_print_styles()
    
    # Add print button
    if show_button:
        if button_position == "top":
            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                render_print_button("🖨️ In trang này")
        else:
            st.markdown("---")
            render_print_button("🖨️ In trang này")


def add_print_metadata(
    title: str,
    author: str = "Clinical Assistant",
    description: str = None
) -> None:
    """
    Add print metadata to page
    
    Args:
        title: Page title
        author: Author name
        description: Page description
    """
    metadata_html = f"""
    <div class="print-only" style="display: none;">
        <div class="print-title">{title}</div>
        <div class="print-author">{author}</div>
        {f'<div class="print-description">{description}</div>' if description else ''}
        <div class="print-date">{st.session_state.get('print_date', 'N/A')}</div>
    </div>
    """
    st.markdown(metadata_html, unsafe_allow_html=True)


__all__ = [
    'setup_print_friendly_page',
    'add_print_metadata',
]

