"""
Protocol Evidence Integration Helper
Helper functions to integrate evidence badges into protocols
"""

import streamlit as st
from typing import Optional, Dict
from utils.evidence_levels import EvidenceMetadata
from components.evidence_badge import render_evidence_badge


def render_protocol_evidence(
    protocol_name: str,
    recommendation_key: str = None,
    show_badge: bool = True,
    show_citation: bool = True
) -> None:
    """
    Render evidence badge for a protocol recommendation
    
    Args:
        protocol_name: Protocol name (e.g., "sepsis", "stroke")
        recommendation_key: Specific recommendation key (optional)
        show_badge: Show evidence badge
        show_citation: Show citation
    """
    try:
        from protocols.evidence_examples import get_protocol_evidence
        
        evidence = get_protocol_evidence(protocol_name, recommendation_key)
        
        if evidence:
            if isinstance(evidence, dict):
                # Multiple evidence items
                for key, ev in evidence.items():
                    if show_badge:
                        render_evidence_badge(
                            ev,
                            show_description=True,
                            show_citation=show_citation,
                            compact=False
                        )
            else:
                # Single evidence item
                if show_badge:
                    render_evidence_badge(
                        evidence,
                        show_description=True,
                        show_citation=show_citation,
                        compact=False
                    )
    except ImportError:
        # Evidence examples not available
        pass


def add_evidence_to_recommendation(
    recommendation_text: str,
    evidence: Optional[EvidenceMetadata] = None,
    inline: bool = False
) -> str:
    """
    Add evidence badge inline to recommendation text
    
    Args:
        recommendation_text: Recommendation text
        evidence: Evidence metadata
        inline: Show badge inline (compact mode)
    
    Returns:
        HTML string with evidence badge
    """
    if not evidence:
        return recommendation_text
    
    from utils.evidence_levels import get_evidence_level_color
    color = get_evidence_level_color(evidence.level)
    
    badge_html = f'<span style="background: {color}; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: 600; margin-left: 8px;">Level {evidence.level.value}</span>'
    
    if inline:
        return f"{recommendation_text} {badge_html}"
    else:
        return f"{recommendation_text}<br/>{badge_html}"


__all__ = [
    'render_protocol_evidence',
    'add_evidence_to_recommendation',
]

