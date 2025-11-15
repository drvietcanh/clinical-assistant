"""
Antimicrobial Drugs Package
All antimicrobial drug modules organized by type: antibiotics, antivirals, antifungals
"""

# Import all drug categories
from .antibiotics import ANTIMICROBIAL_ANTIBIOTICS
from .antivirals import ANTIVIRALS
from .antifungals import ANTIFUNGALS

# Merge all categories
ANTIMICROBIAL_DRUGS = {
    **ANTIMICROBIAL_ANTIBIOTICS,
    **ANTIVIRALS,
    **ANTIFUNGALS,
}

__all__ = ['ANTIMICROBIAL_DRUGS']
