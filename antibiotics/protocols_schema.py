"""
Antibiotic Protocols Schema
Cấu trúc dữ liệu chuẩn hóa cho phác đồ kháng sinh
Hỗ trợ infection_site, severity, setting, regimens, guideline_source, year
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum
from .vietnamese_terms import (
    INFECTION_SITE_VI, SEVERITY_VI, SETTING_VI, 
    REGIMEN_TYPE_VI, RECOMMENDATION_LEVEL_VI
)


class InfectionSite(str, Enum):
    """Site of infection"""
    CAP = "CAP"  # Community-acquired pneumonia
    HAP = "HAP"  # Hospital-acquired pneumonia
    VAP = "VAP"  # Ventilator-associated pneumonia
    UTI = "UTI"  # Urinary tract infection
    SSTI = "SSTI"  # Skin and soft tissue infection
    CNS = "CNS"  # Central nervous system infection
    IAI = "IAI"  # Intra-abdominal infection
    BACTEREMIA = "BACTEREMIA"  # Bacteremia
    SEPSIS = "SEPSIS"  # Sepsis
    OSTEOMYELITIS = "OSTEOMYELITIS"  # Bone infection
    ENDOCARDITIS = "ENDOCARDITIS"  # Endocarditis
    
    def get_vietnamese_label(self) -> str:
        """Get Vietnamese label for this infection site"""
        return INFECTION_SITE_VI.get(self.value, self.value)


class Severity(str, Enum):
    """Infection severity"""
    MILD = "MILD"
    MODERATE = "MODERATE"
    SEVERE = "SEVERE"
    ICU = "ICU"  # ICU-level care
    
    def get_vietnamese_label(self) -> str:
        """Get Vietnamese label for this severity"""
        return SEVERITY_VI.get(self.value, self.value)


class Setting(str, Enum):
    """Clinical setting"""
    OPD = "OPD"  # Outpatient
    WARD = "WARD"  # Inpatient ward
    ICU = "ICU"  # Intensive care unit
    
    def get_vietnamese_label(self) -> str:
        """Get Vietnamese label for this setting"""
        return SETTING_VI.get(self.value, self.value)


class RecommendationLevel(str, Enum):
    """Evidence-based recommendation level"""
    STRONG = "STRONG"
    WEAK = "WEAK"
    CONDITIONAL = "CONDITIONAL"
    
    def get_vietnamese_label(self) -> str:
        """Get Vietnamese label for this recommendation level"""
        return RECOMMENDATION_LEVEL_VI.get(self.value, self.value)


class EvidenceLevel(str, Enum):
    """Evidence quality level (A/B/C/D)"""
    A = "A"  # High-quality evidence (RCTs, meta-analyses)
    B = "B"  # Moderate-quality evidence (observational studies)
    C = "C"  # Low-quality evidence (case series, expert opinion)
    D = "D"  # Very low-quality evidence
    
    def get_vietnamese_label(self) -> str:
        """Get Vietnamese label for evidence level"""
        labels = {
            "A": "Chất lượng cao (RCT, meta-analysis)",
            "B": "Chất lượng trung bình (Nghiên cứu quan sát)",
            "C": "Chất lượng thấp (Case series, ý kiến chuyên gia)",
            "D": "Chất lượng rất thấp"
        }
        return labels.get(self.value, self.value)
    
    def get_color(self) -> str:
        """Get color for evidence level badge"""
        colors = {
            "A": "#4caf50",  # Green
            "B": "#2196f3",  # Blue
            "C": "#ff9800",  # Orange
            "D": "#f44336"   # Red
        }
        return colors.get(self.value, "#666")


class RegimenType(str, Enum):
    """Type of regimen"""
    FIRST_LINE = "FIRST_LINE"
    ALTERNATIVE = "ALTERNATIVE"
    RESCUE = "RESCUE"
    STEP_DOWN = "STEP_DOWN"  # IV to PO switch
    
    def get_vietnamese_label(self) -> str:
        """Get Vietnamese label for this regimen type"""
        return REGIMEN_TYPE_VI.get(self.value, self.value)


@dataclass
class DrugDose:
    """Drug dosing information"""
    drug_name: str
    dose: str  # e.g., "2g", "15-20 mg/kg"
    route: str  # "IV", "PO", "IM"
    frequency: str  # "q8h", "q12h", "once daily"
    duration: Optional[str] = None  # e.g., "7-10 days", "until afebrile 48h"
    notes: Optional[str] = None  # Special notes


@dataclass
class Regimen:
    """Antibiotic regimen"""
    regimen_type: RegimenType
    drugs: List[DrugDose]
    indication: str  # Brief indication
    rationale: Optional[str] = None  # Why this regimen
    recommendation_level: Optional[RecommendationLevel] = None
    evidence_level: Optional[EvidenceLevel] = None  # Evidence quality (A/B/C/D)
    special_populations: Optional[Dict[str, str]] = None  # e.g., {"pregnancy": "Safe", "renal": "Adjust if CrCl <30"}
    warnings: Optional[List[str]] = None  # e.g., ["QT prolongation risk", "C. difficile risk"]
    step_down_options: Optional[List[DrugDose]] = None  # IV to PO options


@dataclass
class AntibioticProtocol:
    """Complete antibiotic protocol for a specific infection scenario"""
    infection_site: InfectionSite
    severity: Severity
    setting: Setting
    title: str  # e.g., "CAP Non-severe (Outpatient)"
    description: Optional[str] = None
    regimens: List[Regimen] = field(default_factory=list)
    guideline_source: Optional[str] = None  # e.g., "IDSA/ATS 2019"
    guideline_year: Optional[int] = None
    last_reviewed: Optional[str] = None  # Date string
    notes: Optional[List[str]] = None  # General notes
    risk_factors: Optional[List[str]] = None  # e.g., ["MRSA risk", "Pseudomonas risk"]


@dataclass
class ProtocolCollection:
    """Collection of antibiotic protocols"""
    protocols: List[AntibioticProtocol] = field(default_factory=list)
    
    def get_by_infection_site(self, site: InfectionSite) -> List[AntibioticProtocol]:
        """Get protocols by infection site"""
        return [p for p in self.protocols if p.infection_site == site]
    
    def get_by_severity(self, severity: Severity) -> List[AntibioticProtocol]:
        """Get protocols by severity"""
        return [p for p in self.protocols if p.severity == severity]
    
    def get_by_setting(self, setting: Setting) -> List[AntibioticProtocol]:
        """Get protocols by setting"""
        return [p for p in self.protocols if p.setting == setting]
    
    def search(self, 
               site: Optional[InfectionSite] = None,
               severity: Optional[Severity] = None,
               setting: Optional[Setting] = None) -> List[AntibioticProtocol]:
        """Search protocols with filters"""
        results = self.protocols
        
        if site:
            results = [p for p in results if p.infection_site == site]
        if severity:
            results = [p for p in results if p.severity == severity]
        if setting:
            results = [p for p in results if p.setting == setting]
        
        return results


# Example protocol structure (will be populated with actual data)
EXAMPLE_PROTOCOLS = ProtocolCollection()
