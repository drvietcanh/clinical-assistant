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
]

