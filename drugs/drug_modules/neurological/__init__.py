"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# Import all drug categories
from .anticonvulsants import ANTICONVULSANTS_DRUGS
from .ssri_selective_serotonin_reuptake_inhibitors import SSRI_SELECTIVE_SEROTONIN_REUPTAKE_INHIBITORS_DRUGS
from .anticonvulsant_alpha_2_delta_ligands import ANTICONVULSANT_ALPHA_2_DELTA_LIGANDS_DRUGS

# Merge all categories
NEUROLOGICAL_DRUGS = {
    **ANTICONVULSANTS_DRUGS,
    **SSRI_SELECTIVE_SEROTONIN_REUPTAKE_INHIBITORS_DRUGS,
    **ANTICONVULSANT_ALPHA_2_DELTA_LIGANDS_DRUGS,
}

__all__ = ['NEUROLOGICAL_DRUGS']
