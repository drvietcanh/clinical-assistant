import streamlit as st

def render_paracetamol_poisoning():
    st.header("☠️ Ngộ độc Paracetamol (Acetaminophen)")
    st.caption("Dựa trên Rumack-Matthew Nomogram & Hướng dẫn Chống độc")

    st.warning("⚠️ Paracetamol là nguyên nhân hàng đầu gây suy gan cấp do thuốc.")

    tab1, tab2, tab3 = st.tabs(["1. Đánh giá & Nguy cơ", "2. Rumack-Matthew Nomogram", "3. Điều trị (NAC)"])

    with tab1:
        st.subheader("Đánh giá ban đầu")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**1. Bệnh sử:**")
            st.markdown("- Thời gian uống?")
            st.markdown("- Số lượng? (Dạng bào chế?)")
            st.markdown("- Uống một lần hay nhiều lần (Staggered overdose)?")
            st.markdown("- Các thuốc uống kèm?")
        
        with col2:
            st.markdown("**2. Liều độc:**")
            st.markdown("- **Người lớn:** > 150 mg/kg hoặc > 7.5g (tùy cái nào thấp hơn).")
            st.markdown("- **Trẻ em:** > 150 mg/kg.")
            st.error("**Nguy cơ cao:** Nghiện rượu, suy dinh dưỡng, dùng thuốc gây cảm ứng men gan (CYP2E1).")

        st.info("**Xét nghiệm:** Định lượng nồng độ Paracetamol (quan trọng nhất), Men gan (AST/ALT), Đông máu (INR), Bilirubin, Chức năng thận, Khí máu.")

    with tab2:
        st.subheader("Biểu đồ Rumack-Matthew")
        st.write("Chỉ áp dụng cho **uống một lần duy nhất** (Single acute ingestion) và lấy mẫu máu từ **4-24 giờ** sau uống.")
        
        st.markdown("""
        | Giờ sau uống | Nồng độ (mcg/mL) - Treatment Line |
        | :--- | :--- |
        | 4 giờ | **150** |
        | 8 giờ | **75** |
        | 12 giờ | **37.5** |
        | 16 giờ | **18.8** |
        | 20 giờ | **9.4** |
        | 24 giờ | **4.7** |
        """)
        
        st.warning("Nếu nồng độ nằm **TRÊN** đường điều trị -> **Bắt buộc dùng NAC**.")
        st.markdown("**Lưu ý:** Nếu không định lượng được hoặc uống nhiều lần (Staggered), điều trị ngay nếu uống quá liều độc hoặc có dấu hiệu tổn thương gan.")

    with tab3:
        st.subheader("Điều trị N-Acetylcysteine (NAC)")
        st.success("NAC hiệu quả nhất nếu dùng trong vòng **8 giờ** đầu.")

        protocol_choice = st.radio("Chọn phác đồ:", ["Truyền tĩnh mạch (IV) - Phác đồ 21 giờ", "Uống (Oral) - Phác đồ 72 giờ"])

        if protocol_choice == "Truyền tĩnh mạch (IV) - Phác đồ 21 giờ":
            st.markdown("### Phác đồ IV 3 túi (21 giờ):")
            st.markdown("1.  **Liều tải (1 giờ):** 150 mg/kg pha trong 200ml Glucose 5% truyền trong 60 phút.")
            st.markdown("2.  **Liều duy trì 1 (4 giờ):** 50 mg/kg pha trong 500ml Glucose 5% truyền trong 4 giờ.")
            st.markdown("3.  **Liều duy trì 2 (16 giờ):** 100 mg/kg pha trong 1000ml Glucose 5% truyền trong 16 giờ.")
            st.error("**Phản ứng phản vệ (Anaphylactoid):** Nếu đỏ da/ngứa nhẹ -> Tạm ngưng, kháng histamin, giảm tốc độ truyền. Nếu nặng -> Ngưng, adrenalin.")
        
        else:
            st.markdown("### Phác đồ Uống (72 giờ):")
            st.markdown("1.  **Liều tải:** 140 mg/kg.")
            st.markdown("2.  **Liều duy trì:** 70 mg/kg mỗi 4 giờ x 17 liều.")
            st.markdown("- Có thể pha với nước ngọt/nước trái cây để dễ uống. Nếu nôn trong 1h -> Uống lại.")

        st.info("**Tiêu chuẩn ngưng NAC:** INR < 2.0, ALT/AST bình thường hoặc giảm rõ rệt, bệnh nhân không có triệu chứng não gan.")
