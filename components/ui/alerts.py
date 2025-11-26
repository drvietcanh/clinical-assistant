"""
Alert Components
Standardized alert components for info, success, warning, and error messages
"""

import streamlit as st
from typing import Optional
from config.theme import THEME


def render_info_alert(
    message: str,
    title: Optional[str] = None,
    icon: str = "ℹ️",
    expanded: bool = False
) -> None:
    """
    Render an info alert
    
    Args:
        message: Alert message
        title: Optional alert title
        icon: Icon emoji
        expanded: Whether to show in expanded view
    
    Example:
        >>> render_info_alert("Enter patient age", title="Instructions")
    """
    content = f"**{icon} {title}**\n\n{message}" if title else f"{icon} {message}"
    st.info(content, icon=icon)


def render_success_alert(
    message: str,
    title: Optional[str] = None,
    icon: str = "✅",
    expanded: bool = False
) -> None:
    """
    Render a success alert
    
    Args:
        message: Alert message
        title: Optional alert title
        icon: Icon emoji
        expanded: Whether to show in expanded view
    
    Example:
        >>> render_success_alert("Calculation completed successfully")
    """
    content = f"**{icon} {title}**\n\n{message}" if title else f"{icon} {message}"
    st.success(content, icon=icon)


def render_warning_alert(
    message: str,
    title: Optional[str] = None,
    icon: str = "⚠️",
    expanded: bool = False
) -> None:
    """
    Render a warning alert
    
    Args:
        message: Alert message
        title: Optional alert title
        icon: Icon emoji
        expanded: Whether to show in expanded view
    
    Example:
        >>> render_warning_alert("Value is outside normal range", title="Warning")
    """
    content = f"**{icon} {title}**\n\n{message}" if title else f"{icon} {message}"
    st.warning(content, icon=icon)


def render_error_alert(
    message: str,
    title: Optional[str] = None,
    icon: str = "❌",
    show_details: bool = False,
    details: Optional[str] = None
) -> None:
    """
    Render an error alert
    
    Args:
        message: Error message
        title: Optional error title
        icon: Icon emoji
        show_details: Show error details in expander
        details: Error details to show
    
    Example:
        >>> render_error_alert("Invalid input", title="Error", show_details=True, details="Age must be positive")
    """
    content = f"**{icon} {title}**\n\n{message}" if title else f"{icon} {message}"
    st.error(content, icon=icon)
    
    if show_details and details:
        with st.expander("🔍 Chi tiết Lỗi"):
            st.code(details, language="text")


def render_custom_alert(
    message: str,
    alert_type: str = "info",
    title: Optional[str] = None,
    icon: Optional[str] = None,
    html: bool = False
) -> None:
    """
    Render a custom alert with HTML styling
    
    Args:
        message: Alert message
        alert_type: Alert type (info, success, warning, error)
        title: Optional title
        icon: Custom icon (emoji or HTML)
        html: Whether message contains HTML
    
    Example:
        >>> render_custom_alert(
        ...     "Custom message", "warning", title="Alert",
        ...     icon="🚨", html=True
        ... )
    """
    # Default icons
    default_icons = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌",
    }
    
    icon = icon or default_icons.get(alert_type, "ℹ️")
    
    # Color mapping
    color_map = {
        "info": THEME['colors']['info'],
        "success": THEME['colors']['success'],
        "warning": THEME['colors']['warning'],
        "error": THEME['colors']['error'],
    }
    
    bg_color = color_map.get(alert_type, THEME['colors']['info'])
    
    title_html = f"<strong>{icon} {title}</strong><br/><br/>" if title else f"{icon} "
    
    alert_html = f"""
    <div style="
        background: {bg_color}15;
        border-left: 4px solid {bg_color};
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        color: {THEME['colors']['text_primary']};
    ">
        {title_html}{message}
    </div>
    """
    
    st.markdown(alert_html, unsafe_allow_html=True)

