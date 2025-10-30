"""
PPS - Palliative Performance Scale Calculator
Thang đo thể trạng chăm sóc giảm nhẹ
"""

import streamlit as st


def render():
    """Render PPS calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #8B5CF6;'>🕊️ PPS - Palliative Performance Scale</h2>
    <p style='text-align: center;'><em>Thang đo thể trạng chăm sóc giảm nhẹ</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về PPS"):
        st.markdown("""
        **PPS** đánh giá thể trạng bệnh nhân trong chăm sóc giảm nhẹ, giúp dự đoán tiên lượng sống.
        
        **Đánh giá 5 yếu tố:**
        - Khả năng di chuyển
        - Hoạt động & bằng chứng bệnh
        - Tự chăm sóc
        - Ăn uống
        - Mức độ ý thức
        
        **Thang điểm:** 0-100% (10% mỗi bậc)
        """)
    
    st.markdown("---")
    
    pps_score = st.select_slider(
        "Chọn mức PPS phù hợp:",
        options=[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],
        value=50,
        format_func=lambda x: {
            100: "100% - Hoàn toàn bình thường",
            90: "90% - Hoạt động bình thường, triệu chứng nhẹ",
            80: "80% - Hoạt động bình thường với nỗ lực",
            70: "70% - Không làm việc, tự chăm sóc được",
            60: "60% - Cần hỗ trợ đôi khi",
            50: "50% - Cần hỗ trợ đáng kể",
            40: "40% - Chủ yếu nằm giường",
            30: "30% - Hoàn toàn nằm giường",
            20: "20% - Hoàn toàn nằm giường, cần chăm sóc toàn diện",
            10: "10% - Hấp hối",
            0: "0% - Tử vong"
        }[x]
    )
    
    st.markdown("---")
    
    with st.expander("📖 Mô tả chi tiết từng mức"):
        st.markdown("""
        ### 100% - Hoàn toàn bình thường
        - Di chuyển: Đầy đủ
        - Hoạt động: Bình thường, không bệnh
        - Tự chăm sóc: Hoàn toàn
        - Ăn uống: Bình thường
        - Ý thức: Đầy đủ
        
        ### 50% - Cần hỗ trợ đáng kể  
        - Di chuyển: Chủ yếu ngồi/nằm
        - Hoạt động: Không thể làm việc, bệnh lan rộng
        - Tự chăm sóc: Cần hỗ trợ đáng kể
        - Ăn uống: Giảm
        - Ý thức: Đầy đủ hoặc lú lẫn
        
        ### 10% - Hấp hối
        - Di chuyển: Hoàn toàn nằm giường
        - Hoạt động: Tử vong sắp xảy ra
        - Tự chăm sóc: Hoàn toàn phụ thuộc
        - Ăn uống: Chỉ nuốt được
        - Ý thức: Hôn mê sâu
        """)
    
    if st.button("🔬 Đánh giá PPS", type="primary", use_container_width=True):
        if pps_score >= 70:
            prognosis = "Tuần/tháng"
            color = "green"
            care = "Chăm sóc giảm nhẹ ngoại trú"
        elif pps_score >= 50:
            prognosis = "Tuần"
            color = "orange"
            care = "Chăm sóc tại nhà với hỗ trợ"
        elif pps_score >= 20:
            prognosis = "Ngày/tuần"
            color = "orange"
            care = "Chăm sóc tại nhà hoặc hospice"
        else:
            prognosis = "Giờ/ngày"
            color = "red"
            care = "Hospice, chăm sóc end-of-life"
        
        score_color_map = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }
        sc = score_color_map[color]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {sc}22 0%, {sc}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {sc}; margin: 20px 0;'>
            <h2 style='color: {sc}; margin: 0; text-align: center;'>PPS: {pps_score}%</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {sc}22; padding: 20px; border-radius: 10px; border: 2px solid {sc};'>
            <h3 style='color: {sc};'>🎯 Tiên lượng sống: {prognosis}</h3>
            <p style='font-size: 1.1em;'><strong>Khuyến cáo:</strong> {care}</p>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    render()

