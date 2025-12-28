"""
FIB-4 Index for Liver Fibrosis
Đánh giá mức độ xơ hóa gan không xâm lấn
"""

import streamlit as st
from scores.utils.validation import validate_range, validate_age, validate_lab_value
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def calculate_fib4(age, ast, alt, platelets):
    """
    Calculate FIB-4 Index
    
    Formula: FIB-4 = (Age × AST) / (Platelets × √ALT)
    
    Args:
        age: Age in years
        ast: AST (U/L)
        alt: ALT (U/L)
        platelets: Platelet count (×10³/µL or ×10⁹/L)
    
    Returns:
        FIB-4 index value
    """
    import math
    
    # Ensure ALT > 0 to avoid division by zero
    if alt <= 0:
        return None
    
    fib4 = (age * ast) / (platelets * math.sqrt(alt))
    return fib4


def interpret_fib4(fib4_value, etiology="HCV"):
    """
    Interpret FIB-4 value
    
    Args:
        fib4_value: FIB-4 index
        etiology: "HCV", "HBV", or "NAFLD"
    
    Returns:
        dict with interpretation
    """
    if etiology == "HCV":
        if fib4_value < 1.45:
            return {
                "status": "🟢 Thấp",
                "interpretation": "FIB-4 < 1.45 - Xơ hóa không đáng kể (F0-F1)",
                "risk": "Thấp",
                "recommendations": [
                    "Theo dõi định kỳ",
                    "Có thể trì hoãn sinh thiết gan"
                ]
            }
        elif fib4_value < 3.25:
            return {
                "status": "🟡 Trung bình",
                "interpretation": "FIB-4 1.45-3.25 - Xơ hóa trung bình (F2-F3)",
                "risk": "Trung bình",
                "recommendations": [
                    "Cân nhắc sinh thiết gan hoặc đánh giá thêm",
                    "Theo dõi sát hơn",
                    "Xem xét điều trị"
                ]
            }
        else:
            return {
                "status": "🔴 Cao",
                "interpretation": "FIB-4 ≥ 3.25 - Xơ hóa nặng/xơ gan (F4)",
                "risk": "Cao",
                "recommendations": [
                    "Cân nhắc sinh thiết gan để xác nhận",
                    "Điều trị tích cực",
                    "Theo dõi biến chứng xơ gan",
                    "Tầm soát ung thư gan"
                ]
            }
    elif etiology == "HBV":
        if fib4_value < 1.45:
            return {
                "status": "🟢 Thấp",
                "interpretation": "FIB-4 < 1.45 - Xơ hóa không đáng kể",
                "risk": "Thấp",
                "recommendations": ["Theo dõi định kỳ"]
            }
        elif fib4_value < 3.25:
            return {
                "status": "🟡 Trung bình",
                "interpretation": "FIB-4 1.45-3.25 - Xơ hóa trung bình",
                "risk": "Trung bình",
                "recommendations": ["Cân nhắc đánh giá thêm", "Xem xét điều trị"]
            }
        else:
            return {
                "status": "🔴 Cao",
                "interpretation": "FIB-4 ≥ 3.25 - Xơ hóa nặng/xơ gan",
                "risk": "Cao",
                "recommendations": ["Điều trị tích cực", "Theo dõi biến chứng"]
            }
    else:  # NAFLD
        if fib4_value < 1.30:
            return {
                "status": "🟢 Thấp",
                "interpretation": "FIB-4 < 1.30 - Xơ hóa không đáng kể",
                "risk": "Thấp",
                "recommendations": ["Theo dõi định kỳ"]
            }
        elif fib4_value < 2.67:
            return {
                "status": "🟡 Trung bình",
                "interpretation": "FIB-4 1.30-2.67 - Xơ hóa trung bình",
                "risk": "Trung bình",
                "recommendations": ["Cân nhắc đánh giá thêm"]
            }
        else:
            return {
                "status": "🔴 Cao",
                "interpretation": "FIB-4 ≥ 2.67 - Xơ hóa nặng/xơ gan",
                "risk": "Cao",
                "recommendations": ["Điều trị tích cực", "Theo dõi biến chứng"]
            }


def render():
    """Render FIB-4 calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🩸 FIB-4 Index for Liver Fibrosis</h2>
    <p style='text-align: center;'><em>Đánh giá mức độ xơ hóa gan không xâm lấn</em></p>
    """, unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "fib4":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'FIB-4 Index')}")
    
    with st.expander("ℹ️ Giới thiệu về FIB-4 Index"):
        st.markdown("""
        **FIB-4 Index** là chỉ số đánh giá **xơ hóa gan không xâm lấn**, đặc biệt hữu ích trong viêm gan C, B và NAFLD.
        
        **Công thức:**
        ```
        FIB-4 = (Age × AST) / (Platelets × √ALT)
        ```
        
        **Ngưỡng cho HCV:**
        - **< 1.45:** Xơ hóa không đáng kể (F0-F1) - Nguy cơ thấp
        - **1.45-3.25:** Xơ hóa trung bình (F2-F3) - Nguy cơ trung bình
        - **≥ 3.25:** Xơ hóa nặng/xơ gan (F4) - Nguy cơ cao
        
        **Ngưỡng cho NAFLD:**
        - **< 1.30:** Xơ hóa không đáng kể
        - **1.30-2.67:** Xơ hóa trung bình
        - **≥ 2.67:** Xơ hóa nặng/xơ gan
        
        **Ưu điểm:**
        - Đơn giản, không xâm lấn
        - Sử dụng xét nghiệm thường quy
        - Hữu ích để quyết định sinh thiết gan
        
        **Nhược điểm:**
        - Độ chính xác thay đổi theo nguyên nhân
        - Có thể không chính xác ở người cao tuổi
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    etiology = st.radio(
        "Nguyên nhân bệnh gan",
        options=["HCV", "HBV", "NAFLD"],
        index=0,
        horizontal=True,
        help="Chọn nguyên nhân để áp dụng ngưỡng phù hợp"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=50,
            step=1
        )
        
        ast = st.number_input(
            "AST (U/L)",
            min_value=1.0,
            max_value=5000.0,
            value=40.0,
            step=1.0,
            format="%.0f",
            help="Aspartate Aminotransferase"
        )
    
    with col2:
        alt = st.number_input(
            "ALT (U/L)",
            min_value=1.0,
            max_value=5000.0,
            value=40.0,
            step=1.0,
            format="%.0f",
            help="Alanine Aminotransferase"
        )
        
        platelets = st.number_input(
            "Tiểu cầu (×10³/µL hoặc ×10⁹/L)",
            min_value=10.0,
            max_value=1000.0,
            value=200.0,
            step=1.0,
            format="%.0f",
            help="Platelet count"
        )
    
    st.markdown("---")
    
    # Validation
    errors = []
    if alt <= 0:
        errors.append("ALT phải lớn hơn 0")
    if platelets <= 0:
        errors.append("Tiểu cầu phải lớn hơn 0")
    
    if errors:
        render_validation_errors(errors)
        st.stop()
    
    # Calculate
    if st.button("🧮 Tính FIB-4", type="primary", use_container_width=True):
        fib4_value = calculate_fib4(age, ast, alt, platelets)
        interpretation = interpret_fib4(fib4_value, etiology)
        
        st.subheader("📊 Kết quả")
        
        render_result_box(
            title="FIB-4 Index",
            value=f"{fib4_value:.2f}",
            unit="",
            status=interpretation["status"]
        )
        
        # Interpretation
        st.info(f"**{interpretation['interpretation']}**")
        st.info(f"**Nguy cơ xơ hóa:** {interpretation['risk']}")
        
        # Formula
        with st.expander("📐 Công thức"):
            import math
            st.markdown(f"""
            **Công thức:**
            ```
            FIB-4 = (Age × AST) / (Platelets × √ALT)
            FIB-4 = ({age} × {ast}) / ({platelets} × √{alt})
            FIB-4 = {age * ast} / ({platelets} × {math.sqrt(alt):.2f})
            FIB-4 = {age * ast} / {platelets * math.sqrt(alt):.2f}
            FIB-4 = {fib4_value:.2f}
            ```
            """)
        
        # Recommendations
        st.subheader("💡 Khuyến cáo lâm sàng")
        for rec in interpretation["recommendations"]:
            st.markdown(f"- {rec}")
        
        # Additional notes
        st.info("""
        **Lưu ý:**
        - FIB-4 là công cụ sàng lọc, không thay thế sinh thiết gan
        - Kết hợp với lâm sàng và các xét nghiệm khác
        - Theo dõi định kỳ để đánh giá tiến triển
        """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "fib4",
            "calculator_name": "FIB-4 Index for Liver Fibrosis",
            "inputs": {
                "Tuổi": f"{age} năm",
                "AST": f"{ast} U/L",
                "ALT": f"{alt} U/L",
                "Tiểu cầu": f"{platelets} ×10³/µL",
                "Nguyên nhân": etiology
            },
            "results": {
                "FIB-4 Index": f"{fib4_value:.2f}",
                "Diễn giải": interpretation["interpretation"],
                "Nguy cơ": interpretation["risk"]
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
        
        # Suggestions
        render_suggestions("fib4", fib4_value)
    
    # History
    render_history_ui("fib4", "FIB-4 Index for Liver Fibrosis")
    
    # References
    references = get_references("fib4")
    if references:
        render_references_section(references)

