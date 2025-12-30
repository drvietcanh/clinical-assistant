"""
Unified Info Box Components
Standardized info, warning, success, and error boxes for consistent UI
"""

import streamlit as st
import html
import textwrap


def render_info_box(
    message: str,
    type: str = "info",
    icon: str = None,
    gradient: bool = True,
    title: str = None
):
    """
    Render standardized info box with consistent styling.
    
    Args:
        message: Main message content
        type: Box type - "info", "warning", "success", "error"
        icon: Custom icon (emoji or HTML)
        gradient: Use gradient background (default: True)
        title: Optional title above message
    
    Returns:
        None (renders directly)
    """
    # Default icons by type
    default_icons = {
        "info": "💡",
        "warning": "⚠️",
        "success": "✅",
        "error": "❌"
    }
    
    # Color schemes by type
    color_schemes = {
        "info": {
            "gradient": "linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
            "border": "#2196f3",
            "text": "#1565c0",
            "bg_solid": "#e3f2fd"
        },
        "warning": {
            "gradient": "linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
            "border": "#ff9800",
            "text": "#e65100",
            "bg_solid": "#fff3e0"
        },
        "success": {
            "gradient": "linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
            "border": "#4caf50",
            "text": "#2e7d32",
            "bg_solid": "#e8f5e9"
        },
        "error": {
            "gradient": "linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)",
            "border": "#f44336",
            "text": "#c62828",
            "bg_solid": "#ffebee"
        }
    }
    
    # Get colors
    colors = color_schemes.get(type, color_schemes["info"])
    display_icon = icon or default_icons.get(type, "💡")
    bg_style = colors["gradient"] if gradient else colors["bg_solid"]
    
    # Build HTML
    title_html = ""
    if title:
        title_html = f'''<div style="font-weight: 700; font-size: 1rem; color: {colors["text"]}; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.2rem;">{display_icon}</span>
            <span>{html.escape(title)}</span>
        </div>'''
    
    margin_top = "margin-top: 8px;" if title else ""
    
    # Detect if message is raw HTML (ignoring leading whitespace)
    _msg_stripped = message.lstrip() if isinstance(message, str) else ""
    is_html = isinstance(message, str) and _msg_stripped.startswith("<")

    # If HTML, also remove leading indentation to avoid Markdown treating it as code
    processed_message = message
    if is_html:
        try:
            processed_message = textwrap.dedent(message).strip()
        except Exception:
            processed_message = message

    box_html = f"""
    <div style="background: {bg_style};
                padding: 1.25rem 1.5rem;
                border-radius: 12px;
                border-left: 5px solid {colors['border']};
                margin-bottom: 1.5rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        {title_html}
        <div style="color: #424242; font-size: 0.95rem; line-height: 1.6; {margin_top}">
            {html.escape(message) if not is_html else processed_message}
        </div>
    </div>
    """
    
    st.markdown(box_html, unsafe_allow_html=True)


def render_hero_section(
    title: str,
    subtitle: str = None,
    gradient_colors: tuple = None,
    icon: str = None,
    description: str = None
):
    """
    Render standardized hero section for page headers.
    
    Args:
        title: Main title
        subtitle: Subtitle text (smaller, above title)
        gradient_colors: Tuple of (color1, color2) for gradient
        icon: Icon emoji or HTML
        description: Description text below title
    
    Returns:
        None (renders directly)
    """
    # Default gradient (purple-blue)
    default_gradient = ("#667eea", "#764ba2")
    gradient = gradient_colors or default_gradient
    
    subtitle_html = ""
    if subtitle:
        subtitle_html = f'''<div style="font-size: 0.95rem; opacity: 0.95; margin-bottom: 0.5rem; font-weight: 500; 
                        letter-spacing: 0.5px; text-transform: uppercase;">{html.escape(subtitle)}</div>'''
    
    icon_html = ""
    if icon:
        icon_html = f'<span style="font-size: 2.2rem;">{icon}</span>'
    
    description_html = ""
    if description:
        description_html = f'<p style="margin: 0; font-size: 1rem; opacity: 0.95; line-height: 1.6; max-width: 800px;">{html.escape(description)}</p>'
    
    hero_html = f"""
    <div style="background: linear-gradient(135deg, {gradient[0]} 0%, {gradient[1]} 100%);
                padding: 2rem 2.5rem;
                border-radius: 20px;
                margin-bottom: 2rem;
                color: white;
                box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; 
                    background: rgba(255,255,255,0.1); border-radius: 50%;"></div>
        <div style="position: absolute; bottom: -30px; left: -30px; width: 150px; height: 150px; 
                    background: rgba(255,255,255,0.08); border-radius: 50%;"></div>
        <div style="position: relative; z-index: 1;">
            {subtitle_html}
            <h2 style="margin: 0 0 0.75rem 0; font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; display: flex; align-items: center; gap: 12px;">
                {icon_html}
                <span>{html.escape(title)}</span>
            </h2>
            {description_html}
        </div>
    </div>
    """
    
    st.markdown(hero_html, unsafe_allow_html=True)


def render_compact_info(
    message: str,
    type: str = "info",
    icon: str = None
):
    """
    Render compact info box (smaller, inline-friendly).
    
    Args:
        message: Message content
        type: Box type
        icon: Custom icon
    """
    icons = {
        "info": "💡",
        "warning": "⚠️",
        "success": "✅",
        "error": "❌"
    }
    
    colors = {
        "info": ("#e3f2fd", "#2196f3"),
        "warning": ("#fff3e0", "#ff9800"),
        "success": ("#e8f5e9", "#4caf50"),
        "error": ("#ffebee", "#f44336")
    }
    
    bg, border = colors.get(type, colors["info"])
    display_icon = icon or icons.get(type, "💡")
    
    compact_html = f"""
    <div style="background: {bg};
                padding: 0.75rem 1rem;
                border-radius: 8px;
                border-left: 3px solid {border};
                margin: 0.5rem 0;
                font-size: 0.9rem;
                color: #424242;">
        <span style="margin-right: 8px;">{display_icon}</span>
        {html.escape(message)}
    </div>
    """
    
    st.markdown(compact_html, unsafe_allow_html=True)

