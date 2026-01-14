"""
Badge Components for Antibiotics Module
Reusable badge components with CSS classes instead of inline styles
"""

from typing import Optional
from enum import Enum
import streamlit as st


class BadgeType(str, Enum):
    """Badge type enumeration"""
    FIRST_LINE = "first-line"
    ALTERNATIVE = "alternative"
    RESCUE = "rescue"
    STEP_DOWN = "step-down"
    STRONG = "strong"
    WEAK = "weak"
    CONDITIONAL = "conditional"


class BadgeSize(str, Enum):
    """Badge size enumeration"""
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


# Badge icons mapping
BADGE_ICONS = {
    BadgeType.FIRST_LINE: "🟢",
    BadgeType.ALTERNATIVE: "🟡",
    BadgeType.RESCUE: "🔴",
    BadgeType.STEP_DOWN: "💊",
    BadgeType.STRONG: "✅",
    BadgeType.WEAK: "⚠️",
    BadgeType.CONDITIONAL: "🔶",
}


def render_badge(
    text: str,
    badge_type: BadgeType,
    size: BadgeSize = BadgeSize.MEDIUM,
    icon: Optional[str] = None,
    show_icon: bool = True
) -> str:
    """
    Render a badge component with CSS classes.
    
    Args:
        text: Badge text content
        badge_type: Type of badge (FIRST_LINE, ALTERNATIVE, etc.)
        size: Badge size (SMALL, MEDIUM, LARGE)
        icon: Custom icon (if None, uses default for badge_type)
        show_icon: Whether to show icon
    
    Returns:
        HTML string with badge markup
    """
    # Get icon
    if icon is None and show_icon:
        icon = BADGE_ICONS.get(badge_type, "")
    
    # Build CSS classes
    classes = [
        "badge",
        f"badge-{badge_type.value}",
        f"badge-{size.value}"
    ]
    class_str = " ".join(classes)
    
    # Build HTML
    icon_html = f'<span class="badge-icon">{icon}</span>' if icon and show_icon else ""
    text_html = f'<span class="badge-text">{text}</span>'
    
    html = f'''
    <span class="{class_str}">
        {icon_html}
        {text_html}
    </span>
    '''
    
    return html.strip()


def render_badge_html(
    text: str,
    badge_type: BadgeType,
    size: BadgeSize = BadgeSize.MEDIUM,
    icon: Optional[str] = None,
    show_icon: bool = True
) -> None:
    """
    Render a badge component directly using st.markdown.
    
    Args:
        text: Badge text content
        badge_type: Type of badge
        size: Badge size
        icon: Custom icon
        show_icon: Whether to show icon
    """
    html = render_badge(text, badge_type, size, icon, show_icon)
    st.markdown(html, unsafe_allow_html=True)


def render_guideline_badge_html(source: str, year: Optional[int] = None, last_reviewed: Optional[str] = None) -> str:
    """
    Render guideline badge HTML.
    
    Args:
        source: Guideline source name (e.g., "IDSA/ATS")
        year: Guideline year
        last_reviewed: Last reviewed date
    
    Returns:
        HTML string
    """
    guideline_text = source
    if year:
        guideline_text += f" ({year})"
    if last_reviewed:
        guideline_text += f" • Cập nhật: {last_reviewed}"
    
    html = f'''
    <div style="margin-bottom: 12px;">
        <span class="guideline-badge">📋 {guideline_text}</span>
    </div>
    '''
    
    return html.strip()
