"""
Acute Cholecystitis / Cholangitis Protocol
Tokyo Guidelines 2018
Management of acute cholecystitis and cholangitis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Cholecystitis / Cholangitis Protocol"""
    st.subheader("🫀 Acute Cholecystitis / Cholangitis")
    st.caption("Tokyo Guidelines 2018 - Management of acute cholecystitis and cholangitis")
    
    st.warning("""
    **⚠️ ACUTE CHOLECYSTITIS / CHOLANGITIS = URGENT ASSESSMENT REQUIRED**
    
    **Triệu chứng:**
    - Đau bụng hạ sườn phải
    - Sốt, ớn lạnh
    - Buồn nôn, nôn
    - Vàng da (cholangitis)
    - Murphy's sign dương tính (cholecystitis)
    
    **Cần điều trị sớm để tránh biến chứng!**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: SELECTION ==========
    st.markdown("### 📊 Chọn Bệnh")
    
    condition = st.radio(
        "**Bệnh:**",
        ["Acute Cholecystitis", "Acute Cholangitis"],
        key="cholecystitis_cholangitis"
    )
    
    st.markdown("---")
    
    if condition == "Acute Cholecystitis":
        render_cholecystitis_protocol()
    else:
        render_cholangitis_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 2: TOKYO GUIDELINES ==========
    st.markdown("### 📋 Tokyo Guidelines 2018")
    
    with st.expander("🔍 Xem tiêu chuẩn Tokyo Guidelines", expanded=False):
        st.markdown("""
        **Acute Cholecystitis - Diagnostic Criteria:**
        
        **A. Local signs of inflammation:**
        - Murphy's sign
        - Mass/pain/tenderness in RUQ
        
        **B. Systemic signs of inflammation:**
        - Fever
        - Elevated WBC
        - Elevated CRP
        
        **C. Imaging findings:**
        - Thickening of GB wall
        - Distension of GB
        - Pericholecystic fluid
        
        **Diagnosis:** A + C, hoặc A + B
        
        **Severity Grading:**
        - **Grade I (Mild):** No organ dysfunction
        - **Grade II (Moderate):** Organ dysfunction
        - **Grade III (Severe):** Organ failure
        
        **Acute Cholangitis - Diagnostic Criteria:**
        
        **A. Systemic inflammation:**
        - Fever and/or chills
        - Elevated WBC or CRP
        
        **B. Cholestasis:**
        - Jaundice
        - Elevated ALP, GGT, bilirubin
        
        **C. Imaging:**
        - Biliary dilatation
        - Evidence of etiology (stone, stricture, etc.)
        
        **Diagnosis:** A + B + C (Charcot's triad), hoặc A + C, hoặc B + C
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: REFERENCES ==========
    render_references_section(get_references("cholecystitis_cholangitis"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_cholecystitis_protocol():
    """Acute Cholecystitis Protocol"""
    st.error("## 🚨 ACUTE CHOLECYSTITIS")
    
    st.markdown("### ⚡ Xử Trí Ban Đầu")
    
    st.markdown("""
    **1. Resuscitation:**
    - **Fluid:** NS/LR 1-2 L nếu cần
    - **Pain control:** Morphine 2-5 mg IV hoặc Fentanyl 50-100 mcg IV
    - **NPO:** Không ăn uống
    
    **2. Antibiotics:**
    - **Grade I (Mild):**
      - **Cefazolin:** 1-2 g IV q8h
      - **Ceftriaxone:** 1-2 g IV q24h
    - **Grade II (Moderate):**
      - **Piperacillin-tazobactam:** 4.5 g IV q8h
      - **Ceftriaxone + Metronidazole:** 1-2 g IV q24h + 500 mg IV q8h
    - **Grade III (Severe):**
      - **Meropenem:** 1 g IV q8h
      - **Imipenem-cilastatin:** 500 mg IV q6h
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔪 Surgical Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Grade I (Mild):**
        - **Early cholecystectomy:** Trong vòng 72 giờ
        - **Laparoscopic:** Ưu tiên
        - **Open:** Nếu không thể laparoscopic
        
        **Grade II (Moderate):**
        - **Early cholecystectomy:** Trong vòng 72 giờ
        - **Laparoscopic:** Có thể
        - **Open:** Cân nhắc nếu phức tạp
        """)
    
    with col2:
        st.markdown("""
        **Grade III (Severe):**
        - **Percutaneous cholecystostomy:** Trước
        - **Cholecystectomy:** Sau khi ổn định
        - **Timing:** 2-3 tháng sau
        
        **Contraindications to early surgery:**
        - Unstable hemodynamics
        - Severe organ failure
        - High surgical risk
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Monitoring")
    
    st.markdown("""
    **Theo dõi sát:**
    - **Vital signs:** BP, HR, Temp, SpO₂
    - **Labs:** WBC, CRP, LFTs, bilirubin
    - **Clinical exam:** Murphy's sign, RUQ tenderness
    - **Imaging:** US/CT nếu cần
    
    **Dấu hiệu xấu đi:**
    - Tăng sốt, ớn lạnh
    - Tăng WBC, CRP
    - Peritonitis
    - Organ dysfunction
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Early cholecystectomy (< 72h) tốt hơn delayed
    - Laparoscopic ưu tiên nếu có thể
    - Percutaneous cholecystostomy cho Grade III
    - Theo dõi sát để phát hiện biến chứng
    """)


def render_cholangitis_protocol():
    """Acute Cholangitis Protocol"""
    st.error("## 🚨 ACUTE CHOLANGITIS")
    
    st.markdown("### ⚡ Xử Trí Ban Đầu")
    
    st.markdown("""
    **1. Resuscitation:**
    - **Fluid:** NS/LR 1-2 L nếu cần
    - **Vasopressors:** Nếu shock
    - **NPO:** Không ăn uống
    
    **2. Antibiotics:**
    - **Mild:**
      - **Ceftriaxone:** 1-2 g IV q24h
      - **Cefotaxime:** 1-2 g IV q8h
    - **Moderate/Severe:**
      - **Piperacillin-tazobactam:** 4.5 g IV q8h
      - **Meropenem:** 1 g IV q8h
      - **Imipenem-cilastatin:** 500 mg IV q6h
    - **Coverage:** Gram-negative, anaerobes
    
    **3. Biliary Drainage:**
    - **ERCP:** Ưu tiên (có thể điều trị nguyên nhân)
    - **PTC:** Nếu ERCP thất bại
    - **Surgical:** Nếu không thể can thiệp
    - **Timing:** Càng sớm càng tốt (trong vòng 24-48h)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔪 Endoscopic/Surgical Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **ERCP:**
        - **Sphincterotomy:** Mở cơ vòng Oddi
        - **Stone extraction:** Lấy sỏi
        - **Stenting:** Đặt stent nếu cần
        - **Timing:** Trong vòng 24-48h
        
        **PTC:**
        - **Percutaneous drainage:** Dẫn lưu qua da
        - **Chỉ định:** Nếu ERCP thất bại
        """)
    
    with col2:
        st.markdown("""
        **Surgical:**
        - **Choledochotomy:** Mở ống mật chủ
        - **T-tube:** Đặt ống T
        - **Chỉ định:** Nếu không thể can thiệp
        - **Timing:** Sau khi ổn định
        
        **Complications:**
        - Perforation
        - Bleeding
        - Pancreatitis
        - Infection
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Monitoring")
    
    st.markdown("""
    **Theo dõi sát:**
    - **Vital signs:** BP, HR, Temp, SpO₂
    - **Labs:** WBC, CRP, LFTs, bilirubin, amylase
    - **Clinical exam:** RUQ tenderness, jaundice
    - **Imaging:** US/CT/MRCP nếu cần
    
    **Dấu hiệu xấu đi:**
    - Tăng sốt, ớn lạnh
    - Tăng WBC, CRP
    - Tăng bilirubin
    - Organ dysfunction
    - Peritonitis
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Biliary drainage là điều trị chính
    - ERCP ưu tiên nếu có thể
    - Timing quan trọng (trong vòng 24-48h)
    - Theo dõi sát để phát hiện biến chứng
    - Charcot's triad: Fever, RUQ pain, Jaundice
    - Reynolds' pentad: Charcot's triad + Shock + Altered mental status
    """)

