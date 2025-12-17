"""
Acute Intestinal Obstruction Protocol
WSES 2019, EAST 2020
Management of acute intestinal obstruction
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Intestinal Obstruction Protocol"""
    st.subheader("🫀 Acute Intestinal Obstruction")
    st.caption("WSES 2019, EAST 2020 - Management of acute intestinal obstruction")
    
    st.warning("""
    **⚠️ ACUTE INTESTINAL OBSTRUCTION = URGENT ASSESSMENT REQUIRED**
    
    **Triệu chứng:**
    - Đau bụng, đau quặn
    - Nôn, nôn ra dịch mật
    - Bí trung đại tiện
    - Bụng chướng
    - Tăng nhu động ruột (early) → Giảm nhu động (late)
    
    **Cần phân biệt: Mechanical vs Paralytic**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại")
    
    obstruction_type = st.radio(
        "**Loại tắc ruột:**",
        ["Small Bowel Obstruction (SBO)", "Large Bowel Obstruction (LBO)", "Paralytic Ileus"],
        key="obstruction_type"
    )
    
    st.markdown("---")
    
    if obstruction_type == "Small Bowel Obstruction (SBO)":
        render_sbo_protocol()
    elif obstruction_type == "Large Bowel Obstruction (LBO)":
        render_lbo_protocol()
    else:
        render_paralytic_ileus_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 2: INITIAL ASSESSMENT ==========
    st.markdown("### ⚡ Đánh giá Ban Đầu")
    
    with st.expander("🔍 Xem đánh giá ban đầu", expanded=True):
        st.markdown("""
        **1. ABC (Airway, Breathing, Circulation):**
        - **Airway:** Đảm bảo thông thoáng
        - **Breathing:** Đánh giá suy hô hấp (do chướng bụng)
        - **Circulation:** Đánh giá shock, tưới máu
        
        **2. Dấu hiệu nguy hiểm:**
        - Peritonitis
        - Free air
        - Strangulation (đau liên tục, sốt, tăng WBC)
        - Shock
        - Lú lẫn
        
        **3. Xét nghiệm cần thiết:**
        - **CBC:** Tăng WBC nếu strangulation
        - **BMP:** Điện giải, chức năng thận
        - **Lactate:** Tăng nếu strangulation
        - **ABG:** Acidosis nếu nặng
        - **Plain X-ray:** Đánh giá mức nước-mức hơi
        - **CT:** Tiêu chuẩn vàng (độ nhạy > 95%)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: RESUSCITATION ==========
    st.markdown("### 💉 Resuscitation")
    
    st.markdown("""
    **1. Fluid Resuscitation:**
    - **NS/LR:** 1-2 L bolus
    - **Mục tiêu:** MAP ≥ 65 mmHg
    - **Theo dõi:** CVP, lượng nước tiểu
    
    **2. NG Tube:**
    - **Chỉ định:** Tất cả trừ paralytic ileus nhẹ
    - **Mục tiêu:** Giảm chướng bụng, giảm nôn
    - **Theo dõi:** Lượng dịch hút
    
    **3. Electrolytes:**
    - **K+:** Bổ sung nếu giảm
    - **Na+:** Điều chỉnh nếu rối loạn
    - **Ca2+:** Bổ sung nếu giảm
    
    **4. Pain Control:**
    - **Morphine:** 2-5 mg IV
    - **Fentanyl:** 50-100 mcg IV
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: SURGICAL MANAGEMENT ==========
    st.markdown("### 🔪 Surgical Management")
    
    with st.expander("🏥 Xem chỉ định phẫu thuật", expanded=False):
        st.markdown("""
        **Chỉ định tuyệt đối:**
        - Peritonitis
        - Free air
        - Strangulation
        - Complete obstruction (không cải thiện sau 48h)
        
        **Chỉ định tương đối:**
        - Partial obstruction không cải thiện sau 48-72h
        - LBO (thường cần phẫu thuật)
        - Recurrent obstruction
        
        **Procedures:**
        - **Adhesiolysis:** Cắt dính
        - **Resection:** Cắt bỏ đoạn ruột
        - **Bypass:** Nối tắt
        - **Colostomy:** Tạo hậu môn nhân tạo (LBO)
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Triệu chứng không điển hình
        - Tỷ lệ biến chứng cao hơn
        - Cần phẫu thuật sớm hơn
        - Cân nhắc chất lượng cuộc sống
        
        **Bệnh nhân có bệnh nền:**
        - **Malignancy:** Có thể do khối u
        - **Crohn's disease:** Có thể do stricture
        - **Previous surgery:** Có thể do dính
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Hiếm gặp
        - Cẩn thận với imaging
        - Cần tư vấn sản khoa
        
        **Trẻ em:**
        - Thường do nguyên nhân khác (intussusception, volvulus)
        - Cần tư vấn nhi khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: REFERENCES ==========
    render_references_section(get_references("acute_intestinal_obstruction"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_sbo_protocol():
    """Small Bowel Obstruction Protocol"""
    st.warning("## ⚠️ SMALL BOWEL OBSTRUCTION (SBO)")
    
    st.markdown("""
    **Nguyên nhân:**
    - **Adhesions:** Phổ biến nhất (60-70%)
    - **Hernia:** 10-15%
    - **Malignancy:** 5-10%
    - **Stricture:** Crohn's, radiation
    - **Volvulus:** Xoắn ruột
    
    **Quy trình:**
    
    1. **Initial Management:**
       - **NG Tube:** Đặt ngay
       - **Fluid:** Resuscitation
       - **NPO:** Không ăn uống
       - **Pain control:** Morphine
    
    2. **Partial Obstruction:**
       - **Conservative:** 48-72 giờ
       - **Theo dõi:** Clinical, X-ray
       - **Surgery:** Nếu không cải thiện
    
    3. **Complete Obstruction:**
       - **Surgery:** Trong vòng 24-48 giờ
       - **Timing:** Sớm hơn nếu strangulation
    
    4. **Strangulation:**
       - **Emergent surgery:** Cần ngay
       - **Signs:** Đau liên tục, sốt, tăng WBC, lactate
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Partial obstruction có thể điều trị bảo tồn
    - Complete obstruction thường cần phẫu thuật
    - Strangulation cần phẫu thuật ngay
    - NG tube quan trọng để giảm chướng bụng
    """)


def render_lbo_protocol():
    """Large Bowel Obstruction Protocol"""
    st.error("## 🚨 LARGE BOWEL OBSTRUCTION (LBO)")
    
    st.markdown("""
    **Nguyên nhân:**
    - **Malignancy:** Phổ biến nhất (60-70%)
    - **Volvulus:** 10-15%
    - **Diverticulitis:** 5-10%
    - **Stricture:** IBD, radiation
    
    **Quy trình:**
    
    1. **Initial Management:**
       - **NG Tube:** Đặt ngay
       - **Fluid:** Resuscitation
       - **NPO:** Không ăn uống
       - **Pain control:** Morphine
    
    2. **Volvulus:**
       - **Sigmoid volvulus:** Decompression (colonoscopy/rectal tube)
       - **Cecal volvulus:** Surgery
       - **Recurrence:** Surgery sau khi ổn định
    
    3. **Malignancy/Stricture:**
       - **Surgery:** Thường cần
       - **Stenting:** Có thể tạm thời
       - **Timing:** Sau khi ổn định
    
    4. **Cecal Dilatation:**
       - **> 10 cm:** Nguy cơ perforation
       - **Surgery:** Cần ngay
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - LBO thường cần phẫu thuật
    - Volvulus có thể decompression trước
    - Cecal dilatation > 10 cm nguy hiểm
    - Cân nhắc stenting tạm thời
    """)


def render_paralytic_ileus_protocol():
    """Paralytic Ileus Protocol"""
    st.info("## ℹ️ PARALYTIC ILEUS")
    
    st.markdown("""
    **Nguyên nhân:**
    - **Post-operative:** Phổ biến nhất
    - **Electrolyte imbalance:** K+, Na+, Ca2+
    - **Medications:** Opioids, anticholinergics
    - **Infection:** Peritonitis, sepsis
    - **Metabolic:** Uremia, diabetes
    
    **Quy trình:**
    
    1. **Initial Management:**
       - **NG Tube:** Nếu chướng bụng nặng
       - **Fluid:** Resuscitation
       - **NPO:** Không ăn uống
       - **Electrolytes:** Điều chỉnh
    
    2. **Điều trị nguyên nhân:**
       - **Electrolytes:** Bổ sung K+, Na+, Ca2+
       - **Medications:** Giảm opioids nếu có thể
       - **Infection:** Antibiotics nếu cần
    
    3. **Supportive Care:**
       - **Early mobilization:** Nếu có thể
       - **Chewing gum:** Có thể giúp
       - **Prokinetics:** Metoclopramide, erythromycin
    
    4. **Theo dõi:**
       - Clinical exam
       - X-ray
       - Labs
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Thường tự khỏi
    - Điều trị nguyên nhân là quan trọng nhất
    - NG tube chỉ nếu chướng bụng nặng
    - Không cần phẫu thuật (trừ biến chứng)
    """)

