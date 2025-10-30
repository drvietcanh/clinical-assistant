"""
Obstetrics Scoring Systems
All obstetrics calculators organized by individual files
"""

from .bishop import render as render_bishop
from .modified_bishop import render as render_modified_bishop


def render_obstetrics_calculator(calculator_id):
    """
    Route to the correct obstetrics calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    import streamlit as st
    
    calculators = {
        "Bishop Score": render_bishop,
        "Modified Bishop": render_modified_bishop,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")


__all__ = [
    'render_obstetrics_calculator',
    'render_bishop',
    'render_modified_bishop',
]

