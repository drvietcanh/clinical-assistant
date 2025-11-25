"""
Phác đồ phòng ngừa hội chứng tan u (TLS)
Hướng dẫn NCCN 2023
Phòng ngừa và điều trị TLS trong các bệnh ác tính huyết học
"""

import streamlit as st


def render():
    """Phác đồ phòng ngừa hội chứng tan u (TLS)"""
    st.subheader("🎗️ Phòng ngừa hội chứng tan u (TLS)")
    st.caption("Hướng dẫn NCCN 2023 - Phòng ngừa và điều trị TLS")
    
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
    st.markdown("### 📊 Phân Tầng Nguy Cơ")
    
    st.markdown("""
    **Theo NCCN 2023, phân loại nguy cơ TLS:**
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **🔴 NGUY CƠ CAO:**
        
        **Huyết học:**
        - ALL (Burkitt, T-cell) với WBC >100k
        - AML với WBC >50k
        - U lympho không Hodgkin độ cao (Burkitt, lymphoblastic)
        - CLL với WBC >100k và bệnh khối lớn
        
        **Khối u đặc:**
        - U tế bào mầm (khối lớn)
        - Ung thư phổi tế bào nhỏ (lan rộng)
        - U nguyên bào thần kinh (nguy cơ cao)
        """)
    
    with col2:
        st.warning("""
        **🟡 NGUY CƠ TRUNG BÌNH:**
        
        **Huyết học:**
        - ALL (nguy cơ chuẩn)
        - AML (nguy cơ chuẩn)
        - U lympho không Hodgkin độ trung bình
        - CLL với WBC 25-100k
        
        **Khối u đặc:**
        - U tế bào mầm (không khối lớn)
        - Ung thư vú (khối u lớn)
        """)
    
    st.success("""
    **🟢 NGUY CƠ THẤP:**
    
    - Hầu hết các khối u đặc
    - U lympho độ thấp
    - CLL với WBC <25k
    - Đa u tủy xương (nguy cơ chuẩn)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: LABORATORY CRITERIA ==========
    st.markdown("### 🧪 Tiêu Chuẩn Xét Nghiệm (Laboratory TLS)")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán TLS", expanded=True):
        st.markdown("""
        **Chẩn đoán Laboratory TLS khi có ≥2 trong 4 tiêu chuẩn (trong 3 ngày trước hoặc 7 ngày sau hóa trị):**
        
        **1. Uric acid:**
        - Tăng >25% so với ban đầu
        - Hoặc >8 mg/dL (476 µmol/L) ở người lớn
        - Hoặc >6.5 mg/dL (387 µmol/L) ở trẻ em
        
        **2. Kali:**
        - Tăng >25% so với ban đầu
        - Hoặc >6.0 mEq/L (6.0 mmol/L)
        
        **3. Phosphate:**
        - Tăng >25% so với ban đầu
        - Hoặc >4.5 mg/dL (1.45 mmol/L) ở người lớn
        - Hoặc >6.5 mg/dL (2.1 mmol/L) ở trẻ em
        
        **4. Calci:**
        - Giảm >25% so với ban đầu
        - Hoặc <7.0 mg/dL (1.75 mmol/L)
        - Hoặc calci ion hóa <1.0 mmol/L
        """)
        
        st.warning("""
        **⚠️ Clinical TLS = Laboratory TLS + ≥1 biểu hiện lâm sàng:**
        - Creatinine tăng (≥1.5 × giới hạn trên bình thường)
        - Loạn nhịp tim
        - Co giật
        - Đột tử
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: PREVENTION PROTOCOL ==========
    st.markdown("### 🛡️ Phác Đồ Phòng Ngừa")
    
    risk_level = st.radio(
        "**Mức độ nguy cơ:**",
        ["Nguy cơ cao", "Nguy cơ trung bình", "Nguy cơ thấp"],
        key="tls_risk"
    )
    
    st.markdown("---")
    
    if "cao" in risk_level:
        render_high_risk_protocol()
    elif "trung bình" in risk_level:
        render_intermediate_risk_protocol()
    else:
        render_low_risk_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 4: HYDRATION ==========
    st.markdown("### 💧 Phác Đồ Bù Dịch")
    
    st.info("""
    **Bù dịch là nền tảng của phòng ngừa TLS:**
    
    **Mục Tiêu:**
    - Duy trì lượng nước tiểu >100 ml/h (Người Lớn)
    - Hoặc >2 ml/kg/h (Trẻ Em)
    - Giảm nguy cơ kết tinh uric acid trong thận
    
    **Phác đồ:**
    - **Natri clorid 0.9% hoặc Dextrose 5%:** 2-3 L/m²/ngày
    - Hoặc 200-300 ml/h (Người Lớn)
    - Bắt đầu 24-48h trước hóa trị
    - Tiếp tục trong và sau hóa trị
    
    **⚠️ Lưu ý:**
    - Cẩn thận với suy tim, suy thận
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
        **Chỉ Định:**
        - Nguy cơ thấp đến trung bình
        - Không có thiếu hụt G6PD
        - Không có tăng uric acid máu nặng (>10 mg/dL)
        
        **Liều dùng:**
        - **Liều tải:** 600-900mg uống/ngày (chia 2-3 lần)
        - **Liều duy trì:** 300-600mg uống/ngày
        - **Trẻ em:** 10 mg/kg/ngày (tối đa 600mg/ngày)
        
        **Bắt đầu:**
        - 24-48h trước hóa trị
        - Tiếp tục 7-10 ngày sau hóa trị
        
        **Cơ chế:**
        - Ức chế xanthine oxidase
        - Ngăn tạo uric acid từ purines
        - Không phá hủy uric acid đã có
        
        **⚠️ Lưu ý:**
        - Không hiệu quả nếu uric acid đã cao
        - Có thể gây phát ban, hội chứng Stevens-Johnson (hiếm)
        - Điều chỉnh liều nếu suy thận
        """)
    
    with tab2:
        st.markdown("#### Rasburicase")
        
        st.error("""
        **Chỉ Định:**
        - **TLS nguy cơ cao**
        - Tăng uric acid máu nặng (>10 mg/dL)
        - Laboratory TLS đã xảy ra
        - Không đáp ứng allopurinol
        
        **⚠️ CHỐNG CHỈ ĐỊNH:**
        - Thiếu hụt G6PD (nguy cơ tan máu)
        - Methemoglobinemia
        
        **Liều dùng:**
        - **0.15-0.2 mg/kg tĩnh mạch** trong 30 phút
        - **Mỗi ngày × 5-7 ngày**
        - Hoặc đến khi uric acid <7.5 mg/dL
        
        **Bắt đầu:**
        - 4-24h trước hóa trị (nguy cơ cao)
        - Ngay khi có laboratory TLS
        
        **Cơ chế:**
        - Enzyme chuyển uric acid → allantoin (hòa tan tốt)
        - Phá hủy uric acid đã có
        - Tác dụng nhanh (vài giờ)
        
        **Theo Dõi:**
        - Uric acid mỗi 4-6h
        - Hemoglobin, methemoglobin (nếu có triệu chứng)
        - Ngừng nếu tan máu hoặc methemoglobinemia
        
        **⚠️ Lưu ý:**
        - Đắt tiền
        - Cần bảo quản lạnh
        - Không dùng cùng allopurinol (không cần thiết)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: ELECTROLYTE MANAGEMENT ==========
    st.markdown("### ⚡ Điều Chỉnh Điện Giải")
    
    st.markdown("""
    **1. Tăng kali máu:**
    - Xem protocol Tăng kali máu
    - Điều trị ngay nếu K⁺ >6.0 hoặc có thay đổi ECG
    - Có thể cần lọc máu
    
    **2. Tăng phosphate máu:**
    - Xem protocol Giảm phosphate máu (ngược lại)
    - Thuốc gắn phosphate: Sevelamer, Calcium acetate
    - Có thể cần lọc máu
    
    **3. Giảm calci máu:**
    - Xem protocol Giảm calci máu
    - Chỉ bổ sung nếu có triệu chứng hoặc iCa <1.0
    - ⚠️ Không bổ sung nếu PO4 cao (nguy cơ kết tủa)
    
    **4. Bảo vệ thận:**
    - Bù dịch đầy đủ
    - Tránh thuốc độc thận
    - Có thể cần lọc máu
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Phác Đồ Theo Dõi")
    
    st.markdown("""
    **Ban đầu (trước hóa trị):**
    - Tổng phân tích tế bào máu, Xét nghiệm chuyển hóa cơ bản (K⁺, PO₄³⁻, Ca²⁺, Cr, BUN)
    - Uric acid
    - LDH
    - ECG (nếu có nguy cơ cao)
    
    **Trong quá trình điều trị:**
    - **Nguy cơ cao:** Mỗi 6-12h × 3-5 ngày
    - **Nguy cơ trung bình:** Mỗi 12-24h × 3-5 ngày
    - **Nguy cơ thấp:** Mỗi 24-48h
    
    **Các thông số cần theo dõi:**
    - Uric acid (mục tiêu: <7.5 mg/dL)
    - K⁺ (mục tiêu: <5.5 mEq/L)
    - PO₄³⁻ (mục tiêu: <4.5 mg/dL)
    - Ca²⁺, calci ion hóa
    - Creatinine, BUN
    - Lượng nước tiểu
    - ECG (nếu có tăng kali máu)
    
    **Dấu hiệu cảnh báo:**
    - ⚠️ Creatinine tăng >1.5 × ban đầu
    - ⚠️ Uric acid >10 mg/dL
    - ⚠️ K⁺ >6.0 hoặc thay đổi ECG
    - ⚠️ PO₄³⁻ >6.5 mg/dL
    - 🚨 Thiểu niệu/vô niệu
    - 🚨 Loạn nhịp tim
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: TREATMENT OF ESTABLISHED TLS ==========
    st.markdown("### 🚨 Điều Trị TLS Đã Xảy Ra")
    
    st.error("""
    **Nếu Laboratory TLS đã xảy ra:**
    
    **1. Tăng cường bù dịch:**
    - 3-4 L/m²/ngày
    - Hoặc 300-400 ml/h
    - Có thể cần furosemide
    
    **2. Rasburicase (nếu chưa dùng):**
    - 0.15-0.2 mg/kg tĩnh mạch ngay
    - Lặp lại mỗi ngày đến khi uric acid <7.5
    
    **3. Điều chỉnh điện giải:**
    - Tăng kali máu: Calci, Insulin+D50, Kayexalate
    - Tăng phosphate máu: Thuốc gắn phosphate
    - Giảm calci máu: Chỉ nếu có triệu chứng và PO4 không cao
    
    **4. Chỉ định lọc máu:**
    - Creatinine tăng nhanh
    - Thiểu niệu/vô niệu
    - K⁺ >6.5 không đáp ứng điều trị
    - PO₄³⁻ >6.5 mg/dL
    - Uric acid >10 mg/dL
    - Quá tải thể tích
    
    **5. Tạm hoãn hóa trị:**
    - Nếu TLS nặng
    - Đợi TLS ổn định
    - Giảm liều hóa trị sau đó
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Nguy cơ cao hơn (tỷ lệ tế bào/tổng khối lượng cao)
        - Bù dịch: 2-3 L/m²/ngày
        - Allopurinol: 10 mg/kg/ngày
        - Rasburicase: 0.15-0.2 mg/kg
        - Theo dõi sát hơn
        
        **Suy thận:**
        - Giảm liều allopurinol
        - Cẩn thận với bù dịch
        - Có thể cần lọc máu sớm
        """)
    
    with col2:
        st.markdown("""
        **Suy tim:**
        - Cẩn thận với bù dịch
        - Có thể cần furosemide
        - Theo dõi dấu hiệu quá tải
        
        **Thiếu hụt G6PD:**
        - ⚠️ CHỐNG CHỈ ĐỊNH Rasburicase
        - Chỉ dùng Allopurinol
        - Theo dõi tan máu
        """)
    
    st.markdown("---")
    
    # ========== SECTION 10: REFERENCES ==========
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    st.markdown("""
    1. **NCCN Clinical Practice Guidelines in Oncology** - Hội chứng tan u (Version 2023)
       - Phân tầng nguy cơ
       - Phác đồ phòng ngừa
       - Hướng dẫn điều trị
    
    2. **Cairo MS, et al.** Recommendations for the evaluation of risk and prophylaxis of tumour lysis syndrome (TLS) in adults and children with malignant diseases: an expert TLS panel consensus.
       Br J Haematol. 2010;149(4):578-586.
    
    3. **UpToDate:** Hội chứng tan u - Cập nhật lần cuối 2024
       - Đặc điểm lâm sàng và chẩn đoán
       - Phác đồ phòng ngừa và điều trị
    
    4. **Howard SC, et al.** The tumor lysis syndrome.
       N Engl J Med. 2011;364(19):1844-1854.
    """)
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất. TLS là biến chứng đe dọa tính mạng, cần phòng ngừa và điều trị tích cực.")


def render_high_risk_protocol():
    """Phác đồ phòng ngừa TLS nguy cơ cao"""
    st.error("## 🔴 PHÁC ĐỒ PHÒNG NGỪA TLS NGUY CƠ CAO")
    
    st.markdown("""
    **1. Bù dịch:**
    - **2-3 L/m²/ngày** Natri clorid 0.9% hoặc Dextrose 5%
    - Bắt đầu **24-48h trước hóa trị**
    - Duy trì trong và sau hóa trị
    - Mục tiêu: Lượng nước tiểu >100 ml/h
    
    **2. Rasburicase:**
    - **0.15-0.2 mg/kg tĩnh mạch** trong 30 phút
    - Bắt đầu **4-24h trước hóa trị**
    - Lặp lại mỗi ngày × 5-7 ngày
    - Hoặc đến khi uric acid <7.5 mg/dL
    
    **3. Theo dõi:**
    - **Mỗi 6-12h × 3-5 ngày:**
      * Uric acid
      * K⁺, PO₄³⁻, Ca²⁺
      * Creatinine, BUN
      * Lượng nước tiểu
    - ECG nếu có tăng kali máu
    
    **4. Cân nhắc:**
    - Tư vấn thận học sớm
    - Chuẩn bị lọc máu nếu cần
    - Theo dõi tại ICU nếu có nguy cơ cao
    """)


def render_intermediate_risk_protocol():
    """Phác đồ phòng ngừa TLS nguy cơ trung bình"""
    st.warning("## 🟡 PHÁC ĐỒ PHÒNG NGỪA TLS NGUY CƠ TRUNG BÌNH")
    
    st.markdown("""
    **1. Bù dịch:**
    - **2-3 L/m²/ngày** Natri clorid 0.9% hoặc Dextrose 5%
    - Bắt đầu **24h trước hóa trị**
    - Duy trì trong và sau hóa trị
    - Mục tiêu: Lượng nước tiểu >100 ml/h
    
    **2. Allopurinol:**
    - **600-900mg uống/ngày** (chia 2-3 lần)
    - Bắt đầu **24-48h trước hóa trị**
    - Tiếp tục **7-10 ngày sau hóa trị**
    - Hoặc chuyển sang Rasburicase nếu uric acid >10 mg/dL
    
    **3. Theo dõi:**
    - **Mỗi 12-24h × 3-5 ngày:**
      * Uric acid
      * K⁺, PO₄³⁻, Ca²⁺
      * Creatinine, BUN
      * Lượng nước tiểu
    
    **4. Chuyển sang Rasburicase nếu:**
    - Uric acid >10 mg/dL
    - Laboratory TLS xảy ra
    - Không đáp ứng allopurinol
    """)


def render_low_risk_protocol():
    """Phác đồ phòng ngừa TLS nguy cơ thấp"""
    st.success("## 🟢 PHÁC ĐỒ PHÒNG NGỪA TLS NGUY CƠ THẤP")
    
    st.markdown("""
    **1. Bù dịch:**
    - **1.5-2 L/m²/ngày** Natri clorid 0.9% hoặc Dextrose 5%
    - Bắt đầu **ngày hóa trị**
    - Duy trì 2-3 ngày sau hóa trị
    
    **2. Allopurinol (tùy chọn):**
    - **300-600mg uống/ngày**
    - Nếu có nguy cơ tăng uric acid
    - Bắt đầu ngày hóa trị
    
    **3. Theo dõi:**
    - **Mỗi 24-48h × 2-3 ngày:**
      * Uric acid
      * K⁺, PO₄³⁻, Ca²⁺
      * Creatinine
    
    **4. Tăng cường điều trị nếu:**
    - Uric acid tăng nhanh
    - Có dấu hiệu TLS
    """)

