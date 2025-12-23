"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology, Immunosuppressants"""

# Import all drug categories
from .vitamins import VITAMINS_DRUGS
from .xanthine_oxidase_inhibitors import XANTHINE_OXIDASE_INHIBITORS_DRUGS
from .gout_medications import GOUT_MEDICATIONS_DRUGS
from .immunosuppressants import IMMUNOSUPPRESSANTS_DRUGS
from .biological_drugs import BIOLOGICAL_DRUGS

# Merge all categories
MISCELLANEOUS_DRUGS = {
    **VITAMINS_DRUGS,
    **XANTHINE_OXIDASE_INHIBITORS_DRUGS,
    **GOUT_MEDICATIONS_DRUGS,
    **IMMUNOSUPPRESSANTS_DRUGS,
    **BIOLOGICAL_DRUGS,
}

__all__ = ['MISCELLANEOUS_DRUGS']
