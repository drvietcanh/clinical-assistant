"""
Sepsis 1-Hour Bundle Protocol
Surviving Sepsis Campaign 2021
"""

import streamlit as st


def render():
    """Sepsis 1-Hour Bundle Protocol"""
    st.subheader("🦠 Sepsis 1-Hour Bundle")
    st.caption("Surviving Sepsis Campaign 2021")
    
    st.info("""
    **Chẩn đoán Sepsis:**
    - Nhiễm trùng (nghi ngờ hoặc xác định)
    - qSOFA ≥2 hoặc SOFA tăng ≥2 điểm
    - Rối loạn chức năng cơ quan
    """)
    
    st.markdown("---")
    
    st.markdown("### ⏱️ Sepsis 1-Hour Bundle")
    
    st.error("""
    **Thực hiện NGAY trong vòng 1 GIỜ:**
    
    1. ✅ **Đo Lactate**
       - Lactate >2 mmol/L = septic shock
       - Đo lại sau 2-4h nếu tăng
    
    2. ✅ **Cấy máu trước khi kháng sinh**
       - 2 bộ cấy máu (từ 2 vị trí khác nhau)
       - Cấy dịch từ ổ nhiễm (nếu có)
    
    3. ✅ **Kháng sinh phổ rộng**
       - Trong vòng 1 giờ
       - Theo guideline địa phương
       - Liều đủ, đường IV
    
    4. ✅ **Truyền dịch nhanh**
       - 30 mL/kg crystalloid
       - Trong 3 giờ đầu
       - Ringer Lactate hoặc Normal Saline
    
    5. ✅ **Vasopressor nếu hạ huyết áp**
       - Nếu MAP <65 mmHg sau truyền dịch
       - Norepinephrine là thuốc đầu tay
       - Mục tiêu MAP ≥65 mmHg
    """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Lựa Chọn Kháng Sinh Thực Nghiệm")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **Nhiễm trùng cộng đồng:**
        - Ceftriaxone 2g IV q24h
        + Azithromycin 500mg IV q24h
        
        **Hoặc:**
        - Piperacillin-Tazobactam 4.5g IV q6h
        """)
    
    with col2:
        st.warning("""
        **Nhiễm trùng bệnh viện:**
        - Meropenem 1g IV q8h
        + Vancomycin 15-20mg/kg IV
        
        **Hoặc:**
        - Piperacillin-Tazobactam 4.5g IV q6h
        + Vancomycin
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị (First 6 Hours)")
    
    st.info("""
    **Resuscitation Goals:**
    - MAP ≥65 mmHg
    - Urine output ≥0.5 mL/kg/h
    - Lactate bình thường hóa
    - ScvO2 ≥70% (nếu đo được)
    
    **Monitoring:**
    - Vital signs q15-30min
    - Lactate q2-4h cho đến bình thường
    - Urine output hourly
    - Consider arterial line
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Vasopressor/Inotrope")
    
    st.error("""
    **Lựa chọn vasopressor:**
    
    **1st line: Norepinephrine**
    - 0.05-2 mcg/kg/min
    - Mục tiêu MAP ≥65 mmHg
    
    **2nd line: Vasopressin**
    - 0.03-0.04 units/min
    - Thêm vào nếu norepinephrine không đủ
    
    **3rd line: Epinephrine**
    - 0.05-2 mcg/kg/min
    - Nếu cần thêm vasopressor
    
    **Inotrope: Dobutamine**
    - 2.5-20 mcg/kg/min
    - Nếu cardiac output thấp
    """)
    
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        **Surviving Sepsis Campaign Guidelines 2021**
        
        **Key Changes:**
        - 1-hour bundle (từ 3-hour và 6-hour)
        - Lactate measurement mandatory
        - Blood culture before antibiotics
        - 30 mL/kg crystalloid in 3 hours
        
        **Reference:**
        Evans L, et al. Surviving Sepsis Campaign: International Guidelines for Management of Sepsis and Septic Shock 2021. Crit Care Med. 2021;49(11):e1063-e1143.
        
        **Link:**
        https://www.sccm.org/SurvivingSepsisCampaign
        """)

