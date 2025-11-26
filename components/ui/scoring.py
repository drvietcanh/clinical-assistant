"""
Scoring Calculator UI Components
Specialized components for scoring calculators with color-coded results
"""

import streamlit as st
from typing import Optional, Dict, List, Tuple
from config.theme import THEME, COLORS


def get_risk_color(score: int, thresholds: Dict[str, int] = None) -> Tuple[str, str]:
    """
    Get color based on risk score (MDCalc style)
    
    Args:
        score: The calculated score
        thresholds: Custom thresholds dict with keys: low, moderate, high, critical
                   Default: low=6, moderate=11, high=14
    
    Returns:
        Tuple of (color_name, color_hex)
    
    Example:
        >>> color_name, color_hex = get_risk_color(12)
        >>> # Returns: ("risk_high", "#ff5722")
    """
    if thresholds is None:
        thresholds = {
            "low": 6,
            "moderate": 11,
            "high": 14,
        }
    
    if score <= thresholds.get("low", 6):
        return "risk_low", COLORS["risk_low"]
    elif score <= thresholds.get("moderate", 11):
        return "risk_moderate", COLORS["risk_moderate"]
    elif score <= thresholds.get("high", 14):
        return "risk_high", COLORS["risk_high"]
    else:
        return "risk_critical", COLORS["risk_critical"]


def render_score_result(
    title: str,
    score: int,
    interpretation: str,
    mortality: Optional[str] = None,
    color: Optional[str] = None,
    icon: Optional[str] = None,
    thresholds: Optional[Dict[str, int]] = None,
    size: str = "large"
) -> None:
    """
    Render a color-coded score result (MDCalc style)
    
    Args:
        title: Score title (e.g., "SOFA Score")
        score: The calculated score
        interpretation: Interpretation text
        mortality: Optional mortality risk text
        color: Optional color override (if None, auto-calculated from score)
        icon: Optional icon emoji
        thresholds: Custom risk thresholds
        size: Size (small, medium, large)
    
    Example:
        >>> render_score_result(
        ...     "SOFA Score", 12, "Suy cơ quan nặng",
        ...     mortality="~40-60%", icon="🚨"
        ... )
    """
    # Auto-determine color if not provided
    if color is None:
        _, color = get_risk_color(score, thresholds)
    
    # Size mapping
    size_map = {
        "small": {"title": "1rem", "score": "2rem", "padding": "1rem"},
        "medium": {"title": "1.1rem", "score": "2.5rem", "padding": "1.5rem"},
        "large": {"title": "1.25rem", "score": "3rem", "padding": "2rem"},
    }
    
    styles = size_map.get(size, size_map["large"])
    
    icon_html = f'<span style="font-size: {styles["score"]};">{icon}</span> ' if icon else ""
    mortality_html = f'<div style="font-size: 1rem; color: {COLORS["text_secondary"]}; margin-top: 0.5rem;">Tử vong ước tính: <strong>{mortality}</strong></div>' if mortality else ""
    
    box_html = f"""
    <div style="
        background: linear-gradient(135deg, {color}15 0%, {color}05 100%);
        border: 3px solid {color};
        border-radius: 16px;
        padding: {styles['padding']};
        margin: 1.5rem 0;
        text-align: center;
        box-shadow: {THEME['shadows']['lg']};
    ">
        <div style="font-size: {styles['title']}; color: {COLORS['text_secondary']}; margin-bottom: 0.75rem; font-weight: 500;">
            {title}
        </div>
        <div style="font-size: {styles['score']}; font-weight: bold; color: {color}; margin: 0.75rem 0;">
            {icon_html}{score} điểm
        </div>
        <div style="font-size: 1.1rem; font-weight: 600; color: {COLORS['text_primary']}; margin: 0.5rem 0;">
            {interpretation}
        </div>
        {mortality_html}
    </div>
    """
    
    st.markdown(box_html, unsafe_allow_html=True)


def _hex_to_rgba(hex_color: str, alpha: float = 0.15) -> str:
    """Convert hex color to rgba format"""
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {alpha})"


def render_score_breakdown(
    title: str,
    subscores: Dict[str, int],
    total_score: int,
    color_map: Optional[Dict[str, str]] = None
) -> None:
    """
    Render a breakdown of subscores (like organ systems in SOFA)
    
    Args:
        title: Section title
        subscores: Dictionary of {organ_name: score}
        total_score: Total score
        color_map: Optional color mapping for each organ
    
    Example:
        >>> render_score_breakdown(
        ...     "Điểm Từng Hệ Cơ Quan",
        ...     {"Hô hấp": 2, "Tim mạch": 3, "Thận": 1},
        ...     total_score=6
        ... )
    """
    if color_map is None:
        color_map = {}
    
    # Build subscores HTML - using proper formatting to avoid rendering issues
    subscores_html = ""
    for organ, score in subscores.items():
        organ_color = color_map.get(organ, COLORS["primary"])
        organ_bg = _hex_to_rgba(organ_color, 0.15)
        # Escape HTML in organ name to prevent XSS
        organ_escaped = str(organ).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        # Build each row with proper structure
        subscores_html += (
            '<div style="'
            'display: flex; '
            'justify-content: space-between; '
            'align-items: center; '
            f'padding: 0.75rem 1rem; '
            f'border-bottom: 1px solid {COLORS["border"]};'
            '">'
            f'<span style="font-size: 0.95rem; color: {COLORS["text_primary"]};">{organ_escaped}</span>'
            '<span style="'
            'font-size: 1.25rem; '
            'font-weight: bold; '
            f'color: {organ_color}; '
            f'background: {organ_bg}; '
            'padding: 0.25rem 0.75rem; '
            'border-radius: 8px;'
            f'">{score}</span>'
            '</div>'
        )
    
    # Convert primary color to rgba for gradient
    primary_rgba_start = _hex_to_rgba(COLORS['primary'], 0.1)
    primary_rgba_end = _hex_to_rgba(COLORS['primary'], 0.05)
    
    # Escape title to prevent XSS
    title_escaped = str(title).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    # Build complete HTML structure with proper nesting
    breakdown_html = (
        '<div style="'
        f'background: {COLORS["surface"]}; '
        f'border: 2px solid {COLORS["border"]}; '
        'border-radius: 12px; '
        'margin: 1rem 0; '
        'overflow: hidden; '
        f'box-shadow: {THEME["shadows"]["md"]};'
        '">'
        '<div style="'
        f'background: linear-gradient(135deg, {primary_rgba_start} 0%, {primary_rgba_end} 100%); '
        'padding: 1rem; '
        f'border-bottom: 2px solid {COLORS["border"]};'
        '">'
        f'<strong style="font-size: 1.1rem; color: {COLORS["text_primary"]};">{title_escaped}</strong>'
        '</div>'
        '<div>'
        f'{subscores_html}'
        '</div>'
        '<div style="'
        f'background: {COLORS["background_secondary"]}; '
        'padding: 1rem; '
        f'border-top: 2px solid {COLORS["border"]}; '
        'text-align: center;'
        '">'
        f'<span style="font-size: 0.9rem; color: {COLORS["text_secondary"]}; margin-right: 0.5rem;">Tổng điểm:</span>'
        f'<span style="font-size: 1.5rem; font-weight: bold; color: {COLORS["primary"]};">{total_score} điểm</span>'
        '</div>'
        '</div>'
    )
    
    st.markdown(breakdown_html, unsafe_allow_html=True)


def render_quick_reference_table(
    title: str,
    headers: List[str],
    rows: List[List[str]],
    highlight_row: Optional[int] = None
) -> None:
    """
    Render a quick reference table (MDCalc style)
    
    Args:
        title: Table title
        headers: List of column headers
        rows: List of rows (each row is a list of cells)
        highlight_row: Optional row index to highlight
    
    Example:
        >>> render_quick_reference_table(
        ...     "SOFA Scoring Table",
        ...     ["Hệ Cơ Quan", "0", "1", "2", "3", "4"],
        ...     [
        ...         ["Hô hấp", "≥400", "<400", "<300", "<200", "<100"],
        ...         ["Đông máu", "≥150", "<150", "<100", "<50", "<20"],
        ...     ]
        ... )
    """
    # Build header HTML
    header_html = "".join([
        f'<th style="padding: 0.75rem; background: {COLORS["primary"]}; color: white; font-weight: 600; text-align: center;">{header}</th>'
        for header in headers
    ])
    
    # Build rows HTML
    rows_html = ""
    for i, row in enumerate(rows):
        bg_color = COLORS["primary"] + "10" if i == highlight_row else COLORS["surface"]
        rows_html += "<tr>"
        for j, cell in enumerate(row):
            cell_style = f'style="padding: 0.75rem; background: {bg_color}; text-align: {"center" if j > 0 else "left"}; border-bottom: 1px solid {COLORS["border"]};"'
            rows_html += f"<td {cell_style}>{cell}</td>"
        rows_html += "</tr>"
    
    table_html = f"""
    <div style="margin: 1.5rem 0;">
        <h4 style="color: {COLORS['text_primary']}; margin-bottom: 1rem;">{title}</h4>
        <div style="overflow-x: auto;">
            <table style="
                width: 100%;
                border-collapse: collapse;
                background: {COLORS['surface']};
                border-radius: 8px;
                overflow: hidden;
                box-shadow: {THEME['shadows']['sm']};
            ">
                <thead>
                    <tr>{header_html}</tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
    </div>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)


__all__ = [
    'get_risk_color',
    'render_score_result',
    'render_score_breakdown',
    'render_quick_reference_table',
]

