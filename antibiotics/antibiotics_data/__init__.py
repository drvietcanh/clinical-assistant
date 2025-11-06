"""
Antibiotics Database Package
All antibiotic modules organized by drug class
"""

from .penicillins import PENICILLINS
from .cephalosporins import CEPHALOSPORINS
from .carbapenems import CARBAPENEMS
from .aminoglycosides import AMINOGLYCOSIDES
from .glycopeptides import GLYCOPEPTIDES
from .fluoroquinolones import FLUOROQUINOLONES
from .macrolides import MACROLIDES
from .lincosamides import LINCOSAMIDES
from .tetracyclines import TETRACYCLINES
from .others import OTHER_ANTIBIOTICS

# Merge all antibiotic dictionaries
ANTIBIOTICS_DATABASE = {
    **PENICILLINS,
    **CEPHALOSPORINS,
    **CARBAPENEMS,
    **AMINOGLYCOSIDES,
    **GLYCOPEPTIDES,
    **FLUOROQUINOLONES,
    **MACROLIDES,
    **LINCOSAMIDES,
    **TETRACYCLINES,
    **OTHER_ANTIBIOTICS,
}

__all__ = [
    'PENICILLINS',
    'CEPHALOSPORINS',
    'CARBAPENEMS',
    'AMINOGLYCOSIDES',
    'GLYCOPEPTIDES',
    'FLUOROQUINOLONES',
    'MACROLIDES',
    'LINCOSAMIDES',
    'TETRACYCLINES',
    'OTHER_ANTIBIOTICS',
    'ANTIBIOTICS_DATABASE',
]
