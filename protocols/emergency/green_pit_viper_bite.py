"""
Green Pit Viper Bite Protocol (Rắn Lục Xanh Đuôi Đỏ)
Trimeresurus albolabris / Trimeresurus stejnegeri
Common venomous snake in Vietnam
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Green Pit Viper Bite Protocol"""
    st.subheader("🐍 Rắn Lục Xanh Đuôi Đỏ Cắn (Green Pit Viper Bite)")
    st.caption("Trimeresurus albolabris / Trimeresurus stejnegeri - Cấp cứu rắn độc phổ biến tại Việt Nam")
    
    st.error("""
    **⚠️ RẮN LỤC XANH ĐUÔI ĐỎ CẮN = CẤP CỨU Y TẾ**
    
    **Đặc điểm:**
    - Rắn độc phổ biến nhất tại Việt Nam
    - Phân bố: Khắp cả nước, đặc biệt vùng núi, rừng
    - Hoạt động: Ban đêm, ẩn trong cây cối
    - Độc tố: Hemotoxic (gây rối loạn đông máu)
    
    **Tỷ lệ tử vong:** <1% nếu điều trị đúng
    **Biến chứng:** Rối loạn đông máu, xuất huyết, hoại tử tại chỗ
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: IDENTIFICATION ==========
    st.markdown("### 🎯 Nhận dạng rắn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Đặc điểm nhận dạng:**
        - Màu xanh lá cây
        - Đuôi đỏ hoặc nâu đỏ
        - Kích thước: 50-100cm
        - Đầu hình tam giác
        - Mắt có đồng tử dọc
        """)
    
    with col2:
        st.warning("""
        **Phân biệt với rắn không độc:**
        - Rắn lục có đầu tam giác rõ
        - Có rãnh nhiệt (heat pit)
        - Màu sắc đặc trưng
        - Nếu không chắc chắn → Xử trí như rắn độc
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
        
        has_envenomation = st.checkbox("Có dấu hiệu nhiễm độc", value=False)
    
    with col2:
        if time_since_bite > 0:
            st.info(f"""
            **Thời gian:** {time_since_bite:.1f} giờ sau khi cắn
            
            **Lưu ý:**
            - <6 giờ: Giai đoạn sớm, điều trị tối ưu
            - 6-24 giờ: Vẫn có thể điều trị hiệu quả
            - >24 giờ: Điều trị hỗ trợ, theo dõi biến chứng
            """)
    
    st.markdown("---")
    
    # ========== SECTION 3: SIGNS OF ENVENOMATION ==========
    st.markdown("### 🔍 Dấu hiệu nhiễm độc")
    
    tab1, tab2, tab3 = st.tabs(["Tại chỗ", "Toàn thân", "Xét nghiệm"])
    
    with tab1:
        st.markdown("""
        **Dấu hiệu tại chỗ:**
        - ✅ Đau tại vết cắn (thường rất đau)
        - ✅ Sưng nề (có thể lan rộng)
        - ✅ Bầm tím, xuất huyết dưới da
        - ✅ Phỏng nước (có thể có)
        - ✅ Hoại tử (trường hợp nặng)
        - ✅ Hạch vùng sưng to
        
        **Mức độ sưng:**
        - Nhẹ: Sưng quanh vết cắn (<5cm)
        - Trung bình: Sưng lan đến khớp gần
        - Nặng: Sưng lan toàn chi, có thể lan thân mình
        """)
    
    with tab2:
        st.markdown("""
        **Dấu hiệu toàn thân:**
        - ✅ Chảy máu (chảy máu chân răng, chảy máu mũi)
        - ✅ Xuất huyết dưới da, ban xuất huyết
        - ✅ Nôn ra máu, đi ngoài phân đen
        - ✅ Tiểu máu
        - ✅ Sốt (có thể có)
        - ✅ Buồn nôn, nôn
        - ✅ Đau đầu, chóng mặt
        - ✅ Hạ huyết áp (trường hợp nặng)
        
        **⚠️ Dấu hiệu nặng:**
        - Sốc xuất huyết
        - Rối loạn đông máu nặng
        - Suy đa tạng
        """)
    
    with tab3:
        st.markdown("""
        **Xét nghiệm cần làm:**
        
        **Cấp cứu (ngay):**
        - ✅ Công thức máu (CBC) - Giảm tiểu cầu
        - ✅ PT/INR, aPTT - Kéo dài
        - ✅ Fibrinogen - Giảm
        - ✅ D-dimer - Tăng
        
        **Theo dõi (mỗi 6-12h):**
        - Công thức máu
        - PT/INR, aPTT
        - Fibrinogen
        - Chức năng thận (Creatinine, BUN)
        - Chức năng gan (ALT, AST)
        
        **Đặc trưng:**
        - Giảm fibrinogen rõ rệt
        - Tăng D-dimer
        - PT/INR kéo dài
        - Giảm tiểu cầu (có thể)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: FIRST AID ==========
    st.markdown("### 🚑 Sơ cứu ban đầu")
    
    st.success("""
    **✅ NÊN LÀM:**
    1. **Bình tĩnh:** Giữ bệnh nhân yên tĩnh
    2. **Bất động chi:** Nẹp chi bị cắn, để thấp hơn tim
    3. **Loại bỏ trang sức:** Tháo nhẫn, vòng tay (tránh chèn ép khi sưng)
    4. **Vận chuyển nhanh:** Đưa đến cơ sở y tế gần nhất
    5. **Ghi nhớ:** Mô tả rắn nếu có thể (không cần bắt rắn)
    
    **❌ KHÔNG NÊN:**
    - ❌ Garo chặt (chỉ garo nhẹ nếu cần)
    - ❌ Rạch, hút nọc độc
    - ❌ Chườm đá
    - ❌ Đắp lá cây, thuốc nam
    - ❌ Uống rượu
    - ❌ Chạy, vận động mạnh
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: TREATMENT PROTOCOL ==========
    st.markdown("### 💊 Phác đồ điều trị")
    
    severity = st.radio(
        "**Mức độ nhiễm độc:**",
        ["Không có dấu hiệu nhiễm độc", "Nhẹ", "Trung bình", "Nặng"],
        key="viper_severity"
    )
    
    st.markdown("---")
    
    if "Không có" in severity:
        render_no_envenomation()
    elif "Nhẹ" in severity:
        render_mild_envenomation()
    elif "Trung bình" in severity:
        render_moderate_envenomation()
    else:
        render_severe_envenomation()
    
    st.markdown("---")
    
    # ========== SECTION 6: ANTIVENOM ==========
    st.markdown("### 💉 Huyết thanh kháng nọc")
    
    st.warning("""
    **Huyết thanh kháng nọc rắn lục:**
    
    **Chỉ định:**
    - Có dấu hiệu nhiễm độc rõ ràng
    - Rối loạn đông máu (PT/INR >1.5, fibrinogen <1.5 g/L)
    - Sưng lan rộng
    - Xuất huyết
    
    **Liều lượng:**
    - **Nhẹ:** 2-4 lọ
    - **Trung bình:** 4-6 lọ
    - **Nặng:** 6-10 lọ hoặc hơn
    
    **Cách dùng:**
    - Pha trong 100-200ml NaCl 0.9%
    - Truyền tĩnh mạch chậm (30-60 phút)
    - Test da trước (nếu có thể)
    - Theo dõi phản ứng dị ứng
    
    **Theo dõi sau truyền:**
    - Đánh giá lại sau 6 giờ
    - Nếu không cải thiện → Lặp lại liều
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: SUPPORTIVE CARE ==========
    st.markdown("### 🏥 Điều trị hỗ trợ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Điều trị tại chỗ:**
        - Vệ sinh vết cắn
        - Kháng sinh dự phòng (nếu cần)
        - Giảm đau (Paracetamol, không dùng NSAID)
        - Nâng cao chi bị cắn
        - Theo dõi hoại tử
        
        **Xử trí hoại tử:**
        - Cắt lọc nếu cần
        - Chăm sóc vết thương
        - Có thể cần ghép da
        """)
    
    with col2:
        st.markdown("""
        **Điều trị toàn thân:**
        - Bù dịch nếu cần
        - Điều chỉnh rối loạn đông máu
        - Truyền máu nếu mất máu nhiều
        - Truyền tiểu cầu nếu giảm nặng
        - Truyền huyết tương tươi đông lạnh (FFP) nếu cần
        
        **Theo dõi:**
        - Dấu hiệu sống mỗi 2-4 giờ
        - Xét nghiệm đông máu mỗi 6-12 giờ
        - Theo dõi chức năng thận, gan
        """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.error("""
    **Biến chứng có thể gặp:**
    
    **1. Rối loạn đông máu:**
    - Xuất huyết nặng
    - Chảy máu nội tạng
    - Xuất huyết não (hiếm nhưng nguy hiểm)
    
    **2. Hoại tử tại chỗ:**
    - Hoại tử mô
    - Nhiễm trùng thứ phát
    - Có thể cần cắt cụt (hiếm)
    
    **3. Suy đa tạng:**
    - Suy thận cấp
    - Suy gan
    - Rối loạn chức năng đa cơ quan
    
    **4. Phản ứng với huyết thanh:**
    - Sốc phản vệ
    - Bệnh huyết thanh (sau 5-10 ngày)
    
    **Xử trí:**
    - Điều trị theo triệu chứng
    - Hồi sức tích cực nếu cần
    - Theo dõi sát
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: PREVENTION ==========
    st.markdown("### 🛡️ Phòng ngừa")
    
    st.info("""
    **Khuyến cáo phòng ngừa:**
    
    **Khi vào rừng, vùng có rắn:**
    - Mang giày cao cổ, quần dài
    - Dùng đèn pin ban đêm
    - Không đi chân đất
    - Cẩn thận khi bước qua cây cối, đá
    - Không đưa tay vào hang, khe đá
    
    **Nếu gặp rắn:**
    - Không chạm vào
    - Lùi lại từ từ
    - Không đuổi theo
    - Để rắn tự đi
    
    **Giáo dục:**
    - Nhận biết rắn độc
    - Sơ cứu đúng cách
    - Đưa đến viện ngay
    """)
    
    st.markdown("---")
    
    # ========== REFERENCES ==========
    render_references_section(get_references("green_pit_viper_bite"))


def render_no_envenomation():
    """No envenomation protocol"""
    st.success("## ✅ KHÔNG CÓ DẤU HIỆU NHIỄM ĐỘC")
    
    st.markdown("""
    **Đặc điểm:**
    - Không có sưng nề
    - Không có rối loạn đông máu
    - Xét nghiệm bình thường
    - Có thể chỉ là vết cắn "dry bite"
    
    **Xử trí:**
    1. **Vệ sinh vết cắn:** Rửa sạch, sát trùng
    2. **Tiêm phòng uốn ván:** Nếu chưa tiêm trong 5 năm
    3. **Theo dõi:** 24 giờ tại viện
    4. **Xét nghiệm:** CBC, PT/INR ban đầu và sau 6-12 giờ
    
    **Xuất viện khi:**
    - Không có dấu hiệu nhiễm độc sau 24 giờ
    - Xét nghiệm bình thường
    - Hướng dẫn theo dõi tại nhà
    """)


def render_mild_envenomation():
    """Mild envenomation protocol"""
    st.warning("## ⚠️ NHIỄM ĐỘC NHẸ")
    
    st.markdown("""
    **Đặc điểm:**
    - Sưng quanh vết cắn (<5cm)
    - Đau tại chỗ
    - Xét nghiệm: PT/INR có thể tăng nhẹ
    - Không có xuất huyết
    
    **Xử trí:**
    1. **Theo dõi sát:** Mỗi 4-6 giờ
    2. **Xét nghiệm:** CBC, PT/INR, fibrinogen mỗi 12 giờ
    3. **Huyết thanh kháng nọc:** Có thể cân nhắc nếu:
       - PT/INR >1.5
       - Fibrinogen <1.5 g/L
       - Sưng lan rộng
    4. **Giảm đau:** Paracetamol
    5. **Nâng cao chi:** Giảm sưng
    
    **Theo dõi:**
    - Dấu hiệu sống mỗi 4 giờ
    - Đánh giá sưng nề
    - Xét nghiệm đông máu
    """)


def render_moderate_envenomation():
    """Moderate envenomation protocol"""
    st.error("## 🚨 NHIỄM ĐỘC TRUNG BÌNH")
    
    st.markdown("""
    **Đặc điểm:**
    - Sưng lan đến khớp gần
    - Rối loạn đông máu rõ (PT/INR >1.5, fibrinogen <1.5)
    - Có thể có xuất huyết nhẹ
    - Bầm tím quanh vết cắn
    
    **Xử trí:**
    1. **Huyết thanh kháng nọc:** 4-6 lọ
       - Pha trong 200ml NaCl 0.9%
       - Truyền tĩnh mạch chậm (30-60 phút)
       - Theo dõi phản ứng dị ứng
    
    2. **Xét nghiệm:** 
       - CBC, PT/INR, fibrinogen, D-dimer
       - Lặp lại sau 6 giờ
    
    3. **Theo dõi:**
       - Dấu hiệu sống mỗi 2-4 giờ
       - Đánh giá đáp ứng điều trị
       - Nếu không cải thiện → Lặp lại huyết thanh
    
    4. **Điều trị hỗ trợ:**
       - Giảm đau
       - Nâng cao chi
       - Vệ sinh vết cắn
       - Kháng sinh dự phòng (nếu cần)
    """)


def render_severe_envenomation():
    """Severe envenomation protocol"""
    st.error("## 🚨🚨 NHIỄM ĐỘC NẶNG - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Sưng lan toàn chi hoặc lan thân mình
    - Rối loạn đông máu nặng
    - Xuất huyết rõ ràng
    - Có thể có sốc
    - Hoại tử tại chỗ
    
    **Xử trí khẩn cấp:**
    1. **Huyết thanh kháng nọc:** 6-10 lọ hoặc hơn
       - Truyền ngay
       - Có thể truyền nhanh hơn nếu sốc
       - Theo dõi sát phản ứng
    
    2. **Hồi sức:**
       - Đường thở: Đảm bảo thông thoáng
       - Hô hấp: Oxy nếu cần
       - Tuần hoàn: Bù dịch, vasopressor nếu cần
    
    3. **Điều chỉnh đông máu:**
       - Truyền FFP nếu cần
       - Truyền tiểu cầu nếu giảm nặng
       - Truyền máu nếu mất máu
    
    4. **ICU Monitoring:**
       - Continuous monitoring
       - Xét nghiệm mỗi 6 giờ
       - Theo dõi chức năng đa cơ quan
    
    5. **Xử trí hoại tử:**
       - Cắt lọc nếu cần
       - Chăm sóc vết thương
       - Có thể cần phẫu thuật
    
    **Tiên lượng:**
    - Cần điều trị tích cực
    - Thời gian nằm viện: 5-10 ngày
    - Có thể có di chứng
    """)

