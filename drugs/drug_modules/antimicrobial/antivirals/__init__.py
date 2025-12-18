"""
Antivirals Module
Combines all antiviral categories: herpes, influenza, CMV, hepatitis
"""

from .herpes import HERPES_ANTIVIRALS
from .influenza import INFLUENZA_ANTIVIRALS
from .cmv import CMV_ANTIVIRALS
from .hepatitis import HEPATITIS_ANTIVIRALS
from .hiv_arvs import HIV_ARVS

# Merge all categories
ANTIVIRALS = {
    **HERPES_ANTIVIRALS,
    **INFLUENZA_ANTIVIRALS,
    **CMV_ANTIVIRALS,
    **HEPATITIS_ANTIVIRALS,
    **HIV_ARVS,
}

__all__ = ['ANTIVIRALS']

