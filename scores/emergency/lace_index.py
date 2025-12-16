"""
LACE Index
==========

Predicts 30-day readmission or death after hospital discharge

Reference:
- van Walraven C, et al. Derivation and validation of an index to predict early death 
  or unplanned readmission after discharge from hospital to the community. 
  CMAJ. 2010;182(6):551-557.

LACE Index Components (4 factors):
- L: Length of stay (days)
- A: Acuity of admission (emergent vs elective)
- C: Comorbidity (Charlson Comorbidity Index)
- E: Emergency department visits in past 6 months

Total: 0-19 points

Risk Stratification:
- 0-4: Low risk (<5%)
- 5-9: Moderate risk (5-10%)
- 10-14: High risk (10-20%)
- ≥15: Very high risk (>20%)

Clinical Utility:
- Predict 30-day readmission or death
- Discharge planning
- Resource allocation
- Quality improvement
"""

import streamlit as st
from components.ui.results import render_result_box
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def get_lace_length_points(length_of_stay: int) -> int:
    """Length of stay points"""
    if length_of_stay == 0:
        return 0
    elif length_of_stay == 1:
        return 1
    elif length_of_stay == 2:
        return 2
    elif length_of_stay == 3:
        return 3
    elif length_of_stay == 4:
        return 4
    elif length_of_stay == 5:
        return 5
    elif length_of_stay == 6:
        return 5
    elif length_of_stay <= 13:
        return 5
    else:
        return 7


def get_lace_acuity_points(is_emergent: bool) -> int:
    """Acuity of admission points"""
    if is_emergent:
        return 3
    else:
        return 0


def get_lace_comorbidity_points(charlson_index: int) -> int:
    """Comorbidity points (Charlson Index)"""
    if charlson_index == 0:
        return 0
    elif charlson_index == 1:
        return 1
    elif charlson_index == 2:
        return 2
    elif charlson_index == 3:
        return 3
    else:
        return 5


def get_lace_ed_points(ed_visits: int) -> int:
    """Emergency department visits points"""
    if ed_visits == 0:
        return 0
    elif ed_visits == 1:
        return 1
    elif ed_visits == 2:
        return 2
    elif ed_visits == 3:
        return 3
    elif ed_visits == 4:
        return 4
    else:
        return 4


def calculate_lace_index(
    length_of_stay: int,
    is_emergent: bool,
    charlson_index: int,
    ed_visits: int
) -> dict:
    """
    Calculate LACE Index
    
    Args:
        length_of_stay: Length of stay (days)
        is_emergent: Emergent admission (True) vs elective (False)
        charlson_index: Charlson Comorbidity Index
        ed_visits: Emergency department visits in past 6 months
    
    Returns:
        Dictionary with score and interpretation
    """
    # Calculate points for each component
    l_points = get_lace_length_points(length_of_stay)
    a_points = get_lace_acuity_points(is_emergent)
    c_points = get_lace_comorbidity_points(charlson_index)
    e_points = get_lace_ed_points(ed_visits)
    
    total_score = l_points + a_points + c_points + e_points
    
    # Risk stratification
    if total_score <= 4:
        risk = "<5%"
        interpretation = "Nguy cơ thấp"
        color = "success"
        severity = "Thấp"
    elif total_score <= 9:
        risk = "5-10%"
        interpretation = "Nguy cơ trung bình"
        color = "warning"
        severity = "Trung bình"
    elif total_score <= 14:
        risk = "10-20%"
        interpretation = "Nguy cơ cao"
        color = "error"
        severity = "Cao"
    else:
        risk = ">20%"
        interpretation = "Nguy cơ rất cao"
        color = "error"
        severity = "Rất cao"
    
    return {
        "total_score": total_score,
        "l_points": l_points,
        "a_points": a_points,
        "c_points": c_points,
        "e_points": e_points,
        "risk": risk,
        "interpretation": interpretation,
        "color": color,
        "severity": severity,
        "details": [
            f"L (Length of stay): {length_of_stay} ngày → {l_points} điểm",
            f"A (Acuity): {'Cấp cứu' if is_emergent else 'Theo kế hoạch'} → {a_points} điểm",
            f"C (Comorbidity): Charlson Index {charlson_index} → {c_points} điểm",
            f"E (ED visits): {ed_visits} lần trong 6 tháng qua → {e_points} điểm"
        ]
    }


def render():
    """LACE Index Calculator"""
    st.subheader("🏥 LACE Index")
    st.caption("Dự đoán tái nhập viện hoặc tử vong 30 ngày sau xuất viện")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'lace_index':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Smart Suggestions (sidebar)
    with st.sidebar:
        render_suggestions(
            calculator_id="lace_index",
            calculator_name="LACE Index",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    st.markdown("""
    **LACE Index** dự đoán nguy cơ tái nhập viện hoặc tử vong trong 30 ngày sau xuất viện.
    
    **4 yếu tố (tổng 0-19 điểm):**
    - **L:** Length of stay (Thời gian nằm viện) - 0-7 điểm
    - **A:** Acuity of admission (Mức độ cấp cứu) - 0-3 điểm
    - **C:** Comorbidity (Bệnh kèm theo - Charlson Index) - 0-5 điểm
    - **E:** Emergency department visits (Số lần cấp cứu trong 6 tháng) - 0-4 điểm
    
    **Phân tầng nguy cơ:**
    - **0-4 điểm:** Thấp (<5%)
    - **5-9 điểm:** Trung bình (5-10%)
    - **10-14 điểm:** Cao (10-20%)
    - **≥15 điểm:** Rất cao (>20%)
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📝 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        length_of_stay = st.number_input(
            "Thời gian nằm viện (ngày):",
            min_value=0,
            max_value=365,
            value=3,
            step=1,
            key="lace_los"
        )
        
        is_emergent = st.checkbox(
            "Nhập viện cấp cứu (không theo kế hoạch)",
            value=True,
            key="lace_emergent"
        )
    
    with col2:
        charlson_index = st.number_input(
            "Charlson Comorbidity Index:",
            min_value=0,
            max_value=30,
            value=0,
            step=1,
            key="lace_charlson",
            help="Tổng điểm Charlson Comorbidity Index (0 = không có bệnh kèm theo)"
        )
        
        ed_visits = st.number_input(
            "Số lần cấp cứu trong 6 tháng qua:",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key="lace_ed"
        )
    
    # Charlson Index helper
    with st.expander("💡 Hướng dẫn tính Charlson Comorbidity Index"):
        st.markdown("""
        **Charlson Comorbidity Index** đánh giá bệnh kèm theo:
        
        **1 điểm mỗi:**
        - Nhồi máu cơ tim
        - Suy tim
        - Bệnh mạch máu ngoại biên
        - Bệnh mạch máu não
        - Sa sút trí tuệ
        - Bệnh phổi mạn tính
        - Bệnh mô liên kết
        - Loét dạ dày
        - Bệnh gan nhẹ
        - Đái tháo đường (không biến chứng)
        
        **2 điểm mỗi:**
        - Bệnh thận mạn tính
        - Đái tháo đường (có biến chứng)
        - Bệnh gan vừa/nặng
        - Bệnh ác tính (localized)
        - Bệnh bạch cầu
        - Lymphoma
        
        **3 điểm mỗi:**
        - Bệnh ác tính (metastatic)
        - AIDS
        
        **6 điểm:**
        - Bệnh gan nặng
        
        **Tổng điểm:** Cộng tất cả các bệnh kèm theo
        """)
    
    st.markdown("---")
    
    if st.button("🧮 Tính LACE Index", type="primary", use_container_width=True):
        result = calculate_lace_index(
            length_of_stay,
            is_emergent,
            charlson_index,
            ed_visits
        )
        
        # Display results
        st.markdown("### 📊 Kết quả")
        
        render_result_box(
            "LACE Index",
            f"{result['total_score']}/19",
            subtitle=f"Nguy cơ: {result['risk']} - {result['interpretation']}",
            color=result['color'],
            icon="🏥"
        )
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown(f"""
            **L (Length of stay):** {result['l_points']} điểm
            - {result['details'][0]}
            
            **A (Acuity):** {result['a_points']} điểm
            - {result['details'][1]}
            """)
        
        with col4:
            st.markdown(f"""
            **C (Comorbidity):** {result['c_points']} điểm
            - {result['details'][2]}
            
            **E (ED visits):** {result['e_points']} điểm
            - {result['details'][3]}
            """)
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến nghị")
        
        if result['severity'] == "Thấp":
            st.success("""
            **✅ Nguy cơ thấp (<5%):**
            - Xuất viện theo kế hoạch bình thường
            - Hướng dẫn xuất viện chuẩn
            - Tái khám theo lịch
            """)
        elif result['severity'] == "Trung bình":
            st.warning("""
            **⚠️ Nguy cơ trung bình (5-10%):**
            - Tăng cường hướng dẫn xuất viện
            - Đảm bảo hiểu rõ thuốc
            - Tái khám trong 1 tuần
            - Cân nhắc chăm sóc tại nhà
            """)
        elif result['severity'] == "Cao":
            st.error("""
            **🚨 Nguy cơ cao (10-20%):**
            - Hướng dẫn xuất viện chi tiết
            - Tái khám trong 48-72 giờ
            - Cân nhắc chăm sóc tại nhà
            - Liên hệ với bệnh nhân sau 24-48 giờ
            """)
        else:
            st.error("""
            **🚨 Nguy cơ rất cao (>20%):**
            - Hướng dẫn xuất viện rất chi tiết
            - Tái khám trong 24-48 giờ
            - Cân nhắc chăm sóc tại nhà hoặc chuyển viện
            - Liên hệ với bệnh nhân sau 24 giờ
            - Điều chỉnh thuốc nếu cần
            - Đảm bảo có người chăm sóc
            """)
        
        # Prepare inputs for history and share
        inputs_dict = {
            "Length of Stay": f"{length_of_stay} ngày",
            "Is Emergent": "Có" if is_emergent else "Không",
            "Charlson Index": f"{charlson_index}",
            "ED Visits (6 months)": f"{ed_visits} lần"
        }
        
        results_dict = {
            "LACE Index": f"{result['total_score']}/19",
            "Risk": result['risk'],
            "Interpretation": result['interpretation'],
            "Severity": result['severity'],
            "L Points": result['l_points'],
            "A Points": result['a_points'],
            "C Points": result['c_points'],
            "E Points": result['e_points']
        }
        
        # Save to history
        save_calculation_to_history(
            calculator_id="lace_index",
            calculator_name="LACE Index",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="lace_index",
            calculator_name="LACE Index",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="lace_index", show_actions=True)
    
    st.markdown("---")
    
    with st.expander("📖 Bảng điểm LACE Index"):
        st.markdown("""
        ### L: Length of Stay (Thời gian nằm viện)
        
        | Thời gian | Điểm |
        |-----------|------|
        | 0 ngày | 0 |
        | 1 ngày | 1 |
        | 2 ngày | 2 |
        | 3 ngày | 3 |
        | 4 ngày | 4 |
        | 5-13 ngày | 5 |
        | ≥14 ngày | 7 |
        
        ### A: Acuity (Mức độ cấp cứu)
        
        | Loại nhập viện | Điểm |
        |----------------|------|
        | Theo kế hoạch (elective) | 0 |
        | Cấp cứu (emergent) | 3 |
        
        ### C: Comorbidity (Bệnh kèm theo - Charlson Index)
        
        | Charlson Index | Điểm |
        |----------------|------|
        | 0 | 0 |
        | 1 | 1 |
        | 2 | 2 |
        | 3 | 3 |
        | ≥4 | 5 |
        
        ### E: Emergency Department Visits (Số lần cấp cứu trong 6 tháng)
        
        | Số lần | Điểm |
        |--------|------|
        | 0 | 0 |
        | 1 | 1 |
        | 2 | 2 |
        | 3 | 3 |
        | ≥4 | 4 |
        """)
    
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        **Tài liệu tham khảo:**
        
        - van Walraven C, et al. Derivation and validation of an index to predict early death 
          or unplanned readmission after discharge from hospital to the community. 
          CMAJ. 2010;182(6):551-557.
        """)
    
    # References section
    references = get_references("LACE Index")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.caption("⚠️ LACE Index chỉ là công cụ hỗ trợ. Quyết định xuất viện phải dựa trên đánh giá lâm sàng toàn diện.")

