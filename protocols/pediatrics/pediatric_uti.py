import streamlit as st

def render_pediatric_uti():
    st.header("👶 Nhiễm Trùng Tiểu Trẻ em (Pediatric UTI)")
    st.caption("Dựa trên hướng dẫn AAP 2011 (Reaffirmed 2016/2021)")

    st.warning("⚠️ Cần chẩn đoán và điều trị sớm để ngăn ngừa sẹo thận (Renal Scarring).")

    st.subheader("1. Chẩn đoán")
    st.markdown("""
    - **Nghi ngờ:** Trẻ < 2 tuổi sốt không rõ nguyên nhân.
    - **Tiêu chuẩn vàng:**
        1. **Tổng phân tích nước tiểu (Urinalysis):** Bạch cầu niệu (Pyuria) và/hoặc Nitrite dương tính.
        2. **Cấy nước tiểu (Urine Culture):** > 50,000 CFU/mL (mẫu thông tiểu) của một vi khuẩn gây bệnh.
    - **Cách lấy mẫu:**
        - Trẻ chưa kiểm soát tiểu: Thông tiểu (Catheterization) hoặc chọc hút trên xương mu (SPA). *Túi dán nước tiểu (Bag urine) chỉ có giá trị loại trừ (nếu âm tính).*
        - Trẻ đã kiểm soát tiểu: Nước tiểu giữa dòng (Clean catch).
    """)

    st.subheader("2. Điều trị (Febrile UTI)")
    st.info("**Thời gian điều trị:** 7-14 ngày (AAP khuyến cáo). Ngắn ngày (1-3 ngày) không đủ hiệu quả.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Đường uống (Oral) - Ưu tiên:**")
        st.markdown("- **Cephalexin:** 50-100 mg/kg/ngày (chia 3-4 lần).")
        st.markdown("- **Cefixime:** 8 mg/kg/ngày (1 lần hoặc chia 2).")
        st.markdown("- **Amoxicillin/Clavulanate:** 20-40 mg/kg/ngày (chia 3).")
        st.markdown("- *Tránh Nitrofurantoin cho viêm bể thận (không ngấm mô thận).*")
        
    with col2:
        st.markdown("**Đường tĩnh mạch (IV) - Khi trẻ nôn/độc tính:**")
        st.markdown("- **Ceftriaxone:** 50-75 mg/kg/ngày (1 lần).")
        st.markdown("- **Gentamicin:** 7.5 mg/kg/ngày (1 lần).")
        st.markdown("- Chuyển sang uống khi hết sốt 24-48h.")

    st.subheader("3. Chẩn đoán hình ảnh (Imaging)")
    st.markdown("""
    - **Siêu âm thận (RBUS):** Khuyến cáo cho **TẤT CẢ** trường hợp UTI có sốt lần đầu (ở trẻ 2-24 tháng).
    - **Chụp bàng quang ngược dòng (VCUG):**
        - Không khuyến cáo thường quy sau UTI lần đầu.
        - Chỉ định nếu: Siêu âm bất thường (thận ứ nước, sẹo), hoặc UTI tái phát.
    """)
