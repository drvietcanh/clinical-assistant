import streamlit as st

def render_preterm_labor():
    st.header("🤰 Dọa Sanh Non & Sanh Non (Preterm Labor)")
    st.caption("Dựa trên hướng dẫn ACOG 2019")

    st.info("**Định nghĩa:** Cơn gò tử cung đều đặn gây xóa mở cổ tử cung tử 20W - 37W.")

    st.subheader("1. Đánh giá ban đầu")
    st.markdown("- Đo chiều dài kênh cổ tử cung (CL) qua siêu âm đầu dò.")
    st.markdown("- Xét nghiệm Fetal Fibronectin (fFN) nếu CL 20-30mm.")
    st.markdown("- **CL < 20mm** hoặc **CL 20-30mm + fFN dương tính** -> Nguy cơ sanh non cao.")

    st.markdown("---")
    st.subheader("2. Xử trí (Tuổi thai < 34 tuần)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("**A. Corticosteroids (Trưởng thành phổi)**")
        st.markdown("- **Betamethasone:** 12 mg IM, 2 liều cách nhau 24h.")
        st.markdown("- Hoặc **Dexamethasone:** 6 mg IM, 4 liều cách nhau 12h.")
        st.markdown("- Giảm suy hô hấp (RDS), xuất huyết não, viêm ruột hoại tử.")
        
    with col2:
        st.warning("**B. Bảo vệ thần kinh (Neuroprotection)**")
        st.markdown("- **Magnesium Sulfate (MgSO4):**")
        st.markdown("- Chỉ định: Thai < 32 tuần sắp sanh (trong vòng 24h).")
        st.markdown("- Giảm nguy cơ bại não (Cerebral Palsy).")
        st.markdown("- Liều tải 4g IV, duy trì 1g/h.")

    st.subheader("C. Cắt cơn gò (Tocolysis)")
    st.write("Mục đích: Trì hoãn cuộc sanh 48h để steroid có tác dụng và chuyển tuyến.")
    st.markdown("""
    1.  **Nifedipine (Ức chế canxi):** Lựa chọn đầu tay (ACOG). Liều tải 20-30mg uống, duy trì 10-20mg mỗi 4-6h.
    2.  **Indomethacin (NSAID):** Ưu tiên cho thai < 30-32 tuần. (Tránh dùng > 32 tuần vì đóng sớm ống động mạch).
    3.  **Không dùng:** Beta-mimetics (Terbutaline) kéo dài do tác dụng phụ tim mạch.
    """)

    st.subheader("D. Dự phòng GBS")
    st.markdown("- Kháng sinh dự phòng nhiễm liên cầu nhóm B (GBS) cho đến khi có kết quả cấy âm tính hoặc loại trừ.")
    st.markdown("- Penicillin G hoặc Ampicillin.")
