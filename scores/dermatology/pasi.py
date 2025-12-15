"""PASI - Psoriasis Area Severity Index"""
import streamlit as st
from scores.utils.validation import (
    validate_range
)
from components.ui.validation import render_validation_errors

def render():
    st.markdown("<h2 style='text-align: center; color: #EC4899;'>🩹 PASI Score</h2><p style='text-align: center;'><em>Mức độ nặng vẩy nến</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ PASI"): st.markdown("**PASI** đánh giá mức độ vẩy nến theo diện tích và mức độ. **Điểm:** 0-72")
    st.markdown("---"); st.info("Đánh giá 4 vùng: Đầu, Thân, Tay, Chân"); head_area = st.slider("Đầu - % diện tích", 0, 6, 0); head_erythema = st.slider("Đầu - Đỏ", 0, 4, 0); head_thick = st.slider("Đầu - Dày", 0, 4, 0); head_scale = st.slider("Đầu - Vảy", 0, 4, 0); trunk_area = st.slider("Thân - % diện tích", 0, 6, 0); trunk_e = st.slider("Thân - Đỏ", 0, 4, 0); trunk_t = st.slider("Thân - Dày", 0, 4, 0); trunk_s = st.slider("Thân - Vảy", 0, 4, 0); upper_area = st.slider("Tay - % diện tích", 0, 6, 0); upper_e = st.slider("Tay - Đỏ", 0, 4, 0); upper_t = st.slider("Tay - Dày", 0, 4, 0); upper_s = st.slider("Tay - Vảy", 0, 4, 0); lower_area = st.slider("Chân - % diện tích", 0, 6, 0); lower_e = st.slider("Chân - Đỏ", 0, 4, 0); lower_t = st.slider("Chân - Dày", 0, 4, 0); lower_s = st.slider("Chân - Vảy", 0, 4, 0); head_pasi = 0.1 * head_area * (head_erythema + head_thick + head_scale); trunk_pasi = 0.3 * trunk_area * (trunk_e + trunk_t + trunk_s); upper_pasi = 0.2 * upper_area * (upper_e + upper_t + upper_s); lower_pasi = 0.4 * lower_area * (lower_e + lower_t + lower_s); total = head_pasi + trunk_pasi + upper_pasi + lower_pasi
    if st.button("🔬 Tính PASI", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Area validations (0-6 for each region)
        area_inputs = [head_area, trunk_area, upper_area, lower_area]
        area_names = ["Đầu - % diện tích", "Thân - % diện tích", "Tay - % diện tích", "Chân - % diện tích"]
        for area, name in zip(area_inputs, area_names):
            is_valid_area, area_error = validate_range(area, 0, 6, name)
            if not is_valid_area:
                validation_errors.append(f"{name}: {area_error}")
        
        # Severity scores validation (0-4 for each: erythema, thickness, scaling)
        severity_inputs = [
            (head_erythema, "Đầu - Đỏ"), (head_thick, "Đầu - Dày"), (head_scale, "Đầu - Vảy"),
            (trunk_e, "Thân - Đỏ"), (trunk_t, "Thân - Dày"), (trunk_s, "Thân - Vảy"),
            (upper_e, "Tay - Đỏ"), (upper_t, "Tay - Dày"), (upper_s, "Tay - Vảy"),
            (lower_e, "Chân - Đỏ"), (lower_t, "Chân - Dày"), (lower_s, "Chân - Vảy")
        ]
        for score, name in severity_inputs:
            is_valid_score, score_error = validate_range(score, 0, 4, name)
            if not is_valid_score:
                validation_errors.append(f"{name}: {score_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        if total < 10: severity = "Nhẹ"; color = "#28a745"
        elif total < 20: severity = "Trung bình"; color = "#fd7e14"
        else: severity = "Nặng"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>PASI: {total:.1f}/72</h2><p style='text-align: center; margin-top: 10px;'>{severity}</p></div>", unsafe_allow_html=True)
if __name__ == "__main__": render()

