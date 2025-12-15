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
from datetime import datetime

from .fena_calculator import calculate_fena, interpret_fena
from .fena_ui_input import render_input_form
from scores.utils.validation import (
    validate_lab_value,
    validate_range
)
from components.ui.validation import render_validation_errors
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
    st.caption("Phân biệt suy thận cấp tiền thận vs thận")
    
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
        # Validate inputs
        validation_errors = []
        
        # Plasma Sodium validation
        is_valid_pna, pna_error = validate_range(inputs["p_na"], 100.0, 180.0, "Plasma Sodium")
        if not is_valid_pna:
            validation_errors.append(f"Plasma Sodium: {pna_error}")
        
        # Plasma Creatinine validation (already in mg/dL)
        is_valid_pcr, pcr_error = validate_lab_value(inputs["p_cr_mgdl"], "Plasma Creatinine", 0.1, 20.0)
        if not is_valid_pcr:
            validation_errors.append(f"Plasma Creatinine: {pcr_error}")
        
        # Urine Sodium validation
        is_valid_una, una_error = validate_range(inputs["u_na"], 1.0, 300.0, "Urine Sodium")
        if not is_valid_una:
            validation_errors.append(f"Urine Sodium: {una_error}")
        
        # Urine Creatinine validation (already in mg/dL)
        is_valid_ucr, ucr_error = validate_lab_value(inputs["u_cr_mgdl"], "Urine Creatinine", 1.0, 500.0)
        if not is_valid_ucr:
            validation_errors.append(f"Urine Creatinine: {ucr_error}")
        
        # Check for zero in denominator (P-Na × U-Cr cannot be zero)
        if inputs["p_na"] == 0:
            validation_errors.append("Plasma Sodium không thể bằng 0 (mẫu số trong công thức FENa)")
        if inputs["u_cr_mgdl"] == 0:
            validation_errors.append("Urine Creatinine không thể bằng 0 (mẫu số trong công thức FENa)")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        # Track calculation
        try:
            from components.analytics import track_calculation
            track_calculation(
                calculator_id="fena",
                calculator_name="FENa Calculator",
                inputs=inputs,
                results=None
            )
        except ImportError:
            pass
        
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
        
        # Render notes section
        try:
            from components.notes import render_notes_section
            from datetime import datetime
            result_id = f"fena_{fena:.2f}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            render_notes_section(
                calculator_id="fena",
                result_id=result_id,
                show_add_form=True,
                show_search=True,
                show_export=True,
                max_display=10
            )
        except ImportError:
            pass  # Notes component not available
        
        # Render notes section
        try:
            from components.notes import render_notes_section
            result_id = f"fena_{fena:.2f}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            render_notes_section(
                calculator_id="fena",
                result_id=result_id,
                show_add_form=True,
                show_search=True,
                show_export=True,
                max_display=10
            )
        except (ImportError, Exception) as e:
            pass  # Notes component not available or error
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    render_what_is_fena_expander()
    render_limitations_expander()
    
    # Footer
    render_summary_info()
