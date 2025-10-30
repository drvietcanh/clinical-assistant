"""
Psychiatry & Psychology Scoring Systems
Mental health assessment calculators
"""

from .phq9 import render as render_phq9
from .gad7 import render as render_gad7
from .mmse import render as render_mmse
from .moca import render as render_moca
from .cam import render as render_cam
from .ciwa import render as render_ciwa
from .cows import render as render_cows


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
        "MMSE": render_mmse,
        "MoCA": render_moca,
        "CAM": render_cam,
        "CIWA-Ar": render_ciwa,
        "COWS": render_cows,
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

