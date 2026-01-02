"""
Print-Friendly Component
Print-optimized styles and layouts
"""

import streamlit as st
from typing import Optional


def inject_print_styles() -> None:
    """
    Inject print-friendly CSS styles
    """
    st.markdown("""
    <style>
    @media print {
        /* Hide non-essential elements */
        [data-testid="stSidebar"],
        [data-testid="stHeader"],
        button,
        .stButton,
        .stDownloadButton,
        .stFileUploader,
        footer {
            display: none !important;
        }
        
        /* Optimize layout for print */
        .main {
            max-width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Page breaks */
        h1, h2, h3 {
            page-break-after: avoid;
        }
        
        table {
            page-break-inside: avoid;
        }
        
        /* Colors for print */
        * {
            color: #000 !important;
            background: #fff !important;
        }
        
        /* Links */
        a {
            color: #000 !important;
            text-decoration: underline !important;
        }
        
        /* Remove shadows and borders for cleaner print */
        * {
            box-shadow: none !important;
            border: 1px solid #000 !important;
        }
    }
    
    /* Print button styling */
    .print-button {
        background: #1976d2;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 14px;
        font-weight: 500;
        margin: 10px 0;
    }
    
    .print-button:hover {
        background: #1565c0;
    }
    </style>
    """, unsafe_allow_html=True)


def render_print_button(text: str = "🖨️ In trang này") -> None:
    """
    Render print button
    
    Args:
        text: Button text
    """
    inject_print_styles()
    
    st.markdown(f"""
    <button onclick="window.print()" class="print-button">
        {text}
    </button>
    """, unsafe_allow_html=True)


def render_print_friendly_section(
    title: str,
    content: str,
    show_print_button: bool = True
) -> None:
    """
    Render a print-friendly section
    
    Args:
        title: Section title
        content: Section content (HTML)
        show_print_button: Show print button
    """
    inject_print_styles()
    
    if show_print_button:
        render_print_button()
    
    st.markdown(f"""
    <div class="print-friendly-section">
        <h2>{title}</h2>
        <div class="print-content">
            {content}
        </div>
    </div>
    """, unsafe_allow_html=True)


__all__ = [
    'inject_print_styles',
    'render_print_button',
    'render_print_friendly_section',
]

