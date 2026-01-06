"""
Geriatrics Module
Clinical calculators for elderly patients
Frailty, fall risk, cognitive assessment, medication safety
"""

from .cfs import render_cfs
from .morse_fall import render_morse_fall
from .mmse import render_mmse
from .moca import render_moca
from .beers import render_beers
from .stopp_start import render_stopp_start

def render_geriatrics_calculator(score_id: str):
    """Main router for geriatrics calculators"""
    
    calculator_map = {
        "CFS": render_cfs,
        "Morse Fall Scale": render_morse_fall,
        "MMSE": render_mmse,
        "MoCA": render_moca,
        "Beers Criteria": render_beers,
        "STOPP/START": render_stopp_start,
    }
    
    # Try to find matching calculator
    for key, render_func in calculator_map.items():
        if key in score_id or score_id in key:
            render_func(score_id)
            return
    
    # Fallback: try direct match
    if score_id in calculator_map:
        calculator_map[score_id](score_id)
        return
    
    # If no match found
    import streamlit as st
    st.error(f"Calculator '{score_id}' chưa được implement trong module Geriatrics")

__all__ = [
    'render_cfs',
    'render_morse_fall',
    'render_mmse',
    'render_moca',
    'render_beers',
    'render_stopp_start',
    'render_geriatrics_calculator',
]
