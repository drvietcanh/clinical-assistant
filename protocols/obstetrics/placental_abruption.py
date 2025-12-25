"""
Placental Abruption Protocol
ACOG Guidelines 2024, UpToDate 2024
Premature separation of placenta - obstetric emergency
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Placental Abruption Management Protocol"""
    st.subheader("🤰 Nhau Bong Non (Placental Abruption)")
    st.caption("ACOG Guidelines 2024, UpToDate 2024 - Premature separation of placenta")
    
    st.error("""
    **⚠️ NHAU BONG NON = CẤP CỨU SẢN KHOA - NGUY HIỂM CHO MẸ VÀ THAI**
    
    **Định nghĩa:**
    - Bong nhau thai sớm trước khi sinh
    - Có thể gây xuất huyết nặng
    - Có thể gây suy thai
    
    **Triệu chứng:**
    - Đau bụng đột ngột, dữ dội
    - Xuất huyết âm đạo (có thể ẩn)
    - Tử cung cứng, đau
    - Nhịp tim thai bất thường
    - Có thể có shock
    
    **Nguyên nhân:**
    - Chấn thương
    - Tăng huyết áp
    - Hút thuốc
    - Sử dụng cocaine
    - Tiền sử nhau bong non
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức
        - Suy hô hấp
        - Chuẩn bị phẫu thuật
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 5-15 phút
        
        **Truyền dịch:**
        - **NS:** 1000-2000 mL bolus
        - **Mục tiêu:** SBP ≥90 mmHg
        """)
    
    with col2:
        st.warning("""
        **3. FETAL MONITORING**
        
        - **Continuous FHR:** (nếu có thể)
        - **Đánh giá:** Tình trạng thai nhi
        
        **4. LABS NGAY:**
        - **CBC:** Hct, Hb, Platelets
        - **Coagulation:** PT/INR, aPTT, Fibrinogen
        - **Type & Screen:** (chuẩn bị truyền máu)
        - **BMP:** Creatinine, Electrolytes
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    - Đau bụng đột ngột, dữ dội
    - Xuất huyết âm đạo (có thể ẩn)
    - Tử cung cứng, đau
    - Nhịp tim thai bất thường
    - Có thể có shock
    
    **Xét nghiệm:**
    - **Ultrasound:** (có thể thấy khối máu tụ sau nhau)
    - **CBC:** Hct, Hb giảm
    - **Coagulation:** Có thể rối loạn (DIC)
    - **FHR monitoring:** Bất thường
    
    **Lưu ý:**
    - Chẩn đoán chủ yếu dựa vào lâm sàng
    - Ultrasound có thể không thấy
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        [
            "Nhẹ (Mild)",
            "Trung bình (Moderate)",
            "Nặng (Severe)"
        ],
        key="abruption_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_abruption()
    elif "Trung bình" in severity:
        render_moderate_abruption()
    else:
        render_severe_abruption()
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Resuscitation:**
    - **Truyền máu:** PRBC 2-4 đơn vị (nếu cần)
    - **Truyền dịch:** NS 1000-2000 mL bolus
    - **FFP:** Nếu rối loạn đông máu
    - **Platelets:** Nếu giảm tiểu cầu
    
    **2. Monitoring:**
    - **Mẹ:** BP, HR, Hct mỗi 15-30 phút
    - **Thai:** FHR mỗi 15-30 phút
    - **Coagulation:** Mỗi 4-6h (nếu nặng)
    
    **3. Complications:**
    - DIC
    - Suy thai
    - Xuất huyết nặng
    - Tử vong thai nhi
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Delivery (Lấy thai)")
    
    st.error("## 🚨 CHỈ ĐỊNH LẤY THAI")
    
    st.success("""
    **Chỉ định:**
    - Tất cả bệnh nhân nhau bong non
    - **Cấp cứu:** Lấy thai ngay
    
    **Phương pháp:**
    - **C-section:** (ưu tiên, nhanh)
    - **Hoặc:** Induction (nếu có thể, ổn định)
    
    **Lưu ý:**
    - Không chờ corticosteroids
    - Lấy thai càng sớm càng tốt
    - Chuẩn bị truyền máu
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Mẹ:** Tốt nếu điều trị sớm
    - **Thai:** Phụ thuộc vào mức độ và tuổi thai
    - **Tử vong thai nhi:** 10-30% (nếu nặng)
    - **Yếu tố nguy cơ:**
      - Chậm trễ lấy thai
      - Xuất huyết nặng
      - DIC
    
    **Theo dõi:**
    - **ICU:** Nếu nặng
    - **BP, HR:** Mỗi 15-30 phút
    - **Hct, Hb:** Mỗi 4-6h
    - **Coagulation:** Mỗi 4-6h (nếu nặng)
    
    **Xuất viện:**
    - Ổn định sau lấy thai
    - Hct, Hb ổn định
    - Không biến chứng
    - Theo dõi ít nhất 24-48h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Placental Abruption")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACOG Guidelines 2024** - American College of Obstetricians and Gynecologists
        2. **UpToDate:** Placental Abruption - Last updated 2024
        3. **Obstetrics & Gynecology** - Placental Abruption Management
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_abruption():
    """Mild Abruption"""
    st.warning("## ⚠️ NHAU BONG NON NHẸ")
    
    st.markdown("""
    **Đặc điểm:**
    - Xuất huyết nhẹ
    - Đau bụng nhẹ
    - Tử cung không cứng
    - FHR bình thường
    
    **Điều trị:**
    
    **1. Monitoring:**
    - FHR mỗi 15-30 phút
    - BP, HR mỗi 1-2h
    - Hct, Hb mỗi 6-12h
    
    **2. Delivery:**
    - ≥37 tuần: Lấy thai
    - <37 tuần: Theo dõi sát, lấy thai nếu nặng
    """)


def render_moderate_abruption():
    """Moderate Abruption"""
    st.error("## 🚨 NHAU BONG NON TRUNG BÌNH")
    
    st.markdown("""
    **Đặc điểm:**
    - Xuất huyết trung bình
    - Đau bụng
    - Tử cung cứng, đau
    - FHR có thể bất thường
    
    **Điều trị:**
    
    **1. Resuscitation:**
    - Truyền máu: PRBC 1-2 đơn vị
    - Truyền dịch: NS 1000 mL
    
    **2. Delivery:**
    - **Cấp cứu:** Lấy thai ngay
    - **C-section:** (ưu tiên)
    
    **3. Monitoring:**
    - ICU
    - BP, HR mỗi 15-30 phút
    - FHR mỗi 15-30 phút
    """)


def render_severe_abruption():
    """Severe Abruption"""
    st.error("## 🚨🚨 NHAU BONG NON NẶNG - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Xuất huyết nặng
    - Đau bụng dữ dội
    - Tử cung cứng như gỗ
    - FHR bất thường hoặc mất
    - Có thể có shock
    - Có thể có DIC
    
    **Điều trị:**
    
    **1. Resuscitation:**
    - Truyền máu: PRBC 4-6 đơn vị
    - Truyền dịch: NS 2000 mL bolus
    - FFP: 2-4 đơn vị
    - Platelets: Nếu cần
    
    **2. Delivery:**
    - **Cấp cứu:** Lấy thai ngay
    - **C-section:** (ưu tiên, nhanh)
    
    **3. Monitoring:**
    - ICU
    - BP, HR mỗi 5-15 phút
    - Hct, Hb mỗi 2-4h
    - Coagulation mỗi 2-4h
    """)




