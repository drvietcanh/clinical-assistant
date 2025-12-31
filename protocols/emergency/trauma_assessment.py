import streamlit as st

def render_trauma_assessment():
    st.header("🚑 Đánh giá Chấn thương (ATLS 10th Ed)")
    
    st.info("**Nguyên tắc vàng:** Điều trị ngay các đe dọa tính mạng khi phát hiện. Không chờ chẩn đoán xác định.")

    tab1, tab2, tab3 = st.tabs(["1. Khảo sát ban đầu (Primary)", "2. Khảo sát thứ cấp (Secondary)", "3. Glasgow Coma Scale"])

    with tab1:
        st.subheader("ABCDE - Khảo sát ban đầu & Hồi sức")
        
        col1, col2 = st.columns(2)
        with col1:
            st.error("🅰️ **A - Airway (Đường thở) + Cột sống cổ**")
            st.markdown("""
            - **Đánh giá:** Tắc nghẽn? Dị vật? Phù nề? Gãy xương mặt?
            - **Xử trí:**
                - Hút đờm dãi, lấy dị vật.
                - Nâng cằm (Chin lift), đẩy hàm (Jaw thrust).
                - Canuyn miệng/mũi hầu.
                - **Đặt nội khí quản** nếu: GCS < 8, suy hô hấp, nguy cơ tắc nghẽn.
                - **Mở khí quản** nếu không đặt được NKQ.
            - **Cố định:** Luôn giữ nẹp cổ cứng (Collar).
            """)

            st.warning("🅱️ **B - Breathing (Hô hấp)**")
            st.markdown("""
            - **Đánh giá:** Tần số thở, SpO2, rì rào phế nang, lồng ngực di động?
            - **Xử trí ngay đe dọa tính mạng:**
                - **Tràn khí màng phổi áp lực:** Chọc kim giải áp (khoang liên sườn 2 đường trung đòn hoặc KLS 5 đường nách giữa) -> Dẫn lưu.
                - **Tràn khí màng phổi hở:** Băng kín 3 cạnh -> Dẫn lưu.
                - **Mảng sườn di động:** Cố định, giảm đau, hỗ trợ hô hấp.
            - **Hỗ trợ:** Oxy 100% qua mask túi.
            """)

        with col2:
            st.error("©️ **C - Circulation (Tuần hoàn) + Cầm máu**")
            st.markdown("""
            - **Đánh giá:** Mạch, huyết áp, màu sắc da, dấu hiệu sốc.
            - **Xử trí:**
                - **Cầm máu ngoài:** Băng ép trực tiếp (Không kẹp mạch mù).
                - **Đường truyền:** 2 đường truyền lớn (14G-16G).
                - **Dịch:** Ringer Lactate hoặc NaCl 0.9% (ấm).
                - **Truyền máu:** Nếu không đáp ứng với dịch hoặc mất máu nhiều (Quy trình truyền máu khối lượng lớn - MTP).
                - **Sốc chấn thương:** Tìm nguyên nhân (Chảy máu trong: Ngực, Bụng, Xương chậu, Xương đùi).
            - **FAST E-FAST:** Siêu âm tại giường tìm dịch.
            """)
            
            st.info("🇩 **D - Disability (Thần kinh)**")
            st.markdown("""
            - **GCS:** Đánh giá nhanh (Mắt, Lời nói, Vận động).
            - **Đồng tử:** Kích thước, phản xạ ánh sáng (giãn một bên -> tụ máu nội sọ?).
            - **Dấu thần kinh khu trú:** Yếu liệt?
            """)

            st.success("🇪 **E - Exposure (Bộc lộ) + Môi trường**")
            st.markdown("""
            - Cắt bỏ quần áo để khám toàn diện.
            - **Ủ ấm:** Tránh hạ thân nhiệt (Hạ thân nhiệt -> Rối loạn đông máu).
            """)

    with tab2:
        st.subheader("Khảo sát thứ cấp (Secondary Survey)")
        st.write("Chỉ thực hiện khi Khảo sát ban đầu đã ổn định.")
        
        st.markdown("""
        **Bệnh sử AMPLE:**
        - **A**llergies (Dị ứng)
        - **M**edications (Thuốc đang dùng)
        - **P**ast illnesses (Bệnh nền/Thai kỳ)
        - **L**ast meal (Bữa ăn cuối)
        - **E**vents (Hoàn cảnh xảy ra tai nạn)
        """)

        with st.expander("Khám toàn diện từ đầu đến chân"):
            st.markdown("""
            1.  **Đầu mặt:** Vết thương da đầu, gãy xương mặt, mắt, tai (dấu Battle), mũi.
            2.  **Cổ:** Khí quản lệch? Tĩnh mạch cổ nổi? Tràn khí dưới da? Đau cột sống cổ?
            3.  **Ngực:** Sờ tìm điểm đau, gãy xương sườn, nghe phổi, tim.
            4.  **Bụng:** Nhìn, nghe, gõ, sờ. Dấu hiệu viêm phúc mạc?
            5.  **Chậu:** Ấn đau? Mất vững? (Chỉ khám 1 lần). Kiểm tra tầng sinh môn/trực tràng/âm đạo.
            6.  **Tứ chi:** Gãy xương? Mạch ngoại vi? Chèn ép khoang?
            7.  **Thần kinh:** Khám kỹ vận động, cảm giác.
            """)
        
        st.markdown("**Cận lâm sàng cần làm:**")
        st.markdown("- **X-quang:** Ngực thẳng, Chậu thẳng, Cột sống cổ.")
        st.markdown("- **CT Scan:** Sọ não, Cột sống cổ, Ngực, Bụng chậu (nếu ổn định).")
        st.markdown("- **Xét nghiệm:** Công thức máu, Đông máu, Nhóm máu, Lactate, Khí máu.")

    with tab3:
        st.subheader("Thang điểm Glasgow Coma Scale (GCS)")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.write("**Mắt (Eye - E)**")
            st.markdown("""
            4. Mở tự nhiên
            3. Mở khi gọi
            2. Mở khi cấu đau
            1. Không mở
            """)
        with c2:
            st.write("**Lời nói (Verbal - V)**")
            st.markdown("""
            5. Trả lời đúng, định hướng tốt
            4. Trả lời lầm lẫn
            3. Trả lời không phù hợp
            2. Ú ớ, không thành tiếng
            1. Không trả lời
            """)
        with c3:
            st.write("**Vận động (Motor - M)**")
            st.markdown("""
            6. Tuân lệnh
            5. Định khu được đau
            4. Co tay khi cấu (Quá mức)
            3. Co cứng mất vỏ (Gập tay)
            2. Duỗi cứng mất não
            1. Không đáp ứng
            """)
        
        st.markdown("---")
        st.info("**Phân loại TBI:** Nhẹ (13-15), Trung bình (9-12), Nặng (3-8). **GCS ≤ 8: Đặt nội khí quản.**")
