"""SLEDAI - SLE Disease Activity Index"""
import streamlit as st
import streamlit.components.v1 as components
def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦋 SLEDAI</h2><p style='text-align: center;'><em>Hoạt động bệnh Lupus</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ SLEDAI"): st.markdown("**SLEDAI** đánh giá hoạt động bệnh SLE trong 10 ngày qua. **Điểm:** 0-105")
    st.markdown("---"); st.info("Đánh dấu triệu chứng trong **10 ngày qua**:"); score = 0; score += 8 if st.checkbox("Co giật (8đ)") else 0; score += 8 if st.checkbox("Loạn thần (8đ)") else 0; score += 8 if st.checkbox("Hội chứng não (8đ)") else 0; score += 8 if st.checkbox("Rối loạn thị giác (8đ)") else 0; score += 8 if st.checkbox("Tổn thương thần kinh sọ (8đ)") else 0; score += 8 if st.checkbox("Đau đầu lupus (8đ)") else 0; score += 8 if st.checkbox("TIA (8đ)") else 0; score += 4 if st.checkbox("Viêm mạch (4đ)") else 0; score += 4 if st.checkbox("Viêm khớp (4đ)") else 0; score += 4 if st.checkbox("Viêm cơ (4đ)") else 0; score += 4 if st.checkbox("Trụ niệu (4đ)") else 0; score += 4 if st.checkbox("Hồng cầu niệu (4đ)") else 0; score += 4 if st.checkbox("Protein niệu (4đ)") else 0; score += 4 if st.checkbox("Bạch cầu niệu (4đ)") else 0; score += 2 if st.checkbox("Ban da mới (2đ)") else 0; score += 2 if st.checkbox("Loét miệng (2đ)") else 0; score += 2 if st.checkbox("Rụng tóc (2đ)") else 0; score += 2 if st.checkbox("Viêm màng phổi/tim (2đ)") else 0; score += 1 if st.checkbox("Giảm C3/C4 (1đ)") else 0; score += 2 if st.checkbox("Tăng anti-DNA (2đ)") else 0; score += 1 if st.checkbox("Sốt (1đ)") else 0; score += 1 if st.checkbox("Giảm tiểu cầu (1đ)") else 0; score += 1 if st.checkbox("Giảm bạch cầu (1đ)") else 0
    if st.button("🔬 Tính SLEDAI", type="primary", use_container_width=True):
        if score == 0: status = "Không hoạt động"; color = "#28a745"
        elif score <= 5: status = "Hoạt động nhẹ"; color = "#28a745"
        elif score <= 11: status = "Hoạt động trung bình"; color = "#fd7e14"
        else: status = "Hoạt động cao"; color = "#dc3545"
        result_html = f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>SLEDAI: {score}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>"
        components.html(result_html, height=120, scrolling=False)
if __name__ == "__main__": render()

