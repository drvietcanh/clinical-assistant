"""
TIMI Risk Score Calculator
"""

import streamlit as st


def render():
    """TIMI Risk Score Calculator"""
    st.subheader("💔 TIMI Risk Score")
    st.caption("Đánh Giá Nguy Cơ Trong UA/NSTEMI")
    
    st.info("""
    **TIMI Risk Score** dự đoán tử vong, nhồi máu cơ tim mới hoặc cần tái can thiệp trong 14 ngày.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí (7 Tiêu Chuẩn)")
        
        score = 0
        details = []
        
        # Age >= 65
        age_65 = st.checkbox(
            "**Tuổi ≥ 65**",
            help="1 điểm nếu tuổi ≥65",
            key="timi_age"
        )
        if age_65:
            score += 1
            details.append("✓ Tuổi ≥65 (+1)")
        
        # >= 3 CAD risk factors
        st.markdown("**≥ 3 Yếu tố nguy cơ mạch vành**")
        st.caption("THA, ĐTĐ, hút thuốc, cholesterol cao, TSGĐ CHD")
        
        rf_count = 0
        col_rf1, col_rf2 = st.columns(2)
        with col_rf1:
            if st.checkbox("Tăng huyết áp", key="timi_htn"):
                rf_count += 1
            if st.checkbox("Đái tháo đường", key="timi_dm"):
                rf_count += 1
            if st.checkbox("Hút thuốc (hiện tại)", key="timi_smoke"):
                rf_count += 1
        with col_rf2:
            if st.checkbox("Cholesterol cao", key="timi_chol"):
                rf_count += 1
            if st.checkbox("TSGĐ bệnh mạch vành", key="timi_fhx"):
                rf_count += 1
        
        if rf_count >= 3:
            score += 1
            details.append(f"✓ ≥3 yếu tố nguy cơ ({rf_count}) (+1)")
        
        # Known CAD (stenosis >= 50%)
        known_cad = st.checkbox(
            "**Bệnh mạch vành đã biết** (hẹp ≥50%)",
            help="1 điểm nếu có tiền sử can thiệp hoặc hẹp mạch vành đã biết",
            key="timi_cad"
        )
        if known_cad:
            score += 1
            details.append("✓ Bệnh mạch vành đã biết (+1)")
        
        # Aspirin use in past 7 days
        aspirin = st.checkbox(
            "**Dùng Aspirin trong 7 ngày qua**",
            help="1 điểm - nghịch lý cho thấy nguy cơ cao hơn",
            key="timi_aspirin"
        )
        if aspirin:
            score += 1
            details.append("✓ Dùng aspirin 7 ngày qua (+1)")
        
        # Severe angina (>= 2 episodes in 24h)
        severe_angina = st.checkbox(
            "**Đau thắt ngực nặng** (≥2 đợt trong 24h)",
            help="1 điểm nếu có ≥2 đợt đau trong 24h",
            key="timi_angina"
        )
        if severe_angina:
            score += 1
            details.append("✓ Đau thắt ngực nặng (+1)")
        
        # ST changes >= 0.5mm
        st_changes = st.checkbox(
            "**ST chênh ≥ 0.5mm trên ECG**",
            help="ST chênh lên hoặc xuống ≥0.5mm",
            key="timi_st"
        )
        if st_changes:
            score += 1
            details.append("✓ ST chênh ≥0.5mm (+1)")
        
        # Elevated cardiac markers
        elevated_markers = st.checkbox(
            "**Marker tim tăng** (Troponin/CK-MB)",
            help="1 điểm nếu troponin hoặc CK-MB tăng",
            key="timi_markers"
        )
        if elevated_markers:
            score += 1
            details.append("✓ Marker tim tăng (+1)")
        
        if st.button("🧮 Tính TIMI Risk Score", type="primary", key="timi_calc"):
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if score <= 2:
                    st.success(f"## TIMI = {score}")
                    st.success("✅ Nguy cơ THẤP")
                    risk_level = "thấp"
                elif score <= 4:
                    st.warning(f"## TIMI = {score}")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                    risk_level = "trung bình"
                else:
                    st.error(f"## TIMI = {score}")
                    st.error("🚨 Nguy cơ CAO")
                    risk_level = "cao"
            
            # Risk percentages based on score
            risk_data = {
                0: "4.7%",
                1: "8.3%",
                2: "13.2%",
                3: "19.9%",
                4: "26.2%",
                5: "40.9%",
                6: "52.2%",
                7: "65.0%"
            }
            
            st.markdown("### 💡 Chi Tiết Điểm")
            if details:
                for d in details:
                    st.write(f"- {d}")
            else:
                st.write("- Không có yếu tố nguy cơ")
            
            st.markdown("---")
            st.markdown("### 📈 Nguy Cơ Tử Vong/MI/Tái Can Thiệp (14 Ngày)")
            st.metric(
                label="Nguy cơ sự kiện bất lợi",
                value=risk_data.get(score, ">65%"),
                delta=f"TIMI Score = {score}"
            )
            
            st.markdown("### 💊 Khuyến Cáo Điều Trị")
            
            if score <= 2:
                st.success(f"""
                **Nguy cơ {risk_level} ({risk_data.get(score)})**
                
                **Chiến lược bảo tồn (Conservative):**
                - ✅ Có thể xuất viện sớm nếu ổn định
                - Aspirin + P2Y12 inhibitor (DAPT)
                - Statin liều cao
                - Beta-blocker, ACE-I
                - Theo dõi ngoại trú
                - Stress test ngoại trú
                """)
            
            elif score <= 4:
                st.warning(f"""
                **Nguy cơ {risk_level} ({risk_data.get(score)})**
                
                **Chiến lược xâm lấn sớm (Early Invasive):**
                - ⚠️ Nhập viện theo dõi
                - DAPT (Aspirin + Ticagrelor/Prasugrel)
                - Anticoagulation (Enoxaparin/Fondaparinux)
                - Statin liều cao
                - Cân nhắc coronary angiography trong 24-72h
                - Hội chẩn tim mạch
                """)
            
            else:
                st.error(f"""
                **Nguy cơ {risk_level} ({risk_data.get(score)})**
                
                **Chiến lược xâm lấn khẩn cấp (Urgent Invasive):**
                - 🚨 Nhập viện ICU/CCU
                - DAPT ngay (Aspirin + Ticagrelor/Prasugrel)
                - Anticoagulation (Enoxaparin hoặc UFH)
                - GPI (GP IIb/IIIa inhibitor) nếu cần
                - Statin liều cao, Beta-blocker, ACE-I
                - **Coronary angiography KHẨN CẤP (< 24h)**
                - Chuẩn bị PCI/CABG
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **TIMI Risk Score for UA/NSTEMI**
                
                **7 Tiêu chuẩn (mỗi mục 1 điểm):**
                1. Age ≥65 years
                2. ≥3 CAD risk factors (HTN, DM, smoking, high cholesterol, family Hx)
                3. Known CAD (stenosis ≥50%)
                4. Aspirin use in past 7 days
                5. Severe angina (≥2 episodes in 24h)
                6. ST deviation ≥0.5mm
                7. Elevated cardiac markers (troponin/CK-MB)
                
                **Score: 0-7**
                
                **Risk of Death/MI/Urgent Revascularization at 14 days:**
                - 0-1: 4.7-8.3% (Low)
                - 2: 13.2% (Low-Intermediate)
                - 3-4: 19.9-26.2% (Intermediate)
                - 5-7: 40.9-65% (High)
                
                **Original Study:**
                - Antman EM et al. JAMA. 2000;284(7):835-842.
                
                **Guidelines:**
                - AHA/ACC 2014 NSTE-ACS Guidelines
                - ESC 2020 ACS Guidelines
                
                **Link:**
                - https://www.mdcalc.com/timi-risk-score-ua-nstemi
                """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
