"""
Patient Education Topics - All Topics Aggregator
Combines all topics from category-specific files
"""

from .disease import DISEASE_TOPICS
from .medication import MEDICATION_TOPICS
from .lifestyle import LIFESTYLE_TOPICS
from .procedure import PROCEDURE_TOPICS

# Combine all topics
ALL_PATIENT_EDUCATION_TOPICS = (
    DISEASE_TOPICS +
    MEDICATION_TOPICS +
    LIFESTYLE_TOPICS +
    PROCEDURE_TOPICS
)

__all__ = ['ALL_PATIENT_EDUCATION_TOPICS']

