"""
Psychiatry & Psychology Scoring Systems
Mental health assessment calculators
"""

from .phq9 import render as render_phq9
from .gad7 import render as render_gad7


def render_psychiatry_calculator(calculator_id):
    """
    Route to the correct psychiatry calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "PHQ-9": render_phq9,
        "GAD-7": render_gad7,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_psychiatry_calculator',
    'render_phq9',
    'render_gad7',
]

