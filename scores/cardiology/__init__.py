"""
Cardiology Scoring Systems
All cardiac risk calculators organized by individual files
"""

from .cha2ds2vasc import render as render_cha2ds2vasc
from .hasbled import render as render_hasbled
from .score2 import render as render_score2
from .score2_op import render as render_score2_op
from .heart import render as render_heart_score
from .timi import render as render_timi_risk
from .grace import render as render_grace_score
from .framingham import render as render_framingham
from .qtc import render as render_qtc


def render_cardiology_calculator(calculator_id):
    """
    Route to the correct cardiology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "CHA2DS2-VASc": render_cha2ds2vasc,
        "HAS-BLED": render_hasbled,
        "SCORE2": render_score2,
        "SCORE2-OP": render_score2_op,
        "HEART Score": render_heart_score,
        "TIMI Risk": render_timi_risk,
        "GRACE Score": render_grace_score,
        "Framingham": render_framingham,
        "Corrected QT": render_qtc,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_cardiology_calculator',
    'render_cha2ds2vasc',
    'render_hasbled',
    'render_score2',
    'render_score2_op',
    'render_heart_score',
    'render_timi_risk',
    'render_grace_score',
    'render_framingham',
    'render_qtc',
]

