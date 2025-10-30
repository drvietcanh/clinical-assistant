"""PASI - Psoriasis Area Severity Index"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #EC4899;'>🩹 PASI Score</h2><p style='text-align: center;'><em>Mức độ nặng vẩy nến</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ PASI"): st.markdown("**PASI** đánh giá mức độ vẩy nến theo diện tích và mức độ. **Điểm:** 0-72")
    st.markdown("---"); st.info("Đánh giá 4 vùng: Đầu, Thân, Tay, Chân"); head_area = st.slider("Đầu - % diện tích", 0, 6, 0); head_erythema = st.slider("Đầu - Đỏ", 0, 4, 0); head_thick = st.slider("Đầu - Dày", 0, 4, 0); head_scale = st.slider("Đầu - Vảy", 0, 4, 0); trunk_area = st.slider("Thân - % diện tích", 0, 6, 0); trunk_e = st.slider("Thân - Đỏ", 0, 4, 0); trunk_t = st.slider("Thân - Dày", 0, 4, 0); trunk_s = st.slider("Thân - Vảy", 0, 4, 0); upper_area = st.slider("Tay - % diện tích", 0, 6, 0); upper_e = st.slider("Tay - Đỏ", 0, 4, 0); upper_t = st.slider("Tay - Dày", 0, 4, 0); upper_s = st.slider("Tay - Vảy", 0, 4, 0); lower_area = st.slider("Chân - % diện tích", 0, 6, 0); lower_e = st.slider("Chân - Đỏ", 0, 4, 0); lower_t = st.slider("Chân - Dày", 0, 4, 0); lower_s = st.slider("Chân - Vảy", 0, 4, 0); head_pasi = 0.1 * head_area * (head_erythema + head_thick + head_scale); trunk_pasi = 0.3 * trunk_area * (trunk_e + trunk_t + trunk_s); upper_pasi = 0.2 * upper_area * (upper_e + upper_t + upper_s); lower_pasi = 0.4 * lower_area * (lower_e + lower_t + lower_s); total = head_pasi + trunk_pasi + upper_pasi + lower_pasi
    if st.button("🔬 Tính PASI", type="primary", use_container_width=True):
        if total < 10: severity = "Nhẹ"; color = "#28a745"
        elif total < 20: severity = "Trung bình"; color = "#fd7e14"
        else: severity = "Nặng"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>PASI: {total:.1f}/72</h2><p style='text-align: center; margin-top: 10px;'>{severity}</p></div>", unsafe_allow_html=True)
if __name__ == "__main__": render()

