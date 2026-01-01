"""
PPS - Palliative Performance Scale Calculator
Thang đo thể trạng chăm sóc giảm nhẹ
"""

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
    """Render PPS calculator interface"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'pps':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'PPS')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.markdown("""
    st.markdown(f"<h2 style='text-align: center; color: {COLORS['success']};'>🕊️ PPS - Palliative Performance Scale</h2>", unsafe_allow_html=True)
    st.caption("<p style='text-align: center;'>Thang đo thể trạng chăm sóc giảm nhẹ</p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về PPS"):
        st.markdown("""
        **PPS** đánh giá thể trạng bệnh nhân trong chăm sóc giảm nhẹ, giúp dự đoán tiên lượng sống.
        
        **Đánh giá 5 yếu tố:**
        - Khả năng di chuyển
        - Hoạt động & bằng chứng bệnh
        - Tự chăm sóc
        - Ăn uống
        - Mức độ ý thức
        
        **Thang điểm:** 0-100% (10% mỗi bậc)
        """)
    
    st.markdown("---")
    
    pps_score = st.select_slider(
        "Chọn mức PPS phù hợp:",
        options=[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],
        value=50,
        format_func=lambda x: {
            100: "100% - Hoàn toàn bình thường",
            90: "90% - Hoạt động bình thường, triệu chứng nhẹ",
            80: "80% - Hoạt động bình thường với nỗ lực",
            70: "70% - Không làm việc, tự chăm sóc được",
            60: "60% - Cần hỗ trợ đôi khi",
            50: "50% - Cần hỗ trợ đáng kể",
            40: "40% - Chủ yếu nằm giường",
            30: "30% - Hoàn toàn nằm giường",
            20: "20% - Hoàn toàn nằm giường, cần chăm sóc toàn diện",
            10: "10% - Hấp hối",
            0: "0% - Tử vong"
        }[x]
    )
    
    st.markdown("---")
    
    with st.expander("📖 Mô tả chi tiết từng mức"):
        st.markdown("""
        ### 100% - Hoàn toàn bình thường
        - Di chuyển: Đầy đủ
        - Hoạt động: Bình thường, không bệnh
        - Tự chăm sóc: Hoàn toàn
        - Ăn uống: Bình thường
        - Ý thức: Đầy đủ
        
        ### 50% - Cần hỗ trợ đáng kể  
        - Di chuyển: Chủ yếu ngồi/nằm
        - Hoạt động: Không thể làm việc, bệnh lan rộng
        - Tự chăm sóc: Cần hỗ trợ đáng kể
        - Ăn uống: Giảm
        - Ý thức: Đầy đủ hoặc lú lẫn
        
        ### 10% - Hấp hối
        - Di chuyển: Hoàn toàn nằm giường
        - Hoạt động: Tử vong sắp xảy ra
        - Tự chăm sóc: Hoàn toàn phụ thuộc
        - Ăn uống: Chỉ nuốt được
        - Ý thức: Hôn mê sâu
        """)
    
    if st.button("🔬 Đánh giá PPS", type="primary", use_container_width=True):
        if pps_score >= 70:
            prognosis = "Tuần/tháng"
            color = COLORS["success"]
            care = "Chăm sóc giảm nhẹ ngoại trú"
            icon = "✅"
        elif pps_score >= 50:
            prognosis = "Tuần"
            color = COLORS["warning"]
            care = "Chăm sóc tại nhà với hỗ trợ"
            icon = "⚠️"
        elif pps_score >= 20:
            prognosis = "Ngày/tuần"
            color = COLORS["warning"]
            care = "Chăm sóc tại nhà hoặc hospice"
            icon = "🟠"
        else:
            prognosis = "Giờ/ngày"
            color = COLORS["error"]
            care = "Hospice, chăm sóc end-of-life"
            icon = "🚨"
        
        render_score_result(
            title="PPS Score",
            score=f"{pps_score}%",
            interpretation=f"Tiên lượng sống: {prognosis}",
            mortality=f"Khuyến cáo: {care}",
            color=color,
            icon=icon,
            size="large",
            max_score=100
        )
        
        # Prepare data for history and share
        inputs_dict = {
            "PPS Score": f"{pps_score}%"
        }
        
        results_dict = {
            "PPS Score": f"{pps_score}%",
            "Prognosis": prognosis,
            "Care Recommendation": care
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="PPS",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="PPS"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="pps",
            calculator_name="PPS",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="pps",
            calculator_name="PPS",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="pps", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="pps",
            calculator_name="PPS",
            category="Ung thư học",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("PPS")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()

