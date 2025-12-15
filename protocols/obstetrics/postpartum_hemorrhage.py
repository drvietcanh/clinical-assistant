"""
Postpartum Hemorrhage (PPH) Protocol
ACOG 2017 Guidelines
Excessive bleeding after delivery
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Postpartum Hemorrhage Protocol"""
    st.subheader("🤰 Xuất huyết sau sinh (Postpartum Hemorrhage)")
    st.caption("ACOG 2017 Guidelines - Excessive bleeding after delivery")
    
    st.error("""
    **⚠️ XUẤT HUYẾT SAU SINH = CẤP CỨU SẢN KHOA**
    
    **Định nghĩa:**
    - **Sớm (Primary PPH):** Mất máu ≥500 mL sau sinh thường hoặc ≥1000 mL sau mổ lấy thai (trong 24 giờ đầu)
    - **Muộn (Secondary PPH):** Mất máu bất thường sau 24 giờ đến 12 tuần sau sinh
    
    **Nguyên nhân (4T):**
    - **Tone:** Đờ tử cung (thường gặp nhất)
    - **Trauma:** Rách đường sinh dục
    - **Tissue:** Sót nhau, nhau cài răng lược
    - **Thrombin:** Rối loạn đông máu
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: RISK FACTORS ==========
    st.markdown("### ⚠️ Yếu tố nguy cơ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Yếu tố nguy cơ:**
        - Đa thai
        - Đa ối
        - Thai to
        - Chuyển dạ kéo dài
        - Sử dụng oxytocin
        - Tiền sử PPH
        - Nhau tiền đạo
        """)
    
    with col2:
        st.markdown("""
        **Yếu tố nguy cơ (tiếp):**
        - Nhau bong non
        - Rách đường sinh dục
        - Rối loạn đông máu
        - Béo phì
        - Tuổi mẹ cao
        - Sinh mổ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Xử trí ngay lập tức")
    
    st.error("""
    **1. Gọi đội cấp cứu PPH:**
    - Bác sĩ sản khoa
    - Gây mê hồi sức
    - Huyết học
    - Ngân hàng máu
    
    **2. ABC:**
    - Đảm bảo đường thở
    - Oxygen 100%
    - 2 đường truyền tĩnh mạch lớn (16-18G)
    - Truyền dịch tinh thể (Ringer lactate, Normal saline)
    
    **3. Đánh giá mất máu:**
    - Đếm gạc, khăn
    - Đo lượng máu
    - Đánh giá dấu hiệu sốc
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ALGORITHM ==========
    st.markdown("### 💊 Phác đồ điều trị")
    
    st.markdown("#### **Bước 1: Xử trí đờ tử cung (Uterine Atony)**")
    
    st.success("""
    **A. Xoa bóp tử cung:**
    - Xoa bóp đáy tử cung qua thành bụng
    - Kiểm tra tử cung trong âm đạo
    
    **B. Thuốc co tử cung:**
    
    **Oxytocin:**
    - **10-40 đơn vị trong 500-1000 mL dịch truyền**
    - Hoặc: 10 đơn vị IM
    - **Lưu ý:** Có thể gây hạ natri máu nếu dùng liều cao
    
    **Methylergonovine (Methergine):**
    - **0.2 mg IM** (có thể lặp lại q2-4h)
    - **Chống chỉ định:** Tăng huyết áp, bệnh tim
    
    **Carboprost (Hemabate):**
    - **250 mcg IM** (có thể lặp lại q15-90 phút, tối đa 8 liều)
    - **Chống chỉ định:** Hen, bệnh tim, phổi
    
    **Misoprostol:**
    - **600-1000 mcg đặt trực tràng hoặc dưới lưỡi**
    - Dùng khi không có thuốc khác
    """)
    
    st.markdown("---")
    
    st.markdown("#### **Bước 2: Kiểm tra và xử trí nguyên nhân khác**")
    
    st.warning("""
    **A. Kiểm tra đường sinh dục:**
    - Soi cổ tử cung, âm đạo
    - Tìm rách, khâu nếu có
    
    **B. Kiểm tra nhau:**
    - Kiểm tra nhau có đủ không
    - Nạo buồng tử cung nếu sót nhau
    
    **C. Điều trị rối loạn đông máu:**
    - Truyền huyết tương tươi đông lạnh (FFP)
    - Truyền tiểu cầu
    - Truyền cryoprecipitate
    """)
    
    st.markdown("---")
    
    st.markdown("#### **Bước 3: Can thiệp nếu không đáp ứng**")
    
    st.error("""
    **A. Thủ thuật:**
    - **Bóng chèn tử cung (Bakri balloon):** Chèn vào buồng tử cung
    - **Khâu B-Lynch:** Khâu tử cung để co tử cung
    - **Thắt động mạch tử cung:** Nếu có điều kiện
    
    **B. Phẫu thuật:**
    - **Cắt tử cung:** Nếu các biện pháp khác thất bại
    - **Chỉ định:** Mất máu nặng, đe dọa tính mạng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: BLOOD TRANSFUSION ==========
    st.markdown("### 🩸 Truyền máu")
    
    st.info("""
    **Chỉ định truyền máu:**
    - Mất máu >1000 mL
    - Hoặc có dấu hiệu sốc
    - Hoặc Hb <7 g/dL (hoặc <8 g/dL nếu có bệnh tim)
    
    **Phác đồ truyền:**
    - **Hồng cầu:** 2-4 đơn vị (tùy mất máu)
    - **FFP:** 4 đơn vị (nếu PT/PTT kéo dài)
    - **Tiểu cầu:** 1 đơn vị (nếu <50,000/µL)
    - **Cryoprecipitate:** 10 đơn vị (nếu fibrinogen <100 mg/dL)
    
    **Tỷ lệ truyền:**
    - Hồng cầu:FFP:Tiểu cầu = 1:1:1 (Massive transfusion protocol)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Dấu hiệu sinh tồn:** Mỗi 15-30 phút
    - **Lượng máu mất:** Liên tục
    - **Lượng nước tiểu:** Mỗi giờ (cần >30 mL/h)
    - **Hb, Hct:** Mỗi 2-4 giờ
    - **Đông máu:** PT, PTT, fibrinogen, tiểu cầu
    - **Tử cung:** Kích thước, độ co
    
    **Dấu hiệu cải thiện:**
    - Giảm chảy máu
    - Ổn định dấu hiệu sinh tồn
    - Tử cung co tốt
    
    **Dấu hiệu xấu đi:**
    - Chảy máu tiếp tục
    - Sốc
    - Rối loạn đông máu
    - Cần phẫu thuật
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: REFERENCES ==========
    references = get_references("Postpartum Hemorrhage")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            show_evidence_level=True,
            show_links=True
        )
    else:
        st.markdown("### 📚 Tài liệu tham khảo")
        st.markdown("""
        1. **ACOG Practice Bulletin No. 183** - Postpartum Hemorrhage (2017)
        2. **WHO Recommendations** - Prevention and Treatment of Postpartum Haemorrhage (2012)
        3. **UpToDate:** Postpartum Hemorrhage - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

