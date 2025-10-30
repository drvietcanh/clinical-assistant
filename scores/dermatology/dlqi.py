"""
DLQI - Dermatology Life Quality Index
Chỉ số chất lượng cuộc sống bệnh da
"""

import streamlit as st

def calculate_dlqi(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    """Tính DLQI"""
    total = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    
    if total <= 1:
        impact = "Không ảnh hưởng"; color = "green"
    elif total <= 5:
        impact = "Ảnh hưởng nhỏ"; color = "green"
    elif total <= 10:
        impact = "Ảnh hưởng trung bình"; color = "orange"
    elif total <= 20:
        impact = "Ảnh hưởng lớn"; color = "orange"
    else:
        impact = "Ảnh hưởng rất lớn"; color = "red"
    
    return {"total_score": total, "impact": impact, "color": color}

def render():
    st.markdown("<h2 style='text-align: center; color: #EC4899;'>🩹 DLQI</h2><p style='text-align: center;'><em>Chất lượng cuộc sống bệnh da</em></p>", unsafe_allow_html=True)
    
    with st.expander("ℹ️ DLQI"):
        st.markdown("**DLQI** đánh giá ảnh hưởng bệnh da đến chất lượng sống. **Thang điểm:** 0-30")
    
    st.markdown("---")
    st.info("**Trong 1 tuần qua**, bệnh da ảnh hưởng như thế nào?")
    
    options = [("Rất nhiều", 3), ("Nhiều", 2), ("Một chút", 1), ("Không", 0)]
    
    q1 = st.radio("1. Ngứa, đau, cảm giác khó chịu?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q2 = st.radio("2. Xấu hổ, tự ti?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q3 = st.radio("3. Ảnh hưởng mua sắm hoặc chăm sóc nhà?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q4 = st.radio("4. Ảnh hưởng chọn quần áo?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q5 = st.radio("5. Ảnh hưởng hoạt động xã hội/giải trí?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q6 = st.radio("6. Ảnh hưởng thể thao?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q7 = st.radio("7. Ngăn cản làm việc/học tập?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q8 = st.radio("8. Gây vấn đề với bạn bè/người thân?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q9 = st.radio("9. Gây khó khăn tình dục?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    q10 = st.radio("10. Điều trị gây phiền toái?", [3,2,1,0], format_func=lambda x: dict(options)[x])
    
    if st.button("🔬 Tính DLQI", type="primary", use_container_width=True):
        result = calculate_dlqi(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10)
        score_color = {"green": "#28a745", "orange": "#fd7e14", "red": "#dc3545"}[result["color"]]
        
        st.markdown(f"<div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'><h2 style='color: {score_color}; margin: 0; text-align: center;'>DLQI: {result['total_score']}/30</h2></div>", unsafe_allow_html=True)
        
        st.markdown(f"<div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'><h3 style='color: {score_color};'>🎯 Ảnh hưởng: {result['impact']}</h3></div>", unsafe_allow_html=True)
        
        st.info("""
        **Phân loại:**
        - 0-1: Không ảnh hưởng
        - 2-5: Ảnh hưởng nhỏ
        - 6-10: Ảnh hưởng trung bình
        - 11-20: Ảnh hưởng lớn
        - 21-30: Ảnh hưởng rất lớn
        """)

if __name__ == "__main__":
    render()

