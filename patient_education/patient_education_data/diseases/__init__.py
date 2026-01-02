"""
Patient Education Topics - Diseases
Combines all disease topics from specialty-specific files
"""

from .cardiovascular import CARDIOVASCULAR_TOPICS
from .dermatology import DERMATOLOGY_TOPICS
from .diabetes import DIABETES_TOPICS
from .gastrointestinal import GASTROINTESTINAL_TOPICS
from .hematology import HEMATOLOGY_TOPICS
from .infectious import INFECTIOUS_TOPICS
from .mental_health import MENTAL_HEALTH_TOPICS
from .metabolic import METABOLIC_TOPICS
from .neurological import NEUROLOGICAL_TOPICS
from .obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_TOPICS
from .ophthalmology import OPHTHALMOLOGY_TOPICS
from .other import OTHER_TOPICS
from .respiratory import RESPIRATORY_TOPICS
from .rheumatology import RHEUMATOLOGY_TOPICS

# Combine all disease topics
DISEASE_TOPICS = [
    *CARDIOVASCULAR_TOPICS,
    *DERMATOLOGY_TOPICS,
    *DIABETES_TOPICS,
    *GASTROINTESTINAL_TOPICS,
    *HEMATOLOGY_TOPICS,
    *INFECTIOUS_TOPICS,
    *MENTAL_HEALTH_TOPICS,
    *METABOLIC_TOPICS,
    *NEUROLOGICAL_TOPICS,
    *OBSTETRICS_GYNECOLOGY_TOPICS,
    *OPHTHALMOLOGY_TOPICS,
    *OTHER_TOPICS,
    *RESPIRATORY_TOPICS,
    *RHEUMATOLOGY_TOPICS,
]

__all__ = ['DISEASE_TOPICS']
