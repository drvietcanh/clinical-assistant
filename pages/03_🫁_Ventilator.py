"""
Ventilator Module - Mechanical Ventilation Settings
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Ventilator - Clinical Assistant", page_icon="🫁", layout="wide")

# ========== HEADER ==========
st.title("🫁 Thở Máy - Ventilator Settings")
st.markdown("Cài đặt thông số máy thở ban đầu")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("Chọn Protocol")
    
    protocol = st.selectbox(
        "Tình huống lâm sàng:",
        [
            "ARDSNet - Low Tidal Volume",
            "COPD - Permissive Hypercapnia",
            "Asthma - High I:E Ratio",
            "Obesity - PBW-based",
            "PEEP/FiO₂ Table"
        ]
    )
    
    st.markdown("---")
    st.info("""
    **Guidelines:**
    - ARDSNet Protocol (NEJM 2000)
    - GOLD COPD Guidelines
    - GINA Asthma Guidelines
    """)

# ========== MAIN CONTENT ==========

# ===== ARDSNet =====
if "ARDSNet" in protocol:
    st.subheader("🫁 ARDSNet Low Tidal Volume Ventilation")
    st.caption("For ARDS / Acute Lung Injury")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Patient Parameters")
        
        height = st.number_input(
            "Height (cm)",
            min_value=140,
            max_value=220,
            value=170,
            step=1
        )
        
        sex = st.radio(
            "Sex",
            ["Male", "Female"],
            horizontal=True
        )
        
        fio2 = st.slider(
            "FiO₂ (%)",
            min_value=30,
            max_value=100,
            value=60,
            step=5,
            help="Current or target FiO₂"
        ) / 100
        
        if st.button("Calculate ARDSNet Settings", type="primary"):
            # Calculate PBW (Predicted Body Weight)
            height_inch = height / 2.54
            if sex == "Male":
                pbw = 50 + 2.3 * (height_inch - 60)
            else:
                pbw = 45.5 + 2.3 * (height_inch - 60)
            
            pbw = round(pbw, 1)
            
            # Tidal Volume: 6 mL/kg PBW
            vt = round(6 * pbw)
            
            # PEEP based on FiO₂ (ARDSNet lower PEEP table)
            peep_table = {
                0.3: 5,  0.35: 5,  0.4: 5,  0.45: 8,
                0.5: 8,  0.55: 10, 0.6: 10, 0.65: 10,
                0.7: 10, 0.75: 14, 0.8: 14, 0.85: 14,
                0.9: 14, 0.95: 18, 1.0: 18
            }
            
            # Find closest FiO₂ in table
            fio2_rounded = min(peep_table.keys(), key=lambda x: abs(x - fio2))
            peep = peep_table[fio2_rounded]
            
            # Display results
            with col2:
                st.markdown("### Initial Settings")
                
                st.success(f"**PBW:** {pbw} kg")
                
                st.metric("Mode", "Volume Control")
                st.metric("Tidal Volume", f"{vt} mL")
                st.metric("Rate", "20-25 /min")
                st.metric("FiO₂", f"{int(fio2*100)}%")
                st.metric("PEEP", f"{peep} cmH₂O")
            
            # Goals
            st.markdown("### Goals & Targets")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.markdown("""
                **Ventilator Goals:**
                - ✅ Vt = 6 mL/kg PBW
                - ✅ Plateau pressure < 30 cmH₂O
                - ✅ pH ≥ 7.30
                - ✅ SpO₂ 88-95% or PaO₂ 55-80 mmHg
                """)
            
            with col_b:
                st.markdown("""
                **Monitoring:**
                - Plateau pressure q4h
                - ABG q4-6h initially
                - Adjust FiO₂/PEEP per table
                - Wean as tolerated
                """)
            
            # PEEP/FiO₂ Table
            with st.expander("📊 ARDSNet PEEP/FiO₂ Table (Lower PEEP)"):
                peep_fio2_df = pd.DataFrame({
                    'FiO₂': ['0.3', '0.4', '0.4', '0.5', '0.5', '0.6', '0.7', '0.7', '0.7', '0.8', '0.9', '0.9', '1.0'],
                    'PEEP (cmH₂O)': [5, 5, 8, 8, 10, 10, 10, 12, 14, 14, 14, 16, 18]
                })
                st.table(peep_fio2_df)
            
            # Reference
            with st.expander("📚 Clinical Reference"):
                st.markdown("""
                **ARDSNet Protocol for ARDS**
                
                **Strategy:** Low Tidal Volume Ventilation
                
                **Key Principles:**
                1. **Limit Vt:** 6 mL/kg PBW (not actual weight!)
                2. **Limit Pplat:** Keep < 30 cmH₂O
                3. **Permissive hypercapnia:** Accept pH ≥ 7.30
                4. **Moderate oxygenation:** SpO₂ 88-95%
                
                **Adjustments:**
                - If Pplat > 30: ↓ Vt by 1 mL/kg (min 4 mL/kg)
                - If pH < 7.30: ↑ Rate (max 35)
                - If pH < 7.15: Consider bicarb, prone positioning
                
                **FiO₂/PEEP Titration:**
                - Use table to balance oxygenation
                - Higher PEEP strategy alternative exists
                - Wean FiO₂ first to <0.4, then wean PEEP
                
                **Mortality Benefit:**
                - 22% vs. 40% (ARMA trial)
                - NNT = 6
                
                **Reference:**
                The Acute Respiratory Distress Syndrome Network. Ventilation 
                with lower tidal volumes as compared with traditional tidal 
                volumes for acute lung injury and the acute respiratory 
                distress syndrome. N Engl J Med. 2000;342(18):1301-1308.
                
                **Guidelines:**
                - AHRQ LTVV Guide
                - ARDSNet Protocol Cards (ardsnet.org)
                """)

# ===== COPD =====
elif "COPD" in protocol:
    st.subheader("🫁 COPD Ventilator Settings")
    st.caption("Permissive Hypercapnia Strategy")
    
    st.warning("🚧 **Under Development** - Expected: Week 3")
    
    st.markdown("""
    **Preview - COPD Ventilation:**
    
    **Key Principles:**
    - Lower tidal volume (6-8 mL/kg IBW)
    - Lower PEEP (3-5 cmH₂O) to minimize auto-PEEP
    - Longer expiratory time (I:E 1:3 to 1:5)
    - Permissive hypercapnia (accept PaCO₂ 50-70)
    
    **Initial Settings:**
    - Mode: Volume or Pressure Control
    - Vt: 6-8 mL/kg IBW
    - Rate: 10-14 /min (start low)
    - PEEP: 3-5 cmH₂O
    - I:E: 1:3 or longer
    
    **Monitoring:**
    - Auto-PEEP (plateau - PEEP)
    - Peak airway pressure
    - Expiratory flow (ensure reaches zero)
    
    **Reference:** GOLD 2025, ATS/ERS Guidelines
    """)

# ===== PEEP/FiO2 Table =====
elif "PEEP/FiO₂" in protocol:
    st.subheader("📊 PEEP/FiO₂ Combination Table")
    st.caption("ARDSNet Oxygenation Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Lower PEEP Strategy")
        lower_peep = pd.DataFrame({
            'FiO₂': [0.3, 0.4, 0.4, 0.5, 0.5, 0.6, 0.7, 0.7, 0.7, 0.8, 0.9, 0.9, 0.9, 0.9, 1.0, 1.0, 1.0],
            'PEEP': [5, 5, 8, 8, 10, 10, 10, 12, 14, 14, 14, 16, 18, 20, 20, 22, 24]
        })
        st.dataframe(lower_peep, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### Higher PEEP Strategy")
        higher_peep = pd.DataFrame({
            'FiO₂': [0.3, 0.3, 0.3, 0.4, 0.4, 0.5, 0.5, 0.5, 0.6, 0.7, 0.7, 0.8, 0.9, 1.0, 1.0],
            'PEEP': [5, 8, 10, 10, 12, 12, 14, 16, 16, 16, 18, 18, 20, 22, 24]
        })
        st.dataframe(higher_peep, use_container_width=True, hide_index=True)
    
    st.markdown("""
    ### How to Use
    
    1. **Titrate FiO₂ and PEEP together** based on SpO₂/PaO₂
    2. **Target:** SpO₂ 88-95% or PaO₂ 55-80 mmHg
    3. **Wean:** Decrease FiO₂ first to < 0.4, then decrease PEEP
    4. **Increase:** Follow table upward
    
    **Notes:**
    - Lower PEEP = traditional ARDSNet
    - Higher PEEP = may be beneficial in severe ARDS
    - No clear mortality benefit between strategies
    - Use clinical judgment
    """)

# ===== Others =====
else:
    st.info(f"**{protocol}** calculator under development")

# ========== FOOTER ==========
st.markdown("---")

st.warning("""
**⚠️ Critical Ventilator Safety:**
- Always verify settings with attending physician
- Monitor plateau pressure q4h (keep < 30 cmH₂O)
- Check ABG 30 min after changes
- Set appropriate alarms
- Document all changes
""")

st.caption("📚 Based on ARDSNet ARMA trial, GOLD guidelines, and ATS/ERS recommendations")

