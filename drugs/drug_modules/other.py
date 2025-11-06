"""
Other Common Medications
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules:
- cardiovascular_other.py: Cardiovascular drugs (antiplatelets, statins, ACE IV)
- infectious_other.py: Infectious disease & antibiotic drugs
- psychiatry_other.py: Psychiatry drugs (SSRIs, SNRIs, TCAs)
- endocrinology_other.py: Endocrinology drugs (corticosteroids)
- miscellaneous.py: Miscellaneous drugs (metabolism, respiratory, analgesic, hematology)
"""

# Import split modules
from .cardiovascular_other import CARDIOVASCULAR_OTHER_DRUGS
from .infectious_other import INFECTIOUS_OTHER_DRUGS
from .psychiatry_other import PSYCHIATRY_OTHER_DRUGS
from .endocrinology_other import ENDOCRINOLOGY_OTHER_DRUGS
from .miscellaneous import MISCELLANEOUS_DRUGS

# Merge all split modules to maintain backward compatibility
OTHER_DRUGS = {
    **CARDIOVASCULAR_OTHER_DRUGS,
    **INFECTIOUS_OTHER_DRUGS,
    **PSYCHIATRY_OTHER_DRUGS,
    **ENDOCRINOLOGY_OTHER_DRUGS,
    **MISCELLANEOUS_DRUGS,
}

__all__ = ['OTHER_DRUGS']
