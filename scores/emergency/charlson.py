"""
Charlson Comorbidity Index Calculator
======================================

Predicts 10-year mortality based on comorbidities

Reference:
- Charlson ME, et al. A new method of classifying prognostic comorbidity in 
  longitudinal studies: development and validation. J Chronic Dis. 1987;40(5):373-383.
- Updated weights: Charlson ME, et al. Validation of a combined comorbidity index. 
  J Clin Epidemiol. 1994;47(12):1245-1251.

Charlson Comorbidity Index Components (19 conditions):
1. Myocardial infarction (1 point)
2. Congestive heart failure (1 point)
3. Peripheral vascular disease (1 point)
4. Cerebrovascular disease (1 point)
5. Dementia (1 point)
6. Chronic pulmonary disease (1 point)
7. Connective tissue disease (1 point)
8. Ulcer disease (1 point)
9. Mild liver disease (1 point)
10. Diabetes without complications (1 point)
11. Hemiplegia (2 points)
12. Moderate to severe renal disease (2 points)
13. Diabetes with complications (2 points)
14. Any tumor (2 points)
15. Leukemia (2 points)
16. Lymphoma (2 points)
17. Moderate to severe liver disease (3 points)
18. Metastatic solid tumor (6 points)
19. AIDS (6 points)

Total: 0-37 points

10-Year Mortality Risk:
- 0 points: ~12%
- 1-2 points: ~26%
- 3-4 points: ~52%
- ≥5 points: ~85%

Clinical Utility:
- Used widely in research and clinical practice
- Predicts mortality and healthcare utilization
- Adjusts for comorbidities in studies
- Guides treatment decisions
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


CHARLSON_CONDITIONS = {
    # 1 point conditions
    "myocardial_infarction": {"name": "Nhồi máu cơ tim", "points": 1},
    "heart_failure": {"name": "Suy tim", "points": 1},
    "peripheral_vascular": {"name": "Bệnh mạch máu ngoại biên", "points": 1},
    "cerebrovascular": {"name": "Bệnh mạch máu não", "points": 1},
    "dementia": {"name": "Sa sút trí tuệ", "points": 1},
    "copd": {"name": "Bệnh phổi mạn tính", "points": 1},
    "connective_tissue": {"name": "Bệnh mô liên kết", "points": 1},
    "peptic_ulcer": {"name": "Loét dạ dày-tá tràng", "points": 1},
    "mild_liver": {"name": "Bệnh gan nhẹ", "points": 1},
    "diabetes_no_complications": {"name": "Đái tháo đường không biến chứng", "points": 1},
    
    # 2 points conditions
    "hemiplegia": {"name": "Liệt nửa người", "points": 2},
    "renal_disease": {"name": "Bệnh thận trung bình-nặng", "points": 2},
    "diabetes_with_complications": {"name": "Đái tháo đường có biến chứng", "points": 2},
    "any_tumor": {"name": "U bất kỳ (không di căn)", "points": 2},
    "leukemia": {"name": "Bệnh bạch cầu", "points": 2},
    "lymphoma": {"name": "Lymphoma", "points": 2},
    
    # 3 points conditions
    "moderate_severe_liver": {"name": "Bệnh gan trung bình-nặng", "points": 3},
    
    # 6 points conditions
    "metastatic_tumor": {"name": "U di căn", "points": 6},
    "aids": {"name": "AIDS", "points": 6},
}


def calculate_charlson_index(selected_conditions: list) -> dict:
    """
    Calculate Charlson Comorbidity Index
    
    Args:
        selected_conditions: List of condition keys that are present
    
    Returns:
        Dictionary with total score and mortality risk
    """
    total_score = 0
    details = []
    
    for condition_key in selected_conditions:
        if condition_key in CHARLSON_CONDITIONS:
            condition = CHARLSON_CONDITIONS[condition_key]
            total_score += condition['points']
            details.append(f"✓ {condition['name']} → +{condition['points']} điểm")
    
    if not details:
        details.append("Không có bệnh lý mạn tính")
    
    # Estimate 10-year mortality risk
    if total_score == 0:
        mortality_risk = "~12%"
        risk_category = "Thấp"
        risk_class = "LOW"
    elif total_score <= 2:
        mortality_risk = "~26%"
        risk_category = "Trung bình"
        risk_class = "MODERATE"
    elif total_score <= 4:
        mortality_risk = "~52%"
        risk_category = "Cao"
        risk_class = "HIGH"
    else:
        mortality_risk = "~85%"
        risk_category = "Rất cao"
        risk_class = "VERY_HIGH"
    
    return {
        'total_score': total_score,
        'mortality_risk': mortality_risk,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'details': details
    }


def render():
    """Render Charlson Comorbidity Index calculator"""
    
    # st.title("🏥 Charlson Comorbidity Index")
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🏥 Charlson Comorbidity Index</h2>
    <p style='text-align: center;'><em>Dự đoán tử vong 10 năm dựa trên bệnh lý mạn tính</em></p>
    """, unsafe_allow_html=True)
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'charlson':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information - Enhanced with Phase 1
    if CALCULATOR_ENHANCEMENTS_AVAILABLE:
        render_calculator_explanation(
            title="Về Charlson Comorbidity Index",
            content="""
            **Charlson Comorbidity Index** dự đoán tử vong 10 năm dựa trên bệnh lý mạn tính:
            
            - Dùng rộng rãi trong nghiên cứu và lâm sàng
            - Điều chỉnh cho bệnh lý kèm theo trong các nghiên cứu
            - Hướng dẫn quyết định điều trị
            - 19 bệnh lý mạn tính với điểm số khác nhau (1-6 điểm)
            
            **19 bệnh lý mạn tính:**
            - **1 điểm:** Nhồi máu cơ tim, Suy tim, Bệnh mạch máu ngoại biên, Bệnh mạch máu não, Sa sút trí tuệ, Bệnh phổi mạn tính, Bệnh mô liên kết, Loét dạ dày-tá tràng, Bệnh gan nhẹ, Đái tháo đường không biến chứng
            - **2 điểm:** Liệt nửa người, Bệnh thận trung bình-nặng, Đái tháo đường có biến chứng, U bất kỳ (không di căn), Bệnh bạch cầu, Lymphoma
            - **3 điểm:** Bệnh gan trung bình-nặng
            - **6 điểm:** U di căn, AIDS
            
            **Tổng điểm: 0-37**
            """,
            when_to_use="""
            **Sử dụng Charlson Comorbidity Index khi:**
            - Cần đánh giá nguy cơ tử vong 10 năm
            - Điều chỉnh cho bệnh lý kèm theo trong nghiên cứu
            - Hướng dẫn quyết định điều trị
            - Đánh giá healthcare utilization
            """,
            limitations="""
            **Hạn chế:**
            - Dự đoán tử vong 10 năm, không phải ngắn hạn
            - Dựa trên bệnh lý mạn tính, không tính đến bệnh cấp tính
            - Một số bệnh lý có thể không được ghi nhận đầy đủ
            - Không thay thế đánh giá lâm sàng cá thể hóa
            """,
            clinical_context="""
            **Bối cảnh lâm sàng:**
            - **0 điểm:** Tử vong 10 năm ~12% → Nguy cơ thấp
            - **1-2 điểm:** Tử vong 10 năm ~26% → Nguy cơ trung bình
            - **3-4 điểm:** Tử vong 10 năm ~52% → Nguy cơ cao
            - **≥5 điểm:** Tử vong 10 năm ~85% → Nguy cơ rất cao
            - Charlson Index cao cần cân nhắc kỹ khi quyết định điều trị xâm lấn
            """
        )
        
        # Evidence citation
        render_evidence_citation(
            citation_text="Charlson ME, et al. A new method of classifying prognostic comorbidity in longitudinal studies: development and validation. J Chronic Dis. 1987;40(5):373-83.",
            doi="10.1016/0021-9681(87)90171-8",
            pmid="3558716"
        )
    else:
        # Fallback to original expander
        with st.expander("ℹ️ Thông tin & cách sử dụng"):
            st.markdown("""
            ### 📋 Giới Thiệu
            
            **Charlson Comorbidity Index** dự đoán tử vong 10 năm:
            - Dùng rộng rãi trong nghiên cứu và lâm sàng
            - Điều chỉnh cho bệnh lý kèm theo trong các nghiên cứu
            - 19 bệnh lý mạn tính với điểm số khác nhau
            
            ### 🎯 19 Bệnh lý mạn tính
            
            **1 điểm:**
            - Nhồi máu cơ tim, Suy tim, Bệnh mạch máu ngoại biên, Bệnh mạch máu não
            - Sa sút trí tuệ, Bệnh phổi mạn tính, Bệnh mô liên kết
            - Loét dạ dày-tá tràng, Bệnh gan nhẹ, Đái tháo đường không biến chứng
            
            **2 điểm:**
        - Liệt nửa người, Bệnh thận trung bình-nặng, Đái tháo đường có biến chứng
        - U bất kỳ (không di căn), Bệnh bạch cầu, Lymphoma
        
        **3 điểm:**
        - Bệnh gan trung bình-nặng
        
        **6 điểm:**
        - U di căn, AIDS
        
        ### 📊 Nguy cơ tử vong 10 năm
        
        - **0 điểm:** ~12%
        - **1-2 điểm:** ~26%
        - **3-4 điểm:** ~52%
        - **≥5 điểm:** ~85%
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="charlson",
            calculator_name="Charlson Comorbidity Index",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Chọn bệnh lý mạn tính")
    
    st.markdown("**Chọn tất cả các bệnh lý mạn tính mà bệnh nhân đang mắc:**")
    
    selected_conditions = []
    
    # 1 point conditions
    st.markdown("#### 1 điểm mỗi bệnh:")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.checkbox(CHARLSON_CONDITIONS["myocardial_infarction"]["name"], key="charlson_mi"):
            selected_conditions.append("myocardial_infarction")
        if st.checkbox(CHARLSON_CONDITIONS["heart_failure"]["name"], key="charlson_hf"):
            selected_conditions.append("heart_failure")
        if st.checkbox(CHARLSON_CONDITIONS["peripheral_vascular"]["name"], key="charlson_pvd"):
            selected_conditions.append("peripheral_vascular")
        if st.checkbox(CHARLSON_CONDITIONS["cerebrovascular"]["name"], key="charlson_cvd"):
            selected_conditions.append("cerebrovascular")
        if st.checkbox(CHARLSON_CONDITIONS["dementia"]["name"], key="charlson_dementia"):
            selected_conditions.append("dementia")
    
    with col2:
        if st.checkbox(CHARLSON_CONDITIONS["copd"]["name"], key="charlson_copd"):
            selected_conditions.append("copd")
        if st.checkbox(CHARLSON_CONDITIONS["connective_tissue"]["name"], key="charlson_ctd"):
            selected_conditions.append("connective_tissue")
        if st.checkbox(CHARLSON_CONDITIONS["peptic_ulcer"]["name"], key="charlson_ulcer"):
            selected_conditions.append("peptic_ulcer")
        if st.checkbox(CHARLSON_CONDITIONS["mild_liver"]["name"], key="charlson_mild_liver"):
            selected_conditions.append("mild_liver")
        if st.checkbox(CHARLSON_CONDITIONS["diabetes_no_complications"]["name"], key="charlson_dm1"):
            selected_conditions.append("diabetes_no_complications")
    
    st.markdown("#### 2 điểm mỗi bệnh:")
    col3, col4 = st.columns(2)
    
    with col3:
        if st.checkbox(CHARLSON_CONDITIONS["hemiplegia"]["name"], key="charlson_hemiplegia"):
            selected_conditions.append("hemiplegia")
        if st.checkbox(CHARLSON_CONDITIONS["renal_disease"]["name"], key="charlson_renal"):
            selected_conditions.append("renal_disease")
        if st.checkbox(CHARLSON_CONDITIONS["diabetes_with_complications"]["name"], key="charlson_dm2"):
            selected_conditions.append("diabetes_with_complications")
    
    with col4:
        if st.checkbox(CHARLSON_CONDITIONS["any_tumor"]["name"], key="charlson_tumor"):
            selected_conditions.append("any_tumor")
        if st.checkbox(CHARLSON_CONDITIONS["leukemia"]["name"], key="charlson_leukemia"):
            selected_conditions.append("leukemia")
        if st.checkbox(CHARLSON_CONDITIONS["lymphoma"]["name"], key="charlson_lymphoma"):
            selected_conditions.append("lymphoma")
    
    st.markdown("#### 3 điểm:")
    if st.checkbox(CHARLSON_CONDITIONS["moderate_severe_liver"]["name"], key="charlson_liver"):
        selected_conditions.append("moderate_severe_liver")
    
    st.markdown("#### 6 điểm mỗi bệnh:")
    col5, col6 = st.columns(2)
    
    with col5:
        if st.checkbox(CHARLSON_CONDITIONS["metastatic_tumor"]["name"], key="charlson_metastatic"):
            selected_conditions.append("metastatic_tumor")
    
    with col6:
        if st.checkbox(CHARLSON_CONDITIONS["aids"]["name"], key="charlson_aids"):
            selected_conditions.append("aids")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Charlson Index", type="primary", use_container_width=True):
        result = calculate_charlson_index(selected_conditions)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**Charlson Index**",
                f"{result['total_score']}"
            )
        
        with col_r2:
            st.markdown(f"### {result['risk_category'].upper()}")
            st.caption(f"Nguy cơ tử vong 10 năm: {result['mortality_risk']}")
        
        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
            st.markdown(f"**Tổng điểm: {result['total_score']}**")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['risk_class'] == "LOW":
            st.success(f"""
            **✅ Nguy cơ tử vong THẤP ({result['mortality_risk']}):**
            
            - Ít bệnh lý mạn tính
            - Tiên lượng tốt
            - Có thể điều trị tích cực
            """)
        elif result['risk_class'] == "MODERATE":
            st.warning(f"""
            **⚠️ Nguy cơ tử vong TRUNG BÌNH ({result['mortality_risk']}):**
            
            - Có một số bệnh lý mạn tính
            - Cần điều chỉnh điều trị phù hợp
            - Theo dõi sát
            """)
        elif result['risk_class'] == "HIGH":
            st.error(f"""
            **🚨 Nguy cơ tử vong CAO ({result['mortality_risk']}):**
            
            - Nhiều bệnh lý mạn tính
            - Tiên lượng xấu hơn
            - Cần điều trị thận trọng
            - Cân nhắc mục tiêu điều trị
            """)
        else:
            st.error(f"""
            **🚨🚨 Nguy cơ tử vong RẤT CAO ({result['mortality_risk']}):**
            
            - Rất nhiều bệnh lý mạn tính nặng
            - Tiên lượng rất xấu
            - Cần điều trị thận trọng
            - Cân nhắc mục tiêu điều trị và chăm sóc giảm nhẹ
            """)
        
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - Charlson Index dùng để điều chỉnh trong nghiên cứu và đánh giá tiên lượng
        - Không thay thế đánh giá lâm sàng toàn diện
        - Cần kết hợp với tuổi, tình trạng chức năng, và các yếu tố khác
        - Quyết định điều trị cuối cùng thuộc về bác sĩ lâm sàng
        """)
        
        # Prepare inputs and results
        conditions_list = [CHARLSON_CONDITIONS[c]['name'] for c in selected_conditions]
        inputs_dict = {
            "Selected Conditions": ", ".join(conditions_list) if conditions_list else "Không có"
        }
        
        results_dict = {
            "Charlson Index": f"{result['total_score']}",
            "10-Year Mortality Risk": result['mortality_risk'],
            "Risk Category": result['risk_category']
        }
        
        # Export section
        render_export_section(
            title="Charlson Comorbidity Index",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Charlson Index"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="charlson",
            calculator_name="Charlson Comorbidity Index",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="charlson",
            calculator_name="Charlson Comorbidity Index",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="charlson", show_actions=True)
        
        # References section
        references = get_references("Charlson")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['charlson_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("Charlson")
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
            **Charlson Comorbidity Index**
            
            **Reference:**
            Charlson ME, Pompei P, Ales KL, MacKenzie CR. A new method of classifying 
            prognostic comorbidity in longitudinal studies: development and validation. 
            J Chronic Dis. 1987;40(5):373-383.
            
            **19 Conditions with different weights:**
            - 1 point: 10 conditions (MI, HF, PVD, CVD, dementia, COPD, etc.)
            - 2 points: 6 conditions (hemiplegia, renal disease, diabetes with complications, etc.)
            - 3 points: 1 condition (moderate-severe liver disease)
            - 6 points: 2 conditions (metastatic tumor, AIDS)
            
            **Total: 0-37 points**
            
            **10-Year Mortality Risk:**
            - 0: ~12%
            - 1-2: ~26%
            - 3-4: ~52%
            - ≥5: ~85%
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

