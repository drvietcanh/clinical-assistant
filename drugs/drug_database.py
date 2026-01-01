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
    ANTIPSYCHOTICS,
    MOOD_STABILIZERS,
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
    **ANTIPSYCHOTICS,
    **MOOD_STABILIZERS,
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

# Apply enhanced-field overrides (bổ sung/chuẩn hóa 14 fields cho một số thuốc)
for _name, _fields in EXTRA_ENHANCED_FIELDS.items():
    if _name in DRUG_DATABASE:
        DRUG_DATABASE[_name].update(_fields)

# Calculate total
TOTAL_DRUGS = len(DRUG_DATABASE)

__all__ = ['DRUG_DATABASE', 'DRUG_GROUPS', 'TOTAL_DRUGS']
