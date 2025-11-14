"""Endocrinology Drugs (Other) - Corticosteroids"""

# Import all drug categories
from .corticosteroids import CORTICOSTEROIDS_DRUGS

# Merge all categories
ENDOCRINOLOGY_OTHER_DRUGS = {
    **CORTICOSTEROIDS_DRUGS,
}

__all__ = ['ENDOCRINOLOGY_OTHER_DRUGS']
