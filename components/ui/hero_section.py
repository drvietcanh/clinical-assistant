"""
Hero Section Component
Standardized hero sections for page headers
"""

import streamlit as st
import html


def render_hero(
    title: str,
    subtitle: str = None,
    description: str = None,
    gradient: tuple = None,
    icon: str = None,
    badges: list = None
):
    """
    Render standardized hero section.
    
    Args:
        title: Main title
        subtitle: Subtitle (small text above title)
        description: Description text
        gradient: Tuple (color1, color2) for gradient
        icon: Icon emoji
        badges: List of badge texts to display
    """
    default_gradient = ("#667eea", "#764ba2")
    gradient_colors = gradient or default_gradient
    
    badges_html = ""
    if badges:
        badges_html = '<div style="margin-top: 1rem; display: flex; flex-wrap: wrap; gap: 8px;">'
        for badge in badges:
            badges_html += f'''
            <span style="background: rgba(255,255,255,0.2);
                        padding: 4px 12px;
                        border-radius: 16px;
                        font-size: 0.85rem;
                        border: 1px solid rgba(255,255,255,0.3);">
                {html.escape(badge)}
            </span>
            '''
        badges_html += '</div>'
    
    subtitle_html = ""
    if subtitle:
        subtitle_html = f'''<div style="font-size: 0.95rem; opacity: 0.95; margin-bottom: 0.5rem; font-weight: 500; 
                        letter-spacing: 0.5px; text-transform: uppercase;">{html.escape(subtitle)}</div>'''
    
    icon_html = ""
    if icon:
        icon_html = f'<span style="font-size: 2.2rem;">{icon}</span>'
    
    description_html = ""
    if description:
        description_html = f'<p style="margin: 0; font-size: 1rem; opacity: 0.95; line-height: 1.6; max-width: 800px;">{html.escape(description)}</p>'
    
    hero_html = f"""
    <div style="background: linear-gradient(135deg, {gradient_colors[0]} 0%, {gradient_colors[1]} 100%);
                padding: 2rem 2.5rem;
                border-radius: 20px;
                margin-bottom: 2rem;
                color: white;
                box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
                position: relative;
                overflow: hidden;">
        <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; 
                    background: rgba(255,255,255,0.1); border-radius: 50%;"></div>
        <div style="position: absolute; bottom: -30px; left: -30px; width: 150px; height: 150px; 
                    background: rgba(255,255,255,0.08); border-radius: 50%;"></div>
        <div style="position: relative; z-index: 1;">
            {subtitle_html}
            <h2 style="margin: 0 0 0.75rem 0; font-size: 2rem; font-weight: 700; letter-spacing: -0.5px; display: flex; align-items: center; gap: 12px;">
                {icon_html}
                <span>{html.escape(title)}</span>
            </h2>
            {description_html}
            {badges_html}
        </div>
    </div>
    """
    
    st.markdown(hero_html, unsafe_allow_html=True)

