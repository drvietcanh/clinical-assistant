"""CIPN - Chemotherapy-Induced Peripheral Neuropathy Grading"""
import streamlit as st
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
    
    st.markdown("<h2 style='text-align: center; color: #8B5CF6;'>💊 CIPN Grading</h2><p style='text-align: center;'><em>Phân độ tổn thương thần kinh ngoại biên do hóa trị</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ CIPN"): st.markdown("**CIPN** phân độ tổn thương thần kinh ngoại biên do hóa trị (taxanes, platinum, vinca alkaloids). **Độ:** 0-4")
    st.markdown("---"); grade = st.radio("Chọn độ CIPN:", [0,1,2,3,4], format_func=lambda x: ["0: Không triệu chứng", "1: Tê nhẹ, không ảnh hưởng chức năng", "2: Tê/đau trung bình, ảnh hưởng ADL", "3: Tê/đau nặng, ảnh hưởng ADL nặng", "4: Liệt, mất chức năng"][x])
    if st.button("🔬 Đánh giá CIPN", type="primary", use_container_width=True):
        if grade == 0: st.success("✅ **Độ 0:** Không CIPN")
        elif grade == 1: st.info("**Độ 1:** CIPN nhẹ - Tiếp tục hóa trị, theo dõi")
        elif grade == 2: st.warning("⚠️ **Độ 2:** CIPN trung bình - Cân nhắc giảm liều 25%")
        elif grade == 3: st.error("🚨 **Độ 3:** CIPN nặng - Tạm ngừng hóa trị đến khi giảm xuống Độ 1")
        else: 
            st.error("🆘 **Độ 4:** Liệt - NGỪNG hóa trị gây CIPN")
            st.info("""**Điều trị CIPN:** Duloxetine (30-60mg/ngày) - Bằng chứng tốt nhất""")
        
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

