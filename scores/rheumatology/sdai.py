"""SDAI - Simplified Disease Activity Index for RA"""
import streamlit as st
import streamlit.components.v1 as components
from scores.utils.validation import (
    validate_range,
    validate_lab_value
)
from components.ui.validation import render_validation_errors

def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 SDAI</h2><p style='text-align: center;'><em>Chỉ số đơn giản hóa RA</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SDAI"): st.markdown("**SDAI** = CDAI + CRP. Tương tự CDAI nhưng có CRP.")
    st.markdown("---"); tjc = st.number_input("TJC - Số khớp đau (0-28)", 0, 28, 0, format="%d"); sjc = st.number_input("SJC - Số khớp sưng (0-28)", 0, 28, 0, format="%d"); pga = st.slider("PGA - Bệnh nhân đánh giá (cm, 0-10)", 0.0, 10.0, 5.0, 0.1); ega = st.slider("EGA - Bác sĩ đánh giá (cm, 0-10)", 0.0, 10.0, 5.0, 0.1); crp = st.number_input("CRP (mg/dL)", 0.0, 20.0, 0.5, 0.1, format="%.1f"); sdai = tjc + sjc + pga + ega + crp
    if st.button("🔬 Tính SDAI", type="primary", use_container_width=True):
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
        
        # PGA validation (0-10)
        is_valid_pga, pga_error = validate_range(pga, 0.0, 10.0, "PGA (Bệnh nhân đánh giá)")
        if not is_valid_pga:
            validation_errors.append(f"PGA: {pga_error}")
        
        # EGA validation (0-10)
        is_valid_ega, ega_error = validate_range(ega, 0.0, 10.0, "EGA (Bác sĩ đánh giá)")
        if not is_valid_ega:
            validation_errors.append(f"EGA: {ega_error}")
        
        # CRP validation
        is_valid_crp, crp_error = validate_lab_value(crp, "CRP", 0.0, 20.0)
        if not is_valid_crp:
            validation_errors.append(f"CRP: {crp_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        if sdai <= 3.3: status = "Thuyên giảm"; color = "#28a745"
        elif sdai <= 11: status = "Hoạt động thấp"; color = "#28a745"
        elif sdai <= 26: status = "Hoạt động trung bình"; color = "#fd7e14"
        else: status = "Hoạt động cao"; color = "#dc3545"
        result_html = f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>SDAI: {sdai:.1f}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>"
        components.html(result_html, height=120, scrolling=False)
if __name__ == "__main__": render()

