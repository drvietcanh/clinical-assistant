"""
Drug Database - Common Medications in Vietnam
Database 100-200 thuốc phổ biến tại Việt Nam
Ưu tiên thuốc thường dùng trong lâm sàng

NOTE: Data đã được tách ra file drug_modules/
File này import và merge tất cả modules để giữ backward compatibility
"""

from .drug_modules import (
    # Main organized modules (reorganized for better access)
    CARDIOVASCULAR_DRUGS,  # Now includes cardiovascular_other
    DIABETES_DRUGS,
    GASTROINTESTINAL_DRUGS,
    ANALGESICS_DRUGS,
    RESPIRATORY_DRUGS,
    NEUROLOGICAL_DRUGS,  # Now includes psychiatry_other
    HEMATOLOGY_DRUGS,
    SUPPORTIVE_DRUGS,
    ANTIMICROBIAL_DRUGS,  # Now includes infectious_other
    METABOLIC_DRUGS,
    ENDOCRINOLOGY_DRUGS,  # Renamed from endocrinology_other
    ONCOLOGY_DRUGS,
    EMERGENCY_DRUGS,
    UROLOGY_DRUGS,
    DERMATOLOGY_DRUGS,
    OPHTHALMOLOGY_DRUGS,
    OBSTETRICS_GYNECOLOGY_DRUGS,
    ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    MISCELLANEOUS_DRUGS,
    # New Standardized Modules
    # Psychiatry

    # Anesthesia
    ANESTHESIA_DRUGS,
    # Vaccines
    VACCINES_DRUGS,
    # Toxicology
    TOXICOLOGY_DRUGS,
    # Allergy
    ALLERGY_DRUGS,
    # Nutrition
    NUTRITION_DRUGS,
    # Rheumatology
    RHEUMATOLOGY_DRUGS,
    # Immunology
    IMMUNOLOGY_DRUGS,
    # Oncology
    ONCOLOGY_DRUGS,
    # Deprecated modules (kept for backward compatibility, but already merged above)
    CARDIOVASCULAR_OTHER_DRUGS,
    INFECTIOUS_OTHER_DRUGS,
    PSYCHIATRY_OTHER_DRUGS,
    ENDOCRINOLOGY_OTHER_DRUGS,
    OTHER_DRUGS,
)

from .drug_utils import DRUG_GROUPS
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS
import copy

# Merge all drug dictionaries
# Note: CARDIOVASCULAR_DRUGS now includes cardiovascular_other
#       ANTIMICROBIAL_DRUGS now includes infectious_other
#       NEUROLOGICAL_DRUGS now includes psychiatry_other
#       ENDOCRINOLOGY_DRUGS renamed from endocrinology_other
DRUG_DATABASE = {
    **CARDIOVASCULAR_DRUGS,  # Includes cardiovascular_other
    **DIABETES_DRUGS,
    **GASTROINTESTINAL_DRUGS,
    **ANALGESICS_DRUGS,
    **RESPIRATORY_DRUGS,
    **NEUROLOGICAL_DRUGS,  # Includes psychiatry_other
    **HEMATOLOGY_DRUGS,
    **SUPPORTIVE_DRUGS,
    **ANTIMICROBIAL_DRUGS,  # Includes infectious_other
    **METABOLIC_DRUGS,
    **ENDOCRINOLOGY_DRUGS,  # Renamed from endocrinology_other
    **ONCOLOGY_DRUGS,
    **EMERGENCY_DRUGS,
    **UROLOGY_DRUGS,
    **DERMATOLOGY_DRUGS,
    **OPHTHALMOLOGY_DRUGS,
    **OBSTETRICS_GYNECOLOGY_DRUGS,
    **ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    **MISCELLANEOUS_DRUGS,

    **ANESTHESIA_DRUGS,
    **VACCINES_DRUGS,
    **TOXICOLOGY_DRUGS,
    **ALLERGY_DRUGS,
    **NUTRITION_DRUGS,
    **RHEUMATOLOGY_DRUGS,
    **IMMUNOLOGY_DRUGS,
    **ONCOLOGY_DRUGS,
    # Note: Deprecated modules (CARDIOVASCULAR_OTHER_DRUGS, INFECTIOUS_OTHER_DRUGS,
    #       PSYCHIATRY_OTHER_DRUGS, ENDOCRINOLOGY_OTHER_DRUGS, OTHER_DRUGS)
    #       are already included in the main modules above, so we don't merge them again
    #       to avoid duplicates
}

# Remove stray non-drug keys that may appear from malformed imports
_NON_DRUG_KEYS = [
    "administration_instructions",
    "contraindications",
    "contraindications_detail",
    "drug_interactions",
    "hepatic_adjustment",
    "overdose_management",
    "pharmacokinetics",
    "pregnancy_lactation",
    "renal_adjustment",
    "reversal_agents",
    "risk_flags",
]
for _k in _NON_DRUG_KEYS:
    DRUG_DATABASE.pop(_k, None)

# Apply enhanced-field overrides (bổ sung/chuẩn hóa 14 fields cho một số thuốc)
for _name, _fields in EXTRA_ENHANCED_FIELDS.items():
    if _name in DRUG_DATABASE:
        DRUG_DATABASE[_name].update(_fields)

# Skeleton defaults to guarantee all enhanced fields có key (và không trống)
_DEFAULT_ENHANCED_FIELDS = {
    "mechanism_of_action": "Đang cập nhật",
    "monitoring": ["Đang cập nhật"],
    "precautions": ["Đang cập nhật"],
    "pharmacokinetics": {
        "absorption": "Đang cập nhật",
        "distribution": "Đang cập nhật",
        "metabolism": "Đang cập nhật",
        "excretion": "Đang cập nhật",
        "half_life": "Đang cập nhật",
        "notes": "Đang cập nhật",
    },
    "storage": "Đang cập nhật",
    "black_box_warnings": "Đang cập nhật",
    "drug_interactions": {
        "major": [],
        "moderate": [],
        "minor": [],
    },
    "contraindications_detail": {
        "tuyệt_đối": [],
        "tương_đối": [],
    },
    "pregnancy_lactation": "Đang cập nhật",
    "hepatic_adjustment": "Đang cập nhật",
    "renal_adjustment": {
        "normal": "Đang cập nhật",
        "30_60": "Đang cập nhật",
        "under_30": "Đang cập nhật",
        "dialysis": "Đang cập nhật",
        "notes": "Đang cập nhật",
    },
    "overdose_management": "Đang cập nhật",
    "reversal_agents": {
        "available": False,
        "agents": [],
        "notes": "Đang cập nhật",
    },
    "administration_instructions": "Đang cập nhật",
}


def _ensure_enhanced_fields_on_database():
    """Guarantee every drug has all enhanced fields with non-empty skeleton."""
    for _drug_name, _drug_data in DRUG_DATABASE.items():
        if not isinstance(_drug_data, dict):
            continue
        for _field, _default in _DEFAULT_ENHANCED_FIELDS.items():
            if _field not in _drug_data or _drug_data[_field] is None:
                _drug_data[_field] = copy.deepcopy(_default)
            elif isinstance(_drug_data[_field], str) and not _drug_data[_field].strip():
                _drug_data[_field] = copy.deepcopy(_default)
            elif isinstance(_drug_data[_field], (list, dict)) and len(_drug_data[_field]) == 0:
                _drug_data[_field] = copy.deepcopy(_default)


_ensure_enhanced_fields_on_database()

# Calculate total
TOTAL_DRUGS = len(DRUG_DATABASE)

__all__ = ['DRUG_DATABASE', 'DRUG_GROUPS', 'TOTAL_DRUGS']
