"""
Trauma Scoring Systems
All trauma assessment calculators organized by individual files
"""

from .rts import render as render_rts
from .iss import render as render_iss
from .nexus import render as render_nexus
from .canadian_cspine import render as render_canadian_cspine


def render_trauma_calculator(calculator_id):
    """
    Route to the correct trauma calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "RTS": render_rts,
        "ISS": render_iss,
        "NEXUS": render_nexus,
        "Canadian C-Spine": render_canadian_cspine,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_trauma_calculator',
    'render_rts',
    'render_iss',
    'render_nexus',
    'render_canadian_cspine',
]

