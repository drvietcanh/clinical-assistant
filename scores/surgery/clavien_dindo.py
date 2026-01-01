"""
Clavien-Dindo Classification Calculator
========================================

Classifies surgical complications

Reference:
- Dindo D, Demartines N, Clavien PA. Classification of surgical complications: 
  a new proposal with evaluation in a cohort of 6336 patients and results of a survey. 
  Ann Surg. 2004;240(2):205-213.

Clavien-Dindo Classification (5 Grades):
- Grade I: Any deviation from normal postoperative course without need for 
  pharmacological treatment or surgical, endoscopic, and radiological interventions
- Grade II: Requiring pharmacological treatment with drugs other than those allowed 
  for grade I complications
- Grade III: Requiring surgical, endoscopic, or radiological intervention
  - IIIa: Not under general anesthesia
  - IIIb: Under general anesthesia
- Grade IV: Life-threatening complication requiring ICU management
  - IVa: Single organ dysfunction
  - IVb: Multi-organ dysfunction
- Grade V: Death of patient

Clinical Utility:
- Used daily in surgical practice
- Standardizes complication reporting
- Allows comparison between studies
- Guides quality improvement
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


CLAVIEN_DINDO_GRADES = {
    "I": {
        "name": "Grade I",
        "description": "Lệch khỏi diễn biến sau mổ bình thường, không cần điều trị",
        "detail": "Không cần thuốc (ngoài thuốc thường quy) hoặc can thiệp"
    },
    "II": {
        "name": "Grade II",
        "description": "Cần điều trị bằng thuốc",
        "detail": "Cần thuốc khác ngoài thuốc thường quy (kháng sinh, thuốc tim mạch, etc.)"
    },
    "IIIa": {
        "name": "Grade IIIa",
        "description": "Cần can thiệp, KHÔNG cần gây mê toàn thân",
        "detail": "Can thiệp phẫu thuật/nội soi/chẩn đoán hình ảnh, không cần gây mê toàn thân"
    },
    "IIIb": {
        "name": "Grade IIIb",
        "description": "Cần can thiệp, CẦN gây mê toàn thân",
        "detail": "Can thiệp phẫu thuật/nội soi/chẩn đoán hình ảnh, cần gây mê toàn thân"
    },
    "IVa": {
        "name": "Grade IVa",
        "description": "Biến chứng đe dọa tính mạng, suy một cơ quan, cần ICU",
        "detail": "Cần điều trị ICU, suy một cơ quan"
    },
    "IVb": {
        "name": "Grade IVb",
        "description": "Biến chứng đe dọa tính mạng, suy đa cơ quan, cần ICU",
        "detail": "Cần điều trị ICU, suy đa cơ quan"
    },
    "V": {
        "name": "Grade V",
        "description": "Tử vong",
        "detail": "Bệnh nhân tử vong"
    }
}


def render():
    """Render Clavien-Dindo Classification calculator"""
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🔪 Clavien-Dindo Classification</h2>
    <p style='text-align: center;'><em>Phân loại biến chứng sau phẫu thuật (DÙNG HÀNG NGÀY)</em></p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'clavien_dindo':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Clavien-Dindo Classification** phân loại biến chứng sau phẫu thuật:
        - Dùng hàng ngày trong phẫu thuật
        - Tiêu chuẩn quốc tế để báo cáo biến chứng
        - 5 mức độ (Grade I-V)
        
        ### 🎯 5 Mức độ
        
        - **Grade I:** Lệch khỏi bình thường, không cần điều trị
        - **Grade II:** Cần điều trị bằng thuốc
        - **Grade III:** Cần can thiệp
          - IIIa: Không cần gây mê toàn thân
          - IIIb: Cần gây mê toàn thân
        - **Grade IV:** Biến chứng đe dọa tính mạng, cần ICU
          - IVa: Suy một cơ quan
          - IVb: Suy đa cơ quan
        - **Grade V:** Tử vong
        
        ### 📊 Ý nghĩa
        
        - Grade I-II: Biến chứng nhẹ-trung bình
        - Grade III: Biến chứng nặng, cần can thiệp
        - Grade IV: Biến chứng rất nặng, đe dọa tính mạng
        - Grade V: Tử vong
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="clavien_dindo",
            calculator_name="Clavien-Dindo",
            category="Phẫu thuật",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Chọn mức độ biến chứng")
    
    st.markdown("""
    **Hướng dẫn:** Chọn mức độ biến chứng cao nhất mà bệnh nhân gặp phải.
    """)
    
    selected_grade = st.radio(
        "Clavien-Dindo Grade:",
        options=list(CLAVIEN_DINDO_GRADES.keys()),
        format_func=lambda x: f"{CLAVIEN_DINDO_GRADES[x]['name']}: {CLAVIEN_DINDO_GRADES[x]['description']}",
        index=0,
        help="Chọn mức độ biến chứng"
    )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Xem Kết quả", type="primary", use_container_width=True):
        grade_info = CLAVIEN_DINDO_GRADES[selected_grade]
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**Clavien-Dindo**",
                grade_info['name']
            )
        
        with col_r2:
            st.markdown(f"### {grade_info['description']}")
            st.caption(grade_info['detail'])
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if selected_grade == "I":
            st.success("""
            **✅ Grade I - Biến chứng nhẹ:**
            
            - Lệch khỏi diễn biến sau mổ bình thường
            - Không cần điều trị đặc biệt
            - Ví dụ: Sốt nhẹ, buồn nôn, đau nhiều
            - Không ảnh hưởng đáng kể đến kết quả
            """)
        elif selected_grade == "II":
            st.info("""
            **ℹ️ Grade II - Biến chứng trung bình:**
            
            - Cần điều trị bằng thuốc
            - Ví dụ: Nhiễm trùng cần kháng sinh, rối loạn nhịp tim cần thuốc
            - Có thể kéo dài thời gian nằm viện
            - Tiên lượng tốt với điều trị
            """)
        elif selected_grade.startswith("III"):
            st.warning("""
            **⚠️ Grade III - Biến chứng nặng, cần can thiệp:**
            
            - Cần can thiệp phẫu thuật/nội soi/chẩn đoán hình ảnh
            - **IIIa:** Không cần gây mê toàn thân (ví dụ: Chọc dò, nội soi)
            - **IIIb:** Cần gây mê toàn thân (ví dụ: Mổ lại)
            - Ảnh hưởng đáng kể đến kết quả
            - Cần theo dõi sát
            """)
        elif selected_grade.startswith("IV"):
            st.error("""
            **🚨 Grade IV - Biến chứng đe dọa tính mạng:**
            
            - Biến chứng đe dọa tính mạng
            - Cần điều trị ICU
            - **IVa:** Suy một cơ quan
            - **IVb:** Suy đa cơ quan
            - Tiên lượng xấu
            - Cần điều trị tích cực
            """)
        else:  # Grade V
            st.error("""
            **🚨🚨 Grade V - Tử vong:**
            
            - Bệnh nhân tử vong
            - Có thể liên quan đến biến chứng sau mổ
            - Cần đánh giá nguyên nhân
            - Báo cáo và phân tích
            """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Clavien-Dindo Grade": grade_info['name'],
            "Description": grade_info['description']
        }
        
        results_dict = {
            "Grade": grade_info['name'],
            "Description": grade_info['description'],
            "Detail": grade_info['detail']
        }
        
        # Export section
        render_export_section(
            title="Clavien-Dindo Classification",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Clavien-Dindo"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="clavien_dindo",
            calculator_name="Clavien-Dindo Classification",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="clavien_dindo",
            calculator_name="Clavien-Dindo Classification",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="clavien_dindo", show_actions=True)
        
        # References section
        references = get_references("Clavien-Dindo")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['clavien_dindo_result'] = {
            'grade': selected_grade,
            'description': grade_info['description']
        }
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("Clavien-Dindo")
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
            **Clavien-Dindo Classification**
            
            **Reference:**
            Dindo D, Demartines N, Clavien PA. Classification of surgical complications: 
            a new proposal with evaluation in a cohort of 6336 patients and results of a survey. 
            Ann Surg. 2004;240(2):205-213.
            
            **5 Grades:**
            - Grade I: Deviation from normal, no treatment needed
            - Grade II: Pharmacological treatment required
            - Grade III: Surgical/endoscopic/radiological intervention
              - IIIa: Without general anesthesia
              - IIIb: With general anesthesia
            - Grade IV: Life-threatening, ICU required
              - IVa: Single organ dysfunction
              - IVb: Multi-organ dysfunction
            - Grade V: Death
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

