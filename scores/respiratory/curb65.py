"""
CURB-65 Score
Community-Acquired Pneumonia severity assessment
"""

import streamlit as st


def render():
    """CURB-65 Score Calculator"""
    st.subheader("🫁 CURB-65")
    st.caption("Mức Độ Nặng Viêm Phổi Cộng Đồng")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu Chí Đánh Giá")
        
        confusion = st.checkbox(
            "**C** - Confusion (Lú lẫn)",
            help="Mới xuất hiện hoặc AMT ≤8"
        )
        
        # Urea with unit conversion
        st.markdown("#### **U** - Urea")
        urea_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L"],
            horizontal=True,
            key="urea_unit_curb65"
        )
        
        if urea_unit == "mg/dL":
            urea_input = st.number_input(
                "Urea (mg/dL)",
                min_value=0.0,
                max_value=200.0,
                value=20.0,
                step=1.0,
                help="BUN (Blood Urea Nitrogen)",
                key="urea_mgdl"
            )
            urea_mmol = urea_input / 2.8  # Convert to mmol/L
        else:
            urea_input = st.number_input(
                "Urea (mmol/L)",
                min_value=0.0,
                max_value=70.0,
                value=7.0,
                step=0.5,
                key="urea_mmol"
            )
            urea_mmol = urea_input
        
        # Display converted value
        if urea_unit == "mmol/L":
            st.caption(f"≈ {urea_mmol * 2.8:.1f} mg/dL")
        else:
            st.caption(f"≈ {urea_mmol:.1f} mmol/L")
        
        urea_high = urea_mmol > 7.0  # >7 mmol/L (>20 mg/dL)
        
        # Respiratory rate
        rr = st.number_input(
            "**R** - Respiratory Rate (nhịp thở/phút)",
            min_value=0,
            max_value=60,
            value=18,
            step=1,
            help="Bình thường: 12-20/phút"
        )
        
        # Blood pressure
        sbp = st.number_input(
            "**B** - Systolic BP (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=5
        )
        
        dbp = st.number_input(
            "Diastolic BP (mmHg)",
            min_value=0,
            max_value=200,
            value=80,
            step=5
        )
        
        # Age
        age = st.number_input(
            "Tuổi",
            min_value=0,
            max_value=120,
            value=50,
            step=1
        )
        
        if st.button("🧮 Tính CURB-65", type="primary"):
            score = 0
            details = []
            
            if confusion:
                score += 1
                details.append("✓ Confusion - Lú lẫn (+1)")
            
            if urea_high:
                score += 1
                details.append(f"✓ Urea >7 mmol/L ({urea_mmol:.1f}) (+1)")
            
            if rr >= 30:
                score += 1
                details.append(f"✓ RR ≥30/phút ({rr}) (+1)")
            
            if sbp < 90 or dbp <= 60:
                score += 1
                details.append(f"✓ BP thấp (SBP<90 hoặc DBP≤60) (+1)")
            
            if age >= 65:
                score += 1
                details.append(f"✓ Tuổi ≥65 ({age}) (+1)")
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if score == 0:
                    st.success(f"## CURB-65 = {score}")
                    st.success("✅ Nguy Cơ THẤP")
                    mortality = "0.7%"
                    recommendation = "Điều trị ngoại trú"
                elif score == 1:
                    st.info(f"## CURB-65 = {score}")
                    st.info("💡 Nguy Cơ THẤP")
                    mortality = "2.1%"
                    recommendation = "Điều trị ngoại trú hoặc theo dõi ngắn"
                elif score == 2:
                    st.warning(f"## CURB-65 = {score}")
                    st.warning("⚠️ Nguy Cơ TRUNG BÌNH")
                    mortality = "9.2%"
                    recommendation = "Cân nhắc nhập viện"
                elif score == 3:
                    st.error(f"## CURB-65 = {score}")
                    st.error("❗ Nguy Cơ CAO")
                    mortality = "14.5%"
                    recommendation = "Nhập viện, ICU nếu cần"
                else:
                    st.error(f"## CURB-65 = {score}")
                    st.error("🚨 Nguy Cơ RẤT CAO")
                    mortality = "40%"
                    recommendation = "Nhập ICU ngay"
            
            st.markdown("### 💡 Giải Thích")
            
            if details:
                for d in details:
                    st.write(f"- {d}")
            else:
                st.write("- Không có tiêu chí nào")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo")
            
            st.info(f"""
            **Tỷ lệ tử vong 30 ngày:** {mortality}
            
            **Khuyến cáo:** {recommendation}
            """)
            
            if score <= 1:
                st.success("""
                **Điều trị ngoại trú:**
                - Amoxicillin hoặc Macrolide
                - Theo dõi tại nhà
                - Tái khám sau 2-3 ngày
                """)
            elif score == 2:
                st.warning("""
                **Cân nhắc nhập viện:**
                - Đánh giá thêm các yếu tố khác
                - Oxy saturation
                - Bệnh lý nền
                - Khả năng tuân thủ điều trị
                """)
            else:
                st.error("""
                **Nhập viện/ICU:**
                - Kháng sinh IV
                - Beta-lactam + Macrolide
                - Hỗ trợ oxy
                - Theo dõi sát
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **CURB-65 Score**
                
                **Tiêu chí (1 điểm mỗi mục):**
                - **C**: Confusion (AMT ≤8)
                - **U**: Urea >7 mmol/L (>20 mg/dL BUN)
                - **R**: Respiratory rate ≥30/min
                - **B**: Blood pressure (SBP <90 hoặc DBP ≤60 mmHg)
                - **65**: Age ≥65 years
                
                **Tỷ lệ tử vong 30 ngày:**
                - Score 0-1: 0.7-2.1% (điều trị ngoại trú)
                - Score 2: 9.2% (cân nhắc nhập viện)
                - Score 3-5: 14.5-40% (nhập viện/ICU)
                
                **Reference:**
                Lim WS, et al. Defining community acquired pneumonia severity on presentation to hospital: an international derivation and validation study. Thorax. 2003;58(5):377-382.
                
                **Guidelines:**
                - BTS Guidelines for CAP (2009)
                - IDSA/ATS Guidelines (2019)
                """)

