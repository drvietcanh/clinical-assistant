"""
mMRC Dyspnea Scale (modified Medical Research Council)
======================================================

Assesses breathlessness severity in COPD patients

Reference:
- Bestall JC, et al. Usefulness of the Medical Research Council (MRC) dyspnoea scale 
  as a measure of disability in patients with chronic obstructive pulmonary disease. 
  Thorax. 1999;54(7):581-586.

mMRC Scale (0-4):
- Grade 0: Breathless only with strenuous exercise
- Grade 1: Breathless when hurrying on level or walking up a slight hill
- Grade 2: Walks slower than people of same age on level ground, or stops for breath 
          when walking at own pace on level ground
- Grade 3: Stops for breath after walking ~100m or after a few minutes on level ground
- Grade 4: Too breathless to leave house, or breathless when dressing/undressing

Clinical Utility:
- Assess COPD severity (part of GOLD classification)
- Guide treatment decisions
- Monitor disease progression
- Used daily in respiratory clinics
"""

import streamlit as st
from config.theme import COLORS
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


MMRC_SCALE = {
    0: {
        "description": "Chỉ khó thở khi gắng sức mạnh",
        "detail": "Không khó thở khi đi bộ trên đường bằng hoặc leo cầu thang"
    },
    1: {
        "description": "Khó thở khi đi nhanh trên đường bằng hoặc leo dốc nhẹ",
        "detail": "Khó thở khi vội vàng hoặc leo đồi nhẹ"
    },
    2: {
        "description": "Đi chậm hơn người cùng tuổi trên đường bằng, hoặc phải dừng lại để thở khi đi với tốc độ bình thường trên đường bằng",
        "detail": "Phải dừng lại để thở khi đi bộ trên đường bằng với tốc độ của mình"
    },
    3: {
        "description": "Phải dừng lại để thở sau khi đi khoảng 100m hoặc sau vài phút trên đường bằng",
        "detail": "Phải dừng lại để thở sau khi đi khoảng 100m"
    },
    4: {
        "description": "Quá khó thở để ra khỏi nhà, hoặc khó thở khi mặc/quần áo",
        "detail": "Khó thở ngay cả khi nghỉ ngơi hoặc thực hiện hoạt động tối thiểu"
    }
}


def render():
    """Render mMRC Dyspnea Scale calculator"""
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🫁 mMRC Dyspnea Scale</h2>
    <p style='text-align: center; color: #6B7280;'>
    Đánh giá mức độ khó thở ở bệnh nhân COPD (DÙNG HÀNG NGÀY)
    </p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'mmrc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **mMRC (modified Medical Research Council) Dyspnea Scale** đánh giá mức độ khó thở:
        - Dùng hàng ngày trong phòng khám hô hấp
        - Là một phần của phân loại GOLD cho COPD
        - Giúp quyết định điều trị và theo dõi tiến triển
        
        ### 🎯 Thang điểm (0-4)
        
        - **Grade 0:** Chỉ khó thở khi gắng sức mạnh
        - **Grade 1:** Khó thở khi đi nhanh hoặc leo dốc nhẹ
        - **Grade 2:** Đi chậm hơn hoặc phải dừng lại để thở khi đi bộ
        - **Grade 3:** Phải dừng lại sau ~100m
        - **Grade 4:** Quá khó thở để ra khỏi nhà
        
        ### 📊 Phân loại GOLD
        
        mMRC được dùng trong phân loại GOLD COPD:
        - **GOLD A:** mMRC 0-1, ít đợt cấp
        - **GOLD B:** mMRC 0-1, nhiều đợt cấp
        - **GOLD C:** mMRC ≥2, ít đợt cấp
        - **GOLD D:** mMRC ≥2, nhiều đợt cấp
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="mmrc",
            calculator_name="mMRC Dyspnea Scale",
            category="Hô hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Chọn mức độ khó thở")
    
    st.markdown("""
    **Hướng dẫn:** Hỏi bệnh nhân về mức độ khó thở của họ trong các hoạt động hàng ngày.
    """)
    
    # Display scale options
    mmrc_options = []
    for grade in range(5):
        option_text = f"Grade {grade}: {MMRC_SCALE[grade]['description']}"
        mmrc_options.append(option_text)
    
    selected_grade = st.radio(
        "mMRC Grade:",
        options=list(range(5)),
        format_func=lambda x: f"Grade {x}: {MMRC_SCALE[x]['description']}",
        index=0,
        help="Chọn mức độ khó thở phù hợp nhất với bệnh nhân"
    )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Xem Kết quả mMRC", type="primary", use_container_width=True):
        grade_info = MMRC_SCALE[selected_grade]
        
        # Display results
        st.subheader("📊 Kết quả")
        
        # Determine color based on grade
        if selected_grade == 0:
            color = COLORS["success"]
            severity = "Mức độ nhẹ"
            icon = "✅"
        elif selected_grade == 1:
            color = COLORS["info"]
            severity = "Mức độ nhẹ-trung bình"
            icon = "ℹ️"
        elif selected_grade == 2:
            color = COLORS["warning"]
            severity = "Mức độ trung bình"
            icon = "⚠️"
        elif selected_grade == 3:
            color = COLORS["error"]
            severity = "Mức độ nặng"
            icon = "🚨"
        else:  # Grade 4
            color = COLORS["dark"]  # Using a distinct color for very severe if defined, else 'error' could work but 'dark' or similar emphasizes severity
            # If 'dark' isn't standard, stick to 'error' or define it. Assuming 'error' for safety or checking colors. 
            # Sticking to standard colors used in other files.
            color = COLORS["error"]
            severity = "Mức độ rất nặng"
            icon = "🚨"

        from components.ui.scoring import render_score_result
        render_score_result(
            title=f"mMRC Grade {selected_grade}",
            score=selected_grade,
            max_score=4,
            interpretation=f"{severity}: {grade_info['description']}",
            recommendation=grade_info['detail'],
            color=color,
            icon=icon
        )
        
        # GOLD Classification
        st.markdown("---")
        st.markdown("### 📋 Phân loại GOLD COPD")
        
        st.info("""
        **mMRC được dùng trong phân loại GOLD:**
        
        - **GOLD A:** mMRC 0-1, ít đợt cấp (0-1 lần/năm)
        - **GOLD B:** mMRC 0-1, nhiều đợt cấp (≥2 lần/năm)
        - **GOLD C:** mMRC ≥2, ít đợt cấp (0-1 lần/năm)
        - **GOLD D:** mMRC ≥2, nhiều đợt cấp (≥2 lần/năm)
        
        **Lưu ý:** Cần kết hợp với số đợt cấp và FEV1 để phân loại đầy đủ.
        """)
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị")
        
        if selected_grade <= 1:
            st.success("""
            **Điều trị:**
            - SABA/SAMA khi cần (short-acting bronchodilators)
            - Có thể dùng LABA/LAMA (long-acting bronchodilators)
            - Tránh hút thuốc, tiêm phòng cúm/phế cầu
            - Tập thể dục, phục hồi chức năng hô hấp
            """)
        elif selected_grade == 2:
            st.warning("""
            **Điều trị:**
            - LABA/LAMA (ưu tiên)
            - Có thể kết hợp ICS nếu có đợt cấp
            - Phục hồi chức năng hô hấp
            - Xem xét oxy liệu pháp nếu SpO2 <88%
            """)
        else:  # Grade 3-4
            st.error("""
            **Điều trị tích cực:**
            - LABA/LAMA/ICS (triple therapy)
            - Oxy liệu pháp nếu SpO2 <88% hoặc PaO2 <55 mmHg
            - Phục hồi chức năng hô hấp
            - Xem xét thở máy không xâm lấn (NIV) nếu cần
            - Đánh giá ghép phổi nếu phù hợp
            """)
        
        # Prepare inputs and results
        inputs_dict = {
            "mMRC Grade": f"{selected_grade}",
            "Description": grade_info['description']
        }
        
        results_dict = {
            "mMRC Grade": f"{selected_grade}/4",
            "Severity": grade_info['description'],
            "Detail": grade_info['detail']
        }
        
        # Export section
        render_export_section(
            title="mMRC Dyspnea Scale",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="mMRC Dyspnea Scale"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="mmrc",
            calculator_name="mMRC Dyspnea Scale",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="mmrc",
            calculator_name="mMRC Dyspnea Scale",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="mmrc", show_actions=True)
        
        # References section
        references = get_references("mMRC")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['mmrc_result'] = {
            'grade': selected_grade,
            'description': grade_info['description']
        }
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("mMRC")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **mMRC Dyspnea Scale**
            
            **Reference:**
            Bestall JC, Paul EA, Garrod R, et al. Usefulness of the Medical Research Council (MRC) 
            dyspnoea scale as a measure of disability in patients with chronic obstructive pulmonary disease. 
            Thorax. 1999;54(7):581-586.
            
            **GOLD Guidelines:**
            Global Initiative for Chronic Obstructive Lung Disease (GOLD). 
            Global Strategy for the Diagnosis, Management, and Prevention of Chronic Obstructive Pulmonary Disease. 
            2024 Report.
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

