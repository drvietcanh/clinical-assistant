"""
Universal Antibiotic Dosing Calculator
Tính liều kháng sinh tự động dựa trên eGFR/CrCl cho bất kỳ kháng sinh nào
Enhanced with: Special populations, detailed dosing, warnings, pediatric support

NOTE: Functions đã được tách ra các module riêng:
- dosing_helpers.py: Helper calculations
- dosing_processing.py: Parsing functions
- dosing_calculations.py: Main calculations
File này re-export để giữ backward compatibility
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE

# Import và re-export từ helpers
from .dosing_helpers import (
    calculate_ibw,
    calculate_abw,
    calculate_bmi,
    get_renal_category,
    calculate_crcl,
    calculate_egfr_simplified
)

# Import và re-export từ processing
from .dosing_processing import (
    parse_dosage_text,
    calculate_infusion_details
)

# Import và re-export từ calculations
from .dosing_calculations import (
    calculate_adjusted_dose,
    calculate_detailed_dose,
    calculate_icu_adjustment,
    check_warnings
)

# Re-export for backward compatibility
__all__ = [
    'calculate_ibw',
    'calculate_abw',
    'calculate_bmi',
    'get_renal_category',
    'calculate_crcl',
    'calculate_egfr_simplified',
    'parse_dosage_text',
    'calculate_infusion_details',
    'calculate_adjusted_dose',
    'calculate_detailed_dose',
    'calculate_icu_adjustment',
    'check_warnings',
    'render_dosing_calculator'
]

def render_dosing_calculator():
    """Universal antibiotic dosing calculator interface - REFACTORED to use UI components"""
    
    # Import UI components
    from .dosing_ui import (
        render_header,
        render_patient_inputs,
        render_weight_metrics,
        render_renal_metrics,
        render_antibiotic_selection,
        check_imported_values,
        render_dosage_results,
        render_warnings_section
    )
    
    # Render header
    render_header()
    
    # Check for imported values
    use_imported, imported_crcl, imported_egfr, imported_gfr_absolute = check_imported_values()
    
    # Get patient inputs
    patient_data = render_patient_inputs()
    
    st.markdown("---")
    
    # Calculate IBW, ABW, BMI
    ibw = patient_data['ibw']
    bmi = patient_data['bmi']
    is_obese = patient_data['is_obese']
    abw = patient_data['abw']
    weight = patient_data['weight']
    
    # Display weight metrics
    render_weight_metrics(weight, ibw, bmi, is_obese, abw)
    
    st.markdown("---")
    
    # Calculate CrCl (use imported if available)
    if use_imported and imported_crcl:
        crcl = imported_crcl
        st.info(f"📥 Sử dụng CrCl đã import: {crcl:.1f} mL/min")
    else:
        # Calculate with appropriate weight
        crcl = calculate_crcl(
            patient_data['age'],
            abw if is_obese else weight,
            patient_data['scr_mgdl'],
            patient_data['sex'],
            use_abw=is_obese,
            abw=abw
        )
    
    # Calculate eGFR (use imported if available)
    if use_imported and imported_egfr:
        egfr = imported_egfr
        st.info(f"📥 Sử dụng eGFR đã import: {egfr:.1f} mL/min/1.73m²")
    else:
        egfr = calculate_egfr_simplified(
            patient_data['age'],
            patient_data['scr_mgdl'],
            patient_data['sex']
        )
    
    # Get renal category
    renal_category = get_renal_category(
        crcl, egfr,
        patient_data['is_hemodialysis'],
        patient_data['is_continuous_hd'],
        patient_data['is_peritoneal_dialysis']
    )
    
    # Display renal metrics
    render_renal_metrics(crcl, egfr, renal_category)
    
    st.markdown("---")
    
    # Antibiotic selection
    selected_ab, indication_code, other_drugs = render_antibiotic_selection()
    
    st.markdown("---")
    
    # Calculate dose button
    if st.button("🧮 Tính liều", type="primary", use_container_width=True):
        # Calculate adjusted dose
        result = calculate_adjusted_dose(
            selected_ab,
            crcl,
            egfr,
            indication=indication_code,
            albumin_gdl=patient_data['albumin_gdl'] if patient_data['is_icu'] else None,
            shock_type=patient_data['shock_type'] if patient_data['is_icu'] else None,
            is_icu=patient_data['is_icu']
        )
        
        if "error" in result:
            st.error(result["error"])
            st.info(result["recommendation"])
        else:
            ab_data = ANTIBIOTICS_DATABASE[selected_ab]
            
            # Render dosage results
            render_dosage_results(
                result,
                selected_ab,
                ab_data,
                crcl,
                renal_category,
                patient_data,
                indication_code
            )
            
            # Render warnings
            render_warnings_section(
                selected_ab,
                crcl,
                patient_data['age'],
                patient_data['is_pregnant'],
                patient_data['is_breastfeeding'],
                other_drugs
            )
    
    # Integration with eGFR calculator
    st.markdown("---")
    
    # Link to database view
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **🔗 Tích hợp với eGFR Calculator:**
        - Tính eGFR/GFR đầy đủ với nhiều công thức tại trang **Calculators** → **eGFR/GFR Calculator**
        - Tự động chuyển đổi giữa eGFR chuẩn hóa và GFR tuyệt đối
        - Hỗ trợ tính BSA và điều chỉnh cho bệnh nhân béo phì/gầy
        """)
    
    with col2:
        st.info("""
        **📖 Tra Cứu Kháng Sinh:**
        - Xem thông tin đầy đủ về kháng sinh đã chọn
        - Tính liều nhanh ngay trong trang tra cứu
        - Dùng **"🔍 Tra cứu & Dữ liệu kháng sinh"** ở menu
        """)


