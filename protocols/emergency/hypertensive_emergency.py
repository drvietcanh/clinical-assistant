"""
Hypertensive Emergency/Urgency Protocol
AHA/ACC 2017, JNC 8
Acute severe hypertension with or without end-organ damage
"""

import streamlit as st


def render():
    """Hypertensive Emergency/Urgency Protocol"""
    st.subheader("⚡ Cơn Tăng Huyết áp Cấp cứu")
    st.caption("AHA/ACC 2017, JNC 8 - Hypertensive Emergency/Urgency Management")
    
    st.info("""
    **Phân biệt:**
    - **Cơn tăng huyết áp cấp cứu (Hypertensive Emergency):** 
      - BP rất cao (thường >180/120 mmHg)
      - **CÓ** tổn thương cơ quan đích mới/tiến triển
      - Cần hạ BP ngay (trong vài giờ)
    
    - **Cơn tăng huyết áp khẩn cấp (Hypertensive Urgency):**
      - BP rất cao (>180/120 mmHg)
      - **KHÔNG** có tổn thương cơ quan đích
      - Có thể hạ BP từ từ (trong 24-48 giờ)
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Chẩn đoán")
    
    with st.expander("🔍 Tiêu chuẩn chẩn đoán", expanded=True):
        st.markdown("""
        **Cơn tăng huyết áp cấp cứu khi có:**
        1. **Huyết áp:** Thường >180/120 mmHg (có thể thấp hơn nếu có tổn thương cơ quan)
        2. **Tổn thương cơ quan đích:**
           - **Não:** Encephalopathy, stroke, TIA
           - **Tim:** ACS, suy tim cấp, phù phổi
           - **Thận:** AKI, proteinuria nặng
           - **Mắt:** Xuất huyết võng mạc, phù gai thị
           - **Mạch máu:** Bóc tách động mạch chủ
        
        **Cơn tăng huyết áp khẩn cấp:**
        - BP >180/120 mmHg
        - **KHÔNG** có triệu chứng/tổn thương cơ quan
        """)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Mục tiêu Hạ Huyết áp")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **Cơn tăng huyết áp cấp cứu:**
        - **Mục tiêu:** Giảm 15-25% trong 1 giờ đầu
        - **Sau đó:** Giảm từ từ đến mục tiêu
        - **Tránh:** Hạ quá nhanh (nguy cơ thiếu máu cục bộ)
        
        **Ví dụ:**
        - BP 220/130 → Mục tiêu: 160-180/100-110 trong 1 giờ
        """)
    
    with col2:
        st.warning("""
        **Cơn tăng huyết áp khẩn cấp:**
        - **Mục tiêu:** Hạ từ từ trong 24-48 giờ
        - **Có thể:** Điều trị ngoại trú
        - **Thuốc:** Uống, không cần IV
        
        **Ví dụ:**
        - BP 200/120 → Mục tiêu: <160/100 trong 24-48 giờ
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Thuốc Điều trị")
    
    condition_type = st.radio(
        "**Loại tổn thương cơ quan:**",
        [
            "Không có tổn thương (Urgency)",
            "Tổn thương não (Encephalopathy/Stroke)",
            "Tổn thương tim (ACS/Suy tim)",
            "Bóc tách động mạch chủ",
            "Preeclampsia/Eclampsia",
            "Tổn thương thận (AKI)"
        ],
        key="hypertensive_condition"
    )
    
    st.markdown("---")
    
    if "Không có" in condition_type:
        render_urgency_protocol()
    elif "não" in condition_type.lower():
        render_neurologic_protocol()
    elif "tim" in condition_type.lower():
        render_cardiac_protocol()
    elif "Bóc tách" in condition_type or "aortic" in condition_type.lower():
        render_aortic_dissection_protocol()
    elif "Preeclampsia" in condition_type or "Eclampsia" in condition_type:
        render_preeclampsia_protocol()
    elif "thận" in condition_type.lower():
        render_renal_protocol()
    
    st.markdown("---")
    
    st.markdown("### 📊 Thuốc IV Thường Dùng")
    
    st.info("""
    **1. Labetalol (Alpha + Beta blocker):**
    - **Liều:** 20-80 mg IV bolus q10min
    - **Hoặc:** 0.5-2 mg/min truyền tĩnh mạch
    - **Ưu điểm:** Tác dụng nhanh, ít tác dụng phụ
    - **Chống chỉ định:** Suy tim nặng, block nhĩ thất, hen phế quản
    
    **2. Nicardipine (CCB):**
    - **Liều:** 5-15 mg/h truyền tĩnh mạch
    - **Ưu điểm:** Tác dụng nhanh, dễ điều chỉnh
    - **Chống chỉ định:** Suy tim nặng
    
    **3. Esmolol (Beta blocker):**
    - **Liều:** 500 mcg/kg bolus, sau đó 50-300 mcg/kg/min
    - **Ưu điểm:** Thời gian bán hủy ngắn
    - **Chống chỉ định:** Suy tim, block nhĩ thất, hen phế quản
    
    **4. Nitroprusside:**
    - **Liều:** 0.25-10 mcg/kg/min
    - **Ưu điểm:** Tác dụng rất nhanh
    - **Nhược điểm:** Cần monitor sát, nguy cơ thiếu máu cục bộ
    - **Chống chỉ định:** Suy thận nặng
    
    **5. Hydralazine:**
    - **Liều:** 10-20 mg IV q20-30min
    - **Ưu điểm:** An toàn cho thai kỳ
    - **Nhược điểm:** Tác dụng không dự đoán được
    
    **6. Enalaprilat (ACE inhibitor):**
    - **Liều:** 0.625-1.25 mg IV q6h
    - **Chống chỉ định:** Suy thận, hẹp động mạch thận, có thai
    """)
    
    st.markdown("---")
    
    st.markdown("### 📋 Checklist Điều trị")
    
    checklist_items = [
        "✅ Đánh giá tổn thương cơ quan đích",
        "✅ Đo BP cả 2 tay (nếu nghi bóc tách)",
        "✅ ECG (tìm dấu hiệu thiếu máu cục bộ)",
        "✅ Xét nghiệm: BUN, Cr, Troponin, BNP",
        "✅ Chọn thuốc phù hợp với tổn thương cơ quan",
        "✅ Hạ BP từ từ (15-25% trong 1 giờ đầu)",
        "✅ Monitor BP liên tục",
        "✅ Tránh hạ quá nhanh",
        "✅ Điều chỉnh liều theo đáp ứng"
    ]
    
    for item in checklist_items:
        st.markdown(f"- {item}")
    
    st.markdown("---")
    
    st.markdown("### ⚠️ Cảnh báo")
    
    st.error("""
    **Tránh hạ huyết áp quá nhanh:**
    - Nguy cơ thiếu máu cục bộ não, tim, thận
    - Đặc biệt nguy hiểm ở người cao tuổi
    - Có thể gây đột quỵ, nhồi máu cơ tim
    
    **Chống chỉ định một số thuốc:**
    - **ACE inhibitor:** Suy thận, hẹp động mạch thận, có thai
    - **Beta blocker:** Suy tim nặng, block nhĩ thất, hen phế quản
    - **Nitroprusside:** Suy thận nặng (nguy cơ nhiễm độc cyanide)
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Hạ BP từ từ hơn
        - Bắt đầu với liều thấp
        - Theo dõi sát triệu chứng
        
        **Có thai:**
        - Hydralazine, labetalol an toàn
        - Tránh ACE inhibitor, ARB
        - Magnesium sulfate nếu eclampsia
        """)
    
    with col2:
        st.markdown("""
        **Suy thận:**
        - Tránh ACE inhibitor nếu hẹp động mạch thận
        - Cẩn thận với nitroprusside
        - Theo dõi chức năng thận
        
        **Suy tim:**
        - Tránh beta blocker nếu suy tim nặng
        - Có thể dùng nitroprusside, nicardipine
        """)
    
    st.markdown("---")
    
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **AHA/ACC 2017 Hypertension Guidelines**
       - Whelton PK, et al. Hypertension. 2018
    
    2. **JNC 8 Guidelines 2014**
       - James PA, et al. JAMA. 2014
    
    3. **UpToDate:** Hypertensive emergencies
       - Last updated: 2024
    
    4. **Medscape:** Hypertensive Crisis Management
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_urgency_protocol():
    """Hypertensive urgency protocol"""
    st.success("## 🟢 Cơn Tăng Huyết áp Khẩn Cấp")
    
    st.markdown("""
    **Đặc điểm:**
    - BP >180/120 mmHg
    - Không có triệu chứng/tổn thương cơ quan
    
    **Điều trị:**
    1. **Có thể điều trị ngoại trú**
    2. **Thuốc uống:**
       - Amlodipine 5-10 mg PO
       - Hoặc: Captopril 25 mg PO
       - Hoặc: Clonidine 0.1-0.2 mg PO
    3. **Mục tiêu:** Hạ từ từ trong 24-48 giờ
    4. **Theo dõi:** Tái khám sau 24-48 giờ
    
    **Xuất viện:** Có thể nếu ổn định
    """)


def render_neurologic_protocol():
    """Neurologic emergency protocol"""
    st.error("## 🔴 Tổn Thương Não - Cấp cứu")
    
    st.markdown("""
    **Tình huống:**
    - Encephalopathy, stroke, TIA
    
    **Điều trị:**
    1. **Labetalol:** 20-80 mg IV bolus q10min
       - Hoặc: 0.5-2 mg/min truyền tĩnh mạch
    
    2. **Nicardipine:** 5-15 mg/h truyền tĩnh mạch
    
    3. **Mục tiêu BP:**
       - **Nếu stroke:** <185/110 (trước tPA)
       - **Sau tPA:** <180/105
       - **Nếu không tPA:** Có thể cho phép cao hơn
    
    4. **Tránh:** Hạ quá nhanh (nguy cơ thiếu máu cục bộ)
    
    5. **Theo dõi:** Thần kinh, BP liên tục
    """)


def render_cardiac_protocol():
    """Cardiac emergency protocol"""
    st.error("## 🔴 Tổn Thương Tim - Cấp cứu")
    
    st.markdown("""
    **Tình huống:**
    - ACS, suy tim cấp, phù phổi
    
    **Điều trị:**
    1. **Nếu ACS:**
       - Nitroglycerin: 10-20 mcg/min
       - Labetalol: 20-80 mg IV
       - Mục tiêu: <140/90
    
    2. **Nếu suy tim/phù phổi:**
       - Nitroprusside: 0.25-10 mcg/kg/min
       - Hoặc: Enalaprilat: 0.625-1.25 mg IV
       - Furosemide: 40-80 mg IV
    
    3. **Tránh:** Beta blocker nếu suy tim nặng
    
    4. **Theo dõi:** ECG, troponin, BNP
    """)


def render_aortic_dissection_protocol():
    """Aortic dissection protocol"""
    st.error("## 🔴 Bóc Tách Động Mạch Chủ - Cấp cứu Tối")
    
    st.markdown("""
    **Tình huống:**
    - Bóc tách động mạch chủ type A hoặc B
    
    **Điều trị ngay:**
    1. **Mục tiêu BP:** <120/80 mmHg (hoặc SBP <100-120)
    2. **Mục tiêu HR:** <60 bpm
    
    3. **Thuốc:**
       - **Esmolol:** 500 mcg/kg bolus, sau đó 50-300 mcg/kg/min
       - **Hoặc:** Labetalol: 20-80 mg IV bolus
       - **Thêm:** Nitroprusside: 0.25-10 mcg/kg/min nếu cần
    
    4. **Giảm đau:** Morphine IV
    
    5. **Phẫu thuật:** Type A cần phẫu thuật ngay
    
    6. **Theo dõi:** BP, HR liên tục, CT scan
    """)


def render_preeclampsia_protocol():
    """Preeclampsia/eclampsia protocol"""
    st.error("## 🔴 Preeclampsia/Eclampsia - Cấp cứu")
    
    st.markdown("""
    **Tình huống:**
    - Preeclampsia nặng, eclampsia
    
    **Điều trị:**
    1. **Hydralazine:** 5-10 mg IV q20min
       - Hoặc: 10-20 mg IM
    
    2. **Labetalol:** 20-40 mg IV q10min
    
    3. **Nifedipine:** 10-20 mg PO (nếu không có IV)
    
    4. **Nếu eclampsia:**
       - Magnesium sulfate: 4-6 g IV bolus
       - Sau đó: 1-2 g/h truyền tĩnh mạch
    
    5. **Mục tiêu BP:** <160/110
    
    6. **Theo dõi:** Thai nhi, sản phụ
    """)


def render_renal_protocol():
    """Renal emergency protocol"""
    st.error("## 🔴 Tổn Thương Thận - Cấp cứu")
    
    st.markdown("""
    **Tình huống:**
    - AKI, proteinuria nặng
    
    **Điều trị:**
    1. **Labetalol:** 20-80 mg IV bolus
       - Hoặc: 0.5-2 mg/min truyền tĩnh mạch
    
    2. **Nicardipine:** 5-15 mg/h truyền tĩnh mạch
    
    3. **Tránh:**
       - ACE inhibitor nếu hẹp động mạch thận
       - Nitroprusside nếu suy thận nặng
    
    4. **Mục tiêu BP:** <160/100
    
    5. **Theo dõi:** BUN, Cr, điện giải
    """)

