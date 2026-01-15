"""
Dark Mode Support
Dark theme components and theme switcher
"""

import streamlit as st
from typing import Optional


# Dark mode color scheme
DARK_MODE_COLORS = {
    "background": "#1e1e1e",
    "surface": "#2d2d2d",
    "primary": "#4a9eff",
    "secondary": "#6c757d",
    "text": "#e0e0e0",
    "text_secondary": "#b0b0b0",
    "border": "#404040",
    "success": "#28a745",
    "warning": "#ffc107",
    "error": "#dc3545",
    "info": "#17a2b8"
}

LIGHT_MODE_COLORS = {
    "background": "#ffffff",
    "surface": "#f8f9fa",
    "primary": "#1f77b4",
    "secondary": "#6c757d",
    "text": "#212529",
    "text_secondary": "#6c757d",
    "border": "#dee2e6",
    "success": "#28a745",
    "warning": "#ffc107",
    "error": "#dc3545",
    "info": "#17a2b8"
}


def init_theme_state():
    """Initialize theme state"""
    if 'dark_mode' not in st.session_state:
        # Default to light mode, can be changed by user
        st.session_state['dark_mode'] = False


def get_current_theme() -> dict:
    """Get current theme colors"""
    init_theme_state()
    
    if st.session_state.get('dark_mode', False):
        return DARK_MODE_COLORS
    else:
        return LIGHT_MODE_COLORS


def render_theme_switcher():
    """Render theme switcher button"""
    init_theme_state()
    
    current_theme = "🌙" if not st.session_state.get('dark_mode', False) else "☀️"
    theme_label = "Dark Mode" if not st.session_state.get('dark_mode', False) else "Light Mode"
    
    if st.button(f"{current_theme} {theme_label}", key="theme_switcher"):
        st.session_state['dark_mode'] = not st.session_state.get('dark_mode', False)
        st.rerun()


def apply_theme_styles():
    """Apply theme styles to the page"""
    init_theme_state()
    
    theme = get_current_theme()
    
    theme_css = f"""
    <style>
    :root {{
        --bg-color: {theme['background']};
        --surface-color: {theme['surface']};
        --primary-color: {theme['primary']};
        --text-color: {theme['text']};
        --text-secondary: {theme['text_secondary']};
        --border-color: {theme['border']};
    }}
    
    .stApp {{
        background-color: {theme['background']};
        color: {theme['text']};
    }}
    
    .main .block-container {{
        background-color: {theme['background']};
        color: {theme['text']};
    }}
    
    .stCard {{
        background-color: {theme['surface']};
        border: 1px solid {theme['border']};
        color: {theme['text']};
    }}
    
    .metric-card {{
        background-color: {theme['surface']};
        border: 1px solid {theme['border']};
        color: {theme['text']};
    }}
    
    /* Override Streamlit default styles */
    .stMarkdown {{
        color: {theme['text']};
    }}
    
    .stTextInput>div>div>input {{
        background-color: {theme['surface']};
        color: {theme['text']};
        border-color: {theme['border']};
    }}
    
    .stSelectbox>div>div>select {{
        background-color: {theme['surface']};
        color: {theme['text']};
    }}
    
    .stNumberInput>div>div>input {{
        background-color: {theme['surface']};
        color: {theme['text']};
        border-color: {theme['border']};
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background-color: {theme['surface']};
    }}
    
    /* Alerts */
    .alert-success {{
        background-color: {theme['success']}20;
        border-left: 4px solid {theme['success']};
        color: {theme['text']};
    }}
    
    .alert-warning {{
        background-color: {theme['warning']}20;
        border-left: 4px solid {theme['warning']};
        color: {theme['text']};
    }}
    
    .alert-error {{
        background-color: {theme['error']}20;
        border-left: 4px solid {theme['error']};
        color: {theme['text']};
    }}
    
    .alert-info {{
        background-color: {theme['info']}20;
        border-left: 4px solid {theme['info']};
        color: {theme['text']};
    }}
    </style>
    """
    
    st.markdown(theme_css, unsafe_allow_html=True)


def render_dark_mode_card(content: str, title: Optional[str] = None):
    """Render card with dark mode support"""
    theme = get_current_theme()
    
    card_html = f"""
    <div style="
        background-color: {theme['surface']};
        border: 1px solid {theme['border']};
        border-radius: 8px;
        padding: 16px;
        margin: 8px 0;
        color: {theme['text']};
    ">
    """
    
    if title:
        card_html += f"<h3 style='color: {theme['text']}; margin-top: 0;'>{title}</h3>"
    
    card_html += f"<div style='color: {theme['text']};'>{content}</div>"
    card_html += "</div>"
    
    st.markdown(card_html, unsafe_allow_html=True)


def get_theme_color(color_name: str) -> str:
    """Get theme color by name"""
    theme = get_current_theme()
    return theme.get(color_name, theme['text'])
