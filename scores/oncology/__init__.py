"""
Oncology Scoring Systems
Cancer assessment calculators
"""

from .ecog import render as render_ecog


def render_oncology_calculator(calculator_id):
    """
    Route to the correct oncology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "ECOG": render_ecog,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_oncology_calculator',
    'render_ecog',
]

