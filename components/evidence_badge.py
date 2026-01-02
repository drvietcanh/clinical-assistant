"""
Evidence Badge Component
Display evidence levels and citations for recommendations
"""

import streamlit as st
from typing import Optional, List
from dataclasses import dataclass
from utils.evidence_levels import (
    EvidenceLevel,
    EvidenceMetadata,
    get_evidence_level_description,
    get_evidence_level_color,
    format_citation
)


def render_evidence_badge(
    metadata: EvidenceMetadata,
    show_description: bool = True,
    show_citation: bool = True,
    compact: bool = False
) -> None:
    """
    Render evidence badge with level and citation
    
    Args:
        metadata: Evidence metadata
        show_description: Show evidence level description
        show_citation: Show citation
        compact: Use compact layout
    """
    level = metadata.level
    color = get_evidence_level_color(level)
    description = get_evidence_level_description(level)
    
    if compact:
        # Compact badge (just level)
        st.markdown(
            f"""
            <div style="
                display: inline-block;
                background: {color};
                color: white;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.75rem;
                font-weight: 600;
                margin-right: 8px;
            ">Level {level.value}</div>
            """,
            unsafe_allow_html=True
        )
    else:
        # Full badge with description and citation
        badge_html = f"""
        <div style="
            background: {color}15;
            border-left: 4px solid {color};
            padding: 12px;
            border-radius: 4px;
            margin: 8px 0;
        ">
            <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                <span style="
                    background: {color};
                    color: white;
                    padding: 4px 8px;
                    border-radius: 4px;
                    font-size: 0.75rem;
                    font-weight: 600;
                ">Level {level.value}</span>
        """
        
        if show_description:
            badge_html += f"""
                <span style="font-size: 0.85rem; color: var(--text-secondary, #666);">
                    {description}
                </span>
            """
        
        badge_html += "</div>"
        
        if show_citation and metadata.citation:
            citation_text = format_citation(metadata)
            badge_html += f"""
                <div style="
                    font-size: 0.8rem;
                    color: var(--text-secondary, #666);
                    margin-top: 8px;
                    padding-top: 8px;
                    border-top: 1px solid var(--border, #e0e0e0);
                ">
                    <strong>Reference:</strong> {citation_text}
                </div>
            """
        
        if metadata.synopsis:
            badge_html += f"""
                <div style="
                    font-size: 0.85rem;
                    color: var(--text-primary, #212121);
                    margin-top: 8px;
                    font-style: italic;
                ">
                    {metadata.synopsis}
                </div>
            """
        
        badge_html += "</div>"
        
        st.markdown(badge_html, unsafe_allow_html=True)


def render_evidence_level_simple(level: str) -> None:
    """
    Render simple evidence level badge
    
    Args:
        level: Evidence level (A, B, C, or D)
    """
    try:
        level_enum = EvidenceLevel[level.upper()]
        color = get_evidence_level_color(level_enum)
        
        st.markdown(
            f"""
            <div style="
                display: inline-block;
                background: {color};
                color: white;
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.75rem;
                font-weight: 600;
            ">Level {level.upper()}</div>
            """,
            unsafe_allow_html=True
        )
    except (KeyError, AttributeError):
        # Invalid level, don't render
        pass


def render_evidence_section(evidence_list: list, title: str = "Evidence") -> None:
    """
    Render a section with multiple evidence badges
    
    Args:
        evidence_list: List of EvidenceMetadata objects
        title: Section title
    """
    if not evidence_list:
        return
    
    st.markdown(f"### {title}")
    for evidence in evidence_list:
        render_evidence_badge(evidence, show_description=True, show_citation=True)


def render_evidence_summary(evidence: EvidenceMetadata, summary_text: str = None) -> None:
    """
    Render evidence summary with optional text
    
    Args:
        evidence: EvidenceMetadata object
        summary_text: Optional summary text
    """
    render_evidence_badge(evidence, show_description=True, show_citation=True)
    if summary_text:
        st.markdown(summary_text)


@dataclass
class Citation:
    """Citation data class for backward compatibility"""
    authors: str
    title: str
    journal: str
    year: int
    doi: Optional[str] = None
    pubmed_id: Optional[str] = None
    
    def __str__(self):
        return f"{self.authors}. {self.title}. {self.journal}. {self.year}."


# Export
__all__ = [
    'render_evidence_badge',
    'render_evidence_level_simple',
    'render_evidence_section',
    'render_evidence_summary',
    'Citation',
]
