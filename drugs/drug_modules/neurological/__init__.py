"""Neurological and Psychiatric Medications
Active module - contains all neurological and psychiatric drug data
Includes: anticonvulsants, antidepressants (SSRI, SNRI, TCA), antipsychotics,
benzodiazepines, Alzheimer/dementia drugs, Parkinson's drugs, ADHD medications, etc."""

# Import all drug categories from neurological subdirectory
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

# Import from psychiatry_other (merged into neurological module)
from ..psychiatry_other.ssris import SSRI_DRUGS
from ..psychiatry_other.snris import SNRI_DRUGS
from ..psychiatry_other.tcas import TCA_DRUGS
from ..psychiatry_other.antipsychotics import ANTIPSYCHOTICS_DRUGS
from ..psychiatry_other.antidepressants import OTHER_ANTIDEPRESSANTS_DRUGS
from ..psychiatry_other.adhd_anxiolytics import ADHD_ANXIOLYTICS_DRUGS

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
    # Merged from psychiatry_other
    **SSRI_DRUGS,
    **SNRI_DRUGS,
    **TCA_DRUGS,
    **ANTIPSYCHOTICS_DRUGS,
    **OTHER_ANTIDEPRESSANTS_DRUGS,
    **ADHD_ANXIOLYTICS_DRUGS,
}

__all__ = ['NEUROLOGICAL_DRUGS']
