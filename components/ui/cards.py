"""
Standard Card Components
Unified card design system for consistent UI
"""

import streamlit as st
import html
from typing import List, Dict, Optional


def render_info_card(
    title: str,
    content: str = None,
    badges: List[Dict] = None,
    actions: List[Dict] = None,
    style: str = "default",
    border_color: str = None,
    gradient: tuple = None
):
    """
    Render standardized info card.
    
    Args:
        title: Card title
        content: Main content (HTML or text)
        badges: List of {text, color, bg} dicts
        actions: List of {label, url, type} dicts
        style: "default", "gradient", "outlined"
        border_color: Custom border color
        gradient: Tuple (color1, color2) for gradient background
    
    Returns:
        None (renders directly)
    """
    # Style configurations
    style_configs = {
        "default": {
            "bg": "white",
            "border": "1px solid #e0e0e0",
            "shadow": "0 2px 8px rgba(0,0,0,0.08)"
        },
        "gradient": {
            "bg": gradient[0] if gradient else "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "border": "none",
            "shadow": "0 4px 12px rgba(102, 126, 234, 0.2)"
        },
        "outlined": {
            "bg": "transparent",
            "border": f"2px solid {border_color or '#667eea'}",
            "shadow": "none"
        }
    }
    
    config = style_configs.get(style, style_configs["default"])
    
    # Badges HTML
    badges_html = ""
    if badges:
        badges_html = '<div style="margin-bottom: 12px; display: flex; flex-wrap: wrap; gap: 8px;">'
        for badge in badges:
            bg = badge.get("bg", "#e3f2fd")
            color = badge.get("color", "#1976d2")
            text = badge.get("text", "")
            badges_html += f'''
            <span style="background: {bg};
                        color: {color};
                        padding: 4px 12px;
                        border-radius: 16px;
                        font-size: 0.8rem;
                        font-weight: 500;">
                {html.escape(text)}
            </span>
            '''
        badges_html += '</div>'
    
    # Actions HTML
    actions_html = ""
    if actions:
        actions_html = '<div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e0e0e0; display: flex; gap: 12px; flex-wrap: wrap;">'
        for action in actions:
            label = action.get("label", "")
            url = action.get("url", "#")
            action_type = action.get("type", "primary")
            
            if action_type == "primary":
                btn_style = "background: #2196f3; color: white; padding: 8px 16px; border-radius: 8px; text-decoration: none; font-weight: 500;"
            else:
                btn_style = "background: transparent; color: #2196f3; padding: 8px 16px; border-radius: 8px; text-decoration: none; border: 1px solid #2196f3;"
            
            actions_html += f'''
            <a href="{html.escape(url)}" target="_blank" style="{btn_style}">
                {html.escape(label)}
            </a>
            '''
        actions_html += '</div>'
    
    content_html = ""
    if content:
        content_escaped = content if content.startswith("<") else html.escape(content)
        content_html = f'<div style="color: #424242; font-size: 0.95rem; line-height: 1.6; margin: 12px 0;">{content_escaped}</div>'
    
    card_html = f"""
    <div style="background: {config['bg']};
                border: {config['border']};
                border-radius: 12px;
                padding: 24px;
                margin-bottom: 20px;
                box-shadow: {config['shadow']};
                transition: all 0.3s ease;">
        <h3 style="margin: 0 0 12px 0; font-size: 1.3rem; font-weight: 700; color: #1a1a1a;">
            {html.escape(title)}
        </h3>
        {badges_html}
        {content_html}
        {actions_html}
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def render_stat_card(
    label: str,
    value: str,
    icon: str = None,
    trend: str = None,
    color: str = "#2196f3"
):
    """
    Render statistic card (for dashboards).
    
    Args:
        label: Stat label
        value: Stat value
        icon: Icon emoji
        trend: Trend indicator (e.g., "+5%")
        color: Accent color
    """
    card_html = f"""
    <div style="background: white;
                border-radius: 12px;
                padding: 1.5rem;
                border-left: 4px solid {color};
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
        <div style="font-size: 0.85rem; color: #616161; margin-bottom: 8px;">
            {f'<span style="margin-right: 6px;">{icon}</span>' if icon else ''}
            {html.escape(label)}
        </div>
        <div style="font-size: 2rem; font-weight: 700; color: {color};">
            {html.escape(value)}
        </div>
        {f'<div style="font-size: 0.8rem; color: #4caf50; margin-top: 4px;">{html.escape(trend)}</div>' if trend else ''}
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
