"""
Evidence Levels Management
Evidence-based medicine levels (A/B/C) for recommendations
"""

from typing import Dict, Optional, List
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class EvidenceLevel(Enum):
    """Evidence levels for recommendations"""
    A = "A"  # High-quality evidence
    B = "B"  # Moderate-quality evidence
    C = "C"  # Low-quality evidence or expert opinion
    D = "D"  # Very low-quality evidence


@dataclass
class EvidenceMetadata:
    """Evidence metadata for a recommendation"""
    level: EvidenceLevel
    citation: Optional[str] = None
    doi: Optional[str] = None
    pubmed_id: Optional[str] = None
    last_reviewed: Optional[str] = None
    version: Optional[str] = None
    synopsis: Optional[str] = None


def get_evidence_level_description(level: EvidenceLevel) -> str:
    """
    Get description for evidence level
    
    Args:
        level: Evidence level
    
    Returns:
        Description string
    """
    descriptions = {
        EvidenceLevel.A: "Mức độ A: Bằng chứng chất lượng cao (RCTs, meta-analyses)",
        EvidenceLevel.B: "Mức độ B: Bằng chứng chất lượng trung bình (cohort studies, case-control)",
        EvidenceLevel.C: "Mức độ C: Bằng chứng chất lượng thấp hoặc ý kiến chuyên gia",
        EvidenceLevel.D: "Mức độ D: Bằng chứng chất lượng rất thấp",
    }
    return descriptions.get(level, "Không xác định")


def get_evidence_level_color(level: EvidenceLevel) -> str:
    """
    Get color for evidence level badge
    
    Args:
        level: Evidence level
    
    Returns:
        Color hex code
    """
    colors = {
        EvidenceLevel.A: "#4caf50",  # Green
        EvidenceLevel.B: "#ff9800",   # Orange
        EvidenceLevel.C: "#f44336",  # Red
        EvidenceLevel.D: "#9e9e9e",  # Gray
    }
    return colors.get(level, "#757575")


def format_citation(metadata: EvidenceMetadata) -> str:
    """
    Format citation string
    
    Args:
        metadata: Evidence metadata
    
    Returns:
        Formatted citation string
    """
    parts = []
    
    if metadata.citation:
        parts.append(metadata.citation)
    
    if metadata.doi:
        parts.append(f"DOI: {metadata.doi}")
    
    if metadata.pubmed_id:
        parts.append(f"PubMed: {metadata.pubmed_id}")
    
    if metadata.last_reviewed:
        parts.append(f"Last reviewed: {metadata.last_reviewed}")
    
    return " | ".join(parts) if parts else "No citation available"


def create_evidence_metadata(
    level: str,
    citation: Optional[str] = None,
    doi: Optional[str] = None,
    pubmed_id: Optional[str] = None,
    last_reviewed: Optional[str] = None,
    version: Optional[str] = None,
    synopsis: Optional[str] = None
) -> EvidenceMetadata:
    """
    Create evidence metadata
    
    Args:
        level: Evidence level (A, B, C, or D)
        citation: Citation text
        doi: DOI link
        pubmed_id: PubMed ID
        last_reviewed: Last reviewed date
        version: Version number
        synopsis: Evidence synopsis
    
    Returns:
        EvidenceMetadata object
    """
    # Convert string to EvidenceLevel
    level_enum = EvidenceLevel.A
    if level.upper() == "A":
        level_enum = EvidenceLevel.A
    elif level.upper() == "B":
        level_enum = EvidenceLevel.B
    elif level.upper() == "C":
        level_enum = EvidenceLevel.C
    elif level.upper() == "D":
        level_enum = EvidenceLevel.D
    
    return EvidenceMetadata(
        level=level_enum,
        citation=citation,
        doi=doi,
        pubmed_id=pubmed_id,
        last_reviewed=last_reviewed or datetime.now().strftime("%Y-%m-%d"),
        version=version,
        synopsis=synopsis
    )


# Export
__all__ = [
    'EvidenceLevel',
    'EvidenceMetadata',
    'get_evidence_level_description',
    'get_evidence_level_color',
    'format_citation',
    'create_evidence_metadata',
]

