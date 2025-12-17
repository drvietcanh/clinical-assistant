"""
Caprini VTE Risk Score
Nguy cơ huyết khối tĩnh mạch sau phẫu thuật
"""

import streamlit as st
import streamlit.components.v1 as components
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================

def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'caprini':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("<h2 style='text-align: center; color: #DC2626;'>🩸 Caprini VTE Risk Score</h2><p style='text-align: center;'><em>Nguy cơ huyết khối sau phẫu thuật</em></p>", unsafe_allow_html=True)
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
            st.markdown("**Caprini** đánh giá nguy cơ VTE sau phẫu thuật để quyết định dự phòng. Điểm cao = Nguy cơ cao")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="caprini",
            calculator_name="Caprini VTE Risk Score",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.markdown("---")
    st.subheader("📝 Yếu tố nguy cơ")
    
    score = 0
    
    st.markdown("### 1 điểm mỗi yếu tố:")
    age_40_60 = st.checkbox("Tuổi 41-60"); score += 1 if age_40_60 else 0
    minor_surgery = st.checkbox("Phẫu thuật nhỏ"); score += 1 if minor_surgery else 0
    bmi_25_30 = st.checkbox("BMI > 25"); score += 1 if bmi_25_30 else 0
    varicose = st.checkbox("Suy giãn tĩnh mạch"); score += 1 if varicose else 0
    
    st.markdown("### 2 điểm:")
    age_60_74 = st.checkbox("Tuổi 61-74"); score += 2 if age_60_74 else 0
    laparoscopic = st.checkbox("Phẫu thuật nội soi > 45 phút"); score += 2 if laparoscopic else 0
    malignancy = st.checkbox("Ung thư"); score += 2 if malignancy else 0
    bed_rest = st.checkbox("Nằm giường > 72h"); score += 2 if bed_rest else 0
    
    st.markdown("### 3 điểm:")
    age_75 = st.checkbox("Tuổi ≥ 75"); score += 3 if age_75 else 0
    dvt_history = st.checkbox("Tiền sử DVT/PE"); score += 3 if dvt_history else 0
    family_history = st.checkbox("Gia đình có DVT/PE"); score += 3 if family_history else 0
    
    st.markdown("### 5 điểm:")
    stroke = st.checkbox("Đột quỵ < 1 tháng"); score += 5 if stroke else 0
    major_surgery = st.checkbox("Phẫu thuật lớn > 45 phút"); score += 5 if major_surgery else 0
    
    st.markdown("---")
    
    if st.button("🔬 Tính Caprini", type="primary", use_container_width=True):
        if score <= 1:
            risk = "Rất thấp"; prophylaxis = "Vận động sớm"; color = "green"
        elif score <= 2:
            risk = "Thấp"; prophylaxis = "Vận động sớm, tất chống huyết khối"; color = "green"
        elif score <= 4:
            risk = "Trung bình"; prophylaxis = "Heparin liều thấp hoặc LMWH"; color = "orange"
        else:
            risk = "Cao"; prophylaxis = "LMWH liều cao + tất chống huyết khối"; color = "red"
        
        score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[color]
        
        result_html1 = f"<div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'><h2 style='color: {score_color}; margin: 0; text-align: center;'>Caprini: {score}</h2></div>"
        components.html(result_html1, height=120, scrolling=False)
        
        result_html2 = f"<div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'><h3 style='color: {score_color};'>🎯 Nguy cơ: {risk}</h3><p style='font-size: 1.2em;'><strong>Dự phòng:</strong> {prophylaxis}</p></div>"
        components.html(result_html2, height=120, scrolling=False)
        
        # Prepare data for history and share
        inputs_dict = {
            "Tuổi 41-60": "Có" if age_40_60 else "Không",
            "Phẫu thuật nhỏ": "Có" if minor_surgery else "Không",
            "BMI > 25": "Có" if bmi_25_30 else "Không",
            "Suy giãn tĩnh mạch": "Có" if varicose else "Không",
            "Tuổi 61-74": "Có" if age_60_74 else "Không",
            "Phẫu thuật nội soi > 45 phút": "Có" if laparoscopic else "Không",
            "Ung thư": "Có" if malignancy else "Không",
            "Nằm giường > 72h": "Có" if bed_rest else "Không",
            "Tuổi ≥ 75": "Có" if age_75 else "Không",
            "Tiền sử DVT/PE": "Có" if dvt_history else "Không",
            "Gia đình có DVT/PE": "Có" if family_history else "Không",
            "Đột quỵ < 1 tháng": "Có" if stroke else "Không",
            "Phẫu thuật lớn > 45 phút": "Có" if major_surgery else "Không"
        }
        
        results_dict = {
            "Caprini Score": f"{score}",
            "Nguy cơ": risk,
            "Dự phòng": prophylaxis
        }
        
        # Export section
        render_export_section(
            calculator_id="caprini",
            calculator_name="Caprini VTE Risk Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="caprini",
            calculator_name="Caprini VTE Risk Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="caprini",
            calculator_name="Caprini VTE Risk Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="caprini", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("Caprini")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

if __name__ == "__main__":
    render()

