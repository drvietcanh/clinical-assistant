"""
Cardiology Protocols
ACS, Heart Failure, and cardiac emergency protocols organized by individual files
"""

from .acs import render as render_acs
from .heart_failure import render as render_hf
from .acute_decompensated_hf import render as render_acute_decompensated_hf
from .atrial_fibrillation import render as render_atrial_fibrillation
from .dvt_pe import render as render_dvt_pe
from .bradycardia import render as render_bradycardia
from .tachycardia import render as render_tachycardia


__all__ = [
    'render_acs',
    'render_hf',
    'render_acute_decompensated_hf',
    'render_atrial_fibrillation',
    'render_dvt_pe',
    'render_bradycardia',
    'render_tachycardia',
]

