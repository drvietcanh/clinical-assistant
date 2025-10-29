"""
Emergency & Critical Care Scoring Systems
All emergency and ICU calculators organized by individual files
"""

from .qsofa import render as render_qsofa
from .sofa import render as render_sofa
from .apache2 import render as render_apache2
from .saps2 import render as render_saps2
from .mods import render as render_mods


def render_emergency_calculator(calculator_id):
    """
    Route to the correct emergency calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "qSOFA": render_qsofa,
        "SOFA": render_sofa,
        "APACHE II": render_apache2,
        "SAPS II": render_saps2,
        "MODS": render_mods,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_emergency_calculator',
    'render_qsofa',
    'render_sofa',
    'render_apache2',
    'render_saps2',
    'render_mods',
]

