"""
Rheumatology Scoring Systems
Rheumatology and immunology calculators
"""


def render_rheumatology_calculator(calculator_id):
    """
    Route to the correct rheumatology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        # Will add calculators here
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_rheumatology_calculator',
]

