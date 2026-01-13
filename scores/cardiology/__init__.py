"""
Cardiology Scoring Systems
All cardiac risk calculators organized by individual files
"""

from .ascvd import render as render_ascvd
from .cha2ds2vasc import render as render_cha2ds2vasc
from .hasbled import render as render_hasbled
from .score2 import render as render_score2
from .score2_op import render as render_score2_op
from .heart import render as render_heart_score
from .timi import render as render_timi_risk
from .grace import render as render_grace_score
from .crusade import render as render_crusade
from .framingham import render as render_framingham
from .precise_dapt import render as render_precise_dapt
from .dapt_score import render as render_dapt_score
from .qtc import render as render_qtc
from .nyha import render as render_nyha
from .killip import render as render_killip
from .duke import render as render_duke
from .arc_hbr import render as render_arc_hbr
from .pcp_hf import render as render_pcp_hf
from .euroscore2 import render as render_euroscore2
from .atria import render as render_atria
from .orbit import render as render_orbit
from .same_tt2r2 import render as render_same_tt2r2
from .duke_treadmill import render as render_duke_treadmill
# Cardio-Oncology calculators
from .cardio_oncology.hfa_icos_multiple_myeloma import render as render_hfa_icos_multiple_myeloma
from .cardio_oncology.hfa_icos_cml import render as render_hfa_icos_cml
from .cardio_oncology.hfa_icos_raf_mek import render as render_hfa_icos_raf_mek
from .cardio_oncology.hfa_icos_vegf import render as render_hfa_icos_vegf
from .cardio_oncology.hfa_icos_her2 import render as render_hfa_icos_her2
from .cardio_oncology.hfa_icos_anthracycline import render as render_hfa_icos_anthracycline


def render_cardiology_calculator(calculator_id):
    """
    Route to the correct cardiology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "ASCVD Risk": render_ascvd,
        "NYHA": render_nyha,
        "Killip": render_killip,
        "Duke": render_duke,
        "CHA2DS2-VASc": render_cha2ds2vasc,
        "HAS-BLED": render_hasbled,
        "SCORE2": render_score2,
        "SCORE2-OP": render_score2_op,
        "HEART Score": render_heart_score,
        "TIMI Risk": render_timi_risk,
        "GRACE Score": render_grace_score,
        "CRUSADE Score": render_crusade,
        "Framingham": render_framingham,
        "Corrected QT": render_qtc,
        "PRECISE-DAPT": render_precise_dapt,
        "DAPT Score": render_dapt_score,
        "ARC-HBR Criteria": render_arc_hbr,
        "PCP-HF Risk Score": render_pcp_hf,
        "EuroSCORE II": render_euroscore2,
        "ATRIA Bleeding Risk": render_atria,
        "ORBIT Bleeding Risk": render_orbit,
        "SAMe-TT₂R₂": render_same_tt2r2,
        "Duke Treadmill": render_duke_treadmill,
        # Cardio-Oncology
        "HFA-ICOS Multiple Myeloma": render_hfa_icos_multiple_myeloma,
        "HFA-ICOS CML TKI": render_hfa_icos_cml,
        "HFA-ICOS RAF/MEK": render_hfa_icos_raf_mek,
        "HFA-ICOS VEGF": render_hfa_icos_vegf,
        "HFA-ICOS HER2": render_hfa_icos_her2,
        "HFA-ICOS Anthracycline": render_hfa_icos_anthracycline,
    }
    
    from utils.errors import safe_render_calculator, CalculatorNotFoundError
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        safe_render_calculator(calculator_func, calculator_id)
    else:
        handle_error = CalculatorNotFoundError(f"Calculator '{calculator_id}' not found in cardiology module")
        from utils.errors import handle_calculator_error
        handle_calculator_error(handle_error, calculator_id)


__all__ = [
    'render_cardiology_calculator',
    'render_ascvd',
    'render_cha2ds2vasc',
    'render_hasbled',
    'render_score2',
    'render_score2_op',
    'render_heart_score',
    'render_timi_risk',
    'render_grace_score',
    'render_crusade',
    'render_framingham',
    'render_qtc',
]

