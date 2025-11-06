"""
Drug Modules Package
All drug data modules organized by therapeutic category
"""

from .cardiovascular import CARDIOVASCULAR_DRUGS
from .diabetes import DIABETES_DRUGS
from .gastrointestinal import GASTROINTESTINAL_DRUGS
from .analgesics import ANALGESICS_DRUGS
from .respiratory import RESPIRATORY_DRUGS
from .neurological import NEUROLOGICAL_DRUGS
from .hematology import HEMATOLOGY_DRUGS
from .supportive import SUPPORTIVE_DRUGS
from .antimicrobial import ANTIMICROBIAL_DRUGS
from .metabolic import METABOLIC_DRUGS
from .oncology import ONCOLOGY_DRUGS
from .emergency import EMERGENCY_DRUGS
from .other import OTHER_DRUGS

# Import split modules from other.py
from .cardiovascular_other import CARDIOVASCULAR_OTHER_DRUGS
from .infectious_other import INFECTIOUS_OTHER_DRUGS
from .psychiatry_other import PSYCHIATRY_OTHER_DRUGS
from .endocrinology_other import ENDOCRINOLOGY_OTHER_DRUGS
from .miscellaneous import MISCELLANEOUS_DRUGS

__all__ = [
    'CARDIOVASCULAR_DRUGS',
    'DIABETES_DRUGS',
    'GASTROINTESTINAL_DRUGS',
    'ANALGESICS_DRUGS',
    'RESPIRATORY_DRUGS',
    'NEUROLOGICAL_DRUGS',
    'HEMATOLOGY_DRUGS',
    'SUPPORTIVE_DRUGS',
    'ANTIMICROBIAL_DRUGS',
    'METABOLIC_DRUGS',
    'ONCOLOGY_DRUGS',
    'EMERGENCY_DRUGS',
    'OTHER_DRUGS',
    # Split modules from other.py
    'CARDIOVASCULAR_OTHER_DRUGS',
    'INFECTIOUS_OTHER_DRUGS',
    'PSYCHIATRY_OTHER_DRUGS',
    'ENDOCRINOLOGY_OTHER_DRUGS',
    'MISCELLANEOUS_DRUGS',
]

