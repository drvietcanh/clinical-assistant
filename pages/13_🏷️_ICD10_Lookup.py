"""
ICD-10 Code Lookup Module
International Classification of Diseases, 10th Revision
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero, get_paginated_items
from components.page_sidebar import render_standard_sidebar
from icd10.search import (
    search_by_name,
    search_by_code,
    search_by_category,
    get_code_info,
    get_all_categories
)

# Standard page setup
setup_page(
    page_title="Tra cứu mã ICD-10",
    page_icon="🏷️",
    description="Tra cứu mã ICD-10 - Phân loại quốc tế về bệnh tật, phiên bản 10"
)

# ========== SIDEBAR ==========
filters = render_standard_sidebar(
    title="Tra cứu ICD-10",
    icon="🏷️",
    description="Công cụ tra cứu mã phân loại bệnh tật quốc tế",
    module_group="🏷️ Thông tin Y học",
    filters={
        "search_type": {
            "type": "radio",
            "label": "Tìm kiếm theo:",
            "options": ["Tên bệnh", "Mã ICD-10", "Chuyên khoa"],
            "default": "Tên bệnh",
            "key": "icd10_search_type"
        }
    },
    info_text="""
    **🏷️ ICD-10 Code Lookup:**
    - Tra cứu mã ICD-10 theo **tên bệnh** (tiếng Việt hoặc tiếng Anh)
    - Tra cứu **mã ICD-10** → Tên bệnh
    - Lọc theo **chuyên khoa**
    
    **💡 Lưu ý:**
    - ICD-10 là hệ thống phân loại bệnh tật quốc tế
    - Sử dụng cho mục đích tham khảo và coding
    - Cần xác nhận với guidelines chính thức khi sử dụng
    """
)

search_type = filters.get("search_type", "Tên bệnh")

# ========== MAIN CONTENT ==========

# Use standard hero section
render_hero(
    title="Tra cứu mã ICD-10",
    subtitle="ICD-10 Code Lookup",
    description="International Classification of Diseases, 10th Revision. Tra cứu mã ICD-10 để hỗ trợ coding và billing trong y tế.",
    icon="🏷️",
    gradient=("#667eea", "#764ba2")
)

# Search interface
if search_type == "Tên bệnh":
    st.markdown("### 🔍 Tìm kiếm theo tên bệnh")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input(
            "Nhập tên bệnh (tiếng Việt hoặc tiếng Anh):",
            placeholder="Ví dụ: Đái tháo đường, Diabetes, Pneumonia...",
            key="icd10_name_search"
        )
    with col2:
        category_filter = st.selectbox(
            "Lọc theo chuyên khoa:",
            ["Tất cả"] + get_all_categories(),
            key="icd10_category_filter"
        )
    
    if query:
        category = None if category_filter == "Tất cả" else category_filter
        results = search_by_name(query, category)
        
        if results:
            # Use pagination
            paginated_results = get_paginated_items(results, items_per_page=10, page_key="icd10_name_page")
            
            render_info_box(
                f"Tìm thấy {len(results)} kết quả",
                type="success",
                title="Kết quả tìm kiếm"
            )
            
            # Display results in a table
            for code in paginated_results:
                with st.expander(f"**{code.code}** - {code.name_vn}", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Mã ICD-10:** `{code.code}`")
                        st.markdown(f"**Tên tiếng Việt:** {code.name_vn}")
                        st.markdown(f"**Tên tiếng Anh:** {code.name_en}")
                    with col2:
                        st.markdown(f"**Chuyên khoa:** {code.category}")
                        st.markdown(f"**Chương:** {code.chapter}")
                        if code.block:
                            st.markdown(f"**Block:** {code.block}")
                    if code.notes:
                        render_info_box(
                            code.notes,
                            type="info",
                            title="Ghi chú"
                        )
        else:
            render_info_box(
                "Không tìm thấy kết quả. Vui lòng thử lại với từ khóa khác.",
                type="warning"
            )

elif search_type == "Mã ICD-10":
    st.markdown("### 🔍 Tìm kiếm theo mã ICD-10")
    
    code_query = st.text_input(
        "Nhập mã ICD-10:",
        placeholder="Ví dụ: I10, E11.9, A00.0...",
        key="icd10_code_search"
    )
    
    if code_query:
        result = search_by_code(code_query)
        
        if result:
            render_info_box(
                "Tìm thấy mã ICD-10",
                type="success",
                title="Kết quả"
            )
            
            # Display code information
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Mã ICD-10:** `{result.code}`")
                st.markdown(f"**Tên tiếng Việt:** {result.name_vn}")
                st.markdown(f"**Tên tiếng Anh:** {result.name_en}")
            with col2:
                st.markdown(f"**Chuyên khoa:** {result.category}")
                st.markdown(f"**Chương:** {result.chapter}")
                if result.block:
                    st.markdown(f"**Block:** {result.block}")
            
            if result.notes:
                render_info_box(
                    result.notes,
                    type="info",
                    title="Ghi chú"
                )
        else:
            render_info_box(
                f"Không tìm thấy mã ICD-10: {code_query}",
                type="warning"
            )
            render_info_box(
                "Thử tìm kiếm theo tên bệnh nếu không biết mã chính xác.",
                type="info",
                icon="💡"
            )

else:  # Chuyên khoa
    st.markdown("### 🔍 Tìm kiếm theo chuyên khoa")
    
    selected_category = st.selectbox(
        "Chọn chuyên khoa:",
        get_all_categories(),
        key="icd10_category_search"
    )
    
    if selected_category:
        results = search_by_category(selected_category)
        
        if results:
            # Use pagination
            paginated_results = get_paginated_items(results, items_per_page=10, page_key="icd10_category_page")
            
            render_info_box(
                f"Tìm thấy {len(results)} mã ICD-10 trong chuyên khoa **{selected_category}**",
                type="success",
                title="Kết quả"
            )
            
            # Display results
            for code in paginated_results:
                with st.expander(f"**{code.code}** - {code.name_vn}", expanded=False):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Mã ICD-10:** `{code.code}`")
                        st.markdown(f"**Tên tiếng Việt:** {code.name_vn}")
                        st.markdown(f"**Tên tiếng Anh:** {code.name_en}")
                    with col2:
                        st.markdown(f"**Chuyên khoa:** {code.category}")
                        st.markdown(f"**Chương:** {code.chapter}")
                    if code.notes:
                        render_info_box(
                            code.notes,
                            type="info",
                            title="Ghi chú"
                        )
        else:
            render_info_box(
                f"Không tìm thấy mã ICD-10 nào trong chuyên khoa {selected_category}",
                type="warning"
            )

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về ICD-10")
st.markdown("""
**ICD-10** (International Classification of Diseases, 10th Revision) là hệ thống phân loại bệnh tật quốc tế được Tổ chức Y tế Thế giới (WHO) phát triển.

**Cấu trúc mã ICD-10:**
- **Chương I:** Bệnh truyền nhiễm và ký sinh trùng (A00-B99)
- **Chương II:** Khối u (C00-D49)
- **Chương III:** Bệnh về máu và cơ quan tạo máu (D50-D89)
- **Chương IV:** Bệnh nội tiết, dinh dưỡng và chuyển hóa (E00-E89)
- **Chương V:** Rối loạn tâm thần và hành vi (F01-F99)
- **Chương VI:** Bệnh hệ thần kinh (G00-G99)
- **Chương VII:** Bệnh mắt và phần phụ (H00-H59)
- **Chương VIII:** Bệnh tai và xương chũm (H60-H95)
- **Chương IX:** Bệnh hệ tuần hoàn (I00-I99)
- **Chương X:** Bệnh hệ hô hấp (J00-J99)
- **Chương XI:** Bệnh hệ tiêu hóa (K00-K95)
- **Chương XII:** Bệnh da và mô dưới da (L00-L99)
- **Chương XIII:** Bệnh hệ cơ xương khớp và mô liên kết (M00-M99)
- **Chương XIV:** Bệnh hệ sinh dục tiết niệu (N00-N99)
- **Chương XV:** Thai nghén, sinh đẻ và hậu sản (O00-O9A)
- **Chương XVI:** Một số bệnh lý xuất hiện trong thời kỳ chu sinh (P00-P96)
- **Chương XVII:** Dị tật bẩm sinh và bất thường nhiễm sắc thể (Q00-Q99)
- **Chương XVIII:** Triệu chứng, dấu hiệu và kết quả bất thường (R00-R94)
- **Chương XIX:** Chấn thương, ngộ độc và một số hậu quả khác (S00-T88)
- **Chương XX:** Nguyên nhân bên ngoài của bệnh tật và tử vong (V00-Y99)
- **Chương XXI:** Các yếu tố ảnh hưởng đến tình trạng sức khỏe (Z00-Z99)

**Lưu ý:** Database này chứa các mã ICD-10 phổ biến nhất. Để tra cứu đầy đủ, vui lòng tham khảo tài liệu chính thức của WHO.
""")

# Footer
render_standard_footer(disclaimer=True)

