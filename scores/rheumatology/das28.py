"""DAS28 - Disease Activity Score for Rheumatoid Arthritis"""
import streamlit as st
import streamlit.components.v1 as components
import math
from scores.utils.validation import (
    validate_range,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================

def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'das28':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'DAS28')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
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
        result_html = f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>DAS28: {das28:.2f}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>"
        components.html(result_html, height=120, scrolling=False)
        st.info(f"**Mục tiêu điều trị:** < 2.6 (thuyên giảm) hoặc < 3.2 (hoạt động thấp)")
        
        # Prepare data for history and share
        inputs_dict = {
            "TJC": tjc,
            "SJC": sjc,
            "Method": method,
            "ESR" if method == "DAS28-ESR" else "CRP": esr if method == "DAS28-ESR" else crp,
            "PGA": pga
        }
        
        results_dict = {
            "DAS28 Score": f"{das28:.2f}",
            "Status": status,
            "Treatment Goal": "< 2.6 (remission) or < 3.2 (low activity)"
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="das28",
            calculator_name="DAS28",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="das28",
            calculator_name="DAS28",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="das28",
            calculator_name="DAS28",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="das28", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="das28",
            calculator_name="DAS28",
            category="Thấp Khớp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("DAS28")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

