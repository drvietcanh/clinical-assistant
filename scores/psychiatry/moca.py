"""MoCA - Montreal Cognitive Assessment"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #7C3AED;'>🧠 MoCA</h2><p style='text-align: center;'><em>Đánh giá nhận thức Montreal</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ MoCA"): st.markdown("**MoCA** nhạy hơn MMSE với suy giảm nhẹ (MCI). **Điểm:** 0-30")
    st.markdown("---"); visuospatial = st.number_input("Thị-không gian (0-5)", 0, 5, 5); naming = st.number_input("Đặt tên (0-3)", 0, 3, 3); attention = st.number_input("Chú ý (0-6)", 0, 6, 6); language = st.number_input("Ngôn ngữ (0-3)", 0, 3, 3); abstraction = st.number_input("Trừu tượng (0-2)", 0, 2, 2); memory = st.number_input("Trí nhớ (0-5)", 0, 5, 5); orientation = st.number_input("Định hướng (0-6)", 0, 6, 6); total = visuospatial + naming + attention + language + abstraction + memory + orientation; education = st.checkbox("+1 điểm nếu học ≤12 năm"); if education: total += 1; total = min(total, 30)
    if st.button("🔬 Tính MoCA", type="primary", use_container_width=True):
        if total >= 26: status = "Bình thường"; color = "#28a745"
        else: status = "Suy giảm nhận thức"; color = "#fd7e14"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>MoCA: {total}/30</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>", unsafe_allow_html=True); st.info("**Điểm cắt:** < 26 → Suy giảm nhận thức (MCI hoặc Dementia)")
if __name__ == "__main__": render()

