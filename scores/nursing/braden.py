"""
Braden Scale
Thang điểm đánh giá nguy cơ loét tì đè
"""

import streamlit as st


def render():
    """Braden Scale Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🛏️ Braden Scale</h2>
    <p style='text-align: center;'><em>Thang điểm đánh giá nguy cơ loét tì đè</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Braden Scale** là thang điểm tiêu chuẩn để đánh giá nguy cơ loét tì đè (pressure ulcer).
        
        **Chỉ Định:**
        - Tất cả bệnh nhân nội trú
        - Bệnh nhân nằm liệt giường
        - Bệnh nhân hạn chế vận động
        - Đánh giá khi vào viện và định kỳ
        
        **6 Tiêu chí (tổng điểm 6-23):**
        1. **Sensory Perception (Cảm giác)** - 1-4 điểm
        2. **Moisture (Độ ẩm)** - 1-4 điểm
        3. **Activity (Hoạt động)** - 1-4 điểm
        4. **Mobility (Di chuyển)** - 1-4 điểm
        5. **Nutrition (Dinh dưỡng)** - 1-4 điểm
        6. **Friction & Shear (Ma sát)** - 1-3 điểm
        
        **Nguy cơ:**
        - **≤ 12:** Nguy cơ cao
        - **13-14:** Nguy cơ trung bình
        - **15-18:** Nguy cơ thấp
        - **≥ 19:** Rất ít nguy cơ
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá")
    
    # 1. Sensory Perception
    st.markdown("### 1️⃣ Sensory Perception (Cảm giác)")
    sensory = st.radio(
        "Khả năng phản ứng với cảm giác khó chịu liên quan đến áp lực:",
        [
            "4 - Không bị suy giảm: Phản ứng bình thường với cảm giác đau/khó chịu",
            "3 - Suy giảm nhẹ: Phản ứng với lời nói, nhưng không phải lúc nào cũng thể hiện sự khó chịu hoặc đau",
            "2 - Suy giảm vừa: Chỉ phản ứng với kích thích đau, không thể giao tiếp bằng lời nói",
            "1 - Suy giảm hoàn toàn: Không phản ứng với kích thích đau (hôn mê, liệt)"
        ],
        key="braden_sensory"
    )
    sensory_score = int(sensory[0])
    
    # 2. Moisture
    st.markdown("### 2️⃣ Moisture (Độ ẩm)")
    moisture = st.radio(
        "Mức độ tiếp xúc với độ ẩm:",
        [
            "4 - Hiếm khi ẩm ướt: Da thường khô, thay quần áo/băng gạc khi cần",
            "3 - Thỉnh thoảng ẩm ướt: Da ẩm ướt khoảng 1 lần/ngày",
            "2 - Thường xuyên ẩm ướt: Da ẩm ướt ít nhất 1 lần/ngày",
            "1 - Luôn ẩm ướt: Da luôn ẩm ướt do mồ hôi, nước tiểu, phân"
        ],
        key="braden_moisture"
    )
    moisture_score = int(moisture[0])
    
    # 3. Activity
    st.markdown("### 3️⃣ Activity (Hoạt động)")
    activity = st.radio(
        "Mức độ hoạt động thể chất:",
        [
            "4 - Đi lại: Đi lại ít nhất 2 lần/ngày",
            "3 - Đi lại hạn chế: Đi lại trong phòng, nhưng khoảng cách rất ngắn",
            "2 - Ngồi ghế: Khả năng chịu trọng lượng tốt, nhưng không thể đi lại",
            "1 - Nằm liệt giường: Nằm trên giường hoặc ghế"
        ],
        key="braden_activity"
    )
    activity_score = int(activity[0])
    
    # 4. Mobility
    st.markdown("### 4️⃣ Mobility (Di chuyển)")
    mobility = st.radio(
        "Khả năng thay đổi và kiểm soát vị trí cơ thể:",
        [
            "4 - Hoàn toàn: Thay đổi vị trí thường xuyên và độc lập",
            "3 - Hơi hạn chế: Thay đổi vị trí thường xuyên nhưng cần hỗ trợ nhẹ",
            "2 - Rất hạn chế: Thay đổi vị trí thỉnh thoảng, nhưng cần hỗ trợ đáng kể",
            "1 - Bất động: Không thể thay đổi vị trí mà không có hỗ trợ"
        ],
        key="braden_mobility"
    )
    mobility_score = int(mobility[0])
    
    # 5. Nutrition
    st.markdown("### 5️⃣ Nutrition (Dinh dưỡng)")
    nutrition = st.radio(
        "Tình trạng dinh dưỡng:",
        [
            "4 - Tốt: Ăn uống đầy đủ, không cần bổ sung",
            "3 - Đầy đủ: Ăn uống đầy đủ, đôi khi từ chối bữa ăn, bổ sung protein",
            "2 - Có thể không đủ: Ăn < 50% bữa ăn, bổ sung dinh dưỡng, truyền dịch",
            "1 - Rất kém: Ăn rất ít, không ăn uống, truyền dịch hoặc nuôi ăn qua ống"
        ],
        key="braden_nutrition"
    )
    nutrition_score = int(nutrition[0])
    
    # 6. Friction & Shear
    st.markdown("### 6️⃣ Friction & Shear (Ma sát)")
    friction = st.radio(
        "Ma sát và lực cắt:",
        [
            "3 - Không có vấn đề: Di chuyển trên giường/ghế độc lập, có đủ sức mạnh để nâng mình lên",
            "2 - Có vấn đề tiềm ẩn: Di chuyển yếu, cần hỗ trợ nhẹ khi di chuyển",
            "1 - Có vấn đề: Cần hỗ trợ đáng kể để di chuyển, da trượt trên giường/ghế"
        ],
        key="braden_friction"
    )
    friction_score = int(friction[0])
    
    st.markdown("---")
    
    if st.button("📊 Tính điểm Braden", type="primary", use_container_width=True):
        total_score = sensory_score + moisture_score + activity_score + mobility_score + nutrition_score + friction_score
        
        st.markdown("## 📊 Kết quả")
        
        # Interpret risk
        if total_score <= 12:
            risk_level = "Nguy cơ cao"
            color = "#ef4444"
            icon = "🚨"
            interpretation = "Nguy cơ loét tì đè cao, cần can thiệp ngay"
        elif total_score <= 14:
            risk_level = "Nguy cơ trung bình"
            color = "#f59e0b"
            icon = "⚠️"
            interpretation = "Nguy cơ loét tì đè trung bình, cần theo dõi"
        elif total_score <= 18:
            risk_level = "Nguy cơ thấp"
            color = "#fbbf24"
            icon = "💡"
            interpretation = "Nguy cơ loét tì đè thấp, tiếp tục phòng ngừa"
        else:
            risk_level = "Rất ít nguy cơ"
            color = "#10b981"
            icon = "✅"
            interpretation = "Rất ít nguy cơ loét tì đè"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} Braden Score = {total_score}/23
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {risk_level}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Breakdown
        st.markdown("### 📋 Chi tiết điểm số:")
        st.markdown(f"""
        - **Sensory Perception (Cảm giác):** {sensory_score}/4
        - **Moisture (Độ ẩm):** {moisture_score}/4
        - **Activity (Hoạt động):** {activity_score}/4
        - **Mobility (Di chuyển):** {mobility_score}/4
        - **Nutrition (Dinh dưỡng):** {nutrition_score}/4
        - **Friction & Shear (Ma sát):** {friction_score}/3
        
        **Tổng:** {total_score}/23
        """)
        
        # Prevention recommendations
        st.markdown("---")
        st.markdown("### 🛡️ Khuyến nghị phòng ngừa")
        
        if total_score <= 12:
            st.error("""
            **🚨 Nguy cơ cao (Braden ≤ 12) - Can thiệp ngay:**
            
            **Biện pháp phòng ngừa:**
            
            1. **Giảm áp lực:**
               - Thay đổi tư thế mỗi 2 giờ (nếu có thể)
               - Sử dụng đệm giảm áp lực (air mattress, gel mattress)
               - Nâng cao gót chân khỏi giường
               - Tránh nằm trực tiếp lên vết thương
            
            2. **Giảm ma sát:**
               - Nâng bệnh nhân, không kéo lê
               - Sử dụng ga trải giường mềm mại
               - Bảo vệ khuỷu tay, gót chân bằng băng dính hoặc gối
            
            3. **Chăm sóc da:**
               - Kiểm tra da mỗi 8 giờ
               - Giữ da khô ráo, sạch sẽ
               - Sử dụng kem dưỡng ẩm
               - Tránh massage vùng da đỏ
            
            4. **Dinh dưỡng:**
               - Đảm bảo đủ protein (1.2-1.5 g/kg/ngày)
               - Bổ sung vitamin C, kẽm nếu thiếu
               - Đánh giá lại tình trạng dinh dưỡng
            
            5. **Theo Dõi:**
               - Đánh giá lại Braden mỗi 24 giờ
               - Ghi nhận vị trí da đỏ, vết loét
               - Báo bác sĩ nếu có dấu hiệu loét
            """)
        elif total_score <= 14:
            st.warning("""
            **⚠️ Nguy cơ trung bình (Braden 13-14) - Theo dõi:**
            
            **Biện pháp phòng ngừa:**
            
            1. **Giảm áp lực:**
               - Thay đổi tư thế mỗi 4 giờ
               - Sử dụng đệm giảm áp lực
               - Nâng cao gót chân
            
            2. **Chăm sóc da:**
               - Kiểm tra da mỗi 12 giờ
               - Giữ da khô ráo, sạch sẽ
            
            3. **Dinh dưỡng:**
               - Đảm bảo đủ protein
               - Đánh giá lại tình trạng dinh dưỡng
            
            4. **Theo Dõi:**
               - Đánh giá lại Braden mỗi 48 giờ
            """)
        elif total_score <= 18:
            st.info("""
            **💡 Nguy cơ thấp (Braden 15-18) - Phòng ngừa cơ bản:**
            
            **Biện pháp:**
            
            1. **Giảm áp lực:**
               - Thay đổi tư thế định kỳ
               - Khuyến khích vận động
            
            2. **Chăm sóc da:**
               - Kiểm tra da hàng ngày
               - Giữ da sạch sẽ, khô ráo
            
            3. **Theo Dõi:**
               - Đánh giá lại Braden mỗi 72 giờ hoặc khi có thay đổi
            """)
        else:
            st.success("""
            **✅ Rất ít nguy cơ (Braden ≥ 19):**
            
            - Tiếp tục chăm sóc da cơ bản
            - Đánh giá lại khi có thay đổi tình trạng
            """)
        
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            1. **Đánh giá khi vào viện:**
               - Tất cả bệnh nhân nội trú
               - Bệnh nhân nằm liệt giường
               - Bệnh nhân hạn chế vận động
            
            2. **Đánh giá định kỳ:**
               - Nguy cơ cao (≤ 12): Mỗi 24 giờ
               - Nguy cơ trung bình (13-14): Mỗi 48 giờ
               - Nguy cơ thấp (15-18): Mỗi 72 giờ
               - Rất ít nguy cơ (≥ 19): Khi có thay đổi
            
            3. **Đánh giá lại khi:**
               - Tình trạng bệnh nhân thay đổi
               - Sau phẫu thuật
               - Sau khi chuyển khoa
               - Khi có dấu hiệu loét
            
            ### 📋 Vị Trí Loét Tì Đè Thường gặp:
            - Gót chân
            - Mông, xương cùng
            - Khuỷu tay
            - Vai, xương bả vai
            - Đầu (nếu nằm lâu)
            - Tai (nếu nằm nghiêng)
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Bergstrom N, Braden BJ, Laguzza A, Holman V.** The Braden Scale for Predicting Pressure Sore Risk. 
               *Nurs Res.* 1987;36(4):205-210.
            
            2. **National Pressure Ulcer Advisory Panel, European Pressure Ulcer Advisory Panel, Pan Pacific Pressure Injury Alliance.** Prevention and Treatment of Pressure Ulcers: Clinical Practice Guideline. 
               *Osborne Park, Australia: Cambridge Media; 2014.*
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Braden ≤ 12:** Nguy cơ cao → Can thiệp ngay
    2. **Braden 13-14:** Nguy cơ trung bình → Theo dõi
    3. **Braden 15-18:** Nguy cơ thấp → Phòng ngừa cơ bản
    4. **Braden ≥ 19:** Rất ít nguy cơ
    5. **Đánh giá lại:** Tùy theo mức độ nguy cơ (24-72 giờ)
    6. **Mục Tiêu:** Phòng ngừa loét tì đè, không để xảy ra loét
    """)

