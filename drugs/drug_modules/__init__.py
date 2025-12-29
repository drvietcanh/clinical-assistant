"""
Drug Modules Package
All drug data modules organized by therapeutic category
Reorganized for better access and statistics (666 drugs total)
"""

# Main therapeutic categories (reorganized and merged)
from .cardiovascular import CARDIOVASCULAR_DRUGS  # Includes cardiovascular_other
from .diabetes import DIABETES_DRUGS
from .gastrointestinal import GASTROINTESTINAL_DRUGS
from .analgesics import ANALGESICS_DRUGS
from .respiratory import RESPIRATORY_DRUGS
from .neurological import NEUROLOGICAL_DRUGS  # Includes psychiatry_other
from .hematology import HEMATOLOGY_DRUGS
from .supportive import SUPPORTIVE_DRUGS
from .antimicrobial import ANTIMICROBIAL_DRUGS  # Includes infectious_other
from .metabolic import METABOLIC_DRUGS
from .endocrinology import ENDOCRINOLOGY_DRUGS  # Renamed from endocrinology_other
from .oncology import ONCOLOGY_DRUGS
from .emergency import EMERGENCY_DRUGS
from .urology import UROLOGY_DRUGS
from .dermatology import DERMATOLOGY_DRUGS
from .ophthalmology import OPHTHALMOLOGY_DRUGS
from .obstetrics_gynecology import OBSTETRICS_GYNECOLOGY_DRUGS
from .ent_oral_nasal_combinations import ENT_ORAL_NASAL_COMBINATIONS_DRUGS
from .miscellaneous import MISCELLANEOUS_DRUGS

# Backward compatibility - keep old imports but they point to merged modules
# These are now included in the main modules above
from .cardiovascular_other import CARDIOVASCULAR_OTHER_DRUGS  # Deprecated: use CARDIOVASCULAR_DRUGS
from .infectious_other import INFECTIOUS_OTHER_DRUGS  # Deprecated: use ANTIMICROBIAL_DRUGS
from .psychiatry_other import PSYCHIATRY_OTHER_DRUGS  # Deprecated: use NEUROLOGICAL_DRUGS
from .endocrinology_other import ENDOCRINOLOGY_OTHER_DRUGS  # Deprecated: use ENDOCRINOLOGY_DRUGS
from .other import OTHER_DRUGS  # Deprecated: use individual modules

__all__ = [
    # Main organized modules (use these)
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
    'ENDOCRINOLOGY_DRUGS',
    'ONCOLOGY_DRUGS',
    'EMERGENCY_DRUGS',
    'UROLOGY_DRUGS',
    'DERMATOLOGY_DRUGS',
    'OPHTHALMOLOGY_DRUGS',
    'OBSTETRICS_GYNECOLOGY_DRUGS',
    'ENT_ORAL_NASAL_COMBINATIONS_DRUGS',
    'MISCELLANEOUS_DRUGS',
    # Deprecated (kept for backward compatibility)
    'CARDIOVASCULAR_OTHER_DRUGS',
    'INFECTIOUS_OTHER_DRUGS',
    'PSYCHIATRY_OTHER_DRUGS',
    'ENDOCRINOLOGY_OTHER_DRUGS',
    'OTHER_DRUGS',
]

