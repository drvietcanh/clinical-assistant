"""
Rheumatology Scoring Systems
Rheumatology and immunology calculators
"""

from .das28 import render as render_das28
from .cdai import render as render_cdai
from .sdai import render as render_sdai
from .acr_ra import render as render_acr_ra
from .slicc import render as render_slicc
from .sledai import render as render_sledai
from .gout import render as render_gout


def render_rheumatology_calculator(calculator_id):
    """
    Route to the correct rheumatology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "DAS28": render_das28,
        "CDAI": render_cdai,
        "SDAI": render_sdai,
        "ACR Criteria": render_acr_ra,
        "SLICC": render_slicc,
        "SLEDAI": render_sledai,
        "Gout Diagnostic": render_gout,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_rheumatology_calculator',
]

