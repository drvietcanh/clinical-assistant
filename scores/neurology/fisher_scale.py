"""
Fisher Scale Calculator
========================

Assesses risk of vasospasm after subarachnoid hemorrhage

Reference:
- Fisher CM, et al. Relation of cerebral vasospasm to subarachnoid hemorrhage 
  visualized by computerized tomographic scanning. Neurosurgery. 1980;6(1):1-9.

Fisher Scale Components:
- Amount of blood on CT scan

Classification:
- Grade 1: No blood detected
- Grade 2: Diffuse or vertical layers <1 mm thick
- Grade 3: Localized clot and/or vertical layer ≥1 mm thick
- Grade 4: Intraparenchymal or intraventricular clot with diffuse or no SAH

Risk of Vasospasm:
- Grade 1-2: Low risk
- Grade 3: High risk
- Grade 4: Variable risk

Clinical Utility:
- Predict risk of cerebral vasospasm after SAH
- Guide monitoring and treatment decisions
- Help determine need for nimodipine prophylaxis
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
from components.export import render_export_section
# ======================================


def calculate_fisher_scale(fisher_grade: int) -> dict:
    """
    Calculate Fisher Scale assessment
    
    Args:
        fisher_grade: Fisher grade (1-4)
    
    Returns:
        Dictionary with grade, risk assessment, and interpretation
    """
    grade_descriptions = {
        1: {
            'description': 'Không phát hiện máu',
            'risk': 'Thấp',
            'risk_class': 'LOW',
            'vasospasm_risk': 'Thấp',
            'color': COLORS['success']
        },
        2: {
            'description': 'Máu lan tỏa hoặc lớp dọc <1 mm',
            'risk': 'Thấp',
            'risk_class': 'LOW',
            'vasospasm_risk': 'Thấp',
            'color': COLORS['success']
        },
        3: {
            'description': 'Cục máu khu trú và/hoặc lớp dọc ≥1 mm',
            'risk': 'Cao',
            'risk_class': 'HIGH',
            'vasospasm_risk': 'Cao',
            'color': COLORS['error']
        },
        4: {
            'description': 'Máu trong nhu mô hoặc não thất, có hoặc không có SAH lan tỏa',
            'risk': 'Thay đổi',
            'risk_class': 'VARIABLE',
            'vasospasm_risk': 'Thay đổi',
            'color': COLORS['warning']
        }
    }
    
    grade_info = grade_descriptions.get(fisher_grade, {})
    
    return {
        'grade': fisher_grade,
        'description': grade_info.get('description', 'N/A'),
        'risk': grade_info.get('risk', 'N/A'),
        'risk_class': grade_info.get('risk_class', 'UNKNOWN'),
        'vasospasm_risk': grade_info.get('vasospasm_risk', 'N/A'),
        'color': grade_info.get('color', COLORS['info'])
    }


def render():
    """Render Fisher Scale calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 Fisher Scale</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá nguy cơ co thắt mạch sau xuất huyết dưới nhện**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'fisher_scale':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Fisher Scale** đánh giá nguy cơ co thắt mạch sau xuất huyết dưới nhện (SAH):
        - Dựa trên lượng máu trên CT scan
        - Dự đoán nguy cơ co thắt mạch não
        - Hướng dẫn điều trị và theo dõi
        
        ### 🎯 Phân loại (4 mức độ)
        
        **Grade 1:** Không phát hiện máu
        - Nguy cơ co thắt mạch: Thấp
        
        **Grade 2:** Máu lan tỏa hoặc lớp dọc <1 mm
        - Nguy cơ co thắt mạch: Thấp
        
        **Grade 3:** Cục máu khu trú và/hoặc lớp dọc ≥1 mm
        - Nguy cơ co thắt mạch: **Cao** ⚠️
        
        **Grade 4:** Máu trong nhu mô hoặc não thất, có hoặc không có SAH lan tỏa
        - Nguy cơ co thắt mạch: Thay đổi
        
        ### 📊 Nguy cơ co thắt mạch
        
        | Grade | Nguy cơ | Khuyến nghị |
        |-------|---------|-------------|
        | 1-2 | Thấp | Theo dõi thường quy |
        | 3 | Cao | Theo dõi sát, nimodipine |
        | 4 | Thay đổi | Đánh giá cá thể hóa |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân SAH
        - Đánh giá trên CT scan sớm (24-48 giờ đầu)
        - Grade 3 có nguy cơ co thắt mạch cao nhất
        - Kết hợp với Hunt & Hess Scale để đánh giá toàn diện
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="fisher_scale",
            calculator_name="Fisher Scale",
            category="Thần kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin từ CT scan")
    
    fisher_grade = st.selectbox(
        "Fisher Grade",
        [
            (1, "Grade 1: Không phát hiện máu"),
            (2, "Grade 2: Máu lan tỏa hoặc lớp dọc <1 mm"),
            (3, "Grade 3: Cục máu khu trú và/hoặc lớp dọc ≥1 mm"),
            (4, "Grade 4: Máu trong nhu mô hoặc não thất, có hoặc không có SAH lan tỏa")
        ],
        index=2,
        format_func=lambda x: x[1],
        help="Phân loại dựa trên lượng máu trên CT scan"
    )
    fisher_grade = fisher_grade[0]
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Đánh giá Fisher Scale", type="primary", use_container_width=True):
        result = calculate_fisher_scale(fisher_grade)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "LOW": "✅",
            "HIGH": "🚨",
            "VARIABLE": "⚠️"
        }
        icon = icon_map.get(result['risk_class'], "🧠")
        
        render_score_result(
            title=f"Fisher Grade {result['grade']}",
            score=f"Grade {result['grade']}",
            interpretation=f"{result['description']} - Nguy cơ co thắt mạch: {result['vasospasm_risk']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **Fisher Grade {result['grade']}** - Nguy cơ thấp
            
            - **Mô tả:** {result['description']}
            - **Nguy cơ co thắt mạch:** {result['vasospasm_risk']}
            - Theo dõi thường quy
            - Cân nhắc nimodipine prophylaxis
            """)
        elif result['risk_class'] == "HIGH":
            st.error(f"""
            **Fisher Grade {result['grade']}** - Nguy cơ cao ⚠️
            
            - **Mô tả:** {result['description']}
            - **Nguy cơ co thắt mạch:** {result['vasospasm_risk']}
            - **Khuyến cáo:**
              → Theo dõi sát (TCD, DSA nếu cần)
              → Nimodipine prophylaxis (60mg mỗi 4 giờ)
              → Điều trị tăng huyết áp (nếu cần)
              → Theo dõi triệu chứng thần kinh
            - Nguy cơ co thắt mạch cao nhất ở Grade 3
            """)
        else:
            st.warning(f"""
            **Fisher Grade {result['grade']}** - Nguy cơ thay đổi
            
            - **Mô tả:** {result['description']}
            - **Nguy cơ co thắt mạch:** {result['vasospasm_risk']}
            - Đánh giá cá thể hóa dựa trên lâm sàng
            - Cân nhắc các yếu tố khác (Hunt & Hess, tuổi, bệnh lý kèm theo)
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - Fisher Scale giúp dự đoán nguy cơ co thắt mạch sau SAH
        - **Grade 3:** Nguy cơ cao nhất, cần theo dõi sát và điều trị dự phòng
        - Kết hợp với Hunt & Hess Scale để đánh giá toàn diện
        - Nimodipine được khuyến cáo cho tất cả bệnh nhân SAH (trừ chống chỉ định)
        - Theo dõi triệu chứng thần kinh và TCD nếu có
        - Co thắt mạch thường xảy ra vào ngày 4-14 sau SAH
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'fisher_scale',
            'calculator_name': 'Fisher Scale',
            'inputs': {
                'fisher_grade': fisher_grade
            },
            'results': {
                'grade': result['grade'],
                'description': result['description'],
                'risk': result['risk'],
                'vasospasm_risk': result['vasospasm_risk']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('fisher_scale')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Fisher CM, et al. Relation of cerebral vasospasm to subarachnoid hemorrhage 
          visualized by computerized tomographic scanning. Neurosurgery. 1980;6(1):1-9.
        """)
    
    # History
    render_history_ui(calculator_id="fisher_scale", show_actions=True)
