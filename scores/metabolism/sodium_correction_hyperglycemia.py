"""
Sodium Correction for Hyperglycemia
Điều chỉnh Na khi tăng đường huyết
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_range, validate_lab_value
from components.ui.validation import render_validation_errors
from components.ui.scoring import render_score_result, render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def calculate_corrected_sodium(measured_na, glucose, glucose_unit="mg/dL"):
    """
    Calculate corrected sodium for hyperglycemia
    
    Formula: Corrected Na = Measured Na + 0.024 × (Glucose - 100) [if glucose in mg/dL]
    Alternative: Corrected Na = Measured Na + 0.016 × (Glucose - 5.5) [if glucose in mmol/L]
    
    Args:
        measured_na: Measured sodium (mmol/L)
        glucose: Blood glucose level
        glucose_unit: "mg/dL" or "mmol/L"
    
    Returns:
        Corrected sodium (mmol/L)
    """
    if glucose_unit == "mg/dL":
        # Katz formula: Corrected Na = Measured Na + 0.024 × (Glucose - 100)
        corrected_na = measured_na + 0.024 * (glucose - 100)
    else:  # mmol/L
        # Corrected Na = Measured Na + 0.016 × (Glucose - 5.5)
        corrected_na = measured_na + 0.016 * (glucose - 5.5)
    
    return corrected_na


def interpret_sodium(na_value):
    """
    Interpret sodium level
    
    Returns:
        dict with interpretation
    """
    if na_value < 135:
        return {
            "status": "🔴 Hạ natri máu",
            "interpretation": "Na < 135 mmol/L - Hạ natri máu",
            "severity": "Nhẹ" if na_value >= 130 else "Trung bình" if na_value >= 125 else "Nặng"
        }
    elif na_value <= 145:
        return {
            "status": "🟢 Bình thường",
            "interpretation": "Na 135-145 mmol/L - Bình thường",
            "severity": "Bình thường"
        }
    else:
        return {
            "status": "🔴 Tăng natri máu",
            "interpretation": "Na > 145 mmol/L - Tăng natri máu",
            "severity": "Nhẹ" if na_value <= 150 else "Trung bình" if na_value <= 155 else "Nặng"
        }


def render():
    """Render Sodium Correction calculator interface"""
    
    st.markdown(f"""
    <h2 style='text-align: center; color: {COLORS['success']};'>🧪 Sodium Correction for Hyperglycemia</h2>
    <p style='text-align: center;'><em>Điều chỉnh Na khi tăng đường huyết</em></p>
    """, unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "sodium_correction_hyperglycemia":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'Sodium Correction')}")
    
    with st.expander("ℹ️ Giới thiệu về Sodium Correction"):
        st.markdown("""
        **Sodium Correction for Hyperglycemia** điều chỉnh Na đo được khi có tăng đường huyết.
        
        **Cơ chế:**
        - Tăng đường huyết → tăng áp lực thẩm thấu → dịch di chuyển từ nội bào ra ngoại bào
        - → Pha loãng Na ngoại bào → Na đo được giảm giả tạo
        - → Cần điều chỉnh để đánh giá đúng Na thực tế
        
        **Công thức Katz (phổ biến nhất):**
        ```
        Corrected Na (mg/dL) = Measured Na + 0.024 × (Glucose - 100)
        Corrected Na (mmol/L) = Measured Na + 0.016 × (Glucose - 5.5)
        ```
        
        **Khi nào dùng:**
        - Glucose > 100 mg/dL (5.5 mmol/L)
        - Đánh giá Na ở bệnh nhân đái tháo đường
        - Hạ natri máu giả tạo do tăng đường huyết
        
        **Lưu ý:**
        - Công thức này ước tính, không hoàn toàn chính xác
        - Cần đánh giá lâm sàng kết hợp
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        measured_na = st.number_input(
            "Na đo được (mmol/L)",
            min_value=100.0,
            max_value=180.0,
            value=135.0,
            step=0.1,
            format="%.1f",
            help="Na đo được trong máu"
        )
    
    with col2:
        glucose_unit = st.radio(
            "Đơn vị Glucose",
            options=["mg/dL", "mmol/L"],
            index=0,
            horizontal=True
        )
        
        if glucose_unit == "mg/dL":
            glucose = st.number_input(
                "Glucose (mg/dL)",
                min_value=50.0,
                max_value=1000.0,
                value=200.0,
                step=1.0,
                format="%.0f",
                help="Đường huyết"
            )
        else:
            glucose = st.number_input(
                "Glucose (mmol/L)",
                min_value=2.5,
                max_value=55.0,
                value=11.0,
                step=0.1,
                format="%.1f",
                help="Đường huyết"
            )
    
    st.markdown("---")
    
    # Calculate
    if st.button("🧮 Tính Na điều chỉnh", type="primary", use_container_width=True):
        corrected_na = calculate_corrected_sodium(measured_na, glucose, glucose_unit)
        interpretation = interpret_sodium(corrected_na)
        measured_interp = interpret_sodium(measured_na)
        
        st.subheader("📊 Kết quả")
        
        # Difference
        difference = corrected_na - measured_na
        
        corrected_status = interpretation["status"]
        is_normal = "Bình thường" in corrected_status
        
        render_score_result(
            title="Kết quả Na điều chỉnh",
            score=f"{corrected_na:.1f} mmol/L",
            interpretation=f"**{interpretation['interpretation']}**\n\nChênh lệch: {difference:+.1f} mmol/L",
            mortality=interpretation['severity'],
            color=COLORS['success'] if is_normal else COLORS['warning'] if "Nhẹ" in interpretation['severity'] else COLORS['error'],
            icon="🧪"
        )
        
        # Difference
        difference = corrected_na - measured_na
        st.info(f"**Chênh lệch:** {difference:+.1f} mmol/L")
        
        # Interpretation
        st.info(f"**{interpretation['interpretation']}** (Mức độ: {interpretation['severity']})")
        
        # Formula
        with st.expander("📐 Công thức"):
            if glucose_unit == "mg/dL":
                st.markdown(f"""
                **Công thức Katz:**
                ```
                Corrected Na = Measured Na + 0.024 × (Glucose - 100)
                Corrected Na = {measured_na} + 0.024 × ({glucose} - 100)
                Corrected Na = {measured_na} + {0.024 * (glucose - 100):.3f}
                Corrected Na = {corrected_na:.1f} mmol/L
                ```
                """)
            else:
                st.markdown(f"""
                **Công thức:**
                ```
                Corrected Na = Measured Na + 0.016 × (Glucose - 5.5)
                Corrected Na = {measured_na} + 0.016 × ({glucose} - 5.5)
                Corrected Na = {measured_na} + {0.016 * (glucose - 5.5):.3f}
                Corrected Na = {corrected_na:.1f} mmol/L
                ```
                """)
        
        # Recommendations
        st.subheader("💡 Khuyến cáo lâm sàng")
        if corrected_na < 135:
            st.warning("""
            - ⚠️ **Hạ natri máu thực sự** - Cần điều chỉnh
            - Đánh giá nguyên nhân hạ natri máu
            - Điều chỉnh Na cẩn thận (tránh điều chỉnh quá nhanh)
            """)
        elif corrected_na > 145:
            st.warning("""
            - ⚠️ **Tăng natri máu** - Cần điều chỉnh
            - Đánh giá nguyên nhân tăng natri máu
            - Bù dịch đẳng trương hoặc nhược trương
            """)
        else:
            st.success("""
            - ✅ Na điều chỉnh trong giới hạn bình thường
            - Tiếp tục theo dõi Na và glucose
            """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "sodium_correction_hyperglycemia",
            "calculator_name": "Sodium Correction for Hyperglycemia",
            "inputs": {
                "Na đo được": f"{measured_na} mmol/L",
                "Glucose": f"{glucose} {glucose_unit}"
            },
            "results": {
                "Na điều chỉnh": f"{corrected_na:.1f} mmol/L",
                "Chênh lệch": f"{difference:+.1f} mmol/L",
                "Diễn giải": interpretation["interpretation"]
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
        
        # Suggestions
        render_suggestions("sodium_correction_hyperglycemia", corrected_na)
    
    # History
    render_history_ui("sodium_correction_hyperglycemia", "Sodium Correction for Hyperglycemia")
    
    # References
    references = get_references("sodium_correction_hyperglycemia")
    if references:
        render_references_section(references)

