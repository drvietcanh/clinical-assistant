"""
Diabetic Ketoacidosis (DKA) Protocol
DKA Management Protocol
"""

import streamlit as st


def calculate_fluid_deficit(weight_kg, current_na, baseline_na=140):
    """
    Calculate fluid deficit in DKA
    
    Args:
        weight_kg: Body weight
        current_na: Current sodium
        baseline_na: Baseline sodium (usually 140 mEq/L)
    
    Returns:
        Fluid deficit in liters
    """
    # Simplified: Assume 10% dehydration in severe DKA
    fluid_deficit_l = weight_kg * 0.1
    
    # Adjust based on Na (if Na high → more dehydration)
    if current_na > baseline_na:
        correction = (current_na - baseline_na) * 2  # Rough estimate
        fluid_deficit_l += correction
    
    return round(fluid_deficit_l, 1)


def calculate_insulin_rate(weight_kg):
    """
    Calculate initial insulin infusion rate
    
    Args:
        weight_kg: Body weight
    
    Returns:
        Insulin rate in U/h
    """
    # Standard: 0.1 U/kg/h
    rate = weight_kg * 0.1
    return round(rate, 1)


def render():
    """DKA Protocol"""
    st.subheader("🍭 DKA Protocol")
    st.caption("Diabetic Ketoacidosis Management - ADA/ISPAD Guidelines")
    
    st.error("""
    **DKA Diagnostic Criteria:**
    - Glucose >250 mg/dL (thường >300)
    - pH <7.3 HOẶC HCO₃⁻ <18 mEq/L
    - Ketones (+)
    - Anion gap >12
    """)
    
    st.markdown("---")
    
    # Severity selection
    severity = st.radio(
        "**Mức độ DKA:**",
        ["Nhẹ", "Trung bình", "Nặng"],
        key="dka_severity"
    )
    
    st.markdown("---")
    
    if "Nhẹ" in severity:
        render_mild_dka()
    elif "Trung bình" in severity:
        render_moderate_dka()
    else:
        render_severe_dka()


def render_mild_dka():
    """Mild DKA Management"""
    
    st.warning("## ⚠️ MILD DKA PROTOCOL")
    
    st.markdown("### Criteria:")
    st.info("""
    - pH: 7.25-7.30
    - HCO₃⁻: 15-18 mEq/L
    - Anion gap: 10-12
    - Mental status: Alert
    """)
    
    st.markdown("---")
    st.markdown("### 1️⃣ Resuscitation")
    
    st.success("""
    **Fluids:**
    - NS 0.9%: 1-1.5L trong 1-2h đầu
    - Sau đó: NS hoặc 0.45% NS dựa trên Na⁺
    - Mục tiêu: Correct trong 24-48h
    
    **Insulin:**
    - **IV Insulin:** 0.1 U/kg/h
    - Hoặc **SC insulin:** Rapid-acting mỗi 1-2h
    - Mục tiêu: Glucose drop 50-75 mg/dL/h
    
    **Monitoring:**
    - Glucose mỗi 1-2h
    - ABG/VBG mỗi 4h
    - Electrolytes mỗi 4h
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Transition to SC Insulin")
    
    st.info("""
    **Khi nào chuyển SC:**
    - pH >7.3
    - HCO₃⁻ >18
    - Anion gap <12
    - Bệnh nhân ăn được
    
    **Cách chuyển:**
    - Cho SC insulin 30-60 phút TRƯỚC khi ngừng IV
    - Overlap để tránh rebound
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Discharge Criteria")
    
    st.success("""
    - pH >7.3
    - HCO₃⁻ >18
    - Bệnh nhân ăn được
    - Có kế hoạch điều trị tại nhà
    """)


def render_moderate_dka():
    """Moderate DKA Management"""
    
    st.error("## 🚨 MODERATE DKA PROTOCOL")
    
    st.markdown("### Criteria:")
    st.warning("""
    - pH: 7.00-7.24
    - HCO₃⁻: 10-15 mEq/L
    - Anion gap: 12-15
    - Mental status: Alert or drowsy
    """)
    
    st.markdown("---")
    st.markdown("### 1️⃣ Immediate Resuscitation")
    
    st.error("""
    **< 1 Hour:**
    
    1. ✅ **IV access:** 2 lines
    2. ✅ **Labs:** Glucose, ABG, CBC, CMP, ketones
    3. ✅ **ECG** (tìm hypokalemia)
    4. ✅ **Fluid bolus:** 1-1.5L NS 0.9% trong 1h
    5. ✅ **Insulin:** 0.1 U/kg/h IV (không bolus!)
    6. ✅ **K⁺ replacement:** Nếu K <5.5 và urine output tốt
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Fluid Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Calculate Fluid Deficit:**
        
        **Typical deficit:** 6-10% body weight
        
        **Timeline:**
        - **0-2h:** 1-1.5L NS
        - **2-12h:** 50% của deficit
        - **12-24h:** 50% còn lại
        
        **Type:**
        - Na <135: NS 0.9%
        - Na normal/high: 0.45% NS hoặc NS
        """)
    
    with col2:
        st.warning("""
        **Monitoring:**
        
        **Signs of over-resuscitation:**
        - Na drop >5 mEq/L/h
        - Headache, confusion
        - Cerebral edema risk (peds)
        
        **Signs of under-resuscitation:**
        - Persistent hypotension
        - Low UO
        - Tachycardia
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Insulin Protocol")
    
    st.success("""
    **IV Insulin Infusion:**
    
    **Rate:** 0.1 U/kg/h (no bolus!)
    
    **Example:** 70kg patient
    - Rate: 7 U/h
    
    **Titration:**
    - Mục tiêu: Glucose drop 50-75 mg/dL/h
    - Nếu drop <50: Tăng 1-2 U/h
    - Nếu drop >100: Giảm 50% rate
    
    **Khi Glucose <250 mg/dL:**
    - Add D5W hoặc D10W
    - Continue insulin cho đến khi:
      * pH >7.3
      * HCO₃⁻ >18
      * Anion gap <12
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Potassium Replacement")
    
    st.error("""
    **⚠️ CRITICAL: K⁺ thường thấp nhưng K⁺ máu có thể bình thường/cao do acidosis!**
    
    **Check K⁺ mỗi 2-4h**
    
    **K⁺ <3.5:** Thêm K⁺ vào IV fluids
    - 20-40 mEq/L NS (max 40 mEq/L)
    - Mục tiêu: K⁺ 4-5 mEq/L
    
    **K⁺ 3.5-5.0:** Thêm 20 mEq/L vào fluids
    
    **K⁺ >5.0:** KHÔNG cho K⁺ (nhưng check lại sau khi insulin)
    
    **⚠️ Nếu anuria/oliguria:** Cẩn thận với K⁺
    """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Bicarbonate (Controversial)")
    
    st.warning("""
    **Chỉ dùng nếu:**
    - pH <7.0
    - Hemodynamic instability
    - Severe acidosis
    
    **Liều:**
    - 1-2 mEq/kg NaHCO₃ IV trong 1h
    - Mục tiêu: pH 7.1-7.2 (không normalize!)
    
    **⚠️ Lưu ý:**
    - Có thể gây hypokalemia
    - Có thể gây paradoxical CSF acidosis
    - Không dùng thường quy
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Monitoring")
    
    st.info("""
    **Labs:**
    - Glucose: Mỗi 1-2h
    - ABG/VBG: Mỗi 2-4h
    - Electrolytes: Mỗi 4h
    - Ketones: Mỗi 4-6h
    
    **Clinical:**
    - Vital signs mỗi 1-2h
    - Mental status
    - UO
    """)
    
    st.markdown("---")
    st.markdown("### 7️⃣ Resolution Criteria")
    
    st.success("""
    **DKA resolved khi:**
    - pH >7.3
    - HCO₃⁻ >18
    - Anion gap <12
    - Glucose <250 (có thể chuyển SC insulin)
    
    **Timing:** Thường 12-24h
    """)


def render_severe_dka():
    """Severe DKA Management"""
    
    st.error("## 🚨🚨 SEVERE DKA PROTOCOL - ICU")
    
    st.markdown("### Criteria:")
    st.error("""
    - pH: <7.00
    - HCO₃⁻: <10 mEq/L
    - Anion gap: >15
    - Mental status: Obtunded, coma
    - OR: Hemodynamic instability
    """)
    
    st.markdown("---")
    st.markdown("### 1️⃣ Immediate ICU Care")
    
    st.error("""
    **< 30 Minutes:**
    
    1. ✅ **ICU admission**
    2. ✅ **2 IV lines** (16-18G)
    3. ✅ **Arterial line** (nếu shock)
    4. ✅ **Foley catheter**
    5. ✅ **Labs ngay:**
       * Glucose, ABG, CBC, CMP
       * Lactate, ketones
       * Troponin (không loại trừ MI)
    6. ✅ **ECG** (tìm hypokalemia, MI)
    7. ✅ **Chest X-ray** (nếu respiratory distress)
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Aggressive Resuscitation")
    
    st.error("""
    **Fluid:**
    - **Bolus:** 1-2L NS trong 30-60 phút
    - **Sau đó:** Aggressive hydration
    - **Monitor:** CVP, UO, Na trends
    
    **Insulin:**
    - **IV:** 0.1 U/kg/h (NO bolus!)
    - **Titrate:** Aggressively để control glucose
    - **Add D5W/D10W:** Khi glucose <250
    
    **K⁺:**
    - **Check ngay và thường xuyên**
    - **Replace aggressively** (20-40 mEq/L)
    - **Monitor ECG**
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Bicarbonate Consideration")
    
    st.warning("""
    **Cân nhắc NaHCO₃ nếu:**
    - pH <7.0
    - Hemodynamic instability
    - Severe acidosis
    
    **Dose:** 1-2 mEq/kg IV trong 1h
    
    **⚠️ Monitor K⁺ closely!**
    """)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Complications to Watch")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **Cerebral Edema:**
        - Đặc biệt ở trẻ em
        - Dấu hiệu: Headache, confusion, seizures
        - Xử trí: Mannitol, hyperventilation
        
        **Hypokalemia:**
        - Xảy ra sau insulin
        - Monitor thường xuyên
        """)
    
    with col2:
        st.warning("""
        **Hypoglycemia:**
        - Khi glucose <250
        - Add dextrose
        - Don't stop insulin!
        
        **Hyponatremia:**
        - Do hyperglycemia
        - Corrected Na = Na + 1.6 × (Glucose - 100)/100
        """)
    
    st.markdown("---")
    st.markdown("### 5️⃣ Monitoring")
    
    st.info("""
    **ICU Monitoring:**
    - Continuous ECG
    - Arterial BP
    - CVP (nếu cần)
    - Pulse oximetry
    
    **Labs:**
    - Glucose: Mỗi 1h
    - ABG: Mỗi 2-4h
    - Electrolytes: Mỗi 2-4h
    - Ketones: Mỗi 4h
    
    **Clinical:**
    - Neurologic checks mỗi 1-2h
    - Vital signs liên tục
    """)
    
    st.markdown("---")
    st.markdown("### 6️⃣ Resolution & Transition")
    
    st.success("""
    **When stable:**
    - pH >7.3
    - HCO₃⁻ >18
    - Hemodynamically stable
    - Transition to floor
    
    **When eating:**
    - Switch to SC insulin
    - Overlap IV and SC
    
    **Timing:** Usually 24-48h
    """)
    
    st.markdown("---")
    with st.expander("📚 Tài Liệu Tham Khảo"):
        st.markdown("""
        - **ADA Standards of Care 2024**
        - **ISPAD Guidelines 2022**
        - **Key Points:**
          * No insulin bolus (avoid rapid drops)
          * Aggressive fluid resuscitation
          * K⁺ replacement critical
          * Monitor for cerebral edema (peds)
          * Resolution takes 12-24h typically
        """)

