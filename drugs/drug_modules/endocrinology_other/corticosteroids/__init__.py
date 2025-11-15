"""
Corticosteroids - All Types
Merge short/intermediate-acting and long-acting corticosteroids
"""

from .short_intermediate_acting import SHORT_INTERMEDIATE_ACTING
from .long_acting import LONG_ACTING

# Merge all corticosteroids
CORTICOSTEROIDS_DRUGS = {
    **SHORT_INTERMEDIATE_ACTING,
    **LONG_ACTING,
}

__all__ = [
    'SHORT_INTERMEDIATE_ACTING',
    'LONG_ACTING',
    'CORTICOSTEROIDS_DRUGS',
]

