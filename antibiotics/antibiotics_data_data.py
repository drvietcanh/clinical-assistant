"""
Antibiotic Database - Common Injectable Antibiotics in Vietnam
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules in antibiotics_data/:
- penicillins.py: Penicillins
- cephalosporins.py: Cephalosporins
- carbapenems.py: Carbapenems
- aminoglycosides.py: Aminoglycosides
- glycopeptides.py: Glycopeptides
- fluoroquinolones.py: Fluoroquinolones
- macrolides.py: Macrolides
- lincosamides.py: Lincosamides
- tetracyclines.py: Tetracyclines
- others.py: Other Antibiotics
"""

# Import from antibiotics_data subdirectory
from .antibiotics_data import ANTIBIOTICS_DATABASE

__all__ = ['ANTIBIOTICS_DATABASE']
