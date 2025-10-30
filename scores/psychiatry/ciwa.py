"""
CIWA-Ar - Clinical Institute Withdrawal Assessment for Alcohol
Đánh giá mức độ nặng cai rượu
"""

import streamlit as st

def calculate_ciwa(nausea, tremor, sweating, anxiety, agitation, tactile, auditory, visual, headache, orientation):
    """Tính CIWA-Ar score"""
    total = nausea + tremor + sweating + anxiety + agitation + tactile + auditory + visual + headache + orientation
    
    if total < 8:
        severity = "Nhẹ"; management = "Theo dõi, không cần thuốc"; color = "green"
    elif total <= 15:
        severity = "Trung bình"; management = "Cân nhắc benzodiazepine"; color = "orange"
    else:
        severity = "Nặng"; management = "Benzodiazepine ngay, theo dõi ICU"; color = "red"
    
    return {"total_score": total, "severity": severity, "management": management, "color": color}

def render():
    st.markdown("<h2 style='text-align: center; color: #DC2626;'>🍺 CIWA-Ar</h2><p style='text-align: center;'><em>Đánh giá cai rượu</em></p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu CIWA-Ar"):
        st.markdown("**CIWA-Ar** đánh giá mức độ nặng cai rượu, hướng dẫn điều trị benzos. **Thang điểm:** 0-67")
    
    st.markdown("---")
    nausea = st.slider("1. Buồn nôn/Nôn", 0, 7, 0, help="0=Không, 7=Nôn liên tục")
    tremor = st.slider("2. Run", 0, 7, 0, help="0=Không, 7=Run nặng")
    sweating = st.slider("3. Đổ mồ hôi", 0, 7, 0, help="0=Không, 7=Đổ nhiều mồ hôi")
    anxiety = st.slider("4. Lo âu", 0, 7, 0, help="0=Không, 7=Lo âu nặng")
    agitation = st.slider("5. Kích động", 0, 7, 0, help="0=Không, 7=Kích động liên tục")
    tactile = st.slider("6. Ảo giác xúc giác", 0, 7, 0, help="0=Không, 7=Ảo giác xúc giác liên tục")
    auditory = st.slider("7. Ảo giác thính giác", 0, 7, 0, help="0=Không, 7=Ảo giác rõ")
    visual = st.slider("8. Ảo giác thị giác", 0, 7, 0, help="0=Không, 7=Ảo giác rõ")
    headache = st.slider("9. Đau đầu", 0, 7, 0, help="0=Không, 7=Đau đầu nặng")
    orientation = st.slider("10. Định hướng", 0, 4, 0, help="0=Định hướng đầy đủ, 4=Không định hướng")
    
    if st.button("🔬 Tính CIWA-Ar", type="primary", use_container_width=True):
        result = calculate_ciwa(nausea, tremor, sweating, anxiety, agitation, tactile, auditory, visual, headache, orientation)
        score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[result["color"]]
        
        st.markdown(f"<div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'><h2 style='color: {score_color}; margin: 0; text-align: center;'>CIWA-Ar: {result['total_score']}/67</h2></div>", unsafe_allow_html=True)
        
        st.markdown(f"<div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'><h3 style='color: {score_color};'>🎯 Mức độ: {result['severity']}</h3><p style='font-size: 1.2em;'><strong>Điều trị:</strong> {result['management']}</p></div>", unsafe_allow_html=True)
        
        st.info("""
        **Khuyến cáo điều trị:**
        - **< 8:** Không cần benzodiazepine, theo dõi
        - **8-15:** Lorazepam 1-2mg hoặc Diazepam 5-10mg
        - **> 15:** Lorazepam 2-4mg hoặc Diazepam 10-20mg, đánh giá lại mỗi 1h
        
        **Đánh giá lại:** Mỗi 1-4 giờ tùy mức độ
        """)

if __name__ == "__main__":
    render()

