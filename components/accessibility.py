"""
Accessibility Component
Screen reader support, high contrast, keyboard navigation
"""

import streamlit as st
from typing import Optional


def inject_accessibility_styles() -> None:
    """
    Inject accessibility CSS styles
    """
    st.markdown("""
    <style>
    /* High contrast mode */
    .high-contrast {
        --text-primary: #000000 !important;
        --text-secondary: #333333 !important;
        --background: #ffffff !important;
        --border: #000000 !important;
    }
    
    /* Screen reader only text */
    .sr-only {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border-width: 0;
    }
    
    /* Focus indicators */
    *:focus {
        outline: 3px solid #1976d2 !important;
        outline-offset: 2px !important;
    }
    
    /* Skip to main content link */
    .skip-link {
        position: absolute;
        top: -40px;
        left: 0;
        background: #1976d2;
        color: white;
        padding: 8px;
        text-decoration: none;
        z-index: 10000;
    }
    
    .skip-link:focus {
        top: 0;
    }
    
    /* ARIA labels support */
    [aria-label]::before {
        content: attr(aria-label);
    }
    </style>
    """, unsafe_allow_html=True)


def render_accessibility_toggle() -> None:
    """
    Render accessibility options toggle
    """
    inject_accessibility_styles()
    
    st.markdown("### ♿ Tùy chọn Truy cập")
    
    col1, col2 = st.columns(2)
    
    with col1:
        high_contrast = st.checkbox(
            "High Contrast Mode",
            value=st.session_state.get('high_contrast', False),
            key='high_contrast_toggle',
            help="Tăng độ tương phản cho dễ đọc"
        )
        st.session_state['high_contrast'] = high_contrast
    
    with col2:
        large_text = st.checkbox(
            "Large Text",
            value=st.session_state.get('large_text', False),
            key='large_text_toggle',
            help="Tăng kích thước chữ"
        )
        st.session_state['large_text'] = large_text
    
    # Apply styles based on settings
    if high_contrast:
        st.markdown("""
        <script>
        document.body.classList.add('high-contrast');
        </script>
        """, unsafe_allow_html=True)
    
    if large_text:
        st.markdown("""
        <style>
        body {
            font-size: 1.2em !important;
        }
        </style>
        """, unsafe_allow_html=True)


def render_skip_to_content_link() -> None:
    """
    Render skip to main content link for screen readers
    """
    st.markdown("""
    <a href="#main-content" class="skip-link">Skip to main content</a>
    <div id="main-content"></div>
    """, unsafe_allow_html=True)


def add_aria_labels(element_type: str, label: str) -> str:
    """
    Generate HTML with ARIA labels
    
    Args:
        element_type: Type of element
        label: ARIA label text
    
    Returns:
        HTML string with ARIA attributes
    """
    return f'aria-label="{label}" role="{element_type}"'


__all__ = [
    'inject_accessibility_styles',
    'render_accessibility_toggle',
    'render_skip_to_content_link',
    'add_aria_labels',
]

