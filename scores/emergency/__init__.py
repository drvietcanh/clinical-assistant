"""
Emergency & Critical Care Scoring Systems
All emergency and ICU calculators organized by individual files
"""

from .news2 import render as render_news2
from .mews import render as render_mews
from .saps3 import render as render_saps3
from .qsofa import render as render_qsofa
from .sofa import render as render_sofa
from .sofa2 import render as render_sofa2
from .apache2 import render as render_apache2
from .apache3 import render as render_apache3
from .apache4 import render as render_apache4
from .saps2 import render as render_saps2
from .saps3 import render as render_saps3
from .mods import render as render_mods
from .lods import render as render_lods
from .hospital_score import render as render_hospital_score
from .lace_index import render as render_lace_index
from .alvarado import render as render_alvarado
from .rox_index import render as render_rox_index
from .lactate_clearance import render as render_lactate_clearance
from .charlson import render as render_charlson
from .crb65 import render as render_crb65
from .scorten import render as render_scorten
from .rdos import render as render_rdos
from .cpis import render as render_cpis
from .sf_syncope import render as render_sf_syncope


def render_emergency_calculator(calculator_id):
    """
    Route to the correct emergency calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "NEWS2": render_news2,
        "MEWS": render_mews,
        "SAPS III": render_saps3,
        "qSOFA": render_qsofa,
        "SOFA": render_sofa,
        "SOFA-2 (2025)": render_sofa2,
        "APACHE II": render_apache2,
        "APACHE III": render_apache3,
        "APACHE IV": render_apache4,
        "SAPS II": render_saps2,
        "SAPS III": render_saps3,
        "MODS": render_mods,
        "LODS": render_lods,
        "HOSPITAL Score": render_hospital_score,
        "LACE Index": render_lace_index,
        "Alvarado Score": render_alvarado,
        "ROX Index": render_rox_index,
        "Lactate Clearance": render_lactate_clearance,
        "Charlson Index": render_charlson,
        "CRB-65 Score": render_crb65,
        "SCORTEN Score": render_scorten,
        "RDOS": render_rdos,
        "CPIS": render_cpis,
        "San Francisco Syncope": render_sf_syncope,
    }
    
    from utils.errors import safe_render_calculator, CalculatorNotFoundError
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        safe_render_calculator(calculator_func, calculator_id)
    else:
        handle_error = CalculatorNotFoundError(f"Calculator '{calculator_id}' not found in emergency module")
        from utils.errors import handle_calculator_error
        handle_calculator_error(handle_error, calculator_id)


__all__ = [
    'render_emergency_calculator',
    'render_news2',
    'render_mews',
    'render_saps3',
    'render_qsofa',
    'render_sofa',
    'render_sofa2',
    'render_apache2',
    'render_apache3',
    'render_apache4',
    'render_saps2',
    'render_saps3',
    'render_mods',
    'render_lods',
    'render_hospital_score',
    'render_lace_index',
    'render_alvarado',
    'render_rox_index',
    'render_lactate_clearance',
    'render_charlson',
]

