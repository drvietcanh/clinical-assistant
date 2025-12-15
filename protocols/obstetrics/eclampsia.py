"""
Eclampsia Protocol
ACOG 2020 Guidelines
Seizures in pregnancy with preeclampsia
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Eclampsia Protocol"""
    st.subheader("🤰 Sản giật (Eclampsia)")
    st.caption("ACOG 2020 Guidelines - Seizures in pregnancy with preeclampsia")
    
    st.error("""
    **⚠️ SẢN GIẬT = CẤP CỨU SẢN KHOA**
    
    **Định nghĩa:**
    - Co giật hoặc hôn mê ở bệnh nhân tiền sản giật
    - Không do nguyên nhân thần kinh khác
    - Có thể xảy ra trước, trong, hoặc sau sinh
    
    **Yếu tố nguy cơ:**
    - Tiền sản giật
    - Tiền sử sản giật
    - Đa thai
    - Tuổi mẹ <20 hoặc >35
    - Bệnh lý mạn tính (tăng huyết áp, đái tháo đường)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    st.warning("""
    **Chẩn đoán sản giật khi có:**
    
    1. **Tiền sản giật (Preeclampsia):**
       - Huyết áp ≥140/90 mmHg (sau 20 tuần)
       - VÀ Protein niệu ≥300 mg/24h hoặc tỷ số protein/creatinine ≥0.3
       - HOẶC có dấu hiệu nội tạng (tăng men gan, giảm tiểu cầu, phù phổi)
    
    2. **Co giật hoặc hôn mê:**
       - Co giật toàn thân
       - Hoặc hôn mê không do nguyên nhân khác
       - Loại trừ: Động kinh, u não, viêm màng não
    
    **Phân loại:**
    - **Sản giật trước sinh:** Trước khi chuyển dạ
    - **Sản giật trong chuyển dạ:** Trong quá trình chuyển dạ
    - **Sản giật sau sinh:** Trong 48 giờ sau sinh (có thể đến 4 tuần)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 2: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng tiền sản giật:**
        - Tăng huyết áp
        - Protein niệu
        - Phù
        - Đau đầu
        - Rối loạn thị giác
        - Đau thượng vị
        """)
    
    with col2:
        st.markdown("""
        **Triệu chứng sản giật:**
        - Co giật toàn thân
        - Hôn mê sau co giật
        - Kích động
        - Đau đầu dữ dội
        - Rối loạn thị giác
        - Đau thượng vị (HELLP syndrome)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: IMMEDIATE MANAGEMENT ==========
    st.markdown("### 🚨 Xử trí ngay lập tức")
    
    st.error("""
    **1. ABC (Đường thở, Hô hấp, Tuần hoàn):**
    - Đảm bảo đường thở (nghiêng đầu sang bên)
    - Oxygen 100%
    - Monitor: BP, HR, SpO2, CTG (nếu chưa sinh)
    - Đặt đường truyền tĩnh mạch
    
    **2. Ngăn ngừa chấn thương:**
    - Đệm xung quanh giường
    - Không cố gắng giữ bệnh nhân
    - Không đặt vật vào miệng
    
    **3. Điều trị co giật:**
    - **Magnesium Sulfate:** Loading 4-6 g IV (truyền trong 15-20 phút)
    - **Sau đó:** 1-2 g/h IV (duy trì)
    - **Nếu còn co giật:** Thêm 2 g IV bolus
    
    **4. Hạ huyết áp (nếu cần):**
    - **Labetalol:** 20 mg IV, sau đó 40-80 mg q10-15 phút (tối đa 300 mg)
    - **Hoặc:** Hydralazine: 5-10 mg IV q20-30 phút
    - **Mục tiêu:** SBP 140-160 mmHg, DBP 90-110 mmHg
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: MAGNESIUM SULFATE PROTOCOL ==========
    st.markdown("### 💉 Magnesium Sulfate Protocol")
    
    st.success("""
    **Magnesium Sulfate (Thuốc chính điều trị sản giật):**
    
    **Loading Dose:**
    - **4-6 g IV** (truyền trong 15-20 phút)
    - Hoặc: 10 g IM (5g mỗi mông)
    
    **Maintenance:**
    - **1-2 g/h IV** (duy trì)
    - Tiếp tục 24 giờ sau sinh hoặc sau cơn co giật cuối
    
    **Theo dõi:**
    - Phản xạ gân xương (mỗi 1 giờ)
    - Nhịp thở (mỗi 1 giờ)
    - Lượng nước tiểu (mỗi giờ, cần >100 mL/4h)
    - Nồng độ Mg (nếu có): Mục tiêu 4-7 mg/dL
    
    **Dấu hiệu quá liều:**
    - Mất phản xạ gân xương
    - Nhịp thở <12/phút
    - Lượng nước tiểu <100 mL/4h
    - **Điều trị:** Calcium gluconate 1 g IV (10% 10 mL)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: DELIVERY ==========
    st.markdown("### 👶 Chuyển dạ")
    
    st.info("""
    **Chỉ định chuyển dạ:**
    - Sản giật là chỉ định chuyển dạ
    - Chuyển dạ ngay sau khi ổn định (thường trong 24 giờ)
    
    **Phương pháp:**
    - **Sinh thường:** Nếu điều kiện cho phép
    - **Mổ lấy thai:** Nếu có chỉ định sản khoa khác
    
    **Lưu ý:**
    - Tiếp tục Magnesium Sulfate trong và sau chuyển dạ
    - Theo dõi sát mẹ và con
    - Có thể cần hồi sức sơ sinh
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **Huyết áp:** Mỗi 15-30 phút
    - **Triệu chứng thần kinh:** Mỗi 1 giờ
    - **Phản xạ gân xương:** Mỗi 1 giờ (nếu dùng Mg)
    - **Lượng nước tiểu:** Mỗi giờ (cần >100 mL/4h)
    - **CBC, chức năng gan, thận:** Mỗi 12-24 giờ
    - **CTG (nếu chưa sinh):** Liên tục
    - **Nồng độ Mg:** Nếu có (mục tiêu 4-7 mg/dL)
    
    **Dấu hiệu cải thiện:**
    - Hết co giật
    - Cải thiện ý thức
    - Ổn định huyết áp
    - Cải thiện chức năng thận
    
    **Dấu hiệu xấu đi:**
    - Co giật tái phát
    - Hôn mê
    - Suy đa tạng
    - HELLP syndrome
    - Cần ICU
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.warning("""
    **Biến chứng mẹ:**
    - Suy đa tạng
    - HELLP syndrome
    - Suy thận cấp
    - Phù phổi
    - Đột quỵ
    - Tử vong (hiếm)
    
    **Biến chứng con:**
    - Sinh non
    - Nhẹ cân
    - Suy thai
    - Tử vong chu sinh
    
    **Phòng ngừa:**
    - Phát hiện sớm tiền sản giật
    - Theo dõi sát trong thai kỳ
    - Điều trị kịp thời
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: REFERENCES ==========
    references = get_references("Eclampsia")
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
        1. **ACOG Practice Bulletin No. 222** - Preeclampsia and Eclampsia (2020)
        2. **WHO Recommendations** - Prevention and Treatment of Pre-eclampsia and Eclampsia (2011)
        3. **UpToDate:** Eclampsia - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

