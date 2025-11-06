"""
Antimicrobial Drugs Package
All antimicrobial drug modules organized by type: antibiotics, antivirals, antifungals
"""

from .antibiotics import ANTIMICROBIAL_ANTIBIOTICS
from .antivirals import ANTIVIRALS
from .antifungals import ANTIFUNGALS

# Merge all antimicrobial drug dictionaries
ANTIMICROBIAL_DRUGS = {
    **ANTIMICROBIAL_ANTIBIOTICS,
    **ANTIVIRALS,
    **ANTIFUNGALS,
}

__all__ = [
    'ANTIMICROBIAL_ANTIBIOTICS',
    'ANTIVIRALS',
    'ANTIFUNGALS',
    'ANTIMICROBIAL_DRUGS',
]
