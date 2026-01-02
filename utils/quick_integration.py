"""
Quick Integration Utilities
One-line functions to quickly add features to pages
"""

import streamlit as st
from typing import Optional


def add_print_button(position: str = "top") -> None:
    """
    Quick way to add print button to any page
    
    Args:
        position: "top" or "bottom"
    """
    try:
        from components.print_friendly_helper import setup_print_friendly_page
        setup_print_friendly_page(show_button=True, button_position=position)
    except ImportError:
        pass


def add_evidence_badge(
    level: str,
    citation: str,
    doi: Optional[str] = None
) -> None:
    """
    Quick way to add evidence badge
    
    Args:
        level: Evidence level (A, B, C, D)
        citation: Citation text
        doi: DOI (optional)
    """
    try:
        from utils.evidence_helper import quick_evidence_badge
        quick_evidence_badge(level=level, citation=citation, doi=doi)
    except ImportError:
        pass


def add_score_chart(
    score: float,
    score_name: str,
    max_score: float = 100,
    min_score: float = 0
) -> None:
    """
    Quick way to add score chart
    
    Args:
        score: Calculated score
        score_name: Name of score
        max_score: Maximum possible score
        min_score: Minimum possible score
    """
    try:
        from components.calculator_visuals_helper import render_score_with_visual, get_default_risk_levels
        
        # Try to detect score type from name
        score_type = score_name.lower().replace(" score", "").replace(" ", "_")
        risk_levels = get_default_risk_levels(score_type)
        
        render_score_with_visual(
            score=score,
            score_name=score_name,
            min_score=min_score,
            max_score=max_score,
            risk_levels=risk_levels,
            show_chart=True,
            show_interpretation=False
        )
    except ImportError:
        # Fallback: simple display
        st.markdown(f"### {score_name}: {score:.1f}/{max_score}")


def add_accessibility_toggle() -> None:
    """
    Quick way to add accessibility toggle to sidebar
    """
    try:
        from components.accessibility import render_accessibility_toggle
        with st.sidebar:
            render_accessibility_toggle()
    except ImportError:
        pass


def add_dashboard_widgets() -> None:
    """
    Quick way to add dashboard widgets to a page
    """
    try:
        from components.dashboard_widgets import render_dashboard_layout
        render_dashboard_layout(
            show_quick_access=True,
            show_activity=True,
            show_recommendations=True,
            show_stats=True
        )
    except ImportError:
        pass


__all__ = [
    'add_print_button',
    'add_evidence_badge',
    'add_score_chart',
    'add_accessibility_toggle',
    'add_dashboard_widgets',
]

