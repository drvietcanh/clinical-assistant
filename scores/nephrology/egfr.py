"""
eGFR Calculator - CKD-EPI & MDRD
Tính tốc độ lọc cầu thận ước tính
"""

import streamlit as st
import math


def calculate_ckd_epi(creatinine_mg, age, gender, race, creatinine_unit="mg/dL"):
    """
    CKD-EPI 2009 formula (the most accurate current formula)
    
    Returns eGFR in mL/min/1.73m²
    """
    # Convert to mg/dL if needed
    if creatinine_unit == "µmol/L":
        creatinine_mg = creatinine_mg / 88.4
    
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


def calculate_mdrd(creatinine_mg, age, gender, race, creatinine_unit="mg/dL"):
    """
    MDRD formula (older, less accurate but still used)
    
    Returns eGFR in mL/min/1.73m²
    """
    # Convert to mg/dL if needed
    if creatinine_unit == "µmol/L":
        creatinine_mg = creatinine_mg / 88.4
    
    # Gender factor
    gender_factor = 0.742 if gender == "female" else 1.0
    
    # Race factor
    race_factor = 1.212 if race == "black" else 1.0
    
    # Calculate
    egfr = 175 * (creatinine_mg ** -1.154) * (age ** -0.203) * gender_factor * race_factor
    
    return egfr


def interpret_egfr(egfr):
    """Interpret eGFR according to CKD stages"""
    
    if egfr >= 90:
        stage = "G1 - Bình thường hoặc cao"
        description = "Chức năng thận bình thường (nếu không có bằng chứng tổn thương thận khác)"
        color = "green"
        action = "Theo dõi thường quy nếu có yếu tố nguy cơ"
    elif egfr >= 60:
        stage = "G2 - Giảm nhẹ"
        description = "Giảm GFR nhẹ (có thể bình thường ở người cao tuổi)"
        color = "green"
        action = "Theo dõi, kiểm soát yếu tố nguy cơ"
    elif egfr >= 45:
        stage = "G3a - Giảm nhẹ-trung bình"
        description = "Suy thận mạn giai đoạn 3a"
        color = "orange"
        action = "Theo dõi 6-12 tháng, điều chỉnh liều thuốc, kiểm soát ĐTĐ/THA"
    elif egfr >= 30:
        stage = "G3b - Giảm trung bình-nặng"
        description = "Suy thận mạn giai đoạn 3b"
        color = "orange"
        action = "Theo dõi 3-6 tháng, chuẩn bị điều trị thận, hội chẩn chuyên khoa"
    elif egfr >= 15:
        stage = "G4 - Giảm nặng"
        description = "Suy thận mạn giai đoạn 4"
        color = "red"
        action = "⚠️ Theo dõi 1-3 tháng, chuẩn bị lọc máu/ghép thận, hội chẩn thận"
    else:
        stage = "G5 - Suy thận giai đoạn cuối"
        description = "Suy thận giai đoạn cuối (ESRD)"
        color = "red"
        action = "🚨 Cần lọc máu hoặc ghép thận"
    
    return {
        "stage": stage,
        "description": description,
        "color": color,
        "action": action
    }


def render():
    """Render eGFR calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧪 eGFR Calculator</h2>
    <p style='text-align: center;'><em>Tính tốc độ lọc cầu thận ước tính - CKD-EPI & MDRD</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về eGFR
    with st.expander("ℹ️ Giới thiệu về eGFR"):
        st.markdown("""
        **eGFR (estimated Glomerular Filtration Rate)** là chỉ số ước tính tốc độ lọc cầu thận, 
        dùng để đánh giá chức năng thận.
        
        **2 công thức phổ biến:**
        
        1. **CKD-EPI (2009)** - Khuyến cáo hiện tại ⭐
           - Chính xác hơn MDRD
           - Đặc biệt tốt ở eGFR > 60
           - Công thức tiêu chuẩn hiện nay
        
        2. **MDRD (1999)** - Công thức cũ
           - Vẫn được dùng rộng rãi
           - Ít chính xác hơn CKD-EPI
           - Có xu hướng đánh giá thấp eGFR > 60
        
        **Đơn vị:** mL/min/1.73m²
        
        **Lưu ý:**
        - eGFR dựa trên creatinine máu
        - Không chính xác ở: trẻ em, bệnh gan nặng, suy dinh dưỡng, bệnh cơ
        - Cần kết hợp với albumin niệu để phân loại CKD đầy đủ
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
            help="Tuổi của bệnh nhân (≥18)"
        )
        
        gender = st.radio(
            "Giới tính",
            options=["male", "female"],
            format_func=lambda x: "Nam" if x == "male" else "Nữ",
            horizontal=True
        )
        
        race = st.radio(
            "Chủng tộc",
            options=["non-black", "black"],
            format_func=lambda x: "Châu Phi / Da đen" if x == "black" else "Khác (Châu Á, Châu Âu...)",
            help="CKD-EPI có hệ số điều chỉnh cho người da đen"
        )
    
    with col2:
        creatinine_unit = st.radio(
            "Đơn vị Creatinine",
            options=["µmol/L", "mg/dL"],
            index=0,
            horizontal=True,
            help="µmol/L phổ biến ở Việt Nam, mg/dL ở Mỹ"
        )
        
        if creatinine_unit == "µmol/L":
            creatinine = st.number_input(
                "Creatinine (µmol/L)",
                min_value=10.0,
                max_value=2000.0,
                value=100.0,
                step=1.0,
                help="Bình thường: Nam 62-106, Nữ 44-80 µmol/L"
            )
            st.caption(f"💡 = {creatinine / 88.4:.2f} mg/dL")
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
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Tính eGFR", type="primary", use_container_width=True):
        # Calculate both formulas
        egfr_ckd_epi = calculate_ckd_epi(creatinine, age, gender, race, creatinine_unit)
        egfr_mdrd = calculate_mdrd(creatinine, age, gender, race, creatinine_unit)
        
        # Interpret based on CKD-EPI (preferred)
        interpretation = interpret_egfr(egfr_ckd_epi)
        
        # Display results
        st.markdown("## 📊 Kết quả")
        
        # Main result - CKD-EPI
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[interpretation["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h3 style='color: {score_color}; margin: 0; text-align: center;'>
                eGFR (CKD-EPI): {egfr_ckd_epi:.1f} mL/min/1.73m²
            </h3>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {interpretation['stage']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Comparison table
        st.markdown("### 📋 So sánh 2 công thức:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "CKD-EPI (Khuyến cáo)",
                f"{egfr_ckd_epi:.1f} mL/min/1.73m²",
                help="Công thức chính xác hơn, khuyến cáo sử dụng"
            )
        
        with col2:
            diff = egfr_mdrd - egfr_ckd_epi
            st.metric(
                "MDRD (Tham khảo)",
                f"{egfr_mdrd:.1f} mL/min/1.73m²",
                delta=f"{diff:+.1f}",
                help="Công thức cũ, có thể khác biệt với CKD-EPI"
            )
        
        st.markdown("---")
        
        # Interpretation
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Giai đoạn: {interpretation['stage']}</h3>
            <p style='font-size: 1.1em; margin: 10px 0;'>{interpretation['description']}</p>
            <p style='font-size: 1.2em; color: {score_color}; font-weight: bold; margin: 10px 0;'>
                💡 {interpretation['action']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Clinical guidance
        st.markdown("---")
        st.markdown("### 📋 Hướng dẫn lâm sàng")
        
        if egfr_ckd_epi >= 60:
            st.success("""
            ✅ **eGFR ≥ 60 - Chức năng thận tốt/giảm nhẹ**
            
            **Quản lý:**
            - Theo dõi hàng năm nếu có yếu tố nguy cơ (ĐTĐ, THA)
            - Kiểm soát đường huyết, huyết áp
            - Kiểm tra albumin niệu (quan trọng!)
            - Lối sống lành mạnh
            
            **Lưu ý:**
            - eGFR 60-89 có thể bình thường ở người cao tuổi
            - Chỉ chẩn đoán CKD nếu có bằng chứng tổn thương thận khác
            """)
        
        elif egfr_ckd_epi >= 30:
            st.warning("""
            ⚠️ **eGFR 30-59 - Suy thận mạn giai đoạn 3**
            
            **Quản lý:**
            - **Theo dõi 3-12 tháng** tùy giai đoạn
            - Kiểm soát chặt chẽ:
              - ĐTĐ: HbA1c < 7%
              - THA: BP < 130/80 (< 120/80 nếu có albumin niệu)
              - Lipid: LDL < 100 mg/dL
            
            - **Điều chỉnh liều thuốc** theo eGFR
            - **Tránh:** NSAIDs, thuốc cản quang (hoặc dự phòng)
            - **ACEi/ARB** nếu có albumin niệu
            - **Chế độ ăn:** Hạn chế protein (0.8 g/kg/ngày)
            
            - **Hội chẩn thận** nếu G3b (eGFR < 45)
            """)
        
        else:
            st.error("""
            🚨 **eGFR < 30 - Suy thận nặng/giai đoạn cuối**
            
            **Quản lý:**
            - ⚠️ **Hội chẩn chuyên khoa thận NGAY**
            - Theo dõi 1-3 tháng
            
            **Chuẩn bị thay thế thận:**
            - eGFR < 20: Chuẩn bị lọc máu/ghép thận
            - eGFR < 15: Thường cần bắt đầu lọc máu
            - Đánh giá AVF (fistula) cho lọc máu
            - Đánh giá ghép thận nếu phù hợp
            
            **Điều trị:**
            - Điều chỉnh liều thuốc theo eGFR
            - Kiểm soát biến chứng: thiếu máu, bệnh xương, acid-base
            - Chế độ ăn giảm protein, giảm phosphate
            - Tránh tuyệt đối thuốc độc thận
            
            **Chỉ định lọc máu:**
            - eGFR < 10-15 + triệu chứng
            - Toan chuyển hóa kháng trị
            - Tăng K+ kháng trị
            - Phù phổi kháng trị
            - Viêm màng phổi/tim do urê cao
            """)
        
        # CKD stages table
        with st.expander("📊 Bảng phân loại CKD (KDIGO)"):
            st.markdown("""
            | Giai đoạn | eGFR (mL/min/1.73m²) | Mô tả | Quản lý |
            |:----------|:---------------------|:------|:--------|
            | **G1** | ≥ 90 | Bình thường/Cao | Theo dõi nếu có tổn thương thận |
            | **G2** | 60-89 | Giảm nhẹ | Theo dõi, kiểm soát nguy cơ |
            | **G3a** | 45-59 | Giảm nhẹ-TB | Theo dõi 6-12 tháng |
            | **G3b** | 30-44 | Giảm TB-nặng | Theo dõi 3-6 tháng, hội chẩn thận |
            | **G4** | 15-29 | Giảm nặng | Theo dõi 1-3 tháng, chuẩn bị thay thế |
            | **G5** | < 15 | ESRD | Lọc máu hoặc ghép thận |
            
            **Phân loại CKD đầy đủ cần cả:**
            - Giai đoạn G (dựa eGFR)
            - Giai đoạn A (dựa albumin niệu):
              - A1: < 30 mg/g
              - A2: 30-300 mg/g
              - A3: > 300 mg/g
            
            **Ví dụ:** CKD G3aA2 = eGFR 45-59 + albumin niệu 30-300
            """)
        
        # Drug dosing
        with st.expander("💊 Điều chỉnh liều thuốc theo eGFR"):
            st.markdown(f"""
            **eGFR hiện tại: {egfr_ckd_epi:.0f} mL/min/1.73m²**
            
            ### Thuốc cần điều chỉnh liều:
            
            **Kháng sinh:**
            - Beta-lactams (Penicillin, Cephalosporins)
            - Aminoglycosides (Gentamicin, Amikacin)
            - Vancomycin
            - Fluoroquinolones
            
            **Tim mạch:**
            - Digoxin
            - LMWH (Enoxaparin)
            - Một số thuốc hạ áp
            
            **Khác:**
            - Metformin (tránh nếu eGFR < 30)
            - SGLT2i (tránh nếu eGFR < 20)
            - Allopurinol
            - Gabapentin, Pregabalin
            
            **Thuốc TRÁNH khi eGFR thấp:**
            - NSAIDs (tránh nếu < 60, chống chỉ định nếu < 30)
            - Metformin (chống chỉ định < 30)
            - Spironolactone (cẩn trọng < 30)
            
            ⚠️ **Lưu ý:** Luôn tra cứu liều chính xác trong sách hướng dẫn!
            """)
        
        # Limitations
        with st.expander("⚠️ Giới hạn của eGFR"):
            st.markdown("""
            **eGFR KHÔNG chính xác ở:**
            
            1. **Trẻ em < 18 tuổi** (dùng công thức Schwartz)
            2. **Thai kỳ** (GFR sinh lý tăng)
            3. **Người rất gầy hoặc béo phì** (BMI < 18 hoặc > 35)
            4. **Bệnh cơ nặng** (creatinine thấp)
            5. **Suy dinh dưỡng nặng**
            6. **Bệnh gan nặng** (giảm sản xuất creatinine)
            7. **Ăn nhiều thịt** (tăng creatinine tạm thời)
            8. **Sau khi tập thể dục nặng**
            9. **Cắt cụt chi**
            
            **Khi nghi ngờ eGFR không chính xác:**
            - Đo **Cystatin C** (ít bị ảnh hưởng bởi cơ)
            - Tính eGFR dựa trên Cystatin C
            - Đo GFR trực tiếp (Inulin, EDTA) - chuẩn vàng
            - Thu thập nước tiểu 24h tính CrCl
            
            **Lưu ý:**
            - eGFR chỉ chính xác khi creatinine ổn định
            - Trong AKI (creatinine tăng nhanh), eGFR KHÔNG có giá trị
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Levey AS, Stevens LA, Schmid CH, et al.** A new equation to estimate glomerular 
               filtration rate. Ann Intern Med. 2009;150(9):604-12. *(CKD-EPI Formula)*
            
            2. **Levey AS, Bosch JP, Lewis JB, et al.** A more accurate method to estimate glomerular 
               filtration rate from serum creatinine: a new prediction equation. 
               Ann Intern Med. 1999;130(6):461-70. *(MDRD Formula)*
            
            3. **KDIGO 2012 Clinical Practice Guideline for the Evaluation and Management of 
               Chronic Kidney Disease.** Kidney Int Suppl. 2013;3(1):1-150.
            
            4. **Inker LA, Astor BC, Fox CH, et al.** KDOQI US commentary on the 2012 KDIGO clinical 
               practice guideline for the evaluation and management of CKD. 
               Am J Kidney Dis. 2014;63(5):713-35.
            
            5. **Stevens PE, Levin A; Kidney Disease: Improving Global Outcomes Chronic Kidney Disease 
               Guideline Development Work Group Members.** Evaluation and management of chronic kidney disease: 
               synopsis of the kidney disease: improving global outcomes 2012 clinical practice guideline. 
               Ann Intern Med. 2013;158(11):825-30.
            """)
    
    # Quick guide
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **CKD-EPI là công thức khuyến cáo hiện nay** - Chính xác hơn MDRD
    
    2. **eGFR < 60 trong ≥ 3 tháng** = Suy thận mạn (nếu có tổn thương thận)
    
    3. **Luôn kiểm tra albumin niệu** - Cần thiết để phân loại CKD đầy đủ
    
    4. **Kiểm soát ĐTĐ & THA** - Quan trọng nhất để ngăn tiến triển
    
    5. **Tránh thuốc độc thận:** NSAIDs, aminoglycosides, thuốc cản quang
    
    6. **Hội chẩn thận khi:**
       - eGFR < 45 (G3b)
       - eGFR giảm > 25% trong 1 năm
       - Albumin niệu > 300 mg/g
    """)


if __name__ == "__main__":
    render()

