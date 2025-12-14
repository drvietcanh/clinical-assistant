"""
Ventilator Weaning Protocol
SCCM Guidelines, Evidence-Based Weaning
Mechanical Ventilation Liberation
"""

import streamlit as st


def render():
    """Ventilator Weaning Protocol"""
    st.subheader("🫁 Ventilator Weaning Protocol")
    st.caption("SCCM Guidelines - Mechanical Ventilation Liberation")
    
    st.info("""
    **Ventilator Weaning là quá trình giảm dần hỗ trợ thở máy và cuối cùng là cai máy thở.**
    - **Mục tiêu:** Giảm thời gian thở máy, giảm complications
    - **Timing:** Bắt đầu sớm khi có thể
    - **Success rate:** 70-80% với protocol chuẩn
    """)
    
    st.markdown("---")
    
    # Readiness assessment
    st.markdown("### 1️⃣ Readiness Assessment - Đánh giá Sẵn Sàng Cai Máy")
    
    st.markdown("#### 📋 Checklist - Sẵn Sàng Cai Máy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Nguyên nhân thở máy đã được giải quyết:**")
        cause_resolved = st.checkbox("✅ Nguyên nhân đã cải thiện", key="wean_cause")
        
        st.markdown("**Oxygenation:**")
        pao2_fio2 = st.number_input(
            "**PaO₂/FiO₂ (mmHg):**",
            min_value=50.0,
            max_value=500.0,
            value=200.0,
            step=10.0,
            key="wean_pao2_fio2"
        )
        fio2_ok = st.checkbox("**FiO₂ ≤0.5**", key="wean_fio2")
        peep_ok = st.checkbox("**PEEP ≤8 cmH₂O**", key="wean_peep")
        
        st.markdown("**Ventilation:**")
        pplat_ok = st.checkbox("**Pplat ≤30 cmH₂O**", key="wean_pplat")
        ph_ok = st.checkbox("**pH ≥7.25**", key="wean_ph")
        paco2_ok = st.checkbox("**PaCO₂ acceptable**", key="wean_paco2")
    
    with col2:
        st.markdown("**Hemodynamics:**")
        hemodynamic_stable = st.checkbox("**Hemodynamically stable**", key="wean_hemo")
        no_vasopressors = st.checkbox("**Không cần vasopressors hoặc liều thấp**", key="wean_vaso")
        
        st.markdown("**Neurologic:**")
        awake = st.checkbox("**Awake, có thể follow commands**", key="wean_awake")
        no_seizures = st.checkbox("**Không có seizures**", key="wean_seizure")
        
        st.markdown("**Other:**")
        cough_adequate = st.checkbox("**Cough adequate**", key="wean_cough")
        secretions_ok = st.checkbox("**Secretions manageable**", key="wean_secretions")
        no_fever = st.checkbox("**Không sốt cao**", key="wean_fever")
    
    # Calculate readiness score
    readiness_criteria = [
        cause_resolved,
        pao2_fio2 >= 150 and fio2_ok and peep_ok,
        pplat_ok and ph_ok and paco2_ok,
        hemodynamic_stable and no_vasopressors,
        awake and no_seizures,
        cough_adequate and secretions_ok,
        no_fever
    ]
    
    readiness_score = sum(readiness_criteria)
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if readiness_score >= 6:
            st.success("### ✅ **SẴN SÀNG CAI MÁY**")
            st.success(f"Đạt {readiness_score}/7 tiêu chuẩn - Có thể bắt đầu weaning protocol")
            ready = True
        elif readiness_score >= 4:
            st.warning("### ⚠️ **GẦN SẴN SÀNG**")
            st.warning(f"Đạt {readiness_score}/7 tiêu chuẩn - Cần cải thiện thêm trước khi wean")
            ready = False
        else:
            st.error("### ❌ **CHƯA SẴN SÀNG**")
            st.error(f"Chỉ đạt {readiness_score}/7 tiêu chuẩn - Cần điều trị thêm")
            ready = False
    
    with col2:
        st.metric("**Readiness Score:**", f"{readiness_score}/7")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Weaning Methods")
    
    method = st.radio(
        "**Phương pháp weaning:**",
        ["Spontaneous Breathing Trial (SBT)", "Pressure Support Weaning", "T-piece Trial", "SIMV Weaning"],
        key="wean_method"
    )
    
    st.markdown("---")
    
    if method == "Spontaneous Breathing Trial (SBT)":
        render_sbt()
    elif method == "Pressure Support Weaning":
        render_pressure_support()
    elif method == "T-piece Trial":
        render_tpiece()
    else:
        render_simv()
    
    st.markdown("---")
    st.markdown("### 3️⃣ Extubation Criteria")
    
    st.info("""
    **Sau khi SBT thành công, đánh giá extubation:**
    
    **Airway Protection:**
    - Gag reflex present
    - Cough adequate (peak cough flow >60 L/min)
    - Secretions manageable
    - No excessive secretions
    
    **Mental Status:**
    - Awake, alert
    - Can follow commands
    - No delirium
    
    **Other:**
    - No stridor risk (cuff leak test nếu cần)
    - No planned surgery trong 24h
    - Reintubation risk assessment
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Failed Weaning - Xử Trí")
    
    st.warning("""
    **Nếu SBT thất bại:**
    
    **Nguyên nhân thường gặp:**
    1. **Respiratory muscle weakness:**
       - ICU-acquired weakness
       - Malnutrition
       - Electrolyte imbalance (K⁺, PO₄⁻, Mg²⁺)
    
    2. **Cardiac dysfunction:**
       - Heart failure
       - Ischemia
    
    3. **Metabolic:**
       - Acidosis
       - Hypercapnia
    
    4. **Psychological:**
       - Anxiety
       - Delirium
    
    **Xử trí:**
    - Điều trị nguyên nhân
    - Nghỉ ngơi 24-48h
    - Physical therapy
    - Nutrition support
    - Reassess sau 24-48h
    """)
    
    st.markdown("---")
    st.markdown("### 📚 References")
    
    st.markdown("""
    1. **SCCM Guidelines** - Liberation from Mechanical Ventilation 2017
    2. **Spontaneous Breathing Trial** - Esteban et al. 1995
    3. **UpToDate:** Liberation from Mechanical Ventilation - Last updated 2024
    """)
    
    st.markdown("---")
    st.caption("⚠️ Protocol chỉ mang tính tham khảo. Điều chỉnh theo tình huống lâm sàng cụ thể.")


def render_sbt():
    """Spontaneous Breathing Trial Protocol"""
    st.success("## ✅ Spontaneous Breathing Trial (SBT) - Phương Pháp Ưu Tiên")
    
    st.info("""
    **SBT là phương pháp weaning ưu tiên (Evidence-based):**
    - **Duration:** 30-120 phút
    - **Mode:** Pressure support 5-7 cmH₂O hoặc T-piece
    - **Frequency:** Mỗi ngày (nếu đủ tiêu chuẩn)
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📋 SBT Protocol")
        
        sbt_mode = st.selectbox(
            "**SBT Mode:**",
            ["Pressure Support 5-7 cmH₂O", "T-piece", "CPAP 5 cmH₂O"],
            key="sbt_mode"
        )
        
        sbt_duration = st.number_input(
            "**Duration (phút):**",
            min_value=30,
            max_value=120,
            value=30,
            step=15,
            key="sbt_duration"
        )
        
        st.markdown("**Pre-SBT:**")
        st.checkbox("✅ Đảm bảo readiness criteria", key="sbt_pre1")
        st.checkbox("✅ Suction ETT và oral", key="sbt_pre2")
        st.checkbox("✅ Pre-oxygenate với FiO₂ 1.0", key="sbt_pre3")
    
    with col2:
        st.markdown("#### 📊 SBT Monitoring")
        
        st.markdown("**Monitor mỗi 5-15 phút:**")
        st.checkbox("✅ SpO₂", key="sbt_mon1")
        st.checkbox("✅ HR, BP", key="sbt_mon2")
        st.checkbox("✅ RR", key="sbt_mon3")
        st.checkbox("✅ Work of breathing", key="sbt_mon4")
        st.checkbox("✅ ABG (nếu cần)", key="sbt_mon5")
        
        st.markdown("---")
        st.markdown("#### 🚨 SBT Failure Criteria")
        
        st.error("""
        **Dừng SBT nếu có:**
        - SpO₂ <88-90%
        - HR >140 hoặc <50
        - SBP >180 hoặc <90
        - RR >35 hoặc <8
        - Agitation, diaphoresis
        - Signs of respiratory distress
        """)
    
    st.markdown("---")
    st.markdown("#### ✅ SBT Success")
    
    st.success("""
    **Nếu SBT thành công (30-120 phút):**
    1. Đánh giá extubation criteria
    2. Nếu đủ tiêu chuẩn → Extubate
    3. Nếu chưa đủ → Tiếp tục thở máy, reassess ngày mai
    """)


def render_pressure_support():
    """Pressure Support Weaning"""
    st.info("## 💨 Pressure Support Weaning")
    
    st.markdown("""
    **Protocol:**
    1. Bắt đầu với PS 10-15 cmH₂O
    2. Giảm dần PS mỗi 2-4h: 15 → 12 → 10 → 8 → 5 cmH₂O
    3. Khi PS ≤5 cmH₂O: Chuyển sang SBT
    4. Nếu thất bại: Quay lại PS cao hơn 5 cmH₂O
    """)


def render_tpiece():
    """T-piece Trial"""
    st.info("## 🔄 T-piece Trial")
    
    st.markdown("""
    **Protocol:**
    1. Disconnect từ ventilator
    2. T-piece với O₂ flow 10-15 L/min
    3. Duration: 30-120 phút
    4. Monitor sát (tương tự SBT)
    5. Nếu thành công → Extubate
    """)


def render_simv():
    """SIMV Weaning"""
    st.warning("## ⚠️ SIMV Weaning (Không Khuyến cáo)")
    
    st.markdown("""
    **SIMV weaning KHÔNG được khuyến cáo:**
    - Tăng work of breathing
    - Kéo dài thời gian weaning
    - Không cải thiện kết quả
    
    **Nên dùng:** SBT hoặc Pressure Support weaning
    """)

