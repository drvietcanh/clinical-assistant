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
]

