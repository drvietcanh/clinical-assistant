"""
Hematology Scoring Systems
All hematology assessment calculators organized by individual files
"""

from .wells_dvt import render as render_wells_dvt
from .four_ts import render as render_four_ts
from .dic_score import render as render_dic_score
from .padua import render as render_padua
from .warfarin_dosing import render as render_warfarin_dosing
from .inr_target import render as render_inr_target
from .bleeding_risk import render as render_bleeding_risk


def render_hematology_calculator(calculator_id):
    """
    Route to the correct hematology calculator based on ID

    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st

    calculators = {
        "Padua": render_padua,
        "Wells DVT": render_wells_dvt,
        "4Ts Score": render_four_ts,
        "DIC Score": render_dic_score,
        "Warfarin Dosing": render_warfarin_dosing,
        "INR Target": render_inr_target,
        "Bleeding Risk": render_bleeding_risk,
    }

    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_hematology_calculator',
    'render_wells_dvt',
    'render_four_ts',
    'render_dic_score',
    'render_warfarin_dosing',
    'render_inr_target',
    'render_bleeding_risk',
]

