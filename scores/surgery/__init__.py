"""
Surgery & Anesthesia Scoring Systems
Surgical risk assessment calculators
"""

from .asa import render as render_asa


def render_surgery_calculator(calculator_id):
    """
    Route to the correct surgery calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "ASA": render_asa,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_surgery_calculator',
    'render_asa',
]

