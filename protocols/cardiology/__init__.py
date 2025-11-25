"""
Cardiology Protocols
ACS, Heart Failure, and cardiac emergency protocols organized by individual files
"""

from .acs import render as render_acs
from .heart_failure import render as render_hf
from .atrial_fibrillation import render as render_atrial_fibrillation
from .dvt_pe import render as render_dvt_pe


__all__ = [
    'render_acs',
    'render_hf',
    'render_atrial_fibrillation',
    'render_dvt_pe',
]

