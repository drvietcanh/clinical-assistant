"""
CSS Fix Utility for Scores Pages
Injects CSS directly to fix text overlap issues
"""

import streamlit as st


def inject_text_overlap_fix():
    """
    Inject CSS to fix text overlap issues in input fields and headers.
    Call this at the beginning of any score page render function.
    """
    st.markdown("""
    <style>
    /* ========== FIX TEXT OVERLAP IN INPUT FIELDS ========== */
    div[data-testid="stTextInput"] {
        position: relative !important;
        width: 100% !important;
    }
    
    div[data-testid="stTextInput"] > div {
        position: relative !important;
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    div[data-testid="stTextInput"] label {
        position: relative !important;
        display: block !important;
        width: 100% !important;
        margin-bottom: 8px !important;
        z-index: 0 !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                     'Noto Sans', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                     'Helvetica Neue', sans-serif !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        line-height: 1.4 !important;
        color: rgb(49, 51, 63) !important;
    }
    
    div[data-testid="stTextInput"] > div > div > div {
        position: relative !important;
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
    }
    
    div[data-testid="stTextInput"] input {
        position: relative !important;
        z-index: 1 !important;
        width: 100% !important;
        padding: 12px 40px 12px 16px !important;
        box-sizing: border-box !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 
                     'Noto Sans', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                     'Helvetica Neue', sans-serif !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
        color: rgb(49, 51, 63) !important;
        background: white !important;
        border: 1px solid rgb(230, 234, 241) !important;
        border-radius: 8px !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    /* Fix help icon positioning */
    div[data-testid="stTextInput"] [data-testid="stTooltipIcon"],
    div[data-testid="stTextInput"] [class*="help"],
    div[data-testid="stTextInput"] [class*="icon"] {
        position: absolute !important;
        right: 12px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        z-index: 2 !important;
        pointer-events: auto !important;
        width: auto !important;
        height: auto !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove any pseudo-elements */
    div[data-testid="stTextInput"] *::before,
    div[data-testid="stTextInput"] *::after {
        content: none !important;
        display: none !important;
    }
    
    /* Fix BaseWeb input wrapper */
    div[data-testid="stTextInput"] [data-baseweb="input"] {
        position: relative !important;
        width: 100% !important;
    }
    
    div[data-testid="stTextInput"] [data-baseweb="input"] > div {
        position: relative !important;
        width: 100% !important;
    }
    
    div[data-testid="stTextInput"] [data-baseweb="input"] input {
        width: 100% !important;
        padding-right: 40px !important;
    }
    
    /* ========== FIX TEXT OVERLAP IN HEADERS ========== */
    h1, h2, h3, h4, h5, h6 {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
        position: relative !important;
        z-index: 1 !important;
    }
    
    .stMarkdown h1,
    .stMarkdown h2,
    .stMarkdown h3,
    .stMarkdown h4,
    .stMarkdown h5,
    .stMarkdown h6 {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.3 !important;
        position: relative !important;
        z-index: 1 !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Fix subtitle text */
    .stMarkdown p strong,
    .stMarkdown p {
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        line-height: 1.5 !important;
    }
    </style>
    """, unsafe_allow_html=True)

