"""
Fungal Skin Infections (Nhiễm nấm da) Protocol
Common in tropical climates like Vietnam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Fungal Skin Infections (Nhiễm nấm da) Protocol"""
    st.subheader("🩹 Nhiễm nấm da (Fungal Skin Infections)")
    st.caption("Common in tropical climates - Very common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Nhiễm nấm da do dermatophytes, yeasts, hoặc molds
    - Rất phổ biến ở Việt Nam do khí hậu nóng ẩm
    
    **Phân loại:**
    1. **Dermatophytosis (Nấm da):** Tinea corporis, Tinea cruris, Tinea pedis, Tinea capitis
    2. **Candidiasis (Nhiễm nấm men):** Nhiễm Candida
    3. **Pityriasis versicolor (Lang ben):** Do Malassezia
    
    **Yếu tố nguy cơ:**
    - Khí hậu nóng ẩm
    - Vệ sinh kém
    - Dùng chung đồ dùng
    - Suy giảm miễn dịch
    - Đái tháo đường
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: TYPES ==========
    st.markdown("### 📋 Phân loại")
    
    infection_type = st.radio(
        "**Loại nhiễm nấm:**",
        ["Nấm da (Dermatophytosis)", "Nấm men (Candidiasis)", "Lang ben (Pityriasis versicolor)"],
        key="fungal_type"
    )
    
    st.markdown("---")
    
    # ========== SECTION 2: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 🔍 Tiêu chuẩn chẩn đoán")
    
    if infection_type == "Nấm da (Dermatophytosis)":
        render_dermatophytosis()
    elif infection_type == "Nấm men (Candidiasis)":
        render_candidiasis()
    else:
        render_pityriasis_versicolor()
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **Nguyên tắc:**
    1. Xác định loại nấm
    2. Điều trị đủ thời gian
    3. Phòng ngừa tái phát
    
    **Điều trị tại chỗ (Cho tổn thương khu trú):**
    - **Clotrimazole 1%:** Bôi 2 lần/ngày, 2-4 tuần
    - **Miconazole 2%:** Bôi 2 lần/ngày, 2-4 tuần
    - **Terbinafine 1%:** Bôi 1-2 lần/ngày, 1-2 tuần
    - **Ketoconazole 2%:** Bôi 1-2 lần/ngày, 2-4 tuần
    
    **Điều trị toàn thân (Cho tổn thương lan rộng, tái phát):**
    - **Terbinafine:** 250 mg/ngày, 2-4 tuần
    - **Itraconazole:** 200 mg/ngày, 1-2 tuần
    - **Fluconazole:** 150-300 mg/tuần, 2-4 tuần
    - **Griseofulvin:** 500-1000 mg/ngày, 4-8 tuần (cho Tinea capitis)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: SPECIFIC TREATMENT ==========
    st.markdown("### 🎯 Điều trị theo loại")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Tinea corporis (Hắc lào):**
        - Tại chỗ: 2-4 tuần
        - Toàn thân: Nếu lan rộng, không đáp ứng
        
        **Tinea cruris (Nấm bẹn):**
        - Tại chỗ: 2-4 tuần
        - Giữ khô ráo, mặc quần rộng
        
        **Tinea pedis (Nấm chân):**
        - Tại chỗ: 4-6 tuần
        - Toàn thân: Nếu nặng, tái phát
        """)
    
    with col2:
        st.markdown("""
        **Tinea capitis (Nấm da đầu):**
        - Bắt buộc điều trị toàn thân
        - Griseofulvin hoặc Terbinafine
        - Kết hợp dầu gội chống nấm
        
        **Candidiasis:**
        - Tại chỗ: Nystatin, Clotrimazole
        - Toàn thân: Fluconazole (nếu cần)
        
        **Lang ben:**
        - Dầu gội Ketoconazole 2%
        - Hoặc Fluconazole 300 mg/tuần, 2 tuần
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: PREVENTION ==========
    st.markdown("### 🏠 Phòng ngừa")
    
    st.markdown("""
    **Biện pháp phòng ngừa:**
    
    1. **Vệ sinh:**
       - Tắm rửa sạch sẽ, lau khô
       - Thay quần áo thường xuyên
       - Giữ chân khô ráo
    
    2. **Tránh:**
       - Dùng chung khăn, quần áo
       - Đi chân đất ở nơi công cộng
       - Mặc quần áo ẩm ướt
    
    3. **Môi trường:**
       - Giữ môi trường khô ráo, thoáng mát
       - Phơi quần áo dưới nắng
       - Vệ sinh giày dép
    
    4. **Điều trị:**
       - Điều trị đủ thời gian
       - Điều trị đồng thời các vị trí nhiễm
       - Điều trị người trong gia đình nếu cần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Theo dõi điều trị:**
    - **2 tuần:** Đánh giá đáp ứng
    - **4 tuần:** Đánh giá hiệu quả
    - **Sau điều trị:** Theo dõi tái phát
    
    **Khi dùng thuốc toàn thân:**
    - **Terbinafine:** Theo dõi chức năng gan (nếu dùng >4 tuần)
    - **Itraconazole:** Theo dõi chức năng gan, tương tác thuốc
    - **Fluconazole:** Thường an toàn, ít tác dụng phụ
    
    **Dấu hiệu cần khám lại:**
    - Không đáp ứng sau 2-4 tuần
    - Tái phát
    - Tác dụng phụ thuốc
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Biến chứng:**
    - **Nhiễm trùng thứ phát:** Do gãi, tổn thương da
    - **Mạn tính:** Tái phát, khó điều trị
    - **Lan rộng:** Sang các vùng khác, người khác
    
    **Yếu tố làm nặng:**
    - Suy giảm miễn dịch
    - Đái tháo đường
    - Dùng corticosteroid
    - Vệ sinh kém
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    references = get_references("Fungal Skin Infections")
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
        1. **Gupta AK, et al. Treatment of tinea capitis: A systematic review.** Pediatr Dermatol. 2018
        2. **Elewski BE, et al. Terbinafine hydrochloride in the treatment of superficial fungal infections.** Clin Dermatol. 1997
        3. **UpToDate:** Dermatophyte (tinea) infections - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_dermatophytosis():
    """Dermatophytosis diagnosis and treatment"""
    st.markdown("""
    **Tinea corporis (Hắc lào):**
    - Tổn thương hình tròn, có viền rõ
    - Ngứa, đỏ, bong vảy
    - Vị trí: Thân mình, tay chân
    
    **Tinea cruris (Nấm bẹn):**
    - Tổn thương ở bẹn, đùi trong
    - Viền rõ, có thể lan ra mông
    
    **Tinea pedis (Nấm chân):**
    - Kẽ ngón chân: Ẩm ướt, trắng
    - Lòng bàn chân: Khô, bong vảy
    - Mụn nước: Ở lòng bàn chân
    
    **Tinea capitis (Nấm da đầu):**
    - Rụng tóc từng mảng
    - Vảy, mụn mủ
    - Hạch cổ (nếu viêm)
    """)


def render_candidiasis():
    """Candidiasis diagnosis and treatment"""
    st.markdown("""
    **Triệu chứng:**
    - Tổn thương đỏ, ẩm ướt
    - Mụn nước, mụn mủ nhỏ
    - Vị trí: Nếp gấp (nách, bẹn, dưới vú)
    
    **Yếu tố nguy cơ:**
    - Béo phì
    - Đái tháo đường
    - Dùng kháng sinh
    - Suy giảm miễn dịch
    
    **Điều trị:**
    - Tại chỗ: Nystatin, Clotrimazole
    - Toàn thân: Fluconazole (nếu cần)
    - Giữ khô ráo
    """)


def render_pityriasis_versicolor():
    """Pityriasis versicolor diagnosis and treatment"""
    st.markdown("""
    **Triệu chứng:**
    - Đốm trắng hoặc nâu
    - Bong vảy nhẹ
    - Vị trí: Ngực, lưng, cổ
    - Nổi rõ khi ra nắng
    
    **Nguyên nhân:**
    - Malassezia furfur
    - Phát triển trong môi trường nóng ẩm
    
    **Điều trị:**
    - Dầu gội Ketoconazole 2%: 2-4 tuần
    - Hoặc Fluconazole 300 mg/tuần, 2 tuần
    - Tái phát thường xuyên → Điều trị dự phòng
    """)

