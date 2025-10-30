"""
Dermatology Scoring Systems
Skin disease calculators
"""

from .pasi import render as render_pasi
from .scorad import render as render_scorad
from .dlqi import render as render_dlqi
from .burn_tbsa import render as render_burn_tbsa
from .parkland import render as render_parkland


def render_dermatology_calculator(calculator_id):
    """
    Route to the correct dermatology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "PASI": render_pasi,
        "SCORAD": render_scorad,
        "DLQI": render_dlqi,
        "Burn TBSA": render_burn_tbsa,
        "Parkland Formula": render_parkland,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_dermatology_calculator',
]

