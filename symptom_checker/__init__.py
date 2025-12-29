"""
Symptom Checker Module
Advanced symptom analysis and diagnosis suggestion
"""

from symptom_checker.data import (
    SYMPTOM_DATABASE,
    get_all_symptoms,
    get_symptoms_by_category
)

from symptom_checker.algorithm import (
    analyze_symptoms,
    get_diagnosis_suggestions,
    calculate_severity,
    check_urgency
)

__all__ = [
    'SYMPTOM_DATABASE',
    'get_all_symptoms',
    'get_symptoms_by_category',
    'analyze_symptoms',
    'get_diagnosis_suggestions',
    'calculate_severity',
    'check_urgency',
]

