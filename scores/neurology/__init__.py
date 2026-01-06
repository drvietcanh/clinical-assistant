"""
Neurology Scoring Systems
All neurological assessment calculators organized by individual files
"""

from .gcs import render as render_gcs
from .nihss import render as render_nihss
from .ich_score import render as render_ich_score
from .hunt_hess import render as render_hunt_hess
from .mrs import render as render_mrs
from .aspects import render as render_aspects
from .abcd2 import render as render_abcd2
from .barthel import render as render_barthel
from .four_score import render as render_four_score
from .canadian_ct_head import render as render_canadian_ct_head
from .fast_ed import render as render_fast_ed
from .icans import render as render_icans
from .sudbury_vertigo import render as render_sudbury_vertigo
from .mgfa import render as render_mgfa
from .mg_adl import render as render_mg_adl
from .ice_score import render as render_ice_score
from .canadian_stroke_scale import render as render_canadian_stroke_scale
from utils.errors import CalculatorNotFoundError, safe_render_calculator


def render_neurology_calculator(calculator_id):
    """
    Route to the correct neurology calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    calculators = {
        "GCS": render_gcs,
        "NIHSS": render_nihss,
        "ICH Score": render_ich_score,
        "Hunt & Hess": render_hunt_hess,
        "mRS": render_mrs,
        "ASPECTS": render_aspects,
        "ABCD2": render_abcd2,
        "Barthel Index": render_barthel,
        "FOUR Score": render_four_score,
        "Canadian CT Head": render_canadian_ct_head,
        "FAST-ED": render_fast_ed,
        "ICANS Consensus Grading": render_icans,
        "Sudbury Vertigo Risk Score": render_sudbury_vertigo,
        "MGFA Clinical Classification": render_mgfa,
        "MG-ADL": render_mg_adl,
        "ICE Score": render_ice_score,
        "Canadian Stroke Scale": render_canadian_stroke_scale,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        safe_render_calculator(calculator_func, calculator_id)
    else:
        raise CalculatorNotFoundError(f"Calculator '{calculator_id}' not found in neurology module")


__all__ = [
    'render_neurology_calculator',
    'render_gcs',
    'render_nihss',
    'render_ich_score',
    'render_hunt_hess',
    'render_mrs',
    'render_aspects',
    'render_abcd2',
    'render_barthel',
    'render_four_score',
    'render_canadian_stroke_scale',
]

