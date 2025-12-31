"""
Burn Management Protocol
ABA Burn Care Guidelines 2024, ATLS Guidelines 2024
Life-threatening burns requiring immediate assessment and treatment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)
from components.phase1_protocol_enhancer import (
    render_protocol_header,
    render_recommendation_with_evidence,
    render_protocol_footer
)


def render():
    """Burn Management Protocol"""
    st.subheader("🔥 Bỏng (Burn Management)")
    st.caption("ABA Burn Care Guidelines 2024, ATLS Guidelines 2024 - Life-threatening burns")
    
    # Enhanced header with Phase 1 components
    render_protocol_header(
        protocol_name="Burn Management",
        guideline_source="ABA 2024, ATLS 2024",
        show_version=True,
        show_evidence_summary=True
    )
    
    st.error("""
    **⚠️ BỎNG NẶNG = CẤP CỨU Y KHOA**
    
    **Phân loại Bỏng:**
    - **Độ I:** Đỏ da, đau (chỉ lớp ngoài)
    - **Độ II:** Phỏng nước, đau (lớp biểu bì và một phần lớp bì)
    - **Độ III:** Mất cảm giác, trắng/đen (toàn bộ lớp bì)
    - **Độ IV:** Tổn thương cơ/xương
    
    **Yếu tố Nguy hiểm:**
    - Diện tích bỏng lớn (≥20% ở người lớn, ≥10% ở trẻ em)
    - Bỏng vùng mặt, cổ, tay, chân, bộ phận sinh dục
    - Bỏng đường hô hấp
    - Bỏng điện
    - Bỏng hóa chất
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation (Ưu tiên):**
        - Bỏng vùng mặt/cổ
        - Bỏng đường hô hấp
        - Phù nề đường thở
        - Khó thở
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        - **Lưu ý:** CO poisoning (nếu bỏng do cháy)
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **2 đường tĩnh mạch lớn**
        - **Lưu ý:** Tính toán dịch truyền đặc biệt
        """)
    
    with col2:
        st.warning("""
        **3. REMOVE SOURCE**
        
        **Ngừng quá trình bỏng:**
        - Dập lửa
        - Loại bỏ quần áo cháy
        - Rửa hóa chất (nếu bỏng hóa chất)
        - Ngắt điện (nếu bỏng điện)
        
        **4. ASSESSMENT**
        
        **Đánh giá:**
        - Diện tích bỏng (Rule of Nines)
        - Độ sâu bỏng
        - Vị trí bỏng
        - Tuổi bệnh nhân
        - Bệnh kèm theo
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Diện tích Bỏng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Rule of Nines (Người lớn):**
        - **Đầu & Cổ:** 9%
        - **Mỗi cánh tay:** 9%
        - **Mỗi chân:** 18%
        - **Thân trước:** 18%
        - **Thân sau:** 18%
        - **Bộ phận sinh dục:** 1%
        
        **Tổng:** 100%
        """)
    
    with col2:
        st.markdown("""
        **Rule of Nines (Trẻ em):**
        - **Đầu & Cổ:** 18% (trẻ nhỏ)
        - **Mỗi cánh tay:** 9%
        - **Mỗi chân:** 14% (trẻ nhỏ)
        - **Thân trước:** 18%
        - **Thân sau:** 18%
        
        **Lưu ý:** Tỷ lệ thay đổi theo tuổi
        """)
    
    # Calculate burn area
    total_burn_area = st.number_input(
        "**Tổng diện tích bỏng (%):**",
        min_value=0.0,
        max_value=100.0,
        value=0.0,
        step=0.5,
        help="Tổng diện tích bỏng tính bằng % cơ thể"
    )
    
    patient_weight = st.number_input(
        "**Cân nặng (kg):**",
        min_value=0,
        max_value=200,
        value=70,
        step=1,
        format="%d",
        help="Cân nặng bệnh nhân"
    )
    
    st.markdown("---")
    
    if total_burn_area > 0 and patient_weight > 0:
        st.markdown("### 💧 Tính toán Dịch Truyền (Parkland Formula)")
        
        # Parkland Formula: 4 mL × %BSA × kg body weight
        # First 24 hours: 50% in first 8 hours, 50% in next 16 hours
        total_fluid_24h = 4 * total_burn_area * patient_weight
        first_8h = total_fluid_24h * 0.5
        next_16h = total_fluid_24h * 0.5
        
        st.success(f"""
        **Parkland Formula:**
        - **Tổng dịch 24h đầu:** {total_fluid_24h:.0f} mL
        - **8 giờ đầu:** {first_8h:.0f} mL ({first_8h/8:.0f} mL/h)
        - **16 giờ tiếp:** {next_16h:.0f} mL ({next_16h/16:.0f} mL/h)
        
        **Loại dịch:** Lactated Ringer's (ưu tiên) hoặc Normal Saline
        
        **Mục tiêu:**
        - Urine output: 0.5-1 mL/kg/h (người lớn)
        - Urine output: 1-2 mL/kg/h (trẻ em)
        - Huyết áp ổn định
        - HR <120 bpm
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Phân loại Mức độ Nghiêm trọng")
    
    burn_severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        [
            "Nhẹ (Minor)",
            "Trung bình (Moderate)",
            "Nặng (Major)",
            "Rất nặng (Critical)"
        ],
        key="burn_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in burn_severity:
        render_minor_burn()
    elif "Trung bình" in burn_severity:
        render_moderate_burn()
    elif "Nặng" in burn_severity:
        render_major_burn()
    else:
        render_critical_burn()
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Thuốc")
    
    st.info("""
    **1. Pain Management:**
    - **Morphine:** 2-5 mg IV (mỗi 2-4h)
    - **Fentanyl:** 50-100 mcg IV (mỗi 1-2h)
    - **Ketamine:** 0.5-1 mg/kg IV (nếu cần)
    
    **2. Tetanus Prophylaxis:**
    - **Nếu chưa tiêm trong 5 năm:** Tetanus toxoid 0.5 mL IM
    - **Nếu chưa tiêm trong 10 năm:** Tetanus toxoid 0.5 mL IM
    - **Nếu không chắc:** Tetanus toxoid + TIG
    
    **3. Antibiotics:**
    - **Không dùng dự phòng** (trừ bỏng nặng)
    - **Chỉ dùng nếu:** Nhiễm trùng xác định
    - **Lựa chọn:** Vancomycin + Piperacillin-Tazobactam
    
    **4. Monitoring:**
    - Urine output (mỗi giờ)
    - Huyết áp, HR (mỗi 15-30 phút)
    - Hct, Hb (mỗi 4-6h)
    - Electrolytes (mỗi 6-12h)
    """)
    
    st.markdown("---")
    
    st.markdown("### 🩹 Chăm sóc Vết bỏng")
    
    st.info("""
    **1. Làm sạch:**
    - Rửa nhẹ nhàng với nước muối sinh lý
    - Loại bỏ mảnh vụn
    - Không chọc phỏng nước (nếu nhỏ)
    
    **2. Băng bó:**
    - **Bỏng độ I-II:** Băng ẩm, thay mỗi 12-24h
    - **Bỏng độ III:** Băng khô, vô trùng
    - **Silver sulfadiazine:** (nếu có)
    
    **3. Chỉ định Phẫu thuật:**
    - Bỏng độ III ≥20%
    - Bỏng vùng mặt, tay, chân
    - Bỏng vòng quanh (circumferential)
    - Bỏng điện nặng
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Biến chứng")
    
    with st.expander("📋 Xem các biến chứng thường gặp", expanded=False):
        st.markdown("""
        **Sớm (0-48h):**
        - Shock do mất dịch
        - Suy hô hấp (bỏng đường hô hấp)
        - Rối loạn điện giải
        - Nhiễm trùng
        
        **Muộn (>48h):**
        - Nhiễm trùng vết bỏng
        - Suy đa tạng
        - Rối loạn đông máu
        - Co rút sẹo
        """)
    
    st.markdown("---")
    
    # Enhanced footer with Phase 1 component
    render_protocol_footer("Burn Management")
    
    # Keep existing references as fallback
    references = get_references("Burn Management")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References (Additional)")
        st.markdown("""
        1. **ABA Burn Care Guidelines 2024** - American Burn Association
        2. **ATLS Guidelines 2024** - Advanced Trauma Life Support
        3. **UpToDate:** Burn Management - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_minor_burn():
    """Minor Burn"""
    st.success("## ⚠️ BỎNG NHẸ")
    
    st.markdown("""
    **Tiêu chuẩn:**
    - Diện tích <10% (người lớn)
    - Diện tích <5% (trẻ em)
    - Bỏng độ I-II
    - Không bỏng vùng đặc biệt
    
    **Điều trị:**
    - Làm sạch vết bỏng
    - Băng bó
    - Pain management
    - Theo dõi ngoại trú
    
    **Tiên lượng:**
    - Thường tự lành
    - Ít biến chứng
    """)


def render_moderate_burn():
    """Moderate Burn"""
    st.warning("## 🚨 BỎNG TRUNG BÌNH")
    
    st.markdown("""
    **Tiêu chuẩn:**
    - Diện tích 10-20% (người lớn)
    - Diện tích 5-10% (trẻ em)
    - Bỏng độ II-III
    - Có thể có bỏng vùng đặc biệt
    
    **Điều trị:**
    - Nhập viện
    - Tính toán dịch truyền
    - Pain management
    - Chăm sóc vết bỏng
    - Theo dõi sát
    
    **Tiên lượng:**
    - Cần điều trị tích cực
    - Có thể có biến chứng
    """)


def render_major_burn():
    """Major Burn"""
    st.error("## 🚨🚨 BỎNG NẶNG - ICU")
    
    st.markdown("""
    **Tiêu chuẩn:**
    - Diện tích 20-40% (người lớn)
    - Diện tích 10-20% (trẻ em)
    - Bỏng độ III
    - Bỏng vùng đặc biệt
    
    **Điều trị:**
    - ICU
    - Tính toán dịch truyền (Parkland)
    - Pain management tích cực
    - Chăm sóc vết bỏng chuyên khoa
    - Phẫu thuật (nếu cần)
    - Monitoring sát
    
    **Tiên lượng:**
    - Tử vong: 10-20%
    - Cần điều trị lâu dài
    """)


def render_critical_burn():
    """Critical Burn"""
    st.error("## 🚨🚨🚨 BỎNG RẤT NẶNG - ICU")
    
    st.markdown("""
    **Tiêu chuẩn:**
    - Diện tích >40% (người lớn)
    - Diện tích >20% (trẻ em)
    - Bỏng độ III-IV
    - Bỏng đường hô hấp
    - Bỏng điện nặng
    
    **Điều trị:**
    - ICU
    - Tính toán dịch truyền (Parkland)
    - Intubation (nếu cần)
    - Pain management tích cực
    - Chăm sóc vết bỏng chuyên khoa
    - Phẫu thuật sớm
    - Monitoring sát
    
    **Tiên lượng:**
    - Tử vong: 30-50%
    - Cần điều trị rất lâu dài
    - Nhiều biến chứng
    """)
