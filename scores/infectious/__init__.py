"""
Infectious Disease Scoring Systems
Infection assessment calculators
"""

from .centor import render as render_centor


def render_infectious_calculator(calculator_id):
    """
    Route to the correct infectious disease calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Centor": render_centor,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_infectious_calculator',
    'render_centor',
]

