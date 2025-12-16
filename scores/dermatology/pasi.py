"""PASI - Psoriasis Area Severity Index"""
import streamlit as st
import streamlit.components.v1 as components
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================
from scores.utils.validation import (
    validate_range
)
from components.ui.validation import render_validation_errors

def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'pasi':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'PASI')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
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
        result_html = f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>PASI: {total:.1f}/72</h2><p style='text-align: center; margin-top: 10px;'>{severity}</p></div>"
        components.html(result_html, height=120, scrolling=False)
        
        # Prepare data for history and share
        inputs_dict = {
            "Head Area": head_area, "Head Erythema": head_erythema, "Head Thick": head_thick, "Head Scale": head_scale,
            "Trunk Area": trunk_area, "Trunk E": trunk_e, "Trunk T": trunk_t, "Trunk S": trunk_s,
            "Upper Area": upper_area, "Upper E": upper_e, "Upper T": upper_t, "Upper S": upper_s,
            "Lower Area": lower_area, "Lower E": lower_e, "Lower T": lower_t, "Lower S": lower_s
        }
        
        results_dict = {
            "PASI Score": f"{total:.1f}/72",
            "Severity": severity
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="pasi",
            calculator_name="PASI",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="pasi",
            calculator_name="PASI",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="pasi",
            calculator_name="PASI",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="pasi", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="pasi",
            calculator_name="PASI",
            category="Da liễu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("PASI")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

