"""
Electrolyte Emergency Protocols
Hyperkalemia & Hyponatremia Correction
"""

import streamlit as st


def render():
    """Electrolyte Emergency Protocols"""
    st.subheader("⚡ Electrolyte Emergency Protocols")
    st.caption("Hyperkalemia, Hyponatremia, Hypomagnesemia, Hypophosphatemia, Hypocalcemia")
    
    st.markdown("---")
    
    # Electrolyte selection
    electrolyte = st.radio(
        "**Chọn tình trạng:**",
        [
            "Hyperkalemia (Tăng kali máu)",
            "Hyponatremia (Hạ natri máu)",
            "Hypomagnesemia (Hạ magie máu)",
            "Hypophosphatemia (Hạ phospho máu)",
            "Hypocalcemia (Hạ canxi máu)"
        ],
        key="electrolyte_type"
    )
    
    st.markdown("---")
    
    if "Hyperkalemia" in electrolyte:
        render_hyperkalemia()
    elif "Hyponatremia" in electrolyte:
        render_hyponatremia()
    elif "Hypomagnesemia" in electrolyte or "magie" in electrolyte.lower():
        render_hypomagnesemia()
    elif "Hypophosphatemia" in electrolyte or "phospho" in electrolyte.lower():
        render_hypophosphatemia()
    elif "Hypocalcemia" in electrolyte or "canxi" in electrolyte.lower():
        render_hypocalcemia()


def render_hyperkalemia():
    """Hyperkalemia Emergency Protocol"""
    
    st.error("## 🚨 HYPERKALEMIA EMERGENCY PROTOCOL")
    
    st.markdown("### 1️⃣ ECG Changes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **ECG Progression:**
        
        **K⁺ 5.5-6.5:**
        - Tall peaked T waves
        - QT shortening
        
        **K⁺ 6.5-7.5:**
        - PR prolongation
        - QRS widening
        - P waves flatten/disappear
        
        **K⁺ >7.5:**
        - Sine wave pattern
        - Ventricular fibrillation
        - Asystole
        
        **⚠️ Nếu có ECG changes:** Treat as EMERGENCY
        """)
    
    with col2:
        st.warning("""
        **Severity:**
        
        **Mild (5.5-6.0):**
        - Often asymptomatic
        - Monitor, treat cause
        
        **Moderate (6.0-7.0):**
        - May have ECG changes
        - Requires treatment
        
        **Severe (>7.0):**
        - Dangerous ECG changes
        - EMERGENCY!
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Treatment Ladder")
    
    st.info("""
    **Phase 1: Membrane Stabilization (< 5 minutes)**
    
    **✅ Calcium:**
    - **Calcium gluconate 10%:** 1g IV (10ml) trong 2-3 phút
    - Hoặc **Calcium chloride 10%:** 0.5-1g IV (5-10ml)
    - **Effect:** Immediate (within 1-3 min)
    - **Duration:** 30-60 min
    - **⚠️ Không giảm K⁺, chỉ bảo vệ tim!**
    """)
    
    st.markdown("---")
    st.success("""
    **Phase 2: Shift K⁺ into Cells (5-15 minutes)**
    
    **A. Insulin + Dextrose:**
    - **Regular insulin:** 10 U IV
    - **D50:** 50ml IV (hoặc 1 amp)
    - **Effect:** Onset 15-30 min
    - **Duration:** 4-6h
    - **Check glucose:** Mỗi 1h × 4h (risk hypoglycemia!)
    
    **B. Albuterol:**
    - **10-20mg nebulized**
    - **Effect:** Onset 15-30 min
    - **Duration:** 2-3h
    - **Additive với insulin**
    
    **C. NaHCO₃ (nếu acidotic):**
    - **50-100 mEq IV** trong 5-10 min
    - **Chỉ nếu pH <7.2**
    - **Effect:** Onset 15-30 min
    - **⚠️ Không dùng nếu volume overload**
    """)
    
    st.markdown("---")
    st.warning("""
    **Phase 3: Remove K⁺ from Body (30 min - hours)**
    
    **A. Loop Diuretics:**
    - **Furosemide 40-80mg IV**
    - **Chỉ nếu:** Normal/high UO, volume overload
    - **Effect:** Onset 30 min
    - **⚠️ Không dùng nếu oliguric/anuric**
    
    **B. Potassium Binders:**
    - **Sodium Polystyrene Sulfonate (Kayexalate):**
      * 15-30g PO/PR q4-6h
      * Effect: Onset 1-2h
      * Duration: 4-6h
    - **Patiromer (Veltassa):** 8.4-25.2g PO q24h
    - **Sodium Zirconium Cyclosilicate (Lokelma):** 10g TID
    
    **C. Hemodialysis:**
    - **Indication:**
      * K⁺ >6.5 không đáp ứng
      * Renal failure
      * Oliguric/anuric
      * Severe ECG changes
    - **Effect:** Immediate removal
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Protocol by K⁺ Level")
    
    tab1, tab2, tab3 = st.tabs(["K⁺ 5.5-6.0", "K⁺ 6.0-7.0", "K⁺ >7.0"])
    
    with tab1:
        st.markdown("#### ⚠️ Mild Hyperkalemia (5.5-6.0)")
        
        st.info("""
        **Actions:**
        1. ✅ Check ECG (nếu có changes → treat as moderate)
        2. ✅ Identify cause
        3. ✅ Discontinue K⁺ supplements, K⁺-sparing diuretics
        4. ✅ Monitor K⁺ mỗi 4-6h
        5. ✅ Consider:
           * Loop diuretic
           * K⁺ binder (Kayexalate)
        
        **Usually:** Non-urgent, treat cause
        """)
    
    with tab2:
        st.markdown("#### 🚨 Moderate Hyperkalemia (6.0-7.0)")
        
        st.error("""
        **Immediate Actions:**
        1. ✅ **ECG ngay** - Nếu có changes → Treat as severe
        2. ✅ **IV access**
        3. ✅ **Monitor ECG continuously**
        
        **Treatment:**
        1. **Calcium:** 1g IV (if ECG changes)
        2. **Insulin + D50:** 10U + 50ml
        3. **Albuterol:** 10-20mg nebulized
        4. **Furosemide:** 40-80mg IV (nếu có UO)
        5. **K⁺ binder:** Kayexalate 15-30g
        
        **Monitor:**
        - K⁺ mỗi 2-4h
        - ECG mỗi 1-2h
        - Glucose mỗi 1h (nếu dùng insulin)
        """)
    
    with tab3:
        st.markdown("#### 🚨🚨 Severe Hyperkalemia (>7.0)")
        
        st.error("""
        **CODE HYPERKALEMIA - EMERGENCY!**
        
        **Immediate (< 5 min):**
        1. ✅ **ECG ngay** - Monitor continuously
        2. ✅ **IV access** (2 lines)
        3. ✅ **Calcium:** 1g IV trong 2-3 phút
        4. ✅ **Repeat calcium** nếu ECG không cải thiện
        
        **Within 15 min:**
        1. ✅ **Insulin + D50:** 10U + 50ml
        2. ✅ **Albuterol:** 20mg nebulized
        3. ✅ **NaHCO₃:** 50-100 mEq (nếu acidotic)
        
        **Within 30-60 min:**
        1. ✅ **Furosemide:** 80-120mg IV (nếu có UO)
        2. ✅ **Kayexalate:** 30g PO/PR
        3. ✅ **Nephrology consult** - Prepare for HD
        
        **Indications for HD:**
        - K⁺ >7.0 với ECG changes
        - Oliguric/anuric
        - Renal failure
        - Không đáp ứng treatment
        
        **Monitor:**
        - K⁺ mỗi 1-2h
        - ECG continuous
        - Glucose mỗi 1h × 4h
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Common Causes")
    
    st.warning("""
    **Pseudohyperkalemia:**
    - Hemolysis
    - Thrombocytosis (>1M)
    - Leukocytosis (>100k)
    - Recheck nếu nghi ngờ
    
    **True Hyperkalemia:**
    - **Renal failure:** AKI, CKD
    - **Medications:**
      * K⁺-sparing diuretics (Spironolactone, Amiloride)
      * ACE-I, ARBs
      * NSAIDs
      * Cyclosporine, Tacrolimus
    - **Acidosis:** Metabolic acidosis
    - **Tissue breakdown:** Rhabdo, tumor lysis
    - **Adrenal insufficiency**
    - **K⁺ supplements**
    """)


def render_hyponatremia():
    """Hyponatremia Correction Protocol"""
    
    st.error("## 🚨 HYPONATREMIA CORRECTION PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Severity:**
        
        **Mild (130-135):**
        - Often asymptomatic
        - Mild nausea, fatigue
        
        **Moderate (120-130):**
        - Headache, nausea
        - Confusion
        - Weakness
        
        **Severe (<120):**
        - Seizures
        - Coma
        - Brain herniation
        - DEATH
        """)
    
    with col2:
        st.error("""
        **⚠️ Osmotic Demyelination (ODS):**
        
        **Risk nếu:**
        - Correct quá nhanh (>10-12 mEq/L trong 24h)
        - Chronic hyponatremia
        - Alcoholism, malnutrition
        
        **Symptoms (1-3 days sau correction):**
        - Dysarthria
        - Dysphagia
        - Paraparesis/quadriparesis
        - Locked-in syndrome
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Correction Rate Limits")
    
    st.error("""
    **⚠️ CRITICAL: Rate limits để tránh ODS!**
    
    **Acute hyponatremia (<48h):**
    - **Max correction:** 8-10 mEq/L trong 24h
    - Có thể nhanh hơn nếu symptomatic
    
    **Chronic hyponatremia (>48h):**
    - **Max correction:** 6-8 mEq/L trong 24h
    - **Max correction:** 10-12 mEq/L trong 48h
    - **⚠️ Không quá 18 mEq/L trong 48h**
    
    **Severe symptomatic (<120 với seizures):**
    - Correct 4-6 mEq/L trong vài giờ đầu
    - Sau đó giảm tốc độ
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Calculation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_na = st.number_input(
            "Na⁺ hiện tại (mEq/L)",
            min_value=100.0,
            max_value=135.0,
            value=125.0,
            step=1.0,
            format="%.0f",
            key="na_current"
        )
        
        target_na = st.number_input(
            "Mục tiêu Na⁺ (mEq/L)",
            min_value=120.0,
            max_value=140.0,
            value=130.0,
            step=1.0,
            format="%.0f",
            key="na_target"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            format="%.0f",
            key="na_weight"
        )
        
        duration = st.number_input(
            "Thời gian (giờ)",
            min_value=6.0,
            max_value=48.0,
            value=24.0,
            step=1.0,
            format="%.0f",
            key="na_duration"
        )
    
    with col2:
        # Calculate
        na_deficit = target_na - current_na
        tbw = weight * 0.6  # Total body water (60% of weight for men)
        na_needed = na_deficit * tbw
        
        # Rate check
        hourly_rate = na_deficit / duration if duration > 0 else 0
        daily_rate = hourly_rate * 24
        
        st.markdown("### 📊 Kết Quả:")
        
        st.metric("Na⁺ deficit", f"{na_deficit:.0f} mEq/L")
        st.metric("TBW", f"{tbw:.1f} L")
        st.metric("Na⁺ needed", f"{na_needed:.0f} mEq")
        st.metric("Hourly rate", f"{hourly_rate:.2f} mEq/L/h")
        st.metric("Daily rate", f"{daily_rate:.1f} mEq/L/24h")
        
        # Warning
        if daily_rate > 12:
            st.error("⚠️ QUÁ NHANH! Risk ODS. Giảm tốc độ!")
        elif daily_rate > 8:
            st.warning("⚠️ Gần giới hạn. Theo dõi sát!")
        else:
            st.success("✅ Tốc độ an toàn")
    
    st.markdown("---")
    st.markdown("### 4️⃣ Treatment")
    
    tab1, tab2, tab3 = st.tabs(["Acute", "Chronic", "Severe Symptomatic"])
    
    with tab1:
        st.markdown("#### ⚡ Acute Hyponatremia (<48h)")
        
        st.success("""
        **If symptomatic (seizures, coma):**
        1. ✅ **3% Saline:** 100-150ml IV trong 10-20 min
        2. ✅ **Check Na⁺ sau 1h**
        3. ✅ **Repeat nếu cần** (mục tiêu: +4-6 mEq/L)
        4. ✅ **Sau đó:** Slow down rate
        
        **If mild/moderate:**
        1. ✅ **Identify cause**
        2. ✅ **3% Saline:** 0.5-2 ml/kg/h
        3. ✅ **Monitor Na⁺ mỗi 2-4h**
        4. ✅ **Adjust rate** để không vượt 8 mEq/L/24h
        """)
    
    with tab2:
        st.markdown("#### 📅 Chronic Hyponatremia (>48h)")
        
        st.error("""
        **⚠️ CỰC KỲ THẬN TRỌNG - High risk ODS!**
        
        **If severe symptomatic:**
        1. ✅ **3% Saline:** 100ml IV trong 1h
        2. ✅ **Check Na⁺ sau 1h**
        3. ✅ **Goal:** +4-6 mEq/L trong vài giờ đầu
        4. ✅ **Then:** SLOW DOWN!
        5. ✅ **Max:** 10-12 mEq/L trong 48h
        
        **If moderate:**
        1. ✅ **Identify cause**
        2. ✅ **Fluid restriction:** 800-1200ml/day
        3. ✅ **Consider:**
           * Demeclocycline (SIADH)
           * Vaptans (tolvaptan) - cautious
           * Loop diuretic + NaCl tablets
        4. ✅ **3% Saline:** Rất thận trọng, slow rate
        5. ✅ **Monitor Na⁺ mỗi 4-6h**
        """)
    
    with tab3:
        st.markdown("#### 🚨 Severe Symptomatic (Seizures, Coma)")
        
        st.error("""
        **EMERGENCY!**
        
        **Immediate:**
        1. ✅ **3% Saline:** 100-150ml IV trong 10-20 min
        2. ✅ **Repeat nếu cần:** Mỗi 1h
        3. ✅ **Goal:** +4-6 mEq/L trong vài giờ đầu
        4. ✅ **Check Na⁺ mỗi 1h × 4h**
        
        **After initial correction:**
        1. ✅ **SLOW DOWN!** - Risk ODS!
        2. ✅ **Max:** 8-10 mEq/L trong 24h
        3. ✅ **If over-correcting:** Give free water (D5W) hoặc DDAVP
        4. ✅ **Monitor:** Neurologic status, Na⁺ trends
        
        **⚠️ If correcting too fast:**
        - Stop hypertonic saline
        - Give D5W 100-200ml/h
        - Hoặc DDAVP 1-2 mcg IV q6-8h
        - Monitor Na⁺ mỗi 2h
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ 3% Saline Calculation")
    
    st.info("""
    **3% Saline = 513 mEq/L Na⁺**
    
    **Formula:**
    - Na⁺ needed (mEq) = (Target - Current) × TBW
    - Volume 3% saline (L) = Na⁺ needed / 513
    - Rate (ml/h) = Volume (L) / Hours × 1000
    
    **Example:**
    - Current Na: 120, Target: 130, Weight: 70kg
    - TBW: 42L
    - Na needed: (130-120) × 42 = 420 mEq
    - Volume: 420 / 513 = 0.82 L
    - Rate over 24h: 0.82 / 24 × 1000 = 34 ml/h
    
    **⚠️ Monitor Na⁺ mỗi 2-4h và điều chỉnh!**
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Common Causes")
    
    st.warning("""
    **Hypovolemic:**
    - Diarrhea, vomiting
    - Diuretics
    - Burns
    - Treatment: NS hoặc LR
    
    **Hypervolemic:**
    - Heart failure
    - Cirrhosis
    - Nephrotic syndrome
    - Treatment: Fluid restriction + diuretics
    
    **Euvolemic:**
    - SIADH
    - Hypothyroidism
    - Adrenal insufficiency
    - Treatment: Fluid restriction, cause-specific
    """)


def render_hypomagnesemia():
    """Hypomagnesemia Correction Protocol"""
    
    st.warning("## ⚠️ HYPOMAGNESEMIA CORRECTION PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Severity:**
        
        **Mild (1.5-1.7 mg/dL):**
        - Often asymptomatic
        - Mild weakness
        
        **Moderate (1.0-1.5 mg/dL):**
        - Muscle cramps
        - Weakness
        - Tremor
        
        **Severe (<1.0 mg/dL):**
        - Seizures
        - Tetany
        - Arrhythmias
        - Cardiac arrhythmias
        """)
    
    with col2:
        st.error("""
        **⚠️ Important:**
        
        **Hypomagnesemia thường kèm:**
        - Hypokalemia (khó điều chỉnh nếu không bổ sung Mg)
        - Hypocalcemia (khó điều chỉnh nếu không bổ sung Mg)
        
        **⚠️ Luôn kiểm tra:**
        - K⁺, Ca²⁺, PO₄³⁻
        - Điều chỉnh đồng thời nếu cần
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Calculation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_mg = st.number_input(
            "Mg²⁺ hiện tại (mg/dL)",
            min_value=0.5,
            max_value=2.0,
            value=1.2,
            step=0.1,
            format="%.1f",
            key="mg_current"
        )
        
        target_mg = st.number_input(
            "Mục tiêu Mg²⁺ (mg/dL)",
            min_value=1.5,
            max_value=2.5,
            value=2.0,
            step=0.1,
            format="%.1f",
            key="mg_target"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            format="%.0f",
            key="mg_weight"
        )
        
        severity = st.radio(
            "Mức độ:",
            ["Nhẹ (asymptomatic)", "Trung bình (symptomatic)", "Nặng (seizures, arrhythmias)"],
            key="mg_severity"
        )
    
    with col2:
        # Calculate
        mg_deficit = target_mg - current_mg
        # Total body Mg: ~0.3-0.4 mEq/kg (or ~24 mEq total)
        # 1g MgSO4 = 8.12 mEq Mg
        # Deficit (mEq) = (Target - Current) × Weight × 0.3
        mg_deficit_meq = mg_deficit * weight * 0.3  # Approximate
        
        # MgSO4 needed
        # 1g MgSO4 = 8.12 mEq Mg
        mgso4_needed = mg_deficit_meq / 8.12
        
        st.markdown("### 📊 Kết Quả:")
        
        st.metric("Mg²⁺ deficit", f"{mg_deficit:.2f} mg/dL")
        st.metric("Mg²⁺ deficit", f"{mg_deficit_meq:.1f} mEq")
        st.metric("MgSO4 needed", f"{mgso4_needed:.1f} g")
        
        # Recommendations
        if "Nặng" in severity:
            st.error("""
            **🚨 SEVERE - IV Replacement:**
            - Loading: 2-4g MgSO4 IV trong 10-15 phút
            - Maintenance: 1-2g/h × 4-6h
            - Sau đó: 0.5-1g/h × 12-24h
            """)
        elif "Trung bình" in severity:
            st.warning("""
            **⚠️ MODERATE:**
            - IV: 1-2g MgSO4 IV trong 1h, lặp lại q6-8h
            - Hoặc PO: 400-800mg q8-12h
            """)
        else:
            st.success("""
            **✅ MILD:**
            - PO: 400-600mg q8-12h
            - Hoặc IV: 1g MgSO4 IV trong 1h
            """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Treatment")
    
    tab1, tab2 = st.tabs(["IV Replacement", "Oral Replacement"])
    
    with tab1:
        st.markdown("#### 💉 IV Magnesium Replacement")
        
        st.error("""
        **Severe (<1.0 mg/dL hoặc symptomatic):**
        
        **Loading dose:**
        - **MgSO4 2-4g IV** trong 10-15 phút
        - Hoặc 25-50 mg/kg (1.8-3.6 mEq/kg)
        - **⚠️ Monitor:** BP, HR, ECG (risk bradycardia, hypotension)
        
        **Maintenance:**
        - **1-2g/h × 4-6h** (8-16 mEq/h)
        - Sau đó: **0.5-1g/h × 12-24h**
        - Tổng: 6-12g trong 24h đầu
        
        **Monitoring:**
        - Mg²⁺ mỗi 4-6h
        - Deep tendon reflexes (mất phản xạ = quá liều)
        - ECG, BP, HR
        - Urine output (risk renal failure nếu quá liều)
        """)
        
        st.warning("""
        **Moderate (1.0-1.5 mg/dL):**
        
        **Option 1:**
        - **1-2g MgSO4 IV** trong 1h
        - Lặp lại q6-8h × 2-3 lần
        
        **Option 2:**
        - **1g MgSO4 IV** trong 1h q8h × 24h
        """)
        
        st.info("""
        **⚠️ Precautions:**
        - **Renal failure:** Giảm liều 50-75%
        - **Monitor reflexes:** Mất phản xạ = quá liều
        - **Antidote:** Calcium gluconate 1g IV (nếu quá liều)
        """)
    
    with tab2:
        st.markdown("#### 💊 Oral Magnesium Replacement")
        
        st.success("""
        **Mild to moderate (≥1.0 mg/dL, asymptomatic/mild symptoms):**
        
        **Options:**
        
        **1. Magnesium Oxide:**
        - 400-800mg PO q8-12h
        - Tác dụng phụ: Tiêu chảy
        
        **2. Magnesium Citrate:**
        - 200-400mg PO q8-12h
        - Dễ hấp thu hơn
        
        **3. Magnesium Gluconate:**
        - 500-1000mg PO q12h
        
        **Duration:**
        - 1-2 tuần
        - Kiểm tra Mg²⁺ sau 1 tuần
        """)
        
        st.warning("""
        **⚠️ Lưu ý:**
        - Tiêu chảy có thể hạn chế hấp thu
        - Cần thời gian để bù đủ
        - Không dùng nếu severe hoặc symptomatic
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Common Causes")
    
    st.warning("""
    **GI Losses:**
    - Diarrhea, vomiting
    - Malabsorption
    - Fistulas
    
    **Renal Losses:**
    - Diuretics (loop, thiazide)
    - Alcoholism
    - Diabetes (osmotic diuresis)
    - Hypercalcemia
    - Medications (aminoglycosides, amphotericin)
    
    **Redistribution:**
    - Hungry bone syndrome
    - Acute pancreatitis
    - Transfusion (citrate chelation)
    
    **Inadequate Intake:**
    - Malnutrition
    - TPN without Mg
    - Alcoholism
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Hypomagnesemia + Hypokalemia:**
    - Khó điều chỉnh K⁺ nếu không bổ sung Mg
    - Bổ sung Mg trước hoặc đồng thời với K⁺
    
    **Hypomagnesemia + Hypocalcemia:**
    - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
    - Bổ sung Mg trước hoặc đồng thời với Ca²⁺
    
    **Renal Failure:**
    - Giảm liều 50-75%
    - Theo dõi sát (risk hypermagnesemia)
    - Tránh dùng nếu CrCl <30
    
    **Pregnancy:**
    - MgSO4 an toàn (dùng trong preeclampsia)
    - Liều tương tự
    """)


def render_hypophosphatemia():
    """Hypophosphatemia Management Protocol"""
    
    st.warning("## ⚠️ HYPOPHOSPHATEMIA MANAGEMENT PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Severity:**
        
        **Mild (2.0-2.5 mg/dL):**
        - Often asymptomatic
        - Mild weakness
        
        **Moderate (1.0-2.0 mg/dL):**
        - Weakness, fatigue
        - Muscle pain
        - Irritability
        
        **Severe (<1.0 mg/dL):**
        - Rhabdomyolysis
        - Respiratory failure
        - Cardiac dysfunction
        - Hemolysis
        - Seizures, coma
        """)
    
    with col2:
        st.error("""
        **⚠️ Critical Levels:**
        
        **<0.5 mg/dL:**
        - Life-threatening
        - Respiratory failure
        - Cardiac arrest
        - Hemolysis
        
        **⚠️ Risk Groups:**
        - Alcoholism
        - Refeeding syndrome
        - DKA recovery
        - TPN without phosphate
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Calculation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        current_phos = st.number_input(
            "PO₄³⁻ hiện tại (mg/dL)",
            min_value=0.5,
            max_value=3.0,
            value=1.5,
            step=0.1,
            format="%.1f",
            key="phos_current"
        )
        
        target_phos = st.number_input(
            "Mục tiêu PO₄³⁻ (mg/dL)",
            min_value=2.0,
            max_value=4.5,
            value=3.0,
            step=0.1,
            format="%.1f",
            key="phos_target"
        )
        
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=30.0,
            max_value=150.0,
            value=70.0,
            step=1.0,
            format="%.0f",
            key="phos_weight"
        )
        
        severity = st.radio(
            "Mức độ:",
            ["Nhẹ (asymptomatic)", "Trung bình (symptomatic)", "Nặng (<1.0 mg/dL)"],
            key="phos_severity"
        )
    
    with col2:
        # Calculate
        phos_deficit = target_phos - current_phos
        # Phosphate deficit (mmol) = (Target - Current) × Weight × 0.3
        # 1 mmol PO4 = 31 mg PO4
        # 1 mmol KPO4 = 1 mmol PO4 + 1 mmol K
        phos_deficit_mmol = phos_deficit * weight * 0.3 / 31  # Approximate
        
        # Potassium phosphate: 1 mmol = 31 mg PO4
        # Sodium phosphate: 1 mmol = 31 mg PO4
        # Need: phos_deficit_mmol mmol
        
        st.markdown("### 📊 Kết Quả:")
        
        st.metric("PO₄³⁻ deficit", f"{phos_deficit:.2f} mg/dL")
        st.metric("PO₄³⁻ deficit", f"{phos_deficit_mmol:.1f} mmol")
        
        # Recommendations
        if "Nặng" in severity or current_phos < 1.0:
            st.error("""
            **🚨 SEVERE - IV Replacement:**
            - 0.08-0.16 mmol/kg IV trong 2-6h
            - Hoặc 15-30 mmol IV trong 2-6h
            - Lặp lại q6-12h nếu cần
            """)
        elif "Trung bình" in severity:
            st.warning("""
            **⚠️ MODERATE:**
            - IV: 0.08 mmol/kg IV trong 2-4h
            - Hoặc 15-20 mmol IV trong 2-4h
            - Hoặc PO: 250-500mg q6-8h
            """)
        else:
            st.success("""
            **✅ MILD:**
            - PO: 250-500mg q8-12h
            - Hoặc IV: 10-15 mmol trong 2-4h
            """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Treatment")
    
    tab1, tab2 = st.tabs(["IV Replacement", "Oral Replacement"])
    
    with tab1:
        st.markdown("#### 💉 IV Phosphate Replacement")
        
        st.error("""
        **Severe (<1.0 mg/dL hoặc symptomatic):**
        
        **Dosing:**
        - **0.08-0.16 mmol/kg IV** trong 2-6h
        - Hoặc **15-30 mmol IV** trong 2-6h
        - **Max:** 0.25 mmol/kg trong 6h
        
        **Repeat:**
        - Lặp lại q6-12h nếu cần
        - Kiểm tra PO₄³⁻ sau mỗi lần truyền
        
        **⚠️ Precautions:**
        - **Risk hypocalcemia:** Theo dõi Ca²⁺
        - **Risk hyperphosphatemia:** Không quá 0.25 mmol/kg
        - **Renal failure:** Giảm liều 50-75%
        - **IV site:** Có thể gây kích ứng (phlebitis)
        """)
        
        st.warning("""
        **Moderate (1.0-2.0 mg/dL):**
        
        **Option 1:**
        - **0.08 mmol/kg IV** trong 2-4h
        - Hoặc **15-20 mmol IV** trong 2-4h
        
        **Option 2:**
        - **10-15 mmol IV** trong 2-4h q12h × 2-3 lần
        """)
        
        st.info("""
        **Formulations:**
        
        **Potassium Phosphate:**
        - 1 ml = 3 mmol PO4 + 4.4 mEq K
        - 15 mmol = 5 ml
        
        **Sodium Phosphate:**
        - 1 ml = 3 mmol PO4 + 4 mEq Na
        - 15 mmol = 5 ml
        
        **⚠️ Chọn dựa trên:**
        - K⁺ level (dùng KPO4 nếu hypokalemia)
        - Na⁺ level (dùng NaPO4 nếu hyponatremia)
        - Volume status
        """)
    
    with tab2:
        st.markdown("#### 💊 Oral Phosphate Replacement")
        
        st.success("""
        **Mild to moderate (≥1.0 mg/dL, asymptomatic/mild symptoms):**
        
        **Options:**
        
        **1. Sodium Phosphate:**
        - 250-500mg PO q6-8h
        - Tác dụng phụ: Tiêu chảy
        
        **2. Potassium Phosphate:**
        - 250-500mg PO q6-8h
        - Nếu có hypokalemia
        
        **3. Neutra-Phos:**
        - 250mg PO q6-8h
        - Balanced Na/K
        
        **Duration:**
        - 1-2 tuần
        - Kiểm tra PO₄³⁻ sau 3-5 ngày
        """)
        
        st.warning("""
        **⚠️ Lưu ý:**
        - Tiêu chảy có thể hạn chế hấp thu
        - Cần thời gian để bù đủ
        - Không dùng nếu severe hoặc symptomatic
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Common Causes")
    
    st.warning("""
    **Refeeding Syndrome:**
    - Sau nhịn đói lâu
    - TPN/enteral nutrition
    - ⚠️ Cần bổ sung PO4 sớm
    
    **Alcoholism:**
    - Malnutrition
    - Renal losses
    
    **DKA Recovery:**
    - Insulin đưa PO4 vào tế bào
    - ⚠️ Theo dõi sát khi điều trị DKA
    
    **GI Losses:**
    - Diarrhea, vomiting
    - Malabsorption
    
    **Renal Losses:**
    - Hyperparathyroidism
    - Fanconi syndrome
    - Medications (diuretics)
    
    **Redistribution:**
    - Respiratory alkalosis
    - Hungry bone syndrome
    - Sepsis
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Refeeding Syndrome:**
    - Bổ sung PO4 ngay khi bắt đầu nutrition
    - 15-30 mmol/ngày × 3-5 ngày
    - Theo dõi sát PO4, K⁺, Mg²⁺, Ca²⁺
    
    **DKA Recovery:**
    - Bổ sung PO4 khi K⁺ <4.0
    - 15-30 mmol trong 2-4h
    - Theo dõi sát
    
    **Renal Failure:**
    - Giảm liều 50-75%
    - Theo dõi sát (risk hyperphosphatemia)
    - Tránh dùng nếu CrCl <30
    
    **Hypocalcemia:**
    - Bổ sung PO4 có thể làm giảm Ca²⁺
    - Điều chỉnh Ca²⁺ trước hoặc đồng thời
    """)


def render_hypocalcemia():
    """Hypocalcemia Emergency Protocol"""
    
    st.error("## 🚨 HYPOCALCEMIA EMERGENCY PROTOCOL")
    
    st.markdown("### 1️⃣ Severity & Symptoms")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.warning("""
        **Severity (Total Ca):**
        
        **Mild (8.0-8.5 mg/dL):**
        - Often asymptomatic
        - Mild paresthesias
        
        **Moderate (7.0-8.0 mg/dL):**
        - Paresthesias (fingers, toes, lips)
        - Muscle cramps
        - Chvostek sign, Trousseau sign
        
        **Severe (<7.0 mg/dL):**
        - Tetany
        - Seizures
        - Laryngospasm
        - Cardiac arrhythmias
        - Prolonged QT
        """)
    
    with col2:
        st.error("""
        **⚠️ Ionized Ca (iCa) - More Important:**
        
        **Normal:** 4.5-5.3 mg/dL (1.1-1.3 mmol/L)
        
        **Mild:** 4.0-4.5 mg/dL
        **Moderate:** 3.5-4.0 mg/dL
        **Severe:** <3.5 mg/dL
        
        **⚠️ Check iCa nếu:**
        - Albumin thấp
        - pH bất thường
        - Critical illness
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Correction for Albumin")
    
    col1, col2 = st.columns(2)
    
    with col1:
        total_ca = st.number_input(
            "Total Ca hiện tại (mg/dL)",
            min_value=5.0,
            max_value=12.0,
            value=7.5,
            step=0.1,
            format="%.1f",
            key="ca_total"
        )
        
        albumin = st.number_input(
            "Albumin (g/dL)",
            min_value=1.0,
            max_value=5.0,
            value=4.0,
            step=0.1,
            format="%.1f",
            key="ca_albumin"
        )
        
        ionized_ca = st.number_input(
            "Ionized Ca (mg/dL) - nếu có",
            min_value=2.0,
            max_value=7.0,
            value=0.0,
            step=0.1,
            format="%.1f",
            key="ca_ionized"
        )
    
    with col2:
        # Corrected Ca = Total Ca + 0.8 × (4.0 - Albumin)
        corrected_ca = total_ca + 0.8 * (4.0 - albumin)
        
        st.markdown("### 📊 Kết Quả:")
        
        st.metric("Total Ca", f"{total_ca:.1f} mg/dL")
        st.metric("Corrected Ca", f"{corrected_ca:.1f} mg/dL")
        
        if ionized_ca > 0:
            st.metric("Ionized Ca", f"{ionized_ca:.1f} mg/dL")
            if ionized_ca < 3.5:
                st.error("🚨 **SEVERE HYPOCALCEMIA** - Cần điều trị ngay!")
            elif ionized_ca < 4.0:
                st.warning("⚠️ **MODERATE HYPOCALCEMIA**")
            else:
                st.info("✅ Ionized Ca trong giới hạn")
        else:
            if corrected_ca < 7.0:
                st.error("🚨 **SEVERE HYPOCALCEMIA** - Cần điều trị ngay!")
            elif corrected_ca < 8.0:
                st.warning("⚠️ **MODERATE HYPOCALCEMIA**")
            else:
                st.info("✅ Corrected Ca trong giới hạn")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Treatment")
    
    tab1, tab2, tab3 = st.tabs(["Severe Symptomatic", "Moderate", "Chronic"])
    
    with tab1:
        st.markdown("#### 🚨 Severe Symptomatic (<7.0 mg/dL hoặc iCa <3.5)")
        
        st.error("""
        **EMERGENCY - IV Calcium:**
        
        **Calcium Gluconate 10% (Preferred):**
        - **1-2g IV** (10-20ml) trong 10-20 phút
        - Hoặc 10-15 mg/kg (1-1.5 mEq/kg)
        - **Effect:** Immediate (within minutes)
        - **Duration:** 2-3h
        
        **Calcium Chloride 10% (Nếu không có gluconate):**
        - **0.5-1g IV** (5-10ml) trong 5-10 phút
        - Hoặc 5-10 mg/kg (0.5-1 mEq/kg)
        - **⚠️ More irritating, use central line if possible**
        
        **After initial dose:**
        - **Continuous infusion:** 1-2g/h (10-20 mg/kg/h)
        - Hoặc **Intermittent:** 1g q4-6h
        - **Duration:** 12-24h hoặc đến khi ổn định
        
        **Monitoring:**
        - Ca²⁺ mỗi 2-4h
        - ECG (QT interval)
        - Symptoms (tetany, seizures)
        """)
        
        st.warning("""
        **⚠️ Precautions:**
        - **Hypercalcemia:** Không quá 2g trong 1h
        - **Digoxin:** Cẩn thận (risk arrhythmias)
        - **IV site:** Có thể gây kích ứng (phlebitis)
        - **Renal failure:** Theo dõi sát PO4
        """)
    
    with tab2:
        st.markdown("#### ⚠️ Moderate (7.0-8.0 mg/dL hoặc iCa 3.5-4.0)")
        
        st.warning("""
        **Option 1: IV Calcium:**
        - **1g Calcium gluconate IV** trong 1h
        - Lặp lại q6-8h nếu cần
        
        **Option 2: Oral Calcium:**
        - **Calcium carbonate:** 1-2g PO q6-8h
        - Hoặc **Calcium citrate:** 1-2g PO q6-8h
        - **With meals** (tăng hấp thu)
        
        **Duration:**
        - 1-2 tuần
        - Kiểm tra Ca²⁺ sau 3-5 ngày
        """)
        
        st.info("""
        **If hypomagnesemia present:**
        - Điều chỉnh Mg²⁺ trước hoặc đồng thời
        - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
        """)
    
    with tab3:
        st.markdown("#### 📅 Chronic Hypocalcemia")
        
        st.success("""
        **Oral Calcium:**
        - **Calcium carbonate:** 1-2g PO TID (với meals)
        - Hoặc **Calcium citrate:** 1-2g PO TID
        - **Total:** 1.5-3g elemental Ca/ngày
        
        **Vitamin D:**
        - **Cholecalciferol (D3):** 1000-2000 IU/ngày
        - Hoặc **Calcitriol:** 0.25-0.5 mcg BID (nếu suy thận)
        
        **Monitoring:**
        - Ca²⁺, PO4, PTH mỗi 3-6 tháng
        - 24h urine Ca (risk nephrolithiasis)
        """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Common Causes")
    
    st.warning("""
    **Hypoparathyroidism:**
    - Post-surgical (thyroid, parathyroid surgery)
    - Autoimmune
    - Congenital
    
    **Vitamin D Deficiency:**
    - Malnutrition
    - Malabsorption
    - Renal failure (decreased 1,25-OH D)
    
    **Hypomagnesemia:**
    - ⚠️ Luôn kiểm tra Mg²⁺
    - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
    
    **Renal Failure:**
    - Decreased 1,25-OH D production
    - Hyperphosphatemia
    
    **Acute Pancreatitis:**
    - Saponification (Ca binds to fat)
    
    **Massive Transfusion:**
    - Citrate chelation
    
    **Hungry Bone Syndrome:**
    - Sau parathyroidectomy
    - Sau điều trị hypercalcemia
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Special Considerations")
    
    st.info("""
    **Hypomagnesemia:**
    - ⚠️ Luôn kiểm tra và điều chỉnh Mg²⁺
    - Khó điều chỉnh Ca²⁺ nếu không bổ sung Mg
    
    **Hyperphosphatemia:**
    - Điều chỉnh PO4 trước hoặc đồng thời
    - Ca × PO4 product <55 (risk precipitation)
    
    **Digoxin:**
    - Cẩn thận với IV Ca (risk arrhythmias)
    - Điều chỉnh từ từ
    
    **Renal Failure:**
    - Dùng Calcitriol (1,25-OH D)
    - Điều chỉnh PO4 trước
    - Theo dõi sát Ca × PO4 product
    
    **Pregnancy:**
    - Ca²⁺ an toàn
    - Liều tương tự
    - Theo dõi sát
    """)

