"""SCORAD - SCORing Atopic Dermatitis"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #EC4899;'>🩹 SCORAD</h2><p style='text-align: center;'><em>Điểm viêm da cơ địa</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SCORAD"): st.markdown("**SCORAD** đánh giá mức độ viêm da cơ địa. **Điểm:** 0-103")
    st.markdown("---"); extent = st.slider("A. % Diện tích bị ảnh hưởng (Rule of 9s)", 0, 100, 10); erythema = st.slider("B1. Đỏ", 0, 3, 0); edema = st.slider("B2. Phù/Sần", 0, 3, 0); oozing = st.slider("B3. Chảy nước/Vảy", 0, 3, 0); excoriation = st.slider("B4. Trầy xước", 0, 3, 0); lichenification = st.slider("B5. Dày da", 0, 3, 0); dryness = st.slider("B6. Khô da", 0, 3, 0); intensity = erythema + edema + oozing + excoriation + lichenification + dryness; itch = st.slider("C1. Ngứa (0-10)", 0, 10, 0); sleep_loss = st.slider("C2. Mất ngủ (0-10)", 0, 10, 0); subjective = itch + sleep_loss; total = extent/5 * 0.7 + intensity * 7/2 + subjective
    if st.button("🔬 Tính SCORAD", type="primary", use_container_width=True):
        if total < 25: severity = "Nhẹ"; color = "#28a745"
        elif total < 50: severity = "Trung bình"; color = "#fd7e14"
        else: severity = "Nặng"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>SCORAD: {total:.1f}/103</h2><p style='text-align: center; margin-top: 10px;'>{severity}</p></div>", unsafe_allow_html=True)
if __name__ == "__main__": render()

