"""
eGFR Calculator - Help Sections and Expanders
Handles all help content and educational expanders
"""

import streamlit as st


def render_overview_expander():
    """Render the overview expander at the top"""
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


def render_calculation_details(
    weight_kg, height_cm, age, creatinine_mg, creatinine_unit, creatinine,
    use_abw, abw, bsa, egfr_ckd_epi, egfr_mdrd, crcl, gfr_absolute_ckd_epi
):
    """Render detailed calculation breakdown expander"""
    with st.expander("📋 Chi tiết tính toán"):
        st.markdown(f"""
        ### 1. BSA (Body Surface Area) - Mosteller
        
        Công thức được KDIGO, FDA, NCCN khuyến cáo:
        ```python
        BSA = √[(Cân nặng × Chiều cao) / 3600]
        BSA = √[({weight_kg:.0f} × {height_cm}) / 3600]
        BSA = √[{weight_kg * height_cm:.0f} / 3600]
        BSA = {bsa:.2f} m²
        ```
        
        ### 2. CKD-EPI 2009
        
        Công thức khuyến cáo cho chẩn đoán CKD:
        ```python
        egfr_ckd_epi = 141 × (Scr/κ)ᵅ × (Scr/κ)^-1.209 × 0.993^age × G × R
        egfr = {egfr_ckd_epi:.1f} mL/min/1.73m²
        ```
        
        ### 3. MDRD
        
        Công thức cũ, ít chính xác hơn:
        ```python
        egfr_mdrd = 175 × Scr^-1.154 × age^-0.203 × G × R
        egfr = {egfr_mdrd:.1f} mL/min/1.73m²
        ```
        
        ### 4. Cockcroft-Gault
        
        Ưu tiên cho điều chỉnh liều thuốc:
        ```python
        CrCl = [(140 - age) × weight] / (72 × SCr) × G
        {('ABW = ' + f'{abw:.1f}' + ' kg (nếu dùng ABW)' if use_abw else '')}
        CrCl = {crcl:.1f} mL/min
        ```
        
        ### 5. Chuyển đổi GFR
        
        Từ eGFR chuẩn hóa sang GFR tuyệt đối:
        ```python
        GFR_absolute = eGFR × (BSA / 1.73)
        GFR_absolute = {egfr_ckd_epi:.1f} × ({bsa:.2f} / 1.73)
        GFR_absolute = {gfr_absolute_ckd_epi:.1f} mL/min
        ```
        """)


def render_formula_guide():
    """Render when to use which formula expander"""
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


def render_example(
    age, height_cm, weight_kg, creatinine, creatinine_unit, creatinine_mg,
    bsa, egfr_ckd_epi, interpretation, gfr_absolute_ckd_epi, dosing_gfr
):
    """Render example illustration expander"""
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


def render_ckd_stages_table():
    """Render CKD stages table expander"""
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


def render_bsa_comparison(
    bsa_mosteller, bsa_dubois, bsa_haycock, bsa_boyd, bsa_shuter, bsa
):
    """Render BSA formulas comparison expander"""
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


def render_references():
    """Render references expander"""
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


def render_detailed_explanations():
    """Render detailed explanations expander"""
    with st.expander("📖 Giải Thích Chuyên Sâu Các Thuật Ngữ", expanded=False):
        st.markdown("""
        ### 🧪 eGFR (estimated Glomerular Filtration Rate - Tốc Độ Lọc Cầu Thận Ước Tính)
        
        **Định nghĩa:** eGFR là giá trị ước tính tốc độ lọc cầu thận (GFR) dựa trên các công thức tính toán, không cần đo trực tiếp. GFR là thể tích huyết tương được lọc qua cầu thận trong một đơn vị thời gian (thường là mL/min).
        
        **Đơn vị:**
        - **eGFR chuẩn hóa:** mL/min/1.73m² (chuẩn hóa theo BSA 1.73 m²)
        - **GFR tuyệt đối:** mL/min (không chuẩn hóa)
        
        **Tại sao chuẩn hóa theo BSA 1.73 m²?**
        - Cho phép so sánh chức năng thận giữa các bệnh nhân có kích thước khác nhau
        - 1.73 m² là BSA trung bình của người trưởng thành (nam, 70 kg, 170 cm)
        - Giúp phân loại CKD chính xác hơn, không bị ảnh hưởng bởi cân nặng
        
        **Các công thức eGFR:**
        
        **1. CKD-EPI (2009) - ⭐ Khuyến nghị hàng đầu:**
        - Phát triển bởi Chronic Kidney Disease Epidemiology Collaboration
        - Chính xác hơn MDRD, đặc biệt ở eGFR > 60 mL/min/1.73m²
        - Được KDIGO, FDA, và nhiều hướng dẫn quốc tế khuyến cáo
        - Công thức phức tạp, dựa trên: Creatinine, tuổi, giới tính, chủng tộc
        
        **2. MDRD (1999) - Công thức cũ:**
        - Modification of Diet in Renal Disease Study
        - Chính xác ở eGFR < 60, nhưng kém chính xác ở eGFR cao
        - Vẫn được một số lab sử dụng, nhưng đang dần thay thế bởi CKD-EPI
        
        **3. Cystatin C-based eGFR (2012):**
        - Dựa trên Cystatin C (protein ổn định hơn Creatinine)
        - Không bị ảnh hưởng bởi khối cơ, dinh dưỡng
        - Tốt cho: Người gầy, suy dinh dưỡng, bệnh nhân có khối cơ bất thường
        
        **Khi nào dùng eGFR?**
        - ✅ **Chẩn đoán và phân loại CKD:** Theo KDIGO Guidelines
        - ✅ **Theo dõi tiến triển bệnh thận mạn:** So sánh giữa các thời điểm
        - ✅ **Nghiên cứu và báo cáo:** Dữ liệu chuẩn hóa dễ so sánh
        - ⚠️ **KHÔNG dùng trực tiếp cho điều chỉnh liều thuốc:** Cần chuyển sang GFR tuyệt đối
        
        ---
        
        ### 🩸 CrCl (Creatinine Clearance - Độ Thanh Thải Creatinine)
        
        **Định nghĩa:** CrCl là tốc độ thải trừ creatinine từ máu qua thận, được tính bằng công thức Cockcroft-Gault hoặc đo trực tiếp từ nước tiểu 24 giờ.
        
        **Công thức Cockcroft-Gault (1976):**
        ```
        CrCl (nam) = [(140 - tuổi) × cân nặng (kg)] / (72 × SCr mg/dL)
        CrCl (nữ) = CrCl (nam) × 0.85
        ```
        
        **Đơn vị:** mL/min (KHÔNG chuẩn hóa theo BSA)
        
        **Ưu điểm:**
        - Đơn giản, dễ tính toán tại giường bệnh
        - Được sử dụng trong hầu hết hướng dẫn điều chỉnh liều thuốc
        - Tốt cho bệnh nhân có cân nặng bình thường
        
        **Nhược điểm:**
        - Đánh giá quá cao ở bệnh nhân béo phì (mỡ không sản xuất creatinine)
        - Đánh giá quá thấp ở bệnh nhân suy dinh dưỡng (khối cơ giảm)
        - Kém chính xác ở người cao tuổi, bệnh nhân có khối cơ bất thường
        
        **Khi nào dùng CrCl?**
        - ✅ **Điều chỉnh liều thuốc:** Hầu hết hướng dẫn dựa trên CrCl
        - ✅ **Béo phì:** Cockcroft-Gault với ABW (Adjusted Body Weight)
        - ✅ **Tính toán nhanh:** Không cần BSA
        
        ---
        
        ### 🔄 GFR Tuyệt Đối vs eGFR Chuẩn Hóa
        
        **eGFR chuẩn hóa (mL/min/1.73m²):**
        - Đã được điều chỉnh để bệnh nhân có BSA = 1.73 m²
        - Dùng cho: Chẩn đoán CKD, phân loại giai đoạn
        - **Ví dụ:** eGFR = 60 mL/min/1.73m² → CKD G3a
        
        **GFR tuyệt đối (mL/min):**
        - Giá trị thực tế, không điều chỉnh theo BSA
        - Dùng cho: Điều chỉnh liều thuốc
        - **Tính từ eGFR:** GFR tuyệt đối = eGFR × (BSA thực tế / 1.73)
        
        **Ví dụ cụ thể:**
        - Bệnh nhân A: 50 kg, 160 cm, BSA = 1.50 m²
        - eGFR = 60 mL/min/1.73m²
        - GFR tuyệt đối = 60 × (1.50 / 1.73) = **52.0 mL/min**
        
        - Bệnh nhân B: 90 kg, 180 cm, BSA = 2.10 m²
        - eGFR = 60 mL/min/1.73m²
        - GFR tuyệt đối = 60 × (2.10 / 1.73) = **72.8 mL/min**
        
        → Cùng eGFR nhưng GFR tuyệt đối khác nhau → Liều thuốc khác nhau!
        
        ---
        
        ### 🦴 CKD (Chronic Kidney Disease - Bệnh Thận Mạn)
        
        **Định nghĩa:** CKD là tình trạng tổn thương thận hoặc giảm GFR kéo dài ≥ 3 tháng, ảnh hưởng đến sức khỏe.
        
        **Tiêu chuẩn chẩn đoán (KDIGO 2012):**
        1. **Tổn thương thận:** Albumin niệu, bất thường hình ảnh học, hoặc bệnh lý mô học
        2. **Giảm GFR:** eGFR < 60 mL/min/1.73m²
        3. **Kéo dài ≥ 3 tháng**
        
        **Phân loại CKD theo GFR (KDIGO):**
        | Giai đoạn | eGFR (mL/min/1.73m²) | Mô tả |
        |:----------|:---------------------|:------|
        | G1 | ≥ 90 | Chức năng thận bình thường hoặc cao |
        | G2 | 60-89 | Giảm nhẹ |
        | G3a | 45-59 | Giảm nhẹ-trung bình |
        | G3b | 30-44 | Giảm trung bình-nặng |
        | G4 | 15-29 | Giảm nặng |
        | G5 | < 15 hoặc lọc máu | Suy thận giai đoạn cuối (ESRD) |
        
        **Ý nghĩa lâm sàng:**
        - **G1-G2:** Theo dõi, kiểm soát yếu tố nguy cơ
        - **G3a-G3b:** Điều chỉnh liều thuốc, hội chẩn chuyên khoa
        - **G4:** Chuẩn bị lọc máu, tư vấn ghép thận
        - **G5:** Cần lọc máu hoặc ghép thận
        
        ---
        
        ### 📋 Khi Nào Dùng Cái Gì?
        
        | Mục đích | Dùng gì? | Đơn vị | Giải thích |
        |:---------|:---------|:-------|:-----------|
        | **Chẩn đoán CKD** | eGFR CKD-EPI (chuẩn hóa) | mL/min/1.73m² | Phân loại theo KDIGO |
        | **Điều chỉnh liều thuốc** | CrCl hoặc GFR tuyệt đối | mL/min | FDA, Micromedex khuyến cáo CrCl |
        | **Béo phì (BMI > 30)** | Cockcroft-Gault + ABW | mL/min | ABW chính xác hơn cân nặng thực tế |
        | **Người gầy/Suy dinh dưỡng** | Cystatin C eGFR | mL/min/1.73m² | Ít bị ảnh hưởng bởi khối cơ |
        | **ICU/AKI** | Đo CrCl 24h hoặc Jelliffe | mL/min | Cr biến động, không dùng eGFR |
        | **Người già** | CKD-EPI 2021 | mL/min/1.73m² | Chính xác hơn ở người cao tuổi |
        
        ---
        
        ### ⚠️ Lưu ý quan trọng
        
        **1. Chẩn đoán CKD:**
        - ✅ Dùng **eGFR chuẩn hóa** (mL/min/1.73m²)
        - ✅ Công thức **CKD-EPI** (khuyến cáo nhất)
        - ❌ KHÔNG dùng CrCl để phân loại CKD
        
        **2. Điều chỉnh liều thuốc:**
        - ✅ Dùng **GFR tuyệt đối** (mL/min) hoặc **CrCl**
        - ✅ Chuyển đổi: GFR tuyệt đối = eGFR × (BSA / 1.73)
        - ✅ Béo phì: Dùng **Cockcroft-Gault với ABW**
        - ⚠️ Luôn tra cứu liều chính xác cho từng thuốc cụ thể
        
        **3. Bệnh nhân đặc biệt:**
        - **Béo phì:** Cockcroft-Gault + ABW
        - **Gầy/Suy dinh dưỡng:** Cân nhắc Cystatin C eGFR
        - **Cụt chi:** Điều chỉnh BSA
        - **Bệnh nhân lọc máu:** KHÔNG tính eGFR
        - **Bệnh nhân thận nhân tạo chu kỳ:** Đo CrCl 24h
        
        **4. Hội chẩn chuyên khoa:**
        - eGFR < 30 mL/min/1.73m² → Hội chẩn thận học
        - eGFR < 45 mL/min/1.73m² + có triệu chứng → Hội chẩn thận học
        - Điều chỉnh liều thuốc phức tạp → Hội chẩn dược sĩ
        """)


def render_summary_info():
    """Render summary info at the bottom"""
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng (Tóm tắt):**
    
    **1. Chẩn đoán CKD:** Dùng eGFR chuẩn hóa (CKD-EPI)
    
    **2. Điều chỉnh liều thuốc:** Dùng GFR tuyệt đối hoặc CrCl
    
    **3. Béo phì:** Ưu tiên Cockcroft-Gault với ABW
    
    **4. Chuyển đổi:** GFR_absolute = eGFR × (BSA / 1.73)
    
    **5. Luôn tra cứu** liều chính xác cho từng thuốc
    
    **6. Hội chẩn** dược sĩ/thận nếu eGFR < 30 hoặc < 45 + có triệu chứng
    """)

