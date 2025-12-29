"""
Cardiovascular Drugs Package
All cardiovascular drug modules organized by therapeutic subgroup
Includes: ACE inhibitors, ARBs, beta-blockers, calcium blockers, diuretics,
antiarrhythmics, anticoagulants, statins, antiplatelets, vasodilators, etc.
"""

# Import all drug categories from cardiovascular subdirectory
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

# Import from cardiovascular_other (merged into main cardiovascular module)
from ..cardiovascular_other.antiplatelets import ANTIPLATELETS_DRUGS
from ..cardiovascular_other.statins import STATINS_DRUGS as STATINS_OTHER_DRUGS
from ..cardiovascular_other.ace_inhibitors_iv import ACE_INHIBITORS_IV_DRUGS

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
    # Merged from cardiovascular_other
    **ANTIPLATELETS_DRUGS,
    **STATINS_OTHER_DRUGS,
    **ACE_INHIBITORS_IV_DRUGS,
}

__all__ = ['CARDIOVASCULAR_DRUGS']
