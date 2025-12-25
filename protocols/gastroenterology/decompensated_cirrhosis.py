"""
Decompensated Cirrhosis Protocol
AASLD Guidelines 2024, EASL Guidelines 2024
Advanced cirrhosis with complications
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Decompensated Cirrhosis Management Protocol"""
    st.subheader("🫀 Xơ Gan Mất Bù (Decompensated Cirrhosis)")
    st.caption("AASLD Guidelines 2024, EASL Guidelines 2024 - Advanced cirrhosis")
    
    st.error("""
    **⚠️ XƠ GAN MẤT BÙ = BỆNH NẶNG - TỬ VONG CAO**
    
    **Định nghĩa:**
    - Xơ gan với biến chứng
    - Mất bù chức năng gan
    
    **Biến chứng:**
    - **Cổ trướng (Ascites):** (phổ biến nhất)
    - **Xuất huyết tiêu hóa:** (varices)
    - **Hôn mê gan (Hepatic Encephalopathy):** (20-30%)
    - **Hội chứng gan thận (HRS):** (10-20%)
    - **Nhiễm trùng:** SBP, pneumonia
    - **Ung thư gan:** (HCC)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Đánh giá Biến chứng")
    
    complication = st.radio(
        "**Biến chứng hiện tại:**",
        [
            "Cổ trướng (Ascites)",
            "Xuất huyết tiêu hóa (Variceal Bleeding)",
            "Hôn mê gan (Hepatic Encephalopathy)",
            "Hội chứng gan thận (Hepatorenal Syndrome)",
            "Nhiễm trùng (SBP, Pneumonia)",
            "Nhiều biến chứng"
        ],
        key="cirrhosis_complication"
    )
    
    st.markdown("---")
    
    if "Cổ trướng" in complication:
        render_ascites()
    elif "Xuất huyết" in complication:
        render_variceal_bleeding()
    elif "Hôn mê" in complication:
        render_hepatic_encephalopathy()
    elif "Hội chứng gan thận" in complication:
        st.info("Xem protocol **Hội Chứng Gan Thận** trong chuyên khoa Thận")
    elif "Nhiễm trùng" in complication:
        render_infection()
    else:
        render_multiple_complications()
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Tổng quát")
    
    st.info("""
    **1. Điều trị Nguyên nhân:**
    - **Viêm gan B:** Entecavir, Tenofovir
    - **Viêm gan C:** DAA therapy
    - **Rượu:** Cai rượu
    - **NAFLD:** Giảm cân, điều trị đái tháo đường
    
    **2. Điều trị Biến chứng:**
    - Theo từng biến chứng
    - Xem các protocol riêng
    
    **3. Monitoring:**
    - **LFTs:** ALT, AST, Bilirubin, Albumin, INR
    - **Creatinine, BUN:** (suy thận)
    - **CBC:** (thiếu máu, giảm tiểu cầu)
    - **Triệu chứng:** Mỗi ngày
    
    **4. Liver Transplant:**
    - **Chỉ định:** Nếu có thể
    - **MELD Score:** Đánh giá ưu tiên
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Decompensated Cirrhosis")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **AASLD Guidelines 2024** - American Association for the Study of Liver Diseases
        2. **EASL Guidelines 2024** - European Association for the Study of the Liver
        3. **UpToDate:** Decompensated Cirrhosis - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_ascites():
    """Ascites"""
    st.warning("## ⚠️ CỔ TRƯỚNG")
    
    st.markdown("""
    **Điều trị:**
    
    **1. Diuretics:**
    - **Spironolactone:** 100-400 mg/ngày PO
    - **Furosemide:** 40-160 mg/ngày PO
    - **Tỷ lệ:** Spironolactone:Furosemide = 100:40
    
    **2. Paracentesis:**
    - **Chỉ định:** Nếu cổ trướng lớn, khó thở
    - **Albumin:** 6-8 g/L dịch rút ra
    
    **3. TIPS:**
    - **Chỉ định:** Nếu cổ trướng kháng trị
    - **Lưu ý:** Có thể gây hôn mê gan
    """)


def render_variceal_bleeding():
    """Variceal Bleeding"""
    st.error("## 🚨 XUẤT HUYẾT DO VARICES - CẤP CỨU")
    
    st.markdown("""
    **Điều trị:**
    
    **1. Resuscitation:**
    - Truyền máu: PRBC 2-4 đơn vị
    - Truyền dịch: NS 1000-2000 mL
    
    **2. Vasoactive Drugs:**
    - **Octreotide:** 50 mcg IV bolus, sau đó 50 mcg/h
    - **Hoặc:** Terlipressin 2 mg IV q4h
    
    **3. Endoscopy:**
    - **Cấp cứu:** Trong 12h
    - **Variceal banding:** (ưu tiên)
    - **Hoặc:** Sclerotherapy
    
    **4. Antibiotics:**
    - **Ceftriaxone:** 1 g IV q24h
    - **Hoặc:** Norfloxacin 400 mg PO bid
    - **Mục đích:** Phòng ngừa SBP
    """)


def render_hepatic_encephalopathy():
    """Hepatic Encephalopathy"""
    st.warning("## ⚠️ HÔN MÊ GAN")
    
    st.markdown("""
    **Điều trị:**
    
    **1. Lactulose:**
    - **Liều:** 30-45 mL PO tid-qid
    - **Mục tiêu:** 2-3 lần đi tiêu/ngày
    
    **2. Rifaximin:**
    - **Liều:** 550 mg PO bid
    - **Mục đích:** Giảm ammonia
    
    **3. Điều trị Nguyên nhân:**
    - Nhiễm trùng
    - Xuất huyết
    - Rối loạn điện giải
    - Táo bón
    """)


def render_infection():
    """Infection"""
    st.error("## 🚨 NHIỄM TRÙNG")
    
    st.markdown("""
    **SBP (Spontaneous Bacterial Peritonitis):**
    - **Ceftriaxone:** 2 g IV q24h
    - **Hoặc:** Cefotaxime 2 g IV q8h
    - **Albumin:** 1.5 g/kg ngày 1, 1 g/kg ngày 3
    
    **Pneumonia:**
    - Kháng sinh phù hợp
    - Theo protocol viêm phổi
    """)


def render_multiple_complications():
    """Multiple Complications"""
    st.error("## 🚨🚨 NHIỀU BIẾN CHỨNG - ICU")
    
    st.markdown("""
    **Điều trị:**
    - ICU
    - Điều trị từng biến chứng
    - Monitoring sát
    - Cân nhắc liver transplant
    """)

