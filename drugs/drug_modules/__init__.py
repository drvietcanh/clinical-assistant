"""
Drug Modules Package
All drug data modules organized by therapeutic category
Reorganized for better access and statistics (700+ drugs total)
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

# Additional modules from Phase 1-10
from .anesthesia import ANESTHESIA_DRUGS
from .allergy import ALLERGY_DRUGS
from .nutrition import NUTRITION_DRUGS
from .toxicology import TOXICOLOGY_DRUGS
from .vaccines import VACCINES_DRUGS
from .immunology import IMMUNOLOGY_DRUGS
from .rheumatology import RHEUMATOLOGY_DRUGS
from .psychiatry import PSYCHIATRY_DRUGS

# Backward compatibility - keep old imports but they point to merged modules
# These are now included in the main modules above
from .cardiovascular_other import CARDIOVASCULAR_OTHER_DRUGS  # Deprecated: use CARDIOVASCULAR_DRUGS
from .infectious_other import INFECTIOUS_OTHER_DRUGS  # Deprecated: use ANTIMICROBIAL_DRUGS
from .psychiatry_other import PSYCHIATRY_OTHER_DRUGS  # Deprecated: use NEUROLOGICAL_DRUGS
from .endocrinology_other import ENDOCRINOLOGY_OTHER_DRUGS  # Deprecated: use ENDOCRINOLOGY_DRUGS
from .other import OTHER_DRUGS  # Deprecated: use individual modules

# Unified dictionary of all drugs
ALL_DRUGS = {}
ALL_DRUGS.update(CARDIOVASCULAR_DRUGS)
ALL_DRUGS.update(DIABETES_DRUGS)
ALL_DRUGS.update(GASTROINTESTINAL_DRUGS)
ALL_DRUGS.update(ANALGESICS_DRUGS)
ALL_DRUGS.update(RESPIRATORY_DRUGS)
ALL_DRUGS.update(NEUROLOGICAL_DRUGS)
ALL_DRUGS.update(HEMATOLOGY_DRUGS)
ALL_DRUGS.update(SUPPORTIVE_DRUGS)
ALL_DRUGS.update(ANTIMICROBIAL_DRUGS)
ALL_DRUGS.update(METABOLIC_DRUGS)
ALL_DRUGS.update(ENDOCRINOLOGY_DRUGS)
ALL_DRUGS.update(ONCOLOGY_DRUGS)
ALL_DRUGS.update(EMERGENCY_DRUGS)
ALL_DRUGS.update(UROLOGY_DRUGS)
ALL_DRUGS.update(DERMATOLOGY_DRUGS)
ALL_DRUGS.update(OPHTHALMOLOGY_DRUGS)
ALL_DRUGS.update(OBSTETRICS_GYNECOLOGY_DRUGS)
ALL_DRUGS.update(ENT_ORAL_NASAL_COMBINATIONS_DRUGS)
ALL_DRUGS.update(MISCELLANEOUS_DRUGS)
ALL_DRUGS.update(ANESTHESIA_DRUGS)
# Add other collections if they have unique keys not covered above
ALL_DRUGS.update(CARDIOVASCULAR_OTHER_DRUGS)
ALL_DRUGS.update(INFECTIOUS_OTHER_DRUGS)
ALL_DRUGS.update(PSYCHIATRY_OTHER_DRUGS)
ALL_DRUGS.update(ENDOCRINOLOGY_OTHER_DRUGS)
ALL_DRUGS.update(OTHER_DRUGS)


__all__ = [
    'ALL_DRUGS',
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
    'ANESTHESIA_DRUGS',
    'VACCINES_DRUGS',
    'TOXICOLOGY_DRUGS',
    'ALLERGY_DRUGS',
    'NUTRITION_DRUGS',
    'RHEUMATOLOGY_DRUGS',
    'IMMUNOLOGY_DRUGS',
    'ONCOLOGY_DRUGS',

    # Deprecated (kept for backward compatibility)
    'CARDIOVASCULAR_OTHER_DRUGS',
    'INFECTIOUS_OTHER_DRUGS',
    'PSYCHIATRY_OTHER_DRUGS',
    'ENDOCRINOLOGY_OTHER_DRUGS',
    'OTHER_DRUGS',
]
