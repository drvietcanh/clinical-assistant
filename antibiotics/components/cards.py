"""
Card Components for Antibiotics Module
Reusable card components with CSS classes instead of inline styles
"""

from typing import Optional, List
import streamlit as st
from ..protocols_schema import (
    AntibioticProtocol, Regimen, Severity, DrugDose
)
from .badges import render_badge, BadgeType, BadgeSize
from ..protocols_schema import RegimenType, RecommendationLevel


def render_protocol_card_html(
    protocol: AntibioticProtocol,
    key_prefix: str = ""
) -> str:
    """
    Render protocol card HTML with CSS classes.
    
    Args:
        protocol: AntibioticProtocol object
        key_prefix: Prefix for unique keys
    
    Returns:
        HTML string
    """
    # Get severity class
    severity_class = f"severity-{protocol.severity.value.lower()}"
    
    # Build card HTML
    html = f'''
    <div class="protocol-card {severity_class}">
        <div class="card-header">
            <h3 class="card-title">{protocol.title}</h3>
        </div>
        <div class="card-body">
            <p class="indication-text">{protocol.description or ''}</p>
        </div>
    </div>
    '''
    
    return html.strip()


def render_regimen_card_html(
    regimen: Regimen,
    key_prefix: str = ""
) -> str:
    """
    Render regimen card HTML with CSS classes.
    
    Args:
        regimen: Regimen object
        key_prefix: Prefix for unique keys
    
    Returns:
        HTML string
    """
    # Get badge type
    badge_type_map = {
        RegimenType.FIRST_LINE: BadgeType.FIRST_LINE,
        RegimenType.ALTERNATIVE: BadgeType.ALTERNATIVE,
        RegimenType.RESCUE: BadgeType.RESCUE,
        RegimenType.STEP_DOWN: BadgeType.STEP_DOWN,
    }
    badge_type = badge_type_map.get(regimen.regimen_type, BadgeType.FIRST_LINE)
    badge_text = regimen.regimen_type.get_vietnamese_label()
    
    # Render badge
    badge_html = render_badge(badge_text, badge_type, BadgeSize.MEDIUM)
    
    # Recommendation badge if available
    rec_badge_html = ""
    if regimen.recommendation_level:
        rec_type_map = {
            RecommendationLevel.STRONG: BadgeType.STRONG,
            RecommendationLevel.WEAK: BadgeType.WEAK,
            RecommendationLevel.CONDITIONAL: BadgeType.CONDITIONAL,
        }
        rec_type = rec_type_map.get(regimen.recommendation_level, BadgeType.STRONG)
        rec_text = regimen.recommendation_level.get_vietnamese_label()
        rec_badge_html = render_badge(rec_text, rec_type, BadgeSize.SMALL)
    
    # Build card HTML
    html = f'''
    <div class="regimen-card">
        <div class="card-badges">
            {badge_html}
            {rec_badge_html}
        </div>
        <p class="indication-text">
            <strong>Chỉ định:</strong> {regimen.indication}
        </p>
    </div>
    '''
    
    return html.strip()


def render_drug_card_html(
    drug: DrugDose,
    key_prefix: str = ""
) -> str:
    """
    Render drug card HTML with CSS classes.
    
    Args:
        drug: DrugDose object
        key_prefix: Prefix for unique keys
    
    Returns:
        HTML string
    """
    drug_text = f"{drug.drug_name} {drug.dose} {drug.route} {drug.frequency}"
    if drug.duration:
        drug_text += f" × {drug.duration}"
    
    notes_html = ""
    if drug.notes:
        notes_html = f'<div style="margin-top: 8px; color: #f44336; font-size: 0.85em;">⚠️ {drug.notes}</div>'
    
    html = f'''
    <div class="drug-card">
        <div class="drug-info">
            <span class="drug-name">{drug_text}</span>
        </div>
        {notes_html}
    </div>
    '''
    
    return html.strip()


def render_protocol_card(
    protocol: AntibioticProtocol,
    key_prefix: str = ""
) -> None:
    """
    Render protocol card using st.markdown.
    
    Args:
        protocol: AntibioticProtocol object
        key_prefix: Prefix for unique keys
    """
    html = render_protocol_card_html(protocol, key_prefix)
    st.markdown(html, unsafe_allow_html=True)


def render_regimen_card(
    regimen: Regimen,
    key_prefix: str = ""
) -> None:
    """
    Render regimen card using st.markdown.
    
    Args:
        regimen: Regimen object
        key_prefix: Prefix for unique keys
    """
    html = render_regimen_card_html(regimen, key_prefix)
    st.markdown(html, unsafe_allow_html=True)


def render_drug_card(
    drug: DrugDose,
    key_prefix: str = ""
) -> None:
    """
    Render drug card using st.markdown.
    
    Args:
        drug: DrugDose object
        key_prefix: Prefix for unique keys
    """
    html = render_drug_card_html(drug, key_prefix)
    st.markdown(html, unsafe_allow_html=True)
