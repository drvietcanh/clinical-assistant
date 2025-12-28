"""
Pediatric Dosing Calculator UI Component
Calculate drug doses for pediatric patients
"""

import streamlit as st
from drugs.pediatric_dosing import (
    calculate_pediatric_infusion,
    validate_pediatric_dose,
    get_age_group,
    get_age_group_info,
    get_pediatric_dose_range
)
from drugs.cardiovascular_calculator import get_drug_names, get_drug_info
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


def render_pediatric_dosing_calculator():
    """Render pediatric dosing calculator interface."""
    
    st.markdown("## 👶 Pediatric Dosing Calculator")
    st.markdown("""
    Tính liều thuốc tim mạch cho bệnh nhân nhi.
    
    **Lưu ý:**
    - Liều pediatric thường thấp hơn người lớn
    - Trẻ sơ sinh cần liều thấp nhất
    - Theo dõi sát hơn ở trẻ em
    """)
    
    st.markdown("---")
    
    # Get available drugs
    drug_names = get_drug_names()
    
    # Patient information
    st.markdown("### 👤 Thông tin bệnh nhân")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age_input = st.radio(
            "**Nhập tuổi:**",
            ["Ngày", "Tháng", "Năm"],
            key="ped_age_type"
        )
    
    with col2:
        if age_input == "Ngày":
            age_value = st.number_input(
                "**Tuổi (ngày):**",
                min_value=0.0,
                max_value=365.0,
                value=30.0,
                step=1.0,
                format="%.0f",
                key="ped_age_days"
            )
            age_days = age_value
        elif age_input == "Tháng":
            age_months = st.number_input(
                "**Tuổi (tháng):**",
                min_value=0.0,
                max_value=24.0,
                value=6.0,
                step=0.5,
                format="%.1f",
                key="ped_age_months"
            )
            age_days = age_months * 30.44  # Average days per month
        else:  # Năm
            age_years = st.number_input(
                "**Tuổi (năm):**",
                min_value=0.0,
                max_value=18.0,
                value=5.0,
                step=0.5,
                format="%.1f",
                key="ped_age_years"
            )
            age_days = age_years * 365.25
    
    with col3:
        weight_kg = st.number_input(
            "**Cân nặng (kg):**",
            min_value=0.1,
            max_value=100.0,
            value=10.0,
            step=0.1,
            format="%.1f",
            key="ped_weight"
        )
    
    # Display age group
    age_group = get_age_group(age_days)
    age_group_info = get_age_group_info(age_group)
    
    if age_group_info:
        st.info(f"**Nhóm tuổi:** {age_group_info.get('description', age_group)} ({age_group_info.get('age_range', '')})")
    
    st.markdown("---")
    
    # Drug selection
    st.markdown("### 💊 Chọn thuốc và liều")
    
    col1, col2 = st.columns(2)
    
    with col1:
        selected_drug = st.selectbox(
            "**Thuốc:**",
            drug_names,
            key="ped_drug"
        )
    
    with col2:
        # Get recommended dose range
        dose_info = get_pediatric_dose_range(selected_drug, age_group)
        if dose_info:
            recommended_dose = dose_info.get("initial_dose", "0.05–0.1")
            # Extract first value from range
            try:
                initial_dose_value = float(recommended_dose.split("–")[0].split()[0])
            except (ValueError, IndexError):
                initial_dose_value = 0.1
        else:
            initial_dose_value = 0.1
        
        dose_mcg_kg_min = st.number_input(
            "**Liều (µg/kg/phút):**",
            min_value=0.01,
            max_value=100.0,
            value=initial_dose_value,
            step=0.01,
            format="%.2f",
            key="ped_dose",
            help=f"Liều khuyến nghị: {dose_info.get('initial_dose', 'N/A') if dose_info else 'N/A'}"
        )
    
    # Infusion method
    st.markdown("### 💉 Phương pháp truyền")
    
    # For small children, prefer smaller syringe
    if age_days <= 365:  # < 1 year
        default_method = "syringe_pump_20ml"
        method_help = "Trẻ nhỏ nên dùng bơm 20ml để tăng độ chính xác"
    else:
        default_method = "syringe_pump_50ml"
        method_help = "Có thể dùng bơm 50ml hoặc 20ml"
    
    infusion_method = st.radio(
        "**Phương pháp:**",
        ["syringe_pump_50ml", "syringe_pump_20ml"],
        format_func=lambda x: "Bơm tiêm điện 50ml" if x == "syringe_pump_50ml" else "Bơm tiêm điện 20ml (cho trẻ nhỏ)",
        index=0 if default_method == "syringe_pump_50ml" else 1,
        key="ped_method",
        help=method_help
    )
    
    st.markdown("---")
    
    # Validate dose
    validation = validate_pediatric_dose(selected_drug, dose_mcg_kg_min, age_days)
    
    if validation.get("error"):
        render_error_alert(validation["error"], title="❌ Lỗi liều dùng")
    elif validation.get("warning"):
        render_warning_alert(validation["warning"], title="⚠️ Cảnh báo")
    
    # Display dose range info
    if dose_info:
        with st.expander("ℹ️ Thông tin liều cho nhóm tuổi này"):
            st.markdown(f"**Khoảng liều:** {dose_info.get('dose_range', 'N/A')}")
            st.markdown(f"**Liều khởi đầu:** {dose_info.get('initial_dose', 'N/A')}")
            st.markdown(f"**Liều tối đa:** {dose_info.get('max_dose', 'N/A')}")
            if dose_info.get('notes'):
                st.markdown(f"**Lưu ý:** {dose_info.get('notes')}")
    
    # Calculate button
    if st.button("🧮 Tính toán", key="ped_calculate", type="primary", use_container_width=True):
        try:
            # Calculate infusion
            results = calculate_pediatric_infusion(
                selected_drug,
                dose_mcg_kg_min,
                weight_kg,
                age_days,
                infusion_method
            )
            
            st.markdown("---")
            st.markdown("### 📊 Kết quả tính toán")
            
            # Display results
            metrics = [
                {
                    "label": "Tốc độ truyền",
                    "value": f"{results['infusion_rate_ml_hour']:.2f} ml/h",
                    "icon": "💉"
                },
                {
                    "label": "Tổng liều/giờ",
                    "value": f"{results['total_dose_mcg_hour']:.2f} µg/h",
                    "icon": "💊"
                },
                {
                    "label": "Nồng độ pha",
                    "value": f"{results['concentration_mcg_ml']:.2f} µg/ml",
                    "icon": "💧"
                }
            ]
            
            render_result_card("Kết quả", metrics, color="primary")
            
            # Preparation instructions
            st.markdown("---")
            st.markdown("### 🧪 Hướng dẫn pha")
            render_info_alert(
                results.get("preparation_instructions", ""),
                title="Cách pha"
            )
            
            # Pediatric-specific notes
            pediatric_dosing = get_pediatric_dose_range(selected_drug, age_group)
            if pediatric_dosing and pediatric_dosing.get("special_notes"):
                st.markdown("---")
                st.markdown("### ⚠️ Lưu ý đặc biệt cho trẻ em")
                render_warning_alert(
                    pediatric_dosing.get("special_notes"),
                    title="Lưu ý"
                )
            
            # Drug info
            drug_info = get_drug_info(selected_drug)
            if drug_info:
                st.markdown("---")
                st.markdown("### 💡 Thông tin thuốc")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Chỉ định:** {drug_info.get('indication', 'N/A')}")
                    st.markdown(f"**Chống chỉ định:** {drug_info.get('contraindication', 'N/A')}")
                
                with col2:
                    st.markdown(f"**Tác dụng phụ:** {drug_info.get('side_effects', 'N/A')}")
                    st.markdown(f"**Theo dõi:** {drug_info.get('monitoring', 'N/A')}")
            
        except ValueError as e:
            st.error(f"Lỗi: {str(e)}")
        except Exception as e:
            st.error(f"Lỗi không xác định: {str(e)}")
    
    # Reference
    with st.expander("📋 Bảng tham khảo nhóm tuổi"):
        age_groups_data = []
        for ag in ["neonatal", "infant", "child", "adolescent"]:
            info = get_age_group_info(ag)
            if info:
                age_groups_data.append({
                    "Nhóm": info.get("description", ag),
                    "Tuổi": info.get("age_range", ""),
                    "Mô tả": f"Liều thường thấp hơn người lớn" if ag in ["neonatal", "infant"] else "Liều gần như người lớn"
                })
        
        if age_groups_data:
            import pandas as pd
            df = pd.DataFrame(age_groups_data)
            st.dataframe(df, use_container_width=True, hide_index=True)

