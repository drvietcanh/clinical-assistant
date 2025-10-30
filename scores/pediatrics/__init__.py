"""
Pediatrics Scoring Systems
Pediatric assessment calculators
"""

from .apgar import render as render_apgar


def render_pediatrics_calculator(calculator_id):
    """
    Route to the correct pediatrics calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "APGAR": render_apgar,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_pediatrics_calculator',
    'render_apgar',
]

