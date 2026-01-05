"""
Meningitis / Encephalitis Protocol
IDSA 2016 Guidelines
Bacterial & Viral Meningitis, Encephalitis Management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)


def render():
    """Meningitis / Encephalitis Protocol"""
    st.subheader("🧠 Meningitis / Encephalitis Protocol")
    st.caption("IDSA 2016 - Bacterial & Viral Meningitis, Encephalitis Management")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="Meningitis / Encephalitis",
        guideline_source="IDSA 2016, IDSA 2017",
        show_version=True,
        show_evidence_summary=True
    )
    
    # IDSA Guidelines Summary
    with st.expander("📚 IDSA 2016 Guidelines - Key Recommendations", expanded=False):
        st.markdown("""
        **IDSA 2016 Guidelines for Bacterial Meningitis:**
        
        **Class I Recommendations (Strong Evidence):**
        - Empiric antibiotics within 1 hour of presentation
        - Dexamethasone before or with first dose of antibiotics (adults with suspected pneumococcal meningitis)
        - CSF analysis (cell count, glucose, protein, Gram stain, culture)
        - Blood cultures before antibiotics
        
        **IDSA 2017 Guidelines for Viral Meningitis/Encephalitis:**
        - Empiric acyclovir for suspected HSV encephalitis
        - CSF PCR for HSV, enterovirus, arboviruses
        - MRI brain for encephalitis evaluation
        
        **Key Updates:**
        - Time to antibiotics: <1 hour critical
        - Dexamethasone: 10mg IV q6h × 4 days (start before antibiotics)
        - Empiric coverage: Vancomycin + Ceftriaxone (or Cefotaxime)
        - Acyclovir: 10mg/kg IV q8h for HSV encephalitis
        """)
    
    st.error("""
    **⚠️ CRITICAL: Meningitis/Encephalitis là cấp cứu thần kinh!**
    - **Mortality:** 10-30% (bacterial), 5-10% (viral)
    - **Time to antibiotics:** < 1 giờ từ khi nhập viện
    - **Neurologic sequelae:** 20-50% nếu điều trị muộn
    """)
    
    st.markdown("---")
    
    # Type selection
    infection_type = st.radio(
        "**Loại nhiễm trùng:**",
        ["Bacterial Meningitis", "Viral Meningitis/Encephalitis", "Chưa xác định"],
        key="meningitis_type"
    )
    
    st.markdown("---")
    
    if "Bacterial" in infection_type:
        render_bacterial_meningitis()
    elif "Viral" in infection_type:
        render_viral_meningitis_encephalitis()
    else:
        render_unknown_meningitis()


def render_bacterial_meningitis():
    """Bacterial Meningitis Protocol"""
    
    st.error("## 🚨 BACTERIAL MENINGITIS PROTOCOL")
    st.error("**CODE MENINGITIS - Xử trí khẩn cấp!**")
    
    st.markdown("### 1️⃣ Xử tríTức Thì (< 10 Phút)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **ABC - Đường thở, Hô hấp, Tuần hoàn:**
        
        **A - Airway:**
        - Đảm bảo đường thở thông thoáng
        - Cân nhắc đặt nội khí quản nếu:
          * GCS <8
          * Không bảo vệ được đường thở
          * Respiratory failure
        
        **B - Breathing:**
        - O₂ để duy trì SpO₂ >94%
        - Theo dõi SpO₂ liên tục
        
        **C - Circulation:**
        - **2 đường truyền tĩnh mạch lớn**
        - **Lấy máu ngay:**
          * CBC, PT/INR, aPTT
          * Blood cultures (2 sets)
          * Glucose, electrolytes
          * Lactate
        - **ECG**
        """)
    
    with col2:
        st.warning("""
        **Clinical Features:**
        
        **Classic Triad (chỉ 44% có đủ 3):**
        - Fever
        - Neck stiffness
        - Altered mental status
        
        **Other Symptoms:**
        - Headache (87%)
        - Photophobia
        - Nausea/vomiting
        - Seizures (20-30%)
        - Focal neurologic deficits
        - Petechial/purpuric rash (meningococcal)
        
        **Physical Exam:**
        - Kernig sign
        - Brudzinski sign
        - Nuchal rigidity
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Lumbar Puncture (LP) - Timing")
    
    st.info("""
    **Timing cho LP:**
    
    **NGAY (trong 30-60 phút):**
    - Nếu không có chống chỉ định
    - Trước khi dùng kháng sinh (nếu có thể)
    
    **Chống chỉ định LP:**
    - ⚠️ **Focal neurologic deficit** (nghi mass lesion)
    - ⚠️ **Papilledema** (nghi ↑ICP)
    - ⚠️ **Seizure** gần đây
    - ⚠️ **Immunocompromised** (nghi fungal/atypical)
    - ⚠️ **Coagulopathy** (INR >1.5, Platelet <50k)
    - ⚠️ **Local infection** tại vị trí LP
    
    **Nếu chống chỉ định LP:**
    - **CT Head trước** (nếu có focal deficit, papilledema, seizure)
    - **Dùng kháng sinh ngay** (không chờ LP)
    - LP sau khi CT OK và đã dùng kháng sinh
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Empiric Antibiotics - NGAY (< 1 Giờ)")
    
    st.error("""
    **⚠️ KHÔNG CHỜ LP HOẶC CULTURE - Dùng kháng sinh NGAY!**
    
    **Timing:**
    - **< 1 giờ** từ khi nhập viện
    - **Trước LP** nếu LP bị trì hoãn
    - **Sau LP** nếu LP ngay được
    """)
    
    st.markdown("---")
    st.markdown("#### 💉 Empiric Antibiotics by Age & Risk Factors")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Người lớn (18-50)", "Người lớn (>50)", "Trẻ em", "Immunocompromised"])
    
    with tab1:
        st.success("""
        **Người lớn 18-50 tuổi:**
        
        **Standard:**
        - **Ceftriaxone:** 2g IV q12h
        - **Vancomycin:** 15-20 mg/kg IV q8-12h (target trough 15-20)
        - **Dexamethasone:** 0.15 mg/kg IV q6h × 4 ngày (trước hoặc cùng lúc với kháng sinh)
        
        **Nếu nghi Listeria (pregnant, immunocompromised):**
        - Thêm **Ampicillin:** 2g IV q4h
        """)
    
    with tab2:
        st.warning("""
        **Người lớn >50 tuổi:**
        
        **Standard:**
        - **Ceftriaxone:** 2g IV q12h
        - **Vancomycin:** 15-20 mg/kg IV q8-12h
        - **Ampicillin:** 2g IV q4h (Listeria coverage)
        - **Dexamethasone:** 0.15 mg/kg IV q6h × 4 ngày
        
        **Lý do thêm Ampicillin:**
        - Listeria risk tăng theo tuổi
        - Immunocompromised risk cao hơn
        """)
    
    with tab3:
        st.info("""
        **Trẻ em:**
        
        **< 3 tháng:**
        - **Ampicillin:** 50 mg/kg IV q6h
        - **Cefotaxime:** 50 mg/kg IV q6h
        - **Vancomycin:** 15 mg/kg IV q6h
        
        **3 tháng - 18 tuổi:**
        - **Ceftriaxone:** 50-75 mg/kg IV q12h (max 2g)
        - **Vancomycin:** 15 mg/kg IV q6h
        - **Dexamethasone:** 0.15 mg/kg IV q6h × 4 ngày (nếu nghi H. influenzae)
        """)
    
    with tab4:
        st.error("""
        **Immunocompromised:**
        
        **Bacterial coverage:**
        - **Ceftriaxone:** 2g IV q12h
        - **Vancomycin:** 15-20 mg/kg IV q8-12h
        - **Ampicillin:** 2g IV q4h
        
        **Fungal coverage (nếu nghi):**
        - **Amphotericin B:** 0.7-1 mg/kg IV q24h
        - Hoặc **Fluconazole:** 400-800mg IV q24h
        
        **TB coverage (nếu nghi):**
        - **4-drug regimen:** RIPE (Rifampin, Isoniazid, Pyrazinamide, Ethambutol)
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Dexamethasone - Steroids")
    
    st.info("""
    **Dexamethasone Protocol:**
    
    **Chỉ định:**
    - ✅ **Bacterial meningitis** (confirmed hoặc suspected)
    - ✅ **Trước hoặc cùng lúc** với kháng sinh đầu tiên
    - ✅ **Người lớn** và **trẻ em >6 tuần**
    
    **Liều:**
    - **0.15 mg/kg IV q6h × 4 ngày**
    - **Max:** 10mg q6h
    
    **Lợi ích:**
    - Giảm hearing loss (đặc biệt H. influenzae)
    - Giảm neurologic sequelae
    - Giảm mortality (một số nghiên cứu)
    
    **Lưu ý:**
    - Chỉ dùng nếu **trước hoặc cùng lúc** với kháng sinh
    - Nếu đã dùng kháng sinh >1h trước → Không dùng steroids
    - Không dùng nếu nghi fungal/TB meningitis
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Pathogen-Specific Treatment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **S. pneumoniae:**
        - **Penicillin-susceptible (MIC <0.06):**
          * Penicillin G: 4 million units IV q4h
          * Hoặc Ampicillin: 2g IV q4h
        - **Penicillin-intermediate (MIC 0.12-1):**
          * Ceftriaxone: 2g IV q12h
        - **Penicillin-resistant (MIC ≥2):**
          * Vancomycin: 15-20 mg/kg IV q8-12h
          * + Ceftriaxone: 2g IV q12h
        
        **N. meningitidis:**
        - **Penicillin-susceptible:**
          * Penicillin G: 4 million units IV q4h
        - **Penicillin-resistant:**
          * Ceftriaxone: 2g IV q12h
        
        **H. influenzae:**
        - **Beta-lactamase negative:**
          * Ampicillin: 2g IV q4h
        - **Beta-lactamase positive:**
          * Ceftriaxone: 2g IV q12h
        """)
    
    with col2:
        st.warning("""
        **Listeria monocytogenes:**
        - **Ampicillin:** 2g IV q4h
        - **+ Gentamicin:** 1.5-2 mg/kg IV q8h (synergy)
        - **Duration:** 14-21 ngày
        
        **Staphylococcus (nếu post-op, shunt):**
        - **Vancomycin:** 15-20 mg/kg IV q8-12h
        - **+ Rifampin:** 600mg IV/PO q24h (nếu biofilm)
        - **Duration:** 14-21 ngày
        
        **Gram-negative (E. coli, Klebsiella):**
        - **Ceftriaxone:** 2g IV q12h
        - Hoặc **Cefepime:** 2g IV q8h
        - **Duration:** 14-21 ngày
        """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Duration of Treatment")
    
    st.info("""
    **Duration by Pathogen:**
    
    - **S. pneumoniae:** 10-14 ngày
    - **N. meningitidis:** 7 ngày
    - **H. influenzae:** 7-10 ngày
    - **Listeria:** 14-21 ngày
    - **Gram-negative:** 14-21 ngày
    - **Staphylococcus:** 14-21 ngày
    
    **Lưu ý:**
    - Có thể rút ngắn nếu cải thiện nhanh
    - Có thể kéo dài nếu chậm cải thiện
    - LP lặp lại nếu không cải thiện sau 48h
    """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Monitoring & Complications")
    
    st.warning("""
    **Monitoring:**
    - **Neurologic checks:** Mỗi 1-2 giờ
    - **Vital signs:** Mỗi 1-2 giờ
    - **Labs:** CBC, electrolytes mỗi 24h
    - **LP lặp lại:** Nếu không cải thiện sau 48h
    
    **Complications:**
    - **Seizures:** Levetiracetam, Phenytoin
    - **ICP ↑:** Mannitol, hyperventilation (tạm thời)
    - **SIADH:** Fluid restriction
    - **Hearing loss:** Screen sau điều trị
    - **Hydrocephalus:** CT/MRI, neurosurgery consult
    """)
    
    st.markdown("---")
    st.markdown("### 8️⃣ Chemoprophylaxis (Meningococcal)")
    
    st.success("""
    **Chỉ định:**
    - **N. meningitidis** confirmed
    - **Close contacts** (household, daycare, kissing)
    
    **Regimens:**
    - **Rifampin:** 600mg PO q12h × 2 ngày (người lớn)
    - **Ciprofloxacin:** 500mg PO × 1 liều (người lớn)
    - **Ceftriaxone:** 250mg IM × 1 liều (pregnant)
    
    **Timing:** Trong 24h từ khi tiếp xúc
    """)


def render_viral_meningitis_encephalitis():
    """Viral Meningitis / Encephalitis Protocol"""
    
    st.error("## 🚨 VIRAL MENINGITIS / ENCEPHALITIS PROTOCOL")
    
    st.markdown("### 1️⃣ Clinical Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Viral Meningitis:**
        - Fever
        - Headache
        - Neck stiffness
        - Photophobia
        - Nausea/vomiting
        - **NO altered mental status**
        - **NO focal deficits**
        
        **Common Pathogens:**
        - Enteroviruses (80-90%)
        - HSV-2 (meningitis)
        - Arboviruses
        - Mumps
        """)
    
    with col2:
        st.warning("""
        **Viral Encephalitis:**
        - **Altered mental status** (key difference!)
        - Fever
        - Headache
        - Seizures
        - Focal neurologic deficits
        - Behavioral changes
        
        **Common Pathogens:**
        - **HSV-1** (most common, treatable)
        - Enteroviruses
        - Arboviruses (West Nile, Japanese encephalitis)
        - VZV
        - EBV, CMV
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Diagnostic Workup")
    
    st.info("""
    **LP (Lumbar Puncture):**
    - **CSF analysis:**
      * WBC: 10-500 (lymphocytic)
      * Glucose: Normal
      * Protein: Mildly elevated
      * **PCR:** HSV, Enterovirus, VZV, etc.
    
    **Imaging:**
    - **MRI Brain:** Nếu encephalitis (temporal lobe involvement → HSV)
    - **CT Head:** Nếu có focal deficit trước LP
    
    **Labs:**
    - Blood cultures (loại trừ bacterial)
    - Serology (arboviruses)
    - CSF PCR (HSV, Enterovirus, VZV, etc.)
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Empiric Treatment - HSV Encephalitis")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Dùng Acyclovir NGAY nếu nghi encephalitis!**
    
    **Acyclovir Protocol:**
    - **10 mg/kg IV q8h** (người lớn)
    - **20 mg/kg IV q8h** (trẻ em)
    - **Duration:** 14-21 ngày (HSV encephalitis)
    - **Adjust for renal function:**
      * CrCl 25-50: 10 mg/kg q12h
      * CrCl 10-25: 10 mg/kg q24h
      * CrCl <10: 5 mg/kg q24h
    
    **Lý do dùng ngay:**
    - HSV encephalitis có mortality 70% nếu không điều trị
    - Mortality giảm xuống 20-30% nếu điều trị sớm
    - Không thể phân biệt HSV với viral khác lâm sàng
    - PCR có thể mất 24-48h
    
    **Khi nào dừng:**
    - Nếu CSF PCR (-) cho HSV và không nghi HSV
    - Nếu chẩn đoán khác rõ ràng
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Pathogen-Specific Treatment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **HSV-1 Encephalitis:**
        - **Acyclovir:** 10 mg/kg IV q8h × 14-21 ngày
        - **Monitor:** Renal function, neurotoxicity
        
        **HSV-2 Meningitis:**
        - **Acyclovir:** 10 mg/kg IV q8h × 10-14 ngày
        - Hoặc **Valacyclovir:** 1g PO TID × 10-14 ngày (nếu mild)
        
        **VZV:**
        - **Acyclovir:** 10 mg/kg IV q8h × 14 ngày
        - Hoặc **Valacyclovir:** 1g PO TID × 14 ngày
        """)
    
    with col2:
        st.warning("""
        **Enteroviruses:**
        - **Supportive care** (không có điều trị đặc hiệu)
        - **Pleconaril:** (experimental, không có sẵn)
        
        **Arboviruses:**
        - **Supportive care**
        - Không có điều trị đặc hiệu
        
        **CMV (immunocompromised):**
        - **Ganciclovir:** 5 mg/kg IV q12h
        - **+ Foscarnet:** 90 mg/kg IV q12h (nếu resistant)
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Supportive Care")
    
    st.info("""
    **General Support:**
    - **Fluids:** Euvolemia, tránh SIADH
    - **Fever:** Acetaminophen
    - **Seizures:** Levetiracetam, Phenytoin
    - **ICP management:** Nếu có ↑ICP
    
    **Monitoring:**
    - Neurologic checks mỗi 1-2h
    - Vital signs
    - Labs (electrolytes, renal function)
    
    **Prognosis:**
    - **Viral meningitis:** Thường tự khỏi, recovery tốt
    - **HSV encephalitis:** 20-30% mortality, 50% có sequelae
    - **Other encephalitis:** Phụ thuộc pathogen
    """)


def render_unknown_meningitis():
    """Protocol when type unknown"""
    
    st.warning("## ⚠️ CHƯA XÁC ĐỊNH LOẠI MENINGITIS/ENCEPHALITIS")
    
    st.error("""
    **Xử trí ngay trong khi chờ chẩn đoán:**
    
    1. ✅ **ABC** - Đường thở, Hô hấp, Tuần hoàn
    2. ✅ **2 đường truyền** tĩnh mạch
    3. ✅ **Lấy máu:** CBC, PT/INR, Blood cultures
    4. ✅ **LP ngay** (nếu không chống chỉ định)
    5. ✅ **Empiric antibiotics NGAY** (bacterial coverage)
    6. ✅ **Acyclovir NGAY** nếu có altered mental status (encephalitis)
    7. ✅ **Dexamethasone** nếu nghi bacterial (trước kháng sinh)
    
    **Timeline:**
    - LP trong 30-60 phút
    - Antibiotics < 1 giờ
    - Acyclovir < 1 giờ (nếu encephalitis)
    - CSF PCR results: 24-48h
    
    **Sau khi có kết quả:**
    - Nếu bacterial → Tiếp tục antibiotics, dừng acyclovir
    - Nếu viral → Dừng antibiotics, tiếp tục acyclovir nếu HSV
    - Nếu fungal/TB → Điều chỉnh theo pathogen
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Decision Tree")
    
    st.info("""
    **Nếu có altered mental status:**
    - → **Encephalitis** → Dùng **Acyclovir** ngay
    - → **+ Antibiotics** (empiric bacterial coverage)
    
    **Nếu không có altered mental status:**
    - → **Meningitis** → Dùng **Antibiotics** ngay
    - → **+ Acyclovir** nếu nghi HSV-2 meningitis
    
    **Sau khi có CSF results:**
    - **CSF WBC >1000, PMN >80%:** → Bacterial
    - **CSF WBC 10-500, Lymphocytes:** → Viral
    - **CSF Glucose low, Protein high:** → Bacterial hoặc TB/Fungal
    - **CSF PCR (+):** → Pathogen-specific treatment
    """)
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("Meningitis / Encephalitis")
    
    # Keep existing references as fallback
    references = get_references("Meningitis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo (Additional)",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )

