"""
Modified Rankin Scale (mRS) - Measure of Disability After Stroke
Assesses degree of disability or dependence in daily activities

Scale: 0-6
- 0 = No symptoms
- 6 = Dead

Reference:
van Swieten JC, et al. Interobserver agreement for the assessment of handicap in stroke patients.
Stroke. 1988;19(5):604-7.

Also: Rankin J. Cerebral vascular accidents in patients over the age of 60. II. Prognosis.
Scott Med J. 1957;2(5):200-15.
"""

import streamlit as st
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# =====================================

from .mrs_ui_selection import render_selection
from .mrs_ui_results import render_results_display
from .mrs_ui_help import (
    render_important_notes,
    render_comparison_table,
    render_barthel_comparison,
    render_references,
    render_assessment_guide,
    render_clinical_decisions,
    render_common_mistakes,
    render_footer
)


def render():
    """Render Modified Rankin Scale Calculator"""
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mrs':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Modified Rankin Scale')}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.subheader("🧠 mRS - Modified Rankin Scale")
    st.caption("Đánh giá mức độ khuyết tật/phụ thuộc sau đột quỵ")
    
    st.markdown("""
    **Modified Rankin Scale (mRS)** là thang điểm đánh giá mức độ khuyết tật hoặc 
    phụ thuộc trong sinh hoạt hàng ngày sau đột quỵ hoặc các bệnh lý thần kinh khác.
    
    **Ứng dụng:**
    - Đánh giá kết cục chức năng sau đột quỵ
    - Theo dõi tiến triển phục hồi chức năng
    - Tiêu chí chính trong các nghiên cứu lâm sàng về đột quỵ
    """)
    
    st.markdown("---")
    
    # Selection
    selected_mrs, mrs_info = render_selection()
    
    # Calculate button
    st.markdown("---")
    if st.button("🧮 Xác Nhận mRS Score", type="primary", use_container_width=True):
        st.session_state.total_calculations = st.session_state.get('total_calculations', 0) + 1
        
        # Display results
        render_results_display(selected_mrs, mrs_info)
        
        # Help sections
        render_important_notes()
        render_comparison_table()
        render_barthel_comparison()
        render_references()
        
        # Prepare data for history and share
        inputs_dict = {
            "mRS Score": selected_mrs
        }
        
        results_dict = {
            "mRS Score": f"{selected_mrs}/6",
            "Description": mrs_info.get('description', ''),
            "Category": mrs_info.get('category', '')
        }
        
        # Export section
        from components.export import render_export_section
        render_export_section(
                title="Modified Rankin Scale",
                inputs=inputs_dict,
                results=results_dict
        ,
                calculator_name="Modified Rankin Scale"
            )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mrs",
            calculator_name="Modified Rankin Scale",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="mrs",
            calculator_name="Modified Rankin Scale",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        render_history_ui(calculator_id="mrs", show_actions=True)
    
    # Smart Suggestions
    col_main, col_suggestions = st.columns([2, 1])
    with col_suggestions:
        render_suggestions(
            calculator_id="mrs",
            calculator_name="Modified Rankin Scale",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    render_assessment_guide()
    render_clinical_decisions()
    render_common_mistakes()
    render_footer()
    
    # References section (always at bottom)
    st.markdown("---")
    references = get_references("Modified Rankin Scale")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )


if __name__ == "__main__":
    render()
