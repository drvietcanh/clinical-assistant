"""
Chronic Constipation Treatment Protocol
ACG 2021, AGA 2021 Guidelines
Management of chronic constipation
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Chronic Constipation Treatment Protocol"""
    st.subheader("🫀 Điều Trị Táo Bón Mạn Tính (Chronic Constipation)")
    st.caption("ACG 2021, AGA 2021 - Management of chronic constipation")
    
    st.info("""
    **Táo bón mạn tính:**
    - Tỷ lệ ở Việt Nam: ~10-15% dân số
    - Định nghĩa: <3 lần đại tiện/tuần hoặc khó đại tiện ≥3 tháng
    - Phân loại:
      - **Functional constipation:** Không có nguyên nhân thực thể
      - **Slow transit:** Vận động ruột chậm
      - **Outlet obstruction:** Rối loạn đại tiện
    - Nguyên nhân: Chế độ ăn, lối sống, thuốc, bệnh lý
    
    **Triệu chứng:**
    - Phân cứng, khó đại tiện
    - Cảm giác không hết phân
    - Phải rặn nhiều
    - Đầy bụng, khó chịu
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Chẩn Đoán")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Tiêu Chuẩn Rome IV")
        st.info("""
        **Chẩn đoán khi có ≥2 trong số:**
        1. Đại tiện <3 lần/tuần
        2. Phân cứng >25% thời gian
        3. Phải rặn >25% thời gian
        4. Cảm giác tắc nghẽn >25% thời gian
        5. Cảm giác không hết phân >25% thời gian
        6. Phải dùng tay hỗ trợ >25% thời gian
        
        **Thời gian:** ≥3 tháng
        """)
        
        symptoms = st.multiselect(
            "**Triệu chứng bệnh nhân:**",
            ["Đại tiện <3 lần/tuần", "Phân cứng", "Phải rặn", "Cảm giác tắc nghẽn", "Cảm giác không hết phân", "Phải dùng tay hỗ trợ"],
            key="constipation_symptoms"
        )
    
    with col2:
        st.markdown("#### Đánh Giá")
        frequency = st.number_input(
            "**Số lần đại tiện/tuần:**",
            min_value=0,
            max_value=14,
            value=2,
            key="constipation_frequency"
        )
        
        stool_type = st.selectbox(
            "**Loại phân (Bristol Stool Scale):**",
            ["Type 1 (Cứng, rời rạc)", "Type 2 (Lổn nhổn)", "Type 3 (Có vết nứt)", "Type 4 (Mềm, mịn)", "Type 5-7 (Lỏng)"],
            key="stool_type"
        )
        
        duration = st.number_input(
            "**Thời gian (tháng):**",
            min_value=1,
            max_value=120,
            value=6,
            key="constipation_duration"
        )
        
        red_flags = st.checkbox("**Có dấu hiệu cảnh báo (giảm cân, máu trong phân, thiếu máu)**", key="constipation_red_flags")
    
    st.markdown("---")
    
    if red_flags:
        st.error("""
        **⚠️ DẤU HIỆU CẢNH BÁO - CẦN ĐÁNH GIÁ THÊM:**
        - Nội soi đại tràng
        - Xét nghiệm máu (CBC, TSH, Ca, glucose)
        - Loại trừ: Khối u, bệnh thần kinh, rối loạn chuyển hóa
        """)
    
    st.markdown("### 💊 Điều Trị")
    
    st.markdown("#### 1. Thay Đổi Lối Sống")
    
    with st.expander("📋 Xem khuyến cáo thay đổi lối sống", expanded=True):
        st.markdown("""
        **1. Chế độ ăn:**
        - **Tăng chất xơ:** 25-30g/ngày
          - Trái cây: Táo, lê, mận
          - Rau: Bông cải, cà rốt, đậu
          - Ngũ cốc: Yến mạch, gạo lứt
        - **Uống đủ nước:** 1.5-2L/ngày
        - **Tránh:** Thức ăn chế biến sẵn, ít chất xơ
        
        **2. Tập thể dục:**
        - **Aerobic:** ≥30 phút/ngày, 5 ngày/tuần
        - **Đi bộ:** Đơn giản, hiệu quả
        - **Tăng hoạt động:** Thay đổi thói quen
        
        **3. Thói quen đại tiện:**
        - **Thời gian:** Sau bữa ăn (tận dụng gastrocolic reflex)
        - **Tư thế:** Ngồi xổm hoặc nâng chân
        - **Không nhịn:** Đi ngay khi có cảm giác
        """)
    
    st.markdown("#### 2. Thuốc Điều Trị")
    
    treatment_category = st.selectbox(
        "**Nhóm thuốc:**",
        [
            "Chất xơ (Fiber supplements) - First-line",
            "Osmotic laxatives (Lợi tiểu thẩm thấu)",
            "Stimulant laxatives (Kích thích nhu động)",
            "Prokinetics (Tăng vận động ruột)",
            "Secretagogues (Tăng tiết dịch)",
            "Lubricants (Bôi trơn)"
        ],
        key="constipation_treatment_category"
    )
    
    st.markdown("---")
    
    if "Chất xơ" in treatment_category or "Fiber" in treatment_category:
        render_fiber()
    elif "Osmotic" in treatment_category or "thẩm thấu" in treatment_category:
        render_osmotic()
    elif "Stimulant" in treatment_category or "Kích thích" in treatment_category:
        render_stimulant()
    elif "Prokinetics" in treatment_category or "vận động" in treatment_category:
        render_prokinetics()
    elif "Secretagogues" in treatment_category or "tiết dịch" in treatment_category:
        render_secretagogues()
    else:
        render_lubricants()
    
    st.markdown("---")
    
    st.markdown("### 📋 Phác Đồ Điều Trị Theo Bước")
    
    st.markdown("#### Bước 1: Thay Đổi Lối Sống")
    
    st.success("""
    - Tăng chất xơ (25-30g/ngày)
    - Uống đủ nước (1.5-2L/ngày)
    - Tập thể dục (≥30 phút/ngày)
    - Thay đổi thói quen đại tiện
    - **Thời gian:** 4-8 tuần
    """)
    
    st.markdown("#### Bước 2: Chất Xơ Bổ Sung")
    
    st.info("""
    - **Psyllium:** 3-5g x 2-3 lần/ngày
    - **Methylcellulose:** 2-4g x 2-3 lần/ngày
    - **Polycarbophil:** 1g x 2-4 lần/ngày
    - **Uống với nhiều nước**
    - **Thời gian:** 4-8 tuần
    """)
    
    st.markdown("#### Bước 3: Osmotic Laxatives")
    
    st.info("""
    - **Polyethylene glycol (PEG):** 17-34g/ngày
    - **Lactulose:** 15-30mL x 1-2 lần/ngày
    - **Magnesium hydroxide:** 30-60mL/ngày
    - **An toàn:** Có thể dùng dài hạn
    """)
    
    st.markdown("#### Bước 4: Nếu Không Đáp Ứng")
    
    st.warning("""
    - **Stimulant laxatives:** Senna, Bisacodyl (ngắn hạn)
    - **Prokinetics:** Prucalopride, Linaclotide
    - **Secretagogues:** Lubiprostone, Plecanatide
    - **Đánh giá lại:** Có thể cần chuyên khoa
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Nhóm Bệnh Nhân Đặc Biệt")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người Cao Tuổi:**
        - Nguy cơ cao hơn
        - Cẩn thận với thuốc (tương tác)
        - PEG an toàn
        - Tránh stimulant dài hạn
        
        **Có Thai:**
        - **An toàn:** PEG, Lactulose
        - **Tránh:** Stimulant, Mineral oil
        - Tăng chất xơ, uống nước
        """)
    
    with col2:
        st.markdown("""
        **Trẻ Em:**
        - Nguyên nhân thường khác
        - **PEG:** An toàn, liều tính theo kg
        - **Lactulose:** Có thể dùng
        - Tăng chất xơ, uống nước
        
        **Dùng Thuốc:**
        - Đánh giá thuốc gây táo bón
        - Opioid, anticholinergic, sắt
        - Cân nhắc thay đổi hoặc điều chỉnh
        """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Danh Sách Kiểm Tra")
    
    checklist_items = [
        "✅ Đánh giá triệu chứng theo Rome IV",
        "✅ Loại trừ dấu hiệu cảnh báo (nếu có)",
        "✅ Tư vấn thay đổi lối sống (chất xơ, nước, tập thể dục)",
        "✅ Bắt đầu chất xơ bổ sung nếu cần",
        "✅ Thêm osmotic laxative nếu không đáp ứng",
        "✅ Đánh giá đáp ứng sau 4-8 tuần",
        "✅ Điều chỉnh điều trị nếu cần",
        "✅ Đánh giá thuốc gây táo bón",
        "✅ Tư vấn về thói quen đại tiện"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 📚 Tài liệu tham khảo")
    
    st.markdown("""
    1. **ACG 2021 Guidelines**
       - Bharucha AE, Lacy BE. Am J Gastroenterol. 2021
    
    2. **AGA 2021 Guidelines**
       - Rao SSC, et al. Gastroenterology. 2021
    
    3. **UpToDate:** Management of chronic constipation in adults
       - Last updated: 2024
    """)
    
    st.markdown("---")
    
    # References section
    references = get_references("Chronic Constipation")
    if references:
        render_references_section(
            references=references,
            title="📚 Tài liệu tham khảo",
            last_updated="2024-01-15",
            show_evidence_level=True,
            show_links=True
        )
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_fiber():
    """Fiber Supplements"""
    st.success("## 💊 Chất Xơ Bổ Sung (First-line)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Psyllium (Metamucil):**
    - **Liều:** 3-5g x 2-3 lần/ngày
    - **Cách dùng:** Pha với nước, uống ngay
    - **Tác dụng:** Tăng khối lượng phân, làm mềm phân
    
    **Methylcellulose (Citrucel):**
    - **Liều:** 2-4g x 2-3 lần/ngày
    - **Cách dùng:** Pha với nước
    - **Ưu điểm:** Ít gây đầy hơi hơn psyllium
    
    **Polycarbophil (FiberCon):**
    - **Liều:** 1g x 2-4 lần/ngày
    - **Cách dùng:** Uống với nước
    - **Ưu điểm:** Không cần pha
    
    **Lưu ý:**
    - Uống với nhiều nước (quan trọng!)
    - Bắt đầu liều thấp, tăng dần
    - Có thể gây đầy hơi ban đầu
    """)


def render_osmotic():
    """Osmotic Laxatives"""
    st.success("## 💊 Osmotic Laxatives (Lợi Tiểu Thẩm Thấu)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Polyethylene Glycol (PEG):**
    - **Liều:** 17-34g/ngày
    - **Cách dùng:** Pha với nước, uống 1 lần/ngày
    - **An toàn:** Có thể dùng dài hạn
    - **Hiệu quả:** Tốt
    
    **Lactulose:**
    - **Liều:** 15-30mL x 1-2 lần/ngày
    - **Cách dùng:** Uống trực tiếp hoặc pha với nước
    - **Tác dụng phụ:** Đầy hơi, chuột rút
    
    **Magnesium Hydroxide (Milk of Magnesia):**
    - **Liều:** 30-60mL/ngày
    - **Cách dùng:** Uống trực tiếp
    - **Lưu ý:** Tránh ở suy thận
    
    **Sorbitol:**
    - **Liều:** 15-30mL x 1-2 lần/ngày
    - **Tương tự:** Lactulose
    """)


def render_stimulant():
    """Stimulant Laxatives"""
    st.warning("## 💊 Stimulant Laxatives (Kích Thích Nhu Động)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Senna:**
    - **Liều:** 15-30mg/ngày
    - **Cách dùng:** Uống trước khi ngủ
    - **Tác dụng:** Sau 6-12 giờ
    
    **Bisacodyl:**
    - **Liều:** 5-15mg/ngày
    - **Cách dùng:** Uống hoặc đặt hậu môn
    - **Tác dụng:** Sau 6-12 giờ
    
    **Lưu ý:**
    - Chỉ dùng ngắn hạn (1-2 tuần)
    - Không dùng dài hạn (nguy cơ phụ thuộc)
    - Có thể gây chuột rút, tiêu chảy
    """)


def render_prokinetics():
    """Prokinetics"""
    st.info("## 💊 Prokinetics (Tăng Vận Động Ruột)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Prucalopride:**
    - **Liều:** 2mg x 1 lần/ngày
    - **Chỉ định:** Táo bón mạn tính không đáp ứng
    - **Tác dụng phụ:** Đau đầu, buồn nôn, tiêu chảy
    
    **Lưu ý:**
    - Chỉ dùng khi không đáp ứng với điều trị khác
    - Cần đánh giá chuyên khoa
    """)


def render_secretagogues():
    """Secretagogues"""
    st.info("## 💊 Secretagogues (Tăng Tiết Dịch)")
    
    st.markdown("### Liều Dùng")
    
    st.info("""
    **Lubiprostone:**
    - **Liều:** 24mcg x 2 lần/ngày
    - **Chỉ định:** Táo bón mạn tính không đáp ứng
    - **Tác dụng phụ:** Buồn nôn, tiêu chảy
    
    **Plecanatide:**
    - **Liều:** 3mg x 1 lần/ngày
    - **Chỉ định:** Táo bón mạn tính
    - **Tác dụng phụ:** Tiêu chảy
    
    **Lưu ý:**
    - Chỉ dùng khi không đáp ứng với điều trị khác
    - Cần đánh giá chuyên khoa
    """)


def render_lubricants():
    """Lubricants"""
    st.info("## 💊 Lubricants (Bôi Trơn)")
    
    st.markdown("### Liều Dùng")
    
    st.warning("""
    **Mineral Oil:**
    - **Liều:** 15-45mL/ngày
    - **Cách dùng:** Uống hoặc thụt
    - **Lưu ý:** 
      - Tránh ở trẻ em, có thai, người cao tuổi
      - Nguy cơ hít sặc (aspiration)
      - Giảm hấp thu vitamin tan trong dầu
    
    **Glycerin Suppository:**
    - **Liều:** 1 suppository khi cần
    - **Cách dùng:** Đặt hậu môn
    - **An toàn:** Có thể dùng khi cần
    """)

