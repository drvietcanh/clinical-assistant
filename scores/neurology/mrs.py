"""
Modified Rankin Scale (mRS) - Measure of Disability After Stroke
Assesses degree of disability or dependence in daily activities

Scale: 0-6
- 0 = No symptoms
- 6 = Dead

Reference:
van Swieten JC, et al. Interobserver agreement for the assessment of handicap in stroke patients.
Stroke. 1988;19(5):604-7.

Also: Rankin J. Cerebral vascular accidents in patients over the age of 60. II. Prognosis.
Scott Med J. 1957;2(5):200-15.
"""

import streamlit as st


def render():
    """Render Modified Rankin Scale Calculator"""
    
    st.subheader("🧠 mRS - Modified Rankin Scale")
    st.caption("Đánh giá mức độ khuyết tật/phụ thuộc sau đột quỵ")
    
    st.markdown("""
    **Modified Rankin Scale (mRS)** là thang điểm đánh giá mức độ khuyết tật hoặc 
    phụ thuộc trong sinh hoạt hàng ngày sau đột quỵ hoặc các bệnh lý thần kinh khác.
    
    **Ứng dụng:**
    - Đánh giá kết cục chức năng sau đột quỵ
    - Theo dõi tiến triển phục hồi chức năng
    - Tiêu chí chính trong các nghiên cứu lâm sàng về đột quỵ
    """)
    
    st.markdown("---")
    
    # mRS grades description
    mrs_grades = {
        0: {
            "name": "mRS 0 - Không có triệu chứng",
            "desc": """
            **Hoàn toàn không có triệu chứng**
            
            **Đặc điểm:**
            - Không có bất kỳ triệu chứng nào
            - Hoàn toàn bình thường
            - Có thể thực hiện tất cả các hoạt động như trước
            
            **Ví dụ:**
            - Người bệnh đã hồi phục hoàn toàn sau TIA hoặc đột quỵ nhẹ
            - Không có dấu hiệu suy giảm thần kinh
            """,
            "color": "green",
            "icon": "✅",
            "outcome": "Excellent",
            "independence": "Hoàn toàn độc lập"
        },
        1: {
            "name": "mRS 1 - Không khuyết tật đáng kể",
            "desc": """
            **Không khuyết tật đáng kể mặc dù có triệu chứng**
            
            **Đặc điểm:**
            - Có thể thực hiện tất cả nhiệm vụ và hoạt động thường ngày như trước
            - Có thể có triệu chứng nhẹ (ví dụ: yếu nhẹ, rối loạn cảm giác nhẹ)
            - Triệu chứng không ảnh hưởng đến khả năng tự chăm sóc bản thân
            
            **Ví dụ:**
            - Yếu tay/chân nhẹ nhưng vẫn làm việc bình thường
            - Tê bì nhẹ nhưng không ảnh hưởng sinh hoạt
            - Nói khó nhẹ nhưng vẫn giao tiếp tốt
            """,
            "color": "green",
            "icon": "✅",
            "outcome": "Excellent",
            "independence": "Hoàn toàn độc lập"
        },
        2: {
            "name": "mRS 2 - Khuyết tật nhẹ",
            "desc": """
            **Khuyết tật nhẹ: Không thể thực hiện tất cả hoạt động như trước, nhưng tự chăm sóc được**
            
            **Đặc điểm:**
            - Không thể thực hiện một số hoạt động như trước đột quỵ
            - Có thể tự chăm sóc bản thân KHÔNG CẦN trợ giúp
            - Có thể đi lại độc lập
            - Có thể cần thay đổi công việc hoặc giảm giờ làm
            
            **Ví dụ:**
            - Không thể chạy bộ nhưng đi bộ bình thường
            - Không thể làm việc cũ (nặng) nhưng làm việc nhẹ được
            - Tự nấu ăn, tắm rửa, ăn uống được
            - Yếu tay/chân vừa phải nhưng không cần người hỗ trợ
            """,
            "color": "lightgreen",
            "icon": "🟢",
            "outcome": "Good",
            "independence": "Độc lập"
        },
        3: {
            "name": "mRS 3 - Khuyết tật trung bình",
            "desc": """
            **Khuyết tật trung bình: Cần một ít trợ giúp, nhưng đi lại không cần hỗ trợ**
            
            **Đặc điểm:**
            - Cần một ít trợ giúp trong sinh hoạt
            - **Có thể đi lại KHÔNG CẦN hỗ trợ** (không cần người nâng đỡ, có thể dùng gậy)
            - Cần giúp đỡ một số hoạt động: nấu ăn, giặt giũ, quản lý tiền bạc
            
            **Ví dụ:**
            - Tự đi lại được (có thể dùng gậy) nhưng cần người giúp nấu ăn
            - Tự tắm rửa, ăn uống nhưng cần giúp mặc quần áo
            - Đi lại trong nhà tốt, ra ngoài cần có người đi cùng
            - Cần giúp quản lý thuốc, tài chính
            """,
            "color": "orange",
            "icon": "🟡",
            "outcome": "Moderate",
            "independence": "Phụ thuộc nhẹ"
        },
        4: {
            "name": "mRS 4 - Khuyết tật vừa nặng",
            "desc": """
            **Khuyết tật vừa nặng: Không thể đi lại độc lập và không tự chăm sóc được**
            
            **Đặc điểm:**
            - **KHÔNG thể đi lại mà không có hỗ trợ** (cần người nâng đỡ)
            - **KHÔNG thể tự chăm sóc nhu cầu cơ thể** (tắm, vệ sinh, ăn uống)
            - Cần người chăm sóc thường xuyên trong ngày
            
            **Ví dụ:**
            - Cần người đỡ để đi từ giường sang ghế
            - Cần giúp tắm, vệ sinh, mặc quần áo
            - Có thể cần giúp ăn uống
            - Liệt nặng, chỉ ngồi được trên xe lăn hoặc nằm giường
            - Có thể tự ngồi nhưng không tự đi được
            """,
            "color": "red",
            "icon": "🔴",
            "outcome": "Poor",
            "independence": "Phụ thuộc nặng"
        },
        5: {
            "name": "mRS 5 - Khuyết tật nặng",
            "desc": """
            **Khuyết tật nặng: Nằm liệt giường, tiểu tiện không tự chủ, cần chăm sóc liên tục**
            
            **Đặc điểm:**
            - **Nằm liệt giường** (bedridden)
            - **Tiểu tiện không tự chủ** (incontinence)
            - **Cần chăm sóc y tế liên tục 24/7**
            - Không thể tự thực hiện bất kỳ hoạt động nào
            
            **Ví dụ:**
            - Nằm liệt giường hoàn toàn
            - Không thể tự thay đổi tư thế
            - Cần đặt thông tiểu hoặc tã người lớn
            - Cần cho ăn qua ống hoặc nuôi bằng thìa
            - Cần chăm sóc toàn bộ: vệ sinh, thay đổi tư thế, phòng loét
            - Có thể ở trạng thái thực vật (vegetative state)
            """,
            "color": "darkred",
            "icon": "⚫",
            "outcome": "Very Poor",
            "independence": "Phụ thuộc hoàn toàn"
        },
        6: {
            "name": "mRS 6 - Tử vong",
            "desc": """
            **Tử vong**
            
            **Đặc điểm:**
            - Bệnh nhân đã tử vong
            """,
            "color": "black",
            "icon": "💀",
            "outcome": "Death",
            "independence": "N/A"
        }
    }
    
    # Selection
    st.markdown("### 🩺 Chọn Mức Độ Chức Năng")
    
    st.info("""
    **Hướng dẫn:** Chọn mức độ phù hợp nhất với tình trạng chức năng hiện tại của bệnh nhân.
    
    **Câu hỏi then chốt:**
    1. Bệnh nhân có thể **đi lại** mà không cần người hỗ trợ không? (Dùng gậy OK)
       - Có → mRS 0-3
       - Không → mRS 4-5
    
    2. Bệnh nhân có thể **tự chăm sóc bản thân** (tắm, vệ sinh, ăn uống) không?
       - Có → mRS 0-3
       - Không → mRS 4-5
    
    3. Bệnh nhân có **nằm liệt giường** và **không tự chủ tiểu tiện** không?
       - Có → mRS 5
       - Không → mRS 0-4
    """)
    
    selected_mrs = st.radio(
        "Chọn mRS Grade:",
        list(mrs_grades.keys()),
        format_func=lambda x: mrs_grades[x]["name"],
        help="Chọn grade phù hợp nhất với khả năng chức năng của bệnh nhân"
    )
    
    # Display selected grade details
    mrs_info = mrs_grades[selected_mrs]
    
    with st.expander(f"📖 Chi Tiết mRS {selected_mrs}", expanded=True):
        st.markdown(mrs_info["desc"])
    
    # Calculate button
    st.markdown("---")
    if st.button("🧮 Xác Nhận mRS Score", type="primary", use_container_width=True):
        st.session_state.total_calculations = st.session_state.get('total_calculations', 0) + 1
        
        # Display result
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
            st.metric("Mức Độ Độc Lập", mrs_info["independence"])
        
        st.markdown("---")
        
        # Interpretation and recommendations
        st.markdown("### 📋 ĐÁNH GIÁ & KHUYẾN NGHỊ")
        
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
        
        # Additional important notes
        st.markdown("---")
        st.info(f"""
        **📌 LƯU Ý QUAN TRỌNG VỀ mRS:**
        
        **1. Thời điểm đánh giá:**
        - **3 tháng sau đột quỵ** là thời điểm chuẩn trong nghiên cứu lâm sàng
        - Cũng có thể đánh giá tại: xuất viện, 1 tháng, 6 tháng, 1 năm
        - mRS có thể thay đổi theo thời gian (thường cải thiện trong 6-12 tháng đầu)
        
        **2. mRS trong nghiên cứu đột quỵ:**
        - **Primary endpoint** trong hầu hết nghiên cứu về đột quỵ
        - **Kết cục tốt** thường định nghĩa là: mRS 0-2 (độc lập)
        - **Kết cục xấu:** mRS 3-6 (phụ thuộc hoặc tử vong)
        
        **3. Các yếu tố ảnh hưởng mRS:**
        - Mức độ nặng đột quỵ ban đầu (NIHSS)
        - Vị trí, kích thước tổn thương
        - Tuổi (càng cao càng xấu)
        - Bệnh đi kèm
        - Thời gian được điều trị (thời gian đến bệnh viện)
        - Chất lượng phục hồi chức năng
        
        **4. Hạn chế của mRS:**
        - **Chủ quan:** Phụ thuộc người đánh giá
        - **Không chi tiết:** Không phân biệt giữa các loại khuyết tật (vận động vs nhận thức)
        - **Hiệu ứng trần/sàn:** Không nhạy với thay đổi nhỏ ở hai đầu thang điểm
        - **Khó phân biệt:** Đặc biệt là giữa mRS 2 vs 3, và 3 vs 4
        
        **5. Các thang điểm bổ sung:**
        - **Barthel Index:** Đánh giá chi tiết hơn ADL
        - **FIM (Functional Independence Measure):** Phục hồi chức năng
        - **NIHSS:** Đánh giá thần kinh học
        - **MoCA/MMSE:** Đánh giá nhận thức
        
        **6. "Good outcome" (mRS 0-2):**
        - Mục tiêu của điều trị đột quỵ cấp (thrombolysis, thrombectomy)
        - **Number Needed to Treat (NNT)** thường tính dựa trên tỷ lệ đạt mRS 0-2
        
        **7. Cân nhắc văn hóa:**
        - Khái niệm "phụ thuộc" có thể khác nhau giữa các nền văn hóa
        - Tại Việt Nam: Gia đình thường hỗ trợ nhiều hơn → Cần đánh giá kỹ khả năng thực sự của bệnh nhân
        """)
        
        # Comparison table
        with st.expander("📊 Bảng So Sánh mRS Scores"):
            st.markdown("""
            | mRS | Mô Tả | Đi Lại | Tự Chăm Sóc | Độc Lập | Kết Cục |
            |-----|-------|--------|-------------|---------|---------|
            | **0** | Không triệu chứng | ✅ Bình thường | ✅ Hoàn toàn | ✅ Hoàn toàn | 🟢 Excellent |
            | **1** | Triệu chứng nhẹ | ✅ Bình thường | ✅ Hoàn toàn | ✅ Hoàn toàn | 🟢 Excellent |
            | **2** | Khuyết tật nhẹ | ✅ Độc lập | ✅ Tự chăm sóc | ✅ Độc lập | 🟢 Good |
            | **3** | Khuyết tật trung bình | ✅ Không cần nâng | ⚠️ Cần giúp đỡ | ⚠️ Một phần | 🟡 Moderate |
            | **4** | Khuyết tật vừa nặng | ❌ Cần người đỡ | ❌ Cần giúp | ❌ Phụ thuộc | 🔴 Poor |
            | **5** | Khuyết tật nặng | ❌ Nằm giường | ❌ Cần chăm sóc 24/7 | ❌ Hoàn toàn | 🔴 Very Poor |
            | **6** | Tử vong | N/A | N/A | N/A | ⚫ Death |
            
            **Phân loại kết cục:**
            - **Good outcome:** mRS 0-2 (độc lập)
            - **Poor outcome:** mRS 3-6 (phụ thuộc hoặc tử vong)
            """)
        
        # Barthel Index comparison
        with st.expander("🔄 mRS vs Barthel Index"):
            st.markdown("""
            **Barthel Index** là thang điểm chi tiết hơn để đánh giá ADL (Activities of Daily Living).
            
            **So sánh tương đương (xấp xỉ):**
            
            | mRS | Barthel Index | Diễn Giải |
            |-----|---------------|-----------|
            | 0-1 | 100 | Hoàn toàn độc lập |
            | 2 | 95 | Gần như độc lập |
            | 3 | 60-90 | Cần giúp đỡ một phần |
            | 4 | 25-55 | Phụ thuộc nặng |
            | 5 | 0-20 | Phụ thuộc hoàn toàn |
            
            **Ưu điểm của Barthel:**
            - Chi tiết hơn (10 mục ADL)
            - Nhạy hơn với thay đổi nhỏ
            - Hữu ích cho theo dõi phục hồi chức năng
            
            **Ưu điểm của mRS:**
            - Đơn giản, nhanh
            - Tiêu chuẩn trong nghiên cứu đột quỵ
            - Dễ so sánh giữa các nghiên cứu
            """)
        
        # References
        with st.expander("📚 Tài Liệu Tham Khảo"):
            st.markdown("""
            **Primary References:**
            - Rankin J. *Cerebral vascular accidents in patients over the age of 60. II. Prognosis.* 
              Scott Med J. 1957 May;2(5):200-15. [PMID: 13432835]
            
            - van Swieten JC, Koudstaal PJ, Visser MC, Schouten HJ, van Gijn J. 
              *Interobserver agreement for the assessment of handicap in stroke patients.* 
              Stroke. 1988 May;19(5):604-7. [PMID: 3363593]
            
            **Structured Interview:**
            - Bruno A, Akinwuntan AE, Lin C, et al. 
              *Simplified modified rankin scale questionnaire: reproducibility over the telephone and validation with quality of life.* 
              Stroke. 2011;42(8):2276-9.
            
            **In Clinical Trials:**
            - Saver JL, Filip B, Hamilton S, et al. 
              *Improving the reliability of stroke disability grading in clinical trials and clinical practice: the Rankin Focused Assessment (RFA).* 
              Stroke. 2010;41(5):992-5.
            
            **Guidelines:**
            - Powers WJ, et al. *Guidelines for the Early Management of Patients With Acute Ischemic Stroke.* 
              Stroke. 2019;50(12):e344-e418.
            
            - Quinn TJ, Dawson J, Walters MR, Lees KR. 
              *Reliability of the modified Rankin Scale: a systematic review.* 
              Stroke. 2009;40(10):3393-5.
            """)
    
    # Educational content
    st.markdown("---")
    st.markdown("### 📖 THÔNG TIN THÊM")
    
    with st.expander("❓ Cách Đánh Giá mRS Chính Xác"):
        st.markdown("""
        **Cách tiếp cận có cấu trúc để đánh giá mRS:**
        
        **Bước 1: Hỏi về triệu chứng**
        - "Bạn có triệu chứng gì từ cơn đột quỵ không?"
        - Nếu KHÔNG → mRS 0
        - Nếu CÓ → Tiếp bước 2
        
        **Bước 2: Hỏi về hoạt động thường ngày**
        - "Bạn có thể làm tất cả những gì bạn làm trước đột quỵ không?"
        - Nếu CÓ → mRS 1
        - Nếu KHÔNG → Tiếp bước 3
        
        **Bước 3: Hỏi về tự chăm sóc**
        - "Bạn có thể tự chăm sóc bản thân không cần ai giúp không?" (tắm, vệ sinh, ăn uống, mặc quần áo)
        - Nếu CÓ → mRS 2
        - Nếu KHÔNG → Tiếp bước 4
        
        **Bước 4: Hỏi về đi lại**
        - "Bạn có thể đi lại mà không cần ai nâng đỡ không?" (dùng gậy OK)
        - Nếu CÓ → mRS 3
        - Nếu KHÔNG → Tiếp bước 5
        
        **Bước 5: Hỏi về nằm giường và tiểu tiện**
        - "Bạn có nằm liệt giường và không tự chủ tiểu tiện không?"
        - Nếu CÓ → mRS 5
        - Nếu KHÔNG → mRS 4
        
        **Lưu ý:**
        - Đánh giá dựa trên **khả năng thực sự**, không phải **tiềm năng**
        - Đánh giá **trạng thái hiện tại**, không phải trạng thái tốt nhất
        - Nếu bệnh nhân cần giúp đỡ vì lý do khác (không phải đột quỵ), cần cân nhắc riêng
        """)
    
    with st.expander("🎯 mRS Trong Quyết Định Lâm Sàng"):
        st.markdown("""
        **mRS được sử dụng để quyết định điều trị:**
        
        **1. Thrombolysis (Tiêu sợi huyết):**
        - Mục tiêu: Tăng tỷ lệ mRS 0-2 tại 3 tháng
        - Trong thực tế: mRS trước đột quỵ (pre-stroke mRS) quan trọng
        - Nếu pre-stroke mRS ≥2: Cân nhắc lợi ích/nguy cơ cẩn thận
        
        **2. Thrombectomy (Lấy huyết khối):**
        - Mục tiêu: mRS 0-2 tại 90 ngày
        - Tiêu chí: Pre-stroke mRS thường ≤1 (một số nghiên cứu ≤2)
        - NNT = 3-5 để có thêm 1 người đạt mRS 0-2
        
        **3. Decompressive Craniectomy (Mở hộp sọ giảm áp):**
        - Giảm tử vong nhưng có thể tăng mRS 4-5
        - Cần thảo luận với gia đình: Sống với khuyết tật nặng vs tử vong
        - Tuổi <60, GCS >8: Tiên lượng tốt hơn
        
        **4. Quyết định DNR/Comfort Care:**
        - Dự đoán mRS ≥5: Có thể cân nhắc comfort care
        - Nhưng KHÔNG nên quyết định quá sớm (đợi ít nhất 72h)
        - Cân nhắc ý muốn bệnh nhân, gia đình
        
        **5. Chỉ định phục hồi chức năng:**
        - mRS 2-4: Hưởng lợi nhiều nhất từ rehab
        - mRS 5: Rehab để phòng biến chứng
        - mRS 0-1: Có thể rehab ngoại trú
        """)
    
    with st.expander("⚠️ Những Sai Lầm Thường Gặp"):
        st.markdown("""
        **1. Đánh giá dựa trên tiềm năng thay vì thực tế:**
        - ❌ SAI: "Bệnh nhân CÓ THỂ tự tắm nếu cố gắng" → mRS 2
        - ✅ ĐÚNG: "Bệnh nhân THỰC TẾ cần giúp đỡ tắm" → mRS 3 hoặc 4
        
        **2. Nhầm lẫn giữa sử dụng dụng cụ vs cần người giúp:**
        - Dùng gậy đi lại → Vẫn "đi lại độc lập" → mRS 0-3
        - Cần người nâng đỡ đi lại → "Không đi lại độc lập" → mRS 4-5
        
        **3. Đánh giá quá sớm:**
        - mRS dao động nhiều trong 1-2 tuần đầu
        - Nên đánh giá tại thời điểm ổn định (ví dụ: khi xuất viện, 3 tháng)
        
        **4. Bỏ qua pre-stroke mRS:**
        - Bệnh nhân đã mRS 3 trước đột quỵ → Sau đột quỵ vẫn mRS 3 → Không tệ đi
        - Quan trọng so sánh với baseline
        
        **5. Nhầm giữa mRS 3 và 4:**
        - **Câu hỏi then chốt:** "Đi lại có cần người nâng đỡ không?"
        - Nếu CẦN → mRS 4
        - Nếu KHÔNG CẦN (dù dùng gậy) → mRS 3
        
        **6. Đánh giá không khách quan:**
        - Cần hỏi cụ thể, quan sát thực tế
        - Nếu có thể, dùng structured interview (câu hỏi chuẩn)
        - Hỏi gia đình/người chăm sóc để xác nhận
        """)
    
    # Footer
    st.markdown("---")
    st.caption("📚 Based on: Rankin 1957, van Swieten et al. 1988")
    st.caption("⚠️ Most commonly used outcome measure in stroke trials")
    st.caption("🎯 Good outcome = mRS 0-2 (functional independence)")

