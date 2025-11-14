"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Import all drug categories
from .nsaids import NSAIDS_DRUGS
from .opioid_agonists import OPIOID_AGONISTS_DRUGS

# Merge all categories
ANALGESICS_DRUGS = {
    **NSAIDS_DRUGS,
    **OPIOID_AGONISTS_DRUGS,
}

__all__ = ['ANALGESICS_DRUGS']
