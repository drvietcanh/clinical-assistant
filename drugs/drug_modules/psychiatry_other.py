"""
Psychiatry Drugs (Other) - SSRIs, SNRIs, TCAs
NOTE: This module has been split into smaller modules for better maintainability.
This file now imports and merges the split modules to maintain backward compatibility.

Split modules in psychiatry_other/:
- ssris.py: SSRI (Selective Serotonin Reuptake Inhibitor) drugs
- snris.py: SNRI (Serotonin-Norepinephrine Reuptake Inhibitor) drugs
- tcas.py: TCA (Tricyclic Antidepressant) drugs
"""

# Import from psychiatry_other subdirectory
from .psychiatry_other import PSYCHIATRY_OTHER_DRUGS

__all__ = ['PSYCHIATRY_OTHER_DRUGS']
