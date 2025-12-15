"""
Pediatrics Scoring Systems
Pediatric assessment calculators
"""

from .apgar import render as render_apgar
from .pews import render as render_pews
from .pediatric_gcs import render as render_pediatric_gcs
from .westley_croup import render as render_westley_croup
from .pelod2 import render as render_pelod2
from .prism3 import render as render_prism3
from .pim2 import render as render_pim2
from .pediatric_sofa import render as render_pediatric_sofa
from .pediatric_dosing import render_pediatric_dosing_calculator


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
        "PELOD-2": render_pelod2,
        "PRISM III": render_prism3,
        "PIM2": render_pim2,
        "Pediatric SOFA": render_pediatric_sofa,
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
    'render_pelod2',
    'render_prism3',
    'render_pim2',
    'render_pediatric_sofa',
]

