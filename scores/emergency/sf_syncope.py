"""
San Francisco Syncope Rule Calculator
======================================

Assesses risk of serious adverse events after syncope

Reference:
- Quinn JV, et al. Derivation of the San Francisco Syncope Rule to predict patients 
  with short-term serious outcomes. Ann Emerg Med. 2004;43(2):224-232.

San Francisco Syncope Rule Components (5 criteria):
- History of congestive heart failure
- Hematocrit <30%
- Abnormal ECG
- Shortness of breath
- Systolic BP <90 mmHg

Any positive = High risk

Clinical Utility:
- Identify low-risk syncope patients safe for discharge
- Reduce unnecessary hospitalizations
- Guide ED disposition decisions
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_blood_pressure, validate_lab_value
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


def calculate_sf_syncope_rule(
    chf_history: bool,
    hematocrit: float,
    abnormal_ecg: bool,
    sob: bool,
    sbp: float
) -> dict:
    """
    Calculate San Francisco Syncope Rule
    
    Args:
        chf_history: History of congestive heart failure
        hematocrit: Hematocrit (%)
        abnormal_ecg: Abnormal ECG findings
        sob: Shortness of breath
        sbp: Systolic blood pressure (mmHg)
    
    Returns:
        Dictionary with risk assessment and details
    """
    risk_factors = []
    details = []
    
    # CHF history
    if chf_history:
        risk_factors.append("Tiền sử suy tim")
        details.append("✅ Tiền sử suy tim → Yếu tố nguy cơ")
    else:
        details.append("❌ Không có tiền sử suy tim")
    
    # Hematocrit <30%
    if hematocrit < 30:
        risk_factors.append("Hematocrit <30%")
        details.append(f"✅ Hematocrit {hematocrit:.1f}% (<30%) → Yếu tố nguy cơ")
    else:
        details.append(f"❌ Hematocrit {hematocrit:.1f}% (≥30%)")
    
    # Abnormal ECG
    if abnormal_ecg:
        risk_factors.append("ECG bất thường")
        details.append("✅ ECG bất thường → Yếu tố nguy cơ")
    else:
        details.append("❌ ECG bình thường")
    
    # Shortness of breath
    if sob:
        risk_factors.append("Khó thở")
        details.append("✅ Khó thở → Yếu tố nguy cơ")
    else:
        details.append("❌ Không khó thở")
    
    # SBP <90 mmHg
    if sbp < 90:
        risk_factors.append("Huyết áp tâm thu <90 mmHg")
        details.append(f"✅ SBP {sbp:.0f} mmHg (<90) → Yếu tố nguy cơ")
    else:
        details.append(f"❌ SBP {sbp:.0f} mmHg (≥90)")
    
    # Risk assessment
    if len(risk_factors) > 0:
        risk_category = "Cao"
        risk_class = "HIGH"
        interpretation = "Nguy cơ cao biến cố nghiêm trọng - Cần nhập viện"
        color = COLORS["error"]
        recommendation = "Khuyến cáo nhập viện để theo dõi và đánh giá thêm"
    else:
        risk_category = "Thấp"
        risk_class = "LOW"
        interpretation = "Nguy cơ thấp - Có thể xuất viện an toàn"
        color = COLORS["success"]
        recommendation = "Có thể xuất viện với theo dõi ngoại trú"
    
    return {
        'risk_factors': risk_factors,
        'risk_category': risk_category,
        'risk_class': risk_class,
        'interpretation': interpretation,
        'recommendation': recommendation,
        'color': color,
        'details': details
    }


def render():
    """Render San Francisco Syncope Rule calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🚨 San Francisco Syncope Rule</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá nguy cơ biến cố nghiêm trọng sau ngất**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'sf_syncope':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **San Francisco Syncope Rule** đánh giá nguy cơ biến cố nghiêm trọng sau ngất:
        - Giúp xác định bệnh nhân nguy cơ thấp có thể xuất viện an toàn
        - Giảm nhập viện không cần thiết
        - Hướng dẫn quyết định xuất viện từ ED
        
        ### 🎯 Tiêu chí đánh giá (5 tiêu chí)
        
        **Bất kỳ tiêu chí nào dương tính = Nguy cơ cao**
        
        1. **Tiền sử suy tim**
        
        2. **Hematocrit <30%**
        
        3. **ECG bất thường**
           - Rối loạn nhịp tim
           - Block nhĩ thất
           - ST-T thay đổi
           - Các bất thường khác
        
        4. **Khó thở**
        
        5. **Huyết áp tâm thu <90 mmHg**
        
        ### 📊 Phân loại
        
        | Kết quả | Nguy cơ | Khuyến nghị |
        |---------|---------|-------------|
        | Có ≥1 tiêu chí | Cao | Nhập viện |
        | Không có tiêu chí | Thấp | Có thể xuất viện |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân ngất trong ED
        - Không áp dụng cho bệnh nhân chấn thương, động kinh, hoặc ngộ độc
        - Kết hợp với đánh giá lâm sàng
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="sf_syncope",
            calculator_name="San Francisco Syncope Rule",
            category="Hồi sức Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👤 Tiền sử & Triệu chứng")
        chf_history = st.checkbox(
            "Tiền sử suy tim",
            help="Tiền sử suy tim sung huyết"
        )
        
        sob = st.checkbox(
            "Khó thở",
            help="Bệnh nhân có khó thở"
        )
        
        abnormal_ecg = st.checkbox(
            "ECG bất thường",
            help="Rối loạn nhịp tim, block, ST-T thay đổi, hoặc các bất thường khác"
        )
    
    with col2:
        st.markdown("#### 🩺 Sinh hiệu & Xét nghiệm")
        sbp = st.number_input(
            "Huyết áp tâm thu (mmHg)",
            50.0, 200.0, 120.0, 1.0,
            format="%.0f",
            help="Huyết áp tâm thu khi đánh giá"
        )
        
        hematocrit = st.number_input(
            "Hematocrit (%)",
            10.0, 60.0, 40.0, 0.1,
            format="%.1f",
            help="Hematocrit"
        )
        
        if sbp < 90:
            st.warning("⚠️ Huyết áp tâm thu <90 mmHg")
        if hematocrit < 30:
            st.warning("⚠️ Hematocrit <30%")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Đánh giá San Francisco Syncope Rule", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_sbp, sbp_error = validate_blood_pressure(sbp)
        if not is_valid_sbp:
            validation_errors.append(f"Huyết áp tâm thu: {sbp_error}")
        
        is_valid_hct, hct_error = validate_lab_value(hematocrit, "Hematocrit", 10.0, 60.0)
        if not is_valid_hct:
            validation_errors.append(f"Hematocrit: {hct_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_sf_syncope_rule(
            chf_history=chf_history,
            hematocrit=hematocrit,
            abnormal_ecg=abnormal_ecg,
            sob=sob,
            sbp=sbp
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "HIGH": "🚨",
            "LOW": "✅"
        }
        icon = icon_map.get(result['risk_class'], "🚨")
        
        render_score_result(
            title="San Francisco Syncope Rule",
            score=f"{len(result['risk_factors'])}/5",
            interpretation=f"{result['interpretation']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
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
            
            - **Khuyến nghị:** {result['recommendation']}
            - Nguy cơ biến cố nghiêm trọng trong 7 ngày cao
            - Cần nhập viện để theo dõi và đánh giá thêm
            - Cân nhắc các xét nghiệm bổ sung (troponin, BNP, siêu âm tim)
            """)
        else:
            st.success(f"""
            **Nguy cơ thấp** - Không phát hiện yếu tố nguy cơ
            
            - **Khuyến nghị:** {result['recommendation']}
            - Nguy cơ biến cố nghiêm trọng trong 7 ngày thấp (<2%)
            - Có thể xuất viện an toàn với theo dõi ngoại trú
            - Hướng dẫn bệnh nhân quay lại nếu triệu chứng tái phát
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - San Francisco Syncope Rule giúp xác định bệnh nhân nguy cơ thấp có thể xuất viện an toàn
        - **Nguy cơ cao:** Nhập viện để theo dõi và đánh giá thêm
        - **Nguy cơ thấp:** Có thể xuất viện với theo dõi ngoại trú
        - Kết hợp với đánh giá lâm sàng và tiền sử bệnh nhân
        - Không áp dụng cho bệnh nhân chấn thương, động kinh, hoặc ngộ độc
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'sf_syncope',
            'calculator_name': 'San Francisco Syncope Rule',
            'inputs': {
                'chf_history': chf_history,
                'hematocrit': hematocrit,
                'abnormal_ecg': abnormal_ecg,
                'sob': sob,
                'sbp': sbp
            },
            'results': {
                'risk_factors_count': len(result['risk_factors']),
                'risk_category': result['risk_category'],
                'risk_class': result['risk_class'],
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
    references = get_references('sf_syncope')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Quinn JV, et al. Derivation of the San Francisco Syncope Rule to predict patients 
          with short-term serious outcomes. Ann Emerg Med. 2004;43(2):224-232.
        """)
    
    # History
    render_history_ui(calculator_id="sf_syncope", show_actions=True)
