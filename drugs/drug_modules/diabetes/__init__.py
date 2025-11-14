"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Import all drug categories
from .biguanides import BIGUANIDES_DRUGS
from .dpp_4_inhibitors import DPP_4_INHIBITORS_DRUGS
from .insulins import INSULINS_DRUGS
from .sglt2_inhibitors import SGLT2_INHIBITORS_DRUGS
from .sulfonylureas import SULFONYLUREAS_DRUGS
from .thiazolidinedione_tzds import THIAZOLIDINEDIONE_TZDS_DRUGS

# Merge all categories
DIABETES_DRUGS = {
    **BIGUANIDES_DRUGS,
    **DPP_4_INHIBITORS_DRUGS,
    **INSULINS_DRUGS,
    **SGLT2_INHIBITORS_DRUGS,
    **SULFONYLUREAS_DRUGS,
    **THIAZOLIDINEDIONE_TZDS_DRUGS,
}

__all__ = ['DIABETES_DRUGS']
