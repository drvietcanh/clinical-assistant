"""
NSTEMI (Non-ST-Elevation Myocardial Infarction) Protocol
ESC/ACC Guidelines 2024, AHA/ACC 2023
Acute coronary syndrome requiring risk stratification
"""

import streamlit as st
from protocols.references_config import get_references
from components.references import render_references_section


def render():
    """NSTEMI Management Protocol"""
    st.subheader("💔 NSTEMI (Non-ST-Elevation Myocardial Infarction)")
    st.caption("ESC/ACC Guidelines 2024, AHA/ACC 2023 - Acute coronary syndrome")
    
    st.error("""
    **⚠️ NSTEMI = CẤP CỨU Y KHOA - PHÂN TẦNG NGUY CƠ**
    
    **Tiêu chuẩn Chẩn đoán:**
    - **ECG:** ST chênh xuống, T đảo ngược, hoặc bình thường
    - **Troponin:** Tăng (≥99th percentile)
    - **Triệu chứng:** Đau ngực, khó thở
    
    **Khác với STEMI:**
    - Không có ST chênh lên
    - Cần phân tầng nguy cơ trước
    - Chiến lược điều trị khác
    """)
    
    st.markdown("---")
    
    st.markdown("### ⚡ Xử trí ngay lập tức (ABC)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **1. AIRWAY & BREATHING**
        
        **Oxygen:**
        - **Chỉ nếu:** SpO₂ <90% hoặc suy hô hấp
        - **Liều:** 2-4 L/min qua nasal cannula
        - **Lưu ý:** Tránh oxygen không cần thiết
        
        **2. CIRCULATION**
        
        **Monitoring:**
        - **Continuous ECG**
        - **Arterial line** (nếu shock)
        - **BP, HR:** Mỗi 15-30 phút
        
        **Truyền dịch:**
        - **NS:** 250-500 mL bolus (nếu hạ HA)
        - **Thận trọng:** Tránh quá tải
        """)
    
    with col2:
        st.warning("""
        **3. VENOUS ACCESS**
        
        - **2 đường tĩnh mạch lớn**
        - Chuẩn bị thuốc
        
        **4. LABS NGAY:**
        - **Troponin:** (quan trọng)
        - **CK-MB:** (nếu có)
        - **CBC, BMP, Coagulation**
        - **Lipid panel:** (nếu có thể)
        - **BNP/NT-proBNP:** (đánh giá suy tim)
        """)
    
    st.markdown("---")
    
    st.markdown("### 💊 Điều trị Thuốc")
    
    st.success("""
    **1. ASPIRIN (Ngay lập tức)**
    
    - **Liều:** 325 mg PO (nhai) hoặc 300 mg IV
    - **Chống chỉ định:** Dị ứng nặng, xuất huyết hoạt động
    
    **2. P2Y12 INHIBITOR (Ngay lập tức)**
    
    **Ticagrelor (Ưu tiên):**
    - **Liều:** 180 mg PO (loading dose)
    - **Duy trì:** 90 mg PO bid
    
    **Hoặc Clopidogrel:**
    - **Liều:** 600 mg PO (loading dose)
    - **Duy trì:** 75 mg PO qd
    
    **Hoặc Prasugrel:**
    - **Liều:** 60 mg PO (loading dose)
    - **Duy trì:** 10 mg PO qd
    - **Chống chỉ định:** Tiền sử TIA/Stroke, tuổi ≥75
    
    **3. ATORVASTATIN (Ngay lập tức)**
    
    - **Liều:** 80 mg PO
    - **Mục tiêu:** Giảm LDL, ổn định mảng xơ vữa
    """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Phân tầng Nguy cơ (Risk Stratification)")
    
    st.markdown("#### GRACE Score Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input("**Tuổi:**", min_value=0, max_value=120, value=60, step=1)
        heart_rate = st.number_input("**Nhịp tim (bpm):**", min_value=0, max_value=250, value=80, step=1)
        systolic_bp = st.number_input("**Huyết áp tâm thu (mmHg):**", min_value=0, max_value=300, value=120, step=1)
        creatinine = st.number_input("**Creatinine (mg/dL):**", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    
    with col2:
        has_st_elevation = st.checkbox("ST chênh lên", key="grace_st")
        has_cardiac_arrest = st.checkbox("Ngừng tim", key="grace_arrest")
        has_killip_class_2_4 = st.checkbox("Killip Class 2-4", key="grace_killip")
        has_elevated_cardiac_enzymes = st.checkbox("Troponin tăng", key="grace_troponin")
    
    st.markdown("---")
    
    # Simplified GRACE score calculation (approximate)
    if st.button("Tính GRACE Score"):
        # This is a simplified version - actual GRACE score is more complex
        grace_score = 0
        grace_score += age
        if heart_rate > 100:
            grace_score += 20
        if systolic_bp < 100:
            grace_score += 30
        if creatinine > 1.5:
            grace_score += 20
        if has_st_elevation:
            grace_score += 30
        if has_cardiac_arrest:
            grace_score += 40
        if has_killip_class_2_4:
            grace_score += 40
        if has_elevated_cardiac_enzymes:
            grace_score += 15
        
        st.markdown(f"### GRACE Score: **{grace_score}**")
        
        if grace_score < 100:
            st.success("✅ **Nguy cơ THẤP** - Có thể điều trị bảo tồn")
        elif grace_score < 140:
            st.warning("⚠️ **Nguy cơ TRUNG BÌNH** - Cần đánh giá thêm")
        else:
            st.error("🚨 **Nguy cơ CAO** - Cần can thiệp sớm")
    
    st.markdown("---")
    
    st.markdown("### 🔄 Chiến lược Điều trị")
    
    treatment_strategy = st.radio(
        "**Chiến lược Điều trị:**",
        [
            "Invasive Strategy (Early PCI) - Nguy cơ cao",
            "Conservative Strategy (Medical Management) - Nguy cơ thấp",
            "Selective Invasive - Nguy cơ trung bình"
        ],
        key="nstemi_strategy"
    )
    
    st.markdown("---")
    
    if "Invasive" in treatment_strategy and "Early" in treatment_strategy:
        render_early_invasive()
    elif "Conservative" in treatment_strategy:
        render_conservative()
    else:
        render_selective_invasive()
    
    st.markdown("---")
    
    st.markdown("### 💉 Điều trị Hỗ trợ")
    
    st.info("""
    **1. Anticoagulation:**
    
    **Heparin (Nếu PCI):**
    - **Liều:** 70-100 units/kg IV bolus
    - **Duy trì:** 12-15 units/kg/h
    - **Mục tiêu:** aPTT 50-70s
    
    **Hoặc Enoxaparin:**
    - **Liều:** 1 mg/kg SC q12h
    - **Hoặc:** 0.75 mg/kg SC q12h (nếu CrCl <30)
    
    **Hoặc Fondaparinux:**
    - **Liều:** 2.5 mg SC qd
    
    **2. Beta-blockers:**
    
    - **Metoprolol:** 25-50 mg PO bid (nếu không chống chỉ định)
    - **Chống chỉ định:** 
      - Suy tim nặng
      - AV block
      - Shock
      - COPD nặng
    
    **3. ACE Inhibitors:**
    
    - **Lisinopril:** 5-10 mg PO qd (nếu không chống chỉ định)
    - **Chống chỉ định:**
      - Hạ huyết áp
      - Suy thận nặng
      - Tăng K
    
    **4. Monitoring:**
    - ECG liên tục
    - Troponin (mỗi 6-12h)
    - CK-MB (nếu có)
    - Chức năng thận
    """)
    
    st.markdown("---")
    
    # References
    references = get_references("NSTEMI")
    if references:
        render_references_section(references)
    else:
        st.markdown("### 📚 References")
        st.markdown("""
        1. **ESC/ACC Guidelines 2024** - European Society of Cardiology
        2. **AHA/ACC Guidelines 2023** - American Heart Association
        3. **UpToDate:** NSTEMI Management - Last updated 2024
        """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể và guidelines mới nhất.")


def render_early_invasive():
    """Early Invasive Strategy"""
    st.error("## 🚨 EARLY INVASIVE STRATEGY - Nguy cơ cao")
    
    st.markdown("""
    **Chỉ định:**
    - GRACE Score >140
    - Troponin tăng
    - ST chênh xuống mới
    - Đau ngực tái phát
    - Rối loạn huyết động
    - Rối loạn nhịp tim
    
    **Thời gian:**
    - **<2 giờ:** Nếu shock, đau ngực tái phát
    - **<24 giờ:** Nếu ổn định
    
    **Trước PCI:**
    - Aspirin 325 mg
    - P2Y12 inhibitor (loading dose)
    - Atorvastatin 80 mg
    - Anticoagulation
    
    **Trong PCI:**
    - Stent (Drug-eluting stent ưu tiên)
    - GP IIb/IIIa inhibitor (nếu cần)
    
    **Sau PCI:**
    - DAPT (Dual Antiplatelet Therapy):
      - Aspirin 81-100 mg PO qd
      - P2Y12 inhibitor (duy trì)
    - Atorvastatin 80 mg PO qd
    - Beta-blocker (nếu không chống chỉ định)
    - ACE inhibitor (nếu không chống chỉ định)
    """)


def render_conservative():
    """Conservative Strategy"""
    st.success("## ✅ CONSERVATIVE STRATEGY - Nguy cơ thấp")
    
    st.markdown("""
    **Chỉ định:**
    - GRACE Score <100
    - Troponin bình thường hoặc tăng nhẹ
    - Không có ST chênh xuống
    - Không có triệu chứng tái phát
    - Ổn định huyết động
    
    **Điều trị:**
    - Aspirin 81-100 mg PO qd
    - P2Y12 inhibitor (duy trì)
    - Atorvastatin 80 mg PO qd
    - Beta-blocker (nếu không chống chỉ định)
    - ACE inhibitor (nếu không chống chỉ định)
    - Anticoagulation (nếu cần)
    
    **Theo dõi:**
    - ECG mỗi 6-12h
    - Troponin mỗi 6-12h
    - Triệu chứng
    
    **Chỉ định PCI sau:**
    - Nếu triệu chứng tái phát
    - Nếu troponin tăng
    - Nếu stress test dương tính
    """)


def render_selective_invasive():
    """Selective Invasive Strategy"""
    st.warning("## ⚠️ SELECTIVE INVASIVE STRATEGY - Nguy cơ trung bình")
    
    st.markdown("""
    **Chỉ định:**
    - GRACE Score 100-140
    - Troponin tăng nhẹ-trung bình
    - Có thể có ST chênh xuống
    - Ổn định huyết động
    
    **Điều trị:**
    - Aspirin 81-100 mg PO qd
    - P2Y12 inhibitor (duy trì)
    - Atorvastatin 80 mg PO qd
    - Beta-blocker (nếu không chống chỉ định)
    - ACE inhibitor (nếu không chống chỉ định)
    - Anticoagulation
    
    **Đánh giá:**
    - Stress test (nếu ổn định)
    - CT coronary angiography (nếu có thể)
    - Echocardiography
    
    **Chỉ định PCI:**
    - Nếu stress test dương tính
    - Nếu CT CTA có tổn thương nặng
    - Nếu triệu chứng tái phát
    - Thời gian: 24-72 giờ
    """)

