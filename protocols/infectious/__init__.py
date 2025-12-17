"""
Infectious Disease Protocols
"""

from .cap import render as render_cap
from .hap_vap import render as render_hap_vap
from .cdiff import render as render_cdiff
from .meningitis import render as render_meningitis
from .endocarditis import render as render_endocarditis
from .parasitic_worms import render as render_parasitic_worms
from .dengue_fever import render as render_dengue_fever

__all__ = [
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
    'render_meningitis',
    'render_endocarditis',
    'render_parasitic_worms',
    'render_dengue_fever',
]

