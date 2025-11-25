"""
Critical Care Ventilator Management Tools
Ideal Body Weight, Tidal Volume, PEEP, Plateau Pressure, Weaning
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert


def calculate_ibw(sex: str, height_cm: float) -> float:
    """
    Calculate Ideal Body Weight (IBW) / Predicted Body Weight (PBW)
    
    Formulas:
    - Male: IBW = 50 + 2.3 × (height_inches - 60) = 50 + 0.91 × (height_cm - 152.4)
    - Female: IBW = 45.5 + 2.3 × (height_inches - 60) = 45.5 + 0.91 × (height_cm - 152.4)
    
    Args:
        sex: "Nam" or "Nữ"
        height_cm: Height in cm
    
    Returns:
        IBW in kg
    """
    height_inches = height_cm / 2.54
    
    if sex == "Nam" or sex.lower() == "male":
        ibw = 50 + 2.3 * (height_inches - 60)
    else:  # Female
        ibw = 45.5 + 2.3 * (height_inches - 60)
    
    return max(ibw, 0)  # Ensure non-negative


def calculate_tidal_volume(ibw_kg: float, ml_per_kg: float = 6.0) -> dict:
    """
    Calculate recommended tidal volume based on IBW
    
    Args:
        ibw_kg: Ideal Body Weight in kg
        ml_per_kg: ml/kg (default 6 for ARDSNet)
    
    Returns:
        Dictionary with tidal volume recommendations
    """
    vt_ml = ibw_kg * ml_per_kg
    
    return {
        "vt_ml": vt_ml,
        "vt_liters": vt_ml / 1000,
        "ml_per_kg": ml_per_kg,
        "ibw_kg": ibw_kg
    }


def get_peep_fio2_table():
    """Get ARDSNet PEEP/FiO2 table"""
    return [
        {"FiO2": 0.3, "PEEP_min": 5, "PEEP_max": 8},
        {"FiO2": 0.4, "PEEP_min": 8, "PEEP_max": 10},
        {"FiO2": 0.5, "PEEP_min": 10, "PEEP_max": 12},
        {"FiO2": 0.6, "PEEP_min": 12, "PEEP_max": 14},
        {"FiO2": 0.7, "PEEP_min": 14, "PEEP_max": 16},
        {"FiO2": 0.8, "PEEP_min": 16, "PEEP_max": 18},
        {"FiO2": 0.9, "PEEP_min": 18, "PEEP_max": 20},
        {"FiO2": 1.0, "PEEP_min": 20, "PEEP_max": 24},
    ]


def recommend_peep(fio2: float) -> dict:
    """
    Recommend PEEP based on FiO2 (ARDSNet protocol)
    
    Args:
        fio2: FiO2 as decimal (0.3-1.0)
    
    Returns:
        Dictionary with PEEP recommendation
    """
    table = get_peep_fio2_table()
    
    # Find matching range
    for entry in table:
        if fio2 <= entry["FiO2"]:
            return {
                "peep_min": entry["PEEP_min"],
                "peep_max": entry["PEEP_max"],
                "peep_recommended": (entry["PEEP_min"] + entry["PEEP_max"]) / 2,
                "fio2": fio2
            }
    
    # If FiO2 > 1.0, use highest PEEP
    return {
        "peep_min": 20,
        "peep_max": 24,
        "peep_recommended": 22,
        "fio2": fio2
    }


def calculate_plateau_pressure(vt_ml: float, compliance: float, peep: float) -> dict:
    """
    Calculate plateau pressure from compliance
    
    Formula: Plateau = (Vt / Compliance) + PEEP
    
    Args:
        vt_ml: Tidal volume in ml
        compliance: Static compliance in ml/cmH2O
        peep: PEEP in cmH2O
    
    Returns:
        Dictionary with plateau pressure
    """
    if compliance > 0:
        plateau = (vt_ml / compliance) + peep
    else:
        plateau = None
    
    driving_pressure = plateau - peep if plateau else None
    
    return {
        "plateau": plateau,
        "driving_pressure": driving_pressure,
        "vt_ml": vt_ml,
        "compliance": compliance,
        "peep": peep
    }


def calculate_rsbi(rr: float, vt_liters: float) -> dict:
    """
    Calculate Rapid Shallow Breathing Index (RSBI)
    
    RSBI = RR / Vt (L)
    
    Args:
        rr: Respiratory rate (breaths/min)
        vt_liters: Tidal volume in liters
    
    Returns:
        Dictionary with RSBI and interpretation
    """
    if vt_liters > 0:
        rsbi = rr / vt_liters
    else:
        rsbi = None
    
    if rsbi is None:
        interpretation = None
        color = None
    elif rsbi < 105:
        interpretation = "Tốt - Có thể cai máy thở"
        color = "success"
    elif rsbi < 130:
        interpretation = "Trung bình - Cần theo dõi"
        color = "warning"
    else:
        interpretation = "Kém - Khó cai máy thở"
        color = "error"
    
    return {
        "rsbi": rsbi,
        "interpretation": interpretation,
        "color": color,
        "rr": rr,
        "vt_liters": vt_liters
    }


def render_ibw_calculator():
    """Render Ideal Body Weight calculator"""
    st.subheader("📏 Ideal Body Weight (IBW) Calculator")
    st.caption("Tính trọng lượng cơ thể lý tưởng để tính tidal volume")
    
    st.markdown("""
    **IBW (Ideal Body Weight)** hay **PBW (Predicted Body Weight)** được sử dụng để tính tidal volume 
    trong ARDSNet protocol, không dùng actual body weight.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sex = st.radio(
            "Giới tính:",
            ["Nam", "Nữ"],
            horizontal=True,
            key="ibw_sex"
        )
    
    with col2:
        height_cm = st.number_input(
            "Chiều cao (cm):",
            min_value=100,
            max_value=250,
            value=170,
            step=1,
            format="%d",
            key="ibw_height"
        )
    
    if st.button("Tính toán", type="primary", key="calc_ibw"):
        ibw = calculate_ibw(sex, height_cm)
        
        st.markdown("### 📊 Kết Quả")
        
        render_result_box(
            "Ideal Body Weight",
            f"{ibw:.1f} kg",
            subtitle=f"Chiều cao: {height_cm} cm ({sex})",
            color="primary",
            icon="📏"
        )
        
        st.markdown("---")
        st.info(f"""
        **💡 Sử dụng IBW để tính Tidal Volume:**
        - ARDSNet protocol: **6 ml/kg IBW**
        - Tidal volume khuyến nghị: **{ibw * 6:.0f} ml** ({ibw * 6 / 1000:.2f} L)
        - Mục tiêu: Bảo vệ phổi (lung-protective ventilation)
        """)
        
        st.markdown("---")
        st.markdown("### 📋 Công Thức")
        
        if sex == "Nam":
            st.latex(r"IBW = 50 + 2.3 \times (height_{inches} - 60)")
        else:
            st.latex(r"IBW = 45.5 + 2.3 \times (height_{inches} - 60)")


def render_tidal_volume_calculator():
    """Render Tidal Volume calculator"""
    st.subheader("💨 Tidal Volume Calculator")
    st.caption("Tính tidal volume dựa trên IBW (ARDSNet protocol)")
    
    st.markdown("""
    **ARDSNet Protocol:** Tidal volume = 6 ml/kg IBW (lung-protective ventilation)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ibw_kg = st.number_input(
            "Ideal Body Weight (kg):",
            min_value=20.0,
            max_value=150.0,
            value=70.0,
            step=0.1,
            format="%.1f",
            key="tidal_ibw",
            help="Sử dụng IBW, không dùng actual body weight"
        )
    
    with col2:
        ml_per_kg = st.number_input(
            "ml/kg:",
            min_value=4.0,
            max_value=10.0,
            value=6.0,
            step=0.5,
            format="%.1f",
            key="tidal_ml_per_kg",
            help="ARDSNet: 6 ml/kg IBW"
        )
    
    if st.button("Tính toán", type="primary", key="calc_tidal"):
        results = calculate_tidal_volume(ibw_kg, ml_per_kg)
        
        st.markdown("### 📊 Kết Quả")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            render_result_box(
                "Tidal Volume",
                f"{results['vt_ml']:.0f} ml",
                subtitle=f"{results['vt_liters']:.2f} L",
                color="primary",
                icon="💨"
            )
        
        with col2:
            render_result_box(
                "ml/kg IBW",
                f"{ml_per_kg:.1f} ml/kg",
                subtitle=f"IBW: {ibw_kg:.1f} kg",
                color="info"
            )
        
        with col3:
            # Check if protective
            if ml_per_kg <= 6:
                status = "✅ Bảo vệ phổi"
                color_status = "success"
            elif ml_per_kg <= 8:
                status = "⚠️ Trung bình"
                color_status = "warning"
            else:
                status = "🚨 Cao"
                color_status = "error"
            
            render_result_box(
                "Trạng thái",
                status,
                color=color_status
            )
        
        st.markdown("---")
        st.info(f"""
        **💡 Khuyến nghị:**
        - **ARDSNet protocol:** 6 ml/kg IBW = **{ibw_kg * 6:.0f} ml**
        - **Mục tiêu:** Plateau pressure < 30 cmH2O
        - **Driving pressure:** < 15 cmH2O
        - **Lưu ý:** Sử dụng IBW, không dùng actual body weight
        """)


def render_peep_calculator():
    """Render PEEP calculator"""
    st.subheader("📊 PEEP Calculator")
    st.caption("Khuyến nghị PEEP dựa trên FiO2 (ARDSNet protocol)")
    
    st.markdown("""
    **ARDSNet PEEP/FiO2 Table:** Khuyến nghị PEEP dựa trên FiO2 để đạt SpO2 88-95% hoặc PaO2 55-80 mmHg.
    """)
    
    st.markdown("---")
    
    fio2_percent = st.slider(
        "FiO₂ (%):",
        min_value=30,
        max_value=100,
        value=50,
        step=5,
        key="peep_fio2_percent"
    )
    
    fio2_decimal = fio2_percent / 100
    
    if st.button("Tính toán", type="primary", key="calc_peep"):
        recommendation = recommend_peep(fio2_decimal)
        
        st.markdown("### 📊 Kết Quả")
        
        render_result_box(
            "PEEP khuyến nghị",
            f"{recommendation['peep_recommended']:.0f} cmH2O",
            subtitle=f"Range: {recommendation['peep_min']}-{recommendation['peep_max']} cmH2O",
            color="primary",
            icon="📊"
        )
        
        st.markdown("---")
        st.markdown("### 📋 ARDSNet PEEP/FiO2 Table")
        
        table = get_peep_fio2_table()
        
        # Highlight current row
        for entry in table:
            is_current = entry["FiO2"] * 100 == fio2_percent
            bg_color = "#e3f2fd" if is_current else "white"
            border = "3px solid #2196f3" if is_current else "1px solid #ddd"
            
            st.markdown(f"""
            <div style="padding: 10px; margin: 5px 0; background: {bg_color}; border-left: {border}; border-radius: 4px;">
                <strong>FiO₂ {entry['FiO2']*100:.0f}%:</strong> PEEP {entry['PEEP_min']}-{entry['PEEP_max']} cmH2O
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.info("""
        **💡 Lưu ý:**
        - PEEP được điều chỉnh để đạt SpO2 88-95% hoặc PaO2 55-80 mmHg
        - Theo dõi huyết động khi tăng PEEP
        - Cân nhắc recruitment maneuver nếu cần
        - Tránh PEEP quá cao gây barotrauma
        """)


def render_plateau_pressure_calculator():
    """Render Plateau Pressure calculator"""
    st.subheader("📈 Plateau Pressure Calculator")
    st.caption("Tính plateau pressure và driving pressure")
    
    st.markdown("""
    **Plateau Pressure:** Áp lực trong phổi khi giữ hơi thở cuối thì hít vào (end-inspiratory pause).
    **Mục tiêu:** < 30 cmH2O (lung-protective ventilation)
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        vt_ml = st.number_input(
            "Tidal Volume (ml):",
            min_value=100,
            max_value=1000,
            value=420,
            step=10,
            format="%d",
            key="plateau_vt"
        )
        
        compliance = st.number_input(
            "Static Compliance (ml/cmH2O):",
            min_value=10,
            max_value=200,
            value=50,
            step=1,
            format="%d",
            key="plateau_compliance",
            help="C_static = Vt / (Plateau - PEEP)"
        )
    
    with col2:
        peep = st.number_input(
            "PEEP (cmH2O):",
            min_value=0,
            max_value=30,
            value=10,
            step=1,
            format="%d",
            key="plateau_peep"
        )
    
    if st.button("Tính toán", type="primary", key="calc_plateau"):
        results = calculate_plateau_pressure(vt_ml, compliance, peep)
        
        if results["plateau"] is None:
            st.error("Không thể tính toán. Vui lòng kiểm tra giá trị nhập vào.")
        else:
            st.markdown("### 📊 Kết Quả")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Check if safe
                if results["plateau"] < 30:
                    status = "✅ An toàn"
                    color = "success"
                elif results["plateau"] < 35:
                    status = "⚠️ Cao"
                    color = "warning"
                else:
                    status = "🚨 Rất cao"
                    color = "error"
                
                render_result_box(
                    "Plateau Pressure",
                    f"{results['plateau']:.1f} cmH2O",
                    subtitle=status,
                    color=color,
                    icon="📈"
                )
            
            with col2:
                # Check driving pressure
                if results["driving_pressure"] and results["driving_pressure"] < 15:
                    dp_status = "✅ Tốt"
                    dp_color = "success"
                elif results["driving_pressure"] and results["driving_pressure"] < 20:
                    dp_status = "⚠️ Trung bình"
                    dp_color = "warning"
                else:
                    dp_status = "🚨 Cao"
                    dp_color = "error"
                
                render_result_box(
                    "Driving Pressure",
                    f"{results['driving_pressure']:.1f} cmH2O",
                    subtitle=dp_status,
                    color=dp_color,
                    icon="📉"
                )
            
            st.markdown("---")
            st.warning(f"""
            **⚠️ Khuyến nghị:**
            - **Plateau pressure:** Mục tiêu < 30 cmH2O (hiện tại: {results['plateau']:.1f} cmH2O)
            - **Driving pressure:** Mục tiêu < 15 cmH2O (hiện tại: {results['driving_pressure']:.1f} cmH2O)
            - Nếu cao: Giảm Vt hoặc tăng PEEP (nếu phù hợp)
            - **Lưu ý:** Driving pressure = Plateau - PEEP
            """)


def render_weaning_calculator():
    """Render Ventilator Weaning calculator"""
    st.subheader("🔄 Ventilator Weaning Calculator")
    st.caption("Đánh giá sẵn sàng cai máy thở (RSBI)")
    
    st.markdown("""
    **RSBI (Rapid Shallow Breathing Index)** = RR / Vt (L)
    
    - **RSBI < 105:** Tốt - Có thể cai máy thở
    - **RSBI 105-130:** Trung bình - Cần theo dõi
    - **RSBI > 130:** Kém - Khó cai máy thở
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rr = st.number_input(
            "Respiratory Rate (breaths/min):",
            min_value=5,
            max_value=50,
            value=20,
            step=1,
            format="%d",
            key="weaning_rr"
        )
    
    with col2:
        vt_liters = st.number_input(
            "Tidal Volume (L):",
            min_value=0.1,
            max_value=2.0,
            value=0.5,
            step=0.05,
            format="%.2f",
            key="weaning_vt",
            help="Tidal volume trong spontaneous breathing"
        )
    
    if st.button("Tính toán", type="primary", key="calc_weaning"):
        results = calculate_rsbi(rr, vt_liters)
        
        if results["rsbi"] is None:
            st.error("Không thể tính toán. Vt phải > 0.")
        else:
            st.markdown("### 📊 Kết Quả")
            
            render_result_box(
                "RSBI",
                f"{results['rsbi']:.1f}",
                subtitle=results["interpretation"],
                color=results["color"],
                icon="🔄"
            )
            
            st.markdown("---")
            st.info(f"""
            **💡 Đánh giá:**
            - **RSBI:** {results['rsbi']:.1f} = {rr:.0f} / {vt_liters:.2f}
            - **Kết luận:** {results['interpretation']}
            
            **Tiêu chí cai máy thở:**
            - RSBI < 105
            - P/F ratio ≥ 200
            - PEEP ≤ 8 cmH2O
            - FiO₂ ≤ 50%
            - Bệnh nhân tỉnh, hợp tác
            - Không có shock, không có rối loạn nhịp tim nặng
            """)


def render_ventilator_calculator():
    """Main function to render ventilator management tools"""
    
    st.markdown("## 🫁 Ventilator Management Tools")
    st.markdown("""
    Công cụ quản lý máy thở cho ICU:
    - Ideal Body Weight (IBW) - Tính trọng lượng lý tưởng
    - Tidal Volume - Tính thể tích khí lưu thông
    - PEEP Calculator - Khuyến nghị PEEP dựa trên FiO2
    - Plateau Pressure - Tính áp lực cao nguyên
    - Weaning Parameters - Đánh giá sẵn sàng cai máy thở
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📏 IBW",
        "💨 Tidal Volume",
        "📊 PEEP",
        "📈 Plateau Pressure",
        "🔄 Weaning"
    ])
    
    with tab1:
        render_ibw_calculator()
    
    with tab2:
        render_tidal_volume_calculator()
    
    with tab3:
        render_peep_calculator()
    
    with tab4:
        render_plateau_pressure_calculator()
    
    with tab5:
        render_weaning_calculator()
    
    st.markdown("---")
    st.warning("""
    **⚠️ QUAN TRỌNG:**
    - Các tính toán này chỉ mục đích hỗ trợ quyết định lâm sàng
    - Luôn đánh giá lâm sàng và điều chỉnh theo đáp ứng của bệnh nhân
    - Theo dõi huyết động, ABG, và các thông số khác
    - Tuân thủ hướng dẫn của Bộ Y tế, Bệnh viện
    """)

