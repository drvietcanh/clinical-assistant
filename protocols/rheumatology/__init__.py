"""
Rheumatology Protocols
"""

from .acute_gout import render as render_acute_gout
from .ra_flare import render as render_ra_flare

__all__ = [
    'render_acute_gout',
    'render_ra_flare',
]

