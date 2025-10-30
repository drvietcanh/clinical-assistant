"""MMSE - Mini Mental State Exam"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #7C3AED;'>🧠 MMSE</h2><p style='text-align: center;'><em>Đánh giá nhận thức</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ MMSE"): st.markdown("**MMSE** sàng lọc suy giảm nhận thức. **Điểm:** 0-30")
    st.markdown("---"); orientation = st.number_input("Định hướng (0-10)", 0, 10, 10); registration = st.number_input("Ghi nhớ (0-3)", 0, 3, 3); attention = st.number_input("Chú ý (0-5)", 0, 5, 5); recall = st.number_input("Nhớ lại (0-3)", 0, 3, 3); language = st.number_input("Ngôn ngữ (0-9)", 0, 9, 9); total = orientation + registration + attention + recall + language
    if st.button("🔬 Tính MMSE", type="primary", use_container_width=True):
        if total >= 27: status = "Bình thường"; color = "#28a745"
        elif total >= 21: status = "Suy giảm nhẹ"; color = "#fd7e14"
        elif total >= 10: status = "Suy giảm trung bình"; color = "#fd7e14"
        else: status = "Suy giảm nặng"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>MMSE: {total}/30</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>", unsafe_allow_html=True)
if __name__ == "__main__": render()

