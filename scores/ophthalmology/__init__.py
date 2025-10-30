"""
Ophthalmology Scoring Systems
Eye disease calculators
"""

from .iop_correction import render as render_iop_correction


def render_ophthalmology_calculator(calculator_id):
    """
    Route to the correct ophthalmology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Intraocular Pressure": render_iop_correction,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_ophthalmology_calculator',
    'render_iop_correction',
]

