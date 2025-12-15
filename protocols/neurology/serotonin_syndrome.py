"""
Serotonin Syndrome Protocol
Hunter Criteria, Sternbach Criteria
Life-threatening condition from excessive serotonergic activity
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Serotonin Syndrome Protocol"""
    st.subheader("🧠 Hội chứng Serotonin (Serotonin Syndrome)")
    st.caption("Hunter Criteria 2003 - Excessive serotonergic activity management")
    
    st.error("""
    **⚠️ HỘI CHỨNG SEROTONIN = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Tăng hoạt động serotonergic quá mức
    - Thường do tương tác thuốc hoặc quá liều
    - Có thể gây tử vong nếu không điều trị
    
    **Nguyên nhân thường gặp:**
    - SSRI + MAOI
    - SSRI + Tramadol
    - SSRI + Triptans
    - Quá liều SSRI/SNRI
    - Tương tác nhiều thuốc serotonergic
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    st.markdown("#### **Hunter Criteria (2003) - Độ nhạy cao hơn**")
    
    st.warning("""
    **Chẩn đoán khi có 1 trong các tiêu chuẩn sau:**
    
    1. **Spontaneous clonus** (Clonus tự phát)
    2. **Inducible clonus** + Agitation hoặc Diaphoresis (Vã mồ hôi)
    3. **Ocular clonus** + Agitation hoặc Diaphoresis
    4. **Tremor** + Hyperreflexia
    5. **Hypertonia** + Nhiệt độ >38°C + Ocular clonus hoặc Inducible clonus
    """)
    
    st.markdown("#### **Sternbach Criteria (1991) - Cổ điển**")
    
    st.info("""
    **Chẩn đoán khi có:**
    - Đang dùng thuốc serotonergic
    - Có ≥3 trong các triệu chứng:
      1. Thay đổi tâm thần (confusion, agitation)
      2. Kích động (agitation)
      3. Myoclonus (Giật cơ)
      4. Hyperreflexia (Phản xạ tăng)
      5. Sốt
      6. Run (tremor)
      7. Tiêu chảy
      8. Đồng tử giãn
      9. Vã mồ hôi (diaphoresis)
      10. Run rẩy (shivering)
    - Loại trừ: Nhiễm trùng, rối loạn chuyển hóa, cai thuốc
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Thần kinh:**
        - Confusion (Lú lẫn)
        - Agitation (Kích động)
        - Anxiety (Lo âu)
        - Coma (Hôn mê)
        - Seizures (Co giật)
        """)
    
    with col2:
        st.markdown("""
        **Vận động:**
        - Myoclonus (Giật cơ)
        - Clonus (Clonus)
        - Hyperreflexia (Phản xạ tăng)
        - Hypertonia (Tăng trương lực)
        - Tremor (Run)
        """)
    
    with col3:
        st.markdown("""
        **Tự chủ:**
        - Hyperthermia (Sốt cao)
        - Diaphoresis (Vã mồ hôi)
        - Tachycardia (Nhịp nhanh)
        - Hypertension (Tăng huyết áp)
        - Mydriasis (Đồng tử giãn)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: SEVERITY ASSESSMENT ==========
    st.markdown("### 📊 Phân loại mức độ")
    
    severity = st.radio(
        "**Mức độ nặng:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)"],
        key="serotonin_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_serotonin()
    elif "Trung bình" in severity:
        render_moderate_serotonin()
    else:
        render_severe_serotonin()
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### **1. Ngừng ngay tất cả thuốc serotonergic**")
    st.warning("""
    **Ngừng ngay:**
    - Tất cả SSRI, SNRI, MAOI
    - Tramadol, Fentanyl, Meperidine
    - Triptans
    - Linezolid
    - Các thuốc serotonergic khác
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Hỗ trợ (Supportive Care)**")
    
    st.success("""
    **Điều trị hỗ trợ:**
    - **Hạ nhiệt:** Paracetamol, làm mát ngoài
    - **An thần:** Benzodiazepines (Lorazepam, Diazepam)
    - **Hạ huyết áp:** Nếu cần (thường tự hết)
    - **Điều chỉnh rối loạn điện giải**
    - **Theo dõi sát:** Nhiệt độ, huyết áp, nhịp tim
    """)
    
    st.markdown("---")
    
    st.markdown("#### **3. Điều trị đặc hiệu (Nếu nặng)**")
    
    st.error("""
    **Cyproheptadine (Thuốc kháng serotonin):**
    - **Liều:** 12 mg PO/NG, sau đó 2 mg q2h nếu cần
    - **Tối đa:** 32 mg/ngày
    - **Lưu ý:** Chỉ dùng khi nặng, không có dạng IV
    
    **Chlorpromazine:**
    - **Liều:** 50-100 mg IM
    - **Lưu ý:** Có thể gây hạ huyết áp
    
    **Olanzapine:**
    - **Liều:** 10 mg IM
    - **Lưu ý:** Có thể dùng thay thế
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Nhiệt độ:** Mỗi 1-2 giờ
    - **Huyết áp, nhịp tim:** Liên tục
    - **Triệu chứng thần kinh:** Mỗi 2-4 giờ
    - **CK (Creatine Kinase):** Nếu có myoclonus nặng (rhabdomyolysis)
    - **Chức năng thận:** Nếu có rhabdomyolysis
    
    **Dấu hiệu cải thiện:**
    - Giảm nhiệt độ
    - Giảm clonus/myoclonus
    - Giảm kích động
    - Cải thiện ý thức
    
    **Dấu hiệu xấu đi:**
    - Nhiệt độ >40°C
    - Rhabdomyolysis
    - Suy đa tạng
    - Cần ICU
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: DIFFERENTIAL DIAGNOSIS ==========
    st.markdown("### 🔄 Chẩn đoán phân biệt")
    
    st.markdown("""
    **Cần phân biệt với:**
    
    1. **Neuroleptic Malignant Syndrome (NMS):**
       - Do thuốc chống loạn thần
       - Cứng cơ (rigidity) > clonus
       - Khởi phát chậm hơn (ngày)
       - Điều trị: Dantrolene, Bromocriptine
    
    2. **Malignant Hyperthermia:**
       - Do thuốc mê (halothane, succinylcholine)
       - Cứng cơ toàn thân
       - Điều trị: Dantrolene
    
    3. **Anticholinergic Toxicity:**
       - Đồng tử giãn, da khô, bí tiểu
       - Không có clonus
       - Điều trị: Physostigmine
    
    4. **Sympathomimetic Toxicity:**
       - Do cocaine, amphetamines
       - Tăng huyết áp, nhịp nhanh
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: REFERENCES ==========
    references = get_references("Serotonin Syndrome")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **Hunter Serotonin Toxicity Criteria** - Dunkley EJC, et al. QJM 2003
        2. **Sternbach H. The serotonin syndrome.** Am J Psychiatry. 1991
        3. **Boyer EW, Shannon M. The serotonin syndrome.** N Engl J Med. 2005
        4. **UpToDate:** Serotonin Syndrome - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_serotonin():
    """Mild Serotonin Syndrome"""
    st.success("## ⚠️ MILD SEROTONIN SYNDROME")
    
    st.markdown("""
    **Triệu chứng:**
    - Run nhẹ
    - Phản xạ tăng nhẹ
    - Lo âu, kích động nhẹ
    - Nhiệt độ bình thường hoặc tăng nhẹ
    
    **Điều trị:**
    1. **Ngừng thuốc serotonergic**
    2. **Theo dõi:** Mỗi 4-6 giờ
    3. **Benzodiazepine:** Nếu kích động (Lorazepam 1-2 mg)
    4. **Thường tự hết trong 24-48 giờ**
    
    **Tiên lượng:** Tốt, thường tự khỏi
    """)


def render_moderate_serotonin():
    """Moderate Serotonin Syndrome"""
    st.warning("## 🚨 MODERATE SEROTONIN SYNDROME")
    
    st.markdown("""
    **Triệu chứng:**
    - Clonus rõ ràng
    - Myoclonus
    - Kích động vừa
    - Nhiệt độ 38-39°C
    - Tăng huyết áp, nhịp nhanh
    
    **Điều trị:**
    1. **Ngừng thuốc serotonergic**
    2. **Benzodiazepine:** Lorazepam 2-4 mg IV/IM q4-6h
    3. **Hạ nhiệt:** Paracetamol, làm mát ngoài
    4. **Theo dõi:** Mỗi 2-4 giờ
    5. **Cyproheptadine:** 12 mg PO, sau đó 2 mg q2h nếu cần
    
    **Tiên lượng:** Tốt với điều trị, cải thiện trong 24-72 giờ
    """)


def render_severe_serotonin():
    """Severe Serotonin Syndrome"""
    st.error("## 🚨🚨 SEVERE SEROTONIN SYNDROME - ICU")
    
    st.markdown("""
    **Triệu chứng:**
    - Clonus tự phát
    - Myoclonus nặng
    - Hyperthermia >40°C
    - Rhabdomyolysis
    - Suy đa tạng
    - Có thể tử vong
    
    **Điều trị ngay:**
    1. **ICU:** Nhập ICU ngay
    2. **Ngừng thuốc serotonergic**
    3. **An thần:** Midazolam hoặc Propofol (nếu cần)
    4. **Hạ nhiệt tích cực:** Làm mát ngoài, có thể cần làm mát nội mạch
    5. **Cyproheptadine:** 12 mg PO/NG, sau đó 2 mg q2h (tối đa 32 mg/ngày)
    6. **Điều trị rhabdomyolysis:** Truyền dịch, theo dõi CK, chức năng thận
    7. **Theo dõi:** Liên tục
    
    **Tiên lượng:** Nghiêm trọng, cần điều trị tích cực
    """)

