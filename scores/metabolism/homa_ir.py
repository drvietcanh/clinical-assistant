"""
HOMA-IR Calculator (Homeostatic Model Assessment of Insulin Resistance)
========================================================================

Assesses insulin resistance

Reference:
- Matthews DR, et al. Homeostasis model assessment: insulin resistance and 
  beta-cell function from fasting plasma glucose and insulin concentrations in man. 
  Diabetologia. 1985;28(7):412-419.

HOMA-IR Formula:
HOMA-IR = (Fasting Glucose × Fasting Insulin) / 22.5

Where:
- Fasting Glucose: mmol/L (or convert from mg/dL)
- Fasting Insulin: μU/mL (or mU/L)

Interpretation:
- Normal: <1.0
- Mild insulin resistance: 1.0-2.5
- Moderate insulin resistance: 2.5-5.0
- Severe insulin resistance: >5.0

Clinical Utility:
- Used daily in endocrinology clinics
- Assess insulin resistance
- Monitor treatment response
- Predict diabetes risk
"""

import streamlit as st
from scores.utils.validation import validate_lab_value
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_homa_ir(fasting_glucose: float, fasting_insulin: float, glucose_unit: str = "mmol/L") -> dict:
    """
    Calculate HOMA-IR
    
    Args:
        fasting_glucose: Fasting plasma glucose
        fasting_insulin: Fasting plasma insulin (μU/mL or mU/L)
        glucose_unit: Unit of glucose ("mmol/L" or "mg/dL")
    
    Returns:
        Dictionary with HOMA-IR value and interpretation
    """
    # Convert glucose to mmol/L if needed
    if glucose_unit == "mg/dL":
        glucose_mmol = fasting_glucose / 18.0
    else:
        glucose_mmol = fasting_glucose
    
    # Calculate HOMA-IR
    homa_ir = (glucose_mmol * fasting_insulin) / 22.5
    
    # Interpretation
    if homa_ir < 1.0:
        interpretation = "Bình thường"
        resistance_level = "NORMAL"
        color = "success"
        recommendation = "Không có đề kháng insulin"
    elif homa_ir < 2.5:
        interpretation = "Đề kháng insulin nhẹ"
        resistance_level = "MILD"
        color = "warning"
        recommendation = "Theo dõi, thay đổi lối sống"
    elif homa_ir < 5.0:
        interpretation = "Đề kháng insulin trung bình"
        resistance_level = "MODERATE"
        color = "error"
        recommendation = "Điều trị tích cực, xem xét metformin"
    else:
        interpretation = "Đề kháng insulin nặng"
        resistance_level = "SEVERE"
        color = "error"
        recommendation = "Điều trị tích cực, nguy cơ đái tháo đường cao"
    
    return {
        'homa_ir': homa_ir,
        'interpretation': interpretation,
        'resistance_level': resistance_level,
        'color': color,
        'recommendation': recommendation,
        'glucose_mmol': glucose_mmol
    }


def render():
    """Render HOMA-IR calculator"""
    
    st.title("💉 HOMA-IR Calculator")
    st.markdown("**Đánh giá đề kháng insulin (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'homa_ir':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **HOMA-IR (Homeostatic Model Assessment of Insulin Resistance)** đánh giá đề kháng insulin:
        - Dùng hàng ngày trong phòng khám nội tiết
        - Công thức đơn giản từ glucose và insulin lúc đói
        - Giúp đánh giá nguy cơ đái tháo đường type 2
        
        ### 🧮 Công thức
        
        **HOMA-IR = (Glucose lúc đói × Insulin lúc đói) / 22.5**
        
        - Glucose: mmol/L (hoặc mg/dL)
        - Insulin: μU/mL (hoặc mU/L)
        
        ### 📊 Phân loại
        
        - **<1.0:** Bình thường
        - **1.0-2.5:** Đề kháng insulin nhẹ
        - **2.5-5.0:** Đề kháng insulin trung bình
        - **>5.0:** Đề kháng insulin nặng
        
        ### ⚠️ Lưu ý
        
        - Cần lấy máu lúc đói (nhịn ăn 8-12 giờ)
        - Không dùng khi đang dùng insulin ngoại sinh
        - Kết hợp với đánh giá lâm sàng
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="homa_ir",
            calculator_name="HOMA-IR",
            category="Nội tiết",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập kết quả xét nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        glucose_unit = st.radio(
            "Đơn vị glucose",
            ["mmol/L", "mg/dL"],
            horizontal=True,
            index=0
        )
        
        if glucose_unit == "mmol/L":
            fasting_glucose = st.number_input(
                "Glucose lúc đói (mmol/L)",
                2.0, 30.0, 5.5, 0.1,
                format="%.1f",
                help="Fasting plasma glucose"
            )
        else:
            fasting_glucose = st.number_input(
                "Glucose lúc đói (mg/dL)",
                40.0, 600.0, 100.0, 1.0,
                format="%.0f",
                help="Fasting plasma glucose"
            )
            st.caption(f"💡 Chuyển đổi: {fasting_glucose:.0f} mg/dL = {fasting_glucose/18.0:.1f} mmol/L")
    
    with col2:
        st.markdown("#### Insulin")
        fasting_insulin = st.number_input(
            "Insulin lúc đói (μU/mL hoặc mU/L)",
            0.5, 200.0, 10.0, 0.1,
            format="%.1f",
            help="Fasting plasma insulin"
        )
        st.caption("Lưu ý: μU/mL = mU/L (cùng đơn vị)")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính HOMA-IR", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        if glucose_unit == "mmol/L":
            is_valid_glucose, glucose_error = validate_lab_value(fasting_glucose, "Fasting Glucose", 2.0, 30.0)
        else:
            is_valid_glucose, glucose_error = validate_lab_value(fasting_glucose, "Fasting Glucose", 40.0, 600.0)
        
        if not is_valid_glucose:
            validation_errors.append(f"Glucose lúc đói: {glucose_error}")
        
        is_valid_insulin, insulin_error = validate_lab_value(fasting_insulin, "Fasting Insulin", 0.5, 200.0)
        if not is_valid_insulin:
            validation_errors.append(f"Insulin lúc đói: {insulin_error}")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_homa_ir(fasting_glucose, fasting_insulin, glucose_unit)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**HOMA-IR**",
                f"{result['homa_ir']:.2f}"
            )
        
        with col_r2:
            st.markdown(f"### {result['interpretation']}")
            st.caption(f"Đề kháng insulin: {result['resistance_level']}")
        
        # Formula display
        with st.expander("🧮 Công thức tính", expanded=False):
            st.markdown(f"""
            **HOMA-IR = (Glucose × Insulin) / 22.5**
            
            - Glucose: {result['glucose_mmol']:.2f} mmol/L ({fasting_glucose:.1f} {'mg/dL' if glucose_unit == 'mg/dL' else 'mmol/L'})
            - Insulin: {fasting_insulin:.1f} μU/mL
            - **HOMA-IR = ({result['glucose_mmol']:.2f} × {fasting_insulin:.1f}) / 22.5 = {result['homa_ir']:.2f}**
            """)
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['resistance_level'] == "NORMAL":
            st.success(f"""
            **✅ Bình thường (HOMA-IR = {result['homa_ir']:.2f}):**
            
            - Không có đề kháng insulin
            - Độ nhạy insulin tốt
            - Nguy cơ đái tháo đường thấp
            - Khuyến cáo: Duy trì lối sống lành mạnh
            """)
        elif result['resistance_level'] == "MILD":
            st.warning(f"""
            **⚠️ Đề kháng insulin nhẹ (HOMA-IR = {result['homa_ir']:.2f}):**
            
            - Có đề kháng insulin nhẹ
            - Nguy cơ đái tháo đường tăng
            - Khuyến cáo:
              * Thay đổi lối sống (giảm cân, tập thể dục)
              * Chế độ ăn ít carbohydrate
              * Theo dõi định kỳ
              * Xem xét metformin nếu có chỉ định
            """)
        elif result['resistance_level'] == "MODERATE":
            st.error(f"""
            **🚨 Đề kháng insulin trung bình (HOMA-IR = {result['homa_ir']:.2f}):**
            
            - Đề kháng insulin rõ rệt
            - Nguy cơ đái tháo đường cao
            - Khuyến cáo:
              * **Điều trị tích cực**
              * Metformin (nếu chưa dùng)
              * Thay đổi lối sống mạnh mẽ
              * Theo dõi sát (HbA1c, glucose)
              * Xem xét thuốc khác (thiazolidinediones, GLP-1 agonists)
            """)
        else:
            st.error(f"""
            **🚨🚨 Đề kháng insulin nặng (HOMA-IR = {result['homa_ir']:.2f}):**
            
            - Đề kháng insulin rất nặng
            - Nguy cơ đái tháo đường rất cao
            - Khuyến cáo:
              * **Điều trị khẩn cấp**
              * Metformin liều cao
              * Thiazolidinediones (pioglitazone)
              * GLP-1 agonists hoặc SGLT2 inhibitors
              * Thay đổi lối sống tích cực
              * Theo dõi sát (HbA1c mỗi 3 tháng)
              * Đánh giá biến chứng
            """)
        
        st.info("""
        **📌 Lưu ý quan trọng:**
        
        - HOMA-IR chỉ là công cụ hỗ trợ, không thay thế đánh giá lâm sàng
        - Cần kết hợp với: HbA1c, glucose tolerance test, lipid profile
        - Không dùng khi đang dùng insulin ngoại sinh
        - Quyết định điều trị cuối cùng thuộc về bác sĩ lâm sàng
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Fasting Glucose": f"{fasting_glucose:.1f} {glucose_unit}",
            "Fasting Insulin": f"{fasting_insulin:.1f} μU/mL"
        }
        
        results_dict = {
            "HOMA-IR": f"{result['homa_ir']:.2f}",
            "Interpretation": result['interpretation'],
            "Resistance Level": result['resistance_level'],
            "Recommendation": result['recommendation']
        }
        
        # Export section
        render_export_section(
            title="HOMA-IR",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="HOMA-IR"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="homa_ir",
            calculator_name="HOMA-IR",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="homa_ir",
            calculator_name="HOMA-IR",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="homa_ir", show_actions=True)
        
        # References section
        references = get_references("HOMA-IR")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['homa_ir_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("HOMA-IR")
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
            **HOMA-IR (Homeostatic Model Assessment of Insulin Resistance)**
            
            **Reference:**
            Matthews DR, Hosker JP, Rudenski AS, et al. Homeostasis model assessment: 
            insulin resistance and beta-cell function from fasting plasma glucose and 
            insulin concentrations in man. Diabetologia. 1985;28(7):412-419.
            
            **Formula:**
            HOMA-IR = (Fasting Glucose × Fasting Insulin) / 22.5
            
            **Interpretation:**
            - <1.0: Normal
            - 1.0-2.5: Mild insulin resistance
            - 2.5-5.0: Moderate insulin resistance
            - >5.0: Severe insulin resistance
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

