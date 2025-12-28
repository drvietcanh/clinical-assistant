"""
Psychiatry Drugs (Other) Module
Combines SSRI, SNRI, TCA, and Other Antidepressants categories
"""

from .ssris import SSRI_DRUGS
from .snris import SNRI_DRUGS
from .tcas import TCA_DRUGS
from .antipsychotics import ANTIPSYCHOTICS_DRUGS
from .antidepressants import OTHER_ANTIDEPRESSANTS_DRUGS
from .adhd_anxiolytics import ADHD_ANXIOLYTICS_DRUGS

# Merge all categories
PSYCHIATRY_OTHER_DRUGS = {
    **SSRI_DRUGS,
    **SNRI_DRUGS,
    **TCA_DRUGS,
    **ANTIPSYCHOTICS_DRUGS,
    **OTHER_ANTIDEPRESSANTS_DRUGS,
    **ADHD_ANXIOLYTICS_DRUGS,
}

__all__ = ['PSYCHIATRY_OTHER_DRUGS']

