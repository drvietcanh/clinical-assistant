"""CIPN - Chemotherapy-Induced Peripheral Neuropathy Grading"""
import streamlit as st
from config.theme import COLORS
from components.ui.scoring import render_score_result
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
    if shared and shared.get('calculator_id') == 'cipn':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'CIPN Grading')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>💊 CIPN Grading</h2><p style='text-align: center;'><em>Phân độ tổn thương thần kinh ngoại biên do hóa trị</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ CIPN"): st.markdown("**CIPN** phân độ tổn thương thần kinh ngoại biên do hóa trị (taxanes, platinum, vinca alkaloids). **Độ:** 0-4")
    st.markdown("---"); grade = st.radio("Chọn độ CIPN:", [0,1,2,3,4], format_func=lambda x: ["0: Không triệu chứng", "1: Tê nhẹ, không ảnh hưởng chức năng", "2: Tê/đau trung bình, ảnh hưởng ADL", "3: Tê/đau nặng, ảnh hưởng ADL nặng", "4: Liệt, mất chức năng"][x])
    if st.button("🔬 Đánh giá CIPN", type="primary", use_container_width=True):
        if grade == 0: 
            interpretation = "Không CIPN"
            color = COLORS["success"]
            icon = "✅"
            action = "Tiếp tục theo dõi"
        elif grade == 1: 
            interpretation = "CIPN nhẹ"
            color = COLORS["info"]
            icon = "ℹ️" 
            action = "Tiếp tục hóa trị, theo dõi"
        elif grade == 2: 
            interpretation = "CIPN trung bình"
            color = COLORS["warning"]
            icon = "⚠️"
            action = "Cân nhắc giảm liều 25%"
        elif grade == 3: 
            interpretation = "CIPN nặng"
            color = COLORS["error"]
            icon = "🚨"
            action = "Tạm ngừng hóa trị đến khi giảm xuống Độ 1"
        else: 
            interpretation = "Liệt - Mất chức năng"
            color = COLORS["error"]
            icon = "🆘"
            action = "NGỪNG hóa trị gây CIPN. Điều trị: Duloxetine (30-60mg/ngày)"

        render_score_result(
            title="CIPN Grade",
            score=grade,
            interpretation=interpretation,
            mortality=action,
            color=color,
            icon=icon,
            size="large",
            max_score=4
        )
        
        # Prepare data for history and share
        inputs_dict = {
            "CIPN Grade": grade
        }
        
        grade_descriptions = {
            0: "Không triệu chứng",
            1: "Tê nhẹ, không ảnh hưởng chức năng",
            2: "Tê/đau trung bình, ảnh hưởng ADL",
            3: "Tê/đau nặng, ảnh hưởng ADL nặng",
            4: "Liệt, mất chức năng"
        }
        
        results_dict = {
            "CIPN Grade": f"{grade}",
            "Description": grade_descriptions[grade]
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="CIPN Grading",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="CIPN Grading"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="cipn",
            calculator_name="CIPN Grading",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="cipn",
            calculator_name="CIPN Grading",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="cipn", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="cipn",
            calculator_name="CIPN Grading",
            category="Ung thư học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("CIPN")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
if __name__ == "__main__": render()

