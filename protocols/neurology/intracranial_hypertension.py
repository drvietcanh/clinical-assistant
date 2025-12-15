"""
Intracranial Hypertension Protocol
Management of elevated intracranial pressure
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Intracranial Hypertension Protocol"""
    st.subheader("🧠 Tăng áp lực nội sọ (Intracranial Hypertension)")
    st.caption("Management of elevated ICP - Neurocritical Care Guidelines")
    
    st.error("""
    **⚠️ TĂNG ÁP LỰC NỘI SỌ = CẤP CỨU Y TẾ**
    
    **Định nghĩa:**
    - Áp lực nội sọ (ICP) >20 mmHg (bình thường: 5-15 mmHg)
    - Có thể gây giảm tưới máu não → Tổn thương não không hồi phục
    
    **Nguyên nhân:**
    - Chấn thương sọ não
    - Xuất huyết não
    - U não
    - Viêm màng não
    - Não úng thủy
    - Tăng CO2, hạ O2
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLINICAL FEATURES ==========
    st.markdown("### 🔍 Triệu chứng lâm sàng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Triệu chứng:**
        - Đau đầu
        - Buồn nôn, nôn
        - Thay đổi ý thức
        - Đồng tử giãn (một hoặc hai bên)
        - Liệt dây thần kinh sọ
        - Cứng gáy (nếu có viêm màng não)
        """)
    
    with col2:
        st.markdown("""
        **Dấu hiệu nặng:**
        - Hôn mê
        - Đồng tử giãn cố định
        - Tăng huyết áp + Nhịp chậm (Cushing's triad)
        - Ngừng thở
        - Tử vong
        """)
    
    st.markdown("---")
    
    # ========== SECTION 2: DIAGNOSTIC CRITERIA ==========
    st.markdown("### 📋 Chẩn đoán")
    
    st.warning("""
    **Chẩn đoán tăng ICP:**
    
    **Lâm sàng:**
    - Triệu chứng + Dấu hiệu thần kinh
    - Cushing's triad: Tăng huyết áp + Nhịp chậm + Rối loạn nhịp thở
    
    **Cận lâm sàng:**
    - **ICP Monitor:** ICP >20 mmHg (tiêu chuẩn vàng)
    - **CT/MRI não:** Phù não, xẹp não thất, mất rãnh cuộn não
    - **Fundoscopy:** Phù gai thị (nếu mạn tính)
    """)
    
    st.markdown("---")
    
    # ========== SECTION 3: TREATMENT ==========
    st.markdown("### 💊 Điều trị")
    
    st.markdown("#### **1. Điều trị tức thì (Immediate)**")
    
    st.error("""
    **A. ABC:**
    - Đảm bảo đường thở (có thể cần đặt nội khí quản)
    - Oxygen 100%
    - Đảm bảo tuần hoàn
    
    **B. Tư thế:**
    - Đầu cao 30° (nếu không chống chỉ định)
    - Cổ thẳng (tránh xoay, gập)
    
    **C. Hyperventilation (Tạm thời):**
    - PaCO2: 30-35 mmHg (tạm thời, 30-60 phút)
    - ⚠️ Không duy trì lâu (gây thiếu máu não)
    """)
    
    st.markdown("---")
    
    st.markdown("#### **2. Điều trị nội khoa (Medical Management)**")
    
    st.success("""
    **A. Hyperosmolar Therapy:**
    
    **Mannitol:**
    - **Liều:** 0.25-1 g/kg IV (thường 0.5-1 g/kg)
    - **Tốc độ:** Truyền trong 15-30 phút
    - **Lặp lại:** Mỗi 4-6 giờ nếu cần
    - **Lưu ý:** Theo dõi Na, osmolality (không >320 mOsm/kg)
    
    **Hypertonic Saline (3% hoặc 23.4%):**
    - **3% NaCl:** 250-500 mL IV (truyền trong 30-60 phút)
    - **23.4% NaCl:** 30-60 mL IV (truyền trong 10-20 phút)
    - **Lưu ý:** Theo dõi Na (không >160 mEq/L)
    
    **B. Điều chỉnh rối loạn:**
    - **Hạ sốt:** Paracetamol, làm mát ngoài
    - **Điều chỉnh đường huyết:** 140-180 mg/dL
    - **Điều chỉnh Na:** 140-150 mEq/L
    - **Tránh hạ huyết áp:** Duy trì MAP >80 mmHg
    """)
    
    st.markdown("---")
    
    st.markdown("#### **3. Điều trị nặng (Severe Cases)**")
    
    st.warning("""
    **A. Sedation:**
    - **Propofol:** 50-200 mcg/kg/min
    - **Midazolam:** 0.1-0.2 mg/kg/h
    - **Lưu ý:** Cần đặt nội khí quản
    
    **B. Neuromuscular Blockade:**
    - **Vecuronium:** 0.1 mg/kg IV, sau đó 0.05-0.1 mg/kg/h
    - **Lưu ý:** Chỉ dùng khi cần thiết, ngắn hạn
    
    **C. Barbiturate Coma:**
    - **Pentobarbital:** Loading 10 mg/kg, sau đó 1-3 mg/kg/h
    - **Lưu ý:** Chỉ dùng khi các biện pháp khác thất bại
    """)
    
    st.markdown("---")
    
    st.markdown("#### **4. Điều trị phẫu thuật (Surgical)**")
    
    st.info("""
    **Chỉ định phẫu thuật:**
    - ICP không đáp ứng với điều trị nội khoa
    - Có khối choán chỗ (máu tụ, u)
    - Não úng thủy
    - Phù não nặng
    
    **Phương pháp:**
    - Dẫn lưu não thất (Ventriculostomy)
    - Mở sọ giải áp (Decompressive craniectomy)
    - Lấy máu tụ, u
    """)
    
    st.markdown("---")
    
    # ========== SECTION 4: MONITORING ==========
    st.markdown("### 📈 Theo dõi")
    
    st.markdown("""
    **Cần theo dõi:**
    - **ICP:** Liên tục (nếu có monitor)
    - **CPP (Cerebral Perfusion Pressure):** CPP = MAP - ICP
      - Mục tiêu: CPP >60-70 mmHg
    - **Triệu chứng thần kinh:** Mỗi 1-2 giờ
    - **Na, osmolality:** Mỗi 4-6 giờ (nếu dùng mannitol/hypertonic saline)
    - **PaCO2:** Mỗi 2-4 giờ (nếu hyperventilation)
    - **CT não:** Nếu triệu chứng xấu đi
    
    **Dấu hiệu cải thiện:**
    - Giảm ICP
    - Cải thiện ý thức
    - Cải thiện dấu hiệu thần kinh
    
    **Dấu hiệu xấu đi:**
    - ICP >25 mmHg
    - CPP <60 mmHg
    - Đồng tử giãn cố định
    - Cần can thiệp phẫu thuật
    """)
    
    st.markdown("---")
    
    # ========== SECTION 5: REFERENCES ==========
    references = get_references("Intracranial Hypertension")
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
        1. **Brain Trauma Foundation Guidelines** - Management of Severe Traumatic Brain Injury
        2. **UpToDate:** Elevated Intracranial Pressure - Last updated 2024
        3. **Neurocritical Care Society Guidelines**
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

