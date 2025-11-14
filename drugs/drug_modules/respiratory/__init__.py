"""Respiratory Medications
Active module - contains all respiratory drug data"""

# Import all drug categories
from .leukotriene_receptor_antagonists import LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS

# Merge all categories
RESPIRATORY_DRUGS = {
    **LEUKOTRIENE_RECEPTOR_ANTAGONISTS_DRUGS,
}

__all__ = ['RESPIRATORY_DRUGS']
