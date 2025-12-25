"""
Chorioamnionitis Protocol
ACOG Guidelines 2024, UpToDate 2024
Intra-amniotic infection requiring urgent delivery
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Chorioamnionitis Management Protocol"""
    st.subheader("🤰 Nhiễm Trùng Ối (Chorioamnionitis)")
    st.caption("ACOG Guidelines 2024, UpToDate 2024 - Intra-amniotic infection")
    
    st.error("""
    **⚠️ NHIỄM TRÙNG ỐI = CẤP CỨU SẢN KHOA - CẦN LẤY THAI NGAY**
    
    **Định nghĩa:**
    - Nhiễm trùng màng ối và nước ối
    - Có thể gây nhiễm trùng cho mẹ và thai nhi
    - Cần lấy thai và điều trị kháng sinh
    
    **Triệu chứng:**
    - Sốt ≥38°C
    - Đau bụng dưới
    - Nhịp tim thai nhanh (>160 bpm)
    - Dịch tiết âm đạo có mùi hôi
    - Tử cung đau khi sờ
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **FHR monitoring:** (nếu có thể)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 500-1000 mL bolus (nếu hạ HA)
        """)
    
    with col2:
        st.warning("""
        **3. FETAL MONITORING**
        
        - **Continuous FHR:** (nếu có thể)
        - **Đánh giá:** Tình trạng thai nhi
        
        **4. LABS NGAY:**
        - **CBC:** WBC, Neutrophils
        - **BMP:** Creatinine, Electrolytes
        - **Blood cultures:** (nếu sốt)
        - **Amniotic fluid:** (nếu có thể)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    
    **1. Sốt:**
    - ≥38°C (≥100.4°F)
    - Đo 2 lần cách nhau ≥30 phút
    
    **2. VÀ một trong các dấu hiệu:**
    - Nhịp tim thai nhanh (>160 bpm)
    - Tử cung đau khi sờ
    - Dịch tiết âm đạo có mùi hôi
    - WBC tăng (>15,000/μL)
    - CRP tăng
    
    **3. Xét nghiệm:**
    - **CBC:** WBC tăng, Neutrophils tăng
    - **CRP:** Tăng
    - **Blood cultures:** (nếu sốt)
    - **Amniotic fluid:** (nếu có thể, Gram stain, culture)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.error("## 🚨 ĐIỀU TRỊ CẤP CỨU - LẤY THAI NGAY")
    
    st.success("""
    **1. ANTIBIOTICS - Bắt đầu NGAY:**
    
    **Ampicillin + Gentamicin (Ưu tiên):**
    - **Ampicillin:** 2 g IV q6h
    - **Gentamicin:** 5 mg/kg IV q24h (hoặc 2 mg/kg loading, sau đó 1.5 mg/kg q8h)
    
    **Hoặc:**
    - **Ampicillin-Sulbactam:** 3 g IV q6h
    - **Hoặc:** Cefotetan 2 g IV q12h
    - **Hoặc:** Cefoxitin 2 g IV q8h
    
    **2. DELIVERY (Lấy thai) - Cấp cứu:**
    
    **Chỉ định:**
    - Tất cả bệnh nhân chorioamnionitis
    - **Không chờ:** Corticosteroids
    - **Cấp cứu:** Lấy thai ngay
    
    **Phương pháp:**
    - **C-section:** (ưu tiên, nhanh)
    - **Hoặc:** Induction (nếu có thể)
    
    **3. Postpartum Antibiotics:**
    - Tiếp tục 24-48h sau lấy thai
    - Hoặc cho đến khi hết sốt 24h
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Antipyretics:**
    - **Acetaminophen:** 650-1000 mg PO/IV q4-6h
    - **Mục đích:** Giảm sốt
    
    **2. Monitoring:**
    - **Mẹ:** BP, HR, nhiệt độ mỗi 1-2h
    - **Thai:** FHR mỗi 15-30 phút
    - **Labs:** WBC, CRP mỗi 12-24h
    
    **3. Complications:**
    - Nhiễm trùng huyết
    - Nhiễm trùng vết mổ
    - Nhiễm trùng thai nhi
    - Suy thai
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Thai nhi")
    
    st.warning("""
    **1. Sau khi lấy thai:**
    - **Đánh giá:** Tình trạng thai nhi
    - **Blood cultures:** (nếu nghi ngờ nhiễm trùng)
    - **CBC, CRP:** (nếu nghi ngờ nhiễm trùng)
    
    **2. Antibiotics cho thai nhi:**
    - **Nếu nghi ngờ nhiễm trùng:**
      - **Ampicillin:** 50-100 mg/kg IV q12h
      - **Gentamicin:** 2.5 mg/kg IV q12h
    - **Thời gian:** 7-10 ngày
    
    **3. Monitoring:**
    - Nhiệt độ, HR, RR
    - Triệu chứng nhiễm trùng
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Mẹ:** Tốt nếu điều trị sớm
    - **Thai:** Phụ thuộc vào tuổi thai và thời gian nhiễm trùng
    - **Yếu tố nguy cơ:**
      - Chậm trễ lấy thai
      - Nhiễm trùng nặng
      - Tuổi thai non
    
    **Theo dõi:**
    - **Mẹ:** Nhiệt độ, BP, HR mỗi 1-2h
    - **Labs:** WBC, CRP mỗi 12-24h
    - **Triệu chứng:** Mỗi 1-2h
    
    **Cải thiện:**
    - Hết sốt trong 24-48h
    - WBC giảm
    - Triệu chứng cải thiện
    
    **Xuất viện:**
    - Hết sốt ≥24h
    - WBC cải thiện
    - Không triệu chứng
    - Theo dõi ít nhất 48-72h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Chorioamnionitis")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACOG Guidelines 2024** - American College of Obstetricians and Gynecologists
        2. **UpToDate:** Chorioamnionitis - Last updated 2024
        3. **Obstetrics & Gynecology** - Chorioamnionitis Management
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")




