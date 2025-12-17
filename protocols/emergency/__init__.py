"""
Emergency Protocols
Sepsis, shock, and critical care protocols organized by individual files
"""

from .sepsis import render as render_sepsis
from .sepsis_3hour import render as render_sepsis_3hour
from .shock import render as render_shock
from .stroke import render as render_stroke
from .gi_bleeding import render as render_gi_bleeding
from .dka import render as render_dka
from .electrolytes import render as render_electrolytes
from .anaphylaxis import render as render_anaphylaxis
from .hypertensive_emergency import render as render_hypertensive_emergency
from .status_epilepticus import render as render_status_epilepticus
from .opioid_overdose import render as render_opioid_overdose
from .alcohol_withdrawal import render as render_alcohol_withdrawal
from .paracetamol_overdose import render as render_paracetamol_overdose
from .salicylate_overdose import render as render_salicylate_overdose
from .carbon_monoxide_poisoning import render as render_carbon_monoxide_poisoning
from .organophosphate_poisoning import render as render_organophosphate_poisoning
from .toxic_alcohol_poisoning import render as render_toxic_alcohol_poisoning
from .malignant_arrhythmias import render as render_malignant_arrhythmias
from .pneumothorax import render as render_pneumothorax
from .traumatic_brain_injury import render as render_traumatic_brain_injury
from .drowning import render as render_drowning
from .heat_stroke import render as render_heat_stroke
from .hypothermia import render as render_hypothermia
from .cardiac_arrest import render as render_cardiac_arrest
from .upper_airway_obstruction import render as render_upper_airway_obstruction
from .spinal_cord_injury import render as render_spinal_cord_injury
from .green_pit_viper_bite import render as render_green_pit_viper_bite
from .cobra_bite import render as render_cobra_bite
from .krait_bite import render as render_krait_bite


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
    'render_cardiac_arrest',
    'render_upper_airway_obstruction',
    'render_spinal_cord_injury',
    'render_green_pit_viper_bite',
    'render_cobra_bite',
    'render_krait_bite',
]

