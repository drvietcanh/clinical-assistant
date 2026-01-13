"""
ABC/2 Method Calculator
========================

Estimates intracerebral hemorrhage volume

Reference:
- Kothari RU, et al. The ABCs of measuring intracerebral hemorrhage volumes. 
  Stroke. 1996;27(8):1304-1305.

ABC/2 Formula:
Volume (mL) = (A × B × C) / 2

Where:
- A = Largest diameter (cm)
- B = Perpendicular diameter to A (cm)
- C = Height (number of slices × slice thickness in cm)

Clinical Utility:
- Quick estimation of ICH volume
- Guide treatment decisions
- Predict prognosis
- ICH volume >30 mL associated with poor outcome
"""

import streamlit as st
from config.theme import COLORS
from scores.utils.validation import validate_lab_value
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


def calculate_abc2_volume(
    diameter_a: float,
    diameter_b: float,
    height: float
) -> dict:
    """
    Calculate ICH volume using ABC/2 method
    
    Args:
        diameter_a: Largest diameter (cm)
        diameter_b: Perpendicular diameter to A (cm)
        height: Height (cm) - can be number of slices × slice thickness
    
    Returns:
        Dictionary with volume and interpretation
    """
    # Calculate volume
    volume = (diameter_a * diameter_b * height) / 2.0
    
    # Determine prognosis
    if volume < 30:
        prognosis = "Tốt hơn"
        risk_class = "LOW"
        color = COLORS["success"]
        interpretation = "Thể tích <30 mL - Tiên lượng tốt hơn"
    elif volume < 60:
        prognosis = "Trung bình"
        risk_class = "MEDIUM"
        color = COLORS["warning"]
        interpretation = "Thể tích 30-60 mL - Tiên lượng trung bình"
    else:
        prognosis = "Kém"
        risk_class = "HIGH"
        color = COLORS["error"]
        interpretation = "Thể tích ≥60 mL - Tiên lượng kém"
    
    return {
        'volume': volume,
        'prognosis': prognosis,
        'risk_class': risk_class,
        'interpretation': interpretation,
        'color': color
    }


def render():
    """Render ABC/2 Method calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🧠 ABC/2 Method</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Ước tính thể tích xuất huyết não (ICH)**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'abc2':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **ABC/2 Method** ước tính thể tích xuất huyết não (ICH):
        - Phương pháp nhanh và đơn giản
        - Dựa trên đo đạc trên CT scan
        - Hướng dẫn quyết định điều trị và tiên lượng
        
        ### 🎯 Công thức
        
        **Thể tích (mL) = (A × B × C) / 2**
        
        - **A:** Đường kính lớn nhất (cm)
        - **B:** Đường kính vuông góc với A (cm)
        - **C:** Chiều cao (cm)
          - Có thể tính: Số lát cắt × Độ dày lát cắt (cm)
        
        ### 📊 Tiên lượng
        
        | Thể tích | Tiên lượng |
        |----------|------------|
        | <30 mL | Tốt hơn |
        | 30-60 mL | Trung bình |
        | ≥60 mL | Kém |
        
        ### ⚠️ Lưu ý
        
        - Đo trên CT scan
        - ICH volume >30 mL liên quan đến tiên lượng kém
        - Hướng dẫn quyết định phẫu thuật
        - Kết hợp với các yếu tố khác (vị trí, tuổi, GCS)
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="abc2",
            calculator_name="ABC/2 Method",
            category="Thần Kinh",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin từ CT scan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📏 Kích thước")
        diameter_a = st.number_input(
            "Đường kính lớn nhất A (cm)",
            0.1, 20.0, 3.0, 0.1,
            format="%.1f",
            help="Đường kính lớn nhất của khối xuất huyết"
        )
        
        diameter_b = st.number_input(
            "Đường kính vuông góc B (cm)",
            0.1, 20.0, 3.0, 0.1,
            format="%.1f",
            help="Đường kính vuông góc với A"
        )
    
    with col2:
        st.markdown("#### 📐 Chiều cao")
        method = st.radio(
            "Phương pháp tính chiều cao",
            ["Nhập trực tiếp", "Tính từ số lát cắt"],
            horizontal=False
        )
        
        if method == "Nhập trực tiếp":
            height = st.number_input(
                "Chiều cao C (cm)",
                0.1, 20.0, 3.0, 0.1,
                format="%.1f",
                help="Chiều cao của khối xuất huyết"
            )
        else:
            num_slices = st.number_input(
                "Số lát cắt",
                1, 50, 3, 1,
                format="%d",
                help="Số lát cắt CT có xuất huyết"
            )
            slice_thickness = st.number_input(
                "Độ dày lát cắt (cm)",
                0.1, 2.0, 0.5, 0.1,
                format="%.1f",
                help="Độ dày mỗi lát cắt CT (thường 0.5 cm)"
            )
            height = num_slices * slice_thickness
            st.info(f"Chiều cao tính được: {height:.1f} cm")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính thể tích ABC/2", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        if diameter_a <= 0 or diameter_a > 20:
            validation_errors.append("Đường kính A phải trong khoảng 0.1-20 cm")
        
        if diameter_b <= 0 or diameter_b > 20:
            validation_errors.append("Đường kính B phải trong khoảng 0.1-20 cm")
        
        if height <= 0 or height > 20:
            validation_errors.append("Chiều cao C phải trong khoảng 0.1-20 cm")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_abc2_volume(
            diameter_a=diameter_a,
            diameter_b=diameter_b,
            height=height
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "LOW": "✅",
            "MEDIUM": "⚠️",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🧠")
        
        render_score_result(
            title="ABC/2 Volume",
            score=f"{result['volume']:.1f} mL",
            interpretation=f"{result['interpretation']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Details
        st.markdown("### 📋 Chi tiết tính toán")
        st.markdown(f"""
        - **A (đường kính lớn nhất):** {diameter_a:.1f} cm
        - **B (đường kính vuông góc):** {diameter_b:.1f} cm
        - **C (chiều cao):** {height:.1f} cm
        - **Công thức:** (A × B × C) / 2
        - **Thể tích:** ({diameter_a:.1f} × {diameter_b:.1f} × {height:.1f}) / 2 = **{result['volume']:.1f} mL**
        """)
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **Thể tích: {result['volume']:.1f} mL** - Tiên lượng tốt hơn ✅
            
            - Thể tích <30 mL
            - Tiên lượng tốt hơn so với xuất huyết lớn
            - Cân nhắc điều trị bảo tồn
            - Theo dõi sát diễn biến
            """)
        elif result['risk_class'] == "MEDIUM":
            st.warning(f"""
            **Thể tích: {result['volume']:.1f} mL** - Tiên lượng trung bình ⚠️
            
            - Thể tích 30-60 mL
            - Tiên lượng trung bình
            - Cân nhắc điều trị tích cực
            - Đánh giá chỉ định phẫu thuật dựa trên các yếu tố khác
            """)
        else:
            st.error(f"""
            **Thể tích: {result['volume']:.1f} mL** - Tiên lượng kém 🚨
            
            - Thể tích ≥60 mL
            - Tiên lượng kém, tỷ lệ tử vong cao
            - Cân nhắc phẫu thuật giải áp (nếu phù hợp)
            - Điều trị tích cực và hỗ trợ
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - ABC/2 Method giúp ước tính nhanh thể tích ICH
        - **Thể tích >30 mL:** Liên quan đến tiên lượng kém
        - **Thể tích >60 mL:** Tiên lượng rất kém, tỷ lệ tử vong cao
        - Quyết định phẫu thuật dựa trên:
          → Thể tích xuất huyết
          → Vị trí xuất huyết
          → Tuổi và tình trạng bệnh nhân
          → GCS và tình trạng thần kinh
        - Kết hợp với các yếu tố khác để đánh giá toàn diện
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'abc2',
            'calculator_name': 'ABC/2 Method',
            'inputs': {
                'diameter_a': diameter_a,
                'diameter_b': diameter_b,
                'height': height
            },
            'results': {
                'volume': result['volume'],
                'prognosis': result['prognosis'],
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
    references = get_references('abc2')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Kothari RU, et al. The ABCs of measuring intracerebral hemorrhage volumes. 
          Stroke. 1996;27(8):1304-1305.
        """)
    
    # History
    render_history_ui(calculator_id="abc2", show_actions=True)
