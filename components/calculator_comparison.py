"""
Calculator Comparison Component
Compare multiple scores/calculators side by side
"""

import streamlit as st
from typing import List, Dict, Optional
import pandas as pd


def render_calculator_comparison(
    calculators: List[Dict[str, any]],
    comparison_fields: List[str] = None
) -> None:
    """
    Render side-by-side comparison of multiple calculators
    
    Args:
        calculators: List of calculator dicts with 'name', 'result', 'interpretation', etc.
        comparison_fields: List of fields to compare (default: ['name', 'result', 'interpretation'])
    """
    if not calculators:
        st.info("No calculators to compare")
        return
    
    if comparison_fields is None:
        comparison_fields = ['name', 'result', 'interpretation', 'risk_level']
    
    # Create comparison table
    comparison_data = []
    for calc in calculators:
        row = {}
        for field in comparison_fields:
            row[field] = calc.get(field, 'N/A')
        comparison_data.append(row)
    
    df = pd.DataFrame(comparison_data)
    
    # Display as table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    # Display as cards for better visualization
    num_cols = min(len(calculators), 3)
    cols = st.columns(num_cols)
    
    for idx, calc in enumerate(calculators):
        with cols[idx % num_cols]:
            st.markdown(f"### {calc.get('name', 'Calculator')}")
            st.metric("Result", calc.get('result', 'N/A'))
            
            interpretation = calc.get('interpretation', '')
            if interpretation:
                st.info(interpretation)
            
            risk_level = calc.get('risk_level', '')
            if risk_level:
                st.warning(f"Risk: {risk_level}")


def render_batch_calculation_input(
    num_patients: int = 5
) -> List[Dict[str, any]]:
    """
    Render input form for batch calculations
    
    Args:
        num_patients: Number of patients to calculate for
    
    Returns:
        List of patient data dicts
    """
    st.markdown("### Batch Calculation")
    st.caption(f"Enter data for {num_patients} patients")
    
    patients = []
    
    for i in range(num_patients):
        with st.expander(f"Patient {i+1}", expanded=(i == 0)):
            patient_data = {}
            
            col1, col2 = st.columns(2)
            with col1:
                patient_data['age'] = st.number_input(
                    "Age",
                    min_value=0,
                    max_value=150,
                    value=65,
                    key=f"age_{i}"
                )
                patient_data['gender'] = st.selectbox(
                    "Gender",
                    ["Male", "Female"],
                    key=f"gender_{i}"
                )
            
            with col2:
                patient_data['weight'] = st.number_input(
                    "Weight (kg)",
                    min_value=0.0,
                    value=70.0,
                    key=f"weight_{i}"
                )
                patient_data['height'] = st.number_input(
                    "Height (cm)",
                    min_value=0.0,
                    value=170.0,
                    key=f"height_{i}"
                )
            
            patients.append(patient_data)
    
    return patients


# Export
__all__ = [
    'render_calculator_comparison',
    'render_batch_calculation_input',
]

