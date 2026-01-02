"""
Calculator Visuals Helper
Easy integration of calculator visuals into score pages
"""

import streamlit as st
from typing import Optional, Dict, Any, List, Tuple
from components.calculator_visuals import render_score_chart


def render_score_with_visual(
    score: float,
    score_name: str,
    min_score: float = 0,
    max_score: float = 100,
    risk_levels: Optional[List[Tuple[float, float, str, str]]] = None,
    interpretation: Optional[str] = None,
    show_chart: bool = True,
    show_interpretation: bool = True
) -> None:
    """
    Render score with visual chart and interpretation
    
    Args:
        score: Calculated score value
        score_name: Name of the score
        min_score: Minimum possible score
        max_score: Maximum possible score
        risk_levels: List of (min, max, label, color) tuples
        interpretation: Text interpretation of the score
        show_chart: Whether to show visual chart
        show_interpretation: Whether to show interpretation text
    """
    # Display score result
    st.markdown(f"### 📊 Kết quả: {score_name}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        '>
            <div style='font-size: 0.9em; opacity: 0.9; margin-bottom: 5px;'>Score</div>
            <div style='font-size: 2.5em; font-weight: bold;'>{score:.1f}</div>
            <div style='font-size: 0.8em; opacity: 0.8;'>/ {max_score}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if interpretation:
            st.info(interpretation)
    
    # Visual chart
    if show_chart:
        if risk_levels is None:
            # Default risk levels if not provided
            risk_levels = [
                (min_score, max_score * 0.33, "Low", "#4caf50"),
                (max_score * 0.33, max_score * 0.67, "Moderate", "#ff9800"),
                (max_score * 0.67, max_score, "High", "#f44336")
            ]
        
        render_score_chart(
            score=score,
            min_score=min_score,
            max_score=max_score,
            risk_levels=risk_levels,
            title=score_name
        )
    
    # Interpretation text
    if show_interpretation and interpretation:
        st.markdown("---")
        st.markdown(f"#### 💡 Giải thích")
        st.markdown(interpretation)


def get_default_risk_levels(score_type: str) -> List[Tuple[float, float, str, str]]:
    """
    Get default risk levels for common score types
    
    Args:
        score_type: Type of score (e.g., "sofa", "apache", "gcs")
    
    Returns:
        List of (min, max, label, color) tuples
    """
    defaults = {
        "sofa": [
            (0, 6, "Low Risk", "#4caf50"),
            (6, 12, "Moderate Risk", "#ff9800"),
            (12, 24, "High Risk", "#f44336")
        ],
        "apache": [
            (0, 15, "Low Risk", "#4caf50"),
            (15, 30, "Moderate Risk", "#ff9800"),
            (30, 71, "High Risk", "#f44336")
        ],
        "gcs": [
            (3, 8, "Severe", "#f44336"),
            (8, 13, "Moderate", "#ff9800"),
            (13, 15, "Mild", "#4caf50")
        ],
        "nihss": [
            (0, 4, "Minor", "#4caf50"),
            (4, 15, "Moderate", "#ff9800"),
            (15, 42, "Severe", "#f44336")
        ]
    }
    
    return defaults.get(score_type.lower(), [
        (0, 33, "Low", "#4caf50"),
        (33, 67, "Moderate", "#ff9800"),
        (67, 100, "High", "#f44336")
    ])


def render_comparison_for_scores(
    scores: List[Dict[str, Any]],
    title: str = "So sánh Scores"
) -> None:
    """
    Render comparison for multiple scores
    
    Args:
        scores: List of score dicts with keys: name, result, interpretation, risk_level
        title: Comparison title
    """
    try:
        from components.calculator_comparison import render_calculator_comparison
        render_calculator_comparison(scores, title=title)
    except ImportError:
        # Fallback: simple display
        st.markdown(f"### {title}")
        for score in scores:
            st.markdown(f"**{score.get('name', 'N/A')}**: {score.get('result', 'N/A')} - {score.get('interpretation', 'N/A')}")


__all__ = [
    'render_score_with_visual',
    'get_default_risk_levels',
    'render_comparison_for_scores',
]

