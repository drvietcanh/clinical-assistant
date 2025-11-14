"""Miscellaneous Drugs - Metabolism, Respiratory, Analgesic, Hematology"""

# Import all drug categories
from .vitamins import VITAMINS_DRUGS
from .xanthine_oxidase_inhibitors import XANTHINE_OXIDASE_INHIBITORS_DRUGS

# Merge all categories
MISCELLANEOUS_DRUGS = {
    **VITAMINS_DRUGS,
    **XANTHINE_OXIDASE_INHIBITORS_DRUGS,
}

__all__ = ['MISCELLANEOUS_DRUGS']
