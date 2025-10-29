"""
Cardiology Protocols
ACS, Heart Failure, and cardiac emergency protocols
"""

import streamlit as st


def render_acs():
    """Acute Coronary Syndrome Protocol"""
    st.subheader("💔 ACS - Hội Chứng Vành Cấp")
    st.caption("STEMI & NSTEMI Management")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 2")
    
    st.info("""
    **ACS Protocol:**
    - STEMI vs NSTEMI
    - Antiplatelet therapy (DAPT)
    - Anticoagulation
    - Reperfusion strategy
    - Time to intervention
    - Post-MI care
    """)


def render_hf():
    """Acute Heart Failure Protocol"""
    st.subheader("💔 Suy Tim Cấp")
    st.caption("Acute Decompensated Heart Failure")
    
    st.warning("🚧 **Đang phát triển** - Dự kiến hoàn thành: Tuần 3")
    
    st.info("""
    **Heart Failure Management:**
    - Phân loại (HFrEF, HFpEF, HFmrEF)
    - Diuretics
    - Vasodilators
    - Inotropes
    - GDMT (Guideline-Directed Medical Therapy)
    """)

