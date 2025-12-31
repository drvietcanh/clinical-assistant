import streamlit as st

def render_ectopic_pregnancy():
    st.header("🤰 Thai Ngoài Tử Cung (Ectopic Pregnancy)")
    st.caption("Dựa trên hướng dẫn ACOG 2018 (Reaffirmed 2020)")

    st.error("🚨 Cấp cứu sản phụ khoa hàng đầu. Vỡ thai ngoài TC gây xuất huyết nội đe dọa tính mạng.")

    st.subheader("Chẩn đoán")
    st.markdown("""
    - **Tam chứng:** Trễ kinh + Đau bụng hạ vị + Ra huyết âm đạo.
    - **Beta-hCG:**
        - Ngưỡng phân định (Discriminatory zone): 1500-2000 mIU/mL (với siêu âm đầu dò âm đạo - TVS).
        - Nếu hCG > 2000 mà KHÔNG thấy túi thai trong TC -> Nghi ngờ cao Thai ngoài TC.
    - **Siêu âm:** Khối cạnh tử cung (Adnexal mass), dịch cùng đồ (Fluid in cul-de-sac).
    """)

    st.markdown("---")
    st.subheader("Lựa chọn Điều trị")
    
    treatment_option = st.radio("Tình trạng bệnh nhân:", ["Huyết động ổn định", "Huyết động KHÔNG ổn định / Vỡ"])

    if treatment_option == "Huyết động KHÔNG ổn định / Vỡ":
        st.error("**PHẪU THUẬT KHẨN CẤP (Laparoscopy/Laparotomy)**")
        st.markdown("- Hồi sức chống sốc, lập đường truyền, dự trù máu.")
        st.markdown("- Phẫu thuật cắt vòi trứng (Salpingectomy) thường được ưu tiên khi đã vỡ.")
    else:
        st.success("**Cân nhắc Điều trị Nội khoa (Methotrexate - MTX)**")
        st.markdown("**Chỉ định Methotrexate:**")
        st.markdown("- Huyết động ổn định.")
        st.markdown("- Khối thai chưa vỡ.")
        st.markdown("- Kích thước khối thai < 4 cm.")
        st.markdown("- Beta-hCG < 5000 mIU/mL (lý tưởng).")
        st.markdown("- Không có tim thai hoạt động.")
        st.markdown("- Bệnh nhân tuân thủ theo dõi.")

        with st.expander("Phác đồ Methotrexate (Đơn liều)"):
            st.markdown("""
            1.  **Ngày 1:** Tiêm bắp (IM) Methotrexate 50 mg/m² diện tích da. Đo hCG nền.
            2.  **Ngày 4:** Đo lại hCG. (Có thể tăng nhẹ so với ngày 1).
            3.  **Ngày 7:** Đo lại hCG.
                - Nếu giảm > 15% so với Ngày 4 -> Theo dõi mỗi tuần cho đến khi âm tính.
                - Nếu giảm < 15% -> Tiêm liều MTX thứ 2.
            4.  **Lưu ý:** Kiêng rượu, acid folic, giao hợp hợp trong thời gian điều trị. Tránh nắng.
            """)
        
        st.markdown("**Chống chỉ định MTX:** Đang cho con bú, suy gan/thận, loét dạ dày, suy giảm miễn dịch, huyết động không ổn định.")
