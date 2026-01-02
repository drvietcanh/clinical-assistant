"""
Page Template System
Unified page template with slots for consistent structure
"""

import streamlit as st
from typing import Callable, Optional, List, Tuple
from utils.page_helper import setup_page, render_standard_footer


def render_page_template(
    title: str,
    icon: str,
    description: str,
    sidebar_content: Optional[Callable] = None,
    main_content: Callable = None,
    breadcrumbs: Optional[List[Tuple[str, Optional[str]]]] = None,
    hero_section: Optional[str] = None,
    mobile_header: bool = True,
    show_footer: bool = True
) -> None:
    """
    Unified page template with slots
    
    Args:
        title: Page title
        icon: Page icon
        description: Page description
        sidebar_content: Function to render sidebar content
        main_content: Function to render main content (required)
        breadcrumbs: List of (label, url) tuples
        hero_section: Hero section HTML/text
        mobile_header: Show mobile header
        show_footer: Show standard footer
    """
    # Setup page
    setup_page(
        page_title=title,
        page_icon=icon,
        description=description,
        mobile_header=mobile_header
    )
    
    # Breadcrumbs
    if breadcrumbs:
        try:
            from components.mobile_page_wrapper import render_breadcrumbs
            render_breadcrumbs(breadcrumbs)
        except ImportError:
            # Fallback
            breadcrumb_text = " > ".join([label for label, _ in breadcrumbs])
            st.caption(breadcrumb_text)
    
    # Hero section
    if hero_section:
        st.markdown(hero_section, unsafe_allow_html=True)
    
    # Sidebar
    if sidebar_content:
        with st.sidebar:
            sidebar_content()
    
    # Main content
    if main_content:
        main_content()
    else:
        st.error("Main content function is required")
    
    # Footer
    if show_footer:
        render_standard_footer()


def render_simple_page(
    title: str,
    icon: str,
    content: Callable,
    sidebar: Optional[Callable] = None
) -> None:
    """
    Simple page template (minimal)
    
    Args:
        title: Page title
        icon: Page icon
        content: Content function
        sidebar: Optional sidebar function
    """
    setup_page(
        page_title=title,
        page_icon=icon,
        description=f"{icon} {title}",
        mobile_header=True
    )
    
    if sidebar:
        with st.sidebar:
            sidebar()
    
    content()
    
    render_standard_footer()


__all__ = [
    'render_page_template',
    'render_simple_page',
]

