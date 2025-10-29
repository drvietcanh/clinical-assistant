"""
Neurology Scoring Systems
All neurological assessment calculators organized by individual files
"""

from .gcs import render as render_gcs
from .nihss import render as render_nihss
from .ich_score import render as render_ich_score
from .hunt_hess import render as render_hunt_hess
from .mrs import render as render_mrs


def render_neurology_calculator(calculator_id):
    """
    Route to the correct neurology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "GCS": render_gcs,
        "NIHSS": render_nihss,
        "ICH Score": render_ich_score,
        "Hunt & Hess": render_hunt_hess,
        "mRS": render_mrs,  # ✅ ALL NEUROLOGY SCORES COMPLETE!
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_neurology_calculator',
    'render_gcs',
    'render_nihss',
    'render_ich_score',
    'render_hunt_hess',
    'render_mrs',
]

