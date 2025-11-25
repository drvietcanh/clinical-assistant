"""
Clostridioides difficile (C. diff) Infection Treatment Protocol
IDSA/SHEA 2021 Guidelines
"""

import streamlit as st


def render():
    """Clostridioides difficile (C. diff) Infection Treatment Protocol"""
    st.subheader("🦠 Clostridioides difficile (C. diff) Infection Treatment")
    st.caption("IDSA/SHEA 2021 Guidelines - C. diff Infection Management")
    
    st.info("""
    **Chẩn đoán C. diff khi có:**
    - Tiêu chảy (≥3 lần/ngày, phân lỏng) hoặc tắc ruột
    - Xét nghiệm dương tính: NAAT (PCR) hoặc GDH + Toxin EIA
    - Có yếu tố nguy cơ: kháng sinh gần đây, nhập viện, tuổi cao, suy giảm miễn dịch
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: SEVERITY ASSESSMENT ==========
    st.markdown("### 📊 Đánh Giá Mức Độ Nặng")
    
    st.markdown("**Phân loại mức độ theo IDSA/SHEA 2021:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Nhẹ - Mild:**
        - Tiêu chảy, không có dấu hiệu nặng
        - WBC <15,000/µL
        - Creatinine <1.5x ban đầu
        - Không có dấu hiệu tắc ruột
        """)
        
        st.warning("""
        **Trung bình - Moderate:**
        - Tiêu chảy + 1 trong các dấu hiệu:
        - WBC 15,000-20,000/µL
        - Creatinine 1.5-2x ban đầu
        - Hoặc có dấu hiệu tắc ruột nhẹ
        """)
    
    with col2:
        st.error("""
        **Nặng - Severe:**
        - Tiêu chảy + 1 trong các dấu hiệu:
        - WBC >20,000/µL
        - Creatinine >2x ban đầu
        - Hoặc albumin <3 g/dL
        - Hoặc có dấu hiệu tắc ruột nặng
        """)
        
        st.error("""
        **Rất nặng - Fulminant:**
        - Sốc, tụt huyết áp
        - Megacolon độc tố
        - Thủng ruột
        - Cần phẫu thuật
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: INITIAL EPISODE TREATMENT ==========
    st.markdown("### 💊 Điều Trị Đợt Đầu Tiên (Initial Episode)")
    
    st.markdown("**Nguyên tắc:** Ngừng kháng sinh gây bệnh nếu có thể, bắt đầu điều trị ngay")
    
    # Severity-based treatment
    with st.expander("📋 Phác Đồ Điều Trị Theo Mức Độ", expanded=True):
        st.markdown("#### **1. Nhẹ - Mild (First Episode)**")
        st.success("""
        **Lựa chọn 1 (Ưu tiên):**
        - **Fidaxomicin 200mg PO BID x 10 ngày**
        - Tỷ lệ tái phát thấp hơn Vancomycin
        
        **Lựa chọn 2:**
        - **Vancomycin 125mg PO QID x 10 ngày**
        - Hoặc Vancomycin 250mg PO QID nếu cần
        
        **Lựa chọn 3 (Nếu không có Fidaxomicin/Vancomycin):**
        - **Metronidazole 500mg PO TID x 10 ngày**
        - ⚠️ Không dùng cho đợt nặng hoặc tái phát
        """)
        
        st.markdown("---")
        
        st.markdown("#### **2. Trung bình - Moderate (First Episode)**")
        st.warning("""
        **Lựa chọn 1 (Ưu tiên):**
        - **Fidaxomicin 200mg PO BID x 10 ngày**
        
        **Lựa chọn 2:**
        - **Vancomycin 125mg PO QID x 10 ngày**
        
        **Lựa chọn 3:**
        - **Vancomycin 250mg PO QID x 10 ngày** (nếu cần)
        
        ⚠️ **Không dùng Metronidazole** cho mức độ trung bình trở lên
        """)
        
        st.markdown("---")
        
        st.markdown("#### **3. Nặng - Severe (First Episode)**")
        st.error("""
        **Lựa chọn 1 (Ưu tiên):**
        - **Fidaxomicin 200mg PO BID x 10 ngày**
        
        **Lựa chọn 2:**
        - **Vancomycin 125mg PO QID x 10 ngày**
        
        **Lựa chọn 3 (Nếu không uống được):**
        - **Vancomycin 500mg PO QID x 10 ngày**
        - Hoặc Vancomycin retention enema (nếu tắc ruột)
        
        ⚠️ **Không dùng Metronidazole** cho mức độ nặng
        """)
        
        st.markdown("---")
        
        st.markdown("#### **4. Rất nặng - Fulminant (First Episode)**")
        st.error("""
        **Phác đồ kết hợp:**
        - **Vancomycin 500mg PO QID** (hoặc qua ống thông mũi-dạ dày)
        - **+ Metronidazole 500mg IV TID**
        - **+ Vancomycin retention enema** (nếu tắc ruột)
        
        **Cân nhắc phẫu thuật nếu:**
        - Megacolon độc tố
        - Thủng ruột
        - Sốc không đáp ứng điều trị
        - Lactate >5 mmol/L
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: RECURRENT C. DIFF ==========
    st.markdown("### 🔄 Điều Trị Tái Phát (Recurrent C. diff)")
    
    st.markdown("**Định nghĩa:** Tái phát trong vòng 8 tuần sau khi ngừng điều trị")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Tái phát lần 1 (First Recurrence)**")
        st.warning("""
        **Lựa chọn 1 (Ưu tiên):**
        - **Fidaxomicin 200mg PO BID x 10 ngày**
        - Tỷ lệ tái phát thấp hơn Vancomycin
        
        **Lựa chọn 2:**
        - **Vancomycin tapered/pulsed regimen:**
          - 125mg PO QID x 10-14 ngày
          - Sau đó: 125mg PO BID x 7 ngày
          - Sau đó: 125mg PO QD x 7 ngày
          - Sau đó: 125mg PO mỗi 2-3 ngày x 2-8 tuần
        
        **Lựa chọn 3:**
        - **Vancomycin 125mg PO QID x 10 ngày**
        """)
    
    with col2:
        st.markdown("#### **Tái phát lần 2 trở đi (Multiple Recurrences)**")
        st.error("""
        **Lựa chọn 1 (Ưu tiên):**
        - **Fidaxomicin 200mg PO BID x 10 ngày**
        
        **Lựa chọn 2:**
        - **Vancomycin tapered/pulsed regimen** (như trên)
        
        **Lựa chọn 3:**
        - **Bezlotoxumab (Zinplava) 10mg/kg IV x 1 liều**
          - Monoclonal antibody chống độc tố B
          - Dùng cùng với kháng sinh (Vancomycin hoặc Fidaxomicin)
          - Giảm tỷ lệ tái phát 10% (từ 26% → 16%)
          - Chỉ định: ≥1 lần tái phát, nguy cơ tái phát cao
        
        **Lựa chọn 4:**
        - **Fecal Microbiota Transplantation (FMT)**
          - Chỉ định: ≥2 lần tái phát
          - Hiệu quả: 80-90% thành công
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: FECAL MICROBIOTA TRANSPLANTATION (FMT) ==========
    st.markdown("### 💩 Fecal Microbiota Transplantation (FMT)")
    
    st.markdown("**Chỉ định FMT:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Chỉ định:**
        - ≥2 lần tái phát C. diff
        - Hoặc ≥3 lần tái phát
        - Đã thất bại với Vancomycin/Fidaxomicin
        - Không có chống chỉ định
        
        **Hiệu quả:**
        - Tỷ lệ thành công: 80-90%
        - Thường chỉ cần 1 lần
        - Tác dụng nhanh (1-3 ngày)
        """)
    
    with col2:
        st.error("""
        **Chống chỉ định:**
        - Megacolon độc tố
        - Thủng ruột
        - Suy giảm miễn dịch nặng
        - Đang dùng ức chế miễn dịch mạnh
        
        **Cách thức:**
        - Colonoscopy (ưu tiên)
        - Hoặc nasoduodenal tube
        - Hoặc enema (ít hiệu quả hơn)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: BEZLOTOXUMAB ==========
    st.markdown("### 💉 Bezlotoxumab (Zinplava)")
    
    st.info("""
    **Bezlotoxumab** là monoclonal antibody chống độc tố B của C. diff.
    
    **Chỉ định:**
    - Dùng cùng với Vancomycin hoặc Fidaxomicin
    - Bệnh nhân có ≥1 lần tái phát C. diff
    - Hoặc nguy cơ tái phát cao (tuổi >65, suy giảm miễn dịch, nhiễm C. diff nặng)
    
    **Liều dùng:**
    - 10mg/kg IV x 1 liều
    - Truyền trong 60 phút
    - Dùng cùng lúc với kháng sinh (không thay thế kháng sinh)
    
    **Hiệu quả:**
    - Giảm tỷ lệ tái phát từ 26% → 16% (giảm 10%)
    - Tác dụng phụ: Buồn nôn, sốt, đau đầu (hiếm)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SUPPORTIVE CARE ==========
    st.markdown("### 🏥 Chăm Sóc Hỗ Trợ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Điều chỉnh kháng sinh:**")
        st.warning("""
        - **Ngừng kháng sinh gây bệnh** nếu có thể
        - Nếu phải tiếp tục kháng sinh:
          - Chọn kháng sinh ít gây C. diff
          - Cân nhắc dùng probiotic (Lactobacillus, Saccharomyces)
        """)
        
        st.markdown("#### **Bù dịch và điện giải:**")
        st.info("""
        - Bù dịch qua đường uống hoặc IV
        - Theo dõi điện giải (Na, K, Cl)
        - Bổ sung kali nếu cần
        """)
    
    with col2:
        st.markdown("#### **Tránh thuốc chống nhu động:**")
        st.error("""
        - **Không dùng:** Loperamide, Diphenoxylate
        - Lý do: Làm chậm thải trừ độc tố, tăng nguy cơ megacolon
        - Chỉ dùng khi thực sự cần thiết và đã điều trị C. diff
        """)
        
        st.markdown("#### **Probiotics:**")
        st.info("""
        - **Saccharomyces boulardii** có thể giúp giảm tái phát
        - Dùng cùng với kháng sinh
        - Liều: 500mg PO BID
        - ⚠️ Thận trọng ở bệnh nhân suy giảm miễn dịch
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📊 Theo Dõi")
    
    st.markdown("**Theo dõi trong quá trình điều trị:**")
    
    monitoring_items = [
        "**Triệu chứng:** Số lần tiêu chảy, đau bụng, sốt",
        "**Dấu hiệu sinh tồn:** Huyết áp, nhịp tim, nhiệt độ",
        "**Xét nghiệm:** WBC, Creatinine, Albumin (nếu nặng)",
        "**Dấu hiệu biến chứng:** Megacolon, thủng ruột, sốc",
        "**Đáp ứng điều trị:** Giảm tiêu chảy sau 3-5 ngày",
    ]
    
    for item in monitoring_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    # ========== SECTION 8: PREVENTION ==========
    st.markdown("### 🛡️ Phòng Ngừa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Phòng ngừa ban đầu:**")
        st.success("""
        - **Sử dụng kháng sinh hợp lý:**
          - Tránh kháng sinh phổ rộng không cần thiết
          - Rút ngắn thời gian điều trị khi có thể
          - Chọn kháng sinh ít gây C. diff
        
        - **Vệ sinh tay:**
          - Rửa tay bằng xà phòng và nước
          - Không chỉ dùng gel cồn (không diệt được bào tử)
        """)
    
    with col2:
        st.markdown("#### **Phòng ngừa tái phát:**")
        st.warning("""
        - **Tránh kháng sinh không cần thiết** trong 8 tuần sau điều trị
        
        - **Probiotics:**
          - Saccharomyces boulardii
          - Lactobacillus
          - Dùng trong và sau điều trị
        
        - **Fidaxomicin** thay vì Vancomycin (giảm tái phát)
        
        - **Bezlotoxumab** cho nguy cơ tái phát cao
        """)
    
    st.markdown("---")
    
    # ========== SECTION 9: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Dân Số Đặc Biệt")
    
    with st.expander("🔍 Xem hướng dẫn cho dân số đặc biệt", expanded=False):
        st.markdown("#### **Phụ nữ có thai:**")
        st.info("""
        - **Vancomycin 125mg PO QID** là lựa chọn an toàn
        - Fidaxomicin: Dữ liệu hạn chế, cân nhắc nếu cần
        - Metronidazole: Tránh trong tam cá nguyệt 1
        - FMT: Cân nhắc cẩn thận, dữ liệu hạn chế
        """)
        
        st.markdown("---")
        
        st.markdown("#### **Suy thận:**")
        st.info("""
        - **Vancomycin:** Không hấp thu qua đường tiêu hóa, an toàn cho suy thận
        - **Fidaxomicin:** Không cần điều chỉnh liều
        - **Metronidazole:** Cần điều chỉnh liều nếu CrCl <50
        """)
        
        st.markdown("---")
        
        st.markdown("#### **Suy giảm miễn dịch:**")
        st.warning("""
        - Điều trị tương tự, nhưng:
        - Cân nhắc điều trị lâu hơn (14 ngày thay vì 10 ngày)
        - Theo dõi sát hơn
        - Tránh FMT nếu suy giảm miễn dịch nặng
        - Tránh Saccharomyces boulardii (nguy cơ nhiễm trùng huyết)
        """)
        
        st.markdown("---")
        
        st.markdown("#### **Trẻ em:**")
        st.info("""
        - **Vancomycin:** 40mg/kg/ngày chia 4 lần (max 2g/ngày)
        - **Metronidazole:** 30mg/kg/ngày chia 3 lần (max 1.5g/ngày)
        - **Fidaxomicin:** Dữ liệu hạn chế ở trẻ em
        - FMT: Có thể dùng, nhưng cần cân nhắc cẩn thận
        """)
    
    st.markdown("---")
    
    # ========== SECTION 10: DURATION & FOLLOW-UP ==========
    st.markdown("### ⏱️ Thời Gian Điều Trị & Theo Dõi")
    
    st.markdown("**Thời gian điều trị tiêu chuẩn:**")
    
    duration_table = {
        "Mức độ": ["Nhẹ", "Trung bình", "Nặng", "Rất nặng"],
        "Thời gian": ["10 ngày", "10 ngày", "10-14 ngày", "14 ngày"],
        "Ghi chú": [
            "Có thể dùng Fidaxomicin hoặc Vancomycin",
            "Fidaxomicin ưu tiên, hoặc Vancomycin",
            "Vancomycin liều cao, có thể kéo dài",
            "Kết hợp Vancomycin + Metronidazole IV"
        ]
    }
    
    st.table(duration_table)
    
    st.markdown("**Theo dõi sau điều trị:**")
    st.info("""
    - **Không cần test lại** nếu triệu chứng đã hết
    - Test lại chỉ khi:
      - Triệu chứng tái phát
      - Hoặc cần xác nhận để ngừng cách ly
    - Theo dõi trong 8 tuần để phát hiện tái phát
    """)
    
    st.markdown("---")
    
    # ========== SECTION 11: REFERENCES ==========
    st.markdown("### 📚 Tài Liệu Tham Khảo")
    
    references = [
        "**IDSA/SHEA 2021:** Clinical Practice Guidelines for Clostridioides difficile Infection in Adults and Children",
        "**UpToDate:** Clostridioides difficile infection in adults: Treatment and prevention",
        "**Lexicomp:** Fidaxomicin, Vancomycin (oral), Metronidazole drug monographs",
        "**FDA:** Bezlotoxumab (Zinplava) prescribing information",
    ]
    
    for ref in references:
        st.markdown(f"- {ref}")
    
    st.caption("💡 Protocol này dựa trên IDSA/SHEA 2021 guidelines. Cập nhật thường xuyên theo guidelines mới nhất.")

