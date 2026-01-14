"""
Evidence Grading System
Level of Evidence (A/B/C) and Strength of Recommendation (Strong/Weak)
"""

from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class EvidenceLevel:
    """Level of evidence (A/B/C)"""
    level: str  # "A", "B", "C"
    description: str
    description_vn: str
    color: str
    bg_color: str
    icon: str


EVIDENCE_LEVELS: Dict[str, EvidenceLevel] = {
    "A": EvidenceLevel(
        level="A",
        description="High-quality evidence",
        description_vn="Bằng chứng chất lượng cao",
        color="#28a745",  # Green
        bg_color="#d4edda",  # Light green
        icon="🟢"
    ),
    "B": EvidenceLevel(
        level="B",
        description="Moderate-quality evidence",
        description_vn="Bằng chứng chất lượng trung bình",
        color="#ffc107",  # Yellow/Orange
        bg_color="#fff3cd",  # Light yellow
        icon="🟡"
    ),
    "C": EvidenceLevel(
        level="C",
        description="Low-quality evidence",
        description_vn="Bằng chứng chất lượng thấp",
        color="#dc3545",  # Red
        bg_color="#f8d7da",  # Light red
        icon="🔴"
    )
}


@dataclass
class RecommendationStrength:
    """Strength of recommendation (Strong/Weak)"""
    strength: str  # "Strong", "Weak"
    description: str
    description_vn: str
    color: str
    bg_color: str
    icon: str


RECOMMENDATION_STRENGTHS: Dict[str, RecommendationStrength] = {
    "Strong": RecommendationStrength(
        strength="Strong",
        description="Strong recommendation",
        description_vn="Khuyến nghị mạnh",
        color="#007bff",  # Blue
        bg_color="#cfe2ff",  # Light blue
        icon="💪"
    ),
    "Weak": RecommendationStrength(
        strength="Weak",
        description="Weak recommendation",
        description_vn="Khuyến nghị yếu",
        color="#6c757d",  # Gray
        bg_color="#e9ecef",  # Light gray
        icon="🤏"
    )
}


@dataclass
class EvidenceGrade:
    """Complete evidence grade"""
    level: str  # "A", "B", "C"
    strength: str  # "Strong", "Weak"
    source: Optional[str] = None  # Guideline source (e.g., "SCCM 2021")
    year: Optional[int] = None  # Publication year
    notes: Optional[str] = None  # Additional notes
    
    def __post_init__(self):
        """Validate evidence grade"""
        if self.level not in EVIDENCE_LEVELS:
            raise ValueError(f"Invalid evidence level: {self.level}. Must be A, B, or C")
        if self.strength not in RECOMMENDATION_STRENGTHS:
            raise ValueError(f"Invalid recommendation strength: {self.strength}. Must be Strong or Weak")
    
    def get_level_info(self) -> EvidenceLevel:
        """Get evidence level information"""
        return EVIDENCE_LEVELS[self.level]
    
    def get_strength_info(self) -> RecommendationStrength:
        """Get recommendation strength information"""
        return RECOMMENDATION_STRENGTHS[self.strength]
    
    def get_display_text(self) -> str:
        """Get display text for evidence grade"""
        level_info = self.get_level_info()
        strength_info = self.get_strength_info()
        
        text = f"{level_info.icon} Level {self.level} ({strength_info.description_vn})"
        if self.source:
            text += f" - {self.source}"
        if self.year:
            text += f" {self.year}"
        
        return text


# Common evidence grades for quick reference
COMMON_EVIDENCE_GRADES = {
    "high_strong": EvidenceGrade(level="A", strength="Strong"),
    "high_weak": EvidenceGrade(level="A", strength="Weak"),
    "moderate_strong": EvidenceGrade(level="B", strength="Strong"),
    "moderate_weak": EvidenceGrade(level="B", strength="Weak"),
    "low_strong": EvidenceGrade(level="C", strength="Strong"),
    "low_weak": EvidenceGrade(level="C", strength="Weak"),
}


def create_evidence_grade(
    level: str,
    strength: str,
    source: Optional[str] = None,
    year: Optional[int] = None,
    notes: Optional[str] = None
) -> EvidenceGrade:
    """
    Create an EvidenceGrade instance
    
    Args:
        level: Evidence level ("A", "B", or "C")
        strength: Recommendation strength ("Strong" or "Weak")
        source: Guideline source (optional)
        year: Publication year (optional)
        notes: Additional notes (optional)
    
    Returns:
        EvidenceGrade instance
    """
    return EvidenceGrade(
        level=level,
        strength=strength,
        source=source,
        year=year,
        notes=notes
    )
