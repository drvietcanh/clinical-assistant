"""
Protocols Module - Clinical Protocols and Guidelines
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Protocols - Clinical Assistant", page_icon="📋", layout="wide")

# ========== HEADER ==========
st.title("📋 Phác Đồ Điều Trị")
st.markdown("Clinical protocols theo guidelines quốc tế")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Chọn Phác Đồ")
    
    protocol = st.selectbox(
        "Clinical Scenario:",
        [
            "COPD Exacerbation",
            "Sepsis 1-Hour Bundle",
            "DKA - Diabetic Ketoacidosis",
            "UGIB - Upper GI Bleeding",
            "HAP/VAP - Hospital Pneumonia",
            "Acute Coronary Syndrome",
            "Anaphylaxis"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **Guidelines:**
    - GOLD 2025 (COPD)
    - Surviving Sepsis 2021
    - ADA 2024 (DKA)
    - ACG/ESGE 2021 (UGIB)
    - IDSA/ATS 2016 (Pneumonia)
    """)

# ========== MAIN CONTENT ==========

# ===== COPD Exacerbation =====
if "COPD" in protocol:
    st.subheader("🫁 COPD Exacerbation Protocol")
    st.caption("GOLD 2025 Guidelines")
    
    # Severity assessment
    st.markdown("### 1️⃣ Assess Severity")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **Mild**
        - SpO₂ >90%
        - No accessory muscles
        - Can speak sentences
        
        ➔ Outpatient treatment
        """)
    
    with col2:
        st.warning("""
        **Moderate**
        - SpO₂ 85-90%
        - Increased work of breathing
        - Speaks in phrases
        
        ➔ Hospitalization
        """)
    
    with col3:
        st.error("""
        **Severe**
        - SpO₂ <85%
        - Severe dyspnea
        - Confusion/drowsiness
        
        ➔ ICU admission
        """)
    
    # Treatment steps
    st.markdown("### 2️⃣ Treatment Bundle")
    
    with st.expander("🎯 **Step 1: Oxygen** (Immediate)", expanded=True):
        st.markdown("""
        **Target:** SpO₂ **88-92%**
        
        - Start with nasal cannula 1-2 L/min
        - Titrate to target (avoid hyperoxia!)
        - Use Venturi mask if needed (24-28%)
        - Consider NIV if pH < 7.35
        
        **Monitoring:**
        - Continuous pulse oximetry
        - ABG at 30 min, 1h, then q4-6h
        - Watch for CO₂ retention (hypercapnia)
        
        **Reference:** AARC 2022, BTS 2017, GOLD 2025
        """)
    
    with st.expander("💨 **Step 2: Bronchodilators** (Within 1 hour)"):
        st.markdown("""
        **Short-acting β₂-agonist (SABA):**
        - Salbutamol 2.5-5 mg nebulized q4-6h
        - OR MDI 4-8 puffs q4h
        
        **Short-acting anticholinergic (SAMA):**
        - Ipratropium 0.5 mg nebulized q6h
        - Can combine with SABA
        
        **Combination (preferred):**
        - Salbutamol + Ipratropium nebulized q4-6h
        
        **Notes:**
        - MDI + spacer as effective as nebulizer
        - Continue home long-acting bronchodilators
        """)
    
    with st.expander("💊 **Step 3: Systemic Steroids** (Within 2 hours)"):
        st.markdown("""
        **Dose:**
        - **Prednisone 40 mg PO daily × 5 days**
        - OR Methylprednisolone 40-80 mg IV daily × 5 days
        
        **Duration:** 5 days (NOT longer)
        - No taper needed for 5-day course
        - Longer courses = more side effects, no benefit
        
        **Equivalent doses:**
        - Prednisone 40 mg PO
        - Methylprednisolone 32 mg IV
        - Hydrocortisone 160 mg IV
        
        **Reference:** GOLD 2025, Cochrane Review
        """)
    
    with st.expander("💉 **Step 4: Antibiotics** (If indicated)"):
        st.markdown("""
        **Indications (≥2 of 3):**
        1. Increased dyspnea
        2. Increased sputum volume
        3. Increased sputum purulence
        
        **Empiric choices:**
        - **Amoxicillin/Clavulanate** 875/125 mg PO q12h × 5-7 days
        - **Azithromycin** 500 mg PO daily × 3 days
        - **Levofloxacin** 750 mg PO daily × 5 days
        
        **Severe/ICU:**
        - Ceftriaxone + Azithromycin
        - OR Levofloxacin/Moxifloxacin alone
        
        **Note:** Adjust per local resistance patterns
        """)
    
    with st.expander("🩺 **Step 5: Monitoring & Supportive Care**"):
        st.markdown("""
        **Monitoring:**
        - SpO₂ continuous
        - ABG q4-6h initially
        - ECG (r/o MI)
        - CXR (r/o pneumonia, pneumothorax)
        
        **Supportive:**
        - IV fluids if dehydrated
        - DVT prophylaxis (LMWH)
        - Nutrition support
        - Early mobilization
        
        **NIV Indications:**
        - pH 7.25-7.35
        - PaCO₂ >45 mmHg
        - RR >24
        
        **Intubation Indications:**
        - pH < 7.25
        - Severe hypoxemia despite O₂
        - Decreased LOC
        - Hemodynamic instability
        """)
    
    # Discharge criteria
    st.markdown("### 3️⃣ Discharge Criteria")
    
    st.success("""
    **Safe to discharge when:**
    - ✅ SpO₂ >90% on room air or baseline O₂
    - ✅ Stable vital signs × 24h
    - ✅ Able to eat, sleep, walk
    - ✅ Patient/family confident in management
    - ✅ Follow-up arranged
    
    **Discharge medications:**
    - Continue bronchodilators
    - Complete steroid course (5 days total)
    - Complete antibiotics if started
    - Consider long-term O₂ if indicated
    - Smoking cessation counseling
    """)
    
    # Reference
    with st.expander("📚 Full Guidelines"):
        st.markdown("""
        **GOLD 2025 Report - COPD Exacerbation Management**
        
        **Key Changes 2025:**
        - Emphasis on SpO₂ 88-92% target
        - 5-day steroid course (no longer 7-14 days)
        - NIV as first-line for acidosis
        
        **Evidence:**
        - O₂ target 88-92%: AARC 2022, BTS 2017
        - Steroids 40mg × 5d: Cochrane meta-analysis
        - Antibiotics: Anthonisen criteria (NEJM 1987)
        
        **Links:**
        - GOLD Report: https://goldcopd.org/2025-gold-report/
        - AARC Guidelines: https://rc.rcjournal.com/
        - BTS Guidelines: https://www.brit-thoracic.org.uk/
        """)

# ===== Sepsis =====
elif "Sepsis" in protocol:
    st.subheader("🚨 Sepsis 1-Hour Bundle")
    st.caption("Surviving Sepsis Campaign 2021")
    
    st.error("""
    ### ⏰ TIME-CRITICAL - Complete within 1 hour of recognition
    """)
    
    tasks = [
        {
            "task": "1. Measure lactate",
            "details": "Initial lactate level. Remeasure if >2 mmol/L",
            "completed": False
        },
        {
            "task": "2. Obtain blood cultures BEFORE antibiotics",
            "details": "2 sets (aerobic + anaerobic) from different sites",
            "completed": False
        },
        {
            "task": "3. Administer broad-spectrum antibiotics",
            "details": "Within 1 hour. Empiric coverage based on source",
            "completed": False
        },
        {
            "task": "4. Begin rapid fluid resuscitation",
            "details": "30 mL/kg crystalloid if hypotensive or lactate ≥4",
            "completed": False
        },
        {
            "task": "5. Apply vasopressors if hypotensive",
            "details": "Target MAP ≥65 mmHg during/after fluid resuscitation",
            "completed": False
        }
    ]
    
    for i, item in enumerate(tasks):
        with st.expander(f"**{item['task']}**", expanded=(i<2)):
            st.write(item['details'])
            
            if i == 0:  # Lactate
                st.markdown("""
                **Interpretation:**
                - <2 mmol/L: Low risk
                - 2-4 mmol/L: Moderate risk
                - ≥4 mmol/L: High risk, aggressive resuscitation
                
                **Timing:** Remeasure within 2-4h if elevated
                """)
            
            elif i == 1:  # Blood cultures
                st.markdown("""
                **Technique:**
                - 2 sets from different sites
                - Before antibiotics (but don't delay >45 min)
                - Adequate volume (20-30 mL total)
                
                **Other cultures:** Urine, sputum, wound as indicated
                """)
            
            elif i == 2:  # Antibiotics
                st.markdown("""
                **Empiric choices (adjust per source):**
                
                **Pneumonia (CAP):**
                - Ceftriaxone 2g IV + Azithromycin 500mg IV
                
                **Pneumonia (HAP/VAP):**
                - Pip/Tazo 4.5g IV + Vancomycin
                
                **Intra-abdominal:**
                - Pip/Tazo 4.5g IV OR Meropenem 1g IV
                
                **Urosepsis:**
                - Ceftriaxone 2g IV OR Pip/Tazo 4.5g IV
                
                **Unknown source:**
                - Vancomycin + Pip/Tazo or Meropenem
                
                **De-escalate** based on cultures (48-72h)
                """)
            
            elif i == 3:  # Fluids
                st.markdown("""
                **30 mL/kg crystalloid bolus**
                
                **Example:** 70 kg patient → 2100 mL (≈2L)
                
                **Fluid choice:**
                - Normal saline OR
                - Lactated Ringer's
                
                **Reassess:** After bolus
                - Repeat PRN if still hypotensive
                - Watch for fluid overload
                - Consider dynamic measures (pulse pressure variation)
                """)
            
            elif i == 4:  # Vasopressors
                st.markdown("""
                **First-line: Norepinephrine**
                - Start 0.05 mcg/kg/min
                - Titrate to MAP ≥65 mmHg
                - Max usually 1-2 mcg/kg/min
                
                **Alternative: Vasopressin**
                - Add at 0.03-0.04 units/min
                - Norepinephrine-sparing
                
                **Avoid:** Dopamine (unless bradycardic)
                
                **Target:** MAP ≥65 mmHg (or higher if chronic HTN)
                """)
    
    st.markdown("---")
    st.info("""
    **After 1-Hour Bundle:**
    - Source control (drain abscess, remove infected device)
    - ICU consult if needed
    - Serial lactate q2-4h until normalized
    - Consider steroids if shock refractory
    - Procalcitonin to guide duration
    """)

# ===== Others =====
else:
    st.info(f"**{protocol}** protocol under development")
    
    st.markdown("""
    ### Coming Soon:
    
    **DKA Protocol:**
    - Fluids (NS 1L/h initially)
    - Insulin (0.1 U/kg/h regular)
    - K+ replacement
    - Transition to SubQ insulin
    
    **UGIB Protocol:**
    - Risk stratification (Glasgow-Blatchford)
    - PPI infusion
    - Endoscopy timing
    - Blood transfusion triggers
    
    **HAP/VAP:**
    - Empiric antibiotics (Pip/Tazo + Vanc)
    - Culture-guided de-escalation
    - 7-day treatment duration
    
    **ACS:**
    - Aspirin + P2Y12 inhibitor
    - Anticoagulation
    - Reperfusion strategy
    
    **Anaphylaxis:**
    - Epinephrine 0.3mg IM
    - Remove trigger
    - H1/H2 blockers
    - Steroids
    - Observation 4-6h
    """)

# ========== FOOTER ==========
st.markdown("---")

st.warning("""
**⚠️ Protocol Reminders:**
- These are GENERAL guidelines
- Adjust based on patient-specific factors
- Follow hospital protocols where they differ
- Consult specialist as needed
- Document deviations and rationale
""")

st.caption("📚 Based on international society guidelines (GOLD, Surviving Sepsis, ADA, IDSA, etc.)")

