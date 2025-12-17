"""
Cobra Bite Protocol (Rắn Hổ Mang Cắn)
Naja kaouthia / Naja siamensis
Neurotoxic venomous snake in Vietnam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Cobra Bite Protocol"""
    st.subheader("🐍 Rắn Hổ Mang Cắn (Cobra Bite)")
    st.caption("Naja kaouthia / Naja siamensis - Rắn độc thần kinh phổ biến tại Việt Nam")
    
    st.error("""
    **⚠️ RẮN HỔ MANG CẮN = CẤP CỨU Y TẾ KHẨN CẤP**
    
    **Đặc điểm:**
    - Rắn độc thần kinh nguy hiểm
    - Phân bố: Khắp cả nước, đặc biệt đồng bằng, vùng nông thôn
    - Hoạt động: Ban ngày và ban đêm
    - Độc tố: Neurotoxic (gây liệt cơ, suy hô hấp)
    
    **Tỷ lệ tử vong:** 5-10% nếu không điều trị kịp thời
    **Biến chứng:** Liệt cơ, suy hô hấp, ngừng thở
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: IDENTIFICATION ==========
    st.markdown("### 🎯 Nhận dạng rắn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Đặc điểm nhận dạng:**
        - Màu nâu, đen, hoặc vàng
        - Có "mang" khi đe dọa
        - Kích thước: 1-2m
        - Đầu hình tam giác khi bạnh mang
        - Mắt tròn, đồng tử tròn
        """)
    
    with col2:
        st.warning("""
        **Phân loại tại Việt Nam:**
        - Rắn hổ mang Đông Dương (Naja kaouthia)
        - Rắn hổ mang Xiêm (Naja siamensis)
        - Rắn hổ mang đất (Naja atra) - hiếm
        
        **⚠️ Tất cả đều rất độc!**
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        time_since_bite = st.number_input(
            "**Thời gian sau khi bị cắn (giờ):**",
            min_value=0.0,
            max_value=72.0,
            value=0.0,
            step=0.5,
            help="Thời gian từ khi bị cắn đến khi đến viện"
        )
        
        bite_location = st.selectbox(
            "**Vị trí cắn:**",
            ["Tay", "Chân", "Đầu/Cổ", "Thân mình", "Khác"]
        )
        
        respiratory_status = st.selectbox(
            "**Tình trạng hô hấp:**",
            ["Bình thường", "Khó thở nhẹ", "Khó thở nặng", "Ngừng thở"]
        )
    
    with col2:
        if time_since_bite > 0:
            st.info(f"""
            **Thời gian:** {time_since_bite:.1f} giờ sau khi cắn
            
            **Lưu ý:**
            - Triệu chứng xuất hiện: 15 phút - 2 giờ
            - Liệt cơ có thể xảy ra nhanh
            - Cần theo dõi sát hô hấp
            """)
    
    st.markdown("---")
    
    # ========== SECTION 3: SIGNS OF ENVENOMATION ==========
    st.markdown("### 🔍 Dấu hiệu nhiễm độc")
    
    tab1, tab2, tab3 = st.tabs(["Tại chỗ", "Thần kinh", "Toàn thân"])
    
    with tab1:
        st.markdown("""
        **Dấu hiệu tại chỗ:**
        - ✅ Đau tại vết cắn (thường ít đau hơn rắn lục)
        - ✅ Sưng nề nhẹ đến trung bình
        - ✅ Tê bì quanh vết cắn
        - ✅ Hoại tử tại chỗ (ít gặp hơn rắn lục)
        
        **⚠️ Lưu ý:**
        - Dấu hiệu tại chỗ có thể nhẹ
        - Không nên đánh giá mức độ dựa vào dấu hiệu tại chỗ
        """)
    
    with tab2:
        st.markdown("""
        **Dấu hiệu thần kinh (QUAN TRỌNG):**
        
        **Sớm (15 phút - 2 giờ):**
        - ✅ Tê bì quanh vết cắn
        - ✅ Tê bì môi, lưỡi
        - ✅ Nhìn đôi (song thị)
        - ✅ Sụp mi mắt (ptosis)
        - ✅ Nói khó, nuốt khó
        
        **Tiến triển (2-6 giờ):**
        - ✅ Liệt cơ mặt
        - ✅ Liệt cơ nhai
        - ✅ Liệt cơ cổ
        - ✅ Liệt tứ chi
        - ✅ Liệt cơ hô hấp → **SUY HÔ HẤP**
        
        **⚠️ Dấu hiệu nguy hiểm:**
        - Khó thở tăng dần
        - Yếu cơ hô hấp
        - Giảm SpO2
        - Cần thở máy
        """)
    
    with tab3:
        st.markdown("""
        **Dấu hiệu toàn thân:**
        - ✅ Buồn nôn, nôn
        - ✅ Chóng mặt
        - ✅ Yếu mệt
        - ✅ Hạ huyết áp (có thể)
        - ✅ Rối loạn nhịp tim (hiếm)
        
        **Xét nghiệm:**
        - Thường bình thường
        - Có thể tăng CK nếu liệt cơ nặng
        - ABG: Giảm oxy nếu suy hô hấp
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: FIRST AID ==========
    st.markdown("### 🚑 Sơ cứu ban đầu")
    
    st.success("""
    **✅ NÊN LÀM:**
    1. **Bình tĩnh:** Giữ bệnh nhân yên tĩnh
    2. **Bất động chi:** Nẹp chi bị cắn
    3. **Vận chuyển NGAY:** Đưa đến cơ sở y tế gần nhất
    4. **Theo dõi hô hấp:** Quan sát nhịp thở, SpO2 nếu có
    5. **Chuẩn bị:** Có thể cần thở máy
    
    **❌ KHÔNG NÊN:**
    - ❌ Garo chặt
    - ❌ Rạch, hút nọc độc
    - ❌ Chườm đá
    - ❌ Đắp lá cây
    - ❌ Uống rượu
    - ❌ Để bệnh nhân ngủ (có thể nhầm với liệt)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác đồ điều trị")
    
    severity = st.radio(
        "**Mức độ nhiễm độc:**",
        ["Không có dấu hiệu nhiễm độc", "Nhẹ", "Trung bình", "Nặng"],
        key="cobra_severity"
    )
    
    st.markdown("---")
    
    if "Không có" in severity:
        render_no_envenomation_cobra()
    elif "Nhẹ" in severity:
        render_mild_envenomation_cobra()
    elif "Trung bình" in severity:
        render_moderate_envenomation_cobra()
    else:
        render_severe_envenomation_cobra()
    
    st.markdown("---")
    
    # ========== SECTION 6: ANTIVENOM ==========
    st.markdown("### 💉 Huyết thanh kháng nọc")
    
    st.warning("""
    **Huyết thanh kháng nọc rắn hổ mang:**
    
    **Chỉ định:**
    - Có dấu hiệu nhiễm độc thần kinh
    - Sụp mi, nhìn đôi
    - Nói khó, nuốt khó
    - Yếu cơ, liệt cơ
    - Khó thở
    
    **Liều lượng:**
    - **Nhẹ:** 4-6 lọ
    - **Trung bình:** 6-10 lọ
    - **Nặng:** 10-20 lọ hoặc hơn
    
    **Cách dùng:**
    - Pha trong 200-500ml NaCl 0.9%
    - Truyền tĩnh mạch chậm (60-90 phút)
    - Test da trước (nếu có thể)
    - Theo dõi phản ứng dị ứng
    
    **Lưu ý:**
    - Càng sớm càng tốt
    - Có thể truyền trước khi có liệt hoàn toàn
    - Đánh giá lại sau 2-4 giờ
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: RESPIRATORY SUPPORT ==========
    st.markdown("### 🫁 Hỗ trợ hô hấp")
    
    st.error("""
    **⚠️ QUAN TRỌNG: Hỗ trợ hô hấp là ưu tiên hàng đầu**
    
    **Theo dõi:**
    - Nhịp thở mỗi 15-30 phút
    - SpO2 liên tục
    - Đánh giá sức cơ hô hấp
    - Dấu hiệu suy hô hấp
    
    **Chỉ định thở máy:**
    - Khó thở tăng dần
    - SpO2 <90% dù có oxy
    - Yếu cơ hô hấp rõ
    - Liệt cơ hô hấp
    - PaO2 <60 mmHg hoặc PaCO2 >50 mmHg
    
    **Thở máy:**
    - Chế độ: Assist-Control hoặc SIMV
    - FiO2: Bắt đầu 100%, giảm dần
    - PEEP: 5-10 cmH2O
    - Theo dõi sát
    
    **Cai máy:**
    - Khi huyết thanh có hiệu quả
    - Cơ hô hấp phục hồi
    - Test cai máy từng bước
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.error("""
    **Biến chứng có thể gặp:**
    
    **1. Suy hô hấp:**
    - Liệt cơ hô hấp
    - Ngừng thở
    - Cần thở máy kéo dài
    
    **2. Viêm phổi:**
    - Do hít sặc (liệt nuốt)
    - Do thở máy
    - Cần kháng sinh
    
    **3. Loét do tì đè:**
    - Do liệt, nằm lâu
    - Cần xoay trở, chăm sóc da
    
    **4. Yếu cơ kéo dài:**
    - Có thể kéo dài vài tuần
    - Cần vật lý trị liệu
    
    **5. Phản ứng với huyết thanh:**
    - Sốc phản vệ
    - Bệnh huyết thanh
    
    **Xử trí:**
    - Hồi sức tích cực
    - Điều trị theo triệu chứng
    - Phục hồi chức năng
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("cobra_bite"))


def render_no_envenomation_cobra():
    """No envenomation protocol"""
    st.success("## ✅ KHÔNG CÓ DẤU HIỆU NHIỄM ĐỘC")
    
    st.markdown("""
    **Đặc điểm:**
    - Không có dấu hiệu thần kinh
    - Không có liệt
    - Hô hấp bình thường
    
    **Xử trí:**
    1. **Theo dõi:** 24 giờ tại viện
    2. **Đánh giá:** Mỗi 2-4 giờ
    3. **Xét nghiệm:** Không cần thiết
    4. **Tiêm phòng uốn ván:** Nếu cần
    
    **Xuất viện khi:**
    - Không có dấu hiệu sau 24 giờ
    - Hướng dẫn theo dõi tại nhà
    """)


def render_mild_envenomation_cobra():
    """Mild envenomation protocol"""
    st.warning("## ⚠️ NHIỄM ĐỘC NHẸ")
    
    st.markdown("""
    **Đặc điểm:**
    - Tê bì quanh vết cắn
    - Sụp mi nhẹ
    - Nhìn đôi
    - Hô hấp còn tốt
    
    **Xử trí:**
    1. **Huyết thanh:** 4-6 lọ
    2. **Theo dõi sát:** Mỗi 1-2 giờ
    3. **Đánh giá hô hấp:** Liên tục
    4. **Chuẩn bị:** Có thể cần thở máy
    
    **Theo dõi:**
    - Dấu hiệu thần kinh
    - Chức năng hô hấp
    - Đáp ứng với huyết thanh
    """)


def render_moderate_envenomation_cobra():
    """Moderate envenomation protocol"""
    st.error("## 🚨 NHIỄM ĐỘC TRUNG BÌNH")
    
    st.markdown("""
    **Đặc điểm:**
    - Sụp mi rõ
    - Nói khó, nuốt khó
    - Yếu cơ cổ, tứ chi
    - Khó thở nhẹ đến trung bình
    
    **Xử trí:**
    1. **Huyết thanh:** 6-10 lọ ngay
    2. **Hỗ trợ hô hấp:**
       - Oxy cao
       - Theo dõi SpO2 liên tục
       - Chuẩn bị thở máy
    3. **Theo dõi:** Mỗi 30-60 phút
    4. **ICU:** Nên chuyển ICU
    
    **Cảnh báo:**
    - Có thể tiến triển nhanh
    - Cần sẵn sàng thở máy
    """)


def render_severe_envenomation_cobra():
    """Severe envenomation protocol"""
    st.error("## 🚨🚨 NHIỄM ĐỘC NẶNG - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Liệt hoàn toàn
    - Suy hô hấp hoặc ngừng thở
    - Cần thở máy
    - Có thể có sốc
    
    **Xử trí khẩn cấp:**
    1. **Đường thở:** Đặt nội khí quản NGAY
    2. **Thở máy:** Bắt đầu ngay
    3. **Huyết thanh:** 10-20 lọ
       - Có thể truyền nhanh hơn
    4. **Hồi sức:**
       - Bù dịch
       - Vasopressor nếu cần
    5. **ICU Monitoring:**
       - Continuous monitoring
       - Theo dõi đáp ứng
       - Đánh giá phục hồi
    
    **Tiên lượng:**
    - Cần thở máy: 3-7 ngày
    - Phục hồi: 1-3 tuần
    - Có thể có di chứng
    """)

