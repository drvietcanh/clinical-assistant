"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Import all drug categories
from .biguanides import BIGUANIDES_DRUGS
from .dpp_4_inhibitors import DPP_4_INHIBITORS_DRUGS
from .insulins import INSULINS_DRUGS
from .sglt2_inhibitors import SGLT2_INHIBITORS_DRUGS
from .sulfonylureas import SULFONYLUREAS_DRUGS
from .thiazolidinedione_tzds import THIAZOLIDINEDIONE_TZDS_DRUGS
from .meglitinides import MEGLITINIDES_DRUGS
from .alpha_glucosidase_inhibitors import ALPHA_GLUCOSIDASE_INHIBITORS_DRUGS
from .glp1_agonists import GLP1_AGONISTS_DRUGS
from .fixed_dose_combinations import DIABETES_FIXED_DOSE_COMBINATIONS

# Merge all categories
DIABETES_DRUGS = {
    **BIGUANIDES_DRUGS,
    **DPP_4_INHIBITORS_DRUGS,
    **INSULINS_DRUGS,
    **SGLT2_INHIBITORS_DRUGS,
    **SULFONYLUREAS_DRUGS,
    **THIAZOLIDINEDIONE_TZDS_DRUGS,
    **MEGLITINIDES_DRUGS,
    **ALPHA_GLUCOSIDASE_INHIBITORS_DRUGS,
    **GLP1_AGONISTS_DRUGS,
    **DIABETES_FIXED_DOSE_COMBINATIONS,
}

__all__ = ['DIABETES_DRUGS']
