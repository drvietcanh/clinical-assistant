import streamlit as st

def render_bronchiolitis():
    st.header("👶 Viêm Tiểu Phế Quản Cấp (Bronchiolitis)")
    st.caption("Dựa trên hướng dẫn AAP 2014 (Review 2023)")

    st.error("⚠️ Chủ yếu là điều trị hỗ trợ. Tránh lạm dụng thuốc không cần thiết.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Chẩn đoán")
        st.markdown("""
        - **Tuổi:** Thường < 2 tuổi (đỉnh điểm 3-6 tháng).
        - **Triệu chứng:** Khởi phát viêm hô hấp trên (sổ mũi, sốt nhẹ) -> ho, thở nhanh, khò khè, rút lõm lồng ngực.
        - **Cận lâm sàng:** Không khuyến cáo X-quang, công thức máu thường quy. Test virus (RSV) chỉ để cách ly/kohort.
        """)
        
    with col2:
        st.subheader("Đánh giá độ nặng")
        st.markdown("""
        - **Nhẹ:** Tỉnh, ăn bú được, SpO2 > 92%, không rút lõm nặng.
        - **Trung bình/Nặng:** Ăn bú kém (<50%), SpO2 < 92%, thở nhanh, rút lõm lồng ngực rõ, phập phồng cánh mũi, rên rỉ.
        - **Nguy cơ cao:** < 12 tuần tuổi, sanh non, bệnh tim/phổi mạn, suy giảm miễn dịch.
        """)

    st.markdown("---")
    st.subheader("Điều trị (AAP Guidelines)")
    
    tab1, tab2 = st.tabs(["✅ Nên làm (Do's)", "❌ Không nên làm (Dont's)"])
    
    with tab1:
        st.success("**Điều trị hỗ trợ là chủ yếu:**")
        st.markdown("1. **Cung cấp Oxy:** Nếu SpO2 < 90% (AAP) hoặc < 92% (tùy lâm sàng). Cai oxy khi SpO2 > 90% ổn định.")
        st.markdown("2. **Hút mũi:** Thông thoáng đường thở, đặc biệt trước khi ăn/ngủ. (Hút bóng hoặc áp lực nhẹ).")
        st.markdown("3. **Dinh dưỡng/Dịch:**")
        st.markdown("   - Nếu bú kém/thở nhanh (60-70 l/p): Chia nhỏ cữ bú hoặc sonde dạ dày.")
        st.markdown("   - Nếu suy hô hấp nặng: Truyền dịch IV.")
        st.markdown("   - Tránh quá tải dịch (SIADH).")
        st.markdown("4. **Nước muối ưu trương (Hypertonic saline 3%):** Cân nhắc khí dung cho trẻ nội trú > 3 ngày (gây ho, long đàm) - *Chứng cứ yếu/tranh cãi*.")

    with tab2:
        st.error("**Các biện pháp KHÔNG khuyến cáo thường quy:**")
        st.markdown("- **Salbutamol/Giãn phế quản (Beta-agonists):** KHÔNG dùng. (Có thể thử 1 lần nếu nghi ngờ hen/dị ứng mạnh, ngưng nếu không đáp ứng).")
        st.markdown("- **Corticosteroids (Uống/Hít/IV):** KHÔNG dùng.")
        st.markdown("- **Adrenaline (Epinephrine) khí dung:** KHÔNG dùng thường quy.")
        st.markdown("- **Kháng sinh:** KHÔNG dùng (trừ khi có bằng chứng bội nhiễm vi khuẩn/viêm tai giữa cấp kèm theo).")
        st.markdown("- **Vật lý trị liệu hô hấp (Vỗ rung):** KHÔNG hiệu quả.")

    st.info("**Tiêu chuẩn xuất viện:** SpO2 ổn định khí trời (>90-92%), ăn bú đủ nhu cầu, người nhà biết cách chăm sóc/theo dõi.")
