"""
Pain Assessment Scales Module
Thang điểm đánh giá đau
"""

from .nrs import render as render_nrs
from .vas import render as render_vas
from .flacc import render as render_flacc
from .nips import render as render_nips
from .wong_baker import render as render_wong_baker
from .dn4 import render as render_dn4


def render_pain_calculator(calculator_id: str):
    """Route to appropriate pain calculator"""
    calculators = {
        "NRS": render_nrs,
        "VAS": render_vas,
        "FLACC": render_flacc,
        "NIPS": render_nips,
        "Wong-Baker": render_wong_baker,
        "DN4": render_dn4,
    }
    
    if calculator_id in calculators:
        calculators[calculator_id]()
    else:
        import streamlit as st
        st.error(f"Calculator '{calculator_id}' not found in pain module")

