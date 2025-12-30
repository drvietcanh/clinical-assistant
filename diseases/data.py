"""
Disease Encyclopedia Database - Base Module
Disease class definition and utility functions
"""

from typing import List, Optional
from dataclasses import dataclass, field


@dataclass
class Disease:
    """Disease information"""
    id: str
    name: str
    name_vn: str  # Vietnamese name
    category: str  # Cardiology, Infectious, etc.
    definition: str = ""
    causes: List[str] = field(default_factory=list)
    symptoms: List[str] = field(default_factory=list)
    diagnosis: dict = field(default_factory=dict)  # {"criteria": [], "tests": [], "imaging": []}
    treatment: dict = field(default_factory=dict)  # {"general": "", "medications": [], "procedures": []}
    prevention: List[str] = field(default_factory=list)
    complications: List[str] = field(default_factory=list)
    related_scores: List[str] = field(default_factory=list)  # e.g., ["CURB-65", "PSI"]
    related_drugs: List[str] = field(default_factory=list)  # e.g., ["Amoxicillin", "Azithromycin"]
    related_protocols: List[str] = field(default_factory=list)  # e.g., ["pneumonia_treatment"]
    icd10_codes: List[str] = field(default_factory=list)  # e.g., ["J18.9", "J15.9"]


# Import diseases from specialty modules
from diseases.modules.infectious import INFECTIOUS_DISEASES
from diseases.modules.cardiology import CARDIOLOGY_DISEASES
from diseases.modules.respiratory import RESPIRATORY_DISEASES
from diseases.modules.gastroenterology import GASTROENTEROLOGY_DISEASES
from diseases.modules.endocrinology import ENDOCRINOLOGY_DISEASES
from diseases.modules.nephrology import NEPHROLOGY_DISEASES
from diseases.modules.neurology import NEUROLOGY_DISEASES
from diseases.modules.rheumatology import RHEUMATOLOGY_DISEASES
from diseases.modules.hematology import HEMATOLOGY_DISEASES
from diseases.modules.dermatology import DERMATOLOGY_DISEASES
from diseases.modules.psychiatry import PSYCHIATRY_DISEASES
from diseases.modules.emergency import EMERGENCY_DISEASES
from diseases.modules.oncology import ONCOLOGY_DISEASES
from diseases.modules.obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DISEASES
from diseases.modules.pediatrics import PEDIATRICS_DISEASES
from diseases.modules.urology import UROLOGY_DISEASES
from diseases.modules.ophthalmology import OPHTHALMOLOGY_DISEASES
from diseases.modules.ent import ENT_DISEASES
from diseases.modules.orthopedics import ORTHOPEDICS_DISEASES
from diseases.modules.critical_care import CRITICAL_CARE_DISEASES
from diseases.modules.allergy_immunology import ALLERGY_IMMUNOLOGY_DISEASES


# Combine all diseases into one database
DISEASES_DATABASE: List[Disease] = (
    INFECTIOUS_DISEASES +
    CARDIOLOGY_DISEASES +
    RESPIRATORY_DISEASES +
    GASTROENTEROLOGY_DISEASES +
    ENDOCRINOLOGY_DISEASES +
    NEPHROLOGY_DISEASES +
    NEUROLOGY_DISEASES +
    RHEUMATOLOGY_DISEASES +
    HEMATOLOGY_DISEASES +
    DERMATOLOGY_DISEASES +
    PSYCHIATRY_DISEASES +
    EMERGENCY_DISEASES +
    ONCOLOGY_DISEASES +
    OBSTETRICS_GYNECOLOGY_DISEASES +
    PEDIATRICS_DISEASES +
    UROLOGY_DISEASES +
    OPHTHALMOLOGY_DISEASES +
    ENT_DISEASES +
    ORTHOPEDICS_DISEASES +
    CRITICAL_CARE_DISEASES +
    ALLERGY_IMMUNOLOGY_DISEASES
)


# Category mapping (auto-generated from database)
def _generate_category_mapping() -> dict:
    """Generate category mapping from diseases database"""
    mapping = {}
    for disease in DISEASES_DATABASE:
        if disease.category not in mapping:
            mapping[disease.category] = []
        mapping[disease.category].append(disease.id)
    return mapping


CATEGORY_MAPPING = _generate_category_mapping()


def get_all_diseases() -> List[Disease]:
    """Get all diseases"""
    return DISEASES_DATABASE


def get_diseases_by_category(category: str) -> List[Disease]:
    """Get diseases filtered by category"""
    if not category or category == "All":
        return DISEASES_DATABASE
    return [d for d in DISEASES_DATABASE if d.category == category]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(d.category for d in DISEASES_DATABASE)
    return sorted(list(categories))
