"""CDAI - Clinical Disease Activity Index for RA"""
import streamlit as st
def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 CDAI</h2><p style='text-align: center;'><em>Chỉ số hoạt động lâm sàng RA</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ CDAI"): st.markdown("**CDAI** = TJC + SJC + PGA + EGA. Không cần xét nghiệm, tính nhanh.")
    st.markdown("---"); tjc = st.number_input("TJC - Số khớp đau (0-28)", 0, 28, 0, format="%d"); sjc = st.number_input("SJC - Số khớp sưng (0-28)", 0, 28, 0, format="%d"); pga = st.slider("PGA - Bệnh nhân đánh giá (cm, 0-10)", 0.0, 10.0, 5.0, 0.1); ega = st.slider("EGA - Bác sĩ đánh giá (cm, 0-10)", 0.0, 10.0, 5.0, 0.1); cdai = tjc + sjc + pga + ega
    if st.button("🔬 Tính CDAI", type="primary", use_container_width=True):
        if cdai <= 2.8: status = "Thuyên giảm"; color = "#28a745"
        elif cdai <= 10: status = "Hoạt động thấp"; color = "#28a745"
        elif cdai <= 22: status = "Hoạt động trung bình"; color = "#fd7e14"
        else: status = "Hoạt động cao"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>CDAI: {cdai:.1f}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>", unsafe_allow_html=True)
if __name__ == "__main__": render()

