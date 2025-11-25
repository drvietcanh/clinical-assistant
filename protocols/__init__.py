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
    render_status_epilepticus
)
from .respiratory import render_copd, render_asthma
from .cardiology import render_acs, render_hf, render_atrial_fibrillation, render_dvt_pe
from .nephrology import render_aki
from .infectious import render_cap, render_hap_vap, render_cdiff
from .endocrinology import (
    render_thyrotoxic_crisis,
    render_myxedema_coma,
    render_adrenal_crisis
)
from .oncology import (
    render_tls,
    render_febrile_neutropenia,
    render_hypercalcemia
)

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
    'render_copd',
    'render_asthma',
    'render_acs',
    'render_hf',
    'render_atrial_fibrillation',
    'render_dvt_pe',
    'render_aki',
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
    'render_thyrotoxic_crisis',
    'render_myxedema_coma',
    'render_adrenal_crisis',
    'render_tls',
    'render_febrile_neutropenia',
    'render_hypercalcemia',
]

