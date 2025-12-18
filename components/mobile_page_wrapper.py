"""
Mobile Page Wrapper Component
Optimizes page layout for mobile devices with consistent header, breadcrumbs, and mobile-friendly sidebar
"""

import streamlit as st
from typing import Optional, List, Tuple


def render_mobile_page_header(
    title: str,
    icon: str = "📄",
    subtitle: Optional[str] = None,
    show_back_button: bool = True,
    back_url: str = "/"
) -> None:
    """
    Render mobile-optimized page header
    
    Args:
        title: Page title
        icon: Page icon
        subtitle: Optional subtitle
        show_back_button: Show back button
        back_url: URL to navigate back to
    """
    st.markdown("""
    <style>
    .mobile-page-header {
        background: var(--card-bg);
        border-bottom: 1px solid var(--border);
        padding: 1rem;
        margin: -1rem -1rem 1rem -1rem;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 4px var(--shadow);
    }
    
    @media (min-width: 769px) {
        .mobile-page-header {
            display: none;
        }
    }
    
    .mobile-header-content {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .mobile-back-btn {
        background: none;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 8px;
        transition: background 0.2s ease;
        -webkit-tap-highlight-color: transparent;
    }
    
    .mobile-back-btn:active {
        background: var(--border);
    }
    
    .mobile-header-title {
        flex: 1;
    }
    
    .mobile-header-title h1 {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .mobile-header-subtitle {
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin-top: 0.25rem;
    }
    </style>
    
    <div class="mobile-page-header">
        <div class="mobile-header-content">
            """ + (f"""
            <button class="mobile-back-btn" onclick="window.location.href='{back_url}'" aria-label="Quay lại">
                ←
            </button>
            """ if show_back_button else "") + f"""
            <div class="mobile-header-title">
                <h1>{icon} {title}</h1>
                {f'<div class="mobile-header-subtitle">{subtitle}</div>' if subtitle else ''}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_breadcrumbs(items: List[Tuple[str, Optional[str]]]) -> None:
    """
    Render breadcrumb navigation
    
    Args:
        items: List of (label, url) tuples. Last item should have url=None
    """
    if len(items) <= 1:
        return
    
    breadcrumb_html = '<div class="breadcrumb-nav" style="margin-bottom: 1rem; font-size: 0.85rem; color: var(--text-secondary);">'
    
    for idx, (label, url) in enumerate(items):
        if url:
            breadcrumb_html += f'<a href="{url}" style="color: var(--primary); text-decoration: none;">{label}</a>'
        else:
            breadcrumb_html += f'<span style="color: var(--text-primary); font-weight: 600;">{label}</span>'
        
        if idx < len(items) - 1:
            breadcrumb_html += ' <span style="margin: 0 0.5rem;">/</span> '
    
    breadcrumb_html += '</div>'
    
    st.markdown(breadcrumb_html, unsafe_allow_html=True)


def render_mobile_optimized_sidebar(
    title: str,
    content_func,
    collapsible: bool = True
) -> None:
    """
    Render mobile-optimized sidebar that collapses on mobile
    
    Args:
        title: Sidebar title
        content_func: Function that renders sidebar content
        collapsible: Whether sidebar should be collapsible on mobile
    """
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Make sidebar more mobile-friendly */
        [data-testid="stSidebar"] {
            width: 100% !important;
            max-width: 100% !important;
        }
        
        /* Hide sidebar toggle button on mobile if collapsible */
        .mobile-sidebar-toggle {
            position: fixed;
            bottom: 90px; /* Above bottom nav */
            right: 1rem;
            z-index: 999;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 50%;
            width: 56px;
            height: 56px;
            font-size: 1.5rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
    }
    
    @media (min-width: 769px) {
        .mobile-sidebar-toggle {
            display: none;
        }
    }
    </style>
    
    """ + ("""
    <button class="mobile-sidebar-toggle" onclick="
        const sidebar = document.querySelector('[data-testid=\\'stSidebar\\']');
        if (sidebar) {
            sidebar.style.display = sidebar.style.display === 'none' ? 'block' : 'none';
        }
    " aria-label="Mở sidebar">
        ☰
    </button>
    """ if collapsible else ""), unsafe_allow_html=True)
    
    # Render sidebar content
    with st.sidebar:
        st.header(title)
        content_func()


def render_mobile_friendly_tabs(
    tabs: List[Tuple[str, str]],
    default_tab: int = 0
) -> str:
    """
    Render mobile-friendly tabs
    
    Args:
        tabs: List of (label, key) tuples
        default_tab: Default tab index
    
    Returns:
        Selected tab key
    """
    st.markdown("""
    <style>
    /* Mobile-optimized tabs */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab-list"] {
            flex-wrap: wrap;
            gap: 4px;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 8px 12px;
            font-size: 0.85rem;
            min-height: 44px;
            flex: 1;
            min-width: calc(50% - 4px);
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    tab_labels = [label for label, _ in tabs]
    tab_keys = [key for _, key in tabs]
    
    selected_tab = st.tabs(tab_labels)[default_tab]
    
    # Return the key of selected tab (simplified - actual implementation would track selection)
    return tab_keys[default_tab]


def render_mobile_card(
    title: str,
    content: str,
    icon: Optional[str] = None,
    color: str = "var(--primary)",
    onclick: Optional[str] = None
) -> None:
    """
    Render mobile-optimized card
    
    Args:
        title: Card title
        content: Card content (HTML)
        icon: Optional icon
        color: Accent color
        onclick: Optional onclick JavaScript
    """
    onclick_attr = f'onclick="{onclick}"' if onclick else ''
    cursor_style = 'cursor: pointer;' if onclick else ''
    
    st.markdown(f"""
    <div class="mobile-card" style="
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-left: 4px solid {color};
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px var(--shadow);
        transition: all 0.2s ease;
        {cursor_style}
    " {onclick_attr}>
        <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 0.5rem;">
            {f'<span style="font-size: 1.5rem;">{icon}</span>' if icon else ''}
            <h3 style="margin: 0; font-size: 1.1rem; font-weight: 600; color: var(--text-primary);">
                {title}
            </h3>
        </div>
        <div style="color: var(--text-secondary); font-size: 0.9rem; line-height: 1.5;">
            {content}
        </div>
    </div>
    
    <style>
    .mobile-card:hover {{
        box-shadow: 0 4px 8px var(--shadow-hover);
        transform: translateY(-1px);
    }}
    
    .mobile-card:active {{
        transform: scale(0.98);
    }}
    
    @media (max-width: 768px) {{
        .mobile-card {{
            padding: 0.875rem;
            margin-bottom: 0.75rem;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


def render_empty_state(
    icon: str,
    title: str,
    message: str,
    action_label: Optional[str] = None,
    action_url: Optional[str] = None
) -> None:
    """
    Render empty state for mobile
    
    Args:
        icon: Icon emoji
        title: Empty state title
        message: Empty state message
        action_label: Optional action button label
        action_url: Optional action button URL
    """
    action_html = ""
    if action_label and action_url:
        action_html = f"""
        <a href="{action_url}" style="
            display: inline-block;
            margin-top: 1rem;
            padding: 0.75rem 1.5rem;
            background: var(--primary);
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.2s ease;
        ">
            {action_label}
        </a>
        """
    
    st.markdown(f"""
    <div style="
        text-align: center;
        padding: 3rem 1rem;
        color: var(--text-secondary);
    ">
        <div style="font-size: 4rem; margin-bottom: 1rem;">{icon}</div>
        <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">{title}</h3>
        <p style="margin-bottom: 1rem;">{message}</p>
        {action_html}
    </div>
    """, unsafe_allow_html=True)

