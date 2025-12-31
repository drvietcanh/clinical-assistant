"""
Atopic Dermatitis (Viêm da cơ địa) Protocol
Chronic inflammatory skin disease
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Atopic Dermatitis (Viêm da cơ địa) Protocol"""
    st.subheader("🩹 Viêm da cơ địa (Atopic Dermatitis / Eczema)")
    st.caption("Chronic inflammatory skin disease - Common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Bệnh viêm da mạn tính, tái phát
    - Thường kèm theo hen suyễn, viêm mũi dị ứng
    - Phổ biến ở trẻ em (15-20%), người lớn (2-10%)
    - Tỷ lệ cao ở Việt Nam do khí hậu nóng ẩm
    
    **Đặc điểm:**
    - Ngứa dữ dội
    - Tổn thương da khô, đỏ, bong vảy
    - Vị trí: Mặt, khuỷu tay, khoeo chân, cổ, thân mình
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán (Hanifin & Rajka)", expanded=True):
        st.markdown("""
        **Chẩn đoán khi có ≥3 tiêu chuẩn chính + ≥3 tiêu chuẩn phụ:**
        
        **Tiêu chuẩn chính (bắt buộc):**
        1. Ngứa
        2. Tổn thương da điển hình (vị trí, hình thái)
        3. Tiền sử bản thân/gia đình có bệnh dị ứng
        4. Bệnh mạn tính, tái phát
        
        **Tiêu chuẩn phụ:**
        - Da khô (xerosis)
        - Ichthyosis, lòng bàn tay dày
        - Phản ứng da tức thì dương tính
        - IgE tăng
        - Nhiễm trùng da tái phát
        - Viêm môi
        - Nếp gấp cổ
        - Viêm kết mạc tái phát
        - Đục giác mạc
        - Chàm núm vú
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: SEVERITY ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá mức độ")
    
    severity = st.radio(
        "**Mức độ bệnh:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="ad_severity"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **SCORAD Index (Scoring Atopic Dermatitis):**
        - **Nhẹ:** <25 điểm
        - **Trung bình:** 25-50 điểm
        - **Nặng:** >50 điểm
        
        **EASI Score:**
        - Đánh giá diện tích và mức độ
        - 0-72 điểm
        """)
    
    with col2:
        st.markdown("""
        **Đánh giá lâm sàng:**
        - **Nhẹ:** <5% diện tích, ngứa nhẹ
        - **Trung bình:** 5-20% diện tích, ngứa vừa
        - **Nặng:** >20% diện tích, ngứa nặng, ảnh hưởng giấc ngủ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    if severity == "Nhẹ":
        render_mild_treatment()
    elif severity == "Trung bình":
        render_moderate_treatment()
    else:
        render_severe_treatment()
    
    st.markdown("---")
    
    # ========== SECTION 4: TOPICAL TREATMENT ==========
    st.markdown("### 🧴 Điều trị tại chỗ")
    
    st.success("""
    **1. Dưỡng ẩm (QUAN TRỌNG NHẤT):**
    - **Mục tiêu:** Phục hồi hàng rào da
    - **Sản phẩm:** Kem dưỡng ẩm không mùi, không chất bảo quản
    - **Tần suất:** 2-3 lần/ngày, đặc biệt sau tắm
    - **Thời điểm:** Ngay sau tắm (trong vòng 3 phút)
    
    **2. Corticosteroid tại chỗ:**
    - **Nhẹ:** Hydrocortisone 1%, Clobetasone butyrate 0.05%
    - **Trung bình:** Betamethasone valerate 0.1%, Mometasone furoate 0.1%
    - **Nặng:** Clobetasol propionate 0.05%
    - **Cách dùng:** Bôi 1-2 lần/ngày, 7-14 ngày
    - **Lưu ý:** Giảm liều dần, không ngừng đột ngột
    
    **3. Calcineurin inhibitors (Tacrolimus, Pimecrolimus):**
    - **Chỉ định:** Vùng mặt, nếp gấp, trẻ em
    - **Tacrolimus 0.03-0.1%:** Bôi 2 lần/ngày
    - **Pimecrolimus 1%:** Bôi 2 lần/ngày
    - **Lưu ý:** Tránh ánh nắng, có thể gây bỏng rát ban đầu
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SYSTEMIC TREATMENT ==========
    st.markdown("### 💉 Điều trị toàn thân")
    
    st.warning("""
    **Chỉ định khi:**
    - Bệnh nặng, không đáp ứng điều trị tại chỗ
    - Tổn thương diện rộng
    - Ảnh hưởng chất lượng cuộc sống
    
    **1. Antihistamines (Giảm ngứa):**
    - **Cetirizine:** 10 mg/ngày (người lớn), 5 mg/ngày (trẻ 6-12 tuổi)
    - **Loratadine:** 10 mg/ngày
    - **Fexofenadine:** 180 mg/ngày
    - **Lưu ý:** Tác dụng an thần ở một số người
    
    **2. Corticosteroid đường uống (ngắn hạn):**
    - **Prednisolone:** 0.5-1 mg/kg/ngày, 5-7 ngày
    - **Chỉ dùng khi:** Bùng phát nặng, không dùng kéo dài
    
    **3. Cyclosporine:**
    - **Liều:** 3-5 mg/kg/ngày, chia 2 lần
    - **Theo dõi:** Huyết áp, chức năng thận, lipid máu
    - **Thời gian:** 3-6 tháng
    
    **4. Methotrexate:**
    - **Liều:** 7.5-15 mg/tuần (người lớn)
    - **Bổ sung:** Folic acid 5 mg/tuần
    - **Theo dõi:** Chức năng gan, công thức máu
    
    **5. Dupilumab (Monoclonal antibody - IL-4/13):**
    - **Liều:** 600 mg khởi đầu, sau đó 300 mg mỗi 2 tuần
    - **Chỉ định:** Bệnh trung bình-nặng, không kiểm soát được bằng thuốc bôi
    - **An toàn:** Dùng được cho trẻ em (tùy độ tuổi)

    **6. Tralokinumab (Anti-IL-13):**
    - **Liều:** 600 mg khởi đầu, sau đó 300 mg mỗi 2 tuần
    - **Chỉ định:** Người lớn bệnh trung bình-nặng
    
    **7. JAK Inhibitors (Thuốc uống mới - AAD 2024 Update):**
    - **Upadacitinib:** 15-30 mg/ngày
    - **Abrocitinib:** 100-200 mg/ngày
    - **Ưu điểm:** Tác dụng nhanh, giảm ngứa rất tốt
    - **⚠️ Lưu ý:** Cần sàng lọc TB, viêm gan B/C, theo dõi công thức máu, lipid. Black box warning về tim mạch/ung thư (dù hiếm ở nhóm AD trẻ).
    """)

    st.markdown("---")
    st.markdown("### 🧴 New Topical Therapies (Non-Steroidal)")
    st.info("""
    **1. Ruxolitinib Cream 1.5% (Topical JAKi):**
    - Dùng ngắn hạn cho bệnh nhẹ-trung bình
    - Hiệu quả nhanh, không gây teo da
    
    **2. Roflumilast Cream 0.3% / Foam (PDE4 Inhibitor):**
    - Dùng cho vùng da nếp gấp, mặt
    - Không gây châm chích như crisaborole
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: LIFESTYLE & PREVENTION ==========
    st.markdown("### 🏠 Chăm sóc và phòng ngừa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Tắm rửa:**
        - Tắm nước ấm (không nóng), 5-10 phút
        - Dùng sữa tắm không xà phòng, pH trung tính
        - Không chà xát mạnh
        - Thấm khô nhẹ nhàng (không chà)
        - Bôi dưỡng ẩm ngay sau tắm
        
        **Quần áo:**
        - Mặc quần áo cotton, rộng rãi
        - Tránh len, sợi tổng hợp
        - Giặt quần áo bằng xà phòng nhẹ
        """)
    
    with col2:
        st.markdown("""
        **Môi trường:**
        - Tránh nhiệt độ quá nóng/lạnh
        - Độ ẩm 40-60%
        - Tránh khói thuốc, bụi
        - Tránh dị nguyên: Phấn hoa, lông thú
        
        **Chế độ ăn:**
        - Tránh thực phẩm gây dị ứng (nếu có)
        - Bổ sung omega-3
        - Uống đủ nước
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Nhiễm trùng da:**
    - **Staphylococcus aureus:** Thường gặp nhất
    - **Herpes simplex (Eczema herpeticum):** Cấp cứu
    - **Điều trị:** Kháng sinh/kháng virus phù hợp
    
    **Biến chứng khác:**
    - Rối loạn giấc ngủ
    - Trầm cảm, lo âu
    - Ảnh hưởng chất lượng cuộc sống
    - Tăng nguy cơ hen suyễn, viêm mũi dị ứng
    
    **Dấu hiệu cần khám lại:**
    - Nhiễm trùng da (mủ, sốt)
    - Bệnh nặng hơn dù đã điều trị
    - Tác dụng phụ của thuốc
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Theo dõi định kỳ:**
    - **2 tuần:** Đánh giá đáp ứng điều trị
    - **1-3 tháng:** Đánh giá lại mức độ bệnh
    - **6-12 tháng:** Đánh giá toàn diện
    
    **Cần theo dõi khi dùng thuốc:**
    - **Cyclosporine:** Huyết áp, chức năng thận, lipid máu (mỗi tháng)
    - **Methotrexate:** Công thức máu, chức năng gan (mỗi 1-3 tháng)
    - **Corticosteroid tại chỗ:** Dấu hiệu teo da, giãn mạch
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    references = get_references("Atopic Dermatitis")
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
        1. **Eichenfield LF, et al. Guidelines of care for the management of atopic dermatitis.** J Am Acad Dermatol. 2014
        2. **Wollenberg A, et al. Consensus-based European guidelines for treatment of atopic eczema (atopic dermatitis) in adults and children.** J Eur Acad Dermatol Venereol. 2018
        3. **UpToDate:** Atopic dermatitis (eczema) - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_treatment():
    """Mild atopic dermatitis treatment"""
    st.success("## ⚠️ ĐIỀU TRỊ VIÊM DA CƠ ĐỊA MỨC ĐỘ NHẸ")
    
    st.markdown("""
    **Nguyên tắc:**
    1. Dưỡng ẩm tích cực (2-3 lần/ngày)
    2. Corticosteroid tại chỗ nhẹ (khi cần)
    3. Tránh yếu tố kích thích
    
    **Điều trị:**
    - **Dưỡng ẩm:** Bôi 2-3 lần/ngày, đặc biệt sau tắm
    - **Corticosteroid:** Hydrocortisone 1% hoặc Clobetasone butyrate 0.05%
      - Bôi 1-2 lần/ngày khi có tổn thương
      - Dùng 7-14 ngày, sau đó giảm dần
    - **Antihistamine:** Nếu ngứa nhiều (Cetirizine 10 mg/ngày)
    
    **Theo dõi:**
    - Tái khám sau 2-4 tuần
    - Đánh giá đáp ứng điều trị
    """)


def render_moderate_treatment():
    """Moderate atopic dermatitis treatment"""
    st.warning("## 🚨 ĐIỀU TRỊ VIÊM DA CƠ ĐỊA MỨC ĐỘ TRUNG BÌNH")
    
    st.markdown("""
    **Nguyên tắc:**
    1. Dưỡng ẩm tích cực
    2. Corticosteroid tại chỗ trung bình
    3. Calcineurin inhibitors (nếu cần)
    4. Antihistamines
    
    **Điều trị:**
    - **Dưỡng ẩm:** Bôi 2-3 lần/ngày
    - **Corticosteroid:** Betamethasone valerate 0.1% hoặc Mometasone furoate 0.1%
      - Bôi 1-2 lần/ngày
      - Dùng 2-4 tuần, sau đó giảm dần hoặc chuyển sang dưỡng ẩm
    - **Calcineurin inhibitors:** Tacrolimus 0.1% (vùng mặt, nếp gấp)
      - Bôi 2 lần/ngày, 2-4 tuần
    - **Antihistamine:** Cetirizine 10 mg/ngày hoặc Loratadine 10 mg/ngày
    
    **Theo dõi:**
    - Tái khám sau 2 tuần
    - Nếu không đáp ứng, xem xét điều trị toàn thân
    """)


def render_severe_treatment():
    """Severe atopic dermatitis treatment"""
    st.error("## 🚨🚨 ĐIỀU TRỊ VIÊM DA CƠ ĐỊA MỨC ĐỘ NẶNG")
    
    st.markdown("""
    **Nguyên tắc:**
    1. Dưỡng ẩm tích cực
    2. Corticosteroid tại chỗ mạnh (ngắn hạn)
    3. Điều trị toàn thân
    4. Xem xét Dupilumab
    
    **Điều trị tại chỗ:**
    - **Dưỡng ẩm:** Bôi 3-4 lần/ngày
    - **Corticosteroid:** Clobetasol propionate 0.05%
      - Bôi 1-2 lần/ngày, 1-2 tuần
      - Sau đó giảm dần sang loại nhẹ hơn
    
    **Điều trị toàn thân:**
    - **Corticosteroid (ngắn hạn):** Prednisolone 0.5-1 mg/kg/ngày, 5-7 ngày
    - **Cyclosporine:** 3-5 mg/kg/ngày, chia 2 lần
      - Theo dõi: Huyết áp, chức năng thận, lipid máu
    - **Methotrexate:** 7.5-15 mg/tuần
      - Bổ sung Folic acid 5 mg/tuần
    - **Dupilumab:** 600 mg khởi đầu, sau đó 300 mg mỗi 2 tuần
      - Chỉ định: Bệnh nặng, không đáp ứng điều trị khác
    
    **Theo dõi:**
    - Tái khám sau 1-2 tuần
    - Theo dõi tác dụng phụ của thuốc
    - Đánh giá đáp ứng điều trị
    """)

