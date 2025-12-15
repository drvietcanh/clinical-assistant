"""
Framingham Risk Score Calculator
"""

import streamlit as st
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box, render_result_card
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def render():
    """Framingham Risk Score Calculator"""
    st.subheader("📈 Framingham Risk Score")
    st.caption("Nguy cơ Bệnh Tim Mạch 10 Năm")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'framingham':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    st.info("""
    **Framingham Risk Score** dự đoán nguy cơ mắc bệnh tim mạch trong 10 năm tới.
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông tin bệnh nhân")
        
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
            format="%d",
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
                format="%.0f",
                key="fram_chol_mgdl"
            )
        else:
            chol_mmol = st.number_input(
                "Total Cholesterol (mmol/L)",
                min_value=2.5,
                max_value=10.0,
                value=5.2,
                step=0.1,
                format="%.1f",
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
                format="%.0f",
                key="fram_hdl_mgdl"
            )
        else:
            hdl_mmol = st.number_input(
                "HDL (mmol/L)",
                min_value=0.5,
                max_value=2.5,
                value=1.3,
                step=0.1,
                format="%.1f",
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
            format="%d",
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
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="framingham",
            calculator_name="Framingham Risk Score",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    if st.button("🧮 Tính Framingham Risk", type="primary", key="fram_calc"):
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 30, 79)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            # Validate cholesterol
            if chol_unit == "mg/dL":
                is_valid_chol, chol_error = validate_lab_value(total_chol, "Total Cholesterol (mg/dL)", 100, 400)
            else:
                is_valid_chol, chol_error = validate_lab_value(chol_mmol, "Total Cholesterol (mmol/L)", 2.5, 10.0)
            if not is_valid_chol:
                validation_errors.append(chol_error)
            
            # Validate HDL
            if chol_unit == "mg/dL":
                is_valid_hdl, hdl_error = validate_lab_value(hdl, "HDL (mg/dL)", 20, 100)
            else:
                is_valid_hdl, hdl_error = validate_lab_value(hdl_mmol, "HDL (mmol/L)", 0.5, 2.5)
            if not is_valid_hdl:
                validation_errors.append(hdl_error)
            
            is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
            
            if validation_errors:
                render_validation_errors(validation_errors)
            
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
            
            # Map color names to component colors
            color_map = {
                "success": "success",
                "warning": "warning",
                "error": "error"
            }
            icon_map = {
                "success": "✅",
                "warning": "⚠️",
                "error": "🚨"
            }
            component_color = color_map.get(color, "info")
            component_icon = icon_map.get(color, "💡")
            
            with col2:
                st.markdown("### 📊 Kết quả")
                
                # Use render_result_box for risk percentage display
                render_result_box(
                    title="Nguy cơ 10 năm mắc bệnh tim mạch",
                    value=f"{risk_pct}%",
                    subtitle=f"Nguy cơ {risk_cat}",
                    color=component_color,
                    icon=component_icon,
                    size="large"
                )
            
            st.markdown("---")
            st.markdown("### 💡 Phân tích")
            st.write(f"**Nguy cơ mắc bệnh tim mạch trong 10 năm:** {risk_pct}%")
            st.write(f"**Tổng điểm:** {points}")
            
            st.markdown("---")
            st.markdown("### 💊 Khuyến cáo")
            
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
            
            # Prepare inputs and results for export/history
            inputs_dict = {
                "Gender": sex,
                "Age": str(age),
                "Total Cholesterol": f"{total_chol:.0f} {chol_unit}" if chol_unit == "mg/dL" else f"{chol_mmol:.1f} {chol_unit}",
                "HDL": f"{hdl:.0f} {chol_unit}" if chol_unit == "mg/dL" else f"{hdl_mmol:.1f} {chol_unit}",
                "Systolic BP": f"{sbp} mmHg",
                "BP Treatment": "Có" if bp_treated else "Không",
                "Smoker": "Có" if smoker else "Không",
                "Diabetes": "Có" if diabetes else "Không"
            }
            
            results_dict = {
                "Framingham Risk Score": f"{points} điểm",
                "10-Year Risk": f"{risk_pct}%",
                "Risk Category": risk_cat.upper(),
                "Recommendation": "Thay đổi lối sống" if risk_pct < 10 else "Cân nhắc statin" if risk_pct < 20 else "Statin + Aspirin"
            }
            
            # Export section
            st.markdown("---")
            from components.export import render_export_section
            render_export_section(
                title=f"Framingham Risk = {risk_pct}%",
                inputs=inputs_dict,
                results=results_dict,
                calculator_name="Framingham Risk Score",
                filename="framingham_result"
            )
            
            # Save to history
            save_calculation_to_history(
                calculator_id="framingham",
                calculator_name="Framingham Risk Score",
                inputs=inputs_dict,
                results=results_dict
            )
            
            # Share section
            render_share_section(
                calculator_id="framingham",
                calculator_name="Framingham Risk Score",
                inputs=inputs_dict,
                results=results_dict,
                show_qr=True
            )
            
            # History section
            st.markdown("---")
            from components.calculation_history import render_history_ui
            render_history_ui(calculator_id="framingham", show_actions=True)
            
            # References section
            references = get_references("Framingham")
            if references:
                render_references_section(
                    references=references,
                    title="📚 Tài liệu tham khảo",
                    last_updated="2024-01-15",
                    show_evidence_level=True,
                    show_links=True
                )
            else:
                # Fallback to manual references
                with st.expander("📚 Tài liệu tham khảo"):
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
    
    # Always show references at the bottom
    references = get_references("Framingham")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")
