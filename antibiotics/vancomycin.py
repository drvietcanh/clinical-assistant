"""
Vancomycin Dosing Calculator
Loading and Maintenance Dosing with TDM
"""

import streamlit as st


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def calculate_vancomycin_dose(
    age: int,
    weight_kg: float,
    height_cm: float,
    sex: str,
    scr_mgdl: float,
    indication: str,
) -> dict:
    """
    Hàm tính liều Vancomycin thuần (không phụ thuộc UI) để tiện test.
    Trả về:
      - ibw, dosing_weight, crcl, loading_dose_mg_kg, loading_dose_mg,
        maintenance_dose_mg, interval_h
    """
    # IBW
    if sex == "Nam":
        ibw = 50 + 2.3 * ((height_cm - 152.4) / 2.54)
    else:
        ibw = 45.5 + 2.3 * ((height_cm - 152.4) / 2.54)

    # Obesity check & dosing weight
    if weight_kg > ibw * 1.25:
        dosing_weight = ibw + 0.4 * (weight_kg - ibw)
    else:
        dosing_weight = weight_kg

    # CrCl (Cockcroft-Gault) với trọng lượng dùng để tính liều
    crcl = ((140 - age) * dosing_weight) / (72 * scr_mgdl)
    if sex == "Nữ":
        crcl *= 0.85

    # Loading dose
    if "nặng" in indication or "nội tâm mạc" in indication or "màng não" in indication:
        loading_dose_mg_kg = 30
    else:
        loading_dose_mg_kg = 25
    loading_dose_mg = round((dosing_weight * loading_dose_mg_kg) / 250) * 250

    # Maintenance dose
    if crcl >= 90:
        maint_mg = 15 * dosing_weight
        interval = 12
    elif crcl >= 60:
        maint_mg = 15 * dosing_weight
        interval = 12
    elif crcl >= 40:
        maint_mg = 12.5 * dosing_weight
        interval = 12
    elif crcl >= 20:
        maint_mg = 10 * dosing_weight
        interval = 24
    elif crcl >= 10:
        maint_mg = 7.5 * dosing_weight
        interval = 24
    else:
        maint_mg = 5 * dosing_weight
        interval = 48

    maint_mg = round(maint_mg / 250) * 250

    return {
        "ibw": ibw,
        "dosing_weight": dosing_weight,
        "crcl": round(crcl, 1),
        "loading_dose_mg_kg": loading_dose_mg_kg,
        "loading_dose_mg": loading_dose_mg,
        "maintenance_dose_mg": maint_mg,
        "interval_h": interval,
    }


def render():
    """Vancomycin Dosing Calculator"""
    st.subheader("💉 Vancomycin - Tính liều")
    st.caption("Liều Khởi Đầu & Theo dõi Nồng Độ Thuốc (TDM)")
    
    st.info("""
    **Vancomycin TDM** - Hướng dẫn theo ASHP/IDSA/SIDP 2020:
    - Mục tiêu AUC/MIC ≥400 cho nhiễm khuẩn nặng
    - Liều khởi đầu dựa trên cân nặng và CrCl
    - Điều chỉnh theo nồng độ máu
    """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 📋 Thông số bệnh nhân")
        
        # Patient info
        age = st.number_input(
            "Tuổi (năm)",
            min_value=18,
            max_value=120,
            value=65,
            step=1,
            key="vanco_age"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=200.0,
            value=50.0,
            step=0.5,
            format="%.1f",
            help="Cân nặng thực tế. Nếu béo phì sử dụng Adjusted Body Weight",
            key="vanco_weight"
        )
        
        height = st.number_input(
            "Chiều cao (cm)",
            min_value=120,
            max_value=220,
            value=160,
            step=1,
            format="%d",
            key="vanco_height"
        )
        
        sex = st.radio(
            "Giới tính",
            ["Nam", "Nữ"],
            horizontal=True,
            key="vanco_sex"
        )
        
        # Creatinine
        st.markdown("#### Creatinine máu")
        scr_unit = st.radio(
            "Đơn vị:",
            ["µmol/L", "mg/dL"],
            horizontal=True,
            index=0,
            key="vanco_scr_unit"
        )
        
        if scr_unit == "µmol/L":
            scr_umol = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=1500.0,
                value=88.0,
                step=5.0,
                format="%d",
                key="vanco_scr_umol"
            )
            scr_mgdl = scr_umol / 88.4
            st.caption(f"≈ {_format_num(scr_mgdl, 1)} mg/dL")
        else:  # mg/dL
            scr_mgdl = st.number_input(
                "Creatinine (mg/dL)",
                min_value=0.1,
                max_value=15.0,
                value=1.0,
                step=0.1,
                format="%.1f",
                key="vanco_scr_mgdl"
            )
            st.caption(f"≈ {round(scr_mgdl * 88.4)} µmol/L")
        
        # Tính liều bằng hàm thuần để tái sử dụng & test
        dose_result = calculate_vancomycin_dose(
            age=age,
            weight_kg=weight,
            height_cm=height,
            sex=sex,
            scr_mgdl=scr_mgdl,
            indication=indication,
        )

        ibw = dose_result["ibw"]
        dosing_weight = dose_result["dosing_weight"]
        crcl = dose_result["crcl"]
        loading_dose_mg_kg = dose_result["loading_dose_mg_kg"]
        loading_dose = dose_result["loading_dose_mg"]
        maint_dose = dose_result["maintenance_dose_mg"]
        interval = dose_result["interval_h"]

        # Hiển thị IBW/ABW thông tin
        if weight > ibw * 1.25:
            abw = dosing_weight
            st.info(f"**Béo phì:** IBW = {ibw:.1f} kg → Dùng ABW = {abw:.1f} kg để tính liều")
        else:
            st.caption(f"IBW = {_format_num(ibw, 1)} kg")

        st.metric("CrCl (Cockcroft-Gault)", f"{crcl} mL/phút")
        
        # Indication
        st.markdown("#### Chỉ định sử dụng")
        indication = st.selectbox(
            "Loại nhiễm khuẩn:",
            [
                "Nhiễm khuẩn nặng/phức tạp (MRSA)",
                "Viêm nội tâm mạc",
                "Viêm màng não",
                "Viêm xương tủy",
                "Nhiễm khuẩn huyết",
                "Viêm phổi do MRSA",
                "Nhiễm khuẩn da và mô mềm"
            ],
            key="vanco_indication"
        )
        
        if st.button("🧮 Tính liều Vancomycin", type="primary", key="vanco_calc"):
            with col2:
                st.markdown("### 📊 Liều Khuyến cáo")
                st.success(f"## Loading Dose")
                st.metric("Liều khởi đầu", f"{loading_dose:.0f} mg", f"{loading_dose_mg_kg} mg/kg")
                st.caption("Truyền trong 1-2 giờ")
                
                st.markdown("---")
                
                st.info(f"## Maintenance")
                st.metric("Liều duy trì", f"{maint_dose:.0f} mg")
                st.metric("Tần suất", f"Mỗi {interval}h")
                st.caption(f"Liều ngày: {round(maint_dose * (24/interval))} mg/ngày")
            
            st.markdown("### 💡 Chi tiết tính toán")
            st.write(f"- **Cân nặng tính liều:** {dosing_weight:.1f} kg")
            st.write(f"- **CrCl:** {crcl} mL/phút")
            st.write(f"- **Loading dose:** {loading_dose_mg_kg} mg/kg × {dosing_weight:.1f} kg = {loading_dose:.0f} mg")
            st.write(f"- **Maintenance:** {maint_dose:.0f} mg mỗi {interval}h")
            
            st.markdown("---")
            st.markdown("### 🎯 Mục tiêu TDM (Therapeutic Drug Monitoring)")
            
            if "nặng" in indication or "nội tâm mạc" in indication or "viêm phổi" in indication.lower():
                st.error("""
                **Nhiễm khuẩn nặng - Mục tiêu AUC/MIC ≥400**
                
                **Hướng dẫn TDM 2020:**
                - **KHÔNG** dùng trough-only monitoring
                - **KHUYẾN CÁO:** AUC-guided dosing
                - Mục tiêu AUC₀₋₂₄: 400-600 mg·h/L
                - Cần lấy ít nhất 2 mẫu máu để tính AUC
                
                **Thời điểm lấy mẫu (AUC monitoring):**
                - Mẫu 1: Ngay trước liều (trough)
                - Mẫu 2: 1-2h sau kết thúc truyền (peak)
                - Lấy mẫu sau khi đạt steady-state (liều 4-5)
                """)
            else:
                st.warning("""
                **Mục tiêu TDM:**
                
                **Theo hướng dẫn 2020:**
                - Ưu tiên AUC-guided dosing
                - AUC₀₋₂₄: 400-600 mg·h/L
                
                **Nếu chỉ theo dõi trough (cách cũ):**
                - Mục tiêu nồng độ đáy: 10-20 mg/L
                - Nhiễm khuẩn nặng: 15-20 mg/L
                - Lấy mẫu ngay trước liều tiếp theo
                """)
            
            st.markdown("### ⚠️ Lưu ý An Toàn")
            st.warning("""
            **Theo dõi độc tính:**
            - ⚠️ Độc thận: Creatinine hàng ngày, đặc biệt nếu CrCl thấp
            - ⚠️ Độc tai: Hỏi về ù tai, chóng mặt
            - ⚠️ "Red man syndrome": Truyền chậm >1h, có thể dùng kháng histamine
            
            **Tương tác thuốc:**
            - Tăng độc thận: Aminoglycosides, NSAID, contrast, vancomycin + piperacillin/tazobactam
            - Cần theo dõi sát nếu phối hợp
            
            **Điều chỉnh liều:**
            - Dựa trên nồng độ máu (AUC hoặc trough)
            - Theo dõi chức năng thận hàng ngày
            - Tham khảo dược sĩ lâm sàng để tính AUC
            """)
            
            st.markdown("### 📝 Hướng dẫn truyền")
            st.info(f"""
            **Quy trình truyền Vancomycin:**
            
            **Loading dose: {loading_dose:.0f} mg**
            - Pha trong 250 mL NS hoặc D5W
            - Nồng độ tối đa: 5 mg/mL
            - Tốc độ truyền: ≤10 mg/phút
            - **Thời gian truyền:** Ít nhất {max(60, loading_dose/10):.0f} phút (khuyến cáo 1-2 giờ)
            
            **Maintenance: {maint_dose:.0f} mg mỗi {interval}h**
            - Pha tương tự loading dose
            - Truyền trong 1-2 giờ
            - Bắt đầu sau {interval}h kể từ lúc bắt đầu loading dose
            
            **Lưu ý:**
            - Truyền chậm để tránh Red man syndrome
            - Có thể cho kháng histamine (diphenhydramine) nếu cần
            """)
            
            with st.expander("📚 Tài liệu tham khảo"):
                st.markdown("""
                **Vancomycin Dosing Guidelines**
                
                **Dosing Strategy:**
                - **Loading dose:** 25-30 mg/kg (based on actual or ABW)
                - **Maintenance:** 15-20 mg/kg/dose q8-12h
                - Adjust based on renal function
                
                **AUC/MIC Monitoring (2020 Guidelines):**
                - Target AUC₀₋₂₄/MIC: ≥400
                - For MIC = 1: Target AUC₀₋₂₄: 400-600 mg·h/L
                - Use Bayesian software or pharmacokinetic consultation
                
                **Theo dõi nồng độ đáy (Truyền thống):**
                - Mục tiêu nồng độ đáy: 10-20 mg/L
                - Serious infections (endocarditis, meningitis, pneumonia): 15-20 mg/L
                - Sample before 4th or 5th dose at steady state
                
                **Adjusted Body Weight (Obesity):**
                - ABW = IBW + 0.4 × (TBW - IBW)
                - Use for patients >25% above IBW
                
                **References:**
                - Rybak MJ et al. Am J Health Syst Pharm. 2020;77(11):835-864.
                - Vancomycin Consensus Guidelines 2020 (ASHP/IDSA/SIDP)
                - Liu C et al. Clin Infect Dis. 2011;52(3):e18-55.
                
                **Link:**
                - https://www.ashp.org/pharmacy-practice/resource-centers/infectious-diseases
                """)
    
    st.markdown("---")
    st.caption("⚠️ Công cụ hỗ trợ - Tham khảo dược sĩ lâm sàng để tính AUC chính xác")
