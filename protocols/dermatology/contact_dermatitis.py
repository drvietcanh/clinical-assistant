"""
Contact Dermatitis (Viêm da tiếp xúc) Protocol
Inflammatory skin reaction to external agents
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Contact Dermatitis (Viêm da tiếp xúc) Protocol"""
    st.subheader("🩹 Viêm da tiếp xúc (Contact Dermatitis)")
    st.caption("Inflammatory skin reaction to external agents - Common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Phản ứng viêm da do tiếp xúc với chất kích thích hoặc dị nguyên
    - **2 loại chính:**
      1. **Viêm da tiếp xúc kích thích (Irritant):** 80% - Phản ứng không miễn dịch
      2. **Viêm da tiếp xúc dị ứng (Allergic):** 20% - Phản ứng miễn dịch type IV
    
    **Phổ biến ở Việt Nam:**
    - Hóa chất công nghiệp, nông nghiệp
    - Mỹ phẩm, nước hoa
    - Niken, cao su
    - Thực vật (cây thường xuân, xoài)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Chẩn đoán dựa trên:**
        
        1. **Lâm sàng:**
           - Tổn thương da tại vùng tiếp xúc
           - Ngứa, đỏ, phù nề
           - Mụn nước, bong vảy
           - Ranh giới rõ (dị ứng) hoặc không rõ (kích thích)
        
        2. **Tiền sử:**
           - Tiếp xúc với chất nghi ngờ
           - Thời gian: Vài giờ đến vài ngày (dị ứng) hoặc ngay lập tức (kích thích)
        
        3. **Patch test (Test áp da):**
           - Xác định dị nguyên (cho viêm da dị ứng)
           - Đọc kết quả sau 48-72 giờ
        
        **Phân biệt:**
        - **Kích thích:** Ngay lập tức, ranh giới không rõ, đau hơn ngứa
        - **Dị ứng:** Sau vài giờ-ngày, ranh giới rõ, ngứa nhiều
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: COMMON CAUSES ==========
    st.markdown("### 🔍 Nguyên nhân thường gặp")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Viêm da kích thích:**
        - Nước, xà phòng
        - Hóa chất tẩy rửa
        - Dung môi hữu cơ
        - Xi măng, vôi
        - Thực vật có độc
        
        **Dị nguyên thường gặp:**
        - **Niken:** Trang sức, khóa, đồng hồ
        - **Cao su:** Găng tay, giày dép
        - **Mỹ phẩm:** Nước hoa, chất bảo quản
        """)
    
    with col2:
        st.markdown("""
        **Dị nguyên (tiếp):**
        - **Formaldehyde:** Quần áo, keo
        - **Thực vật:** Cây thường xuân, xoài, cây sơn
        - **Thuốc tại chỗ:** Neomycin, Bacitracin
        - **Paraphenylenediamine:** Thuốc nhuộm tóc
        - **Chromate:** Xi măng, da thuộc
        
        **Nghề nghiệp:**
        - Thợ xây, thợ sơn
        - Thợ làm tóc
        - Nhân viên y tế
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **1. Tránh tiếp xúc (QUAN TRỌNG NHẤT):**
    - Xác định và tránh chất gây bệnh
    - Sử dụng găng tay bảo vệ (nếu cần)
    - Thay đổi môi trường làm việc (nếu có thể)
    
    **2. Điều trị tại chỗ:**
    - **Rửa sạch:** Ngay sau tiếp xúc, dùng nước sạch
    - **Corticosteroid tại chỗ:**
      - **Nhẹ-trung bình:** Hydrocortisone 1%, Betamethasone valerate 0.1%
      - **Nặng:** Clobetasol propionate 0.05%
      - Bôi 1-2 lần/ngày, 1-2 tuần
    - **Dưỡng ẩm:** Bôi sau khi tổn thương cải thiện
    
    **3. Điều trị toàn thân:**
    - **Antihistamines:** Giảm ngứa
      - Cetirizine 10 mg/ngày
      - Loratadine 10 mg/ngày
      - Fexofenadine 180 mg/ngày
    - **Corticosteroid đường uống (nếu nặng):**
      - Prednisolone 0.5-1 mg/kg/ngày, 5-7 ngày
      - Giảm liều dần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: ACUTE MANAGEMENT ==========
    st.markdown("### 🚨 Xử trí cấp")
    
    st.warning("""
    **Khi tiếp xúc với chất gây bệnh:**
    
    1. **Rửa ngay:**
       - Dùng nước sạch, nhiều nước
       - Rửa trong 15-20 phút
       - Không chà xát mạnh
    
    2. **Loại bỏ quần áo:**
       - Cởi bỏ quần áo bị dính
       - Giặt sạch hoặc bỏ đi
    
    3. **Điều trị ngay:**
       - Bôi corticosteroid tại chỗ
       - Uống antihistamine nếu ngứa nhiều
       - Chườm lạnh nếu phù nề
    
    4. **Theo dõi:**
       - Nếu tổn thương lan rộng, nặng → Khám ngay
       - Nếu có dấu hiệu nhiễm trùng → Kháng sinh
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: PREVENTION ==========
    st.markdown("### 🏠 Phòng ngừa")
    
    st.markdown("""
    **Biện pháp phòng ngừa:**
    
    1. **Tránh tiếp xúc:**
       - Xác định dị nguyên qua patch test
       - Đọc nhãn sản phẩm
       - Tránh chất đã biết gây dị ứng
    
    2. **Bảo vệ:**
       - Đeo găng tay (chọn loại phù hợp)
       - Mặc quần áo bảo hộ
       - Bôi kem bảo vệ (barrier cream)
    
    3. **Vệ sinh:**
       - Rửa tay sau tiếp xúc
       - Thay quần áo sau làm việc
       - Giữ môi trường sạch sẽ
    
    4. **Giáo dục:**
       - Tư vấn bệnh nhân về dị nguyên
       - Hướng dẫn nhận biết sớm
       - Cung cấp thông tin về sản phẩm thay thế
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: PATCH TESTING ==========
    st.markdown("### 🧪 Patch Testing")
    
    st.info("""
    **Chỉ định:**
    - Viêm da tiếp xúc dị ứng tái phát
    - Không xác định được nguyên nhân
    - Bệnh nhân muốn xác định dị nguyên
    
    **Quy trình:**
    1. Áp các dị nguyên lên da lưng
    2. Để 48 giờ
    3. Đọc kết quả sau 48-72 giờ
    4. Đọc lại sau 7 ngày (nếu cần)
    
    **Bộ test chuẩn:**
    - True Test (24 dị nguyên phổ biến)
    - Hoặc test riêng lẻ theo nghi ngờ
    
    **Lưu ý:**
    - Không dùng corticosteroid trước test
    - Không tắm trong thời gian test
    - Có thể gây kích ứng nhẹ
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.markdown("""
    **Biến chứng:**
    - **Nhiễm trùng:** Do gãi, tổn thương da
    - **Mạn tính:** Da dày, lichen hóa
    - **Ảnh hưởng nghề nghiệp:** Phải đổi nghề
    - **Chất lượng cuộc sống:** Ngứa, mất ngủ
    
    **Dấu hiệu cần khám lại:**
    - Tổn thương lan rộng
    - Nhiễm trùng (mủ, sốt)
    - Không đáp ứng điều trị
    - Tái phát thường xuyên
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    references = get_references("Contact Dermatitis")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **DeKoven JG, et al. North American Contact Dermatitis Group Patch Test Results: 2015-2016.** Dermatitis. 2018
        2. **Fonacier L, et al. Contact dermatitis: a practice parameter-update 2015.** J Allergy Clin Immunol Pract. 2015
        3. **UpToDate:** Contact dermatitis - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

