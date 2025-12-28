"""
Lactate Clearance Calculator
=============================

Assesses effectiveness of resuscitation in shock patients

Reference:
- Nguyen HB, et al. Early lactate clearance is associated with improved outcome 
  in severe sepsis and septic shock. Crit Care Med. 2004;32(8):1637-1642.

Lactate Clearance Formula:
Lactate Clearance (%) = [(Initial Lactate - Repeat Lactate) / Initial Lactate] × 100

Where:
- Initial Lactate: Lactate level at presentation (mmol/L)
- Repeat Lactate: Lactate level after resuscitation (mmol/L)

Interpretation:
- ≥20% clearance: Good response to resuscitation
- 10-19% clearance: Moderate response
- <10% clearance: Poor response, consider additional interventions

Clinical Utility:
- Used daily in ICU and emergency
- Assesses response to fluid resuscitation
- Guides further management
- Predicts outcome in sepsis/septic shock
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


def calculate_lactate_clearance(initial_lactate: float, repeat_lactate: float) -> dict:
    """
    Calculate Lactate Clearance
    
    Args:
        initial_lactate: Initial lactate level (mmol/L)
        repeat_lactate: Repeat lactate level after resuscitation (mmol/L)
    
    Returns:
        Dictionary with clearance percentage and interpretation
    """
    # Calculate clearance
    if initial_lactate <= 0:
        clearance_percent = 0
    else:
        clearance_percent = ((initial_lactate - repeat_lactate) / initial_lactate) * 100
    
    # Absolute change
    absolute_change = initial_lactate - repeat_lactate
    
    # Interpretation
    if clearance_percent >= 20:
        response = "Tốt"
        response_class = "GOOD"
        color = "success"
        recommendation = "Đáp ứng tốt với hồi sức, tiếp tục điều trị hiện tại"
    elif clearance_percent >= 10:
        response = "Trung bình"
        response_class = "MODERATE"
        color = "warning"
        recommendation = "Đáp ứng trung bình, xem xét tăng cường hồi sức"
    else:
        response = "Kém"
        response_class = "POOR"
        color = "error"
        recommendation = "Đáp ứng kém, cần can thiệp tích cực hơn"
    
    return {
        'clearance_percent': clearance_percent,
        'absolute_change': absolute_change,
        'response': response,
        'response_class': response_class,
        'color': color,
        'recommendation': recommendation
    }


def render():
    """Render Lactate Clearance calculator"""
    
    st.title("🩸 Lactate Clearance")
    st.markdown("**Đánh giá hiệu quả hồi sức ở bệnh nhân sốc (DÙNG HÀNG NGÀY)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'lactate_clearance':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **Lactate Clearance** đánh giá hiệu quả hồi sức:
        - Dùng hàng ngày trong ICU và cấp cứu
        - Đánh giá đáp ứng với điều trị sốc
        - Giúp quyết định tiếp tục hay thay đổi điều trị
        
        ### 🧮 Công thức
        
        **Lactate Clearance (%) = [(Lactate ban đầu - Lactate sau hồi sức) / Lactate ban đầu] × 100**
        
        ### 📊 Phân loại
        
        - **≥20%:** Đáp ứng tốt → Tiếp tục điều trị hiện tại
        - **10-19%:** Đáp ứng trung bình → Xem xét tăng cường
        - **<10%:** Đáp ứng kém → Cần can thiệp tích cực hơn
        
        ### ⏰ Thời điểm đánh giá
        
        - Lactate ban đầu: Khi nhập viện/bắt đầu sốc
        - Lactate sau hồi sức: Sau 2-6 giờ điều trị
        
        ### ⚠️ Lưu ý
        
        - Lactate clearance ≥20% liên quan với tiên lượng tốt hơn
        - Cần kết hợp với đánh giá lâm sàng khác
        - Không chỉ dựa vào lactate clearance
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="lactate_clearance",
            calculator_name="Lactate Clearance",
            category="Cấp cứu",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập kết quả Lactate")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🩸 Lactate Ban đầu")
        initial_lactate = st.number_input(
            "Lactate ban đầu (mmol/L)",
            0.0, 30.0, 4.0, 0.1,
            format="%.1f",
            help="Lactate khi nhập viện/bắt đầu sốc"
        )
        st.caption("Thường đo khi nhập viện hoặc khi chẩn đoán sốc")
    
    with col2:
        st.markdown("#### 🩸 Lactate Sau hồi sức")
        repeat_lactate = st.number_input(
            "Lactate sau hồi sức (mmol/L)",
            0.0, 30.0, 3.0, 0.1,
            format="%.1f",
            help="Lactate sau 2-6 giờ điều trị"
        )
        st.caption("Thường đo sau 2-6 giờ hồi sức")
        
        time_interval = st.number_input(
            "Khoảng thời gian (giờ)",
            0.5, 24.0, 2.0, 0.5,
            format="%.1f",
            help="Thời gian giữa 2 lần đo"
        )
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính Lactate Clearance", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        is_valid_initial, initial_error = validate_lab_value(initial_lactate, "Initial Lactate", 0.0, 30.0)
        if not is_valid_initial:
            validation_errors.append(f"Lactate ban đầu: {initial_error}")
        
        is_valid_repeat, repeat_error = validate_lab_value(repeat_lactate, "Repeat Lactate", 0.0, 30.0)
        if not is_valid_repeat:
            validation_errors.append(f"Lactate sau hồi sức: {repeat_error}")
        
        if initial_lactate <= 0:
            validation_errors.append("Lactate ban đầu phải > 0 để tính clearance")
        
        if repeat_lactate > initial_lactate:
            st.warning("⚠️ Lactate sau hồi sức cao hơn ban đầu - Có thể tình trạng xấu đi!")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_lactate_clearance(initial_lactate, repeat_lactate)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col_r1, col_r2, col_r3 = st.columns(3)
        
        with col_r1:
            st.metric(
                "**Lactate Clearance**",
                f"{result['clearance_percent']:.1f}%"
            )
        
        with col_r2:
            st.metric(
                "**Thay đổi tuyệt đối**",
                f"{result['absolute_change']:.1f} mmol/L",
                delta=f"Từ {initial_lactate:.1f} → {repeat_lactate:.1f}"
            )
        
        with col_r3:
            st.markdown(f"### {result['response']}")
            st.caption("Đáp ứng với hồi sức")
        
        # Formula display
        with st.expander("🧮 Công thức tính", expanded=False):
            st.markdown(f"""
            **Lactate Clearance = [(Lactate ban đầu - Lactate sau) / Lactate ban đầu] × 100**
            
            - Lactate ban đầu: {initial_lactate:.1f} mmol/L
            - Lactate sau hồi sức: {repeat_lactate:.1f} mmol/L
            - Thay đổi: {result['absolute_change']:.1f} mmol/L
            - **Clearance = [({initial_lactate:.1f} - {repeat_lactate:.1f}) / {initial_lactate:.1f}] × 100 = {result['clearance_percent']:.1f}%**
            """)
        
        # Interpretation
        st.markdown("---")
        st.markdown("### 💡 Diễn giải")
        
        if result['response_class'] == "GOOD":
            st.success(f"""
            **✅ Đáp ứng TỐT (Clearance = {result['clearance_percent']:.1f}% ≥ 20%):**
            
            **Khuyến cáo:**
            - Tiếp tục điều trị hiện tại
            - Theo dõi lactate định kỳ
            - Tiên lượng tốt hơn
            - Có thể giảm cường độ hồi sức nếu ổn định
            """)
        elif result['response_class'] == "MODERATE":
            st.warning(f"""
            **⚠️ Đáp ứng TRUNG BÌNH (Clearance = {result['clearance_percent']:.1f}% 10-19%):**
            
            **Khuyến cáo:**
            - Xem xét tăng cường hồi sức
            - Đánh giá lại thể tích dịch
            - Có thể cần thêm dịch hoặc vận mạch
            - Theo dõi sát, đánh giá lại sau 2-4 giờ
            - Xem xét các nguyên nhân khác của sốc
            """)
        else:
            st.error(f"""
            **🚨 Đáp ứng KÉM (Clearance = {result['clearance_percent']:.1f}% < 10%):**
            
            **Khuyến cáo:**
            - **Cần can thiệp TÍCH CỰC hơn**
            - Đánh giá lại nguyên nhân sốc
            - Tăng cường hồi sức dịch (nếu còn thiếu dịch)
            - Xem xét vận mạch sớm
            - Đánh giá nguồn nhiễm trùng (nếu sốc nhiễm trùng)
            - Xem xét các nguyên nhân khác:
              * Thiếu máu
              * Rối loạn chuyển hóa
              * Tổn thương cơ quan
            - Hội chẩn chuyên khoa
            - Theo dõi sát, đánh giá lại sau 1-2 giờ
            """)
        
        # Additional info
        st.info(f"""
        **📌 Lưu ý quan trọng:**
        
        - Lactate clearance được đánh giá sau **{time_interval:.1f} giờ** điều trị
        - Clearance ≥20% liên quan với tiên lượng tốt hơn trong sốc nhiễm trùng
        - Cần kết hợp với đánh giá lâm sàng: huyết áp, nhịp tim, lượng nước tiểu, ý thức
        - Lactate ban đầu: {initial_lactate:.1f} mmol/L
        - Lactate hiện tại: {repeat_lactate:.1f} mmol/L
        - Mục tiêu: Lactate <2.0 mmol/L và clearance ≥20%
        """)
        
        # Prepare inputs and results
        inputs_dict = {
            "Initial Lactate": f"{initial_lactate:.1f} mmol/L",
            "Repeat Lactate": f"{repeat_lactate:.1f} mmol/L",
            "Time Interval": f"{time_interval:.1f} giờ"
        }
        
        results_dict = {
            "Lactate Clearance": f"{result['clearance_percent']:.1f}%",
            "Absolute Change": f"{result['absolute_change']:.1f} mmol/L",
            "Response": result['response'],
            "Recommendation": result['recommendation']
        }
        
        # Export section
        render_export_section(
            title="Lactate Clearance",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Lactate Clearance"
        )
        
        # Save to history
        save_calculation_to_history(
            calculator_id="lactate_clearance",
            calculator_name="Lactate Clearance",
            inputs=inputs_dict,
            results=results_dict
        )
        
        # Share section
        render_share_section(
            calculator_id="lactate_clearance",
            calculator_name="Lactate Clearance",
            inputs=inputs_dict,
            results=results_dict,
            show_qr=True
        )
        
        # History section
        st.markdown("---")
        render_history_ui(calculator_id="lactate_clearance", show_actions=True)
        
        # References section
        references = get_references("Lactate Clearance")
        if references:
            render_references_section(
                references=references,
                title="📚 Tài liệu tham khảo",
                last_updated="2024-01-15",
                show_evidence_level=True,
                show_links=True
            )
        
        st.session_state['lactate_clearance_result'] = result
    
    # Always show references at the bottom
    st.markdown("---")
    references = get_references("Lactate Clearance")
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
            **Lactate Clearance**
            
            **Reference:**
            Nguyen HB, Rivers EP, Knoblich BP, et al. Early lactate clearance is associated 
            with improved outcome in severe sepsis and septic shock. Crit Care Med. 2004;32(8):1637-1642.
            
            **Formula:**
            Lactate Clearance (%) = [(Initial Lactate - Repeat Lactate) / Initial Lactate] × 100
            
            **Interpretation:**
            - ≥20%: Good response
            - 10-19%: Moderate response
            - <10%: Poor response
            
            **Clinical Significance:**
            - Lactate clearance ≥20% associated with better outcomes
            - Assess after 2-6 hours of resuscitation
            """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ lâm sàng - không thay thế đánh giá lâm sàng toàn diện")

