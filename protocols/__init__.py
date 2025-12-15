"""
Protocols Module - Clinical Treatment Protocols
Modular structure for easy maintenance
"""

from .emergency import (
    render_sepsis,
    render_sepsis_3hour,
    render_shock,
    render_stroke,
    render_gi_bleeding,
    render_dka,
    render_electrolytes,
    render_anaphylaxis,
    render_hypertensive_emergency,
    render_status_epilepticus,
    render_opioid_overdose,
    render_alcohol_withdrawal,
    render_paracetamol_overdose,
    render_salicylate_overdose,
    render_carbon_monoxide_poisoning,
    render_organophosphate_poisoning,
    render_toxic_alcohol_poisoning,
    render_malignant_arrhythmias,
    render_pneumothorax,
    render_traumatic_brain_injury,
    render_drowning,
    render_heat_stroke,
    render_hypothermia
)
from .pain import render_acute_pain
from .respiratory import render_copd, render_asthma
from .cardiology import render_acs, render_hf, render_atrial_fibrillation, render_dvt_pe, render_bradycardia, render_tachycardia
from .nephrology import render_aki
from .infectious import render_cap, render_hap_vap, render_cdiff, render_meningitis, render_endocarditis
from .endocrinology import (
    render_thyrotoxic_crisis,
    render_myxedema_coma,
    render_adrenal_crisis,
    render_hhs,
    render_hypoglycemia
)
from .neurology import render_serotonin_syndrome, render_neuroleptic_malignant_syndrome, render_intracranial_hypertension
from .obstetrics import render_eclampsia, render_postpartum_hemorrhage
from .dermatology import render_stevens_johnson_syndrome
from .gastroenterology import render_acute_pancreatitis, render_acute_liver_failure, render_ibd_exacerbation
from .hematology import render_transfusion, render_anticoagulation_reversal
from .oncology import (
    render_tls,
    render_febrile_neutropenia,
    render_hypercalcemia
)
from .critical_care import render_delirium, render_sedation, render_ards, render_ventilator_weaning, render_stress_ulcer
from .rheumatology import render_acute_gout, render_ra_flare

__all__ = [
    'render_sepsis',
    'render_sepsis_3hour',
    'render_shock',
    'render_stroke',
    'render_gi_bleeding',
    'render_dka',
    'render_electrolytes',
    'render_anaphylaxis',
    'render_hypertensive_emergency',
    'render_status_epilepticus',
    'render_opioid_overdose',
    'render_alcohol_withdrawal',
    'render_paracetamol_overdose',
    'render_salicylate_overdose',
    'render_carbon_monoxide_poisoning',
    'render_organophosphate_poisoning',
    'render_toxic_alcohol_poisoning',
    'render_malignant_arrhythmias',
    'render_pneumothorax',
    'render_traumatic_brain_injury',
    'render_drowning',
    'render_heat_stroke',
    'render_hypothermia',
    'render_acute_pain',
    'render_copd',
    'render_asthma',
    'render_acs',
    'render_hf',
    'render_atrial_fibrillation',
    'render_dvt_pe',
    'render_bradycardia',
    'render_tachycardia',
    'render_aki',
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
    'render_meningitis',
    'render_endocarditis',
    'render_thyrotoxic_crisis',
    'render_myxedema_coma',
    'render_adrenal_crisis',
    'render_hhs',
    'render_hypoglycemia',
    'render_serotonin_syndrome',
    'render_neuroleptic_malignant_syndrome',
    'render_intracranial_hypertension',
    'render_eclampsia',
    'render_postpartum_hemorrhage',
    'render_stevens_johnson_syndrome',
    'render_acute_pancreatitis',
    'render_acute_liver_failure',
    'render_transfusion',
    'render_anticoagulation_reversal',
    'render_tls',
    'render_febrile_neutropenia',
    'render_hypercalcemia',
    'render_delirium',
    'render_sedation',
    'render_ards',
    'render_ventilator_weaning',
    'render_stress_ulcer',
    'render_acute_gout',
    'render_ra_flare',
    'render_ibd_exacerbation',
]

