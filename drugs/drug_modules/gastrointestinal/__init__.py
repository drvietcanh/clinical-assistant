"""Gastrointestinal Drugs
Active module - contains all gastrointestinal drug data"""

# Import all drug categories
from .antidiarrheals import ANTIDIARRHEALS_DRUGS
from .h2_receptor_antagonists import H2_RECEPTOR_ANTAGONISTS_DRUGS
from .mucosal_protectants import MUCOSAL_PROTECTANTS_DRUGS
from .proton_pump_inhibitors import PROTON_PUMP_INHIBITORS_DRUGS
from .prokinetic_antiemetics import PROKINETIC_ANTIEMETICS_DRUGS

# Merge all categories
GASTROINTESTINAL_DRUGS = {
    **ANTIDIARRHEALS_DRUGS,
    **H2_RECEPTOR_ANTAGONISTS_DRUGS,
    **MUCOSAL_PROTECTANTS_DRUGS,
    **PROTON_PUMP_INHIBITORS_DRUGS,
    **PROKINETIC_ANTIEMETICS_DRUGS,
}

__all__ = ['GASTROINTESTINAL_DRUGS']
