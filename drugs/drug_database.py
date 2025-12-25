"""
Drug Database - Common Medications in Vietnam
Database 100-200 thuốc phổ biến tại Việt Nam
Ưu tiên thuốc thường dùng trong lâm sàng

NOTE: Data đã được tách ra file drug_modules/
File này import và merge tất cả modules để giữ backward compatibility
"""

from .drug_modules import (
    CARDIOVASCULAR_DRUGS,
    DIABETES_DRUGS,
    GASTROINTESTINAL_DRUGS,
    ANALGESICS_DRUGS,
    RESPIRATORY_DRUGS,
    NEUROLOGICAL_DRUGS,
    HEMATOLOGY_DRUGS,
    SUPPORTIVE_DRUGS,
    ANTIMICROBIAL_DRUGS,
    METABOLIC_DRUGS,
    ONCOLOGY_DRUGS,
    EMERGENCY_DRUGS,
    OTHER_DRUGS,
    DERMATOLOGY_DRUGS,
    OPHTHALMOLOGY_DRUGS,
    UROLOGY_DRUGS,
    # Split modules from other.py (already included in OTHER_DRUGS, but available separately)
    CARDIOVASCULAR_OTHER_DRUGS,
    INFECTIOUS_OTHER_DRUGS,
    PSYCHIATRY_OTHER_DRUGS,
    ENDOCRINOLOGY_OTHER_DRUGS,
    MISCELLANEOUS_DRUGS,
)

from .drug_utils import DRUG_GROUPS
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

# Merge all drug dictionaries
DRUG_DATABASE = {
    **CARDIOVASCULAR_DRUGS,
    **DIABETES_DRUGS,
    **GASTROINTESTINAL_DRUGS,
    **ANALGESICS_DRUGS,
    **RESPIRATORY_DRUGS,
    **NEUROLOGICAL_DRUGS,
    **HEMATOLOGY_DRUGS,
    **SUPPORTIVE_DRUGS,
    **ANTIMICROBIAL_DRUGS,
    **METABOLIC_DRUGS,
    **ONCOLOGY_DRUGS,
    **EMERGENCY_DRUGS,
    **OTHER_DRUGS,
    **DERMATOLOGY_DRUGS,
    **OPHTHALMOLOGY_DRUGS,
    **UROLOGY_DRUGS,
    # Additional modules
    **INFECTIOUS_OTHER_DRUGS,
    **CARDIOVASCULAR_OTHER_DRUGS,
    **PSYCHIATRY_OTHER_DRUGS,
    **ENDOCRINOLOGY_OTHER_DRUGS,
    **MISCELLANEOUS_DRUGS,
}

# Apply enhanced-field overrides (bổ sung/chuẩn hóa 14 fields cho một số thuốc)
for _name, _fields in EXTRA_ENHANCED_FIELDS.items():
    if _name in DRUG_DATABASE:
        DRUG_DATABASE[_name].update(_fields)

# Calculate total
TOTAL_DRUGS = len(DRUG_DATABASE)

__all__ = ['DRUG_DATABASE', 'DRUG_GROUPS', 'TOTAL_DRUGS']
