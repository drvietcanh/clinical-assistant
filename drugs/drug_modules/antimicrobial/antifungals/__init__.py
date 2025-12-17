"""
Antifungals - Antifungal Medications
"""

# Import all drug categories
from .azoles import AZOLES_DRUGS
from .polyenes import POLYENES_DRUGS
from .echinocandins import ECHINOCANDINS_DRUGS

# Merge all categories
ANTIFUNGALS = {
    **AZOLES_DRUGS,
    **POLYENES_DRUGS,
    **ECHINOCANDINS_DRUGS,
}

__all__ = ['ANTIFUNGALS']

