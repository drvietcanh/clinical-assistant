"""
Metabolism & Lab Calculators
Basic clinical calculations used daily
"""

from .anion_gap import render as render_anion_gap
from .corrected_calcium import render as render_corrected_calcium
from .fena import render as render_fena


def render_metabolism_calculator(calculator_id):
    """
    Route to the correct metabolism calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Anion Gap": render_anion_gap,
        "Corrected Ca": render_corrected_calcium,
        "FENa": render_fena,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_metabolism_calculator',
    'render_anion_gap',
    'render_corrected_calcium',
    'render_fena',
]

