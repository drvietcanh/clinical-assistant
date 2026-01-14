"""Diabetes Medications
Active module - contains all diabetes drug data"""

# Import all drug categories
# Temporarily skip biguanides.py due to syntax errors
# from .biguanides import BIGUANIDES_DRUGS
from .dpp_4_inhibitors import DPP_4_INHIBITORS_DRUGS
from .insulins import INSULINS_DRUGS
from .specific_insulins import SPECIFIC_INSULINS_DRUGS
from .sglt2_inhibitors import SGLT2_INHIBITORS_DRUGS
from .sulfonylureas import SULFONYLUREAS_DRUGS
from .thiazolidinedione_tzds import THIAZOLIDINEDIONE_TZDS_DRUGS
from .meglitinides import MEGLITINIDES_DRUGS
from .alpha_glucosidase_inhibitors import ALPHA_GLUCOSIDASE_INHIBITORS_DRUGS
from .glp1_agonists import GLP1_AGONISTS_DRUGS
from .fixed_dose_combinations import DIABETES_FIXED_DOSE_COMBINATIONS
from .t1dm_prevention import T1DM_PREVENTION_DRUGS
from .other_antidiabetics import OTHER_ANTIDIABETICS_DRUGS

# Merge all categories
DIABETES_DRUGS = {
    # **BIGUANIDES_DRUGS,  # Temporarily skipped
    **DPP_4_INHIBITORS_DRUGS,
    **INSULINS_DRUGS,
    **SPECIFIC_INSULINS_DRUGS,
    **SGLT2_INHIBITORS_DRUGS,
    **SULFONYLUREAS_DRUGS,
    **THIAZOLIDINEDIONE_TZDS_DRUGS,
    **MEGLITINIDES_DRUGS,
    **ALPHA_GLUCOSIDASE_INHIBITORS_DRUGS,
    **GLP1_AGONISTS_DRUGS,
    **DIABETES_FIXED_DOSE_COMBINATIONS,
    **T1DM_PREVENTION_DRUGS,
    **OTHER_ANTIDIABETICS_DRUGS,
}

__all__ = ['DIABETES_DRUGS']
