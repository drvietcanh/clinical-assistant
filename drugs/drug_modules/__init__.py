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
]

