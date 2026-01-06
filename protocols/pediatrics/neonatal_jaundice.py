import streamlit as st

def render_neonatal_jaundice():
    st.header("👶 Vàng Da Sơ Sinh (Neonatal Jaundice)")
    st.caption("Dựa trên hướng dẫn AAP 2022")

    st.warning("⚠️ Mục tiêu chính: Ngăn ngừa bệnh não cấp do Bilirubin (Kernicterus).")

    st.markdown("### 1. Đánh giá nguy cơ nhiễm độc thần kinh")
    risk_factors = st.multiselect("Yếu tố nguy cơ:", 
        ["Tuổi thai < 38 tuần", "Albumin < 3.0 g/dL", "Tan máu miễn dịch (Isoimmune)", "Thiếu men G6PD", "Nhiễm trùng huyết (Sepsis)", "Lừ đừ/Li bì/Mất ổn định"])
    
    is_high_risk = len(risk_factors) > 0
    if is_high_risk:
        st.error("👉 **Nhóm Nguy Cơ Cao** nhiễm độc thần kinh.")
    else:
        st.success("👉 Nhóm Nguy Cơ Tiêu chuẩn.")

    st.markdown("### 2. Chỉ định Chiếu đèn (Phototherapy)")
    st.info("Tra cứu mức Bilirubin toàn phần (TSB) theo tuổi sau sinh (giờ).")
    
    # Simple table for quick lookup (simplified AAP 2022 thresholds for >= 38 weeks)
    st.markdown("**Ngưỡng chiếu đèn tham khảo (Trẻ >= 38 tuần, không yếu tố nguy cơ):**")
    st.markdown("""
    | Tuổi (Giờ) | TSB (mg/dL) | TSB (µmol/L) |
    | :--- | :--- | :--- |
    | 24h | **> 12** | > 205 |
    | 48h | **> 15** | > 256 |
    | 72h | **> 18** | > 308 |
    | > 96h | **> 21** | > 359 |
    """)
    st.caption("Lưu ý: Nếu có yếu tố nguy cơ hoặc sanh non, ngưỡng chiếu đèn sẽ thấp hơn 2-3 mg/dL.")
    
    with st.expander("📝 Nguyên tắc chiếu đèn"):
        st.markdown("""
        - **Ánh sáng xanh (Blue light):** Bước sóng 460-490 nm.
        - **Tích cực (Intensive):** Cường độ > 30 µW/cm²/nm, diện tích da tối đa.
        - **Bảo vệ mắt:** Che chắn kỹ mắt trẻ.
        - **Bù dịch:** Tăng nhu cầu dịch 10-20% (ưu tiên bú mẹ/bú bình thường xuyên).
        - **Ngưỡng ngưng:** Khi TSB giảm ít nhất 2-3 mg/dL dưới ngưỡng bắt đầu.
        """)

    st.markdown("### 3. Chỉ định Thay máu (Exchange Transfusion)")
    st.error("🚨 Chỉ định khi có dấu hiệu bệnh não cấp HOẶC TSB vượt ngưỡng thay máu.")
    st.markdown("""
    - **Dấu hiệu thần kinh:** Tăng trương lực cơ, khóc thét, ưỡn người (Opisthotonus). -> **THAY MÁU NGAY**.
    - **Ngưỡng tham khảo (>= 38 tuần):** Thường cao hơn ngưỡng chiếu đèn khoảng 10 mg/dL (VD: >25-30 mg/dL).
    - **Trong khi chờ thay máu:** Chiếu đèn tích cực, truyền dịch, IVIG (nếu tan máu miễn dịch: 0.5-1 g/kg).
    """)

    st.info("**Theo dõi sau xuất viện:** Khám lại sau 24-48h nếu xuất viện sớm (<72h).")
