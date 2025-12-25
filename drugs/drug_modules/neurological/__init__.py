"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data"""

# Import all drug categories
from .anticonvulsants import ANTICONVULSANTS_DRUGS
from .ssri_selective_serotonin_reuptake_inhibitors import SSRI_SELECTIVE_SEROTONIN_REUPTAKE_INHIBITORS_DRUGS
from .anticonvulsant_alpha_2_delta_ligands import ANTICONVULSANT_ALPHA_2_DELTA_LIGANDS_DRUGS
from .alzheimer_dementia_drugs import ALZHEIMER_DEMENTIA_DRUGS
from .benzodiazepines import BENZODIAZEPINES_DRUGS
from .muscle_relaxants import MUSCLE_RELAXANTS_DRUGS
from .antiparkinsonian import ANTIPARKINSONIAN_DRUGS
from .cerebral_circulation import CEREBRAL_CIRCULATION_DRUGS
from .neurological_combinations import NEUROLOGICAL_COMBINATIONS_DRUGS
from .migraine_cgrp_drugs import MIGRAINE_CGRP_DRUGS
from .multiple_sclerosis_drugs import MULTIPLE_SCLEROSIS_DRUGS

# Merge all categories
NEUROLOGICAL_DRUGS = {
    **ANTICONVULSANTS_DRUGS,
    **SSRI_SELECTIVE_SEROTONIN_REUPTAKE_INHIBITORS_DRUGS,
    **ANTICONVULSANT_ALPHA_2_DELTA_LIGANDS_DRUGS,
    **ALZHEIMER_DEMENTIA_DRUGS,
    **BENZODIAZEPINES_DRUGS,
    **MUSCLE_RELAXANTS_DRUGS,
    **ANTIPARKINSONIAN_DRUGS,
    **CEREBRAL_CIRCULATION_DRUGS,
    **NEUROLOGICAL_COMBINATIONS_DRUGS,
    **MIGRAINE_CGRP_DRUGS,
    **MULTIPLE_SCLEROSIS_DRUGS,
}

__all__ = ['NEUROLOGICAL_DRUGS']
