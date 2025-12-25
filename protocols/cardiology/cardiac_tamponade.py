"""
Cardiac Tamponade Protocol
ESC Guidelines 2024, AHA/ACC 2023
Life-threatening compression of the heart
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Cardiac Tamponade Management Protocol"""
    st.subheader("💔 Chèn Ép Tim (Cardiac Tamponade)")
    st.caption("ESC Guidelines 2024, AHA/ACC 2023 - Life-threatening compression of the heart")
    
    st.error("""
    **⚠️ CHÈN ÉP TIM = CẤP CỨU Y KHOA - TỬ VONG CAO**
    
    **Định nghĩa:**
    - Tích tụ dịch trong màng ngoài tim
    - Tăng áp lực màng ngoài tim
    - Chèn ép tim → Giảm đổ đầy tim → Giảm cung lượng tim
    
    **Triệu chứng (Beck's Triad):**
    - Hạ huyết áp
    - Tĩnh mạch cổ nổi (JVD)
    - Tim nhỏ, tiếng tim mờ
    
    **Thêm:**
    - Khó thở
    - Mạch nghịch (Pulsus Paradoxus)
    - Shock
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Intubation:**
        - Nếu suy hô hấp nặng
        - Giảm ý thức
        - Chuẩn bị trước khi chọc dò
        
        **Oxygen:**
        - **High-flow:** 10-15 L/min qua mask
        - **Mục tiêu:** SpO₂ ≥95%
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (theo dõi BP liên tục)
        - **Central line** (nếu cần)
        - **BP, HR:** Mỗi 5 phút
        """)
    
    with col2:
        st.warning("""
        **3. TRUYỀN DỊCH (Tạm thời)**
        
        - **NS:** 500-1000 mL bolus
        - **Mục đích:** Tăng tiền gánh tạm thời
        - **Lưu ý:** Chỉ tạm thời, không giải quyết nguyên nhân
        
        **4. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị thuốc cấp cứu
        
        **5. ECHO (Nếu có)**
        
        - Xác định chẩn đoán
        - Đánh giá lượng dịch
        - Hướng dẫn chọc dò
        """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán")
    
    st.info("""
    **Triệu chứng Lâm sàng:**
    - **Beck's Triad:**
      1. Hạ huyết áp
      2. Tĩnh mạch cổ nổi (JVD)
      3. Tim nhỏ, tiếng tim mờ
    
    - **Mạch nghịch (Pulsus Paradoxus):**
      - Giảm SBP >10 mmHg khi hít vào
      - Đo bằng sphygmomanometer
    
    - **Khác:**
      - Khó thở
      - Đau ngực
      - Shock
    
    **Cận lâm sàng:**
    - **ECG:** Điện thế thấp, thay đổi ST-T, điện thế luân phiên
    - **Chest X-ray:** Tim to, hình bầu rượu
    - **Echo:** Dịch màng ngoài tim, chèn ép tim
    - **CT scan:** (nếu cần)
    """)
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Đặc hiệu")
    
    st.error("## 🚨 PERICARDIOCENTESIS - ĐIỀU TRỊ CHÍNH")
    
    st.success("""
    **1. PERICARDIOCENTESIS (Chọc dò màng ngoài tim)**
    
    **Chỉ định:**
    - Chèn ép tim xác định
    - Shock không đáp ứng truyền dịch
    - Hạ huyết áp nặng
    
    **Kỹ thuật:**
    
    **A. Vị trí (Subxiphoid - Ưu tiên):**
    - Dưới mũi ức, góc 30-45°
    - Hướng về vai trái
    - Tránh gan, phổi
    
    **B. Dụng cụ:**
    - **Kim:** 18G, dài 15-20 cm
    - **Ống thông:** 6-8F (nếu cần)
    - **Echo guidance:** (ưu tiên)
    
    **C. Kỹ thuật:**
    1. Sát trùng vùng chọc
    2. Gây tê tại chỗ (Lidocaine 1-2%)
    3. Chọc kim dưới mũi ức, góc 30-45°
    4. Hướng về vai trái
    5. Hút dịch cho đến khi hết chèn ép
    6. Đặt ống thông (nếu cần)
    
    **D. Hiệu quả:**
    - Huyết áp cải thiện ngay
    - JVD giảm
    - Triệu chứng cải thiện
    
    **E. Biến chứng:**
    - Chọc vào tim (rối loạn nhịp, chảy máu)
    - Chọc vào phổi (tràn khí màng phổi)
    - Chọc vào gan
    - Nhiễm trùng
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Tìm Nguyên nhân")
    
    with st.expander("📋 Xem các nguyên nhân thường gặp", expanded=False):
        st.markdown("""
        **Cấp tính:**
        - Chấn thương ngực
        - Vỡ tim (sau nhồi máu)
        - Vỡ phình động mạch chủ
        - Thủng tim (do thủ thuật)
        - Xuất huyết (do thuốc chống đông)
        
        **Bán cấp:**
        - Viêm màng ngoài tim
        - Ung thư (di căn)
        - Suy thận (uremia)
        - Sau phẫu thuật tim
        
        **Mạn tính:**
        - Viêm màng ngoài tim co thắt
        - Ung thư
        - Suy thận
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Truyền dịch:**
    - **NS:** 500-1000 mL bolus
    - **Mục đích:** Tăng tiền gánh tạm thời
    - **Lưu ý:** Chỉ tạm thời
    
    **2. Inotropes (Nếu cần):**
    - **Dobutamine:** 2-20 mcg/kg/min
    - **Norepinephrine:** 0.05-0.2 mcg/kg/min
    - **Lưu ý:** Chỉ tạm thời, không giải quyết nguyên nhân
    
    **3. Điều trị Nguyên nhân:**
    - **Viêm màng ngoài tim:** NSAIDs, Colchicine, Corticosteroids
    - **Ung thư:** Hóa trị, Xạ trị
    - **Suy thận:** Lọc máu
    - **Chấn thương:** Phẫu thuật
    
    **4. Monitoring:**
    - Huyết áp, HR (mỗi 5-15 phút)
    - JVD
    - Echo (nếu cần)
    - Lượng dịch chọc ra
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Lưu ý Đặc biệt")
    
    st.warning("""
    **1. Chống chỉ định Pericardiocentesis:**
    - Rối loạn đông máu nặng
    - Không có dịch (nếu xác định)
    - Bệnh nhân không hợp tác
    
    **2. Thận trọng:**
    - Chọc vào tim (rối loạn nhịp, chảy máu)
    - Chọc vào phổi (tràn khí màng phổi)
    - Chọc vào gan
    
    **3. Sau Pericardiocentesis:**
    - Theo dõi sát huyết áp
    - Đánh giá lại dịch (nếu tái tích tụ)
    - Điều trị nguyên nhân
    - Có thể cần phẫu thuật (nếu tái phát)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Tiên lượng & Theo dõi")
    
    st.info("""
    **Tiên lượng:**
    - **Tốt:** Nếu điều trị sớm và đúng
    - **Xấu:** Nếu chậm trễ (tử vong cao)
    - **Yếu tố nguy cơ:**
      - Chậm trễ điều trị
      - Nguyên nhân ác tính
      - Tái phát
    
    **Theo dõi:**
    - **Huyết áp, HR:** Mỗi 5-15 phút (cho đến khi ổn định)
    - **JVD:** Mỗi 15-30 phút
    - **Echo:** Sau chọc dò (nếu cần)
    - **Lượng dịch:** Nếu có ống thông
    
    **Xuất viện:**
    - Huyết áp ổn định
    - Không tái tích tụ dịch
    - Đã điều trị nguyên nhân
    - Theo dõi ít nhất 24-48h
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("Cardiac Tamponade")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ESC Guidelines 2024** - European Society of Cardiology
        2. **AHA/ACC Guidelines 2023** - American Heart Association
        3. **UpToDate:** Cardiac Tamponade - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

