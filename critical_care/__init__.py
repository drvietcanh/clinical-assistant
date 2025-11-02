"""
Critical Care Module
Fluid therapy, vasopressors, and critical care calculations
"""

from .fluids import render_fluid_calculator
from .vasopressors import render_vasopressor_guide

__all__ = [
    'render_fluid_calculator',
    'render_vasopressor_guide',
]

