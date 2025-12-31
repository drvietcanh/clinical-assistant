import streamlit as st

def render_febrile_seizures():
    st.header("👶 Co Giật Do Sốt (Febrile Seizures)")
    st.caption("Dựa trên hướng dẫn AAP 2011 (Reaffirmed 2019)")

    st.info("**Định nghĩa:** Co giật kèm sốt (>38°C) ở trẻ 6 tháng - 5 tuổi, không có nhiễm trùng hệ thần kinh trung ương (CNS) hay rối loạn chuyển hóa.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Phân loại")
        st.markdown("""
        **1. Đơn giản (Simple):**
        - Co giật toàn thể (Generalized).
        - Thời gian < 15 phút.
        - Không tái phát trong vòng 24h.
        
        **2. Phức tạp (Complex):**
        - Khu trú (Focal).
        - Thời gian > 15 phút.
        - Tái phát trong vòng 24h.
        """)
        
    with col2:
        st.subheader("Đánh giá nguy cơ")
        st.warning("""
        **Dấu hiệu cần Chọc Dò Tủy Sống (Lumbar Puncture):**
        - Dấu màng não (Cổ cứng, Kernig, Brudzinski).
        - Thóp phồng.
        - Rối loạn tri giác kéo dài sau cơn (postictal).
        - Trẻ 6-12 tháng chưa tiêm chủng H. influenzae hoặc phế cầu đầy đủ.
        - Đang dùng kháng sinh (che lấp triệu chứng viêm màng não).
        """)

    st.markdown("---")
    st.subheader("Xử trí cấp cứu")
    
    st.markdown("1. **Trong cơn giật:**")
    st.markdown("- Đặt trẻ nằm nghiêng trái, thông thoáng đường thở. Không nhét gì vào miệng.")
    st.markdown("- Nếu > 5 phút: Cắt cơn bằng **Diazepam** (0.5 mg/kg đường hậu môn) hoặc **Midazolam** (0.2 mg/kg tiêm bắp/xịt mũi).")
    
    st.markdown("2. **Sau cơn giật (Hồi phục):**")
    st.markdown("- Hạ sốt (Paracetamol 10-15 mg/kg hoặc Ibuprofen 10 mg/kg). *Lưu ý: Hạ sốt không ngăn ngừa tái phát cơn giật.*")
    st.markdown("- Tìm nguyên nhân sốt (Viêm họng, viêm tai giữa, nhiễm siêu vi...).")

    st.markdown("---")
    st.subheader("Cận lâm sàng & Nhập viện")
    
    tab1, tab2 = st.tabs(["Co giật đơn giản", "Co giật phức tạp"])
    
    with tab1:
        st.success("**Co giật đơn giản:**")
        st.markdown("- **EEG:** Không khuyến cáo.")
        st.markdown("- **CT/MRI:** Không khuyến cáo.")
        st.markdown("- **Xét nghiệm máu:** Chỉ làm khi cần tìm nguyên nhân sốt.")
        st.markdown("- **Nhập viện:** Không cần thiết nếu trẻ tỉnh táo, hồng hào, nguồn gốc sốt rõ ràng.")
    
    with tab2:
        st.warning("**Co giật phức tạp:**")
        st.markdown("- Cân nhắc làm xét nghiệm, EEG, hoặc CT/MRI (nếu nghi ngờ tổn thương cấu trúc).")
        st.markdown("- Thường cần nhập viện theo dõi.")

    st.info("**Tư vấn:** Lành tính, không ảnh hưởng trí tuệ, nguy cơ động kinh sau này thấp (gần như trẻ bình thường).")
