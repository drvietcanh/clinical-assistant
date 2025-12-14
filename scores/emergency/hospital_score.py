"""
HOSPITAL Score
==============

Predicts 30-day readmission risk for hospitalized patients

Reference:
- Donze J, et al. Potentially avoidable 30-day hospital readmissions in medical patients:
  derivation and validation of a prediction model. JAMA Intern Med. 2013;173(8):632-638.

HOSPITAL Score Components (7 factors):
- H: Hemoglobin at discharge (<12 g/dL)
- O: Discharge from Oncology service
- S: Sodium level at discharge (<135 mEq/L)
- P: Procedure during admission
- I: Index admission type (non-elective)
- T: Number of admissions in past year (≥2)
- A: Length of stay (≥5 days)
- L: (not used in score, but in acronym)

Total: 0-13 points

Clinical Utility:
- Predict 30-day readmission risk
- Identify high-risk patients for discharge planning
- Quality improvement
- Resource allocation
"""

import streamlit as st
from components.ui.results import render_result_box


def calculate_hospital_score(
    hemoglobin: float,
    is_oncology: bool,
    sodium: float,
    had_procedure: bool,
    is_elective: bool,
    admissions_past_year: int,
    length_of_stay: int
) -> dict:
    """
    Calculate HOSPITAL Score
    
    Args:
        hemoglobin: Hemoglobin at discharge (g/dL)
        is_oncology: Discharged from oncology service
        sodium: Sodium at discharge (mEq/L)
        had_procedure: Had procedure during admission
        is_elective: Elective admission (False = non-elective)
        admissions_past_year: Number of admissions in past year
        length_of_stay: Length of stay (days)
    
    Returns:
        Dictionary with score and interpretation
    """
    score = 0
    details = []
    
    # H: Hemoglobin <12 g/dL
    if hemoglobin < 12:
        score += 1
        details.append(f"H: Hemoglobin {hemoglobin:.1f} g/dL <12 → 1 điểm")
    else:
        details.append(f"H: Hemoglobin {hemoglobin:.1f} g/dL ≥12 → 0 điểm")
    
    # O: Oncology service
    if is_oncology:
        score += 2
        details.append("O: Xuất viện từ khoa Ung thư → 2 điểm")
    else:
        details.append("O: Không phải khoa Ung thư → 0 điểm")
    
    # S: Sodium <135 mEq/L
    if sodium < 135:
        score += 1
        details.append(f"S: Sodium {sodium:.0f} mEq/L <135 → 1 điểm")
    else:
        details.append(f"S: Sodium {sodium:.0f} mEq/L ≥135 → 0 điểm")
    
    # P: Procedure during admission
    if had_procedure:
        score += 1
        details.append("P: Có thủ thuật/phẫu thuật → 1 điểm")
    else:
        details.append("P: Không có thủ thuật/phẫu thuật → 0 điểm")
    
    # I: Non-elective admission
    if not is_elective:
        score += 1
        details.append("I: Nhập viện không theo kế hoạch → 1 điểm")
    else:
        details.append("I: Nhập viện theo kế hoạch → 0 điểm")
    
    # T: ≥2 admissions in past year
    if admissions_past_year >= 2:
        score += 2
        details.append(f"T: ≥2 lần nhập viện trong năm qua ({admissions_past_year} lần) → 2 điểm")
    else:
        details.append(f"T: <2 lần nhập viện trong năm qua ({admissions_past_year} lần) → 0 điểm")
    
    # A: Length of stay ≥5 days
    if length_of_stay >= 5:
        score += 1
        details.append(f"A: Thời gian nằm viện ≥5 ngày ({length_of_stay} ngày) → 1 điểm")
    else:
        details.append(f"A: Thời gian nằm viện <5 ngày ({length_of_stay} ngày) → 0 điểm")
    
    # Risk stratification
    if score <= 4:
        readmission_risk = "<10%"
        interpretation = "Nguy cơ tái nhập viện thấp"
        color = "success"
        severity = "Thấp"
    elif score <= 6:
        readmission_risk = "10-20%"
        interpretation = "Nguy cơ tái nhập viện trung bình"
        color = "warning"
        severity = "Trung bình"
    else:
        readmission_risk = ">20%"
        interpretation = "Nguy cơ tái nhập viện cao"
        color = "error"
        severity = "Cao"
    
    return {
        "total_score": score,
        "readmission_risk": readmission_risk,
        "interpretation": interpretation,
        "color": color,
        "severity": severity,
        "details": details
    }


def render():
    """HOSPITAL Score Calculator"""
    st.subheader("🏥 HOSPITAL Score")
    st.caption("Dự đoán nguy cơ tái nhập viện 30 ngày")
    
    st.markdown("""
    **HOSPITAL Score** dự đoán nguy cơ tái nhập viện trong 30 ngày sau xuất viện.
    
    **7 yếu tố (tổng 0-13 điểm):**
    - **H:** Hemoglobin <12 g/dL (1 điểm)
    - **O:** Xuất viện từ khoa Ung thư (2 điểm)
    - **S:** Sodium <135 mEq/L (1 điểm)
    - **P:** Có thủ thuật/phẫu thuật (1 điểm)
    - **I:** Nhập viện không theo kế hoạch (1 điểm)
    - **T:** ≥2 lần nhập viện trong năm qua (2 điểm)
    - **A:** Thời gian nằm viện ≥5 ngày (1 điểm)
    
    **Nguy cơ tái nhập viện:**
    - **≤4 điểm:** <10% (Thấp)
    - **5-6 điểm:** 10-20% (Trung bình)
    - **≥7 điểm:** >20% (Cao)
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📝 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        hemoglobin = st.number_input(
            "Hemoglobin khi xuất viện (g/dL):",
            min_value=0.0,
            max_value=20.0,
            value=12.0,
            step=0.1,
            key="hospital_hb"
        )
        
        is_oncology = st.checkbox(
            "Xuất viện từ khoa Ung thư",
            key="hospital_oncology"
        )
        
        sodium = st.number_input(
            "Sodium khi xuất viện (mEq/L):",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            key="hospital_na"
        )
        
        had_procedure = st.checkbox(
            "Có thủ thuật/phẫu thuật trong lần nhập viện này",
            key="hospital_procedure"
        )
    
    with col2:
        is_elective = st.checkbox(
            "Nhập viện theo kế hoạch (elective)",
            value=True,
            key="hospital_elective"
        )
        
        admissions_past_year = st.number_input(
            "Số lần nhập viện trong 12 tháng qua:",
            min_value=0,
            max_value=20,
            value=0,
            step=1,
            key="hospital_admissions"
        )
        
        length_of_stay = st.number_input(
            "Thời gian nằm viện (ngày):",
            min_value=0,
            max_value=365,
            value=3,
            step=1,
            key="hospital_los"
        )
    
    st.markdown("---")
    
    if st.button("🧮 Tính HOSPITAL Score", type="primary", use_container_width=True):
        result = calculate_hospital_score(
            hemoglobin,
            is_oncology,
            sodium,
            had_procedure,
            is_elective,
            admissions_past_year,
            length_of_stay
        )
        
        # Display results
        st.markdown("### 📊 Kết quả")
        
        render_result_box(
            "HOSPITAL Score",
            f"{result['total_score']}/13",
            subtitle=f"Nguy cơ tái nhập viện: {result['readmission_risk']}",
            color=result['color'],
            icon="🏥"
        )
        
        st.markdown(f"**Đánh giá:** {result['interpretation']}")
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        for detail in result['details']:
            st.markdown(f"- {detail}")
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến nghị")
        
        if result['severity'] == "Thấp":
            st.success("""
            **✅ Nguy cơ tái nhập viện thấp (<10%):**
            - Xuất viện theo kế hoạch bình thường
            - Hướng dẫn xuất viện chuẩn
            - Tái khám theo lịch
            """)
        elif result['severity'] == "Trung bình":
            st.warning("""
            **⚠️ Nguy cơ tái nhập viện trung bình (10-20%):**
            - Tăng cường hướng dẫn xuất viện
            - Đảm bảo hiểu rõ thuốc và chế độ ăn
            - Tái khám sớm (trong 1 tuần)
            - Cân nhắc chăm sóc tại nhà
            """)
        else:
            st.error("""
            **🚨 Nguy cơ tái nhập viện cao (>20%):**
            - Hướng dẫn xuất viện chi tiết
            - Đảm bảo có người chăm sóc
            - Tái khám trong 48-72 giờ
            - Cân nhắc chăm sóc tại nhà hoặc chuyển viện
            - Liên hệ với bệnh nhân sau 24-48 giờ
            - Điều chỉnh thuốc nếu cần
            """)
        
        st.markdown("---")
        st.info("""
        **💡 Các biện pháp giảm nguy cơ tái nhập viện:**
        
        1. **Hướng dẫn xuất viện:**
           - Giải thích rõ ràng về bệnh và điều trị
           - Đảm bảo hiểu rõ cách dùng thuốc
           - Hướng dẫn dấu hiệu cần tái khám ngay
        
        2. **Theo dõi sau xuất viện:**
           - Tái khám sớm
           - Liên hệ với bệnh nhân sau 24-48 giờ
           - Điều chỉnh thuốc nếu cần
        
        3. **Hỗ trợ xã hội:**
           - Đảm bảo có người chăm sóc
           - Hỗ trợ vận chuyển nếu cần
           - Liên kết với dịch vụ chăm sóc tại nhà
        """)
    
    st.markdown("---")
    
    with st.expander("📖 Thông tin về HOSPITAL Score"):
        st.markdown("""
        **HOSPITAL Score** dự đoán nguy cơ tái nhập viện trong 30 ngày sau xuất viện.
        
        **7 yếu tố:**
        1. **H:** Hemoglobin <12 g/dL
        2. **O:** Discharge from Oncology service
        3. **S:** Sodium <135 mEq/L
        4. **P:** Procedure during admission
        5. **I:** Index admission type (non-elective)
        6. **T:** Number of admissions in past year (≥2)
        7. **A:** Length of stay (≥5 days)
        
        **Tài liệu tham khảo:**
        - Donze J, et al. Potentially avoidable 30-day hospital readmissions in medical patients:
          derivation and validation of a prediction model. JAMA Intern Med. 2013;173(8):632-638.
        """)
    
    st.caption("⚠️ HOSPITAL Score chỉ là công cụ hỗ trợ. Quyết định xuất viện phải dựa trên đánh giá lâm sàng toàn diện.")

