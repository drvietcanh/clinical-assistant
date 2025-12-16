"""
Carbon Monoxide Poisoning Protocol
Hyperbaric oxygen therapy guidelines
Life-threatening hypoxia from CO binding to hemoglobin
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Carbon Monoxide Poisoning Protocol"""
    st.subheader("💨 Ngộ Độc Carbon Monoxide (CO)")
    st.caption("Hyperbaric oxygen therapy guidelines - CO poisoning management")
    
    st.error("""
    **⚠️ NGỘ ĐỘC CO = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - CO có ái lực với hemoglobin cao gấp 200-250 lần O2
    - Tạo carboxyhemoglobin (COHb) → Giảm vận chuyển O2
    - Gây thiếu oxy mô, đặc biệt là não và tim
    
    **Nguồn phổ biến:**
    - Khói cháy
    - Lò sưởi, bếp gas
    - Xe máy, ô tô (garage kín)
    - Hút thuốc lá
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá Nguy cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        exposure_duration = st.number_input(
            "**Thời gian phơi nhiễm (phút):**",
            min_value=0,
            max_value=1440,
            value=0,
            step=5,
            help="Thời gian tiếp xúc với CO"
        )
        
        co_level = st.number_input(
            "**Nồng độ CO trong môi trường (ppm):**",
            min_value=0,
            max_value=10000,
            value=0,
            step=10,
            help="Nồng độ CO trong không khí (ppm)"
        )
        
        has_carboxyhemoglobin = st.checkbox("Có kết quả COHb", value=False)
    
    with col2:
        if has_carboxyhemoglobin:
            cohb_level = st.number_input(
                "**Nồng độ COHb (%):**",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                step=0.1,
                help="Nồng độ carboxyhemoglobin (%)"
            )
            
            if cohb_level > 0:
                if cohb_level >= 25:
                    st.error(f"""
                    🚨 **NGUY CƠ RẤT CAO** - COHb: {cohb_level:.1f}%
                    
                    - Cần điều trị oxy cao áp ngay
                    - Nguy cơ tổn thương thần kinh
                    """)
                elif cohb_level >= 15:
                    st.warning(f"""
                    ⚠️ **NGUY CƠ CAO** - COHb: {cohb_level:.1f}%
                    
                    - Cần điều trị oxy 100%
                    - Cân nhắc oxy cao áp
                    """)
                elif cohb_level >= 10:
                    st.warning(f"""
                    ⚠️ **NGUY CƠ TRUNG BÌNH** - COHb: {cohb_level:.1f}%
                    
                    - Cần điều trị oxy 100%
                    - Theo dõi triệu chứng
                    """)
                else:
                    st.success(f"""
                    ✅ **NGUY CƠ THẤP** - COHb: {cohb_level:.1f}%
                    
                    - Điều trị oxy nếu có triệu chứng
                    """)
        
        if co_level > 0:
            st.info(f"""
            **Nồng độ CO:** {co_level} ppm
            
            **Đánh giá:**
            - **An toàn:** <50 ppm
            - **Nguy hiểm:** 50-200 ppm
            - **Rất nguy hiểm:** >200 ppm
            - **Gây tử vong:** >1200 ppm
            """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL PRESENTATION ==========
    st.markdown("### 🔍 Triệu chứng Lâm sàng")
    
    st.markdown("""
    **Triệu chứng sớm:**
    - Đau đầu (phổ biến nhất)
    - Chóng mặt, mệt mỏi
    - Buồn nôn, nôn
    - Khó thở
    - Đau ngực
    
    **Triệu chứng nặng:**
    - Rối loạn ý thức
    - Co giật
    - Hôn mê
    - Rối loạn nhịp tim
    - Suy hô hấp
    
    **Triệu chứng muộn (2-40 ngày sau):**
    - Rối loạn nhận thức
    - Rối loạn vận động
    - Rối loạn cảm giác
    - Parkinsonism
    - Sa sút trí tuệ
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: DIAGNOSIS ==========
    st.markdown("### 📋 Chẩn đoán")
    
    st.warning("""
    **Chẩn đoán:**
    - **Lâm sàng:** Tiền sử phơi nhiễm + Triệu chứng
    - **COHb level:** Xác định chẩn đoán
    - **ABG:** PaO2 có thể bình thường (do O2 hòa tan)
    - **Lactate:** Có thể tăng (thiếu oxy mô)
    
    **Lưu ý:**
    - COHb level có thể giảm nhanh sau khi rời môi trường CO
    - Triệu chứng có thể không tương quan với COHb level
    - Cần điều trị dựa trên triệu chứng, không chỉ dựa vào COHb
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác đồ Điều trị")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Rất nặng (Critical)"],
        key="co_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_protocol()
    elif "Trung bình" in severity:
        render_moderate_protocol()
    elif "Nặng" in severity:
        render_severe_protocol()
    else:
        render_critical_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 5: OXYGEN THERAPY ==========
    st.markdown("### 💨 Điều trị Oxy")
    
    st.info("""
    **Oxy 100% qua mask không thở lại:**
    - **Mục đích:** Giảm thời gian bán hủy COHb
    - **Thời gian bán hủy:** 
      - Không khí: 4-6 giờ
      - Oxy 100%: 60-90 phút
      - Oxy cao áp (2.5-3 ATA): 20-30 phút
    
    **Chỉ định oxy 100%:**
    - Tất cả bệnh nhân ngộ độc CO
    - Cho đến khi COHb <5% hoặc không có triệu chứng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: HYPERBARIC OXYGEN ==========
    st.markdown("### 🏥 Oxy Cao Áp (Hyperbaric Oxygen - HBO)")
    
    st.error("""
    **Chỉ định oxy cao áp:**
    
    **Tuyệt đối:**
    - COHb >25%
    - Rối loạn ý thức (bất kỳ mức độ)
    - Co giật
    - Hôn mê
    - Rối loạn thần kinh khu trú
    - Đau ngực
    - Rối loạn nhịp tim
    
    **Tương đối:**
    - COHb >15% ở phụ nữ có thai
    - COHb >15% ở trẻ em
    - COHb >15% với triệu chứng kéo dài
    - Tiền sử bệnh tim mạch
    
    **Chống chỉ định:**
    - Tràn khí màng phổi không điều trị
    - Bệnh phổi tắc nghẽn nặng
    - Sốt cao không kiểm soát
    """)
    
    st.markdown("""
    **Phác đồ oxy cao áp:**
    - **Áp suất:** 2.5-3.0 ATA
    - **Thời gian:** 90-120 phút
    - **Số lần:** 1-3 lần tùy đáp ứng
    
    **Lợi ích:**
    - Giảm nhanh COHb
    - Giảm nguy cơ tổn thương thần kinh muộn
    - Cải thiện triệu chứng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Đặc biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Phụ nữ có thai:**
        - COHb của mẹ = COHb của thai nhi
        - Thai nhi nhạy cảm hơn với thiếu oxy
        - Chỉ định HBO ở COHb >15%
        - Theo dõi thai nhi chặt chẽ
        
        **Trẻ em:**
        - Nhạy cảm hơn với CO
        - Chỉ định HBO ở COHb >15%
        - Cần điều trị tích cực
        """)
    
    with col2:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ tổn thương thần kinh cao hơn
        - Bệnh lý kèm theo (tim, phổi)
        - Cần điều trị tích cực
        
        **Bệnh tim mạch:**
        - Nguy cơ rối loạn nhịp tim
        - Cần theo dõi ECG
        - Chỉ định HBO ở COHb >15%
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Trong quá trình điều trị:**
    
    **Xét nghiệm:**
    - **COHb:** Mỗi 2-4 giờ cho đến khi <5%
    - **ABG:** Nếu có triệu chứng nặng
    - **Lactate:** Nếu nghi ngờ thiếu oxy mô
    - **ECG:** Nếu có triệu chứng tim
    
    **Triệu chứng:**
    - Mức độ ý thức
    - Triệu chứng thần kinh
    - Triệu chứng tim
    - Triệu chứng hô hấp
    
    **Theo dõi muộn:**
    - Đánh giá nhận thức sau 2-4 tuần
    - Phát hiện tổn thương thần kinh muộn
    - Điều trị nếu có triệu chứng
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("carbon_monoxide_poisoning"))


def render_mild_protocol():
    """Mild CO poisoning"""
    st.success("## ⚠️ MILD CO POISONING")
    
    st.markdown("""
    **Đặc điểm:**
    - COHb: 10-15%
    - Triệu chứng nhẹ: Đau đầu, chóng mặt
    - Không có rối loạn ý thức
    
    **Điều trị:**
    1. **Oxy 100%:** Qua mask không thở lại
    2. **Theo dõi:** COHb mỗi 4 giờ
    3. **Xuất viện:** Khi COHb <5% và không có triệu chứng
    
    **Theo dõi:**
    - Nếu triệu chứng cải thiện → Có thể xuất viện sau 4-6 giờ
    - Nếu triệu chứng không cải thiện → Điều trị lâu hơn
    """)


def render_moderate_protocol():
    """Moderate CO poisoning"""
    st.warning("## 🚨 MODERATE CO POISONING")
    
    st.markdown("""
    **Đặc điểm:**
    - COHb: 15-25%
    - Triệu chứng: Đau đầu nặng, buồn nôn, khó thở
    - Có thể có rối loạn ý thức nhẹ
    
    **Điều trị:**
    1. **Oxy 100%:** Qua mask không thở lại
    2. **Cân nhắc HBO:** Nếu có triệu chứng nặng hoặc không cải thiện
    3. **Theo dõi:** COHb mỗi 2-4 giờ
    4. **Đánh giá thần kinh:** Định kỳ
    
    **Mục tiêu:**
    - COHb <5%
    - Cải thiện triệu chứng
    - Không có tổn thương thần kinh
    """)


def render_severe_protocol():
    """Severe CO poisoning"""
    st.error("## 🚨🚨 SEVERE CO POISONING - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - COHb: >25%
    - Rối loạn ý thức
    - Có thể có co giật
    - Có thể có rối loạn nhịp tim
    
    **Điều trị ngay lập tức:**
    1. **ABC:** Đảm bảo đường thở, thở, tuần hoàn
    2. **Oxy 100%:** Qua mask hoặc đặt nội khí quản
    3. **HBO:** Chỉ định ngay lập tức
    4. **Theo dõi:** COHb mỗi 2 giờ
    
    **ICU Monitoring:**
    - Continuous monitoring
    - ABG mỗi 2-4 giờ
    - COHb mỗi 2 giờ
    - ECG monitoring
    - Theo dõi thần kinh
    
    **HBO:**
    - Bắt đầu càng sớm càng tốt
    - 1-3 lần tùy đáp ứng
    """)


def render_critical_protocol():
    """Critical CO poisoning"""
    st.error("## 🚨🚨🚨 CRITICAL CO POISONING - EMERGENCY HBO")
    
    st.markdown("""
    **Đặc điểm:**
    - COHb: >25%
    - Hôn mê
    - Co giật
    - Suy hô hấp
    - Rối loạn nhịp tim nặng
    
    **Điều trị khẩn cấp:**
    1. **ABC:** Ngay lập tức
    2. **Đặt nội khí quản:** Nếu cần
    3. **Oxy 100%:** Trong khi chờ HBO
    4. **HBO:** NGAY LẬP TỨC
       - Không chờ điều trị nội khoa
       - HBO là điều trị chính
    5. **Điều trị hỗ trợ:** Chống co giật, điều chỉnh nhịp tim
    
    **HBO:**
    - **Áp suất:** 2.5-3.0 ATA
    - **Thời gian:** 90-120 phút
    - **Số lần:** 2-3 lần trong 24 giờ đầu
    
    **Tiên lượng:**
    - Tỷ lệ tử vong cao nếu không điều trị
    - Nguy cơ tổn thương thần kinh muộn
    - Cần điều trị tích cực ngay lập tức
    """)

