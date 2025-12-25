"""
Abdominal Trauma Protocol
ATLS Guidelines 2024, EAST Guidelines 2024
Life-threatening trauma requiring immediate assessment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Abdominal Trauma Management Protocol"""
    st.subheader("🫀 Chấn Thương Bụng (Abdominal Trauma)")
    st.caption("ATLS Guidelines 2024, EAST Guidelines 2024 - Life-threatening trauma")
    
    st.error("""
    **⚠️ CHẤN THƯƠNG BỤNG = CẤP CỨU Y KHOA**
    
    **Các Tổn thương Nguy hiểm:**
    - **Xuất huyết trong ổ bụng (Hemoperitoneum)**
    - **Vỡ gan (Liver Laceration)**
    - **Vỡ lách (Splenic Rupture)**
    - **Vỡ thận (Renal Injury)**
    - **Vỡ ruột (Bowel Perforation)**
    - **Vỡ mạch máu (Vascular Injury)**
    - **Chấn thương tụy (Pancreatic Injury)**
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức (GCS <8)
        - Suy hô hấp
        - Tổn thương đường thở
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 5 phút
        
        **Truyền dịch:**
        - **2 đường tĩnh mạch lớn**
        - **NS/LR:** 500-1000 mL bolus
        """)
    
    with col2:
        st.warning("""
        **3. PRIMARY SURVEY (ATLS)**
        
        **A - Airway:**
        - Kiểm tra tắc nghẽn
        - C-spine protection
        
        **B - Breathing:**
        - Đối xứng 2 bên?
        - Ran phổi?
        - SpO₂?
        
        **C - Circulation:**
        - Mạch, huyết áp
        - Chảy máu?
        - Bụng căng?
        
        **D - Disability:**
        - GCS
        - Pupil
        
        **E - Exposure:**
        - Toàn bộ cơ thể
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán Tổn thương")
    
    injury_type = st.radio(
        "**Loại tổn thương nghi ngờ:**",
        [
            "Xuất huyết trong ổ bụng (Hemoperitoneum)",
            "Vỡ gan (Liver Laceration)",
            "Vỡ lách (Splenic Rupture)",
            "Vỡ thận (Renal Injury)",
            "Vỡ ruột (Bowel Perforation)",
            "Vỡ mạch máu (Vascular Injury)",
            "Chấn thương tụy (Pancreatic Injury)"
        ],
        key="abdominal_trauma_type"
    )
    
    st.markdown("---")
    
    if "Hemoperitoneum" in injury_type:
        render_hemoperitoneum()
    elif "Liver" in injury_type:
        render_liver_injury()
    elif "Splenic" in injury_type:
        render_splenic_injury()
    elif "Renal" in injury_type:
        render_renal_injury()
    elif "Bowel" in injury_type:
        render_bowel_perforation()
    elif "Vascular" in injury_type:
        render_vascular_injury()
    else:  # Pancreatic
        render_pancreatic_injury()
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Pain Management:**
    - **Morphine:** 2-5 mg IV (thận trọng)
    - **Fentanyl:** 50-100 mcg IV
    - **Tránh:** NSAIDs (có thể làm nặng chảy máu)
    
    **2. Antibiotics:**
    - **Nếu vỡ ruột:** Cefotetan 2g IV hoặc Cefoxitin 2g IV
    - **Hoặc:** Piperacillin-Tazobactam 4.5g IV
    - **Thời gian:** 24-48h
    
    **3. Monitoring:**
    - **Continuous:** ECG, SpO₂, BP
    - **Frequent:** HR, RR, GCS, Abdomen exam
    - **Labs:** Hct, Hb, Lactate, Base deficit
    - **FAST:** Nếu có (Focused Assessment with Sonography)
    - **CT scan:** Nếu ổn định
    
    **4. Prophylaxis:**
    - **VTE prophylaxis:** Nếu không chống chỉ định
    - **Stress ulcer prophylaxis:** Nếu cần
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi & Đánh giá")
    
    st.info("""
    **Theo dõi trong 24-48h đầu:**
    
    **Lâm sàng:**
    - Đánh giá bụng (mỗi 1-2h)
    - Dấu hiệu sinh tồn (mỗi 1-2h)
    - Đánh giá thần kinh (mỗi 2-4h)
    - Cân bằng nước vào/ra
    
    **Cận lâm sàng:**
    - Hct, Hb (mỗi 4-6h)
    - Lactate, Base deficit (mỗi 6-12h)
    - CT scan (nếu cần)
    
    **Dấu hiệu cải thiện:**
    - ✅ Huyết áp ổn định
    - ✅ Hct ổn định
    - ✅ Giảm đau
    - ✅ Bụng mềm
    
    **Dấu hiệu xấu đi:**
    - ⚠️ Hạ huyết áp
    - ⚠️ Hct giảm
    - ⚠️ Bụng căng tăng
    - ⚠️ Đau tăng
    - 🚨 Cần phẫu thuật
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Abdominal Trauma")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ATLS Guidelines 2024** - Advanced Trauma Life Support
        2. **EAST Guidelines 2024** - Eastern Association for the Surgery of Trauma
        3. **UpToDate:** Abdominal Trauma - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_hemoperitoneum():
    """Hemoperitoneum"""
    st.error("## 🚨🚨 XUẤT HUYẾT TRONG Ổ BỤNG - CẤP CỨU")
    
    st.markdown("""
    **Triệu chứng:**
    - Hạ huyết áp
    - Shock
    - Bụng căng
    - Đau bụng
    - Mất máu (da xanh, niêm mạc nhợt)
    
    **Chẩn đoán:**
    - **FAST:** (Focused Assessment with Sonography)
    - **CT scan:** (nếu ổn định)
    - **DPL:** (Diagnostic Peritoneal Lavage) - ít dùng
    
    **Điều trị:**
    
    **1. Resuscitation:**
    - **Truyền máu:** PRBC 2-4 đơn vị
    - **FFP:** 2-4 đơn vị (nếu cần)
    - **Platelets:** Nếu giảm tiểu cầu
    - **Truyền dịch:** NS/LR 500-1000 mL bolus
    
    **2. Chỉ định Phẫu thuật:**
    - Shock không đáp ứng
    - Xuất huyết liên tục
    - FAST dương tính + Shock
    - CT scan: Tổn thương mạch máu lớn
    
    **3. Monitoring:**
    - Huyết áp, HR
    - Hct, Hb (mỗi 2-4h)
    - FAST (mỗi 4-6h nếu không phẫu thuật)
    """)


def render_liver_injury():
    """Liver Injury"""
    st.error("## 🚨 VỠ GAN")
    
    st.markdown("""
    **Phân loại (AAST):**
    - **Grade I-II:** Nhẹ (thường bảo tồn)
    - **Grade III-IV:** Trung bình-nặng (có thể bảo tồn hoặc phẫu thuật)
    - **Grade V:** Rất nặng (thường phẫu thuật)
    
    **Triệu chứng:**
    - Đau bụng trên phải
    - Hạ huyết áp
    - Shock
    - Có thể có vết thương vùng gan
    
    **Điều trị:**
    
    **1. Bảo tồn (Nếu ổn định):**
    - **Monitoring:** Sát trong 24-48h
    - **Truyền máu:** Nếu cần
    - **CT scan:** Theo dõi
    
    **2. Phẫu thuật (Nếu không ổn định):**
    - Shock không đáp ứng
    - Xuất huyết liên tục
    - Grade IV-V
    
    **3. Angioembolization:**
    - Nếu có tổn thương mạch máu
    - Nếu xuất huyết liên tục nhưng ổn định
    
    **4. Monitoring:**
    - Huyết áp, HR
    - Hct, Hb
    - ALT, AST
    """)


def render_splenic_injury():
    """Splenic Injury"""
    st.error("## 🚨 VỠ LÁCH")
    
    st.markdown("""
    **Phân loại (AAST):**
    - **Grade I-II:** Nhẹ (thường bảo tồn)
    - **Grade III-IV:** Trung bình-nặng (có thể bảo tồn hoặc phẫu thuật)
    - **Grade V:** Rất nặng (thường phẫu thuật)
    
    **Triệu chứng:**
    - Đau bụng trên trái
    - Hạ huyết áp
    - Shock
    - Có thể có vết thương vùng lách
    
    **Điều trị:**
    
    **1. Bảo tồn (Nếu ổn định):**
    - **Monitoring:** Sát trong 24-48h
    - **Truyền máu:** Nếu cần
    - **CT scan:** Theo dõi
    - **Lưu ý:** Nguy cơ vỡ muộn
    
    **2. Phẫu thuật (Nếu không ổn định):**
    - Shock không đáp ứng
    - Xuất huyết liên tục
    - Grade IV-V
    
    **3. Splenectomy:**
    - Nếu không thể bảo tồn
    - **Sau phẫu thuật:** Vaccination (Pneumococcus, Meningococcus, H. influenzae)
    
    **4. Monitoring:**
    - Huyết áp, HR
    - Hct, Hb
    - Platelets
    """)


def render_renal_injury():
    """Renal Injury"""
    st.warning("## ⚠️ VỠ THẬN")
    
    st.markdown("""
    **Phân loại (AAST):**
    - **Grade I-II:** Nhẹ (thường bảo tồn)
    - **Grade III-IV:** Trung bình-nặng (có thể bảo tồn hoặc phẫu thuật)
    - **Grade V:** Rất nặng (thường phẫu thuật)
    
    **Triệu chứng:**
    - Đau bụng/sườn
    - Tiểu máu
    - Hạ huyết áp (nếu xuất huyết nặng)
    
    **Điều trị:**
    
    **1. Bảo tồn (Nếu ổn định):**
    - **Monitoring:** Sát trong 24-48h
    - **Truyền máu:** Nếu cần
    - **CT scan:** Theo dõi
    
    **2. Phẫu thuật (Nếu không ổn định):**
    - Shock không đáp ứng
    - Xuất huyết liên tục
    - Grade IV-V
    
    **3. Monitoring:**
    - Huyết áp, HR
    - Hct, Hb
    - Creatinine, Urine output
    - Tiểu máu
    """)


def render_bowel_perforation():
    """Bowel Perforation"""
    st.error("## 🚨 VỠ RUỘT")
    
    st.markdown("""
    **Triệu chứng:**
    - Đau bụng
    - Bụng căng
    - Sốt
    - Viêm phúc mạc
    - Có thể có khí tự do
    
    **Chẩn đoán:**
    - **CT scan:** (ưu tiên)
    - **X-ray:** Khí tự do
    - **Lâm sàng:** Viêm phúc mạc
    
    **Điều trị:**
    
    **1. Phẫu thuật (Cấp cứu):**
    - **Chỉ định:** Vỡ ruột xác định
    - **Mục tiêu:** Sửa chữa hoặc cắt bỏ
    
    **2. Antibiotics:**
    - **Trước phẫu thuật:** Cefotetan 2g IV hoặc Cefoxitin 2g IV
    - **Hoặc:** Piperacillin-Tazobactam 4.5g IV
    - **Thời gian:** 24-48h
    
    **3. Monitoring:**
    - Triệu chứng viêm phúc mạc
    - Sốt
    - Bạch cầu
    - CT scan (nếu cần)
    """)


def render_vascular_injury():
    """Vascular Injury"""
    st.error("## 🚨🚨🚨 VỠ MẠCH MÁU - CẤP CỨU")
    
    st.markdown("""
    **Triệu chứng:**
    - Hạ huyết áp nặng
    - Shock
    - Bụng căng
    - Mất máu nặng
    
    **Chẩn đoán:**
    - **CT scan:** (nếu ổn định)
    - **Angiography:** (nếu cần)
    - **FAST:** Xuất huyết lớn
    
    **Điều trị:**
    
    **1. Resuscitation:**
    - **Truyền máu:** PRBC 4-6 đơn vị
    - **FFP:** 4-6 đơn vị
    - **Platelets:** Nếu cần
    - **Truyền dịch:** NS/LR bolus
    
    **2. Phẫu thuật (Cấp cứu):**
    - **Chỉ định:** Shock không đáp ứng
    - **Mục tiêu:** Kiểm soát xuất huyết
    
    **3. Angioembolization:**
    - Nếu ổn định
    - Tổn thương mạch máu nhỏ
    
    **4. Monitoring:**
    - Huyết áp, HR
    - Hct, Hb (mỗi 1-2h)
    - Lactate, Base deficit
    """)


def render_pancreatic_injury():
    """Pancreatic Injury"""
    st.warning("## ⚠️ CHẤN THƯƠNG TỤY")
    
    st.markdown("""
    **Triệu chứng:**
    - Đau bụng trên
    - Có thể có viêm tụy
    - Có thể có tổn thương ống tụy
    
    **Chẩn đoán:**
    - **CT scan:** (ưu tiên)
    - **Amylase, Lipase:** (có thể tăng)
    - **ERCP:** (nếu nghi ngờ tổn thương ống tụy)
    
    **Điều trị:**
    
    **1. Bảo tồn (Nếu nhẹ):**
    - **Monitoring:** Sát
    - **NPO:** Cho đến khi ổn định
    - **TPN:** Nếu cần
    
    **2. Phẫu thuật (Nếu nặng):**
    - Tổn thương ống tụy
    - Viêm tụy nặng
    - Biến chứng
    
    **3. Monitoring:**
    - Amylase, Lipase
    - Triệu chứng viêm tụy
    - CT scan (nếu cần)
    """)

