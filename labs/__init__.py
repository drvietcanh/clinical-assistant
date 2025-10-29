"""
Labs Module - Laboratory Values & Interpretation
Modular structure - Each panel in its own file for easy maintenance
"""

from .normal_ranges import get_normal_range, is_critical, interpret_value
from .converter import convert_units

# Import individual panels (each in separate file)
from .cbc import render as render_cbc
from .bmp import render as render_bmp
from .cmp import render as render_cmp
from .lft import render as render_lft
from .lipid import render as render_lipid
from .cardiac import render as render_cardiac_markers
from .coag import render as render_coag
from .thyroid import render as render_thyroid
from .abg import render as render_abg

__all__ = [
    # Core functions
    'get_normal_range',
    'is_critical',
    'interpret_value',
    'convert_units',
    
    # Lab panels
    'render_cbc',
    'render_cmp',
    'render_bmp',
    'render_lft',
    'render_lipid',
    'render_cardiac_markers',
    'render_coag',
    'render_thyroid',
    'render_abg',
]

