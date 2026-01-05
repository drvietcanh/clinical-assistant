"""
Acute Liver Failure Protocol
AASLD 2011, EASL 2017 Guidelines
Acute Liver Failure Management & Liver Transplant Criteria
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)


def render():
    """Acute Liver Failure Protocol"""
    st.subheader("🫀 Acute Liver Failure Protocol")
    st.caption("AASLD 2011, EASL 2017, AASLD 2023 - Acute Liver Failure Management & Liver Transplant Criteria")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="Acute Liver Failure",
        guideline_source="AASLD 2011, EASL 2017, AASLD 2023",
        show_version=True,
        show_evidence_summary=True
    )
    
    # AASLD Guidelines Summary
    with st.expander("📚 AASLD 2011 & 2023 Guidelines - Key Recommendations", expanded=False):
        st.markdown("""
        **AASLD 2011 Guidelines for Acute Liver Failure:**
        
        **Definition:**
        - Coagulopathy (INR ≥1.5) + Encephalopathy
        - Within 26 weeks of symptom onset
        - No pre-existing liver disease
        
        **AASLD 2023 Updates:**
        - Enhanced prognostic scoring systems
        - Updated transplant criteria
        - Improved management of complications
        
        **Class I Recommendations:**
        - Immediate ICU admission
        - Identify and treat reversible causes
        - Early transplant evaluation
        - Manage complications (ICP, infection, bleeding)
        
        **King's College Criteria (Acetaminophen):**
        - pH <7.3 (after fluid resuscitation) OR
        - All of: PT >100s, Cr >3.4 mg/dL, Grade 3-4 encephalopathy
        
        **King's College Criteria (Non-Acetaminophen):**
        - PT >100s OR
        - Any 3 of: Age <10 or >40, Duration >7 days, PT >50s, Bilirubin >17.5 mg/dL
        """)
    
    st.error("""
    **⚠️ CRITICAL: Acute Liver Failure là cấp cứu nội khoa!**
    - **Definition:** Coagulopathy (INR ≥1.5) + Encephalopathy trong vòng 26 tuần từ khi khởi phát
    - **Mortality:** 30-50% nếu không điều trị/transplant
    - **Time to transplant:** < 7 ngày (nếu có chỉ định)
    """)
    
    st.markdown("---")
    
    # Etiology selection
    etiology = st.radio(
        "**Nguyên nhân:**",
        ["Acetaminophen (Paracetamol)", "Viral Hepatitis", "Drug-Induced (Non-Acetaminophen)", "Autoimmune", "Wilson Disease", "Chưa xác định"],
        key="alf_etiology"
    )
    
    st.markdown("---")
    
    if "Acetaminophen" in etiology or "Paracetamol" in etiology:
        render_acetaminophen_alf()
    elif "Viral" in etiology:
        render_viral_alf()
    elif "Drug-Induced" in etiology:
        render_drug_induced_alf()
    elif "Autoimmune" in etiology:
        render_autoimmune_alf()
    elif "Wilson" in etiology:
        render_wilson_alf()
    else:
        render_unknown_alf()


def render_acetaminophen_alf():
    """Acetaminophen-Induced ALF Protocol"""
    
    st.error("## 🚨 ACETAMINOPHEN-INDUCED ALF PROTOCOL")
    st.error("**N-ACETYLCYSTEINE (NAC) - ĐIỀU TRỊ KHẨN CẤP!**")
    
    st.markdown("### 1️⃣ Xử tríTức Thì (< 1 Giờ)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **ABC - Đường thở, Hô hấp, Tuần hoàn:**
        
        **A - Airway:**
        - Đánh giá GCS
        - Cân nhắc đặt nội khí quản nếu:
          * GCS <8
          * Encephalopathy grade 3-4
          * Không bảo vệ được đường thở
        
        **B - Breathing:**
        - O₂ để duy trì SpO₂ >94%
        - Theo dõi SpO₂ liên tục
        
        **C - Circulation:**
        - **2 đường truyền tĩnh mạch lớn**
        - **Lấy máu ngay:**
          * CBC, PT/INR, aPTT
          * LFT (AST, ALT, bilirubin, albumin)
          * Glucose, electrolytes
          * Lactate, ammonia
          * Acetaminophen level (nếu <24h từ khi uống)
          * Creatinine, BUN
        - **ECG**
        """)
    
    with col2:
        st.warning("""
        **Clinical Features:**
        
        **Timing:**
        - **0-24h:** Nausea, vomiting, malaise
        - **24-48h:** LFT ↑ (AST/ALT peak)
        - **48-72h:** Encephalopathy, coagulopathy
        - **3-5 days:** Peak toxicity
        
        **Risk Factors:**
        - Dose >150 mg/kg (single) hoặc >7.5g/day (chronic)
        - Alcohol use
        - Malnutrition
        - Fasting
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ N-Acetylcysteine (NAC) - NGAY")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Dùng NAC NGAY nếu nghi ngờ acetaminophen toxicity!**
    
    **Chỉ định:**
    - ✅ Acetaminophen level >150 mcg/mL (4h post-ingestion)
    - ✅ Nghi ngờ acetaminophen toxicity (bất kể level)
    - ✅ ALF với nguyên nhân chưa rõ (empiric)
    
    **Timing:**
    - **< 8h từ khi uống:** Hiệu quả tối đa
    - **8-24h:** Vẫn có lợi ích
    - **> 24h:** Vẫn nên dùng nếu có ALF
    """)
    
    st.markdown("---")
    st.markdown("#### 💉 NAC Dosing Protocol")
    
    tab1, tab2 = st.tabs(["IV Protocol (Preferred)", "PO Protocol"])
    
    with tab1:
        st.success("""
        **IV NAC (Acetadote):**
        
        **Loading:** 150 mg/kg trong 250ml D5W × 1h
        
        **Then:** 50 mg/kg trong 500ml D5W × 4h
        
        **Then:** 100 mg/kg trong 1000ml D5W × 16h
        
        **Total:** 21h protocol
        
        **Lưu ý:**
        - Có thể lặp lại nếu cần
        - Theo dõi anaphylactoid reactions (rash, bronchospasm)
        - Nếu có reaction: Dừng 1h, sau đó tiếp tục với tốc độ chậm hơn
        """)
    
    with tab2:
        st.info("""
        **PO NAC (Mucomyst):**
        
        **Loading:** 140 mg/kg PO × 1
        
        **Then:** 70 mg/kg PO q4h × 17 liều (68h total)
        
        **Lưu ý:**
        - Pha trong nước/juice để giảm mùi vị
        - Có thể gây nôn (dùng antiemetic)
        - Nếu nôn trong 1h: Lặp lại liều
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Supportive Care")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Glucose Management:**
        - **Hypoglycemia:** Thường gặp (do mất glycogen)
        - **Dextrose 10-20%:** Truyền liên tục
        - **Monitor:** Glucose mỗi 1-2h
        - **Mục tiêu:** 80-150 mg/dL
        
        **Coagulopathy:**
        - **Vitamin K:** 10mg IV × 3 ngày
        - **FFP:** Chỉ nếu có bleeding hoặc trước procedure
        - **INR:** Theo dõi nhưng không điều trị trừ khi bleeding
        """)
    
    with col2:
        st.info("""
        **ICP Management (nếu có encephalopathy grade 3-4):**
        - **ICP monitoring:** Cân nhắc nếu grade 3-4
        - **Mục tiêu ICP:** <20 mmHg
        - **CPP:** 50-70 mmHg
        - **Mannitol:** 0.5-1 g/kg IV nếu ICP >20
        - **Hyperventilation:** PaCO₂ 30-35 mmHg (tạm thời)
        
        **Renal Protection:**
        - **Hydration:** Euvolemia
        - **Avoid nephrotoxins**
        - **RRT:** Nếu AKI nặng
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ King's College Criteria (Transplant)")
    
    st.error("""
    **King's College Criteria cho Acetaminophen ALF:**
    
    **Chỉ định transplant nếu:**
    
    ✅ **pH <7.30** (sau fluid resuscitation) HOẶC
    
    ✅ **Tất cả 3 điều sau:**
    - INR >6.5
    - Creatinine >3.4 mg/dL
    - Encephalopathy grade 3-4
    
    **Timing:**
    - Đánh giá sau 24h từ khi nhập viện
    - Nếu đạt criteria → Liver transplant consult NGAY
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Monitoring & Prognosis")
    
    st.success("""
    **Monitoring:**
    - **LFT:** AST/ALT mỗi 12-24h (sẽ giảm nếu recovery)
    - **INR:** Mỗi 12-24h
    - **Ammonia:** Mỗi 12-24h (nếu có encephalopathy)
    - **Glucose:** Mỗi 1-2h
    - **Neurologic:** GCS, encephalopathy grade
    
    **Prognosis:**
    - **Good:** AST/ALT giảm, INR cải thiện trong 48-72h
    - **Poor:** INR tiếp tục tăng, encephalopathy nặng lên
    - **Mortality:** 20-30% nếu không transplant
    """)


def render_viral_alf():
    """Viral Hepatitis-Induced ALF Protocol"""
    
    st.error("## 🚨 VIRAL HEPATITIS-INDUCED ALF PROTOCOL")
    
    st.markdown("### 1️⃣ Etiology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Common Viruses:**
        - **HAV:** Thường tự khỏi, ít gây ALF
        - **HBV:** Có thể gây ALF (acute hoặc flare)
        - **HEV:** Phổ biến ở châu Á, có thể nặng
        - **HDV:** Co-infection với HBV
        - **HCV:** Hiếm gây ALF
        """)
    
    with col2:
        st.warning("""
        **Serology:**
        - **HAV:** Anti-HAV IgM
        - **HBV:** HBsAg, Anti-HBc IgM, HBV DNA
        - **HEV:** Anti-HEV IgM, HEV RNA
        - **HDV:** Anti-HDV IgM (nếu HBsAg +)
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Treatment")
    
    st.success("""
    **HBV ALF:**
    - **Nucleos(t)ide analog:**
      * **Entecavir:** 0.5mg PO QD
      * **Tenofovir:** 300mg PO QD
    - **Duration:** Thường 3-6 tháng (đến khi HBsAg -)
    
    **HAV/HEV:**
    - **Supportive care** (không có điều trị đặc hiệu)
    - Thường tự khỏi
    
    **General Supportive:**
    - Tương tự acetaminophen ALF
    - Glucose, coagulopathy, ICP management
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ King's College Criteria (Non-Acetaminophen)")
    
    st.error("""
    **King's College Criteria cho Non-Acetaminophen ALF:**
    
    **Chỉ định transplant nếu:**
    
    ✅ **INR >6.5** (bất kể encephalopathy grade) HOẶC
    
    ✅ **Bất kỳ 3 trong 5 điều sau:**
    - Age <10 hoặc >40
    - Etiology: Non-A, non-B, halothane, idiosyncratic drug
    - Jaundice >7 ngày trước encephalopathy
    - INR >3.5
    - Bilirubin >17.5 mg/dL
    
    **Timing:**
    - Đánh giá sau 24h
    - Transplant consult nếu đạt criteria
    """)


def render_drug_induced_alf():
    """Drug-Induced (Non-Acetaminophen) ALF Protocol"""
    
    st.error("## 🚨 DRUG-INDUCED ALF PROTOCOL")
    
    st.markdown("### 1️⃣ Common Culprits")
    
    st.warning("""
    **Drugs thường gây ALF:**
    - **Antibiotics:** Isoniazid, Rifampin, Sulfonamides
    - **Antifungals:** Ketoconazole, Fluconazole
    - **Antiepileptics:** Phenytoin, Valproate, Carbamazepine
    - **NSAIDs:** Diclofenac, Ibuprofen
    - **Herbal:** Kava, Comfrey, Ma-huang
    - **Others:** Amiodarone, Allopurinol, Methotrexate
    
    **Mechanism:**
    - Idiosyncratic (không liên quan liều)
    - Thường xảy ra trong 1-3 tháng đầu dùng
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Treatment")
    
    st.info("""
    **Immediate Actions:**
    1. ✅ **Ngừng thuốc nghi ngờ NGAY**
    2. ✅ **Supportive care** (tương tự acetaminophen)
    3. ✅ **N-acetylcysteine:** Có thể có lợi ích (empiric)
    4. ✅ **Corticosteroids:** Cân nhắc nếu nghi autoimmune component
    
    **Supportive:**
    - Glucose management
    - Coagulopathy (vitamin K, FFP nếu bleeding)
    - ICP management nếu encephalopathy
    - RRT nếu AKI
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Prognosis")
    
    st.success("""
    **Prognosis:**
    - Phụ thuộc vào drug và timing
    - Nếu ngừng sớm: Có thể recovery
    - Nếu nặng: Cần transplant
    
    **King's College Criteria:** Áp dụng cho non-acetaminophen ALF
    """)


def render_autoimmune_alf():
    """Autoimmune Hepatitis-Induced ALF Protocol"""
    
    st.error("## 🚨 AUTOIMMUNE HEPATITIS ALF PROTOCOL")
    
    st.markdown("### 1️⃣ Diagnosis")
    
    st.info("""
    **Clinical Features:**
    - Thường ở phụ nữ trẻ/middle-aged
    - Có thể có autoimmune markers (ANA, ASMA, anti-LKM1)
    - IgG elevated
    
    **Diagnosis:**
    - Clinical + serology + histology (nếu có thể)
    - Simplified AIH score
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Treatment")
    
    st.warning("""
    **Corticosteroids:**
    - **Prednisone:** 40-60mg PO QD
    - **+ Azathioprine:** 50mg PO QD (nếu không có ALF nặng)
    - **Response:** Đánh giá sau 7-14 ngày
    
    **Nếu không đáp ứng:**
    - Xem xét liver transplant
    
    **Supportive:**
    - Tương tự các ALF khác
    """)


def render_wilson_alf():
    """Wilson Disease-Induced ALF Protocol"""
    
    st.error("## 🚨 WILSON DISEASE ALF PROTOCOL")
    
    st.markdown("### 1️⃣ Diagnosis")
    
    st.warning("""
    **Clinical Features:**
    - Age: 10-40 tuổi
    - Kayser-Fleischer rings (slit lamp)
    - Hemolytic anemia
    - Low ceruloplasmin
    - High urinary copper
    
    **Diagnosis:**
    - Ceruloplasmin <20 mg/dL
    - 24h urinary copper >100 mcg
    - Liver copper >250 mcg/g (nếu có biopsy)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Treatment")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Wilson ALF thường cần transplant!**
    
    **Chelation (nếu có thời gian):**
    - **D-penicillamine:** 1-2g PO QD (nếu không ALF nặng)
    - **Trientine:** 1-2g PO QD
    - **Zinc:** 50mg PO TID (blocking copper absorption)
    
    **Nếu ALF nặng:**
    - **Liver transplant:** Thường cần
    - **MELD exception:** Có thể được priority
    
    **Supportive:**
    - Tương tự các ALF khác
    - Hemolysis management
    """)


def render_unknown_alf():
    """Protocol when etiology unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH NGUYÊN NHÂN ALF")
    
    st.error("""
    **Xử trí ngay trong khi chờ chẩn đoán:**
    
    1. ✅ **ABC** - Đường thở, Hô hấp, Tuần hoàn
    2. ✅ **2 đường truyền** tĩnh mạch
    3. ✅ **Lấy máu:** LFT, PT/INR, Acetaminophen level, Viral serology, Autoimmune markers, Ceruloplasmin, Copper
    4. ✅ **N-acetylcysteine:** Empiric nếu nghi acetaminophen
    5. ✅ **Supportive care:** Glucose, coagulopathy, ICP
    6. ✅ **Liver transplant consult:** Nếu đạt King's College criteria
    
    **Timeline:**
    - Labs trong 1h
    - NAC ngay nếu nghi acetaminophen
    - Transplant evaluation nếu đạt criteria
    
    **Workup:**
    - Acetaminophen level
    - Viral serology (HAV, HBV, HEV)
    - Autoimmune markers (ANA, ASMA, anti-LKM1, IgG)
    - Wilson (ceruloplasmin, copper)
    - Drug history (detailed)
    """)
    
    st.markdown("---")
    st.markdown("### 📊 King's College Criteria Summary")
    
    st.info("""
    **Acetaminophen ALF:**
    - pH <7.30 HOẶC
    - INR >6.5 + Cr >3.4 + Encephalopathy grade 3-4
    
    **Non-Acetaminophen ALF:**
    - INR >6.5 HOẶC
    - 3/5: Age <10 or >40, Non-A/B etiology, Jaundice >7d, INR >3.5, Bilirubin >17.5
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Acute Liver Failure")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

