"""
Infectious Disease Protocols
"""

from .cap import render as render_cap
from .hap_vap import render as render_hap_vap
from .cdiff import render as render_cdiff
from .meningitis import render as render_meningitis

__all__ = [
    'render_cap',
    'render_hap_vap',
    'render_cdiff',
    'render_meningitis',
]

