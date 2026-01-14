"""
UI Helper Functions for Antibiotics Module
Common UI components, colors, badges, key helpers and styling utilities
"""

from typing import Dict, Tuple
import re

from .protocols_schema import (
    Severity,
    RegimenType,
    RecommendationLevel,
    AntibioticProtocol,
)

# Color schemes
SEVERITY_COLORS: Dict[Severity, Tuple[str, str]] = {
    Severity.MILD: ("#e8f5e9", "#4caf50"),  # Background, Border
    Severity.MODERATE: ("#fff3e0", "#ff9800"),
    Severity.SEVERE: ("#ffebee", "#f44336"),
    Severity.ICU: ("#fce4ec", "#e91e63")
}

REGIMEN_BADGE_COLORS: Dict[RegimenType, Tuple[str, str]] = {
    RegimenType.FIRST_LINE: ("#4caf50", "🟢"),
    RegimenType.ALTERNATIVE: ("#ff9800", "🟡"),
    RegimenType.RESCUE: ("#f44336", "🔴"),
    RegimenType.STEP_DOWN: ("#2196f3", "💊")
}

RECOMMENDATION_COLORS: Dict[RecommendationLevel, str] = {
    RecommendationLevel.STRONG: "#4caf50",
    RecommendationLevel.WEAK: "#ff9800",
    RecommendationLevel.CONDITIONAL: "#ffc107"
}

AWARE_COLORS = {
    "ACCESS": "#4caf50",  # Green
    "WATCH": "#ffc107",   # Yellow
    "RESERVE": "#f44336"  # Red
}


def slugify_for_key(value: str, max_length: int = 40) -> str:
    """
    Convert an arbitrary string into a safe, compact slug for use in Streamlit keys.

    - Lowercase
    - Replace whitespace with underscores
    - Remove characters outside [a-z0-9_]
    - Trim to max_length, falling back to 'item' if empty
    """
    if not value:
        return "item"

    slug = value.strip().lower()
    slug = re.sub(r"\s+", "_", slug)
    slug = re.sub(r"[^a-z0-9_]+", "", slug)

    if not slug:
        slug = "item"

    return slug[:max_length]


def make_protocol_key(prefix: str, protocol: AntibioticProtocol, index: int) -> str:
    """
    Build a stable, unique key prefix for a protocol and its children.

    Using only site + severity was causing DuplicateElementKey when multiple
    protocols shared the same combination. We include:
    - prefix (e.g. 'infection')
    - infection_site value
    - severity value
    - slugified title
    - protocol index within its group
    """
    parts = [
        prefix,
        getattr(protocol.infection_site, "value", None),
        getattr(protocol.severity, "value", None),
        slugify_for_key(getattr(protocol, "title", "") or "protocol"),
        str(index),
    ]

    key = "_".join(p for p in parts if p)
    # Hard cap to keep keys reasonably short
    return key[:120]


def make_drug_key(base_prefix: str, drug_name: str) -> str:
    """
    Build a safe key prefix for drug-level widgets under a regimen.

    This keeps drug names (often có dấu / khoảng trắng) khỏi làm trùng hoặc
    phá vỡ key của Streamlit.
    """
    slug = slugify_for_key(drug_name or "drug")
    if base_prefix:
        return f"{base_prefix}_drug_{slug}"
    return f"drug_{slug}"


def get_card_style() -> str:
    """Get enhanced card CSS style"""
    return """
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 1px solid #e0e0e0;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    """


def get_protocol_card_style(bg_color: str, border_color: str) -> str:
    """Get protocol card style with colors"""
    return f"""
    background: {bg_color};
    border-left: 4px solid {border_color};
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    """


def render_skeleton_loader(count: int = 3):
    """Render skeleton loaders for loading state"""
    import streamlit as st
    
    for i in range(count):
        st.markdown(f"""
        <div style='
            background: #f5f5f5;
            border-radius: 16px;
            padding: 20px;
            margin-bottom: 16px;
            animation: pulse 1.5s ease-in-out infinite;
        '>
            <div style='height: 20px; background: #e0e0e0; border-radius: 4px; margin-bottom: 12px; width: 60%;'></div>
            <div style='height: 16px; background: #e0e0e0; border-radius: 4px; margin-bottom: 8px; width: 80%;'></div>
            <div style='height: 16px; background: #e0e0e0; border-radius: 4px; width: 40%;'></div>
        </div>
        <style>
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        </style>
        """, unsafe_allow_html=True)


def render_empty_state(message: str, icon: str = "📋"):
    """Render empty state message"""
    import streamlit as st
    
    st.markdown(f"""
    <div style='
        text-align: center;
        padding: 60px 20px;
        color: #666;
    '>
        <div style='font-size: 4em; margin-bottom: 20px;'>{icon}</div>
        <h3 style='color: #333; margin-bottom: 12px;'>{message}</h3>
        <p style='color: #999; font-size: 0.95em;'>Vui lòng thử điều chỉnh bộ lọc hoặc từ khóa tìm kiếm</p>
    </div>
    """, unsafe_allow_html=True)
