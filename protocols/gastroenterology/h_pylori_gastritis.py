"""
H. pylori Gastritis/Ulcer Treatment Protocol
Maastricht V/Florence 2016, ACG 2017, AGA 2021 Guidelines
Management of H. pylori positive gastritis and peptic ulcer disease
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """H. pylori Gastritis/Ulcer Treatment Protocol"""
    st.subheader("🫀 Điều trị Viêm Loét Dạ Dày HP (+) (H. pylori Gastritis/Ulcer)")
    st.caption("ACG 2024, Maastricht VI - H. pylori eradication therapy")
    
    st.info("""
    **Cập nhật ACG 2024:**
    - **Bismuth Quadruple:** Ưu tiên hàng đầu (Strong recommendation).
    - **Thời gian:** 14 ngày bắt buộc.
    - **PCAB (Vonoprazan):** Thay thế hiệu quả cho PPI.
    """)
    
    st.info("""
    **Helicobacter pylori (H. pylori):**
    - Tỷ lệ nhiễm ở Việt Nam: ~70-80% dân số
    - Nguyên nhân chính: Viêm dạ dày, loét dạ dày-tá tràng, ung thư dạ dày
    - Đường lây: Miệng-miệng, phân-miệng, nước bị ô nhiễm
    
    **Chỉ định điều trị:**
    - Loét dạ dày-tá tràng (PUD)
    - Viêm dạ dày mạn tính
    - Sau cắt polyp dạ dày
    - Tiền sử gia đình ung thư dạ dày
    - Thiếu máu thiếu sắt không rõ nguyên nhân
    - ITP (Idiopathic Thrombocytopenic Purpura)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Chẩn đoán H. pylori")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Phương Pháp Chẩn đoán")
        st.info("""
        **Xâm lấn (Cần nội soi):**
        - **CLO test (Rapid Urease Test):** Nhanh, rẻ
        - **Histology:** Tiêu chuẩn vàng
        - **Culture:** Cần cho kháng sinh đồ
        
        **Không xâm lấn:**
        - **Urea Breath Test (UBT):** Tiêu chuẩn vàng không xâm lấn
        - **Stool Antigen Test (SAT):** Độ nhạy cao
        - **Serology:** Không dùng để đánh giá sau điều trị
        """)
    
    with col2:
        st.markdown("#### Lựa Chọn Test")
        test_choice = st.radio(
            "**Tình huống:**",
            ["Chẩn đoán lần đầu (chưa điều trị)", "Đánh giá sau điều trị (4-8 tuần)"],
            key="hp_test_choice"
        )
        
        if "lần đầu" in test_choice or "đầu" in test_choice:
            st.success("""
            **Khuyến cáo:**
            - **UBT hoặc SAT:** Ưu tiên
            - **Nội soi:** Nếu có chỉ định (PUD, nghi ngờ ung thư)
            """)
        else:
            st.warning("""
            **Khuyến cáo:**
            - **UBT hoặc SAT:** Bắt buộc
            - **Không dùng:** Serology (không chính xác)
            - **Thời gian:** Sau khi ngừng PPI 2 tuần, kháng sinh 4 tuần
            """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Phác Đồ Điều trị")
    
    st.markdown("#### Lựa Chọn Phác Đồ")
    
    treatment_scenario = st.radio(
        "**Tình huống:**",
        [
            "Điều trị lần đầu (First-line)",
            "Thất bại lần đầu (Second-line)",
            "Kháng Clarithromycin (Resistance)",
            "Dị ứng Penicillin"
        ],
        key="hp_treatment_scenario"
    )
    
    st.markdown("---")
    
    if "lần đầu" in treatment_scenario or "First-line" in treatment_scenario:
        render_first_line()
    elif "Thất bại" in treatment_scenario or "Second-line" in treatment_scenario:
        render_second_line()
    elif "Kháng" in treatment_scenario or "Resistance" in treatment_scenario:
        render_resistant()
    else:
        render_penicillin_allergy()
    
    st.markdown("---")
    
    st.markdown("### 📋 Phác Đồ Chi tiết")
    
    protocol_choice = st.selectbox(
        "**Chọn phác đồ:**",
        [
            "Triple Therapy (Clarithromycin) - 14 ngày",
            "Triple Therapy (Metronidazole) - 14 ngày",
            "Quadruple Therapy (Bismuth) - 14 ngày",
            "Sequential Therapy - 10 ngày",
            "Concomitant Therapy - 10-14 ngày",
            "Levofloxacin Triple - 10-14 ngày"
        ],
        key="hp_protocol"
    )
    
    st.markdown("---")
    
    if "Triple" in protocol_choice and "Clarithromycin" in protocol_choice:
        render_triple_clarithromycin()
    elif "Triple" in protocol_choice and "Metronidazole" in protocol_choice:
        render_triple_metronidazole()
    elif "Quadruple" in protocol_choice or "Bismuth" in protocol_choice:
        render_quadruple_bismuth()
    elif "Sequential" in protocol_choice:
        render_sequential()
    elif "Concomitant" in protocol_choice:
        render_concomitant()
    else:
        render_levofloxacin_triple()
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Kháng Thuốc & Thất Bại")
    
    st.warning("""
    **Tỷ lệ kháng thuốc ở Việt Nam:**
    - **Clarithromycin:** ~20-30% (cao)
    - **Metronidazole:** ~60-70% (rất cao)
    - **Levofloxacin:** ~15-25%
    - **Amoxicillin:** <5% (thấp)
    
    **Nguyên nhân thất bại:**
    - Kháng thuốc (đặc biệt Clarithromycin)
    - Không tuân thủ điều trị
    - Liều không đủ
    - Thời gian điều trị ngắn (<10 ngày)
    - PPI liều thấp
    """)
    
    st.markdown("### 🔄 Xử trí Thất Bại")
    
    with st.expander("📋 Xem chiến lược xử trí", expanded=True):
        st.markdown("""
        **Nếu thất bại phác đồ Clarithromycin:**
        1. **Chuyển sang:** Quadruple bismuth (14 ngày)
        2. **Hoặc:** Levofloxacin triple (14 ngày)
        3. **Hoặc:** Concomitant therapy (14 ngày)
        
        **Nếu thất bại lần 2:**
        1. **Kháng sinh đồ:** Nếu có thể
        2. **Phác đồ cứu vãn:** Dựa trên kháng sinh đồ
        3. **Hoặc:** High-dose dual therapy (PPI + Amoxicillin)
        
        **Lưu ý:**
        - Không lặp lại phác đồ đã thất bại
        - Tăng thời gian điều trị (14 ngày)
        - Tăng liều PPI
        - Đánh giá tuân thủ
        """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Đánh giá Sau Điều trị")
    
    st.markdown("#### Thời Điểm Đánh giá")
    
    st.info("""
    **Thời gian:**
    - **Sau 4-8 tuần** kể từ khi kết thúc điều trị
    - **Sau khi ngừng PPI** ít nhất 2 tuần
    - **Sau khi ngừng kháng sinh** ít nhất 4 tuần
    
    **Phương pháp:**
    - **UBT (Urea Breath Test):** Ưu tiên
    - **SAT (Stool Antigen Test):** Lựa chọn thay thế
    - **Không dùng:** Serology
    """)
    
    st.markdown("#### Kết quả")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Thành công (Eradication):**
        - UBT/SAT âm tính
        - Tỷ lệ: 80-90% với phác đồ phù hợp
        - Không cần điều trị lại
        - Theo dõi: Nếu có PUD, tái khám định kỳ
        """)
    
    with col2:
        st.error("""
        **Thất bại (Persistent):**
        - UBT/SAT vẫn dương tính
        - Cần điều trị lại với phác đồ khác
        - Đánh giá: Tuân thủ, kháng thuốc
        - Cân nhắc: Kháng sinh đồ
        """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Có Thai:**
        - **An toàn:** Amoxicillin, Metronidazole (sau 3 tháng đầu)
        - **Tránh:** Clarithromycin, Levofloxacin, Tetracycline
        - **PPI:** Omeprazole, Pantoprazole (Category B)
        - **Phác đồ:** Amoxicillin + Metronidazole + PPI (14 ngày)
        
        **Trẻ Em:**
        - **Liều:** Tính theo kg
        - **Phác đồ:** Triple therapy (Amoxicillin + Clarithromycin + PPI)
        - **Thời gian:** 14 ngày
        - **Theo dõi:** Tác dụng phụ
        """)
    
    with col2:
        st.markdown("""
        **Suy Thận:**
        - **Amoxicillin:** Điều chỉnh liều nếu CrCl <30
        - **Clarithromycin:** Thận trọng
        - **Metronidazole:** Giảm liều nếu CrCl <10
        - **PPI:** Không cần điều chỉnh
        
        **Người Cao Tuổi:**
        - Cẩn thận với tương tác thuốc
        - Giảm liều nếu suy thận
        - Theo dõi tác dụng phụ
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Xác định chỉ định điều trị H. pylori",
        "✅ Chọn test chẩn đoán phù hợp (UBT/SAT)",
        "✅ Chọn phác đồ điều trị (dựa trên kháng thuốc địa phương)",
        "✅ Tư vấn về tuân thủ điều trị (quan trọng!)",
        "✅ Tư vấn về tác dụng phụ",
        "✅ Đánh giá sau điều trị (UBT/SAT sau 4-8 tuần)",
        "✅ Xử trí thất bại nếu cần",
        "✅ Tư vấn về tái nhiễm và phòng ngừa"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **Maastricht V/Florence Consensus 2016**
       - Malfertheiner P, et al. Gut. 2017
    
    2. **ACG 2017 Guidelines**
       - Chey WD, et al. Am J Gastroenterol. 2017
    
    3. **AGA 2021 Guidelines**
       - Shah SC, et al. Gastroenterology. 2021
    
    4. **UpToDate:** Treatment regimens for Helicobacter pylori
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("H. pylori")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_first_line():
    """First-line Treatment"""
    st.success("## 💊 Điều trị Lần Đầu (First-line)")
    
    st.markdown("### Khuyến cáo")
    
    st.info("""
    **Phác đồ ưu tiên (Việt Nam):**
    1. **Quadruple bismuth (14 ngày):** Nếu tỷ lệ kháng Clarithromycin >15%
    2. **Triple Clarithromycin (14 ngày):** Nếu tỷ lệ kháng <15%
    3. **Concomitant (14 ngày):** Lựa chọn thay thế
    
    **Lưu ý:**
    - Ở Việt Nam, tỷ lệ kháng Clarithromycin cao (~20-30%)
    - Khuyến cáo: Quadruple bismuth hoặc Concomitant
    - Thời gian: Tối thiểu 14 ngày
    """)


def render_second_line():
    """Second-line Treatment"""
    st.warning("## 💊 Điều trị Lần 2 (Second-line)")
    
    st.info("""
    **Nếu thất bại phác đồ Clarithromycin:**
    - **Chuyển sang:** Quadruple bismuth (14 ngày)
    - **Hoặc:** Levofloxacin triple (14 ngày)
    - **Hoặc:** Concomitant therapy (14 ngày)
    
    **Nếu thất bại phác đồ Metronidazole:**
    - **Chuyển sang:** Triple Clarithromycin (14 ngày)
    - **Hoặc:** Quadruple bismuth (14 ngày)
    
    **Lưu ý:**
    - Không lặp lại phác đồ đã thất bại
    - Tăng liều PPI
    - Đánh giá tuân thủ
    """)


def render_resistant():
    """Resistant H. pylori"""
    st.error("## ⚠️ H. pylori Kháng Thuốc")
    
    st.warning("""
    **Kháng Clarithromycin:**
    - Chuyển sang: Quadruple bismuth hoặc Levofloxacin triple
    
    **Kháng Metronidazole:**
    - Chuyển sang: Triple Clarithromycin hoặc Quadruple bismuth
    
    **Kháng đa thuốc:**
    - Kháng sinh đồ: Nếu có thể
    - Phác đồ cứu vãn: Dựa trên kháng sinh đồ
    - Hoặc: High-dose dual therapy (PPI + Amoxicillin)
    """)


def render_penicillin_allergy():
    """Penicillin Allergy"""
    st.warning("## ⚠️ Dị Ứng Penicillin")
    
    st.info("""
    **Phác đồ thay thế:**
    1. **Quadruple bismuth (14 ngày):**
       - PPI + Bismuth + Metronidazole + Tetracycline
       
    2. **Levofloxacin triple (14 ngày):**
       - PPI + Levofloxacin + Metronidazole
       
    3. **Clarithromycin + Metronidazole + PPI (14 ngày):**
       - Nếu không dị ứng Clarithromycin
    """)


def render_triple_clarithromycin():
    """Triple Therapy with Clarithromycin"""
    st.success("## 💊 Triple Therapy (Clarithromycin) - 14 ngày")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày HOẶC
      - Lansoprazole 30mg x 2 lần/ngày HOẶC
      - Pantoprazole 40mg x 2 lần/ngày HOẶC
      - Esomeprazole 20mg x 2 lần/ngày HOẶC
      - Rabeprazole 20mg x 2 lần/ngày
    
    - **Amoxicillin:** 1000mg x 2 lần/ngày
    
    - **Clarithromycin:** 500mg x 2 lần/ngày
    
    **Thời gian:** 14 ngày
    
    **Cách dùng:**
    - Uống trước ăn 30 phút (PPI)
    - Uống với thức ăn (kháng sinh)
    - Uống đủ nước
    """)
    
    st.markdown("### Hiệu Quả")
    
    st.warning("""
    **Tỷ lệ thành công:**
    - **Không kháng Clarithromycin:** 85-90%
    - **Kháng Clarithromycin:** 40-50% (thấp!)
    
    **Lưu ý:**
    - Ở Việt Nam, tỷ lệ kháng Clarithromycin cao (~20-30%)
    - Không khuyến cáo nếu tỷ lệ kháng >15%
    - Cân nhắc: Quadruple bismuth hoặc Concomitant
    """)
    
    st.markdown("### Tác Dụng Phụ")
    
    st.info("""
    - **Clarithromycin:** Vị kim loại, buồn nôn, tiêu chảy
    - **Amoxicillin:** Tiêu chảy, phát ban (dị ứng)
    - **PPI:** Đau đầu, tiêu chảy (hiếm)
    
    **Xử trí:**
    - Tiêu chảy: Probiotics, bù nước
    - Vị kim loại: Uống nhiều nước, kẹo ngọt
    - Phát ban: Ngừng Amoxicillin, đổi phác đồ
    """)


def render_triple_metronidazole():
    """Triple Therapy with Metronidazole"""
    st.success("## 💊 Triple Therapy (Metronidazole) - 14 ngày")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày (hoặc tương đương)
    
    - **Amoxicillin:** 1000mg x 2 lần/ngày
    
    - **Metronidazole:** 500mg x 3 lần/ngày HOẶC 500mg x 2 lần/ngày
    
    **Thời gian:** 14 ngày
    
    **Cách dùng:**
    - Uống trước ăn 30 phút (PPI)
    - Uống với thức ăn (kháng sinh)
    - **Tránh rượu:** Trong và sau điều trị 48 giờ (phản ứng disulfiram)
    """)
    
    st.markdown("### Hiệu Quả")
    
    st.warning("""
    **Tỷ lệ thành công:**
    - **Không kháng Metronidazole:** 80-85%
    - **Kháng Metronidazole:** 50-60% (thấp!)
    
    **Lưu ý:**
    - Ở Việt Nam, tỷ lệ kháng Metronidazole rất cao (~60-70%)
    - Không khuyến cáo làm first-line
    - Có thể dùng nếu không có lựa chọn khác
    """)


def render_quadruple_bismuth():
    """Quadruple Bismuth Therapy"""
    st.success("## 💊 Quadruple Therapy (Bismuth) - 14 ngày")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày (hoặc tương đương)
    
    - **Bismuth Subsalicylate:** 524mg x 4 lần/ngày HOẶC
      - **Bismuth Subcitrate:** 120mg x 4 lần/ngày
    
    - **Metronidazole:** 500mg x 3 lần/ngày
    
    - **Tetracycline:** 500mg x 4 lần/ngày
    
    **Thời gian:** 14 ngày
    
    **Cách dùng:**
    - Uống trước ăn 30 phút (PPI)
    - Uống với thức ăn (kháng sinh, bismuth)
    - **Tránh rượu:** Trong và sau điều trị 48 giờ
    - **Tetracycline:** Uống với nhiều nước, tránh nằm ngay sau khi uống
    """)
    
    st.markdown("### Hiệu Quả")
    
    st.success("""
    **Tỷ lệ thành công:**
    - **85-95%** (cao, ngay cả khi kháng Clarithromycin)
    
    **Ưu điểm:**
    - Hiệu quả cao, không phụ thuộc vào kháng Clarithromycin
    - Phù hợp với Việt Nam (tỷ lệ kháng Clarithromycin cao)
    - Có thể dùng làm first-line
    
    **Nhược điểm:**
    - Nhiều viên thuốc (4 loại)
    - Tác dụng phụ nhiều hơn
    - Tetracycline: Tránh ở trẻ em <8 tuổi, có thai
    """)
    
    st.markdown("### Tác Dụng Phụ")
    
    st.warning("""
    - **Bismuth:** Phân đen (bình thường), buồn nôn
    - **Metronidazole:** Vị kim loại, buồn nôn, phản ứng với rượu
    - **Tetracycline:** Loét thực quản, nhạy cảm ánh sáng, ố răng (trẻ em)
    - **PPI:** Đau đầu, tiêu chảy (hiếm)
    
    **Xử trí:**
    - Phân đen: Bình thường, không phải xuất huyết
    - Vị kim loại: Uống nhiều nước, kẹo ngọt
    - Loét thực quản: Uống với nhiều nước, tránh nằm ngay
    """)


def render_sequential():
    """Sequential Therapy"""
    st.success("## 💊 Sequential Therapy - 10 ngày")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Giai đoạn 1 (5 ngày đầu):**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày
    - **Amoxicillin:** 1000mg x 2 lần/ngày
    
    **Giai đoạn 2 (5 ngày sau):**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày
    - **Clarithromycin:** 500mg x 2 lần/ngày
    - **Metronidazole:** 500mg x 2 lần/ngày
    
    **Tổng thời gian:** 10 ngày
    
    **Cách dùng:**
    - Uống trước ăn 30 phút (PPI)
    - Uống với thức ăn (kháng sinh)
    """)
    
    st.markdown("### Hiệu Quả")
    
    st.info("""
    **Tỷ lệ thành công:**
    - **80-90%** (tương đương triple 14 ngày)
    
    **Ưu điểm:**
    - Thời gian ngắn hơn (10 ngày)
    - Hiệu quả tốt
    
    **Nhược điểm:**
    - Phức tạp hơn (2 giai đoạn)
    - Dễ nhầm lẫn
    """)


def render_concomitant():
    """Concomitant Therapy"""
    st.success("## 💊 Concomitant Therapy - 10-14 ngày")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần (dùng đồng thời):**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày
    
    - **Amoxicillin:** 1000mg x 2 lần/ngày
    
    - **Clarithromycin:** 500mg x 2 lần/ngày
    
    - **Metronidazole:** 500mg x 2 lần/ngày
    
    **Thời gian:** 10-14 ngày (khuyến cáo 14 ngày)
    
    **Cách dùng:**
    - Uống trước ăn 30 phút (PPI)
    - Uống với thức ăn (kháng sinh)
    """)
    
    st.markdown("### Hiệu Quả")
    
    st.success("""
    **Tỷ lệ thành công:**
    - **85-95%** (cao, ngay cả khi kháng Clarithromycin)
    
    **Ưu điểm:**
    - Hiệu quả cao
    - Không phụ thuộc vào kháng Clarithromycin
    - Phù hợp với Việt Nam
    
    **Nhược điểm:**
    - Nhiều viên thuốc (4 loại)
    - Tác dụng phụ nhiều hơn
    """)


def render_levofloxacin_triple():
    """Levofloxacin Triple Therapy"""
    st.warning("## 💊 Levofloxacin Triple Therapy - 10-14 ngày")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Thành phần:**
    - **PPI:** Omeprazole 20mg x 2 lần/ngày
    
    - **Amoxicillin:** 1000mg x 2 lần/ngày
    
    - **Levofloxacin:** 500mg x 1 lần/ngày
    
    **Thời gian:** 10-14 ngày (khuyến cáo 14 ngày)
    
    **Cách dùng:**
    - Uống trước ăn 30 phút (PPI)
    - Uống với thức ăn (kháng sinh)
    """)
    
    st.markdown("### Hiệu Quả")
    
    st.info("""
    **Tỷ lệ thành công:**
    - **80-90%** (nếu không kháng Levofloxacin)
    - **50-60%** (nếu kháng Levofloxacin)
    
    **Chỉ định:**
    - Second-line (sau thất bại phác đồ Clarithromycin)
    - Không dùng first-line (bảo tồn Levofloxacin)
    
    **Lưu ý:**
    - Ở Việt Nam, tỷ lệ kháng Levofloxacin ~15-25%
    - Tránh ở trẻ em, có thai, cho con bú
    - Nguy cơ: Gân, thần kinh, tim mạch
    """)

