"""P-POSSUM - Portsmouth Physiological and Operative Severity Score"""
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
    if shared and shared.get('calculator_id') == 'possum':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("<h2 style='text-align: center; color: #DC2626;'>🏥 P-POSSUM Score</h2><p style='text-align: center;'><em>Nguy cơ tử vong phẫu thuật</em></p>", unsafe_allow_html=True)
    
    col_main, col_suggestions = st.columns([2, 1])
    
    with col_main:
        with st.expander("ℹ️ P-POSSUM"): st.markdown("**P-POSSUM** dự đoán tử vong sau phẫu thuật dựa trên 12 yếu tố sinh lý và 6 yếu tố phẫu thuật. Phức tạp, thường dùng trong nghiên cứu.")
    
    with col_suggestions:
        # Smart Suggestions
        render_suggestions(
            calculator_id="possum",
            calculator_name="P-POSSUM Score",
            category="Phẫu Thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.markdown("---"); st.warning("⚠️ **Lưu ý:** P-POSSUM rất phức tạp (18 biến số), thường cần tính toán chuyên dụng. Đây là phiên bản đơn giản hóa."); age = st.number_input("Tuổi", 20, 100, 60, format="%d"); cardiac = st.selectbox("Tim mạch", ["Bình thường", "Bệnh tim", "Suy tim"]); respiratory = st.selectbox("Hô hấp", ["Bình thường", "Khó thở nhẹ", "COPD"]); bp = st.number_input("SBP (mmHg)", 50, 200, 120, format="%d"); pulse_rate = st.number_input("Mạch", 40, 150, 80, format="%d"); gcs_score = st.number_input("GCS", 3, 15, 15, format="%d"); operation_severity = st.selectbox("Mức độ phẫu thuật", ["Nhỏ", "Trung bình", "Lớn", "Lớn+"])
    if st.button("🔬 Ước tính P-POSSUM", type="primary", use_container_width=True):
        risk_score = 0; risk_score += max(0, (age - 60) // 5); risk_score += 1 if cardiac != "Bình thường" else 0; risk_score += 1 if respiratory != "Bình thường" else 0; risk_score += 1 if bp < 100 else 0; risk_score += 1 if gcs_score < 15 else 0; risk_score += {"Nhỏ": 0, "Trung bình": 1, "Lớn": 2, "Lớn+": 3}[operation_severity]
        if risk_score <= 2: risk = "Thấp (<5%)"; color = "#28a745"
        elif risk_score <= 4: risk = "Trung bình (5-15%)"; color = "#fd7e14"
        else: risk = "Cao (>15%)"; color = "#dc3545"
        result_html = f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>Nguy cơ: {risk}</h2></div>"
        components.html(result_html, height=120, scrolling=False)
        st.info("💡 **Lưu ý:** Đây chỉ là ước tính đơn giản. P-POSSUM thực tế cần 18 biến số và công thức phức tạp.")
        
        # Prepare data for history and share
        inputs_dict = {
            "Tuổi": age,
            "Tim mạch": cardiac,
            "Hô hấp": respiratory,
            "SBP": bp,
            "Mạch": pulse_rate,
            "GCS": gcs_score,
            "Mức độ phẫu thuật": operation_severity
        }
        
        results_dict = {
            "Risk Score": risk_score,
            "Nguy cơ": risk
        }
        
        # Save to history
        save_calculation_to_history(
            calculator_id="possum",
            calculator_name="P-POSSUM Score",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="possum",
            calculator_name="P-POSSUM Score",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        from components.calculation_history import render_history_ui
        render_history_ui(calculator_id="possum", show_actions=True)
    
    # References section (always visible)
    st.markdown("---")
    references = get_references("P-POSSUM")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

if __name__ == "__main__": render()

