"""
Unified Card Component
Standard card design for all pages
"""

import streamlit as st
from typing import List, Dict, Optional
import html


def render_info_card(
    title: str,
    content: str,
    badges: Optional[List[Dict]] = None,
    actions: Optional[List[Dict]] = None,
    style: str = "default",
    icon: Optional[str] = None
) -> None:
    """
    Standard card component
    
    Args:
        title: Card title
        content: Card content (can be HTML)
        badges: List of badge dicts with 'label', 'color', 'bg_color'
        actions: List of action dicts with 'label', 'action' (callable), 'icon'
        style: Card style ("default", "gradient", "outlined")
        icon: Optional icon
    """
    # Style configurations
    styles = {
        "default": {
            "background": "#ffffff",
            "border": "1px solid #e0e0e0",
            "border_left": "4px solid #2196f3"
        },
        "gradient": {
            "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            "border": "none",
            "border_left": "none",
            "color": "white"
        },
        "outlined": {
            "background": "#ffffff",
            "border": "2px solid #2196f3",
            "border_left": "none"
        }
    }
    
    card_style = styles.get(style, styles["default"])
    
    # Build card HTML
    card_html = f"""
    <div style="
        background: {card_style.get('background', '#ffffff')};
        border: {card_style.get('border', '1px solid #e0e0e0')};
        border-left: {card_style.get('border_left', '4px solid #2196f3')};
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: {card_style.get('color', '#212121')};
    ">
    """
    
    # Title
    if icon:
        card_html += f"<h3 style='margin: 0 0 12px 0; color: {card_style.get('color', '#212121')};'>{icon} {html.escape(title)}</h3>"
    else:
        card_html += f"<h3 style='margin: 0 0 12px 0; color: {card_style.get('color', '#212121')};'>{html.escape(title)}</h3>"
    
    # Badges
    if badges:
        card_html += "<div style='margin-bottom: 12px;'>"
        for badge in badges:
            label = badge.get('label', '')
            bg_color = badge.get('bg_color', '#e3f2fd')
            color = badge.get('color', '#1976d2')
            card_html += f"""
            <span style="
                background: {bg_color};
                color: {color};
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 0.75rem;
                font-weight: 600;
                margin-right: 8px;
            ">{html.escape(label)}</span>
            """
        card_html += "</div>"
    
    # Content
    card_html += f"<div style='color: {card_style.get('color', '#424242')}; line-height: 1.6;'>{content}</div>"
    
    # Actions
    if actions:
        card_html += "<div style='margin-top: 16px; display: flex; gap: 8px;'>"
        for action in actions:
            action_label = action.get('label', '')
            action_icon = action.get('icon', '')
            card_html += f"""
            <button style="
                background: #2196f3;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 0.9rem;
            ">{action_icon} {html.escape(action_label)}</button>
            """
        card_html += "</div>"
    
    card_html += "</div>"
    
    st.markdown(card_html, unsafe_allow_html=True)


def render_card_grid(
    cards: List[Dict],
    columns: int = 3,
    card_style: str = "default"
) -> None:
    """
    Render cards in a grid layout
    
    Args:
        cards: List of card dicts with 'title', 'content', 'badges', 'actions', 'icon'
        columns: Number of columns
        card_style: Card style
    """
    cols = st.columns(columns)
    
    for idx, card in enumerate(cards):
        with cols[idx % columns]:
            render_info_card(
                title=card.get('title', ''),
                content=card.get('content', ''),
                badges=card.get('badges'),
                actions=card.get('actions'),
                style=card_style,
                icon=card.get('icon')
            )


__all__ = [
    'render_info_card',
    'render_card_grid',
]

