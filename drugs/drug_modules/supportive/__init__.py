"""Supportive Care Medications (Vitamins, Corticosteroids, Antihistamines)
Active module - contains all supportive care drug data"""

# Import all drug categories
from .calciums import CALCIUMS_DRUGS
from .folates import FOLATES_DRUGS
from .irons import IRONS_DRUGS
from .vitamin_b12s import VITAMIN_B12S_DRUGS
from .vitamin_ds import VITAMIN_DS_DRUGS

# Merge all categories
SUPPORTIVE_DRUGS = {
    **CALCIUMS_DRUGS,
    **FOLATES_DRUGS,
    **IRONS_DRUGS,
    **VITAMIN_B12S_DRUGS,
    **VITAMIN_DS_DRUGS,
}

__all__ = ['SUPPORTIVE_DRUGS']
