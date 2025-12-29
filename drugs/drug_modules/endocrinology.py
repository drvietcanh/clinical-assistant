"""
Endocrinology Drugs
Corticosteroids, Sex Hormones, Osteoporosis treatments
Renamed from endocrinology_other for better organization
"""

# Import all drug categories from endocrinology_other subdirectory
from .endocrinology_other import ENDOCRINOLOGY_OTHER_DRUGS

# Use the merged drugs from endocrinology_other
ENDOCRINOLOGY_DRUGS = ENDOCRINOLOGY_OTHER_DRUGS

__all__ = ['ENDOCRINOLOGY_DRUGS']

