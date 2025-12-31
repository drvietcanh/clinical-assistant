"""
Acute Pulmonary Edema Protocol
ESC Heart Failure Guidelines 2023, AHA/ACC 2022
Life-threatening condition requiring immediate treatment
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section
from components.evidence_badge import (
    render_evidence_badge,
    render_evidence_summary,
    Citation
)


def render():
    """Acute Pulmonary Edema Management Protocol"""
    st.subheader("🫁 Phù Phổi Cấp (Acute Pulmonary Edema)")
    st.caption("ESC Heart Failure Guidelines 2023, AHA/ACC 2022 - Life-threatening condition")
    
    # Evidence summary
    render_evidence_summary(
        last_reviewed="2024-04-01",
        last_updated="2024-04-01",
        version="2024",
        guideline_source="ESC 2023, AHA/ACC 2022"
    )
    
    st.error("""
    **⚠️ PHÙ PHỔI CẤP = CẤP CỨU Y KHOA**
    
    **Triệu chứng Điển Hình:**
    - Khó thở dữ dội, đột ngột
    - Ho khạc bọt hồng
    - Ngồi dậy để thở (orthopnea)
    - Vã mồ hôi, lo lắng
    - Tím tái, SpO₂ giảm
    - Ran ẩm 2 phế trường
    - Tăng huyết áp hoặc hạ huyết áp
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. OXYGEN & NON-INVASIVE VENTILATION**
        
        **Oxygen:**
        - **High-flow oxygen:** 10-15 L/min qua mask không thở lại
        - **Mục tiêu:** SpO₂ ≥95% (hoặc ≥90% nếu COPD)
        
        **CPAP/BiPAP (Ưu tiên):**
        - **CPAP:** 5-10 cmH₂O
        - **BiPAP:** IPAP 8-12, EPAP 4-6 cmH₂O
        - **Chỉ định:** Khó thở nặng, SpO₂ <90%
        - **Chống chỉ định:** 
          - Hạ huyết áp nặng (SBP <90)
          - Giảm ý thức
          - Nôn nhiều
          - Không hợp tác
        
        **Intubation:**
        - Nếu CPAP/BiPAP thất bại
        - Giảm ý thức
        - Suy hô hấp nặng
        """)
    
    with col2:
        st.warning("""
        **2. POSITIONING & MONITORING**
        
        **Position:**
        - **Ngồi dậy, chân thả xuống** (giảm tiền gánh)
        - Tránh nằm ngửa
        
        **Monitoring:**
        - **Continuous:** ECG, SpO₂, BP
        - **Frequent:** HR, RR, mental status
        - **Labs:** BNP/NT-proBNP, Troponin, BUN/Cr, Electrolytes
        
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị truyền dịch nếu cần
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Thuốc")
    
    # Assess blood pressure
    bp_status = st.radio(
        "**Tình trạng huyết áp:**",
        ["Tăng huyết áp (SBP >140)", "Bình thường (SBP 90-140)", "Hạ huyết áp (SBP <90)"],
        key="ape_bp_status"
    )
    
    st.markdown("---")
    
    if "Tăng huyết áp" in bp_status or "Bình thường" in bp_status:
        st.success("## 💉 ĐIỀU TRỊ CHUẨN - Huyết áp ổn định")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **1. NITROGLYCERIN (Ưu tiên)**
            
            **Sublingual:**
            - **0.4-0.8 mg** mỗi 5 phút (tối đa 3 lần)
            
            **IV (Nếu cần):**
            - **Khởi đầu:** 10-20 mcg/min
            - **Tăng dần:** 10-20 mcg/min mỗi 5-10 phút
            - **Mục tiêu:** Giảm SBP 10-15 mmHg
            - **Tối đa:** 200 mcg/min
            
            **Chống chỉ định:**
            - SBP <90 mmHg
            - Đã dùng PDE-5 inhibitors (sildenafil, tadalafil) trong 24-48h
            - Hẹp van động mạch chủ nặng
            - Tăng áp lực nội sọ
            """)
        
        with col2:
            st.markdown("""
            **2. FUROSEMIDE IV**
            
            **Liều:**
            - **Chưa dùng:** 40-80 mg IV bolus
            - **Đã dùng:** Liều gấp đôi liều PO hàng ngày
            - **Lặp lại:** Mỗi 6-12h nếu cần
            
            **Mục tiêu:**
            - Tiểu ≥100-150 mL/h trong 6h đầu
            - Giảm cân 0.5-1 kg/ngày
            - Giảm triệu chứng
            
            **Theo dõi:**
            - Điện giải (K, Mg, Na)
            - Creatinine
            - Cân bằng nước vào/ra
            """)
        
        st.info("""
        **3. MORPHINE (Nếu đau ngực/lo lắng nặng)**
        
        - **2-5 mg IV** (thận trọng)
        - **Chống chỉ định:** Giảm ý thức, suy hô hấp nặng
        - **Lưu ý:** Có thể gây suy hô hấp, dùng thận trọng
        """)
        
    else:  # Hypotension
        st.error("## 🚨 HẠ HUYẾT ÁP - Điều trị đặc biệt")
        
        st.warning("""
        **⚠️ KHÔNG dùng Nitroglycerin!**
        
        **1. TRUYỀN DỊCH (Thận trọng):**
        - **250-500 mL NS bolus** (nếu không có dấu hiệu quá tải)
        - Đánh giá đáp ứng
        - Tránh truyền quá nhiều (làm nặng phù phổi)
        
        **2. INOTROPES (Nếu cần):**
        - **Dopamine:** 2-10 mcg/kg/min
        - **Dobutamine:** 2-20 mcg/kg/min
        - **Norepinephrine:** 0.05-0.2 mcg/kg/min (nếu shock)
        
        **3. FUROSEMIDE:**
        - Liều thấp hơn: **20-40 mg IV**
        - Theo dõi sát huyết áp
        
        **4. XÉT NGHIỆM:**
        - ECG (loại trừ STEMI)
        - Echo (đánh giá chức năng tim)
        - Troponin (loại trừ ACS)
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân loại mức độ")
    
    severity = st.radio(
        "**Mức độ nghiêm trọng:**",
        ["Nhẹ (Mild)", "Trung bình (Moderate)", "Nặng (Severe)", "Sốc tim (Cardiogenic Shock)"],
        key="ape_severity"
    )
    
    st.markdown("---")
    
    if severity == "Nhẹ (Mild)":
        render_mild_ape()
    elif severity == "Trung bình (Moderate)":
        render_moderate_ape()
    elif severity == "Nặng (Severe)":
        render_severe_ape()
    else:
        render_cardiogenic_shock()
    
    st.markdown("---")
    
    st.markdown("### 🔍 Chẩn đoán Nguyên nhân")
    
    with st.expander("📋 Xem các nguyên nhân thường gặp", expanded=False):
        st.markdown("""
        **Nguyên nhân Tim mạch (Cardiogenic):**
        - Suy tim cấp (ADHF)
        - Nhồi máu cơ tim (STEMI/NSTEMI)
        - Rối loạn nhịp tim (AF, VT)
        - Bệnh van tim (hẹp/hở van 2 lá, hẹp van ĐMC)
        - Viêm cơ tim
        - Bóc tách động mạch chủ
        
        **Nguyên nhân Không do Tim (Non-cardiogenic):**
        - ARDS
        - Viêm phổi nặng
        - Hít sặc
        - Ngộ độc (CO, salicylates)
        - Độ cao
        - Dị ứng (anaphylaxis)
        - Tắc mạch phổi (PE)
        
        **Nguyên nhân Hỗn hợp:**
        - Suy thận cấp
        - Quá tải dịch
        - Thiếu máu nặng
        """)
    
    st.markdown("---")
    
    st.markdown("### 📈 Theo dõi & Đánh giá")
    
    st.info("""
    **Theo dõi trong 24-48h đầu:**
    
    **Lâm sàng:**
    - Triệu chứng khó thở (mỗi 1-2h)
    - Dấu hiệu sinh tồn (mỗi 1-2h)
    - Cân nặng (mỗi 12h)
    - Cân bằng nước vào/ra (mỗi 6-12h)
    - Ran phổi (mỗi 4-6h)
    
    **Cận lâm sàng:**
    - BNP/NT-proBNP (ban đầu và sau 24h)
    - Troponin (nếu nghi ngờ ACS)
    - Creatinine, Điện giải (mỗi 12-24h)
    - Chest X-ray (nếu cần)
    
    **Dấu hiệu cải thiện:**
    - ✅ Giảm khó thở
    - ✅ SpO₂ ≥95%
    - ✅ Giảm ran phổi
    - ✅ Tiểu tốt
    - ✅ Giảm cân
    
    **Dấu hiệu xấu đi:**
    - ⚠️ Khó thở tăng
    - ⚠️ SpO₂ giảm
    - ⚠️ Tăng creatinine
    - ⚠️ Hạ huyết áp
    - 🚨 Cần intubation
    """)
    
    st.markdown("---")
    
    st.markdown("### 👥 Điều chỉnh theo Đặc điểm Bệnh nhân")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Người cao tuổi:**
        - Thận trọng với nitroglycerin (hạ huyết áp)
        - Liều furosemide thấp hơn
        - Theo dõi sát chức năng thận
        
        **Suy thận:**
        - Furosemide liều cao hơn
        - Có thể cần lọc máu
        - Tránh quá tải dịch
        
        **COPD/Asthma:**
        - Thận trọng với CPAP/BiPAP
        - Mục tiêu SpO₂ 90-92%
        """)
    
    with col2:
        st.markdown("""
        **Có thai:**
        - Tránh ACE inhibitors, ARBs
        - Furosemide an toàn
        - Nitroglycerin thận trọng
        
        **Hẹp van ĐMC:**
        - Tránh nitroglycerin
        - Tránh giảm tiền gánh quá mức
        
        **Bệnh van tim:**
        - Cần đánh giá echo
        - Có thể cần phẫu thuật
        """)
    
    st.markdown("---")
    
    # References
    references = get_references("Acute Pulmonary Edema")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ESC Heart Failure Guidelines 2023** - European Society of Cardiology
        2. **AHA/ACC Heart Failure Guidelines 2022** - American Heart Association
        3. **UpToDate:** Acute Pulmonary Edema - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_mild_ape():
    """Mild Acute Pulmonary Edema"""
    st.success("## ⚠️ PHÙ PHỔI CẤP MỨC ĐỘ NHẸ")
    
    st.markdown("""
    **Đặc điểm:**
    - Khó thở nhẹ-trung bình
    - SpO₂ 90-95% với oxygen
    - Ran ẩm nhẹ 2 phế trường dưới
    - Huyết áp ổn định
    
    **Điều trị:**
    1. **Oxygen:** 2-4 L/min qua nasal cannula
    2. **Furosemide:** 40 mg IV bolus
    3. **Nitroglycerin:** 0.4 mg SL (nếu SBP >120)
    4. **Theo dõi:** Mỗi 2-4h
    
    **Tiên lượng:**
    - Thường đáp ứng tốt
    - Có thể xuất viện sau 24-48h nếu ổn định
    """)


def render_moderate_ape():
    """Moderate Acute Pulmonary Edema"""
    st.warning("## 🚨 PHÙ PHỔI CẤP MỨC ĐỘ TRUNG BÌNH")
    
    st.markdown("""
    **Đặc điểm:**
    - Khó thở trung bình-nặng
    - SpO₂ 85-90% với oxygen
    - Ran ẩm rõ 2 phế trường
    - Có thể có bọt hồng
    - Huyết áp ổn định hoặc tăng
    
    **Điều trị:**
    1. **CPAP/BiPAP:** 5-10 cmH₂O (ưu tiên)
    2. **Oxygen:** 10-15 L/min qua mask
    3. **Furosemide:** 80 mg IV bolus
    4. **Nitroglycerin IV:** 10-20 mcg/min, tăng dần
    5. **Theo dõi:** Mỗi 1-2h
    
    **Tiên lượng:**
    - Cần nhập viện
    - Thường đáp ứng trong 6-12h
    - Có thể cần ICU nếu không cải thiện
    """)


def render_severe_ape():
    """Severe Acute Pulmonary Edema"""
    st.error("## 🚨🚨 PHÙ PHỔI CẤP MỨC ĐỘ NẶNG - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Khó thở dữ dội
    - SpO₂ <85% dù oxygen cao
    - Ran ẩm toàn bộ 2 phế trường
    - Bọt hồng nhiều
    - Có thể tím tái
    - Huyết áp có thể tăng hoặc giảm
    
    **Điều trị ngay:**
    1. **CPAP/BiPAP:** 10-12 cmH₂O (hoặc intubation nếu thất bại)
    2. **Furosemide:** 80-120 mg IV bolus
    3. **Nitroglycerin IV:** 20-50 mcg/min, tăng nhanh
    4. **Morphine:** 2-5 mg IV (nếu đau/lo lắng)
    5. **Theo dõi:** Continuous monitoring
    
    **ICU Management:**
    - Arterial line (theo dõi BP liên tục)
    - Central line (nếu cần inotropes)
    - Echo (đánh giá chức năng tim)
    - Có thể cần IABP/ECMO nếu shock tim
    """)


def render_cardiogenic_shock():
    """Cardiogenic Shock"""
    st.error("## 🚨🚨🚨 SỐC TIM (CARDIOGENIC SHOCK) - ICU")
    
    st.markdown("""
    **Đặc điểm:**
    - Hạ huyết áp (SBP <90)
    - Dấu hiệu giảm tưới máu (lạnh, tím, thiểu niệu)
    - Phù phổi nặng
    - Có thể loạn nhịp tim
    
    **Điều trị ngay:**
    1. **Intubation:** Nếu suy hô hấp nặng
    2. **Inotropes:**
       - **Dobutamine:** 2-20 mcg/kg/min
       - **Norepinephrine:** 0.05-0.2 mcg/kg/min (nếu hạ HA nặng)
    3. **IABP:** Nếu có chỉ định
    4. **ECMO:** Nếu không đáp ứng
    
    **Nguyên nhân:**
    - STEMI (ưu tiên tái tưới máu)
    - Viêm cơ tim
    - Bệnh van tim nặng
    - Loạn nhịp tim nặng
    
    **Tiên lượng:**
    - Tử vong cao (30-50%)
    - Cần điều trị tích cực
    - Có thể cần phẫu thuật
    """)

