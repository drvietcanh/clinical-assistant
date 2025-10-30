"""
Karnofsky Performance Scale Calculator
Thang đo thể trạng bệnh nhân ung thư
"""

import streamlit as st


def interpret_karnofsky(score):
    """Interpret Karnofsky score"""
    
    if score >= 80:
        status = "Tốt - Tự chăm sóc được"
        care = "Tự chăm sóc, hoạt động bình thường"
        prognosis = "Tiên lượng tốt, có thể điều trị tích cực"
        color = "green"
    elif score >= 50:
        status = "Trung bình - Cần hỗ trợ"
        care = "Cần hỗ trợ nhưng chưa cần chăm sóc liên tục"
        prognosis = "Có thể điều trị, cần theo dõi chặt"
        color = "orange"
    else:
        status = "Kém - Cần chăm sóc nhiều"
        care = "Cần chăm sóc y tế liên tục"
        prognosis = "Tiên lượng xấu, cân nhắc chăm sóc giảm nhẹ"
        color = "red"
    
    return {
        "score": score,
        "status": status,
        "care": care,
        "prognosis": prognosis,
        "color": color
    }


def render():
    """Render Karnofsky Performance Scale interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #8B5CF6;'>📊 Karnofsky Performance Scale (KPS)</h2>
    <p style='text-align: center;'><em>Thang đo thể trạng bệnh nhân ung thư</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu về Karnofsky Performance Scale"):
        st.markdown("""
        **KPS** là thang đo thể trạng (functional status) được sử dụng rộng rãi trong ung thư học.
        
        **Mục đích:**
        - Đánh giá khả năng hoạt động của bệnh nhân
        - Quyết định phác đồ điều trị
        - Dự đoán tiên lượng
        - Theo dõi diễn biến bệnh
        
        **Thang điểm:** 0-100 (10 điểm mỗi bậc)
        - 100: Hoàn toàn bình thường
        - 0: Tử vong
        
        **So sánh với ECOG:**
        - KPS: 0-100, chi tiết hơn
        - ECOG: 0-5, đơn giản hơn
        - Có thể chuyển đổi qua lại
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Chọn mức độ phù hợp nhất với bệnh nhân")
    
    kps_score = st.select_slider(
        "Karnofsky Performance Scale",
        options=[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0],
        value=80,
        format_func=lambda x: {
            100: "100 - Bình thường, không triệu chứng",
            90: "90 - Hoạt động bình thường, triệu chứng nhẹ",
            80: "80 - Hoạt động bình thường với nỗ lực, có triệu chứng",
            70: "70 - Tự chăm sóc nhưng không làm việc được",
            60: "60 - Cần hỗ trợ đôi khi, tự chăm sóc hầu hết",
            50: "50 - Cần hỗ trợ đáng kể và chăm sóc y tế thường xuyên",
            40: "40 - Cần chăm sóc đặc biệt, bất lực",
            30: "30 - Bất lực nặng, nên nhập viện",
            20: "20 - Bệnh rất nặng, cần nhập viện tích cực",
            10: "10 - Hấp hối",
            0: "0 - Tử vong"
        }[x],
        help="Kéo để chọn mức độ phù hợp"
    )
    
    st.markdown("---")
    
    # Detailed descriptions
    with st.expander("📖 Mô tả chi tiết từng mức"):
        st.markdown("""
        ### 🟢 80-100: Tốt - Tự chăm sóc
        
        **100** - Bình thường, không triệu chứng hoặc bệnh tật
        
        **90** - Hoạt động bình thường; triệu chứng hoặc dấu hiệu bệnh nhẹ
        
        **80** - Hoạt động bình thường với nỗ lực; có một số triệu chứng/dấu hiệu bệnh
        
        ### 🟡 50-70: Trung bình - Cần hỗ trợ
        
        **70** - Tự chăm sóc được; không thể làm việc hoặc hoạt động bình thường
        
        **60** - Cần hỗ trợ thỉnh thoảng nhưng tự chăm sóc hầu hết nhu cầu
        
        **50** - Cần hỗ trợ đáng kể và chăm sóc y tế thường xuyên
        
        ### 🔴 0-40: Kém - Phụ thuộc
        
        **40** - Tàn tật (disabled); cần chăm sóc và hỗ trợ đặc biệt
        
        **30** - Tàn tật nặng; nên nhập viện mặc dù chưa đến giai đoạn hấp hối
        
        **20** - Bệnh rất nặng; cần nhập viện; cần điều trị hỗ trợ tích cực
        
        **10** - Hấp hối; tiến triển nhanh đến tử vong
        
        **0** - Tử vong
        """)
    
    if st.button("🔬 Đánh giá Karnofsky", type="primary", use_container_width=True):
        result = interpret_karnofsky(kps_score)
        
        st.markdown("## 📊 Kết quả")
        
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                KPS: {result['score']}
            </h2>
            <p style='text-align: center; font-size: 1.2em; margin-top: 10px;'>
                {result['status']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Đánh giá</h3>
            <p style='font-size: 1.1em;'><strong>Khả năng tự chăm sóc:</strong> {result['care']}</p>
            <p style='font-size: 1.1em;'><strong>Ý nghĩa lâm sàng:</strong> {result['prognosis']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Clinical implications
        if result["score"] >= 80:
            st.success("""
            ✅ **KPS 80-100: Thể trạng tốt**
            
            **Điều trị:**
            - Có thể điều trị tích cực (hóa trị, xạ trị, phẫu thuật)
            - Dung nạp điều trị tốt
            - Có thể tham gia thử nghiệm lâm sàng
            
            **Tiên lượng:** Tốt hơn nhóm KPS thấp
            """)
        elif result["score"] >= 50:
            st.warning("""
            ⚠️ **KPS 50-70: Thể trạng trung bình**
            
            **Điều trị:**
            - Cân nhắc điều trị phù hợp với thể trạng
            - Có thể cần giảm liều hóa trị
            - Tăng cường hỗ trợ dinh dưỡng, phục hồi chức năng
            
            **Theo dõi:** Cần đánh giá kỹ lợi ích/nguy cơ điều trị
            """)
        else:
            st.error("""
            🔴 **KPS < 50: Thể trạng kém**
            
            **Điều trị:**
            - Cân nhắc chăm sóc giảm nhẹ (palliative care)
            - Điều trị triệu chứng
            - Hỗ trợ tâm lý, tinh thần
            - Thảo luận mục tiêu chăm sóc với bệnh nhân/gia đình
            
            **Lưu ý:** KPS < 30 thường không phù hợp điều trị tích cực
            """)
        
        # KPS to ECOG conversion
        with st.expander("🔄 Chuyển đổi KPS ↔ ECOG"):
            st.markdown("""
            | KPS | ECOG | Mô tả |
            |:---:|:----:|:------|
            | 100 | 0 | Hoạt động hoàn toàn bình thường |
            | 80-90 | 1 | Hạn chế hoạt động nặng, làm việc nhẹ được |
            | 60-70 | 2 | Tự chăm sóc, không làm việc được, nằm < 50% thời gian |
            | 40-50 | 3 | Tự chăm sóc hạn chế, nằm > 50% thời gian |
            | 10-30 | 4 | Hoàn toàn phụ thuộc, nằm liệt giường |
            | 0 | 5 | Tử vong |
            """)
        
        with st.expander("📊 Ý nghĩa tiên lượng"):
            st.markdown("""
            ### Tiên lượng sống:
            
            **KPS cao (≥ 70):**
            - Sống còn dài hơn
            - Đáp ứng điều trị tốt hơn
            - Chất lượng sống tốt hơn
            
            **KPS thấp (< 50):**
            - Tiên lượng xấu
            - Nguy cơ biến chứng điều trị cao
            - Nên cân nhắc chăm sóc giảm nhẹ
            
            ### Quyết định điều trị:
            
            - **KPS ≥ 80:** Hầu hết phác đồ đều phù hợp
            - **KPS 60-70:** Cần điều chỉnh phác đồ
            - **KPS < 50:** Ưu tiên chăm sóc giảm nhẹ
            - **KPS < 30:** Không nên điều trị tích cực
            
            **Lưu ý:** KPS chỉ là một trong nhiều yếu tố quyết định điều trị
            """)


if __name__ == "__main__":
    render()

