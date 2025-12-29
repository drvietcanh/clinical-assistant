"""
Protocol Dark Mode Component
Toggle between dark and light theme
"""

import streamlit as st
from pathlib import Path


def get_theme_preference() -> str:
    """
    Get user's theme preference from session state.
    
    Returns:
        "dark" or "light"
    """
    return st.session_state.get('protocol_theme', 'light')


def set_theme_preference(theme: str):
    """
    Set user's theme preference.
    
    Args:
        theme: "dark" or "light"
    """
    st.session_state['protocol_theme'] = theme


def toggle_theme():
    """Toggle between dark and light theme."""
    current = get_theme_preference()
    new_theme = 'dark' if current == 'light' else 'light'
    set_theme_preference(new_theme)
    return new_theme


def load_dark_mode_css():
    """Load dark mode CSS if theme is dark."""
    theme = get_theme_preference()
    
    if theme == 'dark':
        try:
            css_file = Path(__file__).parent.parent / "static" / "protocol_dark_mode.css"
            if css_file.exists():
                with open(css_file, "r", encoding="utf-8") as f:
                    return f.read()
        except Exception as e:
            pass
    
    return ""


def apply_theme():
    """Apply theme to page."""
    theme = get_theme_preference()
    
    # Load dark mode CSS if needed
    dark_css = load_dark_mode_css()
    
    # Apply theme attribute to HTML
    theme_script = f"""
    <script>
    (function() {{
        // Set theme attribute
        document.documentElement.setAttribute('data-theme', '{theme}');
        
        // Also apply to body and main container
        document.body.setAttribute('data-theme', '{theme}');
        const mainContainer = document.querySelector('.stApp');
        if (mainContainer) {{
            mainContainer.setAttribute('data-theme', '{theme}');
        }}
    }})();
    </script>
    """
    
    if dark_css:
        st.markdown(f"<style>{dark_css}</style>", unsafe_allow_html=True)
    
    st.markdown(theme_script, unsafe_allow_html=True)


def render_theme_toggle():
    """
    Render theme toggle button in sidebar.
    """
    current_theme = get_theme_preference()
    
    # Icon based on current theme
    icon = "🌙" if current_theme == 'light' else "☀️"
    label = "Dark Mode" if current_theme == 'light' else "Light Mode"
    tooltip = "Chuyển sang Dark Mode" if current_theme == 'light' else "Chuyển sang Light Mode"
    
    if st.button(
        f"{icon} {label}",
        key="protocol_theme_toggle",
        use_container_width=True,
        help=tooltip
    ):
        new_theme = toggle_theme()
        st.rerun()


def render_theme_selector():
    """
    Render theme selector (radio buttons).
    """
    current_theme = get_theme_preference()
    
    theme_options = {
        "☀️ Light Mode": "light",
        "🌙 Dark Mode": "dark"
    }
    
    selected = st.radio(
        "**Giao diện:**",
        options=list(theme_options.keys()),
        index=0 if current_theme == 'light' else 1,
        key="protocol_theme_radio",
        label_visibility="collapsed"
    )
    
    selected_theme = theme_options[selected]
    
    if selected_theme != current_theme:
        set_theme_preference(selected_theme)
        st.rerun()


def init_theme():
    """
    Initialize theme on page load.
    Should be called at the beginning of the page.
    """
    # Initialize theme if not set
    if 'protocol_theme' not in st.session_state:
        # Try to get from browser preference (future enhancement)
        # For now, default to light
        set_theme_preference('light')
    
    # Apply theme
    apply_theme()

