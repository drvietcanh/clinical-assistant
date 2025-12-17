"""
Acne Vulgaris (Mụn trứng cá) Protocol
Common inflammatory skin condition
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acne Vulgaris (Mụn trứng cá) Protocol"""
    st.subheader("🩹 Mụn trứng cá (Acne Vulgaris)")
    st.caption("Common inflammatory skin condition - Very common in Vietnam")
    
    st.info("""
    **Định nghĩa:**
    - Bệnh viêm nang lông-tuyến bã
    - Phổ biến ở thanh thiếu niên (85%), người lớn (12-50%)
    - Tỷ lệ cao ở Việt Nam do khí hậu nóng ẩm
    
    **Cơ chế:**
    1. Tăng sản xuất bã nhờn
    2. Tăng sừng hóa nang lông
    3. Nhiễm khuẩn Propionibacterium acnes
    4. Viêm
    
    **Yếu tố nguy cơ:**
    - Hormone (dậy thì, chu kỳ kinh)
    - Di truyền
    - Mỹ phẩm, stress
    - Một số thuốc (corticosteroid, lithium)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📋 Phân loại")
    
    severity = st.radio(
        "**Mức độ mụn:**",
        ["Nhẹ", "Trung bình", "Nặng", "Rất nặng"],
        key="acne_severity"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Nhẹ:**
        - Mụn đầu đen, đầu trắng
        - <10 mụn viêm
        - Không có nốt sâu
        
        **Trung bình:**
        - 10-40 mụn viêm
        - Có thể có nốt nhỏ
        - Tổn thương vừa phải
        """)
    
    with col2:
        st.markdown("""
        **Nặng:**
        - >40 mụn viêm
        - Nhiều nốt sâu
        - Tổn thương lan rộng
        
        **Rất nặng:**
        - Mụn nốt lớn, sâu
        - Sẹo nhiều
        - Mụn đỏ, đau
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    if severity == "Nhẹ":
        render_mild_acne()
    elif severity == "Trung bình":
        render_moderate_acne()
    elif severity == "Nặng":
        render_severe_acne()
    else:
        render_very_severe_acne()
    
    st.markdown("---")
    
    # ========== SECTION 3: TOPICAL TREATMENT ==========
    st.markdown("### 🧴 Điều trị tại chỗ")
    
    st.success("""
    **1. Retinoids (Tretinoin, Adapalene):**
    - **Tretinoin 0.025-0.1%:** Bôi tối, 1 lần/ngày
    - **Adapalene 0.1-0.3%:** Bôi tối, 1 lần/ngày
    - **Lưu ý:** Có thể gây kích ứng, khô da ban đầu
    - **Cách dùng:** Bôi mỏng, tránh vùng mắt, dùng kem chống nắng
    
    **2. Benzoyl Peroxide (BPO):**
    - **2.5-10%:** Bôi 1-2 lần/ngày
    - **Tác dụng:** Diệt khuẩn, giảm viêm
    - **Lưu ý:** Có thể làm khô da, tẩy màu quần áo
    
    **3. Kháng sinh tại chỗ:**
    - **Clindamycin 1%:** Bôi 2 lần/ngày
    - **Erythromycin 2%:** Bôi 2 lần/ngày
    - **Lưu ý:** Không dùng đơn độc, kết hợp với BPO hoặc retinoid
    
    **4. Azelaic Acid:**
    - **15-20%:** Bôi 2 lần/ngày
    - **Tác dụng:** Giảm viêm, giảm sắc tố
    
    **5. Salicylic Acid:**
    - **0.5-2%:** Bôi 1-2 lần/ngày
    - **Tác dụng:** Tẩy tế bào chết, thông thoáng nang lông
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: SYSTEMIC TREATMENT ==========
    st.markdown("### 💉 Điều trị toàn thân")
    
    st.warning("""
    **Chỉ định:**
    - Mụn trung bình-nặng
    - Không đáp ứng điều trị tại chỗ
    - Mụn ở lưng, ngực
    - Nguy cơ sẹo
    
    **1. Kháng sinh đường uống:**
    - **Doxycycline:** 50-100 mg, 2 lần/ngày
    - **Minocycline:** 50-100 mg, 2 lần/ngày
    - **Tetracycline:** 250-500 mg, 2 lần/ngày
    - **Thời gian:** 3-6 tháng
    - **Lưu ý:** Uống khi no, tránh ánh nắng, không dùng khi có thai
    
    **2. Isotretinoin (Accutane):**
    - **Liều:** 0.5-1 mg/kg/ngày, 4-6 tháng
    - **Chỉ định:** Mụn nặng, không đáp ứng điều trị khác
    - **Tác dụng phụ:** Khô da, môi, tăng lipid máu, ảnh hưởng gan
    - **CHỐNG CHỈ ĐỊNH:** Có thai, cho con bú (phải tránh thai)
    - **Theo dõi:** Lipid máu, chức năng gan, công thức máu
    
    **3. Hormone (cho nữ):**
    - **OCP (Oral Contraceptive Pills):** Chứa estrogen + progestin
    - **Spironolactone:** 50-200 mg/ngày
    - **Chỉ định:** Mụn liên quan hormone, mụn ở nữ trưởng thành
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: COMBINATION THERAPY ==========
    st.markdown("### 🔄 Phác đồ kết hợp")
    
    st.markdown("""
    **Phác đồ đầu tay (Nhẹ-Trung bình):**
    - **Retinoid tại chỗ** (tối) + **BPO** (sáng)
    - Hoặc: **Adapalene + BPO** (kết hợp sẵn)
    
    **Phác đồ thay thế:**
    - **Retinoid** + **Kháng sinh tại chỗ**
    - **BPO** + **Kháng sinh tại chỗ**
    
    **Phác đồ nặng:**
    - **Điều trị tại chỗ** + **Kháng sinh đường uống**
    - Sau 3-6 tháng: Giảm kháng sinh, tiếp tục tại chỗ
    
    **Phác đồ rất nặng:**
    - **Isotretinoin** (có thể kết hợp kháng sinh ngắn hạn)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 6: LIFESTYLE ==========
    st.markdown("### 🏠 Chăm sóc da")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Rửa mặt:**
        - Rửa 2 lần/ngày (sáng, tối)
        - Dùng sữa rửa mặt nhẹ, pH trung tính
        - Không chà xát mạnh
        - Thấm khô nhẹ nhàng
        
        **Dưỡng ẩm:**
        - Dùng kem dưỡng ẩm không gây mụn (non-comedogenic)
        - Tránh kem quá dầu
        """)
    
    with col2:
        st.markdown("""
        **Chống nắng:**
        - Bắt buộc khi dùng retinoid, isotretinoin
        - SPF 30+, không gây mụn
        - Bôi lại mỗi 2-3 giờ
        
        **Tránh:**
        - Nặn mụn (gây viêm, sẹo)
        - Mỹ phẩm gây bít tắc
        - Stress, thiếu ngủ
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Theo dõi điều trị:**
    - **2-4 tuần:** Đánh giá đáp ứng ban đầu
    - **8-12 tuần:** Đánh giá hiệu quả
    - **3-6 tháng:** Đánh giá toàn diện
    
    **Khi dùng Isotretinoin:**
    - **Trước điều trị:** Lipid máu, chức năng gan, công thức máu, test thai (nữ)
    - **Mỗi tháng:** Lipid máu, chức năng gan, test thai (nữ)
    - **Theo dõi:** Tác dụng phụ, đáp ứng điều trị
    
    **Dấu hiệu cần khám lại:**
    - Không đáp ứng sau 8-12 tuần
    - Tác dụng phụ nặng
    - Nhiễm trùng da
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: COMPLICATIONS ==========
    st.markdown("### ⚠️ Biến chứng")
    
    st.info("""
    **Sẹo:**
    - Sẹo lõm, sẹo phì đại
    - Phòng ngừa: Điều trị sớm, không nặn mụn
    - Điều trị: Laser, lăn kim, filler
    
    **Tăng sắc tố sau viêm:**
    - Thường gặp ở da sẫm màu
    - Điều trị: Retinoid, azelaic acid, hydroquinone
    
    **Tác dụng phụ thuốc:**
    - Kích ứng da (retinoid, BPO)
    - Kháng kháng sinh
    - Ảnh hưởng gan, lipid (isotretinoin)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    references = get_references("Acne Vulgaris")
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
        1. **Zaenglein AL, et al. Guidelines of care for the management of acne vulgaris.** J Am Acad Dermatol. 2016
        2. **Thiboutot D, et al. Practical management of acne for clinicians: An international consensus from the Global Alliance to Improve Outcomes in Acne.** J Am Acad Dermatol. 2018
        3. **UpToDate:** Acne vulgaris - Last updated 2024
        4. **Hướng dẫn chẩn đoán và điều trị bệnh da liễu - Bộ Y tế Việt Nam**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_acne():
    """Mild acne treatment"""
    st.success("## ⚠️ ĐIỀU TRỊ MỤN NHẸ")
    
    st.markdown("""
    **Điều trị tại chỗ:**
    - **Retinoid:** Adapalene 0.1% hoặc Tretinoin 0.025% (tối)
    - **BPO:** 2.5-5% (sáng)
    - Hoặc: **Adapalene + BPO** (kết hợp)
    
    **Thời gian:** 8-12 tuần
    
    **Theo dõi:** Tái khám sau 4-8 tuần
    """)


def render_moderate_acne():
    """Moderate acne treatment"""
    st.warning("## 🚨 ĐIỀU TRỊ MỤN TRUNG BÌNH")
    
    st.markdown("""
    **Phác đồ 1 (Điều trị tại chỗ):**
    - **Retinoid** (tối) + **BPO** (sáng)
    - Hoặc: **Retinoid + Kháng sinh tại chỗ**
    
    **Phác đồ 2 (Kết hợp):**
    - **Điều trị tại chỗ** + **Kháng sinh đường uống**
    - Doxycycline 50-100 mg, 2 lần/ngày
    - Thời gian: 3-6 tháng
    
    **Theo dõi:** Tái khám sau 4 tuần, sau đó mỗi 8-12 tuần
    """)


def render_severe_acne():
    """Severe acne treatment"""
    st.error("## 🚨🚨 ĐIỀU TRỊ MỤN NẶNG")
    
    st.markdown("""
    **Phác đồ 1:**
    - **Điều trị tại chỗ** + **Kháng sinh đường uống**
    - Doxycycline 100 mg, 2 lần/ngày
    - Thời gian: 3-6 tháng
    
    **Phác đồ 2 (Nếu không đáp ứng):**
    - **Isotretinoin:** 0.5-1 mg/kg/ngày
    - Thời gian: 4-6 tháng
    - Theo dõi: Lipid máu, chức năng gan mỗi tháng
    
    **Theo dõi:** Tái khám sau 2-4 tuần
    """)


def render_very_severe_acne():
    """Very severe acne treatment"""
    st.error("## 🚨🚨🚨 ĐIỀU TRỊ MỤN RẤT NẶNG")
    
    st.markdown("""
    **Điều trị chính:**
    - **Isotretinoin:** 0.5-1 mg/kg/ngày
    - Thời gian: 4-6 tháng
    - Tổng liều: 120-150 mg/kg
    
    **Có thể kết hợp:**
    - Kháng sinh đường uống ngắn hạn (1-2 tháng đầu)
    - Corticosteroid đường uống (nếu viêm nặng)
    
    **Theo dõi:**
    - Lipid máu, chức năng gan, công thức máu mỗi tháng
    - Test thai (nữ) mỗi tháng
    - Đánh giá đáp ứng điều trị
    
    **Lưu ý:**
    - CHỐNG CHỈ ĐỊNH: Có thai, cho con bú
    - Phải tránh thai ít nhất 1 tháng trước, trong và sau điều trị
    """)

