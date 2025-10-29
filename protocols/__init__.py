"""
Protocols Module - Clinical Treatment Protocols
Modular structure for easy maintenance
"""

from .emergency import render_sepsis, render_shock
from .respiratory import render_copd, render_asthma
from .cardiology import render_acs, render_hf

__all__ = [
    'render_sepsis',
    'render_shock',
    'render_copd',
    'render_asthma',
    'render_acs',
    'render_hf',
]

