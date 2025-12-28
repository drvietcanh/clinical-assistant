"""
Titration Calculator UI Component
Guide for adjusting infusion rates
"""

import streamlit as st
from critical_care.titration_guide import (
    calculate_titration,
    add_titration_step,
    get_titration_summary
)
from drugs.cardiovascular_calculator import get_drug_names
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert


def render_titration_calculator():
    """Render titration calculator interface."""
    
    st.markdown("## 📈 Infusion Rate Titration Guide")
    st.markdown("""
    Hướng dẫn điều chỉnh tốc độ truyền dịch.
    
    **Tính năng:**
    - Tính tốc độ mới khi thay đổi liều
    - Theo dõi lịch sử điều chỉnh
    - Khuyến nghị an toàn
    """)
    
    st.markdown("---")
    
    # Initialize session state
    if "titration_history" not in st.session_state:
        st.session_state.titration_history = []
    
    # Get available drugs
    drug_names = get_drug_names()
    
    # Patient info
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="titration_weight"
        )
    
    with col2:
        selected_drug = st.selectbox(
            "**Thuốc:**",
            drug_names,
            key="titration_drug"
        )
    
    st.markdown("---")
    
    # Dose information
    st.markdown("### 💊 Thông tin liều")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        old_dose = st.number_input(
            "**Liều hiện tại (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=0.1,
            step=0.01,
            format="%.2f",
            key="titration_old_dose"
        )
    
    with col2:
        new_dose = st.number_input(
            "**Liều mới (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=0.15,
            step=0.01,
            format="%.2f",
            key="titration_new_dose"
        )
    
    with col3:
        reason = st.text_input(
            "**Lý do điều chỉnh (tùy chọn):**",
            value="",
            key="titration_reason",
            placeholder="Ví dụ: Huyết áp thấp, cần tăng liều"
        )
    
    # Infusion method
    infusion_method = st.radio(
        "**Phương pháp truyền:**",
        ["syringe_pump_50ml", "iv_bag_500ml"],
        format_func=lambda x: "Bơm tiêm điện (50ml)" if x == "syringe_pump_50ml" else "Chai truyền (500ml)",
        key="titration_method"
    )
    
    drop_factor = None
    if infusion_method == "iv_bag_500ml":
        drop_factor = st.selectbox(
            "**Drop factor (gtt/ml):**",
            [10, 15, 20, 60],
            index=2,
            key="titration_drop_factor"
        )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🧮 Tính điều chỉnh", key="titration_calculate", type="primary", use_container_width=True):
        try:
            # Calculate titration
            result = calculate_titration(
                selected_drug,
                old_dose,
                new_dose,
                weight_kg,
                infusion_method,
                drop_factor,
                reason if reason else None
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả điều chỉnh")
            
            # Display changes
            metrics = [
                {
                    "label": "Liều cũ",
                    "value": f"{result['old_dose']:.2f} µg/kg/phút",
                    "icon": "💊"
                },
                {
                    "label": "Liều mới",
                    "value": f"{result['new_dose']:.2f} µg/kg/phút",
                    "icon": "💉"
                },
                {
                    "label": "Thay đổi",
                    "value": f"{result['dose_change']:+.3f} µg/kg/phút ({result['dose_change_percent']:+.1f}%)",
                    "icon": "📈"
                }
            ]
            
            render_result_card("Thay đổi liều", metrics, color="primary")
            
            # Rate changes
            st.markdown("---")
            st.markdown("### 💧 Thay đổi tốc độ truyền")
            
            rate_metrics = [
                {
                    "label": "Tốc độ cũ",
                    "value": f"{result['old_rate_ml_hour']:.2f} ml/h",
                    "icon": "💧"
                },
                {
                    "label": "Tốc độ mới",
                    "value": f"{result['new_rate_ml_hour']:.2f} ml/h",
                    "icon": "💧"
                },
                {
                    "label": "Thay đổi",
                    "value": f"{result['rate_change_ml_hour']:+.2f} ml/h ({result['rate_change_percent']:+.1f}%)",
                    "icon": "📊"
                }
            ]
            
            render_result_card("Thay đổi tốc độ", rate_metrics, color="info")
            
            # Drop rate if applicable
            if result.get("old_drop_rate") and result.get("new_drop_rate"):
                st.markdown("---")
                col1, col2 = st.columns(2)
                with col1:
                    render_result_box(
                        "Giọt/phút cũ",
                        f"{result['old_drop_rate']:.1f} gtt/min",
                        color="info"
                    )
                with col2:
                    render_result_box(
                        "Giọt/phút mới",
                        f"{result['new_drop_rate']:.1f} gtt/min",
                        color="success"
                    )
            
            # Recommendations
            if result.get("recommendations"):
                st.markdown("---")
                st.markdown("### 💡 Khuyến nghị")
                for rec in result["recommendations"]:
                    if "⚠️" in rec:
                        render_warning_alert(rec.replace("⚠️ ", ""), title="⚠️ Cảnh báo")
                    else:
                        st.markdown(f"  • {rec}")
            
            # Add to history button
            st.markdown("---")
            if st.button("➕ Thêm vào lịch sử", key="titration_add_history", type="secondary"):
                step = add_titration_step(
                    st.session_state.titration_history,
                    selected_drug,
                    old_dose,
                    new_dose,
                    weight_kg,
                    infusion_method,
                    drop_factor,
                    reason if reason else None
                )
                st.success("Đã thêm vào lịch sử!")
                st.rerun()
            
        except ValueError as e:
            st.error(f"Lỗi: {str(e)}")
        except Exception as e:
            st.error(f"Lỗi không xác định: {str(e)}")
    
    # Titration history
    if st.session_state.titration_history:
        st.markdown("---")
        st.markdown("### 📋 Lịch sử điều chỉnh")
        
        # Summary
        summary = get_titration_summary(st.session_state.titration_history)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            render_result_box(
                "Số lần điều chỉnh",
                f"{summary['total_steps']} lần",
                color="primary"
            )
        with col2:
            render_result_box(
                "Liều ban đầu",
                f"{summary['initial_dose']:.3f} µg/kg/phút",
                color="info"
            )
        with col3:
            render_result_box(
                "Liều hiện tại",
                f"{summary['current_dose']:.3f} µg/kg/phút",
                color="success"
            )
        
        # Net change
        if summary['net_change'] != 0:
            st.markdown("---")
            change_color = "success" if summary['net_change'] > 0 else "error"
            render_result_box(
                "Thay đổi tổng",
                f"{summary['net_change']:+.3f} µg/kg/phút ({summary['net_change_percent']:+.1f}%)",
                color=change_color
            )
        
        # History table
        st.markdown("---")
        with st.expander("📊 Chi tiết lịch sử"):
            import pandas as pd
            
            history_data = []
            for idx, step in enumerate(st.session_state.titration_history, 1):
                history_data.append({
                    "Lần": idx,
                    "Liều cũ": f"{step['old_dose_mcg_kg_min']:.3f}",
                    "Liều mới": f"{step['new_dose_mcg_kg_min']:.3f}",
                    "Thay đổi": f"{step['dose_change']:+.3f}",
                    "Tốc độ cũ": f"{step['old_rate_ml_hour']:.2f} ml/h",
                    "Tốc độ mới": f"{step['new_rate_ml_hour']:.2f} ml/h",
                    "Lý do": step.get("reason", "-")
                })
            
            if history_data:
                df = pd.DataFrame(history_data)
                st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Clear history
        if st.button("🗑️ Xóa lịch sử", key="titration_clear_history", type="secondary"):
            st.session_state.titration_history = []
            st.success("Đã xóa lịch sử!")
            st.rerun()

