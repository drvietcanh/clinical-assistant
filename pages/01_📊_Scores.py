"""
Scores Module - Clinical Scoring Systems
"""

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Scores - Clinical Assistant", page_icon="📊", layout="wide")

# ========== HEADER ==========
st.title("📊 Thang Điểm Lâm Sàng")
st.markdown("Calculators cho các hệ thống đánh giá lâm sàng phổ biến")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Chọn Thang Điểm")
    
    score_type = st.selectbox(
        "Calculator:",
        [
            "qSOFA - Quick SOFA",
            "SOFA - Sequential Organ Failure Assessment",
            "CHA₂DS₂-VASc - Stroke Risk in AF",
            "HAS-BLED - Bleeding Risk",
            "CURB-65 - Pneumonia Severity",
            "GCS - Glasgow Coma Scale"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **Tất cả calculators dựa trên:**
    - Guidelines quốc tế
    - Evidence-based medicine
    - Peer-reviewed publications
    """)

# ========== MAIN CONTENT ==========

# ===== qSOFA =====
if "qSOFA" in score_type:
    st.subheader("🩺 qSOFA (Quick SOFA)")
    st.caption("Sepsis-3 Criteria for Sepsis Screening")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Patient Parameters")
        
        # Inputs
        rr = st.number_input(
            "Respiratory Rate (/min)",
            min_value=0,
            max_value=60,
            value=20,
            step=1,
            help="Normal: 12-20 /min"
        )
        
        sbp = st.number_input(
            "Systolic Blood Pressure (mmHg)",
            min_value=0,
            max_value=300,
            value=120,
            step=1,
            help="Normal: 90-120 mmHg"
        )
        
        gcs = st.number_input(
            "Glasgow Coma Scale",
            min_value=3,
            max_value=15,
            value=15,
            step=1,
            help="Normal: 15; Coma: 3"
        )
        
        # Calculate button
        if st.button("🔢 Calculate qSOFA", type="primary"):
            # Calculation
            score = 0
            details = []
            
            if rr >= 22:
                score += 1
                details.append("✓ Respiratory rate ≥22 /min (+1)")
            else:
                details.append("✗ Respiratory rate <22 /min (0)")
            
            if sbp <= 100:
                score += 1
                details.append("✓ Systolic BP ≤100 mmHg (+1)")
            else:
                details.append("✗ Systolic BP >100 mmHg (0)")
            
            if gcs < 15:
                score += 1
                details.append("✓ Altered mentation (GCS <15) (+1)")
            else:
                details.append("✗ GCS = 15 (0)")
            
            # Display result
            with col2:
                st.markdown("### Result")
                
                # Score display
                if score >= 2:
                    st.error(f"## qSOFA = {score}")
                    st.error("⚠️ **CONCERNING FOR SEPSIS**")
                    interpretation = """
                    **Action Required:**
                    - Assess for infection source
                    - Consider blood cultures
                    - Start antibiotics if indicated
                    - Monitor closely
                    - Calculate full SOFA score
                    """
                elif score == 1:
                    st.warning(f"## qSOFA = {score}")
                    st.warning("⚡ Intermediate Risk")
                    interpretation = """
                    **Consider:**
                    - Close monitoring
                    - Reassess frequently
                    - Look for other sepsis signs
                    """
                else:
                    st.success(f"## qSOFA = {score}")
                    st.success("✅ Low Risk")
                    interpretation = """
                    **Interpretation:**
                    - Low probability of sepsis
                    - Routine monitoring
                    - Reassess if clinical change
                    """
                
                st.markdown(interpretation)
            
            # Details
            st.markdown("### Breakdown")
            for detail in details:
                st.write(detail)
            
            # Reference
            with st.expander("📚 Clinical Reference"):
                st.markdown("""
                **qSOFA (Quick SOFA) Score**
                
                **Purpose:** Rapid bedside screening for sepsis outside ICU
                
                **Criteria (1 point each):**
                1. Respiratory rate ≥ 22/min
                2. Altered mentation (GCS < 15)
                3. Systolic blood pressure ≤ 100 mmHg
                
                **Interpretation:**
                - **qSOFA ≥ 2:** Concerning for sepsis
                  - Increased risk of death or prolonged ICU stay
                  - Triggers full SOFA assessment
                  - Consider sepsis bundle
                
                - **qSOFA < 2:** Lower risk
                  - Does NOT rule out infection
                  - Clinical judgment still essential
                
                **Limitations:**
                - NOT for diagnosis, only screening
                - Less sensitive than SIRS criteria
                - Better specificity for adverse outcomes
                
                **Reference:**
                Singer M, et al. The Third International Consensus Definitions 
                for Sepsis and Septic Shock (Sepsis-3). JAMA. 2016;315(8):801-810.
                doi:10.1001/jama.2016.0287
                
                **Guidelines:**
                - Surviving Sepsis Campaign 2021
                - Use as part of clinical assessment
                - Not a standalone diagnostic tool
                """)
    
    # Additional tools
    st.markdown("---")
    st.info("""
    **Next Steps:**
    - If qSOFA ≥2 → Calculate full **SOFA score**
    - Consider **Sepsis Bundle** protocol
    - Review **Antibiotic** selection
    """)

# ===== SOFA =====
elif "SOFA" in score_type:
    st.subheader("🏥 SOFA Score")
    st.caption("Sequential Organ Failure Assessment")
    
    st.warning("""
    🚧 **Under Development**
    
    SOFA calculator đang được phát triển.
    
    **Dự kiến hoàn thành:** Week 2
    
    **Sẽ bao gồm:**
    - Respiratory (PaO₂/FiO₂)
    - Coagulation (Platelets)
    - Liver (Bilirubin)
    - Cardiovascular (MAP, Vasopressors)
    - CNS (GCS)
    - Renal (Creatinine, Urine output)
    """)
    
    st.markdown("### Preview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pao2_fio2 = st.number_input("PaO₂/FiO₂ (mmHg)", value=350)
    with col2:
        platelets = st.number_input("Platelets (×10³/µL)", value=150)
    with col3:
        bilirubin = st.number_input("Bilirubin (mg/dL)", value=1.0, step=0.1)
    
    st.info("Full SOFA calculator coming soon...")

# ===== CHA2DS2-VASc =====
elif "CHA₂DS₂-VASc" in score_type:
    st.subheader("❤️ CHA₂DS₂-VASc Score")
    st.caption("Stroke Risk Stratification in Atrial Fibrillation")
    
    st.warning("🚧 **Under Development** - Expected: Week 2")
    
    st.markdown("""
    **Will include:**
    - C: Congestive heart failure (1 point)
    - H: Hypertension (1 point)
    - A₂: Age ≥75 (2 points)
    - D: Diabetes (1 point)
    - S₂: Prior Stroke/TIA (2 points)
    - V: Vascular disease (1 point)
    - A: Age 65-74 (1 point)
    - Sc: Sex category (Female = 1 point)
    
    **Reference:** ESC AF Guidelines 2020
    """)

# ===== HAS-BLED =====
elif "HAS-BLED" in score_type:
    st.subheader("🩸 HAS-BLED Score")
    st.caption("Bleeding Risk in Anticoagulated Patients")
    
    st.warning("🚧 **Under Development** - Expected: Week 3")

# ===== CURB-65 =====
elif "CURB-65" in score_type:
    st.subheader("🫁 CURB-65")
    st.caption("Pneumonia Severity Assessment")
    
    st.warning("🚧 **Under Development** - Expected: Week 3")

# ===== GCS =====
elif "GCS" in score_type:
    st.subheader("🧠 Glasgow Coma Scale")
    st.caption("Level of Consciousness Assessment")
    
    st.warning("🚧 **Under Development** - Expected: Week 2")

# ========== FOOTER ==========
st.markdown("---")
st.caption("📚 All scores based on international guidelines and peer-reviewed literature")
st.caption("⚠️ For reference only - Always use clinical judgment")

