"""
Navigation Configuration
Reorganized navigation structure with categories and sub-modules
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class NavigationCategory:
    """Navigation category with sub-modules"""
    id: str
    title: str
    icon: str
    description: str
    module_ids: List[str]
    color: str
    border: str


# Navigation structure with 5-6 main categories
NAVIGATION_CATEGORIES = {
    "calculators_scores": NavigationCategory(
        id="calculators_scores",
        title="📊 Calculators & Scores",
        icon="📊",
        description="Clinical scores, lab calculators, and TDM",
        module_ids=["scores", "labs", "tdm"],
        color="linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%)",
        border="#1976d2"
    ),
    "drugs_dosing": NavigationCategory(
        id="drugs_dosing",
        title="💊 Drugs & Dosing",
        icon="💊",
        description="Drug database, antibiotics, pill identifier, interactions",
        module_ids=["drug_database", "antibiotics", "pill_identifier"],
        color="linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%)",
        border="#4caf50"
    ),
    "critical_care": NavigationCategory(
        id="critical_care",
        title="🫁 Critical Care",
        icon="🫁",
        description="Ventilator, fluids, vasopressors, protocols, guidelines",
        module_ids=["critical_care", "ventilator", "protocols", "guidelines_tracker"],
        color="linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%)",
        border="#ff6f00"
    ),
    "diagnosis_reference": NavigationCategory(
        id="diagnosis_reference",
        title="🩺 Diagnosis & Reference",
        icon="🩺",
        description="Differential diagnosis, disease encyclopedia, symptom checker, ICD-10, articles",
        module_ids=["diagnosis", "disease_encyclopedia", "icd10_lookup", "in_depth_articles"],
        color="linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%)",
        border="#f44336"
    ),
    "clinical_tools": NavigationCategory(
        id="clinical_tools",
        title="💉 Clinical Tools",
        icon="💉",
        description="Vaccination, decision support, patient education",
        module_ids=["vaccination", "phase2_features", "patient_education"],
        color="linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%)",
        border="#0288d1"
    ),
}


def get_category_by_module_id(module_id: str) -> Optional[NavigationCategory]:
    """Get navigation category for a module ID"""
    for category in NAVIGATION_CATEGORIES.values():
        if module_id in category.module_ids:
            return category
    return None


def get_all_categories() -> Dict[str, NavigationCategory]:
    """Get all navigation categories"""
    return NAVIGATION_CATEGORIES


def get_modules_by_category(category_id: str) -> List[str]:
    """Get module IDs for a category"""
    category = NAVIGATION_CATEGORIES.get(category_id)
    if category:
        return category.module_ids
    return []


def get_category_info(category_id: str) -> Optional[NavigationCategory]:
    """Get category information"""
    return NAVIGATION_CATEGORIES.get(category_id)


# Export
__all__ = [
    'NavigationCategory',
    'NAVIGATION_CATEGORIES',
    'get_category_by_module_id',
    'get_all_categories',
    'get_modules_by_category',
    'get_category_info',
]

