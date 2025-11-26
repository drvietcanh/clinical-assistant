"""
Enhanced References Component
Display references with GRADE system, PubMed links, and evidence levels
"""

import streamlit as st
from typing import List, Dict, Any, Optional
from datetime import datetime


# GRADE Evidence Levels
GRADE_HIGH = "High"
GRADE_MODERATE = "Moderate"
GRADE_LOW = "Low"
GRADE_VERY_LOW = "Very Low"

# Evidence Level Mapping (AHA/ACC style)
EVIDENCE_LEVEL_I = "I"  # High quality evidence
EVIDENCE_LEVEL_IIA = "IIa"  # Moderate quality evidence
EVIDENCE_LEVEL_IIB = "IIb"  # Low quality evidence
EVIDENCE_LEVEL_III = "III"  # Very low quality evidence

# Strength of Recommendation
STRENGTH_STRONG = "Strong"
STRENGTH_MODERATE = "Moderate"
STRENGTH_WEAK = "Weak"


def get_evidence_level_info(level: str) -> Dict[str, Any]:
    """
    Get evidence level information
    
    Args:
        level: Evidence level (I, IIa, IIb, III or High, Moderate, Low, Very Low)
    
    Returns:
        Dict with color, label, description
    """
    level_map = {
        # GRADE system
        GRADE_HIGH: {
            "color": "#28a745",
            "label": "High Quality",
            "description": "Further research is very unlikely to change our confidence in the estimate of effect."
        },
        GRADE_MODERATE: {
            "color": "#17a2b8",
            "label": "Moderate Quality",
            "description": "Further research is likely to have an important impact on our confidence."
        },
        GRADE_LOW: {
            "color": "#ffc107",
            "label": "Low Quality",
            "description": "Further research is very likely to have an important impact."
        },
        GRADE_VERY_LOW: {
            "color": "#dc3545",
            "label": "Very Low Quality",
            "description": "Any estimate of effect is very uncertain."
        },
        # AHA/ACC style
        EVIDENCE_LEVEL_I: {
            "color": "#28a745",
            "label": "Level I (High Quality)",
            "description": "Multiple randomized trials or meta-analyses"
        },
        EVIDENCE_LEVEL_IIA: {
            "color": "#17a2b8",
            "label": "Level IIa (Moderate Quality)",
            "description": "Single randomized trial or nonrandomized studies"
        },
        EVIDENCE_LEVEL_IIB: {
            "color": "#ffc107",
            "label": "Level IIb (Low Quality)",
            "description": "Single well-designed nonrandomized study"
        },
        EVIDENCE_LEVEL_III: {
            "color": "#dc3545",
            "label": "Level III (Very Low Quality)",
            "description": "Expert opinion, case studies, or standard of care"
        }
    }
    
    return level_map.get(level, {
        "color": "#6c757d",
        "label": level,
        "description": ""
    })


def format_apa_citation(
    authors: str,
    year: int,
    title: str,
    journal: str,
    volume: Optional[str] = None,
    issue: Optional[str] = None,
    pages: Optional[str] = None,
    doi: Optional[str] = None,
    pmid: Optional[str] = None
) -> str:
    """
    Format citation in APA style
    
    Args:
        authors: Author names (e.g., "Espinel CH" or "Levey AS, Stevens LA, Schmid CH")
        year: Publication year
        title: Article title
        journal: Journal name
        volume: Volume number
        issue: Issue number
        pages: Page numbers
        doi: DOI
        pmid: PubMed ID
    
    Returns:
        Formatted APA citation string
    """
    # Format authors
    if "," in authors:
        # Multiple authors
        author_list = [a.strip() for a in authors.split(",")]
        if len(author_list) > 6:
            formatted_authors = ", ".join(author_list[:6]) + ", et al."
        else:
            formatted_authors = ", ".join(author_list[:-1]) + ", & " + author_list[-1] if len(author_list) > 1 else author_list[0]
    else:
        formatted_authors = authors
    
    # Format journal
    journal_italic = f"*{journal}*"
    
    # Build citation
    citation = f"{formatted_authors} ({year}). {title}. {journal_italic}"
    
    if volume:
        citation += f", {volume}"
        if issue:
            citation += f"({issue})"
    
    if pages:
        citation += f", {pages}"
    
    citation += "."
    
    # Add identifiers
    if doi:
        citation += f" https://doi.org/{doi}"
    elif pmid:
        citation += f" [PMID: {pmid}]"
    
    return citation


def generate_pubmed_link(pmid: str) -> str:
    """
    Generate PubMed link from PMID
    
    Args:
        pmid: PubMed ID
    
    Returns:
        PubMed URL
    """
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def generate_pubmed_search_link(query: str) -> str:
    """
    Generate PubMed search link
    
    Args:
        query: Search query
    
    Returns:
        PubMed search URL
    """
    from urllib.parse import quote
    return f"https://pubmed.ncbi.nlm.nih.gov/?term={quote(query)}"


def render_reference_item(
    reference: Dict[str, Any],
    show_evidence_level: bool = True,
    show_links: bool = True
) -> None:
    """
    Render a single reference item
    
    Args:
        reference: Reference dictionary with keys:
            - title: Article title
            - authors: Author names
            - journal: Journal name
            - year: Publication year
            - volume: Volume (optional)
            - issue: Issue (optional)
            - pages: Pages (optional)
            - doi: DOI (optional)
            - pmid: PubMed ID (optional)
            - evidence_level: Evidence level (optional)
            - strength: Strength of recommendation (optional)
            - type: Reference type ("primary", "guideline", "review", etc.)
        show_evidence_level: Whether to show evidence level badge
        show_links: Whether to show PubMed/DOI links
    """
    # Get reference type icon
    type_icons = {
        "primary": "📚",
        "guideline": "📋",
        "review": "📖",
        "meta-analysis": "📊",
        "case": "📄",
        "other": "📑"
    }
    icon = type_icons.get(reference.get("type", "other"), "📚")
    
    # Evidence level badge
    evidence_badge = ""
    if show_evidence_level and "evidence_level" in reference:
        level_info = get_evidence_level_info(reference["evidence_level"])
        evidence_badge = f"""
        <span style="
            background: {level_info['color']}15;
            border: 1px solid {level_info['color']};
            color: {level_info['color']};
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            margin-left: 8px;
        ">{level_info['label']}</span>
        """
    
    # Format citation
    if "citation" in reference:
        citation = reference["citation"]
    else:
        citation = format_apa_citation(
            authors=reference.get("authors", ""),
            year=reference.get("year", ""),
            title=reference.get("title", ""),
            journal=reference.get("journal", ""),
            volume=reference.get("volume"),
            issue=reference.get("issue"),
            pages=reference.get("pages"),
            doi=reference.get("doi"),
            pmid=reference.get("pmid")
        )
    
    # Links
    links_html = ""
    if show_links:
        links = []
        
        if "pmid" in reference:
            pubmed_url = generate_pubmed_link(reference["pmid"])
            links.append(f'<a href="{pubmed_url}" target="_blank" style="text-decoration: none; color: #0066cc;">🔗 PubMed</a>')
        
        if "doi" in reference:
            doi_url = f"https://doi.org/{reference['doi']}"
            links.append(f'<a href="{doi_url}" target="_blank" style="text-decoration: none; color: #0066cc;">📄 Full Text</a>')
        
        if "url" in reference:
            links.append(f'<a href="{reference[\"url\"]}" target="_blank" style="text-decoration: none; color: #0066cc;">🔗 Link</a>')
        
        if "pdf_url" in reference:
            links.append(f'<a href="{reference[\"pdf_url\"]}" target="_blank" style="text-decoration: none; color: #0066cc;">📥 Download PDF</a>')
        
        if links:
            links_html = f"""
            <div style="margin-top: 8px;">
                {' | '.join(links)}
            </div>
            """
    
    # Strength of recommendation
    strength_badge = ""
    if "strength" in reference:
        strength_colors = {
            STRENGTH_STRONG: "#28a745",
            STRENGTH_MODERATE: "#ffc107",
            STRENGTH_WEAK: "#dc3545"
        }
        strength_color = strength_colors.get(reference["strength"], "#6c757d")
        strength_badge = f"""
        <span style="
            background: {strength_color}15;
            border: 1px solid {strength_color};
            color: {strength_color};
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: bold;
            margin-left: 8px;
        ">Strength: {reference['strength']}</span>
        """
    
    # Render
    reference_html = f"""
    <div style="
        padding: 1rem;
        margin: 0.75rem 0;
        background: #f8f9fa;
        border-left: 4px solid #007bff;
        border-radius: 4px;
    ">
        <div style="font-size: 1rem; margin-bottom: 0.5rem;">
            {icon} <strong>{reference.get('title', 'Reference')}</strong>
            {evidence_badge}
            {strength_badge}
        </div>
        <div style="font-size: 0.9rem; color: #495057; line-height: 1.6;">
            {citation}
        </div>
        {links_html}
    </div>
    """
    
    st.markdown(reference_html, unsafe_allow_html=True)


def render_references_section(
    references: List[Dict[str, Any]],
    title: str = "📚 Tài liệu tham khảo",
    last_updated: Optional[str] = None,
    show_evidence_level: bool = True,
    show_links: bool = True,
    grouped: bool = True
) -> None:
    """
    Render a complete references section
    
    Args:
        references: List of reference dictionaries
        title: Section title
        last_updated: Last updated date (YYYY-MM-DD format)
        show_evidence_level: Whether to show evidence level badges
        show_links: Whether to show PubMed/DOI links
        grouped: Whether to group by type
    """
    st.markdown("---")
    
    with st.expander(title, expanded=False):
        if not references:
            st.info("Không có tài liệu tham khảo.")
            return
        
        # Group references by type if requested
        if grouped:
            grouped_refs = {}
            for ref in references:
                ref_type = ref.get("type", "other")
                if ref_type not in grouped_refs:
                    grouped_refs[ref_type] = []
                grouped_refs[ref_type].append(ref)
            
            # Render by group
            type_labels = {
                "primary": "📚 Primary Reference",
                "guideline": "📋 Guidelines",
                "review": "📖 Review Articles",
                "meta-analysis": "📊 Meta-Analyses",
                "case": "📄 Case Reports",
                "other": "📑 Other References"
            }
            
            for ref_type, refs in grouped_refs.items():
                if refs:
                    label = type_labels.get(ref_type, "📑 References")
                    st.markdown(f"### {label}")
                    
                    for ref in refs:
                        render_reference_item(
                            ref,
                            show_evidence_level=show_evidence_level,
                            show_links=show_links
                        )
        else:
            # Render all references
            for ref in references:
                render_reference_item(
                    ref,
                    show_evidence_level=show_evidence_level,
                    show_links=show_links
                )
        
        # Last updated
        if last_updated:
            st.markdown("---")
            st.caption(f"🔄 **Last Updated:** {last_updated}")


def render_evidence_summary(
    references: List[Dict[str, Any]]
) -> None:
    """
    Render evidence level summary
    
    Args:
        references: List of reference dictionaries
    """
    if not references:
        return
    
    # Count by evidence level
    level_counts = {}
    for ref in references:
        if "evidence_level" in ref:
            level = ref["evidence_level"]
            level_counts[level] = level_counts.get(level, 0) + 1
    
    if not level_counts:
        return
    
    st.markdown("### 📊 Evidence Summary")
    
    cols = st.columns(len(level_counts))
    for idx, (level, count) in enumerate(level_counts.items()):
        level_info = get_evidence_level_info(level)
        with cols[idx]:
            st.metric(
                level_info["label"],
                count,
                delta=None
            )

