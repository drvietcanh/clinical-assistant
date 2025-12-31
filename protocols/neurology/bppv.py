import streamlit as st

def render_bppv():
    st.header("🌀 Chóng Mặt Lành Tính Do Tư Thế (BPPV)")
    st.caption("Dựa trên hướng dẫn AAO-HNS 2017")

    st.info("**Đặc điểm:** Chóng mặt kiểu xoay tròn (Vertigo) ngắn (<1 phút), kích khởi bởi thay đổi tư thế đầu (lăn trở, ngước lên, cúi xuống). Không có dấu thần kinh khu trú.")

    st.subheader("1. Chẩn đoán (Nghiệm pháp Dix-Hallpike)")
    with st.expander("👉 Cách thực hiện Dix-Hallpike"):
        st.markdown("""
        1. Bệnh nhân ngồi, xoay đầu 45° sang bên cần khám.
        2. Nằm ngửa nhanh sao cho đầu thõng xuống mép giường 20-30°.
        3. Quan sát mắt trong 30-60 giây.
        4. **Dương tính:** Xuất hiện rung giật nhãn cầu (Nystagmus) xoay vòng + cảm giác chóng mặt. Chiều của nystagmus chỉ điểm ống bán khuyên bị ảnh hưởng.
        """)
        st.warning("*Thận trọng: Bệnh lý cột sống cổ, hẹp động mạch đốt sống.*")

    st.markdown("---")
    st.subheader("2. Điều trị (Thủ thuật tái định vị thạch nhĩ)")
    st.success("Hiệu quả cao > 90% chỉ sau 1-2 lần thực hiện.")
    
    tab1, tab2 = st.tabs(["Epley Maneuver (Ống sau)", "Lempert (Ống ngang)"])
    
    with tab1:
        st.markdown("**Epley Maneuver (Cho ống bán khuyên sau - Phổ biến nhất):**")
        st.markdown("1.  **Dix-Hallpike:** Như bước chẩn đoán (đầu nghiêng 45°, thõng xuống). Giữ 30s.")
        st.markdown("2.  **Xoay đầu 90°:** Sang bên đối diện. (Giữ nguyên đầu thõng). Giữ 30s.")
        st.markdown("3.  **Xoay người 90°:** Bệnh nhân xoay cả người sang nằm nghiêng (cùng chiều xoay đầu), đầu chúi xuống sàn. Giữ 30s.")
        st.markdown("4.  **Ngồi dậy:** Từ tư thế nằm nghiêng.")
    
    with tab2:
        st.markdown("**Lempert (BBQ) Maneuver (Cho ống bán khuyên ngang):**")
        st.markdown("1.  Nằm ngửa, đầu xoay 90° sang bên bệnh.")
        st.markdown("2.  Xoay đầu 90° về giữa (ngửa).")
        st.markdown("3.  Xoay đầu 90° sang bên lành.")
        st.markdown("4.  Xoay tiếp 90° (mũi chúi xuống sàn).")
        st.markdown("5.  Ngồi dậy.")

    st.markdown("---")
    st.subheader("3. Thuốc (Hỗ trợ)")
    st.markdown("- Chỉ dùng ngắn hạn (1-3 ngày) để giảm triệu chứng buồn nôn/chóng mặt nặng.")
    st.markdown("- **Điển hình:** Acetyl-DL-leucine (Tanganil), Betahistine, Antihistamines (Cinnarizine).")
    st.markdown("- *Lưu ý: Thuốc không chữa khỏi BPPV, thủ thuật mới là chính.*")
