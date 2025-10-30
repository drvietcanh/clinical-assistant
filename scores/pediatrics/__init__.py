"""
Pediatrics Scoring Systems
Pediatric assessment calculators
"""

from .apgar import render as render_apgar
from .pews import render as render_pews
from .pediatric_gcs import render as render_pediatric_gcs
from .westley_croup import render as render_westley_croup


def render_pediatrics_calculator(calculator_id):
    """
    Route to the correct pediatrics calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Westley Croup": render_westley_croup,
        "APGAR": render_apgar,
        "PEWS": render_pews,
        "Pediatric GCS": render_pediatric_gcs,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_pediatrics_calculator',
    'render_apgar',
    'render_pews',
    'render_pediatric_gcs',
]

