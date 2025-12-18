"""Endocrinology Drugs (Other) - Corticosteroids, Sex Hormones, Osteoporosis"""

# Import all drug categories
from .corticosteroids import CORTICOSTEROIDS_DRUGS
from .sex_hormones import SEX_HORMONES_DRUGS
from .osteoporosis_bisphosphonates import BISPHOSPHONATES_DRUGS
from .osteoporosis_other import OSTEOPOROSIS_OTHER_DRUGS

# Merge all categories
ENDOCRINOLOGY_OTHER_DRUGS = {
    **CORTICOSTEROIDS_DRUGS,
    **SEX_HORMONES_DRUGS,
    **BISPHOSPHONATES_DRUGS,
    **OSTEOPOROSIS_OTHER_DRUGS,
}

__all__ = ['ENDOCRINOLOGY_OTHER_DRUGS']
