"""
Antibiotics Module
Combines all antibiotic categories
"""

from .beta_lactams import BETA_LACTAM_ANTIBIOTICS
from .lincosamides import LINCOSAMIDE_ANTIBIOTICS
from .sulfonamides import SULFONAMIDE_ANTIBIOTICS
from .fluoroquinolones import FLUOROQUINOLONE_ANTIBIOTICS

# Merge all antibiotic categories
ANTIMICROBIAL_ANTIBIOTICS = {
    **BETA_LACTAM_ANTIBIOTICS,
    **LINCOSAMIDE_ANTIBIOTICS,
    **SULFONAMIDE_ANTIBIOTICS,
    **FLUOROQUINOLONE_ANTIBIOTICS,
}

__all__ = ['ANTIMICROBIAL_ANTIBIOTICS']

