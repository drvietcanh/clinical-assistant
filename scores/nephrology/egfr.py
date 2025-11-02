"""
eGFR/GFR Calculator - Comprehensive
Tính tốc độ lọc cầu thận với nhiều công thức và tính BSA
Chuẩn hóa và tuyệt đối GFR
"""

import streamlit as st
import math


def calculate_bsa_mosteller(weight_kg, height_cm):
    """
    BSA using Mosteller formula - Recommended by KDIGO, FDA, NCCN, NIH
    
    Formula: BSA = √[(height_cm × weight_kg) / 3600]
    
    Mosteller is the optimal standard for clinical practice:
    - Simple, easy to remember
    - Low error (< 5%)
    - Recommended by major organizations
    """
    bsa = math.sqrt((weight_kg * height_cm) / 3600)
    return bsa


def calculate_bsa_dubois(weight_kg, height_cm):
    """
    BSA using Du Bois formula (1916) - Classic formula
    
    Formula: BSA = 0.007184 × W^0.425 × H^0.725
    
    Used as the basis for eGFR standardization to 1.73 m²
    """
    bsa = 0.007184 * (weight_kg ** 0.425) * (height_cm ** 0.725)
    return bsa


def calculate_bsa_haycock(weight_kg, height_cm):
    """
    BSA using Haycock formula (1978)
    
    Formula: BSA = 0.024265 × W^0.5378 × H^0.3964
    
    Validated from newborns to adults, good for all ages
    """
    bsa = 0.024265 * (weight_kg ** 0.5378) * (height_cm ** 0.3964)
    return bsa


def calculate_bsa_boyd(weight_kg, height_cm):
    """
    BSA using Boyd formula (1935)
    
    Formula: BSA = 0.0003207 × H^0.3 × [1000×W]^(0.7285 - 0.0188×log10(1000×W))
    
    Takes body density into account, good for obesity/extreme weight
    """
    log_factor = math.log10(1000 * weight_kg)
    bsa = 0.0003207 * (height_cm ** 0.3) * ((1000 * weight_kg) ** (0.7285 - 0.0188 * log_factor))
    return bsa


def calculate_bsa_shuter_aslani(weight_kg, height_cm):
    """
    BSA using Shuter & Aslani formula (2000)
    
    Formula: BSA = 0.00949 × W^0.441 × H^0.655
    
    Modern dataset, high accuracy for obesity and tall stature
    """
    bsa = 0.00949 * (weight_kg ** 0.441) * (height_cm ** 0.655)
    return bsa


def calculate_ckd_epi(creatinine_mg, age, gender, race="non-black"):
    """
    CKD-EPI 2009 formula
    
    Returns eGFR in mL/min/1.73m²
    """
    # Gender-specific parameters
    kappa = 0.7 if gender == "female" else 0.9
    alpha = -0.329 if gender == "female" else -0.411
    gender_factor = 1.018 if gender == "female" else 1.0
    
    # Race factor
    race_factor = 1.159 if race == "black" else 1.0
    
    # Calculate
    min_val = min(creatinine_mg / kappa, 1)
    max_val = max(creatinine_mg / kappa, 1)
    
    egfr = 141 * (min_val ** alpha) * (max_val ** -1.209) * (0.993 ** age) * gender_factor * race_factor
    
    return egfr


def calculate_mdrd(creatinine_mg, age, gender, race="non-black"):
    """
    MDRD formula
    
    Returns eGFR in mL/min/1.73m²
    """
    # Gender factor
    gender_factor = 0.742 if gender == "female" else 1.0
    
    # Race factor
    race_factor = 1.212 if race == "black" else 1.0
    
    # Calculate
    egfr = 175 * (creatinine_mg ** -1.154) * (age ** -0.203) * gender_factor * race_factor
    
    return egfr


def calculate_cockcroft_gault(age, weight_kg, creatinine_mg, gender, use_abw=False, abw=None):
    """
    Cockcroft-Gault formula for Creatinine Clearance
    
    Returns CrCl in mL/min
    """
    # Use ABW if specified
    weight_to_use = abw if (use_abw and abw) else weight_kg
    
    # Cockcroft-Gault formula
    crcl = ((140 - age) * weight_to_use) / (72 * creatinine_mg)
    
    if gender == "female":
        crcl = crcl * 0.85
    
    return crcl


def calculate_abw(actual_weight, ibw):
    """Calculate Adjusted Body Weight for obesity"""
    abw = ibw + 0.4 * (actual_weight - ibw)
    return abw


def calculate_ibw(height_cm, gender):
    """Calculate Ideal Body Weight using Devine formula"""
    if gender == "male":
        ibw = 50 + 0.91 * (height_cm - 152.4)
    else:  # female
        ibw = 45.5 + 0.91 * (height_cm - 152.4)
    
    return max(ibw, 0)


def convert_egfr_to_absolute_gfr(egfr_normalized, bsa_actual):
    """
    Convert eGFR normalized (mL/min/1.73m²) to absolute GFR (mL/min)
    
    GFR_absolute = eGFR_normalized × (BSA_actual / 1.73)
    """
    gfr_absolute = egfr_normalized * (bsa_actual / 1.73)
    return gfr_absolute


def interpret_egfr(egfr):
    """Interpret eGFR according to CKD stages"""
    
    if egfr >= 90:
        stage = "G1 - Bình thường hoặc cao"
        description = "Chức năng thận bình thường (nếu không có bằng chứng tổn thương thận khác)"
        color = "#28a745"
        icon = "✅"
        action = "Theo dõi thường quy nếu có yếu tố nguy cơ"
    elif egfr >= 60:
        stage = "G2 - Giảm nhẹ"
        description = "Giảm GFR nhẹ (có thể bình thường ở người cao tuổi)"
        color = "#28a745"
        icon = "✅"
        action = "Theo dõi, kiểm soát yếu tố nguy cơ"
    elif egfr >= 45:
        stage = "G3a - Giảm nhẹ-trung bình"
        description = "Suy thận mạn giai đoạn 3a"
        color = "#ffc107"
        icon = "⚠️"
        action = "Theo dõi 6-12 tháng, điều chỉnh liều thuốc"
    elif egfr >= 30:
        stage = "G3b - Giảm trung bình-nặng"
        description = "Suy thận mạn giai đoạn 3b"
        color = "#fd7e14"
        icon = "⚠️"
        action = "Theo dõi 3-6 tháng, hội chẩn chuyên khoa"
    elif egfr >= 15:
        stage = "G4 - Giảm nặng"
        description = "Suy thận mạn giai đoạn 4"
        color = "#dc3545"
        icon = "🚨"
        action = "Theo dõi 1-3 tháng, chuẩn bị lọc máu"
    else:
        stage = "G5 - Suy thận giai đoạn cuối"
        description = "Suy thận giai đoạn cuối (ESRD)"
        color = "#dc3545"
        icon = "🚨🚨"
        action = "Cần lọc máu hoặc ghép thận NGAY"
    
    return {
        "stage": stage,
        "description": description,
        "color": color,
        "icon": icon,
        "action": action
    }


def get_recommended_formula(bmi, age, nutrition_status):
    """
    Recommend best formula based on patient characteristics
    """
    if bmi >= 30:
        return "Cockcroft-Gault (với ABW)", "Bệnh nhân béo phì, nên dùng Cockcroft-Gault với cân nặng hiệu chỉnh (ABW)"
    elif bmi < 18.5:
        return "CKD-EPI Cystatin C", "Bệnh nhân gầy, nên dùng Cystatin C hoặc kết hợp Creatinin + Cystatin C"
    elif age >= 65:
        return "CKD-EPI 2021", "Người cao tuổi, CKD-EPI 2021 chính xác hơn"
    else:
        return "CKD-EPI 2009", "Bệnh nhân bình thường, CKD-EPI là khuyến cáo"


def render():
    """Render comprehensive eGFR/GFR calculator"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧪 eGFR/GFR Calculator</h2>
    <p style='text-align: center;'><em>Tính tốc độ lọc cầu thận với nhiều công thức</em></p>
    """, unsafe_allow_html=True)
    
    # Overview
    with st.expander("ℹ️ Tổng quan về eGFR/GFR"):
        st.markdown("""
        ### Mức lọc cầu thận (GFR) phản ánh khả năng lọc của thận
        
        **Khái niệm:**
        - **eGFR chuẩn hóa:** mL/min/1.73m² - Chuẩn hóa theo BSA, để so sánh giữa các cá thể
        - **GFR tuyệt đối:** mL/min - Giá trị thực tế theo diện tích cơ thể
        - **CrCl:** mL/min - Thanh thải creatinine, KHÔNG chuẩn hóa
        
        **Khi nào cần BSA:**
        - ❌ **Không cần:** Phân giai đoạn CKD (dùng eGFR chuẩn hóa)
        - ✅ **Cần:** Điều chỉnh liều thuốc (chuyển sang GFR tuyệt đối)
        - ✅ **Cần:** Bệnh nhân gầy/béo phì/cụt chi
        
        **Các công thức eGFR:**
        1. **CKD-EPI (2009)** ⭐ - Khuyến cáo cho hầu hết trường hợp
        2. **MDRD** - Công thức cũ, ít chính xác
        3. **Cockcroft-Gault** ⭐ - Ưu tiên cho điều chỉnh liều thuốc
        
        **Lựa chọn công thức:**
        - Người bình thường: **CKD-EPI**
        - Béo phì: **Cockcroft-Gault + ABW**
        - Gầy/Suy dinh dưỡng: **Cystatin C** (chưa có trong tool này)
        - Người già: **CKD-EPI**
        """)
    
    st.markdown("---")
    
    # Input form
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
    
    # Calculate button
    if st.button("🔬 Tính tất cả", type="primary", use_container_width=True):
        # Calculate BSA using selected formula
        bsa_formulas = {
            "mosteller": calculate_bsa_mosteller,
            "dubois": calculate_bsa_dubois,
            "haycock": calculate_bsa_haycock,
            "boyd": calculate_bsa_boyd,
            "shuter_aslani": calculate_bsa_shuter_aslani
        }
        bsa = bsa_formulas[bsa_formula](weight_kg, height_cm)
        
        # Also calculate with other formulas for comparison
        bsa_mosteller = calculate_bsa_mosteller(weight_kg, height_cm)
        bsa_dubois = calculate_bsa_dubois(weight_kg, height_cm)
        bsa_haycock = calculate_bsa_haycock(weight_kg, height_cm)
        bsa_boyd = calculate_bsa_boyd(weight_kg, height_cm)
        bsa_shuter = calculate_bsa_shuter_aslani(weight_kg, height_cm)
        
        # Calculate all GFR formulas
        egfr_ckd_epi = calculate_ckd_epi(creatinine_mg, age, gender, race)
        egfr_mdrd = calculate_mdrd(creatinine_mg, age, gender, race)
        crcl = calculate_cockcroft_gault(age, weight_kg, creatinine_mg, gender, use_abw, abw)
        
        # Calculate absolute GFRs (for drug dosing)
        gfr_absolute_ckd_epi = convert_egfr_to_absolute_gfr(egfr_ckd_epi, bsa)
        gfr_absolute_mdrd = convert_egfr_to_absolute_gfr(egfr_mdrd, bsa)
        
        # Interpret CKD stage
        interpretation = interpret_egfr(egfr_ckd_epi)
        
        # Get recommended formula
        recommended, reason = get_recommended_formula(bmi, age, "normal")
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Patient info summary
        st.markdown(f"""
        <div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
            <h4 style='margin-top: 0;'>📋 Thông tin bệnh nhân</h4>
            <p><strong>Tuổi:</strong> {age}, <strong>Giới:</strong> {"Nam" if gender == "male" else "Nữ"}, 
               <strong>BMI:</strong> {bmi:.1f} kg/m²</p>
            <p><strong>BSA:</strong> {bsa:.2f} m² (Mosteller)</p>
            <p><strong>Creatinine:</strong> {creatinine:.1f} {creatinine_unit.replace("/", "/")} ({creatinine_mg:.2f} mg/dL)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Main result - CKD-EPI
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {interpretation["color"]}22 0%, {interpretation["color"]}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {interpretation["color"]}; margin: 20px 0;'>
            <h2 style='color: {interpretation["color"]}; margin: 0; text-align: center;'>
                {interpretation["icon"]} eGFR (CKD-EPI): {egfr_ckd_epi:.1f} mL/min/1.73m²
            </h2>
            <p style='text-align: center; font-size: 1.2em; margin-top: 10px; font-weight: bold;'>
                {interpretation['stage']}
            </p>
            <p style='text-align: center; font-size: 1.1em; margin-top: 5px;'>
                {interpretation['description']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommendation
        if recommended.startswith("Cockcroft-Gault"):
            st.info(f"""
            💡 **Khuyến cáo:** {recommended}
            
            {reason}
            
            **CrCl hiện tại:** {crcl:.1f} mL/min (Cockcroft-Gault)
            - Dùng cho điều chỉnh liều thuốc
            """)
        else:
            st.info(f"""
            💡 **Khuyến cáo:** {recommended}
            
            {reason}
            """)
        
        # All formulas comparison
        st.markdown("---")
        st.markdown("### 📊 So sánh tất cả công thức")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**eGFR Chuẩn hóa (1.73m²)**")
            st.metric("CKD-EPI", f"{egfr_ckd_epi:.1f}", help="Khuyến cáo cho chẩn đoán CKD")
            st.metric("MDRD", f"{egfr_mdrd:.1f}", delta=f"{egfr_mdrd - egfr_ckd_epi:+.1f}", 
                     help="Công thức cũ")
            st.metric("CrCl (Cockcroft-Gault)", f"{crcl:.1f}", 
                     help="Ưu tiên cho điều chỉnh liều thuốc")
        
        with col2:
            st.markdown("**GFR Tuyệt đối (mL/min)**")
            st.metric("CKD-EPI → GFR", f"{gfr_absolute_ckd_epi:.1f}", 
                     help="Từ CKD-EPI chuyển đổi")
            st.metric("MDRD → GFR", f"{gfr_absolute_mdrd:.1f}", 
                     delta=f"{gfr_absolute_mdrd - gfr_absolute_ckd_epi:+.1f}",
                     help="Từ MDRD chuyển đổi")
            st.metric("CrCl = GFR", f"{crcl:.1f}", 
                     help="CrCl = GFR tuyệt đối (không chuẩn hóa)")
        
        with col3:
            st.markdown("**Thông tin khác**")
            bsa_name = {"mosteller": "Mosteller", "dubois": "Du Bois", "haycock": "Haycock", 
                       "boyd": "Boyd", "shuter_aslani": "Shuter & Aslani"}[bsa_formula]
            st.metric("BSA (đã chọn)", f"{bsa:.2f} m²", delta=f"{bsa_name}", 
                     help="Diện tích da cơ thể")
            st.metric("BSA vs Mosteller", f"{bsa_mosteller:.2f}", 
                     delta=f"{bsa - bsa_mosteller:+.3f}",
                     help="So sánh với Mosteller")
            st.metric("Chuyển đổi", f"{bsa / 1.73:.3f}", 
                     help="BSA_actual / 1.73")
        
        # Interpretation and action
        st.markdown("---")
        st.markdown(f"""
        <div style='background-color: {interpretation["color"]}22; padding: 20px; border-radius: 10px; border: 2px solid {interpretation["color"]};'>
            <h3 style='color: {interpretation["color"]}; margin-top: 0;'>
                {interpretation["icon"]} Hành động đề xuất
            </h3>
            <p style='font-size: 1.2em; color: {interpretation["color"]}; font-weight: bold; margin: 10px 0;'>
                {interpretation['action']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Clinical guidance
        st.markdown("---")
        st.markdown("### 💊 Hướng dẫn điều chỉnh liều thuốc")
        
        # Choose the appropriate GFR value for dosing
        if bmi >= 30 or use_abw:
            dosing_gfr = crcl  # Use Cockcroft-Gault for obesity
            dosing_source = f"Cockcroft-Gault (với ABW: {abw:.1f} kg)"
        else:
            dosing_gfr = gfr_absolute_ckd_epi  # Use absolute GFR from CKD-EPI
            dosing_source = "CKD-EPI (GFR tuyệt đối)"
        
        st.markdown(f"""
        **GFR dùng cho điều chỉnh liều: {dosing_gfr:.1f} mL/min**
        - *Nguồn: {dosing_source}*
        
        **Công thức chuyển đổi:**
        ```
        GFR_tuyệt_đối = eGFR_chuẩn × (BSA_thực / 1.73)
        GFR_tuyệt_đối = {egfr_ckd_epi:.1f} × ({bsa:.2f} / 1.73)
        GFR_tuyệt_đối = {egfr_ckd_epi:.1f} × {bsa / 1.73:.3f}
        GFR_tuyệt_đối = {gfr_absolute_ckd_epi:.1f} mL/min
        ```
        """)
        
        # Dosing recommendations
        if dosing_gfr >= 60:
            st.success("""
            ✅ **GFR ≥ 60 mL/min - Chức năng thận gần bình thường**
            
            **Hầu hết các thuốc:** Dùng liều bình thường, không cần điều chỉnh.
            """)
        elif dosing_gfr >= 30:
            st.warning(f"""
            ⚠️ **GFR 30-59 mL/min - Suy thận mạn**
            
            **GFR hiện tại: {dosing_gfr:.0f} mL/min**
            
            **Cần điều chỉnh liều nhiều thuốc:**
            - Beta-lactams, Fluoroquinolones, Aminoglycosides
            - Vancomycin (monitor nồng độ)
            - Digoxin, LMWH, NOACs
            - Metformin (tránh nếu < 45)
            - SGLT2i (tránh nếu < 45)
            
            ⚠️ **Tra cứu hướng dẫn cụ thể cho từng thuốc!**
            """)
        else:
            st.error(f"""
            🚨 **GFR < 30 mL/min - Suy thận nặng**
            
            **GFR hiện tại: {dosing_gfr:.0f} mL/min**
            
            **⚠️ NGUY HIỂM - Hội chẩn dược sĩ/thận ngay!**
            
            **Nhiều thuốc CHỐNG CHỈ ĐỊNH hoặc giảm liều mạnh:**
            - ❌ Metformin (chống chỉ định)
            - ❌ SGLT2i (chống chỉ định)
            - ❌ NSAIDs (tránh hoặc chống chỉ định)
            - ✅ Hầu hết thuốc cần điều chỉnh liều đáng kể
            
            **Khuyến cáo:** 📞 Hội chẩn dược lâm sàng cho MỌI đơn thuốc!
            """)
        
        # Detailed calculation breakdown
        with st.expander("📋 Chi tiết tính toán"):
            st.markdown("""
            ### 1. BSA (Body Surface Area) - Mosteller
            
            Công thức được KDIGO, FDA, NCCN khuyến cáo:
            ```python
            BSA = √[(Cân nặng × Chiều cao) / 3600]
            BSA = √[(""" + f"{weight_kg:.0f} × {height_cm}" + """) / 3600]
            BSA = √[""" + f"{weight_kg * height_cm:.0f} / 3600" + """]
            BSA = """ + f"{bsa:.2f} m²" + """
            ```
            
            ### 2. CKD-EPI 2009
            
            Công thức khuyến cáo cho chẩn đoán CKD:
            ```python
            egfr_ckd_epi = 141 × (Scr/κ)ᵅ × (Scr/κ)^-1.209 × 0.993^age × G × R
            egfr = """ + f"{egfr_ckd_epi:.1f} mL/min/1.73m²" + """
            ```
            
            ### 3. MDRD
            
            Công thức cũ, ít chính xác hơn:
            ```python
            egfr_mdrd = 175 × Scr^-1.154 × age^-0.203 × G × R
            egfr = """ + f"{egfr_mdrd:.1f} mL/min/1.73m²" + """
            ```
            
            ### 4. Cockcroft-Gault
            
            Ưu tiên cho điều chỉnh liều thuốc:
            ```python
            CrCl = [(140 - age) × weight] / (72 × SCr) × G
            """ + f"{'ABW = ' + f'{abw:.1f}' + ' kg (nếu dùng ABW)' if use_abw else ''}" + """
            CrCl = """ + f"{crcl:.1f} mL/min" + """
            ```
            
            ### 5. Chuyển đổi GFR
            
            Từ eGFR chuẩn hóa sang GFR tuyệt đối:
            ```python
            GFR_absolute = eGFR × (BSA / 1.73)
            GFR_absolute = """ + f"{egfr_ckd_epi:.1f} × ({bsa:.2f} / 1.73)" + """
            GFR_absolute = """ + f"{gfr_absolute_ckd_epi:.1f} mL/min" + """
            ```
            """)
        
        # When to use which formula
        with st.expander("🎯 Khi nào dùng công thức nào?"):
            st.markdown("""
            | Mục đích | Dùng gì? | Giải thích |
            |:---------|:---------|:-----------|
            | **Chẩn đoán CKD** | eGFR CKD-EPI (chuẩn hóa) | Phân giai đoạn theo KDIGO |
            | **Điều chỉnh liều thuốc** | CrCl hoặc GFR tuyệt đối | FDA, Micromedex khuyến cáo CrCl |
            | **Béo phì (BMI > 30)** | Cockcroft-Gault + ABW | Cân nặng hiệu chỉnh chính xác hơn |
            | **Người gầy** | CKD-EPI Cystatin C | Ít bị ảnh hưởng bởi khối cơ |
            | **Suy dinh dưỡng** | Cystatin C hoặc đo trực tiếp | Creatinine thấp giả tạo |
            | **Người già** | CKD-EPI 2021 | Chính xác hơn ở người cao tuổi |
            | **ICU/AKI** | Jelliffe hoặc đo CrCl 24h | Cr biến động, không dùng eGFR |
            
            **Lưu ý quan trọng:**
            - ✅ **Chẩn đoán CKD:** Dùng eGFR chuẩn hóa (1.73m²)
            - ✅ **Điều chỉnh liều:** Dùng GFR tuyệt đối (mL/min)
            - ✅ **Béo/Gầy:** Cần hiệu chỉnh BSA hoặc dùng Cystatin C
            - ❌ **Bệnh nhân lọc máu:** Không tính eGFR
            - ❌ **Bệnh nhân PD:** Đo clearance 24h
            """)
        
        # Example
        with st.expander("📖 Ví dụ minh họa"):
            st.markdown(f"""
            **Bệnh nhân:** Nam, {age} tuổi, {height_cm} cm, {weight_kg} kg
            **Creatinine:** {creatinine:.1f} {creatinine_unit.replace("/", "/")} ({creatinine_mg:.2f} mg/dL)
            
            **Bước 1: Tính BSA**
            ```
            BSA = √[({weight_kg:.0f} × {height_cm}) / 3600] = {bsa:.2f} m²
            ```
            
            **Bước 2: Tính eGFR chuẩn hóa**
            ```
            eGFR (CKD-EPI) = {egfr_ckd_epi:.1f} mL/min/1.73m²
            → Giai đoạn: {interpretation['stage']}
            ```
            
            **Bước 3: Chuyển sang GFR tuyệt đối (cho điều chỉnh liều)**
            ```
            GFR_tuyệt_đối = {egfr_ckd_epi:.1f} × ({bsa:.2f} / 1.73)
            GFR_tuyệt_đối = {gfr_absolute_ckd_epi:.1f} mL/min
            ```
            
            **Bước 4: Dùng liều thuốc theo {dosing_gfr:.0f} mL/min**
            """)
        
        # CKD stages table
        with st.expander("📊 Bảng phân loại CKD (KDIGO)"):
            st.markdown("""
            | Giai đoạn | eGFR | Mô tả | Quản lý | Tần suất theo dõi |
            |:----------|:-----|:------|:---------|:------------------|
            | **G1** | ≥ 90 | Bình thường/Cao | Theo dõi nếu có tổn thương | Hàng năm |
            | **G2** | 60-89 | Giảm nhẹ | Kiểm soát nguy cơ | 6-12 tháng |
            | **G3a** | 45-59 | Giảm nhẹ-TB | Điều chỉnh thuốc | 6-12 tháng |
            | **G3b** | 30-44 | Giảm TB-nặng | Hội chẩn thận | 3-6 tháng |
            | **G4** | 15-29 | Giảm nặng | Chuẩn bị lọc máu | 1-3 tháng |
            | **G5** | < 15 | ESRD | Lọc máu/Ghép thận | Thường xuyên |
            
            **Phân loại đầy đủ cần cả giai đoạn G (eGFR) và A (albumin niệu).**
            """)
        
        # BSA formulas comparison
        with st.expander("📏 So sánh các công thức BSA"):
            st.markdown(f"""
            ### Tất cả công thức BSA cho bệnh nhân này:
            
            | Công thức | Năm | BSA (m²) | Chênh lệch vs Mosteller | Đặc điểm |
            |:----------|:----|:---------|:------------------------|:---------|
            | **Mosteller** | 1987 | **{bsa_mosteller:.2f}** | - | ⭐ Đơn giản, KDIGO/FDA khuyến nghị |
            | Du Bois | 1916 | {bsa_dubois:.2f} | {bsa_dubois - bsa_mosteller:+.3f} | Cổ điển, nền tảng 1.73m² |
            | Haycock | 1978 | {bsa_haycock:.2f} | {bsa_haycock - bsa_mosteller:+.3f} | Tốt cho mọi lứa tuổi |
            | Boyd | 1935 | {bsa_boyd:.2f} | {bsa_boyd - bsa_mosteller:+.3f} | Phức tạp, tốt cho BMI cực |
            | Shuter & Aslani | 2000 | {bsa_shuter:.2f} | {bsa_shuter - bsa_mosteller:+.3f} | Hiện đại, chính xác cao |
            
            **Chênh lệch lớn nhất:** {max(abs(bsa_dubois - bsa_mosteller), abs(bsa_haycock - bsa_mosteller), 
                                          abs(bsa_boyd - bsa_mosteller), abs(bsa_shuter - bsa_mosteller)):.3f} m²
            
            ### Khuyến nghị:
            
            **Nên dùng Mosteller** khi:
            - ✅ BMI 18-30 (bệnh nhân bình thường)
            - ✅ Tính eGFR hiệu chỉnh liều thuốc
            - ✅ Cần công thức đơn giản, nhanh
            
            **Nên dùng công thức khác** khi:
            - BMI < 18 hoặc > 35: Dùng **Boyd** hoặc **Shuter & Aslani**
            - Trẻ em/người già: Dùng **Haycock**
            - Chuẩn hóa eGFR: Dùng **Du Bois** (chuẩn 1.73m²)
            
            **Lưu ý:** Chênh lệch 5-10% BSA → sai liều thuốc đáng kể!
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Mosteller RD.** Simplified calculation of body-surface area. N Engl J Med. 1987;317(17):1098.
            
            2. **Levey AS, Stevens LA, Schmid CH, et al.** A new equation to estimate glomerular filtration rate. 
               Ann Intern Med. 2009;150(9):604-12. *(CKD-EPI)*
            
            3. **Levey AS, Bosch JP, Lewis JB, et al.** A more accurate method to estimate glomerular filtration rate from serum creatinine: 
               a new prediction equation. Ann Intern Med. 1999;130(6):461-70. *(MDRD)*
            
            4. **Cockcroft DW, Gault MH.** Prediction of creatinine clearance from serum creatinine. Nephron. 1976;16(1):31-41.
            
            5. **KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease.** 
               Kidney Int Suppl. 2013;3(1):1-150.
            
            6. **Stevens LA, Nolin TD, Richardson MM, et al.** Comparison of drug dosing recommendations based on measured GFR 
               and kidney function estimating equations. Am J Kidney Dis. 2009;54(1):33-42.
            """)
    
    # Quick guide
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    **1. Chẩn đoán CKD:** Dùng eGFR chuẩn hóa (CKD-EPI)
    
    **2. Điều chỉnh liều thuốc:** Dùng GFR tuyệt đối hoặc CrCl
    
    **3. Béo phì:** Ưu tiên Cockcroft-Gault với ABW
    
    **4. Chuyển đổi:** GFR_absolute = eGFR × (BSA / 1.73)
    
    **5. Luôn tra cứu** liều chính xác cho từng thuốc
    
    **6. Hội chẩn** dược sĩ/thận nếu eGFR < 30 hoặc < 45 + có triệu chứng
    """)


if __name__ == "__main__":
    render()
