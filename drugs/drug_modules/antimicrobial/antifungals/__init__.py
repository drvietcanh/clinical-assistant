"""
Antifungals - Antifungal Medications
"""

# Import all drug categories
from .azoles import AZOLES_DRUGS
from .polyenes import POLYENES_DRUGS

# Merge all categories
ANTIFUNGALS = {
    **AZOLES_DRUGS,
    **POLYENES_DRUGS,
}

__all__ = ['ANTIFUNGALS']

