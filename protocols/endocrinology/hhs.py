"""
Hyperglycemic Hyperosmolar State (HHS) Protocol
ADA 2023, Endocrine Society
Management of hyperglycemic hyperosmolar state
"""

import streamlit as st


def render():
    """Hyperglycemic Hyperosmolar State (HHS) Protocol"""
    st.subheader("🍭 Hội Chứng Tăng Đường Huyết Tăng Áp Lực Thẩm Thấu (HHS)")
    st.caption("ADA 2023, Endocrine Society - Hyperglycemic hyperosmolar state management")
    
    st.info("""
    **HHS (Hyperglycemic Hyperosmolar State):**
    - Tần suất: Ít hơn DKA nhưng tỷ lệ tử vong cao hơn (10-20%)
    - Thường gặp ở người cao tuổi, đái tháo đường type 2
    - Đặc điểm: Đường huyết rất cao, tăng áp lực thẩm thấu, không có nhiễm toan ceton
    
    **Chẩn đoán:**
    - Glucose >600 mg/dL
    - Osmolality >320 mOsm/kg
    - pH >7.30 (không có nhiễm toan)
    - Bicarbonate >18 mEq/L
    - Ketones âm tính hoặc nhẹ
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân Biệt HHS vs DKA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **HHS:**
        - Glucose: >600 mg/dL
        - Osmolality: >320
        - pH: >7.30
        - Bicarbonate: >18
        - Ketones: Âm tính/nhẹ
        - Tuổi: Thường >60
        - Type: Type 2
        """)
    
    with col2:
        st.warning("""
        **DKA:**
        - Glucose: >250 mg/dL
        - Osmolality: <320
        - pH: <7.30
        - Bicarbonate: <18
        - Ketones: Dương tính
        - Tuổi: Mọi lứa tuổi
        - Type: Type 1 hoặc 2
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều Trị")
    
    st.error("""
    **1. Fluid Resuscitation (Ưu tiên hàng đầu):**
    - **Loại:** 0.9% Normal Saline
    - **Liều:** 1-2 L trong giờ đầu, sau đó 200-500 mL/h
    - **Mục tiêu:** Bù 50% thiếu hụt trong 12 giờ đầu
    - **Theo dõi:** Dấu hiệu sống, BUN, Cr, osmolality
    
    **2. Insulin Therapy:**
    - **Liều:** 0.05-0.1 units/kg/h (thấp hơn DKA)
    - **Mục tiêu:** Giảm glucose 50-75 mg/dL/h
    - **Tránh:** Hạ quá nhanh (nguy cơ phù não)
    - **Khi glucose <300:** Thêm dextrose 5% + insulin
    
    **3. Electrolyte Management:**
    - **Kali:** Bổ sung ngay (thường thiếu)
    - **Phosphorus:** Bổ sung nếu <1.0 mg/dL
    - **Magnesium:** Bổ sung nếu <1.5 mg/dL
    
    **4. Thrombosis Prophylaxis:**
    - **Heparin:** 5000 units SC q8-12h
    - **Mục đích:** Phòng ngừa huyết khối (nguy cơ cao)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Tính Áp Lực Thẩm Thấu")
    
    st.info("""
    **Công thức:**
    - **Osmolality = 2 × Na + Glucose/18 + BUN/2.8**
    - **Bình thường:** 280-300 mOsm/kg
    - **HHS:** >320 mOsm/kg
    
    **Ví dụ:**
    - Na = 145 mEq/L
    - Glucose = 800 mg/dL
    - BUN = 40 mg/dL
    - Osmolality = 2×145 + 800/18 + 40/2.8 = 290 + 44 + 14 = 348 mOsm/kg
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Biến Chứng")
    
    st.error("""
    **1. Phù Não:**
    - Nguy cơ: Hạ glucose quá nhanh
    - Triệu chứng: Đau đầu, buồn nôn, rối loạn ý thức
    - Phòng ngừa: Hạ glucose từ từ (50-75 mg/dL/h)
    
    **2. Huyết Khối:**
    - Nguy cơ: Rất cao (tăng đông máu)
    - Phòng ngừa: Heparin prophylaxis
    
    **3. Suy Thận:**
    - Nguy cơ: Thiếu dịch nặng
    - Phòng ngừa: Truyền dịch đủ
    
    **4. Rối Loạn Điện Giải:**
    - Nguy cơ: Kali, phosphorus, magnesium
    - Phòng ngừa: Bổ sung sớm
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều Trị")
    
    checklist_items = [
        "✅ Chẩn đoán (Glucose >600, Osmolality >320, pH >7.30)",
        "✅ Truyền dịch ngay (0.9% NS 1-2 L giờ đầu)",
        "✅ Insulin 0.05-0.1 units/kg/h",
        "✅ Bổ sung kali ngay",
        "✅ Heparin prophylaxis",
        "✅ Theo dõi glucose mỗi 1-2 giờ",
        "✅ Theo dõi osmolality mỗi 4-6 giờ",
        "✅ Theo dõi điện giải mỗi 4-6 giờ",
        "✅ Điều trị nguyên nhân (nhiễm trùng, thuốc, v.v.)"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Nguy cơ cao hơn
        - Cẩn thận với truyền dịch (nguy cơ quá tải)
        - Theo dõi huyết động sát
        
        **Suy thận:**
        - Cẩn thận với truyền dịch
        - Theo dõi BUN, Cr sát
        - Có thể cần RRT
        """)
    
    with col2:
        st.markdown("""
        **Suy tim:**
        - Cẩn thận với truyền dịch
        - Có thể cần CVP monitoring
        - Cân nhắc giảm tốc độ truyền
        
        **Có thai:**
        - Hiếm gặp
        - Điều trị tương tự
        - Monitor thai nhi
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục Tiêu Điều Trị")
    
    st.success("""
    **Mục tiêu:**
    - ✅ Glucose: 200-300 mg/dL trong 24 giờ đầu
    - ✅ Osmolality: Giảm <10 mOsm/kg/h
    - ✅ Dấu hiệu sống ổn định
    - ✅ Điện giải bình thường
    - ✅ Không biến chứng
    
    **Theo dõi:**
    - Glucose mỗi 1-2 giờ
    - Osmolality mỗi 4-6 giờ
    - Điện giải mỗi 4-6 giờ
    - Dấu hiệu sống liên tục
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **ADA 2023 Guidelines**
       - American Diabetes Association
    
    2. **Endocrine Society Guidelines**
       - Kitabchi AE, et al. Diabetes Care. 2009
    
    3. **UpToDate:** Hyperglycemic hyperosmolar state
       - Last updated: 2024
    
    4. **Medscape:** HHS Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")

