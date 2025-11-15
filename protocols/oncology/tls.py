"""
Tumor Lysis Syndrome (TLS) Prevention Protocol
NCCN 2023 Guidelines
Prevention and management of TLS in hematologic malignancies
"""

import streamlit as st


def render():
    """Tumor Lysis Syndrome (TLS) Prevention Protocol"""
    st.subheader("🎗️ Tumor Lysis Syndrome (TLS) Prevention")
    st.caption("NCCN 2023 Guidelines - Prevention and management of TLS")
    
    st.error("""
    **⚠️ QUAN TRỌNG: TLS là biến chứng đe dọa tính mạng**
    
    **TLS xảy ra khi:**
    - Tế bào ung thư bị phá hủy nhanh (hóa trị, xạ trị)
    - Giải phóng nội dung tế bào vào máu
    - Gây tăng uric acid, K⁺, PO₄³⁻, giảm Ca²⁺
    - Có thể dẫn đến suy thận cấp, loạn nhịp tim, tử vong
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK STRATIFICATION ==========
    st.markdown("### 📊 Phân Tầng Nguy Cơ (Risk Stratification)")
    
    st.markdown("""
    **Theo NCCN 2023, phân loại nguy cơ TLS:**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **🔴 HIGH RISK:**
        
        **Hematologic:**
        - ALL (Burkitt, T-cell) với WBC >100k
        - AML với WBC >50k
        - High-grade NHL (Burkitt, lymphoblastic)
        - CLL với WBC >100k và bulky disease
        
        **Solid tumors:**
        - Germ cell tumors (bulky)
        - Small cell lung cancer (extensive)
        - Neuroblastoma (high-risk)
        """)
    
    with col2:
        st.warning("""
        **🟡 INTERMEDIATE RISK:**
        
        **Hematologic:**
        - ALL (standard risk)
        - AML (standard risk)
        - Intermediate-grade NHL
        - CLL với WBC 25-100k
        
        **Solid tumors:**
        - Germ cell tumors (non-bulky)
        - Breast cancer (high tumor burden)
        """)
    
    st.success("""
    **🟢 LOW RISK:**
    
    - Most solid tumors
    - Low-grade lymphomas
    - CLL với WBC <25k
    - Multiple myeloma (standard risk)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: LABORATORY CRITERIA ==========
    st.markdown("### 🧪 Tiêu Chuẩn Xét Nghiệm (Laboratory TLS)")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán TLS", expanded=True):
        st.markdown("""
        **Chẩn đoán Laboratory TLS khi có ≥2 trong 4 tiêu chuẩn (trong 3 ngày trước hoặc 7 ngày sau hóa trị):**
        
        **1. Uric acid:**
        - Tăng >25% so với baseline
        - Hoặc >8 mg/dL (476 µmol/L) ở người lớn
        - Hoặc >6.5 mg/dL (387 µmol/L) ở trẻ em
        
        **2. Potassium:**
        - Tăng >25% so với baseline
        - Hoặc >6.0 mEq/L (6.0 mmol/L)
        
        **3. Phosphate:**
        - Tăng >25% so với baseline
        - Hoặc >4.5 mg/dL (1.45 mmol/L) ở người lớn
        - Hoặc >6.5 mg/dL (2.1 mmol/L) ở trẻ em
        
        **4. Calcium:**
        - Giảm >25% so với baseline
        - Hoặc <7.0 mg/dL (1.75 mmol/L)
        - Hoặc ionized Ca <1.0 mmol/L
        """)
        
        st.warning("""
        **⚠️ Clinical TLS = Laboratory TLS + ≥1 clinical manifestation:**
        - Creatinine tăng (≥1.5 × ULN)
        - Loạn nhịp tim
        - Co giật
        - Đột tử
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: PREVENTION PROTOCOL ==========
    st.markdown("### 🛡️ Phác Đồ Phòng Ngừa")
    
    risk_level = st.radio(
        "**Mức độ nguy cơ:**",
        ["High Risk", "Intermediate Risk", "Low Risk"],
        key="tls_risk"
    )
    
    st.markdown("---")
    
    if "High" in risk_level:
        render_high_risk_protocol()
    elif "Intermediate" in risk_level:
        render_intermediate_risk_protocol()
    else:
        render_low_risk_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 4: HYDRATION ==========
    st.markdown("### 💧 Hydration Protocol")
    
    st.info("""
    **Hydration là nền tảng của TLS prevention:**
    
    **Goal:**
    - Duy trì urine output >100 ml/h (người lớn)
    - Hoặc >2 ml/kg/h (trẻ em)
    - Giảm nguy cơ kết tinh uric acid trong thận
    
    **Protocol:**
    - **NS 0.9% hoặc D5W:** 2-3 L/m²/ngày
    - Hoặc 200-300 ml/h (người lớn)
    - Bắt đầu 24-48h trước hóa trị
    - Tiếp tục trong và sau hóa trị
    
    **⚠️ Lưu ý:**
    - Cẩn thận với heart failure, renal failure
    - Theo dõi dấu hiệu quá tải dịch
    - Có thể cần furosemide nếu quá tải
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: URIC ACID LOWERING ==========
    st.markdown("### 💊 Điều Trị Hạ Uric Acid")
    
    tab1, tab2 = st.tabs(["Allopurinol", "Rasburicase"])
    
    with tab1:
        st.markdown("#### Allopurinol")
        
        st.success("""
        **Chỉ định:**
        - Low to intermediate risk
        - Không có G6PD deficiency
        - Không có hyperuricemia nặng (>10 mg/dL)
        
        **Dosing:**
        - **Loading:** 600-900mg PO/ngày (chia 2-3 lần)
        - **Maintenance:** 300-600mg PO/ngày
        - **Pediatric:** 10 mg/kg/ngày (max 600mg/ngày)
        
        **Bắt đầu:**
        - 24-48h trước hóa trị
        - Tiếp tục 7-10 ngày sau hóa trị
        
        **Mechanism:**
        - Ức chế xanthine oxidase
        - Ngăn tạo uric acid từ purines
        - Không phá hủy uric acid đã có
        
        **⚠️ Lưu ý:**
        - Không hiệu quả nếu uric acid đã cao
        - Có thể gây phát ban, Stevens-Johnson (hiếm)
        - Điều chỉnh liều nếu suy thận
        """)
    
    with tab2:
        st.markdown("#### Rasburicase")
        
        st.error("""
        **Chỉ định:**
        - **High risk TLS**
        - Hyperuricemia nặng (>10 mg/dL)
        - Laboratory TLS đã xảy ra
        - Không đáp ứng allopurinol
        
        **⚠️ CHỐNG CHỈ ĐỊNH:**
        - G6PD deficiency (risk hemolysis)
        - Methemoglobinemia
        
        **Dosing:**
        - **0.15-0.2 mg/kg IV** trong 30 phút
        - **Mỗi ngày × 5-7 ngày**
        - Hoặc đến khi uric acid <7.5 mg/dL
        
        **Bắt đầu:**
        - 4-24h trước hóa trị (high risk)
        - Ngay khi có laboratory TLS
        
        **Mechanism:**
        - Enzyme chuyển uric acid → allantoin (hòa tan tốt)
        - Phá hủy uric acid đã có
        - Tác dụng nhanh (vài giờ)
        
        **Monitoring:**
        - Uric acid mỗi 4-6h
        - Hemoglobin, methemoglobin (nếu có triệu chứng)
        - Ngừng nếu hemolysis hoặc methemoglobinemia
        
        **⚠️ Lưu ý:**
        - Đắt tiền
        - Cần bảo quản lạnh
        - Không dùng với allopurinol (không cần thiết)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: ELECTROLYTE MANAGEMENT ==========
    st.markdown("### ⚡ Điều Chỉnh Điện Giải")
    
    st.markdown("""
    **1. Hyperkalemia:**
    - Xem protocol Hyperkalemia
    - Điều trị ngay nếu K⁺ >6.0 hoặc có ECG changes
    - Có thể cần dialysis
    
    **2. Hyperphosphatemia:**
    - Xem protocol Hypophosphatemia (reverse)
    - Phosphate binders: Sevelamer, Calcium acetate
    - Có thể cần dialysis
    
    **3. Hypocalcemia:**
    - Xem protocol Hypocalcemia
    - Chỉ bổ sung nếu symptomatic hoặc iCa <1.0
    - ⚠️ Không bổ sung nếu PO4 cao (risk precipitation)
    
    **4. Renal Protection:**
    - Hydration đầy đủ
    - Tránh nephrotoxic drugs
    - Có thể cần dialysis
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Monitoring Protocol")
    
    st.markdown("""
    **Baseline (trước hóa trị):**
    - CBC, BMP (K⁺, PO₄³⁻, Ca²⁺, Cr, BUN)
    - Uric acid
    - LDH
    - ECG (nếu có nguy cơ cao)
    
    **During treatment:**
    - **High risk:** Mỗi 6-12h × 3-5 ngày
    - **Intermediate risk:** Mỗi 12-24h × 3-5 ngày
    - **Low risk:** Mỗi 24-48h
    
    **Parameters to monitor:**
    - Uric acid (mục tiêu: <7.5 mg/dL)
    - K⁺ (mục tiêu: <5.5 mEq/L)
    - PO₄³⁻ (mục tiêu: <4.5 mg/dL)
    - Ca²⁺, ionized Ca
    - Creatinine, BUN
    - Urine output
    - ECG (nếu có hyperkalemia)
    
    **Dấu hiệu cảnh báo:**
    - ⚠️ Creatinine tăng >1.5 × baseline
    - ⚠️ Uric acid >10 mg/dL
    - ⚠️ K⁺ >6.0 hoặc ECG changes
    - ⚠️ PO₄³⁻ >6.5 mg/dL
    - 🚨 Oliguria/anuria
    - 🚨 Loạn nhịp tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: TREATMENT OF ESTABLISHED TLS ==========
    st.markdown("### 🚨 Điều Trị TLS Đã Xảy Ra")
    
    st.error("""
    **Nếu Laboratory TLS đã xảy ra:**
    
    **1. Tăng cường hydration:**
    - 3-4 L/m²/ngày
    - Hoặc 300-400 ml/h
    - Có thể cần furosemide
    
    **2. Rasburicase (nếu chưa dùng):**
    - 0.15-0.2 mg/kg IV ngay
    - Lặp lại mỗi ngày đến khi uric acid <7.5
    
    **3. Điều chỉnh điện giải:**
    - Hyperkalemia: Calcium, Insulin+D50, Kayexalate
    - Hyperphosphatemia: Phosphate binders
    - Hypocalcemia: Chỉ nếu symptomatic và PO4 không cao
    
    **4. Dialysis indications:**
    - Creatinine tăng nhanh
    - Oliguria/anuria
    - K⁺ >6.5 không đáp ứng
    - PO₄³⁻ >6.5 mg/dL
    - Uric acid >10 mg/dL
    - Volume overload
    
    **5. Tạm hoãn hóa trị:**
    - Nếu TLS nặng
    - Đợi TLS ổn định
    - Giảm liều hóa trị sau đó
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Dân Số Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Nguy cơ cao hơn (tỷ lệ tế bào/tổng khối lượng cao)
        - Hydration: 2-3 L/m²/ngày
        - Allopurinol: 10 mg/kg/ngày
        - Rasburicase: 0.15-0.2 mg/kg
        - Theo dõi sát hơn
        
        **Suy thận:**
        - Giảm liều allopurinol
        - Cẩn thận với hydration
        - Có thể cần dialysis sớm
        """)
    
    with col2:
        st.markdown("""
        **Heart failure:**
        - Cẩn thận với hydration
        - Có thể cần furosemide
        - Theo dõi dấu hiệu quá tải
        
        **G6PD deficiency:**
        - ⚠️ CHỐNG CHỈ ĐỊNH Rasburicase
        - Chỉ dùng Allopurinol
        - Theo dõi hemolysis
        """)
    
    st.markdown("---")
    
    # ========== SECTION 10: REFERENCES ==========
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    st.markdown("""
    1. **NCCN Clinical Practice Guidelines in Oncology** - Tumor Lysis Syndrome (Version 2023)
       - Risk stratification
       - Prevention protocols
       - Management guidelines
    
    2. **Cairo MS, et al.** Recommendations for the evaluation of risk and prophylaxis of tumour lysis syndrome (TLS) in adults and children with malignant diseases: an expert TLS panel consensus.
       Br J Haematol. 2010;149(4):578-586.
    
    3. **UpToDate:** Tumor Lysis Syndrome - Last updated 2024
       - Clinical features and diagnosis
       - Prevention and treatment protocols
    
    4. **Howard SC, et al.** The tumor lysis syndrome.
       N Engl J Med. 2011;364(19):1844-1854.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. TLS là biến chứng đe dọa tính mạng, cần phòng ngừa và điều trị tích cực.")


def render_high_risk_protocol():
    """High Risk TLS Prevention Protocol"""
    st.error("## 🔴 HIGH RISK TLS PREVENTION PROTOCOL")
    
    st.markdown("""
    **1. Hydration:**
    - **2-3 L/m²/ngày** NS hoặc D5W
    - Bắt đầu **24-48h trước hóa trị**
    - Duy trì trong và sau hóa trị
    - Mục tiêu: Urine output >100 ml/h
    
    **2. Rasburicase:**
    - **0.15-0.2 mg/kg IV** trong 30 phút
    - Bắt đầu **4-24h trước hóa trị**
    - Lặp lại mỗi ngày × 5-7 ngày
    - Hoặc đến khi uric acid <7.5 mg/dL
    
    **3. Monitoring:**
    - **Mỗi 6-12h × 3-5 ngày:**
      * Uric acid
      * K⁺, PO₄³⁻, Ca²⁺
      * Creatinine, BUN
      * Urine output
    - ECG nếu có hyperkalemia
    
    **4. Consider:**
    - Nephrology consult sớm
    - Prepare for dialysis nếu cần
    - ICU monitoring nếu có nguy cơ cao
    """)


def render_intermediate_risk_protocol():
    """Intermediate Risk TLS Prevention Protocol"""
    st.warning("## 🟡 INTERMEDIATE RISK TLS PREVENTION PROTOCOL")
    
    st.markdown("""
    **1. Hydration:**
    - **2-3 L/m²/ngày** NS hoặc D5W
    - Bắt đầu **24h trước hóa trị**
    - Duy trì trong và sau hóa trị
    - Mục tiêu: Urine output >100 ml/h
    
    **2. Allopurinol:**
    - **600-900mg PO/ngày** (chia 2-3 lần)
    - Bắt đầu **24-48h trước hóa trị**
    - Tiếp tục **7-10 ngày sau hóa trị**
    - Hoặc chuyển sang Rasburicase nếu uric acid >10 mg/dL
    
    **3. Monitoring:**
    - **Mỗi 12-24h × 3-5 ngày:**
      * Uric acid
      * K⁺, PO₄³⁻, Ca²⁺
      * Creatinine, BUN
      * Urine output
    
    **4. Escalate to Rasburicase nếu:**
    - Uric acid >10 mg/dL
    - Laboratory TLS xảy ra
    - Không đáp ứng allopurinol
    """)


def render_low_risk_protocol():
    """Low Risk TLS Prevention Protocol"""
    st.success("## 🟢 LOW RISK TLS PREVENTION PROTOCOL")
    
    st.markdown("""
    **1. Hydration:**
    - **1.5-2 L/m²/ngày** NS hoặc D5W
    - Bắt đầu **ngày hóa trị**
    - Duy trì 2-3 ngày sau hóa trị
    
    **2. Allopurinol (optional):**
    - **300-600mg PO/ngày**
    - Nếu có nguy cơ tăng uric acid
    - Bắt đầu ngày hóa trị
    
    **3. Monitoring:**
    - **Mỗi 24-48h × 2-3 ngày:**
      * Uric acid
      * K⁺, PO₄³⁻, Ca²⁺
      * Creatinine
    
    **4. Escalate nếu:**
    - Uric acid tăng nhanh
    - Có dấu hiệu TLS
    """)

