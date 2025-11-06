"""
Cardiovascular Drugs
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules in cardiovascular/:
- ace_inhibitors.py: ACE Inhibitors
- arbs.py: Angiotensin Receptor Blockers
- beta_blockers.py: Beta-blockers
- calcium_blockers.py: Calcium Channel Blockers
- diuretics.py: Diuretics
- antiarrhythmics.py: Antiarrhythmics
- anticoagulants.py: Anticoagulants and Antiplatelets
- statins.py: Statins
- vasodilators.py: Vasodilators
- other_cv.py: Other Cardiovascular Drugs
"""

# Import from cardiovascular subdirectory
from .cardiovascular import CARDIOVASCULAR_DRUGS

__all__ = ['CARDIOVASCULAR_DRUGS']
