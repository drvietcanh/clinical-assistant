import streamlit as st

def render_chronic_hepatitis_b():
    st.header("🦠 Viêm Gan B Mạn (Chronic Hepatitis B)")
    st.caption("Dựa trên hướng dẫn AASLD 2018 (Update 2020)")

    st.subheader("1. Đánh giá giai đoạn bệnh")
    st.info("**Xét nghiệm cần làm:** HBsAg, HBeAg, Anti-HBe, HBV DNA, ALT, Fibrosis scan (FibroScan).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Các giai đoạn bệnh:**")
        st.markdown("1. **Dung nạp miễn dịch (Immune Tolerant):** HBeAg (+), DNA cao (>1 triệu), ALT bình thường, Xơ hóa ít.")
        st.markdown("2. **Hoạt động miễn dịch (Immune Active - HBeAg+):** HBeAg (+), DNA > 20,000, ALT tăng, Có viêm/xơ hóa.")
    with col2:
        st.markdown("3. **Người lành mang trùng (Inactive Carrier):** HBeAg (-), Anti-HBe (+), DNA < 2,000, ALT bình thường.")
        st.markdown("4. **Hoạt động miễn dịch (HBeAg-):** HBeAg (-), DNA > 2,000, ALT tăng/dao động.")

    st.markdown("---")
    st.subheader("2. Chỉ định Điều trị (Antiviral Therapy)")
    
    with st.expander("✅ Ai cần điều trị?", expanded=True):
        st.markdown("""
        **1. Xơ gan (Cirrhosis):** Điều trị TẤT CẢ bệnh nhân xơ gan (bù hoặc mất bù) có HBV DNA dương tính (bất kể mức ALT).
        
        **2. Không xơ gan:**
        - **Chỉ định:** ALT > 2x ULN **VÀ** HBV DNA > 20,000 IU/mL (HBeAg+) hoặc > 2,000 (HBeAg-).
        - **Cân nhắc:** ALT tăng (1-2x ULN) + DNA cao + Xơ hóa trung bình (F2) hoặc gia đình có tiền sử HCC.
        """)
        st.caption("ULN (Giới hạn trên bình thường): Nam 35 U/L, Nữ 25 U/L (AASLD).")

    st.markdown("---")
    st.subheader("3. Thuốc Điều trị (First-line)")
    st.success("**Thuốc ức chế men sao chép ngược Nucleos(t)ide (NAs):**")
    
    st.markdown("""
    | Thuốc | Liều dùng | Ưu điểm | Lưu ý |
    | :--- | :--- | :--- | :--- |
    | **Entecavir (ETV)** | 0.5 mg/ngày (1.0 mg nếu kháng Lamivudine) | Potency cao, hàng rào kháng thuốc cao | Tránh dùng nếu đã kháng Lamivudine. Chỉnh liều suy thận. |
    | **Tenofovir (TDF)** | 300 mg/ngày | Hiệu quả cao, rẻ tiền | Theo dõi thận và xương (nguy cơ loãng xương, suy thận). |
    | **Tenofovir (TAF)** | 25 mg/ngày | An toàn hơn cho thận và xương | Ưu tiên cho người >60t, loãng xương, suy thận. |
    """)
    st.warning("**Interferon (Peg-IFN):** Ít dùng do tác dụng phụ nhiều, chỉ định chọn lọc.")

    st.markdown("---")
    st.subheader("4. Tầm soát Ung thư Gan (HCC)")
    st.markdown("- **Phương tiện:** Siêu âm bụng + AFP mỗi 6 tháng.")
    st.markdown("- **Đối tượng:** Xơ gan, Tiền sử gia đình HCC, Nam >40t (Châu Á), Nữ >50t (Châu Á).")
