"""
Emergency & Critical Care Scoring Systems
All emergency and ICU calculators
"""

import streamlit as st


def render_qsofa():
    """qSOFA (Quick SOFA) Calculator"""
    st.subheader("🩺 qSOFA (Quick SOFA)")
    st.caption("Sepsis-3 Criteria for Sepsis Screening")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Patient Parameters")
        
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
        
        if st.button("🔢 Calculate qSOFA", type="primary"):
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
            
            with col2:
                st.markdown("### Result")
                
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
            
            st.markdown("### Breakdown")
            for detail in details:
                st.write(detail)
            
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
    
    st.markdown("---")
    st.info("""
    **Next Steps:**
    - If qSOFA ≥2 → Calculate full **SOFA score**
    - Consider **Sepsis Bundle** protocol
    - Review **Antibiotic** selection
    """)


def render_sofa():
    """SOFA Score Calculator"""
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


def render_apache2():
    """APACHE II Score Calculator"""
    st.subheader("🏥 APACHE II")
    st.caption("Acute Physiology and Chronic Health Evaluation II")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")


def render_saps2():
    """SAPS II Score Calculator"""
    st.subheader("🏥 SAPS II")
    st.caption("Simplified Acute Physiology Score II")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 4")


def render_mods():
    """MODS Score Calculator"""
    st.subheader("🏥 MODS")
    st.caption("Multiple Organ Dysfunction Score")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 4")


# Router function
def render_emergency_calculator(calculator_id):
    """
    Route to the correct emergency calculator based on ID
    
    Args:
        calculator_id: The ID of the calculator to render
    """
    calculators = {
        "qSOFA": render_qsofa,
        "SOFA": render_sofa,
        "APACHE II": render_apache2,
        "SAPS II": render_saps2,
        "MODS": render_mods,
    }
    
    calculator_func = calculators.get(calculator_id)
    if calculator_func:
        calculator_func()
    else:
        st.error(f"Calculator '{calculator_id}' not found!")

