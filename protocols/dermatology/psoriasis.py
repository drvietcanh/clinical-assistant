"""
Psoriasis (Vảy nến) Protocol
Chronic inflammatory skin disease
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Psoriasis (Vảy nến) Protocol"""
    st.subheader("🩹 Vảy nến (Psoriasis)")
    st.caption("Chronic inflammatory skin disease - Common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Bệnh viêm da mạn tính, tái phát
    - Tỷ lệ: 1-3% dân số
    - Phổ biến ở Việt Nam
    
    **Cơ chế:**
    - Tăng sinh tế bào da nhanh (3-4 ngày thay vì 28 ngày)
    - Viêm do tế bào T
    - Yếu tố di truyền, môi trường
    
    **Phân loại:**
    - **Mảng (Plaque):** 80-90%
    - **Giọt (Guttate):** 10%
    - **Mủ (Pustular):** Hiếm
    - **Đỏ da (Erythrodermic):** Hiếm, nặng
    - **Khớp (Arthritis):** 30% bệnh nhân
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Tiêu chuẩn chẩn đoán")
    
    with st.expander("🔍 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Triệu chứng:**
        1. **Tổn thương da:**
           - Mảng đỏ, có vảy bạc
           - Ranh giới rõ
           - Vị trí: Khuỷu tay, đầu gối, da đầu, thân mình
        
        2. **Dấu hiệu đặc trưng:**
           - **Auspitz sign:** Chảy máu khi cạo vảy
           - **Koebner phenomenon:** Tổn thương ở vùng chấn thương
        
        3. **Triệu chứng khác:**
           - Ngứa (50-80%)
           - Đau, nứt da
           - Tổn thương móng (50%)
           - Viêm khớp (30%)
        
        **Chẩn đoán:**
        - Chủ yếu dựa trên lâm sàng
        - Sinh thiết da (nếu không rõ)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: SEVERITY ASSESSMENT ==========
    st.markdown("### 📊 Đánh giá mức độ")
    
    severity = st.radio(
        "**Mức độ bệnh:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="psoriasis_severity"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **PASI Score (Psoriasis Area and Severity Index):**
        - **Nhẹ:** <7 điểm
        - **Trung bình:** 7-12 điểm
        - **Nặng:** >12 điểm
        
        **BSA (Body Surface Area):**
        - **Nhẹ:** <3%
        - **Trung bình:** 3-10%
        - **Nặng:** >10%
        """)
    
    with col2:
        st.markdown("""
        **Đánh giá lâm sàng:**
        - **Nhẹ:** <3% diện tích, ít ảnh hưởng
        - **Trung bình:** 3-10% diện tích
        - **Nặng:** >10% diện tích, ảnh hưởng nhiều
        
        **Yếu tố khác:**
        - Vị trí (mặt, bộ phận sinh dục)
        - Ảnh hưởng chất lượng cuộc sống
        - Viêm khớp
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    if severity == "Nhẹ":
        render_mild_psoriasis()
    elif severity == "Trung bình":
        render_moderate_psoriasis()
    else:
        render_severe_psoriasis()
    
    st.markdown("---")
    
    # ========== SECTION 4: TOPICAL TREATMENT ==========
    st.markdown("### 🧴 Điều trị tại chỗ")
    
    st.success("""
    **1. Corticosteroid tại chỗ:**
    - **Nhẹ-trung bình:** Betamethasone valerate 0.1%, Mometasone furoate 0.1%
    - **Nặng:** Clobetasol propionate 0.05%
    - **Cách dùng:** Bôi 1-2 lần/ngày, 2-4 tuần
    - **Lưu ý:** Giảm liều dần, tránh dùng lâu dài
    
    **2. Vitamin D analogues:**
    - **Calcipotriol 0.005%:** Bôi 2 lần/ngày
    - **Calcitriol 0.0003%:** Bôi 2 lần/ngày
    - **Tác dụng:** Giảm tăng sinh tế bào
    - **Lưu ý:** Có thể gây kích ứng, không dùng quá 100g/tuần
    
    **3. Retinoids:**
    - **Tazarotene 0.05-0.1%:** Bôi 1 lần/ngày
    - **Tác dụng:** Giảm tăng sinh, viêm
    - **Lưu ý:** Gây kích ứng, tránh khi có thai
    
    **4. Kết hợp:**
    - **Corticosteroid + Vitamin D:** Hiệu quả hơn
    - **Corticosteroid + Retinoid:** Giảm kích ứng
    
    **5. Dầu gội (cho da đầu):**
    - **Coal tar:** 2-5%
    - **Salicylic acid:** 2-10%
    - **Ketoconazole:** 2%
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: PHOTOTHERAPY ==========
    st.markdown("### ☀️ Quang trị liệu")
    
    st.warning("""
    **Chỉ định:**
    - Bệnh trung bình-nặng
    - Không đáp ứng điều trị tại chỗ
    - Tổn thương lan rộng
    
    **Loại:**
    - **UVB (Narrowband):** 311 nm, 2-3 lần/tuần
    - **PUVA (Psoralen + UVA):** Uống psoralen, chiếu UVA
    
    **Hiệu quả:**
    - 70-80% đáp ứng tốt
    - Cần 20-30 lần điều trị
    
    **Tác dụng phụ:**
    - Bỏng nắng
    - Lão hóa da
    - Tăng nguy cơ ung thư da (PUVA)
    
    **Chống chỉ định:**
    - Nhạy cảm ánh nắng
    - Uống thuốc nhạy cảm ánh nắng
    - Tiền sử ung thư da
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: SYSTEMIC TREATMENT ==========
    st.markdown("### 💉 Điều trị toàn thân")
    
    st.error("""
    **Chỉ định:**
    - Bệnh nặng (>10% BSA)
    - Không đáp ứng điều trị tại chỗ/quang trị liệu
    - Viêm khớp vảy nến
    - Ảnh hưởng chất lượng cuộc sống
    
    **1. Methotrexate:**
    - **Liều:** 7.5-25 mg/tuần
    - **Bổ sung:** Folic acid 5 mg/tuần
    - **Theo dõi:** Công thức máu, chức năng gan mỗi 1-3 tháng
    - **Hiệu quả:** 60-70%
    
    **2. Cyclosporine:**
    - **Liều:** 3-5 mg/kg/ngày, chia 2 lần
    - **Thời gian:** 3-6 tháng
    - **Theo dõi:** Huyết áp, chức năng thận, lipid máu
    - **Hiệu quả:** 70-80%
    
    **3. Acitretin:**
    - **Liều:** 25-50 mg/ngày
    - **Chống chỉ định:** Có thai, cho con bú
    - **Theo dõi:** Lipid máu, chức năng gan
    - **Hiệu quả:** 40-60%
    
    **4. Biologics (Cho bệnh nặng):**
    - **TNF-α inhibitors:** Adalimumab, Etanercept, Infliximab
    - **IL-17 inhibitors:** Secukinumab, Ixekizumab
    - **IL-23 inhibitors:** Ustekinumab, Guselkumab
    - **Hiệu quả:** 70-90%
    - **Lưu ý:** Đắt tiền, cần đánh giá kỹ, theo dõi nhiễm trùng
    """)
    
    st.markdown("---")
    
    # ========== SECTION 7: PSORIATIC ARTHRITIS ==========
    st.markdown("### 🦴 Viêm khớp vảy nến")
    
    st.info("""
    **Tỷ lệ:** 30% bệnh nhân vảy nến
    
    **Triệu chứng:**
    - Đau, sưng khớp
    - Cứng khớp buổi sáng
    - Tổn thương móng
    - Viêm ngón tay/chân (dactylitis)
    
    **Điều trị:**
    - **NSAIDs:** Giảm đau, viêm
    - **DMARDs:** Methotrexate, Sulfasalazine
    - **Biologics:** TNF-α inhibitors, IL-17 inhibitors
    - **Corticosteroid:** Tiêm khớp (nếu cần)
    
    **Theo dõi:**
    - Đánh giá chức năng khớp
    - X-quang khớp
    - Điều trị phối hợp da và khớp
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: LIFESTYLE ==========
    st.markdown("### 🏠 Chăm sóc")
    
    st.markdown("""
    **Chăm sóc da:**
    - Dưỡng ẩm thường xuyên
    - Tắm nước ấm (không nóng)
    - Tránh chà xát mạnh
    - Bảo vệ da khỏi chấn thương
    
    **Lối sống:**
    - Tránh stress
    - Tập thể dục
    - Tránh hút thuốc, rượu
    - Giảm cân (nếu béo phì)
    
    **Chế độ ăn:**
    - Cân bằng, đủ dinh dưỡng
    - Một số bệnh nhân cải thiện với chế độ ăn đặc biệt
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Biến chứng:**
    - **Viêm khớp vảy nến:** 30% bệnh nhân
    - **Bệnh tim mạch:** Tăng nguy cơ
    - **Hội chứng chuyển hóa:** Béo phì, đái tháo đường
    - **Trầm cảm, lo âu:** Ảnh hưởng chất lượng cuộc sống
    
    **Biến chứng điều trị:**
    - Teo da (corticosteroid)
    - Ảnh hưởng gan, thận (methotrexate, cyclosporine)
    - Nhiễm trùng (biologics)
    - Tăng nguy cơ ung thư (một số thuốc)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 10: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Theo dõi điều trị:**
    - **2-4 tuần:** Đánh giá đáp ứng ban đầu
    - **8-12 tuần:** Đánh giá hiệu quả
    - **3-6 tháng:** Đánh giá toàn diện
    
    **Khi dùng thuốc toàn thân:**
    - **Methotrexate:** Công thức máu, chức năng gan mỗi 1-3 tháng
    - **Cyclosporine:** Huyết áp, chức năng thận, lipid máu mỗi tháng
    - **Biologics:** Theo dõi nhiễm trùng, đáp ứng điều trị
    
    **Dấu hiệu cần khám lại:**
    - Không đáp ứng sau 8-12 tuần
    - Tác dụng phụ
    - Bùng phát nặng
    - Viêm khớp
    """)
    
    st.markdown("---")
    
    # ========== SECTION 11: REFERENCES ==========
    references = get_references("Psoriasis")
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
        1. **Menter A, et al. Guidelines of care for the management of psoriasis and psoriatic arthritis.** J Am Acad Dermatol. 2019
        2. **Nast A, et al. European S3-Guidelines on the systemic treatment of psoriasis vulgaris.** J Eur Acad Dermatol Venereol. 2015
        3. **UpToDate:** Psoriasis - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_psoriasis():
    """Mild psoriasis treatment"""
    st.success("## ⚠️ ĐIỀU TRỊ VẢY NẾN MỨC ĐỘ NHẸ")
    
    st.markdown("""
    **Điều trị tại chỗ:**
    - **Corticosteroid:** Betamethasone valerate 0.1% hoặc Mometasone furoate 0.1%
      - Bôi 1-2 lần/ngày, 2-4 tuần
    - **Vitamin D:** Calcipotriol 0.005%
      - Bôi 2 lần/ngày
    - **Kết hợp:** Corticosteroid + Vitamin D (hiệu quả hơn)
    
    **Theo dõi:** Tái khám sau 4-8 tuần
    """)


def render_moderate_psoriasis():
    """Moderate psoriasis treatment"""
    st.warning("## 🚨 ĐIỀU TRỊ VẢY NẾN MỨC ĐỘ TRUNG BÌNH")
    
    st.markdown("""
    **Phác đồ 1: Điều trị tại chỗ tích cực**
    - **Corticosteroid mạnh:** Clobetasol propionate 0.05%
      - Bôi 1-2 lần/ngày, 2 tuần
    - **Vitamin D:** Calcipotriol 0.005%
      - Bôi 2 lần/ngày
    - **Kết hợp:** Luân phiên hoặc kết hợp
    
    **Phác đồ 2: Quang trị liệu**
    - **UVB narrowband:** 2-3 lần/tuần
    - Hoặc kết hợp với điều trị tại chỗ
    
    **Phác đồ 3: Điều trị toàn thân (nếu cần)**
    - **Methotrexate:** 7.5-15 mg/tuần
    - Hoặc **Acitretin:** 25-50 mg/ngày
    
    **Theo dõi:** Tái khám sau 2-4 tuần
    """)


def render_severe_psoriasis():
    """Severe psoriasis treatment"""
    st.error("## 🚨🚨 ĐIỀU TRỊ VẢY NẾN MỨC ĐỘ NẶNG")
    
    st.markdown("""
    **Phác đồ 1: Quang trị liệu + Điều trị tại chỗ**
    - **UVB narrowband:** 2-3 lần/tuần
    - **Corticosteroid tại chỗ:** Khi cần
    
    **Phác đồ 2: Điều trị toàn thân**
    - **Methotrexate:** 15-25 mg/tuần
      - Bổ sung Folic acid 5 mg/tuần
    - **Cyclosporine:** 3-5 mg/kg/ngày
      - Thời gian: 3-6 tháng
    - **Acitretin:** 25-50 mg/ngày
    
    **Phác đồ 3: Biologics (Nếu không đáp ứng)**
    - **TNF-α inhibitors:** Adalimumab, Etanercept
    - **IL-17 inhibitors:** Secukinumab, Ixekizumab
    - **IL-23 inhibitors:** Ustekinumab, Guselkumab
    
    **Theo dõi:**
    - Tái khám sau 2 tuần
    - Theo dõi tác dụng phụ
    - Đánh giá đáp ứng điều trị
    """)

