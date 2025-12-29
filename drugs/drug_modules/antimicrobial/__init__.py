"""
Antimicrobial Drugs Package
All antimicrobial drug modules organized by type: antibiotics, antivirals, antifungals
Includes: beta-lactams, cephalosporins, macrolides, fluoroquinolones, tetracyclines,
nitroimidazoles, antituberculars, antimalarials, anthelmintics, etc.
"""

# Import all drug categories from antimicrobial subdirectory
from .antibiotics import ANTIMICROBIAL_ANTIBIOTICS
from .antivirals import ANTIVIRALS
from .antifungals import ANTIFUNGALS

# Import from infectious_other (merged into main antimicrobial module)
from ..infectious_other.anthelmintics import ANTHELMINTICS_DRUGS
from ..infectious_other.antimalarials import ANTIMALARIALS_DRUGS
from ..infectious_other.beta_lactams import BETA_LACTAMS_DRUGS
from ..infectious_other.cephalosporins import CEPHALOSPORINS_DRUGS
from ..infectious_other.fluoroquinolones import FLUOROQUINOLONES_DRUGS
from ..infectious_other.macrolides import MACROLIDES_DRUGS
from ..infectious_other.nitroimidazoles import NITROIMIDAZOLES_DRUGS
from ..infectious_other.tetracyclines import TETRACYCLINES_DRUGS
from ..infectious_other.antituberculars import ANTITUBERCULAR_DRUGS

# Merge all categories
ANTIMICROBIAL_DRUGS = {
    **ANTIMICROBIAL_ANTIBIOTICS,
    **ANTIVIRALS,
    **ANTIFUNGALS,
    # Merged from infectious_other
    **ANTHELMINTICS_DRUGS,
    **ANTIMALARIALS_DRUGS,
    **BETA_LACTAMS_DRUGS,
    **CEPHALOSPORINS_DRUGS,
    **FLUOROQUINOLONES_DRUGS,
    **MACROLIDES_DRUGS,
    **NITROIMIDAZOLES_DRUGS,
    **TETRACYCLINES_DRUGS,
    **ANTITUBERCULAR_DRUGS,
}

__all__ = ['ANTIMICROBIAL_DRUGS']
