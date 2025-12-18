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
from .statins import STATINS
from .cholesterol_absorption_inhibitors import CHOLESTEROL_ABSORPTION_INHIBITORS
from .antiarrhythmics import ANTIARRHYTHMICS
from .calcium_blockers import CALCIUM_BLOCKERS
from .diuretics import DIURETICS
from .anticoagulants import ANTICOAGULANTS
from .pcsk9_inhibitors import PCSK9_INHIBITORS
from .triglyceride_lowering import TRIGLYCERIDE_LOWERING_DRUGS
from .fixed_dose_combinations import CARDIOVASCULAR_FIXED_DOSE_COMBINATIONS

# Merge all categories
CARDIOVASCULAR_DRUGS = {
    **OTHER_CV_DRUGS,
    **VASODILATORS,
    **ACE_INHIBITORS,
    **ARBS,
    **BETA_BLOCKERS,
    **STATINS,
    **CHOLESTEROL_ABSORPTION_INHIBITORS,
    **ANTIARRHYTHMICS,
    **CALCIUM_BLOCKERS,
    **DIURETICS,
    **ANTICOAGULANTS,
    **PCSK9_INHIBITORS,
    **TRIGLYCERIDE_LOWERING_DRUGS,
    **CARDIOVASCULAR_FIXED_DOSE_COMBINATIONS,
}

__all__ = ['CARDIOVASCULAR_DRUGS']
