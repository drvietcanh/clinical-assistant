"""
Patient Input Forms for Dosing Calculator
Tách tất cả patient input forms ra khỏi main render function
"""

import streamlit as st
from ..dosing_calculator import calculate_ibw, calculate_abw, calculate_bmi


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def render_patient_inputs():
    """
    Render tất cả patient input forms
    Returns: dict với tất cả patient data
    """
    col1, col2 = st.columns(2)
    
    patient_data = {}
    
    with col1:
        # Age - support pediatric
        age = st.number_input(
            "Tuổi (năm)",
            min_value=0,
            max_value=120,
            value=65,
            step=1,
            key="dosing_age",
            help="Nhập 0-17 cho trẻ em (tự động dùng liều pediatric)"
        )
        is_pediatric = age < 18
        if is_pediatric:
            st.info(f"👶 **Trẻ em:** Tự động áp dụng liều pediatric")
        
        patient_data['age'] = age
        patient_data['is_pediatric'] = is_pediatric
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=10.0,
            max_value=200.0,
            value=50.0,
            step=1.0,
            format="%.1f",
            key="dosing_weight"
        )
        patient_data['weight'] = weight
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=50,
            max_value=220,
            value=160,
            step=1,
            format="%d",
            key="dosing_height"
        )
        patient_data['height'] = height
        
        # Special conditions
        st.markdown("#### 🏥 Tình trạng đặc biệt")
        is_icu = st.checkbox("🏥 Bệnh nhân ICU", key="dosing_icu", help="Tự động điều chỉnh cho ICU: ARC, Vd changes")
        patient_data['is_icu'] = is_icu
        
        # Enhanced HD/PD selection
        dialysis_type = st.radio(
            "Tình trạng thận đặc biệt:",
            ["Không có", "Lọc máu ngắt quãng (HD)", "Lọc máu liên tục (CRRT/CVVH)", "Lọc màng bụng (PD)"],
            key="dialysis_type",
            help="Chọn loại lọc máu để có hướng dẫn liều cụ thể"
        )
        is_hemodialysis = dialysis_type == "Lọc máu ngắt quãng (HD)"
        is_continuous_hd = dialysis_type == "Lọc máu liên tục (CRRT/CVVH)"
        is_peritoneal_dialysis = dialysis_type == "Lọc màng bụng (PD)"
        
        patient_data['is_hemodialysis'] = is_hemodialysis
        patient_data['is_continuous_hd'] = is_continuous_hd
        patient_data['is_peritoneal_dialysis'] = is_peritoneal_dialysis

        # ECMO flag (Phase 1)
        is_ecmo = st.checkbox(
            "🫁 ECMO",
            key="dosing_ecmo",
            help="ECMO có thể làm thay đổi Vd/clearance của một số kháng sinh. Tính năng này sẽ bổ sung guidance và nhắc TDM khi phù hợp."
        )
        patient_data['is_ecmo'] = is_ecmo
        
        if is_hemodialysis:
            hd_schedule = st.selectbox(
                "Lịch lọc máu:",
                ["3 lần/tuần", "Hàng ngày", "Khác"],
                key="hd_schedule",
                help="Thời gian lọc máu ảnh hưởng đến thời điểm cho thuốc"
            )
            patient_data['hd_schedule'] = hd_schedule
        
        is_pregnant = st.checkbox("🤰 Có thai", key="dosing_pregnant")
        is_breastfeeding = st.checkbox("🤱 Đang cho con bú", key="dosing_breastfeeding")
        
        patient_data['is_pregnant'] = is_pregnant
        patient_data['is_breastfeeding'] = is_breastfeeding
        
        # ICU-specific inputs
        if is_icu:
            st.markdown("#### 🔴 Thông số ICU")
            shock_type = st.selectbox(
                "Loại shock:",
                ["Không có", "Sốc nhiễm khuẩn (Septic)", "Sốc tim (Cardiogenic)", "Sốc phân bố (Distributive)", "Sốc giảm thể tích (Hypovolemic)"],
                key="dosing_shock_type"
            )
            shock_type_map = {
                "Không có": None,
                "Sốc nhiễm khuẩn (Septic)": "septic",
                "Sốc tim (Cardiogenic)": "cardiogenic",
                "Sốc phân bố (Distributive)": "distributive",
                "Sốc giảm thể tích (Hypovolemic)": "hypovolemic"
            }
            shock_type_code = shock_type_map.get(shock_type, None)
            patient_data['shock_type'] = shock_type_code
            
            albumin_gdl = st.number_input(
                "Albumin (g/dL)",
                min_value=1.0,
                max_value=5.5,
                value=3.5,
                step=0.1,
                format="%.1f",
                key="dosing_albumin",
                help="Bình thường: 3.5-5.0 g/dL. <3.0 g/dL: ảnh hưởng liều kháng sinh liên kết protein cao"
            )
            
            if albumin_gdl < 3.0:
                st.warning(f"🚨 Albumin rất thấp ({albumin_gdl:.1f} g/dL) - Cần điều chỉnh liều kháng sinh liên kết protein cao!")
            elif albumin_gdl < 3.5:
                st.info(f"⚠️ Albumin giảm ({albumin_gdl:.1f} g/dL)")
            
            patient_data['albumin_gdl'] = albumin_gdl
        else:
            patient_data['shock_type'] = None
            patient_data['albumin_gdl'] = None
    
    with col2:
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="dosing_sex"
        )
        patient_data['sex'] = sex
        
        # Creatinine
        st.markdown("#### Creatinine máu")
        scr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="dosing_scr_unit"
        )
        
        if scr_unit == "µmol/L":
            scr_value = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                format="%d",
                key="dosing_scr_umol"
            )
            scr_mgdl = scr_value / 88.4
            st.caption(f"≈ {_format_num(scr_mgdl, 1)} mg/dL")
        else:
            scr_mgdl = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                format="%.1f",
                key="dosing_scr_mgdl"
            )
            st.caption(f"≈ {round(scr_mgdl * 88.4)} µmol/L")
        
        patient_data['scr_mgdl'] = scr_mgdl
    
    return patient_data


def get_patient_data():
    """
    Helper function để lấy patient data từ session state hoặc inputs
    Returns: dict với tất cả patient data đã tính toán
    """
    patient_data = render_patient_inputs()
    
    # Calculate derived values
    age = patient_data['age']
    weight = patient_data['weight']
    height = patient_data['height']
    sex = patient_data['sex']
    
    # Calculate IBW, ABW, BMI
    ibw = calculate_ibw(height, sex)
    bmi = calculate_bmi(weight, height)
    is_obese = bmi > 30 or weight > ibw * 1.25
    abw = calculate_abw(weight, ibw) if is_obese else weight
    
    patient_data['ibw'] = ibw
    patient_data['bmi'] = bmi
    patient_data['is_obese'] = is_obese
    patient_data['abw'] = abw
    
    return patient_data

