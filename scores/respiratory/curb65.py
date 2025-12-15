"""
CURB-65 Score
Community-Acquired Pneumonia severity assessment
"""

import streamlit as st
from scores.utils.validation import (
    validate_age,
    validate_respiratory_rate,
    validate_blood_pressure,
    validate_lab_value
)
from components.ui.scoring import render_score_result, render_score_breakdown


def render():
    """CURB-65 Score Calculator"""
    st.subheader("🫁 CURB-65")
    st.caption("Mức Độ Nặng Viêm Phổi Cộng Đồng")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Tiêu chí Đánh giá")
        
        confusion = st.checkbox(
            "**C** - Confusion (Lú lẫn)",
            help="Mới xuất hiện hoặc AMT ≤8"
        )
        
        # Urea with unit conversion
        st.markdown("#### **U** - Urea")
        urea_unit = st.radio(
            "Đơn vị:",
            ["mmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="urea_unit_curb65"
        )
        
        if urea_unit == "mmol/L":
            urea_input = st.number_input(
                "Urea (mmol/L)",
                min_value=0.0,
                max_value=70.0,
                value=7.0,
                step=0.5,
                format="%.1f",
                help="Bình thường: 2.5-7.1 mmol/L",
                key="urea_mmol"
            )
            urea_mmol = urea_input
            st.caption(f"≈ {urea_mmol * 2.8:.1f} mg/dL")
        else:
            urea_input = st.number_input(
                "Urea (mg/dL)",
                min_value=0.0,
                max_value=200.0,
                value=20.0,
                step=1.0,
                format="%.0f",
                help="BUN (Blood Urea Nitrogen)",
                key="urea_mgdl"
            )
            urea_mmol = urea_input / 2.8  # Convert to mmol/L
            st.caption(f"≈ {urea_mmol:.1f} mmol/L")
        
        urea_high = urea_mmol > 7.0  # >7 mmol/L (>20 mg/dL)
        
        # Respiratory rate
        rr = st.number_input(
            "**R** - Nhịp thở (nhịp thở/phút)",
            min_value=0,
            max_value=60,
            value=18,
            step=1,
            format="%d",
            help="Bình thường: 12-20/phút"
        )
        
        # Blood pressure
        sbp = st.number_input(
            "**B** - Systolic BP (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=5,
            format="%d"
        )
        
        dbp = st.number_input(
            "Diastolic BP (mmHg)",
            min_value=0,
            max_value=200,
            value=80,
            step=5,
            format="%d"
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
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 0, 120)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            is_valid_rr, rr_error = validate_respiratory_rate(rr)
            if not is_valid_rr:
                validation_errors.append(rr_error)
            
            is_valid_bp, bp_error = validate_blood_pressure(sbp, dbp)
            if not is_valid_bp:
                validation_errors.append(bp_error)
            
            # Validate urea
            if urea_unit == "mmol/L":
                is_valid_urea, urea_error = validate_lab_value(urea_mmol, "Urea (mmol/L)", 0, 70)
            else:
                is_valid_urea, urea_error = validate_lab_value(urea_input, "Urea (mg/dL)", 0, 200)
            if not is_valid_urea:
                validation_errors.append(urea_error)
            
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
            
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
            
            # Determine risk level and color
            if score == 0:
                risk_level = "Nguy cơ THẤP"
                mortality = "0.7%"
                recommendation = "Điều trị ngoại trú"
                color = "#28a745"  # green
                icon = "✅"
            elif score == 1:
                risk_level = "Nguy cơ THẤP"
                mortality = "2.1%"
                recommendation = "Điều trị ngoại trú hoặc theo dõi ngắn"
                color = "#17a2b8"  # info blue
                icon = "💡"
            elif score == 2:
                risk_level = "Nguy cơ TRUNG BÌNH"
                mortality = "9.2%"
                recommendation = "Cân nhắc nhập viện"
                color = "#fd7e14"  # orange
                icon = "⚠️"
            elif score == 3:
                risk_level = "Nguy cơ CAO"
                mortality = "14.5%"
                recommendation = "Nhập viện, ICU nếu cần"
                color = "#dc3545"  # red
                icon = "❗"
            else:
                risk_level = "Nguy cơ RẤT CAO"
                mortality = "40%"
                recommendation = "Nhập ICU ngay"
                color = "#6c757d"  # dark gray
                icon = "🚨"
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_score_result for main score display
                render_score_result(
                    title="CURB-65 Score",
                    score=score,
                    interpretation=risk_level,
                    mortality=f"Tử vong 30 ngày: {mortality}",
                    color=color,
                    icon=icon,
                    size="large"
                )
            
            # Build breakdown of criteria
            criteria_scores = {}
            if confusion:
                criteria_scores["C - Confusion"] = 1
            if urea_high:
                criteria_scores["U - Urea >7 mmol/L"] = 1
            if rr >= 30:
                criteria_scores["R - RR ≥30/phút"] = 1
            if sbp < 90 or dbp <= 60:
                criteria_scores["B - BP thấp"] = 1
            if age >= 65:
                criteria_scores["65 - Tuổi ≥65"] = 1
            
            if criteria_scores:
                render_score_breakdown(
                    title="Tiêu Chí Đánh Giá",
                    subscores=criteria_scores,
                    total_score=score
                )
            
            st.markdown("---")
            st.markdown("### 💡 Chi tiết")
            
            if details:
                for d in details:
                    st.write(f"- {d}")
            else:
                st.write("- Không có tiêu chí nào")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo")
            
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
            
            with st.expander("📚 Tài liệu tham khảo"):
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

