"""
Enhanced Unit Converter UI Component
Auto-detection and context-aware unit conversion
"""

import streamlit as st
from utils.unit_converter_enhanced import (
    detect_unit,
    convert_with_auto_detect,
    convert_value,
    get_available_units,
    format_unit_conversion_result
)
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert


# Context definitions
CONVERSION_CONTEXTS = {
    "creatinine": {
        "name": "Creatinine",
        "units": ["mg/dL", "µmol/L"],
        "description": "Chức năng thận"
    },
    "glucose": {
        "name": "Glucose",
        "units": ["mg/dL", "mmol/L"],
        "description": "Đường huyết"
    },
    "cholesterol": {
        "name": "Cholesterol",
        "units": ["mg/dL", "mmol/L"],
        "description": "Mỡ máu"
    },
    "bilirubin": {
        "name": "Bilirubin",
        "units": ["mg/dL", "µmol/L"],
        "description": "Chức năng gan"
    },
    "bun": {
        "name": "BUN (Urea)",
        "units": ["mg/dL", "mmol/L"],
        "description": "Chức năng thận"
    },
    "triglycerides": {
        "name": "Triglycerides",
        "units": ["mg/dL", "mmol/L"],
        "description": "Mỡ máu"
    },
    "hemoglobin": {
        "name": "Hemoglobin",
        "units": ["g/dL", "g/L"],
        "description": "Huyết học"
    },
    "albumin": {
        "name": "Albumin",
        "units": ["g/dL", "g/L"],
        "description": "Chức năng gan"
    }
}


def render_enhanced_unit_converter():
    """Render enhanced unit converter interface."""
    
    st.markdown("## 🔄 Enhanced Unit Converter")
    st.markdown("""
    Chuyển đổi đơn vị y khoa với auto-detection và context-aware conversion.
    
    **Tính năng:**
    - Tự động phát hiện đơn vị từ input
    - Chuyển đổi theo ngữ cảnh (context-aware)
    - Hỗ trợ nhiều loại đơn vị y khoa
    """)
    
    st.markdown("---")
    
    # Tab 1: Auto-detection
    tab1, tab2 = st.tabs([
        "🔍 Auto-Detection",
        "📊 Manual Conversion"
    ])
    
    # Tab 1: Auto-detection
    with tab1:
        st.markdown("### 🔍 Auto-Detection Mode")
        st.caption("Nhập giá trị kèm đơn vị, hệ thống sẽ tự động phát hiện và chuyển đổi")
        
        col1, col2 = st.columns(2)
        
        with col1:
            input_value = st.text_input(
                "**Nhập giá trị (kèm đơn vị):**",
                value="5.2 mg/dL",
                key="unit_auto_input",
                help="Ví dụ: '5.2 mg/dL', '120 µmol/L', '6.5 mmol/L'"
            )
        
        with col2:
            context = st.selectbox(
                "**Context (tùy chọn):**",
                ["None"] + list(CONVERSION_CONTEXTS.keys()),
                format_func=lambda x: "Tự động phát hiện" if x == "None" else CONVERSION_CONTEXTS[x]["name"],
                key="unit_auto_context"
            )
        
        if st.button("🔄 Chuyển đổi", key="unit_auto_convert", type="primary"):
            try:
                # Detect unit
                detected_context = None if context == "None" else context
                detected = detect_unit(input_value, detected_context)
                
                if not detected:
                    st.error("Không thể phát hiện đơn vị. Vui lòng nhập đúng định dạng (ví dụ: '5.2 mg/dL')")
                else:
                    value, from_unit = detected
                    
                    if from_unit is None:
                        st.warning("Đã phát hiện số nhưng không phát hiện được đơn vị. Vui lòng chọn context hoặc nhập đầy đủ.")
                    else:
                        st.markdown("---")
                        st.markdown("### 📊 Kết quả phát hiện")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            render_result_box(
                                "Giá trị",
                                f"{value:.2f}",
                                color="primary"
                            )
                        with col2:
                            render_result_box(
                                "Đơn vị phát hiện",
                                from_unit,
                                color="info"
                            )
                        
                        # Get available units for conversion
                        if detected_context:
                            available_units = get_available_units(detected_context)
                            if len(available_units) > 1:
                                target_unit = st.selectbox(
                                    "**Chuyển đổi sang:**",
                                    [u for u in available_units if u != from_unit],
                                    key="unit_auto_target"
                                )
                                
                                if st.button("🔄 Thực hiện chuyển đổi", key="unit_auto_execute"):
                                    converted = convert_value(value, from_unit, target_unit, detected_context)
                                    
                                    st.markdown("---")
                                    st.markdown("### ✅ Kết quả chuyển đổi")
                                    
                                    result_str = format_unit_conversion_result(
                                        value, from_unit, target_unit, converted
                                    )
                                    
                                    render_result_box(
                                        "Kết quả",
                                        result_str,
                                        color="success",
                                        icon="✅"
                                    )
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 2: Manual conversion
    with tab2:
        st.markdown("### 📊 Manual Conversion Mode")
        st.caption("Chọn context và đơn vị để chuyển đổi")
        
        # Context selection
        context = st.selectbox(
            "**Chọn loại xét nghiệm:**",
            list(CONVERSION_CONTEXTS.keys()),
            format_func=lambda x: f"{CONVERSION_CONTEXTS[x]['name']} - {CONVERSION_CONTEXTS[x]['description']}",
            key="unit_manual_context"
        )
        
        context_info = CONVERSION_CONTEXTS[context]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            value = st.number_input(
                "**Giá trị:**",
                min_value=0.0,
                max_value=10000.0,
                value=5.2,
                step=0.1,
                format="%.2f",
                key="unit_manual_value"
            )
        
        with col2:
            from_unit = st.selectbox(
                "**Từ đơn vị:**",
                context_info["units"],
                key="unit_manual_from"
            )
        
        with col3:
            to_unit = st.selectbox(
                "**Sang đơn vị:**",
                [u for u in context_info["units"] if u != from_unit],
                key="unit_manual_to"
            )
        
        if st.button("🔄 Chuyển đổi", key="unit_manual_convert", type="primary"):
            try:
                converted = convert_value(value, from_unit, to_unit, context)
                
                st.markdown("---")
                st.markdown("### ✅ Kết quả")
                
                result_str = format_unit_conversion_result(
                    value, from_unit, to_unit, converted
                )
                
                render_result_box(
                    "Kết quả chuyển đổi",
                    result_str,
                    color="success",
                    icon="✅"
                )
                
                # Show conversion formula if available
                with st.expander("ℹ️ Thông tin chuyển đổi"):
                    st.markdown(f"**Context:** {context_info['name']}")
                    st.markdown(f"**Mô tả:** {context_info['description']}")
                    st.markdown(f"**Đơn vị hỗ trợ:** {', '.join(context_info['units'])}")
                
            except ValueError as e:
                st.error(f"Lỗi chuyển đổi: {str(e)}")
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Quick reference
    with st.expander("📋 Bảng tham khảo nhanh"):
        import pandas as pd
        
        ref_data = []
        for ctx_key, ctx_info in CONVERSION_CONTEXTS.items():
            ref_data.append({
                "Loại": ctx_info["name"],
                "Mô tả": ctx_info["description"],
                "Đơn vị": ", ".join(ctx_info["units"])
            })
        
        df = pd.DataFrame(ref_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Disclaimer
    st.markdown("---")
    st.info("""
    **ℹ️ Lưu ý:**
    - Auto-detection hoạt động tốt nhất khi nhập đầy đủ đơn vị (ví dụ: "5.2 mg/dL")
    - Chọn context giúp tăng độ chính xác phát hiện
    - Công thức chuyển đổi dựa trên tiêu chuẩn y khoa quốc tế
    """)

