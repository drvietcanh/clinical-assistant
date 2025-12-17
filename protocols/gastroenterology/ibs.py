"""
IBS (Irritable Bowel Syndrome) Treatment Protocol
ACG 2021, Rome IV 2016 Guidelines
Management of irritable bowel syndrome
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """IBS Treatment Protocol"""
    st.subheader("🫀 Điều trị Hội Chứng Ruột Kích Thích (IBS)")
    st.caption("ACG 2021, Rome IV 2016 - Management of irritable bowel syndrome")
    
    st.info("""
    **Hội chứng ruột kích thích (IBS):**
    - Tỷ lệ ở Việt Nam: ~5-10% dân số
    - Định nghĩa: Rối loạn chức năng ruột mạn tính
    - Triệu chứng: Đau bụng, thay đổi thói quen đại tiện
    - Không có tổn thương thực thể
    
    **Phân loại (theo Rome IV):**
    - **IBS-D:** Tiêu chảy (Diarrhea)
    - **IBS-C:** Táo bón (Constipation)
    - **IBS-M:** Hỗn hợp (Mixed)
    - **IBS-U:** Không phân loại (Unclassified)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Chẩn đoán")
    
    st.markdown("#### Tiêu chuẩn Rome IV")
    
    st.info("""
    **Chẩn đoán IBS khi có:**
    1. **Đau bụng tái phát** ≥1 ngày/tuần trong 3 tháng
    2. **Liên quan với:** ≥2 trong số:
       - Liên quan với đại tiện
       - Thay đổi tần số đại tiện
       - Thay đổi hình dạng phân
    3. **Triệu chứng bắt đầu** ≥6 tháng trước
    
    **Cần loại trừ:**
    - Bệnh thực thể (viêm, khối u)
    - Bệnh celiac
    - Nhiễm trùng
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Phân loại IBS")
    
    ibs_type = st.radio(
        "**Loại IBS:**",
        ["IBS-D (Tiêu chảy)", "IBS-C (Táo bón)", "IBS-M (Hỗn hợp)", "IBS-U (Không phân loại)"],
        key="ibs_type"
    )
    
    st.markdown("---")
    
    if "IBS-D" in ibs_type or "Tiêu chảy" in ibs_type:
        render_ibs_d()
    elif "IBS-C" in ibs_type or "Táo bón" in ibs_type:
        render_ibs_c()
    elif "IBS-M" in ibs_type or "Hỗn hợp" in ibs_type:
        render_ibs_m()
    else:
        render_ibs_u()
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Chung")
    
    st.markdown("#### 1. Thay Đổi Lối Sống")
    
    with st.expander("📋 Xem khuyến cáo thay đổi lối sống", expanded=True):
        st.markdown("""
        **1. Chế độ ăn:**
        - **FODMAP thấp:** Thử trong 4-6 tuần
          - Tránh: Lactose, fructose, fructans, galactans, polyols
          - Giảm: Hành, tỏi, táo, lúa mì, sữa
        - **Chất xơ:** Tăng dần (nếu IBS-C)
        - **Tránh:** Thức ăn kích thích, rượu, cà phê
        
        **2. Tập thể dục:**
        - Tập thể dục đều đặn
        - Giảm stress
        
        **3. Quản lý stress:**
        - Yoga, thiền
        - Tư vấn tâm lý nếu cần
        - Ngủ đủ giấc
        """)
    
    st.markdown("#### 2. Thuốc Điều trị")
    
    treatment_category = st.selectbox(
        "**Nhóm thuốc:**",
        [
            "Antispasmodics (Giảm co thắt)",
            "Antidiarrheals (Chống tiêu chảy - IBS-D)",
            "Laxatives (Nhuận tràng - IBS-C)",
            "Probiotics (Men vi sinh)",
            "Antidepressants (Chống trầm cảm)",
            "Antibiotics (Kháng sinh - Rifaximin)"
        ],
        key="ibs_treatment_category"
    )
    
    st.markdown("---")
    
    if "Antispasmodics" in treatment_category or "co thắt" in treatment_category:
        render_antispasmodics()
    elif "Antidiarrheals" in treatment_category or "tiêu chảy" in treatment_category:
        render_antidiarrheals()
    elif "Laxatives" in treatment_category or "Nhuận tràng" in treatment_category:
        render_laxatives()
    elif "Probiotics" in treatment_category or "Men vi sinh" in treatment_category:
        render_probiotics()
    elif "Antidepressants" in treatment_category or "trầm cảm" in treatment_category:
        render_antidepressants()
    else:
        render_rifaximin()
    
    st.markdown("---")
    
    st.markdown("### 📋 Phác Đồ Điều trị Theo Loại")
    
    st.markdown("#### IBS-D (Tiêu Chảy)")
    
    st.info("""
    **Bước 1: Thay đổi lối sống**
    - FODMAP thấp
    - Tránh thức ăn kích thích
    
    **Bước 2: Thuốc**
    - **Loperamide:** 2-4mg khi cần (max 16mg/ngày)
    - **Rifaximin:** 550mg x 3 lần/ngày x 14 ngày (nếu cần)
    - **Eluxadoline:** 100mg x 2 lần/ngày (nếu có)
    
    **Bước 3: Nếu không đáp ứng**
    - **Tricyclic antidepressants:** Amitriptyline 10-50mg/ngày
    - **SSRI:** Nếu có lo âu/trầm cảm
    """)
    
    st.markdown("#### IBS-C (Táo Bón)")
    
    st.info("""
    **Bước 1: Thay đổi lối sống**
    - Tăng chất xơ (từ từ)
    - Uống đủ nước
    - Tập thể dục
    
    **Bước 2: Thuốc**
    - **Polyethylene glycol (PEG):** 17-34g/ngày
    - **Linaclotide:** 290mcg x 1 lần/ngày (nếu có)
    - **Lubiprostone:** 8mcg x 2 lần/ngày (nếu có)
    - **Prucalopride:** 2mg x 1 lần/ngày (nếu có)
    
    **Bước 3: Nếu không đáp ứng**
    - **SSRI:** Nếu có lo âu/trầm cảm
    """)
    
    st.markdown("#### IBS-M (Hỗn Hợp)")
    
    st.info("""
    **Điều trị theo triệu chứng chính:**
    - Nếu tiêu chảy nhiều hơn → Điều trị như IBS-D
    - Nếu táo bón nhiều hơn → Điều trị như IBS-C
    - Có thể cần phối hợp
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Phụ Nữ:**
        - IBS phổ biến hơn ở phụ nữ
        - Triệu chứng có thể thay đổi theo chu kỳ kinh nguyệt
        - Cẩn thận với thuốc trong thai kỳ
        
        **Người Cao Tuổi:**
        - Triệu chứng có thể khác
        - Cần loại trừ bệnh thực thể kỹ hơn
        - Cẩn thận với tương tác thuốc
        """)
    
    with col2:
        st.markdown("""
        **Trẻ Em:**
        - Chẩn đoán khó hơn
        - Triệu chứng có thể khác
        - Điều trị tương tự nhưng liều điều chỉnh
        
        **Có Thai:**
        - **An toàn:** PEG, Loperamide (ngắn hạn)
        - **Tránh:** Hầu hết thuốc khác
        - **Thay đổi lối sống:** Quan trọng
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm tra")
    
    checklist_items = [
        "✅ Đánh giá triệu chứng theo Rome IV",
        "✅ Phân loại IBS (D/C/M/U)",
        "✅ Loại trừ bệnh thực thể (nếu cần)",
        "✅ Tư vấn thay đổi lối sống (FODMAP, tập thể dục)",
        "✅ Chọn thuốc phù hợp theo loại IBS",
        "✅ Đánh giá đáp ứng sau 4-8 tuần",
        "✅ Điều chỉnh điều trị nếu cần",
        "✅ Quản lý stress và lo âu",
        "✅ Theo dõi triệu chứng định kỳ"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ACG 2021 Guidelines**
       - Lacy BE, et al. Am J Gastroenterol. 2021
    
    2. **Rome IV Criteria 2016**
       - Drossman DA, Hasler WL. Gastroenterology. 2016
    
    3. **UpToDate:** Treatment of irritable bowel syndrome
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("IBS")
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


def render_ibs_d():
    """IBS-D Protocol"""
    st.success("## 💊 IBS-D (Tiêu Chảy)")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **1. Thay đổi lối sống:**
    - FODMAP thấp
    - Tránh thức ăn kích thích
    
    **2. Thuốc:**
    - **Loperamide:** 2-4mg khi cần (max 16mg/ngày)
    - **Rifaximin:** 550mg x 3 lần/ngày x 14 ngày
    - **Eluxadoline:** 100mg x 2 lần/ngày (nếu có)
    
    **3. Nếu không đáp ứng:**
    - **Amitriptyline:** 10-50mg/ngày (tăng dần)
    - **SSRI:** Nếu có lo âu/trầm cảm
    """)


def render_ibs_c():
    """IBS-C Protocol"""
    st.success("## 💊 IBS-C (Táo Bón)")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **1. Thay đổi lối sống:**
    - Tăng chất xơ (từ từ)
    - Uống đủ nước
    - Tập thể dục
    
    **2. Thuốc:**
    - **PEG:** 17-34g/ngày
    - **Linaclotide:** 290mcg x 1 lần/ngày (nếu có)
    - **Lubiprostone:** 8mcg x 2 lần/ngày (nếu có)
    - **Prucalopride:** 2mg x 1 lần/ngày (nếu có)
    
    **3. Nếu không đáp ứng:**
    - **SSRI:** Nếu có lo âu/trầm cảm
    """)


def render_ibs_m():
    """IBS-M Protocol"""
    st.warning("## 💊 IBS-M (Hỗn Hợp)")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **Chiến lược:**
    - Điều trị theo triệu chứng chính
    - Nếu tiêu chảy nhiều → Điều trị như IBS-D
    - Nếu táo bón nhiều → Điều trị như IBS-C
    - Có thể cần phối hợp
    
    **Thuốc:**
    - **Antispasmodics:** Giảm đau bụng
    - **Probiotics:** Có thể giúp
    - **Antidepressants:** Nếu có lo âu/trầm cảm
    """)


def render_ibs_u():
    """IBS-U Protocol"""
    st.info("## 💊 IBS-U (Không Phân loại)")
    
    st.markdown("### Điều trị")
    
    st.info("""
    **Chiến lược:**
    - Điều trị triệu chứng chính
    - Thay đổi lối sống
    - Antispasmodics
    - Probiotics
    - Antidepressants nếu cần
    """)


def render_antispasmodics():
    """Antispasmodics"""
    st.info("## 💊 Antispasmodics (Giảm Co Thắt)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Hyoscine Butylbromide:**
    - **Liều:** 10-20mg x 3 lần/ngày
    - **Cách dùng:** Uống trước ăn
    
    **Mebeverine:**
    - **Liều:** 135mg x 3 lần/ngày
    - **Cách dùng:** Uống trước ăn
    
    **Dicyclomine:**
    - **Liều:** 10-20mg x 3-4 lần/ngày
    
    **Chỉ định:**
    - Đau bụng do co thắt
    - Dùng khi cần (on-demand) hoặc thường xuyên
    
    **Tác dụng phụ:**
    - Khô miệng, mờ mắt (hiếm)
    - Táo bón (nếu dùng nhiều)
    """)


def render_antidiarrheals():
    """Antidiarrheals"""
    st.info("## 💊 Antidiarrheals (Chống Tiêu Chảy)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Loperamide:**
    - **Liều:** 2-4mg khi cần
    - **Tối đa:** 16mg/ngày
    - **Cách dùng:** Sau mỗi lần tiêu chảy
    
    **Chỉ định:**
    - IBS-D
    - Tiêu chảy không kiểm soát được
    
    **Lưu ý:**
    - Không dùng quá liều
    - Ngừng nếu táo bón
    - Tránh ở nhiễm trùng nặng
    """)


def render_laxatives():
    """Laxatives"""
    st.info("## 💊 Laxatives (Nhuận Tràng)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Polyethylene Glycol (PEG):**
    - **Liều:** 17-34g/ngày
    - **Cách dùng:** Pha với nước, uống 1 lần/ngày
    - **An toàn:** Có thể dùng dài hạn
    
    **Lactulose:**
    - **Liều:** 15-30mL x 1-2 lần/ngày
    - **Tác dụng phụ:** Đầy hơi
    
    **Linaclotide:**
    - **Liều:** 290mcg x 1 lần/ngày
    - **Cách dùng:** Uống trước ăn 30 phút
    - **Chỉ định:** IBS-C
    
    **Chỉ định:**
    - IBS-C
    - Táo bón mạn tính
    """)


def render_probiotics():
    """Probiotics"""
    st.info("## 💊 Probiotics (Men Vi Sinh)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Chủng vi khuẩn:**
    - **Bifidobacterium:** Có thể giúp
    - **Lactobacillus:** Có thể giúp
    - **Saccharomyces boulardii:** Có thể giúp
    
    **Liều:**
    - Theo hướng dẫn nhà sản xuất
    - Thường: 1-2 viên/ngày
    
    **Hiệu quả:**
    - Có thể giúp một số bệnh nhân
    - Không phải tất cả đều đáp ứng
    - Thử trong 4-8 tuần
    
    **An toàn:**
    - Rất an toàn
    - Ít tác dụng phụ
    """)


def render_antidepressants():
    """Antidepressants"""
    st.warning("## 💊 Antidepressants (Chống Trầm Cảm)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Tricyclic Antidepressants (TCA):**
    - **Amitriptyline:** 10-50mg/ngày (tăng dần)
    - **Imipramine:** 25-75mg/ngày
    - **Cách dùng:** Uống trước khi ngủ
    - **Chỉ định:** IBS-D, đau bụng
    
    **SSRI:**
    - **Sertraline:** 50-100mg/ngày
    - **Paroxetine:** 20-40mg/ngày
    - **Chỉ định:** IBS-C, lo âu/trầm cảm
    
    **Cơ chế:**
    - Giảm đau (tác dụng trung ương)
    - Điều chỉnh vận động ruột
    - Giảm lo âu
    
    **Lưu ý:**
    - Bắt đầu liều thấp
    - Tăng dần
    - Tác dụng phụ: Khô miệng, buồn ngủ (TCA)
    """)


def render_rifaximin():
    """Rifaximin"""
    st.info("## 💊 Rifaximin (Kháng sinh)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Rifaximin:**
    - **Liều:** 550mg x 3 lần/ngày
    - **Thời gian:** 14 ngày
    - **Chỉ định:** IBS-D
    
    **Cơ chế:**
    - Kháng sinh phổ rộng, không hấp thu
    - Điều chỉnh hệ vi sinh đường ruột
    
    **Hiệu quả:**
    - Có thể giúp một số bệnh nhân IBS-D
    - Có thể lặp lại nếu cần (sau 4 tuần)
    
    **An toàn:**
    - Rất an toàn (không hấp thu)
    - Ít tác dụng phụ
    - Không kháng thuốc (do không hấp thu)
    """)

