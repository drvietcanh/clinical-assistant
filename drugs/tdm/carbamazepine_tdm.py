"""
Carbamazepine TDM Calculator
Therapeutic Drug Monitoring cho Carbamazepine
"""

import streamlit as st
from drugs.tdm.base_template import TDMCalculator
from drugs.tdm.tdm_config import TDM_DRUGS


def calculate_carbamazepine_dose(
    weight_kg,
    current_level_mg_l=None,
    target_level_mg_l=8.0,
    current_dose_mg=None
):
    """
    Calculate Carbamazepine dose
    
    Args:
        weight_kg: Body weight
        current_level_mg_l: Current level if available
        target_level_mg_l: Target level (4-12 mg/L)
        current_dose_mg: Current dose if available
    
    Returns:
        dict with dosing information
    """
    # Initial dose: 10-20 mg/kg/day for adults
    # Usually started at 200-400 mg/day, increased gradually
    
    if current_level_mg_l and current_dose_mg:
        # Dose adjustment based on current level
        # Linear relationship approximation
        dose_ratio = target_level_mg_l / current_level_mg_l
        new_dose = current_dose_mg * dose_ratio
    else:
        # Initial dose calculation
        base_dose_per_kg = 15  # mg/kg/day
        new_dose = base_dose_per_kg * weight_kg
    
    # Round to practical dosing (100mg, 200mg tablets)
    practical_doses = [100, 200, 300, 400, 500, 600, 800, 1000, 1200]
    closest_dose = min(practical_doses, key=lambda x: abs(x - new_dose))
    
    # Frequency: Usually BID or TID
    if closest_dose <= 400:
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


def interpret_carbamazepine_level(level_mg_l):
    """
    Interpret Carbamazepine level
    
    Args:
        level_mg_l: Carbamazepine level (mg/L)
    
    Returns:
        dict with interpretation
    """
    calc = TDMCalculator(
        drug_name="Carbamazepine",
        drug_icon="🧠",
        therapeutic_range="4-12 mg/L",
        target_min=4.0,
        target_max=12.0,
        toxic_threshold=15.0,
        unit="mg/L",
        sampling_time="Trough (pre-dose)",
        half_life_hours=12.0
    )
    
    return calc.interpret_level(level_mg_l)


def render_carbamazepine_tdm():
    """Render Carbamazepine TDM Calculator Interface"""
    
    calc = TDMCalculator(
        drug_name="Carbamazepine",
        drug_icon="🧠",
        therapeutic_range="4-12 mg/L",
        target_min=4.0,
        target_max=12.0,
        toxic_threshold=15.0,
        unit="mg/L",
        sampling_time="Trough (pre-dose)",
        half_life_hours=12.0
    )
    
    calc.render_header()
    
    calc.render_info_box("""
    **Lưu ý đặc biệt:**
    - Nhiều tương tác thuốc (enzyme inducer)
    - Auto-induction: Nồng độ có thể giảm sau 2-4 tuần
    - Theo dõi nồng độ sau khi đạt steady state (5-7 ngày)
    - Có thể cần tăng liều sau auto-induction
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
                key="cbz_weight"
            )
            
            target_level = st.number_input(
                "Mục tiêu nồng độ (mg/L)",
                min_value=4.0,
                max_value=12.0,
                value=8.0,
                step=1.0,
                key="cbz_target",
                help="Thường 4-12 mg/L"
            )
        
        with col2:
            has_current_level = st.checkbox(
                "Có nồng độ hiện tại?",
                key="cbz_has_level"
            )
        
        if has_current_level:
            st.markdown("---")
            st.markdown("#### 📊 Nồng Độ Hiện Tại")
            
            col1, col2 = st.columns(2)
            
            with col1:
                current_level = st.number_input(
                    "Nồng độ hiện tại (mg/L)",
                    min_value=0.0,
                    max_value=20.0,
                    value=6.0,
                    step=0.5,
                    key="cbz_current_level"
                )
            
            with col2:
                current_dose = st.number_input(
                    "Liều hiện tại (mg/ngày)",
                    min_value=100.0,
                    max_value=2000.0,
                    value=600.0,
                    step=100.0,
                    key="cbz_current_dose"
                )
        else:
            current_level = None
            current_dose = None
        
        st.markdown("---")
        
        if st.button("🧮 Tính Liều Carbamazepine", type="primary", use_container_width=True):
            result = calculate_carbamazepine_dose(
                weight, current_level, target_level, current_dose
            )
            
            st.markdown("### 💊 Kết Quả Tính Liều")
            
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
            - Bắt đầu với liều thấp (200-400 mg/ngày), tăng dần
            - Theo dõi nồng độ sau 5-7 ngày (steady state)
            - Lưu ý auto-induction sau 2-4 tuần
            - Nhiều tương tác thuốc (kiểm tra trước khi dùng)
            """)
            
            st.markdown("---")
            st.markdown("### ⚠️ Cảnh Báo Độc Tính")
            
            st.error("""
            **Triệu chứng độc tính Carbamazepine:**
            
            **Thần kinh:**
            - Chóng mặt, buồn ngủ
            - Ataxia (mất thăng bằng)
            - Rối loạn thị giác
            - Lú lẫn
            
            **Tiêu hóa:**
            - Buồn nôn, nôn
            - Chán ăn
            
            **Huyết học:**
            - Giảm bạch cầu
            - Giảm tiểu cầu
            - Thiếu máu bất sản (hiếm nhưng nặng)
            
            **Yếu tố tăng nguy cơ:**
            - Nồng độ > 15 mg/L
            - Tương tác thuốc (đặc biệt với enzyme inhibitors)
            - Suy gan
            """)
    
    with tab2:
        calc.render_level_interpretation_tab()
    
    calc.render_references("""
    - **Carbamazepine TDM Guidelines**
    - **Therapeutic range:** 4-12 mg/L
    - **Half-life:** 12-17 hours (single dose), 5-14 hours (chronic use due to auto-induction)
    - **Protein binding:** 75-80%
    - **Volume of distribution:** 0.8-1.4 L/kg
    - **Auto-induction:** Occurs after 2-4 weeks, may require dose increase
    """)

