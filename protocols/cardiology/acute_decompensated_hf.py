"""
Acute Decompensated Heart Failure (ADHF) Protocol
ESC 2021, AHA/ACC 2022
Management of acute decompensated heart failure
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """Acute Decompensated Heart Failure Protocol"""
    st.subheader("💔 Acute Decompensated Heart Failure (ADHF)")
    st.caption("ESC 2021, AHA/ACC 2022 - Management of acute decompensated heart failure")
    
    st.error("""
    **🚨 ACUTE DECOMPENSATED HEART FAILURE = URGENT ASSESSMENT REQUIRED**
    
    **Định nghĩa:**
    - Suy tim cấp hoặc mất bù cấp
    - Triệu chứng và dấu hiệu suy tim mới hoặc nặng lên
    - Cần điều trị cấp cứu
    
    **Triệu chứng:**
    - Khó thở, orthopnea, PND
    - Phù, tăng cân
    - Mệt mỏi, giảm khả năng gắng sức
    - Ho, khò khè
    """)
    
    st.markdown("---")
    
    # ========== SECTION 1: CLASSIFICATION ==========
    st.markdown("### 📊 Phân loại Theo Hemodynamics")
    
    hf_profile = st.radio(
        "**Hồ sơ huyết động:**",
        ["Warm & Wet (Fluid Overload)", "Cold & Wet (Cardiogenic Shock)", "Warm & Dry (Compensated)", "Cold & Dry (Hypoperfusion)"],
        key="hf_profile"
    )
    
    st.markdown("---")
    
    if hf_profile == "Warm & Wet (Fluid Overload)":
        render_warm_wet_protocol()
    elif hf_profile == "Cold & Wet (Cardiogenic Shock)":
        render_cold_wet_protocol()
    elif hf_profile == "Warm & Dry (Compensated)":
        render_warm_dry_protocol()
    else:
        render_cold_dry_protocol()
    
    st.markdown("---")
    
    # ========== SECTION 2: INITIAL ASSESSMENT ==========
    st.markdown("### ⚡ Đánh giá Ban Đầu")
    
    with st.expander("🔍 Xem đánh giá ban đầu", expanded=True):
        st.markdown("""
        **1. ABC (Airway, Breathing, Circulation):**
        - **Airway:** Đảm bảo thông thoáng
        - **Breathing:** Đánh giá khó thở, SpO₂, công thở
        - **Circulation:** Đánh giá mạch, huyết áp, tưới máu
        
        **2. Dấu hiệu nguy hiểm:**
        - Khó thở nặng, không nói được câu
        - SpO₂ < 90% với O₂ hỗ trợ
        - Huyết áp tâm thu < 90 mmHg
        - Lú lẫn, kích động
        - Tím tái, vã mồ hôi
        
        **3. Xét nghiệm cần thiết:**
        - **BNP/NT-proBNP:** Chẩn đoán, tiên lượng
        - **Troponin:** Loại trừ ACS
        - **Chest X-ray:** Đánh giá phù phổi, tim to
        - **ECG:** Loại trừ ACS, rối loạn nhịp
        - **Echo:** Đánh giá chức năng tim, nguyên nhân
        - **ABG:** Nếu suy hô hấp nặng
        - **Labs:** CBC, BMP, LFTs, TSH
        """)
    
    st.markdown("---")
    
    # ========== SECTION 3: ACUTE PULMONARY EDEMA ==========
    st.markdown("### 🫁 Acute Pulmonary Edema")
    
    with st.expander("💨 Xem quy trình xử trí phù phổi cấp", expanded=False):
        st.markdown("""
        **1. Oxygen Therapy:**
        - **Nasal cannula:** 2-6 L/min
        - **Face mask:** 5-10 L/min
        - **CPAP/BiPAP:** Nếu SpO₂ < 90% với O₂ thông thường
          - CPAP: 5-10 cmH₂O
          - BiPAP: IPAP 10-15 cmH₂O, EPAP 5-8 cmH₂O
        
        **2. Nitroglycerin:**
        - **SL:** 0.4 mg q5 phút (max 3 lần)
        - **IV:** 10-20 mcg/min, tăng 10 mcg/min q5 phút
        - **Mục tiêu:** Giảm SBP 10-15 mmHg
        - **Chống chỉ định:** SBP < 90 mmHg, RV infarction
        
        **3. Furosemide:**
        - **IV:** 20-40 mg (tăng nếu đã dùng trước)
        - **Lặp lại:** q6-12h nếu cần
        - **Theo dõi:** Điện giải, chức năng thận
        
        **4. Morphine (Cân nhắc):**
        - **IV:** 2-5 mg
        - **Lưu ý:** Có thể gây ức chế hô hấp
        - **Chống chỉ định:** COPD, suy hô hấp nặng
        
        **5. Intubation:**
        - Nếu SpO₂ < 90% với CPAP/BiPAP
        - Mệt mỏi cơ hô hấp
        - Lú lẫn, hôn mê
        """)
    
    st.markdown("---")
    
    # ========== SECTION 4: CARDIOGENIC SHOCK ==========
    st.markdown("### ⚡ Cardiogenic Shock")
    
    with st.expander("🚨 Xem quy trình xử trí sốc tim", expanded=False):
        st.markdown("""
        **Định nghĩa:**
        - SBP < 90 mmHg hoặc MAP < 60 mmHg
        - Dấu hiệu hypoperfusion (lạnh, tím, thiểu niệu, lú lẫn)
        - CI < 2.2 L/min/m² hoặc PCWP > 15 mmHg
        
        **Quy trình:**
        
        **1. Fluid Challenge:**
        - 250-500 mL NS trong 10-15 phút
        - Chỉ nếu không có phù phổi
        - Theo dõi sát đáp ứng
        
        **2. Inotropes:**
        - **Dobutamine:** 2-20 mcg/kg/min
          - Ưu tiên nếu SBP ≥ 90 mmHg
        - **Milrinone:** 0.375-0.75 mcg/kg/min
          - Cân nhắc nếu suy thận
        - **Epinephrine:** 0.05-0.5 mcg/kg/min
          - Nếu shock nặng
        
        **3. Vasopressors:**
        - **Norepinephrine:** 0.05-0.5 mcg/kg/min
          - Ưu tiên nếu SBP < 90 mmHg
        - **Dopamine:** 2-20 mcg/kg/min
          - Ít dùng hơn
        
        **4. Mechanical Support:**
        - **IABP:** Intra-aortic balloon pump
        - **Impella:** Percutaneous LVAD
        - **ECMO:** Extracorporeal membrane oxygenation
        - **VAD:** Ventricular assist device
        
        **5. Revascularization:**
        - **PCI:** Nếu STEMI/NSTEMI
        - **CABG:** Nếu cần
        """)
    
    st.markdown("---")
    
    # ========== SECTION 5: DIURETICS ==========
    st.markdown("### 💊 Diuretics")
    
    with st.expander("💉 Xem liều thuốc lợi tiểu", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Furosemide:**
            - **IV:** 20-40 mg (tăng nếu đã dùng trước)
            - **Lặp lại:** q6-12h nếu cần
            - **Continuous infusion:** 5-40 mg/h
            - **Theo dõi:** Điện giải, chức năng thận
            
            **Bumetanide:**
            - **IV:** 0.5-1 mg
            - **Lặp lại:** q6-12h nếu cần
            - **Tương đương:** 1 mg ≈ 40 mg furosemide
            
            **Torsemide:**
            - **IV:** 10-20 mg
            - **Lặp lại:** q12-24h nếu cần
            """)
        
        with col2:
            st.markdown("""
            **Thiazides (Kết hợp):**
            - **Metolazone:** 2.5-10 mg PO
            - **Hydrochlorothiazide:** 25-50 mg PO
            - **Chỉ định:** Kháng furosemide
            
            **Spironolactone:**
            - **PO:** 12.5-50 mg/ngày
            - **Chỉ định:** HFrEF, giảm K+
            - **Theo dõi:** K+, chức năng thận
            """)
    
    st.markdown("---")
    
    # ========== SECTION 6: VASODILATORS ==========
    st.markdown("### 💉 Vasodilators")
    
    with st.expander("📋 Xem liều thuốc giãn mạch", expanded=False):
        st.markdown("""
        **Nitroglycerin:**
        - **SL:** 0.4 mg q5 phút (max 3 lần)
        - **IV:** 10-20 mcg/min, tăng 10 mcg/min q5 phút
        - **Mục tiêu:** Giảm SBP 10-15 mmHg
        - **Max:** 200 mcg/min
        - **Chống chỉ định:** SBP < 90 mmHg, RV infarction
        
        **Nesiritide:**
        - **IV:** 2 mcg/kg bolus, sau đó 0.01 mcg/kg/min
        - **Chỉ định:** ADHF với dyspnea
        - **Theo dõi:** Huyết áp
        
        **Nitroprusside:**
        - **IV:** 0.3-0.5 mcg/kg/min, tăng 0.5 mcg/kg/min q5 phút
        - **Mục tiêu:** SBP 90-100 mmHg
        - **Max:** 10 mcg/kg/min
        - **Theo dõi:** Thiocyanate nếu dùng > 48h
        """)
    
    st.markdown("---")
    
    # ========== SECTION 7: MONITORING ==========
    st.markdown("### 📈 Monitoring")
    
    st.markdown("""
    **Theo dõi sát:**
    - **Huyết động:** BP, HR, MAP, CVP (nếu có)
    - **Hô hấp:** Tần số thở, SpO₂, công thở
    - **Lượng nước tiểu:** q1-2h (mục tiêu > 0.5 mL/kg/h)
    - **Cân nặng:** Hàng ngày
    - **Labs:** BNP/NT-proBNP, troponin, điện giải, chức năng thận
    - **Chest X-ray:** Hàng ngày hoặc khi có thay đổi
    - **Echo:** Theo dõi chức năng tim
    
    **Mục tiêu:**
    - **SBP:** 90-140 mmHg
    - **SpO₂:** ≥ 90%
    - **Lượng nước tiểu:** > 0.5 mL/kg/h
    - **BNP/NT-proBNP:** Giảm > 30%
    - **Cân nặng:** Giảm 1-2 kg/ngày
    """)
    
    st.markdown("---")
    
    # ========== SECTION 8: SPECIAL POPULATIONS ==========
    st.markdown("### 👥 Special Populations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Ngưỡng triệu chứng thấp hơn
        - Tỷ lệ biến chứng cao hơn
        - Cần điều chỉnh liều thuốc
        - Cân nhắc chất lượng cuộc sống
        
        **Suy thận:**
        - Giảm liều diuretics
        - Theo dõi sát chức năng thận
        - Cân nhắc RRT nếu cần
        """)
    
    with col2:
        st.markdown("""
        **Phụ nữ có thai:**
        - Tránh ACEi/ARB, spironolactone
        - Furosemide an toàn
        - Nitroglycerin an toàn
        - Cần tư vấn sản khoa
        
        **Trẻ em:**
        - Liều dựa trên cân nặng
        - Nguyên nhân khác (bẩm sinh)
        - Cần tư vấn nhi khoa
        """)
    
    st.markdown("---")
    
    # ========== SECTION 9: REFERENCES ==========
    render_references_section(get_references("acute_decompensated_hf"))
    
    st.markdown("---")
    
    # Footer
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_warm_wet_protocol():
    """Warm & Wet (Fluid Overload) Protocol"""
    st.success("## ✅ WARM & WET (FLUID OVERLOAD) PROTOCOL")
    
    st.markdown("""
    **Đặc điểm:**
    - SBP ≥ 90 mmHg
    - Dấu hiệu fluid overload (phù, phù phổi)
    - Tưới máu đủ
    
    **Quy trình:**
    
    1. **Oxygen Therapy:**
       - Nasal cannula 2-6 L/min
       - CPAP/BiPAP nếu SpO₂ < 90%
    
    2. **Diuretics:**
       - **Furosemide:** 20-40 mg IV (tăng nếu đã dùng trước)
       - **Lặp lại:** q6-12h nếu cần
       - **Mục tiêu:** Lượng nước tiểu > 0.5 mL/kg/h
    
    3. **Vasodilators:**
       - **Nitroglycerin:** SL 0.4 mg hoặc IV 10-20 mcg/min
       - **Mục tiêu:** Giảm SBP 10-15 mmHg
    
    4. **Theo dõi:**
       - Lượng nước tiểu q1-2h
       - Điện giải q6-12h
       - Cân nặng hàng ngày
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Đây là profile phổ biến nhất
    - Diuretics là điều trị chính
    - Vasodilators giúp giảm preload
    - Theo dõi sát để tránh hypovolemia
    """)


def render_cold_wet_protocol():
    """Cold & Wet (Cardiogenic Shock) Protocol"""
    st.error("## 🚨 COLD & WET (CARDIOGENIC SHOCK) PROTOCOL - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - SBP < 90 mmHg hoặc MAP < 60 mmHg
    - Dấu hiệu hypoperfusion
    - Dấu hiệu fluid overload
    
    **Quy trình:**
    
    1. **Oxygen Therapy:**
       - High-flow O₂ hoặc CPAP/BiPAP
       - Cân nhắc intubation
    
    2. **Fluid Challenge:**
       - 250-500 mL NS trong 10-15 phút
       - Chỉ nếu không có phù phổi nặng
       - Theo dõi sát đáp ứng
    
    3. **Inotropes:**
       - **Dobutamine:** 2-20 mcg/kg/min (nếu SBP ≥ 90 mmHg)
       - **Milrinone:** 0.375-0.75 mcg/kg/min
       - **Epinephrine:** 0.05-0.5 mcg/kg/min (nếu shock nặng)
    
    4. **Vasopressors:**
       - **Norepinephrine:** 0.05-0.5 mcg/kg/min (nếu SBP < 90 mmHg)
       - **Mục tiêu:** MAP ≥ 65 mmHg
    
    5. **Diuretics:**
       - **Furosemide:** 20-40 mg IV
       - Cẩn thận với hypovolemia
    
    6. **Mechanical Support:**
       - Cân nhắc IABP, Impella, ECMO
       - Tư vấn tim mạch can thiệp
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Đây là profile nguy hiểm nhất
    - Cần ICU monitoring
    - Cân bằng giữa inotropes và diuretics
    - Cân nhắc mechanical support sớm
    """)


def render_warm_dry_protocol():
    """Warm & Dry (Compensated) Protocol"""
    st.info("## ℹ️ WARM & DRY (COMPENSATED) PROTOCOL")
    
    st.markdown("""
    **Đặc điểm:**
    - SBP ≥ 90 mmHg
    - Không có dấu hiệu fluid overload
    - Tưới máu đủ
    
    **Quy trình:**
    
    1. **Đánh giá:**
       - Xác định nguyên nhân mất bù
       - Điều trị nguyên nhân
    
    2. **Điều chỉnh thuốc:**
       - Tối ưu hóa ACEi/ARB, beta-blockers
       - Điều chỉnh liều diuretics
       - Bổ sung spironolactone nếu cần
    
    3. **Theo dõi:**
       - Theo dõi sát để phát hiện mất bù
       - Giáo dục bệnh nhân
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Đây là profile ổn định nhất
    - Tập trung vào điều trị lâu dài
    - Phòng ngừa mất bù
    """)


def render_cold_dry_protocol():
    """Cold & Dry (Hypoperfusion) Protocol"""
    st.warning("## ⚠️ COLD & DRY (HYPOPERFUSION) PROTOCOL")
    
    st.markdown("""
    **Đặc điểm:**
    - SBP < 90 mmHg hoặc MAP < 60 mmHg
    - Dấu hiệu hypoperfusion
    - Không có dấu hiệu fluid overload
    
    **Quy trình:**
    
    1. **Fluid Challenge:**
       - 250-500 mL NS trong 10-15 phút
       - Lặp lại nếu đáp ứng
       - Mục tiêu: MAP ≥ 65 mmHg
    
    2. **Inotropes:**
       - **Dobutamine:** 2-20 mcg/kg/min
       - **Milrinone:** 0.375-0.75 mcg/kg/min
    
    3. **Vasopressors:**
       - **Norepinephrine:** 0.05-0.5 mcg/kg/min (nếu vẫn shock sau fluid)
       - **Mục tiêu:** MAP ≥ 65 mmHg
    
    4. **Theo dõi:**
       - Đánh giá đáp ứng với fluid
       - Tránh fluid overload
    """)
    
    st.info("""
    **💡 Mẹo quan trọng:**
    - Có thể do hypovolemia hoặc cardiogenic shock
    - Fluid challenge giúp phân biệt
    - Theo dõi sát để tránh fluid overload
    """)

