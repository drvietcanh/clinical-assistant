"""
Mean Arterial Pressure (MAP) Calculator
Tính huyết áp trung bình động mạch
"""

import streamlit as st
from scores.utils.validation import validate_range
from components.ui.validation import render_validation_errors
from components.ui.results import render_result_box
from scores.references_config import get_references
from components.references import render_references_section
from components.calculation_history import save_calculation_to_history, render_history_ui
from components.share_results import render_share_section, load_shared_result_from_url
from components.smart_suggestions import render_suggestions
from components.export import render_export_section


def calculate_map(sbp, dbp):
    """
    Calculate Mean Arterial Pressure
    
    Formula: MAP = DBP + 1/3(SBP - DBP)
    Alternative: MAP = (2 × DBP + SBP) / 3
    
    Args:
        sbp: Systolic Blood Pressure (mmHg)
        dbp: Diastolic Blood Pressure (mmHg)
    
    Returns:
        MAP in mmHg
    """
    map_value = dbp + (1/3) * (sbp - dbp)
    return map_value


def interpret_map(map_value):
    """
    Interpret MAP value
    
    Returns:
        dict with interpretation and recommendations
    """
    if map_value < 60:
        return {
            "status": "🔴 Nguy hiểm",
            "interpretation": "MAP < 60 mmHg - Thiếu máu cơ quan",
            "recommendations": [
                "Cần hồi sức ngay lập tức",
                "Đánh giá tình trạng sốc",
                "Xem xét truyền dịch và/hoặc vận mạch",
                "Theo dõi lactate, ScvO2"
            ]
        }
    elif map_value < 70:
        return {
            "status": "🟡 Thấp",
            "interpretation": "MAP 60-70 mmHg - Có thể thiếu máu cơ quan",
            "recommendations": [
                "Theo dõi sát dấu hiệu sốc",
                "Đánh giá thể tích tuần hoàn",
                "Xem xét hỗ trợ vận mạch nếu cần"
            ]
        }
    elif map_value <= 100:
        return {
            "status": "🟢 Bình thường",
            "interpretation": "MAP 70-100 mmHg - Bình thường",
            "recommendations": [
                "Duy trì MAP trong khoảng này",
                "Theo dõi huyết áp định kỳ"
            ]
        }
    elif map_value <= 110:
        return {
            "status": "🟡 Cao nhẹ",
            "interpretation": "MAP 100-110 mmHg - Cao nhẹ",
            "recommendations": [
                "Theo dõi huyết áp",
                "Đánh giá nguy cơ tim mạch"
            ]
        }
    else:
        return {
            "status": "🔴 Tăng huyết áp",
            "interpretation": "MAP > 110 mmHg - Tăng huyết áp",
            "recommendations": [
                "Đánh giá tăng huyết áp",
                "Xem xét điều trị nếu có triệu chứng",
                "Theo dõi biến chứng tim mạch"
            ]
        }


def render():
    """Render MAP calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>❤️ Mean Arterial Pressure (MAP)</h2>
    <p style='text-align: center;'><em>Huyết áp trung bình động mạch</em></p>
    """, unsafe_allow_html=True)
    
    shared = load_shared_result_from_url()
    if shared and shared.get("calculator_id") == "map":
        st.info(f"📥 Đã tải kết quả chia sẻ: {shared.get('calculator_name', 'MAP')}")
    
    with st.expander("ℹ️ Giới thiệu về MAP"):
        st.markdown("""
        **Mean Arterial Pressure (MAP)** là **huyết áp trung bình** trong một chu kỳ tim.
        
        **Mục đích:**
        - ✅ Đánh giá tưới máu cơ quan
        - ✅ Mục tiêu hồi sức trong sốc
        - ✅ Đánh giá hiệu quả điều trị tăng huyết áp
        
        **Công thức:**
        ```
        MAP = DBP + 1/3(SBP - DBP)
        MAP = (2 × DBP + SBP) / 3
        ```
        
        **Giá trị bình thường:**
        - **70-100 mmHg** - Bình thường
        - **< 60 mmHg** - Thiếu máu cơ quan (nguy hiểm)
        - **> 110 mmHg** - Tăng huyết áp
        
        **Ứng dụng lâm sàng:**
        - **Sốc:** MAP ≥ 65 mmHg là mục tiêu hồi sức
        - **ICU:** MAP 65-70 mmHg thường đủ để tưới máu cơ quan
        - **Tăng huyết áp:** MAP > 110 mmHg cần đánh giá điều trị
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sbp = st.number_input(
            "Systolic BP (SBP) - mmHg",
            min_value=40,
            max_value=300,
            value=120,
            step=1,
            help="Huyết áp tâm thu"
        )
    
    with col2:
        dbp = st.number_input(
            "Diastolic BP (DBP) - mmHg",
            min_value=20,
            max_value=200,
            value=80,
            step=1,
            help="Huyết áp tâm trương"
        )
    
    # Validation
    errors = []
    if dbp >= sbp:
        errors.append("DBP phải nhỏ hơn SBP")
    
    if errors:
        render_validation_errors(errors)
        st.stop()
    
    st.markdown("---")
    
    # Calculate
    if st.button("🧮 Tính MAP", type="primary", use_container_width=True):
        map_value = calculate_map(sbp, dbp)
        interpretation = interpret_map(map_value)
        
        # Display results
        st.subheader("📊 Kết quả")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            render_result_box(
                title="Mean Arterial Pressure (MAP)",
                value=f"{map_value:.1f}",
                unit="mmHg",
                status=interpretation["status"]
            )
        
        with col2:
            st.metric("SBP", f"{sbp} mmHg")
            st.metric("DBP", f"{dbp} mmHg")
        
        # Interpretation
        st.info(f"**{interpretation['interpretation']}**")
        
        # Recommendations
        if interpretation["recommendations"]:
            st.subheader("💡 Khuyến cáo lâm sàng")
            for rec in interpretation["recommendations"]:
                st.markdown(f"- {rec}")
        
        # Formula
        with st.expander("📐 Công thức"):
            st.markdown(f"""
            **Công thức:**
            ```
            MAP = DBP + 1/3(SBP - DBP)
            MAP = {dbp} + 1/3({sbp} - {dbp})
            MAP = {dbp} + {((sbp - dbp) / 3):.2f}
            MAP = {map_value:.1f} mmHg
            ```
            """)
        
        # Save to history
        calculation_data = {
            "calculator_id": "map",
            "calculator_name": "Mean Arterial Pressure (MAP)",
            "inputs": {
                "SBP": f"{sbp} mmHg",
                "DBP": f"{dbp} mmHg"
            },
            "results": {
                "MAP": f"{map_value:.1f} mmHg",
                "Interpretation": interpretation["interpretation"]
            }
        }
        save_calculation_to_history(calculation_data)
        
        # Share
        render_share_section(calculation_data)
        
        # Export
        render_export_section(calculation_data)
        
        # Suggestions
        render_suggestions("map", map_value)
    
    # History
    render_history_ui("map", "Mean Arterial Pressure (MAP)")
    
    # References
    references = get_references("map")
    if references:
        render_references_section(references)

