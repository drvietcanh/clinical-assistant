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
            format="%d",
            help="Chiều cao của bệnh nhân"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.1,
            format="%.1f",
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
                delta=f"{weight - ibw:+.0f} kg so với actual",
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
            
            - Cân nặng thực tế **{weight:.0f} kg** cao hơn IBW **{ibw:.1f} kg**
            - ABW = {ibw:.1f} + 0.4 × ({weight:.0f} - {ibw:.1f}) = **{abw:.1f} kg**
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
        BMI = {weight:.0f} / ({height_m:.2f})²
        BMI = {weight:.0f} / {height_m**2:.2f}
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
        BSA = √[({weight:.0f} × {height_cm}) / 3600]
        BSA = √[{weight * height_cm:.0f} / 3600]
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
            - Cân nặng: {weight:.0f} kg
            - BMI: {bmi:.1f}
            - IBW: {ibw:.1f} kg
            - BSA: {bsa_mosteller:.2f} m²
            {"- ABW: " + f"{abw:.1f}" + " kg (cho béo phì)" if weight > ibw * 1.2 else ""}
            
            ---
            
            ### 1. Điều chỉnh liều thuốc:
            
            **Dựa trên cân nặng THỰC TẾ ({weight:.0f} kg):**
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
                
                - **Cân nặng mục tiêu:** {target_weight_low:.0f} - {target_weight_high:.0f} kg
                - **Cân nặng hiện tại:** {weight:.0f} kg
                - **Cần {"tăng" if weight < target_weight_low else "giảm"}:** {abs(weight - (target_weight_low if weight < target_weight_low else target_weight_high)):.0f} kg
                
                ---
                
                {"### Kế hoạch TĂNG CÂN an toàn:" if weight < target_weight_low else "### Kế hoạch GIẢM CÂN an toàn:"}
                
                {'''
                **Mục Tiêu:** Tăng 0.5-1 kg/tuần
                
                **Dinh dưỡng:**
                - Tăng 500-1000 kcal/ngày
                - Protein: 1.5-2 g/kg/ngày
                - 5-6 bữa nhỏ/ngày
                - Bổ sung vitamin, khoáng chất
                
                **Vận động:**
                - Tập kháng lực (tạ)
                - Tăng cơ, không chỉ mỡ
                
                **Theo Dõi:**
                - Cân hàng tuần
                - Đánh giá albumin, prealbumin
                ''' if weight < target_weight_low else '''
                **Mục Tiêu:** Giảm 0.5-1 kg/tuần (5-10% trong 6 tháng)
                
                **Dinh dưỡng:**
                - Giảm 500-1000 kcal/ngày
                - Protein: 1.2-1.5 g/kg IBW/ngày
                - Tăng rau, trái cây, chất xơ
                - Giảm đường, chất béo bão hòa
                
                **Vận động:**
                - Aerobic: 150-300 phút/tuần
                - Tập kháng lực 2-3 lần/tuần
                - Tăng hoạt động hàng ngày
                
                **Theo Dõi:**
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
    
    # Quick reference with detailed explanations
    st.markdown("---")
    with st.expander("📖 Giải thích Chuyên Sâu Các Thuật Ngữ", expanded=False):
        st.markdown("""
        ### 📏 BMI (Body Mass Index - Chỉ Số Khối Cơ Thể)
        
        **Định nghĩa:** BMI là chỉ số đo lường mối quan hệ giữa cân nặng và chiều cao, được sử dụng để đánh giá tình trạng dinh dưỡng và phân loại mức độ béo phì/gầy.
        
        **Công thức:** BMI = Cân nặng (kg) / [Chiều cao (m)]²
        
        **Phân loại (WHO - Người Châu Âu/Châu Mỹ):**
        - < 18.5 kg/m²: **Gầy** (Underweight)
        - 18.5-24.9 kg/m²: **Bình thường** (Normal)
        - 25.0-29.9 kg/m²: **Thừa cân** (Overweight)
        - 30.0-34.9 kg/m²: **Béo phì độ I** (Obesity Class I)
        - 35.0-39.9 kg/m²: **Béo phì độ II** (Obesity Class II)
        - ≥ 40.0 kg/m²: **Béo phì độ III (béo phì bệnh lý)** (Obesity Class III/Morbid)
        
        **Phân loại (Khuyến cáo Châu Á):**
        - < 18.5 kg/m²: **Gầy**
        - 18.5-22.9 kg/m²: **Bình thường**
        - 23.0-24.9 kg/m²: **Thừa cân**
        - 25.0-29.9 kg/m²: **Béo phì độ I**
        - ≥ 30.0 kg/m²: **Béo phì độ II**
        
        **Tại sao có sự khác biệt?**
        - Người Châu Á có tỷ lệ mỡ cơ thể cao hơn ở cùng mức BMI
        - Nguy cơ đái tháo đường và bệnh tim mạch tăng ở mức BMI thấp hơn
        - WHO khuyến cáo giảm ngưỡng BMI cho người Châu Á
        
        **Ứng dụng lâm sàng:**
        - ✅ Sàng lọc béo phì và suy dinh dưỡng trong cộng đồng
        - ✅ Đánh giá nguy cơ bệnh tim mạch, đái tháo đường
        - ✅ Theo dõi hiệu quả điều trị giảm cân/tăng cân
        - ⚠️ **Hạn chế:** BMI không phân biệt mỡ và cơ → Vận động viên có BMI cao nhưng không béo phì
        
        ---
        
        ### 🎯 IBW (Ideal Body Weight - Cân Nặng Lý Tưởng)
        
        **Định nghĩa:** IBW là cân nặng lý tưởng dựa trên giới tính và chiều cao, được tính toán để đạt được tỷ lệ mỡ cơ thể tối ưu và giảm nguy cơ bệnh tật.
        
        **Công thức Devine (1974):**
        - **Nam:** IBW = 50 kg + 0.91 × (chiều cao cm - 152.4 cm)
        - **Nữ:** IBW = 45.5 kg + 0.91 × (chiều cao cm - 152.4 cm)
        
        **Lịch sử:** Công thức này được phát triển ban đầu để tính liều gentamicin, sau đó được áp dụng rộng rãi cho nhiều loại thuốc.
        
        **Cơ sở khoa học:**
        - Dựa trên dữ liệu từ quần thể người Mỹ trung bình
        - Giả định tỷ lệ mỡ cơ thể 15-20% (nam) và 20-25% (nữ)
        - Phù hợp với chiều cao 152-183 cm
        
        **Ứng dụng lâm sàng:**
        - ✅ **Tính liều thuốc:** Aminoglycosides (gentamicin, tobramycin, amikacin), Theophylline, Digoxin
        - ✅ **Dinh dưỡng:** Tính nhu cầu calo, protein cho bệnh nhân
        - ✅ **Phẫu thuật:** Ước tính rủi ro gây mê
        - ⚠️ **Hạn chế:** Không chính xác cho bệnh nhân béo phì nặng hoặc gầy mức độ cao
        
        **Ví dụ:**
        - Nam, cao 170 cm: IBW = 50 + 0.91 × (170 - 152.4) = **66.1 kg**
        - Nữ, cao 160 cm: IBW = 45.5 + 0.91 × (160 - 152.4) = **52.4 kg**
        
        ---
        
        ### 📐 BSA (Body Surface Area - Diện Tích Bề Mặt Cơ Thể)
        
        **Định nghĩa:** BSA là diện tích bề mặt ngoài của cơ thể, được tính bằng mét vuông (m²). Chỉ số này quan trọng vì nhiều quá trình sinh lý (như trao đổi chất, thải thuốc) tỷ lệ với BSA chứ không phải cân nặng.
        
        **Công thức Mosteller (1987) - ⭐ Khuyến nghị:**
        ```
        BSA = √[(Cân nặng kg × Chiều cao cm) / 3600]
        ```
        
        **Công thức Du Bois (1916) - Công thức cổ điển:**
        ```
        BSA = 0.007184 × (Cân nặng kg)^0.425 × (Chiều cao cm)^0.725
        ```
        
        **Tại sao BSA quan trọng?**
        - **Trao đổi chất:** Tỷ lệ với BSA, không phải cân nặng
        - **Lưu lượng tim:** Cardiac Index = Cardiac Output / BSA
        - **Chức năng thận:** GFR thường được chuẩn hóa theo BSA 1.73 m²
        - **Liều hóa trị:** Nhiều thuốc được tính theo BSA (mg/m²)
        
        **Chuẩn hóa BSA 1.73 m²:**
        - Đây là BSA trung bình của một người trưởng thành (nam, 70 kg, 170 cm)
        - eGFR thường được báo cáo dưới dạng mL/min/1.73m²
        - Cho phép so sánh chức năng thận giữa các bệnh nhân có kích thước khác nhau
        
        **Ứng dụng lâm sàng:**
        - ✅ **Liều hóa trị:** Hầu hết thuốc hóa trị (carboplatin, doxorubicin, v.v.)
        - ✅ **Chỉ số tim:** Cardiac Index = CO/BSA (bình thường: 2.5-4.0 L/min/m²)
        - ✅ **Chuẩn hóa eGFR:** Chuyển đổi eGFR chuẩn hóa → GFR tuyệt đối
        - ✅ **Tính liều một số kháng sinh:** Một số thuốc dùng BSA thay vì cân nặng
        
        **Chuyển đổi eGFR:**
        ```
        GFR tuyệt đối (mL/min) = eGFR (mL/min/1.73m²) × (BSA thực tế / 1.73)
        ```
        
        **Ví dụ:**
        - Bệnh nhân: 60 kg, 165 cm
        - BSA (Mosteller) = √[(60 × 165) / 3600] = **1.66 m²**
        - eGFR = 60 mL/min/1.73m²
        - GFR tuyệt đối = 60 × (1.66 / 1.73) = **57.6 mL/min**
        
        ---
        
        ### ⚖️ ABW (Adjusted Body Weight - Cân Nặng Điều Chỉnh)
        
        **Định nghĩa:** ABW là cân nặng được điều chỉnh từ IBW và cân nặng thực tế, được sử dụng để tính liều thuốc ở bệnh nhân béo phì. ABW phản ánh thực tế rằng ở người béo phì, mỡ không tham gia vào phân bố và thải trừ thuốc như cơ và các mô khác.
        
        **Công thức:**
        ```
        ABW = IBW + 0.4 × (Cân nặng thực tế - IBW)
        ```
        
        **Hệ số 0.4 nghĩa là gì?**
        - Chỉ 40% khối lượng mỡ thừa được tính vào ABW
        - Dựa trên nghiên cứu về phân bố và thải trừ thuốc ở người béo phì
        - Phản ánh: Mỡ có ít máu tưới, ít tham gia vào quá trình chuyển hóa thuốc
        
        **Khi nào dùng ABW?**
        - ✅ BMI > 30 kg/m² (béo phì)
        - ✅ Cân nặng > 130% IBW
        - ✅ Tính liều: Vancomycin, một số aminoglycosides, CrCl
        - ⚠️ Không dùng cho: Theophylline, Digoxin (dùng IBW)
        
        **Tại sao cần ABW?**
        - **Dùng cân nặng thực tế:** → Quá liều (mỡ không phân bố thuốc)
        - **Dùng IBW:** → Thiếu liều (không đủ hiệu quả)
        - **Dùng ABW:** → Liều tối ưu (cân bằng giữa hiệu quả và an toàn)
        
        **Ví dụ:**
        - Bệnh nhân: Nam, 170 cm, 100 kg (BMI = 34.6, béo phì)
        - IBW = 50 + 0.91 × (170 - 152.4) = 66.1 kg
        - ABW = 66.1 + 0.4 × (100 - 66.1) = **79.6 kg**
        - Liều vancomycin: Dùng ABW = 79.6 kg (không dùng 100 kg hay 66.1 kg)
        
        **Thuốc cần ABW:**
        - **Vancomycin:** ✅ Bắt buộc dùng ABW khi béo phì
        - **Aminoglycosides:** Một số nghiên cứu khuyến cáo ABW
        - **Cockcroft-Gault (CrCl):** Nên dùng ABW thay vì cân nặng thực tế
        
        **Thuốc KHÔNG dùng ABW (dùng IBW):**
        - Theophylline
        - Digoxin
        - Một số thuốc tim mạch khác
        
        ---
        
        ### 📊 So sánh Tổng Hợp
        
        | Chỉ số | Đơn vị | Mục đích | Khi nào dùng |
        |:-------|:-------|:---------|:-------------|
        | **BMI** | kg/m² | Sàng lọc béo phì | Đánh giá tình trạng dinh dưỡng, nguy cơ bệnh tật |
        | **IBW** | kg | Tính liều thuốc cơ bản | Aminoglycosides, Theophylline, Digoxin (người bình thường) |
        | **BSA** | m² | Tính liều hóa trị, chuẩn hóa eGFR | Hóa trị, Cardiac Index, chuyển đổi eGFR |
        | **ABW** | kg | Tính liều ở béo phì | Vancomycin, CrCl, một số aminoglycosides (BMI > 30) |
        
        **Quy tắc vàng:**
        1. **Người bình thường (BMI 18.5-25):** Dùng cân nặng thực tế hoặc IBW
        2. **Béo phì (BMI > 30):** Dùng ABW cho hầu hết thuốc
        3. **Liều hóa trị:** Luôn dùng BSA
        4. **Điều chỉnh liều thận:** Dùng GFR tuyệt đối (từ eGFR × BSA/1.73) hoặc CrCl với ABW
        """)
    
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng (Tóm tắt):**
    
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

