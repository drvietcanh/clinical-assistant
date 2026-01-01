"""
Endocrinology Drugs
Corticosteroids, Sex Hormones, Osteoporosis treatments, Thyroid drugs
Renamed from endocrinology_other for better organization
"""

# Import new modules
from .corticosteroids import CORTICOSTEROIDS_DRUGS
from .thyroid import THYROID_DRUGS

# Import all drug categories from endocrinology_other subdirectory
# Use .. to refer to the sibling package 'endocrinology_other' from inside 'endocrinology' package
from ..endocrinology_other import ENDOCRINOLOGY_OTHER_DRUGS

# Merge all drugs
ENDOCRINOLOGY_DRUGS = {
    **ENDOCRINOLOGY_OTHER_DRUGS,
    **CORTICOSTEROIDS_DRUGS,
    **THYROID_DRUGS,
}

__all__ = ['ENDOCRINOLOGY_DRUGS']
