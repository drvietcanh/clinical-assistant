"""
DLQI - Dermatology Life Quality Index
Chỉ số chất lượng cuộc sống bệnh da
"""

import streamlit as st
import streamlit.components.v1 as components
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================

def calculate_dlqi(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    """Tính DLQI"""
    total = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    
    if total <= 1:
        impact = "Không ảnh hưởng"; color = "green"
    elif total <= 5:
        impact = "Ảnh hưởng nhỏ"; color = "green"
    elif total <= 10:
        impact = "Ảnh hưởng trung bình"; color = "orange"
    elif total <= 20:
        impact = "Ảnh hưởng lớn"; color = "orange"
    else:
        impact = "Ảnh hưởng rất lớn"; color = "red"
    
    return {"total_score": total, "impact": impact, "color": color}

def render():
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'dlqi':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'DLQI')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("<h2 style='text-align: center; color: #EC4899;'>🩹 DLQI</h2><p style='text-align: center;'><em>Chất lượng cuộc sống bệnh da</em></p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ DLQI"):
        st.markdown("**DLQI** đánh giá ảnh hưởng bệnh da đến chất lượng sống. **Thang điểm:** 0-30")
    
    st.markdown("---")
    st.info("**Trong 1 tuần qua**, bệnh da ảnh hưởng như thế nào?")
    
    options_dict = {3: "Rất nhiều", 2: "Nhiều", 1: "Một chút", 0: "Không"}
    
    q1 = st.radio("1. Ngứa, đau, cảm giác khó chịu?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q2 = st.radio("2. Xấu hổ, tự ti?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q3 = st.radio("3. Ảnh hưởng mua sắm hoặc chăm sóc nhà?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q4 = st.radio("4. Ảnh hưởng chọn quần áo?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q5 = st.radio("5. Ảnh hưởng hoạt động xã hội/giải trí?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q6 = st.radio("6. Ảnh hưởng thể thao?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q7 = st.radio("7. Ngăn cản làm việc/học tập?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q8 = st.radio("8. Gây vấn đề với bạn bè/người thân?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q9 = st.radio("9. Gây khó khăn tình dục?", [3,2,1,0], format_func=lambda x: options_dict[x])
    q10 = st.radio("10. Điều trị gây phiền toái?", [3,2,1,0], format_func=lambda x: options_dict[x])
    
    if st.button("🔬 Tính DLQI", type="primary", use_container_width=True):
        result = calculate_dlqi(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10)
        score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[result["color"]]
        
        result_html1 = f"<div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'><h2 style='color: {score_color}; margin: 0; text-align: center;'>DLQI: {result['total_score']}/30</h2></div>"
        components.html(result_html1, height=120, scrolling=False)
        
        result_html2 = f"<div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'><h3 style='color: {score_color};'>🎯 Ảnh hưởng: {result['impact']}</h3></div>"
        components.html(result_html2, height=100, scrolling=False)
        
        st.info("""
        **Phân loại:**
        - 0-1: Không ảnh hưởng
        - 2-5: Ảnh hưởng nhỏ
        - 6-10: Ảnh hưởng trung bình
        - 11-20: Ảnh hưởng lớn
        - 21-30: Ảnh hưởng rất lớn
        """)
        
        # Prepare data for history and share
        inputs_dict = {
            "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5,
            "Q6": q6, "Q7": q7, "Q8": q8, "Q9": q9, "Q10": q10
        }
        
        results_dict = {
            "DLQI Score": f"{result['total_score']}/30",
            "Impact": result['impact']
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
            calculator_id="dlqi",
            calculator_name="DLQI",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="dlqi",
            calculator_name="DLQI",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="dlqi",
            calculator_name="DLQI",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="dlqi", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="dlqi",
            calculator_name="DLQI",
            category="Da liễu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("DLQI")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )

if __name__ == "__main__":
    render()

