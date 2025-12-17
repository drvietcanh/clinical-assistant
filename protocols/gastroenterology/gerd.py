"""
GERD (Gastroesophageal Reflux Disease) Treatment Protocol
ACG 2022, AGA 2021 Guidelines
Management of gastroesophageal reflux disease
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """GERD Treatment Protocol"""
    st.subheader("🫀 Điều Trị Trào Ngược Dạ Dày Thực Quản (GERD)")
    st.caption("ACG 2022, AGA 2021 - Management of gastroesophageal reflux disease")
    
    st.info("""
    **Trào ngược dạ dày thực quản (GERD):**
    - Tỷ lệ ở Việt Nam: ~10-20% dân số
    - Định nghĩa: Trào ngược dịch dạ dày lên thực quản gây triệu chứng/biến chứng
    - Triệu chứng: Ợ nóng, ợ chua, đau ngực, khó nuốt
    - Biến chứng: Viêm thực quản, Barrett thực quản, hẹp thực quản
    
    **Phân loại:**
    - **Non-erosive GERD (NERD):** Có triệu chứng, không có tổn thương
    - **Erosive GERD (ERD):** Có tổn thương thực quản (viêm, loét)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Chẩn Đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Triệu Chứng")
        st.info("""
        **Triệu chứng điển hình:**
        - Ợ nóng (heartburn)
        - Ợ chua (acid regurgitation)
        - Đau ngực (có thể giống đau tim)
        
        **Triệu chứng không điển hình:**
        - Ho mạn tính
        - Khàn tiếng
        - Hen phế quản
        - Đau họng
        """)
        
        symptoms = st.multiselect(
            "**Triệu chứng bệnh nhân:**",
            ["Ợ nóng", "Ợ chua", "Đau ngực", "Khó nuốt", "Ho mạn tính", "Khàn tiếng"],
            key="gerd_symptoms"
        )
    
    with col2:
        st.markdown("#### Chẩn Đoán")
        st.info("""
        **Chẩn đoán lâm sàng:**
        - Triệu chứng điển hình → Thử điều trị PPI
        - Đáp ứng với PPI → Xác nhận GERD
        
        **Nội soi:**
        - Chỉ định: Triệu chứng cảnh báo, không đáp ứng PPI
        - Phát hiện: Viêm thực quản, Barrett, hẹp
        
        **pH monitoring:**
        - Khi chẩn đoán không rõ
        - Đo pH 24 giờ
        """)
        
        diagnosis_method = st.radio(
            "**Phương pháp chẩn đoán:**",
            ["Lâm sàng (Thử PPI)", "Nội soi", "pH monitoring"],
            key="gerd_diagnosis"
        )
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị")
    
    st.markdown("#### Phân Loại Mức Độ")
    
    severity = st.radio(
        "**Mức độ GERD:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Có biến chứng"],
        key="gerd_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_gerd()
    elif "Trung bình" in severity:
        render_moderate_gerd()
    elif "Nặng" in severity:
        render_severe_gerd()
    else:
        render_complicated_gerd()
    
    st.markdown("---")
    
    st.markdown("### 📋 Phác Đồ Điều Trị Chi Tiết")
    
    treatment_choice = st.selectbox(
        "**Chọn phác đồ:**",
        [
            "PPI - Liều tiêu chuẩn (First-line)",
            "PPI - Liều cao (Nếu không đáp ứng)",
            "H2 Blocker (Nếu không dung nạp PPI)",
            "Antacid (Điều trị triệu chứng)",
            "Prokinetic (Phối hợp)",
            "Surgery (Fundoplication)"
        ],
        key="gerd_treatment"
    )
    
    st.markdown("---")
    
    if "PPI" in treatment_choice and "tiêu chuẩn" in treatment_choice:
        render_ppi_standard()
    elif "PPI" in treatment_choice and "cao" in treatment_choice:
        render_ppi_high_dose()
    elif "H2" in treatment_choice:
        render_h2_blocker()
    elif "Antacid" in treatment_choice:
        render_antacid()
    elif "Prokinetic" in treatment_choice:
        render_prokinetic()
    else:
        render_surgery()
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Điều Trị Dài Hạn")
    
    st.warning("""
    **Khi cần điều trị dài hạn:**
    - GERD mạn tính thường cần điều trị duy trì
    - Mục tiêu: Liều thấp nhất hiệu quả
    
    **Chiến lược:**
    1. **Liều tiêu chuẩn PPI:** 4-8 tuần
    2. **Giảm liều:** Nếu đáp ứng tốt
    3. **Liều duy trì:** PPI liều thấp hoặc on-demand
    4. **Thay đổi lối sống:** Quan trọng
    
    **Theo dõi:**
    - Đánh giá triệu chứng định kỳ
    - Nội soi: Nếu có Barrett hoặc viêm nặng
    - Đánh giá tác dụng phụ PPI (dài hạn)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🏃 Thay Đổi Lối Sống")
    
    with st.expander("📋 Xem khuyến cáo thay đổi lối sống", expanded=True):
        st.markdown("""
        **1. Thay đổi chế độ ăn:**
        - Tránh: Thức ăn cay, chua, béo, cà phê, rượu
        - Ăn nhiều bữa nhỏ
        - Không nằm ngay sau khi ăn (2-3 giờ)
        
        **2. Thay đổi tư thế:**
        - Nâng đầu giường 15-20cm
        - Nằm nghiêng trái
        - Tránh cúi người sau khi ăn
        
        **3. Giảm cân:**
        - Béo phì làm tăng áp lực ổ bụng
        - Giảm cân có thể cải thiện triệu chứng
        
        **4. Tránh thuốc:**
        - NSAIDs, Aspirin
        - Một số thuốc huyết áp (nếu có thể)
        
        **5. Bỏ thuốc lá:**
        - Hút thuốc làm giảm cơ thắt thực quản dưới
        """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người Cao Tuổi:**
        - Triệu chứng có thể không điển hình
        - Nguy cơ biến chứng cao hơn
        - Cẩn thận với tương tác thuốc
        - Theo dõi tác dụng phụ PPI (loãng xương, thiếu B12)
        
        **Có Thai:**
        - **An toàn:** Antacid, Sucralfate
        - **PPI:** Omeprazole, Pantoprazole (Category B)
        - **Tránh:** H2 blocker (dữ liệu hạn chế)
        - **Thay đổi lối sống:** Quan trọng
        """)
    
    with col2:
        st.markdown("""
        **Trẻ Em:**
        - Triệu chứng có thể khác (nôn, quấy khóc)
        - **PPI:** Omeprazole, Lansoprazole (liều tính theo kg)
        - **H2 blocker:** Ranitidine (liều tính theo kg)
        - **Thay đổi lối sống:** Quan trọng
        
        **Barrett Thực Quản:**
        - Điều trị PPI liều cao
        - Nội soi định kỳ (mỗi 3-5 năm)
        - Theo dõi loạn sản
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm Tra")
    
    checklist_items = [
        "✅ Đánh giá triệu chứng và mức độ nặng",
        "✅ Xác định chỉ định nội soi (nếu có)",
        "✅ Bắt đầu PPI liều tiêu chuẩn (4-8 tuần)",
        "✅ Tư vấn thay đổi lối sống",
        "✅ Đánh giá đáp ứng sau 4-8 tuần",
        "✅ Điều chỉnh liều nếu cần",
        "✅ Theo dõi triệu chứng định kỳ",
        "✅ Đánh giá tác dụng phụ PPI (dài hạn)",
        "✅ Nội soi định kỳ nếu có Barrett"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ACG 2022 Guidelines**
       - Katz PO, et al. Am J Gastroenterol. 2022
    
    2. **AGA 2021 Guidelines**
       - Gyawali CP, et al. Gastroenterology. 2021
    
    3. **UpToDate:** Medical management of gastroesophageal reflux disease in adults
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("GERD")
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


def render_mild_gerd():
    """Mild GERD Protocol"""
    st.success("## 🟢 GERD Nhẹ")
    
    st.markdown("### Điều Trị")
    
    st.info("""
    **1. Thay đổi lối sống:**
    - Tránh thức ăn kích thích
    - Nâng đầu giường
    - Giảm cân nếu béo phì
    
    **2. Thuốc:**
    - **PPI liều tiêu chuẩn:** 4-8 tuần
    - **Hoặc:** H2 blocker (nếu không dung nạp PPI)
    - **Hoặc:** Antacid on-demand
    
    **3. Theo dõi:**
    - Đánh giá sau 4-8 tuần
    - Có thể giảm liều hoặc ngừng nếu đáp ứng tốt
    """)


def render_moderate_gerd():
    """Moderate GERD Protocol"""
    st.warning("## 🟡 GERD Trung Bình")
    
    st.markdown("### Điều Trị")
    
    st.info("""
    **1. PPI liều tiêu chuẩn:**
    - **Omeprazole:** 20mg x 2 lần/ngày (trước ăn)
    - **Lansoprazole:** 30mg x 2 lần/ngày
    - **Pantoprazole:** 40mg x 2 lần/ngày
    - **Esomeprazole:** 40mg x 1 lần/ngày
    - **Rabeprazole:** 20mg x 2 lần/ngày
    
    **2. Thời gian:**
    - **4-8 tuần** điều trị ban đầu
    - Sau đó đánh giá và điều chỉnh
    
    **3. Thay đổi lối sống:**
    - Quan trọng, không bỏ qua
    """)


def render_severe_gerd():
    """Severe GERD Protocol"""
    st.error("## 🔴 GERD Nặng")
    
    st.markdown("### Điều Trị")
    
    st.warning("""
    **1. PPI liều cao:**
    - **Omeprazole:** 40mg x 2 lần/ngày
    - **Lansoprazole:** 60mg x 2 lần/ngày
    - **Pantoprazole:** 80mg x 2 lần/ngày
    - **Esomeprazole:** 40mg x 2 lần/ngày
    
    **2. Thời gian:**
    - **8-12 tuần** điều trị ban đầu
    - Sau đó giảm liều nếu đáp ứng
    
    **3. Phối hợp:**
    - **H2 blocker:** Trước khi ngủ (nếu triệu chứng ban đêm)
    - **Prokinetic:** Nếu có rối loạn vận động
    
    **4. Nội soi:**
    - Đánh giá tổn thương
    - Loại trừ biến chứng
    """)


def render_complicated_gerd():
    """Complicated GERD Protocol"""
    st.error("## 🚨 GERD Có Biến Chứng")
    
    st.markdown("### Biến Chứng")
    
    complication = st.selectbox(
        "**Loại biến chứng:**",
        ["Viêm thực quản nặng (Erosive esophagitis)", "Barrett thực quản", "Hẹp thực quản", "Loét thực quản"],
        key="gerd_complication"
    )
    
    st.markdown("### Điều Trị")
    
    st.warning("""
    **1. PPI liều cao:**
    - **Omeprazole:** 40mg x 2 lần/ngày
    - **Thời gian:** 8-12 tuần, sau đó duy trì
    
    **2. Nội soi:**
    - Đánh giá và điều trị biến chứng
    - Dilation nếu hẹp
    - Theo dõi Barrett
    
    **3. Theo dõi:**
    - Nội soi định kỳ
    - Đánh giá đáp ứng
    """)


def render_ppi_standard():
    """PPI Standard Dose"""
    st.success("## 💊 PPI - Liều Tiêu Chuẩn")
    
    st.markdown("### Liều Dùng")
    
    ppi_choice = st.selectbox(
        "**Chọn PPI:**",
        ["Omeprazole", "Lansoprazole", "Pantoprazole", "Esomeprazole", "Rabeprazole"],
        key="ppi_choice"
    )
    
    if "Omeprazole" in ppi_choice:
        st.info("""
        **Omeprazole:**
        - **Liều:** 20mg x 1-2 lần/ngày
        - **Cách dùng:** Uống trước ăn 30 phút
        - **Thời gian:** 4-8 tuần
        """)
    elif "Lansoprazole" in ppi_choice:
        st.info("""
        **Lansoprazole:**
        - **Liều:** 30mg x 1-2 lần/ngày
        - **Cách dùng:** Uống trước ăn 30 phút
        - **Thời gian:** 4-8 tuần
        """)
    elif "Pantoprazole" in ppi_choice:
        st.info("""
        **Pantoprazole:**
        - **Liều:** 40mg x 1-2 lần/ngày
        - **Cách dùng:** Uống trước ăn 30 phút
        - **Thời gian:** 4-8 tuần
        """)
    elif "Esomeprazole" in ppi_choice:
        st.info("""
        **Esomeprazole:**
        - **Liều:** 40mg x 1 lần/ngày (hoặc 20mg x 2 lần/ngày)
        - **Cách dùng:** Uống trước ăn 30 phút
        - **Thời gian:** 4-8 tuần
        """)
    else:
        st.info("""
        **Rabeprazole:**
        - **Liều:** 20mg x 1-2 lần/ngày
        - **Cách dùng:** Uống trước ăn 30 phút
        - **Thời gian:** 4-8 tuần
        """)
    
    st.markdown("### Tác Dụng Phụ")
    
    st.warning("""
    **Tác dụng phụ dài hạn:**
    - Loãng xương (nguy cơ gãy xương)
    - Thiếu vitamin B12
    - Nhiễm trùng (C. diff, viêm phổi)
    - Giảm hấp thu sắt, magie
    
    **Theo dõi:**
    - BMD (Bone Mineral Density) nếu dùng dài hạn
    - Vitamin B12 định kỳ
    - Đánh giá nguy cơ gãy xương
    """)


def render_ppi_high_dose():
    """PPI High Dose"""
    st.warning("## 💊 PPI - Liều Cao")
    
    st.info("""
    **Chỉ định:**
    - Không đáp ứng với liều tiêu chuẩn
    - GERD nặng
    - Có biến chứng
    
    **Liều:**
    - **Omeprazole:** 40mg x 2 lần/ngày
    - **Lansoprazole:** 60mg x 2 lần/ngày
    - **Pantoprazole:** 80mg x 2 lần/ngày
    - **Esomeprazole:** 40mg x 2 lần/ngày
    
    **Thời gian:**
    - **8-12 tuần** điều trị ban đầu
    - Sau đó giảm liều nếu đáp ứng
    """)


def render_h2_blocker():
    """H2 Blocker"""
    st.info("## 💊 H2 Blocker")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Ranitidine:**
    - **Liều:** 150mg x 2 lần/ngày hoặc 300mg x 1 lần/ngày (trước khi ngủ)
    - **Cách dùng:** Uống với hoặc không với thức ăn
    
    **Famotidine:**
    - **Liều:** 20mg x 2 lần/ngày hoặc 40mg x 1 lần/ngày
    
    **Chỉ định:**
    - Không dung nạp PPI
    - GERD nhẹ
    - Triệu chứng ban đêm
    
    **Hiệu quả:**
    - Thấp hơn PPI
    - Phù hợp cho GERD nhẹ
    """)


def render_antacid():
    """Antacid"""
    st.info("## 💊 Antacid")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Chỉ định:**
    - Điều trị triệu chứng on-demand
    - GERD nhẹ, không thường xuyên
    
    **Loại:**
    - **Calcium carbonate:** 500-1000mg khi cần
    - **Magnesium hydroxide:** Khi cần
    - **Aluminum hydroxide:** Khi cần
    
    **Cách dùng:**
    - Uống sau ăn hoặc khi có triệu chứng
    - Không dùng quá 2 tuần liên tục
    """)


def render_prokinetic():
    """Prokinetic"""
    st.info("## 💊 Prokinetic")
    
    st.markdown("### Liều Dùng")
    
    st.warning("""
    **Metoclopramide:**
    - **Liều:** 10mg x 3-4 lần/ngày
    - **Chỉ định:** Rối loạn vận động thực quản
    - **Tác dụng phụ:** Rối loạn vận động (tardive dyskinesia)
    
    **Domperidone:**
    - **Liều:** 10mg x 3-4 lần/ngày
    - **An toàn hơn:** Ít tác dụng phụ thần kinh
    
    **Lưu ý:**
    - Chỉ dùng phối hợp với PPI
    - Không dùng đơn độc
    - Thời gian ngắn (4-8 tuần)
    """)


def render_surgery():
    """Surgery - Fundoplication"""
    st.warning("## 🔪 Phẫu Thuật - Fundoplication")
    
    st.markdown("### Chỉ Định")
    
    st.info("""
    **Chỉ định:**
    - Không đáp ứng với điều trị nội khoa
    - Không muốn dùng thuốc dài hạn
    - Biến chứng (hẹp, Barrett)
    - Thoát vị hoành lớn
    
    **Phương pháp:**
    - **Laparoscopic Nissen fundoplication:** Phổ biến
    - **Toupet fundoplication:** Ít tác dụng phụ
    
    **Kết quả:**
    - Tỷ lệ thành công: 80-90%
    - Tác dụng phụ: Đầy hơi, khó nuốt, ợ hơi
    """)

