"""
Acute Hepatitis (Non-viral) Protocol
AASLD 2017, EASL 2019 Guidelines
Management of acute hepatitis (drug-induced, autoimmune, ischemic, toxins)
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Hepatitis (Non-viral) Protocol"""
    st.subheader("🫀 Acute Hepatitis (Non-viral) Protocol")
    st.caption("AASLD 2017, EASL 2019 - Management of acute hepatitis (non-viral causes)")
    
    st.warning("""
    **⚠️ ACUTE HEPATITIS (NON-VIRAL) = URGENT ASSESSMENT REQUIRED**
    
    **Định nghĩa:**
    - Tăng ALT/AST >2x ULN
    - Khởi phát cấp tính (<6 tháng)
    - Loại trừ viêm gan virus (A, B, C, E)
    - Có thể tiến triển thành ALF nếu không điều trị
    
    **Nguyên nhân thường gặp:**
    - Drug-Induced Liver Injury (DILI)
    - Autoimmune Hepatitis
    - Ischemic Hepatitis
    - Toxins (nấm độc, hóa chất)
    """)
    
    st.markdown("---")
    
    # Etiology selection
    etiology = st.radio(
        "**Nguyên nhân nghi ngờ:**",
        ["Drug-Induced Liver Injury (DILI)", "Autoimmune Hepatitis", "Ischemic Hepatitis", "Toxin-Induced", "Chưa xác định"],
        key="hepatitis_etiology"
    )
    
    st.markdown("---")
    
    if "DILI" in etiology or "Drug-Induced" in etiology:
        render_dili()
    elif "Autoimmune" in etiology:
        render_autoimmune_hepatitis()
    elif "Ischemic" in etiology:
        render_ischemic_hepatitis()
    elif "Toxin" in etiology:
        render_toxin_hepatitis()
    else:
        render_unknown_hepatitis()


def render_dili():
    """Drug-Induced Liver Injury Protocol"""
    
    st.error("## 🚨 DRUG-INDUCED LIVER INJURY (DILI) PROTOCOL")
    
    st.markdown("### 1️⃣ Đánh giá Ban Đầu")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Lịch sử Thuốc")
        st.info("""
        **Thuốc thường gây DILI:**
        - **Antibiotics:** Amoxicillin-clavulanate, Flucloxacillin, Nitrofurantoin
        - **NSAIDs:** Diclofenac, Ibuprofen, Naproxen
        - **Antiepileptics:** Valproate, Phenytoin, Carbamazepine
        - **Herbal:** Kava, Comfrey, Green tea extract
        - **Statins:** Atorvastatin, Simvastatin
        - **Antifungals:** Ketoconazole, Fluconazole
        """)
        
        drug_name = st.text_input("**Tên thuốc nghi ngờ:**", key="dili_drug")
        time_to_onset = st.number_input("**Thời gian từ khi dùng đến khởi phát (ngày):**", min_value=1, max_value=365, value=7, key="dili_onset")
        duration_use = st.number_input("**Thời gian sử dụng (ngày):**", min_value=1, max_value=365, value=7, key="dili_duration")
    
    with col2:
        st.markdown("#### Xét nghiệm")
        alt = st.number_input("**ALT (U/L):**", min_value=0, max_value=10000, value=500, key="dili_alt")
        ast = st.number_input("**AST (U/L):**", min_value=0, max_value=10000, value=400, key="dili_ast")
        bilirubin = st.number_input("**Total Bilirubin (mg/dL):**", min_value=0.0, max_value=50.0, value=2.0, step=0.1, key="dili_bili")
        inr = st.number_input("**INR:**", min_value=0.5, max_value=10.0, value=1.2, step=0.1, key="dili_inr")
        
        # Calculate R-value
        if alt > 0 and ast > 0:
            r_value = alt / ast if ast > 0 else 0
            if r_value >= 5:
                pattern = "Hepatocellular"
            elif r_value <= 2:
                pattern = "Cholestatic"
            else:
                pattern = "Mixed"
            
            st.info(f"**R-value:** {r_value:.2f} → **Pattern:** {pattern}")
    
    st.markdown("---")
    
    # Severity assessment
    st.markdown("### 2️⃣ Đánh giá Mức độ Nặng")
    
    if bilirubin >= 2.5 and inr >= 1.5:
        severity = "Severe"
        st.error("## 🚨 DILI NẶNG - Có thể tiến triển thành ALF")
    elif bilirubin >= 2.5 or inr >= 1.5:
        severity = "Moderate"
        st.warning("## ⚠️ DILI TRUNG BÌNH")
    else:
        severity = "Mild"
        st.success("## ✅ DILI NHẸ")
    
    st.markdown("---")
    
    # Management
    st.markdown("### 3️⃣ Điều trị")
    
    st.markdown("#### 🛑 Bước 1: Ngừng Thuốc Nghi Ngờ")
    st.error("""
    **NGỪNG NGAY LẬP TỨC thuốc nghi ngờ!**
    - Không chờ xác nhận
    - Nếu cần thiết, thay thế bằng thuốc khác an toàn hơn
    - Ghi chú trong hồ sơ: "DILI - Ngừng [tên thuốc]"
    """)
    
    st.markdown("#### 💉 Bước 2: N-Acetylcysteine (NAC)")
    
    if "Acetaminophen" in drug_name or "Paracetamol" in drug_name:
        st.error("""
        **NAC cho Acetaminophen Overdose:**
        - **Loading:** 150 mg/kg trong 15 phút
        - **Maintenance:** 50 mg/kg trong 4 giờ, sau đó 100 mg/kg trong 16 giờ
        - **Tổng thời gian:** 21 giờ
        - **Route:** IV (preferred) hoặc PO
        """)
    else:
        st.info("""
        **NAC cho Non-Acetaminophen DILI:**
        - **Evidence:** Có thể có lợi trong DILI nặng (controversial)
        - **Dosing:** 150 mg/kg loading, sau đó 50-100 mg/kg/day
        - **Consider:** Nếu DILI nặng, tiến triển nhanh
        """)
    
    st.markdown("#### 🏥 Bước 3: Hỗ trợ & Theo dõi")
    
    with st.expander("📋 Xem quy trình hỗ trợ", expanded=True):
        st.markdown("""
        **1. Monitoring:**
        - **LFTs:** ALT, AST, Bilirubin, ALP, GGT - Daily
        - **Coagulation:** PT/INR - Daily
        - **Clinical:** Encephalopathy, bleeding
        
        **2. Supportive Care:**
        - **Fluid:** Duy trì cân bằng dịch
        - **Nutrition:** Đủ calo, protein
        - **Glucose:** Theo dõi và điều chỉnh
        - **Electrolytes:** K⁺, Na⁺, Mg²⁺
        
        **3. Complications:**
        - **Encephalopathy:** Lactulose, rifaximin
        - **Coagulopathy:** Vitamin K, FFP nếu cần
        - **Infection:** Prophylaxis nếu cần
        """)
    
    st.markdown("#### 🔄 Bước 4: Tiên Lượng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Tiên lượng Tốt:**")
        st.success("""
        - ALT/AST giảm >50% trong 7 ngày
        - Bilirubin <2.5 mg/dL
        - INR <1.5
        - Không có encephalopathy
        - Thời gian hồi phục: 2-8 tuần
        """)
    
    with col2:
        st.markdown("**Tiên lượng Xấu:**")
        st.error("""
        - ALT/AST tiếp tục tăng
        - Bilirubin >10 mg/dL
        - INR >2.0
        - Encephalopathy xuất hiện
        - Cần đánh giá transplant
        """)
    
    st.markdown("---")
    
    # References
    render_references_section(get_references("Acute Hepatitis"))


def render_autoimmune_hepatitis():
    """Autoimmune Hepatitis Protocol"""
    
    st.error("## 🚨 AUTOIMMUNE HEPATITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán (Simplified AIH Score):**
    - **ANA hoặc ASMA:** +2
    - **IgG:** >1.1x ULN: +2
    - **Liver histology:** Typical: +2, Compatible: +1
    - **Absence of viral hepatitis:** +2
    - **Score ≥6:** Probable AIH
    - **Score ≥7:** Definite AIH
    """)
    
    st.markdown("### 2️⃣ Điều trị")
    
    st.markdown("#### 💊 Corticosteroids")
    
    st.warning("""
    **Prednisone/Prednisolone:**
    - **Induction:** 40-60 mg/day (hoặc 1 mg/kg/day)
    - **Taper:** Giảm 5-10 mg mỗi 1-2 tuần
    - **Maintenance:** 5-10 mg/day
    - **Duration:** 2-3 năm (hoặc lâu hơn)
    """)
    
    st.markdown("#### 💊 Azathioprine")
    
    st.info("""
    **Azathioprine (Steroid-sparing):**
    - **Dosing:** 1-2 mg/kg/day
    - **Start:** Sau khi ALT giảm với steroids
    - **Monitoring:** CBC (weekly x 1 month, then monthly)
    - **Contraindications:** Thiopurine methyltransferase deficiency
    """)
    
    st.markdown("### 3️⃣ Theo dõi")
    
    st.markdown("""
    - **LFTs:** Weekly x 1 month, then monthly
    - **IgG:** Monthly
    - **Response:** ALT giảm >50% trong 2 tuần
    - **Relapse:** Nếu ALT tăng lại sau khi giảm liều
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Hepatitis"))


def render_ischemic_hepatitis():
    """Ischemic Hepatitis Protocol"""
    
    st.error("## 🚨 ISCHEMIC HEPATITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    st.info("""
    **Đặc điểm:**
    - **ALT/AST:** Tăng rất cao (>1000 U/L) trong 24-48h
    - **Bilirubin:** Thường bình thường hoặc tăng nhẹ
    - **LDH:** Tăng cao (LDH > ALT)
    - **Clinical:** Shock, heart failure, sepsis
    - **Recovery:** Nhanh (ALT giảm >50% trong 3-7 ngày)
    """)
    
    st.markdown("### 2️⃣ Điều trị")
    
    st.warning("""
    **Nguyên tắc:**
    1. **Điều trị nguyên nhân:** Shock, heart failure, sepsis
    2. **Hỗ trợ gan:** Tự hồi phục nếu nguyên nhân được điều trị
    3. **Monitoring:** LFTs daily
    4. **Prognosis:** Tốt nếu nguyên nhân được điều trị sớm
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Hepatitis"))


def render_toxin_hepatitis():
    """Toxin-Induced Hepatitis Protocol"""
    
    st.error("## 🚨 TOXIN-INDUCED HEPATITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Nguyên nhân")
    
    st.warning("""
    **Toxins thường gặp:**
    - **Nấm độc:** Amanita phalloides (Death cap)
    - **Hóa chất:** Carbon tetrachloride, Phosphorus
    - **Thực vật:** Kava, Comfrey, Green tea extract
    - **Kim loại nặng:** Arsenic, Copper
    """)
    
    st.markdown("### 2️⃣ Điều trị")
    
    st.error("""
    **Amanita phalloides:**
    - **Silymarin (Milk thistle):** 20-50 mg/kg/day IV
    - **NAC:** 150 mg/kg loading, then 50 mg/kg q4h
    - **Penicillin G:** 1 million U/kg/day (controversial)
    """)
    
    st.markdown("### 3️⃣ Hỗ trợ")
    
    st.info("""
    - **Supportive care:** Như DILI
    - **Monitoring:** LFTs, coagulation
    - **Transplant:** Nếu tiến triển thành ALF
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Hepatitis"))


def render_unknown_hepatitis():
    """Unknown Etiology Hepatitis Protocol"""
    
    st.warning("## ⚠️ ACUTE HEPATITIS - CHƯA XÁC ĐỊNH NGUYÊN NHÂN")
    
    st.markdown("### 1️⃣ Đánh giá Chẩn đoán")
    
    st.info("""
    **Cần loại trừ:**
    1. **Viral hepatitis:** HAV, HBV, HCV, HEV serology
    2. **DILI:** Lịch sử thuốc chi tiết
    3. **Autoimmune:** ANA, ASMA, IgG, liver biopsy
    4. **Ischemic:** Clinical context, LDH
    5. **Wilson disease:** Ceruloplasmin, 24h urine Cu
    6. **Budd-Chiari:** Doppler US
    """)
    
    st.markdown("### 2️⃣ Điều trị Hỗ trợ")
    
    st.warning("""
    - **Supportive care:** Như DILI
    - **Monitoring:** LFTs daily
    - **Biopsy:** Nếu không rõ nguyên nhân sau 1-2 tuần
    - **Consult:** Hepatology
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Hepatitis"))

