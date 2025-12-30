"""
Pill Identifier Module
Identify medications by physical characteristics
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from pill_identifier.search import search_pills_by_attributes
from pill_identifier.data import (
    get_color_list,
    get_shape_list
)

# Standard page setup
setup_page(
    page_title="Nhận diện Thuốc",
    page_icon="💊",
    description="Nhận diện thuốc qua đặc điểm vật lý: màu sắc, hình dạng, ký hiệu"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Nhận diện Thuốc")
    st.caption("Module **Nhận diện Thuốc** – xác định thuốc qua đặc điểm vật lý.")
    
    st.markdown("---")
    render_info_box(
        """
        **💊 Pill Identifier:**
        - Nhập **màu sắc, hình dạng, ký hiệu** của viên thuốc
        - Tìm kiếm và xác định thuốc
        - Xem thông tin chi tiết về thuốc
        
        **💡 Lưu ý:**
        - Cần quan sát kỹ viên thuốc
        - Ký hiệu trên thuốc rất quan trọng
        - Kết quả chỉ mang tính tham khảo
        - Luôn xác nhận với bác sĩ/dược sĩ
        """,
        type="info",
        title="Thông tin Module"
    )

# ========== MAIN CONTENT ==========

# Use standard hero section
render_hero(
    title="Nhận diện Thuốc",
    subtitle="Pill Identifier",
    description="Xác định thuốc qua đặc điểm vật lý: màu sắc, hình dạng, ký hiệu. Nhập thông tin về viên thuốc để tìm kiếm và xác định thuốc.",
    icon="💊",
    gradient=("#667eea", "#764ba2")
)

# Input form
st.markdown("### 📝 Thông tin Viên thuốc")

col1, col2 = st.columns(2)

with col1:
    color = st.selectbox(
        "Màu sắc:",
        ["Tất cả"] + get_color_list(),
        key="pill_color"
    )
    
    shape = st.selectbox(
        "Hình dạng:",
        ["Tất cả"] + get_shape_list(),
        key="pill_shape"
    )

with col2:
    imprint = st.text_input(
        "Ký hiệu trên thuốc (nếu có):",
        placeholder="Ví dụ: AMOX 500, MET 500, ATV 20...",
        key="pill_imprint",
        help="Nhập chữ hoặc số trên viên thuốc"
    )
    
    size = st.selectbox(
        "Kích thước:",
        ["Tất cả", "Small", "Medium", "Large"],
        key="pill_size"
    )

# Search button
if st.button("🔍 Tìm kiếm Thuốc", type="primary", use_container_width=True):
    # Prepare search parameters
    color_param = None if color == "Tất cả" else color
    shape_param = None if shape == "Tất cả" else shape
    imprint_param = imprint.strip() if imprint else None
    size_param = None if size == "Tất cả" else size
    
    # Search
    results = search_pills_by_attributes(
        color=color_param,
        shape=shape_param,
        imprint=imprint_param,
        size=size_param
    )
    
    st.session_state['pill_identifier_results'] = {
        'results': results,
        'search_params': {
            'color': color_param,
            'shape': shape_param,
            'imprint': imprint_param,
            'size': size_param
        }
    }
    st.rerun()

# Display results
if 'pill_identifier_results' in st.session_state:
    results = st.session_state['pill_identifier_results']['results']
    search_params = st.session_state['pill_identifier_results']['search_params']
    
    st.markdown("---")
    st.markdown("### 📊 Kết quả Tìm kiếm")
    
    # Show search parameters
    params_display = []
    if search_params['color']:
        params_display.append(f"Màu: {search_params['color']}")
    if search_params['shape']:
        params_display.append(f"Hình dạng: {search_params['shape']}")
    if search_params['imprint']:
        params_display.append(f"Ký hiệu: {search_params['imprint']}")
    if search_params['size']:
        params_display.append(f"Kích thước: {search_params['size']}")
    
    if params_display:
        render_info_box(
            "**Tìm kiếm theo:** " + ", ".join(params_display),
            type="info"
        )
    
    if results:
        render_info_box(
            f"Tìm thấy {len(results)} kết quả",
            type="success",
            title="Kết quả tìm kiếm"
        )
        
        for pill in results:
            with st.expander(f"**{pill.drug_name}** ({pill.generic_name})", expanded=False):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown(f"**Tên thuốc:** {pill.drug_name}")
                    st.markdown(f"**Tên generic:** {pill.generic_name}")
                    st.markdown(f"**Liều lượng:** {pill.strength}")
                    st.markdown(f"**Dạng:** {pill.form}")
                
                with col2:
                    st.markdown(f"**Màu sắc:** {pill.color}")
                    st.markdown(f"**Hình dạng:** {pill.shape}")
                    st.markdown(f"**Kích thước:** {pill.size}")
                    if pill.imprint:
                        st.markdown(f"**Ký hiệu:** {pill.imprint}")
                
                if pill.notes:
                    render_info_box(
                        pill.notes,
                        type="info",
                        title="Ghi chú"
                    )
                
                # Link to Drug Database
                st.markdown("---")
                st.markdown(f"💡 Xem thêm thông tin về **{pill.drug_name}** trong [Cơ sở dữ liệu thuốc](?page=07_💊_Drug_Database)")
    else:
        render_info_box(
            "Không tìm thấy thuốc phù hợp. Vui lòng thử lại với thông tin khác.",
            type="warning"
        )
        render_info_box(
            """
            **💡 Gợi ý:**
            - Kiểm tra lại màu sắc và hình dạng
            - Đọc kỹ ký hiệu trên thuốc (có thể cần kính lúp)
            - Thử tìm kiếm chỉ với màu sắc và hình dạng (bỏ qua ký hiệu)
            - Tham khảo dược sĩ nếu không tìm thấy
            """,
            type="info",
            icon="💡"
        )
    
    # Clear button
    if st.button("🗑️ Xóa kết quả", use_container_width=True):
        if 'pill_identifier_results' in st.session_state:
            del st.session_state['pill_identifier_results']
        st.rerun()

# Instructions
st.markdown("---")
st.markdown("### 📖 Hướng dẫn Sử dụng")
st.markdown("""
**Cách nhận diện thuốc:**

1. **Quan sát màu sắc:**
   - Màu chính của viên thuốc
   - Có thể có nhiều màu (ví dụ: viên nang có 2 màu)

2. **Quan sát hình dạng:**
   - Round (Tròn)
   - Oval (Bầu dục)
   - Capsule (Viên nang)
   - Các hình dạng khác

3. **Đọc ký hiệu:**
   - Chữ hoặc số trên viên thuốc
   - Có thể cần kính lúp để đọc rõ
   - Ký hiệu rất quan trọng để xác định chính xác

4. **Ước lượng kích thước:**
   - So sánh với các viên thuốc khác
   - Small (Nhỏ), Medium (Trung bình), Large (Lớn)

**Lưu ý:**
- ⚠️ Kết quả chỉ mang tính tham khảo
- ⚠️ Luôn xác nhận với bác sĩ/dược sĩ trước khi dùng
- ⚠️ Không tự ý dùng thuốc không rõ nguồn gốc
- ⚠️ Database có thể không đầy đủ - một số thuốc có thể không có trong database
""")

# Footer
render_standard_footer(disclaimer=True)

