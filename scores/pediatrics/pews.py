"""
PEWS - Pediatric Early Warning Score Calculator
Cảnh báo sớm suy giảm trạng thái lâm sàng ở trẻ em
"""

import streamlit as st


def calculate_pews(behavior, cardiovascular, respiratory):
    """
    Tính điểm PEWS
    
    Parameters:
    - behavior: Điểm hành vi (0-3)
    - cardiovascular: Điểm tim mạch (0-3)
    - respiratory: Điểm hô hấp (0-3)
    
    Returns:
    - dict với total_score và interpretation
    """
    total = behavior + cardiovascular + respiratory
    
    # Phân loại mức độ nguy cơ
    if total == 0:
        risk = "Thấp"
        action = "Tiếp tục theo dõi thường quy"
        color = "green"
    elif total <= 2:
        risk = "Thấp - Trung bình"
        action = "Tăng cường theo dõi, thông báo bác sĩ"
        color = "orange"
    elif total <= 4:
        risk = "Trung bình"
        action = "Gọi bác sĩ khám ngay, theo dõi chặt chẽ"
        color = "orange"
    else:  # >= 5
        risk = "Cao"
        action = "⚠️ KHẨN CẤP: Kích hoạt đội cấp cứu nhi khoa ngay"
        color = "red"
    
    return {
        "total_score": total,
        "risk_level": risk,
        "action": action,
        "color": color
    }


def render():
    """Render PEWS calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #FF6B9D;'>👶 PEWS - Pediatric Early Warning Score</h2>
    <p style='text-align: center;'><em>Cảnh báo sớm suy giảm trạng thái lâm sàng ở trẻ em</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về PEWS
    with st.expander("ℹ️ Giới thiệu về PEWS"):
        st.markdown("""
        **PEWS (Pediatric Early Warning Score)** là công cụ sàng lọc để phát hiện sớm trẻ em có nguy cơ 
        suy giảm trạng thái lâm sàng nghiêm trọng.
        
        **Mục đích:**
        - Phát hiện sớm các dấu hiệu cảnh báo suy giảm
        - Kích hoạt can thiệp kịp thời
        - Giảm tỷ lệ biến chứng và tử vong
        
        **Áp dụng:**
        - Trẻ em nhập viện (không áp dụng cho trẻ sơ sinh)
        - Theo dõi định kỳ hoặc khi có thay đổi lâm sàng
        - Đặc biệt hữu ích tại khoa nhi tổng quát
        
        **Lưu ý:**
        - Không thay thế đánh giá lâm sàng
        - Cần kết hợp với kinh nghiệm lâm sàng
        - Khi có thay đổi đột ngột, đánh giá ngay
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Nhập thông tin đánh giá")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🧠 Hành vi")
        behavior = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "0 - Chơi/Hoạt động bình thường",
                1: "1 - Ngủ nhiều",
                2: "2 - Kích thích/Lơ mơ",
                3: "3 - Li bì/Lú lẫn/Co giật"
            }[x],
            key="pews_behavior",
            help="Đánh giá tình trạng ý thức và hành vi của trẻ"
        )
    
    with col2:
        st.markdown("### ❤️ Tim mạch")
        cardiovascular = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "0 - Hồng hào, CTR < 3s",
                1: "1 - Xanh nhạt/Xám, CTR 3-4s",
                2: "2 - Xanh tái, CTR 4-5s",
                3: "3 - Xanh tái nặng, CTR > 5s"
            }[x],
            key="pews_cardio",
            help="CTR = Capillary Refill Time (thời gian hồi màu mao mạch)"
        )
    
    with col3:
        st.markdown("### 🫁 Hô hấp")
        respiratory = st.radio(
            "Chọn mức độ:",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "0 - Không khó thở, SpO₂ > 95%",
                1: "1 - Tăng thông khí (>10 nhịp), SpO₂ > 95%",
                2: "2 - Khó thở + (>20 nhịp/phút), SpO₂ 90-95%",
                3: "3 - Khó thở ++ (>30 nhịp), SpO₂ < 90%"
            }[x],
            key="pews_resp",
            help="Đánh giá công thở và độ bão hòa oxy"
        )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Tính điểm PEWS", type="primary", use_container_width=True):
        result = calculate_pews(behavior, cardiovascular, respiratory)
        
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
                Điểm PEWS: {result['total_score']}
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed breakdown
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("🧠 Hành vi", f"{behavior} điểm")
        
        with col2:
            st.metric("❤️ Tim mạch", f"{cardiovascular} điểm")
        
        with col3:
            st.metric("🫁 Hô hấp", f"{respiratory} điểm")
        
        st.markdown("---")
        
        # Risk level and action
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>🎯 Mức độ nguy cơ: {result['risk_level']}</h3>
            <p style='font-size: 1.1em; margin: 10px 0;'><strong>Hành động khuyến cáo:</strong></p>
            <p style='font-size: 1.2em; color: {score_color}; font-weight: bold;'>{result['action']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Clinical guidance
        st.markdown("---")
        st.markdown("### 📋 Hướng dẫn lâm sàng")
        
        if result["total_score"] == 0:
            st.success("""
            ✅ **Trạng thái ổn định**
            - Tiếp tục theo dõi theo quy trình thường quy
            - Đánh giá lại định kỳ theo chỉ định
            """)
        
        elif result["total_score"] <= 2:
            st.warning("""
            ⚠️ **Cần tăng cường theo dõi**
            - Thông báo bác sĩ điều trị
            - Tăng tần suất theo dõi (mỗi 2-4 giờ)
            - Đánh giá lại sau 1 giờ
            """)
        
        elif result["total_score"] <= 4:
            st.warning("""
            🚨 **Cần can thiệp y tế ngay**
            - Gọi bác sĩ khám ngay lập tức
            - Theo dõi liên tục
            - Chuẩn bị chuyển ICU nếu cần
            - Đánh giá lại mỗi 30 phút
            """)
        
        else:
            st.error("""
            🆘 **TÌNH TRẠNG KHẨN CẤP**
            - Kích hoạt đội cấp cứu nhi khoa NGAY
            - Theo dõi liên tục không gián đoạn
            - Chuẩn bị hồi sức và chuyển ICU
            - Thông báo trưởng khoa/bác sĩ trưởng ca
            - Đánh giá lại liên tục
            """)
        
        # Score interpretation table
        with st.expander("📊 Bảng phân loại điểm PEWS"):
            st.markdown("""
            | Điểm | Mức độ nguy cơ | Hành động |
            |:----:|:--------------|:----------|
            | 0 | Thấp | Theo dõi thường quy |
            | 1-2 | Thấp - Trung bình | Tăng theo dõi, thông báo bác sĩ |
            | 3-4 | Trung bình | Gọi bác sĩ khám ngay, theo dõi chặt |
            | ≥5 | Cao | ⚠️ KHẨN CẤP: Kích hoạt đội cấp cứu |
            
            **Lưu ý quan trọng:**
            - Bất kỳ thành phần nào đạt 3 điểm → Đánh giá y khoa ngay
            - Thay đổi đột ngột → Đánh giá lại ngay lập tức
            - Kết hợp với đánh giá lâm sàng tổng thể
            """)
        
        # Age-specific normal ranges
        with st.expander("👶 Giá trị bình thường theo tuổi"):
            st.markdown("""
            ### Nhịp tim (nhịp/phút)
            | Tuổi | Bình thường | Nhịp nhanh |
            |:-----|:------------|:-----------|
            | < 1 tuổi | 110-160 | > 160 |
            | 1-2 tuổi | 100-150 | > 150 |
            | 2-5 tuổi | 95-140 | > 140 |
            | 5-12 tuổi | 80-120 | > 120 |
            | > 12 tuổi | 60-100 | > 100 |
            
            ### Nhịp thở (lần/phút)
            | Tuổi | Bình thường | Thở nhanh |
            |:-----|:------------|:----------|
            | < 1 tuổi | 30-40 | > 50 |
            | 1-2 tuổi | 25-35 | > 40 |
            | 2-5 tuổi | 25-30 | > 35 |
            | 5-12 tuổi | 20-25 | > 30 |
            | > 12 tuổi | 15-20 | > 25 |
            
            ### Huyết áp tâm thu (mmHg)
            | Tuổi | Thấp | Bình thường |
            |:-----|:------|:------------|
            | < 1 tuổi | < 70 | 70-90 |
            | 1-10 tuổi | < 70+(2×tuổi) | 90-110 |
            | > 10 tuổi | < 90 | 90-120 |
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Monaghan A.** Detecting and managing deterioration in children. 
               Paediatr Nurs. 2005;17(1):32-5.
            
            2. **Duncan H, Hutchison J, Parshuram CS.** The Pediatric Early Warning System score: 
               a severity of illness score to predict urgent medical need in hospitalized children. 
               J Crit Care. 2006;21(3):271-8.
            
            3. **Parshuram CS, Hutchison J, Middaugh K.** Development and initial validation of the 
               Bedside Paediatric Early Warning System score. Crit Care. 2009;13(4):R135.
            
            4. **Chapman SM, Grocott MP, Franck LS.** Systematic review of paediatric alert criteria 
               for identifying hospitalised children at risk of critical deterioration. 
               Intensive Care Med. 2010;36(4):600-11.
            
            **Lưu ý:** Có nhiều phiên bản PEWS khác nhau. Mỗi bệnh viện nên chọn và chuẩn hóa 
            một phiên bản phù hợp với điều kiện và đối tượng bệnh nhân của mình.
            """)
    
    # Quick reference guide
    st.markdown("---")
    with st.expander("📖 Hướng dẫn nhanh đánh giá các thành phần"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🧠 Đánh giá Hành vi
            
            **0 điểm:** Chơi/Tương tác bình thường
            - Tỉnh táo, phản ứng tốt
            - Chơi phù hợp với lứa tuổi
            
            **1 điểm:** Ngủ nhiều
            - Có thể đánh thức được
            - Phản ứng chậm hơn bình thường
            
            **2 điểm:** Kích thích/Lơ mơ
            - Khó đánh thức
            - Kích thích hoặc rất uể oải
            
            **3 điểm:** Li bì/Lú lẫn/Co giật
            - Không phản ứng hoặc phản ứng rất kém
            - Có co giật
            
            ### ❤️ Đánh giá Tim mạch
            
            **CTR (Capillary Refill Time):**
            - Ấn nhẹ vào đầu ngón tay/lòng bàn tay
            - Thả ra và đếm thời gian hồi màu
            - Đánh giá ở nhiệt độ bình thường
            
            **Màu sắc da:**
            - Hồng hào: Bình thường
            - Xanh nhạt/Xám: Tưới máu giảm
            - Xanh tái: Tưới máu kém
            - Xanh tím: Thiếu oxy nghiêm trọng
            """)
        
        with col2:
            st.markdown("""
            ### 🫁 Đánh giá Hô hấp
            
            **Dấu hiệu khó thở:**
            - Phập phồng cánh mũi
            - Co kéo lồng ngực
            - Rên khi thở
            - Thở khò khè
            - Thở bụng
            
            **Đếm nhịp thở:**
            - Đếm trong 1 phút đầy đủ
            - Khi trẻ bình tĩnh (không khóc/ăn)
            - Quan sát chuyển động ngực
            
            **SpO₂:**
            - Đo ở ngón tay/ngón chân
            - Đảm bảo máy bắt sóng tốt
            - Ghi nhận có hay không dùng O₂
            
            ### ⚠️ Dấu hiệu cảnh báo ngay
            
            - Bất kỳ thành phần nào = 3 điểm
            - Thay đổi đột ngột bất kể điểm số
            - Trực giác lâm sàng "có gì đó không ổn"
            - Phụ huynh lo lắng bất thường
            """)
    
    # Clinical pearls
    st.info("""
    💡 **Lưu ý quan trọng:**
    
    1. **PEWS không thay thế đánh giá lâm sàng** - Luôn kết hợp với kinh nghiệm và trực giác lâm sàng
    
    2. **Xu hướng quan trọng hơn giá trị tuyệt đối** - Theo dõi thay đổi theo thời gian
    
    3. **Đánh giá lại thường xuyên** - Đặc biệt sau can thiệp hoặc khi có thay đổi
    
    4. **Không chờ đợi khi nghi ngờ** - Khi có dấu hiệu bất thường, đánh giá ngay
    
    5. **Truyền thông hiệu quả** - Dùng PEWS để truyền đạt rõ ràng mức độ nghiêm trọng
    """)


if __name__ == "__main__":
    render()
