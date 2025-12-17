"""
Krait Bite Protocol (Rắn Cạp Nia Cắn)
Bungarus fasciatus / Bungarus candidus
Highly neurotoxic venomous snake in Vietnam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Krait Bite Protocol"""
    st.subheader("🐍 Rắn Cạp Nia Cắn (Krait Bite)")
    st.caption("Bungarus fasciatus / Bungarus candidus - Rắn độc thần kinh rất nguy hiểm tại Việt Nam")
    
    st.error("""
    **⚠️ RẮN CẠP NIA CẮN = CẤP CỨU Y TẾ RẤT KHẨN CẤP**
    
    **Đặc điểm:**
    - Rắn độc thần kinh rất nguy hiểm
    - Phân bố: Khắp cả nước, đặc biệt vùng nông thôn
    - Hoạt động: Ban đêm (rất nguy hiểm)
    - Độc tố: Neurotoxic mạnh (gây liệt cơ nhanh)
    
    **Tỷ lệ tử vong:** 10-20% nếu không điều trị kịp thời
    **Biến chứng:** Liệt cơ nhanh, suy hô hấp, ngừng thở
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: IDENTIFICATION ==========
    st.markdown("### 🎯 Nhận dạng rắn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Đặc điểm nhận dạng:**
        - Màu đen với vòng vàng/trắng
        - Thân tròn, đuôi ngắn
        - Kích thước: 1-1.5m
        - Đầu nhỏ, không rõ
        - Hoạt động ban đêm
        """)
    
    with col2:
        st.warning("""
        **Phân loại tại Việt Nam:**
        - Rắn cạp nia (Bungarus fasciatus) - vòng vàng
        - Rắn cạp nia bạch (Bungarus candidus) - vòng trắng
        
        **⚠️ ĐỘC TÍNH RẤT CAO!**
        - Vết cắn có thể không đau
        - Triệu chứng xuất hiện chậm (1-6 giờ)
        - Nhưng khi xuất hiện → Tiến triển rất nhanh
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
        
        has_symptoms = st.checkbox("Đã có triệu chứng", value=False)
    
    with col2:
        if time_since_bite > 0:
            st.info(f"""
            **Thời gian:** {time_since_bite:.1f} giờ sau khi cắn
            
            **⚠️ Lưu ý đặc biệt:**
            - Vết cắn có thể không đau
            - Triệu chứng xuất hiện: 1-6 giờ
            - Khi xuất hiện → Tiến triển RẤT NHANH
            - Cần theo dõi sát ngay cả khi chưa có triệu chứng
            """)
    
    st.markdown("---")
    
    # ========== SECTION 3: SIGNS OF ENVENOMATION ==========
    st.markdown("### 🔍 Dấu hiệu nhiễm độc")
    
    tab1, tab2 = st.tabs(["Tại chỗ", "Thần kinh"])
    
    with tab1:
        st.markdown("""
        **⚠️ ĐẶC ĐIỂM QUAN TRỌNG:**
        - Vết cắn có thể **KHÔNG ĐAU**
        - Sưng nề **RẤT ÍT** hoặc không có
        - Dễ bỏ qua, nhầm với côn trùng cắn
        
        **Dấu hiệu tại chỗ (nếu có):**
        - Tê bì nhẹ quanh vết cắn
        - Có thể có 2 vết răng nhỏ
        """)
    
    with tab2:
        st.markdown("""
        **Dấu hiệu thần kinh (QUAN TRỌNG):**
        
        **Giai đoạn sớm (1-3 giờ):**
        - ✅ Tê bì quanh vết cắn
        - ✅ Tê bì môi, lưỡi
        - ✅ Nhìn đôi (song thị)
        - ✅ Sụp mi mắt (ptosis)
        - ✅ Nói khó, nuốt khó
        
        **Giai đoạn tiến triển (3-6 giờ):**
        - ✅ Liệt cơ mặt
        - ✅ Liệt cơ cổ
        - ✅ Liệt tứ chi
        - ✅ Liệt cơ hô hấp → **SUY HÔ HẤP**
        
        **⚠️ ĐẶC ĐIỂM:**
        - Triệu chứng xuất hiện chậm
        - Nhưng khi xuất hiện → Tiến triển RẤT NHANH
        - Có thể từ không có triệu chứng → Liệt hoàn toàn trong 1-2 giờ
        - Tỷ lệ tử vong cao nếu không điều trị kịp thời
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: FIRST AID ==========
    st.markdown("### 🚑 Sơ cứu ban đầu")
    
    st.success("""
    **✅ NÊN LÀM:**
    1. **Vận chuyển NGAY:** Đưa đến cơ sở y tế gần nhất
    2. **Theo dõi sát:** Ngay cả khi chưa có triệu chứng
    3. **Chuẩn bị:** Có thể cần thở máy
    4. **Bất động:** Giữ bệnh nhân yên tĩnh
    
    **❌ KHÔNG NÊN:**
    - ❌ Chủ quan vì vết cắn không đau
    - ❌ Để bệnh nhân ngủ (có thể nhầm với liệt)
    - ❌ Chờ có triệu chứng mới đi viện
    - ❌ Garo, rạch, hút nọc độc
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác đồ điều trị")
    
    st.warning("""
    **⚠️ LƯU Ý ĐẶC BIỆT:**
    - Ngay cả khi chưa có triệu chứng → Vẫn cần theo dõi sát
    - Nếu có dấu hiệu dù nhẹ → Điều trị ngay
    - Không chờ triệu chứng nặng mới điều trị
    """)
    
    severity = st.radio(
        "**Mức độ nhiễm độc:**",
        ["Chưa có triệu chứng (theo dõi)", "Nhẹ", "Trung bình", "Nặng"],
        key="krait_severity"
    )
    
    st.markdown("---")
    
    if "Chưa có" in severity:
        render_no_symptoms_krait()
    elif "Nhẹ" in severity:
        render_mild_envenomation_krait()
    elif "Trung bình" in severity:
        render_moderate_envenomation_krait()
    else:
        render_severe_envenomation_krait()
    
    st.markdown("---")
    
    # ========== SECTION 6: ANTIVENOM ==========
    st.markdown("### 💉 Huyết thanh kháng nọc")
    
    st.error("""
    **Huyết thanh kháng nọc rắn cạp nia:**
    
    **Chỉ định:**
    - **Ngay cả khi chưa có triệu chứng** (nếu chắc chắn là rắn cạp nia)
    - Có dấu hiệu thần kinh dù nhẹ
    - Tê bì, sụp mi, nhìn đôi
    
    **Liều lượng:**
    - **Chưa có triệu chứng:** 4-6 lọ (dự phòng)
    - **Nhẹ:** 6-10 lọ
    - **Trung bình:** 10-15 lọ
    - **Nặng:** 15-30 lọ hoặc hơn
    
    **Cách dùng:**
    - Pha trong 200-500ml NaCl 0.9%
    - Truyền tĩnh mạch chậm (60-90 phút)
    - Có thể truyền nhanh hơn nếu có liệt
    
    **Lưu ý:**
    - Càng sớm càng tốt
    - Đánh giá lại sau 2-4 giờ
    - Có thể cần lặp lại liều
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
    - SpO2 <90%
    - Yếu cơ hô hấp
    - Liệt cơ hô hấp
    - PaO2 <60 mmHg hoặc PaCO2 >50 mmHg
    
    **Thở máy:**
    - Chế độ: Assist-Control
    - FiO2: Bắt đầu 100%
    - PEEP: 5-10 cmH2O
    - Có thể cần thở máy kéo dài (1-2 tuần)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.error("""
    **Biến chứng có thể gặp:**
    
    **1. Suy hô hấp:**
    - Liệt cơ hô hấp nhanh
    - Ngừng thở
    - Cần thở máy kéo dài
    
    **2. Yếu cơ kéo dài:**
    - Có thể kéo dài vài tuần đến vài tháng
    - Cần vật lý trị liệu
    - Phục hồi chức năng
    
    **3. Viêm phổi:**
    - Do hít sặc
    - Do thở máy
    
    **4. Loét do tì đè:**
    - Do liệt, nằm lâu
    
    **Tiên lượng:**
    - Tỷ lệ tử vong cao nếu không điều trị
    - Phục hồi chậm
    - Có thể có di chứng
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("krait_bite"))


def render_no_symptoms_krait():
    """No symptoms protocol"""
    st.warning("## ⚠️ CHƯA CÓ TRIỆU CHỨNG - THEO DÕI SÁT")
    
    st.markdown("""
    **⚠️ LƯU Ý ĐẶC BIỆT:**
    - Rắn cạp nia có thể không có triệu chứng ban đầu
    - Triệu chứng xuất hiện: 1-6 giờ
    - Khi xuất hiện → Tiến triển RẤT NHANH
    
    **Xử trí:**
    1. **Theo dõi sát:** Mỗi 30-60 phút
    2. **Đánh giá:** Dấu hiệu thần kinh
    3. **Huyết thanh:** Cân nhắc dự phòng nếu:
       - Chắc chắn là rắn cạp nia
       - Thời gian từ khi cắn <6 giờ
       - Có thể không có huyết thanh sẵn
    4. **Chuẩn bị:** Sẵn sàng thở máy
    
    **Theo dõi:**
    - Không được xuất viện trong 24 giờ
    - Đánh giá mỗi 1-2 giờ
    - Cảnh báo bệnh nhân về triệu chứng
    """)


def render_mild_envenomation_krait():
    """Mild envenomation protocol"""
    st.error("## 🚨 NHIỄM ĐỘC NHẸ - ĐIỀU TRỊ NGAY")
    
    st.markdown("""
    **Đặc điểm:**
    - Tê bì, sụp mi
    - Nhìn đôi
    - Hô hấp còn tốt
    
    **Xử trí:**
    1. **Huyết thanh:** 6-10 lọ NGAY
    2. **Theo dõi sát:** Mỗi 30 phút
    3. **Hỗ trợ hô hấp:**
       - Oxy
       - Theo dõi SpO2
       - Chuẩn bị thở máy
    4. **ICU:** Nên chuyển ICU
    
    **Cảnh báo:**
    - Có thể tiến triển rất nhanh
    - Cần sẵn sàng thở máy
    """)


def render_moderate_envenomation_krait():
    """Moderate envenomation protocol"""
    st.error("## 🚨🚨 NHIỄM ĐỘC TRUNG BÌNH - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Liệt cơ rõ
    - Khó thở
    - Yếu cơ hô hấp
    
    **Xử trí:**
    1. **Huyết thanh:** 10-15 lọ NGAY
    2. **Hỗ trợ hô hấp:**
       - Oxy cao
       - Chuẩn bị đặt nội khí quản
       - Có thể cần thở máy ngay
    3. **ICU:** Chuyển ICU ngay
    4. **Theo dõi:** Continuous monitoring
    """)


def render_severe_envenomation_krait():
    """Severe envenomation protocol"""
    st.error("## 🚨🚨🚨 NHIỄM ĐỘC NẶNG - ICU KHẨN CẤP")
    
    st.markdown("""
    **Đặc điểm:**
    - Liệt hoàn toàn
    - Suy hô hấp hoặc ngừng thở
    - Cần thở máy
    
    **Xử trí khẩn cấp:**
    1. **Đường thở:** Đặt nội khí quản NGAY
    2. **Thở máy:** Bắt đầu ngay
    3. **Huyết thanh:** 15-30 lọ
       - Truyền nhanh hơn
    4. **Hồi sức:**
       - Bù dịch
       - Vasopressor nếu cần
    5. **ICU Monitoring:**
       - Continuous monitoring
       - Theo dõi đáp ứng
    
    **Tiên lượng:**
    - Cần thở máy: 1-2 tuần
    - Phục hồi: 2-4 tuần hoặc lâu hơn
    - Có thể có di chứng
    """)

