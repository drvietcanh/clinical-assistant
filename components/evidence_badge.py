"""
Evidence Badge Component
Display evidence level and recommendation strength badges
Supports both new EvidenceGrade system and legacy string-based levels
"""

import streamlit as st
import re
from typing import Union, Optional, Any
from config.evidence_grading import (
    EvidenceGrade,
    EVIDENCE_LEVELS,
    RECOMMENDATION_STRENGTHS,
    create_evidence_grade
)
from utils.evidence_levels import EvidenceLevel, get_evidence_level_color, get_evidence_level_description


def _extract_level_abc(level_text: str) -> Optional[str]:
    """
    Best-effort extraction of A/B/C from strings like:
    - "Class I, Level A"
    - "Level B-R"
    - "A"
    """
    if not level_text:
        return None
    txt = str(level_text).strip().upper()
    # Direct A/B/C
    if txt in {"A", "B", "C"}:
        return txt
    # Look for "... LEVEL X ..."
    m = re.search(r"\bLEVEL\s*([ABC])\b", txt)
    if m:
        return m.group(1)
    # Fallback: first standalone A/B/C token
    m = re.search(r"\b([ABC])\b", txt)
    return m.group(1) if m else None


def render_evidence_badge(
    evidence_grade: Union[EvidenceGrade, str, None] = None,
    strength: Optional[str] = None,
    show_tooltip: bool = True,
    show_description: bool = False,
    size: str = "medium",
    # Legacy API (used by some protocols)
    level: Optional[str] = None,
    recommendation: Optional[str] = None,
    citation: Optional[Any] = None,
) -> None:
    """
    Render evidence badge with level and strength
    
    Args:
        evidence_grade: EvidenceGrade instance or string level ("A", "B", "C")
        strength: Recommendation strength ("Strong", "Weak") - only used if evidence_grade is string
        show_tooltip: Whether to show tooltip on hover
        show_description: Whether to show description text
        size: Badge size ("small", "medium", "large")
    """
    # Legacy kw-API: render_evidence_badge(level="Class I, Level A", recommendation="...", citation=Citation(...))
    if evidence_grade is None and level is not None:
        extracted = _extract_level_abc(level)
        if not extracted:
            st.error(f"Invalid evidence level: {level}")
            return
        evidence_grade = extracted

    # Handle string-based usage (legacy & quick calls)
    if isinstance(evidence_grade, str):
        level_str = evidence_grade.strip().upper()
        if level_str not in EVIDENCE_LEVELS:
            # Try to use legacy EvidenceLevel enum (includes D)
            try:
                legacy_level = EvidenceLevel[level_str]
                level_str = legacy_level.value
            except (KeyError, AttributeError):
                st.error(f"Invalid evidence level: {evidence_grade}")
                return

        strength_str = strength or "Strong"  # Default to Strong if not specified
        evidence_grade = create_evidence_grade(level=level_str, strength=strength_str)

    if evidence_grade is None:
        st.info("Chưa có thông tin về bằng chứng.")
        return
    
    level_info = evidence_grade.get_level_info()
    strength_info = evidence_grade.get_strength_info()
    
    # Size styles
    size_styles = {
        "small": {
            "padding": "4px 8px",
            "font_size": "0.75rem",
            "icon_size": "0.9em"
        },
        "medium": {
            "padding": "6px 12px",
            "font_size": "0.85rem",
            "icon_size": "1em"
        },
        "large": {
            "padding": "8px 16px",
            "font_size": "1rem",
            "icon_size": "1.2em"
        }
    }
    
    style = size_styles.get(size, size_styles["medium"])
    
    # Badge HTML - Only show strength if explicitly provided or in EvidenceGrade
    badge_html = f"""
    <div style="display: inline-flex; align-items: center; gap: 6px; margin: 4px;">
        <span style="
            background-color: {level_info.bg_color};
            color: {level_info.color};
            padding: {style['padding']};
            border-radius: 6px;
            font-size: {style['font_size']};
            font-weight: 600;
            border: 1px solid {level_info.color};
            display: inline-flex;
            align-items: center;
            gap: 4px;
        " title="{level_info.description_vn if show_tooltip else ''}">
            {level_info.icon} Level {evidence_grade.level}
        </span>
    """
    
    # Only show strength badge if strength is provided (not default)
    if strength or (hasattr(evidence_grade, 'strength') and evidence_grade.strength):
        badge_html += f"""
        <span style="
            background-color: {strength_info.bg_color};
            color: {strength_info.color};
            padding: {style['padding']};
            border-radius: 6px;
            font-size: {style['font_size']};
            font-weight: 600;
            border: 1px solid {strength_info.color};
            display: inline-flex;
            align-items: center;
            gap: 4px;
        " title="{strength_info.description_vn if show_tooltip else ''}">
            {strength_info.icon} {strength_info.description_vn}
        </span>
        """
    
    badge_html += "</div>"
    
    if hasattr(evidence_grade, 'source') and evidence_grade.source:
        badge_html += f"""
        <span style="
            color: #6c757d;
            font-size: {style['font_size']};
            margin-left: 8px;
        ">
            ({evidence_grade.source}{f" {evidence_grade.year}" if hasattr(evidence_grade, 'year') and evidence_grade.year else ""})
        </span>
        """
    
    if show_description:
        badge_html += f"""
        <div style="
            font-size: 0.85rem;
            color: #6c757d;
            margin-top: 4px;
        ">
            {level_info.description_vn}
        </div>
        """
    
    st.markdown(badge_html, unsafe_allow_html=True)

    # Optional legacy recommendation + citation rendering (lightweight)
    if recommendation:
        st.caption(f"**Khuyến nghị:** {recommendation}")
    if citation is not None:
        # Support both Citation(text=...) and Citation(source/title/year)
        parts = []
        for attr in ("text", "source", "title", "year", "doi", "pubmed_id"):
            if hasattr(citation, attr):
                val = getattr(citation, attr)
                if val:
                    parts.append(str(val))
        if parts:
            st.caption("**Nguồn:** " + " | ".join(parts))


def render_evidence_level_badge(
    level: str,
    size: str = "medium"
) -> None:
    """
    Render only evidence level badge
    
    Args:
        level: Evidence level ("A", "B", or "C")
        size: Badge size ("small", "medium", "large")
    """
    if level not in EVIDENCE_LEVELS:
        st.error(f"Invalid evidence level: {level}")
        return
    
    level_info = EVIDENCE_LEVELS[level]
    
    size_styles = {
        "small": {"padding": "4px 8px", "font_size": "0.75rem"},
        "medium": {"padding": "6px 12px", "font_size": "0.85rem"},
        "large": {"padding": "8px 16px", "font_size": "1rem"}
    }
    
    style = size_styles.get(size, size_styles["medium"])
    
    badge_html = f"""
    <span style="
        background-color: {level_info.bg_color};
        color: {level_info.color};
        padding: {style['padding']};
        border-radius: 6px;
        font-size: {style['font_size']};
        font-weight: 600;
        border: 1px solid {level_info.color};
        display: inline-flex;
        align-items: center;
        gap: 4px;
    " title="{level_info.description_vn}">
        {level_info.icon} Level {level}
    </span>
    """
    
    st.markdown(badge_html, unsafe_allow_html=True)


def render_recommendation_strength_badge(
    strength: str,
    size: str = "medium"
) -> None:
    """
    Render only recommendation strength badge
    
    Args:
        strength: Recommendation strength ("Strong" or "Weak")
        size: Badge size ("small", "medium", "large")
    """
    if strength not in RECOMMENDATION_STRENGTHS:
        st.error(f"Invalid recommendation strength: {strength}")
        return
    
    strength_info = RECOMMENDATION_STRENGTHS[strength]
    
    size_styles = {
        "small": {"padding": "4px 8px", "font_size": "0.75rem"},
        "medium": {"padding": "6px 12px", "font_size": "0.85rem"},
        "large": {"padding": "8px 16px", "font_size": "1rem"}
    }
    
    style = size_styles.get(size, size_styles["medium"])
    
    badge_html = f"""
    <span style="
        background-color: {strength_info.bg_color};
        color: {strength_info.color};
        padding: {style['padding']};
        border-radius: 6px;
        font-size: {style['font_size']};
        font-weight: 600;
        border: 1px solid {strength_info.color};
        display: inline-flex;
        align-items: center;
        gap: 4px;
    " title="{strength_info.description_vn}">
        {strength_info.icon} {strength_info.description_vn}
    </span>
    """
    
    st.markdown(badge_html, unsafe_allow_html=True)


def _render_evidence_summary_with_grades(
    evidence_grades: list[EvidenceGrade],
    title: str = "Evidence Summary"
) -> None:
    """
    Render evidence summary section with EvidenceGrade list
    
    Args:
        evidence_grades: List of EvidenceGrade instances
        title: Section title
    """
    st.markdown(f"### 📊 {title}")
    
    if not evidence_grades:
        st.info("Chưa có thông tin về bằng chứng.")
        return
    
    # Group by level
    level_counts = {}
    for grade in evidence_grades:
        level = grade.level
        if level not in level_counts:
            level_counts[level] = []
        level_counts[level].append(grade)
    
    # Display summary
    cols = st.columns(len(level_counts))
    for idx, (level, grades) in enumerate(level_counts.items()):
        with cols[idx]:
            level_info = EVIDENCE_LEVELS[level]
            st.markdown(f"""
            <div style="
                background-color: {level_info.bg_color};
                padding: 12px;
                border-radius: 8px;
                border-left: 4px solid {level_info.color};
                text-align: center;
            ">
                <div style="font-size: 1.5rem; margin-bottom: 4px;">
                    {level_info.icon}
                </div>
                <div style="font-weight: 600; color: {level_info.color};">
                    Level {level}
                </div>
                <div style="font-size: 0.85rem; color: #6c757d; margin-top: 4px;">
                    {len(grades)} recommendations
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed list
    st.markdown("**Chi tiết:**")
    for idx, grade in enumerate(evidence_grades, 1):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"{idx}. {grade.get_display_text()}")
        with col2:
            render_evidence_badge(grade, show_tooltip=False, size="small")


# Legacy compatibility functions
def render_evidence_section(
    evidence_grades: list[EvidenceGrade],
    title: str = "Evidence Summary"
) -> None:
    """
    Alias for render_evidence_summary for backward compatibility
    """
    _render_evidence_summary_with_grades(evidence_grades, title)


def render_evidence_summary(
    last_reviewed: Optional[str] = None,
    last_updated: Optional[str] = None,
    version: Optional[str] = None,
    guideline_source: Optional[str] = None,
    evidence_grades: Optional[list[EvidenceGrade]] = None,
    title: str = "Evidence Summary"
) -> None:
    """
    Render evidence summary section (supports both old and new signatures)
    
    Args:
        last_reviewed: Last reviewed date (legacy)
        last_updated: Last updated date (legacy)
        version: Version number (legacy)
        guideline_source: Guideline source (legacy)
        evidence_grades: List of EvidenceGrade instances (new)
        title: Section title
    """
    # If evidence_grades provided, use new format
    if evidence_grades is not None:
        _render_evidence_summary_with_grades(evidence_grades, title)
        return
    
    # Legacy format
    st.markdown(f"### 📊 {title}")
    
    info_items = []
    if guideline_source:
        info_items.append(f"**📚 Guideline:** {guideline_source}")
    if last_reviewed:
        info_items.append(f"**📅 Last Reviewed:** {last_reviewed}")
    if last_updated:
        info_items.append(f"**🔄 Last Updated:** {last_updated}")
    if version:
        info_items.append(f"**📌 Version:** {version}")
    
    if info_items:
        st.info("\n".join(info_items))
    else:
        st.info("Chưa có thông tin về bằng chứng.")




# Citation class for backward compatibility
class Citation:
    """Citation class for evidence references"""
    def __init__(
        self,
        text: Optional[str] = None,
        doi: Optional[str] = None,
        pubmed_id: Optional[str] = None,
        source: Optional[str] = None,
        title: Optional[str] = None,
        year: Optional[int] = None,
        **_: Any,
    ):
        self.text = text
        self.doi = doi
        self.pubmed_id = pubmed_id
        self.source = source
        self.title = title
        self.year = year