"""
Framingham Risk Score Calculator
"""

import streamlit as st


def render():
    """Framingham Risk Score Calculator"""
    st.subheader("📈 Framingham Risk Score")
    st.caption("Nguy Cơ Bệnh Tim Mạch 10 Năm")
    
    st.info("""
    **Framingham Risk Score** dự đoán nguy cơ mắc bệnh tim mạch trong 10 năm tới.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông Tin Bệnh Nhân")
        
        # Gender
        sex = st.radio(
            "**Giới tính**",
            ["Nam", "Nữ"],
            horizontal=True,
            key="fram_sex"
        )
        
        # Age
        age = st.number_input(
            "**Tuổi** (30-79 năm)",
            min_value=30,
            max_value=79,
            value=50,
            step=1,
            key="fram_age"
        )
        
        # Total Cholesterol
        st.markdown("**Total Cholesterol**")
        chol_unit = st.radio(
            "Đơn vị:",
            ["mg/dL", "mmol/L"],
            horizontal=True,
            key="fram_chol_unit"
        )
        
        if chol_unit == "mg/dL":
            total_chol = st.number_input(
                "Total Cholesterol (mg/dL)",
                min_value=100,
                max_value=400,
                value=200,
                step=5,
                key="fram_chol_mgdl"
            )
        else:
            chol_mmol = st.number_input(
                "Total Cholesterol (mmol/L)",
                min_value=2.5,
                max_value=10.0,
                value=5.2,
                step=0.1,
                key="fram_chol_mmol"
            )
            total_chol = chol_mmol * 38.67
        
        # HDL Cholesterol
        st.markdown("**HDL Cholesterol**")
        if chol_unit == "mg/dL":
            hdl = st.number_input(
                "HDL (mg/dL)",
                min_value=20,
                max_value=100,
                value=50,
                step=5,
                key="fram_hdl_mgdl"
            )
        else:
            hdl_mmol = st.number_input(
                "HDL (mmol/L)",
                min_value=0.5,
                max_value=2.5,
                value=1.3,
                step=0.1,
                key="fram_hdl_mmol"
            )
            hdl = hdl_mmol * 38.67
        
        # Systolic BP
        sbp = st.number_input(
            "**Huyết áp tâm thu** (mmHg)",
            min_value=90,
            max_value=200,
            value=120,
            step=5,
            key="fram_sbp"
        )
        
        # Treatment for hypertension
        bp_treated = st.checkbox(
            "**Đang điều trị tăng huyết áp**",
            key="fram_bp_tx"
        )
        
        # Smoker
        smoker = st.checkbox(
            "**Hút thuốc lá** (hiện tại)",
            key="fram_smoke"
        )
        
        # Diabetes
        diabetes = st.checkbox(
            "**Đái tháo đường**",
            key="fram_dm"
        )
        
        if st.button("🧮 Tính Framingham Risk", type="primary", key="fram_calc"):
            points = 0
            
            # Simplified Framingham calculation (point-based)
            # This is a simplified version - real implementation would use precise coefficients
            
            # Age points
            if sex == "Nam":
                if age < 35:
                    age_pts = -1
                elif age < 40:
                    age_pts = 0
                elif age < 45:
                    age_pts = 1
                elif age < 50:
                    age_pts = 2
                elif age < 55:
                    age_pts = 3
                elif age < 60:
                    age_pts = 4
                elif age < 65:
                    age_pts = 5
                elif age < 70:
                    age_pts = 6
                else:
                    age_pts = 7
            else:  # Female
                if age < 35:
                    age_pts = -9
                elif age < 40:
                    age_pts = -4
                elif age < 45:
                    age_pts = 0
                elif age < 50:
                    age_pts = 3
                elif age < 55:
                    age_pts = 6
                elif age < 60:
                    age_pts = 7
                elif age < 65:
                    age_pts = 8
                elif age < 70:
                    age_pts = 8
                else:
                    age_pts = 8
            
            points += age_pts
            
            # Total Cholesterol points
            if sex == "Nam":
                if total_chol < 160:
                    chol_pts = -3
                elif total_chol < 200:
                    chol_pts = 0
                elif total_chol < 240:
                    chol_pts = 1
                elif total_chol < 280:
                    chol_pts = 2
                else:
                    chol_pts = 3
            else:
                if total_chol < 160:
                    chol_pts = -2
                elif total_chol < 200:
                    chol_pts = 0
                elif total_chol < 240:
                    chol_pts = 1
                elif total_chol < 280:
                    chol_pts = 2
                else:
                    chol_pts = 3
            
            points += chol_pts
            
            # HDL points
            if hdl >= 60:
                hdl_pts = -2
            elif hdl >= 50:
                hdl_pts = -1
            elif hdl >= 45:
                hdl_pts = 0
            elif hdl >= 35:
                hdl_pts = 1
            else:
                hdl_pts = 2
            
            points += hdl_pts
            
            # Blood pressure points
            if bp_treated:
                if sbp < 120:
                    bp_pts = -1 if sex == "Nữ" else 0
                elif sbp < 130:
                    bp_pts = 2 if sex == "Nữ" else 1
                elif sbp < 140:
                    bp_pts = 3 if sex == "Nữ" else 2
                elif sbp < 160:
                    bp_pts = 5 if sex == "Nữ" else 3
                else:
                    bp_pts = 6 if sex == "Nữ" else 3
            else:
                if sbp < 120:
                    bp_pts = -3 if sex == "Nữ" else 0
                elif sbp < 130:
                    bp_pts = 0
                elif sbp < 140:
                    bp_pts = 1
                elif sbp < 160:
                    bp_pts = 2
                else:
                    bp_pts = 3
            
            points += bp_pts
            
            # Smoking
            if smoker:
                smoke_pts = 3 if sex == "Nữ" else 4
                points += smoke_pts
            
            # Diabetes
            if diabetes:
                dm_pts = 4 if sex == "Nữ" else 2
                points += dm_pts
            
            # Calculate risk percentage (simplified)
            if sex == "Nam":
                if points < 0:
                    risk_pct = 1
                elif points <= 4:
                    risk_pct = 2
                elif points <= 6:
                    risk_pct = 4
                elif points <= 7:
                    risk_pct = 7
                elif points <= 8:
                    risk_pct = 11
                elif points <= 9:
                    risk_pct = 14
                elif points <= 10:
                    risk_pct = 18
                elif points <= 11:
                    risk_pct = 22
                elif points <= 12:
                    risk_pct = 27
                else:
                    risk_pct = 35
            else:  # Female
                if points < -2:
                    risk_pct = 1
                elif points <= 2:
                    risk_pct = 2
                elif points <= 4:
                    risk_pct = 3
                elif points <= 5:
                    risk_pct = 4
                elif points <= 6:
                    risk_pct = 5
                elif points <= 7:
                    risk_pct = 6
                elif points <= 8:
                    risk_pct = 8
                elif points <= 9:
                    risk_pct = 11
                elif points <= 11:
                    risk_pct = 13
                else:
                    risk_pct = 20
            
            # Risk category
            if risk_pct < 10:
                risk_cat = "thấp"
                color = "success"
            elif risk_pct < 20:
                risk_cat = "trung bình"
                color = "warning"
            else:
                risk_cat = "cao"
                color = "error"
            
            with col2:
                st.markdown("### 📊 Kết Quả")
                
                if color == "success":
                    st.success(f"## {risk_pct}%")
                    st.success("✅ Nguy cơ THẤP")
                elif color == "warning":
                    st.warning(f"## {risk_pct}%")
                    st.warning("⚠️ Nguy cơ TRUNG BÌNH")
                else:
                    st.error(f"## {risk_pct}%")
                    st.error("🚨 Nguy cơ CAO")
            
            st.markdown("### 💡 Phân Tích")
            st.write(f"**Nguy cơ mắc bệnh tim mạch trong 10 năm:** {risk_pct}%")
            st.write(f"**Tổng điểm:** {points}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến Cáo")
            
            if risk_pct < 10:
                st.success("""
                **Nguy cơ THẤP (<10%)**
                
                **Can thiệp:**
                - ✅ Thay đổi lối sống
                - Chế độ ăn lành mạnh (DASH, Mediterranean)
                - Tập thể dục đều đặn (≥150 phút/tuần)
                - Duy trì cân nặng hợp lý
                - Cai thuốc lá nếu có
                - Kiểm tra sức khỏe định kỳ
                
                **Thuốc:**
                - Không cần aspirin dự phòng nếu không có chỉ định khác
                - Statin: cân nhắc nếu LDL >190 mg/dL
                """)
            
            elif risk_pct < 20:
                st.warning("""
                **Nguy cơ TRUNG BÌNH (10-20%)**
                
                **Can thiệp tích cực:**
                - ⚠️ Thay đổi lối sống mạnh mẽ
                - Chế độ ăn nghiêm ngặt
                - Tập thể dục đều đặn
                - Giảm cân nếu thừa cân
                - PHẢI cai thuốc lá
                
                **Thuốc:**
                - **Cân nhắc Statin** (mục tiêu LDL <100 mg/dL)
                - Aspirin 75-100mg nếu nguy cơ chảy máu thấp
                - Kiểm soát THA tốt (mục tiêu <130/80)
                - Kiểm soát ĐTĐ nếu có (HbA1c <7%)
                """)
            
            else:
                st.error("""
                **Nguy cơ CAO (≥20%)**
                
                **Can thiệp mạnh:**
                - 🚨 Thay đổi lối sống toàn diện
                - Hội chẩn tim mạch
                - Theo dõi sát
                
                **Thuốc - KHUYẾN CÁO:**
                - **Statin liều cao** (mục tiêu LDL <70 mg/dL)
                - **Aspirin 75-100mg** hàng ngày
                - Kiểm soát THA nghiêm ngặt (<130/80)
                - Kiểm soát ĐTĐ tốt (HbA1c <7%)
                - ACE-I/ARB nếu có THA hoặc ĐTĐ
                - Cân nhắc ezetimibe hoặc PCSK9i nếu LDL vẫn cao
                
                **Theo dõi:**
                - Lipid profile mỗi 3-6 tháng
                - ECG hàng năm
                - Stress test nếu có triệu chứng
                """)
            
            with st.expander("📚 Tài Liệu Tham Khảo"):
                st.markdown("""
                **Framingham Risk Score (FRS)**
                
                **Dự đoán nguy cơ 10 năm mắc:**
                - Angina
                - Myocardial infarction
                - Coronary death
                - Stroke
                
                **Yếu tố nguy cơ:**
                - Age (tuổi)
                - Gender (giới tính)
                - Total cholesterol
                - HDL cholesterol
                - Systolic BP
                - Treatment for hypertension
                - Smoking status
                - Diabetes
                
                **Phân tầng nguy cơ:**
                - **<10%**: Low risk - lifestyle modification
                - **10-20%**: Intermediate risk - consider statin
                - **≥20%**: High risk - statin + aspirin recommended
                
                **Note:**
                - Áp dụng cho người 30-79 tuổi không có bệnh tim mạch
                - Có thể đánh giá thấp nguy cơ ở một số dân số
                - Các công cụ mới hơn: ASCVD Risk Calculator, SCORE2
                
                **References:**
                - Wilson PW et al. Circulation. 1998;97(18):1837-1847.
                - D'Agostino RB et al. Circulation. 2008;117(6):743-753.
                
                **Guidelines:**
                - AHA/ACC Cholesterol Guidelines
                - ESC CVD Prevention Guidelines
                
                **Link:**
                - https://www.mdcalc.com/framingham-risk-score-hard-coronary-heart-disease
                """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
