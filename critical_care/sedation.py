"""
Sedation & Analgesia Calculator
ICU sedation dosing, titration, and RASS-based management
"""

import streamlit as st
from components.ui.inputs import render_number_input_with_unit
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


# RASS (Richmond Agitation-Sedation Scale) definitions
RASS_SCALE = {
    "+4": "Combative - Overtly combative, violent, immediate danger to staff",
    "+3": "Very Agitated - Pulls or removes tube(s) or catheter(s); aggressive",
    "+2": "Agitated - Frequent non-purposeful movement, fights ventilator",
    "+1": "Restless - Anxious but movements not aggressive or vigorous",
    "0": "Alert and Calm",
    "-1": "Drowsy - Not fully alert, but has sustained awakening (eye-opening/eye contact) to voice (>10 seconds)",
    "-2": "Light Sedation - Briefly awakens with eye contact to voice (<10 seconds)",
    "-3": "Moderate Sedation - Movement or eye opening to voice (but no eye contact)",
    "-4": "Deep Sedation - No response to voice, but movement or eye opening to physical stimulation",
    "-5": "Unarousable - No response to voice or physical stimulation"
}


# Sedative database
SEDATIVES = {
    "Propofol": {
        "name_vn": "Propofol",
        "indication": "An thần ICU, thủ thuật",
        "loading_dose": "0.5-1 mg/kg",
        "maintenance_dose": "5-50 µg/kg/min (0.3-3 mg/kg/h)",
        "tci_dose": "1.5-3 µg/ml (target concentration)",
        "rass_target": "-2 to -3",
        "titration": "Tăng 5-10 µg/kg/min mỗi 5 phút đến khi đạt RASS mục tiêu",
        "monitoring": "MAP, HR, RASS, SpO2, phản ứng đau",
        "side_effects": "Hạ huyết áp, ức chế hô hấp, propofol infusion syndrome (liều cao > 4 mg/kg/h > 48h)",
        "contraindications": "Dị ứng propofol, tăng lipid máu, propofol infusion syndrome",
        "notes": "Khởi phát nhanh, thời gian bán hủy ngắn. Cảnh giác propofol infusion syndrome ở trẻ em."
    },
    "Midazolam": {
        "name_vn": "Midazolam",
        "indication": "An thần ICU, co giật, thủ thuật",
        "loading_dose": "0.05-0.1 mg/kg (max 5 mg)",
        "maintenance_dose": "0.02-0.1 mg/kg/h (0.5-5 mg/h ở người lớn)",
        "bolus_dose": "2-5 mg IV (có thể lặp lại)",
        "rass_target": "-2 to -3",
        "titration": "Tăng 0.5-1 mg/h mỗi 30 phút",
        "monitoring": "MAP, HR, RASS, SpO2, tích tụ (tăng thời gian bán hủy ở suy gan/thận)",
        "side_effects": "Tích tụ, hạ huyết áp, ức chế hô hấp, mê sảng",
        "contraindications": "Suy gan nặng, dị ứng benzodiazepine",
        "notes": "Tích tụ ở bệnh nhân suy gan/thận. Có thể dùng kết hợp với opioid."
    },
    "Dexmedetomidine": {
        "name_vn": "Dexmedetomidine",
        "indication": "An thần ICU, cai máy thở, mê sảng",
        "loading_dose": "1 µg/kg trong 10 phút (tùy chọn)",
        "maintenance_dose": "0.2-1.4 µg/kg/h",
        "rass_target": "0 to -2 (awake sedation)",
        "titration": "Tăng 0.1-0.2 µg/kg/h mỗi 30 phút",
        "monitoring": "MAP, HR (nhịp chậm), RASS, SpO2",
        "side_effects": "Nhịp chậm, hạ huyết áp (liều cao), khô miệng",
        "contraindications": "Block AV độ cao, nhịp chậm nặng",
        "notes": "Gây an thần tỉnh táo (awake sedation), ít ức chế hô hấp. Tốt cho cai máy thở."
    },
    "Fentanyl": {
        "name_vn": "Fentanyl",
        "indication": "Giảm đau ICU, thủ thuật",
        "loading_dose": "1-2 µg/kg",
        "maintenance_dose": "0.5-2 µg/kg/h (25-100 µg/h ở người lớn)",
        "bolus_dose": "25-50 µg IV (có thể lặp lại)",
        "rass_target": "0 to -1 (khi dùng với sedative)",
        "titration": "Tăng 25 µg/h mỗi 30 phút",
        "monitoring": "MAP, HR, RASS, đau, độ cứng ngực (chest wall rigidity)",
        "side_effects": "Ức chế hô hấp, độ cứng ngực, tích tụ",
        "contraindications": "Dị ứng opioid",
        "notes": "Khởi phát nhanh, tác dụng ngắn. Tích tụ ở bệnh nhân suy thận. Cảnh giác độ cứng ngực."
    }
}


def calculate_propofol_dosing(weight_kg: float, target_rass: str, current_rass: str = "0") -> dict:
    """
    Calculate Propofol dosing based on RASS target
    
    Args:
        weight_kg: Patient weight in kg
        target_rass: Target RASS score (-5 to +4)
        current_rass: Current RASS score
    
    Returns:
        Dictionary with dosing recommendations
    """
    # Convert RASS to numeric
    rass_map = {str(k): int(k) if k.lstrip('-').isdigit() else 0 for k in RASS_SCALE.keys()}
    target_rass_num = rass_map.get(target_rass, 0)
    current_rass_num = rass_map.get(current_rass, 0)
    
    # Base dosing based on target RASS
    if target_rass_num >= 0:
        # Awake or slightly drowsy
        dose_mcg_kg_min = 5
        dose_mg_kg_h = 0.3
    elif target_rass_num == -1:
        # Light sedation
        dose_mcg_kg_min = 10
        dose_mg_kg_h = 0.6
    elif target_rass_num == -2:
        # Moderate sedation
        dose_mcg_kg_min = 20
        dose_mg_kg_h = 1.2
    elif target_rass_num == -3:
        # Deep sedation
        dose_mcg_kg_min = 30
        dose_mg_kg_h = 1.8
    else:
        # Very deep sedation
        dose_mcg_kg_min = 40
        dose_mg_kg_h = 2.4
    
    # Adjust based on current RASS
    rass_diff = current_rass_num - target_rass_num
    if rass_diff > 0:
        # More agitated than target - increase dose
        dose_mcg_kg_min *= 1.2
        dose_mg_kg_h *= 1.2
    
    # Calculate absolute doses
    dose_mcg_min = dose_mcg_kg_min * weight_kg
    dose_mg_h = dose_mg_kg_h * weight_kg
    
    # TCI target concentration
    tci_target = 1.5 + (abs(target_rass_num) * 0.3)  # Rough estimate
    
    return {
        "dose_mcg_kg_min": dose_mcg_kg_min,
        "dose_mcg_min": dose_mcg_min,
        "dose_mg_kg_h": dose_mg_kg_h,
        "dose_mg_h": dose_mg_h,
        "tci_target": tci_target,
        "loading_dose_mg": weight_kg * 0.5,  # 0.5 mg/kg loading
        "target_rass": target_rass,
        "current_rass": current_rass
    }


def calculate_midazolam_dosing(weight_kg: float, target_rass: str, current_rass: str = "0") -> dict:
    """
    Calculate Midazolam dosing based on RASS target
    
    Args:
        weight_kg: Patient weight in kg
        target_rass: Target RASS score
        current_rass: Current RASS score
    
    Returns:
        Dictionary with dosing recommendations
    """
    # Convert RASS to numeric
    rass_map = {str(k): int(k) if k.lstrip('-').isdigit() else 0 for k in RASS_SCALE.keys()}
    target_rass_num = rass_map.get(target_rass, 0)
    
    # Base dosing
    if target_rass_num >= 0:
        dose_mg_kg_h = 0.02
    elif target_rass_num == -1:
        dose_mg_kg_h = 0.03
    elif target_rass_num == -2:
        dose_mg_kg_h = 0.05
    elif target_rass_num == -3:
        dose_mg_kg_h = 0.07
    else:
        dose_mg_kg_h = 0.1
    
    # Calculate absolute doses
    dose_mg_h = dose_mg_kg_h * weight_kg
    
    # Loading dose
    loading_dose_mg = weight_kg * 0.05  # 0.05 mg/kg
    
    return {
        "dose_mg_kg_h": dose_mg_kg_h,
        "dose_mg_h": dose_mg_h,
        "loading_dose_mg": loading_dose_mg,
        "bolus_dose_mg": 2 if weight_kg < 70 else 5,
        "target_rass": target_rass,
        "current_rass": current_rass
    }


def calculate_dexmedetomidine_dosing(weight_kg: float, target_rass: str, current_rass: str = "0") -> dict:
    """
    Calculate Dexmedetomidine dosing based on RASS target
    
    Args:
        weight_kg: Patient weight in kg
        target_rass: Target RASS score
        current_rass: Current RASS score
    
    Returns:
        Dictionary with dosing recommendations
    """
    # Convert RASS to numeric
    rass_map = {str(k): int(k) if k.lstrip('-').isdigit() else 0 for k in RASS_SCALE.keys()}
    target_rass_num = rass_map.get(target_rass, 0)
    
    # Base dosing (awake sedation)
    if target_rass_num >= 0:
        dose_mcg_kg_h = 0.3
    elif target_rass_num == -1:
        dose_mcg_kg_h = 0.5
    elif target_rass_num == -2:
        dose_mcg_kg_h = 0.7
    else:
        dose_mcg_kg_h = 1.0
    
    # Calculate absolute dose
    dose_mcg_h = dose_mcg_kg_h * weight_kg
    
    # Loading dose (optional)
    loading_dose_mcg = weight_kg * 1.0  # 1 µg/kg over 10 minutes
    
    return {
        "dose_mcg_kg_h": dose_mcg_kg_h,
        "dose_mcg_h": dose_mcg_h,
        "loading_dose_mcg": loading_dose_mcg,
        "target_rass": target_rass,
        "current_rass": current_rass
    }


def calculate_fentanyl_dosing(weight_kg: float, pain_level: int, target_rass: str = "0") -> dict:
    """
    Calculate Fentanyl dosing for analgesia
    
    Args:
        weight_kg: Patient weight in kg
        pain_level: Pain level (0-10 scale)
        target_rass: Target RASS score (for sedation)
    
    Returns:
        Dictionary with dosing recommendations
    """
    # Base dosing based on pain level
    if pain_level <= 3:
        dose_mcg_kg_h = 0.5
    elif pain_level <= 6:
        dose_mcg_kg_h = 1.0
    else:
        dose_mcg_kg_h = 1.5
    
    # Calculate absolute doses
    dose_mcg_h = dose_mcg_kg_h * weight_kg
    
    # Loading/bolus dose
    loading_dose_mcg = weight_kg * 1.0  # 1 µg/kg
    bolus_dose_mcg = 25 if weight_kg < 70 else 50
    
    return {
        "dose_mcg_kg_h": dose_mcg_kg_h,
        "dose_mcg_h": dose_mcg_h,
        "loading_dose_mcg": loading_dose_mcg,
        "bolus_dose_mcg": bolus_dose_mcg,
        "pain_level": pain_level,
        "target_rass": target_rass
    }


def render_propofol_calculator():
    """Render Propofol dosing calculator"""
    st.subheader("💉 Propofol")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="propofol_weight"
        )
        
        current_rass = st.selectbox(
            "RASS hiện tại",
            list(RASS_SCALE.keys()),
            format_func=lambda x: f"{x} - {RASS_SCALE[x].split(' - ')[0]}",
            index=5,  # Default to 0
            key="propofol_current_rass"
        )
    
    with col2:
        target_rass = st.selectbox(
            "RASS mục tiêu",
            ["-1", "-2", "-3", "-4"],
            format_func=lambda x: f"{x} - {RASS_SCALE[x].split(' - ')[0]}",
            index=1,  # Default to -2
            key="propofol_target_rass"
        )
        
        clinical_scenario = st.selectbox(
            "Tình huống lâm sàng",
            ["An thần thủ thuật (RASS -1 to -2)", "An thần sâu (RASS -3 to -4)", "Tùy chỉnh"],
            key="propofol_scenario"
        )
    
    # Auto-adjust RASS based on scenario
    if "thủ thuật" in clinical_scenario:
        target_rass = "-2"
    elif "sâu" in clinical_scenario:
        target_rass = "-3"
    
    # Calculate
    if st.button("📊 Tính toán", key="propofol_calculate", type="primary"):
        result = calculate_propofol_dosing(weight_kg, target_rass, current_rass)
        
        st.success(f"**Liều Propofol:**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            render_result_card(
                f"{result['dose_mcg_kg_min']:.1f} µg/kg/min",
                "Liều truyền liên tục",
                "blue"
            )
        with col2:
            render_result_card(
                f"{result['dose_mg_h']:.1f} mg/h",
                "Tổng liều/giờ",
                "green"
            )
        with col3:
            render_result_card(
                f"{result['tci_target']:.1f} µg/ml",
                "TCI target",
                "purple"
            )
        
        st.info(f"**Liều khởi đầu:** {result['loading_dose_mg']:.1f} mg (0.5 mg/kg)")
        
        # Drug info
        st.markdown("---")
        st.markdown("### 📋 Thông tin Thuốc")
        drug_info = SEDATIVES["Propofol"]
        
        st.markdown(f"**Chỉ định:** {drug_info['indication']}")
        st.markdown(f"**Titration:** {drug_info['titration']}")
        st.markdown(f"**Theo dõi:** {drug_info['monitoring']}")
        
        render_warning_alert(
            "⚠️ Cảnh báo",
            drug_info['side_effects']
        )


def render_midazolam_calculator():
    """Render Midazolam dosing calculator"""
    st.subheader("💉 Midazolam")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="midazolam_weight"
        )
        
        target_rass = st.selectbox(
            "RASS mục tiêu",
            ["-1", "-2", "-3", "-4"],
            format_func=lambda x: f"{x} - {RASS_SCALE[x].split(' - ')[0]}",
            index=1,
            key="midazolam_target_rass"
        )
    
    with col2:
        current_rass = st.selectbox(
            "RASS hiện tại",
            list(RASS_SCALE.keys()),
            format_func=lambda x: f"{x} - {RASS_SCALE[x].split(' - ')[0]}",
            index=5,
            key="midazolam_current_rass"
        )
        
        use_loading = st.checkbox(
            "Dùng liều khởi đầu",
            value=True,
            key="midazolam_loading"
        )
    
    # Calculate
    if st.button("📊 Tính toán", key="midazolam_calculate", type="primary"):
        result = calculate_midazolam_dosing(weight_kg, target_rass, current_rass)
        
        st.success(f"**Liều Midazolam:**")
        
        col1, col2 = st.columns(2)
        with col1:
            render_result_card(
                f"{result['dose_mg_kg_h']:.3f} mg/kg/h",
                "Liều truyền liên tục",
                "blue"
            )
        with col2:
            render_result_card(
                f"{result['dose_mg_h']:.2f} mg/h",
                "Tổng liều/giờ",
                "green"
            )
        
        if use_loading:
            st.info(f"**Liều khởi đầu:** {result['loading_dose_mg']:.1f} mg (0.05 mg/kg)")
        
        st.info(f"**Liều bolus:** {result['bolus_dose_mg']} mg (có thể lặp lại)")
        
        # Drug info
        st.markdown("---")
        drug_info = SEDATIVES["Midazolam"]
        render_warning_alert(
            "⚠️ Tích tụ",
            "Cảnh giác tích tụ ở bệnh nhân suy gan/thận. Tăng thời gian bán hủy."
        )


def render_dexmedetomidine_calculator():
    """Render Dexmedetomidine dosing calculator"""
    st.subheader("💉 Dexmedetomidine")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="dex_weight"
        )
        
        target_rass = st.selectbox(
            "RASS mục tiêu",
            ["0", "-1", "-2"],
            format_func=lambda x: f"{x} - {RASS_SCALE[x].split(' - ')[0]}",
            index=1,
            key="dex_target_rass",
            help="Dexmedetomidine thường dùng cho awake sedation (RASS 0 to -2)"
        )
    
    with col2:
        use_loading = st.checkbox(
            "Dùng liều khởi đầu (1 µg/kg trong 10 phút)",
            value=False,
            key="dex_loading"
        )
        
        clinical_scenario = st.selectbox(
            "Tình huống",
            ["Cai máy thở", "An thần tỉnh táo", "Mê sảng"],
            key="dex_scenario"
        )
    
    # Calculate
    if st.button("📊 Tính toán", key="dex_calculate", type="primary"):
        result = calculate_dexmedetomidine_dosing(weight_kg, target_rass)
        
        st.success(f"**Liều Dexmedetomidine:**")
        
        col1, col2 = st.columns(2)
        with col1:
            render_result_card(
                f"{result['dose_mcg_kg_h']:.2f} µg/kg/h",
                "Liều truyền liên tục",
                "blue"
            )
        with col2:
            render_result_card(
                f"{result['dose_mcg_h']:.1f} µg/h",
                "Tổng liều/giờ",
                "green"
            )
        
        if use_loading:
            st.info(f"**Liều khởi đầu:** {result['loading_dose_mcg']:.0f} µg (1 µg/kg trong 10 phút)")
        
        # Drug info
        st.markdown("---")
        drug_info = SEDATIVES["Dexmedetomidine"]
        render_info_alert(
            "ℹ️ Awake Sedation",
            "Dexmedetomidine gây an thần tỉnh táo, ít ức chế hô hấp. Tốt cho cai máy thở và mê sảng."
        )


def render_fentanyl_calculator():
    """Render Fentanyl dosing calculator"""
    st.subheader("💉 Fentanyl")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=1.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="fentanyl_weight"
        )
        
        pain_level = st.slider(
            "Mức độ đau (0-10)",
            min_value=0,
            max_value=10,
            value=5,
            key="fentanyl_pain"
        )
    
    with col2:
        use_loading = st.checkbox(
            "Dùng liều khởi đầu",
            value=True,
            key="fentanyl_loading"
        )
        
        use_bolus = st.checkbox(
            "Cho phép bolus",
            value=True,
            key="fentanyl_bolus"
        )
    
    # Calculate
    if st.button("📊 Tính toán", key="fentanyl_calculate", type="primary"):
        result = calculate_fentanyl_dosing(weight_kg, pain_level)
        
        st.success(f"**Liều Fentanyl:**")
        
        col1, col2 = st.columns(2)
        with col1:
            render_result_card(
                f"{result['dose_mcg_kg_h']:.2f} µg/kg/h",
                "Liều truyền liên tục",
                "blue"
            )
        with col2:
            render_result_card(
                f"{result['dose_mcg_h']:.1f} µg/h",
                "Tổng liều/giờ",
                "green"
            )
        
        if use_loading:
            st.info(f"**Liều khởi đầu:** {result['loading_dose_mcg']:.0f} µg (1 µg/kg)")
        
        if use_bolus:
            st.info(f"**Liều bolus:** {result['bolus_dose_mcg']} µg (có thể lặp lại mỗi 5-10 phút)")
        
        # Drug info
        st.markdown("---")
        drug_info = SEDATIVES["Fentanyl"]
        render_warning_alert(
            "⚠️ Cảnh báo",
            "Cảnh giác độ cứng ngực (chest wall rigidity) và ức chế hô hấp. Tích tụ ở suy thận."
        )


def render_rass_guide():
    """Render RASS scale guide"""
    st.subheader("📊 RASS (Richmond Agitation-Sedation Scale)")
    
    st.markdown("""
    **RASS** là thang điểm tiêu chuẩn để đánh giá mức độ an thần và kích động ở ICU.
    """)
    
    # Display RASS scale
    for rass, description in RASS_SCALE.items():
        if rass.startswith('+'):
            color = "red"
        elif rass == '0':
            color = "green"
        else:
            color = "blue"
        
        st.markdown(f"""
        <div style="padding: 10px; margin: 5px 0; border-left: 4px solid {color}; background: #f5f5f5;">
            <strong>RASS {rass}:</strong> {description}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎯 Mục tiêu RASS Theo Tình huống")
    
    scenarios = {
        "An thần thủ thuật": "-1 to -2",
        "An thần sâu": "-3 to -4",
        "Bệnh nhân tỉnh": "0",
        "Cai máy thở": "0 to -1",
        "Mê sảng": "0 to -1 (với Dexmedetomidine)"
    }
    
    for scenario, rass_range in scenarios.items():
        st.markdown(f"**{scenario}:** RASS {rass_range}")


def render_sedation_calculator():
    """Main function to render sedation calculator"""
    st.header("💉 Sedation & Analgesia Calculator")
    st.caption("Tính toán liều an thần và giảm đau ICU dựa trên RASS")
    
    # Calculator selection
    calculator_type = st.selectbox(
        "Chọn thuốc:",
        [
            "💉 Propofol",
            "💉 Midazolam",
            "💉 Dexmedetomidine",
            "💉 Fentanyl",
            "📊 RASS Guide"
        ],
        key="sedation_calc_type"
    )
    
    st.markdown("---")
    
    # Route to appropriate calculator
    if "Propofol" in calculator_type:
        render_propofol_calculator()
    elif "Midazolam" in calculator_type:
        render_midazolam_calculator()
    elif "Dexmedetomidine" in calculator_type:
        render_dexmedetomidine_calculator()
    elif "Fentanyl" in calculator_type:
        render_fentanyl_calculator()
    elif "RASS" in calculator_type:
        render_rass_guide()
    
    st.markdown("---")
    st.caption("⚠️ Chỉ mục đích tham khảo. Điều chỉnh theo tình huống lâm sàng và đáp ứng bệnh nhân.")

