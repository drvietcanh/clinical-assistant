"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Import all drug categories
from .leukotriene_receptor_antagonists import LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS
from .short_acting_beta_2_agonists import SHORT_ACTING_BETA_2_AGONISTS_DRUGS

# Merge all categories
RESPIRATORY_DRUGS = {
    **LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS,
    **SHORT_ACTING_BETA_2_AGONISTS_DRUGS,
}

__all__ = ['RESPIRATORY_DRUGS']
