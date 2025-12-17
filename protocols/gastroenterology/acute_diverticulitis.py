"""
Acute Diverticulitis Protocol
ASCRS 2020, WSES 2020
Management of acute diverticulitis
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Diverticulitis Protocol"""
    st.subheader("🫀 Acute Diverticulitis")
    st.caption("ASCRS 2020, WSES 2020 - Management of acute diverticulitis")
    
    st.warning("""
    **⚠️ ACUTE DIVERTICULITIS = URGENT ASSESSMENT REQUIRED**
    
    **Triệu chứng:**
    - Đau bụng hạ sườn trái (phổ biến nhất)
    - Sốt, ớn lạnh
    - Buồn nôn, nôn
    - Thay đổi thói quen đại tiện
    - Có thể có máu trong phân
    
    **Cần phân loại: Uncomplicated vs Complicated**
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại")
    
    classification = st.radio(
        "**Phân loại:**",
        ["Uncomplicated", "Complicated (Abscess/Perforation/Obstruction/Fistula)"],
        key="diverticulitis_classification"
    )
    
    st.markdown("---")
    
    if classification == "Uncomplicated":
        render_uncomplicated_protocol()
    else:
        render_complicated_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 2: DIAGNOSIS ==========
    st.markdown("### 🔍 Chẩn đoán")
    
    with st.expander("📋 Xem tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Clinical Features:**
        - **Pain:** Hạ sườn trái (phổ biến nhất)
        - **Fever:** Sốt
        - **Nausea/Vomiting:** Buồn nôn, nôn
        - **Change in bowel habits:** Thay đổi thói quen đại tiện
        - **Tenderness:** Đau khi ấn hạ sườn trái
        - **Rebound:** Có thể có nếu nặng
        
        **Laboratory:**
        - **WBC:** Tăng (> 10,000/μL)
        - **CRP:** Tăng (> 10 mg/L)
        - **Procalcitonin:** Tăng nếu nặng
        
        **Imaging:**
        - **CT:** Tiêu chuẩn vàng (độ nhạy > 95%)
        - **US:** Có thể dùng
        - **MRI:** Cho phụ nữ có thai
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: ANTIBIOTICS ==========
    st.markdown("### 💊 Antibiotics")
    
    with st.expander("📋 Xem liều kháng sinh", expanded=False):
        st.markdown("""
        **Uncomplicated (Outpatient):**
        - **Metronidazole:** 500 mg PO q8h
        - **Ciprofloxacin:** 500 mg PO q12h
        - **Levofloxacin:** 500 mg PO q24h
        - **Duration:** 7-10 ngày
        
        **Uncomplicated (Inpatient):**
        - **Metronidazole:** 500 mg IV q8h
        - **Ciprofloxacin:** 400 mg IV q12h
        - **Levofloxacin:** 500 mg IV q24h
        - **Duration:** 7-10 ngày
        
        **Complicated:**
        - **Piperacillin-tazobactam:** 4.5 g IV q8h
        - **Ceftriaxone + Metronidazole:** 1-2 g IV q24h + 500 mg IV q8h
        - **Meropenem:** 1 g IV q8h (nếu nặng)
        - **Duration:** 7-14 ngày hoặc đến khi afebrile 24-48h
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: SURGICAL MANAGEMENT ==========
    st.markdown("### 🔪 Surgical Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Uncomplicated:**
        - **Không cần** phẫu thuật
        - Điều trị nội khoa
        - Có thể điều trị ngoại trú
        
        **Complicated - Abscess:**
        - **Percutaneous drainage:** Ưu tiên
        - **Surgery:** Nếu drainage thất bại
        - **Timing:** Sau khi ổn định
        """)
    
    with col2:
        st.markdown("""
        **Complicated - Perforation:**
        - **Emergent surgery:** Cần ngay
        - **Hartmann's procedure:** Thường dùng
        - **Primary anastomosis:** Cân nhắc nếu ổn định
        
        **Complicated - Obstruction:**
        - **Surgery:** Cần
        - **Timing:** Sau khi ổn định
        
        **Complicated - Fistula:**
        - **Surgery:** Cần
        - **Timing:** Sau khi ổn định
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Triệu chứng không điển hình
        - Tỷ lệ complicated cao hơn
        - Biến chứng nhiều hơn
        - Cần nhập viện thường xuyên hơn
        
        **Bệnh nhân có bệnh nền:**
        - **Immunosuppressed:** Tỷ lệ complicated cao hơn
        - **Diabetes:** Tỷ lệ complicated cao hơn
        - Điều chỉnh liều thuốc
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Hiếm gặp
        - MRI ưu tiên (tránh radiation)
        - Cần tư vấn sản khoa
        - Cẩn thận với antibiotics
        
        **Trẻ em:**
        - Hiếm gặp
        - Thường do nguyên nhân khác
        - Cần tư vấn nhi khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 6: REFERENCES ==========
    render_references_section(get_references("acute_diverticulitis"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_uncomplicated_protocol():
    """Uncomplicated Diverticulitis Protocol"""
    st.success("## ✅ UNCOMPLICATED DIVERTICULITIS")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Outpatient Management:**
       - **Antibiotics:** PO (Metronidazole + Ciprofloxacin)
       - **Diet:** Clear liquids → Low-residue
       - **Pain control:** Acetaminophen, NSAIDs
       - **Follow-up:** 2-3 ngày
    
    2. **Inpatient Management (nếu cần):**
       - **Antibiotics:** IV (Metronidazole + Ciprofloxacin)
       - **NPO:** Không ăn uống
       - **Pain control:** Morphine nếu cần
       - **Discharge:** Khi afebrile, ăn được
    
    3. **Follow-up:**
       - 1-2 tuần sau
       - Cân nhắc colonoscopy sau 4-6 tuần
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Có thể điều trị ngoại trú nếu nhẹ
    - Không cần phẫu thuật
    - Cân nhắc colonoscopy sau để loại trừ ung thư
    - Phòng ngừa: High-fiber diet
    """)


def render_complicated_protocol():
    """Complicated Diverticulitis Protocol"""
    st.error("## 🚨 COMPLICATED DIVERTICULITIS")
    
    st.markdown("""
    **Quy trình:**
    
    1. **Resuscitation:**
       - **Fluid:** NS/LR 1-2 L nếu cần
       - **Vasopressors:** Nếu shock
       - **NPO:** Không ăn uống
    
    2. **Antibiotics:**
       - **Broad-spectrum:** Piperacillin-tazobactam
       - **Duration:** 7-14 ngày
    
    3. **Abscess:**
       - **Percutaneous drainage:** Ưu tiên
       - **Surgery:** Nếu drainage thất bại
    
    4. **Perforation:**
       - **Emergent surgery:** Cần ngay
       - **Hartmann's procedure:** Thường dùng
    
    5. **Obstruction/Fistula:**
       - **Surgery:** Sau khi ổn định
       - **Timing:** 2-4 tuần sau
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Cần nhập viện
    - Cần antibiotics lâu hơn
    - Có thể cần phẫu thuật
    - Theo dõi sát biến chứng
    """)

