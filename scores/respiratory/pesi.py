"""
PESI - Pulmonary Embolism Severity Index
Thang điểm đánh giá mức độ nặng và tiên lượng thuyên tắc phổi
"""

import streamlit as st


def render():
    """PESI Score Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🫁 PESI - Pulmonary Embolism Severity Index</h2>
    <p style='text-align: center;'><em>Thang điểm đánh giá mức độ nặng và tiên lượng thuyên tắc phổi</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **PESI (Pulmonary Embolism Severity Index)** đánh giá mức độ nặng và tiên lượng 30 ngày của bệnh nhân thuyên tắc phổi.
        
        **Chỉ Định:**
        - Bệnh nhân đã được chẩn đoán thuyên tắc phổi (PE)
        - Quyết định điều trị ngoại trú hay nội trú
        - Đánh giá tiên lượng
        
        **11 Tiêu chí (tổng điểm 0-400+):**
        
        **Phân loại nguy cơ:**
        - **Class I (≤ 65 điểm):** Nguy cơ thấp - Tỷ lệ tử vong 30 ngày: 0-1.6%
        - **Class II (66-85 điểm):** Nguy cơ thấp - Tỷ lệ tử vong 30 ngày: 1.7-3.5%
        - **Class III (86-105 điểm):** Nguy cơ trung bình - Tỷ lệ tử vong 30 ngày: 3.2-7.1%
        - **Class IV (106-125 điểm):** Nguy cơ cao - Tỷ lệ tử vong 30 ngày: 4.0-11.4%
        - **Class V (> 125 điểm):** Nguy cơ rất cao - Tỷ lệ tử vong 30 ngày: 10.0-24.5%
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh Giá")
    
    # Age
    st.markdown("### 1️⃣ Tuổi")
    age = st.number_input(
        "Tuổi (năm):",
        min_value=0,
        max_value=120,
        value=60,
        step=1,
        key="pesi_age"
    )
    age_score = age  # 1 điểm cho mỗi năm tuổi
    
    # Gender
    st.markdown("### 2️⃣ Giới Tính")
    gender = st.radio(
        "Giới tính:",
        ["Nam", "Nữ"],
        key="pesi_gender"
    )
    gender_score = 10 if gender == "Nam" else 0
    
    # Cancer
    st.markdown("### 3️⃣ Ung thư")
    cancer = st.checkbox(
        "Có ung thư (đang điều trị hoặc đã điều trị trong 6 tháng qua)",
        key="pesi_cancer"
    )
    cancer_score = 30 if cancer else 0
    
    # Heart failure
    st.markdown("### 4️⃣ Suy Tim")
    heart_failure = st.checkbox(
        "Có suy tim mạn tính",
        key="pesi_heart_failure"
    )
    heart_failure_score = 10 if heart_failure else 0
    
    # Chronic lung disease
    st.markdown("### 5️⃣ Bệnh Phổi Mạn")
    lung_disease = st.checkbox(
        "Có bệnh phổi mạn tính (COPD, hen phế quản...)",
        key="pesi_lung"
    )
    lung_score = 10 if lung_disease else 0
    
    # Pulse
    st.markdown("### 6️⃣ Mạch")
    pulse = st.number_input(
        "Mạch (lần/phút):",
        min_value=0,
        max_value=250,
        value=80,
        step=1,
        key="pesi_pulse"
    )
    if pulse >= 110:
        pulse_score = 20
    else:
        pulse_score = 0
    
    # Systolic BP
    st.markdown("### 7️⃣ Huyết Áp Tâm Thu")
    sbp = st.number_input(
        "Huyết áp tâm thu (mmHg):",
        min_value=0,
        max_value=300,
        value=120,
        step=1,
        key="pesi_sbp"
    )
    if sbp < 100:
        sbp_score = 30
    else:
        sbp_score = 0
    
    # Respiratory rate
    st.markdown("### 8️⃣ Tần Số Thở")
    rr = st.number_input(
        "Tần số thở (lần/phút):",
        min_value=0,
        max_value=60,
        value=20,
        step=1,
        key="pesi_rr"
    )
    if rr >= 30:
        rr_score = 20
    else:
        rr_score = 0
    
    # Temperature
    st.markdown("### 9️⃣ Nhiệt Độ")
    temp_unit = st.radio(
        "Đơn vị nhiệt độ:",
        ["°C", "°F"],
        horizontal=True,
        key="pesi_temp_unit"
    )
    
    if temp_unit == "°C":
        temp_c = st.number_input(
            "Nhiệt độ (°C):",
            min_value=30.0,
            max_value=45.0,
            value=37.0,
            step=0.1,
            format="%.1f",
            key="pesi_temp_c"
        )
        temp_f = temp_c * 9/5 + 32
    else:
        temp_f = st.number_input(
            "Nhiệt độ (°F):",
            min_value=86.0,
            max_value=113.0,
            value=98.6,
            step=0.1,
            format="%.1f",
            key="pesi_temp_f"
        )
        temp_c = (temp_f - 32) * 5/9
    
    if temp_c < 36:
        temp_score = 20
    else:
        temp_score = 0
    
    # Mental status
    st.markdown("### 🔟 Tình Trạng Tâm Thần")
    mental_status = st.radio(
        "Tình trạng tâm thần:",
        [
            "Tỉnh táo, định hướng tốt",
            "Lú lẫn, mê sảng, hôn mê"
        ],
        key="pesi_mental"
    )
    mental_score = 60 if "Lú lẫn" in mental_status or "mê sảng" in mental_status or "hôn mê" in mental_status else 0
    
    # Oxygen saturation
    st.markdown("### 1️⃣1️⃣ Độ Bão Hòa Oxy")
    spo2 = st.number_input(
        "SpO₂ (%):",
        min_value=0,
        max_value=100,
        value=98,
        step=1,
        key="pesi_spo2"
    )
    if spo2 < 90:
        spo2_score = 20
    else:
        spo2_score = 0
    
    st.markdown("---")
    
    if st.button("📊 Tính điểm PESI", type="primary", use_container_width=True):
        total_score = (age_score + gender_score + cancer_score + heart_failure_score + 
                      lung_score + pulse_score + sbp_score + rr_score + temp_score + 
                      mental_score + spo2_score)
        
        st.markdown("## 📊 Kết quả")
        
        # Determine risk class
        if total_score <= 65:
            risk_class = "I"
            risk_level = "Nguy cơ thấp"
            mortality = "0-1.6%"
            color = "#10b981"
            icon = "✅"
            treatment = "Có thể điều trị ngoại trú"
        elif total_score <= 85:
            risk_class = "II"
            risk_level = "Nguy cơ thấp"
            mortality = "1.7-3.5%"
            color = "#3b82f6"
            icon = "💡"
            treatment = "Cân nhắc điều trị ngoại trú (theo dõi sát)"
        elif total_score <= 105:
            risk_class = "III"
            risk_level = "Nguy cơ trung bình"
            mortality = "3.2-7.1%"
            color = "#f59e0b"
            icon = "⚠️"
            treatment = "Nên điều trị nội trú"
        elif total_score <= 125:
            risk_class = "IV"
            risk_level = "Nguy cơ cao"
            mortality = "4.0-11.4%"
            color = "#ef4444"
            icon = "🚨"
            treatment = "Cần điều trị nội trú, theo dõi sát"
        else:
            risk_class = "V"
            risk_level = "Nguy cơ rất cao"
            mortality = "10.0-24.5%"
            color = "#dc2626"
            icon = "🚨"
            treatment = "Cần điều trị nội trú, có thể cần ICU"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} PESI Class {risk_class} = {total_score} điểm
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {risk_level}
            </p>
            <p style='text-align: center; font-size: 1em; margin-top: 10px; color: #6b7280;'>
                Tỷ lệ tử vong 30 ngày: {mortality}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Khuyến nghị điều trị:** {treatment}")
        
        # Breakdown
        st.markdown("### 📋 Chi tiết điểm số:")
        st.markdown(f"""
        - **Tuổi:** {age_score} điểm (1 điểm/năm)
        - **Giới tính (Nam):** {gender_score} điểm
        - **Ung thư:** {cancer_score} điểm
        - **Suy tim:** {heart_failure_score} điểm
        - **Bệnh phổi mạn:** {lung_score} điểm
        - **Mạch ≥ 110:** {pulse_score} điểm
        - **HATT < 100:** {sbp_score} điểm
        - **Tần số thở ≥ 30:** {rr_score} điểm
        - **Nhiệt độ < 36°C:** {temp_score} điểm
        - **Lú lẫn/mê sảng/hôn mê:** {mental_score} điểm
        - **SpO₂ < 90%:** {spo2_score} điểm
        
        **Tổng:** {total_score} điểm
        """)
        
        # Treatment recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến nghị điều trị")
        
        if total_score <= 85:
            st.info(f"""
            **✅ PESI Class {risk_class} - Nguy cơ thấp (≤ 85 điểm)**
            
            **Điều Trị:**
            - **Có thể điều trị ngoại trú** (Class I-II)
            - Kháng đông: DOAC (rivaroxaban, apixaban, edoxaban) hoặc warfarin
            - Theo dõi sát tại nhà
            - Tái khám sau 1 tuần
            
            **Tiêu chuẩn điều trị ngoại trú:**
            - PESI Class I-II
            - Không có chống chỉ định kháng đông
            - Có khả năng tuân thủ điều trị
            - Có người chăm sóc
            - Có thể đến bệnh viện nhanh chóng nếu cần
            """)
        elif total_score <= 105:
            st.warning(f"""
            **⚠️ PESI Class {risk_class} - Nguy cơ trung bình (86-105 điểm)**
            
            **Điều Trị:**
            - **Nên điều trị nội trú**
            - Kháng đông: DOAC hoặc warfarin
            - Theo dõi sát dấu hiệu sinh tồn
            - Đánh giá lại sau 24-48 giờ
            
            **Cân nhắc điều trị ngoại trú nếu:**
            - Tình trạng ổn định sau 24 giờ
            - Không có biến chứng
            - Có khả năng tuân thủ điều trị
            """)
        else:
            st.error(f"""
            **🚨 PESI Class {risk_class} - Nguy cơ cao (≥ 106 điểm)**
            
            **Điều Trị:**
            - **Cần điều trị nội trú, theo dõi sát**
            - Kháng đông: DOAC hoặc warfarin
            - Cân nhắc điều trị tan huyết khối nếu:
              - Huyết động không ổn định
              - Suy hô hấp nặng
              - Không có chống chỉ định
            
            **Theo Dõi:**
            - Dấu hiệu sinh tồn mỗi 4-6 giờ
            - SpO₂ liên tục
            - Đánh giá lại sau 24 giờ
            - Cân nhắc chuyển ICU nếu xấu đi
            
            **Cảnh báo:**
            - Tỷ lệ tử vong 30 ngày: {mortality}
            - Cần theo dõi sát, can thiệp kịp thời
            """)
        
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            1. **Đánh giá khi chẩn đoán PE:**
               - Tính điểm PESI ngay khi chẩn đoán
               - Quyết định điều trị ngoại trú hay nội trú
            
            2. **Theo Dõi:**
               - Đánh giá lại PESI khi có thay đổi tình trạng
               - Đánh giá lại sau 24-48 giờ điều trị
            
            3. **Kết hợp với xét nghiệm:**
               - PESI + Troponin, BNP để đánh giá nguy cơ
               - PESI + siêu âm tim để đánh giá suy tim phải
            
            ### 📋 So sánh PESI vs Wells PE:
            - **Wells PE:** Đánh giá xác suất trước test (có PE hay không)
            - **PESI:** Đánh giá mức độ nặng và tiên lượng (sau khi đã chẩn đoán PE)
            
            ### ⚠️ Lưu ý:
            - PESI dùng cho bệnh nhân đã được chẩn đoán PE
            - Không dùng để chẩn đoán PE
            - Cân nhắc các yếu tố khác (troponin, BNP, siêu âm tim) khi quyết định điều trị
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Aujesky D, Obrosky DS, Stone RA, et al.** Derivation and validation of a prognostic model for pulmonary embolism. 
               *Am J Respir Crit Care Med.* 2005;172(8):1041-1046.
            
            2. **Jiménez D, Aujesky D, Moores L, et al.** Simplification of the pulmonary embolism severity index for prognostication in patients with acute symptomatic pulmonary embolism. 
               *Arch Intern Med.* 2010;170(15):1383-1389.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **PESI Class I-II (≤ 85):** Nguy cơ thấp → Có thể điều trị ngoại trú
    2. **PESI Class III (86-105):** Nguy cơ trung bình → Nên điều trị nội trú
    3. **PESI Class IV-V (≥ 106):** Nguy cơ cao → Cần điều trị nội trú, theo dõi sát
    4. **Mục Tiêu:** Quyết định điều trị ngoại trú hay nội trú, đánh giá tiên lượng
    5. **Lưu ý:** PESI dùng sau khi đã chẩn đoán PE, không dùng để chẩn đoán
    """)

