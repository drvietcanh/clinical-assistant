"""
Nephrology Scoring Systems
All nephrology assessment calculators organized by individual files
"""

from .kdigo import render as render_kdigo
from .rifle import render as render_rifle
from .akin import render as render_akin
from .egfr import render as render_egfr


def render_nephrology_calculator(calculator_id):
    """
    Route to the correct nephrology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "KDIGO": render_kdigo,
        "RIFLE": render_rifle,
        "AKIN": render_akin,
        "eGFR": render_egfr,
    }

    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_nephrology_calculator',
    'render_kdigo',
    'render_rifle',
    'render_akin',
]

