"""
Neuroleptic Malignant Syndrome (NMS) Protocol
Life-threatening reaction to antipsychotic medications
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Neuroleptic Malignant Syndrome Protocol"""
    st.subheader("🧠 Hội chứng ác tính do thuốc chống loạn thần (NMS)")
    st.caption("Neuroleptic Malignant Syndrome - Life-threatening antipsychotic reaction")
    
    st.error("""
    **⚠️ NMS = CẤP CỨU Y TẾ - TỶ LỆ TỬ VONG 10-20%**
    
    **Định nghĩa:**
    - Phản ứng hiếm gặp nhưng nguy hiểm với thuốc chống loạn thần
    - Tỷ lệ: 0.01-0.02% bệnh nhân dùng thuốc chống loạn thần
    - Tỷ lệ tử vong: 10-20% nếu không điều trị
    
    **Nguyên nhân:**
    - Thuốc chống loạn thần: Haloperidol, Risperidone, Olanzapine, v.v.
    - Thuốc chống nôn: Metoclopramide, Prochlorperazine
    - Ngừng đột ngột thuốc chống Parkinson (levodopa)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    st.warning("""
    **Chẩn đoán NMS khi có TẤT CẢ 4 tiêu chuẩn sau:**
    
    1. **Cứng cơ (Muscle Rigidity):**
       - Cứng cơ toàn thân
       - "Lead pipe" rigidity
       - Có thể kèm myoclonus
    
    2. **Sốt (Hyperthermia):**
       - Nhiệt độ >38°C (thường >39-40°C)
       - Không do nhiễm trùng
    
    3. **Rối loạn tự chủ (Autonomic Dysfunction):**
       - Tăng huyết áp hoặc huyết áp không ổn định
       - Nhịp nhanh
       - Vã mồ hôi
       - Tăng nhịp thở
    
    4. **Thay đổi tâm thần (Altered Mental Status):**
       - Lú lẫn
       - Kích động
       - Stupor
       - Hôn mê
    
    **VÀ:**
    - Đang dùng thuốc chống loạn thần hoặc vừa ngừng levodopa
    - Loại trừ: Nhiễm trùng, rối loạn chuyển hóa, nguyên nhân khác
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng chính:**
        - **Cứng cơ:** Toàn thân, "lead pipe"
        - **Sốt:** >38°C, thường 39-42°C
        - **Rối loạn tự chủ:**
          - Tăng huyết áp
          - Nhịp nhanh
          - Vã mồ hôi
          - Tăng nhịp thở
        
        **Triệu chứng khác:**
        - Rhabdomyolysis
        - Tăng CK (Creatine Kinase)
        - Tăng WBC
        - Tăng transaminase
        """)
    
    with col2:
        st.markdown("""
        **Thay đổi tâm thần:**
        - Lú lẫn
        - Kích động
        - Stupor
        - Hôn mê
        
        **Biến chứng:**
        - Suy thận cấp (do rhabdomyolysis)
        - Suy hô hấp
        - Suy đa tạng
        - DIC (hiếm)
        - Tử vong (10-20%)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: RISK FACTORS ==========
    st.markdown("### ⚠️ Yếu tố nguy cơ")
    
    st.info("""
    **Yếu tố nguy cơ:**
    - Dùng thuốc chống loạn thần liều cao
    - Tăng liều nhanh
    - Dùng thuốc chống loạn thần dạng depot
    - Mất nước
    - Nhiệt độ môi trường cao
    - Kích động, căng thẳng
    - Tiền sử NMS
    - Nam giới, trẻ tuổi
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### **1. Ngừng ngay thuốc chống loạn thần**")
    st.error("""
    **NGỪNG NGAY:**
    - Tất cả thuốc chống loạn thần
    - Thuốc chống nôn (nếu đang dùng)
    - Không dùng lại cho đến khi hết NMS
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Hỗ trợ (Supportive Care) - QUAN TRỌNG NHẤT**")
    
    st.success("""
    **Điều trị hỗ trợ (Ưu tiên hàng đầu):**
    
    **A. Hạ nhiệt:**
    - Làm mát ngoài: Chườm lạnh, quạt
    - Paracetamol: 1g IV/PO q6h
    - Có thể cần làm mát nội mạch nếu sốt cao
    
    **B. Bù dịch:**
    - Truyền dịch tích cực (do mất nước, rhabdomyolysis)
    - Theo dõi cân bằng dịch
    
    **C. Điều chỉnh rối loạn tự chủ:**
    - Hạ huyết áp: Nếu cần (thận trọng)
    - Điều chỉnh nhịp tim
    
    **D. Điều trị rhabdomyolysis:**
    - Truyền dịch tích cực
    - Theo dõi CK, chức năng thận
    - Có thể cần lọc máu nếu suy thận
    """)
    
    st.markdown("---")
    
    st.markdown("#### **3. Điều trị đặc hiệu (Nếu nặng hoặc không cải thiện)**")
    
    st.warning("""
    **Dantrolene (Giãn cơ):**
    - **Liều:** 1-2.5 mg/kg IV q6h
    - **Tối đa:** 10 mg/kg/ngày
    - **Hoặc:** 50-200 mg PO q6h
    - **Lưu ý:** Có thể gây suy gan
    
    **Bromocriptine (Dopamine agonist):**
    - **Liều:** 2.5-5 mg PO q8h
    - **Tăng dần:** Lên đến 20-40 mg/ngày
    - **Lưu ý:** Có thể gây hạ huyết áp, nôn
    
    **Amantadine:**
    - **Liều:** 100-200 mg PO BID
    - **Lưu ý:** Có thể dùng thay thế bromocriptine
    
    **Benzodiazepines:**
    - Lorazepam: 1-2 mg IV q4-6h
    - Giúp giãn cơ, an thần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Nhiệt độ:** Mỗi 1-2 giờ
    - **Huyết áp, nhịp tim:** Liên tục
    - **CK (Creatine Kinase):** Mỗi 12-24 giờ
    - **Chức năng thận:** Creatinine, BUN, nước tiểu
    - **Chức năng gan:** AST, ALT
    - **CBC:** WBC thường tăng
    - **Triệu chứng thần kinh:** Mỗi 2-4 giờ
    
    **Dấu hiệu cải thiện:**
    - Giảm nhiệt độ
    - Giảm cứng cơ
    - Cải thiện ý thức
    - Giảm CK
    
    **Dấu hiệu xấu đi:**
    - Nhiệt độ >41°C
    - Rhabdomyolysis nặng
    - Suy thận cấp
    - Suy đa tạng
    - Cần ICU
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: DIFFERENTIAL DIAGNOSIS ==========
    st.markdown("### 🔄 Chẩn đoán phân biệt")
    
    st.markdown("""
    **Cần phân biệt với:**
    
    1. **Serotonin Syndrome:**
       - Do thuốc serotonergic
       - Clonus > cứng cơ
       - Khởi phát nhanh (giờ)
       - Điều trị: Cyproheptadine
    
    2. **Malignant Hyperthermia:**
       - Do thuốc mê (halothane, succinylcholine)
       - Cứng cơ toàn thân
       - Khởi phát trong phẫu thuật
       - Điều trị: Dantrolene
    
    3. **Catatonia:**
       - Cứng cơ, nhưng không sốt
       - Điều trị: Benzodiazepines, ECT
    
    4. **Heat Stroke:**
       - Sốt cao, nhưng không cứng cơ
       - Tiền sử tiếp xúc nhiệt
    
    5. **Infection:**
       - Sốt, nhưng không cứng cơ
       - Có nguồn nhiễm trùng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PROGNOSIS ==========
    st.markdown("### 📊 Tiên lượng")
    
    st.info("""
    **Tiên lượng:**
    - **Tỷ lệ tử vong:** 10-20% (nếu không điều trị)
    - **Thời gian hồi phục:** 7-14 ngày (có thể lâu hơn)
    - **Yếu tố tiên lượng xấu:**
      - Nhiệt độ >41°C
      - Rhabdomyolysis nặng
      - Suy đa tạng
      - Chẩn đoán muộn
    
    **Phòng ngừa tái phát:**
    - Tránh thuốc chống loạn thần trong 2-4 tuần
    - Khi cần dùng lại: Bắt đầu liều thấp, tăng từ từ
    - Theo dõi sát các dấu hiệu NMS
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    references = get_references("Neuroleptic Malignant Syndrome")
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
        1. **Gurrera RJ, et al. An international consensus study of neuroleptic malignant syndrome diagnostic criteria using the Delphi method.** J Clin Psychiatry. 2011
        2. **Strawn JR, et al. Neuroleptic malignant syndrome.** Am J Psychiatry. 2007
        3. **UpToDate:** Neuroleptic Malignant Syndrome - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

