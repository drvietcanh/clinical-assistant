"""
Vasopressor Dosing Guide
Dosing, titration, and compatibility information for vasopressors
"""

import streamlit as st
from components.ui.results import render_result_card, render_result_box
from components.ui.alerts import render_info_alert, render_warning_alert


# Vasopressor database
VASOPRESSORS = {
    "Norepinephrine": {
        "name_vn": "Noradrenaline",
        "indication": "Sốc nhiễm khuẩn, sốc tim, sốc phản vệ",
        "initial_dose": "0.05-0.1 µg/kg/min",
        "titration": "Tăng 0.05-0.1 µg/kg/min mỗi 5-10 phút đến khi đạt MAP mục tiêu",
        "usual_range": "0.05-2 µg/kg/min",
        "max_dose": "3-5 µg/kg/min",
        "concentration": "16 mg/250 ml NS = 64 µg/ml",
        "compatibility": "Tương thích với: Dopamine, Dobutamine, Vasopressin. Không trộn với: Sodium bicarbonate",
        "monitoring": "MAP, HR, ngón tay chân, lactate, ScvO2",
        "side_effects": "Tăng áp lực, loạn nhịp tim, thiếu máu cục bộ ngón tay/chân",
        "notes": "Thuốc lựa chọn đầu tiên trong sốc nhiễm khuẩn (Surviving Sepsis 2021)"
    },
    "Epinephrine": {
        "name_vn": "Adrenaline",
        "indication": "Sốc phản vệ, ngừng tim, sốc tim",
        "initial_dose": "0.05-0.1 µg/kg/min",
        "titration": "Tăng 0.05-0.1 µg/kg/min mỗi 5 phút",
        "usual_range": "0.05-0.5 µg/kg/min",
        "max_dose": "1-2 µg/kg/min",
        "concentration": "1 mg/250 ml NS = 4 µg/ml",
        "compatibility": "Tương thích với: Norepinephrine. Không trộn với: Sodium bicarbonate",
        "monitoring": "MAP, HR, ngón tay chân, lactate, glucose",
        "side_effects": "Tăng áp, loạn nhịp, tăng đường huyết, thiếu máu cục bộ",
        "notes": "Dùng trong sốc phản vệ, ngừng tim"
    },
    "Dopamine": {
        "name_vn": "Dopamine",
        "indication": "Sốc tim, suy thận (liều thấp)",
        "initial_dose": "2-5 µg/kg/min",
        "titration": "Tăng 2-5 µg/kg/min mỗi 10 phút",
        "usual_range": "2-20 µg/kg/min",
        "max_dose": "20-30 µg/kg/min",
        "concentration": "400 mg/250 ml NS = 1600 µg/ml",
        "compatibility": "Tương thích với: Norepinephrine, Dobutamine",
        "monitoring": "MAP, HR, ngón tay chân, lactate",
        "side_effects": "Loạn nhịp tim, tăng áp, thiếu máu cục bộ",
        "notes": "Liều thấp (1-3 µg/kg/min): tăng lưu lượng thận. Hiện ít dùng do tăng tỷ lệ tử vong"
    },
    "Dobutamine": {
        "name_vn": "Dobutamine",
        "indication": "Suy tim, sốc tim, giảm cung lượng tim",
        "initial_dose": "2.5-5 µg/kg/min",
        "titration": "Tăng 2.5-5 µg/kg/min mỗi 10 phút",
        "usual_range": "2.5-15 µg/kg/min",
        "max_dose": "20 µg/kg/min",
        "concentration": "250 mg/250 ml D5W = 1000 µg/ml",
        "compatibility": "Tương thích với: Norepinephrine, Dopamine",
        "monitoring": "MAP, HR, CVP, ScvO2, lactate",
        "side_effects": "Loạn nhịp tim, tăng HR, đau ngực",
        "notes": "Dobutamine là inotrope, không phải vasopressor. Dùng trong suy tim, giảm cung lượng tim"
    },
    "Vasopressin": {
        "name_vn": "Vasopressin",
        "indication": "Sốc nhiễm khuẩn kháng thuốc, sốc do giảm thể tích",
        "initial_dose": "0.03-0.04 units/min",
        "titration": "Liều cố định, không cần điều chỉnh",
        "usual_range": "0.03-0.04 units/min",
        "max_dose": "0.04 units/min (không tăng hơn)",
        "concentration": "20 units/100 ml NS = 0.2 units/ml",
        "compatibility": "Tương thích với: Norepinephrine, Epinephrine",
        "monitoring": "MAP, lactate, ngón tay chân",
        "side_effects": "Thiếu máu cục bộ (ngón tay, chân), thiếu máu mạc treo",
        "notes": "Dùng như thuốc thứ 2 khi norepinephrine không đủ. Liều cố định 0.03-0.04 units/min"
    },
    "Phenylephrine": {
        "name_vn": "Phenylephrine",
        "indication": "Hạ huyết áp trong gây mê, sốc giảm thể tích",
        "initial_dose": "0.5-1.5 µg/kg/min",
        "titration": "Tăng 0.5 µg/kg/min mỗi 10 phút",
        "usual_range": "0.5-6 µg/kg/min",
        "max_dose": "10 µg/kg/min",
        "concentration": "10 mg/250 ml NS = 40 µg/ml",
        "compatibility": "Tương thích với: Norepinephrine",
        "monitoring": "MAP, HR, ngón tay chân",
        "side_effects": "Phản xạ nhịp chậm, thiếu máu cục bộ",
        "notes": "Thuốc lựa chọn trong gây mê. Ít dùng trong ICU so với norepinephrine"
    },
}


def calculate_dose_per_hour(weight_kg: float, dose_mcg_per_kg_min: float) -> dict:
    """
    Calculate vasopressor dose in ml/hour
    
    Args:
        weight_kg: Weight in kg
        dose_mcg_per_kg_min: Dose in µg/kg/min
    
    Returns:
        Dictionary with dose calculations
    """
    # Total dose per minute
    total_mcg_per_min = weight_kg * dose_mcg_per_kg_min
    
    # Convert to ml/hour (assuming standard concentration)
    # Need concentration to calculate
    
    return {
        "mcg_per_min": total_mcg_per_min,
        "mcg_per_hour": total_mcg_per_min * 60,
        "mg_per_hour": (total_mcg_per_min * 60) / 1000,
    }


def render_vasopressor_guide():
    """Render vasopressor dosing guide interface"""
    
    st.markdown("## 💉 Hướng Dẫn Liều Dùng Vasopressor")
    st.markdown("""
    Hướng dẫn liều dùng, điều chỉnh liều, và thông tin tương thích cho các vasopressor.
    
    **Dựa trên:** Surviving Sepsis Campaign 2021, ACCM Guidelines
    """)
    
    st.markdown("---")
    
    # Select vasopressor
    vasopressor_list = list(VASOPRESSORS.keys())
    selected_vaso = st.selectbox(
        "Chọn vasopressor:",
        vasopressor_list,
        key="vasopressor_select"
    )
    
    vasopressor_data = VASOPRESSORS[selected_vaso]
    
    st.markdown("---")
    
    # Display information
    st.markdown(f"### 💉 {selected_vaso}")
    if vasopressor_data.get("name_vn"):
        st.markdown(f"**Tên khác:** {vasopressor_data['name_vn']}")
    
    # Indication
    st.markdown("### 📋 Chỉ định")
    st.info(vasopressor_data['indication'])
    
    # Dosage section
    st.markdown("### 💊 Liều Dùng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        render_result_box(
            "Liều khởi đầu",
            vasopressor_data['initial_dose'],
            color="primary",
            icon="▶️"
        )
    
    with col2:
        render_result_box(
            "Liều thông thường",
            vasopressor_data['usual_range'],
            color="info"
        )
    
    st.markdown(f"**Liều tối đa:** {vasopressor_data['max_dose']}")
    
    st.markdown("---")
    
    # Titration
    st.markdown("### ⚙️ Điều Chỉnh Liều (Titration)")
    st.info(vasopressor_data['titration'])
    
    st.markdown("---")
    
    # Concentration calculator
    st.markdown("### 🧮 Tính Toán Liều")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_vaso = st.number_input(
            "Cân nặng (kg):",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="vaso_weight"
        )
    
    with col2:
        dose_mcg_per_kg_min = st.number_input(
            "Liều (µg/kg/min):",
            min_value=0.01,
            max_value=100.0,
            value=0.1,
            step=0.01,
            key="vaso_dose"
        )
    
    if st.button("Tính toán", key="calc_vaso", type="primary"):
        calc_results = calculate_dose_per_hour(weight_vaso, dose_mcg_per_kg_min)
        
        st.markdown("---")
        
        metrics = [
            {"label": "Tổng liều/phút", "value": f"{calc_results['mcg_per_min']:.2f} µg/min", "icon": "⏱️"},
            {"label": "Tổng liều/giờ", "value": f"{calc_results['mcg_per_hour']:.2f} µg/h", "icon": "💉"},
            {"label": "Tổng liều/giờ", "value": f"{calc_results['mg_per_hour']:.2f} mg/h", "icon": "💊"},
        ]
        
        render_result_card("Liều Tính Toán", metrics, color="primary")
        
        # Show concentration info
        if vasopressor_data.get('concentration'):
            st.markdown("---")
            st.markdown(f"**Nồng độ chuẩn:** {vasopressor_data['concentration']}")
            st.caption("💡 Tính ml/h dựa trên nồng độ này để set tốc độ bơm")
    
    st.markdown("---")
    
    # Compatibility
    st.markdown("### 🔗 Tương Thích (Compatibility)")
    if vasopressor_data.get('compatibility'):
        st.info(vasopressor_data['compatibility'])
    
    st.markdown("---")
    
    # Monitoring
    st.markdown("### 📊 Theo Dõi")
    if vasopressor_data.get('monitoring'):
        monitoring_items = vasopressor_data['monitoring'].split(', ')
        st.markdown("Theo dõi:")
        for item in monitoring_items:
            st.markdown(f"- ✅ {item}")
    
    st.markdown("---")
    
    # Side effects
    st.markdown("### ⚠️ Tác Dụng Phụ")
    if vasopressor_data.get('side_effects'):
        st.warning(vasopressor_data['side_effects'])
    
    st.markdown("---")
    
    # Notes
    if vasopressor_data.get('notes'):
        st.markdown("### 💡 Lưu Ý")
        render_info_alert(vasopressor_data['notes'], title="Thông tin quan trọng")
    
    # Quick reference table
    with st.expander("📋 Bảng So Sánh Nhanh Tất Cả Vasopressor"):
        import pandas as pd
        
        comparison_data = []
        for vaso_name, vaso_data in VASOPRESSORS.items():
            comparison_data.append({
                "Vasopressor": vaso_name,
                "Liều khởi đầu": vaso_data['initial_dose'],
                "Liều thông thường": vaso_data['usual_range'],
                "Liều tối đa": vaso_data['max_dose'],
                "Chỉ định chính": vaso_data['indication']
            })
        
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Disclaimer
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Hướng dẫn này chỉ mục đích tham khảo
    - Luôn điều chỉnh liều theo đáp ứng lâm sàng của bệnh nhân
    - Theo dõi sát các dấu hiệu sống và tác dụng phụ
    - Tuân thủ hướng dẫn địa phương và quy định bệnh viện
    - Dùng đường truyền tĩnh mạch trung tâm khi có thể
    """)


