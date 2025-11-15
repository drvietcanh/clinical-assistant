"""
Antivirals - Antiviral Medications
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules in antivirals/:
- herpes.py: Herpes antivirals (Acyclovir, Valacyclovir)
- influenza.py: Influenza antivirals (Oseltamivir)
- cmv.py: CMV antivirals (Ganciclovir)
- hepatitis.py: Hepatitis antivirals (Ribavirin)
"""

# Import from antivirals subdirectory
from .antivirals import ANTIVIRALS

__all__ = ['ANTIVIRALS']
