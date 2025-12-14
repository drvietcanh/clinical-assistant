"""
Shock Management Protocol
Phân loại và xử trí các loại sốc trong cấp cứu
"""

import streamlit as st


def render():
    """Shock Management Protocol"""
    st.subheader("💔 Quản lý Sốc")
    st.caption("Phân loại và xử trí sốc")
    
    st.info("""
    **Định nghĩa sốc:**
    - Tình trạng suy tuần hoàn dẫn đến giảm cung cấp oxy và chất dinh dưỡng đến mô
    - Dấu hiệu: Hạ huyết áp (MAP <65 mmHg), giảm tưới máu mô
    - Cần xử trí ngay lập tức để tránh tổn thương cơ quan không hồi phục
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔍 Phân Loại Sốc")
    
    # Classification tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🦠 Nhiễm Trùng",
        "💧 Giảm Thể Tích",
        "❤️ Tim",
        "🌊 Phân Bố",
        "🚫 Tắc Nghẽn"
    ])
    
    with tab1:
        st.markdown("#### 🦠 Sốc Nhiễm Trùng (Septic Shock)")
        
        st.error("""
        **Chẩn đoán:**
        - Nhiễm trùng đã xác định hoặc nghi ngờ
        - MAP <65 mmHg (hoặc SBP <90 mmHg) sau truyền dịch ≥30 mL/kg
        - Lactate >2 mmol/L
        - Cần vasopressor để duy trì MAP ≥65 mmHg
        
        **Nguyên nhân thường gặp:**
        - Nhiễm trùng phổi, bụng, tiết niệu, da/mô mềm
        - Gram-negative, Gram-positive, nấm
        """)
        
        st.markdown("##### ⚡ Xử trí Ngay")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **Trong 1 giờ đầu:**
            
            1. ✅ **Đo Lactate**
               - Nếu >2 mmol/L → sốc nhiễm trùng
               - Đo lại sau 2-4h
            
            2. ✅ **Cấy máu**
               - 2 bộ từ 2 vị trí
               - Trước khi dùng kháng sinh
            
            3. ✅ **Kháng sinh IV**
               - Phổ rộng, trong 1 giờ
               - Liều đủ theo cân nặng
            
            4. ✅ **Truyền dịch**
               - 30 mL/kg crystalloid
               - Trong 3 giờ đầu
            """)
        
        with col2:
            st.warning("""
            **Vasopressor:**
            
            **1st line: Norepinephrine**
            - 0.05-2 mcg/kg/min
            - Mục tiêu MAP ≥65 mmHg
            
            **2nd line: Vasopressin**
            - 0.03-0.04 units/min
            - Thêm nếu NE không đủ
            
            **3rd line: Epinephrine**
            - 0.05-2 mcg/kg/min
            
            **Inotrope: Dobutamine**
            - 2.5-20 mcg/kg/min
            - Nếu CO thấp
            """)
        
        st.markdown("##### 🎯 Mục tiêu điều trị")
        st.info("""
        - MAP ≥65 mmHg
        - Urine output ≥0.5 mL/kg/h
        - Lactate bình thường hóa
        - ScvO2 ≥70% (nếu đo được)
        - CVP 8-12 mmHg (nếu đo được)
        """)
    
    with tab2:
        st.markdown("#### 💧 Sốc Giảm Thể Tích (Hypovolemic Shock)")
        
        st.error("""
        **Chẩn đoán:**
        - Mất máu hoặc dịch (mất qua đường nào đó)
        - Dấu hiệu: Da lạnh, nổi da gà, tĩnh mạch cổ xẹp
        - Hạ huyết áp, nhịp tim nhanh
        - Lượng nước tiểu giảm
        
        **Nguyên Nhân:**
        - Chảy máu (chấn thương, xuất huyết tiêu hóa, v.v.)
        - Mất dịch (bỏng, tiêu chảy, nôn, đái tháo đường)
        """)
        
        st.markdown("##### ⚡ Xử trí")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **1. Kiểm soát chảy máu:**
            - Ép trực tiếp
            - Gạc Hemostatic
            - Phẫu thuật nếu cần
            
            **2. Truyền dịch:**
            - Bolus 500-1000 mL NS/RL
            - Lặp lại nếu cần
            - Có thể cần 2-3 L ban đầu
            
            **3. Theo dõi:**
            - Dấu hiệu sống mỗi 5-15 phút
            - Đáp ứng với dịch truyền
            """)
        
        with col2:
            st.warning("""
            **4. Truyền máu nếu:**
            - Mất máu >30% thể tích
            - Hb <7 g/dL (hoặc <10 nếu tim mạch)
            - Đang chảy máu tích cực
            
            **5. Dịch thay thế:**
            - NS: Mất máu, chấn thương
            - RL: Tốt hơn cho chuyển hóa
            - Albumin: Nếu giảm albumin
            - Máu: Mất máu đáng kể
            """)
        
        st.markdown("##### 🎯 Mục tiêu")
        st.info("""
        - SBP ≥90 mmHg
        - HR <100 bpm
        - Urine output ≥0.5 mL/kg/h
        - Mentation cải thiện
        - Da ấm, khô
        """)
    
    with tab3:
        st.markdown("#### ❤️ Sốc Tim (Cardiogenic Shock)")
        
        st.error("""
        **Chẩn đoán:**
        - Suy chức năng tim (giảm CO)
        - Dấu hiệu ứ máu (tĩnh mạch cổ nổi, phù phổi)
        - Hạ huyết áp mặc dù thể tích đủ
        - Cold extremities
        
        **Nguyên Nhân:**
        - Nhồi máu cơ tim cấp
        - Rối loạn nhịp tim
        - Bệnh cơ tim, van tim
        - Thuyên tắc phổi lớn
        """)
        
        st.markdown("##### ⚡ Xử trí")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **1. Hỗ trợ hô hấp:**
            - O₂ cao nếu cần
            - CPAP/BiPAP nếu phù phổi
            - Thở máy nếu suy hô hấp
            
            **2. Điều trị nguyên nhân:**
            - STEMI: PCI ngay (<90 phút)
            - Rối loạn nhịp: Điều chỉnh nhịp
            - PE: Kháng đông/thrombolytic
            
            **3. Hỗ trợ huyết động:**
            - Cẩn thận với dịch truyền
            - Dùng inotrope
            """)
        
        with col2:
            st.warning("""
            **4. Inotrope/Vasopressor:**
            
            **Dobutamine**
            - 2.5-20 mcg/kg/min
            - Tăng CO, giảm SVR
            
            **Norepinephrine**
            - 0.05-2 mcg/kg/min
            - Nếu MAP thấp + CO thấp
            
            **Epinephrine**
            - 0.05-2 mcg/kg/min
            - Sốc tim nặng
            
            **Milrinone**
            - 0.125-0.75 mcg/kg/min
            - Bệnh nhân dùng beta-blocker
            """)
        
        st.markdown("##### 🎯 Mục tiêu")
        st.info("""
        - MAP ≥65 mmHg
        - CO >2.2 L/min/m²
        - CI >2.2 L/min/m²
        - PCWP 15-18 mmHg
        - Urine output ≥0.5 mL/kg/h
        """)
        
        st.error("""
        **⚠️ Tránh:**
        - Truyền dịch quá nhiều (làm nặng phù phổi)
        - Dùng thuốc giãn mạch đơn độc nếu hạ huyết áp
        """)
    
    with tab4:
        st.markdown("#### 🌊 Sốc Phân Bố (Distributive Shock)")
        
        st.error("""
        **Đặc điểm:**
        - Giảm SVR (kháng lực mạch máu hệ thống)
        - CO có thể bình thường hoặc tăng
        - Warm extremities (trừ sốc nhiễm trùng nặng)
        
        **Nguyên Nhân:**
        - Sốc nhiễm trùng (phổ biến nhất)
        - Sốc phản vệ
        - Sốc thần kinh
        - Ngộ độc (beta-blocker, calcium channel blocker)
        """)
        
        st.markdown("##### ⚡ Xử trí")
        
        st.success("""
        **1. Xử trí theo nguyên nhân:**
        
        **Sốc phản vệ:**
        - Epinephrine 0.3-0.5 mg IM (có thể lặp lại)
        - Diphenhydramine 25-50 mg IV
        - Methylprednisolone 125 mg IV
        - Albuterol nếu co thắt phế quản
        
        **Sốc thần kinh:**
        - Điều trị nguyên nhân (chấn thương cột sống, chấn thương sọ não)
        - Fluid resuscitation
        - Vasopressor (norepinephrine hoặc phenylephrine)
        
        **2. Hỗ trợ huyết động:**
        - Truyền dịch (cẩn thận với sốc thần kinh)
        - Vasopressor để duy trì MAP
        """)
    
    with tab5:
        st.markdown("#### 🚫 Sốc Tắc Nghẽn (Obstructive Shock)")
        
        st.error("""
        **Đặc điểm:**
        - Tắc nghẽn dòng máu về hoặc đi từ tim
        - CO giảm do cơ học
        
        **Nguyên Nhân:**
        - Thuyên tắc phổi lớn (massive PE)
        - Chèn ép tim (tamponade)
        - Tràn khí màng phổi áp lực (tension pneumothorax)
        - Hẹp động mạch chủ nặng
        """)
        
        st.markdown("##### ⚡ Xử trí")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **Thuyên tắc phổi:**
            - Kháng đông ngay (Heparin/LMWH)
            - Thrombolytic nếu sốc
            - Embolectomy nếu có
            
            **Tamponade:**
            - Pericardiocentesis ngay
            - Hồi sức dịch tạm thời
            - Phẫu thuật nếu cần
            """)
        
        with col2:
            st.warning("""
            **Tension pneumothorax:**
            - Needle decompression ngay
            - 14G needle, 2nd ICS, MCL
            - Sau đó đặt ống dẫn lưu
            
            **Hẹp động mạch chủ:**
            - Phẫu thuật/valvuloplasty
            - Hỗ trợ huyết động tạm thời
            """)
        
        st.markdown("##### 🎯 Mục tiêu")
        st.info("""
        - Xử trí nguyên nhân tắc nghẽn NGAY
        - Hỗ trợ huyết động tạm thời trong lúc xử trí
        - MAP ≥65 mmHg
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục tiêu Chung Điều trị Sốc")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("MAP", "≥65 mmHg")
        st.metric("SBP", "≥90 mmHg")
    
    with col2:
        st.metric("Urine Output", "≥0.5 mL/kg/h")
        st.metric("Lactate", "<2 mmol/L")
    
    with col3:
        st.metric("ScvO2", "≥70%")
        st.metric("CI", ">2.2 L/min/m²")
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Theo dõi")
    
    st.info("""
    **Monitoring trong sốc:**
    
    **Cơ bản:**
    - Dấu hiệu sống mỗi 5-15 phút (cho đến ổn định)
    - Urine output hourly
    - Mental status
    
    **Nâng cao (nếu có):**
    - Arterial line (đo huyết áp liên tục)
    - Central venous pressure (CVP)
    - Cardiac output (Swan-Ganz nếu cần)
    - Lactate q2-4h
    - ABG để đánh giá tưới máu mô
    """)
    
    st.markdown("---")
    
    with st.expander("📚 Tài liệu tham khảo"):
        st.markdown("""
        **Guidelines:**
        
        1. **Surviving Sepsis Campaign 2021**
           - Evans L, et al. Crit Care Med. 2021;49(11):e1063-e1143.
        
        2. **Cardiogenic Shock:**
           - van Diepen S, et al. Contemporary Management of Cardiogenic Shock: A Scientific Statement From the American Heart Association. Circulation. 2017;136(16):e232-e268.
        
        3. **Hemorrhagic Shock:**
           - ATLS Guidelines (American College of Surgeons)
        
        4. **Anaphylaxis:**
           - Muraro A, et al. Anaphylaxis: guidelines from the European Academy of Allergy and Clinical Immunology. Allergy. 2014;69(8):1026-45.
        
        5. **Obstructive Shock:**
           - Konstantinides SV, et al. 2019 ESC Guidelines for the diagnosis and management of acute pulmonary embolism. Eur Heart J. 2020;41(4):543-603.
        """)
