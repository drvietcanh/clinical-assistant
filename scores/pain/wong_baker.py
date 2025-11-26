"""
Wong-Baker Faces Rating Scale
Thang điểm khuôn mặt đánh giá đau (trẻ em và người lớn)
"""

import streamlit as st


def render():
    """Wong-Baker Faces Pain Scale Calculator"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>😊 Wong-Baker Faces Rating Scale</h2>
    <p style='text-align: center;'><em>Thang điểm khuôn mặt đánh giá đau (0-10)</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **Wong-Baker Faces Rating Scale** sử dụng hình ảnh khuôn mặt biểu cảm để đánh giá đau.
        
        **Ưu điểm:**
        - Dễ hiểu, không cần đọc
        - Phù hợp cho trẻ em (3-7 tuổi)
        - Phù hợp cho người lớn không biết chữ, rối loạn ngôn ngữ
        - Phù hợp cho bệnh nhân già, sa sút trí tuệ
        
        **Chỉ Định:**
        - Trẻ em 3-7 tuổi
        - Người lớn không biết chữ
        - Bệnh nhân rối loạn ngôn ngữ
        - Bệnh nhân sa sút trí tuệ
        
        **Thang điểm: 0-10**
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá đau")
    
    # Display faces
    st.markdown("### 😊 Chọn Khuôn Mặt Mô Tả Mức Độ Đau")
    
    # Create visual faces representation
    faces_data = [
        (0, "😊", "Không đau", "Vui vẻ, cười"),
        (2, "🙂", "Đau nhẹ", "Hơi buồn"),
        (4, "😐", "Đau vừa", "Buồn"),
        (6, "😣", "Đau nhiều", "Rất buồn"),
        (8, "😰", "Đau rất nhiều", "Khóc"),
        (10, "😭", "Đau dữ dội nhất", "Khóc to")
    ]
    
    # Display faces in grid
    cols = st.columns(3)
    selected_face = None
    
    for idx, (score, emoji, label, desc) in enumerate(faces_data):
        with cols[idx % 3]:
            if st.button(
                f"{emoji}\n\n**{score}**\n{label}\n\n{desc}",
                key=f"face_{score}",
                use_container_width=True
            ):
                selected_face = score
    
    # Alternative: slider
    st.markdown("---")
    st.markdown("### Hoặc chọn bằng thanh trượt:")
    pain_level = st.slider(
        "Mức độ đau (0-10):",
        min_value=0,
        max_value=10,
        value=0 if selected_face is None else selected_face,
        step=1,
        help="0 = Không đau, 10 = Đau dữ dội nhất"
    )
    
    # Use slider value if no face button was clicked
    if selected_face is None:
        selected_face = pain_level
    
    # Display selected face
    st.markdown("---")
    st.markdown("### 📊 Khuôn Mặt Đã Chọn")
    
    # Find matching face
    matching_face = next((f for f in faces_data if f[0] == selected_face), faces_data[0])
    face_emoji = matching_face[1]
    face_label = matching_face[2]
    face_desc = matching_face[3]
    
    st.markdown(f"""
    <div style='text-align: center; padding: 30px; background: #f9fafb; border-radius: 15px; margin: 20px 0;'>
        <div style='font-size: 80px; margin-bottom: 20px;'>{face_emoji}</div>
        <h2 style='margin: 0;'>Wong-Baker = {selected_face}/10</h2>
        <p style='font-size: 1.2em; margin-top: 10px;'>{face_label}</p>
        <p style='color: #6b7280;'>{face_desc}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("📊 Đánh giá", type="primary", use_container_width=True):
        st.markdown("## 📊 Kết quả")
        
        # Interpret pain level
        if selected_face == 0:
            severity = "Không đau"
            color = "#10b981"
            icon = "✅"
            interpretation = "Bệnh nhân không có đau"
        elif selected_face <= 3:
            severity = "Đau nhẹ"
            color = "#fbbf24"
            icon = "😐"
            interpretation = "Đau nhẹ, có thể chịu đựng được"
        elif selected_face <= 6:
            severity = "Đau vừa"
            color = "#f59e0b"
            icon = "😣"
            interpretation = "Đau vừa, ảnh hưởng đến hoạt động"
        else:
            severity = "Đau nặng"
            color = "#ef4444"
            icon = "😰"
            interpretation = "Đau nặng, ảnh hưởng nghiêm trọng"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} Wong-Baker = {selected_face}/10
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {severity}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Treatment recommendations (similar to NRS)
        st.markdown("---")
        st.markdown("### 💊 Khuyến nghị điều trị")
        
        if selected_face == 0:
            st.success("**✅ Không cần điều trị giảm đau**")
        elif selected_face <= 3:
            st.info("""
            **💊 Đau nhẹ (Wong-Baker 1-3):**
            - Paracetamol hoặc NSAID
            - Đánh giá lại sau 30-60 phút
            """)
        elif selected_face <= 6:
            st.warning("""
            **💊 Đau vừa (Wong-Baker 4-6):**
            - Opioid yếu (Codeine, Tramadol) + Non-opioid
            - Đánh giá lại sau 30 phút
            """)
        else:
            st.error("""
            **🚨 Đau nặng (Wong-Baker 7-10):**
            - Opioid mạnh (Morphine, Fentanyl) ngay lập tức
            - Đánh giá lại sau 15-30 phút
            """)
        
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            1. **Giải thích cho bệnh nhân/trẻ em:**
               - "Khuôn mặt đầu tiên (0) = Không đau, vui vẻ"
               - "Khuôn mặt cuối cùng (10) = Đau dữ dội nhất, khóc to"
               - "Hãy chọn khuôn mặt mô tả mức độ đau của bạn"
            
            2. **Cho trẻ em:**
               - Chỉ vào từng khuôn mặt và giải thích
               - Hỏi: "Bạn cảm thấy như khuôn mặt nào?"
               - Ghi nhận số tương ứng với khuôn mặt được chọn
            
            3. **Đánh giá đau tại thời điểm:**
               - Đau hiện tại
               - Đau khi nghỉ ngơi
               - Đau khi vận động (nếu có)
            
            ### 📋 Khi nào đánh giá:
            - Khi bệnh nhân/trẻ vào viện
            - Trước và sau điều trị giảm đau
            - Mỗi 4 giờ ở bệnh nhân nội trú
            - Khi bệnh nhân/trẻ than đau
            - Sau phẫu thuật: Mỗi 2-4 giờ trong 24 giờ đầu
            
            ### ⚠️ Lưu ý:
            - Wong-Baker dùng cho trẻ em 3-7 tuổi và người lớn không biết chữ
            - Trẻ < 3 tuổi: Dùng FLACC hoặc NIPS
            - Trẻ > 7 tuổi có thể giao tiếp: Có thể dùng NRS
            - Phù hợp cho bệnh nhân sa sút trí tuệ, rối loạn ngôn ngữ
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Wong DL, Baker CM.** Pain in children: comparison of assessment scales. 
               *Pediatr Nurs.* 1988;14(1):9-17.
            
            2. **Hicks CL, von Baeyer CL, Spafford PA, van Korlaar I, Goodenough B.** The Faces Pain Scale-Revised: toward a common metric in pediatric pain measurement. 
               *Pain.* 2001;93(2):173-183.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **Wong-Baker 0-3:** Đau nhẹ → Non-opioid
    2. **Wong-Baker 4-6:** Đau vừa → Opioid yếu
    3. **Wong-Baker 7-10:** Đau nặng → Opioid mạnh
    4. **Mục tiêu điều trị:** Wong-Baker ≤ 3
    5. **Đánh giá lại:** Sau 15-30 phút (đau nặng) hoặc 30-60 phút (đau nhẹ/vừa)
    """)

