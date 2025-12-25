"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Import all drug categories
from .nsaids import NSAIDS_DRUGS
from .opioid_agonists import OPIOID_AGONISTS_DRUGS
from .opioid_agonist_strongs import OPIOID_AGONIST_STRONGS_DRUGS
from .opioid_agonist_weaks import OPIOID_AGONIST_WEAKS_DRUGS
from .analgesic_antipyretic import ANALGESIC_ANTIPYRETIC_DRUGS
from .antimigraine_5_ht1_receptor_agonists import ANTIMIGRAINE_5_HT1_RECEPTOR_AGONISTS_DRUGS
from .pain_muscle_relaxant_combinations import PAIN_MUSCLE_RELAXANT_COMBINATIONS_DRUGS

# Merge all categories
ANALGESICS_DRUGS = {
    **NSAIDS_DRUGS,
    **OPIOID_AGONISTS_DRUGS,
    **OPIOID_AGONIST_STRONGS_DRUGS,
    **OPIOID_AGONIST_WEAKS_DRUGS,
    **ANALGESIC_ANTIPYRETIC_DRUGS,
    **ANTIMIGRAINE_5_HT1_RECEPTOR_AGONISTS_DRUGS,
    **PAIN_MUSCLE_RELAXANT_COMBINATIONS_DRUGS,
}

__all__ = ['ANALGESICS_DRUGS']
