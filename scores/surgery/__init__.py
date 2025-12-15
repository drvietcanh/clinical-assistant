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
from .apfel_ponv import render as render_apfel_ponv
from .koivuranta_ponv import render as render_koivuranta_ponv
from .wilson_risk import render as render_wilson_risk
from .el_ganzouri import render as render_el_ganzouri
from .lemon import render as render_lemon
from .cormack_lehane import render as render_cormack_lehane
from .ramsay import render as render_ramsay
from .rass import render as render_rass
from .riker_sas import render as render_riker_sas
from .padss import render as render_padss
from .ariscat import render as render_ariscat
from .cam_icu import render as render_cam_icu
from .four_at import render as render_4at
from .surgical_apgar import render as render_surgical_apgar
from .sort import render as render_sort
from .gupta_cardiac import render as render_gupta_cardiac
from .goldman_cardiac import render as render_goldman_cardiac


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
        "Apfel PONV": render_apfel_ponv,
        "Koivuranta PONV": render_koivuranta_ponv,
        "Wilson Risk": render_wilson_risk,
        "El-Ganzouri": render_el_ganzouri,
        "LEMON": render_lemon,
        "Cormack-Lehane": render_cormack_lehane,
        "Ramsay": render_ramsay,
        "RASS": render_rass,
        "Riker SAS": render_riker_sas,
        "PADSS": render_padss,
        "ARISCAT": render_ariscat,
        "CAM-ICU": render_cam_icu,
        "4AT": render_4at,
        "Surgical Apgar": render_surgical_apgar,
        "SORT": render_sort,
        "Gupta Cardiac": render_gupta_cardiac,
        "Goldman Cardiac": render_goldman_cardiac,
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

