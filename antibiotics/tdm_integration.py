"""
TDM Integration for Antibiotics - Phase 5
Tích hợp Therapeutic Drug Monitoring vào antibiotics module
"""

import streamlit as st
from drugs.tdm.vancomycin_tdm import (
    calculate_vancomycin_auc,
    calculate_vancomycin_dose_auc_based,
    calculate_vancomycin_dose_trough_based,
    interpret_vancomycin_level
)


def render_tdm_calculator(antibiotic_name):
    """
    Render TDM calculator cho kháng sinh có TDM
    
    Args:
        antibiotic_name: Tên kháng sinh
    """
    if antibiotic_name != "Vancomycin":
        return  # Chỉ hỗ trợ Vancomycin hiện tại
    
    st.markdown("---")
    st.markdown("### 🧪 Therapeutic Drug Monitoring (TDM)")
    
    st.info("""
    **TDM cho Vancomycin:**
    - **Phương pháp ưu tiên:** AUC-based dosing (400-600 mg·h/L)
    - **Phương pháp thay thế:** Trough-based dosing (10-20 mg/L)
    - **Thời điểm lấy mẫu:** Trough: trước liều tiếp theo (≥ 1 giờ sau khi truyền xong)
    """)
    
    # Tab selection
    tab1, tab2, tab3 = st.tabs(["📊 AUC-Based", "📊 Trough-Based", "🔍 Giải Thích Nồng Độ"])
    
    with tab1:
        st.markdown("#### 📋 AUC-Based Dosing (Ưu Tiên)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key=f"tdm_{antibiotic_name}_weight"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=5.0,
                max_value=150.0,
                value=60.0,
                step=5.0,
                key=f"tdm_{antibiotic_name}_crcl"
            )
        
        with col2:
            target_auc = st.number_input(
                "Mục tiêu AUC (mg·h/L)",
                min_value=300.0,
                max_value=700.0,
                value=500.0,
                step=50.0,
                key=f"tdm_{antibiotic_name}_target_auc",
                help="Thường 400-600 mg·h/L"
            )
            
            has_current_levels = st.checkbox(
                "Có nồng độ hiện tại?",
                key=f"tdm_{antibiotic_name}_has_levels"
            )
        
        if has_current_levels:
            st.markdown("---")
            st.markdown("#### 📊 Nồng Độ Hiện Tại")
            
            col1, col2 = st.columns(2)
            
            with col1:
                current_peak = st.number_input(
                    "Peak (mg/L)",
                    min_value=0.0,
                    max_value=50.0,
                    value=25.0,
                    step=0.5,
                    key=f"tdm_{antibiotic_name}_peak"
                )
            
            with col2:
                current_trough = st.number_input(
                    "Trough (mg/L)",
                    min_value=0.0,
                    max_value=50.0,
                    value=15.0,
                    step=0.5,
                    key=f"tdm_{antibiotic_name}_trough"
                )
            
            # Calculate current AUC
            current_auc = calculate_vancomycin_auc(current_peak, current_trough)
            st.info(f"**AUC hiện tại:** {current_auc:.0f} mg·h/L")
        
        if st.button("🧮 Tính Liều (AUC-based)", type="primary", key=f"calc_auc_{antibiotic_name}"):
            result = calculate_vancomycin_dose_auc_based(
                weight_kg=weight,
                crcl=crcl,
                target_auc=target_auc,
                current_auc=current_auc if has_current_levels else None,
                current_dose_mg=None
            )
            
            if result:
                st.success("### 📊 Kết Quả")
                st.metric("Liều khuyến cáo", f"{result.get('dose_mg', 0):.0f} mg")
                st.metric("Tần suất", f"Mỗi {result.get('frequency_hours', 0):.0f} giờ")
                if result.get('loading_dose_mg'):
                    st.info(f"**Loading dose:** {result['loading_dose_mg']:.0f} mg")
    
    with tab2:
        st.markdown("#### 📋 Trough-Based Dosing")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key=f"tdm_trough_{antibiotic_name}_weight"
            )
            
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=5.0,
                max_value=150.0,
                value=60.0,
                step=5.0,
                key=f"tdm_trough_{antibiotic_name}_crcl"
            )
        
        with col2:
            target_trough = st.number_input(
                "Mục tiêu Trough (mg/L)",
                min_value=5.0,
                max_value=25.0,
                value=15.0,
                step=1.0,
                key=f"tdm_trough_{antibiotic_name}_target",
                help="Thường 10-20 mg/L"
            )
            
            has_current_trough = st.checkbox(
                "Có trough hiện tại?",
                key=f"tdm_trough_{antibiotic_name}_has_trough"
            )
        
        if has_current_trough:
            current_trough = st.number_input(
                "Trough hiện tại (mg/L)",
                min_value=0.0,
                max_value=50.0,
                value=15.0,
                step=0.5,
                key=f"tdm_trough_{antibiotic_name}_current"
            )
            
            current_dose = st.number_input(
                "Liều hiện tại (mg)",
                min_value=0.0,
                max_value=3000.0,
                value=1000.0,
                step=250.0,
                key=f"tdm_trough_{antibiotic_name}_dose"
            )
        else:
            current_trough = None
            current_dose = None
        
        if st.button("🧮 Tính Liều (Trough-based)", type="primary", key=f"calc_trough_{antibiotic_name}"):
            result = calculate_vancomycin_dose_trough_based(
                weight_kg=weight,
                crcl=crcl,
                target_trough=target_trough,
                current_trough=current_trough,
                current_dose_mg=current_dose
            )
            
            if result:
                st.success("### 📊 Kết Quả")
                st.metric("Liều khuyến cáo", f"{result.get('dose_mg', 0):.0f} mg")
                st.metric("Tần suất", f"Mỗi {result.get('frequency_hours', 0):.0f} giờ")
                if result.get('loading_dose_mg'):
                    st.info(f"**Loading dose:** {result['loading_dose_mg']:.0f} mg")
    
    with tab3:
        st.markdown("#### 🔍 Giải Thích Nồng Độ")
        
        col1, col2 = st.columns(2)
        
        with col1:
            trough = st.number_input(
                "Trough (mg/L)",
                min_value=0.0,
                max_value=50.0,
                value=15.0,
                step=0.5,
                key=f"interpret_{antibiotic_name}_trough"
            )
        
        with col2:
            peak = st.number_input(
                "Peak (mg/L) - Tùy chọn",
                min_value=0.0,
                max_value=50.0,
                value=0.0,
                step=0.5,
                key=f"interpret_{antibiotic_name}_peak"
            )
        
        if st.button("🔍 Giải Thích", type="primary", key=f"interpret_{antibiotic_name}"):
            interpretation = interpret_vancomycin_level(
                trough_mg_l=trough if trough > 0 else None,
                peak_mg_l=peak if peak > 0 else None
            )
            
            if interpretation:
                for result in interpretation:
                    color = result.get('color', 'info')
                    level_text = result.get('level_text', '')
                    recommendation = result.get('recommendation', '')
                    
                    if color == 'error':
                        st.error(f"**{level_text}**\n\n{recommendation}")
                    elif color == 'warning':
                        st.warning(f"**{level_text}**\n\n{recommendation}")
                    elif color == 'success':
                        st.success(f"**{level_text}**\n\n{recommendation}")
                    else:
                        st.info(f"**{level_text}**\n\n{recommendation}")

