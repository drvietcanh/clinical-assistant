"""
sPESI (Simplified PESI) Calculator
====================================

Simplified version of PESI for pulmonary embolism risk assessment

Reference:
- Jiménez D, et al. Simplification of the pulmonary embolism severity index 
  for prognostication in patients with acute symptomatic pulmonary embolism. 
  Arch Intern Med. 2010;170(15):1383-1389.

sPESI Components (6 factors):
- Age >80 years
- History of cancer
- History of chronic cardiopulmonary disease
- Heart rate ≥110 bpm
- Systolic BP <100 mmHg
- Arterial oxyhemoglobin saturation <90%

Any positive = High risk

Clinical Utility:
- Simplified version of PESI
- Quick risk assessment for PE
- Guide treatment decisions (outpatient vs inpatient)
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_blood_pressure, validate_heart_rate
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_spesi(
    age: float,
    cancer: bool,
    cardiopulmonary_disease: bool,
    heart_rate: int,
    sbp: float,
    spo2: float
) -> dict:
    """
    Calculate sPESI
    
    Args:
        age: Age in years
        cancer: History of cancer
        cardiopulmonary_disease: History of chronic cardiopulmonary disease
        heart_rate: Heart rate (bpm)
        sbp: Systolic blood pressure (mmHg)
        spo2: Arterial oxyhemoglobin saturation (%)
    
    Returns:
        Dictionary with risk assessment
    """
    risk_factors = []
    details = []
    
    # Age >80
    if age > 80:
        risk_factors.append("Tuổi >80")
        details.append(f"✅ Tuổi {age:.0f} (>80) → Yếu tố nguy cơ")
    else:
        details.append(f"❌ Tuổi {age:.0f} (≤80)")
    
    # Cancer
    if cancer:
        risk_factors.append("Tiền sử ung thư")
        details.append("✅ Tiền sử ung thư → Yếu tố nguy cơ")
    else:
        details.append("❌ Không có tiền sử ung thư")
    
    # Cardiopulmonary disease
    if cardiopulmonary_disease:
        risk_factors.append("Bệnh tim phổi mạn")
        details.append("✅ Bệnh tim phổi mạn → Yếu tố nguy cơ")
    else:
        details.append("❌ Không có bệnh tim phổi mạn")
    
    # Heart rate ≥110
    if heart_rate >= 110:
        risk_factors.append("Nhịp tim ≥110 bpm")
        details.append(f"✅ Nhịp tim {heart_rate} bpm (≥110) → Yếu tố nguy cơ")
    else:
        details.append(f"❌ Nhịp tim {heart_rate} bpm (<110)")
    
    # SBP <100
    if sbp < 100:
        risk_factors.append("Huyết áp tâm thu <100 mmHg")
        details.append(f"✅ SBP {sbp:.0f} mmHg (<100) → Yếu tố nguy cơ")
    else:
        details.append(f"❌ SBP {sbp:.0f} mmHg (≥100)")
    
    # SpO2 <90%
    if spo2 < 90:
        risk_factors.append("SpO2 <90%")
        details.append(f"✅ SpO2 {spo2:.0f}% (<90) → Yếu tố nguy cơ")
    else:
        details.append(f"❌ SpO2 {spo2:.0f}% (≥90)")
    
    # Risk assessment
    if len(risk_factors) > 0:
        risk_category = "Cao"
        risk_class = "HIGH"
        mortality_30d = "8.9-11.4%"
        interpretation = "Nguy cơ cao - Cần nhập viện"
        color = COLORS["error"]
        recommendation = "Khuyến cáo nhập viện để điều trị và theo dõi"
    else:
        risk_category = "Thấp"
        risk_class = "LOW"
        mortality_30d = "1.0-1.1%"
        interpretation = "Nguy cơ thấp - Có thể điều trị ngoại trú"
        color = COLORS["success"]
        recommendation = "Có thể cân nhắc điều trị ngoại trú với thuốc kháng đông"
    
    return {
        'risk_factors': risk_factors,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'mortality_30d': mortality_30d,
        'interpretation': interpretation,
        'recommendation': recommendation,
        'color': color,
        'details': details
    }


def render():
    """Render sPESI calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🫁 sPESI - Simplified PESI</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá nguy cơ tử vong 30 ngày ở bệnh nhân thuyên tắc phổi**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'spesi':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **sPESI (Simplified PESI)** đánh giá nguy cơ tử vong 30 ngày ở bệnh nhân PE:
        - Phiên bản đơn giản của PESI (6 yếu tố vs 11 yếu tố)
        - Hướng dẫn quyết định điều trị ngoại trú vs nội trú
        - Dễ sử dụng hơn PESI đầy đủ
        
        ### 🎯 Yếu tố nguy cơ (6 yếu tố)
        
        **Bất kỳ yếu tố nào dương tính = Nguy cơ cao**
        
        1. **Tuổi >80**
        
        2. **Tiền sử ung thư**
        
        3. **Bệnh tim phổi mạn**
           - Suy tim, COPD, bệnh phổi mạn tính
        
        4. **Nhịp tim ≥110 bpm**
        
        5. **Huyết áp tâm thu <100 mmHg**
        
        6. **SpO2 <90%**
        
        ### 📊 Phân loại
        
        | Kết quả | Nguy cơ | Tử vong 30 ngày | Khuyến nghị |
        |---------|---------|-----------------|-------------|
        | Có ≥1 yếu tố | Cao | 8.9-11.4% | Nhập viện |
        | Không có yếu tố | Thấp | 1.0-1.1% | Có thể ngoại trú |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân đã chẩn đoán PE
        - Đơn giản hơn PESI đầy đủ
        - Hướng dẫn quyết định điều trị
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="spesi",
            calculator_name="sPESI",
            category="Hô hấp",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Tiền sử")
        age = st.number_input(
            "Tuổi (năm)",
            18, 120, 65, 1,
            format="%d",
            help="Tuổi bệnh nhân"
        )
        
        cancer = st.checkbox(
            "Tiền sử ung thư",
            help="Tiền sử ung thư đang hoạt động hoặc đã điều trị"
        )
        
        cardiopulmonary_disease = st.checkbox(
            "Bệnh tim phổi mạn",
            help="Suy tim, COPD, hoặc bệnh phổi mạn tính khác"
        )
    
    with col2:
        st.markdown("#### 🩺 Sinh hiệu")
        heart_rate = st.number_input(
            "Nhịp tim (bpm)",
            40, 200, 80, 1,
            format="%d",
            help="Nhịp tim"
        )
        
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            50.0, 200.0, 120.0, 1.0,
            format="%.0f",
            help="Huyết áp tâm thu"
        )
        
        spo2 = st.number_input(
            "SpO2 (%)",
            50.0, 100.0, 95.0, 1.0,
            format="%.0f",
            help="Độ bão hòa oxy máu động mạch"
        )
        
        if age > 80:
            st.info("ℹ️ Tuổi >80")
        if heart_rate >= 110:
            st.warning("⚠️ Nhịp tim ≥110 bpm")
        if sbp < 100:
            st.warning("⚠️ Huyết áp tâm thu <100 mmHg")
        if spo2 < 90:
            st.warning("⚠️ SpO2 <90%")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính sPESI", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        if age < 18 or age > 120:
            validation_errors.append("Tuổi phải trong khoảng 18-120")
        
        is_valid_hr, hr_error = validate_heart_rate(heart_rate)
        if not is_valid_hr:
            validation_errors.append(f"Nhịp tim: {hr_error}")
        
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(f"Huyết áp tâm thu: {sbp_error}")
        
        if spo2 < 50 or spo2 > 100:
            validation_errors.append("SpO2 phải trong khoảng 50-100%")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_spesi(
            age=age,
            cancer=cancer,
            cardiopulmonary_disease=cardiopulmonary_disease,
            heart_rate=heart_rate,
            sbp=sbp,
            spo2=spo2
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "HIGH": "🚨",
            "LOW": "✅"
        }
        icon = icon_map.get(result['risk_class'], "🫁")
        
        render_score_result(
            title="sPESI",
            score=f"{len(result['risk_factors'])}/6",
            interpretation=f"{result['interpretation']} - Tử vong 30 ngày: {result['mortality_30d']}",
            mortality=result['mortality_30d'],
            color=result['color'],
            icon=icon,
            show_mortality=True
        )
        
        # Details
        with st.expander("📋 Chi tiết đánh giá", expanded=False):
            st.markdown("### Các tiêu chí:")
            for detail in result['details']:
                st.markdown(f"- {detail}")
            
            if result['risk_factors']:
                st.markdown("### ⚠️ Yếu tố nguy cơ phát hiện:")
                for factor in result['risk_factors']:
                    st.markdown(f"- **{factor}**")
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "HIGH":
            st.error(f"""
            **Nguy cơ cao** - Phát hiện **{len(result['risk_factors'])}** yếu tố nguy cơ
            
            - **Tử vong 30 ngày:** {result['mortality_30d']}
            - **Khuyến nghị:** {result['recommendation']}
            - Cần nhập viện để điều trị và theo dõi
            - Điều trị kháng đông và hỗ trợ
            """)
        else:
            st.success(f"""
            **Nguy cơ thấp** - Không phát hiện yếu tố nguy cơ
            
            - **Tử vong 30 ngày:** {result['mortality_30d']}
            - **Khuyến nghị:** {result['recommendation']}
            - Có thể cân nhắc điều trị ngoại trú với thuốc kháng đông
            - Theo dõi sát và hướng dẫn quay lại nếu triệu chứng xấu đi
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - sPESI giúp đánh giá nguy cơ tử vong 30 ngày ở bệnh nhân PE
        - **Nguy cơ cao:** Nhập viện để điều trị và theo dõi
        - **Nguy cơ thấp:** Có thể cân nhắc điều trị ngoại trú với thuốc kháng đông
        - Kết hợp với đánh giá lâm sàng và các yếu tố khác
        - Điều trị kháng đông phù hợp cho tất cả bệnh nhân PE
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'spesi',
            'calculator_name': 'sPESI - Simplified PESI',
            'inputs': {
                'age': age,
                'cancer': cancer,
                'cardiopulmonary_disease': cardiopulmonary_disease,
                'heart_rate': heart_rate,
                'sbp': sbp,
                'spo2': spo2
            },
            'results': {
                'risk_factors_count': len(result['risk_factors']),
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class'],
                'mortality_30d': result['mortality_30d'],
                'interpretation': result['interpretation']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('spesi')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Jiménez D, et al. Simplification of the pulmonary embolism severity index 
          for prognostication in patients with acute symptomatic pulmonary embolism. 
          Arch Intern Med. 2010;170(15):1383-1389.
        """)
    
    # History
    render_history_ui(calculator_id="spesi", show_actions=True)
