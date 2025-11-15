"""
FENa - Fractional Excretion of Sodium
Phân biệt AKI tiền thận (prerenal) vs thận (intrinsic renal)

Formula:
FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100

Interpretation:
- FENa < 1%: Prerenal AKI (hypovolemia, decreased effective circulating volume)
- FENa > 2%: Intrinsic renal AKI (ATN, AIN)
- FENa 1-2%: Indeterminate

Reference:
Espinel CH. The FENa test. Use in the differential diagnosis of acute renal failure.
JAMA. 1976;236(6):579-81.
"""

import streamlit as st

from .fena_calculator import calculate_fena, interpret_fena
from .fena_ui_input import render_input_form
from .fena_ui_results import render_results_display, render_calculation_details
from .fena_ui_help import (
    render_interpretation_details,
    render_feurea_expander,
    render_references_expander,
    render_what_is_fena_expander,
    render_limitations_expander,
    render_summary_info
)


def render():
    """Render FENa Calculator"""
    
    st.subheader("🧪 FENa - Fractional Excretion of Sodium")
    st.caption("Phân Biệt Suy Thận Cấp Tiền Thận vs Thận")
    
    st.markdown("""
    **FENa** giúp phân biệt nguyên nhân suy thận cấp (AKI):
    - **Prerenal** (thiếu tưới máu thận)
    - **Intrinsic renal** (tổn thương nhu mô thận)
    
    **Công thức:** FENa (%) = (U-Na × P-Cr) / (P-Na × U-Cr) × 100
    """)
    
    st.markdown("---")
    
    # Render input form
    inputs = render_input_form()
    
    st.markdown("---")
    
    if st.button("🧮 Tính FENa", type="primary", use_container_width=True):
        # Calculate FENa
        fena = calculate_fena(
            inputs["u_na"],
            inputs["p_na"],
            inputs["u_cr_mgdl"],
            inputs["p_cr_mgdl"]
        )
        
        # Interpret
        interpretation = interpret_fena(fena)
        
        # Render results
        col1, col2 = st.columns([2, 1])
        with col2:
            render_results_display(fena, interpretation, inputs["on_diuretics"])
        
        # Render interpretation details
        render_interpretation_details(fena)
        
        # Render calculation details
        render_calculation_details(
            inputs["u_na"],
            inputs["p_na"],
            inputs["u_cr_mgdl"],
            inputs["p_cr_mgdl"],
            fena
        )
        
        # Render FEUrea expander
        render_feurea_expander()
        
        # Render references
        render_references_expander()
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    render_what_is_fena_expander()
    render_limitations_expander()
    
    # Footer
    render_summary_info()
