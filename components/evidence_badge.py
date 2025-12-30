"""
Evidence Badge Component
Display evidence levels and citations for evidence-based content
"""

import streamlit as st
import html
from typing import Optional, List, Dict
from dataclasses import dataclass


@dataclass
class EvidenceLevel:
    """Evidence level information"""
    level: str  # A, B, C, D
    description: str
    color: str


@dataclass
class Citation:
    """Citation information"""
    authors: str
    title: str
    journal: Optional[str] = None
    year: Optional[int] = None
    doi: Optional[str] = None
    url: Optional[str] = None
    pmid: Optional[str] = None


# Evidence level definitions (based on AHA/ACC classification)
EVIDENCE_LEVELS = {
    "A": EvidenceLevel(
        level="A",
        description="Multiple randomized trials or meta-analyses",
        color="#4caf50"  # Green
    ),
    "B": EvidenceLevel(
        level="B",
        description="Single randomized trial or nonrandomized studies",
        color="#2196f3"  # Blue
    ),
    "C": EvidenceLevel(
        level="C",
        description="Expert opinion, case studies, or standard of care",
        color="#ff9800"  # Orange
    ),
    "D": EvidenceLevel(
        level="D",
        description="Evidence insufficient or conflicting",
        color="#f44336"  # Red
    )
}


def render_evidence_badge(
    level: str,
    show_description: bool = True,
    size: str = "medium"
):
    """
    Render evidence level badge.
    
    Args:
        level: Evidence level (A, B, C, or D)
        show_description: Whether to show description
        size: Badge size ("small", "medium", "large")
    """
    if level not in EVIDENCE_LEVELS:
        return
    
    evidence = EVIDENCE_LEVELS[level]
    
    # Size styles
    size_styles = {
        "small": {
            "font_size": "0.75rem",
            "padding": "4px 8px",
            "badge_size": "1rem"
        },
        "medium": {
            "font_size": "0.85rem",
            "padding": "6px 12px",
            "badge_size": "1.2rem"
        },
        "large": {
            "font_size": "1rem",
            "padding": "8px 16px",
            "badge_size": "1.5rem"
        }
    }
    
    style = size_styles.get(size, size_styles["medium"])
    
    badge_html = f"""
    <div style="display: inline-flex; align-items: center; gap: 6px; margin: 4px 0;">
        <span style="
            background: {evidence.color};
            color: white;
            font-weight: 700;
            font-size: {style['badge_size']};
            padding: {style['padding']};
            border-radius: 6px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        ">Level {evidence.level}</span>
        {f'<span style="font-size: {style["font_size"]}; color: #666;">{html.escape(evidence.description)}</span>' if show_description else ''}
    </div>
    """
    
    st.markdown(badge_html, unsafe_allow_html=True)


def render_citation(
    citation: Citation,
    index: Optional[int] = None,
    show_links: bool = True
):
    """
    Render citation with proper formatting.
    
    Args:
        citation: Citation object
        index: Citation number (optional)
        show_links: Whether to show clickable links
    """
    index_text = f"{index}. " if index else ""
    
    citation_parts = []
    
    # Authors
    if citation.authors:
        citation_parts.append(f"<strong>{html.escape(citation.authors)}</strong>")
    
    # Title
    if citation.title:
        citation_parts.append(f'"{html.escape(citation.title)}"')
    
    # Journal
    if citation.journal:
        citation_parts.append(f"<em>{html.escape(citation.journal)}</em>")
    
    # Year
    if citation.year:
        citation_parts.append(f"({citation.year})")
    
    citation_text = ", ".join(citation_parts)
    
    # Links
    links_html = ""
    if show_links:
        links = []
        if citation.doi:
            links.append(f'<a href="https://doi.org/{citation.doi}" target="_blank" style="color: #1976d2; text-decoration: none; margin-left: 8px;">DOI</a>')
        if citation.url:
            links.append(f'<a href="{html.escape(citation.url)}" target="_blank" style="color: #1976d2; text-decoration: none; margin-left: 8px;">Link</a>')
        if citation.pmid:
            links.append(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{citation.pmid}" target="_blank" style="color: #1976d2; text-decoration: none; margin-left: 8px;">PubMed</a>')
        
        if links:
            links_html = f'<div style="margin-top: 4px;">{" ".join(links)}</div>'
    
    citation_html = f"""
    <div style="margin-bottom: 12px; padding: 8px; background: #f8f9fa; border-radius: 4px; border-left: 3px solid #667eea;">
        <div style="font-size: 0.9rem; line-height: 1.6;">
            {index_text}{citation_text}
        </div>
        {links_html}
    </div>
    """
    
    st.markdown(citation_html, unsafe_allow_html=True)


def render_evidence_section(
    recommendations: List[Dict],
    citations: Optional[List[Citation]] = None
):
    """
    Render evidence section with recommendations and citations.
    
    Args:
        recommendations: List of dicts with 'text', 'level', 'citation_index'
        citations: List of Citation objects
    """
    st.markdown("### 📚 Evidence-Based Recommendations")
    
    for idx, rec in enumerate(recommendations, 1):
        rec_text = rec.get("text", "")
        rec_level = rec.get("level", "C")
        citation_indices = rec.get("citation_indices", [])
        
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"**{idx}. {rec_text}**")
        
        with col2:
            render_evidence_badge(rec_level, show_description=False, size="small")
        
        # Show citation numbers
        if citation_indices and citations:
            citation_nums = ", ".join([f"[{i}]" for i in citation_indices])
            st.caption(f"References: {citation_nums}")
        
        st.markdown("---")
    
    # Citations section
    if citations:
        st.markdown("#### 📖 References")
        for idx, citation in enumerate(citations, 1):
            render_citation(citation, index=idx)


def render_evidence_summary(
    last_reviewed: str,
    last_updated: str,
    version: str = "1.0",
    guideline_source: Optional[str] = None
):
    """
    Render evidence summary box with update information.
    
    Args:
        last_reviewed: Date last reviewed
        last_updated: Date last updated
        version: Version number
        guideline_source: Source guideline (e.g., "AHA/ACC 2023")
    """
    summary_html = f"""
    <div style="
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        padding: 16px;
        border-radius: 8px;
        border-left: 4px solid #1976d2;
        margin: 16px 0;
    ">
        <div style="font-weight: 600; margin-bottom: 8px; color: #1976d2;">
            📋 Evidence Summary
        </div>
        <div style="font-size: 0.9rem; line-height: 1.8;">
            {f'<div><strong>Guideline:</strong> {html.escape(guideline_source)}</div>' if guideline_source else ''}
            <div><strong>Version:</strong> {html.escape(version)}</div>
            <div><strong>Last Reviewed:</strong> {html.escape(last_reviewed)}</div>
            <div><strong>Last Updated:</strong> {html.escape(last_updated)}</div>
        </div>
    </div>
    """
    
    st.markdown(summary_html, unsafe_allow_html=True)

