"""
Metabolic and Endocrine Medications
"""

# Import all drug categories
from .thyroid_hormones import THYROID_HORMONES_DRUGS
from .antithyroid import ANTITHYROID_DRUGS
from .corticosteroids import CORTICOSTEROIDS_DRUGS

# Merge all categories
METABOLIC_DRUGS = {
    **THYROID_HORMONES_DRUGS,
    **ANTITHYROID_DRUGS,
    **CORTICOSTEROIDS_DRUGS,
}

__all__ = ['METABOLIC_DRUGS']

