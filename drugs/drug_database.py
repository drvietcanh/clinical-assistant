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
)

from .drug_utils import DRUG_GROUPS

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
}

# Calculate total
TOTAL_DRUGS = len(DRUG_DATABASE)

__all__ = ['DRUG_DATABASE', 'DRUG_GROUPS', 'TOTAL_DRUGS']
