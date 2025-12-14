"""
Emergency & Critical Care Scoring Systems
All emergency and ICU calculators organized by individual files
"""

from .news2 import render as render_news2
from .mews import render as render_mews
from .saps3 import render as render_saps3
from .qsofa import render as render_qsofa
from .sofa import render as render_sofa
from .sofa2 import render as render_sofa2
from .apache2 import render as render_apache2
from .saps2 import render as render_saps2
from .saps3 import render as render_saps3
from .mods import render as render_mods
from .lods import render as render_lods


def render_emergency_calculator(calculator_id):
    """
    Route to the correct emergency calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "NEWS2": render_news2,
        "MEWS": render_mews,
        "SAPS III": render_saps3,
        "qSOFA": render_qsofa,
        "SOFA": render_sofa,
        "SOFA-2 (2025)": render_sofa2,
        "APACHE II": render_apache2,
        "SAPS II": render_saps2,
        "SAPS III": render_saps3,
        "MODS": render_mods,
        "LODS": render_lods,
    }
    
    from utils.errors import safe_render_calculator, CalculatorNotFoundError
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        safe_render_calculator(calculator_func, calculator_id)
    else:
        handle_error = CalculatorNotFoundError(f"Calculator '{calculator_id}' not found in emergency module")
        from utils.errors import handle_calculator_error
        handle_calculator_error(handle_error, calculator_id)


__all__ = [
    'render_emergency_calculator',
    'render_news2',
    'render_mews',
    'render_saps3',
    'render_qsofa',
    'render_sofa',
    'render_sofa2',
    'render_apache2',
    'render_saps2',
    'render_saps3',
    'render_mods',
    'render_lods',
]

