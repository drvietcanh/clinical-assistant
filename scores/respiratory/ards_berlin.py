"""
ARDS Berlin Definition
Diagnostic criteria for Acute Respiratory Distress Syndrome (ARDS)

Reference:
ARDS Definition Task Force. Acute respiratory distress syndrome: the Berlin Definition.
JAMA. 2012;307(23):2526-2533.
"""

import streamlit as st


def evaluate_ards_berlin(
    timing,
    chest_imaging,
    origin_of_edema,
    oxygenation_mild,
    oxygenation_moderate,
    oxygenation_severe,
    has_abg=False,
    pao2=None,
    fio2=None,
    pf_ratio=None
):
    """
    Evaluate ARDS Berlin Definition criteria
    
    Args:
        timing: Within 1 week of known clinical insult or new/worsening respiratory symptoms
        chest_imaging: Bilateral opacities on chest X-ray or CT
        origin_of_edema: Respiratory failure not fully explained by cardiac failure or fluid overload
        oxygenation_mild: PaO2/FiO2 200-300 mmHg with PEEP ≥5 cmH2O
        oxygenation_moderate: PaO2/FiO2 100-200 mmHg with PEEP ≥5 cmH2O
        oxygenation_severe: PaO2/FiO2 <100 mmHg with PEEP ≥5 cmH2O
        has_abg: Whether ABG is available
        pao2: PaO2 (mmHg)
        fio2: FiO2 (decimal or %)
        pf_ratio: PaO2/FiO2 ratio (mmHg) - if directly available
    
    Returns:
        dict with ARDS diagnosis, severity, and criteria evaluation
    """
    criteria_met = []
    criteria_failed = []
    
    # Criterion 1: Timing
    if timing:
        criteria_met.append("✅ Timing: Trong vòng 1 tuần sau tổn thương lâm sàng hoặc triệu chứng hô hấp mới/trầm trọng hơn")
    else:
        criteria_failed.append("❌ Timing: Không đáp ứng")
    
    # Criterion 2: Chest Imaging
    if chest_imaging:
        criteria_met.append("✅ Chest Imaging: Opacities hai bên trên X-quang hoặc CT ngực")
    else:
        criteria_failed.append("❌ Chest Imaging: Không có opacities hai bên")
    
    # Criterion 3: Origin of Edema
    if origin_of_edema:
        criteria_met.append("✅ Origin of Edema: Suy hô hấp không hoàn toàn do suy tim hoặc quá tải dịch")
    else:
        criteria_failed.append("❌ Origin of Edema: Có thể do suy tim hoặc quá tải dịch")
    
    # Criterion 4: Oxygenation
    severity = None
    oxygenation_met = False
    
    if has_abg and (pf_ratio is not None or (pao2 is not None and fio2 is not None)):
        # Calculate P/F ratio if not provided
        if pf_ratio is None:
            # Convert FiO2 to decimal if needed
            if fio2 > 1:
                fio2_decimal = fio2 / 100
            else:
                fio2_decimal = fio2
            pf_ratio = pao2 / fio2_decimal
        
        # Check severity
        if pf_ratio < 100:
            severity = "Severe ARDS"
            oxygenation_met = True
            criteria_met.append(f"✅ Oxygenation: PaO₂/FiO₂ = {pf_ratio:.0f} mmHg (<100) → **Severe ARDS**")
        elif pf_ratio < 200:
            severity = "Moderate ARDS"
            oxygenation_met = True
            criteria_met.append(f"✅ Oxygenation: PaO₂/FiO₂ = {pf_ratio:.0f} mmHg (100-199) → **Moderate ARDS**")
        elif pf_ratio < 300:
            severity = "Mild ARDS"
            oxygenation_met = True
            criteria_met.append(f"✅ Oxygenation: PaO₂/FiO₂ = {pf_ratio:.0f} mmHg (200-299) → **Mild ARDS**")
        else:
            criteria_failed.append(f"❌ Oxygenation: PaO₂/FiO₂ = {pf_ratio:.0f} mmHg (≥300) → Không đáp ứng tiêu chuẩn ARDS")
    else:
        # Use manual selection
        if oxygenation_severe:
            severity = "Severe ARDS"
            oxygenation_met = True
            criteria_met.append("✅ Oxygenation: PaO₂/FiO₂ <100 mmHg với PEEP ≥5 cmH2O → **Severe ARDS**")
        elif oxygenation_moderate:
            severity = "Moderate ARDS"
            oxygenation_met = True
            criteria_met.append("✅ Oxygenation: PaO₂/FiO₂ 100-200 mmHg với PEEP ≥5 cmH2O → **Moderate ARDS**")
        elif oxygenation_mild:
            severity = "Mild ARDS"
            oxygenation_met = True
            criteria_met.append("✅ Oxygenation: PaO₂/FiO₂ 200-300 mmHg với PEEP ≥5 cmH2O → **Mild ARDS**")
        else:
            criteria_failed.append("❌ Oxygenation: Không đáp ứng tiêu chuẩn")
    
    # Final diagnosis
    all_criteria_met = len(criteria_met) >= 4  # All 4 criteria must be met
    
    if all_criteria_met and oxygenation_met:
        diagnosis = f"ARDS - {severity}"
        color = "error" if severity == "Severe ARDS" else ("warning" if severity == "Moderate ARDS" else "info")
    else:
        diagnosis = "Không đáp ứng tiêu chuẩn ARDS"
        color = "success"
    
    return {
        "diagnosis": diagnosis,
        "severity": severity,
        "all_criteria_met": all_criteria_met,
        "criteria_met": criteria_met,
        "criteria_failed": criteria_failed,
        "color": color,
        "pf_ratio": pf_ratio if has_abg else None
    }


def render():
    """ARDS Berlin Definition Calculator"""
    st.subheader("🫁 ARDS Berlin Definition")
    st.caption("Tiêu chuẩn chẩn đoán ARDS - Berlin Definition 2012")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: ARDS Berlin Definition (2012)**
    
    **4 Tiêu chuẩn Bắt Buộc:**
    1. **Timing:** Trong vòng 1 tuần sau tổn thương lâm sàng hoặc triệu chứng hô hấp mới/trầm trọng hơn
    2. **Chest Imaging:** Opacities hai bên trên X-quang hoặc CT ngực
    3. **Origin of Edema:** Suy hô hấp không hoàn toàn do suy tim hoặc quá tải dịch
    4. **Oxygenation:** Phân loại theo PaO₂/FiO₂ với PEEP ≥5 cmH2O
    
    **Phân Loại:**
    - **Mild ARDS:** PaO₂/FiO₂ 200-300 mmHg
    - **Moderate ARDS:** PaO₂/FiO₂ 100-200 mmHg
    - **Severe ARDS:** PaO₂/FiO₂ <100 mmHg
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📋 Đánh giá Tiêu chuẩn")
    
    # Criterion 1: Timing
    st.markdown("#### 1️⃣ Timing")
    timing = st.checkbox(
        "Trong vòng 1 tuần sau tổn thương lâm sàng hoặc triệu chứng hô hấp mới/trầm trọng hơn",
        key="ards_timing",
        help="Ví dụ: viêm phổi, sepsis, chấn thương, hít sặc, v.v."
    )
    
    st.markdown("---")
    
    # Criterion 2: Chest Imaging
    st.markdown("#### 2️⃣ Chest Imaging")
    chest_imaging = st.checkbox(
        "Opacities hai bên trên X-quang hoặc CT ngực",
        key="ards_imaging",
        help="Không thể giải thích hoàn toàn bằng tràn dịch màng phổi, xẹp phổi, hoặc nốt"
    )
    
    st.markdown("---")
    
    # Criterion 3: Origin of Edema
    st.markdown("#### 3️⃣ Origin of Edema")
    origin_of_edema = st.checkbox(
        "Suy hô hấp không hoàn toàn do suy tim hoặc quá tải dịch",
        key="ards_origin",
        help="Nếu không có bằng chứng về suy tim cấp hoặc quá tải dịch, hoặc nếu có nhưng không giải thích được hoàn toàn"
    )
    
    st.markdown("---")
    
    # Criterion 4: Oxygenation
    st.markdown("#### 4️⃣ Oxygenation (PaO₂/FiO₂ với PEEP ≥5 cmH2O)")
    
    has_abg = st.checkbox(
        "Có ABG (PaO₂ và FiO₂)",
        key="ards_has_abg"
    )
    
    if has_abg:
        col1, col2 = st.columns(2)
        
        with col1:
            pao2 = st.number_input(
                "PaO₂ (mmHg):",
                min_value=30.0,
                max_value=600.0,
                value=100.0,
                step=1.0,
                key="ards_pao2"
            )
        
        with col2:
            fio2_input = st.number_input(
                "FiO₂ (%):",
                min_value=21.0,
                max_value=100.0,
                value=50.0,
                step=1.0,
                key="ards_fio2"
            )
            fio2_decimal = fio2_input / 100
        
        pf_ratio = pao2 / fio2_decimal
        
        st.info(f"**PaO₂/FiO₂ = {pf_ratio:.0f} mmHg**")
        
        # Auto-select based on P/F ratio
        if pf_ratio < 100:
            oxygenation_severe = True
            oxygenation_moderate = False
            oxygenation_mild = False
        elif pf_ratio < 200:
            oxygenation_severe = False
            oxygenation_moderate = True
            oxygenation_mild = False
        elif pf_ratio < 300:
            oxygenation_severe = False
            oxygenation_moderate = False
            oxygenation_mild = True
        else:
            oxygenation_severe = False
            oxygenation_moderate = False
            oxygenation_mild = False
    else:
        pao2 = None
        fio2 = None
        pf_ratio = None
        fio2_decimal = None
        
        st.markdown("**Chọn mức độ oxy hóa (với PEEP ≥5 cmH2O):**")
        
        oxygenation_severe = st.checkbox(
            "Severe ARDS: PaO₂/FiO₂ <100 mmHg",
            key="ards_severe"
        )
        
        oxygenation_moderate = st.checkbox(
            "Moderate ARDS: PaO₂/FiO₂ 100-200 mmHg",
            key="ards_moderate"
        )
        
        oxygenation_mild = st.checkbox(
            "Mild ARDS: PaO₂/FiO₂ 200-300 mmHg",
            key="ards_mild"
        )
    
    st.markdown("---")
    
    # Calculate
    result = evaluate_ards_berlin(
        timing,
        chest_imaging,
        origin_of_edema,
        oxygenation_mild,
        oxygenation_moderate,
        oxygenation_severe,
        has_abg,
        pao2,
        fio2_decimal if has_abg else None,
        pf_ratio
    )
    
    # Display results
    st.markdown("### 📊 Kết quả")
    
    if result["color"] == "error":
        st.error(f"## **{result['diagnosis']}**")
    elif result["color"] == "warning":
        st.warning(f"## **{result['diagnosis']}**")
    elif result["color"] == "info":
        st.info(f"## **{result['diagnosis']}**")
    else:
        st.success(f"## **{result['diagnosis']}**")
    
    st.markdown("---")
    
    # Criteria evaluation
    st.markdown("### ✅ Đánh giá Tiêu chuẩn")
    
    if result["criteria_met"]:
        st.markdown("**Tiêu chuẩn đáp ứng:**")
        for criterion in result["criteria_met"]:
            st.markdown(criterion)
    
    if result["criteria_failed"]:
        st.markdown("**Tiêu chuẩn không đáp ứng:**")
        for criterion in result["criteria_failed"]:
            st.markdown(criterion)
    
    st.markdown("---")
    
    # Clinical implications
    if result["all_criteria_met"] and result["severity"]:
        st.markdown("### 💊 Ý nghĩa lâm sàng")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if result["severity"] == "Severe ARDS":
                st.error("""
                **🚨 Severe ARDS:**
                
                **Điều Trị:**
                - Lung-protective ventilation (6 ml/kg IBW)
                - PEEP cao (12-24 cmH2O)
                - Prone positioning (16-18h/ngày)
                - Cân nhắc ECMO
                - Neuromuscular blockade nếu cần
                - Corticosteroids (nếu ARDS do COVID-19)
                
                **Tiên lượng:**
                - Tỷ lệ tử vong: ~45%
                - Thời gian thở máy: 10-14 ngày
                """)
            elif result["severity"] == "Moderate ARDS":
                st.warning("""
                **⚠️ Moderate ARDS:**
                
                **Điều Trị:**
                - Lung-protective ventilation (6 ml/kg IBW)
                - PEEP trung bình (8-12 cmH2O)
                - Cân nhắc prone positioning
                - Theo dõi sát
                
                **Tiên lượng:**
                - Tỷ lệ tử vong: ~32%
                - Thời gian thở máy: 7-10 ngày
                """)
            else:
                st.info("""
                **ℹ️ Mild ARDS:**
                
                **Điều Trị:**
                - Lung-protective ventilation (6 ml/kg IBW)
                - PEEP thấp-trung bình (5-10 cmH2O)
                - Theo dõi sát
                
                **Tiên lượng:**
                - Tỷ lệ tử vong: ~27%
                - Thời gian thở máy: 5-7 ngày
                """)
        
        with col2:
            st.markdown("""
            **📋 Checklist Điều Trị:**
            
            - ✅ Lung-protective ventilation
            - ✅ PEEP/FiO2 theo ARDSNet
            - ✅ Plateau pressure < 30 cmH2O
            - ✅ Target SpO2: 88-95%
            - ✅ Điều trị nguyên nhân
            - ✅ Hỗ trợ huyết động
            - ✅ Dự phòng VTE
            - ✅ Dự phòng stress ulcer
            """)
    
    st.markdown("---")
    
    # Additional information
    with st.expander("📚 Thông tin thêm"):
        st.markdown("""
        **ARDS Berlin Definition (2012) - Thay thế AECC Definition (1994):**
        
        **Cải tiến:**
        - Phân loại 3 mức độ (Mild, Moderate, Severe)
        - Loại bỏ ALI (Acute Lung Injury)
        - Yêu cầu PEEP ≥5 cmH2O cho tiêu chuẩn oxy hóa
        - Làm rõ timing và origin of edema
        
        **So sánh với AECC (1994):**
        - AECC: ALI (P/F 200-300) và ARDS (P/F <200)
        - Berlin: Mild (200-300), Moderate (100-200), Severe (<100)
        
        **Lưu ý:**
        - Tất cả 4 tiêu chuẩn phải đáp ứng
        - PEEP ≥5 cmH2O là bắt buộc
        - Cần loại trừ suy tim hoặc quá tải dịch
        """)
    
    st.markdown("---")
    
    # References
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ARDS Definition Task Force.** Acute respiratory distress syndrome: the Berlin Definition.
       JAMA. 2012;307(23):2526-2533.
    
    2. **UpToDate:** Acute Respiratory Distress Syndrome - Clinical features and diagnosis
       - Last updated 2024
       - Berlin Definition criteria
    
    3. **ARDSNet Protocol (2000):** Lung-protective ventilation strategy
       - Tidal volume: 6 ml/kg IBW
       - Plateau pressure: < 30 cmH2O
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ ARDS Berlin Definition chỉ mang tính tham khảo. Chẩn đoán và điều trị phải dựa trên đánh giá toàn diện bởi bác sĩ có kinh nghiệm. Tất cả 4 tiêu chuẩn phải đáp ứng để chẩn đoán ARDS.")

