"""
Surgery & Anesthesia Scoring Systems
Surgical risk assessment calculators
"""

from .asa import render as render_asa
from .aldrete import render as render_aldrete
from .mallampati import render as render_mallampati
from .rcri import render as render_rcri
from .caprini import render as render_caprini
from .possum import render as render_possum


def render_surgery_calculator(calculator_id):
    """
    Route to the correct surgery calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "ASA": render_asa,
        "Aldrete Score": render_aldrete,
        "Mallampati": render_mallampati,
        "RCRI": render_rcri,
        "Caprini": render_caprini,
        "P-POSSUM": render_possum,
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

