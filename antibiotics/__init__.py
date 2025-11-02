"""
Antibiotics Module - Dosing and TDM Tools
Modular structure for easy maintenance
"""

from .crcl import render as render_crcl
from .vancomycin import render as render_vancomycin
from .aminoglycoside import render as render_aminoglycoside
from .database import render_antibiotic_lookup, render_database
from .dosing_calculator import render_dosing_calculator
from .multi_dosing_comparison import render_multi_comparison

__all__ = [
    'render_crcl',
    'render_vancomycin',
    'render_aminoglycoside',
    'render_antibiotic_lookup',
    'render_database',
    'render_dosing_calculator',
    'render_multi_comparison',
]

