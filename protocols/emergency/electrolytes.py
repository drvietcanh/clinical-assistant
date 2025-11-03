"""
Electrolyte Emergency Protocols
Hyperkalemia & Hyponatremia Correction
"""

import streamlit as st


def render():
    """Electrolyte Emergency Protocols"""
    st.subheader("⚡ Electrolyte Emergency Protocols")
    st.caption("Hyperkalemia & Hyponatremia Correction")
    
    st.markdown("---")
    
    # Electrolyte selection
    electrolyte = st.radio(
        "**Chọn tình trạng:**",
        ["Hyperkalemia (Tăng kali máu)", "Hyponatremia (Hạ natri máu)"],
        key="electrolyte_type"
    )
    
    st.markdown("---")
    
    if "Hyperkalemia" in electrolyte:
        render_hyperkalemia()
    else:
        render_hyponatremia()


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

