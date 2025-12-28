"""
Time Remaining Calculator UI Component
Calculate remaining time for infusion
"""

import streamlit as st
from critical_care.time_remaining import calculate_remaining_time
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert


def render_time_remaining_calculator():
    """Render time remaining calculator interface."""
    
    st.markdown("## ⏰ Time Remaining Calculator")
    st.markdown("""
    Tính thời gian còn lại của dịch truyền.
    
    **Tính năng:**
    - Tính thời gian còn lại
    - Hiển thị % đã truyền
    - Cảnh báo khi sắp hết
    - Progress bar
    """)
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2 = st.tabs([
        "⏰ Thời gian còn lại",
        "📊 Tính từ thể tích và tốc độ"
    ])
    
    # Tab 1: Remaining time
    with tab1:
        st.markdown("### ⏰ Tính thời gian còn lại")
        st.caption("Tính thời gian còn lại dựa trên thể tích đã truyền")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            initial_volume = st.number_input(
                "**Thể tích ban đầu (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=500.0,
                step=10.0,
                format="%.0f",
                key="time_initial_vol"
            )
        
        with col2:
            infused_volume = st.number_input(
                "**Thể tích đã truyền (ml):**",
                min_value=0.0,
                max_value=10000.0,
                value=250.0,
                step=10.0,
                format="%.0f",
                key="time_infused_vol"
            )
        
        with col3:
            current_rate = st.number_input(
                "**Tốc độ hiện tại (ml/h):**",
                min_value=0.1,
                max_value=1000.0,
                value=50.0,
                step=1.0,
                format="%.1f",
                key="time_current_rate"
            )
        
        if st.button("🧮 Tính toán", key="time_calculate", type="primary"):
            try:
                result = calculate_remaining_time(
                    initial_volume,
                    infused_volume,
                    current_rate
                )
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                # Progress bar
                st.markdown("**Tiến độ truyền:**")
                st.progress(result["percent_infused"] / 100)
                st.caption(f"Đã truyền: {result['percent_infused']:.1f}% | Còn lại: {result['percent_remaining']:.1f}%")
                
                # Metrics
                metrics = [
                    {
                        "label": "Thể tích còn lại",
                        "value": f"{result['remaining_volume_ml']:.1f} ml",
                        "icon": "💧"
                    },
                    {
                        "label": "Thời gian còn lại",
                        "value": result["remaining_time_formatted"],
                        "icon": "⏰"
                    },
                    {
                        "label": "Đã truyền",
                        "value": f"{result['percent_infused']:.1f}%",
                        "icon": "📊"
                    }
                ]
                
                render_result_card("Kết quả", metrics, color="primary")
                
                # Warning
                if result.get("warning"):
                    render_warning_alert(result["warning"], title="⚠️ Cảnh báo")
                
                # Additional info
                st.markdown("---")
                col1, col2 = st.columns(2)
                with col1:
                    render_result_box(
                        "Thể tích đã truyền",
                        f"{infused_volume:.0f} ml",
                        color="info"
                    )
                with col2:
                    render_result_box(
                        "Thể tích còn lại",
                        f"{result['remaining_volume_ml']:.1f} ml",
                        color="warning"
                    )
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")
    
    # Tab 2: Calculate from volume and rate
    with tab2:
        st.markdown("### 📊 Tính thời gian từ thể tích và tốc độ")
        st.caption("Tính thời gian cần để truyền hết một thể tích")
        
        col1, col2 = st.columns(2)
        
        with col1:
            volume_ml = st.number_input(
                "**Thể tích cần truyền (ml):**",
                min_value=1.0,
                max_value=10000.0,
                value=500.0,
                step=10.0,
                format="%.0f",
                key="time_vol"
            )
        
        with col2:
            rate_ml_hour = st.number_input(
                "**Tốc độ truyền (ml/h):**",
                min_value=0.1,
                max_value=1000.0,
                value=50.0,
                step=1.0,
                format="%.1f",
                key="time_rate"
            )
        
        if st.button("🧮 Tính toán", key="time_calc2", type="primary"):
            try:
                from critical_care.enhanced_infusion import calculate_infusion_time
                result = calculate_infusion_time(volume_ml, rate_ml_hour)
                
                st.markdown("---")
                st.markdown("### 📊 Kết quả")
                
                metrics = [
                    {
                        "label": "Thời gian",
                        "value": result["time_formatted"],
                        "icon": "⏰"
                    },
                    {
                        "label": "Giờ",
                        "value": f"{result['time_hours']:.2f} giờ",
                        "icon": "🕐"
                    },
                    {
                        "label": "Phút",
                        "value": f"{result['time_minutes']:.1f} phút",
                        "icon": "⏱️"
                    }
                ]
                
                render_result_card("Thời gian truyền", metrics, color="primary")
                
            except ValueError as e:
                st.error(f"Lỗi: {str(e)}")

