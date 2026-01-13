"""
APRI Score Calculator
======================

Assesses liver fibrosis severity

Reference:
- Wai CT, et al. A simple noninvasive index can predict both significant fibrosis 
  and cirrhosis in patients with chronic hepatitis C. Hepatology. 2003;38(2):518-526.

APRI Formula:
APRI = (AST / ULN) / Platelet count (×10⁹/L) × 100

Where:
- AST = Aspartate aminotransferase (U/L)
- ULN = Upper limit of normal for AST (typically 40 U/L)
- Platelet count = Platelets (×10⁹/L)

Interpretation:
- <0.5: No significant fibrosis (F0-F1)
- 0.5-1.5: Significant fibrosis possible (F2-F3)
- >1.5: Cirrhosis likely (F4)

Clinical Utility:
- Non-invasive assessment of liver fibrosis
- Alternative to liver biopsy
- Monitor fibrosis progression
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


def calculate_apri_score(
    ast: float,
    platelet: float,
    uln: float = 40.0
) -> dict:
    """
    Calculate APRI Score
    
    Args:
        ast: AST level (U/L)
        platelet: Platelet count (×10⁹/L)
        uln: Upper limit of normal for AST (default 40 U/L)
    
    Returns:
        Dictionary with APRI score and interpretation
    """
    # Calculate APRI
    if platelet > 0:
        apri = (ast / uln) / platelet * 100
    else:
        apri = 0
    
    # Determine fibrosis stage
    if apri < 0.5:
        fibrosis_stage = "Không có xơ hóa đáng kể (F0-F1)"
        risk_class = "LOW"
        color = COLORS["success"]
        recommendation = "Không có xơ hóa đáng kể, tiếp tục theo dõi"
    elif apri <= 1.5:
        fibrosis_stage = "Có thể có xơ hóa đáng kể (F2-F3)"
        risk_class = "MEDIUM"
        color = COLORS["warning"]
        recommendation = "Cân nhắc đánh giá thêm (FIB-4, elastography, hoặc sinh thiết gan)"
    else:  # >1.5
        fibrosis_stage = "Có thể xơ gan (F4)"
        risk_class = "HIGH"
        color = COLORS["error"]
        recommendation = "Có thể xơ gan, cần đánh giá thêm và theo dõi biến chứng"
    
    return {
        'apri': apri,
        'fibrosis_stage': fibrosis_stage,
        'risk_class': risk_class,
        'recommendation': recommendation,
        'color': color
    }


def render():
    """Render APRI Score calculator"""
    
    st.markdown(f"""
    <h3 style='text-align: center; color: {COLORS['success']};'>🩺 APRI Score</h3>
    """, unsafe_allow_html=True)
    st.markdown("**Đánh giá mức độ xơ hóa gan không xâm lấn**")
    
    # Load shared result if available
    shared = load_shared_result_from_url()
    if shared and shared.get('calculator_id') == 'apri':
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared['calculator_name']}")
        if 'shared_inputs' not in st.session_state:
            st.session_state['shared_inputs'] = shared.get('inputs', {})
    
    # Educational information
    with st.expander("ℹ️ Thông tin & cách sử dụng"):
        st.markdown("""
        ### 📋 Giới Thiệu
        
        **APRI (AST to Platelet Ratio Index)** đánh giá mức độ xơ hóa gan:
        - Đánh giá không xâm lấn xơ hóa gan
        - Alternative to liver biopsy
        - Theo dõi diễn biến xơ hóa
        
        ### 🎯 Công thức
        
        **APRI = (AST / ULN) / Platelet (×10⁹/L) × 100**
        
        - **AST:** Aspartate aminotransferase (U/L)
        - **ULN:** Upper limit of normal (thường 40 U/L)
        - **Platelet:** Số lượng tiểu cầu (×10⁹/L)
        
        ### 📊 Phân loại
        
        | APRI | Xơ hóa | Giai đoạn |
        |------|--------|-----------|
        | <0.5 | Không đáng kể | F0-F1 |
        | 0.5-1.5 | Có thể đáng kể | F2-F3 |
        | >1.5 | Có thể xơ gan | F4 |
        
        ### ⚠️ Lưu ý
        
        - Dùng cho bệnh nhân viêm gan mạn (HCV, HBV, NAFLD)
        - Kết hợp với các phương pháp khác (FIB-4, elastography)
        - Không thay thế sinh thiết gan khi cần thiết
        """)
    
    st.divider()
    
    # Smart Suggestions
    col_sugg1, col_sugg2 = st.columns([2, 1])
    with col_sugg2:
        render_suggestions(
            calculator_id="apri",
            calculator_name="APRI Score",
            category="Tiêu Hóa",
            show_related=True,
            show_category=True,
            limit=3
        )
    
    # Input section
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ast = st.number_input(
            "AST (U/L)",
            0.0, 1000.0, 40.0, 1.0,
            format="%.1f",
            help="Aspartate aminotransferase"
        )
        
        uln = st.number_input(
            "ULN cho AST (U/L)",
            10.0, 100.0, 40.0, 1.0,
            format="%.1f",
            help="Upper limit of normal (thường 40 U/L)"
        )
    
    with col2:
        platelet = st.number_input(
            "Platelet count (×10⁹/L)",
            0.0, 1000.0, 200.0, 1.0,
            format="%.0f",
            help="Số lượng tiểu cầu"
        )
        
        if platelet < 150:
            st.warning("⚠️ Giảm tiểu cầu (<150 ×10⁹/L)")
    
    st.divider()
    
    # Calculate button
    if st.button("🧮 Tính APRI Score", type="primary", use_container_width=True):
        # Validate inputs
        validation_errors = []
        
        if ast <= 0 or ast > 1000:
            validation_errors.append("AST phải trong khoảng 0.1-1000 U/L")
        
        if platelet <= 0 or platelet > 1000:
            validation_errors.append("Platelet phải trong khoảng 0.1-1000 ×10⁹/L")
        
        if uln <= 0 or uln > 100:
            validation_errors.append("ULN phải trong khoảng 10-100 U/L")
        
        if validation_errors:
            render_validation_errors(validation_errors)
            return
        
        result = calculate_apri_score(
            ast=ast,
            platelet=platelet,
            uln=uln
        )
        
        # Display results
        st.subheader("📊 Kết quả")
        
        icon_map = {
            "LOW": "✅",
            "MEDIUM": "⚠️",
            "HIGH": "🚨"
        }
        icon = icon_map.get(result['risk_class'], "🩺")
        
        render_score_result(
            title="APRI Score",
            score=f"{result['apri']:.2f}",
            interpretation=f"{result['fibrosis_stage']}",
            mortality=None,
            color=result['color'],
            icon=icon,
            show_mortality=False
        )
        
        # Details
        st.markdown("### 📋 Chi tiết tính toán")
        st.markdown(f"""
        - **AST:** {ast:.1f} U/L
        - **ULN:** {uln:.1f} U/L
        - **Platelet:** {platelet:.0f} ×10⁹/L
        - **Công thức:** (AST / ULN) / Platelet × 100
        - **APRI:** ({ast:.1f} / {uln:.1f}) / {platelet:.0f} × 100 = **{result['apri']:.2f}**
        """)
        
        # Interpretation
        st.markdown("### 💡 Giải thích")
        if result['risk_class'] == "LOW":
            st.success(f"""
            **APRI: {result['apri']:.2f}** - Không có xơ hóa đáng kể ✅
            
            - **Giai đoạn:** F0-F1
            - **Khuyến nghị:** {result['recommendation']}
            - Tiếp tục theo dõi định kỳ
            """)
        elif result['risk_class'] == "MEDIUM":
            st.warning(f"""
            **APRI: {result['apri']:.2f}** - Có thể có xơ hóa đáng kể ⚠️
            
            - **Giai đoạn:** F2-F3
            - **Khuyến nghị:** {result['recommendation']}
            - Cân nhắc đánh giá thêm bằng FIB-4, elastography, hoặc sinh thiết gan
            """)
        else:
            st.error(f"""
            **APRI: {result['apri']:.2f}** - Có thể xơ gan 🚨
            
            - **Giai đoạn:** F4
            - **Khuyến nghị:** {result['recommendation']}
            - Cần đánh giá thêm và theo dõi biến chứng xơ gan
            - Cân nhắc siêu âm gan, nội soi thực quản để tìm varices
            """)
        
        # Clinical recommendations
        st.markdown("### 🎯 Khuyến nghị lâm sàng")
        st.info("""
        - APRI Score giúp đánh giá không xâm lấn xơ hóa gan
        - **APRI <0.5:** Không có xơ hóa đáng kể, tiếp tục theo dõi
        - **APRI 0.5-1.5:** Cân nhắc đánh giá thêm (FIB-4, elastography)
        - **APRI >1.5:** Có thể xơ gan, cần đánh giá và theo dõi biến chứng
        - Kết hợp với FIB-4 và các phương pháp khác để đánh giá toàn diện
        - Không thay thế sinh thiết gan khi cần thiết để chẩn đoán chính xác
        """)
        
        # Save to history
        calculation_data = {
            'calculator_id': 'apri',
            'calculator_name': 'APRI Score',
            'inputs': {
                'ast': ast,
                'platelet': platelet,
                'uln': uln
            },
            'results': {
                'apri': result['apri'],
                'fibrosis_stage': result['fibrosis_stage'],
                'risk_class': result['risk_class'],
                'recommendation': result['recommendation']
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share results
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
    
    # References
    st.divider()
    references = get_references('apri')
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        - Wai CT, et al. A simple noninvasive index can predict both significant fibrosis 
          and cirrhosis in patients with chronic hepatitis C. Hepatology. 2003;38(2):518-526.
        """)
    
    # History
    render_history_ui(calculator_id="apri", show_actions=True)
