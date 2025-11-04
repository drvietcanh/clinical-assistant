"""
eGFR Calculator - Input Form UI Components
Handles all input fields and form sections
"""

import streamlit as st
from .egfr_calculators import calculate_ibw, calculate_abw


def render_input_form():
    """Render the input form section for eGFR calculator"""
    
    st.subheader("📝 Nhập thông tin bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input(
            "Tuổi",
            min_value=18,
            max_value=120,
            value=50,
            step=1,
            help="Tuổi của bệnh nhân"
        )
        
        gender = st.radio(
            "Giới tính",
            options=["male", "female"],
            format_func=lambda x: "Nam" if x == "male" else "Nữ",
            horizontal=True
        )
        
        height_cm = st.number_input(
            "Chiều cao (cm)",
            min_value=100,
            max_value=250,
            value=170,
            step=1,
            help="Cần cho tính BSA và GFR tuyệt đối"
        )
        
        weight_kg = st.number_input(
            "Cân nặng (kg)",
            min_value=20,
            max_value=300,
            value=70,
            step=1,
            help="Cân nặng thực tế"
        )
    
    with col2:
        race = st.radio(
            "Chủng tộc",
            options=["non-black", "black"],
            format_func=lambda x: "Châu Phi / Da đen" if x == "black" else "Khác (Châu Á, Châu Âu...)",
            help="Hệ số điều chỉnh cho CKD-EPI và MDRD"
        )
        
        creatinine_unit = st.radio(
            "Đơn vị Creatinine",
            options=["µmol/L", "mg/dL"],
            index=0,
            horizontal=True,
            help="µmol/L phổ biến ở Việt Nam"
        )
        
        if creatinine_unit == "µmol/L":
            creatinine = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=2000.0,
                value=88.0,
                step=1.0,
                format="%.1f",
                help="Bình thường: Nam 62-106, Nữ 44-80 µmol/L"
            )
            st.caption(f"💡 = {creatinine / 88.4:.1f} mg/dL")
        else:
            creatinine = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=25.0,
                value=1.0,
                step=0.1,
                format="%.1f",
                help="Bình thường: Nam 0.7-1.2, Nữ 0.5-0.9 mg/dL"
            )
            st.caption(f"💡 = {creatinine * 88.4:.0f} µmol/L")
    
    # Advanced options
    st.markdown("---")
    st.markdown("### ⚙️ Tùy chọn nâng cao")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Convert creatinine to mg/dL for calculations
        if creatinine_unit == "µmol/L":
            creatinine_mg = creatinine / 88.4
        else:
            creatinine_mg = creatinine
        
        use_abw = st.checkbox(
            "Sử dụng Adjusted Body Weight (cho béo phì)",
            help="Nên dùng nếu BMI > 30 hoặc cân nặng > 130% IBW"
        )
    
    with col2:
        # Calculate IBW and ABW if needed
        if use_abw:
            ibw = calculate_ibw(height_cm, gender)
            abw = calculate_abw(weight_kg, ibw)
            st.info(f"IBW: {ibw:.1f} kg, ABW: {abw:.1f} kg")
        else:
            ibw = calculate_ibw(height_cm, gender)
            abw = None
    
    # BSA formula selection
    st.markdown("**Công thức tính BSA:**")
    bsa_formula = st.radio(
        "Chọn công thức BSA",
        options=["mosteller", "dubois", "haycock", "boyd", "shuter_aslani"],
        format_func=lambda x: {
            "mosteller": "Mosteller (1987) ⭐ - Khuyến nghị KDIGO, FDA, NCCN",
            "dubois": "Du Bois (1916) - Công thức cổ điển, chuẩn 1.73m²",
            "haycock": "Haycock (1978) - Tốt cho mọi lứa tuổi",
            "boyd": "Boyd (1935) - Tốt cho béo phì/gầy",
            "shuter_aslani": "Shuter & Aslani (2000) - Hiện đại, chính xác cao"
        }[x],
        horizontal=False,
        help="Mosteller được khuyến nghị cho hầu hết trường hợp"
    )
    
    # Calculate BMI
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    st.markdown("---")
    
    # Return all input values
    return {
        "age": age,
        "gender": gender,
        "height_cm": height_cm,
        "weight_kg": weight_kg,
        "race": race,
        "creatinine_unit": creatinine_unit,
        "creatinine": creatinine,
        "creatinine_mg": creatinine_mg,
        "use_abw": use_abw,
        "abw": abw,
        "ibw": ibw,
        "bsa_formula": bsa_formula,
        "bmi": bmi,
        "height_m": height_m
    }

