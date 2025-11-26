"""
Barthel Index
Thang điểm đánh giá chức năng hoạt động hàng ngày (ADL)
"""

import streamlit as st


def render():
    """Barthel Index Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🛠️ Barthel Index</h2>
    <p style='text-align: center;'><em>Thang điểm đánh giá chức năng hoạt động hàng ngày (ADL)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Barthel Index** là thang điểm đánh giá khả năng thực hiện các hoạt động sống hàng ngày (Activities of Daily Living - ADL).
        
        **Chỉ Định:**
        - Đánh giá chức năng sau đột quỵ
        - Đánh giá chức năng ở bệnh nhân cao tuổi
        - Theo dõi tiến triển phục hồi chức năng
        - Đánh giá nhu cầu chăm sóc
        
        **10 Hoạt động (tổng điểm 0-100):**
        1. Đi đại tiện
        2. Đi tiểu tiện
        3. Tự chăm sóc cá nhân
        4. Đi lại
        5. Lên xuống cầu thang
        6. Tắm rửa
        7. Mặc quần áo
        8. Kiểm soát đại tiện
        9. Kiểm soát tiểu tiện
        10. Ăn uống
        
        **Mức độ phụ thuộc:**
        - **0-20:** Phụ thuộc hoàn toàn
        - **21-60:** Phụ thuộc nặng
        - **61-90:** Phụ thuộc vừa
        - **91-99:** Phụ thuộc nhẹ
        - **100:** Độc lập hoàn toàn
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá")
    
    # 1. Đi đại tiện
    st.markdown("### 1️⃣ Đi đại tiện")
    bowel = st.radio(
        "Khả năng đi đại tiện:",
        [
            "0 - Không thể đi đại tiện hoặc cần thụt tháo",
            "5 - Thỉnh thoảng cần hỗ trợ (thụt tháo, thuốc nhuận tràng)",
            "10 - Tự đi đại tiện độc lập"
        ],
        key="barthel_bowel"
    )
    bowel_score = int(bowel.split(" - ")[0])
    
    # 2. Đi tiểu tiện
    st.markdown("### 2️⃣ Đi tiểu tiện")
    bladder = st.radio(
        "Khả năng đi tiểu tiện:",
        [
            "0 - Không kiểm soát hoặc cần đặt ống thông tiểu",
            "5 - Thỉnh thoảng không kiểm soát (≤ 1 lần/ngày)",
            "10 - Tự kiểm soát hoàn toàn"
        ],
        key="barthel_bladder"
    )
    bladder_score = int(bladder.split(" - ")[0])
    
    # 3. Tự chăm sóc cá nhân
    st.markdown("### 3️⃣ Tự chăm sóc Cá Nhân")
    grooming = st.radio(
        "Khả năng tự chăm sóc (rửa mặt, chải đầu, đánh răng, cạo râu):",
        [
            "0 - Cần hỗ trợ",
            "5 - Tự làm được (dụng cụ trong tầm với)"
        ],
        key="barthel_grooming"
    )
    grooming_score = int(grooming.split(" - ")[0])
    
    # 4. Đi lại
    st.markdown("### 4️⃣ Đi lại")
    mobility = st.radio(
        "Khả năng đi lại (trong phòng, hành lang):",
        [
            "0 - Không thể đi lại hoặc cần 2 người hỗ trợ",
            "5 - Cần 1 người hỗ trợ hoặc dụng cụ hỗ trợ",
            "10 - Tự đi lại độc lập (có thể dùng dụng cụ hỗ trợ)"
        ],
        key="barthel_mobility"
    )
    mobility_score = int(mobility.split(" - ")[0])
    
    # 5. Lên xuống cầu thang
    st.markdown("### 5️⃣ Lên xuống cầu thang")
    stairs = st.radio(
        "Khả năng lên xuống cầu thang:",
        [
            "0 - Không thể",
            "5 - Cần hỗ trợ hoặc giám sát",
            "10 - Tự lên xuống độc lập"
        ],
        key="barthel_stairs"
    )
    stairs_score = int(stairs.split(" - ")[0])
    
    # 6. Tắm rửa
    st.markdown("### 6️⃣ Tắm rửa")
    bathing = st.radio(
        "Khả năng tắm rửa:",
        [
            "0 - Cần hỗ trợ",
            "5 - Tự tắm được (có thể cần hỗ trợ vào/ra bồn tắm)"
        ],
        key="barthel_bathing"
    )
    bathing_score = int(bathing.split(" - ")[0])
    
    # 7. Mặc quần áo
    st.markdown("### 7️⃣ Mặc quần áo")
    dressing = st.radio(
        "Khả năng mặc quần áo:",
        [
            "0 - Cần hỗ trợ hoàn toàn",
            "5 - Cần hỗ trợ một phần (cúc, khóa kéo, giày)",
            "10 - Tự mặc quần áo độc lập"
        ],
        key="barthel_dressing"
    )
    dressing_score = int(dressing.split(" - ")[0])
    
    # 8. Kiểm soát đại tiện
    st.markdown("### 8️⃣ Kiểm soát đại tiện")
    bowel_control = st.radio(
        "Kiểm soát đại tiện:",
        [
            "0 - Không kiểm soát hoặc cần thụt tháo",
            "5 - Thỉnh thoảng không kiểm soát (≤ 1 lần/tuần)",
            "10 - Tự kiểm soát hoàn toàn"
        ],
        key="barthel_bowel_control"
    )
    bowel_control_score = int(bowel_control.split(" - ")[0])
    
    # 9. Kiểm soát tiểu tiện
    st.markdown("### 9️⃣ Kiểm soát tiểu tiện")
    bladder_control = st.radio(
        "Kiểm soát tiểu tiện:",
        [
            "0 - Không kiểm soát hoặc cần đặt ống thông tiểu",
            "5 - Thỉnh thoảng không kiểm soát (≤ 1 lần/ngày)",
            "10 - Tự kiểm soát hoàn toàn"
        ],
        key="barthel_bladder_control"
    )
    bladder_control_score = int(bladder_control.split(" - ")[0])
    
    # 10. Ăn uống
    st.markdown("### 🔟 Ăn uống")
    feeding = st.radio(
        "Khả năng ăn uống:",
        [
            "0 - Cần hỗ trợ hoàn toàn",
            "5 - Cần hỗ trợ một phần (cắt thức ăn, bôi bơ...)",
            "10 - Tự ăn uống độc lập"
        ],
        key="barthel_feeding"
    )
    feeding_score = int(feeding.split(" - ")[0])
    
    st.markdown("---")
    
    if st.button("📊 Tính điểm Barthel", type="primary", use_container_width=True):
        total_score = (bowel_score + bladder_score + grooming_score + mobility_score + 
                      stairs_score + bathing_score + dressing_score + bowel_control_score + 
                      bladder_control_score + feeding_score)
        
        st.markdown("## 📊 Kết quả")
        
        # Interpret dependency level
        if total_score <= 20:
            dependency = "Phụ thuộc hoàn toàn"
            color = "#ef4444"
            icon = "🚨"
            interpretation = "Cần hỗ trợ hoàn toàn trong mọi hoạt động"
        elif total_score <= 60:
            dependency = "Phụ thuộc nặng"
            color = "#f59e0b"
            icon = "⚠️"
            interpretation = "Cần hỗ trợ nhiều trong hầu hết hoạt động"
        elif total_score <= 90:
            dependency = "Phụ thuộc vừa"
            color = "#fbbf24"
            icon = "💡"
            interpretation = "Cần hỗ trợ một phần trong một số hoạt động"
        elif total_score < 100:
            dependency = "Phụ thuộc nhẹ"
            color = "#3b82f6"
            icon = "👍"
            interpretation = "Hầu như độc lập, chỉ cần hỗ trợ nhẹ"
        else:
            dependency = "Độc lập hoàn toàn"
            color = "#10b981"
            icon = "✅"
            interpretation = "Tự thực hiện tất cả hoạt động độc lập"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} Barthel Index = {total_score}/100
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {dependency}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Breakdown
        st.markdown("### 📋 Chi tiết điểm số:")
        st.markdown(f"""
        - **Đi đại tiện:** {bowel_score}/10
        - **Đi tiểu tiện:** {bladder_score}/10
        - **Tự chăm sóc cá nhân:** {grooming_score}/5
        - **Đi lại:** {mobility_score}/10
        - **Lên xuống cầu thang:** {stairs_score}/10
        - **Tắm rửa:** {bathing_score}/5
        - **Mặc quần áo:** {dressing_score}/10
        - **Kiểm soát đại tiện:** {bowel_control_score}/10
        - **Kiểm soát tiểu tiện:** {bladder_control_score}/10
        - **Ăn uống:** {feeding_score}/10
        
        **Tổng:** {total_score}/100
        """)
        
        # Care recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến nghị chăm sóc")
        
        if total_score <= 20:
            st.error("""
            **🚨 Phụ Thuộc Hoàn Toàn (Barthel 0-20):**
            
            **Nhu cầu chăm sóc:**
            - Cần hỗ trợ hoàn toàn trong mọi hoạt động
            - Cần người chăm sóc 24/7
            - Cân nhắc chăm sóc tại nhà với hỗ trợ hoặc chăm sóc tại cơ sở chuyên biệt
            
            **Can thiệp:**
            - Phục hồi chức năng tích cực
            - Hỗ trợ ADL hoàn toàn
            - Phòng ngừa biến chứng (loét tì đè, nhiễm trùng...)
            """)
        elif total_score <= 60:
            st.warning("""
            **⚠️ Phụ Thuộc Nặng (Barthel 21-60):**
            
            **Nhu cầu chăm sóc:**
            - Cần hỗ trợ nhiều trong hầu hết hoạt động
            - Cần người chăm sóc thường xuyên
            
            **Can thiệp:**
            - Phục hồi chức năng tích cực
            - Hỗ trợ ADL nhiều
            - Tập luyện các kỹ năng cơ bản
            """)
        elif total_score <= 90:
            st.info("""
            **💡 Phụ Thuộc Vừa (Barthel 61-90):**
            
            **Nhu cầu chăm sóc:**
            - Cần hỗ trợ một phần trong một số hoạt động
            - Có thể sống độc lập với hỗ trợ định kỳ
            
            **Can thiệp:**
            - Phục hồi chức năng
            - Hỗ trợ ADL một phần
            - Tập luyện độc lập
            """)
        elif total_score < 100:
            st.success("""
            **👍 Phụ Thuộc Nhẹ (Barthel 91-99):**
            
            **Nhu cầu chăm sóc:**
            - Hầu như độc lập
            - Chỉ cần hỗ trợ nhẹ trong một số hoạt động
            
            **Can thiệp:**
            - Tiếp tục phục hồi chức năng
            - Hỗ trợ tối thiểu
            - Khuyến khích độc lập
            """)
        else:
            st.success("""
            **✅ Độc Lập Hoàn Toàn (Barthel 100):**
            
            - Tự thực hiện tất cả hoạt động độc lập
            - Không cần hỗ trợ
            - Tiếp tục duy trì chức năng
            """)
        
        # Comparison with mRS
        with st.expander("🔄 So sánh Với mRS"):
            st.markdown("""
            **Barthel Index** và **mRS (Modified Rankin Scale)** đều đánh giá chức năng sau đột quỵ:
            
            | Barthel Index | mRS | Diễn giải |
            |--------------|-----|-----------|
            | 100 | 0 | Không có triệu chứng |
            | 91-99 | 1 | Không có khuyết tật đáng kể |
            | 61-90 | 2 | Khuyết tật nhẹ |
            | 21-60 | 3-4 | Khuyết tật vừa đến nặng |
            | 0-20 | 5 | Khuyết tật nặng |
            
            **Ưu điểm Barthel:**
            - Chi tiết hơn, đánh giá từng hoạt động
            - Phù hợp cho phục hồi chức năng
            - Theo dõi tiến triển tốt hơn
            
            **Ưu điểm mRS:**
            - Đơn giản, nhanh chóng
            - Phù hợp cho nghiên cứu
            - Tiêu chuẩn quốc tế
            """)
        
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            1. **Quan sát và hỏi bệnh nhân:**
               - Quan sát bệnh nhân thực hiện các hoạt động
               - Hỏi bệnh nhân về khả năng thực hiện
               - Hỏi người chăm sóc nếu bệnh nhân không thể trả lời
            
            2. **Đánh giá thực tế:**
               - Dựa trên khả năng thực tế, không phải khả năng lý thuyết
               - Đánh giá trong môi trường thực tế (nhà, bệnh viện...)
            
            3. **Ghi nhận:**
               - Ghi nhận điểm số cho từng hoạt động
               - Tính tổng điểm
               - Đánh giá mức độ phụ thuộc
            
            ### 📋 Khi nào đánh giá:
            - Sau đột quỵ: Khi vào viện, khi xuất viện, 3 tháng, 6 tháng, 1 năm
            - Ở bệnh nhân cao tuổi: Khi vào viện, định kỳ
            - Theo dõi phục hồi chức năng: Mỗi tuần hoặc mỗi 2 tuần
            - Đánh giá nhu cầu chăm sóc: Khi lập kế hoạch chăm sóc
            
            ### ⚠️ Lưu ý:
            - Đánh giá dựa trên khả năng thực tế, không phải khả năng lý thuyết
            - Cân nhắc môi trường (nhà, bệnh viện, cơ sở chăm sóc...)
            - Đánh giá lại định kỳ để theo dõi tiến triển
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Mahoney FI, Barthel DW.** Functional Evaluation: The Barthel Index. 
               *Md State Med J.* 1965;14:61-65.
            
            2. **Collin C, Wade DT, Davies S, Horne V.** The Barthel ADL Index: a reliability study. 
               *Int Disabil Stud.* 1988;10(2):61-63.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Barthel 0-20:** Phụ thuộc hoàn toàn → Cần hỗ trợ 24/7
    2. **Barthel 21-60:** Phụ thuộc nặng → Cần hỗ trợ nhiều
    3. **Barthel 61-90:** Phụ thuộc vừa → Cần hỗ trợ một phần
    4. **Barthel 91-99:** Phụ thuộc nhẹ → Hầu như độc lập
    5. **Barthel 100:** Độc lập hoàn toàn
    6. **Sử dụng:** Đánh giá chức năng, theo dõi phục hồi, lập kế hoạch chăm sóc
    """)

