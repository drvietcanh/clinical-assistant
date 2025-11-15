"""
Psychiatry Drugs (Other) Module
Combines SSRI, SNRI, and TCA categories
"""

from .ssris import SSRI_DRUGS
from .snris import SNRI_DRUGS
from .tcas import TCA_DRUGS

# Merge all categories
PSYCHIATRY_OTHER_DRUGS = {
    **SSRI_DRUGS,
    **SNRI_DRUGS,
    **TCA_DRUGS,
}

__all__ = ['PSYCHIATRY_OTHER_DRUGS']

