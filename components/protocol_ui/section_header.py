"""
Protocol Section Header Component
Enhanced section headers with icons and styling
"""

import streamlit as st


def render_section_header(
    title: str,
    icon: str = "📋",
    level: int = 2,
    description: str = None
):
    """
    Render a styled section header for protocol pages.
    
    Args:
        title: Section title
        icon: Icon emoji or symbol
        level: Header level (1-3, affects styling)
        description: Optional description text below title
    """
    level_class = f"level-{level}"
    
    html = f"""
    <div class="protocol-section-header {level_class}">
        <span class="section-icon">{icon}</span>
        <div style="flex: 1;">
            <span class="section-title">{title}</span>
            {f'<p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: var(--protocol-text-secondary);">{description}</p>' if description else ''}
        </div>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)


def render_evidence_badge(
    level: str,
    source: str,
    year: int = None,
    guideline: str = None
):
    """
    Render evidence level badge.
    
    Args:
        level: Evidence level (A, B, C)
        source: Source organization (e.g., "SSC", "AHA")
        year: Publication year
        guideline: Guideline name
    """
    year_text = f" {year}" if year else ""
    guideline_text = f" - {guideline}" if guideline else ""
    
    html = f"""
    <div class="evidence-badge level-{level}">
        <span class="badge-label">Evidence Level {level}</span>
        <span class="badge-source">{source}{year_text}{guideline_text}</span>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)


def render_protocol_card(
    content: str,
    card_type: str = "default",
    title: str = None
):
    """
    Render content in a styled card.
    
    Args:
        content: Card content (markdown)
        card_type: Card type (default, dosing, monitoring, reference)
        title: Optional card title
    """
    title_html = f'<h4 style="margin-top: 0;">{title}</h4>' if title else ""
    
    html = f"""
    <div class="protocol-card {card_type}">
        {title_html}
        {content}
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)


def render_protocol_divider():
    """Render a styled divider between sections."""
    st.markdown('<hr class="protocol-divider">', unsafe_allow_html=True)

