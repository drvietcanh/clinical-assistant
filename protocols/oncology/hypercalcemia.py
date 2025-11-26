"""
Hypercalcemia of Malignancy Protocol
ASCO 2021 Guidelines
Management of hypercalcemia in cancer patients
"""

import streamlit as st


def render():
    """Hypercalcemia of Malignancy Protocol"""
    st.subheader("📈 Hypercalcemia of Malignancy")
    st.caption("ASCO 2021 Guidelines - Management of hypercalcemia in cancer patients")
    
    st.error("""
    **⚠️ CẤP CỨU - Cần điều trị ngay lập tức**
    
    **Hypercalcemia of Malignancy:**
    - Thường gặp trong ung thư (10-30% bệnh nhân)
    - Nguy cơ tử vong cao nếu không điều trị
    - Cần điều trị tích cực: Hydration + Bisphosphonates
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: SEVERITY ==========
    st.markdown("### 📊 Phân Loại Mức Độ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Severity (Total Ca):**
        
        **Mild (10.5-12.0 mg/dL):**
        - Thường không có triệu chứng
        - Có thể có mệt mỏi, yếu cơ nhẹ
        
        **Moderate (12.0-14.0 mg/dL):**
        - Triệu chứng rõ rệt
        - Buồn nôn, nôn, táo bón
        - Yếu cơ, mệt mỏi
        - Polydipsia, polyuria
        
        **Severe (>14.0 mg/dL):**
        - Triệu chứng nặng
        - Lú lẫn, hôn mê
        - Suy thận cấp
        - Loạn nhịp tim
        - Nguy cơ tử vong cao
        """)
    
    with col2:
        st.error("""
        **⚠️ Ionized Ca (iCa) - More Important:**
        
        **Normal:** 4.5-5.3 mg/dL (1.1-1.3 mmol/L)
        
        **Mild:** 5.3-6.0 mg/dL
        **Moderate:** 6.0-7.0 mg/dL
        **Severe:** >7.0 mg/dL
        
        **⚠️ Check iCa nếu:**
        - Albumin thấp
        - pH bất thường
        - Critical illness
        - Total Ca không phù hợp với triệu chứng
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CALCULATION ==========
    st.markdown("### 🧮 Tính Toán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_ca = st.number_input(
            "Total Ca hiện tại (mg/dL)",
            min_value=8.0,
            max_value=20.0,
            value=13.0,
            step=0.1,
            format="%.1f",
            key="hyperca_total"
        )
        
        albumin = st.number_input(
            "Albumin (g/dL)",
            min_value=1.0,
            max_value=5.0,
            value=4.0,
            step=0.1,
            format="%.1f",
            key="hyperca_albumin"
        )
        
        ionized_ca = st.number_input(
            "Ionized Ca (mg/dL) - nếu có",
            min_value=3.0,
            max_value=10.0,
            value=0.0,
            step=0.1,
            format="%.1f",
            key="hyperca_ionized"
        )
        
        symptoms = st.multiselect(
            "Triệu chứng:",
            ["Không có", "Buồn nôn/nôn", "Táo bón", "Yếu cơ", "Lú lẫn", "Suy thận", "Loạn nhịp"],
            key="hyperca_symptoms"
        )
    
    with col2:
        # Corrected Ca = Total Ca + 0.8 × (4.0 - Albumin)
        corrected_ca = total_ca + 0.8 * (4.0 - albumin)
        
        st.markdown("### 📊 Kết quả")
        
        st.metric("Total Ca", f"{total_ca:.1f} mg/dL")
        st.metric("Corrected Ca", f"{corrected_ca:.1f} mg/dL")
        
        if ionized_ca > 0:
            st.metric("Ionized Ca", f"{ionized_ca:.1f} mg/dL")
            if ionized_ca > 7.0:
                st.error("🚨 **SEVERE HYPERCALCEMIA** - Cần điều trị ngay!")
            elif ionized_ca > 6.0:
                st.warning("⚠️ **MODERATE HYPERCALCEMIA**")
            else:
                st.info("✅ Ionized Ca trong giới hạn")
        else:
            if corrected_ca > 14.0:
                st.error("🚨 **SEVERE HYPERCALCEMIA** - Cần điều trị ngay!")
            elif corrected_ca > 12.0:
                st.warning("⚠️ **MODERATE HYPERCALCEMIA**")
            else:
                st.info("✅ Corrected Ca trong giới hạn")
        
        if len(symptoms) > 0 and "Không có" not in symptoms:
            st.warning("⚠️ **Có triệu chứng** - Cần điều trị tích cực")
    
    st.markdown("---")
    
    # ========== SECTION 3: PATHOPHYSIOLOGY ==========
    st.markdown("### 🔬 Cơ Chế Bệnh Sinh")
    
    st.markdown("""
    **Hypercalcemia of Malignancy có 3 cơ chế chính:**
    
    **1. Humoral Hypercalcemia of Malignancy (HHM) - 80%:**
    - PTHrP (Parathyroid Hormone-Related Protein) tăng
    - Tăng tái hấp thu xương, tăng tái hấp thu thận
    - Giảm bài tiết Ca qua thận
    - Thường gặp: Squamous cell carcinoma, renal cell, breast
    
    **2. Local Osteolytic Hypercalcemia - 20%:**
    - Di căn xương trực tiếp
    - Cytokines (IL-1, TNF, TGF-β) kích thích hủy xương
    - Thường gặp: Multiple myeloma, breast, lung
    
    **3. Ectopic 1,25(OH)₂D Production - <1%:**
    - Lymphoma, granulomatous diseases
    - Tăng hấp thu Ca từ ruột
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT ==========
    st.markdown("### 💊 Điều Trị")
    
    st.markdown("""
    **Thứ tự ưu tiên điều trị:**
    """)
    
    # Step 1: Hydration
    st.markdown("#### **1. Hydration (Bước đầu tiên - QUAN TRỌNG)**")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Hydration trước khi dùng bisphosphonates**
    
    **Mục đích:**
    - Tăng bài tiết Ca qua thận
    - Điều chỉnh thể tích (thường mất nước)
    - Giảm nguy cơ suy thận do bisphosphonates
    
    **Protocol:**
    - **NS 0.9%:** 2-4 L trong 24h đầu
    - Hoặc 200-300 ml/h
    - Mục tiêu: Urine output >100 ml/h
    
    **⚠️ Lưu ý:**
    - Cẩn thận với heart failure
    - Có thể cần furosemide nếu quá tải
    - Theo dõi dấu hiệu quá tải dịch
    """)
    
    # Step 2: Bisphosphonates
    st.markdown("#### **2. Bisphosphonates (Điều Trị Chính)**")
    
    st.markdown("""
    **⚠️ CHỐNG CHỈ ĐỊNH:**
    - Creatinine >3.0 mg/dL (hoặc CrCl <30)
    - Hypocalcemia
    - Pregnancy
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Zoledronate (Lựa chọn hàng đầu):**
        
        **Liều:**
        - **4mg IV** trong 15 phút
        - Hoặc **4mg IV** trong 30 phút (nếu suy thận nhẹ)
        
        **Effect:**
        - Onset: 24-48h
        - Peak: 4-7 ngày
        - Duration: 2-4 tuần
        
        **Advantages:**
        - Hiệu quả nhất
        - Tác dụng dài
        - Liều đơn giản
        
        **⚠️ Precautions:**
        - Suy thận: Giảm liều hoặc tránh
        - Hypocalcemia: Bổ sung Ca và Vitamin D
        - Osteonecrosis of jaw (hiếm)
        - Acute phase reaction (sốt, đau cơ) - 24-48h đầu
        """)
    
    with col2:
        st.info("""
        **Pamidronate (Thay thế):**
        
        **Liều:**
        - **60-90mg IV** trong 2-4h
        - Hoặc 90mg IV trong 4h (nếu Ca >13.5)
        
        **Effect:**
        - Onset: 24-48h
        - Peak: 4-7 ngày
        - Duration: 2-4 tuần
        
        **Advantages:**
        - Hiệu quả tốt
        - Tác dụng dài
        
        **Disadvantages:**
        - Truyền lâu hơn (2-4h)
        - Có thể cần liều cao hơn
        
        **⚠️ Precautions:**
        - Tương tự zoledronate
        """)
    
    st.markdown("""
    **Repeat dosing:**
    - Lặp lại sau 2-4 tuần nếu Ca tăng lại
    - Hoặc dùng định kỳ để phòng ngừa
    """)
    
    # Step 3: Calcitonin
    st.markdown("#### **3. Calcitonin (Nếu cần tác dụng nhanh)**")
    
    st.warning("""
    **Chỉ Định:**
    - Severe hypercalcemia (>14 mg/dL)
    - Cần tác dụng nhanh (trong khi chờ bisphosphonates)
    - Không đáp ứng hydration
    
    **Liều:**
    - **Salmon calcitonin:** 4-8 IU/kg IM/SC q6-12h
    - Hoặc 200-400 IU IM/SC q6-12h
    
    **Effect:**
    - Onset: 2-4h
    - Peak: 6-12h
    - Duration: 24-48h (tachyphylaxis)
    
    **Advantages:**
    - Tác dụng nhanh
    - An toàn
    
    **Disadvantages:**
    - Tác dụng ngắn
    - Tachyphylaxis (mất tác dụng sau 2-3 ngày)
    - Chỉ giảm Ca 1-2 mg/dL
    
    **⚠️ Lưu ý:**
    - Dùng kết hợp với bisphosphonates
    - Không dùng đơn độc
    """)
    
    # Step 4: Denosumab
    st.markdown("#### **4. Denosumab (Nếu Bisphosphonates Chống Chỉ Định)**")
    
    st.info("""
    **Chỉ Định:**
    - Suy thận nặng (CrCl <30)
    - Không dung nạp bisphosphonates
    - Không đáp ứng bisphosphonates
    
    **Liều:**
    - **120mg SC** q4 tuần
    - Hoặc **120mg SC** q2 tuần (nếu Ca rất cao)
    
    **Effect:**
    - Onset: 2-4 ngày
    - Peak: 7-10 ngày
    - Duration: 4-8 tuần
    
    **Advantages:**
    - Dùng được trong suy thận
    - Hiệu quả tốt
    
    **Disadvantages:**
    - Đắt tiền
    - Tác dụng chậm hơn bisphosphonates
    - Risk hypocalcemia (bổ sung Ca và Vitamin D)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Monitoring")
    
    st.markdown("""
    **During treatment:**
    - **Ca²⁺:** Mỗi 12-24h (đến khi ổn định)
    - **Creatinine:** Mỗi 24-48h
    - **Phosphate:** Mỗi 24-48h (risk hypophosphatemia)
    - **Magnesium:** Mỗi 24-48h (risk hypomagnesemia)
    - **ECG:** Nếu có loạn nhịp
    
    **After treatment:**
    - **Ca²⁺:** Mỗi 1-2 tuần
    - **Creatinine:** Mỗi 1-2 tuần
    - **Phosphate, Magnesium:** Mỗi 1-2 tuần
    
    **Dấu hiệu cải thiện:**
    - ✅ Ca²⁺ giảm về <12 mg/dL
    - ✅ Triệu chứng cải thiện
    - ✅ Creatinine ổn định
    
    **Dấu hiệu cảnh báo:**
    - ⚠️ Ca²⁺ không giảm sau 48-72h
    - ⚠️ Creatinine tăng
    - ⚠️ Hypocalcemia (sau bisphosphonates)
    - ⚠️ Hypophosphatemia, hypomagnesemia
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SPECIAL CONSIDERATIONS ==========
    st.markdown("### 👥 Các Trường Hợp Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Suy thận:**
        - Hydration cẩn thận
        - Tránh bisphosphonates nếu CrCl <30
        - Dùng Denosumab thay thế
        - Có thể cần dialysis
        
        **Heart failure:**
        - Hydration cẩn thận
        - Có thể cần furosemide
        - Theo dõi dấu hiệu quá tải
        
        **Multiple Myeloma:**
        - Thường đáp ứng tốt với bisphosphonates
        - Có thể dùng định kỳ để phòng ngừa
        """)
    
    with col2:
        st.markdown("""
        **Squamous Cell Carcinoma:**
        - Thường do PTHrP
        - Đáp ứng tốt với bisphosphonates
        - Có thể cần điều trị khối u
        
        **Breast Cancer:**
        - Thường do di căn xương
        - Đáp ứng tốt với bisphosphonates
        - Có thể dùng định kỳ
        
        **Lymphoma:**
        - Có thể do 1,25(OH)₂D
        - Điều trị khối u là chính
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: LONG-TERM MANAGEMENT ==========
    st.markdown("### 🔄 Điều Trị Dài Hạn")
    
    st.markdown("""
    **Prevention of recurrence:**
    
    **1. Bisphosphonates định kỳ:**
    - Zoledronate 4mg IV q3-4 tuần
    - Hoặc Pamidronate 60-90mg IV q3-4 tuần
    - Đặc biệt trong multiple myeloma, breast cancer
    
    **2. Denosumab:**
    - 120mg SC q4 tuần
    - Nếu không dung nạp bisphosphonates
    
    **3. Điều trị khối u:**
    - Điều trị ung thư là chính
    - Hypercalcemia thường tái phát nếu khối u không được điều trị
    
    **4. Monitoring:**
    - Ca²⁺ mỗi 1-2 tuần
    - Creatinine mỗi 1-2 tuần
    - Điều chỉnh liều nếu cần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    st.markdown("""
    1. **ASCO Clinical Practice Guideline** - Management of Hypercalcemia of Malignancy (2021)
       - Treatment protocols
       - Monitoring guidelines
    
    2. **UpToDate:** Hypercalcemia of Malignancy - Last updated 2024
       - Clinical features and diagnosis
       - Treatment protocols
    
    3. **Stewart AF.** Hypercalcemia associated with cancer.
       N Engl J Med. 2005;352(4):373-379.
    
    4. **Major P, et al.** Zoledronic acid is superior to pamidronate in the treatment of hypercalcemia of malignancy: a pooled analysis of two randomized, controlled clinical trials.
       J Clin Oncol. 2001;19(2):558-567.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. Hypercalcemia of Malignancy là cấp cứu, cần điều trị tích cực với hydration và bisphosphonates.")

