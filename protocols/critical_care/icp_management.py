"""
Intracranial Pressure (ICP) Management Protocol
Brain Trauma Foundation Guidelines 2024, AANS Guidelines 2024
Life-threatening increased intracranial pressure
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """ICP Management Protocol"""
    st.subheader("🧠 Quản lý Áp Lực Nội Sọ (ICP Management)")
    st.caption("Brain Trauma Foundation Guidelines 2024, AANS Guidelines 2024 - Increased ICP")
    
    st.error("""
    **⚠️ TĂNG ÁP LỰC NỘI SỌ = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - ICP >20 mmHg (bình thường: 5-15 mmHg)
    - Có thể gây giảm tưới máu não → Tổn thương não
    
    **Nguyên nhân:**
    - **Chấn thương sọ não:** (phổ biến nhất)
    - **Xuất huyết nội sọ:** (ICH, SDH, EDH)
    - **Nhồi máu não lớn:** (stroke)
    - **U não:** (tumor)
    - **Viêm não:** (encephalitis)
    - **Não úng thủy:** (hydrocephalus)
    
    **Triệu chứng:**
    - Đau đầu
    - Nôn
    - Giảm ý thức
    - Dấu hiệu thần kinh khu trú
    - Cushing's Triad (hạ HA, nhịp chậm, thở bất thường)
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - **Chỉ định sớm** nếu:
          - GCS <8
          - Suy hô hấp
          - Không bảo vệ được đường thở
        
        **Ventilation:**
        - **Mục tiêu:** PaCO₂ 35-40 mmHg
        - **Hyperventilation:** Chỉ tạm thời (PaCO₂ 30-35 mmHg)
        - **Lưu ý:** Tránh hyperventilation kéo dài
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Arterial line** (theo dõi BP liên tục)
        - **Central line** (nếu cần)
        - **BP, HR:** Mỗi 5-15 phút
        
        **Truyền dịch:**
        - **NS:** (ưu tiên)
        - **Tránh:** D5W, Lactated Ringer's (có thể làm nặng phù não)
        """)
    
    with col2:
        st.warning("""
        **3. ICP MONITORING**
        
        **Chỉ định:**
        - GCS <8
        - CT scan bất thường
        - Nghi ngờ tăng ICP
        
        **Loại:**
        - **EVD:** (External Ventricular Drain) - có thể dẫn lưu
        - **ICP bolt:** (ít xâm lấn)
        
        **4. POSITIONING**
        
        - **Đầu cao 30°:** (giảm ICP)
        - **Trung tính:** (tránh xoay cổ)
        - **C-spine protection:** (nếu chấn thương)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Mức độ Nghiêm trọng")
    
    # ICP level
    icp_level = st.number_input(
        "**Áp lực Nội sọ (ICP, mmHg):**",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        help="Áp lực nội sọ đo được"
    )
    
    if icp_level > 0:
        if icp_level <= 15:
            st.success("✅ **ICP bình thường** - <15 mmHg")
        elif icp_level <= 20:
            st.warning("⚠️ **ICP tăng nhẹ** - 15-20 mmHg")
        elif icp_level <= 30:
            st.error("🚨 **ICP tăng trung bình** - 20-30 mmHg - Cần điều trị")
        else:
            st.error("🚨🚨 **ICP tăng nặng** - >30 mmHg - Điều trị ngay!")
    
    # CPP calculation
    if icp_level > 0:
        map_value = st.number_input(
            "**Mean Arterial Pressure (MAP, mmHg):**",
            min_value=0,
            max_value=200,
            value=80,
            step=5,
            help="Huyết áp động mạch trung bình"
        )
        
        cpp = map_value - icp_level
        st.markdown(f"### CPP (Cerebral Perfusion Pressure): **{cpp} mmHg**")
        
        if cpp < 50:
            st.error("🚨 **CPP quá thấp** - <50 mmHg - Nguy cơ tổn thương não!")
        elif cpp < 60:
            st.warning("⚠️ **CPP thấp** - 50-60 mmHg - Cần tăng")
        else:
            st.success("✅ **CPP đủ** - ≥60 mmHg")
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Đặc hiệu")
    
    st.error("## 🚨 ĐIỀU TRỊ TĂNG ICP - TIERED APPROACH")
    
    st.markdown("### Tier 1: Basic Measures")
    
    st.success("""
    **1. Positioning:**
    - Đầu cao 30°
    - Trung tính (tránh xoay cổ)
    - C-spine protection
    
    **2. Ventilation:**
    - PaCO₂ 35-40 mmHg (bình thường)
    - Hyperventilation tạm thời (PaCO₂ 30-35 mmHg) nếu ICP tăng nặng
    
    **3. Sedation:**
    - **Propofol:** 0.3-3 mg/kg/h IV
    - **Hoặc:** Midazolam 0.1-0.3 mg/kg/h IV
    - **Mục đích:** Giảm ICP, giảm chuyển hóa
    
    **4. Analgesia:**
    - **Fentanyl:** 1-3 mcg/kg/h IV
    - **Hoặc:** Morphine 0.1-0.2 mg/kg/h IV
    """)
    
    st.markdown("---")
    
    st.markdown("### Tier 2: Medical Management")
    
    st.warning("""
    **1. Hyperosmolar Therapy:**
    
    **Mannitol:**
    - **Liều:** 0.25-1 g/kg IV bolus
    - **Lặp lại:** Mỗi 4-6h nếu cần
    - **Mục tiêu:** Osmolality 300-320 mOsm/kg
    - **Lưu ý:** Tránh nếu suy thận
    
    **Hypertonic Saline (3%):**
    - **Liều:** 250 mL IV bolus
    - **Hoặc:** 2-3 mL/kg/h IV liên tục
    - **Mục tiêu:** Na 145-155 mEq/L
    - **Lưu ý:** Theo dõi Na sát
    
    **2. Hyperventilation:**
    - **PaCO₂:** 30-35 mmHg (tạm thời)
    - **Thời gian:** <24h
    - **Lưu ý:** Có thể giảm tưới máu não
    
    **3. Temperature Control:**
    - **Mục tiêu:** 36-37°C
    - **Hypothermia:** 32-35°C (nếu cần)
    - **Lưu ý:** Có thể có lợi nhưng cần nghiên cứu thêm
    """)
    
    st.markdown("---")
    
    st.markdown("### Tier 3: Advanced Measures")
    
    st.error("""
    **1. Barbiturate Coma:**
    
    **Pentobarbital:**
    - **Loading:** 10 mg/kg IV
    - **Duy trì:** 1-3 mg/kg/h IV
    - **Mục tiêu:** Burst suppression trên EEG
    - **Chỉ định:** Nếu các biện pháp khác thất bại
    - **Lưu ý:** Hạ huyết áp, suy hô hấp
    
    **2. Decompressive Craniectomy:**
    
    **Chỉ định:**
    - ICP >20-25 mmHg không đáp ứng điều trị
    - Tổn thương não khu trú
    - Có thể phẫu thuật
    
    **Lưu ý:**
    - Có thể cải thiện tỷ lệ sống
    - Có thể tăng tỷ lệ tàn tật
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. CPP Management:**
    - **Mục tiêu:** CPP 60-70 mmHg
    - **Nếu CPP <60:** Tăng MAP (norepinephrine)
    - **Nếu CPP >70:** Có thể giảm MAP
    
    **2. Glucose Control:**
    - **Mục tiêu:** 140-180 mg/dL
    - **Tránh:** Hạ đường huyết (tổn thương não)
    - **Tránh:** Tăng đường huyết quá cao
    
    **3. Seizure Prophylaxis:**
    - **Phenytoin:** 15-20 mg/kg IV loading, sau đó 5-7 mg/kg/ngày
    - **Hoặc:** Levetiracetam 1000-2000 mg IV bid
    
    **4. Monitoring:**
    - **ICP:** Liên tục
    - **CPP:** Liên tục
    - **GCS:** Mỗi 1-2h
    - **Pupil:** Mỗi 1-2h
    - **CT scan:** Nếu ICP tăng hoặc thay đổi thần kinh
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Chống chỉ định & Lưu ý")
    
    st.warning("""
    **1. Hyperventilation:**
    - Không dùng kéo dài (>24h)
    - Có thể giảm tưới máu não
    
    **2. Mannitol:**
    - Chống chỉ định nếu suy thận nặng
    - Theo dõi osmolality
    
    **3. Hypertonic Saline:**
    - Theo dõi Na sát
    - Tránh tăng Na quá nhanh
    
    **4. Barbiturates:**
    - Hạ huyết áp nặng
    - Suy hô hấp
    - Cần monitoring sát
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - Phụ thuộc vào nguyên nhân
    - Tốt nếu điều trị sớm
    - Xấu nếu ICP tăng kéo dài
    
    **Theo dõi:**
    - **ICP:** Liên tục (cho đến khi <20 mmHg)
    - **CPP:** Liên tục (mục tiêu 60-70 mmHg)
    - **GCS:** Mỗi 1-2h
    - **Pupil:** Mỗi 1-2h
    - **CT scan:** Nếu cần
    
    **Xuất viện:**
    - ICP ổn định <20 mmHg
    - CPP đủ ≥60 mmHg
    - Không triệu chứng
    - Theo dõi ít nhất 24-48h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("ICP Management")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **Brain Trauma Foundation Guidelines 2024** - BTF
        2. **AANS Guidelines 2024** - American Association of Neurological Surgeons
        3. **UpToDate:** ICP Management - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

