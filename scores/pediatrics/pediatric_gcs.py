"""
Pediatric GCS - Pediatric Glasgow Coma Scale Calculator
Đánh giá mức độ ý thức ở trẻ em
"""

import streamlit as st


def calculate_pediatric_gcs(eye, verbal, motor, age_group):
    """
    Tính điểm Pediatric GCS
    
    Parameters:
    - eye: Điểm mở mắt (1-4)
    - verbal: Điểm đáp ứng lời nói (1-5)
    - motor: Điểm vận động (1-6)
    - age_group: Nhóm tuổi ("infant" < 2 tuổi, "child" >= 2 tuổi)
    
    Returns:
    - dict với total_score, severity và interpretation
    """
    total = eye + verbal + motor
    
    # Phân loại mức độ
    if total >= 13:
        severity = "Nhẹ (Mild)"
        interpretation = "Tình trạng ổn định, tiên lượng tốt"
        color = "green"
    elif total >= 9:
        severity = "Trung bình (Moderate)"
        interpretation = "Cần theo dõi chặt chẽ, có nguy cơ suy giảm"
        color = "orange"
    else:  # 3-8
        severity = "Nặng (Severe)"
        interpretation = "⚠️ Nguy cơ cao, cần hồi sức tích cực"
        color = "red"
    
    return {
        "total_score": total,
        "eye_score": eye,
        "verbal_score": verbal,
        "motor_score": motor,
        "severity": severity,
        "interpretation": interpretation,
        "color": color
    }


def render():
    """Render Pediatric GCS calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #FF6B9D;'>👶 Pediatric GCS - Thang điểm Glasgow cho trẻ em</h2>
    <p style='text-align: center;'><em>Đánh giá mức độ ý thức ở trẻ em và trẻ sơ sinh</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về Pediatric GCS
    with st.expander("ℹ️ Giới thiệu về Pediatric GCS"):
        st.markdown("""
        **Pediatric GCS** là phiên bản điều chỉnh của Glasgow Coma Scale dành cho trẻ em, 
        đặc biệt là trẻ < 2 tuổi chưa phát triển đầy đủ khả năng ngôn ngữ.
        
        **Mục đích:**
        - Đánh giá mức độ ý thức ở trẻ em
        - Theo dõi diễn biến thần kinh
        - Tiên lượng chấn thương sọ não
        
        **Áp dụng:**
        - Chấn thương đầu
        - Rối loạn ý thức bất kỳ nguyên nhân nào
        - Theo dõi sau phẫu thuật thần kinh
        - Đánh giá tình trạng ICU
        
        **Phân loại:**
        - 13-15 điểm: Chấn thương sọ não nhẹ
        - 9-12 điểm: Chấn thương sọ não trung bình
        - 3-8 điểm: Chấn thương sọ não nặng
        
        **Lưu ý:**
        - Đánh giá phản ứng tốt nhất trong mỗi thành phần
        - Nếu có yếu tố gây nhiễu (an thần, tê liệt), cần ghi chú
        - Xu hướng thay đổi quan trọng hơn giá trị tuyệt đối
        """)
    
    st.markdown("---")
    
    # Chọn nhóm tuổi
    st.subheader("📅 Nhóm tuổi")
    age_group = st.radio(
        "Chọn nhóm tuổi của bệnh nhân:",
        options=["infant", "child"],
        format_func=lambda x: "👶 Trẻ sơ sinh / Infant (< 2 tuổi)" if x == "infant" else "🧒 Trẻ em / Child (≥ 2 tuổi)",
        horizontal=True,
        help="Tiêu chí đánh giá khác nhau giữa trẻ < 2 tuổi và ≥ 2 tuổi"
    )
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Đánh giá các thành phần")
    
    # Eye Opening Response
    st.markdown("### 👁️ 1. Phản ứng mở mắt (Eye Opening)")
    
    eye_options = {
        4: "4 - Mở mắt tự nhiên (Spontaneous)",
        3: "3 - Mở mắt khi gọi (To speech/sound)",
        2: "2 - Mở mắt khi kích thích đau (To pain)",
        1: "1 - Không mở mắt (No response)"
    }
    
    eye = st.radio(
        "Chọn phản ứng tốt nhất:",
        options=[4, 3, 2, 1],
        format_func=lambda x: eye_options[x],
        key="pgcs_eye",
        help="Đánh giá phản ứng mở mắt tốt nhất của trẻ"
    )
    
    st.markdown("---")
    
    # Verbal Response (age-specific)
    st.markdown("### 🗣️ 2. Phản ứng lời nói (Verbal Response)")
    
    if age_group == "infant":
        st.info("**Đánh giá cho trẻ < 2 tuổi** (dựa vào tiếng khóc và tương tác)")
        verbal_options = {
            5: "5 - Cười, theo dõi, tương tác bình thường (Coos, babbles)",
            4: "4 - Khóc nhưng dỗ được (Irritable cry, consolable)",
            3: "3 - Khóc khi kích thích đau (Cries to pain)",
            2: "2 - Rên khi kích thích đau (Moans to pain)",
            1: "1 - Không có phản ứng (No response)"
        }
    else:
        st.info("**Đánh giá cho trẻ ≥ 2 tuổi** (dựa vào khả năng ngôn ngữ)")
        verbal_options = {
            5: "5 - Định hướng tốt, nói chuyện bình thường (Oriented, appropriate)",
            4: "4 - Lú lẫn, nói không rõ ràng (Confused, disoriented)",
            3: "3 - Nói từ ngữ không phù hợp (Inappropriate words)",
            2: "2 - Âm thanh không thành lời (Incomprehensible sounds)",
            1: "1 - Không có phản ứng (No response)"
        }
    
    verbal = st.radio(
        "Chọn phản ứng tốt nhất:",
        options=[5, 4, 3, 2, 1],
        format_func=lambda x: verbal_options[x],
        key="pgcs_verbal",
        help="Đánh giá phản ứng lời nói/âm thanh tốt nhất"
    )
    
    st.markdown("---")
    
    # Motor Response (age-specific)
    st.markdown("### 💪 3. Phản ứng vận động (Motor Response)")
    
    if age_group == "infant":
        st.info("**Đánh giá cho trẻ < 2 tuổi** (vận động tự phát và phản xạ)")
        motor_options = {
            6: "6 - Vận động bình thường, tự nhiên (Spontaneous/purposeful)",
            5: "5 - Rút tay khi chạm (Localizes/withdraws to touch)",
            4: "4 - Rút tay khi kích thích đau (Withdraws to pain)",
            3: "3 - Tư thế gấp bất thường (Abnormal flexion)",
            2: "2 - Tư thế duỗi (Extension to pain)",
            1: "1 - Không có phản ứng (No response)"
        }
    else:
        st.info("**Đánh giá cho trẻ ≥ 2 tuổi** (tương tự người lớn)")
        motor_options = {
            6: "6 - Làm theo lệnh (Obeys commands)",
            5: "5 - Định vị kích thích đau (Localizes to pain)",
            4: "4 - Rút tay khi đau (Withdraws from pain)",
            3: "3 - Tư thế gấp bất thường (Abnormal flexion - Decorticate)",
            2: "2 - Tư thế duỗi (Extension - Decerebrate)",
            1: "1 - Không có phản ứng (No response)"
        }
    
    motor = st.radio(
        "Chọn phản ứng tốt nhất:",
        options=[6, 5, 4, 3, 2, 1],
        format_func=lambda x: motor_options[x],
        key="pgcs_motor",
        help="Đánh giá phản ứng vận động tốt nhất"
    )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Tính điểm GCS", type="primary", use_container_width=True):
        result = calculate_pediatric_gcs(eye, verbal, motor, age_group)
        
        # Display result
        st.markdown("## 📊 Kết quả đánh giá")
        
        # Score display
        score_color = {
            "green": "#28a745",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }[result["color"]]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {score_color}22 0%, {score_color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {score_color}; margin: 20px 0;'>
            <h2 style='color: {score_color}; margin: 0; text-align: center;'>
                Pediatric GCS: {result['total_score']}/15
            </h2>
            <p style='text-align: center; font-size: 1.2em; margin: 10px 0;'>
                E{result['eye_score']} V{result['verbal_score']} M{result['motor_score']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Component scores
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("👁️ Mở mắt", f"{result['eye_score']}/4")
        
        with col2:
            st.metric("🗣️ Lời nói", f"{result['verbal_score']}/5")
        
        with col3:
            st.metric("💪 Vận động", f"{result['motor_score']}/6")
        
        st.markdown("---")
        
        # Severity and interpretation
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Mức độ: {result['severity']}</h3>
            <p style='font-size: 1.2em; margin: 0;'>{result['interpretation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Clinical guidance
        st.markdown("---")
        st.markdown("### 📋 Hướng dẫn lâm sàng")
        
        if result["total_score"] >= 13:
            st.success("""
            ✅ **Chấn thương sọ não nhẹ (GCS 13-15)**
            
            **Quản lý:**
            - Theo dõi thần kinh thường xuyên (mỗi 2-4h)
            - Đánh giá lại GCS định kỳ
            - Quan sát dấu hiệu tăng áp lực nội sọ
            - Xem xét chụp CT nếu có triệu chứng
            
            **Tiên lượng:**
            - Thường hồi phục hoàn toàn
            - Nguy cơ biến chứng thấp
            - Có thể xuất viện nếu ổn định
            """)
        
        elif result["total_score"] >= 9:
            st.warning("""
            ⚠️ **Chấn thương sọ não trung bình (GCS 9-12)**
            
            **Quản lý:**
            - Theo dõi thần kinh chặt chẽ liên tục
            - Chụp CT sọ não
            - Nhập viện quan sát
            - Cân nhắc đặt NKQ nếu có nguy cơ
            - Theo dõi dấu hiệu suy giảm
            
            **Tiên lượng:**
            - Nguy cơ suy giảm trung bình
            - Cần theo dõi ICU nếu không ổn định
            - Có thể cần can thiệp thần kinh
            """)
        
        else:
            st.error("""
            🆘 **Chấn thương sọ não nặng (GCS ≤ 8)**
            
            **Quản lý KHẨN CẤP:**
            - ⚠️ Cần bảo vệ đường thở NGAY (GCS ≤ 8)
            - Đặt nội khí quản
            - Chuyển ICU ngay lập tức
            - Chụp CT sọ não khẩn cấp
            - Theo dõi áp lực nội sọ
            - Hội chẩn phẫu thuật thần kinh
            
            **Can thiệp hồi sức:**
            - Duy trì oxy hóa tốt (SpO₂ > 95%)
            - Tránh hạ huyết áp
            - Kiểm soát nhiệt độ
            - Điều chỉnh điện giải
            - Cân nhắc giảm áp lực nội sọ
            
            **Tiên lượng:**
            - Nguy cơ tử vong và di chứng cao
            - Cần điều trị tích cực
            """)
        
        # Additional warnings
        if result["motor_score"] <= 3:
            st.error("""
            ⚠️ **Cảnh báo: Tư thế bất thường**
            
            Điểm vận động ≤ 3 (tư thế gấp hoặc duỗi bất thường) là dấu hiệu nghiêm trọng:
            - Tổn thương não nặng
            - Nguy cơ tăng áp lực nội sọ
            - Cần can thiệp khẩn cấp
            - Hội chẩn thần kinh ngay
            """)
        
        # GCS interpretation table
        with st.expander("📊 Bảng phân loại GCS"):
            st.markdown("""
            | Điểm GCS | Mức độ | Tiên lượng |
            |:--------:|:-------|:-----------|
            | 15 | Ý thức bình thường | Tốt |
            | 13-14 | Chấn thương nhẹ | Thường hồi phục tốt |
            | 9-12 | Chấn thương trung bình | Cần theo dõi chặt |
            | 6-8 | Chấn thương nặng | Nguy cơ cao |
            | 4-5 | Rất nặng | Tiên lượng xấu |
            | 3 | Hôn mê sâu | Tiên lượng rất xấu |
            
            **Chỉ định đặt nội khí quản:**
            - GCS ≤ 8
            - Suy giảm nhanh
            - Mất phản xạ bảo vệ đường thở
            - Cần siêu thông khí
            """)
        
        # Component details
        with st.expander("🔍 Chi tiết các thành phần"):
            st.markdown("""
            ### 👁️ Mở mắt (Eye Opening)
            - **4:** Mở mắt tự nhiên, tỉnh táo
            - **3:** Mở mắt khi gọi hoặc có âm thanh lớn
            - **2:** Chỉ mở mắt khi kích thích đau
            - **1:** Không mở mắt dù kích thích
            
            ### 🗣️ Lời nói (Verbal) - < 2 tuổi
            - **5:** Cười, theo dõi, phát âm (coos, babbles) bình thường
            - **4:** Khóc cáu kỉnh nhưng dỗ được
            - **3:** Khóc khi kích thích đau
            - **2:** Rên khi kích thích đau
            - **1:** Không có âm thanh
            
            ### 🗣️ Lời nói (Verbal) - ≥ 2 tuổi
            - **5:** Nói chuyện bình thường, định hướng đúng
            - **4:** Lú lẫn, nói không rõ ràng
            - **3:** Nói từ ngữ không phù hợp ngữ cảnh
            - **2:** Chỉ phát ra âm thanh không thành lời
            - **1:** Không có phản ứng
            
            ### 💪 Vận động (Motor) - < 2 tuổi
            - **6:** Vận động tự nhiên, chơi bình thường
            - **5:** Rút tay khi chạm nhẹ
            - **4:** Rút tay khi kích thích đau
            - **3:** Tư thế gấp bất thường (decorticate)
            - **2:** Tư thế duỗi (decerebrate)
            - **1:** Không có phản ứng
            
            ### 💪 Vận động (Motor) - ≥ 2 tuổi
            - **6:** Làm theo lệnh (vẫy tay, chỉ ngón...)
            - **5:** Định vị được vị trí kích thích đau
            - **4:** Rút tay khỏi kích thích đau
            - **3:** Tư thế gấp bất thường (decorticate)
            - **2:** Tư thế duỗi (decerebrate)
            - **1:** Không có phản ứng
            """)
        
        # Tips for assessment
        with st.expander("💡 Mẹo đánh giá chính xác"):
            st.markdown("""
            ### Nguyên tắc chung:
            1. **Ghi nhận phản ứng TỐT NHẤT** trong mỗi thành phần
            2. **Kích thích đầy đủ** trước khi kết luận "không phản ứng"
            3. **Ghi chú các yếu tố gây nhiễu:**
               - An thần, thuốc giảm đau
               - Tê liệt, chấn thương cột sống
               - Nội khí quản (đánh dấu "T" cho verbal)
               - Phù mí mắt không mở được (đánh dấu "C" cho eye)
            
            ### Kỹ thuật kích thích đau:
            - **Trung ương:** Ấn hốc trên ức, chà xương sườn
            - **Ngoại vi:** Ấn đáy móng tay, bóp cơ thang vai
            - **Tránh:** Kích thích quá mạnh gây tổn thương
            
            ### Đánh giá trẻ nhỏ:
            - Sử dụng đồ chơi, tiếng ồn để thu hút
            - Quan sát tương tác với ba mẹ
            - Đánh giá khi trẻ tỉnh, không đói, không mệt
            - So sánh với trạng thái bình thường của trẻ
            
            ### Theo dõi xu hướng:
            - Suy giảm ≥ 2 điểm: Đánh giá lại ngay
            - Ghi chép định kỳ (mỗi 15-60 phút tùy mức độ)
            - Biểu đồ hóa để nhận ra xu hướng
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Teasdale G, Jennett B.** Assessment of coma and impaired consciousness: 
               a practical scale. Lancet. 1974;2(7872):81-4.
            
            2. **Holmes JF, Palchak MJ, MacFarlane T, Kuppermann N.** Performance of the pediatric 
               Glasgow Coma Scale in children with blunt head trauma. Acad Emerg Med. 2005;12(9):814-9.
            
            3. **Tatman A, Warren A, Williams A, Powell JE, Whitehouse W.** Development of a modified 
               paediatric coma scale in intensive care clinical practice. Arch Dis Child. 1997;77(6):519-21.
            
            4. **Reilly PL, Simpson DA, Sprod R, Thomas L.** Assessing the conscious level in infants 
               and young children: a paediatric version of the Glasgow Coma Scale. Childs Nerv Syst. 1988;4(1):30-3.
            
            5. **Kirkham FJ, Newton CR, Whitehouse W.** Paediatric coma scales. 
               Dev Med Child Neurol. 2008;50(4):267-74.
            """)
    
    # Quick reference
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    - **GCS ≤ 8:** Chỉ định đặt nội khí quản bảo vệ đường thở
    - **Suy giảm GCS:** Dấu hiệu tăng áp lực nội sọ hoặc tổn thương tiến triển
    - **GCS 3:** Điểm thấp nhất có thể, tiên lượng rất xấu
    - **Xu hướng > Giá trị tuyệt đối:** Thay đổi GCS quan trọng hơn giá trị một lần
    - **Ghi chú đầy đủ:** E_V_M_ + các yếu tố gây nhiễu (T, C, an thần...)
    """)


if __name__ == "__main__":
    render()
