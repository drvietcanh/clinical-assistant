"""SLEDAI - SLE Disease Activity Index"""
import streamlit as st
import streamlit.components.v1 as components
from config.theme import COLORS
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
    if shared and shared.get('calculator_id') == 'sledai':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'SLEDAI')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['warning_dark']};'>🦋 SLEDAI</h2><p style='text-align: center;'><em>Hoạt động bệnh Lupus</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SLEDAI"): 
        st.markdown("**SLEDAI** đánh giá hoạt động bệnh SLE trong 10 ngày qua. **Điểm:** 0-105")
    
    st.markdown("---")
    st.info("Đánh dấu triệu chứng trong **10 ngày qua**:")
    
    score = 0
    symptoms = {}
    
    # 8 points
    symptoms["Co giật"] = st.checkbox("Co giật (8đ)")
    score += 8 if symptoms["Co giật"] else 0
    symptoms["Loạn thần"] = st.checkbox("Loạn thần (8đ)")
    score += 8 if symptoms["Loạn thần"] else 0
    symptoms["Hội chứng não"] = st.checkbox("Hội chứng não (8đ)")
    score += 8 if symptoms["Hội chứng não"] else 0
    symptoms["Rối loạn thị giác"] = st.checkbox("Rối loạn thị giác (8đ)")
    score += 8 if symptoms["Rối loạn thị giác"] else 0
    symptoms["Tổn thương thần kinh sọ"] = st.checkbox("Tổn thương thần kinh sọ (8đ)")
    score += 8 if symptoms["Tổn thương thần kinh sọ"] else 0
    symptoms["Đau đầu lupus"] = st.checkbox("Đau đầu lupus (8đ)")
    score += 8 if symptoms["Đau đầu lupus"] else 0
    symptoms["TIA"] = st.checkbox("TIA (8đ)")
    score += 8 if symptoms["TIA"] else 0
    
    # 4 points
    symptoms["Viêm mạch"] = st.checkbox("Viêm mạch (4đ)")
    score += 4 if symptoms["Viêm mạch"] else 0
    symptoms["Viêm khớp"] = st.checkbox("Viêm khớp (4đ)")
    score += 4 if symptoms["Viêm khớp"] else 0
    symptoms["Viêm cơ"] = st.checkbox("Viêm cơ (4đ)")
    score += 4 if symptoms["Viêm cơ"] else 0
    symptoms["Trụ niệu"] = st.checkbox("Trụ niệu (4đ)")
    score += 4 if symptoms["Trụ niệu"] else 0
    symptoms["Hồng cầu niệu"] = st.checkbox("Hồng cầu niệu (4đ)")
    score += 4 if symptoms["Hồng cầu niệu"] else 0
    symptoms["Protein niệu"] = st.checkbox("Protein niệu (4đ)")
    score += 4 if symptoms["Protein niệu"] else 0
    symptoms["Bạch cầu niệu"] = st.checkbox("Bạch cầu niệu (4đ)")
    score += 4 if symptoms["Bạch cầu niệu"] else 0
    
    # 2 points
    symptoms["Ban da mới"] = st.checkbox("Ban da mới (2đ)")
    score += 2 if symptoms["Ban da mới"] else 0
    symptoms["Loét miệng"] = st.checkbox("Loét miệng (2đ)")
    score += 2 if symptoms["Loét miệng"] else 0
    symptoms["Rụng tóc"] = st.checkbox("Rụng tóc (2đ)")
    score += 2 if symptoms["Rụng tóc"] else 0
    symptoms["Viêm màng phổi/tim"] = st.checkbox("Viêm màng phổi/tim (2đ)")
    score += 2 if symptoms["Viêm màng phổi/tim"] else 0
    
    # 1-2 points
    symptoms["Giảm C3/C4"] = st.checkbox("Giảm C3/C4 (1đ)")
    score += 1 if symptoms["Giảm C3/C4"] else 0
    symptoms["Tăng anti-DNA"] = st.checkbox("Tăng anti-DNA (2đ)")
    score += 2 if symptoms["Tăng anti-DNA"] else 0
    symptoms["Sốt"] = st.checkbox("Sốt (1đ)")
    score += 1 if symptoms["Sốt"] else 0
    symptoms["Giảm tiểu cầu"] = st.checkbox("Giảm tiểu cầu (1đ)")
    score += 1 if symptoms["Giảm tiểu cầu"] else 0
    symptoms["Giảm bạch cầu"] = st.checkbox("Giảm bạch cầu (1đ)")
    score += 1 if symptoms["Giảm bạch cầu"] else 0
    
    if st.button("🔬 Tính SLEDAI", type="primary", use_container_width=True):
        if score == 0: 
            status = "Không hoạt động"
            color = COLORS["success"]
        elif score <= 5: 
            status = "Hoạt động nhẹ"
            color = COLORS["success"]
        elif score <= 11: 
            status = "Hoạt động trung bình"
            color = COLORS["warning"]
        else: 
            status = "Hoạt động cao"
            color = COLORS["error"]
        
        result_html = f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>SLEDAI: {score}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>"
        components.html(result_html, height=120, scrolling=False)
        
        # Prepare data for history and share
        inputs_dict = {k: "Có" if v else "Không" for k, v in symptoms.items()}
        results_dict = {
            "SLEDAI Score": score,
            "Status": status
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="SLEDAI",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="SLEDAI"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="sledai",
            calculator_name="SLEDAI",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="sledai",
            calculator_name="SLEDAI",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="sledai", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="sledai",
            calculator_name="SLEDAI",
            category="Thấp Khớp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("SLEDAI")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

if __name__ == "__main__": 
    render()
