"""
Creatinine Clearance (Cockcroft-Gault)
Tính độ thanh thải creatinine - Quan trọng cho điều chỉnh liều thuốc
"""

import streamlit as st


def _format_num(value: float, decimals: int = 1) -> str:
    """Format số, loại bỏ số 0 thừa"""
    rounded = round(value, decimals)
    if rounded == int(rounded):
        return str(int(rounded))
    return f"{rounded:.{decimals}f}".rstrip('0').rstrip('.')


def calculate_crcl(age, weight, creatinine, gender, creatinine_unit="µmol/L"):
    """
    Cockcroft-Gault formula for Creatinine Clearance
    
    Returns CrCl in mL/min
    """
    # Convert creatinine to mg/dL if needed
    if creatinine_unit == "µmol/L":
        creatinine_mg = creatinine / 88.4
    else:
        creatinine_mg = creatinine
    
    # Cockcroft-Gault formula
    # CrCl (male) = [(140 - age) × weight] / (72 × SCr)
    # CrCl (female) = CrCl (male) × 0.85
    
    crcl = ((140 - age) * weight) / (72 * creatinine_mg)
    
    if gender == "female":
        crcl = crcl * 0.85
    
    return crcl


def render():
    """Render Creatinine Clearance calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧪 Creatinine Clearance (CrCl)</h2>
    <p style='text-align: center;'><em>Cockcroft-Gault Formula - Điều chỉnh liều thuốc</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin
    with st.expander("ℹ️ Giới thiệu về Creatinine Clearance"):
        st.markdown("""
        **Creatinine Clearance (CrCl)** là chỉ số ước tính **chức năng thận** dựa trên công thức **Cockcroft-Gault**.
        
        **Mục đích chính:**
        - ✅ **Điều chỉnh liều thuốc** theo chức năng thận
        - ✅ Đánh giá mức độ suy thận
        - ✅ Theo dõi tiến triển bệnh thận
        
        **Công thức Cockcroft-Gault (1976):**
        ```
        CrCl (nam) = [(140 - tuổi) × cân nặng (kg)] / (72 × SCr mg/dL)
        CrCl (nữ) = CrCl (nam) × 0.85
        ```
        
        **So sánh với eGFR:**
        - **CrCl:** Dựa trên cân nặng thực tế, tốt hơn cho điều chỉnh liều thuốc
        - **eGFR:** Chuẩn hóa theo BSA 1.73m², tốt hơn cho phân loại CKD
        
        **Ưu điểm:**
        - Đơn giản, nhanh
        - Được dùng trong hầu hết hướng dẫn điều chỉnh liều thuốc
        
        **Nhược điểm:**
        - Không chính xác ở: béo phì, suy dinh dưỡng, người cao tuổi
        - Đánh giá quá cao ở béo phì
        
        **Đơn vị:** mL/min (KHÔNG chuẩn hóa theo BSA)
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
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=20,
            max_value=300,
            value=70,
            step=1,
            help="Cân nặng thực tế của bệnh nhân"
        )
    
    with col2:
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
                value=100.0,
                step=1.0,
                format="%d",
                help="Bình thường: Nam 62-106, Nữ 44-80 µmol/L"
            )
            st.caption(f"💡 = {_format_num(creatinine / 88.4, 1)} mg/dL")
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
            st.caption(f"💡 = {round(creatinine * 88.4)} µmol/L")
    
    # Option for adjusted body weight
    st.markdown("---")
    st.markdown("### ⚙️ Tùy chọn nâng cao:")
    
    use_adjusted = st.checkbox(
        "Sử dụng Adjusted Body Weight (cho bệnh nhân béo phì)",
        help="Nên dùng nếu BMI > 30 hoặc cân nặng > 130% IBW"
    )
    
    if use_adjusted:
        height = st.number_input(
            "Chiều cao (cm) - Cần để tính ABW",
            min_value=100,
            max_value=250,
            value=170,
            step=1
        )
        
        # Calculate IBW
        if gender == "male":
            ibw = 50 + 0.91 * (height - 152.4)
        else:
            ibw = 45.5 + 0.91 * (height - 152.4)
        
        # Calculate ABW
        abw = ibw + 0.4 * (weight - ibw)
        
        st.info(f"""
        **Tính toán:**
        - IBW (Ideal Body Weight): **{ibw:.1f} kg**
        - ABW (Adjusted Body Weight): **{abw:.1f} kg**
        - Sẽ dùng ABW thay vì cân nặng thực tế ({weight:.0f} kg)
        """)
        
        weight_to_use = abw
    else:
        weight_to_use = weight
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Tính CrCl", type="primary", use_container_width=True):
        # Calculate CrCl
        crcl = calculate_crcl(age, weight_to_use, creatinine, gender, creatinine_unit)
        
        # Classify kidney function
        if crcl >= 90:
            stage = "Bình thường"
            color = "#28a745"
            icon = "✅"
        elif crcl >= 60:
            stage = "Giảm nhẹ (CKD G2)"
            color = "#28a745"
            icon = "✅"
        elif crcl >= 45:
            stage = "Giảm nhẹ-TB (CKD G3a)"
            color = "#ffc107"
            icon = "⚠️"
        elif crcl >= 30:
            stage = "Giảm TB-nặng (CKD G3b)"
            color = "#fd7e14"
            icon = "⚠️"
        elif crcl >= 15:
            stage = "Giảm nặng (CKD G4)"
            color = "#dc3545"
            icon = "🚨"
        else:
            stage = "Suy thận cuối (CKD G5)"
            color = "#dc3545"
            icon = "🚨"
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 40px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h1 style='color: {color}; margin: 0; text-align: center; font-size: 3em;'>
                {icon} CrCl = {crcl:.1f} mL/min
            </h1>
            <p style='text-align: center; font-size: 1.3em; margin-top: 15px; font-weight: bold;'>
                {stage}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Calculation breakdown
        st.markdown("### 📋 Chi tiết tính toán:")
        
        if creatinine_unit == "µmol/L":
            creatinine_mg = creatinine / 88.4
        else:
            creatinine_mg = creatinine
        
        st.markdown(f"""
        **Công thức Cockcroft-Gault:**
        ```
        CrCl = [(140 - {age}) × {weight_to_use:.0f}] / (72 × {creatinine_mg:.1f})
        CrCl = [{140 - age} × {weight_to_use:.0f}] / {72 * creatinine_mg:.1f}
        CrCl = {((140 - age) * weight_to_use) / (72 * creatinine_mg):.1f} mL/min
        ```
        """)
        
        if gender == "female":
            st.markdown(f"""
            **Điều chỉnh cho nữ giới (×0.85):**
            ```
            CrCl = {((140 - age) * weight_to_use) / (72 * creatinine_mg):.1f} × 0.85
            CrCl = {crcl:.1f} mL/min
            ```
            """)
        
        st.markdown("---")
        
        # Drug dosing guidance
        st.markdown("### 💊 Hướng dẫn điều chỉnh liều thuốc:")
        
        if crcl >= 60:
            st.success("""
            **✅ CrCl ≥ 60 mL/min - Chức năng thận gần bình thường**
            
            **Hầu hết các thuốc:**
            - ✅ Dùng liều bình thường
            - ✅ Không cần điều chỉnh liều
            
            **Ngoại trừ một số thuốc đặc biệt:**
            - Metformin: Cẩn trọng nếu CrCl 45-60
            - SGLT2i: Hiệu quả giảm khi CrCl < 60
            - Dabigatran: Giảm liều nếu CrCl 30-50
            
            **Lưu ý:**
            - Vẫn cần theo dõi chức năng thận định kỳ
            - Tránh thuốc độc thận (NSAIDs, aminoglycosides...)
            """)
        
        elif crcl >= 30:
            st.warning(f"""
            **⚠️ CrCl 30-59 mL/min - Suy thận mạn giai đoạn 3**
            
            **CrCl hiện tại: {crcl:.0f} mL/min**
            
            **Cần điều chỉnh liều nhiều thuốc:**
            
            **Kháng sinh:**
            - **Beta-lactams:** Giảm liều 50-75% hoặc tăng khoảng cách
            - **Fluoroquinolones:** Giảm liều 50%
            - **Aminoglycosides:** Giảm liều đáng kể, monitor nồng độ
            - **Vancomycin:** Điều chỉnh theo nồng độ đáy
            
            **Thuốc tim mạch:**
            - **Digoxin:** Giảm liều 50%, monitor nồng độ
            - **LMWH:** Giảm liều hoặc chuyển UFH
            - **Dabigatran:** Giảm liều (110 mg bid nếu CrCl 30-50)
            - **Rivaroxaban, Apixaban:** Giảm liều
            
            **Đái tháo đường:**
            - **Metformin:** TRÁNH nếu CrCl < 45, cẩn trọng 45-60
            - **SGLT2i:** TRÁNH nếu CrCl < 45
            - **Insulin:** Có thể cần giảm liều (giảm thanh thải)
            
            **Khác:**
            - **Allopurinol:** 100-200 mg/ngày (thay vì 300)
            - **Gabapentin, Pregabalin:** Giảm liều đáng kể
            - **Bisphosphonates:** Cẩn trọng nếu CrCl < 35
            
            ⚠️ **LUÔN tra cứu hướng dẫn cụ thể cho từng thuốc!**
            """)
        
        else:  # CrCl < 30
            st.error(f"""
            **🚨 CrCl < 30 mL/min - Suy thận nặng/giai đoạn cuối**
            
            **CrCl hiện tại: {crcl:.0f} mL/min**
            
            **⚠️ NGUY HIỂM - Cần hội chẩn dược sĩ/thận!**
            
            **Nhiều thuốc CHỐNG CHỈ ĐỊNH hoặc cần giảm liều mạnh:**
            
            **CHỐNG CHỈ ĐỊNH:**
            - ❌ **Metformin** (nguy cơ toan lactic)
            - ❌ **SGLT2i** (Dapagliflozin, Empagliflozin...)
            - ❌ **NSAIDs** (trừ khi thực sự cần thiết)
            - ❌ **Nitrofurantoin** (không hiệu quả)
            - ❌ **Dabigatran** nếu CrCl < 30
            
            **Cần GIẢM LIỀU MẠNH:**
            - **Kháng sinh:** Hầu hết cần điều chỉnh
            - **Digoxin:** 0.0625-0.125 mg/ngày, monitor nồng độ
            - **LMWH:** Chuyển sang UFH hoặc giảm liều rõ rệt
            - **Gabapentin/Pregabalin:** Giảm liều 50-75%
            - **Insulin:** Giảm liều, monitor đường huyết sát
            
            **Lựa chọn an toàn hơn:**
            - **Kháng sinh:** Ceftriaxone (không qua thận)
            - **Chống đông:** Warfarin (nhưng cần monitor)
            - **Giảm đau:** Tramadol (liều thấp), Morphine (cẩn trọng)
            
            **KHUYẾN CÁO:**
            - 🏥 **Hội chẩn dược sĩ lâm sàng** cho MỌI đơn thuốc
            - 📞 **Gọi thận bác sĩ** nếu nghi ngờ
            - 🧪 **Monitor:** SCr, K+, thuốc trong máu (nếu có)
            - 💊 **Cân nhắc lọc máu** nếu CrCl < 15
            
            **Nếu CrCl < 15:**
            - Nhiều thuốc tích lũy nguy hiểm
            - Cân nhắc lọc máu dự phòng
            - Chỉ dùng thuốc thực sự cần thiết
            """)
        
        # Common drugs dosing table
        with st.expander(f"💊 Bảng điều chỉnh liều thuốc phổ biến (CrCl = {crcl:.0f})"):
            if crcl >= 60:
                st.markdown("""
                | Thuốc | Liều bình thường | CrCl ≥60 | Ghi chú |
                |:------|:-----------------|:---------|:--------|
                | Amoxicillin | 500 mg q8h | Không đổi | - |
                | Ceftriaxone | 1-2 g q24h | Không đổi | Không qua thận |
                | Levofloxacin | 500 mg q24h | Không đổi | - |
                | Metformin | 500-1000 mg bid | Không đổi | Cẩn trọng 45-60 |
                | Digoxin | 0.25 mg/ngày | Không đổi | Monitor |
                """)
            
            elif crcl >= 30:
                st.markdown(f"""
                | Thuốc | Liều bình thường | CrCl {crcl:.0f} | Điều chỉnh |
                |:------|:-----------------|:----------------|:-----------|
                | **Amoxicillin** | 500 mg q8h | 250-500 mg q12h | Giảm liều hoặc tăng khoảng |
                | **Ceftriaxone** | 1-2 g q24h | Không đổi | An toàn |
                | **Levofloxacin** | 500 mg q24h | 250 mg q24h | Giảm 50% |
                | **Metformin** | 500-1000 mg bid | **TRÁNH < 45**<br>Cẩn trọng 45-60 | Nguy cơ toan lactic |
                | **Digoxin** | 0.25 mg/ngày | 0.0625-0.125 mg | Giảm 50-75% |
                | **Enoxaparin** | 1 mg/kg q12h | 1 mg/kg q24h | Tăng khoảng cách |
                | **Gabapentin** | 300 mg tid | 200-300 mg qd-bid | Giảm đáng kể |
                """)
            
            else:
                st.markdown(f"""
                | Thuốc | Liều bình thường | CrCl {crcl:.0f} | Điều chỉnh |
                |:------|:-----------------|:----------------|:-----------|
                | **Amoxicillin** | 500 mg q8h | 250 mg q24h | Giảm mạnh |
                | **Ceftriaxone** | 1-2 g q24h | 1 g q24h | Giảm liều |
                | **Levofloxacin** | 500 mg q24h | 250 mg q48h | Giảm mạnh |
                | **Metformin** | 500-1000 mg bid | **❌ CHỐNG CHỈ ĐỊNH** | Nguy hiểm! |
                | **Digoxin** | 0.25 mg/ngày | 0.0625 mg qod-tiw | Rất thấp, monitor |
                | **Enoxaparin** | 1 mg/kg q12h | Chuyển UFH | Không khuyến cáo |
                | **Gabapentin** | 300 mg tid | 100-300 mg qod | Giảm 75-90% |
                | **SGLT2i** | Liều chuẩn | **❌ CHỐNG CHỈ ĐỊNH** | - |
                """)
        
        # Export section
        st.markdown("---")
        from components.export import render_export_section
        
        # Prepare inputs for export
        inputs_dict = {
            "Age": f"{age} tuổi",
            "Gender": "Nam" if gender == "male" else "Nữ",
            "Weight": f"{weight_to_use:.1f} kg" + (f" (ABW, từ {weight:.1f} kg)" if use_adjusted else ""),
            "Creatinine": f"{creatinine:.2f} {creatinine_unit}",
            "Used Adjusted Weight": "Có" if use_adjusted else "Không"
        }
        
        # Prepare results for export
        results_dict = {
            "CrCl": f"{crcl:.1f} mL/min",
            "Kidney Function": stage,
            "CKD Stage": "G1/G2" if crcl >= 60 else "G3a" if crcl >= 45 else "G3b" if crcl >= 30 else "G4" if crcl >= 15 else "G5"
        }
        
        render_export_section(
            title=f"CrCl = {crcl:.1f} mL/min",
            inputs=inputs_dict,
            results=results_dict,
            calculator_name="Creatinine Clearance (Cockcroft-Gault)",
            filename="crcl_result"
        )
        
        # Comparison with eGFR
        with st.expander("🔄 So sánh CrCl vs eGFR"):
            # Calculate eGFR for comparison
            if creatinine_unit == "µmol/L":
                creatinine_mg = creatinine / 88.4
            else:
                creatinine_mg = creatinine
            
            kappa = 0.7 if gender == "female" else 0.9
            alpha = -0.329 if gender == "female" else -0.411
            gender_factor = 1.018 if gender == "female" else 1.0
            
            min_val = min(creatinine_mg / kappa, 1)
            max_val = max(creatinine_mg / kappa, 1)
            
            egfr = 141 * (min_val ** alpha) * (max_val ** -1.209) * (0.993 ** age) * gender_factor
            
            st.markdown(f"""
            ### So sánh 2 chỉ số:
            
            | Chỉ số | Giá trị | Đơn vị | Mục đích |
            |:-------|:--------|:-------|:---------|
            | **CrCl** (Cockcroft-Gault) | **{crcl:.1f}** | mL/min | **Điều chỉnh liều thuốc** ⭐ |
            | **eGFR** (CKD-EPI) | **{egfr:.1f}** | mL/min/1.73m² | **Phân loại CKD** ⭐ |
            
            ---
            
            ### Khi nào dùng CrCl vs eGFR?
            
            **Dùng CrCl (Cockcroft-Gault) khi:**
            - ✅ **Điều chỉnh liều thuốc** (hầu hết hướng dẫn dựa trên CrCl)
            - ✅ Bệnh nhân có cân nặng bất thường
            - ✅ Cần tính toán nhanh tại giường bệnh
            
            **Dùng eGFR (CKD-EPI) khi:**
            - ✅ **Phân loại giai đoạn CKD**
            - ✅ Đánh giá tiến triển bệnh thận mạn
            - ✅ Nghiên cứu, báo cáo
            
            ### Sự khác biệt:
            
            - **CrCl:** Dựa trên cân nặng thực tế → Cao hơn ở người béo
            - **eGFR:** Chuẩn hóa theo BSA 1.73m² → Không phụ thuộc cân nặng
            
            **Ví dụ:**
            - Bệnh nhân béo phì (100 kg): CrCl cao, eGFR bình thường
            - Bệnh nhân gầy (45 kg): CrCl thấp, eGFR có thể bình thường
            
            ### Khuyến cáo:
            
            - 📊 **Dùng CẢ HAI** để đánh giá toàn diện
            - 💊 **Điều chỉnh liều thuốc:** Ưu tiên CrCl
            - 🏥 **Phân loại CKD:** Ưu tiên eGFR
            - ⚠️ **Nếu khác biệt lớn:** Cân nhắc cân nặng, tình trạng dinh dưỡng
            
            ---
            
            ### 📖 Giải Thích Chuyên Sâu
            
            **CrCl (Creatinine Clearance - Độ Thanh Thải Creatinine):**
            - **Định nghĩa:** CrCl là thể tích huyết tương được thanh thải creatinine trong một phút, thể hiện khả năng lọc của thận
            - **Đơn vị:** mL/min (KHÔNG chuẩn hóa theo BSA)
            - **Công thức Cockcroft-Gault:** CrCl = [(140 - tuổi) × cân nặng] / (72 × SCr)
            - **Ưu điểm:** Đơn giản, nhanh, được dùng trong hầu hết hướng dẫn điều chỉnh liều
            - **Nhược điểm:** Đánh giá quá cao ở béo phì, quá thấp ở suy dinh dưỡng
            
            **eGFR (estimated GFR - Tốc Độ Lọc Cầu Thận Ước Tính):**
            - **Định nghĩa:** eGFR là giá trị ước tính GFR dựa trên các công thức (CKD-EPI, MDRD)
            - **Đơn vị:** mL/min/1.73m² (chuẩn hóa theo BSA)
            - **Ưu điểm:** Chuẩn hóa cho phép so sánh giữa các bệnh nhân, tốt cho phân loại CKD
            - **Nhược điểm:** Cần chuyển đổi sang GFR tuyệt đối để điều chỉnh liều thuốc
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Cockcroft DW, Gault MH.** Prediction of creatinine clearance from serum creatinine. 
               *Nephron.* 1976;16(1):31-41.
            
            2. **Levey AS, Bosch JP, Lewis JB, et al.** A more accurate method to estimate glomerular filtation rate from serum creatinine: a new prediction equation. 
               *Ann Intern Med.* 1999;130(6):461-70.
            
            3. **Stevens LA, Nolin TD, Richardson MM, et al.** Comparison of drug dosing recommendations based on measured GFR and kidney function estimating equations. 
               *Am J Kidney Dis.* 2009;54(1):33-42.
            
            4. **Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group.** KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease. 
               *Kidney Int Suppl.* 2013;3:1-150.
            """)
    
    # Quick reference
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **CrCl là chỉ số CHÍNH cho điều chỉnh liều thuốc**
    
    2. **Công thức:** [(140 - tuổi) × cân nặng] / (72 × SCr mg/dL) × 0.85 (nữ)
    
    3. **Béo phì:** Nên dùng Adjusted Body Weight thay vì cân nặng thực
    
    4. **CrCl < 60:** Cần điều chỉnh nhiều thuốc
    
    5. **CrCl < 30:** ⚠️ Hội chẩn dược sĩ/thận cho MỌI đơn thuốc!
    
    6. **Luôn tra cứu** hướng dẫn cụ thể cho từng thuốc
    """)


if __name__ == "__main__":
    render()

