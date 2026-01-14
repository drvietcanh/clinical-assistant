"""
Typography Components for Antibiotics Module
Reusable typography components with CSS classes
"""

from typing import Optional
import streamlit as st


def render_indication_text(text: str, strong_label: Optional[str] = None) -> str:
    """
    Render indication text with CSS classes.
    
    Args:
        text: Indication text
        strong_label: Optional label to make bold (e.g., "Chỉ định:")
    
    Returns:
        HTML string
    """
    if strong_label:
        html = f'''
        <p class="indication-text">
            <strong>{strong_label}</strong> {text}
        </p>
        '''
    else:
        html = f'<p class="indication-text">{text}</p>'
    
    return html.strip()


def render_guideline_badge(source: str, year: Optional[int] = None, last_reviewed: Optional[str] = None) -> str:
    """
    Render guideline badge HTML.
    
    Args:
        source: Guideline source name (e.g., "IDSA/ATS")
        year: Guideline year
        last_reviewed: Last reviewed date
    
    Returns:
        HTML string
    """
    guideline_text = source
    if year:
        guideline_text += f" ({year})"
    if last_reviewed:
        guideline_text += f" • Cập nhật: {last_reviewed}"
    
    html = f'''
    <div style="margin-bottom: 12px;">
        <span class="guideline-badge">📋 {guideline_text}</span>
    </div>
    '''
    
    return html.strip()


def render_drug_info(drug_name: str, dose: str, route: str, group: Optional[str] = None) -> str:
    """
    Render drug information with CSS classes.
    
    Args:
        drug_name: Drug name
        dose: Dose information
        route: Route of administration
        group: Optional drug group
    
    Returns:
        HTML string
    """
    admin_str = f"{dose} {route}"
    
    html = f'''
    <div class="drug-info">
        <span class="drug-name">{admin_str}</span>
    '''
    
    if group:
        html += f'''
        <span style="color: #ddd; margin: 0 10px; font-weight: 300;">•</span>
        <span class="drug-group">{group}</span>
        '''
    
    html += '</div>'
    
    return html.strip()


def render_vietnamese_name(name: str) -> str:
    """
    Render Vietnamese name with CSS classes.
    
    Args:
        name: Vietnamese name
    
    Returns:
        HTML string
    """
    html = f'<div class="vietnamese-name">{name}</div>'
    return html.strip()


def render_indication_text_html(text: str, strong_label: Optional[str] = None) -> None:
    """
    Render indication text directly using st.markdown.
    
    Args:
        text: Indication text
        strong_label: Optional label to make bold
    """
    html = render_indication_text(text, strong_label)
    st.markdown(html, unsafe_allow_html=True)


def render_guideline_badge_html(source: str, year: Optional[int] = None, last_reviewed: Optional[str] = None) -> None:
    """
    Render guideline badge directly using st.markdown.
    
    Args:
        source: Guideline source name
        year: Guideline year
        last_reviewed: Last reviewed date
    """
    html = render_guideline_badge(source, year, last_reviewed)
    st.markdown(html, unsafe_allow_html=True)


def render_drug_info_html(drug_name: str, dose: str, route: str, group: Optional[str] = None) -> None:
    """
    Render drug information directly using st.markdown.
    
    Args:
        drug_name: Drug name
        dose: Dose information
        route: Route of administration
        group: Optional drug group
    """
    html = render_drug_info(drug_name, dose, route, group)
    st.markdown(html, unsafe_allow_html=True)


def render_vietnamese_name_html(name: str) -> None:
    """
    Render Vietnamese name directly using st.markdown.
    
    Args:
        name: Vietnamese name
    """
    html = render_vietnamese_name(name)
    st.markdown(html, unsafe_allow_html=True)
