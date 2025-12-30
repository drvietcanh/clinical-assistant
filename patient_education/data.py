"""
Patient Education Content Database
Educational materials for patients in simple, easy-to-understand language

NOTE: Topics have been moved to patient_education_data submodule for better organization.
This file now imports from the modular structure.
"""

from typing import List
from .models import PatientEducationTopic
from .patient_education_data.all_topics import ALL_PATIENT_EDUCATION_TOPICS

# Backward compatibility: Export the database
PATIENT_EDUCATION_DATABASE: List[PatientEducationTopic] = ALL_PATIENT_EDUCATION_TOPICS

# Legacy database (kept for reference, now using modular structure)
# All topics are now in patient_education_data/ subdirectory:
# - disease.py: Disease-related topics (10 topics)
# - medication.py: Medication-related topics (6 topics)
# - lifestyle.py: Lifestyle-related topics (5 topics)
# - procedure.py: Procedure-related topics (3 topics)
# - all_topics.py: Aggregates all topics


def get_all_topics() -> List[PatientEducationTopic]:
    """Get all patient education topics"""
    return PATIENT_EDUCATION_DATABASE


def get_topics_by_category(category: str) -> List[PatientEducationTopic]:
    """Get topics filtered by category"""
    if not category or category == "All":
        return PATIENT_EDUCATION_DATABASE
    return [t for t in PATIENT_EDUCATION_DATABASE if t.category == category]


def get_category_list() -> List[str]:
    """Get list of all categories"""
    categories = set(t.category for t in PATIENT_EDUCATION_DATABASE)
    return sorted(list(categories))
