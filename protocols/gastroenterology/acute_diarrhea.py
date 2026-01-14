"""
Acute Diarrhea Treatment Protocol
ACG 2016, IDSA 2017, WHO Guidelines
Management of acute diarrhea in adults and children
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Diarrhea Treatment Protocol"""
    st.subheader("🫀 Điều trị Tiêu chảy Cấp (Acute Diarrhea)")
    st.caption("ACG 2016, IDSA 2017, WHO - Management of acute diarrhea")
    
    st.info("""
    **Tiêu chảy cấp:**
    - Định nghĩa: ≥3 lần phân lỏng/ngày, <14 ngày
    - Tỷ lệ: Rất phổ biến, đặc biệt ở trẻ em
    - Nguyên nhân: Nhiễm trùng (virus, vi khuẩn, ký sinh trùng), thuốc, thức ăn
    - Biến chứng: Mất nước, rối loạn điện giải
    
    **Phân loại:**
    - **Infectious:** Nhiễm trùng (phổ biến nhất)
    - **Non-infectious:** Thuốc, thức ăn, bệnh lý khác
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Chẩn đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Đánh giá Lâm Sàng")
        st.info("""
        **Triệu chứng:**
        - Số lần đại tiện/ngày
        - Tính chất phân (lỏng, nước, máu, mủ)
        - Đau bụng, sốt, nôn
        - Dấu hiệu mất nước
        
        **Lịch sử:**
        - Tiếp xúc với người bệnh
        - Thức ăn/đồ uống nghi ngờ
        - Du lịch gần đây
        - Thuốc đang dùng
        """)
        
        patient_age = st.selectbox(
            "**Tuổi bệnh nhân:**",
            ["Trẻ em (<18 tuổi)", "Người lớn (≥18 tuổi)"],
            key="diarrhea_age"
        )
        
        stool_frequency = st.number_input(
            "**Số lần đại tiện/ngày:**",
            min_value=1,
            max_value=20,
            value=5,
            key="diarrhea_frequency"
        )
        
        has_blood = st.checkbox("**Có máu trong phân**", key="diarrhea_blood")
        has_fever = st.checkbox("**Có sốt**", key="diarrhea_fever")
    
    with col2:
        st.markdown("#### Đánh giá Mất Nước")
        st.warning("""
        **Dấu hiệu mất nước nhẹ:**
        - Khát nước
        - Khô miệng
        - Giảm nước tiểu
        
        **Dấu hiệu mất nước trung bình:**
        - Mắt trũng
        - Da khô, giảm đàn hồi
        - Mạch nhanh
        
        **Dấu hiệu mất nước nặng:**
        - Hạ huyết áp
        - Sốc
        - Lơ mơ, hôn mê
        """)
        
        dehydration_level = st.radio(
            "**Mức độ mất nước:**",
            ["Không mất nước", "Nhẹ", "Trung bình", "Nặng"],
            key="dehydration_level"
        )
        
        travel_history = st.checkbox("**Có du lịch gần đây**", key="diarrhea_travel")
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### 1. Bù Nước & Điện giải")
    
    if "Trẻ em" in patient_age:
        render_pediatric_rehydration(dehydration_level)
    else:
        render_adult_rehydration(dehydration_level)
    
    st.markdown("#### 2. Điều trị Nguyên nhân")
    
    if has_blood or has_fever or travel_history:
        st.warning("""
        **⚠️ Có thể là nhiễm trùng:**
        - Cần xét nghiệm phân (nếu nặng hoặc kéo dài)
        - Cấy phân: Tìm vi khuẩn
        - Soi phân: Tìm ký sinh trùng
        - Test nhanh: Rotavirus, Norovirus (nếu có)
        """)
    
    etiology = st.selectbox(
        "**Nguyên nhân nghi ngờ:**",
        [
            "Virus (Rotavirus, Norovirus) - Phổ biến nhất",
            "Vi khuẩn (E. coli, Salmonella, Shigella, Campylobacter)",
            "Ký sinh trùng (Giardia, Cryptosporidium)",
            "Thuốc (Kháng sinh, NSAIDs)",
            "Thức ăn (Ngộ độc thực phẩm)",
            "Chưa xác định"
        ],
        key="diarrhea_etiology"
    )
    
    st.markdown("---")
    
    if "Virus" in etiology:
        render_viral_diarrhea()
    elif "Vi khuẩn" in etiology or "Bacteria" in etiology:
        render_bacterial_diarrhea()
    elif "Ký sinh trùng" in etiology or "Parasite" in etiology:
        render_parasitic_diarrhea()
    elif "Thuốc" in etiology or "Drug" in etiology:
        render_drug_induced_diarrhea()
    else:
        render_unknown_diarrhea()
    
    st.markdown("---")
    
    st.markdown("### 💉 Thuốc điều trị triệu chứng")
    
    st.markdown("#### Loperamide (Imodium)")
    
    st.info("""
    **Chỉ định:**
    - Tiêu chảy không có máu, không sốt
    - Người lớn, không có bệnh nền nặng
    
    **Liều:**
    - **Người lớn:** 4mg ban đầu, sau đó 2mg sau mỗi lần đại tiện (max 16mg/ngày)
    - **Trẻ em:** Không khuyến cáo <6 tuổi
    
    **Chống chỉ định:**
    - Tiêu chảy có máu
    - Sốt >38.5°C
    - Nghi ngờ nhiễm trùng nặng
    - Trẻ em <6 tuổi
    """)
    
    st.markdown("#### Bismuth Subsalicylate (Pepto-Bismol)")
    
    st.info("""
    **Chỉ định:**
    - Tiêu chảy nhẹ đến trung bình
    - Có thể giúp giảm triệu chứng
    
    **Liều:**
    - **Người lớn:** 30mL x 4 lần/ngày
    - **Trẻ em:** 5-10mL x 4 lần/ngày (≥12 tuổi)
    
    **Lưu ý:**
    - Tránh ở trẻ em <12 tuổi (nguy cơ Reye syndrome)
    - Phân đen (bình thường)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🍽️ Chế Độ Ăn")
    
    with st.expander("📋 Xem khuyến cáo chế độ ăn", expanded=True):
        st.markdown("""
        **Trong giai đoạn cấp:**
        - **Tiếp tục ăn:** Nếu có thể
        - **Thức ăn nhẹ:** Cơm, cháo, bánh mì, chuối
        - **Tránh:** Thức ăn cay, béo, sữa (nếu không dung nạp)
        
        **Trẻ em:**
        - **Tiếp tục bú mẹ:** Nếu đang bú
        - **Tiếp tục sữa công thức:** Nếu đang dùng
        - **Thức ăn bổ sung:** Cơm, cháo, chuối
        
        **Tránh:**
        - Nước ngọt, nước trái cây (quá nhiều đường)
        - Thức ăn chế biến sẵn
        """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Khi Cần Nhập Viện")
    
    st.error("""
    **Chỉ định nhập viện:**
    - Mất nước nặng
    - Sốc
    - Không uống được
    - Nôn nhiều, không giữ được dịch
    - Tiêu chảy có máu nặng
    - Sốt cao, nhiễm trùng nặng
    - Trẻ em <6 tháng
    - Bệnh nền nặng (suy thận, suy tim)
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Trẻ em:**
        - Nguy cơ mất nước cao hơn
        - Bù nước ưu tiên (ORS)
        - Tiếp tục cho ăn
        - Tránh Loperamide <6 tuổi
        - Theo dõi sát dấu hiệu mất nước
        
        **Người Cao Tuổi:**
        - Nguy cơ mất nước cao
        - Dễ sốc
        - Cẩn thận với thuốc
        - Theo dõi sát
        """)
    
    with col2:
        st.markdown("""
        **Có Thai:**
        - Bù nước quan trọng
        - Tránh Loperamide (dữ liệu hạn chế)
        - Tránh Bismuth (dữ liệu hạn chế)
        - Kháng sinh: Chọn an toàn (Azithromycin)
        
        **Suy Giảm Miễn dịch:**
        - Nguy cơ nhiễm trùng nặng
        - Cần đánh giá sớm
        - Kháng sinh phù hợp
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Đánh giá mức độ mất nước",
        "✅ Bù nước và điện giải (ORS)",
        "✅ Đánh giá nguyên nhân (lịch sử, triệu chứng)",
        "✅ Xét nghiệm phân nếu cần (máu, sốt, du lịch)",
        "✅ Điều trị nguyên nhân nếu xác định",
        "✅ Thuốc điều trị triệu chứng (nếu phù hợp)",
        "✅ Tư vấn chế độ ăn",
        "✅ Theo dõi dấu hiệu mất nước",
        "✅ Đánh giá chỉ định nhập viện"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ACG 2016 Guidelines**
       - Riddle MS, et al. Am J Gastroenterol. 2016
    
    2. **IDSA 2017 Guidelines**
       - Shane AL, et al. Clin Infect Dis. 2017
    
    3. **WHO Guidelines**
       - The treatment of diarrhoea: a manual for physicians and other senior health workers
    
    4. **UpToDate:** Approach to the adult with acute diarrhea in resource-rich settings
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Acute Diarrhea")
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


def render_pediatric_rehydration(dehydration_level):
    """Pediatric Rehydration"""
    st.success("## 💧 Bù Nước Trẻ em")
    
    if "Nặng" in dehydration_level:
        st.error("""
        **Mất nước nặng - Cần nhập viện:**
        - **Truyền tĩnh mạch:** Ringer Lactate hoặc Normal Saline
        - **Liều:** 20mL/kg trong 1 giờ
        - **Sau đó:** 10mL/kg/h cho đến khi ổn định
        - **Chuyển sang ORS:** Khi có thể uống
        """)
    elif "Trung bình" in dehydration_level:
        st.warning("""
        **Mất nước trung bình:**
        - **ORS:** 75mL/kg trong 4 giờ
        - **Sau đó:** 10-15mL/kg sau mỗi lần đại tiện
        - **Theo dõi:** Dấu hiệu sống, nước tiểu
        - **Nếu không uống được:** Truyền tĩnh mạch
        """)
    else:
        st.info("""
        **Mất nước nhẹ/Không mất nước:**
        - **ORS:** 10-15mL/kg sau mỗi lần đại tiện
        - **Tiếp tục cho ăn:** Nếu có thể
        - **Theo dõi:** Dấu hiệu mất nước
        """)


def render_adult_rehydration(dehydration_level):
    """Adult Rehydration"""
    st.success("## 💧 Bù Nước Người lớn")
    
    if "Nặng" in dehydration_level:
        st.error("""
        **Mất nước nặng - Cần nhập viện:**
        - **Truyền tĩnh mạch:** Normal Saline hoặc Ringer Lactate
        - **Liều:** 1-2L trong 1-2 giờ đầu
        - **Sau đó:** Điều chỉnh theo đáp ứng
        - **Chuyển sang uống:** Khi có thể
        """)
    else:
        st.info("""
        **Mất nước nhẹ/Trung bình:**
        - **ORS:** 200-400mL sau mỗi lần đại tiện
        - **Nước:** 1.5-2L/ngày
        - **Tránh:** Nước ngọt, nước trái cây (quá nhiều đường)
        """)


def render_viral_diarrhea():
    """Viral Diarrhea Treatment"""
    st.info("## 🦠 Tiêu chảy Do Virus")
    
    st.markdown("### Điều trị")
    
    st.success("""
    **Nguyên nhân:**
    - Rotavirus (trẻ em)
    - Norovirus (người lớn)
    - Adenovirus
    
    **Điều trị:**
    - **Hỗ trợ:** Bù nước, điện giải
    - **Tự khỏi:** Thường 3-7 ngày
    - **Không cần kháng sinh**
    - **Thuốc:** Loperamide (nếu phù hợp)
    
    **Phòng ngừa:**
    - Rửa tay
    - Vệ sinh môi trường
    - Tiêm phòng Rotavirus (trẻ em)
    """)


def render_bacterial_diarrhea():
    """Bacterial Diarrhea Treatment"""
    st.warning("## 🦠 Tiêu chảy Do Vi Khuẩn")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **Nguyên nhân:**
    - E. coli (ETEC, EHEC)
    - Salmonella
    - Shigella
    - Campylobacter
    
    **Chỉ định kháng sinh:**
    - Tiêu chảy có máu
    - Sốt >38.5°C
    - Nhiễm trùng nặng
    - Suy giảm miễn dịch
    - Du lịch (traveler's diarrhea)
    
    **Kháng sinh:**
    - **Azithromycin:** 500mg/ngày x 3 ngày (người lớn)
    - **Ciprofloxacin:** 500mg x 2 lần/ngày x 3 ngày (nếu nhạy cảm)
    - **Tránh:** Ciprofloxacin nếu kháng (Campylobacter)
    
    **Lưu ý:**
    - Không dùng kháng sinh cho EHEC (E. coli O157:H7)
    - Cấy phân nếu nặng
    """)


def render_parasitic_diarrhea():
    """Parasitic Diarrhea Treatment"""
    st.info("## 🪱 Tiêu chảy Do Ký Sinh Trùng")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **Nguyên nhân:**
    - Giardia lamblia
    - Cryptosporidium
    - Entamoeba histolytica
    
    **Điều trị:**
    - **Giardia:** Metronidazole 250mg x 3 lần/ngày x 5-7 ngày
    - **Cryptosporidium:** Hỗ trợ (tự khỏi ở người khỏe mạnh)
    - **E. histolytica:** Metronidazole + Paromomycin
    
    **Lưu ý:**
    - Soi phân để xác định
    - Điều trị cả gia đình nếu cần
    """)


def render_drug_induced_diarrhea():
    """Drug-Induced Diarrhea Treatment"""
    st.info("## 💊 Tiêu chảy Do Thuốc")
    
    st.markdown("### Điều trị")
    
    st.warning("""
    **Nguyên nhân:**
    - Kháng sinh (C. diff, AAD)
    - NSAIDs
    - Metformin
    - Laxatives
    
    **Điều trị:**
    - **Ngừng thuốc:** Nếu có thể
    - **C. diff:** Vancomycin, Fidaxomicin
    - **Hỗ trợ:** Bù nước, Probiotics
    
    **Lưu ý:**
    - Đánh giá C. diff nếu dùng kháng sinh gần đây
    - Test C. diff nếu có máu, sốt
    """)


def render_unknown_diarrhea():
    """Unknown Etiology Diarrhea Treatment"""
    st.info("## ❓ Tiêu chảy Chưa Xác Định Nguyên nhân")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **Chiến lược:**
    1. **Bù nước:** Quan trọng nhất
    2. **Điều trị triệu chứng:** Loperamide nếu phù hợp
    3. **Theo dõi:** 2-3 ngày
    4. **Xét nghiệm:** Nếu không cải thiện hoặc nặng hơn
    
    **Khi cần xét nghiệm:**
    - Tiêu chảy >7 ngày
    - Có máu, sốt
    - Mất nước nặng
    - Du lịch gần đây
    - Suy giảm miễn dịch
    """)

