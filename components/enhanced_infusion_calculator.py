"""
Enhanced Infusion Calculator UI Component
Comprehensive calculator for all infusion scenarios
"""

import streamlit as st
from critical_care.enhanced_infusion import (
    calculate_infusion_rate,
    calculate_volume_needed,
    calculate_dose_from_rate,
    calculate_infusion_time,
    calculate_drop_rate
)
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert


def render_enhanced_infusion_calculator():
    """Render enhanced infusion calculator interface."""
    
    st.markdown("## 💧 Enhanced Infusion Calculator")
    st.markdown("""
    Calculator toàn diện cho tính toán truyền dịch: tốc độ truyền, giọt/phút, thời gian, thể tích.
    
    **Tính năng:**
    - Tính tốc độ truyền từ liều
    - Tính thời gian truyền
    - Tính thể tích cần pha
    - Tính liều từ tốc độ (reverse)
    """)
    
    st.markdown("---")
    
    # Tabs for different calculations
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Tính tốc độ truyền",
        "⏰ Tính thời gian truyền",
        "💧 Tính thể tích cần pha",
        "🔄 Tính liều từ tốc độ",
        "⏰ Thời gian còn lại"
    ])
    
    # Tab 1: Calculate infusion rate
    with tab1:
        st.markdown("### 📊 Tính tốc độ truyền")
        st.caption("Tính tốc độ truyền (ml/h) và giọt/phút từ liều dùng")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            dose_mcg_kg_min = st.number_input(
                "**Liều (µg/kg/phút):**",
                min_value=0.01,
                max_value=100.0,
                value=0.1,
                step=0.01,
                format="%.2f",
                key="enh_inf_dose"
            )
        
        with col2:
            weight_kg = st.number_input(
                "**Cân nặng (kg):**",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_weight"
            )
        
        with col3:
            concentration_mcg_ml = st.number_input(
                "**Nồng độ pha (µg/ml):**",
                min_value=0.1,
                max_value=10000.0,
                value=4.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_conc",
                help="Ví dụ: 4 mcg/ml (1mg/250ml NS)"
            )
        
        # Drop factor
        use_drop_rate = st.checkbox("Tính giọt/phút", key="enh_inf_use_drop")
        drop_factor = None
        if use_drop_rate:
            drop_factor = st.selectbox(
                "**Drop factor (gtt/ml):**",
                [10, 15, 20, 60],
                index=2,  # Default 20
                key="enh_inf_drop_factor"
            )
        
        if st.button("🧮 Tính toán", key="enh_inf_calc_rate", type="primary"):
            try:
                result = calculate_infusion_rate(
                    dose_mcg_kg_min, weight_kg, concentration_mcg_ml, drop_factor
                )
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                metrics = [
                    {
                        "label": "Tổng liều/phút",
                        "value": f"{result['total_dose_mcg_min']:.2f} µg/min",
                        "icon": "⏱️"
                    },
                    {
                        "label": "Tổng liều/giờ",
                        "value": f"{result['total_dose_mcg_hour']:.2f} µg/h",
                        "icon": "💉"
                    },
                    {
                        "label": "Tốc độ truyền",
                        "value": f"{result['infusion_rate_ml_hour']:.2f} ml/h",
                        "icon": "💧"
                    }
                ]
                
                if result.get('drop_rate_gtt_min'):
                    metrics.append({
                        "label": "Giọt/phút",
                        "value": f"{result['drop_rate_gtt_min']:.1f} gtt/min",
                        "icon": "💧"
                    })
                
                render_result_card("Kết quả tính toán", metrics, color="primary")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 2: Calculate infusion time
    with tab2:
        st.markdown("### ⏰ Tính thời gian truyền")
        st.caption("Tính thời gian truyền từ thể tích và tốc độ")
        
        col1, col2 = st.columns(2)
        
        with col1:
            volume_ml = st.number_input(
                "**Thể tích (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=50.0,
                step=1.0,
                format="%.0f",
                key="enh_inf_time_vol"
            )
        
        with col2:
            rate_ml_hour = st.number_input(
                "**Tốc độ truyền (ml/h):**",
                min_value=0.1,
                max_value=1000.0,
                value=105.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_time_rate"
            )
        
        if st.button("🧮 Tính toán", key="enh_inf_calc_time", type="primary"):
            try:
                result = calculate_infusion_time(volume_ml, rate_ml_hour)
                
                st.markdown("---")
                st.markdown("### ⏰ Kết quả")
                
                render_result_box(
                    "Thời gian truyền",
                    result['time_formatted'],
                    color="info",
                    icon="⏱️"
                )
                
                st.markdown(f"**Chi tiết:** {result['time_hours']:.2f} giờ ({result['time_minutes']:.1f} phút)")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 3: Calculate volume needed
    with tab3:
        st.markdown("### 💧 Tính thể tích cần pha")
        st.caption("Tính thể tích cần pha cho thời gian truyền nhất định")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            dose_mcg_kg_min = st.number_input(
                "**Liều (µg/kg/phút):**",
                min_value=0.01,
                max_value=100.0,
                value=0.1,
                step=0.01,
                format="%.2f",
                key="enh_inf_vol_dose"
            )
        
        with col2:
            weight_kg = st.number_input(
                "**Cân nặng (kg):**",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_vol_weight"
            )
        
        with col3:
            duration_hours = st.number_input(
                "**Thời gian (giờ):**",
                min_value=0.1,
                max_value=168.0,
                value=24.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_vol_duration"
            )
        
        with col4:
            concentration_mcg_ml = st.number_input(
                "**Nồng độ (µg/ml):**",
                min_value=0.1,
                max_value=10000.0,
                value=4.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_vol_conc"
            )
        
        if st.button("🧮 Tính toán", key="enh_inf_calc_vol", type="primary"):
            try:
                result = calculate_volume_needed(
                    dose_mcg_kg_min, weight_kg, duration_hours, concentration_mcg_ml
                )
                
                st.markdown("---")
                st.markdown("### 💧 Kết quả")
                
                metrics = [
                    {
                        "label": "Tổng liều cần",
                        "value": f"{result['total_dose_mcg']:.2f} µg",
                        "icon": "💉"
                    },
                    {
                        "label": "Thể tích cần pha",
                        "value": f"{result['volume_ml']:.2f} ml",
                        "icon": "💧"
                    },
                    {
                        "label": "Tốc độ truyền",
                        "value": f"{result['infusion_rate_ml_hour']:.2f} ml/h",
                        "icon": "⏱️"
                    }
                ]
                
                render_result_card("Kết quả tính toán", metrics, color="primary")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 4: Calculate dose from rate (reverse)
    with tab4:
        st.markdown("### 🔄 Tính liều từ tốc độ truyền")
        st.caption("Tính liều dùng từ tốc độ truyền hiện tại (reverse calculation)")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            rate_ml_hour = st.number_input(
                "**Tốc độ truyền (ml/h):**",
                min_value=0.1,
                max_value=1000.0,
                value=105.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_rev_rate"
            )
        
        with col2:
            weight_kg = st.number_input(
                "**Cân nặng (kg):**",
                min_value=1.0,
                max_value=300.0,
                value=70.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_rev_weight"
            )
        
        with col3:
            concentration_mcg_ml = st.number_input(
                "**Nồng độ pha (µg/ml):**",
                min_value=0.1,
                max_value=10000.0,
                value=4.0,
                step=0.1,
                format="%.1f",
                key="enh_inf_rev_conc"
            )
        
        if st.button("🧮 Tính toán", key="enh_inf_calc_rev", type="primary"):
            try:
                result = calculate_dose_from_rate(
                    rate_ml_hour, weight_kg, concentration_mcg_ml
                )
                
                st.markdown("---")
                st.markdown("### 🔄 Kết quả")
                
                metrics = [
                    {
                        "label": "Liều dùng",
                        "value": f"{result['dose_mcg_kg_min']:.3f} µg/kg/phút",
                        "icon": "💉"
                    },
                    {
                        "label": "Tổng liều/phút",
                        "value": f"{result['total_dose_mcg_min']:.2f} µg/min",
                        "icon": "⏱️"
                    },
                    {
                        "label": "Tổng liều/giờ",
                        "value": f"{result['total_dose_mcg_hour']:.2f} µg/h",
                        "icon": "💊"
                    }
                ]
                
                render_result_card("Kết quả tính toán", metrics, color="primary")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 5: Time remaining
    with tab5:
        try:
            from components.time_remaining_calculator import render_time_remaining_calculator
            render_time_remaining_calculator()
        except ImportError:
            st.warning("Time Remaining Calculator chưa sẵn sàng.")
    
    # Disclaimer
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Kết quả tính toán chỉ mục đích tham khảo
    - Luôn kiểm tra lại tính toán trước khi sử dụng
    - Tuân thủ hướng dẫn của Bộ Y tế, Bệnh viện
    - Theo dõi sát bệnh nhân khi truyền dịch
    """)

