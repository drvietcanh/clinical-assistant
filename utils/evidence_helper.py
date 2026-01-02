"""
Evidence Helper
Easy integration of evidence badges into protocols
"""

from typing import Optional
from utils.evidence_levels import create_evidence_metadata, EvidenceLevel
from components.evidence_badge import render_evidence_badge


def quick_evidence_badge(
    level: str,
    citation: str,
    doi: Optional[str] = None,
    pubmed_id: Optional[str] = None,
    last_reviewed: Optional[str] = None,
    synopsis: Optional[str] = None
) -> None:
    """
    Quick way to render evidence badge
    
    Args:
        level: Evidence level (A, B, C, or D)
        citation: Citation text
        doi: DOI (optional)
        pubmed_id: PubMed ID (optional)
        last_reviewed: Last reviewed date (optional)
        synopsis: Synopsis text (optional)
    """
    try:
        level_enum = EvidenceLevel[level.upper()]
    except KeyError:
        # Invalid level, skip
        return
    
    evidence = create_evidence_metadata(
        level=level_enum,
        citation=citation,
        doi=doi,
        pubmed_id=pubmed_id,
        last_reviewed=last_reviewed,
        synopsis=synopsis
    )
    
    render_evidence_badge(evidence, show_description=True, show_citation=True)


def evidence_for_recommendation(
    recommendation_text: str,
    level: str,
    citation: str,
    inline: bool = False
) -> str:
    """
    Add evidence badge to recommendation text
    
    Args:
        recommendation_text: Recommendation text
        level: Evidence level
        citation: Citation
        inline: Show inline (compact)
    
    Returns:
        HTML string with evidence
    """
    try:
        from utils.evidence_levels import get_evidence_level_color
        from utils.evidence_levels import EvidenceLevel
        
        level_enum = EvidenceLevel[level.upper()]
        color = get_evidence_level_color(level_enum)
        
        badge = f'<span style="background: {color}; color: white; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; font-weight: 600; margin-left: 8px;">Level {level.upper()}</span>'
        
        if inline:
            return f"{recommendation_text} {badge}"
        else:
            return f"{recommendation_text}<br/>{badge}"
    except (KeyError, ImportError):
        return recommendation_text


__all__ = [
    'quick_evidence_badge',
    'evidence_for_recommendation',
]

