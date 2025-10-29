"""
GRACE Score Calculator
"""

import streamlit as st


def render():
    """GRACE Score Calculator"""
    st.subheader("📊 GRACE Score")
    st.caption("Tiên Lượng Tử Vong Trong ACS")
    
    st.info("""
    **GRACE Score** dự đoán tử vong trong bệnh viện và 6 tháng sau ACS (STEMI/NSTEMI).
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Số Lâm Sàng")
        
        # Age
        age = st.number_input(
            "**Tuổi** (năm)",
            min_value=20,
            max_value=110,
            value=65,
            step=1,
            key="grace_age"
        )
        
        # Heart rate
        hr = st.number_input(
            "**Nhịp tim** (lần/phút)",
            min_value=30,
            max_value=250,
            value=80,
            step=1,
            key="grace_hr"
        )
        
        # Systolic BP
        sbp = st.number_input(
            "**Huyết áp tâm thu** (mmHg)",
            min_value=50,
            max_value=250,
            value=120,
            step=1,
            key="grace_sbp"
        )
        
        # Creatinine
        st.markdown("**Creatinine máu**")
        scr_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "µmol/L"],
            horizontal=True,
            key="grace_scr_unit"
        )
        
        if scr_unit == "mg/dL":
            scr_mgdl = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                key="grace_scr_mgdl"
            )
        else:
            scr_umol = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                key="grace_scr_umol"
            )
            scr_mgdl = scr_umol / 88.4
        
        # Killip class
        killip = st.selectbox(
            "**Killip Class**",
            [
                "I - Không suy tim",
                "II - S3 hoặc ran ẩm phổi",
                "III - Phù phổi cấp",
                "IV - Shock tim"
            ],
            key="grace_killip"
        )
        killip_class = int(killip[0])
        
        # Cardiac arrest
        cardiac_arrest = st.checkbox(
            "**Ngừng tuần hoàn** khi nhập viện",
            key="grace_arrest"
        )
        
        # ST segment deviation
        st_deviation = st.checkbox(
            "**ST chênh** trên ECG",
            help="ST chênh lên hoặc xuống",
            key="grace_st"
        )
        
        # Elevated cardiac enzymes
        enzymes = st.checkbox(
            "**Enzyme tim tăng** (Troponin/CK-MB)",
            key="grace_enzymes"
        )
        
        if st.button("🧮 Tính GRACE Score", type="primary", key="grace_calc"):
            # Calculate points for each variable
            points = 0
            details = []
            
            # Age points
            if age < 30:
                age_pts = 0
            elif age <= 39:
                age_pts = 8
            elif age <= 49:
                age_pts = 25
            elif age <= 59:
                age_pts = 41
            elif age <= 69:
                age_pts = 58
            elif age <= 79:
                age_pts = 75
            elif age <= 89:
                age_pts = 91
            else:
                age_pts = 100
            points += age_pts
            details.append(f"Tuổi {age}: {age_pts} điểm")
            
            # Heart rate points
            if hr < 50:
                hr_pts = 0
            elif hr <= 69:
                hr_pts = 3
            elif hr <= 89:
                hr_pts = 9
            elif hr <= 109:
                hr_pts = 15
            elif hr <= 149:
                hr_pts = 24
            elif hr <= 199:
                hr_pts = 38
            else:
                hr_pts = 46
            points += hr_pts
            details.append(f"Nhịp tim {hr}: {hr_pts} điểm")
            
            # Systolic BP points
            if sbp < 80:
                sbp_pts = 58
            elif sbp <= 99:
                sbp_pts = 53
            elif sbp <= 119:
                sbp_pts = 43
            elif sbp <= 139:
                sbp_pts = 34
            elif sbp <= 159:
                sbp_pts = 24
            elif sbp <= 199:
                sbp_pts = 10
            else:
                sbp_pts = 0
            points += sbp_pts
            details.append(f"HA tâm thu {sbp}: {sbp_pts} điểm")
            
            # Creatinine points
            if scr_mgdl < 0.4:
                scr_pts = 1
            elif scr_mgdl <= 0.79:
                scr_pts = 4
            elif scr_mgdl <= 1.19:
                scr_pts = 7
            elif scr_mgdl <= 1.59:
                scr_pts = 10
            elif scr_mgdl <= 1.99:
                scr_pts = 13
            elif scr_mgdl <= 3.99:
                scr_pts = 21
            else:
                scr_pts = 28
            points += scr_pts
            details.append(f"Creatinine {scr_mgdl:.2f} mg/dL: {scr_pts} điểm")
            
            # Killip class points
            killip_pts = (killip_class - 1) * 15 + (killip_class - 1) * 5 if killip_class > 1 else 0
            if killip_class == 1:
                killip_pts = 0
            elif killip_class == 2:
                killip_pts = 20
            elif killip_class == 3:
                killip_pts = 39
            else:  # Class 4
                killip_pts = 59
            points += killip_pts
            details.append(f"Killip Class {killip_class}: {killip_pts} điểm")
            
            # Cardiac arrest points
            if cardiac_arrest:
                points += 39
                details.append("Ngừng tuần hoàn: 39 điểm")
            
            # ST deviation points
            if st_deviation:
                points += 28
                details.append("ST chênh: 28 điểm")
            
            # Elevated enzymes points
            if enzymes:
                points += 14
                details.append("Enzyme tăng: 14 điểm")
            
            # Risk calculation
            # In-hospital mortality risk
            if points <= 108:
                risk_category = "thấp"
                hospital_mort = "<1%"
                six_month_mort = "<3%"
                color_class = "success"
            elif points <= 140:
                risk_category = "trung bình"
                hospital_mort = "1-3%"
                six_month_mort = "3-8%"
                color_class = "warning"
            else:
                risk_category = "cao"
                hospital_mort = ">3%"
                six_month_mort = ">8%"
                color_class = "error"
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if color_class == "success":
                    st.success(f"## GRACE = {points}")
                    st.success("✅ Nguy cơ THẤP")
                elif color_class == "warning":
                    st.warning(f"## GRACE = {points}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                else:
                    st.error(f"## GRACE = {points}")
                    st.error("🚨 Nguy cơ CAO")
            
            st.markdown("### 💡 Chi Tiết Điểm")
            for d in details:
                st.write(f"- {d}")
            
            st.markdown("---")
            st.markdown("### 📈 Nguy Cơ Tử Vong")
            
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.metric(
                    label="Tử vong trong viện",
                    value=hospital_mort
                )
            with col_m2:
                st.metric(
                    label="Tử vong 6 tháng",
                    value=six_month_mort
                )
            
            st.markdown("### 💊 Khuyến Cáo Xử Trí")
            
            if risk_category == "thấp":
                st.success(f"""
                **Nguy cơ {risk_category.upper()}**
                
                **Chiến lược:**
                - ✅ Điều trị nội khoa tích cực
                - DAPT (Aspirin + P2Y12 inhibitor)
                - Statin, Beta-blocker, ACE-I
                - Có thể cân nhắc xuất viện sớm nếu ổn định
                - Theo dõi ngoại trú
                - Cân nhắc stress test hoặc CT angiography
                """)
            
            elif risk_category == "trung bình":
                st.warning(f"""
                **Nguy cơ {risk_category.upper()}**
                
                **Chiến lược:**
                - ⚠️ Điều trị tích cực
                - DAPT tối ưu
                - Anticoagulation
                - Cân nhắc chiến lược xâm lấn sớm
                - Coronary angiography trong 24-72h
                - Hội chẩn tim mạch
                - Theo dõi sát tại bệnh viện
                """)
            
            else:
                st.error(f"""
                **Nguy cơ {risk_category.upper()}**
                
                **Chiến lược:**
                - 🚨 Điều trị tích cực tối đa
                - DAPT + Anticoagulation
                - Xử trí biến chứng (suy tim, shock)
                - **Coronary angiography KHẨN CẤP**
                - Chuẩn bị can thiệp/CABG
                - ICU/CCU monitoring
                - Hỗ trợ tuần hoàn nếu cần (IABP, ECMO)
                - Hội chẩn đa chuyên khoa
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **GRACE (Global Registry of Acute Coronary Events) Risk Score**
                
                **8 Biến số:**
                1. Age (tuổi)
                2. Heart rate (nhịp tim)
                3. Systolic BP (HA tâm thu)
                4. Creatinine (creatinine máu)
                5. Killip class (phân loại suy tim)
                6. Cardiac arrest at admission (ngừng tuần hoàn)
                7. ST segment deviation (ST chênh)
                8. Elevated cardiac biomarkers (enzyme tim)
                
                **Tổng điểm: 1-372**
                
                **Phân tầng nguy cơ:**
                - **≤108**: Low risk (<1% in-hospital, <3% 6-month mortality)
                - **109-140**: Intermediate risk (1-3% in-hospital, 3-8% 6-month)
                - **>140**: High risk (>3% in-hospital, >8% 6-month mortality)
                
                **Validation:**
                - GRACE Registry (>100,000 patients)
                - Multiple international validations
                
                **Guidelines:**
                - ESC 2020 ACS Guidelines (Class I recommendation)
                - AHA/ACC Guidelines
                
                **References:**
                - Granger CB et al. Arch Intern Med. 2003;163(19):2345-2353.
                - Fox KAA et al. BMJ. 2006;333(7578):1091.
                
                **Link:**
                - https://www.mdcalc.com/grace-acs-risk-mortality-calculator
                """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
