"""
Phase 1 Protocol Enhancement Component
Automatically adds evidence levels, citations, and version tracking to protocols
"""

import streamlit as st
from typing import Optional, Dict, List, Any
from components.protocol_version import render_version_badge, render_version_history, get_protocol_version
from components.evidence_badge import render_evidence_badge, Citation
from components.references import render_references_section
from protocols.references_config import PROTOCOL_REFERENCES, get_references
from utils.evidence_levels import EvidenceMetadata, EvidenceLevel
from datetime import datetime


def render_protocol_header(
    protocol_name: str,
    guideline_source: Optional[str] = None,
    show_version: bool = True,
    show_evidence_summary: bool = True
):
    """
    Render enhanced protocol header with version and evidence info.
    
    Args:
        protocol_name: Name of the protocol
        guideline_source: Source guideline (e.g., "AHA/ACC 2023")
        show_version: Whether to show version badge
        show_evidence_summary: Whether to show evidence summary
    """
    if show_version:
        render_version_badge(protocol_name)
    
    if show_evidence_summary:
        version_info = get_protocol_version(protocol_name)
        if version_info:
            # Create evidence metadata from version info
            guideline_source_str = guideline_source or version_info.get("guideline", "")
            last_updated = version_info.get("last_updated", "")
            version = version_info.get("version", "1.0")
            
            # Create a simple evidence metadata for protocol header
            evidence = EvidenceMetadata(
                level=EvidenceLevel.C,  # Default to C for protocol-level evidence
                citation=guideline_source_str,
                last_reviewed=last_updated,
                version=version,
                synopsis=f"Protocol version {version}. Last updated: {last_updated}."
            )
            
            # Render simple version/guideline info instead of full evidence summary
            if guideline_source_str or last_updated:
                st.markdown(f"""
                <div style="
                    background: #f5f5f5;
                    border-left: 4px solid #2196F3;
                    padding: 12px;
                    border-radius: 4px;
                    margin: 8px 0;
                    font-size: 0.9rem;
                ">
                    <strong>📚 Guideline:</strong> {guideline_source_str}<br>
                    <strong>📅 Last Updated:</strong> {last_updated}<br>
                    <strong>📌 Version:</strong> {version}
                </div>
                """, unsafe_allow_html=True)


def render_recommendation_with_evidence(
    recommendation_text: str,
    evidence_level: str = "C",
    citation_indices: Optional[List[int]] = None,
    inline: bool = True
):
    """
    Render a recommendation with evidence level badge.
    
    Args:
        recommendation_text: The recommendation text
        evidence_level: Evidence level (A, B, C, D)
        citation_indices: List of citation indices
        inline: Whether to show badge inline or separate
    """
    if inline:
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"**{recommendation_text}**")
        with col2:
            render_evidence_badge(evidence_level, show_description=False, size="small")
        
        if citation_indices:
            citation_nums = ", ".join([f"[{i}]" for i in citation_indices])
            st.caption(f"References: {citation_nums}")
    else:
        st.markdown(f"**{recommendation_text}**")
        render_evidence_badge(evidence_level, show_description=True, size="medium")
        if citation_indices:
            citation_nums = ", ".join([f"[{i}]" for i in citation_indices])
            st.caption(f"References: {citation_nums}")


def render_protocol_references(protocol_name: str):
    """
    Render references section for a protocol.
    
    Args:
        protocol_name: Name of the protocol
    """
    references = get_references(protocol_name)
    if references:
        render_references_section(references)
    else:
        st.info("💡 References đang được cập nhật. Vui lòng kiểm tra lại sau.")


def render_protocol_footer(protocol_name: str):
    """
    Render protocol footer with version history and disclaimer.
    
    Args:
        protocol_name: Name of the protocol
    """
    st.markdown("---")
    
    # Version history
    render_version_history(protocol_name)
    
    # References
    st.markdown("---")
    st.markdown("### 📚 References")
    render_protocol_references(protocol_name)
    
    # Disclaimer
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def add_evidence_to_recommendation(
    text: str,
    level: str = "C",
    citations: Optional[List[int]] = None
) -> Dict[str, Any]:
    """
    Helper to create a recommendation dict with evidence.
    
    Args:
        text: Recommendation text
        level: Evidence level
        citations: Citation indices
        
    Returns:
        Dict with recommendation data
    """
    return {
        "text": text,
        "level": level,
        "citation_indices": citations or []
    }

