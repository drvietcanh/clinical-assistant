"""
Result Display Components
Components for displaying calculation results in a standardized way
"""

import streamlit as st
import html
from typing import Optional, Dict, List, Union
from config.theme import THEME


def render_result_box(
    title: str,
    value: str,
    subtitle: Optional[str] = None,
    color: str = "primary",
    icon: Optional[str] = None,
    size: str = "medium"
) -> None:
    """
    Render a result box with title and value
    
    Args:
        title: Result title
        value: Result value (displayed prominently)
        subtitle: Optional subtitle/description
        color: Color theme (primary, success, warning, error, info)
        icon: Optional icon emoji
        size: Size (small, medium, large)
    
    Example:
        >>> render_result_box(
        ...     "SOFA Score", "12", subtitle="Severe sepsis",
        ...     color="error", icon="🚨"
        ... )
    """
    # Color mapping
    color_map = {
        "primary": THEME['colors']['primary'],
        "success": THEME['colors']['success'],
        "warning": THEME['colors']['warning'],
        "error": THEME['colors']['error'],
        "info": THEME['colors']['info'],
        "neutral": THEME['colors']['neutral'],
    }
    
    bg_color = color_map.get(color, THEME['colors']['primary'])
    
    # Size mapping
    size_map = {
        "small": {"title": "1rem", "value": "1.5rem", "padding": "1rem"},
        "medium": {"title": "1.1rem", "value": "2rem", "padding": "1.5rem"},
        "large": {"title": "1.25rem", "value": "2.5rem", "padding": "2rem"},
    }
    
    styles = size_map.get(size, size_map["medium"])
    
    icon_html = f'<span style="font-size: {styles["value"]};">{icon}</span> ' if icon else ""
    
    subtitle_html = f'<div style="font-size: 0.9rem; color: {THEME["colors"]["text_secondary"]}; margin-top: 0.5rem;">{subtitle}</div>' if subtitle else ""
    
    box_html = f"""
    <div style="
        background: linear-gradient(135deg, {bg_color}15 0%, {bg_color}05 100%);
        border: 2px solid {bg_color};
        border-radius: 12px;
        padding: {styles['padding']};
        margin: 1rem 0;
        text-align: center;
    ">
        <div style="font-size: {styles['title']}; color: {THEME['colors']['text_secondary']}; margin-bottom: 0.5rem;">
            {title}
        </div>
        <div style="font-size: {styles['value']}; font-weight: bold; color: {bg_color}; margin: 0.5rem 0;">
            {icon_html}{value}
        </div>
        {subtitle_html}
    </div>
    """
    
    st.markdown(box_html, unsafe_allow_html=True)


def render_result_card(
    title_or_value: Optional[str] = None,
    metrics_or_label: Optional[Union[List[Dict[str, str]], str]] = None,
    color: str = "primary",
    icon: Optional[str] = None,
    # New keyword arguments for metric card style
    title: Optional[str] = None,
    value: Optional[str] = None,
    unit: Optional[str] = None,
    subtitle: Optional[str] = None
) -> None:
    """
    Render a result card with multiple metrics
    
    Supports three calling patterns:
    1. Metric card style: render_result_card(title="Title", value="Value", unit="Unit", color="color", subtitle="Subtitle")
    2. New style: render_result_card(title, metrics_list, color, icon)
    3. Legacy style: render_result_card(value, label, color) - for simple single metric cards
    
    Args:
        title_or_value: Card title (new style) or metric value (legacy style)
        metrics_or_label: List of dicts with 'label', 'value' (new style) or label string (legacy style)
        color: Card accent color
        icon: Optional title icon (new style only)
        title: Card title (metric card style)
        value: Metric value (metric card style)
        unit: Unit for the value (metric card style)
        subtitle: Subtitle/target text (metric card style)
    
    Example (Metric card style):
        >>> render_result_card(
        ...     title="Plateau",
        ...     value="25.5",
        ...     unit="cmH2O",
        ...     color="success",
        ...     subtitle="Target: ≤30"
        ... )
    
    Example (New style):
        >>> render_result_card(
        ...     "Hemodynamic Parameters",
        ...     [
        ...         {"label": "MAP", "value": "85 mmHg", "icon": "🩺"},
        ...         {"label": "HR", "value": "72 bpm", "icon": "💓"},
        ...     ],
        ...     color="primary"
        ... )
    
    Example (Legacy style):
        >>> render_result_card(
        ...     "85 mmHg",
        ...     "MAP",
        ...     "blue"
        ... )
    """
    color_map = {
        "primary": THEME['colors']['primary'],
        "success": THEME['colors']['success'],
        "warning": THEME['colors']['warning'],
        "error": THEME['colors']['error'],
        "info": THEME['colors']['info'],
        "blue": THEME['colors']['info'],
        "green": THEME['colors']['success'],
        "red": THEME['colors']['error'],
        "orange": THEME['colors']['warning'],
        "purple": THEME['colors']['primary'],
        "neutral": THEME['colors']['neutral'],
        "grey": THEME['colors']['neutral'],
    }
    
    accent_color = color_map.get(color, THEME['colors']['primary'])
    
    # Check if metric card style is being used (has title and value keyword args)
    if title is not None and value is not None:
        # Metric card style: render_result_card(title="Title", value="Value", unit="Unit", color="color", subtitle="Subtitle")
        card_title = html.escape(str(title))
        card_value = html.escape(str(value))
        card_unit = f" {html.escape(str(unit))}" if unit else ""
        card_subtitle = f'<div style="font-size: 0.85rem; color: {THEME["colors"]["text_secondary"]}; margin-top: 0.5rem;">{html.escape(str(subtitle))}</div>' if subtitle else ""
        
        card_html = f"""
        <div style="
            background: {THEME['colors']['surface']};
            border: 2px solid {accent_color};
            border-radius: 12px;
            margin: 1rem 0;
            overflow: hidden;
            box-shadow: {THEME['shadows']['md']};
        ">
            <div style="
                background: linear-gradient(135deg, {accent_color}15 0%, {accent_color}05 100%);
                padding: 1rem;
                text-align: center;
            ">
                <div style="font-size: 0.9rem; color: {THEME['colors']['text_secondary']}; margin-bottom: 0.5rem;">
                    {card_title}
                </div>
                <div style="font-size: 1.5rem; font-weight: bold; color: {accent_color};">
                    {card_value}{card_unit}
                </div>
                {card_subtitle}
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        return
    
    # Detect calling pattern: if metrics_or_label is a string and title_or_value is not None, it's legacy style
    if metrics_or_label is not None and isinstance(metrics_or_label, str) and title_or_value is not None:
        # Legacy style: render_result_card(value, label, color)
        value = html.escape(str(title_or_value))
        label = html.escape(str(metrics_or_label))
        
        # Create a simple card with single metric
        card_html = f"""
        <div style="
            background: {THEME['colors']['surface']};
            border: 2px solid {accent_color};
            border-radius: 12px;
            margin: 1rem 0;
            overflow: hidden;
            box-shadow: {THEME['shadows']['md']};
        ">
            <div style="
                background: linear-gradient(135deg, {accent_color}15 0%, {accent_color}05 100%);
                padding: 1rem;
                text-align: center;
            ">
                <div style="font-size: 0.9rem; color: {THEME['colors']['text_secondary']}; margin-bottom: 0.5rem;">
                    {label}
                </div>
                <div style="font-size: 1.5rem; font-weight: bold; color: {accent_color};">
                    {value}
                </div>
            </div>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        return
    
    # New style: render_result_card(title, metrics_list, color, icon)
    if title_or_value is not None and metrics_or_label is not None:
        title = html.escape(str(title_or_value))
        metrics = metrics_or_label
        icon_html = f"{icon} " if icon else ""
        
        # Build metrics HTML
        metrics_html = ""
        for metric in metrics:
            if isinstance(metric, dict):
                metric_icon = metric.get('icon', '')
                metric_icon_html = f"{metric_icon} " if metric_icon else ""
                metric_color = metric.get('color', THEME['colors']['text_primary'])
                metric_label = html.escape(str(metric.get('label', '')))
                metric_value = html.escape(str(metric.get('value', '')))
                
                metrics_html += f'<div style="padding: 0.75rem; border-bottom: 1px solid {THEME["colors"].get("border", "#e0e0e0")};"><div style="font-size: 0.85rem; color: {THEME["colors"]["text_secondary"]}; margin-bottom: 0.25rem;">{metric_icon_html}{metric_label}</div><div style="font-size: 1.1rem; font-weight: bold; color: {metric_color};">{metric_value}</div></div>'
        
        card_html = f'<div style="background: {THEME["colors"]["surface"]}; border: 2px solid {accent_color}; border-radius: 12px; margin: 1rem 0; overflow: hidden; box-shadow: {THEME["shadows"]["md"]};"><div style="background: linear-gradient(135deg, {accent_color}15 0%, {accent_color}05 100%); padding: 1rem; border-bottom: 2px solid {accent_color};"><strong style="font-size: 1.1rem; color: {THEME["colors"]["text_primary"]};">{icon_html}{title}</strong></div><div>{metrics_html}</div></div>'
        
        st.markdown(card_html, unsafe_allow_html=True)
        return


def render_metric_display(
    label: str,
    value: str,
    unit: Optional[str] = None,
    icon: Optional[str] = None,
    color: Optional[str] = None,
    normal_range: Optional[str] = None,
    status: Optional[str] = None
) -> None:
    """
    Render a single metric display (for tables/lists)
    
    Args:
        label: Metric label
        value: Metric value
        unit: Optional unit
        icon: Optional icon
        color: Optional color override
        normal_range: Optional normal range display
        status: Optional status (normal, high, low)
    
    Example:
        >>> render_metric_display(
        ...     "Creatinine", "1.5", unit="mg/dL",
        ...     normal_range="0.6-1.2", status="high"
        ... )
    """
    # Status color mapping
    status_colors = {
        "normal": THEME['colors']['success'],
        "high": THEME['colors']['warning'],
        "low": THEME['colors']['info'],
        "critical": THEME['colors']['error'],
    }
    
    metric_color = color or status_colors.get(status, THEME['colors']['text_primary'])
    icon_html = f"{icon} " if icon else ""
    unit_html = f" {unit}" if unit else ""
    range_html = f' <span style="font-size: 0.85rem; color: {THEME["colors"]["text_secondary"]};">({normal_range})</span>' if normal_range else ""
    
    metric_html = f"""
    <div style="
        padding: 0.75rem;
        border-bottom: 1px solid {THEME['colors'].get('border', '#e0e0e0')};
        display: flex;
        justify-content: space-between;
        align-items: center;
    ">
        <div style="flex: 1;">
            <div style="font-size: 0.9rem; color: {THEME['colors']['text_secondary']};">
                {icon_html}{label}
            </div>
            {range_html}
        </div>
        <div style="font-size: 1.1rem; font-weight: bold; color: {metric_color};">
            {value}{unit_html}
        </div>
    </div>
    """
    
    st.markdown(metric_html, unsafe_allow_html=True)

