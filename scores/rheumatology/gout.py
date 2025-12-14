"""ACR/EULAR Gout Classification Criteria"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 ACR/EULAR Gout Classification</h2><p style='text-align: center;'><em>Tiêu chuẩn chẩn đoán Gout</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ Gout Classification"): st.markdown("**ACR/EULAR 2015** chẩn đoán gout. **Chuẩn vàng:** Thấy tinh thể urat trong dịch khớp. Nếu không có → Dùng điểm số ≥8 để chẩn đoán.")
    st.markdown("---"); crystal = st.radio("Có tinh thể urat trong dịch khớp/tophi?", ["Có", "Không", "Không làm"]); 
    if crystal == "Có": st.success("✅ **Chẩn đoán xác định GOUT**\n\nThấy tinh thể urat → Chuẩn vàng chẩn đoán"); st.info("**Điều trị:** NSAID/Colchicine (cấp) + Allopurinol/Febuxostat (dự phòng)")
    else:
        st.warning("Sử dụng tiêu chuẩn lâm sàng (cần ≥8 điểm):")
        score = 0; pattern = st.radio("Đặc điểm cơn", [0, 1, 2, 3], format_func=lambda x: ["0đ: Không", "1đ: Viêm cổ chân/bàn chân", "2đ: Viêm khớp gối ngón chân cái", "3đ: Đỏ cổ chân/gối ngón chân"][x]); score += pattern
        location = st.checkbox("+1đ: Từng viêm khớp gối ngón chân cái"); score += 1 if location else 0
        time_course = st.radio("Thời gian triệu chứng", [0, 1, 2], format_func=lambda x: ["0đ: Không", "1đ: Bùng phát trong 1 ngày", "2đ: Thuyên giảm trong 14 ngày"][x]); score += time_course
        tophi = st.checkbox("+4đ: Có tophi (hạt gout)"); score += 4 if tophi else 0
        uric_acid = st.radio("Acid uric máu", [0, 2, 3, 4], format_func=lambda x: ["0đ: < 4 mg/dL", "2đ: 4-6", "3đ: 6-8", "4đ: 8-10 hoặc >10"][x]); score += uric_acid
        imaging = st.checkbox("+4đ: X-quang thấy tổn thương gout"); score += 4 if imaging else 0
        
        if st.button("🔬 Đánh giá Gout", type="primary", use_container_width=True):
            if score >= 8: st.error(f"🚨 **{score} điểm - Chẩn đoán GOUT (theo tiêu chuẩn lâm sàng)**"); st.info("**Điều trị cấp:** Colchicine/NSAID/Corticosteroid\n\n**Dự phòng:** Allopurinol/Febuxostat khi acid uric > 6 mg/dL")
            else: st.success(f"✅ **{score} điểm - Chưa đủ tiêu chuẩn Gout lâm sàng**\n\nCân nhắc chẩn đoán khác hoặc chọc dịch khớp tìm tinh thể")
if __name__ == "__main__": render()

