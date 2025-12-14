"""
Antibiotics Module
Combines all antibiotic categories
"""

from .beta_lactams import BETA_LACTAM_ANTIBIOTICS
from .lincosamides import LINCOSAMIDE_ANTIBIOTICS
from .sulfonamides import SULFONAMIDE_ANTIBIOTICS
from .fluoroquinolones import FLUOROQUINOLONE_ANTIBIOTICS
from .aminoglycosides import AMINOGLYCOSIDE_ANTIBIOTICS
from .glycopeptides import GLYCOPEPTIDE_ANTIBIOTICS
from .oxazolidinones import OXAZOLIDINONE_ANTIBIOTICS
from .polymyxins import POLYMYXIN_ANTIBIOTICS

# Merge all antibiotic categories
ANTIMICROBIAL_ANTIBIOTICS = {
    **BETA_LACTAM_ANTIBIOTICS,
    **LINCOSAMIDE_ANTIBIOTICS,
    **SULFONAMIDE_ANTIBIOTICS,
    **FLUOROQUINOLONE_ANTIBIOTICS,
    **AMINOGLYCOSIDE_ANTIBIOTICS,
    **GLYCOPEPTIDE_ANTIBIOTICS,
    **OXAZOLIDINONE_ANTIBIOTICS,
    **POLYMYXIN_ANTIBIOTICS,
}

__all__ = ['ANTIMICROBIAL_ANTIBIOTICS']

