"""
Cardiovascular Other Drugs Module
Antiplatelets, Statins, ACE Inhibitors IV
"""

from .antiplatelets import ANTIPLATELETS_DRUGS
from .statins import STATINS_DRUGS
from .ace_inhibitors_iv import ACE_INHIBITORS_IV_DRUGS

# Merge all categories
CARDIOVASCULAR_OTHER_DRUGS = {
    **ANTIPLATELETS_DRUGS,
    **STATINS_DRUGS,
    **ACE_INHIBITORS_IV_DRUGS,
}

__all__ = [
    'CARDIOVASCULAR_OTHER_DRUGS',
    'ANTIPLATELETS_DRUGS',
    'STATINS_DRUGS',
    'ACE_INHIBITORS_IV_DRUGS'
]

