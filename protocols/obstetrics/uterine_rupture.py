"""
Uterine Rupture Protocol
ACOG Guidelines 2024, UpToDate 2024
Life-threatening obstetric emergency
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Uterine Rupture Management Protocol"""
    st.subheader("🤰 Vỡ Tử Cung (Uterine Rupture)")
    st.caption("ACOG Guidelines 2024, UpToDate 2024 - Life-threatening obstetric emergency")
    
    st.error("""
    **⚠️ VỠ TỬ CUNG = CẤP CỨU SẢN KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - Vỡ thành tử cung
    - Có thể gây xuất huyết nặng
    - Có thể gây tử vong mẹ và thai nhi
    
    **Triệu chứng:**
    - Đau bụng đột ngột, dữ dội
    - Xuất huyết âm đạo
    - Nhịp tim thai bất thường hoặc mất
    - Shock
    - Có thể có khối máu tụ trong ổ bụng
    
    **Nguyên nhân:**
    - Tiền sử mổ lấy thai
    - Chấn thương
    - Sử dụng oxytocin quá mức
    - Đẻ khó
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
        - **NS:** 2000 mL bolus
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
    - Xuất huyết âm đạo
    - Nhịp tim thai bất thường hoặc mất
    - Shock
    - Có thể có khối máu tụ trong ổ bụng
    
    **Xét nghiệm:**
    - **Ultrasound:** (có thể thấy khối máu tụ)
    - **CBC:** Hct, Hb giảm nhanh
    - **Coagulation:** Có thể rối loạn (DIC)
    - **FHR monitoring:** Bất thường hoặc mất
    
    **Lưu ý:**
    - Chẩn đoán chủ yếu dựa vào lâm sàng
    - Nếu nghi ngờ → Phẫu thuật ngay
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.error("## 🚨🚨 PHẪU THUẬT CẤP CỨU - CHỈ ĐỊNH")
    
    st.success("""
    **1. RESUSCITATION:**
    
    - **Truyền máu:** PRBC 4-6 đơn vị (chuẩn bị)
    - **Truyền dịch:** NS 2000 mL bolus
    - **FFP:** 2-4 đơn vị (nếu rối loạn đông máu)
    - **Platelets:** 1-2 đơn vị (nếu giảm tiểu cầu)
    
    **2. PHẪU THUẬT CẤP CỨU:**
    
    - **Chỉ định:** Tất cả bệnh nhân vỡ tử cung
    - **Cấp cứu:** Phẫu thuật ngay
    - **Không chờ:** Xét nghiệm, imaging
    
    **3. Kỹ thuật:**
    
    - **Lấy thai:** C-section cấp cứu
    - **Sửa chữa tử cung:** (nếu có thể)
    - **Hoặc:** Cắt tử cung (nếu không thể sửa)
    
    **4. Post-operative:**
    
    - **Antibiotics:** Cefazolin 2 g IV
    - **Truyền máu:** Tiếp tục nếu cần
    - **Monitoring:** ICU
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Resuscitation:**
    - **Truyền máu:** PRBC 4-6 đơn vị
    - **Truyền dịch:** NS 2000 mL bolus
    - **FFP:** 2-4 đơn vị
    - **Platelets:** 1-2 đơn vị
    
    **2. Monitoring:**
    - **ICU:** Ít nhất 24-48h
    - **BP, HR:** Mỗi 5-15 phút
    - **Hct, Hb:** Mỗi 2-4h
    - **Coagulation:** Mỗi 2-4h
    
    **3. Complications:**
    - DIC
    - Suy thai/Tử vong thai nhi
    - Xuất huyết nặng
    - Tử vong mẹ
    - Nhiễm trùng
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Cắt Tử Cung")
    
    st.error("## 🚨 CHỈ ĐỊNH CẮT TỬ CUNG")
    
    st.markdown("""
    **Chỉ định:**
    - Không thể sửa chữa tử cung
    - Xuất huyết không kiểm soát được
    - Tổn thương nặng
    
    **Lưu ý:**
    - Cắt tử cung có thể cứu sống mẹ
    - Nhưng mất khả năng sinh sản
    - Cần thảo luận với gia đình (nếu có thể)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Mẹ:** Tử vong 1-5% (nếu điều trị sớm)
    - **Thai:** Tử vong 10-30%
    - **Yếu tố nguy cơ:**
      - Chậm trễ phẫu thuật
      - Xuất huyết nặng
      - DIC
    
    **Theo dõi:**
    - **ICU:** Ít nhất 24-48h
    - **BP, HR:** Mỗi 5-15 phút
    - **Hct, Hb:** Mỗi 2-4h
    - **Coagulation:** Mỗi 2-4h
    
    **Xuất viện:**
    - Ổn định sau phẫu thuật
    - Hct, Hb ổn định
    - Không biến chứng
    - Theo dõi ít nhất 48-72h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Uterine Rupture")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACOG Guidelines 2024** - American College of Obstetricians and Gynecologists
        2. **UpToDate:** Uterine Rupture - Last updated 2024
        3. **Obstetrics & Gynecology** - Uterine Rupture Management
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")




