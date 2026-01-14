"""
Patient Education Materials Module
Educational materials for patients in simple language
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box
from components.page_sidebar import render_standard_sidebar
from patient_education.data import (
    get_all_topics,
    get_topics_by_category,
    get_category_list
)
from patient_education.display import render_patient_education_content
from components.patient_education import (
    render_topic_grid,
    render_enhanced_search,
    render_category_filters,
    render_enhanced_content,
    render_related_topics,
    render_hero_section,
    filter_topics_by_search
)

# Standard page setup
setup_page(
    page_title="Giáo dục Bệnh nhân",
    page_icon="👥",
    description="Tài liệu giáo dục bệnh nhân với ngôn ngữ đơn giản, dễ hiểu"
)

# ========== SIDEBAR ==========
filters = render_standard_sidebar(
    title="Giáo dục Bệnh nhân",
    icon="👥",
    description="Tài liệu giáo dục với ngôn ngữ đơn giản",
    module_group="👥 Thông tin Y học",
    filters={
        "view_mode": {
            "type": "radio",
            "label": "Chế độ xem:",
            "options": ["Thẻ", "Danh sách"],
            "default": "Thẻ",
            "key": "patient_edu_view_mode"
        },
        "category": {
            "type": "selectbox",
            "label": "Chọn chủ đề:",
            "options": ["Tất cả"] + get_category_list(),
            "default": "Tất cả",
            "key": "patient_edu_category_filter",
        }
    },
    info_text="""
    **👥 Patient Education:**
    - Tài liệu giáo dục với **ngôn ngữ đơn giản**
    - Dễ hiểu, dễ đọc
    - **Có thể in** để phát cho bệnh nhân
    - Liên kết với bệnh lý và thuốc
    
    **💡 Lưu ý:**
    - Tài liệu chỉ mang tính tham khảo
    - Không thay thế tư vấn của bác sĩ
    - Cần giải thích thêm cho bệnh nhân
    """
)

view_mode = filters.get("view_mode", "Thẻ")
category_filter = filters.get("category", "Tất cả")

# ========== MAIN CONTENT ==========

# Hero Section
all_topics = get_all_topics()
render_hero_section(all_topics, show_featured=True)

# Search Section
st.markdown("### 🔍 Tìm kiếm")
search_query = render_enhanced_search(
    all_topics,
    placeholder="Tìm kiếm bệnh, thuốc, hướng dẫn...",
    show_filters=True,
    show_suggestions=True,
    key="patient_edu_search"
)

# Category Filters
st.markdown("---")
selected_category = render_category_filters(
    all_topics,
    active_category=None if category_filter == "Tất cả" else category_filter,
    show_counts=True,
    key="patient_edu_category_buttons"
)

# Use selected category from buttons or sidebar
if selected_category is not None:
    category_filter = selected_category

# Get topics based on filters
if category_filter == "Tất cả":
    topics = get_all_topics()
else:
    topics = get_topics_by_category(category_filter)

# Apply search filter
if search_query and search_query.strip():
    topics = filter_topics_by_search(topics, search_query)

# Display topics
st.markdown("---")
st.markdown("### 📚 Tài liệu")

if topics:
    # Show stats
    st.info(f"📊 Tìm thấy **{len(topics)}** tài liệu" + (f" cho '{search_query}'" if search_query else ""))
    
    st.markdown("")
    
    # View mode: Cards or List
    if view_mode == "Thẻ":
        # Card grid layout
        # Determine columns based on screen size (responsive)
        cols = 3  # Default for desktop
        
        render_topic_grid(
            topics,
            columns=cols,
            show_preview=True,
            search_query=search_query
        )
        
        # Add expandable content below for detailed view
        st.markdown("---")
        st.markdown("### 📖 Xem chi tiết")
        st.caption("Chọn tài liệu bên dưới để xem nội dung đầy đủ:")
        
        # Show topics in expanders for detailed view
        for topic in topics:
            with st.expander(f"**{topic.title_vn}** ({topic.category})", expanded=False):
                # Use enhanced content viewer
                render_enhanced_content(
                    topic,
                    show_toc=True,
                    show_progress=True,
                    search_query=search_query
                )
                
                # Related topics
                render_related_topics(topic, all_topics)
                
                # Related resources
                render_patient_education_content(topic)
                
                # Print button
                if topic.printable:
                    st.markdown("---")
                    render_info_box(
                        "Bạn có thể in tài liệu này để phát cho bệnh nhân. Nhấn Ctrl+P hoặc Cmd+P để in.",
                        type="info",
                        icon="🖨️"
                    )
    else:
        # List view with expanders (original)
        for topic in topics:
            with st.expander(f"**{topic.title_vn}** ({topic.category})", expanded=False):
                # Use enhanced content viewer
                render_enhanced_content(
                    topic,
                    show_toc=True,
                    show_progress=False,
                    search_query=search_query
                )
                
                # Related topics
                render_related_topics(topic, all_topics)
                
                # Original content
                render_patient_education_content(topic)
                
                # Print button
                if topic.printable:
                    st.markdown("---")
                    render_info_box(
                        "Bạn có thể in tài liệu này để phát cho bệnh nhân. Nhấn Ctrl+P hoặc Cmd+P để in.",
                        type="info",
                        icon="🖨️"
                    )
else:
    render_info_box(
        "Không tìm thấy tài liệu. Vui lòng thử lại với từ khóa khác hoặc chọn chủ đề khác.",
        type="warning"
    )

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
