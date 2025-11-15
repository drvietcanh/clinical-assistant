"""
Calcium Channel Blockers Module
Combines dihydropyridine and non-dihydropyridine categories
"""

from .dihydropyridines import DIHYDROPYRIDINE_CCB
from .non_dihydropyridines import NON_DIHYDROPYRIDINE_CCB

# Merge all categories
CALCIUM_BLOCKERS = {
    **DIHYDROPYRIDINE_CCB,
    **NON_DIHYDROPYRIDINE_CCB,
}

__all__ = ['CALCIUM_BLOCKERS']

