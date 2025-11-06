"""
Antimicrobial Medications (Antibiotics, Antivirals, Antifungals)
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules in antimicrobial/:
- antibiotics.py: Common Oral and IV Antibiotics
- antivirals.py: Antiviral Medications
- antifungals.py: Antifungal Medications
"""

# Import from antimicrobial subdirectory
from .antimicrobial import ANTIMICROBIAL_DRUGS

__all__ = ['ANTIMICROBIAL_DRUGS']
