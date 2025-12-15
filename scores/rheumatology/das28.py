"""DAS28 - Disease Activity Score for Rheumatoid Arthritis"""
import streamlit as st
import math
from scores.utils.validation import (
    validate_range,
    validate_lab_value
)
from components.ui.validation import render_validation_errors

def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 DAS28</h2><p style='text-align: center;'><em>Hoạt động bệnh viêm khớp dạng thấp</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ DAS28"): st.markdown("**DAS28** đánh giá hoạt động bệnh RA. Khám 28 khớp + ESR/CRP + đánh giá chủ quan.")
    st.markdown("---"); tjc = st.number_input("TJC - Số khớp đau (0-28)", 0, 28, 0, format="%d"); sjc = st.number_input("SJC - Số khớp sưng (0-28)", 0, 28, 0, format="%d"); method = st.radio("Chọn phương pháp:", ["DAS28-ESR", "DAS28-CRP"]); 
    if method == "DAS28-ESR": esr = st.number_input("ESR (mm/h)", 0, 200, 10, format="%d"); pga = st.slider("PGA - Bệnh nhân đánh giá (VAS 0-100mm)", 0, 100, 50); das28 = 0.56 * math.sqrt(tjc) + 0.28 * math.sqrt(sjc) + 0.70 * math.log(esr + 1) + 0.014 * pga
    else: crp = st.number_input("CRP (mg/L)", 0.0, 200.0, 5.0, format="%.1f"); pga = st.slider("PGA - Bệnh nhân đánh giá (VAS 0-100mm)", 0, 100, 50); das28 = 0.56 * math.sqrt(tjc) + 0.28 * math.sqrt(sjc) + 0.36 * math.log(crp + 1) + 0.014 * pga + 0.96
    
    if st.button("🔬 Tính DAS28", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # TJC validation (0-28)
        is_valid_tjc, tjc_error = validate_range(tjc, 0, 28, "TJC (Số khớp đau)")
        if not is_valid_tjc:
            validation_errors.append(f"TJC: {tjc_error}")
        
        # SJC validation (0-28)
        is_valid_sjc, sjc_error = validate_range(sjc, 0, 28, "SJC (Số khớp sưng)")
        if not is_valid_sjc:
            validation_errors.append(f"SJC: {sjc_error}")
        
        # PGA validation (0-100)
        is_valid_pga, pga_error = validate_range(pga, 0, 100, "PGA (Bệnh nhân đánh giá)")
        if not is_valid_pga:
            validation_errors.append(f"PGA: {pga_error}")
        
        # ESR/CRP validation
        if method == "DAS28-ESR":
            is_valid_esr, esr_error = validate_lab_value(esr, "ESR", 0, 200)
            if not is_valid_esr:
                validation_errors.append(f"ESR: {esr_error}")
        else:
            is_valid_crp, crp_error = validate_lab_value(crp, "CRP", 0.0, 200.0)
            if not is_valid_crp:
                validation_errors.append(f"CRP: {crp_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        if das28 < 2.6: status = "Thuyên giảm"; color = "#28a745"
        elif das28 < 3.2: status = "Hoạt động thấp"; color = "#28a745"
        elif das28 < 5.1: status = "Hoạt động trung bình"; color = "#fd7e14"
        else: status = "Hoạt động cao"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>DAS28: {das28:.2f}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>", unsafe_allow_html=True); st.info(f"**Mục tiêu điều trị:** < 2.6 (thuyên giảm) hoặc < 3.2 (hoạt động thấp)")
if __name__ == "__main__": render()

