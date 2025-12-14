"""Endocrinology Drugs (Other) - Corticosteroids, Sex Hormones"""

# Import all drug categories
from .corticosteroids import CORTICOSTEROIDS_DRUGS
from .sex_hormones import SEX_HORMONES_DRUGS

# Merge all categories
ENDOCRINOLOGY_OTHER_DRUGS = {
    **CORTICOSTEROIDS_DRUGS,
    **SEX_HORMONES_DRUGS,
}

__all__ = ['ENDOCRINOLOGY_OTHER_DRUGS']
