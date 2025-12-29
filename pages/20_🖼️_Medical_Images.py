"""
Medical Image Library Module
Library of medical images for education and reference
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from medical_images.search import (
    search_images,
    get_image_info
)
from medical_images.data import (
    get_all_images,
    get_images_by_category,
    get_images_by_type,
    get_category_list,
    get_image_type_list
)

# Standard page setup
setup_page(
    page_title="Thư viện Hình ảnh Y khoa",
    page_icon="🖼️",
    description="Thư viện hình ảnh y khoa: X-ray, CT, MRI, Ultrasound, ECG, Clinical photos, Pathology"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("🖼️ Thư viện Hình ảnh")
    st.caption("Module **Thư viện Hình ảnh Y khoa** – hình ảnh y khoa để học tập và tham khảo.")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Tất cả", "Theo loại", "Theo chuyên khoa"],
        key="medical_images_view_mode"
    )
    
    if view_mode == "Theo loại":
        type_filter = st.selectbox(
            "Chọn loại hình ảnh:",
            ["Tất cả"] + get_image_type_list(),
            key="medical_images_type_filter"
        )
    elif view_mode == "Theo chuyên khoa":
        category_filter = st.selectbox(
            "Chọn chuyên khoa:",
            ["Tất cả"] + get_category_list(),
            key="medical_images_category_filter"
        )
    
    st.markdown("---")
    st.info("""
    **🖼️ Medical Image Library:**
    - **X-ray, CT, MRI, Ultrasound**
    - **ECG, Clinical photos**
    - **Pathology images**
    - Có chú thích và giải thích
    
    **💡 Lưu ý:**
    - Hình ảnh chỉ mang tính giáo dục
    - Cần có kiến thức y khoa để hiểu
    - Không thay thế đánh giá lâm sàng
    """)

# ========== MAIN CONTENT ==========

st.markdown("## 🖼️ Thư viện Hình ảnh Y khoa")
st.markdown("""
**Thư viện hình ảnh y khoa để học tập và tham khảo**

Bao gồm: X-ray, CT, MRI, Ultrasound, ECG, ảnh lâm sàng, và giải phẫu bệnh.
""")

# Search
search_query = st.text_input(
    "🔍 Tìm kiếm hình ảnh:",
    placeholder="Ví dụ: Pneumonia, STEMI, Stroke...",
    key="medical_images_search"
)

# Get images based on view mode
if view_mode == "Theo loại":
    image_type = None if type_filter == "Tất cả" else type_filter
    images = get_images_by_type(image_type)
elif view_mode == "Theo chuyên khoa":
    category = None if category_filter == "Tất cả" else category_filter
    images = get_images_by_category(category)
else:
    images = get_all_images()

# Filter by search
if search_query:
    images = search_images(search_query)

# Display images
if images:
    st.success(f"✅ Tìm thấy {len(images)} hình ảnh")
    
    for img in images:
        with st.expander(f"**{img.title_vn}** ({img.image_type})", expanded=False):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Loại:** {img.image_type}")
                st.markdown(f"**Chuyên khoa:** {img.category}")
                
                if img.description:
                    st.markdown(f"**Mô tả:** {img.description}")
                
                if img.findings:
                    st.markdown("**🔍 Dấu hiệu cần tìm:**")
                    st.info(img.findings)
                
                if img.diagnosis:
                    st.markdown(f"**Chẩn đoán:** {img.diagnosis}")
            
            with col2:
                if img.related_disease:
                    st.markdown(f"**Bệnh lý:** {img.related_disease}")
                    st.markdown(f"💡 Xem thêm trong [Bách khoa Bệnh lý](?page=16_📖_Disease_Encyclopedia)")
                
                if img.related_scores:
                    st.markdown("**Thang điểm:**")
                    for score in img.related_scores:
                        st.markdown(f"- {score}")
            
            # Image placeholder
            if img.url:
                st.image(img.url, caption=img.title_vn, use_container_width=True)
            else:
                st.info("📷 **Hình ảnh:** Hình ảnh sẽ được thêm vào trong tương lai. Hiện tại hiển thị metadata và mô tả.")
            
            if img.notes:
                st.caption(f"**Ghi chú:** {img.notes}")
            
            if img.source:
                st.caption(f"**Nguồn:** {img.source}")
else:
    st.warning("Không tìm thấy hình ảnh. Vui lòng thử lại với từ khóa khác.")

# Additional information
st.markdown("---")
st.markdown("### 📚 Thông tin về Medical Image Library")
st.markdown("""
**Các loại hình ảnh:**

1. **X-ray (X-quang):**
   - X-quang ngực, xương, bụng
   - Nhanh, rẻ, dễ tiếp cận
   - Hữu ích cho chấn thương, viêm phổi, COPD

2. **CT (Computed Tomography):**
   - CT não, ngực, bụng
   - Chi tiết hơn X-ray
   - Hữu ích cho đột quỵ, chấn thương, ung thư

3. **MRI (Magnetic Resonance Imaging):**
   - MRI não, cột sống, khớp
   - Không có bức xạ
   - Hữu ích cho thần kinh, cơ xương khớp

4. **Ultrasound (Siêu âm):**
   - Siêu âm bụng, tim, mạch máu
   - An toàn, không bức xạ
   - Hữu ích cho thai kỳ, tim mạch, gan mật

5. **ECG (Điện tâm đồ):**
   - Ghi lại hoạt động điện của tim
   - Nhanh, rẻ
   - Hữu ích cho rối loạn nhịp tim, nhồi máu cơ tim

6. **Clinical Photos (Ảnh lâm sàng):**
   - Ảnh bệnh nhân, tổn thương da
   - Hữu ích cho da liễu, chấn thương

7. **Pathology (Giải phẫu bệnh):**
   - Mẫu mô, tế bào
   - Hữu ích cho chẩn đoán ung thư, bệnh lý

**Lưu ý:**
- Hình ảnh chỉ mang tính giáo dục và tham khảo
- Cần có kiến thức y khoa để hiểu đúng
- Không thay thế đánh giá lâm sàng và chẩn đoán chính thức
- Hình ảnh thực tế sẽ được thêm vào trong tương lai
""")

# Footer
render_standard_footer(disclaimer=True)

