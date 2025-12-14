"""
TRISS - Trauma and Injury Severity Score
=========================================

Predicts probability of survival after trauma

Reference:
- Boyd CR, et al. Evaluating trauma care: the TRISS method. 
  Trauma Score and the Injury Severity Score. J Trauma. 1987;27(4):370-378.

TRISS Components:
- RTS (Revised Trauma Score): Physiological parameters
- ISS (Injury Severity Score): Anatomical injury severity
- Age: Patient age
- Mechanism: Blunt vs penetrating trauma

Formula:
Ps = 1 / (1 + e^(-b))
where b = b0 + b1(RTS) + b2(ISS) + b3(Age) + b4(Mechanism)

Clinical Utility:
- Predict survival probability after trauma
- Quality improvement
- Research
- Resource allocation
"""

import streamlit as st
import math
from components.ui.results import render_result_box
from scores.utils.validation import (
    validate_gcs,
    validate_blood_pressure,
    validate_respiratory_rate,
    validate_age,
    validate_range
)


def calculate_rts_for_triss(gcs: int, sbp: float, rr: float) -> float:
    """
    Calculate RTS for TRISS (simplified version)
    
    Args:
        gcs: Glasgow Coma Scale (3-15)
        sbp: Systolic blood pressure (mmHg)
        rr: Respiratory rate (/min)
    
    Returns:
        RTS value (0-7.84)
    """
    # GCS coding
    if gcs >= 13:
        gcs_coded = 4
    elif gcs >= 9:
        gcs_coded = 3
    elif gcs >= 6:
        gcs_coded = 2
    elif gcs >= 4:
        gcs_coded = 1
    else:
        gcs_coded = 0
    
    # SBP coding
    if sbp > 89:
        sbp_coded = 4
    elif sbp > 75:
        sbp_coded = 3
    elif sbp > 49:
        sbp_coded = 2
    elif sbp > 0:
        sbp_coded = 1
    else:
        sbp_coded = 0
    
    # RR coding
    if rr > 29:
        rr_coded = 4
    elif rr > 9:
        rr_coded = 3
    elif rr > 5:
        rr_coded = 2
    elif rr > 0:
        rr_coded = 1
    else:
        rr_coded = 0
    
    # RTS = (0.9368 × GCS) + (0.7326 × SBP) + (0.2908 × RR)
    rts = (0.9368 * gcs_coded) + (0.7326 * sbp_coded) + (0.2908 * rr_coded)
    
    return rts


def calculate_triss(
    rts: float,
    iss: int,
    age: int,
    is_blunt: bool
) -> dict:
    """
    Calculate TRISS probability of survival
    
    Args:
        rts: Revised Trauma Score (0-7.84)
        iss: Injury Severity Score (0-75)
        age: Patient age (years)
        is_blunt: Blunt trauma (True) vs penetrating (False)
    
    Returns:
        Dictionary with survival probability and interpretation
    """
    # Age coding for TRISS
    if age < 55:
        age_coded = 0
    else:
        age_coded = 1
    
    # Mechanism coding
    mechanism_coded = 0 if is_blunt else 1
    
    # TRISS coefficients (from Boyd et al. 1987)
    if is_blunt:
        b0 = -1.2470
        b1 = 0.9544
        b2 = -0.0768
        b3 = -1.9052
        b4 = 0
    else:  # Penetrating
        b0 = -0.6029
        b1 = 1.1430
        b2 = -0.1516
        b3 = -2.6676
        b4 = 0
    
    # Calculate b
    b = b0 + (b1 * rts) + (b2 * iss) + (b3 * age_coded) + (b4 * mechanism_coded)
    
    # Calculate probability of survival
    ps = 1 / (1 + math.exp(-b))
    ps_percent = ps * 100
    
    # Interpretation
    if ps_percent >= 75:
        interpretation = "Tiên lượng sống tốt"
        color = "success"
        severity = "Tốt"
    elif ps_percent >= 50:
        interpretation = "Tiên lượng sống trung bình"
        color = "warning"
        severity = "Trung bình"
    else:
        interpretation = "Tiên lượng sống kém"
        color = "error"
        severity = "Kém"
    
    return {
        "rts": rts,
        "iss": iss,
        "age": age,
        "mechanism": "Blunt" if is_blunt else "Penetrating",
        "ps": ps,
        "ps_percent": ps_percent,
        "interpretation": interpretation,
        "color": color,
        "severity": severity
    }


def render():
    """TRISS Calculator"""
    st.subheader("🦴 TRISS - Trauma and Injury Severity Score")
    st.caption("Dự đoán khả năng sống sót sau chấn thương")
    
    st.markdown("""
    **TRISS (Trauma and Injury Severity Score)** dự đoán khả năng sống sót sau chấn thương.
    
    **Các thành phần:**
    - **RTS (Revised Trauma Score):** Thông số sinh lý (GCS, SBP, RR)
    - **ISS (Injury Severity Score):** Mức độ nặng tổn thương giải phẫu (0-75)
    - **Age:** Tuổi bệnh nhân
    - **Mechanism:** Chấn thương kín (blunt) hay xuyên thấu (penetrating)
    
    **Công thức:**
    - Ps = 1 / (1 + e^(-b))
    - b = b0 + b1(RTS) + b2(ISS) + b3(Age) + b4(Mechanism)
    
    **Tiên lượng:**
    - **≥75%:** Tốt
    - **50-74%:** Trung bình
    - **<50%:** Kém
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📝 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🧠 RTS - Revised Trauma Score")
        
        gcs = st.number_input(
            "GCS (3-15):",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            key="triss_gcs"
        )
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg):",
            min_value=0.0,
            max_value=300.0,
            value=120.0,
            step=1.0,
            key="triss_sbp"
        )
        
        rr = st.number_input(
            "Nhịp thở (/phút):",
            min_value=0.0,
            max_value=60.0,
            value=20.0,
            step=1.0,
            key="triss_rr"
        )
    
    with col2:
        st.markdown("#### 🦴 ISS - Injury Severity Score")
        
        iss = st.number_input(
            "ISS (0-75):",
            min_value=0,
            max_value=75,
            value=0,
            step=1,
            key="triss_iss",
            help="Tính từ AIS scores (xem ISS calculator để tính chi tiết)"
        )
        
        age = st.number_input(
            "Tuổi (năm):",
            min_value=0,
            max_value=120,
            value=40,
            step=1,
            key="triss_age"
        )
        
        is_blunt = st.radio(
            "Cơ chế chấn thương:",
            ["Chấn thương kín (Blunt)", "Chấn thương xuyên thấu (Penetrating)"],
            key="triss_mechanism"
        )
        is_blunt = is_blunt == "Chấn thương kín (Blunt)"
    
    st.info("💡 **Lưu ý:** Nếu chưa biết ISS, sử dụng ISS Calculator để tính từ AIS scores.")
    
    st.markdown("---")
    
    if st.button("🧮 Tính TRISS", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_gcs, gcs_error = validate_gcs(gcs)
        if not is_valid_gcs:
            validation_errors.append(gcs_error)
        
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(sbp_error)
        
        is_valid_rr, rr_error = validate_respiratory_rate(rr)
        if not is_valid_rr:
            validation_errors.append(rr_error)
        
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(age_error)
        
        is_valid_iss, iss_error = validate_range(iss, 0, 75, "ISS")
        if not is_valid_iss:
            validation_errors.append(iss_error)
        
        if validation_errors:
            st.error("**⚠️ Lỗi validation:**")
            for error in validation_errors:
                st.error(f"- {error}")
            st.stop()
        
        # Calculate RTS
        rts = calculate_rts_for_triss(gcs, sbp, rr)
        
        # Calculate TRISS
        result = calculate_triss(rts, iss, age, is_blunt)
        
        # Display results
        st.markdown("### 📊 Kết quả")
        
        render_result_box(
            "Khả năng sống sót",
            f"{result['ps_percent']:.1f}%",
            subtitle=result['interpretation'],
            color=result['color'],
            icon="🦴"
        )
        
        st.markdown("---")
        st.markdown("### 📋 Chi tiết")
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown(f"""
            **RTS (Revised Trauma Score):** {result['rts']:.2f}
            - GCS: {gcs}
            - SBP: {sbp:.0f} mmHg
            - RR: {rr:.0f} /min
            
            **ISS (Injury Severity Score):** {result['iss']}
            """)
        
        with col4:
            st.markdown(f"""
            **Tuổi:** {result['age']} tuổi
            - Age coded: {'≥55' if age >= 55 else '<55'}
            
            **Cơ chế:** {result['mechanism']}
            """)
        
        st.markdown("---")
        st.markdown("### 💡 Khuyến nghị")
        
        if result['severity'] == "Tốt":
            st.success("""
            **✅ Tiên lượng sống tốt (≥75%):**
            - Điều trị chuẩn
            - Theo dõi định kỳ
            - Tiên lượng tốt
            """)
        elif result['severity'] == "Trung bình":
            st.warning("""
            **⚠️ Tiên lượng sống trung bình (50-74%):**
            - Điều trị tích cực
            - Theo dõi sát
            - Hội chẩn chuyên khoa
            - Thảo luận với gia đình
            """)
        else:
            st.error("""
            **🚨 Tiên lượng sống kém (<50%):**
            - Điều trị rất tích cực
            - Theo dõi liên tục
            - Hội chẩn đa chuyên khoa
            - Thảo luận với gia đình về tiên lượng
            - Cân nhắc các biện pháp hỗ trợ
            """)
        
        st.markdown("---")
        st.info("""
        **💡 Lưu ý:**
        - TRISS chỉ là công cụ dự đoán, không phải quyết định điều trị
        - Kết hợp với đánh giá lâm sàng toàn diện
        - Đánh giá lại khi tình trạng thay đổi
        - TRISS chính xác hơn khi kết hợp RTS và ISS
        """)
    
    st.markdown("---")
    
    with st.expander("📖 Thông tin về TRISS"):
        st.markdown("""
        **TRISS (Trauma and Injury Severity Score)** kết hợp:
        
        1. **RTS (Revised Trauma Score):** Đánh giá sinh lý
           - GCS, SBP, RR
           - RTS = (0.9368 × GCS) + (0.7326 × SBP) + (0.2908 × RR)
        
        2. **ISS (Injury Severity Score):** Đánh giá giải phẫu
           - Tổn thương theo vùng cơ thể
           - ISS = A² + B² + C² (3 điểm AIS cao nhất từ 3 vùng khác nhau)
        
        3. **Age:** Tuổi bệnh nhân (≥55 = 1, <55 = 0)
        
        4. **Mechanism:** Cơ chế chấn thương (Blunt vs Penetrating)
        
        **Công thức:**
        - Ps = 1 / (1 + e^(-b))
        - b = b0 + b1(RTS) + b2(ISS) + b3(Age) + b4(Mechanism)
        
        **Tài liệu tham khảo:**
        - Boyd CR, et al. Evaluating trauma care: the TRISS method. 
          Trauma Score and the Injury Severity Score. J Trauma. 1987;27(4):370-378.
        """)
    
    st.caption("⚠️ TRISS chỉ là công cụ hỗ trợ. Quyết định điều trị phải dựa trên đánh giá lâm sàng toàn diện.")

