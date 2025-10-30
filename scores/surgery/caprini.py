"""
Caprini VTE Risk Score
Nguy cơ huyết khối tĩnh mạch sau phẫu thuật
"""

import streamlit as st

def render():
    st.markdown("<h2 style='text-align: center; color: #DC2626;'>🩸 Caprini VTE Risk Score</h2><p style='text-align: center;'><em>Nguy cơ huyết khối sau phẫu thuật</em></p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ Caprini Score"):
        st.markdown("**Caprini** đánh giá nguy cơ VTE sau phẫu thuật để quyết định dự phòng. Điểm cao = Nguy cơ cao")
    
    st.markdown("---")
    st.subheader("📝 Yếu tố nguy cơ")
    
    score = 0
    
    st.markdown("### 1 điểm mỗi yếu tố:")
    age_40_60 = st.checkbox("Tuổi 41-60"); score += 1 if age_40_60 else 0
    minor_surgery = st.checkbox("Phẫu thuật nhỏ"); score += 1 if minor_surgery else 0
    bmi_25_30 = st.checkbox("BMI > 25"); score += 1 if bmi_25_30 else 0
    varicose = st.checkbox("Suy giãn tĩnh mạch"); score += 1 if varicose else 0
    
    st.markdown("### 2 điểm:")
    age_60_74 = st.checkbox("Tuổi 61-74"); score += 2 if age_60_74 else 0
    laparoscopic = st.checkbox("Phẫu thuật nội soi > 45 phút"); score += 2 if laparoscopic else 0
    malignancy = st.checkbox("Ung thư"); score += 2 if malignancy else 0
    bed_rest = st.checkbox("Nằm giường > 72h"); score += 2 if bed_rest else 0
    
    st.markdown("### 3 điểm:")
    age_75 = st.checkbox("Tuổi ≥ 75"); score += 3 if age_75 else 0
    dvt_history = st.checkbox("Tiền sử DVT/PE"); score += 3 if dvt_history else 0
    family_history = st.checkbox("Gia đình có DVT/PE"); score += 3 if family_history else 0
    
    st.markdown("### 5 điểm:")
    stroke = st.checkbox("Đột quỵ < 1 tháng"); score += 5 if stroke else 0
    major_surgery = st.checkbox("Phẫu thuật lớn > 45 phút"); score += 5 if major_surgery else 0
    
    st.markdown("---")
    
    if st.button("🔬 Tính Caprini", type="primary", use_container_width=True):
        if score <= 1:
            risk = "Rất thấp"; prophylaxis = "Vận động sớm"; color = "green"
        elif score <= 2:
            risk = "Thấp"; prophylaxis = "Vận động sớm, tất chống huyết khối"; color = "green"
        elif score <= 4:
            risk = "Trung bình"; prophylaxis = "Heparin liều thấp hoặc LMWH"; color = "orange"
        else:
            risk = "Cao"; prophylaxis = "LMWH liều cao + tất chống huyết khối"; color = "red"
        
        score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[color]
        
        st.markdown(f"<div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'><h2 style='color: {score_color}; margin: 0; text-align: center;'>Caprini: {score}</h2></div>", unsafe_allow_html=True)
        
        st.markdown(f"<div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'><h3 style='color: {score_color};'>🎯 Nguy cơ: {risk}</h3><p style='font-size: 1.2em;'><strong>Dự phòng:</strong> {prophylaxis}</p></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    render()

