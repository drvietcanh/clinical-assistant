"""
Emergency Protocols
Sepsis, shock, and critical care protocols organized by individual files
"""

from .sepsis import render as render_sepsis
from .shock import render as render_shock
from .stroke import render as render_stroke
from .gi_bleeding import render as render_gi_bleeding
from .dka import render as render_dka
from .electrolytes import render as render_electrolytes


__all__ = [
    'render_sepsis',
    'render_shock',
    'render_stroke',
    'render_gi_bleeding',
    'render_dka',
    'render_electrolytes',
]

