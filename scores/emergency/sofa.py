"""
SOFA Score (Sequential Organ Failure Assessment)
Multi-organ dysfunction assessment
"""

import streamlit as st


def render():
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

