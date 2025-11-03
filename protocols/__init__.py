"""
Protocols Module - Clinical Treatment Protocols
Modular structure for easy maintenance
"""

from .emergency import (
    render_sepsis,
    render_shock,
    render_stroke,
    render_gi_bleeding,
    render_dka,
    render_electrolytes
)
from .respiratory import render_copd, render_asthma
from .cardiology import render_acs, render_hf
from .nephrology import render_aki

__all__ = [
    'render_sepsis',
    'render_shock',
    'render_stroke',
    'render_gi_bleeding',
    'render_dka',
    'render_electrolytes',
    'render_copd',
    'render_asthma',
    'render_acs',
    'render_hf',
    'render_aki',
]

