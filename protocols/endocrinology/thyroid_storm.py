import streamlit as st

def render_thyroid_storm():
    st.header("🦋 Cơn Bão Giáp (Thyroid Storm)")
    st.caption("Dựa trên hướng dẫn ATA 2016 & Burch-Wartofsky Point Scale")

    st.error("🚨 CẤP CỨU NỘI KHOA - Tử vong 10-30%. Cần điều trị ngay khi nghi ngờ, không chờ kết quả xét nghiệm T3/T4.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Chẩn đoán (Burch-Wartofsky)")
        st.info("Tổng điểm >= 45: Gợi ý rất cao Bão giáp.")
        st.markdown("- **Sốt:** 37.2 - >40°C (5-30 điểm).")
        st.markdown("- **Tim mạch:** Nhịp nhanh (90 -> >140), Rung nhĩ (10 điểm), Suy tim (3-15 điểm).")
        st.markdown("- **Thần kinh trung ương:** Kích động (10) -> Mê sảng/Loạn thần (20) -> Hôn mê (30).")
        st.markdown("- **Tiêu hóa:** Tiêu chảy, buồn nôn, vàng da (10-20 điểm).")
    
    with col2:
        st.subheader("Yếu tố thúc đẩy")
        st.markdown("""
        - Ngưng thuốc kháng giáp đột ngột.
        - Nhiễm trùng.
        - Phẫu thuật (tuyến giáp hoặc khác).
        - Chấn thương.
        - Iốt (thuốc cản quang, amiodarone).
        - Thai kỳ/Sanh nở.
        """)

    st.markdown("---")
    st.subheader("Điều trị (Theo trình tự 5 chữ P)")
    
    st.markdown("**1. Ức chế tổng hợp Hormone (Propythiouracil/Methimazole):**")
    st.markdown("- **PTU (Propylthiouracil):** Ưu tiên trong bão giáp (ức chế T4 -> T3 ngoại biên). Liều tải 500-1000mg uống/sonde, duy trì 250mg mỗi 4h.")
    st.markdown("- **Methimazole:** 60-80mg/ngày. Dùng nếu không có PTU.")
    st.caption("*Lưu ý: Phải cho thuốc kháng giáp 1 giờ TRƯỚC khi cho Iốt.*")
    
    st.markdown("**2. Ức chế phóng thích Hormone (Potassium Iodide):**")
    st.markdown("- **Dung dịch SSKI:** 5 giọt uống mỗi 6h.")
    st.markdown("- **Dung dịch Lugol:** 10 giọt uống mỗi 8h.")
    st.markdown("- Mục đích: Hiệu ứng Wolff-Chaikoff.")

    st.markdown("**3. Ức chế tác dụng ngoại biên (Propranolol - Beta blocker):**")
    st.markdown("- **Propranolol:** 60-80mg uống mỗi 4-6h Hoặc 1mg IV chậm mỗi 10p.")
    st.markdown("- Kiểm soát nhịp tim, giảm chuyển T4 -> T3. (Thận trọng nếu suy tim nặng do bơm).")
    
    st.markdown("**4. Ức chế chuyển đổi T4 -> T3 (Hydrocortisone/Dexamethasone):**")
    st.markdown("- **Hydrocortisone:** 300mg IV, sau đó 100mg mỗi 8h.")
    st.markdown("- Cũng giúp điều trị suy thượng thận tương đối.")

    st.markdown("**5. Loại bỏ Hormone/Nguyên nhân (Plasmapheresis/Treat Precipitant):**")
    st.markdown("- Điều trị nhiễm trùng, hạ sốt (Paracetamol - tránh Aspirin vì tranh chấp gắn kết protein), bù dịch tích cực.")
