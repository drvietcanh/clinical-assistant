"""
Chest Trauma Protocol
ATLS Guidelines 2024, EAST Guidelines 2024
Life-threatening trauma requiring immediate assessment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Chest Trauma Management Protocol"""
    st.subheader("🫁 Chấn Thương Ngực (Chest Trauma)")
    st.caption("ATLS Guidelines 2024, EAST Guidelines 2024 - Life-threatening trauma")
    
    st.error("""
    **⚠️ CHẤN THƯƠNG NGỰC = CẤP CỨU Y KHOA**
    
    **Các Tổn thương Nguy hiểm:**
    - **Tràn khí màng phổi áp lực (Tension Pneumothorax)**
    - **Tràn máu màng phổi lớn (Massive Hemothorax)**
    - **Vỡ tim (Cardiac Tamponade)**
    - **Vỡ động mạch chủ (Aortic Rupture)**
    - **Vỡ cơ hoành (Diaphragmatic Rupture)**
    - **Flail Chest**
    - **Tràn khí trung thất (Pneumomediastinum)**
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu giảm ý thức (GCS <8)
        - Suy hô hấp nặng
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
            "Tràn khí màng phổi áp lực (Tension Pneumothorax)",
            "Tràn máu màng phổi lớn (Massive Hemothorax)",
            "Tràn khí màng phổi đơn giản (Simple Pneumothorax)",
            "Vỡ tim (Cardiac Tamponade)",
            "Flail Chest",
            "Tràn khí trung thất (Pneumomediastinum)",
            "Vỡ động mạch chủ (Aortic Rupture)"
        ],
        key="chest_trauma_type"
    )
    
    st.markdown("---")
    
    if "Tension Pneumothorax" in injury_type:
        render_tension_pneumothorax()
    elif "Massive Hemothorax" in injury_type:
        render_massive_hemothorax()
    elif "Simple Pneumothorax" in injury_type:
        render_simple_pneumothorax()
    elif "Cardiac Tamponade" in injury_type:
        render_cardiac_tamponade()
    elif "Flail Chest" in injury_type:
        render_flail_chest()
    elif "Pneumomediastinum" in injury_type:
        render_pneumomediastinum()
    else:  # Aortic Rupture
        render_aortic_rupture()
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Pain Management:**
    - **Morphine:** 2-5 mg IV (thận trọng)
    - **Fentanyl:** 50-100 mcg IV
    - **Regional anesthesia:** Nếu có thể
    
    **2. Respiratory Support:**
    - **CPAP/BiPAP:** Nếu suy hô hấp nhẹ-trung bình
    - **Intubation:** Nếu suy hô hấp nặng
    - **Ventilation:** Lung protective strategy
    
    **3. Monitoring:**
    - **Continuous:** ECG, SpO₂, BP
    - **Frequent:** HR, RR, GCS
    - **Chest X-ray:** Nếu ổn định
    - **CT scan:** Nếu nghi ngờ tổn thương phức tạp
    
    **4. Prophylaxis:**
    - **VTE prophylaxis:** Nếu không chống chỉ định
    - **Stress ulcer prophylaxis:** Nếu cần
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi & Đánh giá")
    
    st.info("""
    **Theo dõi trong 24-48h đầu:**
    
    **Lâm sàng:**
    - Triệu chứng hô hấp (mỗi 1-2h)
    - Dấu hiệu sinh tồn (mỗi 1-2h)
    - Đánh giá ngực (mỗi 4-6h)
    - Đánh giá thần kinh (mỗi 2-4h)
    
    **Cận lâm sàng:**
    - Chest X-ray (ban đầu và sau 6-12h)
    - CT scan (nếu cần)
    - ABG (nếu suy hô hấp)
    
    **Dấu hiệu cải thiện:**
    - ✅ Giảm khó thở
    - ✅ SpO₂ ≥95%
    - ✅ Huyết áp ổn định
    - ✅ Giảm đau
    
    **Dấu hiệu xấu đi:**
    - ⚠️ Khó thở tăng
    - ⚠️ SpO₂ giảm
    - ⚠️ Hạ huyết áp
    - ⚠️ Tràn khí/tràn máu tăng
    - 🚨 Cần phẫu thuật
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Chest Trauma")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ATLS Guidelines 2024** - Advanced Trauma Life Support
        2. **EAST Guidelines 2024** - Eastern Association for the Surgery of Trauma
        3. **UpToDate:** Chest Trauma - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_tension_pneumothorax():
    """Tension Pneumothorax"""
    st.error("## 🚨🚨 TRÀN KHÍ MÀNG PHỔI ÁP LỰC - CẤP CỨU")
    
    st.markdown("""
    **Triệu chứng:**
    - Khó thở dữ dội
    - Đau ngực
    - Tím tái
    - Hạ huyết áp
    - Tĩnh mạch cổ nổi
    - Lệch khí quản
    - Mất ran phổi 1 bên
    - Gõ vang 1 bên
    
    **Điều trị NGAY (Không chờ X-ray):**
    
    **1. Needle Decompression:**
    - **Vị trí:** Khoang liên sườn 2, đường giữa xương đòn
    - **Kim:** 14-16G, dài 5-8 cm
    - **Kỹ thuật:** Chọc thẳng, vuông góc với thành ngực
    - **Hiệu quả:** Nghe tiếng xì khí
    
    **2. Chest Tube (Sau khi needle decompression):**
    - **Vị trí:** Khoang liên sườn 4-5, đường nách giữa
    - **Kích thước:** 28-32F (người lớn)
    - **Hút:** -20 cmH₂O
    
    **3. Monitoring:**
    - SpO₂, BP, HR
    - Đánh giá lại sau 15-30 phút
    """)


def render_massive_hemothorax():
    """Massive Hemothorax"""
    st.error("## 🚨🚨 TRÀN MÁU MÀNG PHỔI LỚN - CẤP CỨU")
    
    st.markdown("""
    **Định nghĩa:**
    - Tràn máu ≥1500 mL (1/3 thể tích máu)
    - Hoặc tràn máu liên tục ≥200 mL/h
    
    **Triệu chứng:**
    - Khó thở
    - Hạ huyết áp
    - Mất ran phổi 1 bên
    - Gõ đục 1 bên
    - Shock
    
    **Điều trị:**
    
    **1. Chest Tube:**
    - **Vị trí:** Khoang liên sườn 4-5, đường nách giữa
    - **Kích thước:** 32-36F (người lớn)
    - **Hút:** -20 cmH₂O
    
    **2. Truyền máu:**
    - **PRBC:** 2-4 đơn vị
    - **FFP:** 2-4 đơn vị (nếu cần)
    - **Platelets:** Nếu giảm tiểu cầu
    
    **3. Chỉ định Phẫu thuật:**
    - Tràn máu ≥1500 mL ban đầu
    - Tràn máu liên tục ≥200 mL/h
    - Shock không đáp ứng
    - Tổn thương mạch máu lớn
    
    **4. Monitoring:**
    - Lượng máu chảy ra
    - Huyết áp, HR
    - Hct, Hb
    """)


def render_simple_pneumothorax():
    """Simple Pneumothorax"""
    st.warning("## ⚠️ TRÀN KHÍ MÀNG PHỔI ĐƠN GIẢN")
    
    st.markdown("""
    **Triệu chứng:**
    - Khó thở nhẹ-trung bình
    - Đau ngực
    - Mất ran phổi 1 bên
    - Gõ vang 1 bên
    
    **Điều trị:**
    
    **1. Nhỏ (<20%):**
    - **Theo dõi:** Nếu không triệu chứng
    - **Oxygen:** 100% (tăng hấp thu khí)
    - **Theo dõi:** Chest X-ray sau 6-12h
    
    **2. Trung bình-Lớn (≥20%):**
    - **Chest Tube:** Khoang liên sườn 4-5
    - **Kích thước:** 20-24F
    - **Hút:** -20 cmH₂O
    
    **3. Monitoring:**
    - SpO₂, triệu chứng
    - Chest X-ray sau 6-12h
    """)


def render_cardiac_tamponade():
    """Cardiac Tamponade"""
    st.error("## 🚨🚨🚨 VỠ TIM / CHÈN ÉP TIM - CẤP CỨU")
    
    st.markdown("""
    **Triệu chứng (Beck's Triad):**
    - Hạ huyết áp
    - Tĩnh mạch cổ nổi
    - Tim nhỏ, tiếng tim mờ
    
    **Thêm:**
    - Khó thở
    - Mạch nghịch (Pulsus Paradoxus)
    - Shock
    
    **Điều trị:**
    
    **1. Pericardiocentesis (Cấp cứu):**
    - **Vị trí:** Dưới mũi ức, góc 45°
    - **Kim:** 18G, dài 15-20 cm
    - **Kỹ thuật:** Hướng về vai trái
    - **Hiệu quả:** Máu ra, huyết áp cải thiện
    
    **2. Phẫu thuật:**
    - **Chỉ định:** Nếu pericardiocentesis thất bại
    - **Cấp cứu:** Mở ngực
    
    **3. Truyền dịch:**
    - **NS:** 500-1000 mL bolus
    - Tăng tiền gánh
    
    **4. Monitoring:**
    - Huyết áp, HR
    - ECG
    - Echo (nếu có)
    """)


def render_flail_chest():
    """Flail Chest"""
    st.warning("## 🚨 FLẠI CHEST")
    
    st.markdown("""
    **Định nghĩa:**
    - ≥3 xương sườn gãy ở ≥2 vị trí
    - Di động ngược (paradoxical movement)
    
    **Triệu chứng:**
    - Khó thở
    - Đau ngực
    - Di động ngược
    - Có thể có phù phổi
    
    **Điều trị:**
    
    **1. Pain Management:**
    - **Epidural:** (ưu tiên)
    - **Paravertebral block**
    - **Opioids:** Morphine, Fentanyl
    
    **2. Respiratory Support:**
    - **CPAP/BiPAP:** Nếu suy hô hấp nhẹ-trung bình
    - **Intubation:** Nếu suy hô hấp nặng
    - **Ventilation:** Lung protective strategy
    
    **3. Surgical Fixation:**
    - **Chỉ định:** Nếu cần thở máy kéo dài
    - **Lợi ích:** Giảm thời gian thở máy
    
    **4. Monitoring:**
    - SpO₂, ABG
    - Đánh giá hô hấp
    """)


def render_pneumomediastinum():
    """Pneumomediastinum"""
    st.warning("## ⚠️ TRÀN KHÍ TRUNG THẤT")
    
    st.markdown("""
    **Triệu chứng:**
    - Đau ngực
    - Khó thở
    - Khó nuốt
    - Crepitus cổ
    
    **Nguyên nhân:**
    - Vỡ phế quản
    - Vỡ thực quản
    - Barotrauma
    
    **Điều trị:**
    
    **1. Đánh giá:**
    - **CT scan:** Đánh giá tổn thương
    - **Esophagoscopy:** Nếu nghi ngờ vỡ thực quản
    - **Bronchoscopy:** Nếu nghi ngờ vỡ phế quản
    
    **2. Điều trị:**
    - **Vỡ thực quản:** Phẫu thuật cấp cứu
    - **Vỡ phế quản:** Phẫu thuật cấp cứu
    - **Tự phát:** Theo dõi, thường tự khỏi
    
    **3. Monitoring:**
    - Triệu chứng
    - Chest X-ray/CT
    """)


def render_aortic_rupture():
    """Aortic Rupture"""
    st.error("## 🚨🚨🚨 VỠ ĐỘNG MẠCH CHỦ - CẤP CỨU")
    
    st.markdown("""
    **Triệu chứng:**
    - Hạ huyết áp nặng
    - Shock
    - Đau ngực/lưng
    - Mạch yếu/chênh lệch
    - Tổn thương cột sống
    
    **Chẩn đoán:**
    - **CT scan:** (ưu tiên)
    - **Chest X-ray:** Tim to, trung thất rộng
    - **Echo:** Nếu có
    
    **Điều trị:**
    
    **1. Ổn định Huyết áp:**
    - **Mục tiêu:** SBP 90-100 mmHg
    - **Beta-blockers:** Esmolol, Labetalol
    - **Nitroprusside:** Nếu cần
    - **Tránh:** Tăng huyết áp (làm nặng vỡ)
    
    **2. Phẫu thuật:**
    - **Cấp cứu:** Mở ngực
    - **Hoặc:** Endovascular repair (nếu có thể)
    
    **3. Truyền máu:**
    - **PRBC:** 4-6 đơn vị
    - **FFP:** 4-6 đơn vị
    - **Platelets:** Nếu cần
    
    **4. Monitoring:**
    - Huyết áp (mục tiêu thấp)
    - HR
    - Triệu chứng
    """)

