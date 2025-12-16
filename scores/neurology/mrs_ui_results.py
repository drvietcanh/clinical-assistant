"""
mRS Calculator - Kết quảs Display UI Components
Handles all results display and recommendations
"""

import streamlit as st


def render_results_display(selected_mrs, mrs_info):
    """Render all results display sections"""
    
    st.markdown("---")
    st.markdown("## 📊 KẾT QUẢ")
    
    # Score badge
    st.markdown(f"""
    <div style="background-color: {mrs_info['color']}; padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="color: white; margin: 0;">{mrs_info['icon']} mRS = {selected_mrs}</h1>
        <p style="color: white; margin: 0; font-size: 1.2rem;">{mrs_info['independence']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("mRS Score", f"{selected_mrs}/6")
    
    with col2:
        st.metric("Kết Cục", mrs_info["outcome"])
    
    with col3:
        st.metric("Mức độ Độc lập", mrs_info["independence"])
    
    st.markdown("---")
    
    # Interpretation and recommendations
    st.markdown("### 📋 ĐÁNH GIÁ & KHUYẾN NGHỊ")
    
    render_recommendations(selected_mrs, mrs_info)


def render_recommendations(selected_mrs, mrs_info):
    """Render recommendations based on selected mRS grade"""
    
    if selected_mrs == 0:
        st.success(f"""
        **{mrs_info['icon']} mRS 0 - HOÀN TOÀN BÌNH THƯỜNG**
        
        **Đánh giá:** Bệnh nhân đã hồi phục hoàn toàn, không còn bất kỳ triệu chứng nào.
        
        **Khuyến nghị:**
        
        1. **Phòng ngừa đột quỵ tái phát:**
           - Kiểm soát yếu tố nguy cơ: tăng huyết áp, đái tháo đường, lipid máu
           - Thuốc chống kết tập tiểu cầu (aspirin, clopidogrel) nếu đột quỵ thiếu máu
           - Kháng đông (warfarin/NOAC) nếu rung nhĩ
           - Statin nếu có chỉ định
        
        2. **Thay đổi lối sống:**
           - Bỏ thuốc lá hoàn toàn
           - Tập thể dục đều đặn (150 phút/tuần)
           - Chế độ ăn lành mạnh (giảm muối, nhiều rau quả)
           - Duy trì cân nặng lý tưởng
        
        3. **Theo dõi định kỳ:**
           - Khám thần kinh mỗi 3-6 tháng năm đầu
           - Theo dõi huyết áp, đường huyết, lipid
           - Siêu âm Doppler động mạch cảnh nếu có hẹp
        
        4. **Giáo dục:**
           - Nhận biết dấu hiệu đột quỵ tái phát (FAST)
           - Tầm quan trọng của tuân thủ thuốc
           - Khi nào cần đến bệnh viện khẩn cấp
        
        **Tiên lượng:** Xuất sắc. Nguy cơ tái phát 3-5%/năm, có thể giảm bằng dự phòng tốt.
        """)
    
    elif selected_mrs == 1:
        st.success(f"""
        **{mrs_info['icon']} mRS 1 - KHUYẾT TẬT KHÔNG ĐÁNG KỂ**
        
        **Đánh giá:** Có triệu chứng nhẹ nhưng không ảnh hưởng đáng kể đến sinh hoạt.
        
        **Khuyến nghị:**
        
        1. **Phục hồi chức năng:**
           - Vật lý trị liệu để cải thiện sức mạnh, phối hợp vận động
           - Ngôn ngữ trị liệu nếu có nói khó nhẹ
           - Trị liệu nghề nghiệp để tối ưu hóa khả năng làm việc
        
        2. **Phòng ngừa thứ phát:**
           - Tương tự mRS 0
           - Kiểm soát yếu tố nguy cơ chặt chẽ
           - Thuốc chống đông/chống kết tập tiểu cầu
        
        3. **Tâm lý:**
           - Sàng lọc trầm cảm sau đột quỵ (phổ biến ~30%)
           - Tư vấn tâm lý nếu cần
           - Hỗ trợ tái hòa nhập xã hội, công việc
        
        4. **Theo dõi:**
           - Đánh giá chức năng định kỳ
           - Theo dõi tiến triển triệu chứng
        
        **Tiên lượng:** Xuất sắc. Chất lượng sống tốt, có thể trở lại làm việc toàn thời gian.
        """)
    
    elif selected_mrs == 2:
        st.success(f"""
        **{mrs_info['icon']} mRS 2 - KHUYẾT TẬT NHẸ**
        
        **Đánh giá:** Khuyết tật nhẹ, tự chăm sóc được nhưng không làm được tất cả hoạt động như trước.
        
        **Khuyến nghị:**
        
        1. **Phục hồi chức năng tích cực:**
           - **Vật lý trị liệu:** 3-5 buổi/tuần
             * Tập sức mạnh, cân bằng, đi bộ
             * Sử dụng dụng cụ hỗ trợ nếu cần (gậy, nẹp...)
           - **Trị liệu nghề nghiệp:**
             * Tập kỹ năng sinh hoạt hàng ngày (ADL)
             * Đánh giá môi trường nhà ở, điều chỉnh nếu cần
           - **Ngôn ngữ trị liệu:** Nếu có vấn đề giao tiếp
        
        2. **Phòng ngừa thứ phát:** (Tương tự mRS 0-1)
        
        3. **Hỗ trợ tâm lý và xã hội:**
           - Sàng lọc trầm cảm
           - Tư vấn nghề nghiệp (có thể cần thay đổi công việc)
           - Hỗ trợ tài chính nếu mất khả năng làm việc
        
        4. **An toàn:**
           - Đánh giá nguy cơ ngã
           - Cải thiện an toàn tại nhà (tay vịn, chống trơn...)
           - Đánh giá khả năng lái xe
        
        5. **Theo dõi:**
           - Đánh giá chức năng mỗi 1-3 tháng
           - Điều chỉnh phục hồi chức năng dựa trên tiến triển
        
        **Tiên lượng:** Tốt. Nhiều bệnh nhân cải thiện thêm trong 6-12 tháng đầu. 
        Một số có thể trở lại làm việc bán thời gian hoặc công việc nhẹ.
        """)
    
    elif selected_mrs == 3:
        st.warning(f"""
        **{mrs_info['icon']} mRS 3 - KHUYẾT TẬT TRUNG BÌNH**
        
        **Đánh giá:** Cần giúp đỡ một số hoạt động nhưng đi lại độc lập.
        
        **Khuyến nghị:**
        
        1. **Phục hồi chức năng chuyên sâu:**
           - **Vật lý trị liệu:** 5-7 buổi/tuần (giai đoạn đầu)
             * Tập đi bộ, cân bằng
             * Tăng sức mạnh chi yếu
             * Dụng cụ hỗ trợ: gậy, walker
           - **Trị liệu nghề nghiệp:**
             * Tập ADL: tắm, mặc quần áo, nấu ăn
             * Đánh giá và cải thiện an toàn tại nhà
           - **Ngôn ngữ trị liệu:** Nếu cần
        
        2. **Hỗ trợ tại nhà:**
           - Cần người giúp việc một phần thời gian
           - Cải thiện nhà ở: tay vịn, ghế tắm, nâng toilet...
           - Dịch vụ giao đồ ăn, giặt giũ nếu cần
        
        3. **Phòng ngừa biến chứng:**
           - Dự phòng ngã: dụng cụ hỗ trợ, cải thiện môi trường
           - Phòng loét: thay đổi tư thế thường xuyên
           - Phòng co rút: vận động, kéo giãn
        
        4. **Hỗ trợ tâm lý:**
           - Sàng lọc và điều trị trầm cảm
           - Nhóm hỗ trợ bệnh nhân đột quỵ
           - Tư vấn gia đình
        
        5. **Theo dõi:**
           - Đánh giá chức năng định kỳ
           - Điều chỉnh phục hồi chức năng
           - Theo dõi biến chứng
        
        **Tiên lượng:** Trung bình. Một số bệnh nhân cải thiện lên mRS 2 với phục hồi chức năng tốt.
        Cần hỗ trợ dài hạn.
        """)
    
    elif selected_mrs == 4:
        st.error(f"""
        **{mrs_info['icon']} mRS 4 - KHUYẾT TẬT VỪA NẶNG**
        
        **Đánh giá:** Phụ thuộc nặng, cần giúp đỡ đi lại và tự chăm sóc.
        
        **Khuyến nghị:**
        
        1. **Phục hồi chức năng:**
           - **Vật lý trị liệu:** Duy trì khả năng vận động tối đa
             * Tập ngồi, đứng, chuyển tư thế
             * Phòng co rút, loét
             * Sử dụng xe lăn, hoyer lift
           - **Trị liệu nghề nghiệp:** Tập ADL cơ bản
           - **Mục tiêu thực tế:** Duy trì chức năng, phòng biến chứng
        
        2. **Chăm sóc tại nhà hoặc cơ sở:**
           - **Cần người chăm sóc toàn thời gian**
           - Cân nhắc:
             * Chăm sóc tại nhà với người giúp việc
             * Nursing home
             * Long-term care facility
           - Dụng cụ: Giường bệnh, xe lăn, tã người lớn, thiết bị nâng
        
        3. **Phòng ngừa biến chứng:**
           - **Loét do tỳ:** Nệm chống loét, thay đổi tư thế q2h
           - **Co rút khớp:** Vận động, kéo giãn, splinting
           - **Viêm phổi hít:** Tư thế đầu cao, vệ sinh răng miệng
           - **DVT:** Compression stockings, anticoagulation nếu phù hợp
           - **Tiểu tiện:** Catheter care, bowel program
        
        4. **Dinh dưỡng:**
           - Đánh giá khả năng nuốt
           - Cân nhắc ống ng dài hạn (PEG) nếu cần
        
        5. **Hỗ trợ gia đình:**
           - Giáo dục kỹ năng chăm sóc
           - Hỗ trợ tâm lý cho người chăm sóc (caregiver burnout)
           - Dịch vụ tạm nghỉ (respite care)
        
        6. **Quyết định chăm sóc:**
           - Thảo luận về advance directives
           - DNR/DNI status
           - Goals of care
        
        **Tiên lượng:** Xấu. Chất lượng sống giảm đáng kể. Cải thiện ít, chủ yếu duy trì chức năng.
        """)
    
    elif selected_mrs == 5:
        st.error(f"""
        **{mrs_info['icon']} mRS 5 - KHUYẾT TẬT NẶNG**
        
        **Đánh giá:** Nằm liệt giường, không tự chủ, cần chăm sóc toàn diện.
        
        **Khuyến nghị:**
        
        1. **Chăm sóc dài hạn:**
           - **BẮT BUỘC chăm sóc 24/7**
           - Cơ sở chăm sóc dài hạn (nursing home, skilled nursing facility)
           - Chăm sóc tại nhà với đội chăm sóc chuyên nghiệp (khó khăn, tốn kém)
        
        2. **Phòng ngừa biến chứng (QUAN TRỌNG):**
           - **Loét do tỳ:**
             * Nệm chống loét (air mattress)
             * Thay đổi tư thế mỗi 2 giờ
             * Chăm sóc da cẩn thận
           - **Co rút khớp:**
             * ROM (Range of Motion) exercises hàng ngày
             * Splinting
           - **Viêm phổi:**
             * Vệ sinh răng miệng
             * Hút đờm
             * Tư thế đầu cao
           - **Tiểu tiện:**
             * Catheter care (Foley hoặc suprapubic)
             * Bowel program (chống táo bón)
           - **DVT/PE:**
             * Compression stockings
             * Cân nhắc anticoagulation
        
        3. **Dinh dưỡng:**
           - Thường cần ống ng dài hạn (PEG tube)
           - Dinh dưỡng cân bằng
           - Phòng hít: tư thế đúng khi cho ăn
        
        4. **Chăm sóc giảm nhẹ (Palliative Care):**
           - **Cân nhắc tham vấn Palliative Care**
           - Kiểm soát triệu chứng: đau, khó thở, lo âu
           - Chất lượng sống > kéo dài sự sống
        
        5. **Hỗ trợ gia đình:**
           - Tư vấn tâm lý
           - Hỗ trợ quyết định
           - Giúp đỡ tài chính, pháp lý
        
        6. **Quyết định chăm sóc:**
           - **Thảo luận nghiêm túc về goals of care:**
             * Mức độ can thiệp y tế
             * DNR/DNI
             * Comfort care measures
           - **Advance directives**
           - **End-of-life planning**
        
        7. **Phục hồi chức năng hạn chế:**
           - ROM để phòng co rút
           - Tư thế tốt để phòng biến chứng
           - Kích thích cảm giác nếu phù hợp
        
        **Tiên lượng:** Rất xấu. Tỷ lệ tử vong cao trong 1 năm. Chất lượng sống rất kém.
        Cần thảo luận thẳng thắn với gia đình về hiện thực và kỳ vọng.
        """)
    
    else:  # mRS 6
        st.error(f"""
        **{mrs_info['icon']} mRS 6 - TỬ VONG**
        
        **Đánh giá:** Bệnh nhân đã tử vong.
        
        **Hỗ trợ gia đình:**
        - Tư vấn tâm lý cho gia đình
        - Giải thích nguyên nhân tử vong
        - Hỗ trợ thủ tục hành chính
        - Cân nhắc khám nghiệm tử thi nếu cần thiết để xác định nguyên nhân
        """)

