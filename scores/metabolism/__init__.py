"""
Metabolism & Lab Calculators
Basic clinical calculations used daily
"""

from .anion_gap import render as render_anion_gap
from .corrected_calcium import render as render_corrected_calcium
from .fena import render as render_fena
from .hba1c_eag import render as render_hba1c_eag
from .winter_formula import render as render_winter_formula
from .free_t4_index import render as render_free_t4_index
from .osmolality import render as render_osmolality


def render_metabolism_calculator(calculator_id):
    """
    Route to the correct metabolism calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Osmolality": render_osmolality,
        "Anion Gap": render_anion_gap,
        "Corrected Ca": render_corrected_calcium,
        "FENa": render_fena,
        "HbA1c": render_hba1c_eag,
        "Winter Formula": render_winter_formula,
        "Free T4 Index": render_free_t4_index,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_metabolism_calculator',
    'render_anion_gap',
    'render_corrected_calcium',
    'render_fena',
    'render_hba1c_eag',
    'render_winter_formula',
]

