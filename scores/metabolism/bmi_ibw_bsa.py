"""
BMI, IBW, BSA Calculator
Body Mass Index, Ideal Body Weight, Body Surface Area
"""

import streamlit as st
import math


def calculate_bmi(weight, height_cm):
    """Calculate BMI"""
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi


def calculate_ibw(height_cm, gender):
    """Calculate Ideal Body Weight (Devine formula)"""
    if gender == "male":
        ibw = 50 + 0.91 * (height_cm - 152.4)
    else:  # female
        ibw = 45.5 + 0.91 * (height_cm - 152.4)
    
    return max(ibw, 0)  # Ensure non-negative


def calculate_abw(actual_weight, ibw):
    """Calculate Adjusted Body Weight"""
    abw = ibw + 0.4 * (actual_weight - ibw)
    return abw


def calculate_bsa_mosteller(weight, height_cm):
    """Calculate BSA using Mosteller formula (most commonly used)"""
    bsa = math.sqrt((weight * height_cm) / 3600)
    return bsa


def calculate_bsa_dubois(weight, height_cm):
    """Calculate BSA using DuBois formula"""
    bsa = 0.007184 * (weight ** 0.425) * (height_cm ** 0.725)
    return bsa


def render():
    """Render BMI/IBW/BSA calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>📏 BMI | IBW | BSA Calculator</h2>
    <p style='text-align: center;'><em>Chỉ số cơ thể - Body Mass Index, Ideal Weight, Body Surface Area</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **3 chỉ số quan trọng về cơ thể:**
        
        ### 1️⃣ BMI (Body Mass Index) - Chỉ số khối cơ thể
        - **Công thức:** Cân nặng (kg) / Chiều cao² (m²)
        - **Mục đích:** Phân loại béo phì, gầy, bình thường
        - **Sử dụng:** Sàng lọc, tư vấn sức khỏe
        
        ### 2️⃣ IBW (Ideal Body Weight) - Cân nặng lý tưởng
        - **Công thức Devine:** 
          - Nam: 50 + 0.91 × (chiều cao cm - 152.4)
          - Nữ: 45.5 + 0.91 × (chiều cao cm - 152.4)
        - **Mục đích:** Tính liều thuốc, dinh dưỡng
        - **Sử dụng:** Điều chỉnh liều (vd: aminoglycosides)
        
        ### 3️⃣ BSA (Body Surface Area) - Diện tích cơ thể
        - **Công thức Mosteller:** √[(cân nặng × chiều cao) / 3600]
        - **Mục đích:** Tính liều hóa trị, chỉ số tim thận
        - **Sử dụng:** Liều hóa chất, cardiac index, eGFR
        
        **ABW (Adjusted Body Weight):** Dùng cho béo phì
        - ABW = IBW + 0.4 × (Actual - IBW)
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Nhập thông tin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        height_cm = st.number_input(
            "Chiều cao (cm)",
            min_value=100,
            max_value=250,
            value=170,
            step=1,
            help="Chiều cao của bệnh nhân"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.5,
            help="Cân nặng hiện tại"
        )
    
    with col2:
        gender = st.radio(
            "Giới tính",
            options=["male", "female"],
            format_func=lambda x: "Nam" if x == "male" else "Nữ",
            horizontal=True,
            help="Cần cho tính IBW"
        )
        
        age = st.number_input(
            "Tuổi (tùy chọn)",
            min_value=0,
            max_value=120,
            value=40,
            step=1,
            help="Để tham khảo thêm"
        )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("📊 Tính toán", type="primary", use_container_width=True):
        # Calculate all metrics
        bmi = calculate_bmi(weight, height_cm)
        ibw = calculate_ibw(height_cm, gender)
        abw = calculate_abw(weight, ibw)
        bsa_mosteller = calculate_bsa_mosteller(weight, height_cm)
        bsa_dubois = calculate_bsa_dubois(weight, height_cm)
        
        # Classify BMI
        if bmi < 16:
            bmi_category = "Gầy độ III (Severe thinness)"
            bmi_color = "#dc3545"
            bmi_icon = "🚨"
        elif bmi < 17:
            bmi_category = "Gầy độ II (Moderate thinness)"
            bmi_color = "#fd7e14"
            bmi_icon = "⚠️"
        elif bmi < 18.5:
            bmi_category = "Gầy độ I (Mild thinness)"
            bmi_color = "#ffc107"
            bmi_icon = "⚠️"
        elif bmi < 25:
            bmi_category = "Bình thường (Normal)"
            bmi_color = "#28a745"
            bmi_icon = "✅"
        elif bmi < 30:
            bmi_category = "Thừa cân (Overweight)"
            bmi_color = "#ffc107"
            bmi_icon = "⚠️"
        elif bmi < 35:
            bmi_category = "Béo phì độ I (Obese class I)"
            bmi_color = "#fd7e14"
            bmi_icon = "⚠️"
        elif bmi < 40:
            bmi_category = "Béo phì độ II (Obese class II)"
            bmi_color = "#dc3545"
            bmi_icon = "🚨"
        else:
            bmi_category = "Béo phì độ III (Obese class III)"
            bmi_color = "#dc3545"
            bmi_icon = "🚨"
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # BMI Result
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {bmi_color}22 0%, {bmi_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {bmi_color}; margin: 20px 0;'>
            <h2 style='color: {bmi_color}; margin: 0; text-align: center;'>
                {bmi_icon} BMI = {bmi:.1f} kg/m²
            </h2>
            <p style='text-align: center; font-size: 1.2em; margin-top: 10px;'>
                {bmi_category}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # All metrics
        st.markdown("### 📏 Tất cả chỉ số:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "BMI",
                f"{bmi:.1f} kg/m²",
                help="Body Mass Index"
            )
        
        with col2:
            st.metric(
                "IBW",
                f"{ibw:.1f} kg",
                delta=f"{weight - ibw:+.1f} kg so với actual",
                help="Ideal Body Weight (Devine)"
            )
        
        with col3:
            st.metric(
                "BSA",
                f"{bsa_mosteller:.2f} m²",
                help="Body Surface Area (Mosteller)"
            )
        
        # ABW if obese
        if weight > ibw * 1.2:  # >20% over IBW
            st.markdown("---")
            st.info(f"""
            **Adjusted Body Weight (ABW):** {abw:.1f} kg
            
            - Cân nặng thực tế **{weight:.1f} kg** cao hơn IBW **{ibw:.1f} kg**
            - ABW = {ibw:.1f} + 0.4 × ({weight:.1f} - {ibw:.1f}) = **{abw:.1f} kg**
            - Dùng ABW cho: CrCl (béo phì), một số thuốc
            """)
        
        # Detailed breakdown
        st.markdown("---")
        st.markdown("### 📋 Chi tiết tính toán:")
        
        height_m = height_cm / 100
        
        st.markdown(f"""
        **1. BMI (Body Mass Index):**
        ```
        BMI = Cân nặng / Chiều cao²
        BMI = {weight} / ({height_m:.2f})²
        BMI = {weight} / {height_m**2:.2f}
        BMI = {bmi:.1f} kg/m²
        ```
        
        **2. IBW (Ideal Body Weight - Devine):**
        ```
        {"Nam: IBW = 50 + 0.91 × (chiều cao - 152.4)" if gender == "male" else "Nữ: IBW = 45.5 + 0.91 × (chiều cao - 152.4)"}
        IBW = {"50" if gender == "male" else "45.5"} + 0.91 × ({height_cm} - 152.4)
        IBW = {"50" if gender == "male" else "45.5"} + 0.91 × {height_cm - 152.4:.1f}
        IBW = {"50" if gender == "male" else "45.5"} + {0.91 * (height_cm - 152.4):.1f}
        IBW = {ibw:.1f} kg
        ```
        
        **3. BSA (Body Surface Area - Mosteller):**
        ```
        BSA = √[(Cân nặng × Chiều cao) / 3600]
        BSA = √[({weight} × {height_cm}) / 3600]
        BSA = √[{weight * height_cm} / 3600]
        BSA = √{(weight * height_cm) / 3600:.2f}
        BSA = {bsa_mosteller:.2f} m²
        ```
        
        **BSA (DuBois - tham khảo):** {bsa_dubois:.2f} m²
        """)
        
        # BMI interpretation
        with st.expander("📊 Bảng phân loại BMI (WHO)"):
            st.markdown("""
            | BMI (kg/m²) | Phân loại | Nguy cơ sức khỏe |
            |:------------|:----------|:-----------------|
            | < 16.0 | Gầy độ III | Cao - suy dinh dưỡng nặng |
            | 16.0 - 16.9 | Gầy độ II | Trung bình-cao |
            | 17.0 - 18.4 | Gầy độ I | Thấp-trung bình |
            | **18.5 - 24.9** | **Bình thường** | **Thấp** ✅ |
            | 25.0 - 29.9 | Thừa cân | Tăng nhẹ |
            | 30.0 - 34.9 | Béo phì độ I | Trung bình |
            | 35.0 - 39.9 | Béo phì độ II | Cao |
            | ≥ 40.0 | Béo phì độ III | Rất cao |
            
            **Lưu ý cho người châu Á:**
            - Nguy cơ bệnh chuyển hóa tăng ở BMI thấp hơn
            - WHO châu Á:
              - Thừa cân: BMI ≥ 23
              - Béo phì: BMI ≥ 25
              - Béo phì nặng: BMI ≥ 30
            """)
        
        # Clinical applications
        with st.expander("💊 Ứng dụng lâm sàng"):
            st.markdown(f"""
            ### Với bệnh nhân này:
            
            **Thông tin:**
            - Chiều cao: {height_cm} cm
            - Cân nặng: {weight} kg
            - BMI: {bmi:.1f}
            - IBW: {ibw:.1f} kg
            - BSA: {bsa_mosteller:.2f} m²
            {"- ABW: " + f"{abw:.1f}" + " kg (cho béo phì)" if weight > ibw * 1.2 else ""}
            
            ---
            
            ### 1. Điều chỉnh liều thuốc:
            
            **Dựa trên cân nặng THỰC TẾ ({weight} kg):**
            - Heparin, LMWH
            - Propofol, Succinylcholine
            - Hầu hết thuốc gây mê
            
            **Dựa trên IBW ({ibw:.1f} kg):**
            - Aminoglycosides (Gentamicin, Amikacin)
            - Theophylline
            - Digoxin
            
            {"**Dựa trên ABW (" + f"{abw:.1f}" + " kg) - cho béo phì:**" if weight > ibw * 1.2 else ""}
            {f"- Vancomycin, Daptomycin" if weight > ibw * 1.2 else ""}
            {f"- Một số thuốc lipophilic" if weight > ibw * 1.2 else ""}
            
            **Dựa trên BSA ({bsa_mosteller:.2f} m²):**
            - Hóa trị (Doxorubicin, Cisplatin...)
            - eGFR (chuẩn hóa theo 1.73 m²)
            - Cardiac Index
            
            ---
            
            ### 2. Đánh giá dinh dưỡng:
            
            **BMI {bmi:.1f}:** {bmi_category}
            
            {"**⚠️ Gầy - Cần đánh giá dinh dưỡng:**" if bmi < 18.5 else ""}
            {f"- Nguy cơ suy dinh dưỡng" if bmi < 18.5 else ""}
            {f"- Tăng cường dinh dưỡng" if bmi < 18.5 else ""}
            {f"- Đánh giá albumin, prealbumin" if bmi < 18.5 else ""}
            
            {"**✅ Bình thường - Duy trì:**" if 18.5 <= bmi < 25 else ""}
            {f"- Chế độ ăn cân bằng" if 18.5 <= bmi < 25 else ""}
            {f"- Vận động đều đặn" if 18.5 <= bmi < 25 else ""}
            
            {"**⚠️ Thừa cân/Béo phì - Cần can thiệp:**" if bmi >= 25 else ""}
            {f"- Tư vấn giảm cân" if bmi >= 25 else ""}
            {f"- Chế độ ăn giảm calories" if bmi >= 25 else ""}
            {f"- Tăng hoạt động thể chất" if bmi >= 25 else ""}
            {f"- Sàng lọc: ĐTĐ, THA, dyslipidemia" if bmi >= 25 else ""}
            {f"- Cân nhắc thuốc giảm cân nếu BMI ≥ 30" if bmi >= 30 else ""}
            {f"- Cân nhắc phẫu thuật nếu BMI ≥ 40" if bmi >= 40 else ""}
            
            ---
            
            ### 3. Nguy cơ phẫu thuật:
            
            {f"**BMI {bmi:.1f} - Nguy cơ cao:**" if bmi >= 35 else ""}
            {f"- Khó đặt nội khí quản" if bmi >= 35 else ""}
            {f"- Nguy cơ hô hấp sau mổ" if bmi >= 35 else ""}
            {f"- Nhiễm trùng vết mổ" if bmi >= 35 else ""}
            {f"- VTE (huyết khối)" if bmi >= 30 else ""}
            {f"- Cần dự phòng VTE" if bmi >= 30 else ""}
            """)
        
        # Weight management
        if bmi < 18.5 or bmi >= 25:
            with st.expander("🎯 Mục tiêu cân nặng"):
                target_bmi_low = 18.5
                target_bmi_high = 24.9
                
                height_m = height_cm / 100
                target_weight_low = target_bmi_low * (height_m ** 2)
                target_weight_high = target_bmi_high * (height_m ** 2)
                
                st.markdown(f"""
                ### Mục tiêu cân nặng lý tưởng:
                
                **Để đạt BMI 18.5-24.9 (bình thường):**
                
                - **Cân nặng mục tiêu:** {target_weight_low:.1f} - {target_weight_high:.1f} kg
                - **Cân nặng hiện tại:** {weight:.1f} kg
                - **Cần {"tăng" if weight < target_weight_low else "giảm"}:** {abs(weight - (target_weight_low if weight < target_weight_low else target_weight_high)):.1f} kg
                
                ---
                
                {"### Kế hoạch TĂNG CÂN an toàn:" if weight < target_weight_low else "### Kế hoạch GIẢM CÂN an toàn:"}
                
                {'''
                **Mục tiêu:** Tăng 0.5-1 kg/tuần
                
                **Dinh dưỡng:**
                - Tăng 500-1000 kcal/ngày
                - Protein: 1.5-2 g/kg/ngày
                - 5-6 bữa nhỏ/ngày
                - Bổ sung vitamin, khoáng chất
                
                **Vận động:**
                - Tập kháng lực (tạ)
                - Tăng cơ, không chỉ mỡ
                
                **Theo dõi:**
                - Cân hàng tuần
                - Đánh giá albumin, prealbumin
                ''' if weight < target_weight_low else '''
                **Mục tiêu:** Giảm 0.5-1 kg/tuần (5-10% trong 6 tháng)
                
                **Dinh dưỡng:**
                - Giảm 500-1000 kcal/ngày
                - Protein: 1.2-1.5 g/kg IBW/ngày
                - Tăng rau, trái cây, chất xơ
                - Giảm đường, chất béo bão hòa
                
                **Vận động:**
                - Aerobic: 150-300 phút/tuần
                - Tập kháng lực 2-3 lần/tuần
                - Tăng hoạt động hàng ngày
                
                **Theo dõi:**
                - Cân hàng tuần
                - Đường huyết, lipid, huyết áp
                '''}
                """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **World Health Organization.** Obesity: preventing and managing the global epidemic. Report of a WHO consultation. 
               *World Health Organ Tech Rep Ser.* 2000;894:i-xii, 1-253.
            
            2. **Devine BJ.** Gentamicin therapy. *Drug Intell Clin Pharm.* 1974;8:650-655.
            
            3. **Mosteller RD.** Simplified calculation of body-surface area. 
               *N Engl J Med.* 1987;317(17):1098.
            
            4. **DuBois D, DuBois EF.** A formula to estimate the approximate surface area if height and weight be known. 
               *Arch Intern Med.* 1916;17:863-871.
            
            5. **WHO Expert Consultation.** Appropriate body-mass index for Asian populations and its implications for policy and intervention strategies. 
               *Lancet.* 2004;363(9403):157-63.
            """)
    
    # Quick reference
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    **BMI (Body Mass Index):**
    - Bình thường: 18.5-24.9 kg/m² (Châu Á: 18.5-22.9)
    - Sàng lọc béo phì, suy dinh dưỡng
    
    **IBW (Ideal Body Weight):**
    - Nam: 50 + 0.91 × (cm - 152.4)
    - Nữ: 45.5 + 0.91 × (cm - 152.4)
    - Dùng cho: Aminoglycosides, Theophylline, Digoxin
    
    **BSA (Body Surface Area):**
    - Mosteller: √[(kg × cm) / 3600]
    - Dùng cho: Liều hóa trị, eGFR, Cardiac Index
    
    **ABW (Adjusted Body Weight):**
    - ABW = IBW + 0.4 × (Actual - IBW)
    - Dùng cho béo phì: Vancomycin, CrCl...
    """)


if __name__ == "__main__":
    render()

