"""
Cardiovascular Drugs Package
All cardiovascular drug modules organized by therapeutic subgroup
"""

from .ace_inhibitors import ACE_INHIBITORS
from .arbs import ARBS
from .beta_blockers import BETA_BLOCKERS
from .calcium_blockers import CALCIUM_BLOCKERS
from .diuretics import DIURETICS
from .antiarrhythmics import ANTIARRHYTHMICS
from .anticoagulants import ANTICOAGULANTS
from .statins import STATINS
from .vasodilators import VASODILATORS
from .other_cv import OTHER_CV_DRUGS

# Merge all cardiovascular drug dictionaries
CARDIOVASCULAR_DRUGS = {
    **ACE_INHIBITORS,
    **ARBS,
    **BETA_BLOCKERS,
    **CALCIUM_BLOCKERS,
    **DIURETICS,
    **ANTIARRHYTHMICS,
    **ANTICOAGULANTS,
    **STATINS,
    **VASODILATORS,
    **OTHER_CV_DRUGS,
}

__all__ = [
    'ACE_INHIBITORS',
    'ARBS',
    'BETA_BLOCKERS',
    'CALCIUM_BLOCKERS',
    'DIURETICS',
    'ANTIARRHYTHMICS',
    'ANTICOAGULANTS',
    'STATINS',
    'VASODILATORS',
    'OTHER_CV_DRUGS',
    'CARDIOVASCULAR_DRUGS',
]
