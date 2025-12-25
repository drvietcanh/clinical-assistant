"""
Hepatorenal Syndrome Protocol
KDIGO Guidelines 2024, AASLD Guidelines 2024
Life-threatening complication of cirrhosis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Hepatorenal Syndrome Management Protocol"""
    st.subheader("🧪 Hội Chứng Gan Thận (Hepatorenal Syndrome)")
    st.caption("KDIGO Guidelines 2024, AASLD Guidelines 2024 - Life-threatening complication")
    
    st.error("""
    **⚠️ HỘI CHỨNG GAN THẬN = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - Suy thận cấp ở bệnh nhân xơ gan
    - Không có nguyên nhân thận khác
    - Cải thiện với điều trị hoặc ghép gan
    
    **Phân loại:**
    - **Type 1:** Suy thận cấp nhanh (tăng creatinine gấp đôi trong <2 tuần)
    - **Type 2:** Suy thận mạn tính (tiến triển chậm hơn)
    
    **Tiêu chuẩn Chẩn đoán:**
    - Xơ gan với cổ trướng
    - Creatinine tăng (≥1.5 mg/dL hoặc tăng ≥50%)
    - Không cải thiện sau ngừng diuretics và truyền dịch
    - Không có nguyên nhân thận khác
    - Protein niệu <500 mg/ngày
    - Không có tắc nghẽn đường tiểu
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức (hôn mê gan)
        - Suy hô hấp
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **Albumin:** 1 g/kg/ngày (tối đa 100 g/ngày)
        - **Thận trọng:** Quá tải dịch
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị thuốc
        
        **4. LABS NGAY:**
        - **Creatinine, BUN:** (đánh giá suy thận)
        - **Na, K, Mg:** (điện giải)
        - **Bilirubin, ALT, AST:** (chức năng gan)
        - **INR:** (đông máu)
        - **Albumin:** (protein)
        - **Urine analysis:** (loại trừ nguyên nhân khác)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán (IC-AKI/HRS):**
    
    **1. Xơ gan với cổ trướng:**
    - Có
    
    **2. Creatinine:**
    - ≥1.5 mg/dL
    - Hoặc tăng ≥50% từ baseline
    
    **3. Không cải thiện sau:**
    - Ngừng diuretics ≥2 ngày
    - Truyền albumin 1 g/kg/ngày ≥2 ngày
    
    **4. Loại trừ:**
    - Shock
    - Nhiễm trùng (SBP)
    - Thuốc độc thận
    - Tắc nghẽn đường tiểu
    - Bệnh thận khác
    
    **5. Protein niệu:**
    - <500 mg/ngày
    
    **6. Hồng cầu niệu:**
    - <50/HPF
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Đặc hiệu")
    
    st.error("## 🚨 VASOCONSTRICTORS + ALBUMIN - ĐIỀU TRỊ CHÍNH")
    
    st.success("""
    **1. ALBUMIN (Thuốc đầu tay)**
    
    **Liều:**
    - **Ngày 1:** 1 g/kg (tối đa 100 g)
    - **Ngày 2-14:** 20-40 g/ngày
    - **Mục đích:** Tăng thể tích tuần hoàn hiệu quả
    
    **2. VASOCONSTRICTORS (Thuốc chính)**
    
    **Terlipressin (Ưu tiên - nếu có):**
    - **Liều:** 1-2 mg IV mỗi 4-6h
    - **Hoặc:** 0.5-2 mg/h IV liên tục
    - **Hiệu quả:** 40-50% đáp ứng
    - **Thời gian:** 3-14 ngày
    
    **Hoặc Midodrine + Octreotide:**
    - **Midodrine:** 7.5-12.5 mg PO tid
    - **Octreotide:** 100-200 mcg SC tid
    - **Hoặc:** 25-50 mcg/h IV liên tục
    - **Hiệu quả:** 30-40% đáp ứng
    
    **Hoặc Norepinephrine:**
    - **Liều:** 0.5-3 mcg/kg/min IV
    - **Hiệu quả:** Tương tự terlipressin
    
    **Mục tiêu:**
    - Creatinine giảm <1.5 mg/dL
    - Hoặc giảm ≥50% từ baseline
    - Cải thiện trong 3-7 ngày
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Ngừng Diuretics:**
    - Ngừng tất cả diuretics
    - Theo dõi cổ trướng
    
    **2. Điều trị Nhiễm trùng:**
    - **SBP:** Kháng sinh (Cefotaxime, Ceftriaxone)
    - **Nhiễm trùng khác:** Điều trị phù hợp
    
    **3. Điều trị Xuất huyết:**
    - **GI bleeding:** Điều trị theo protocol
    - **Truyền máu:** Nếu cần
    
    **4. Lọc máu:**
    - **Chỉ định:** Nếu suy thận nặng, không đáp ứng
    - **Hoặc:** Bridge to liver transplant
    - **Lưu ý:** Không cải thiện tiên lượng
    
    **5. Liver Transplant:**
    - **Chỉ định:** Nếu có thể
    - **Lưu ý:** Cải thiện tiên lượng tốt nhất
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Chống chỉ định & Lưu ý")
    
    st.warning("""
    **Chống chỉ định Vasoconstrictors:**
    - Bệnh mạch vành
    - Bệnh mạch máu ngoại vi
    - Tăng huyết áp nặng
    - Rối loạn nhịp tim
    
    **Lưu ý:**
    - **Terlipressin:** Có thể gây thiếu máu cục bộ
    - **Midodrine:** Cần theo dõi huyết áp
    - **Norepinephrine:** Cần monitoring sát
    
    **Theo dõi:**
    - Huyết áp, HR (mỗi 1-2h)
    - Creatinine (mỗi ngày)
    - Triệu chứng thiếu máu cục bộ
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Type 1:** Tử vong 50-80% trong 1 tháng
    - **Type 2:** Tử vong 50-60% trong 6 tháng
    - **Yếu tố nguy cơ:**
      - Chậm trễ điều trị
      - Nhiễm trùng
      - Xuất huyết
      - Hôn mê gan
    
    **Theo dõi:**
    - **Creatinine:** Mỗi ngày (cho đến khi cải thiện)
    - **BUN:** Mỗi ngày
    - **Huyết áp, HR:** Mỗi 1-2h
    - **Triệu chứng:** Mỗi ngày
    
    **Đáp ứng:**
    - **Tốt:** Creatinine <1.5 mg/dL trong 7-14 ngày
    - **Một phần:** Creatinine giảm nhưng không <1.5
    - **Không đáp ứng:** Creatinine không giảm
    
    **Xuất viện:**
    - Creatinine ổn định
    - Không triệu chứng
    - Đã điều chỉnh thuốc
    - Theo dõi ít nhất 1-2 tuần
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Hepatorenal Syndrome")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **KDIGO Guidelines 2024** - Kidney Disease: Improving Global Outcomes
        2. **AASLD Guidelines 2024** - American Association for the Study of Liver Diseases
        3. **UpToDate:** Hepatorenal Syndrome - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

