"""
ROX Index Calculator
====================

Predicts HFNC (High Flow Nasal Cannula) failure in acute hypoxemic respiratory failure

Reference:
- Roca O, et al. An index combining respiratory rate and oxygenation to predict 
  outcome of nasal high-flow therapy. Am J Respir Crit Care Med. 2019;199(11):1368-1376.

ROX Index Formula:
ROX = (SpO2 / FiO2) / Respiratory Rate

Where:
- SpO2: Oxygen saturation (%)
- FiO2: Fraction of inspired oxygen (0.21-1.0)
- Respiratory Rate: Breaths per minute

Interpretation (at 2, 6, 12 hours):
- ROX ≥4.88 at 2h: Low risk of failure
- ROX ≥4.88 at 6h: Low risk of failure
- ROX ≥4.88 at 12h: Low risk of failure
- ROX <4.88: Higher risk, consider intubation

Clinical Utility:
- Used daily in ICU and emergency
- Predicts HFNC failure
- Guides decision on intubation timing
- Helps avoid delayed intubation
"""

import streamlit as st
from scores.utils.validation import validate_respiratory_rate, validate_lab_value
from components.ui.validation import render_validation_errors
# ========== PHASE 1 IMPORTS ==========
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section
# ======================================


def calculate_rox_index(spo2: float, fio2: float, respiratory_rate: int) -> dict:
    """
    Calculate ROX Index
    
    Args:
        spo2: Oxygen saturation (%)
        fio2: Fraction of inspired oxygen (0.21-1.0)
        respiratory_rate: Respiratory rate (bpm)
    
    Returns:
        Dictionary with ROX index and interpretation
    """
    # Calculate ROX Index
    rox_index = (spo2 / fio2) / respiratory_rate
    
    # Interpretation based on threshold 4.88
    if rox_index >= 4.88:
        risk_level = "Thấp"
        risk_class = "LOW"
        interpretation = "Nguy cơ thất bại HFNC thấp"
        color = "success"
        recommendation = "Tiếp tục HFNC, theo dõi"
    else:
        risk_level = "Cao"
        risk_class = "HIGH"
        interpretation = "Nguy cơ thất bại HFNC cao"
        color = "error"
        recommendation = "Cân nhắc đặt nội khí quản"
    
    return {
        'rox_index': rox_index,
        'risk_level': risk_level,
        'risk_class': risk_class,
        'interpretation': interpretation,
        'color': color,
        'recommendation': recommendation
    }


def render():
    """Render ROX Index calculator"""
    
    st.title("🫁 ROX Index")
    st.markdown("**Dự đoán thất bại HFNC (High Flow Nasal Cannula) - DÙNG HÀNG NGÀY**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'rox_index':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **ROX Index** dự đoán thất bại HFNC (High Flow Nasal Cannula):
        - Dùng hàng ngày trong ICU và cấp cứu
        - Đánh giá sau 2, 6, 12 giờ dùng HFNC
        - Giúp quyết định thời điểm đặt nội khí quản
        
        ### 🧮 Công thức
        
        **ROX = (SpO₂ / FiO₂) / Respiratory Rate**
        
        - SpO₂: Độ bão hòa oxy (%)
        - FiO₂: Nồng độ oxy trong khí thở vào (0.21-1.0)
        - Respiratory Rate: Nhịp thở (/min)
        
        ### 📊 Ngưỡng
        
        - **ROX ≥4.88:** Nguy cơ thất bại thấp → Tiếp tục HFNC
        - **ROX <4.88:** Nguy cơ thất bại cao → Cân nhắc đặt nội khí quản
        
        ### ⏰ Thời điểm đánh giá
        
        - Sau 2 giờ dùng HFNC
        - Sau 6 giờ dùng HFNC
        - Sau 12 giờ dùng HFNC
        
        **Lưu ý:** ROX <4.88 ở bất kỳ thời điểm nào → Nguy cơ cao
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="rox_index",
            calculator_name="ROX Index",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🫁 Hỗ trợ Hô hấp")
        fio2_input = st.number_input(
            "FiO₂ (%)",
            21.0, 100.0, 40.0, 1.0,
            format="%.0f",
            help="Nồng độ oxy trong khí thở vào"
        )
        fio2 = fio2_input / 100.0  # Convert to fraction
        
        time_point = st.selectbox(
            "Thời điểm đánh giá",
            ["Sau 2 giờ", "Sau 6 giờ", "Sau 12 giờ"],
            index=0,
            help="Thời gian đã dùng HFNC"
        )
    
    with col2:
        st.markdown("#### 🩺 Sinh hiệu")
        spo2 = st.number_input(
            "SpO₂ (%)",
            70.0, 100.0, 95.0, 0.1,
            format="%.1f",
            help="Độ bão hòa oxy"
        )
        
        respiratory_rate = st.number_input(
            "Nhịp thở (/min)",
            10, 50, 20, 1,
            format="%d",
            help="Respiratory rate"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính ROX Index", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_spo2, spo2_error = validate_lab_value(spo2, "SpO2", 70.0, 100.0)
        if not is_valid_spo2:
            validation_errors.append(f"SpO2: {spo2_error}")
        
        is_valid_rr, rr_error = validate_respiratory_rate(respiratory_rate)
        if not is_valid_rr:
            validation_errors.append(f"Nhịp thở: {rr_error}")
        
        if fio2 < 0.21 or fio2 > 1.0:
            validation_errors.append(f"FiO2: Phải trong khoảng 21-100%")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_rox_index(spo2, fio2, respiratory_rate)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(
                "**ROX Index**",
                f"{result['rox_index']:.2f}"
            )
            st.caption(f"Ngưỡng: 4.88")
        
        with col_r2:
            st.markdown(f"### {result['risk_level'].upper()}")
            st.caption(f"{result['interpretation']}")
        
        # Formula display
        with st.expander("🧮 Công thức tính", expanded=False):
            st.markdown(f"""
            **ROX = (SpO₂ / FiO₂) / Respiratory Rate**
            
            - SpO₂: {spo2:.1f}%
            - FiO₂: {fio2:.2f} ({fio2_input:.0f}%)
            - Respiratory Rate: {respiratory_rate} /min
            - **ROX = ({spo2:.1f} / {fio2:.2f}) / {respiratory_rate} = {result['rox_index']:.2f}**
            """)
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['risk_class'] == "LOW":
            st.success(f"""
            **✅ Nguy cơ thất bại HFNC THẤP (ROX = {result['rox_index']:.2f} ≥ 4.88):**
            
            **Khuyến cáo:**
            - Tiếp tục HFNC
            - Theo dõi sát SpO₂, nhịp thở
            - Đánh giá lại sau 2-4 giờ
            - Nếu ổn định, có thể tiếp tục HFNC
            - Theo dõi các dấu hiệu thất bại:
              * Tăng nhịp thở
              * Giảm SpO₂
              * Tăng công thở
              * Thay đổi ý thức
            """)
        else:
            st.error(f"""
            **🚨 Nguy cơ thất bại HFNC CAO (ROX = {result['rox_index']:.2f} < 4.88):**
            
            **Khuyến cáo:**
            - **Cân nhắc đặt nội khí quản NGAY**
            - Không nên chờ đợi thêm
            - Chuẩn bị dụng cụ đặt nội khí quản
            - Hội chẩn gây mê hồi sức
            - Xem xét các yếu tố khác:
              * Tình trạng ý thức
              * Công thở
              * pH, PaCO₂
              * Tình trạng tổng thể
            """)
        
        st.info(f"""
        **📌 Lưu ý quan trọng:**
        
        - ROX Index được đánh giá tại thời điểm: **{time_point}**
        - Ngưỡng 4.88 dựa trên nghiên cứu gốc
        - Cần kết hợp với đánh giá lâm sàng toàn diện
        - Không chỉ dựa vào ROX Index để quyết định
        - Các yếu tố khác: ý thức, công thở, pH, PaCO₂
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "SpO2": f"{spo2:.1f}%",
            "FiO2": f"{fio2_input:.0f}% ({fio2:.2f})",
            "Respiratory Rate": f"{respiratory_rate} /min",
            "Time Point": time_point
        }
        
        results_dict = {
            "ROX Index": f"{result['rox_index']:.2f}",
            "Risk Level": result['risk_level'],
            "Interpretation": result['interpretation'],
            "Recommendation": result['recommendation']
        }
        
        # Export section
        render_export_section(
            title="ROX Index",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="ROX Index"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="rox_index",
            calculator_name="ROX Index",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="rox_index",
            calculator_name="ROX Index",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="rox_index", show_actions=True)
        
        # References section
        references = get_references("ROX Index")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['rox_index_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("ROX Index")
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
            **ROX Index**
            
            **Reference:**
            Roca O, Caralt B, Messika J, et al. An index combining respiratory rate and 
            oxygenation to predict outcome of nasal high-flow therapy. 
            Am J Respir Crit Care Med. 2019;199(11):1368-1376.
            
            **Formula:**
            ROX = (SpO₂ / FiO₂) / Respiratory Rate
            
            **Threshold:**
            - ROX ≥4.88: Low risk of HFNC failure
            - ROX <4.88: High risk of HFNC failure
            
            **Time Points:**
            - Assess at 2, 6, and 12 hours after HFNC initiation
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

