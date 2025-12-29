"""
Scores Dark Mode Component
Toggle between dark and light theme for Scores page
"""

import streamlit as st


def get_theme_preference() -> str:
    """Get user's theme preference from session state."""
    return st.session_state.get('scores_theme', 'light')


def set_theme_preference(theme: str):
    """Set user's theme preference."""
    st.session_state['scores_theme'] = theme


def toggle_theme():
    """Toggle between dark and light theme."""
    current = get_theme_preference()
    new_theme = 'dark' if current == 'light' else 'light'
    set_theme_preference(new_theme)
    return new_theme


def apply_theme():
    """Apply theme to page."""
    theme = get_theme_preference()
    
    # Dark mode CSS
    dark_css = """
    <style>
    [data-theme="dark"] {
        --background-color: #1e1e1e;
        --text-color: #e0e0e0;
        --card-background: #2d2d2d;
        --border-color: #404040;
    }
    
    [data-theme="dark"] .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    [data-theme="dark"] .stSidebar {
        background-color: var(--card-background);
    }
    
    [data-theme="dark"] .stMarkdown {
        color: var(--text-color);
    }
    
    [data-theme="dark"] .stInfo {
        background-color: var(--card-background);
        border-color: var(--border-color);
    }
    
    [data-theme="dark"] .stSuccess {
        background-color: #1a4d3a;
        border-color: #2d7a5f;
    }
    
    [data-theme="dark"] .stWarning {
        background-color: #4a3a1a;
        border-color: #7a5f2d;
    }
    
    [data-theme="dark"] .stError {
        background-color: #4a1a1a;
        border-color: #7a2d2d;
    }
    </style>
    """
    
    theme_script = f"""
    <script>
    (function() {{
        document.documentElement.setAttribute('data-theme', '{theme}');
        document.body.setAttribute('data-theme', '{theme}');
        const mainContainer = document.querySelector('.stApp');
        if (mainContainer) {{
            mainContainer.setAttribute('data-theme', '{theme}');
        }}
    }})();
    </script>
    """
    
    if theme == 'dark':
        st.markdown(dark_css, unsafe_allow_html=True)
    
    st.markdown(theme_script, unsafe_allow_html=True)


def render_theme_toggle():
    """Render theme toggle button in sidebar."""
    current_theme = get_theme_preference()
    
    icon = "🌙" if current_theme == 'light' else "☀️"
    label = "Dark Mode" if current_theme == 'light' else "Light Mode"
    
    if st.button(
        f"{icon} {label}",
        key="scores_theme_toggle",
        use_container_width=True,
        help=f"Chuyển sang {'Dark' if current_theme == 'light' else 'Light'} Mode"
    ):
        toggle_theme()
        st.rerun()


def init_theme():
    """Initialize theme on page load."""
    if 'scores_theme' not in st.session_state:
        set_theme_preference('light')
    
    apply_theme()

