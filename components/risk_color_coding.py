"""
Risk Color Coding Component
Provides color coding for risk levels in clinical calculators
"""

import streamlit as st
from typing import Optional, Literal

# Color schemes for risk levels
RISK_COLORS = {
    "very_low": {"color": "#10b981", "bg": "#d1fae5", "text": "Rất thấp"},  # Green
    "low": {"color": "#84cc16", "bg": "#ecfccb", "text": "Thấp"},  # Light green
    "moderate": {"color": "#f59e0b", "bg": "#fef3c7", "text": "Trung bình"},  # Yellow/Orange
    "high": {"color": "#f97316", "bg": "#ffedd5", "text": "Cao"},  # Orange
    "very_high": {"color": "#ef4444", "bg": "#fee2e2", "text": "Rất cao"},  # Red
    "critical": {"color": "#dc2626", "bg": "#fecaca", "text": "Nguy kịch"},  # Dark red
}

# Alternative color scheme (more accessible)
RISK_COLORS_ACCESSIBLE = {
    "very_low": {"color": "#059669", "bg": "#d1fae5", "text": "Rất thấp"},
    "low": {"color": "#65a30d", "bg": "#ecfccb", "text": "Thấp"},
    "moderate": {"color": "#d97706", "bg": "#fef3c7", "text": "Trung bình"},
    "high": {"color": "#ea580c", "bg": "#ffedd5", "text": "Cao"},
    "very_high": {"color": "#dc2626", "bg": "#fee2e2", "text": "Rất cao"},
    "critical": {"color": "#991b1b", "bg": "#fecaca", "text": "Nguy kịch"},
}


def get_risk_level(value: float, thresholds: dict) -> str:
    """
    Determine risk level based on value and thresholds.
    
    Args:
        value: The calculated value
        thresholds: Dict with keys like 'very_low_max', 'low_max', 'moderate_max', 'high_max', 'very_high_max'
    
    Returns:
        Risk level string: 'very_low', 'low', 'moderate', 'high', 'very_high', 'critical'
    """
    if value <= thresholds.get('very_low_max', 0):
        return 'very_low'
    elif value <= thresholds.get('low_max', 0):
        return 'low'
    elif value <= thresholds.get('moderate_max', 0):
        return 'moderate'
    elif value <= thresholds.get('high_max', 0):
        return 'high'
    elif value <= thresholds.get('very_high_max', float('inf')):
        return 'very_high'
    else:
        return 'critical'


def render_risk_badge(
    risk_level: str,
    label: Optional[str] = None,
    value: Optional[float] = None,
    accessible: bool = True
):
    """
    Render a colored risk badge.
    
    Args:
        risk_level: One of 'very_low', 'low', 'moderate', 'high', 'very_high', 'critical'
        label: Optional custom label
        value: Optional value to display
        accessible: Use accessible color scheme
    """
    colors = RISK_COLORS_ACCESSIBLE if accessible else RISK_COLORS
    risk_info = colors.get(risk_level, colors['moderate'])
    
    display_text = label or risk_info['text']
    if value is not None:
        display_text = f"{display_text}: {value:.1f}%"
    
    st.markdown(
        f"""
        <div style="
            background-color: {risk_info['bg']};
            color: {risk_info['color']};
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            border: 2px solid {risk_info['color']};
            font-weight: bold;
            text-align: center;
            display: inline-block;
            margin: 0.25rem;
        ">
            {display_text}
        </div>
        """,
        unsafe_allow_html=True
    )


def render_risk_bar(
    value: float,
    max_value: float = 100,
    thresholds: Optional[dict] = None,
    label: Optional[str] = None,
    accessible: bool = True
):
    """
    Render a colored progress bar for risk visualization.
    
    Args:
        value: Current value
        max_value: Maximum value for scale
        thresholds: Optional dict with risk thresholds
        label: Optional label
        accessible: Use accessible color scheme
    """
    colors = RISK_COLORS_ACCESSIBLE if accessible else RISK_COLORS
    
    # Determine color based on value
    percentage = (value / max_value) * 100 if max_value > 0 else 0
    
    if thresholds:
        risk_level = get_risk_level(value, thresholds)
        color_info = colors.get(risk_level, colors['moderate'])
    else:
        # Simple percentage-based coloring
        if percentage <= 20:
            color_info = colors['very_low']
        elif percentage <= 40:
            color_info = colors['low']
        elif percentage <= 60:
            color_info = colors['moderate']
        elif percentage <= 80:
            color_info = colors['high']
        else:
            color_info = colors['very_high']
    
    display_label = label or f"{value:.1f}%"
    
    st.markdown(
        f"""
        <div style="margin: 0.5rem 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="font-weight: 500;">{display_label}</span>
                <span style="color: {color_info['color']}; font-weight: bold;">{percentage:.1f}%</span>
            </div>
            <div style="
                width: 100%;
                height: 1.5rem;
                background-color: #e5e7eb;
                border-radius: 0.5rem;
                overflow: hidden;
            ">
                <div style="
                    width: {min(percentage, 100)}%;
                    height: 100%;
                    background-color: {color_info['color']};
                    transition: width 0.3s ease;
                "></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_risk_table(
    risk_data: list,
    accessible: bool = True
):
    """
    Render a table with color-coded risk levels.
    
    Args:
        risk_data: List of dicts with keys: 'label', 'value', 'risk_level'
        accessible: Use accessible color scheme
    """
    colors = RISK_COLORS_ACCESSIBLE if accessible else RISK_COLORS
    
    table_html = """
    <table style="width: 100%; border-collapse: collapse; margin: 1rem 0;">
        <thead>
            <tr style="background-color: #f3f4f6;">
                <th style="padding: 0.75rem; text-align: left; border: 1px solid #d1d5db;">Mức độ</th>
                <th style="padding: 0.75rem; text-align: left; border: 1px solid #d1d5db;">Giá trị</th>
                <th style="padding: 0.75rem; text-align: left; border: 1px solid #d1d5db;">Ý nghĩa</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for item in risk_data:
        risk_level = item.get('risk_level', 'moderate')
        color_info = colors.get(risk_level, colors['moderate'])
        
        table_html += f"""
            <tr style="background-color: {color_info['bg']};">
                <td style="padding: 0.75rem; border: 1px solid #d1d5db; color: {color_info['color']}; font-weight: bold;">
                    {item.get('label', '')}
                </td>
                <td style="padding: 0.75rem; border: 1px solid #d1d5db;">
                    {item.get('value', '')}
                </td>
                <td style="padding: 0.75rem; border: 1px solid #d1d5db;">
                    {item.get('meaning', '')}
                </td>
            </tr>
        """
    
    table_html += """
        </tbody>
    </table>
    """
    
    st.markdown(table_html, unsafe_allow_html=True)


def get_risk_color(risk_level: str, accessible: bool = True) -> dict:
    """
    Get color information for a risk level.
    
    Returns:
        Dict with 'color', 'bg', 'text' keys
    """
    colors = RISK_COLORS_ACCESSIBLE if accessible else RISK_COLORS
    return colors.get(risk_level, colors['moderate'])

