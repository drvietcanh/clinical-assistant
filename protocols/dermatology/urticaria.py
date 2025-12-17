"""
Urticaria (Mề đay) Protocol
Common allergic skin condition
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Urticaria (Mề đay) Protocol"""
    st.subheader("🩹 Mề đay (Urticaria)")
    st.caption("Common allergic skin condition - Very common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Phản ứng da với sẩn phù, ngứa
    - Ảnh hưởng 15-20% dân số
    - Phổ biến ở Việt Nam
    
    **Phân loại:**
    1. **Cấp tính:** <6 tuần
    2. **Mạn tính:** >6 tuần
    
    **Cơ chế:**
    - Giải phóng histamine từ mast cells
    - Gây giãn mạch, tăng tính thấm
    - Dẫn đến sẩn phù, ngứa
    
    **Nguyên nhân thường gặp:**
    - Dị ứng thức ăn, thuốc
    - Nhiễm trùng
    - Côn trùng đốt
    - Vật lý (nóng, lạnh, áp lực)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        1. **Sẩn phù (Wheals):**
           - Nổi lên, đỏ, ngứa
           - Kích thước: Vài mm đến vài cm
           - Tồn tại: Vài giờ đến 24 giờ
           - Biến mất không để lại dấu vết
        
        2. **Phù mạch (Angioedema):**
           - Phù sâu hơn, ở mô dưới da
           - Vị trí: Môi, mí mắt, lưỡi, họng
           - Có thể nguy hiểm nếu ở đường thở
        
        3. **Ngứa:** Đặc trưng, nặng hơn về đêm
        
        **Phân loại:**
        - **Cấp tính:** <6 tuần, thường có nguyên nhân rõ
        - **Mạn tính:** >6 tuần, thường không tìm thấy nguyên nhân
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: SEVERITY ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá mức độ")
    
    severity = st.radio(
        "**Mức độ:**",
        ["Nhẹ", "Trung bình", "Nặng", "Cấp cứu (Phù mạch đường thở)"],
        key="urticaria_severity"
    )
    
    if severity == "Cấp cứu (Phù mạch đường thở)":
        st.error("""
        **🚨 CẤP CỨU - PHÙ MẠCH ĐƯỜNG THỞ:**
        - Khó thở, khàn tiếng
        - Phù lưỡi, họng
        - Cần xử trí ngay:
          1. Epinephrine 0.3-0.5 mg IM (thigh)
          2. Antihistamine IV
          3. Corticosteroid IV
          4. Đảm bảo đường thở
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **Nguyên tắc:**
    1. Tránh yếu tố kích thích (nếu xác định được)
    2. Điều trị triệu chứng
    3. Điều trị theo bậc thang
    
    **Bậc 1: Antihistamines H1 (Đầu tay):**
    - **Cetirizine:** 10 mg, 1-2 lần/ngày
    - **Loratadine:** 10 mg, 1-2 lần/ngày
    - **Fexofenadine:** 180 mg, 1-2 lần/ngày
    - **Desloratadine:** 5 mg, 1-2 lần/ngày
    - **Lưu ý:** Dùng liều cao hơn nếu cần (đến 4 lần liều thường)
    
    **Bậc 2: Kết hợp H1 + H2:**
    - **H1:** Cetirizine 10 mg, 2 lần/ngày
    - **H2:** Ranitidine 150 mg, 2 lần/ngày
      - Hoặc Cimetidine 400 mg, 2 lần/ngày
    
    **Bậc 3: Thêm Leukotriene antagonist:**
    - **Montelukast:** 10 mg/ngày
    - Kết hợp với H1 antihistamine
    
    **Bậc 4: Corticosteroid (ngắn hạn):**
    - **Prednisolone:** 0.5-1 mg/kg/ngày, 3-7 ngày
    - Chỉ dùng khi nặng, không đáp ứng
    - Giảm liều dần
    
    **Bậc 5: Điều trị đặc biệt:**
    - **Cyclosporine:** 3-5 mg/kg/ngày (mạn tính nặng)
    - **Omalizumab:** 300 mg mỗi 4 tuần (mạn tính)
    - **Methotrexate:** 7.5-15 mg/tuần
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: ACUTE URTICARIA ==========
    st.markdown("### 🚨 Mề đay cấp tính")
    
    st.warning("""
    **Đặc điểm:**
    - <6 tuần
    - Thường có nguyên nhân rõ
    - Đáp ứng tốt với điều trị
    
    **Nguyên nhân thường gặp:**
    - **Thức ăn:** Tôm, cua, sữa, trứng, đậu phộng
    - **Thuốc:** Penicillin, Aspirin, NSAIDs
    - **Nhiễm trùng:** Virus, vi khuẩn
    - **Côn trùng đốt:** Ong, kiến
    - **Vật lý:** Nóng, lạnh, ánh nắng
    
    **Điều trị:**
    - **Antihistamine H1:** Cetirizine 10 mg, 2 lần/ngày, 3-7 ngày
    - **Corticosteroid (nếu nặng):** Prednisolone 0.5 mg/kg/ngày, 3-5 ngày
    - **Tránh nguyên nhân**
    
    **Theo dõi:**
    - Tái khám nếu không đáp ứng
    - Theo dõi phù mạch
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: CHRONIC URTICARIA ==========
    st.markdown("### 🔄 Mề đay mạn tính")
    
    st.markdown("""
    **Đặc điểm:**
    - >6 tuần
    - Thường không tìm thấy nguyên nhân
    - Ảnh hưởng chất lượng cuộc sống
    
    **Phân loại:**
    - **Tự phát:** Không rõ nguyên nhân (80%)
    - **Vật lý:** Nóng, lạnh, áp lực, nước, ánh nắng
    - **Tự miễn:** Có kháng thể kháng IgE receptor
    
    **Điều trị:**
    - **Bậc 1-2:** Antihistamines (liều cao)
    - **Bậc 3:** Thêm Montelukast
    - **Bậc 4:** Corticosteroid ngắn hạn (khi bùng phát)
    - **Bậc 5:** Cyclosporine, Omalizumab
    
    **Theo dõi:**
    - Điều trị lâu dài
    - Đánh giá đáp ứng mỗi 4-8 tuần
    - Điều chỉnh liều theo đáp ứng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: INVESTIGATION ==========
    st.markdown("### 🧪 Xét nghiệm")
    
    st.info("""
    **Mề đay cấp tính:**
    - Thường không cần xét nghiệm
    - Chỉ xét nghiệm nếu nghi ngờ nguyên nhân cụ thể
    
    **Mề đay mạn tính:**
    - **CBC:** Tìm nhiễm trùng, bệnh máu
    - **ESR/CRP:** Dấu hiệu viêm
    - **TSH:** Bệnh tuyến giáp
    - **Autoantibodies:** Nếu nghi tự miễn
    - **Test dị ứng:** Nếu nghi ngờ dị ứng
    
    **Lưu ý:**
    - Không cần xét nghiệm rộng rãi
    - Chỉ xét nghiệm dựa trên lâm sàng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: LIFESTYLE ==========
    st.markdown("### 🏠 Chăm sóc")
    
    st.markdown("""
    **Tránh yếu tố kích thích:**
    - Thức ăn gây dị ứng
    - Thuốc gây dị ứng
    - Nhiệt độ quá nóng/lạnh
    - Áp lực, ma sát
    - Stress
    
    **Chăm sóc da:**
    - Tắm nước ấm (không nóng)
    - Dùng sữa tắm nhẹ
    - Dưỡng ẩm
    - Tránh gãi
    
    **Theo dõi:**
    - Ghi nhật ký triệu chứng
    - Ghi lại thức ăn, thuốc dùng
    - Tìm mối liên quan
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Biến chứng:**
    - **Phù mạch đường thở:** Nguy hiểm, cần cấp cứu
    - **Sốc phản vệ:** Hiếm, nhưng nguy hiểm
    - **Ảnh hưởng chất lượng cuộc sống:**
      - Mất ngủ do ngứa
      - Lo âu, trầm cảm
      - Ảnh hưởng công việc, học tập
    
    **Dấu hiệu cần cấp cứu:**
    - Khó thở, khàn tiếng
    - Phù lưỡi, họng
    - Choáng, ngất
    - Phù mạch lan rộng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    references = get_references("Urticaria")
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
        1. **Zuberbier T, et al. The EAACI/GA²LEN/EDF/WAO Guideline for the definition, classification, diagnosis and management of urticaria.** Allergy. 2018
        2. **Bernstein JA, et al. The diagnosis and management of acute and chronic urticaria: 2014 update.** J Allergy Clin Immunol. 2014
        3. **UpToDate:** Urticaria - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

