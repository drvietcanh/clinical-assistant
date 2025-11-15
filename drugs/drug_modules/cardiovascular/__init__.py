"""
Cardiovascular Drugs Package
All cardiovascular drug modules organized by therapeutic subgroup
"""

# Import all drug categories
from .other_cv import OTHER_CV_DRUGS
from .vasodilators import VASODILATORS
from .ace_inhibitors import ACE_INHIBITORS
from .arbs import ARBS
from .beta_blockers import BETA_BLOCKERS

# Merge all categories
CARDIOVASCULAR_DRUGS = {
    **OTHER_CV_DRUGS,
    **VASODILATORS,
    **ACE_INHIBITORS,
    **ARBS,
    **BETA_BLOCKERS,
}

__all__ = ['CARDIOVASCULAR_DRUGS']
