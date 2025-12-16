"""
SCORE2 Calculator
==================

10-year cardiovascular disease risk prediction (Ages 40-69)

Reference:
- SCORE2 working group and ESC Cardiovascular risk collaboration. 
  SCORE2 risk prediction algorithms: new models to estimate 10-year risk of
  cardiovascular disease in Europe. Eur Heart J. 2021;42(25):2439-2454.

SCORE2 predicts 10-year risk of:
- Fatal and non-fatal myocardial infarction
- Fatal and non-fatal stroke

Risk Factors:
- Age (40-69 years)
- Sex
- Smoking status
- Systolic blood pressure
- Non-HDL cholesterol (or Total cholesterol)

Risk Regions:
- Low risk: e.g., France, Belgium, Spain
- Moderate risk: e.g., Poland, Germany, Austria, UK  
- High risk: e.g., Romania, Bulgaria, Russia
- Very high risk: e.g., Some Eastern European countries

Note: This is a simplified calculator. For precise calculation, use official ESC tools.
Vietnam is typically considered MODERATE to HIGH risk region.
"""

import streamlit as st
import math
from scores.utils.validation import (
    validate_age,
    validate_blood_pressure,
    validate_lab_value
)
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_score2_moderate_risk(
    age: int,
    is_female: bool,
    is_smoker: bool,
    sbp: float,
    total_chol: float,
    hdl_chol: float = None
) -> dict:
    """
    Calculate SCORE2 for MODERATE risk regions
    
    This is a simplified calculation. Official SCORE2 uses complex lookup tables.
    
    Args:
        age: Age (40-69 years)
        is_female: Female sex
        is_smoker: Current smoker
        sbp: Systolic blood pressure (mmHg)
        total_chol: Total cholesterol (mmol/L)
        hdl_chol: HDL cholesterol (mmol/L) - optional
    
    Returns:
        Dictionary with risk percentage and category
    """
    
    # Calculate non-HDL cholesterol
    if hdl_chol is not None:
        non_hdl = total_chol - hdl_chol
    else:
        # Estimate if HDL not available (assume average HDL ~1.3 mmol/L)
        non_hdl = total_chol - 1.3
    
    # Simplified risk estimation based on SCORE2 moderate risk region
    # This is an approximation - actual SCORE2 uses complex tables
    
    # Base risk increases exponentially with age
    age_factor = math.exp((age - 40) * 0.1)
    
    # Sex factor (women have lower risk at same age)
    sex_factor = 0.6 if is_female else 1.0
    
    # Smoking approximately doubles risk
    smoking_factor = 2.0 if is_smoker else 1.0
    
    # SBP contribution (risk increases ~30% per 20 mmHg above 120)
    sbp_factor = 1.0 + ((sbp - 120) / 20) * 0.3 if sbp > 120 else 1.0
    
    # Non-HDL cholesterol contribution (risk increases ~15% per mmol/L above 2.6)
    chol_factor = 1.0 + ((non_hdl - 2.6) / 1) * 0.15 if non_hdl > 2.6 else 0.8
    
    # Baseline 10-year risk for moderate risk region
    baseline_risk = 2.0  # 2% baseline
    
    # Calculate total risk
    risk_10yr = baseline_risk * age_factor * sex_factor * smoking_factor * sbp_factor * chol_factor
    
    # Cap at reasonable maximum
    risk_10yr = min(risk_10yr, 50.0)
    
    # Risk categories based on ESC 2021 guidelines
    if risk_10yr < 2.5:
        risk_category = "Nguy cơ THẤP"
        risk_class = "LOW"
        color = "🟢"
        recommendation = """
        **🟢 Nguy cơ tim mạch THẤP (<2.5%):**
        
        **Khuyến cáo:**
        - Duy trì lối sống lành mạnh
        - Không cần thuốc statin thường quy
        - Theo dõi định kỳ mỗi 5 năm
        - Tư vấn về chế độ ăn Địa Trung Hải
        - Tập thể dục thường xuyên (150 phút/tuần)
        """
    elif risk_10yr < 7.5:
        risk_category = "Nguy cơ TRUNG BÌNH"
        risk_class = "MODERATE"
        color = "🟡"
        recommendation = """
        **🟡 Nguy cơ tim mạch TRUNG BÌNH (2.5-7.5%):**
        
        **Khuyến cáo:**
        - Thay đổi lối sống tích cực
        - Xem xét statin nếu:
          * LDL-C >3.0 mmol/L (116 mg/dL)
          * Có yếu tố nguy cơ khác
          * Risk enhancers (CAC score, gia đình, etc.)
        - Kiểm soát huyết áp mục tiêu <140/90 mmHg
        - Bỏ thuốc lá (nếu hút)
        - Theo dõi mỗi 2-3 năm
        
        **Mục tiêu:**
        - LDL-C <3.0 mmol/L (116 mg/dL)
        - Non-HDL-C <3.8 mmol/L
        """
    elif risk_10yr < 10:
        risk_category = "Nguy cơ CAO"
        risk_class = "HIGH"
        color = "🟠"
        recommendation = """
        **🟠 Nguy cơ tim mạch CAO (7.5-10%):**
        
        **Khuyến cáo:**
        - **STATIN khuyến cáo** (moderate-high intensity)
        - **Kiểm soát huyết áp** mục tiêu <130/80 mmHg
        - **Bỏ thuốc lá** bắt buộc
        - Xem xét thêm ezetimibe nếu không đạt mục tiêu
        - Aspirin 75-100 mg nếu có chỉ định
        - Theo dõi mỗi 6-12 tháng
        
        **Mục tiêu điều trị:**
        - **LDL-C <1.8 mmol/L (70 mg/dL)** VÀ giảm ≥50%
        - Non-HDL-C <2.6 mmol/L
        - BP <130/80 mmHg
        
        **Thuốc:**
        - Atorvastatin 20-40 mg hoặc Rosuvastatin 10-20 mg
        """
    else:
        risk_category = "Nguy cơ RẤT CAO"
        risk_class = "VERY_HIGH"
        color = "🔴"
        recommendation = """
        **🔴 Nguy cơ tim mạch RẤT CAO (≥10%):**
        
        **Khuyến cáo:**
        - **HIGH-INTENSITY STATIN bắt buộc**
        - **Kiểm soát huyết áp chặt** <130/80 mmHg
        - **Bỏ thuốc lá ngay**
        - Thêm ezetimibe nếu chưa đạt mục tiêu
        - Xem xét PCSK9 inhibitor nếu LDL vẫn cao
        - Aspirin 75-100 mg (xem xét rủi ro/lợi ích)
        - Theo dõi mỗi 3-6 tháng
        
        **Mục tiêu điều trị TÍCH CỰC:**
        - **LDL-C <1.4 mmol/L (55 mg/dL)** VÀ giảm ≥50%
        - Non-HDL-C <2.2 mmol/L
        - BP <130/80 mmHg
        - HbA1c <7% (nếu DM)
        
        **Thuốc:**
        - Atorvastatin 40-80 mg hoặc Rosuvastatin 20-40 mg
        - + Ezetimibe 10 mg
        - ± PCSK9i nếu cần
        """
    
    return {
        'risk_10yr': risk_10yr,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'color': color,
        'recommendation': recommendation,
        'non_hdl': non_hdl
    }


def render():
    """Render SCORE2 calculator"""
    
    st.title("📊 SCORE2 - ESC 2021")
    st.markdown("**Đánh giá nguy cơ bệnh tim mạch 10 năm (40-69 tuổi)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'score2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **SCORE2** là thang điểm ESC 2021 mới nhất:
        - Thay thế SCORE cũ
        - Dự đoán nguy cơ 10 năm mắc CVD (fatal + non-fatal)
        - Bao gồm: Nhồi máu cơ tim, Đột quỵ
        - Dành cho người 40-69 tuổi KHÔNG có CVD
        
        ### 🎯 Yếu tố nguy cơ
        
        1. **Tuổi:** 40-69
        2. **Giới tính:** Nam/Nữ
        3. **Hút thuốc lá:** Có/Không
        4. **Huyết áp tâm thu (SBP)**
        5. **Cholesterol:** Total và HDL (để tính non-HDL)
        
        ### 🌍 Vùng Địa Lý
        
        SCORE2 có 4 calibrations theo vùng:
        - **Low risk:** Pháp, Bỉ, Tây Ban Nha
        - **Moderate risk:** Đức, Anh, Ba Lan *(Việt Nam)*
        - **High risk:** Nga, Bulgaria, Romania
        - **Very high risk:** Một số nước Đông Âu
        
        **Việt Nam:** Được coi là **MODERATE to HIGH risk**
        
        ### 📊 Phân loại nguy cơ
        
        | Nguy cơ 10 năm | Phân loại |
        |----------------|-----------|
        | <2.5% | Thấp |
        | 2.5-7.5% | Trung bình |
        | 7.5-10% | Cao |
        | ≥10% | Rất cao |
        
        ### ⚠️ Lưu ý
        
        - **CHỈ dùng** cho người 40-69 tuổi, KHÔNG có CVD
        - **KHÔNG dùng** nếu có: CAD, stroke, PAD, DM type 1, DM type 2 >10 năm
        - **Risk enhancers** làm tăng nguy cơ: Family history, CAC score, CKD, etc.
        
        ### 📚 Tham khảo
        
        - SCORE2 working group. *Eur Heart J* 2021;42:2439-2454
        - ESC Guidelines 2021 on CVD prevention
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="score2",
            calculator_name="SCORE2",
            category="Tim Mạch",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Thông tin Cá Nhân")
        age = st.number_input("Tuổi", 40, 69, 50, 1, format="%d", help="SCORE2 chỉ dành cho 40-69 tuổi")
        
        sex = st.radio("Giới tính", ["Nam", "Nữ"], horizontal=True)
        is_female = (sex == "Nữ")
        
        is_smoker = st.checkbox("**Đang hút thuốc lá**", help="Hút thuốc hiện tại hoặc bỏ trong <1 năm")
    
    with col2:
        st.markdown("#### 🩺 Sinh hiệu")
        sbp = st.number_input(
            "Huyết áp tâm thu (SBP) mmHg",
            80.0, 220.0, 120.0, 1.0,
            format="%.0f",
            help="Lấy trung bình nhiều lần đo"
        )
    
    st.divider()
    
    # Cholesterol
    st.markdown("#### 🔬 Cholesterol")
    
    chol_unit = st.radio(
        "Đơn vị cholesterol",
        ["mmol/L", "mg/dL"],
        horizontal=True,
        index=0,
        help="mmol/L (đơn vị quốc tế) hoặc mg/dL (đơn vị Mỹ)"
    )
    
    col3, col4 = st.columns(2)
    
    with col3:
        if chol_unit == "mmol/L":
            total_chol_input = st.number_input(
                "Total Cholesterol (mmol/L)",
                2.0, 15.0, 5.0, 0.1,
                format="%.1f"
            )
            total_chol = total_chol_input
        else:
            total_chol_input = st.number_input(
                "Total Cholesterol (mg/dL)",
                80.0, 600.0, 200.0, 1.0,
                format="%.0f"
            )
            total_chol = total_chol_input / 38.67  # Convert to mmol/L
        
        st.caption(f"💡 Chuyển đổi: {total_chol:.1f} mmol/L = {total_chol * 38.67:.0f} mg/dL")
    
    with col4:
        if chol_unit == "mmol/L":
            hdl_chol_input = st.number_input(
                "HDL Cholesterol (mmol/L)",
                0.5, 4.0, 1.3, 0.1,
                format="%.1f",
                help="Nếu không có, sẽ ước tính"
            )
            hdl_chol = hdl_chol_input
        else:
            hdl_chol_input = st.number_input(
                "HDL Cholesterol (mg/dL)",
                20.0, 150.0, 50.0, 1.0,
                format="%.0f",
                help="Nếu không có, sẽ ước tính"
            )
            hdl_chol = hdl_chol_input / 38.67  # Convert to mmol/L
        
        st.caption(f"💡 Chuyển đổi: {hdl_chol:.1f} mmol/L = {hdl_chol * 38.67:.0f} mg/dL")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Nguy cơ SCORE2", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        # Age validation (40-69 for SCORE2)
        is_valid_age, age_error = validate_age(age, 40, 69)
        if not is_valid_age:
            validation_errors.append(f"Tuổi: {age_error}. SCORE2 chỉ áp dụng cho độ tuổi 40-69. Xem xét dùng SCORE2-OP nếu ≥70 tuổi.")
        
        # SBP validation
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(f"Huyết áp tâm thu: {sbp_error}")
        
        # Cholesterol validation (depends on unit)
        if chol_unit == "mmol/L":
            is_valid_tc, tc_error = validate_lab_value(total_chol_input, "Total Cholesterol", 2.0, 15.0)
            if not is_valid_tc:
                validation_errors.append(f"Total Cholesterol (mmol/L): {tc_error}")
            
            is_valid_hdl, hdl_error = validate_lab_value(hdl_chol_input, "HDL Cholesterol", 0.5, 4.0)
            if not is_valid_hdl:
                validation_errors.append(f"HDL Cholesterol (mmol/L): {hdl_error}")
        else:  # mg/dL
            is_valid_tc, tc_error = validate_lab_value(total_chol_input, "Total Cholesterol", 80.0, 600.0)
            if not is_valid_tc:
                validation_errors.append(f"Total Cholesterol (mg/dL): {tc_error}")
            
            is_valid_hdl, hdl_error = validate_lab_value(hdl_chol_input, "HDL Cholesterol", 20.0, 150.0)
            if not is_valid_hdl:
                validation_errors.append(f"HDL Cholesterol (mg/dL): {hdl_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_score2_moderate_risk(
            age=age,
            is_female=is_female,
            is_smoker=is_smoker,
            sbp=sbp,
            total_chol=total_chol,
            hdl_chol=hdl_chol
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**Nguy cơ 10 Năm**",
                f"{result['risk_10yr']:.1f}%"
            )
            st.caption("Mắc CVD trong 10 năm")
        
        with col_r2:
            st.markdown(f"### {result['color']} {result['risk_category']}")
            st.caption("MI tử vong/không tử vong + Đột quỵ tử vong/không tử vong")
        
        # Risk factors summary
        with st.expander("📋 Tóm tắt yếu tố nguy cơ", expanded=True):
            factors = []
            factors.append(f"- Tuổi: {age} tuổi")
            factors.append(f"- Giới tính: {sex}")
            factors.append(f"- Hút thuốc: {'Có' if is_smoker else 'Không'}")
            factors.append(f"- SBP: {sbp:.0f} mmHg")
            factors.append(f"- Total cholesterol: {total_chol:.1f} mmol/L ({total_chol * 38.67:.0f} mg/dL)")
            factors.append(f"- HDL cholesterol: {hdl_chol:.1f} mmol/L ({hdl_chol * 38.67:.0f} mg/dL)")
            factors.append(f"- **Non-HDL cholesterol: {result['non_hdl']:.1f} mmol/L ({result['non_hdl'] * 38.67:.0f} mg/dL)**")
            
            for factor in factors:
                st.markdown(factor)
        
        # Recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến cáo điều trị")
        st.markdown(result['recommendation'])
        
        # Additional info
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - SCORE2 là công cụ HỖ TRỢ, không thay thế đánh giá lâm sàng
        - Quyết định điều trị cần cân nhắc:
          * Risk enhancers (CAC score, family history, CKD, etc.)
          * Tuổi thọ dự kiến
          * Sở thích bệnh nhân
          * Chi phí/lợi ích thuốc
        
        - **Risk enhancers** làm tăng nguy cơ:
          * Family history (CVD sớm ở họ hàng thế hệ 1)
          * CKD (eGFR <60)
          * CAC score >100
          * LDL-C ≥4.9 mmol/L (190 mg/dL)
          * Metabolic syndrome
          * Inflammatory disease (RA, psoriasis, HIV)
        """)
        
        if result['risk_class'] in ['HIGH', 'VERY_HIGH']:
            st.error("""
            **🚨 NGUY CƠ CAO/RẤT CAO:**
            
            - Cần can thiệp điều trị TÍCH CỰC
            - Statin liều cao + ezetimibe
            - Kiểm soát huyết áp chặt chẽ
            - Bỏ thuốc lá ngay lập tức
            - Tập thể dục thường xuyên
            - Theo dõi sát
            """)
        
        st.warning("""
        ⚠️ **Cảnh báo:**
        - Đây là bản ĐƠNGIẢN HÓA của SCORE2
        - Để tính chính xác, sử dụng công cụ chính thức của ESC
        - Không dùng cho người đã có CVD, DM type 1, DM type 2 >10 năm
        - Quyết định điều trị cuối cùng thuộc về bác sĩ
        """)
        
        # Prepare inputs and results for Phase 1
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Gender": sex,
            "Smoker": "Có" if is_smoker else "Không",
            "SBP": f"{sbp:.0f} mmHg",
            "Total Cholesterol": f"{total_chol:.1f} mmol/L ({total_chol * 38.67:.0f} mg/dL)",
            "HDL Cholesterol": f"{hdl_chol:.1f} mmol/L ({hdl_chol * 38.67:.0f} mg/dL)",
            "Non-HDL Cholesterol": f"{result['non_hdl']:.1f} mmol/L ({result['non_hdl'] * 38.67:.0f} mg/dL)"
        }
        
        results_dict = {
            "10-Year Risk": f"{result['risk_10yr']:.1f}%",
            "Risk Category": result['risk_category'],
            "Risk Class": result['risk_class'],
            "Recommendations": result['recommendation']
        }
        
        # Export section
        render_export_section(
            calculator_id="score2",
            calculator_name="SCORE2",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="score2",
            calculator_name="SCORE2",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="score2",
            calculator_name="SCORE2",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="score2", show_actions=True)
        
        # References section
        references = get_references("SCORE2")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['score2_result'] = result
    
    # Quick reference
    with st.expander("📖 Mục tiêu điều trị theo nguy cơ"):
        st.markdown("""
        ### Mục tiêu LDL-C theo ESC 2021
        
        | Phân loại nguy cơ | LDL-C mục tiêu | Non-HDL-C mục tiêu |
        |-------------------|----------------|---------------------|
        | **Thấp** | <3.0 mmol/L (116 mg/dL) | <3.8 mmol/L (147 mg/dL) |
        | **Trung bình** | <3.0 mmol/L (116 mg/dL) | <3.8 mmol/L (147 mg/dL) |
        | **Cao** | <1.8 mmol/L (70 mg/dL) + ↓≥50% | <2.6 mmol/L (100 mg/dL) |
        | **Rất cao** | <1.4 mmol/L (55 mg/dL) + ↓≥50% | <2.2 mmol/L (85 mg/dL) |
        
        ### Liều statin khuyến cáo
        
        **High-intensity:**
        - Atorvastatin 40-80 mg
        - Rosuvastatin 20-40 mg
        
        **Moderate-intensity:**
        - Atorvastatin 10-20 mg
        - Rosuvastatin 5-10 mg
        - Simvastatin 20-40 mg
        
        **Add-on therapy:**
        - Ezetimibe 10 mg (giảm thêm 15-20%)
        - PCSK9 inhibitors (giảm thêm 50-60%)
        """)
    
    # Always show references at the bottom (even before calculation)
    st.markdown("---")
    references = get_references("SCORE2")
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
