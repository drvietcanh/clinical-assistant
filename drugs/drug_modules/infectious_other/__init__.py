"""
Infectious Disease & Antibiotic Drugs (Other) - Split by category
"""

# Import all drug categories
from .anthelmintics import ANTHELMINTICS_DRUGS
from .antimalarials import ANTIMALARIALS_DRUGS
from .beta_lactams import BETA_LACTAMS_DRUGS
from .cephalosporins import CEPHALOSPORINS_DRUGS
from .fluoroquinolones import FLUOROQUINOLONES_DRUGS
from .macrolides import MACROLIDES_DRUGS
from .nitroimidazoles import NITROIMIDAZOLES_DRUGS
from .tetracyclines import TETRACYCLINES_DRUGS

# Merge all categories
INFECTIOUS_OTHER_DRUGS = {
    **ANTHELMINTICS_DRUGS,
    **ANTIMALARIALS_DRUGS,
    **BETA_LACTAMS_DRUGS,
    **CEPHALOSPORINS_DRUGS,
    **FLUOROQUINOLONES_DRUGS,
    **MACROLIDES_DRUGS,
    **NITROIMIDAZOLES_DRUGS,
    **TETRACYCLINES_DRUGS,
}

__all__ = ['INFECTIOUS_OTHER_DRUGS']
