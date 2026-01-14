"""
Lower GI Bleeding Protocol
ACG Guidelines 2024, UpToDate 2024
Acute lower gastrointestinal bleeding management
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Lower GI Bleeding Management Protocol"""
    st.subheader("🩸 Xuất huyết Tiêu hóa Dưới (Lower GI Bleeding)")
    st.caption("ACG Guidelines 2024, UpToDate 2024 - Acute lower gastrointestinal bleeding")
    
    st.error("""
    **⚠️ XUẤT HUYẾT TIÊU HÓA DƯỚI = CẤP CỨU Y KHOA**
    
    **Định nghĩa:**
    - Xuất huyết từ ruột non, đại tràng, trực tràng
    - Biểu hiện: Tiêu máu đỏ tươi, tiêu phân đen (nếu chậm)
    
    **Nguyên nhân Thường gặp:**
    - **Diverticulosis:** (phổ biến nhất, 30-40%)
    - **Angiodysplasia:** (20-30%)
    - **Colitis:** (10-20%)
    - **Polyp/Tumor:** (5-10%)
    - **Hemorrhoids:** (5-10%)
    - **IBD:** (5%)
    - **Khác:** Ischemic colitis, radiation colitis
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức
        - Suy hô hấp
        - Nguy cơ hít sặc
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 500-1000 mL bolus
        - **Mục tiêu:** SBP ≥90 mmHg
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị truyền máu
        
        **4. LABS NGAY:**
        - **CBC:** Hct, Hb, Platelets
        - **BMP:** Creatinine, Electrolytes
        - **Coagulation:** PT/INR, aPTT
        - **Type & Screen:** (chuẩn bị truyền máu)
        - **Lactate:** (đánh giá tưới máu)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Đánh giá Mức độ Nghiêm trọng")
    
    # Assess bleeding severity
    hb_level = st.number_input(
        "**Hemoglobin (g/dL):**",
        min_value=0.0,
        max_value=20.0,
        value=12.0,
        step=0.5,
        help="Nồng độ hemoglobin"
    )
    
    systolic_bp = st.number_input(
        "**Huyết áp tâm thu (mmHg):**",
        min_value=0,
        max_value=300,
        value=120,
        step=5,
        help="Huyết áp tâm thu"
    )
    
    has_shock = st.checkbox("Shock (hạ huyết áp, nhịp nhanh)", key="lgib_shock")
    has_active_bleeding = st.checkbox("Chảy máu đang tiếp diễn", key="lgib_active")
    
    st.markdown("---")
    
    if has_shock or hb_level < 8.0 or systolic_bp < 90:
        render_severe_lgib()
    elif has_active_bleeding or hb_level < 10.0:
        render_moderate_lgib()
    else:
        render_mild_lgib()
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    - Tiêu máu đỏ tươi (hematochezia)
    - Hoặc tiêu phân đen (melena) - nếu chậm
    - Có thể có đau bụng
    - Có thể có thiếu máu
    
    **Xét nghiệm:**
    - **CBC:** Hct, Hb giảm
    - **BMP:** Có thể tăng BUN (do hấp thu protein)
    - **Coagulation:** Bình thường hoặc bất thường
    - **Colonoscopy:** (ưu tiên, sau khi ổn định)
    - **CT angiography:** (nếu chảy máu nhanh)
    - **Tagged RBC scan:** (nếu chảy máu chậm)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị")
    
    st.success("""
    **1. Resuscitation:**
    - **Truyền dịch:** NS 500-1000 mL bolus
    - **Truyền máu:** PRBC nếu Hct <25% hoặc Hct <30% + triệu chứng
    - **Mục tiêu:** SBP ≥90 mmHg, Hct ≥25-30%
    
    **2. Điều trị Nguyên nhân:**
    
    **Diverticulosis:**
    - Thường tự cầm
    - Colonoscopy để xác định
    - Có thể cần embolization hoặc phẫu thuật
    
    **Angiodysplasia:**
    - Colonoscopy + cauterization
    - Hoặc embolization
    
    **Colitis:**
    - Điều trị theo nguyên nhân
    - Infectious: Kháng sinh
    - Ischemic: Điều trị nguyên nhân
    - IBD: Corticosteroids, Immunosuppressants
    
    **3. Endoscopic Treatment:**
    - **Cauterization:** (nếu có thể)
    - **Clipping:** (nếu có thể)
    - **Injection:** (nếu có thể)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Truyền máu:**
    - **PRBC:** Nếu Hct <25% hoặc Hct <30% + triệu chứng
    - **FFP:** Nếu rối loạn đông máu
    - **Platelets:** Nếu giảm tiểu cầu
    
    **2. Điều chỉnh Đông máu:**
    - **Ngừng:** Anticoagulants, Antiplatelets (nếu có thể)
    - **Đảo ngược:** Nếu cần (Warfarin, DOACs)
    
    **3. Monitoring:**
    - **Hct, Hb:** Mỗi 4-6h (cho đến khi ổn định)
    - **Huyết áp, HR:** Mỗi 1-2h
    - **Triệu chứng:** Mỗi 1-2h
    - **Cân bằng nước vào/ra:** Mỗi 6-12h
    
    **4. Colonoscopy:**
    - **Thời gian:** Sau khi ổn định (12-24h)
    - **Chuẩn bị:** Bowel prep (nếu có thể)
    - **Mục đích:** Xác định và điều trị nguyên nhân
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Chỉ định Phẫu thuật")
    
    st.warning("""
    **Chỉ định Phẫu thuật:**
    - Chảy máu không kiểm soát được
    - Chảy máu tái phát nhiều lần
    - Không thể xác định nguyên nhân
    - Tổn thương cần phẫu thuật (tumor, polyp lớn)
    
    **Lưu ý:**
    - Phẫu thuật có tỷ lệ tử vong cao
    - Ưu tiên điều trị nội soi/embolization
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Lower GI Bleeding")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACG Guidelines 2024** - American College of Gastroenterology
        2. **UpToDate:** Lower GI Bleeding - Last updated 2024
        3. **Gastroenterology** - Lower GI Bleeding Management
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_severe_lgib():
    """Severe Lower GI Bleeding"""
    st.error("## 🚨🚨 XUẤT HUYẾT NẶNG - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Shock
    - Hb <8 g/dL
    - Chảy máu đang tiếp diễn
    - Huyết áp <90 mmHg
    
    **Điều trị NGAY:**
    
    **1. Resuscitation:**
    - **Truyền máu:** PRBC 2-4 đơn vị
    - **Truyền dịch:** NS 1000-2000 mL bolus
    - **FFP:** Nếu rối loạn đông máu
    
    **2. Endoscopy/Intervention:**
    - **CT angiography:** (nếu chảy máu nhanh)
    - **Colonoscopy:** (sau khi ổn định)
    - **Embolization:** (nếu có thể)
    
    **3. Phẫu thuật:**
    - Nếu không kiểm soát được
    - Cấp cứu
    
    **Monitoring:**
    - ICU
    - Hct, Hb mỗi 2-4h
    - Huyết áp, HR mỗi 15-30 phút
    """)


def render_moderate_lgib():
    """Moderate Lower GI Bleeding"""
    st.warning("## ⚠️ XUẤT HUYẾT TRUNG BÌNH")
    
    st.markdown("""
    **Đặc điểm:**
    - Hb 8-10 g/dL
    - Có thể có chảy máu
    - Huyết áp ổn định
    
    **Điều trị:**
    
    **1. Resuscitation:**
    - **Truyền máu:** PRBC 1-2 đơn vị (nếu cần)
    - **Truyền dịch:** NS 500-1000 mL
    
    **2. Colonoscopy:**
    - **Thời gian:** 12-24h sau khi ổn định
    - **Mục đích:** Xác định và điều trị
    
    **3. Monitoring:**
    - Hct, Hb mỗi 6-12h
    - Huyết áp, HR mỗi 2-4h
    """)


def render_mild_lgib():
    """Mild Lower GI Bleeding"""
    st.success("## ✅ XUẤT HUYẾT NHẸ")
    
    st.markdown("""
    **Đặc điểm:**
    - Hb ≥10 g/dL
    - Không có chảy máu đang tiếp diễn
    - Huyết áp ổn định
    
    **Điều trị:**
    
    **1. Theo dõi:**
    - Hct, Hb mỗi 12-24h
    - Triệu chứng
    
    **2. Colonoscopy:**
    - **Thời gian:** 24-48h
    - **Mục đích:** Xác định nguyên nhân
    
    **3. Điều trị:**
    - Theo nguyên nhân
    """)

