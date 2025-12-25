"""Emergency and ACLS Medications
Active module - contains all emergency and ACLS drug data"""

# Import all drug categories
from .antiarrhythmics import ANTIARRHYTHMICS_DRUGS
from .anticholinergics import ANTICHOLINERGICS_DRUGS
from .benzodiazepine_antagonists import BENZODIAZEPINE_ANTAGONISTS_DRUGS
from .opioid_antagonists import OPIOID_ANTAGONISTS_DRUGS
from .catecholamine_alpha__beta_agonists import CATECHOLAMINE_ALPHA_BETA_AGONISTS_DRUGS
from .local_anesthetic__antiarrhythmic_class_ibs import LOCAL_ANESTHETIC_ANTIARRHYTHMIC_CLASS_IB_DRUGS
from .electrolytes import ELECTROLYTES_DRUGS
from .uterotonics import UTEROTONICS_DRUGS
from .neuromuscular_blockers import NEUROMUSCULAR_BLOCKERS_DRUGS

# Merge all categories
EMERGENCY_DRUGS = {
    **ANTIARRHYTHMICS_DRUGS,
    **ANTICHOLINERGICS_DRUGS,
    **BENZODIAZEPINE_ANTAGONISTS_DRUGS,
    **OPIOID_ANTAGONISTS_DRUGS,
    **CATECHOLAMINE_ALPHA_BETA_AGONISTS_DRUGS,
    **LOCAL_ANESTHETIC_ANTIARRHYTHMIC_CLASS_IB_DRUGS,
    **ELECTROLYTES_DRUGS,
    **UTEROTONICS_DRUGS,
    **NEUROMUSCULAR_BLOCKERS_DRUGS,
}

__all__ = ['EMERGENCY_DRUGS']
