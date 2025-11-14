"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Import all drug categories
from .nsaids import NSAIDS_DRUGS
from .opioid_agonists import OPIOID_AGONISTS_DRUGS
from .analgesic_antipyretic import ANALGESIC_ANTIPYRETIC_DRUGS

# Merge all categories
ANALGESICS_DRUGS = {
    **NSAIDS_DRUGS,
    **OPIOID_AGONISTS_DRUGS,
    **ANALGESIC_ANTIPYRETIC_DRUGS,
}

__all__ = ['ANALGESICS_DRUGS']
