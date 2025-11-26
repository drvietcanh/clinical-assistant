"""
SIRS - Systemic Inflammatory Response Syndrome Calculator
Hội chứng đáp ứng viêm toàn thân
"""

import streamlit as st


def calculate_sirs(temp_abnormal, hr_high, rr_high_pco2_low, wbc_abnormal):
    """
    Tính số tiêu chuẩn SIRS
    
    Parameters: Mỗi tiêu chuẩn = 1 nếu có, 0 nếu không
    - temp_abnormal: Nhiệt độ < 36°C hoặc > 38°C
    - hr_high: Nhịp tim > 90 lần/phút
    - rr_high_pco2_low: Nhịp thở > 20 hoặc PaCO₂ < 32 mmHg
    - wbc_abnormal: WBC bất thường
    
    Returns:
    - dict với số tiêu chuẩn SIRS và interpretation
    """
    total = temp_abnormal + hr_high + rr_high_pco2_low + wbc_abnormal
    
    # Phân loại
    if total < 2:
        status = "Không SIRS"
        interpretation = "< 2 tiêu chuẩn - không đáp ứng tiêu chuẩn SIRS"
        color = "green"
        recommendation = "Theo dõi lâm sàng thường quy"
    elif total == 2:
        status = "SIRS"
        interpretation = "≥ 2 tiêu chuẩn - Hội chứng đáp ứng viêm toàn thân"
        color = "orange"
        recommendation = "Tìm nguyên nhân, xét nghiệm thêm nếu cần"
    elif total == 3:
        status = "SIRS"
        interpretation = "≥ 2 tiêu chuẩn - SIRS rõ ràng"
        color = "orange"
        recommendation = "Đánh giá nhiễm trùng, xem xét nuôi cấy"
    else:  # 4
        status = "SIRS (4/4 tiêu chuẩn)"
        interpretation = "Tất cả 4 tiêu chuẩn - SIRS nặng"
        color = "red"
        recommendation = "Nghi ngờ nhiễm trùng nặng/sepsis, xử trí tích cực"
    
    return {
        "total_criteria": total,
        "status": status,
        "interpretation": interpretation,
        "color": color,
        "recommendation": recommendation
    }


def render():
    """Render SIRS calculator interface"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #EF4444;'>🔥 SIRS - Systemic Inflammatory Response Syndrome</h2>
    <p style='text-align: center;'><em>Hội chứng đáp ứng viêm toàn thân</em></p>
    """, unsafe_allow_html=True)
    
    # Thông tin về SIRS
    with st.expander("ℹ️ Giới thiệu về SIRS"):
        st.markdown("""
        **SIRS (Systemic Inflammatory Response Syndrome)** là phản ứng viêm toàn thân của cơ thể 
        trước các tổn thương khác nhau (nhiễm trùng, chấn thương, bỏng, viêm tụy...).
        
        **Định nghĩa:**
        - SIRS = Có **≥ 2 trong 4 tiêu chuẩn**
        - Không nhất thiết do nhiễm trùng
        
        **Tiến triển:**
        - SIRS → **Sepsis** (nếu do nhiễm trùng)
        - Sepsis → **Septic shock** → **Tử vong**
        
        **Lưu ý quan trọng:**
        - SIRS là khái niệm CŨ (từ năm 1992)
        - Hiện nay dùng **qSOFA và SOFA** để đánh giá sepsis
        - SIRS vẫn có giá trị trong một số tình huống
        
        **Giá trị:**
        - Đơn giản, dễ nhớ
        - Sàng lọc nhanh tình trạng viêm toàn thân
        - Độ nhạy cao nhưng độ đặc hiệu thấp
        
        **Giới hạn:**
        - Quá nhạy - nhiều dương tính giả
        - Không dự đoán tốt tiên lượng
        - Đã bị thay thế bởi qSOFA/SOFA trong sepsis
        """)
    
    st.markdown("---")
    
    # Input form
    st.subheader("📝 Đánh giá 4 Tiêu Chuẩn SIRS")
    
    st.markdown("""
    <div style='background-color: #FEF3C7; padding: 15px; border-radius: 10px; border-left: 4px solid #F59E0B;'>
        <p style='margin: 0;'><strong>🎯 SIRS = ≥ 2 trong 4 tiêu chuẩn sau:</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ Nhiệt độ cơ thể")
        
        temp = st.number_input(
            "Nhiệt độ (°C)",
            min_value=32.0,
            max_value=42.0,
            value=37.0,
            step=0.1,
            help="Nhiệt độ trung tâm"
        )
        
        temp_abnormal = 1 if (temp < 36.0 or temp > 38.0) else 0
        
        if temp_abnormal:
            st.error(f"✅ Bất thường: {temp}°C (< 36 hoặc > 38°C)")
        else:
            st.success(f"Bình thường: {temp}°C")
        
        st.markdown("### 2️⃣ Nhịp tim")
        
        hr = st.number_input(
            "Nhịp tim (lần/phút)",
            min_value=30,
            max_value=200,
            value=80,
            step=1,
            help="Heart rate"
        )
        
        hr_high = 1 if hr > 90 else 0
        
        if hr_high:
            st.error(f"✅ Nhanh: {hr} lần/phút (> 90)")
        else:
            st.success(f"Bình thường: {hr} lần/phút")
    
    with col2:
        st.markdown("### 3️⃣ Hô hấp")
        
        assessment_method = st.radio(
            "Chọn cách đánh giá:",
            options=["Nhịp thở", "PaCO₂"],
            horizontal=True,
            help="Chọn nhịp thở hoặc PaCO₂"
        )
        
        if assessment_method == "Nhịp thở":
            rr = st.number_input(
                "Nhịp thở (lần/phút)",
                min_value=5,
                max_value=60,
                value=16,
                step=1,
                help="Respiratory rate"
            )
            
            rr_high_pco2_low = 1 if rr > 20 else 0
            
            if rr_high_pco2_low:
                st.error(f"✅ Nhanh: {rr} lần/phút (> 20)")
            else:
                st.success(f"Bình thường: {rr} lần/phút")
        else:
            paco2 = st.number_input(
                "PaCO₂ (mmHg)",
                min_value=10.0,
                max_value=100.0,
                value=40.0,
                step=0.5,
                format="%.1f",
                help="Áp lực CO₂ động mạch"
            )
            
            rr_high_pco2_low = 1 if paco2 < 32 else 0
            
            if rr_high_pco2_low:
                st.error(f"✅ Thấp: {paco2} mmHg (< 32)")
            else:
                st.success(f"Bình thường: {paco2} mmHg")
        
        st.markdown("### 4️⃣ Bạch cầu (WBC)")
        
        wbc = st.number_input(
            "WBC (×10³/µL hoặc ×10⁹/L)",
            min_value=0.0,
            max_value=50.0,
            value=8.0,
            step=0.1,
            help="White blood cell count"
        )
        
        bands = st.number_input(
            "% Băng/Bands (nếu có)",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            help="Phần trăm bạch cầu băng"
        )
        
        wbc_abnormal = 1 if (wbc < 4.0 or wbc > 12.0 or bands > 10) else 0
        
        if wbc_abnormal:
            if wbc < 4.0:
                st.error(f"✅ Thấp: {wbc} ×10³/µL (< 4)")
            elif wbc > 12.0:
                st.error(f"✅ Cao: {wbc} ×10³/µL (> 12)")
            elif bands > 10:
                st.error(f"✅ Bands cao: {bands}% (> 10%)")
        else:
            st.success(f"Bình thường: WBC {wbc}, Bands {bands}%")
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔬 Đánh giá SIRS", type="primary", use_container_width=True):
        result = calculate_sirs(temp_abnormal, hr_high, rr_high_pco2_low, wbc_abnormal)
        
        # Display result
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
                {result['total_criteria']}/4 tiêu chuẩn SIRS
            </h2>
            <p style='text-align: center; font-size: 1.2em; margin-top: 10px;'>
                {result['status']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Criteria breakdown
        st.markdown("### ✅ Tiêu chuẩn đáp ứng:")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("🌡️ Nhiệt độ", "Có" if temp_abnormal else "Không", 
                     delta=None if not temp_abnormal else f"{temp}°C")
        
        with col2:
            st.metric("💓 Nhịp tim", "Có" if hr_high else "Không",
                     delta=None if not hr_high else f"{hr}/phút")
        
        with col3:
            st.metric("🫁 Hô hấp", "Có" if rr_high_pco2_low else "Không")
        
        with col4:
            st.metric("⚪ WBC", "Có" if wbc_abnormal else "Không",
                     delta=None if not wbc_abnormal else f"{wbc}K")
        
        st.markdown("---")
        
        # Interpretation
        st.markdown(f"""
        <div style='background-color: {score_color}22; padding: 20px; border-radius: 10px; border: 2px solid {score_color};'>
            <h3 style='color: {score_color}; margin-top: 0;'>📋 Giải thích</h3>
            <p style='font-size: 1.1em; margin: 10px 0;'>{result['interpretation']}</p>
            <p style='font-size: 1.2em; color: {score_color}; font-weight: bold; margin: 10px 0;'>
                💡 {result['recommendation']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Next steps
        st.markdown("---")
        st.markdown("### 🔍 Hành động tiếp theo")
        
        if result["total_criteria"] >= 2:
            st.warning("""
            ⚠️ **Có SIRS - Cần đánh giá thêm:**
            
            1. **Tìm nguyên nhân:**
               - Nhiễm trùng (sepsis)
               - Chấn thương, phẫu thuật
               - Bỏng
               - Viêm tụy
               - Thuyên tắc phổi
               - Nhồi máu cơ tim
            
            2. **Xét nghiệm cần làm:**
               - **Nếu nghi sepsis:**
                 - Nuôi cấy máu, nước tiểu, đờm
                 - Procalcitonin, CRP
                 - Lactate
                 - Đánh giá qSOFA/SOFA
               - Xét nghiệm theo nguyên nhân nghi ngờ
            
            3. **Điều Trị:**
               - Điều trị nguyên nhân
               - Nếu sepsis → Surviving Sepsis Campaign:
                 - Kháng sinh trong 1 giờ
                 - Truyền dịch hồi sức
                 - Theo dõi lactate
                 - Vasopressor nếu cần
            
            4. **Theo Dõi:**
               - Dấu hiệu sinh tồn thường xuyên
               - Đánh giá lại qSOFA/SOFA
               - Theo dõi chức năng các cơ quan
            """)
        else:
            st.success("""
            ✅ **Không đủ tiêu chuẩn SIRS**
            
            - Theo dõi lâm sàng thường quy
            - Nếu có triệu chứng, tìm nguyên nhân cụ thể
            - Đánh giá lại nếu tình trạng thay đổi
            """)
        
        # SIRS criteria table
        with st.expander("📋 Bảng tiêu chuẩn SIRS chi tiết"):
            st.markdown("""
            | Tiêu chuẩn | Định nghĩa |
            |:-----------|:-----------|
            | **Nhiệt độ** | < 36°C hoặc > 38°C (< 96.8°F hoặc > 100.4°F) |
            | **Nhịp tim** | > 90 lần/phút |
            | **Hô hấp** | Nhịp thở > 20/phút **HOẶC** PaCO₂ < 32 mmHg |
            | **Bạch cầu** | < 4,000/µL **HOẶC** > 12,000/µL **HOẶC** > 10% bands |
            
            **Chẩn đoán SIRS:** ≥ 2 trong 4 tiêu chuẩn trên
            """)
        
        # SIRS vs Sepsis
        with st.expander("🔄 SIRS, Sepsis và tiến triển"):
            st.markdown("""
            ### Định nghĩa (Sepsis-1 & 2, cũ):
            
            **SIRS:** Đáp ứng viêm toàn thân
            - ≥ 2 tiêu chuẩn SIRS
            - Có thể do nhiều nguyên nhân (không chỉ nhiễm trùng)
            
            **Sepsis:** SIRS + Nhiễm trùng đã xác định hoặc nghi ngờ
            
            **Sepsis nặng:** Sepsis + Suy cơ quan hoặc hạ huyết áp
            
            **Sốc nhiễm trùng:** Sepsis + Hạ huyết áp dai dẳng dù truyền dịch đầy đủ
            
            ---
            
            ### Định nghĩa MỚI (Sepsis-3, 2016):
            
            **Sepsis:** Nhiễm trùng + Suy cơ quan (SOFA ≥ 2)
            - Không còn dùng SIRS
            - Dùng qSOFA để sàng lọc
            
            **Sốc nhiễm trùng:** 
            - Sepsis + Cần vasopressor (MAP ≥ 65) + Lactate > 2 mmol/L
            
            ---
            
            ### So sánh:
            
            | Khái niệm | Cũ (Sepsis-1/2) | Mới (Sepsis-3) |
            |:----------|:----------------|:---------------|
            | Sàng lọc | SIRS | qSOFA |
            | Đánh giá mức độ | SIRS/Sepsis/Sepsis nặng/Shock | Sepsis/Septic shock |
            | Tiêu chuẩn suy cơ quan | Lâm sàng | SOFA score |
            
            **Lưu ý:**
            - SIRS vẫn được dùng trong một số tình huống
            - Sepsis-3 (2016) là tiêu chuẩn hiện tại
            - qSOFA/SOFA thay thế SIRS trong đánh giá sepsis
            """)
        
        # Causes of SIRS
        with st.expander("🔍 Nguyên nhân SIRS (không phải nhiễm trùng)"):
            st.markdown("""
            ### Nguyên nhân không nhiễm trùng:
            
            **Chấn thương:**
            - Đa chấn thương
            - Bỏng diện rộng
            - Chấn thương sọ não
            
            **Viêm:**
            - Viêm tụy cấp
            - Viêm mạch (vasculitis)
            - Bệnh tự miễn
            
            **Thiếu máu cục bộ/Nhồi máu:**
            - Nhồi máu cơ tim
            - Đột quỵ
            - Thiếu máu ruột
            
            **Khác:**
            - Thuyên tắc phổi
            - Phản ứng truyền máu
            - Tổn thương tái tưới máu
            - Phẫu thuật lớn
            - Hội chứng giải phóng cytokine (CAR-T)
            - Suy thượng thận cấp
            
            **Lưu ý:** 
            - SIRS không nhất thiết = nhiễm trùng
            - Cần đánh giá lâm sàng và xét nghiệm để tìm nguyên nhân
            - Nhiễm trùng là nguyên nhân thường gặp nhất
            """)
        
        # References
        with st.expander("📚 Tài liệu tham khảo"):
            st.markdown("""
            1. **Bone RC, Balk RA, Cerra FB, et al.** Definitions for sepsis and organ failure and 
               guidelines for the use of innovative therapies in sepsis. The ACCP/SCCM Consensus Conference Committee. 
               Chest. 1992;101(6):1644-55. *(Sepsis-1)*
            
            2. **Levy MM, Fink MP, Marshall JC, et al.** 2001 SCCM/ESICM/ACCP/ATS/SIS International 
               Sepsis Definitions Conference. Crit Care Med. 2003;31(4):1250-6. *(Sepsis-2)*
            
            3. **Singer M, Deutschman CS, Seymour CW, et al.** The Third International Consensus 
               Definitions for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-10. *(Sepsis-3 - Hiện tại)*
            
            4. **Seymour CW, Liu VX, Iwashyna TJ, et al.** Assessment of Clinical Criteria for Sepsis: 
               For the Third International Consensus Definitions for Sepsis and Septic Shock (Sepsis-3). 
               JAMA. 2016;315(8):762-74.
            
            5. **Rhodes A, Evans LE, Alhazzani W, et al.** Surviving Sepsis Campaign: 
               International Guidelines for Management of Sepsis and Septic Shock: 2016. 
               Intensive Care Med. 2017;43(3):304-377.
            """)
    
    # Quick guide
    st.markdown("---")
    st.info("""
    💡 **Điểm quan trọng:**
    
    1. **SIRS là khái niệm CŨ** - Hiện nay dùng qSOFA/SOFA cho sepsis
    
    2. **SIRS không = Sepsis** - Có thể do nhiều nguyên nhân khác
    
    3. **Độ nhạy cao, độ đặc hiệu thấp** - Nhiều dương tính giả
    
    4. **Khi có SIRS:** Tìm nguyên nhân, đặc biệt đánh giá nhiễm trùng
    
    5. **Sepsis-3 (2016):** Dùng qSOFA sàng lọc và SOFA để đánh giá suy cơ quan
    
    6. **Hành động nhanh:** Nếu nghi sepsis → "Sepsis Six" trong 1 giờ:
       - Oxy
       - Nuôi cấy
       - Kháng sinh
       - Truyền dịch
       - Đo lactate
       - Đo nước tiểu
    """)


if __name__ == "__main__":
    render()

