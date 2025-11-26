"""
ABCD2 Score - TIA Risk Stratification
Assessment of stroke risk after transient ischemic attack (TIA)

Reference:
Johnston SC, et al. Validation and refinement of scores to predict very early stroke risk after transient ischaemic attack.
Lancet. 2007;369(9558):283-292.
"""

import streamlit as st


def calculate_abcd2(age, bp, clinical_features, duration, diabetes):
    """
    Calculate ABCD2 Score
    
    Args:
        age: Age in years
        bp: Systolic BP (mmHg)
        clinical_features: "Unilateral weakness", "Speech disturbance", or "Both"
        duration: Duration in minutes
        diabetes: True if diabetes present
    
    Returns:
        dict with total score, risk category, and stroke risk
    """
    score = 0
    
    # Age
    if age >= 60:
        score += 1
    
    # Blood pressure
    # Note: bp parameter should be systolic BP
    # ABCD2 uses: Systolic BP ≥140 mmHg OR Diastolic BP ≥90 mmHg
    # Since we only have one BP value, we check if it's systolic ≥140
    # In the UI, we check both systolic and diastolic separately
    if bp >= 140:  # Systolic ≥140 mmHg
        score += 1
    
    # Clinical features
    if clinical_features == "Unilateral weakness":
        score += 2
    elif clinical_features == "Speech disturbance":
        score += 1
    
    # Duration
    if duration >= 60:
        score += 2
    elif duration >= 10:
        score += 1
    
    # Diabetes
    if diabetes:
        score += 1
    
    # Risk category and stroke risk
    if score >= 6:
        risk_category = "High Risk"
        stroke_risk_2d = "8.1%"
        stroke_risk_7d = "11.7%"
        color = "error"
    elif score >= 4:
        risk_category = "Moderate Risk"
        stroke_risk_2d = "4.1%"
        stroke_risk_7d = "5.9%"
        color = "warning"
    else:
        risk_category = "Low Risk"
        stroke_risk_2d = "1.0%"
        stroke_risk_7d = "1.2%"
        color = "success"
    
    return {
        "total_score": score,
        "risk_category": risk_category,
        "stroke_risk_2d": stroke_risk_2d,
        "stroke_risk_7d": stroke_risk_7d,
        "color": color
    }


def render():
    """ABCD2 Score Calculator"""
    st.subheader("🧠 ABCD2 Score")
    st.caption("TIA Risk Stratification - Stroke Risk After Transient Ischemic Attack")
    
    st.warning("""
    **⚠️ QUAN TRỌNG: TIA là dấu hiệu cảnh báo đột quỵ**
    
    **ABCD2 Score** đánh giá nguy cơ đột quỵ sau TIA:
    - Nguy cơ đột quỵ cao nhất trong 48 giờ đầu
    - Giúp quyết định nhập viện vs điều trị ngoại trú
    - Hướng dẫn workup và điều trị
    """)
    
    st.markdown("---")
    
    # Input section
    st.markdown("### 📋 Thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=0,
            max_value=120,
            value=65,
            step=1,
            key="abcd2_age"
        )
        
        systolic_bp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=80,
            max_value=250,
            value=150,
            step=5,
            key="abcd2_sbp"
        )
        
        diastolic_bp = st.number_input(
            "Huyết áp tâm trương (mmHg)",
            min_value=50,
            max_value=150,
            value=90,
            step=5,
            key="abcd2_dbp"
        )
    
    with col2:
        clinical_features = st.radio(
            "Triệu chứng lâm sàng:",
            [
                "Không có triệu chứng trên",
                "Speech disturbance (Rối loạn ngôn ngữ)",
                "Unilateral weakness (Yếu một bên)",
                "Both (Cả hai)"
            ],
            key="abcd2_clinical"
        )
        
        duration = st.number_input(
            "Thời gian triệu chứng (phút)",
            min_value=0,
            max_value=1440,
            value=30,
            step=5,
            key="abcd2_duration"
        )
        
        diabetes = st.checkbox(
            "Có đái tháo đường",
            key="abcd2_diabetes"
        )
    
    st.markdown("---")
    
    # Calculate
    # ABCD2 BP criterion: Systolic ≥140 OR Diastolic ≥90
    bp_meets_criterion = (systolic_bp >= 140) or (diastolic_bp >= 90)
    # For calculation function, pass systolic BP (it will check >= 140)
    # But we need to adjust the score if only diastolic meets criterion
    bp_for_calc = systolic_bp if systolic_bp > 0 else diastolic_bp
    
    # Map clinical features
    if "Both" in clinical_features or ("Unilateral" in clinical_features and "Speech" in clinical_features):
        clinical_value = "Both"
    elif "Unilateral" in clinical_features:
        clinical_value = "Unilateral weakness"
    elif "Speech" in clinical_features:
        clinical_value = "Speech disturbance"
    else:
        clinical_value = "None"
    
    result = calculate_abcd2(age, bp_for_calc, clinical_value, duration, diabetes)
    
    # Adjust score if only diastolic BP meets criterion
    if bp_meets_criterion and systolic_bp < 140:
        result["total_score"] += 1
        # Recalculate risk category
        if result["total_score"] >= 6:
            result["risk_category"] = "High Risk"
            result["stroke_risk_2d"] = "8.1%"
            result["stroke_risk_7d"] = "11.7%"
            result["color"] = "error"
        elif result["total_score"] >= 4:
            result["risk_category"] = "Moderate Risk"
            result["stroke_risk_2d"] = "4.1%"
            result["stroke_risk_7d"] = "5.9%"
            result["color"] = "warning"
    
    # Display results
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📊 Kết quả")
        
        if result["color"] == "success":
            st.success(f"## **ABCD2 Score: {result['total_score']}/7**")
        elif result["color"] == "warning":
            st.warning(f"## **ABCD2 Score: {result['total_score']}/7**")
        else:
            st.error(f"## **ABCD2 Score: {result['total_score']}/7**")
        
        st.markdown(f"**Phân loại nguy cơ:** {result['risk_category']}")
        st.markdown(f"**Nguy cơ đột quỵ 2 ngày:** {result['stroke_risk_2d']}")
        st.markdown(f"**Nguy cơ đột quỵ 7 ngày:** {result['stroke_risk_7d']}")
        
        # Score breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết điểm số")
        
        breakdown = []
        if age >= 60:
            breakdown.append(f"✅ Tuổi ≥60: +1 điểm")
        if systolic_bp >= 140 or diastolic_bp >= 90:
            breakdown.append(f"✅ Huyết áp ≥140/90: +1 điểm")
        if clinical_value == "Unilateral weakness":
            breakdown.append(f"✅ Yếu một bên: +2 điểm")
        elif clinical_value == "Speech disturbance":
            breakdown.append(f"✅ Rối loạn ngôn ngữ: +1 điểm")
        if duration >= 60:
            breakdown.append(f"✅ Thời gian ≥60 phút: +2 điểm")
        elif duration >= 10:
            breakdown.append(f"✅ Thời gian ≥10 phút: +1 điểm")
        if diabetes:
            breakdown.append(f"✅ Đái tháo đường: +1 điểm")
        
        for item in breakdown:
            st.markdown(item)
    
    with col2:
        st.markdown("### 🎯 Khuyến nghị")
        
        if result["total_score"] >= 6:
            st.error("""
            **🚨 HIGH RISK:**
            
            **Cần nhập viện:**
            - Workup ngay (CT/MRI, carotid imaging, ECG, echo)
            - Bắt đầu antiplatelet ngay
            - Theo dõi sát 24-48h
            - Cân nhắc dual antiplatelet (aspirin + clopidogrel)
            """)
        elif result["total_score"] >= 4:
            st.warning("""
            **⚠️ MODERATE RISK:**
            
            **Cân nhắc nhập viện:**
            - Workup trong 24-48h
            - Bắt đầu antiplatelet
            - Theo dõi sát
            - Tái khám sớm
            """)
        else:
            st.success("""
            **✅ LOW RISK:**
            
            **Có thể điều trị ngoại trú:**
            - Workup trong 48-72h
            - Bắt đầu antiplatelet
            - Tái khám trong 1 tuần
            - Giáo dục dấu hiệu đột quỵ
            """)
    
    st.markdown("---")
    
    # Workup recommendations
    st.markdown("### 🔍 Workup Khuyến nghị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Immediate (nếu nhập viện):**
        - CT đầu (hoặc MRI nếu có)
        - ECG
        - CBC, BMP, Coagulation
        - Carotid imaging (US, CTA, MRA)
        - Echocardiogram (nếu nghi ngờ cardioembolic)
        
        **Within 24-48h:**
        - MRI brain (nếu chưa có)
        - Holter monitor (nếu nghi ngờ AF)
        - Lipid panel
        """)
    
    with col2:
        st.markdown("""
        **Treatment:**
        - **Antiplatelet:** Aspirin 75-325mg/ngày
        - **Hoặc:** Clopidogrel 75mg/ngày
        - **Nếu AF:** Anticoagulation (warfarin, DOAC)
        - **Risk factors:** Điều trị HTN, DM, lipid
        
        **Follow-up:**
        - Tái khám trong 1 tuần
        - Neurologist consult
        - Stroke prevention clinic
        """)
    
    st.markdown("---")
    
    # Score interpretation
    st.markdown("### 📊 Bảng phân loại nguy cơ")
    
    import pandas as pd
    
    risk_table = pd.DataFrame({
        "Điểm": [0, 1, 2, 3, 4, 5, 6, 7],
        "Nguy cơ 2 ngày": ["0.0%", "0.0%", "0.0%", "1.0%", "4.1%", "4.1%", "8.1%", "8.1%"],
        "Nguy cơ 7 ngày": ["0.0%", "0.0%", "0.0%", "1.2%", "5.9%", "5.9%", "11.7%", "11.7%"],
        "Phân loại": [
            "Low", "Low", "Low", "Low", 
            "Moderate", "Moderate", "High", "High"
        ]
    })
    
    st.dataframe(risk_table, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Special considerations
    st.markdown("### ⚠️ Các trường hợp đặc biệt")
    
    st.warning("""
    **ABCD3-I Score (Extended):**
    - Thêm: TIA trong 7 ngày trước (+2 điểm)
    - Thêm: Imaging (DWI positive) (+2 điểm)
    - Tổng: 0-9 điểm
    - Chính xác hơn ABCD2
    
    **Cần workup ngay nếu:**
    - ABCD2 ≥4
    - TIA lặp lại
    - Nghi ngờ cardioembolic
    - Carotid stenosis nặng
    
    **⚠️ Lưu ý:**
    - ABCD2 chỉ là công cụ hỗ trợ
    - Quyết định điều trị phải toàn diện
    - Cân nhắc các yếu tố khác (imaging, risk factors)
    """)
    
    st.markdown("---")
    
    # References
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **Johnston SC, et al.** Validation and refinement of scores to predict very early stroke risk after transient ischaemic attack.
       Lancet. 2007;369(9558):283-292.
    
    2. **Merwick A, et al.** Addition of brain and carotid imaging to the ABCD2 score to identify patients at early risk of stroke after transient ischaemic attack: a multicentre observational study.
       Lancet Neurol. 2010;9(11):1060-1069.
    
    3. **UpToDate:** Transient Ischemic Attack - Last updated 2024
       - Risk stratification
       - Treatment protocols
    
    4. **AHA/ASA Guidelines** - TIA Management (2021)
       - ABCD2 score
       - Workup recommendations
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ ABCD2 Score chỉ mang tính tham khảo. Quyết định điều trị phải dựa trên đánh giá toàn diện bởi bác sĩ có kinh nghiệm. TIA là dấu hiệu cảnh báo đột quỵ, cần điều trị tích cực.")

