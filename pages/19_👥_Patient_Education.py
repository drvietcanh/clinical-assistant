"""
Patient Education Materials Module
Educational materials for patients in simple language
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from patient_education.data import (
    get_all_topics,
    get_topics_by_category,
    get_category_list
)
from patient_education.display import render_patient_education_content

# Standard page setup
setup_page(
    page_title="Giáo dục Bệnh nhân",
    page_icon="👥",
    description="Tài liệu giáo dục bệnh nhân với ngôn ngữ đơn giản, dễ hiểu"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("👥 Giáo dục Bệnh nhân")
    st.caption("Module **Giáo dục Bệnh nhân** – tài liệu giáo dục với ngôn ngữ đơn giản.")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Tất cả", "Theo chủ đề"],
        key="patient_edu_view_mode"
    )
    
    if view_mode == "Theo chủ đề":
        category_filter = st.selectbox(
            "Chọn chủ đề:",
            ["Tất cả"] + get_category_list(),
            key="patient_edu_category_filter"
        )
    
    st.markdown("---")
    st.info("""
    **👥 Patient Education:**
    - Tài liệu giáo dục với **ngôn ngữ đơn giản**
    - Dễ hiểu, dễ đọc
    - **Có thể in** để phát cho bệnh nhân
    - Liên kết với bệnh lý và thuốc
    
    **💡 Lưu ý:**
    - Tài liệu chỉ mang tính tham khảo
    - Không thay thế tư vấn của bác sĩ
    - Cần giải thích thêm cho bệnh nhân
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 👥 Giáo dục Bệnh nhân")
st.markdown("""
**Tài liệu giáo dục bệnh nhân với ngôn ngữ đơn giản, dễ hiểu**

Giúp bệnh nhân hiểu rõ hơn về bệnh tật, thuốc men, và cách chăm sóc sức khỏe.
""")

# Search
search_query = st.text_input(
    "🔍 Tìm kiếm tài liệu:",
    placeholder="Ví dụ: Đái tháo đường, Tăng huyết áp, Kháng sinh...",
    key="patient_edu_search"
)

# Get topics
if view_mode == "Theo chủ đề":
    category = None if category_filter == "Tất cả" else category_filter
    topics = get_topics_by_category(category)
else:
    topics = get_all_topics()

# Filter by search
if search_query:
    search_lower = search_query.lower()
    topics = [t for t in topics if 
              search_lower in t.title.lower() or 
              search_lower in t.title_vn.lower() or
              search_lower in t.content.lower()]

# Display topics
if topics:
    st.success(f"✅ Tìm thấy {len(topics)} tài liệu")
    
    for topic in topics:
        with st.expander(f"**{topic.title_vn}** ({topic.category})", expanded=False):
            render_patient_education_content(topic)
            
            # Print button
            if topic.printable:
                st.markdown("---")
                st.info("💡 Bạn có thể in tài liệu này để phát cho bệnh nhân. Nhấn Ctrl+P hoặc Cmd+P để in.")
else:
    st.warning("Không tìm thấy tài liệu. Vui lòng thử lại với từ khóa khác.")

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Patient Education")
st.markdown("""
**Mục đích:**
- Giúp bệnh nhân hiểu rõ về bệnh tật
- Hướng dẫn sử dụng thuốc đúng cách
- Giáo dục về lối sống lành mạnh
- Tăng tuân thủ điều trị

**Các chủ đề:**
- **Disease:** Thông tin về bệnh lý
- **Medication:** Hướng dẫn dùng thuốc
- **Lifestyle:** Chế độ ăn, tập thể dục

**Lưu ý:**
- Tài liệu được viết bằng ngôn ngữ đơn giản
- Có thể in để phát cho bệnh nhân
- Nên giải thích thêm khi cần
- Không thay thế tư vấn của bác sĩ
""")

# Footer
render_standard_footer(disclaimer=True)

