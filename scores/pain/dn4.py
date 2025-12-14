"""
DN4 - Douleur Neuropathique 4
Thang điểm chẩn đoán đau thần kinh
"""

import streamlit as st


def render():
    """DN4 Neuropathic Pain Diagnostic Tool"""
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🧠 DN4 - Douleur Neuropathique 4</h2>
    <p style='text-align: center;'><em>Thang điểm chẩn đoán đau thần kinh</em></p>
    """, unsafe_allow_html=True)
    
    with st.expander("ℹ️ Giới thiệu"):
        st.markdown("""
        **DN4 (Douleur Neuropathique 4)** là công cụ sàng lọc đau thần kinh.
        
        **Chỉ định:**
        - Bệnh nhân có đau mạn tính
        - Nghi ngờ đau thần kinh (đau sau đột quỵ, đái tháo đường, herpes zoster...)
        - Phân biệt đau thần kinh với đau nội tạng/đau cơ xương
        
        **10 Câu hỏi (7 câu hỏi + 3 dấu hiệu lâm sàng):**
        - Mỗi câu trả lời "Có" = 1 điểm
        - Tổng điểm: 0-10
        
        **Chẩn đoán đau thần kinh:** ≥ 4 điểm
        """)
    
    st.markdown("---")
    
    st.subheader("📝 Đánh giá")
    
    st.markdown("### Phần 1: Hỏi Bệnh nhân (7 câu hỏi)")
    
    # Question 1
    q1 = st.checkbox(
        "1. Đau có cảm giác như bỏng rát?",
        key="dn4_q1"
    )
    
    # Question 2
    q2 = st.checkbox(
        "2. Đau có cảm giác như lạnh buốt?",
        key="dn4_q2"
    )
    
    # Question 3
    q3 = st.checkbox(
        "3. Đau có cảm giác như điện giật?",
        key="dn4_q3"
    )
    
    # Question 4
    q4 = st.checkbox(
        "4. Đau có kèm theo cảm giác tê?",
        key="dn4_q4"
    )
    
    # Question 5
    q5 = st.checkbox(
        "5. Đau có kèm theo cảm giác châm chích?",
        key="dn4_q5"
    )
    
    # Question 6
    q6 = st.checkbox(
        "6. Đau có kèm theo cảm giác như kiến bò?",
        key="dn4_q6"
    )
    
    # Question 7
    q7 = st.checkbox(
        "7. Đau có kèm theo cảm giác ngứa?",
        key="dn4_q7"
    )
    
    st.markdown("---")
    
    st.markdown("### Phần 2: Khám Lâm sàng (3 dấu hiệu)")
    
    # Clinical sign 1
    sign1 = st.checkbox(
        "8. Giảm cảm giác khi chạm nhẹ?",
        help="Dùng bông gòn hoặc bàn chải mềm chạm nhẹ vào vùng đau",
        key="dn4_sign1"
    )
    
    # Clinical sign 2
    sign2 = st.checkbox(
        "9. Giảm cảm giác đau khi châm nhẹ?",
        help="Dùng kim châm nhẹ vào vùng đau (không chảy máu)",
        key="dn4_sign2"
    )
    
    # Clinical sign 3
    sign3 = st.checkbox(
        "10. Tăng cảm giác đau khi châm nhẹ?",
        help="Cảm giác đau tăng lên khi châm nhẹ (hyperalgesia)",
        key="dn4_sign3"
    )
    
    st.markdown("---")
    
    if st.button("📊 Tính điểm DN4", type="primary", use_container_width=True):
        # Calculate score
        score = sum([
            q1, q2, q3, q4, q5, q6, q7,  # Questions 1-7
            sign1, sign2, sign3  # Clinical signs 8-10
        ])
        
        st.markdown("## 📊 Kết quả")
        
        # Interpret
        is_neuropathic = score >= 4
        
        if is_neuropathic:
            severity = "Có đau thần kinh"
            color = "#ef4444"
            icon = "🚨"
            interpretation = "Chẩn đoán đau thần kinh (≥ 4 điểm)"
        else:
            severity = "Không có đau thần kinh"
            color = "#10b981"
            icon = "✅"
            interpretation = "Không đủ tiêu chí đau thần kinh (< 4 điểm)"
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}22 0%, {color}44 100%); 
                    padding: 30px; border-radius: 15px; border-left: 5px solid {color}; margin: 20px 0;'>
            <h2 style='color: {color}; margin: 0; text-align: center;'>
                {icon} DN4 = {score}/10
            </h2>
            <p style='text-align: center; font-size: 1.1em; margin-top: 10px;'>
                {severity}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Diễn giải:** {interpretation}")
        
        # Chi tiết
        st.markdown("### 📋 Chi tiết điểm số:")
        st.markdown(f"""
        **Phần 1 - Hỏi bệnh nhân (7 câu):**
        - Bỏng rát: {'✅' if q1 else '❌'}
        - Lạnh buốt: {'✅' if q2 else '❌'}
        - Điện giật: {'✅' if q3 else '❌'}
        - Tê: {'✅' if q4 else '❌'}
        - Châm chích: {'✅' if q5 else '❌'}
        - Kiến bò: {'✅' if q6 else '❌'}
        - Ngứa: {'✅' if q7 else '❌'}
        
        **Phần 2 - Khám lâm sàng (3 dấu hiệu):**
        - Giảm cảm giác chạm: {'✅' if sign1 else '❌'}
        - Giảm cảm giác đau: {'✅' if sign2 else '❌'}
        - Tăng cảm giác đau: {'✅' if sign3 else '❌'}
        
        **Tổng:** {score}/10
        """)
        
        # Treatment recommendations
        st.markdown("---")
        st.markdown("### 💊 Khuyến nghị điều trị")
        
        if is_neuropathic:
            st.error("""
            **🚨 Chẩn đoán Đau Thần Kinh (DN4 ≥ 4)**
            
            **Điều trị:**
            
            **1. Thuốc hàng đầu (First-line):**
            - **Gabapentin:** 300-600 mg/ngày, tăng dần đến 1800-3600 mg/ngày
            - **Pregabalin:** 75-150 mg/ngày, tăng dần đến 300-600 mg/ngày
            - **Amitriptyline:** 10-25 mg/ngày, tăng dần đến 50-150 mg/ngày
            - **Duloxetine:** 30-60 mg/ngày
            
            **2. Thuốc thay thế (Second-line):**
            - **Tramadol:** 50-100 mg mỗi 6-8 giờ
            - **Tapentadol:** 50-100 mg mỗi 6 giờ
            - **Capsaicin cream:** Bôi tại chỗ
            
            **3. Thuốc bổ trợ:**
            - Paracetamol hoặc NSAID (nếu có đau viêm)
            - Opioid mạnh (nếu đau nặng, không đáp ứng)
            
            **4. Điều trị không dùng thuốc:**
            - Vật lý trị liệu
            - Tâm lý trị liệu
            - Kích thích thần kinh (TENS)
            
            **Lưu ý:**
            - Đau thần kinh thường khó điều trị
            - Cần thời gian để thuốc có tác dụng (2-4 tuần)
            - Có thể cần kết hợp nhiều thuốc
            - Theo dõi tác dụng phụ (buồn ngủ, chóng mặt, phù...)
            """)
        else:
            st.info("""
            **✅ Không Đủ Tiêu chí Đau Thần Kinh (DN4 < 4)**
            
            **Có thể là:**
            - Đau nội tạng
            - Đau cơ xương
            - Đau viêm
            
            **Điều trị:**
            - Điều trị theo nguyên nhân
            - Paracetamol, NSAID
            - Opioid nếu cần
            
            **Lưu ý:**
            - Nếu đau không đáp ứng điều trị thông thường
            - Cân nhắc đánh giá lại với DN4
            - Có thể có đau hỗn hợp (đau thần kinh + đau nội tạng)
            """)
        
        with st.expander("📚 Hướng dẫn sử dụng"):
            st.markdown("""
            ### 🎯 Cách đánh giá:
            
            **Phần 1 - Hỏi bệnh nhân:**
            1. Hỏi từng câu hỏi một cách rõ ràng
            2. Giải thích nếu bệnh nhân không hiểu
            3. Ghi nhận "Có" hoặc "Không"
            
            **Phần 2 - Khám lâm sàng:**
            1. **Giảm cảm giác chạm:**
               - Dùng bông gòn hoặc bàn chải mềm
               - Chạm nhẹ vào vùng đau và vùng đối bên
               - So sánh cảm giác
            
            2. **Giảm cảm giác đau:**
               - Dùng kim châm nhẹ (không chảy máu)
               - Châm vào vùng đau và vùng đối bên
               - So sánh cảm giác đau
            
            3. **Tăng cảm giác đau:**
               - Châm nhẹ vào vùng đau
               - Cảm giác đau tăng lên bất thường (hyperalgesia)
            
            ### 📋 Chẩn đoán:
            - **DN4 ≥ 4:** Chẩn đoán đau thần kinh
            - **DN4 < 4:** Không đủ tiêu chí đau thần kinh
            
            ### ⚠️ Lưu ý:
            - DN4 là công cụ sàng lọc, không phải chẩn đoán xác định
            - Cần kết hợp với khám lâm sàng và xét nghiệm
            - Có thể có đau hỗn hợp (đau thần kinh + đau nội tạng)
            - Độ nhạy: ~83%, Độ đặc hiệu: ~90%
            """)
        
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Bouhassira D, Attal N, Alchaar H, et al.** Comparison of pain syndromes associated with nervous or somatic lesions and development of a new neuropathic pain diagnostic questionnaire (DN4). 
               *Pain.* 2005;114(1-2):29-36.
            
            2. **Bouhassira D, Attal N, Fermanian J, et al.** Development and validation of the Neuropathic Pain Symptom Inventory. 
               *Pain.* 2004;108(3):248-257.
            """)
    
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **DN4 ≥ 4:** Chẩn đoán đau thần kinh
    2. **Điều trị:** Gabapentin, Pregabalin, Amitriptyline, Duloxetine
    3. **Độ nhạy:** ~83%, **Độ đặc hiệu:** ~90%
    4. **Lưu ý:** Đau thần kinh thường khó điều trị, cần thời gian
    5. **Có thể kết hợp:** Đau thần kinh + đau nội tạng
    """)

