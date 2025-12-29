"""
Patient Education Materials Module
Educational materials for patients in simple language
"""

from patient_education.data import (
    PATIENT_EDUCATION_DATABASE,
    get_all_topics,
    get_topics_by_category,
    get_category_list
)

from patient_education.display import (
    render_patient_education_content,
    get_patient_education_pdf
)

__all__ = [
    'PATIENT_EDUCATION_DATABASE',
    'get_all_topics',
    'get_topics_by_category',
    'get_category_list',
    'render_patient_education_content',
    'get_patient_education_pdf',
]

