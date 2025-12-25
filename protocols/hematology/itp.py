"""
Immune Thrombocytopenic Purpura (ITP) Protocol
ASH Guidelines 2024, UpToDate 2024
Autoimmune disorder causing low platelet count
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """ITP Management Protocol"""
    st.subheader("🩸 Xuất Huyết Giảm Tiểu Cầu Miễn Dịch (ITP)")
    st.caption("ASH Guidelines 2024, UpToDate 2024 - Autoimmune disorder")
    
    st.error("""
    **⚠️ ITP = BỆNH TỰ MIỄN - CẦN ĐIỀU TRỊ**
    
    **Định nghĩa:**
    - Giảm tiểu cầu (<100,000/μL)
    - Không có nguyên nhân rõ ràng
    - Tự miễn (kháng thể chống tiểu cầu)
    
    **Phân loại:**
    - **Cấp tính:** <3 tháng (thường ở trẻ em)
    - **Mạn tính:** >3 tháng (thường ở người lớn)
    
    **Triệu chứng:**
    - Xuất huyết da (petechiae, purpura)
    - Chảy máu mũi, chân răng
    - Xuất huyết nặng (hiếm)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Mức độ Nghiêm trọng")
    
    platelet_count = st.number_input(
        "**Số lượng Tiểu cầu (×10³/μL):**",
        min_value=0,
        max_value=500,
        value=0,
        step=5,
        help="Số lượng tiểu cầu trong máu"
    )
    
    if platelet_count > 0:
        if platelet_count >= 50:
            st.success("✅ **Tiểu cầu ≥50** - Nguy cơ xuất huyết thấp")
        elif platelet_count >= 30:
            st.warning("⚠️ **Tiểu cầu 30-50** - Nguy cơ xuất huyết trung bình")
        elif platelet_count >= 10:
            st.error("🚨 **Tiểu cầu 10-30** - Nguy cơ xuất huyết cao")
        else:
            st.error("🚨🚨 **Tiểu cầu <10** - Nguy cơ xuất huyết rất cao!")
    
    has_bleeding = st.checkbox("Có xuất huyết hoạt động", key="itp_bleeding")
    has_severe_bleeding = st.checkbox("Xuất huyết nặng (nội sọ, GI)", key="itp_severe_bleeding")
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    if has_severe_bleeding or platelet_count < 10:
        render_severe_itp()
    elif has_bleeding or platelet_count < 30:
        render_moderate_itp()
    else:
        render_mild_itp()
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    - Giảm tiểu cầu (<100,000/μL)
    - Không có nguyên nhân rõ ràng
    - Tủy xương bình thường (nếu cần)
    - Không có bệnh lý khác
    
    **Xét nghiệm:**
    - **CBC:** Giảm tiểu cầu, các dòng khác bình thường
    - **Peripheral smear:** Tiểu cầu lớn, không có mảnh vỡ hồng cầu
    - **Bone marrow:** (nếu cần, đặc biệt ở người lớn >60 tuổi)
    - **Anti-platelet antibodies:** (không cần thiết)
    
    **Loại trừ:**
    - DIC
    - TTP/HUS
    - HIT
    - Bệnh lý khác
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Chi tiết")
    
    st.markdown("#### 1. First-line Treatment")
    
    st.success("""
    **Corticosteroids:**
    
    **Prednisone:**
    - **Liều:** 1 mg/kg/ngày PO (tối đa 80 mg/ngày)
    - **Thời gian:** 2-4 tuần, sau đó giảm dần
    - **Hiệu quả:** 70-80% đáp ứng
    
    **Hoặc Dexamethasone:**
    - **Liều:** 40 mg/ngày PO × 4 ngày
    - **Lặp lại:** Mỗi 2-4 tuần (nếu cần)
    - **Hiệu quả:** Tương tự prednisone
    
    **IVIG (Nếu cần tăng nhanh):**
    - **Liều:** 1 g/kg/ngày × 2 ngày
    - **Hoặc:** 0.4 g/kg/ngày × 5 ngày
    - **Hiệu quả:** Tăng tiểu cầu nhanh (1-3 ngày)
    """)
    
    st.markdown("---")
    
    st.markdown("#### 2. Second-line Treatment")
    
    st.info("""
    **Nếu không đáp ứng First-line:**
    
    **1. Rituximab:**
    - **Liều:** 375 mg/m² IV mỗi tuần × 4 tuần
    - **Hiệu quả:** 50-60% đáp ứng
    - **Thời gian:** 2-4 tuần
    
    **2. TPO Agonists:**
    
    **Eltrombopag:**
    - **Liều:** 50 mg PO qd (người lớn)
    - **Điều chỉnh:** Theo đáp ứng
    - **Hiệu quả:** 70-80% đáp ứng
    
    **Romiplostim:**
    - **Liều:** 1-10 mcg/kg SC mỗi tuần
    - **Điều chỉnh:** Theo đáp ứng
    - **Hiệu quả:** 70-80% đáp ứng
    
    **3. Splenectomy:**
    - **Chỉ định:** Nếu không đáp ứng thuốc
    - **Hiệu quả:** 60-70% đáp ứng lâu dài
    - **Lưu ý:** Vaccination trước (Pneumococcus, Meningococcus, H. influenzae)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi")
    
    st.info("""
    **Theo dõi:**
    - **CBC:** Mỗi 1-2 tuần (trong điều trị)
    - **Triệu chứng xuất huyết:** Mỗi lần khám
    - **Tác dụng phụ:** Corticosteroids, Rituximab
    
    **Mục tiêu:**
    - Tiểu cầu ≥30,000/μL (không xuất huyết)
    - Hoặc ≥50,000/μL (nếu phẫu thuật)
    - Giảm xuất huyết
    
    **Tiên lượng:**
    - **Cấp tính:** Thường tự khỏi (trẻ em)
    - **Mạn tính:** Cần điều trị lâu dài (người lớn)
    - **Tử vong:** <1% (nếu điều trị đúng)
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("ITP")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ASH Guidelines 2024** - American Society of Hematology
        2. **UpToDate:** ITP Management - Last updated 2024
        3. **Blood Journal** - ITP Treatment Guidelines
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_severe_itp():
    """Severe ITP"""
    st.error("## 🚨🚨 ITP NẶNG - ĐIỀU TRỊ CẤP CỨU")
    
    st.markdown("""
    **Chỉ định:**
    - Tiểu cầu <10,000/μL
    - Xuất huyết nặng (nội sọ, GI)
    - Xuất huyết đe dọa tính mạng
    
    **Điều trị NGAY:**
    
    **1. IVIG:**
    - **Liều:** 1 g/kg/ngày × 2 ngày
    - **Hoặc:** 0.4 g/kg/ngày × 5 ngày
    - **Hiệu quả:** Tăng tiểu cầu trong 1-3 ngày
    
    **2. Corticosteroids:**
    - **Methylprednisolone:** 1-2 mg/kg/ngày IV
    - **Hoặc:** Prednisone 1-2 mg/kg/ngày PO
    
    **3. Truyền Tiểu cầu:**
    - **Chỉ nếu:** Xuất huyết nặng, đe dọa tính mạng
    - **Liều:** 1 đơn vị/10 kg
    - **Lưu ý:** Hiệu quả ngắn (vài giờ)
    
    **4. Rituximab:**
    - **Có thể dùng sớm** nếu cần
    
    **Monitoring:**
    - Tiểu cầu mỗi ngày
    - Triệu chứng xuất huyết
    - Thần kinh (nếu nghi ngờ xuất huyết nội sọ)
    """)


def render_moderate_itp():
    """Moderate ITP"""
    st.warning("## ⚠️ ITP TRUNG BÌNH - ĐIỀU TRỊ TÍCH CỰC")
    
    st.markdown("""
    **Chỉ định:**
    - Tiểu cầu 10-30,000/μL
    - Có xuất huyết nhẹ-trung bình
    
    **Điều trị:**
    
    **1. Corticosteroids:**
    - **Prednisone:** 1 mg/kg/ngày PO
    - **Thời gian:** 2-4 tuần
    
    **2. IVIG (Nếu cần tăng nhanh):**
    - **Liều:** 1 g/kg/ngày × 2 ngày
    - **Hoặc:** 0.4 g/kg/ngày × 5 ngày
    
    **3. Monitoring:**
    - Tiểu cầu mỗi 1-2 tuần
    - Triệu chứng xuất huyết
    
    **Tiên lượng:**
    - Thường đáp ứng tốt
    - Có thể cần điều trị lâu dài
    """)


def render_mild_itp():
    """Mild ITP"""
    st.success("## ✅ ITP NHẸ - THEO DÕI HOẶC ĐIỀU TRỊ")
    
    st.markdown("""
    **Chỉ định:**
    - Tiểu cầu ≥30,000/μL
    - Không có xuất huyết hoặc xuất huyết nhẹ
    
    **Điều trị:**
    
    **1. Theo dõi:**
    - Nếu tiểu cầu ≥50,000/μL và không xuất huyết
    - CBC mỗi 1-3 tháng
    
    **2. Điều trị (Nếu cần):**
    - **Corticosteroids:** Nếu tiểu cầu 30-50,000/μL
    - **Hoặc:** Theo dõi nếu không xuất huyết
    
    **3. Monitoring:**
    - Tiểu cầu mỗi 1-3 tháng
    - Triệu chứng xuất huyết
    
    **Tiên lượng:**
    - Thường ổn định
    - Có thể tự cải thiện
    """)

