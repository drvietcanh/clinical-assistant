"""
Valproic Acid TDM Calculator
Therapeutic Drug Monitoring cho Valproic Acid (Sodium Valproate)
"""

import streamlit as st
from drugs.tdm.base_template import TDMCalculator
from drugs.tdm.tdm_config import TDM_DRUGS


def calculate_valproic_acid_dose(
    weight_kg,
    current_level_mg_l=None,
    target_level_mg_l=75.0,
    current_dose_mg=None
):
    """
    Calculate Valproic Acid dose
    
    Args:
        weight_kg: Body weight
        current_level_mg_l: Current level if available
        target_level_mg_l: Target level (50-100 mg/L)
        current_dose_mg: Current dose if available
    
    Returns:
        dict with dosing information
    """
    # Initial dose: 10-15 mg/kg/day for adults
    # Usually started at 500-1000 mg/day
    
    if current_level_mg_l and current_dose_mg:
        # Dose adjustment based on current level
        # Linear relationship approximation
        dose_ratio = target_level_mg_l / current_level_mg_l
        new_dose = current_dose_mg * dose_ratio
    else:
        # Initial dose calculation
        base_dose_per_kg = 12  # mg/kg/day
        new_dose = base_dose_per_kg * weight_kg
    
    # Round to practical dosing (200mg, 500mg tablets/capsules)
    practical_doses = [200, 300, 400, 500, 600, 750, 1000, 1250, 1500, 2000, 2500]
    closest_dose = min(practical_doses, key=lambda x: abs(x - new_dose))
    
    # Frequency: Usually BID or TID
    if closest_dose <= 1000:
        frequency = 2  # BID
    else:
        frequency = 3  # TID
    
    dose_per_time = closest_dose / frequency
    
    return {
        "dose_mg": closest_dose,
        "dose_mg_calculated": new_dose,
        "frequency": frequency,
        "dose_per_time": dose_per_time,
        "target_level": target_level_mg_l
    }


def interpret_valproic_acid_level(level_mg_l):
    """
    Interpret Valproic Acid level
    
    Args:
        level_mg_l: Valproic acid level (mg/L)
    
    Returns:
        dict with interpretation
    """
    calc = TDMCalculator(
        drug_name="Valproic Acid",
        drug_icon="🧠",
        therapeutic_range="50-100 mg/L",
        target_min=50.0,
        target_max=100.0,
        toxic_threshold=150.0,
        unit="mg/L",
        sampling_time="Trough (pre-dose)",
        half_life_hours=12.0
    )
    
    return calc.interpret_level(level_mg_l)


def render_valproic_acid_tdm():
    """Render Valproic Acid TDM Calculator Interface"""
    
    calc = TDMCalculator(
        drug_name="Valproic Acid",
        drug_icon="🧠",
        therapeutic_range="50-100 mg/L",
        target_min=50.0,
        target_max=100.0,
        toxic_threshold=150.0,
        unit="mg/L",
        sampling_time="Trough (pre-dose)",
        half_life_hours=12.0
    )
    
    calc.render_header()
    
    calc.render_info_box("""
    **Lưu ý đặc biệt:**
    - Protein binding cao (90-95%) - theo dõi free level nếu có bệnh lý giảm protein
    - Nhiều tương tác thuốc (enzyme inhibitor)
    - Độc tính gan (theo dõi LFT)
    - Teratogenic (tránh dùng khi mang thai)
    """)
    
    st.markdown("---")
    
    # Tab selection
    tab1, tab2 = st.tabs(["🧮 Tính Liều", "📊 Giải Thích Nồng Độ"])
    
    with tab1:
        st.markdown("### 📋 Thông Số Bệnh Nhân")
        
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input(
                "Cân nặng (kg)",
                min_value=30.0,
                max_value=150.0,
                value=70.0,
                step=1.0,
                key="vpa_weight"
            )
            
            target_level = st.number_input(
                "Mục tiêu nồng độ (mg/L)",
                min_value=50.0,
                max_value=100.0,
                value=75.0,
                step=5.0,
                key="vpa_target",
                help="Thường 50-100 mg/L"
            )
        
        with col2:
            has_current_level = st.checkbox(
                "Có nồng độ hiện tại?",
                key="vpa_has_level"
            )
        
        if has_current_level:
            st.markdown("---")
            st.markdown("#### 📊 Nồng Độ Hiện Tại")
            
            col1, col2 = st.columns(2)
            
            with col1:
                current_level = st.number_input(
                    "Nồng độ hiện tại (mg/L)",
                    min_value=0.0,
                    max_value=200.0,
                    value=60.0,
                    step=5.0,
                    key="vpa_current_level"
                )
            
            with col2:
                current_dose = st.number_input(
                    "Liều hiện tại (mg/ngày)",
                    min_value=200.0,
                    max_value=3000.0,
                    value=1000.0,
                    step=100.0,
                    key="vpa_current_dose"
                )
        else:
            current_level = None
            current_dose = None
        
        st.markdown("---")
        
        if st.button("🧮 Tính Liều Valproic Acid", type="primary", use_container_width=True):
            result = calculate_valproic_acid_dose(
                weight, current_level, target_level, current_dose
            )
            
            st.markdown("### 💊 Kết quả Tính Liều")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(
                    "Liều đề xuất",
                    f"{result['dose_mg']:.0f} mg/ngày"
                )
            
            with col2:
                freq_text = "BID" if result['frequency'] == 2 else "TID"
                st.metric(
                    "Tần suất",
                    freq_text
                )
            
            with col3:
                st.metric(
                    "Liều mỗi lần",
                    f"{result['dose_per_time']:.0f} mg"
                )
            
            st.markdown("---")
            
            st.success(f"""
            **💊 Khuyến nghị:**
            
            **Liều:** {result['dose_mg']:.0f} mg/ngày chia **{result['frequency']} lần** ({result['dose_per_time']:.0f} mg/lần)
            
            **Lưu ý:**
            - Mục tiêu nồng độ: {result['target_level']:.1f} mg/L
            - Bắt đầu với liều thấp (500-1000 mg/ngày), tăng dần
            - Theo dõi nồng độ sau 3-5 ngày (steady state)
            - Kiểm tra LFT trước và định kỳ
            - Nhiều tương tác thuốc (kiểm tra trước khi dùng)
            """)
            
            st.markdown("---")
            st.markdown("### ⚠️ Cảnh Báo Độc Tính")
            
            st.error("""
            **Triệu chứng độc tính Valproic Acid:**
            
            **Thần kinh:**
            - Chóng mặt, buồn ngủ
            - Tremor
            - Lú lẫn
            - Hôn mê (nồng độ rất cao)
            
            **Gan:**
            - Tăng transaminase
            - Suy gan (hiếm nhưng nặng)
            - Đặc biệt nguy hiểm ở trẻ em < 2 tuổi
            
            **Tụy:**
            - Viêm tụy (hiếm)
            
            **Huyết học:**
            - Giảm tiểu cầu
            - Giảm fibrinogen
            
            **Yếu tố tăng nguy cơ độc tính:**
            - Nồng độ > 150 mg/L
            - Suy gan
            - Trẻ em < 2 tuổi
            - Dùng đồng thời với enzyme inhibitors
            """)
    
    with tab2:
        calc.render_level_interpretation_tab()
    
    calc.render_references("""
    - **Valproic Acid TDM Guidelines**
    - **Therapeutic range:** 50-100 mg/L
    - **Half-life:** 8-17 hours
    - **Protein binding:** 90-95% (theo dõi free level nếu giảm protein)
    - **Volume of distribution:** 0.1-0.2 L/kg
    - **Teratogenic:** Tránh dùng khi mang thai (neural tube defects)
    """)

