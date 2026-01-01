"""
FINDRISC Calculator (Finnish Diabetes Risk Score)
=================================================

Predicts 10-year risk of developing type 2 diabetes

Reference:
- Lindström J, Tuomilehto J. The diabetes risk score: a practical tool to predict 
  type 2 diabetes risk. Diabetes Care. 2003;26(3):725-731.

FINDRISC Components (8 questions):
1. Age (years)
2. BMI (kg/m²)
3. Waist circumference (cm)
4. Physical activity
5. Daily consumption of vegetables, fruits or berries
6. Use of antihypertensive medication
7. History of high blood glucose
8. Family history of diabetes

Total: 0-26 points

Risk Categories:
- <7 points: Low risk (<1%)
- 7-11 points: Slightly elevated (4%)
- 12-14 points: Moderate (17%)
- 15-20 points: High (33%)
- >20 points: Very high (50%)

Clinical Utility:
- Used daily in primary care and endocrinology
- Screen for diabetes risk
- Guide lifestyle interventions
- Predict diabetes development
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_findrisc(
    age: int,
    bmi: float,
    waist_circumference: float,
    is_male: bool,
    physical_activity: bool,
    daily_vegetables: bool,
    antihypertensive: bool,
    high_glucose_history: bool,
    family_history_diabetes: bool
) -> dict:
    """
    Calculate FINDRISC Score
    
    Args:
        age: Age (years)
        bmi: Body Mass Index (kg/m²)
        waist_circumference: Waist circumference (cm)
        is_male: Male sex
        physical_activity: Regular physical activity (≥30 min/day)
        daily_vegetables: Daily consumption of vegetables/fruits
        antihypertensive: Use of antihypertensive medication
        high_glucose_history: History of high blood glucose
        family_history_diabetes: Family history of diabetes
    
    Returns:
        Dictionary with score and risk interpretation
    """
    score = 0
    details = []
    
    # Age
    if age < 45:
        age_points = 0
    elif age < 54:
        age_points = 2
    elif age < 64:
        age_points = 3
    else:
        age_points = 4
    score += age_points
    details.append(f"Tuổi {age} → +{age_points} điểm")
    
    # BMI
    if bmi < 25:
        bmi_points = 0
    elif bmi < 30:
        bmi_points = 1
    else:
        bmi_points = 3
    score += bmi_points
    details.append(f"BMI {bmi:.1f} kg/m² → +{bmi_points} điểm")
    
    # Waist circumference (different for male/female)
    if is_male:
        if waist_circumference < 94:
            waist_points = 0
        elif waist_circumference < 102:
            waist_points = 3
        else:
            waist_points = 4
    else:  # Female
        if waist_circumference < 80:
            waist_points = 0
        elif waist_circumference < 88:
            waist_points = 3
        else:
            waist_points = 4
    score += waist_points
    details.append(f"Vòng bụng {waist_circumference:.0f} cm ({'Nam' if is_male else 'Nữ'}) → +{waist_points} điểm")
    
    # Physical activity
    if not physical_activity:
        score += 2
        details.append("Không tập thể dục thường xuyên → +2 điểm")
    else:
        details.append("Tập thể dục thường xuyên (≥30 phút/ngày) → 0 điểm")
    
    # Daily vegetables
    if not daily_vegetables:
        score += 1
        details.append("Không ăn rau/quả hàng ngày → +1 điểm")
    else:
        details.append("Ăn rau/quả hàng ngày → 0 điểm")
    
    # Antihypertensive medication
    if antihypertensive:
        score += 2
        details.append("Đang dùng thuốc hạ huyết áp → +2 điểm")
    else:
        details.append("Không dùng thuốc hạ huyết áp → 0 điểm")
    
    # History of high blood glucose
    if high_glucose_history:
        score += 5
        details.append("Tiền sử đường huyết cao → +5 điểm")
    else:
        details.append("Không có tiền sử đường huyết cao → 0 điểm")
    
    # Family history of diabetes
    if family_history_diabetes:
        score += 5
        details.append("Gia đình có người bị đái tháo đường → +5 điểm")
    else:
        details.append("Không có tiền sử gia đình đái tháo đường → 0 điểm")
    
    # Risk stratification
    if score < 7:
        risk_category = "Thấp"
        risk_class = "LOW"
        diabetes_risk = "<1%"
        color = COLORS["success"]
    elif score < 12:
        risk_category = "Hơi tăng"
        risk_class = "SLIGHTLY_ELEVATED"
        diabetes_risk = "4%"
        color = COLORS["info"]
    elif score < 15:
        risk_category = "Trung bình"
        risk_class = "MODERATE"
        diabetes_risk = "17%"
        color = COLORS["warning"]
    elif score <= 20:
        risk_category = "Cao"
        risk_class = "HIGH"
        diabetes_risk = "33%"
        color = COLORS["error"]
    else:
        risk_category = "Rất cao"
        risk_class = "VERY_HIGH"
        diabetes_risk = "50%"
        color = COLORS["error"]
    
    return {
        'total_score': score,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'diabetes_risk': diabetes_risk,
        'color': color,
        'details': details
    }


def render():
    """Render FINDRISC calculator"""
    
    st.markdown(f"<h1 style='text-align: center; color: {COLORS['success']};'>💉 FINDRISC Score</h1>", unsafe_allow_html=True)
    st.markdown("**Dự đoán nguy cơ đái tháo đường type 2 trong 10 năm (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'findrisc':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **FINDRISC (Finnish Diabetes Risk Score)** dự đoán nguy cơ đái tháo đường type 2 trong 10 năm:
        - Dùng hàng ngày trong phòng khám nội tiết và chăm sóc sức khỏe ban đầu
        - 8 câu hỏi đơn giản
        - Điểm từ 0-26
        
        ### 🎯 8 Yếu tố
        
        1. **Tuổi** (0-4 điểm)
        2. **BMI** (0-3 điểm)
        3. **Vòng bụng** (0-4 điểm, khác nhau theo giới tính)
        4. **Tập thể dục** (0-2 điểm)
        5. **Ăn rau/quả hàng ngày** (0-1 điểm)
        6. **Dùng thuốc hạ huyết áp** (0-2 điểm)
        7. **Tiền sử đường huyết cao** (0-5 điểm)
        8. **Gia đình có đái tháo đường** (0-5 điểm)
        
        ### 📊 Phân loại nguy cơ
        
        - **<7 điểm:** Nguy cơ thấp (<1%)
        - **7-11 điểm:** Nguy cơ hơi tăng (4%)
        - **12-14 điểm:** Nguy cơ trung bình (17%)
        - **15-20 điểm:** Nguy cơ cao (33%)
        - **>20 điểm:** Nguy cơ rất cao (50%)
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="findrisc",
            calculator_name="FINDRISC",
            category="Nội tiết",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Cơ bản")
        age = st.number_input("Tuổi", 0, 120, 50, 1, format="%d")
        
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True)
        is_male = (sex == "Nam")
        
        bmi = st.number_input(
            "BMI (kg/m²)",
            15.0, 50.0, 25.0, 0.1,
            format="%.1f",
            help="Body Mass Index"
        )
        
        waist_circumference = st.number_input(
            "Vòng bụng (cm)",
            50.0, 200.0, 90.0, 1.0,
            format="%.0f",
            help="Đo ở mức rốn"
        )
    
    with col2:
        st.markdown("#### 🏃 Lối sống & Sức khỏe")
        physical_activity = st.checkbox(
            "**Tập thể dục thường xuyên** (≥30 phút/ngày)",
            help="Tập thể dục ít nhất 30 phút mỗi ngày"
        )
        
        daily_vegetables = st.checkbox(
            "**Ăn rau/quả hàng ngày**",
            help="Ăn rau, quả hoặc quả mọng hàng ngày"
        )
        
        antihypertensive = st.checkbox(
            "**Đang dùng thuốc hạ huyết áp**",
            help="Đang dùng thuốc điều trị tăng huyết áp"
        )
        
        high_glucose_history = st.checkbox(
            "**Tiền sử đường huyết cao**",
            help="Đã từng được chẩn đoán đường huyết cao hoặc đái tháo đường thai kỳ"
        )
        
        family_history_diabetes = st.checkbox(
            "**Gia đình có người bị đái tháo đường**",
            help="Bố, mẹ, anh/chị/em ruột bị đái tháo đường"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính FINDRISC Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_age, age_error = validate_age(age, 0, 120)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}")
        
        is_valid_bmi, bmi_error = validate_lab_value(bmi, "BMI", 15.0, 50.0)
        if not is_valid_bmi:
            validation_errors.append(f"BMI: {bmi_error}")
        
        is_valid_waist, waist_error = validate_lab_value(waist_circumference, "Vòng bụng", 50.0, 200.0)
        if not is_valid_waist:
            validation_errors.append(f"Vòng bụng: {waist_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_findrisc(
            age=age,
            bmi=bmi,
            waist_circumference=waist_circumference,
            is_male=is_male,
            physical_activity=physical_activity,
            daily_vegetables=daily_vegetables,
            antihypertensive=antihypertensive,
            high_glucose_history=high_glucose_history,
            family_history_diabetes=family_history_diabetes
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**FINDRISC Score**",
                f"{result['total_score']}/26"
            )
        
        with col_r2:
            st.markdown(f"### {result['risk_category'].upper()}")
            st.caption(f"Nguy cơ đái tháo đường 10 năm: {result['diabetes_risk']}")
        
        # Score breakdown
        with st.expander("📋 Chi tiết điểm số", expanded=True):
            for detail in result['details']:
                st.markdown(f"- {detail}")
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['risk_class'] == "LOW":
            st.success(f"""
            **✅ Nguy cơ THẤP ({result['diabetes_risk']}):**
            
            **Khuyến cáo:**
            - Duy trì lối sống lành mạnh
            - Tập thể dục thường xuyên
            - Chế độ ăn cân bằng
            - Kiểm tra lại sau 3-5 năm
            """)
        elif result['risk_class'] == "SLIGHTLY_ELEVATED":
            st.info(f"""
            **ℹ️ Nguy cơ HƠI TĂNG ({result['diabetes_risk']}):**
            
            **Khuyến cáo:**
            - Thay đổi lối sống tích cực
            - Giảm cân nếu thừa cân
            - Tập thể dục thường xuyên
            - Chế độ ăn lành mạnh
            - Kiểm tra lại sau 1-2 năm
            """)
        elif result['risk_class'] == "MODERATE":
            st.warning(f"""
            **⚠️ Nguy cơ TRUNG BÌNH ({result['diabetes_risk']}):**
            
            **Khuyến cáo:**
            - **Thay đổi lối sống tích cực**
            - Giảm cân (mục tiêu 5-7% trọng lượng)
            - Tập thể dục ≥150 phút/tuần
            - Chế độ ăn ít carbohydrate
            - Xem xét xét nghiệm đường huyết (HbA1c, OGTT)
            - Kiểm tra lại sau 6-12 tháng
            """)
        elif result['risk_class'] == "HIGH":
            st.error(f"""
            **🚨 Nguy cơ CAO ({result['diabetes_risk']}):**
            
            **Khuyến cáo:**
            - **Thay đổi lối sống MẠNH MẼ**
            - Giảm cân tích cực (mục tiêu 7-10% trọng lượng)
            - Tập thể dục ≥150 phút/tuần
            - Chế độ ăn ít carbohydrate, Địa Trung Hải
            - **Xét nghiệm đường huyết NGAY** (HbA1c, OGTT)
            - Xem xét metformin để phòng ngừa
            - Theo dõi sát (3-6 tháng)
            """)
        else:  # VERY_HIGH
            st.error(f"""
            **🚨🚨 Nguy cơ RẤT CAO ({result['diabetes_risk']}):**
            
            **Khuyến cáo:**
            - **Thay đổi lối sống KHẨN CẤP**
            - Giảm cân tích cực (mục tiêu 10-15% trọng lượng)
            - Tập thể dục ≥150 phút/tuần
            - Chế độ ăn ít carbohydrate, Địa Trung Hải
            - **Xét nghiệm đường huyết NGAY** (HbA1c, OGTT, FPG)
            - **Cân nhắc metformin** để phòng ngừa
            - Hội chẩn nội tiết
            - Theo dõi sát (3 tháng)
            """)
        
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - FINDRISC chỉ dự đoán nguy cơ, không chẩn đoán đái tháo đường
        - Cần xét nghiệm đường huyết để chẩn đoán chính xác
        - Thay đổi lối sống là biện pháp quan trọng nhất
        - Metformin có thể được xem xét để phòng ngừa ở nguy cơ cao
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Gender": sex,
            "BMI": f"{bmi:.1f} kg/m²",
            "Waist Circumference": f"{waist_circumference:.0f} cm",
            "Physical Activity": "Có" if physical_activity else "Không",
            "Daily Vegetables": "Có" if daily_vegetables else "Không",
            "Antihypertensive": "Có" if antihypertensive else "Không",
            "High Glucose History": "Có" if high_glucose_history else "Không",
            "Family History Diabetes": "Có" if family_history_diabetes else "Không"
        }
        
        results_dict = {
            "FINDRISC Score": f"{result['total_score']}/26",
            "Risk Category": result['risk_category'],
            "10-Year Diabetes Risk": result['diabetes_risk'],
            "Risk Class": result['risk_class']
        }
        
        # Export section
        render_export_section(
            title="FINDRISC Score",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="FINDRISC"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="findrisc",
            calculator_name="FINDRISC",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="findrisc",
            calculator_name="FINDRISC",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="findrisc", show_actions=True)
        
        # References section
        references = get_references("FINDRISC")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['findrisc_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("FINDRISC")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    else:
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            **FINDRISC (Finnish Diabetes Risk Score)**
            
            **Reference:**
            Lindström J, Tuomilehto J. The diabetes risk score: a practical tool to predict 
            type 2 diabetes risk. Diabetes Care. 2003;26(3):725-731.
            
            **8 Factors:**
            1. Age (0-4 points)
            2. BMI (0-3 points)
            3. Waist circumference (0-4 points, gender-specific)
            4. Physical activity (0-2 points)
            5. Daily vegetables (0-1 points)
            6. Antihypertensive medication (0-2 points)
            7. History of high blood glucose (0-5 points)
            8. Family history of diabetes (0-5 points)
            
            **Total: 0-26 points**
            
            **10-Year Diabetes Risk:**
            - <7: <1% (Low)
            - 7-11: 4% (Slightly elevated)
            - 12-14: 17% (Moderate)
            - 15-20: 33% (High)
            - >20: 50% (Very high)
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

