"""DAS28 - Disease Activity Score for Rheumatoid Arthritis"""
import streamlit as st
import math
def render():
    st.markdown("<h2 style='text-align: center; color: #F97316;'>🦴 DAS28</h2><p style='text-align: center;'><em>Hoạt động bệnh viêm khớp dạng thấp</em></p>", unsafe_allow_html=True)
    with st.expander("ℹ️ DAS28"): st.markdown("**DAS28** đánh giá hoạt động bệnh RA. Khám 28 khớp + ESR/CRP + đánh giá chủ quan.")
    st.markdown("---"); tjc = st.number_input("TJC - Số khớp đau (0-28)", 0, 28, 0); sjc = st.number_input("SJC - Số khớp sưng (0-28)", 0, 28, 0); method = st.radio("Chọn phương pháp:", ["DAS28-ESR", "DAS28-CRP"]); 
    if method == "DAS28-ESR": esr = st.number_input("ESR (mm/h)", 0, 200, 10); pga = st.slider("PGA - Bệnh nhân đánh giá (VAS 0-100mm)", 0, 100, 50); das28 = 0.56 * math.sqrt(tjc) + 0.28 * math.sqrt(sjc) + 0.70 * math.log(esr + 1) + 0.014 * pga
    else: crp = st.number_input("CRP (mg/L)", 0.0, 200.0, 5.0); pga = st.slider("PGA - Bệnh nhân đánh giá (VAS 0-100mm)", 0, 100, 50); das28 = 0.56 * math.sqrt(tjc) + 0.28 * math.sqrt(sjc) + 0.36 * math.log(crp + 1) + 0.014 * pga + 0.96
    
    if st.button("🔬 Tính DAS28", type="primary", use_container_width=True):
        if das28 < 2.6: status = "Thuyên giảm"; color = "#28a745"
        elif das28 < 3.2: status = "Hoạt động thấp"; color = "#28a745"
        elif das28 < 5.1: status = "Hoạt động trung bình"; color = "#fd7e14"
        else: status = "Hoạt động cao"; color = "#dc3545"
        st.markdown(f"<div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'><h2 style='color: {color}; margin: 0; text-align: center;'>DAS28: {das28:.2f}</h2><p style='text-align: center; margin-top: 10px;'>{status}</p></div>", unsafe_allow_html=True); st.info(f"**Mục tiêu điều trị:** < 2.6 (thuyên giảm) hoặc < 3.2 (hoạt động thấp)")
if __name__ == "__main__": render()

