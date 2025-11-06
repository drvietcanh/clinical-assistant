"""
Antibiotic Database - Quick Dosing Calculator
Compact dosing calculator embedded in antibiotic detail view
"""

import streamlit as st
import pandas as pd
from .dosing_calculator import (
    calculate_adjusted_dose,
    calculate_detailed_dose,
    calculate_ibw,
    calculate_abw,
    calculate_bmi
)

def render_quick_dosing_calculator(ab_name, ab_data, key_prefix=""):
    """
    Compact dosing calculator for embedding in antibiotic detail view
    Returns calculation result or None
    """
    # Sanitize key_prefix to ensure it's safe for session state
    from .database_display import _sanitize_key
    if key_prefix:
        # Extract the actual prefix part (before the last underscore if it ends with _)
        prefix_parts = key_prefix.rstrip('_').split('_')
        sanitized_parts = [_sanitize_key(part) for part in prefix_parts if part]
        key_prefix = '_'.join(sanitized_parts) + '_' if sanitized_parts else 'info_'
    else:
        key_prefix = 'info_'
    st.markdown("---")
    
    # Modern card header
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 15px 0 10px 0;
    '>
        <h4 style='margin: 0; color: white;'>🧮 Tính Liều Cho Bệnh Nhân</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Check for imported CrCl/eGFR
    imported_crcl = st.session_state.get('patient_crcl', None)
    imported_egfr = st.session_state.get('patient_egfr', None)
    
    # Compact input form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=10.0,
            max_value=200.0,
            value=70.0,
            step=1.0,
            key=f"{key_prefix}dosing_weight",
            help="Cân nặng thực tế của bệnh nhân"
        )
    
    with col2:
        # CrCl input with import option
        if imported_crcl:
            use_imported = st.checkbox(
                f"📥 Dùng CrCl đã tính: {imported_crcl:.1f}",
                value=True,
                key=f"{key_prefix}use_crcl"
            )
            if use_imported:
                crcl = imported_crcl
                st.caption(f"✅ {crcl:.1f} mL/min")
            else:
                crcl = st.number_input(
                    "CrCl (mL/min)",
                    min_value=0.0,
                    max_value=200.0,
                    value=float(imported_crcl),
                    step=1.0,
                    key=f"{key_prefix}crcl",
                    help="Creatinine Clearance"
                )
        else:
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=0.0,
                max_value=200.0,
                value=60.0,
                step=1.0,
                key=f"{key_prefix}crcl",
                help="Creatinine Clearance. Dùng eGFR Calculator để tính chính xác"
            )
    
    with col3:
        indication = st.selectbox(
            "Chỉ định:",
            ["Chuẩn", "Nhiễm khuẩn nặng", "Viêm màng não"],
            key=f"{key_prefix}indication",
            help="Loại nhiễm khuẩn"
        )
    
    # Calculate button
    if st.button(
        f"🧮 Tính Liều {ab_name}",
        type="primary",
        use_container_width=True,
        key=f"{key_prefix}calc_btn"
    ):
        indication_map = {
            "Chuẩn": "standard",
            "Nhiễm khuẩn nặng": "severe",
            "Viêm màng não": "meningitis"
        }
        indication_code = indication_map.get(indication, "standard")
        
        # Calculate adjusted dose
        result = calculate_adjusted_dose(
            ab_name,
            crcl,
            egfr=imported_egfr,
            indication=indication_code
        )
        
        if "error" not in result:
            # Store result in session for display
            st.session_state[f"{key_prefix}dosing_result"] = result
            st.session_state[f"{key_prefix}dosing_weight"] = weight
            st.session_state[f"{key_prefix}dosing_crcl"] = crcl
            st.session_state[f"{key_prefix}dosing_indication"] = indication_code
            st.rerun()
        else:
            st.error(result["error"])
    
    # Display results if available
    if f"{key_prefix}dosing_result" in st.session_state:
        result = st.session_state[f"{key_prefix}dosing_result"]
        weight_used = st.session_state.get(f"{key_prefix}dosing_weight", weight)
        crcl_used = st.session_state.get(f"{key_prefix}dosing_crcl", crcl)
        
        # Results card
        st.markdown("---")
        st.markdown("### 📊 Kết Quả Tính Liều:")
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("CrCl", f"{crcl_used:.1f} mL/min")
        with col2:
            renal_cat = result.get('renal_category', 'normal')
            cat_labels = {
                'normal': '✅ Bình thường',
                '30_60': '⚠️ Suy nhẹ-vừa',
                '15_30': '🔴 Suy nặng',
                'under_15': '🚨 Rất nặng'
            }
            st.metric("Phân loại", cat_labels.get(renal_cat, 'N/A'))
        with col3:
            if result.get('icu_factor', 1.0) > 1.0:
                st.metric("Hệ số ICU", f"x{result['icu_factor']:.2f}")
        
        # Adjustment recommendation
        st.success(f"**💡 Khuyến cáo:** {result['adjustment']}")
        
        # Detailed dose calculation
        height_default = 170  # Default for quick calc
        sex_default = "Nam"
        ibw = calculate_ibw(height_default, sex_default)
        bmi = calculate_bmi(weight_used, height_default)
        is_obese = bmi > 30 or weight_used > ibw * 1.25
        abw = calculate_abw(weight_used, ibw) if is_obese else weight_used
        
        detailed = calculate_detailed_dose(
            ab_name, weight_used, ibw, abw, crcl_used,
            indication=st.session_state.get(f"{key_prefix}dosing_indication", "standard"),
            is_pediatric=False
        )
        
        if detailed and detailed.get('calculated_dose_mg'):
            st.markdown("#### 💉 Liều Tính Được:")
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Liều:** {detailed['calculated_dose_mg']:.0f} mg")
            with col2:
                if detailed.get('interval_hours'):
                    st.info(f"**Khoảng cách:** Mỗi {detailed['interval_hours']:.0f} giờ")
        
        # Full renal guide
        if result.get('full_renal_guide'):
            with st.expander("📋 Bảng Điều Chỉnh Đầy Đủ", expanded=False):
                renal_guide = result['full_renal_guide']
                renal_table = []
                
                if 'normal' in renal_guide:
                    renal_table.append({"CrCl": "≥ 60", "Điều chỉnh": renal_guide['normal']})
                if '30_60' in renal_guide:
                    renal_table.append({"CrCl": "30-59", "Điều chỉnh": renal_guide['30_60']})
                if '15_30' in renal_guide:
                    renal_table.append({"CrCl": "15-29", "Điều chỉnh": renal_guide['15_30']})
                if 'under_15' in renal_guide:
                    renal_table.append({"CrCl": "< 15", "Điều chỉnh": renal_guide['under_15']})
                
                if renal_table:
                    st.dataframe(pd.DataFrame(renal_table), use_container_width=True, hide_index=True)
        
        # Link to full calculator
        st.info("💡 **Cần tính chi tiết hơn?** Dùng công cụ **'🧮 Tính Liều Theo eGFR/CrCl'** ở menu để nhập đầy đủ thông tin (chiều cao, giới tính, ICU, HD, etc.)")
        
        # Clear button
        if st.button("🗑️ Xóa kết quả", key=f"{key_prefix}clear_result"):
            keys_to_remove = [
                f"{key_prefix}dosing_result",
                f"{key_prefix}dosing_weight",
                f"{key_prefix}dosing_crcl",
                f"{key_prefix}dosing_indication"
            ]
            for key in keys_to_remove:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()



