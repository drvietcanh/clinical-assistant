"""
PSI/PORT Score (Pneumonia Severity Index)
Đánh giá mức độ nặng viêm phổi cộng đồng
"""

import streamlit as st


def render():
    """PSI/PORT Score Calculator"""
    st.subheader("🫁 PSI/PORT Score")
    st.caption("Pneumonia Severity Index - Chỉ Số Mức Độ Nặng Viêm Phổi")
    
    st.info("""
    **PSI/PORT Score** đánh giá nguy cơ tử vong 30 ngày ở bệnh nhân viêm phổi cộng đồng.
    
    - Phức tạp hơn CURB-65 nhưng chính xác hơn
    - Dựa trên 20 biến số lâm sàng, xét nghiệm, X-quang
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin bệnh nhân")
        
        # Demographics
        age = st.number_input(
            "Tuổi",
            min_value=0,
            max_value=120,
            value=50,
            format="%d",
            step=1,
            help="Tuổi tính bằng năm"
        )
        
        gender = st.radio(
            "Giới tính:",
            ["Nam", "Nữ"],
            horizontal=True
        )
        
        nursing_home = st.checkbox(
            "Cư trú tại nhà dưỡng lão",
            help="+10 điểm"
        )
        
        st.markdown("---")
        st.markdown("### 🏥 Bệnh Lý Nền")
        
        neoplastic = st.checkbox(
            "Bệnh ung thư",
            help="Ung thư hoạt động hoặc chẩn đoán trong năm qua (+30 điểm)"
        )
        
        liver = st.checkbox(
            "Bệnh gan",
            help="Xơ gan hoặc bệnh gan mạn tính (+20 điểm)"
        )
        
        chf = st.checkbox(
            "Suy tim sung huyết",
            help="Tiền sử suy tim (+10 điểm)"
        )
        
        cvd = st.checkbox(
            "Bệnh mạch máu não",
            help="Tiền sử đột quỵ, TIA (+10 điểm)"
        )
        
        renal = st.checkbox(
            "Bệnh thận",
            help="Tiền sử bệnh thận mạn (+10 điểm)"
        )
        
        st.markdown("---")
        st.markdown("### 🌡️ Triệu chứng Lâm sàng")
        
        altered_mental = st.checkbox(
            "Rối loạn ý thức",
            help="Lú lẫn, lơ mơ, định hướng kém (+20 điểm)"
        )
        
        resp_rate = st.number_input(
            "Nhịp thở (lần/phút)",
            min_value=0,
            max_value=60,
            value=18,
            step=1,
            help="≥30/phút: +20 điểm"
        )
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=5,
            help="<90 mmHg: +20 điểm"
        )
        
        temp_c = st.number_input(
            "Nhiệt độ (°C)",
            min_value=35.0,
            max_value=42.0,
            value=37.0,
            step=0.1,
            help="<35°C hoặc ≥40°C: +15 điểm"
        )
        
        pulse = st.number_input(
            "Mạch (lần/phút)",
            min_value=0,
            max_value=200,
            value=80,
            step=5,
            help="≥125/phút: +10 điểm"
        )
        
        st.markdown("---")
        st.markdown("### 🔬 Xét nghiệm")
        
        # pH with unit conversion (arterial pH)
        ph = st.number_input(
            "pH máu động mạch",
            min_value=6.8,
            max_value=7.8,
            value=7.4,
            step=0.01,
            format="%.2f",
            help="<7.35: +30 điểm"
        )
        
        # BUN with unit conversion
        st.markdown("#### Urea (BUN)")
        bun_unit = st.radio(
            "Đơn vị:",
            ["mmol/L (SI - Mặc định)", "mg/dL"],
            horizontal=True,
            index=0,
            key="bun_unit_psi"
        )
        
        if "mmol/L" in bun_unit:
            bun_input = st.number_input(
                "Urea (mmol/L)",
                min_value=0.0,
                max_value=70.0,
                value=5.0,
                step=0.5,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L",
                key="bun_mmol"
            )
            bun_mgdl = bun_input * 2.8  # Convert to mg/dL for scoring
            st.caption(f"≈ {bun_mgdl:.1f} mg/dL")
        else:
            bun_mgdl = st.number_input(
                "BUN (mg/dL)",
                min_value=0.0,
                max_value=200.0,
                value=15.0,
                step=1.0,
                format="%.0f",
                help="Bình thường: 7-20 mg/dL",
                key="bun_mgdl"
            )
            st.caption(f"≈ {bun_mgdl/2.8:.1f} mmol/L")
        
        # Sodium
        sodium = st.number_input(
            "Natri (Na) - mEq/L = mmol/L",
            min_value=100.0,
            max_value=180.0,
            value=140.0,
            step=1.0,
            format="%.0f",
            help="<130 mEq/L: +20 điểm"
        )
        
        # Glucose with unit conversion
        st.markdown("#### Glucose")
        glucose_unit = st.radio(
            "Đơn vị:",
            ["mmol/L (SI - Mặc định)", "mg/dL"],
            horizontal=True,
            index=0,
            key="glucose_unit_psi"
        )
        
        if "mmol/L" in glucose_unit:
            glucose_input = st.number_input(
                "Glucose (mmol/L)",
                min_value=0.0,
                max_value=33.0,
                value=5.5,
                step=0.1,
                format="%.1f",
                help="Bình thường: 3.9-5.6 mmol/L",
                key="glucose_mmol"
            )
            glucose_mgdl = glucose_input * 18.0
            st.caption(f"≈ {glucose_mgdl:.0f} mg/dL")
        else:
            glucose_mgdl = st.number_input(
                "Glucose (mg/dL)",
                min_value=0.0,
                max_value=600.0,
                value=100.0,
                format="%.0f",
                step=5.0,
                help="Bình thường: 70-100 mg/dL",
                key="glucose_mgdl"
            )
            st.caption(f"≈ {glucose_mgdl/18.0:.1f} mmol/L")
        
        # Hematocrit
        hct = st.number_input(
            "Hematocrit (%)",
            min_value=0.0,
            max_value=70.0,
            value=42.0,
            step=0.5,
            help="<30%: +10 điểm"
        )
        
        # PaO2 with unit conversion
        st.markdown("#### PaO2 (Oxy máu động mạch)")
        pao2_unit = st.radio(
            "Đơn vị:",
            ["mmHg", "kPa"],
            horizontal=True,
            key="pao2_unit"
        )
        
        if pao2_unit == "mmHg":
            pao2_input = st.number_input(
                "PaO2 (mmHg)",
                min_value=0.0,
                max_value=150.0,
                value=90.0,
                step=1.0,
                help="Bình thường: 80-100 mmHg",
                key="pao2_mmhg"
            )
            pao2_mmhg = pao2_input
            st.caption(f"≈ {pao2_mmhg/7.5:.1f} kPa")
        else:
            pao2_input = st.number_input(
                "PaO2 (kPa)",
                min_value=0.0,
                max_value=20.0,
                value=12.0,
                step=0.1,
                help="Bình thường: 10.7-13.3 kPa",
                key="pao2_kpa"
            )
            pao2_mmhg = pao2_input * 7.5
            st.caption(f"≈ {pao2_mmhg:.0f} mmHg")
        
        # Pleural effusion
        pleural_effusion = st.checkbox(
            "Tràn dịch màng phổi (trên X-quang)",
            help="+10 điểm"
        )
        
        st.markdown("---")
        
        if st.button("🧮 Tính PSI/PORT Score", type="primary", use_container_width=True):
            # Calculate score
            score = 0
            details = []
            
            # Age
            if gender == "Nam":
                age_points = age
                details.append(f"Tuổi (Nam): {age} điểm")
            else:
                age_points = age - 10
                details.append(f"Tuổi (Nữ): {age} - 10 = {age_points} điểm")
            score += age_points
            
            # Nursing home
            if nursing_home:
                score += 10
                details.append("Nhà dưỡng lão: +10")
            
            # Comorbidities
            if neoplastic:
                score += 30
                details.append("Ung thư: +30")
            if liver:
                score += 20
                details.append("Bệnh gan: +20")
            if chf:
                score += 10
                details.append("Suy tim: +10")
            if cvd:
                score += 10
                details.append("Bệnh mạch máu não: +10")
            if renal:
                score += 10
                details.append("Bệnh thận: +10")
            
            # Physical exam
            if altered_mental:
                score += 20
                details.append("Rối loạn ý thức: +20")
            if resp_rate >= 30:
                score += 20
                details.append(f"Nhịp thở ≥30 ({resp_rate}): +20")
            if sbp < 90:
                score += 20
                details.append(f"HA tâm thu <90 ({sbp}): +20")
            if temp_c < 35 or temp_c >= 40:
                score += 15
                details.append(f"Nhiệt độ bất thường ({temp_c}°C): +15")
            if pulse >= 125:
                score += 10
                details.append(f"Mạch ≥125 ({pulse}): +10")
            
            # Labs
            if ph < 7.35:
                score += 30
                details.append(f"pH <7.35 ({ph:.2f}): +30")
            if bun_mgdl >= 30:
                score += 20
                details.append(f"BUN ≥30 mg/dL ({bun_mgdl:.1f}): +20")
            if sodium < 130:
                score += 20
                details.append(f"Na <130 ({sodium:.0f}): +20")
            if glucose_mgdl >= 250:
                score += 10
                details.append(f"Glucose ≥250 mg/dL ({glucose_mgdl:.0f}): +10")
            if hct < 30:
                score += 10
                details.append(f"Hct <30% ({hct:.1f}): +10")
            if pao2_mmhg < 60:
                score += 10
                details.append(f"PaO2 <60 mmHg ({pao2_mmhg:.0f}): +10")
            if pleural_effusion:
                score += 10
                details.append("Tràn dịch màng phổi: +10")
            
            # Determine risk class
            if score <= 50:
                risk_class = "I"
                mortality = "0.1%"
                recommendation = "Điều trị ngoại trú"
                color = "success"
            elif score <= 70:
                risk_class = "II"
                mortality = "0.6%"
                recommendation = "Điều trị ngoại trú"
                color = "success"
            elif score <= 90:
                risk_class = "III"
                mortality = "2.8%"
                recommendation = "Cân nhắc nhập viện ngắn ngày"
                color = "info"
            elif score <= 130:
                risk_class = "IV"
                mortality = "8.2%"
                recommendation = "Nhập viện"
                color = "warning"
            else:
                risk_class = "V"
                mortality = "29.2%"
                recommendation = "Nhập viện/ICU"
                color = "error"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                if color == "success":
                    st.success(f"## PSI Score: {score}")
                    st.success(f"**Class {risk_class}**")
                elif color == "info":
                    st.info(f"## PSI Score: {score}")
                    st.info(f"**Class {risk_class}**")
                elif color == "warning":
                    st.warning(f"## PSI Score: {score}")
                    st.warning(f"**Class {risk_class}**")
                else:
                    st.error(f"## PSI Score: {score}")
                    st.error(f"**Class {risk_class}**")
                
                st.markdown(f"""
                **Tỷ lệ tử vong 30 ngày:** {mortality}
                
                **Khuyến cáo:** {recommendation}
                """)
            
            st.markdown("---")
            st.markdown("### 💡 Chi tiết tính điểm")
            
            with st.expander("Xem chi tiết"):
                for d in details:
                    st.write(f"• {d}")
                st.markdown(f"**Tổng điểm: {score}**")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo điều trị")
            
            if risk_class in ["I", "II"]:
                st.success(f"""
                **Class {risk_class} - Nguy cơ rất thấp ({mortality})**
                
                **Điều trị ngoại trú:**
                - Kháng sinh đường uống
                - Amoxicillin/Clavulanate hoặc Macrolide
                - Theo dõi tại nhà
                - Tái khám sau 2-3 ngày
                """)
            elif risk_class == "III":
                st.info(f"""
                **Class {risk_class} - Nguy cơ thấp ({mortality})**
                
                **Cân nhắc nhập viện ngắn ngày:**
                - Đánh giá yếu tố xã hội
                - Khả năng tuân thủ điều trị
                - Có thể điều trị ngoại trú nếu ổn định
                - Kháng sinh PO hoặc IV ngắn ngày
                """)
            elif risk_class == "IV":
                st.warning(f"""
                **Class {risk_class} - Nguy cơ trung bình ({mortality})**
                
                **Nhập viện:**
                - Kháng sinh IV
                - Beta-lactam + Macrolide
                - Hỗ trợ oxy nếu cần
                - Theo dõi sát
                - Điều trị ít nhất 24-48h IV
                """)
            else:
                st.error(f"""
                **Class {risk_class} - Nguy cơ cao ({mortality})**
                
                **Nhập viện/ICU ngay:**
                - Kháng sinh IV broad-spectrum
                - Ceftriaxone + Azithromycin
                - Hỗ trợ hô hấp
                - Xem xét ICU nếu:
                  - Cần thở máy
                  - Cần vasopressor
                  - Septic shock
                """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown(f"""
                **PSI/PORT Score - Pneumonia Severity Index**
                
                **Risk Classes & Tỷ lệ tử vong 30 ngày:**
                
                | Class | Điểm | Tử vong | Khuyến cáo |
                |-------|------|---------|------------|
                | I | ≤50 | 0.1% | Ngoại trú |
                | II | 51-70 | 0.6% | Ngoại trú |
                | III | 71-90 | 2.8% | Ngắn ngày/Ngoại trú |
                | IV | 91-130 | 8.2% | Nhập viện |
                | V | >130 | 29.2% | Nhập viện/ICU |
                
                **Kết quả của bạn:** Class {risk_class} ({score} điểm) - {mortality} tử vong
                
                **Ưu điểm:**
                - Chính xác cao hơn CURB-65
                - Dựa trên nhiều biến số lâm sàng và xét nghiệm
                - Validated trong nhiều nghiên cứu lớn
                
                **Nhược điểm:**
                - Phức tạp, cần nhiều xét nghiệm
                - Mất thời gian
                - Có thể không phù hợp cấp cứu
                
                **Reference:**
                Fine MJ, et al. A prediction rule to identify low-risk patients with community-acquired pneumonia. N Engl J Med. 1997;336(4):243-250.
                
                **Guidelines:**
                - IDSA/ATS CAP Guidelines (2019)
                - BTS Guidelines (2009)
                """)


