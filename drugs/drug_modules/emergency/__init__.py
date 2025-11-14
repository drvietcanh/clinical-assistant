"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Import all drug categories
from .antiarrhythmics import ANTIARRHYTHMICS_DRUGS
from .anticholinergics import ANTICHOLINERGICS_DRUGS
from .benzodiazepine_antagonists import BENZODIAZEPINE_ANTAGONISTS_DRUGS
from .opioid_antagonists import OPIOID_ANTAGONISTS_DRUGS

# Merge all categories
EMERGENCY_DRUGS = {
    **ANTIARRHYTHMICS_DRUGS,
    **ANTICHOLINERGICS_DRUGS,
    **BENZODIAZEPINE_ANTAGONISTS_DRUGS,
    **OPIOID_ANTAGONISTS_DRUGS,
}

__all__ = ['EMERGENCY_DRUGS']
