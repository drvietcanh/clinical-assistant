"""
ASCVD Risk Calculator (ACC/AHA Pooled Cohort Equations)
=========================================================

Atherosclerotic Cardiovascular Disease 10-Year Risk Calculator
Based on 2013 ACC/AHA Risk Assessment Guideline

Reference:
- Goff DC Jr, et al. 2013 ACC/AHA Guideline on the Assessment of 
  Cardiovascular Risk: A Report of the American College of Cardiology/
  American Heart Association Task Force on Practice Guidelines. 
  Circulation. 2014;129(25 Suppl 2):S49-S73.
- 2019 ACC/AHA Guideline on the Primary Prevention of Cardiovascular Disease

Variables:
- Age (40-79 years)
- Gender (Male/Female)
- Race (White, African American, Other)
- Total Cholesterol (TC)
- HDL Cholesterol
- Huyết áp tâm thu
- Treatment for hypertension (yes/no)
- Diabetes (yes/no)
- Current smoking (yes/no)
- Current statin use (optional)

Output:
- 10-year ASCVD risk percentage
- Risk category
- Recommendations
"""

import streamlit as st
from config.theme import COLORS
import math
from components.ui.results import render_result_box, render_result_card
from scores.utils.validation import validate_age, validate_blood_pressure, validate_lab_value
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
# ======================================


def calculate_ascvd_male_white(
    age: float,
    tc: float,
    hdl: float,
    sbp: float,
    bp_treated: bool,
    diabetes: bool,
    smoker: bool
) -> float:
    """
    Calculate ASCVD risk for White/African American males
    
    Pooled Cohort Equations coefficients for males
    """
    # Coefficients from 2013 ACC/AHA Pooled Cohort Equations
    # Natural log transformations
    ln_age = math.log(age)
    ln_tc = math.log(tc)
    ln_hdl = math.log(hdl)
    ln_sbp = math.log(sbp)
    
    # Age term
    age_term = 12.344 * ln_age
    
    # Cholesterol terms
    tc_term = 11.853 * ln_tc
    hdl_term = -7.990 * ln_hdl
    
    # Blood pressure terms
    if bp_treated:
        sbp_term = 1.764 * ln_sbp
    else:
        sbp_term = 1.797 * ln_sbp
    
    # Risk factors
    diabetes_term = 0.658 * (1 if diabetes else 0)
    smoker_term = 0.573 * (1 if smoker else 0)
    
    # Sum
    sum_coeff = age_term + tc_term + hdl_term + sbp_term + diabetes_term + smoker_term - 61.18
    
    # Risk
    risk = 1 - math.pow(0.91436, math.exp(sum_coeff))
    
    return max(0, min(100, risk * 100))


def calculate_ascvd_female_white(
    age: float,
    tc: float,
    hdl: float,
    sbp: float,
    bp_treated: bool,
    diabetes: bool,
    smoker: bool
) -> float:
    """
    Calculate ASCVD risk for White/African American females
    """
    ln_age = math.log(age)
    ln_tc = math.log(tc)
    ln_hdl = math.log(hdl)
    ln_sbp = math.log(sbp)
    
    age_term = -29.799 * ln_age + 4.884 * ln_age * ln_age
    tc_term = 13.540 * ln_tc
    hdl_term = -13.578 * ln_hdl
    sbp_term = 2.019 * ln_sbp if bp_treated else 1.957 * ln_sbp
    
    diabetes_term = 0.661 * (1 if diabetes else 0)
    smoker_term = 0.596 * (1 if smoker else 0)
    
    sum_coeff = age_term + tc_term + hdl_term + sbp_term + diabetes_term + smoker_term - 29.18
    
    risk = 1 - math.pow(0.96652, math.exp(sum_coeff))
    
    return max(0, min(100, risk * 100))


def calculate_ascvd_male_african_american(
    age: float,
    tc: float,
    hdl: float,
    sbp: float,
    bp_treated: bool,
    diabetes: bool,
    smoker: bool
) -> float:
    """
    Calculate ASCVD risk for African American males
    """
    ln_age = math.log(age)
    ln_tc = math.log(tc)
    ln_hdl = math.log(hdl)
    ln_sbp = math.log(sbp)
    
    age_term = 2.469 * ln_age
    tc_term = 0.302 * ln_tc
    hdl_term = -0.307 * ln_hdl
    sbp_term = 1.916 * ln_sbp if bp_treated else 1.809 * ln_sbp
    
    diabetes_term = 0.549 * (1 if diabetes else 0)
    smoker_term = 0.645 * (1 if smoker else 0)
    
    sum_coeff = age_term + tc_term + hdl_term + sbp_term + diabetes_term + smoker_term + 0.113 - 17.114
    
    risk = 1 - math.pow(0.89536, math.exp(sum_coeff))
    
    return max(0, min(100, risk * 100))


def calculate_ascvd_female_african_american(
    age: float,
    tc: float,
    hdl: float,
    sbp: float,
    bp_treated: bool,
    diabetes: bool,
    smoker: bool
) -> float:
    """
    Calculate ASCVD risk for African American females
    """
    ln_age = math.log(age)
    ln_tc = math.log(tc)
    ln_hdl = math.log(hdl)
    ln_sbp = math.log(sbp)
    
    age_term = -29.18 * ln_age + 4.459 * ln_age * ln_age
    tc_term = 13.415 * ln_tc
    hdl_term = -13.578 * ln_hdl
    sbp_term = 2.019 * ln_sbp if bp_treated else 1.930 * ln_sbp
    
    diabetes_term = 0.661 * (1 if diabetes else 0)
    smoker_term = 0.597 * (1 if smoker else 0)
    
    sum_coeff = age_term + tc_term + hdl_term + sbp_term + diabetes_term + smoker_term - 86.61
    
    risk = 1 - math.pow(0.95334, math.exp(sum_coeff))
    
    return max(0, min(100, risk * 100))


def calculate_ascvd(
    age: float,
    is_male: bool,
    race: str,
    tc: float,
    hdl: float,
    sbp: float,
    bp_treated: bool,
    diabetes: bool,
    smoker: bool
) -> dict:
    """
    Calculate 10-year ASCVD risk using Pooled Cohort Equations
    
    Args:
        age: Age in years (40-79)
        is_male: True for male, False for female
        race: "White", "African American", or "Other"
        tc: Total cholesterol (mg/dL)
        hdl: HDL cholesterol (mg/dL)
        sbp: Systolic blood pressure (mmHg)
        bp_treated: Whether on treatment for hypertension
        diabetes: Whether has diabetes
        smoker: Whether current smoker
    
    Returns:
        Dictionary with risk percentage, category, and recommendations
    """
    
    # Validate inputs
    if age < 40 or age > 79:
        return {
            'error': 'Tuổi phải từ 40-79 để sử dụng công cụ này',
            'risk': None
        }
    
    # Select calculation function based on gender and race
    if is_male:
        if race == "African American":
            risk_percent = calculate_ascvd_male_african_american(
                age, tc, hdl, sbp, bp_treated, diabetes, smoker
            )
        else:  # White or Other
            risk_percent = calculate_ascvd_male_white(
                age, tc, hdl, sbp, bp_treated, diabetes, smoker
            )
    else:  # Female
        if race == "African American":
            risk_percent = calculate_ascvd_female_african_american(
                age, tc, hdl, sbp, bp_treated, diabetes, smoker
            )
        else:  # White or Other
            risk_percent = calculate_ascvd_female_white(
                age, tc, hdl, sbp, bp_treated, diabetes, smoker
            )
    
    # Determine risk category
    if risk_percent < 5.0:
        category = "Low"
        category_vn = "Thấp"
        color = COLORS["success"]
    elif risk_percent < 7.5:
        category = "Borderline"
        category_vn = "Trung bình"
        color = COLORS["primary"]
    elif risk_percent < 20.0:
        category = "Intermediate"
        category_vn = "Trung bình-Cao"
        color = COLORS["warning"]
    else:
        category = "High"
        category_vn = "Cao"
        color = COLORS["error"]
    
    # Generate recommendations based on 2019 ACC/AHA Primary Prevention Guidelines
    recommendations = []
    
    if risk_percent >= 20.0:
        recommendations.append("✅ **Statin therapy khởi phát** - Nguy cơ cao cần điều trị ngay")
        recommendations.append("✅ **Điều chỉnh lối sống mạnh mẽ** - Diet, exercise, smoking cessation")
        recommendations.append("✅ **Kiểm soát huyết áp** - Mục tiêu <130/80 mmHg nếu có")
        recommendations.append("✅ **Aspirin** - Cân nhắc nếu không có chống chỉ định (75-100 mg/ngày)")
    elif risk_percent >= 7.5:
        recommendations.append("💊 **Cân nhắc statin therapy** - Thảo luận với bệnh nhân")
        recommendations.append("✅ **Điều chỉnh lối sống** - Diet, exercise, weight management")
        recommendations.append("✅ **Kiểm soát các yếu tố nguy cơ** - BP, diabetes, smoking")
        recommendations.append("📊 **Đánh giá thêm** - CAC score hoặc hs-CRP có thể hữu ích")
    elif risk_percent >= 5.0:
        recommendations.append("💡 **Tối ưu hóa lối sống** - Diet, exercise, smoking cessation")
        recommendations.append("📊 **Theo dõi định kỳ** - Đánh giá lại trong 5-10 năm")
        recommendations.append("⚠️ **Kiểm soát các yếu tố nguy cơ** - BP, cholesterol, diabetes")
    else:
        recommendations.append("✅ **Duy trì lối sống lành mạnh** - Diet, exercise")
        recommendations.append("📊 **Theo dõi định kỳ** - Đánh giá lại trong 5-10 năm")
        recommendations.append("💡 **Phòng ngừa tiên phát** - Tránh các yếu tố nguy cơ")
    
    # Additional recommendations based on risk factors
    if diabetes:
        recommendations.append("⚠️ **Đái tháo đường:** Kiểm soát đường huyết chặt chẽ (HbA1c <7%)")
    if smoker:
        recommendations.append("🚭 **Hút thuốc:** Ngừng hút thuốc ngay lập tức - giảm nguy cơ 50% sau 1 năm")
    if sbp >= 130:
        recommendations.append("🩺 **Tăng huyết áp:** Mục tiêu <130/80 mmHg (ACC/AHA 2017)")
    if hdl < 40:
        recommendations.append("📈 **HDL thấp:** Tăng cường exercise, giảm carb, có thể cân nhắc niacin/fibrate")
    
    return {
        'risk': risk_percent,
        'category': category,
        'category_vn': category_vn,
        'color': color,
        'recommendations': recommendations
    }


def render():
    """ASCVD Risk Calculator"""
    # st.subheader("❤️ ASCVD Risk Calculator")
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>❤️ ASCVD Risk Calculator</h3>
    """, unsafe_allow_html=True)
    st.caption("Atherosclerotic Cardiovascular Disease - 10-Year Risk Assessment (ACC/AHA 2013)")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'ascvd':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        # Smart Suggestions
        render_suggestions(
            calculator_id="ascvd",
            calculator_name="ASCVD Risk Calculator",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
        
        # Educational information - Enhanced with Phase 1 Metadata
        if CALCULATOR_METADATA_AVAILABLE:
            st.markdown("---")
            render_calculator_education("ascvd")
        elif CALCULATOR_ENHANCEMENTS_AVAILABLE:
            st.markdown("---")
            render_calculator_explanation(
                title="Về ASCVD Risk Calculator",
                content="ASCVD đánh giá nguy cơ tim mạch 10 năm...",
                when_to_use="Sử dụng khi...",
                limitations="Hạn chế...",
                clinical_context="Bối cảnh lâm sàng..."
            )
    
    with col1:
        st.markdown("### Thông tin bệnh nhân")
        
        # Age
        age = st.number_input(
            "**Tuổi** (40-79 năm)",
            min_value=40,
            max_value=79,
            value=55,
            step=1,
            format="%d",
            help="ASCVD calculator chỉ áp dụng cho người 40-79 tuổi"
        )
        
        # Gender
        sex = st.radio(
            "**Giới tính**",
            ["Nam", "Nữ"],
            horizontal=True,
            index=0
        )
        is_male = (sex == "Nam")
        
        # Race
        race = st.selectbox(
            "**Chủng tộc**",
            ["White", "African American", "Other"],
            index=0,
            help="Pooled Cohort Equations có hệ số riêng cho White và African American"
        )
        
        st.markdown("---")
        st.markdown("### Xét nghiệm")
        
        # Cholesterol units
        chol_unit = st.radio(
            "Đơn vị cholesterol:",
            ["mg/dL", "mmol/L"],
            horizontal=True,
            index=0
        )
        
        # Total Cholesterol
        if chol_unit == "mg/dL":
            tc = st.number_input(
                "**Total Cholesterol** (mg/dL)",
                min_value=100.0,
                max_value=400.0,
                value=200.0,
                step=5.0,
                format="%.0f",
                help="Bình thường: <200 mg/dL"
            )
            tc_mgdl = tc
        else:
            tc_mmol = st.number_input(
                "**Total Cholesterol** (mmol/L)",
                min_value=2.5,
                max_value=10.0,
                value=5.2,
                step=0.1,
                format="%.1f"
            )
            tc_mgdl = tc_mmol * 38.67
            tc = tc_mmol
        
        # HDL Cholesterol
        if chol_unit == "mg/dL":
            hdl = st.number_input(
                "**HDL Cholesterol** (mg/dL)",
                min_value=20.0,
                max_value=150.0,
                value=50.0,
                step=5.0,
                format="%.0f",
                help="Bình thường: ≥40 mg/dL (nam), ≥50 mg/dL (nữ)"
            )
            hdl_mgdl = hdl
        else:
            hdl_mmol = st.number_input(
                "**HDL Cholesterol** (mmol/L)",
                min_value=0.5,
                max_value=4.0,
                value=1.3,
                step=0.1,
                format="%.1f"
            )
            hdl_mgdl = hdl_mmol * 38.67
            hdl = hdl_mmol
        
        st.markdown("---")
        st.markdown("### Yếu tố nguy cơ")
        
        # Systolic BP
        sbp = st.number_input(
            "**Huyết áp tâm thu** (mmHg)",
            min_value=90,
            max_value=250,
            value=120,
            step=5,
            format="%d",
            help="Bình thường: <120 mmHg"
        )
        
        # BP treatment
        bp_treated = st.checkbox(
            "**Đang điều trị tăng huyết áp**",
            help="Bệnh nhân đang dùng thuốc điều trị tăng huyết áp"
        )
        
        # Diabetes
        diabetes = st.checkbox(
            "**Đái tháo đường**",
            help="Bệnh nhân có đái tháo đường type 1 hoặc type 2"
        )
        
        # Smoking
        smoker = st.checkbox(
            "**Hút thuốc lá hiện tại**",
            help="Hút thuốc trong vòng 30 ngày qua"
        )
        
        if st.button("🧮 Tính ASCVD Risk", type="primary"):
            # Validate inputs
            validation_errors = []
            
            is_valid_age, age_error = validate_age(age, 40, 79)
            if not is_valid_age:
                validation_errors.append(age_error)
            
            is_valid_tc, tc_error = validate_lab_value(tc_mgdl, "Total Cholesterol (mg/dL)", 100, 400)
            if not is_valid_tc:
                validation_errors.append(tc_error)
                
            is_valid_hdl, hdl_error = validate_lab_value(hdl_mgdl, "HDL Cholesterol (mg/dL)", 20, 150)
            if not is_valid_hdl:
                validation_errors.append(hdl_error)
                
            is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
            if not is_valid_sbp:
                validation_errors.append(sbp_error)
                
            if validation_errors:
                st.error("**⚠️ Lỗi validation:**")
                for error in validation_errors:
                    st.error(f"- {error}")
                st.stop()
                
            result = calculate_ascvd(
                age=age,
                is_male=is_male,
                race=race,
                tc=tc_mgdl,
                hdl=hdl_mgdl,
                sbp=sbp,
                bp_treated=bp_treated,
                diabetes=diabetes,
                smoker=smoker
            )
            
            if 'error' in result:
                st.error(result['error'])
            else:
                with col2:
                    # Modern Result Card
                    color_hex = color
                    
                    bg_color = {
                        COLORS["error"]: COLORS["error_light"],
                        COLORS["warning"]: COLORS["warning_light"],
                        COLORS["primary"]: COLORS["primary_light"],
                        COLORS["success"]: COLORS["success_light"]
                    }.get(color, COLORS["info_light"])

                    st.markdown(f"""
                    <div style="background: {bg_color}; border-radius: 12px; padding: 24px; border: 1px solid {color_hex}; text-align: center; margin-bottom: 24px;">
                        <h3 style="color: {color_hex}; margin: 0 0 8px 0; font-size: 1.1em; text-transform: uppercase; letter-spacing: 0.5px;">Nguy cơ 10 năm ASCVD</h3>
                        <div style="font-size: 3.5em; font-weight: 700; color: {color_hex}; line-height: 1.2;">
                            {risk_percent:.1f}%
                        </div>
                        <div style="background: {color_hex}; color: white; display: inline-block; padding: 4px 16px; border-radius: 20px; font-weight: 600; margin-top: 8px;">
                            {category_vn} Risk
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Recommendations Card
                    st.markdown("""
                    <div style="background: white; border-radius: 8px; padding: 20px; border: 1px solid #dadce0; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                        <h4 style="margin-top: 0; color: #202124; border-bottom: 1px solid #f1f3f4; padding-bottom: 12px; margin-bottom: 16px;">
                            📋 Khuyến nghị lâm sàng
                        </h4>
                    """, unsafe_allow_html=True)
                    
                    for rec in result['recommendations']:
                        # Style bullet points
                        icon = rec.split(' ', 1)[0]
                        text = rec.split(' ', 1)[1] if ' ' in rec else rec
                        st.markdown(f"""
                        <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px;">
                            <span style="font-size: 1.2em; line-height: 1;">{icon}</span>
                            <span style="color: #3c4043; line-height: 1.5;">{text}</span>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Card container is closed within the same HTML block above
                
                # Display input summary
                st.markdown("### Tóm tắt thông tin đầu vào")
                summary_cols = st.columns(3)
                
                with summary_cols[0]:
                    st.markdown(f"**Tuổi:** {age} tuổi")  
                    st.markdown(f"**Giới tính:** {sex}")
                    st.markdown(f"**Chủng tộc:** {race}")
                
                with summary_cols[1]:
                    st.markdown(f"**Total Cholesterol:** {tc_mgdl:.0f} mg/dL")
                    st.markdown(f"**HDL:** {hdl_mgdl:.0f} mg/dL")
                    st.markdown(f"**Huyết áp tâm thu:** {sbp} mmHg")
                
                with summary_cols[2]:
                    st.markdown(f"**Điều trị THA:** {'Có' if bp_treated else 'Không'}")
                    st.markdown(f"**Đái tháo đường:** {'Có' if diabetes else 'Không'}")
                    st.markdown(f"**Hút thuốc:** {'Có' if smoker else 'Không'}")
                
                # Export section
                st.markdown("---")
                from components.export import render_export_section
                
                # Prepare inputs for export
                inputs_dict = {
                    "Age": f"{age} tuổi",
                    "Gender": sex,
                    "Race": race,
                    "Total Cholesterol": f"{tc_mgdl:.0f} mg/dL",
                    "HDL": f"{hdl_mgdl:.0f} mg/dL",
                    "Systolic BP": f"{sbp} mmHg",
                    "BP Treatment": "Có" if bp_treated else "Không",
                    "Diabetes": "Có" if diabetes else "Không",
                    "Smoker": "Có" if smoker else "Không"
                }
                
                # Prepare results for export
                results_dict = {
                    "10-Year ASCVD Risk": f"{risk_percent:.1f}%",
                    "Risk Category": category_vn,
                    "Recommendations": "\n".join(result['recommendations'])
                }
                
                render_export_section(
                    title=f"ASCVD Risk = {risk_percent:.1f}%",
                    inputs=inputs_dict,
                    results=results_dict,
                    calculator_name="ASCVD Risk Calculator",
                    filename="ascvd_result"
                )
                
                # Save to history
                save_calculation_to_history(
                    calculator_id="ascvd",
                    calculator_name="ASCVD Risk Calculator",
                    inputs=inputs_dict,
                    results=results_dict
                )
                
                # Share section
                render_share_section(
                    calculator_id="ascvd",
                    calculator_name="ASCVD Risk Calculator",
                    inputs=inputs_dict,
                    results=results_dict,
                    show_qr=True
                )
                
                # History section
                st.markdown("---")
                render_history_ui(calculator_id="ascvd", show_actions=True)
                
                # References section
                references = get_references("ASCVD")
                if references:
                    render_references_section(
                        references=references,
                        title="📚 Tài liệu tham khảo",
                        last_updated="2024-01-15",
                        show_evidence_level=True,
                        show_links=True
                    )
                
                with st.expander("📚 Tham khảo lâm sàng"):
                    st.markdown("""
                    **ASCVD Risk Calculator - Pooled Cohort Equations**
                    
                    **Mục đích:** Ước tính nguy cơ 10 năm mắc bệnh tim mạch do xơ vữa động mạch (ASCVD)
                    - Nhồi máu cơ tim tử vong/không tử vong
                    - Đột quỵ tử vong/không tử vong
                    
                    **Phạm vi áp dụng:**
                    - Tuổi: 40-79 tuổi
                    - Không có tiền sử ASCVD
                    - Không có bệnh lý đặc biệt (HD giai đoạn cuối, suy tim, v.v.)
                    
                    **Phân loại nguy cơ:**
                    - **Thấp (<5%):** Nguy cơ thấp, tập trung phòng ngừa
                    - **Trung bình (5-<7.5%):** Borderline risk, tối ưu hóa lối sống
                    - **Trung bình-Cao (7.5-<20%):** Intermediate risk, cân nhắc statin
                    - **Cao (≥20%):** High risk, chỉ định statin + điều chỉnh lối sống
                    
                    **Hướng dẫn 2019 ACC/AHA Primary Prevention:**
                    - **Risk ≥20%:** Statin therapy (Class I)
                    - **Risk 7.5-<20%:** Cân nhắc statin sau khi thảo luận (Class IIa)
                    - **Risk 5-<7.5%:** Có thể dùng statin nếu có yếu tố nguy cơ bổ sung (Class IIb)
                    - **Risk <5%:** Tập trung điều chỉnh lối sống
                    
                    **Lưu ý:**
                    - Công cụ này KHÔNG áp dụng cho:
                      * Bệnh nhân đã có ASCVD
                      * Tuổi <40 hoặc >79
                      * Bệnh nhân đang chạy thận
                      * Bệnh nhân có suy tim nặng
                    - Đối với các chủng tộc khác (không phải White/African American), 
                      sử dụng hệ số White
                    - Kết quả chỉ là ước tính, cần kết hợp với đánh giá lâm sàng
                    
                    **Tham khảo:**
                    - Goff DC Jr, et al. 2013 ACC/AHA Guideline on the Assessment of 
                      Cardiovascular Risk. Circulation. 2014;129(25 Suppl 2):S49-S73.
                    - Arnett DK, et al. 2019 ACC/AHA Guideline on the Primary Prevention 
                      of Cardiovascular Disease. Circulation. 2019;140(11):e596-e646.
                    
                    **Các yếu tố nguy cơ:**
                    - Đái tháo đường làm tăng nguy cơ đáng kể
                    - Hút thuốc lá là yếu tố nguy cơ lớn, ngừng hút giảm 50% nguy cơ sau 1 năm
                    - HDL <40 mg/dL (nam) hoặc <50 mg/dL (nữ) là nguy cơ
                    - Tăng huyết áp không kiểm soát làm tăng nguy cơ
                    """)
    
    # Always show references at the bottom (even before calculation)
    st.markdown("---")
    references = get_references("ASCVD")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.info("""
    **Bước tiếp theo:**
    - Nếu nguy cơ ≥7.5% → Thảo luận về statin therapy với bệnh nhân
    - Nếu nguy cơ ≥20% → Chỉ định statin therapy
    - Xem xét các yếu tố nguy cơ bổ sung (CAC score, hs-CRP)
    - Điều chỉnh lối sống luôn là nền tảng của phòng ngừa
    """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

