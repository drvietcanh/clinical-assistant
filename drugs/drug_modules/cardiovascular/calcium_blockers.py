"""
Calcium Channel Blockers
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules in calcium_blockers/:
- dihydropyridines.py: Dihydropyridine CCBs (Amlodipine, Nifedipine)
- non_dihydropyridines.py: Non-dihydropyridine CCBs (Diltiazem, Verapamil)
"""

# Import from calcium_blockers subdirectory
from .calcium_blockers import CALCIUM_BLOCKERS

__all__ = ['CALCIUM_BLOCKERS']
