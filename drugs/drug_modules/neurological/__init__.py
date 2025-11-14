"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# Import all drug categories
from .anticonvulsants import ANTICONVULSANTS_DRUGS

# Merge all categories
NEUROLOGICAL_DRUGS = {
    **ANTICONVULSANTS_DRUGS,
}

__all__ = ['NEUROLOGICAL_DRUGS']
