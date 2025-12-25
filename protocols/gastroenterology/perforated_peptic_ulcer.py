"""
Perforated Peptic Ulcer Protocol
ACG Guidelines 2024, WSES Guidelines 2024
Surgical emergency requiring immediate treatment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Perforated Peptic Ulcer Management Protocol"""
    st.subheader("🫀 Thủng Dạ Dày Tá Tràng (Perforated Peptic Ulcer)")
    st.caption("ACG Guidelines 2024, WSES Guidelines 2024 - Surgical emergency")
    
    st.error("""
    **⚠️ THỦNG DẠ DÀY TÁ TRÀNG = CẤP CỨU NGOẠI KHOA**
    
    **Định nghĩa:**
    - Thủng dạ dày hoặc tá tràng
    - Dịch tiêu hóa vào ổ bụng → Viêm phúc mạc
    - Cần phẫu thuật cấp cứu
    
    **Triệu chứng Điển Hình:**
    - **Đau bụng:** Đột ngột, dữ dội, lan tỏa
    - **Cứng bụng:** (board-like rigidity)
    - **Sốt:** (nếu viêm phúc mạc)
    - **Nôn:** (có thể)
    - **Shock:** (nếu nặng)
    
    **Nguyên nhân:**
    - Loét dạ dày/tá tràng
    - NSAIDs
    - H. pylori
    - Stress ulcers
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
        - Chuẩn bị phẫu thuật
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 1000-2000 mL bolus
        - **Mục tiêu:** SBP ≥90 mmHg
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị truyền máu
        
        **4. LABS NGAY:**
        - **CBC:** Hct, Hb, WBC
        - **BMP:** Creatinine, Electrolytes
        - **Amylase, Lipase:** (loại trừ viêm tụy)
        - **Lactate:** (đánh giá tưới máu)
        - **Type & Screen:** (chuẩn bị phẫu thuật)
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Tiêu chuẩn Chẩn đoán:**
    - Đau bụng đột ngột, dữ dội
    - Cứng bụng (board-like rigidity)
    - Có thể có sốt
    - Có thể có shock
    
    **Xét nghiệm:**
    - **Chest X-ray:** Khí tự do dưới cơ hoành (quan trọng!)
    - **CT scan:** (nếu cần, xác định vị trí)
    - **Labs:** WBC tăng, Lactate tăng (nếu nặng)
    
    **Lưu ý:**
    - Không cần chờ tất cả xét nghiệm
    - Nếu nghi ngờ cao → Phẫu thuật ngay
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Trước Phẫu thuật")
    
    st.success("""
    **1. Resuscitation:**
    - **Truyền dịch:** NS 1000-2000 mL bolus
    - **Truyền máu:** PRBC nếu cần
    - **Mục tiêu:** SBP ≥90 mmHg
    
    **2. Antibiotics:**
    - **Cefotetan:** 2 g IV
    - **Hoặc:** Cefoxitin 2 g IV
    - **Hoặc:** Piperacillin-Tazobactam 4.5 g IV
    - **Mục đích:** Phòng ngừa nhiễm trùng
    
    **3. NGT (Nasogastric Tube):**
    - **Chỉ định:** Giảm áp lực dạ dày
    - **Lưu ý:** Thận trọng (có thể làm nặng thủng)
    
    **4. Pain Management:**
    - **Morphine:** 2-5 mg IV
    - **Fentanyl:** 50-100 mcg IV
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔪 Phẫu thuật")
    
    st.error("## 🚨 PHẪU THUẬT CẤP CỨU - CHỈ ĐỊNH")
    
    st.success("""
    **Chỉ định:**
    - Tất cả bệnh nhân thủng dạ dày/tá tràng
    - Càng sớm càng tốt
    
    **Kỹ thuật:**
    
    **1. Laparoscopic Repair (Ưu tiên):**
    - Ít xâm lấn
    - Phục hồi nhanh
    - Chỉ định: Nếu ổn định, thủng nhỏ
    
    **2. Open Repair:**
    - Chỉ định: Nếu không thể laparoscopic
    - Hoặc: Thủng lớn, viêm phúc mạc nặng
    
    **3. Options:**
    - **Simple closure:** (thủng nhỏ)
    - **Omental patch:** (thủng tá tràng)
    - **Partial gastrectomy:** (thủng lớn, dạ dày)
    
    **4. Post-op:**
    - **Antibiotics:** 24-48h
    - **PPI:** (điều trị loét)
    - **H. pylori:** Test và điều trị
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Post-operative:**
    - **NPO:** Cho đến khi có nhu động ruột
    - **NGT:** (nếu cần)
    - **Antibiotics:** 24-48h
    - **PPI:** Omeprazole 40 mg IV bid
    
    **2. H. pylori Treatment:**
    - **Test:** Nếu chưa test
    - **Điều trị:** Triple therapy (nếu dương tính)
    
    **3. Monitoring:**
    - **Huyết áp, HR:** Mỗi 1-2h
    - **Triệu chứng:** Mỗi 2-4h
    - **Labs:** WBC, Creatinine mỗi 12-24h
    
    **4. Complications:**
    - Nhiễm trùng vết mổ
    - Rò dạ dày/tá tràng
    - Áp xe ổ bụng
    - Tắc ruột
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Tốt:** Nếu phẫu thuật sớm (<24h)
    - **Xấu:** Nếu chậm trễ (>24h)
    - **Tử vong:** 5-10% (nếu điều trị đúng)
    - **Yếu tố nguy cơ:**
      - Chậm trễ phẫu thuật
      - Tuổi cao
      - Bệnh kèm theo
      - Viêm phúc mạc nặng
    
    **Theo dõi:**
    - **ICU:** Ít nhất 24-48h
    - **Huyết áp, HR:** Mỗi 1-2h
    - **Triệu chứng:** Mỗi 2-4h
    - **Labs:** Mỗi 12-24h
    
    **Xuất viện:**
    - Ổn định sau phẫu thuật
    - Có nhu động ruột
    - Không biến chứng
    - Theo dõi ít nhất 3-5 ngày
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Perforated Peptic Ulcer")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ACG Guidelines 2024** - American College of Gastroenterology
        2. **WSES Guidelines 2024** - World Society of Emergency Surgery
        3. **UpToDate:** Perforated Peptic Ulcer - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

