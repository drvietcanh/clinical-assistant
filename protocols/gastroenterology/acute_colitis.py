"""
Acute Colitis (Non-IBD) Protocol
ACG 2021, WSES 2020 Guidelines
Management of acute colitis (infectious, ischemic, radiation, drug-induced)
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Colitis (Non-IBD) Protocol"""
    st.subheader("🫀 Acute Colitis (Non-IBD) Protocol")
    st.caption("ACG 2021, WSES 2020 - Management of acute colitis (non-IBD causes)")
    
    st.warning("""
    **⚠️ ACUTE COLITIS (NON-IBD) = URGENT ASSESSMENT REQUIRED**
    
    **Định nghĩa:**
    - Viêm đại tràng cấp tính không phải IBD
    - Triệu chứng: Tiêu chảy, đau bụng, chảy máu trực tràng
    - Cần phân biệt với IBD, C.diff (đã có protocol riêng)
    
    **Nguyên nhân thường gặp:**
    - Infectious colitis (bacterial, viral, parasitic)
    - Ischemic colitis
    - Radiation colitis
    - Drug-induced colitis
    """)
    
    st.markdown("---")
    
    # Etiology selection
    etiology = st.radio(
        "**Nguyên nhân nghi ngờ:**",
        ["Infectious Colitis", "Ischemic Colitis", "Radiation Colitis", "Drug-Induced Colitis", "Chưa xác định"],
        key="colitis_etiology"
    )
    
    st.markdown("---")
    
    if "Infectious" in etiology:
        render_infectious_colitis()
    elif "Ischemic" in etiology:
        render_ischemic_colitis()
    elif "Radiation" in etiology:
        render_radiation_colitis()
    elif "Drug-Induced" in etiology:
        render_drug_induced_colitis()
    else:
        render_unknown_colitis()


def render_infectious_colitis():
    """Infectious Colitis Protocol"""
    
    st.error("## 🚨 INFECTIOUS COLITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Triệu chứng")
        diarrhea = st.number_input("**Số lần tiêu chảy/ngày:**", min_value=0, max_value=20, value=5, key="inf_colitis_diarrhea")
        blood_stool = st.checkbox("**Phân máu**", key="inf_colitis_blood")
        abdominal_pain = st.checkbox("**Đau bụng**", key="inf_colitis_pain")
        fever = st.checkbox("**Sốt >38°C**", key="inf_colitis_fever")
        tenesmus = st.checkbox("**Mót rặn**", key="inf_colitis_tenesmus")
    
    with col2:
        st.markdown("#### Xét nghiệm")
        wbc = st.number_input("**WBC (×10³/μL):**", min_value=0, max_value=50, value=12, key="inf_colitis_wbc")
        crp = st.number_input("**CRP (mg/L):**", min_value=0, max_value=500, value=50, key="inf_colitis_crp")
        stool_culture = st.checkbox("**Cấy phân**", key="inf_colitis_culture")
        stool_pcr = st.checkbox("**PCR phân (multiplex)**", key="inf_colitis_pcr")
    
    st.markdown("### 2️⃣ Tác Nhân Gây Bệnh")
    
    pathogen = st.selectbox(
        "**Tác nhân nghi ngờ:**",
        ["E. coli (EHEC/STEC)", "Campylobacter", "Salmonella", "Shigella", "Yersinia", "Aeromonas", "Plesiomonas", "Viral (Norovirus, Rotavirus)", "Parasitic (Giardia, Entamoeba)", "Chưa xác định"],
        key="inf_colitis_pathogen"
    )
    
    st.markdown("### 3️⃣ Điều trị")
    
    if "E. coli" in pathogen or "EHEC" in pathogen or "STEC" in pathogen:
        st.error("""
        **⚠️ E. coli O157:H7 / STEC:**
        - **KHÔNG dùng kháng sinh** (tăng nguy cơ HUS)
        - **Supportive care:** Hydration, monitoring
        - **Monitor:** HUS (hemolytic uremic syndrome)
        - **Indications for antibiotics:** Chỉ khi có bacteremia
        """)
    elif "Campylobacter" in pathogen:
        st.warning("""
        **Campylobacter Colitis:**
        - **Antibiotics:** Chỉ nếu nặng hoặc kéo dài >7 ngày
        - **Azithromycin:** 500 mg PO qd x 3-5 days
        - **OR Erythromycin:** 500 mg PO qid x 5 days
        - **OR Ciprofloxacin:** 500 mg PO bid x 5 days (nếu sensitive)
        """)
    elif "Salmonella" in pathogen:
        st.warning("""
        **Salmonella Colitis:**
        - **Antibiotics:** Chỉ nếu nặng, trẻ em, người già, hoặc immunocompromised
        - **Ciprofloxacin:** 500 mg PO bid x 5-7 days
        - **OR Azithromycin:** 500 mg PO qd x 5-7 days
        - **OR Ceftriaxone:** 1-2 g IV qd x 5-7 days (nếu nặng)
        """)
    elif "Shigella" in pathogen:
        st.warning("""
        **Shigella Colitis:**
        - **Antibiotics:** Luôn điều trị (giảm thời gian bệnh)
        - **Azithromycin:** 500 mg PO qd x 3 days
        - **OR Ciprofloxacin:** 500 mg PO bid x 3 days
        - **OR Ceftriaxone:** 1-2 g IV qd x 3-5 days (nếu nặng)
        """)
    elif "Viral" in pathogen:
        st.info("""
        **Viral Colitis (Norovirus, Rotavirus):**
        - **Supportive care:** Hydration (oral hoặc IV)
        - **No antibiotics**
        - **Duration:** 1-3 ngày (tự khỏi)
        """)
    elif "Parasitic" in pathogen:
        st.warning("""
        **Parasitic Colitis:**
        - **Giardia:** Metronidazole 500 mg PO tid x 5-7 days
        - **Entamoeba:** Metronidazole 750 mg PO tid x 10 days + Paromomycin
        """)
    else:
        st.info("""
        **Empiric Treatment (nếu nặng):**
        - **Ciprofloxacin:** 500 mg PO bid x 5-7 days
        - **OR Azithromycin:** 500 mg PO qd x 5-7 days
        - **Điều chỉnh theo kết quả cấy phân**
        """)
    
    st.markdown("### 4️⃣ Hỗ trợ")
    
    with st.expander("📋 Xem quy trình hỗ trợ", expanded=True):
        st.markdown("""
        **1. Hydration:**
        - **Oral:** ORS nếu có thể
        - **IV:** NS hoặc LR nếu mất nước nặng
        - **Goal:** UOP >0.5 mL/kg/h
        
        **2. Monitoring:**
        - **Vitals:** q4-6h
        - **Labs:** CBC, electrolytes, creatinine
        - **Stool:** Culture, PCR, O&P
        
        **3. Complications:**
        - **Toxic megacolon:** Rare, cần phẫu thuật
        - **HUS:** Monitor nếu STEC
        - **Bacteremia:** Blood cultures nếu sốt cao
        """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Colitis"))


def render_ischemic_colitis():
    """Ischemic Colitis Protocol"""
    
    st.error("## 🚨 ISCHEMIC COLITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    st.info("""
    **Đặc điểm:**
    - **Triệu chứng:** Đau bụng đột ngột, tiêu chảy máu
    - **Vị trí:** Thường đại tràng trái (splenic flexure, sigmoid)
    - **Risk factors:** Age >60, atherosclerosis, AF, heart failure, shock
    - **Imaging:** CT với contrast (thinning wall, "thumbprinting")
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Risk Factors")
        age = st.number_input("**Tuổi:**", min_value=0, max_value=120, value=70, key="isch_colitis_age")
        af = st.checkbox("**Atrial Fibrillation**", key="isch_colitis_af")
        hf = st.checkbox("**Heart Failure**", key="isch_colitis_hf")
        shock = st.checkbox("**Shock**", key="isch_colitis_shock")
    
    with col2:
        st.markdown("#### Xét nghiệm")
        lactate = st.number_input("**Lactate (mmol/L):**", min_value=0.0, max_value=20.0, value=2.0, step=0.1, key="isch_colitis_lactate")
        wbc = st.number_input("**WBC (×10³/μL):**", min_value=0, max_value=50, value=15, key="isch_colitis_wbc")
        crp = st.number_input("**CRP (mg/L):**", min_value=0, max_value=500, value=100, key="isch_colitis_crp")
    
    st.markdown("### 2️⃣ Phân loại")
    
    if lactate > 4.0 or shock or wbc > 20:
        severity = "Severe"
        st.error("## 🚨 ISCHEMIC COLITIS NẶNG - Cần phẫu thuật")
    elif lactate > 2.0 or wbc > 15:
        severity = "Moderate"
        st.warning("## ⚠️ ISCHEMIC COLITIS TRUNG BÌNH")
    else:
        severity = "Mild"
        st.success("## ✅ ISCHEMIC COLITIS NHẸ")
    
    st.markdown("### 3️⃣ Điều trị")
    
    st.markdown("#### 🏥 Bước 1: Hỗ trợ")
    
    st.warning("""
    **1. NPO (Nothing by mouth):**
    - Nghỉ ăn uống để ruột nghỉ ngơi
    - NGT nếu cần
    
    **2. IV Fluids:**
    - NS hoặc LR
    - Duy trì UOP >0.5 mL/kg/h
    
    **3. Broad-spectrum Antibiotics:**
    - **Piperacillin-tazobactam:** 4.5 g IV q6h
    - **OR Cefepime + Metronidazole**
    - **Duration:** 7-10 days
    """)
    
    st.markdown("#### 🔄 Bước 2: Theo dõi")
    
    st.info("""
    **Monitoring:**
    - **Clinical:** Abdominal exam q4-6h
    - **Labs:** CBC, lactate, LFTs daily
    - **Imaging:** CT nếu triệu chứng xấu đi
    
    **Warning Signs (cần phẫu thuật):**
    - Peritonitis
    - Pneumatosis intestinalis
    - Portal venous gas
    - Free air
    - Clinical deterioration
    """)
    
    st.markdown("#### 🔪 Bước 3: Phẫu Thuật")
    
    st.error("""
    **Indications for Surgery:**
    - Peritonitis
    - Pneumatosis intestinalis
    - Portal venous gas
    - Free air
    - Clinical deterioration despite medical treatment
    - Gangrene, perforation
    
    **Procedure:**
    - Resection of ischemic segment
    - Colostomy (temporary)
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Colitis"))


def render_radiation_colitis():
    """Radiation Colitis Protocol"""
    
    st.warning("## ⚠️ RADIATION COLITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    st.info("""
    **Đặc điểm:**
    - **Timing:** Có thể xảy ra trong hoặc sau xạ trị
    - **Acute:** Trong xạ trị (1-2 tuần)
    - **Chronic:** Sau xạ trị (tháng đến năm)
    - **Location:** Vùng được xạ trị (thường đại tràng trực tràng)
    """)
    
    timing = st.radio(
        "**Thời điểm:**",
        ["Acute (trong xạ trị)", "Chronic (sau xạ trị)"],
        key="rad_colitis_timing"
    )
    
    st.markdown("### 2️⃣ Điều trị")
    
    if "Acute" in timing:
        st.warning("""
        **Acute Radiation Colitis:**
        - **Supportive care:** Hydration, antidiarrheals
        - **Loperamide:** 2-4 mg PO q4-6h
        - **Diphenoxylate-atropine:** 2.5-5 mg PO qid
        - **Sucralfate enema:** Có thể giúp
        - **Continue radiation:** Nếu có thể
        """)
    else:
        st.error("""
        **Chronic Radiation Colitis:**
        - **Bleeding:** Endoscopic treatment (argon plasma coagulation)
        - **Stricture:** Dilation hoặc surgery
        - **Fistula:** Surgery
        - **Supportive:** Iron, blood transfusion nếu cần
        """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Colitis"))


def render_drug_induced_colitis():
    """Drug-Induced Colitis Protocol"""
    
    st.warning("## ⚠️ DRUG-INDUCED COLITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Chẩn đoán")
    
    st.info("""
    **Thuốc thường gây viêm đại tràng:**
    - **NSAIDs:** Ibuprofen, Naproxen, Diclofenac
    - **Antibiotics:** Penicillins, Cephalosporins (không phải C.diff)
    - **Chemotherapy:** 5-FU, Irinotecan
    - **Immunosuppressants:** Mycophenolate, Tacrolimus
    - **Laxatives:** Senna, Bisacodyl (overuse)
    """)
    
    drug_name = st.text_input("**Tên thuốc nghi ngờ:**", key="drug_colitis_drug")
    
    st.markdown("### 2️⃣ Điều trị")
    
    st.warning("""
    **Nguyên tắc:**
    1. **Ngừng thuốc nghi ngờ** (nếu có thể)
    2. **Supportive care:** Hydration
    3. **Antidiarrheals:** Cẩn thận (có thể làm nặng)
    4. **Corticosteroids:** Nếu nặng (controversial)
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Colitis"))


def render_unknown_colitis():
    """Unknown Etiology Colitis Protocol"""
    
    st.warning("## ⚠️ ACUTE COLITIS - CHƯA XÁC ĐỊNH NGUYÊN NHÂN")
    
    st.markdown("### 1️⃣ Đánh giá Chẩn đoán")
    
    st.info("""
    **Cần loại trừ:**
    1. **C.diff:** Stool PCR/toxin (đã có protocol riêng)
    2. **IBD:** Colonoscopy, histology (đã có protocol riêng)
    3. **Infectious:** Stool culture, PCR, O&P
    4. **Ischemic:** CT with contrast, clinical context
    5. **Radiation:** History of radiation
    6. **Drug-induced:** Medication history
    """)
    
    st.markdown("### 2️⃣ Điều trị Hỗ trợ")
    
    st.warning("""
    - **Supportive care:** Hydration
    - **Monitoring:** CBC, electrolytes, stool studies
    - **Colonoscopy:** Nếu không rõ nguyên nhân sau 2-3 ngày
    - **Consult:** Gastroenterology
    """)
    
    st.markdown("---")
    render_references_section(get_references("Acute Colitis"))

