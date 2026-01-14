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
from .dengue_fever_vn import render as render_dengue_fever_vn
from .scrub_typhus import render as render_scrub_typhus
from .malaria import render as render_malaria

__all__ = [
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
    'render_meningitis',
    'render_endocarditis',
    'render_parasitic_worms',
    'render_dengue_fever',
    'render_dengue_fever_vn',
    'render_scrub_typhus',
    'render_malaria',
]

