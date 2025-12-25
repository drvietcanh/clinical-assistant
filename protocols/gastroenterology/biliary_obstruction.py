"""
Biliary Obstruction Protocol
ACG Guidelines 2024, AASLD Guidelines 2024
Obstruction of bile ducts requiring intervention
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Biliary Obstruction Management Protocol"""
    st.subheader("🫀 Tắc Mật (Biliary Obstruction)")
    st.caption("ACG Guidelines 2024, AASLD Guidelines 2024 - Bile duct obstruction")
    
    st.error("""
    **⚠️ TẮC MẬT = CẤP CỨU Y KHOA - CẦN CAN THIỆP**
    
    **Định nghĩa:**
    - Tắc nghẽn đường mật
    - Ứ mật → Vàng da, đau bụng
    - Có thể nhiễm trùng (viêm đường mật)
    
    **Nguyên nhân:**
    - **Sỏi mật:** (phổ biến nhất, 40-50%)
    - **Tumor:** (ung thư đường mật, tụy, 20-30%)
    - **Stricture:** (10-20%)
    - **Khác:** Parasites, inflammation
    
    **Triệu chứng:**
    - Vàng da
    - Đau bụng (vùng gan)
    - Sốt (nếu nhiễm trùng)
    - Ngứa
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức (nếu nhiễm trùng nặng)
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
        - **NS:** 500-1000 mL bolus (nếu hạ HA)
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị thuốc
        
        **4. LABS NGAY:**
        - **Bilirubin:** (tăng)
        - **ALT, AST, ALP, GGT:** (tăng)
        - **CBC:** WBC (nếu nhiễm trùng)
        - **Amylase, Lipase:** (nếu viêm tụy)
        - **Coagulation:** (có thể bất thường)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    obstruction_type = st.radio(
        "**Loại tắc mật:**",
        [
            "Sỏi mật (Choledocholithiasis)",
            "Ung thư (Tumor)",
            "Viêm đường mật (Cholangitis)",
            "Stricture",
            "Khác"
        ],
        key="biliary_obstruction_type"
    )
    
    st.markdown("---")
    
    if "Sỏi" in obstruction_type:
        render_choledocholithiasis()
    elif "Ung thư" in obstruction_type:
        render_tumor()
    elif "Viêm đường mật" in obstruction_type:
        render_cholangitis()
    elif "Stricture" in obstruction_type:
        render_stricture()
    else:
        render_other()
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **1. Antibiotics (Nếu nhiễm trùng):**
    
    **Piperacillin-Tazobactam:**
    - **Liều:** 4.5 g IV q6h
    - **Hoặc:** Meropenem 1 g IV q8h
    
    **Hoặc:**
    - **Ceftriaxone:** 2 g IV q24h + Metronidazole 500 mg IV q8h
    
    **2. ERCP (Endoscopic Retrograde Cholangiopancreatography):**
    
    **Chỉ định:**
    - Sỏi mật
    - Stricture
    - Cần can thiệp
    
    **Kỹ thuật:**
    - Sphincterotomy
    - Stone extraction
    - Stent placement
    
    **3. PTC (Percutaneous Transhepatic Cholangiography):**
    
    **Chỉ định:**
    - Nếu ERCP thất bại
    - Hoặc không thể ERCP
    
    **4. Phẫu thuật:**
    
    **Chỉ định:**
    - Nếu ERCP/PTC thất bại
    - Hoặc có chỉ định phẫu thuật
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Biliary Obstruction")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACG Guidelines 2024** - American College of Gastroenterology
        2. **AASLD Guidelines 2024** - American Association for the Study of Liver Diseases
        3. **UpToDate:** Biliary Obstruction - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_choledocholithiasis():
    """Choledocholithiasis"""
    st.warning("## ⚠️ SỎI MẬT")
    
    st.markdown("""
    **Điều trị:**
    
    **1. ERCP:**
    - Sphincterotomy
    - Stone extraction
    - Stent (nếu cần)
    
    **2. Cholecystectomy:**
    - Sau khi ERCP
    - Phòng ngừa tái phát
    
    **3. Monitoring:**
    - Bilirubin, ALT, AST
    - Triệu chứng
    """)


def render_tumor():
    """Tumor Obstruction"""
    st.error("## 🚨 UNG THƯ")
    
    st.markdown("""
    **Điều trị:**
    
    **1. ERCP/PTC:**
    - Stent placement
    - Giảm tắc nghẽn
    
    **2. Phẫu thuật:**
    - Nếu có thể
    - Resection
    
    **3. Hóa trị/Xạ trị:**
    - Nếu có chỉ định
    """)


def render_cholangitis():
    """Cholangitis"""
    st.error("## 🚨 VIÊM ĐƯỜNG MẬT - CẤP CỨU")
    
    st.markdown("""
    **Triệu chứng (Charcot's Triad):**
    - Sốt
    - Đau bụng vùng gan
    - Vàng da
    
    **Thêm (Reynold's Pentad):**
    - Shock
    - Giảm ý thức
    
    **Điều trị:**
    
    **1. Antibiotics:**
    - Piperacillin-Tazobactam 4.5 g IV q6h
    - Hoặc Meropenem 1 g IV q8h
    
    **2. ERCP:**
    - Cấp cứu (trong 24-48h)
    - Giải phóng tắc nghẽn
    
    **3. Monitoring:**
    - ICU nếu nặng
    - Huyết áp, HR
    - WBC, Bilirubin
    """)


def render_stricture():
    """Stricture"""
    st.warning("## ⚠️ STRICTURE")
    
    st.markdown("""
    **Điều trị:**
    
    **1. ERCP:**
    - Dilation
    - Stent placement
    
    **2. Phẫu thuật:**
    - Nếu ERCP thất bại
    - Hoặc stricture lớn
    """)


def render_other():
    """Other Causes"""
    st.info("## ℹ️ NGUYÊN NHÂN KHÁC")
    
    st.markdown("""
    **Điều trị:**
    - Theo nguyên nhân
    - ERCP/PTC nếu cần
    - Phẫu thuật nếu cần
    """)

