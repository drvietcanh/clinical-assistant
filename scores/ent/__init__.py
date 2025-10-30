"""
ENT (Ear, Nose, Throat) Scoring Systems
All ENT calculators organized by individual files
"""

from .epworth import render as render_epworth
from .stop_bang import render as render_stop_bang


def render_ent_calculator(calculator_id):
    """
    Route to the correct ENT calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Epworth": render_epworth,
        "STOP-BANG": render_stop_bang,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_ent_calculator',
    'render_epworth',
]

