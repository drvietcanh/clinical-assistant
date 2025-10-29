"""
Liver Function Tests (LFT)
"""

import streamlit as st
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def render():
    """Liver Function Tests"""
    st.subheader("🫀 LFT - Liver Function Tests")
    st.caption("Chức Năng Gan")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Enter Values")
        
        alt = st.number_input("ALT/SGPT (U/L)", 0.0, 1000.0, 30.0, 1.0)
        ast = st.number_input("AST/SGOT (U/L)", 0.0, 1000.0, 25.0, 1.0)
        alp = st.number_input("ALP (U/L)", 0.0, 1000.0, 80.0, 1.0)
        bili_t = st.number_input("Bilirubin Total (mg/dL)", 0.0, 30.0, 0.8, 0.1)
        bili_d = st.number_input("Bilirubin Direct (mg/dL)", 0.0, 15.0, 0.2, 0.1)
        albumin = st.number_input("Albumin (g/dL)", 0.0, 10.0, 4.0, 0.1, key="lft_alb")
        tp = st.number_input("Total Protein (g/dL)", 0.0, 15.0, 7.0, 0.1, key="lft_tp")
        
        # Calculate ratios
        if ast > 0:
            ast_alt_ratio = ast / alt
            st.info(f"**AST/ALT ratio:** {ast_alt_ratio:.2f}")
            if ast_alt_ratio > 2:
                st.caption("⬆️ >2: Alcoholic liver disease")
            elif ast_alt_ratio < 1:
                st.caption("⬇️ <1: Viral or drug-induced hepatitis")
            else:
                st.caption("✓ Ratio 1-2")
    
    with col2:
        st.markdown("#### Interpretation")
        
        results = {
            "ALT": alt,
            "AST": ast,
            "ALP": alp,
            "Bilirubin_Total": bili_t,
            "Bilirubin_Direct": bili_d,
            "Albumin": albumin,
            "Total_Protein": tp
        }
        
        for test_name, value in results.items():
            test_data = ALL_RANGES.get(test_name, {})
            interpretation = interpret_value(test_name, value)
            
            if "CRITICALLY" in interpretation:
                st.error(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
            elif "Low" in interpretation or "High" in interpretation:
                st.warning(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
            else:
                st.success(f"**{test_data.get('vn_name', test_name)}:** {value} - {interpretation}")
    
    # Patterns
    st.markdown("---")
    with st.expander("📊 Common LFT Patterns"):
        st.markdown("""
        **Hepatocellular Pattern (ALT, AST ⬆️⬆️):**
        - Viral hepatitis (A, B, C)
        - Drug-induced (acetaminophen, statins)
        - Ischemic hepatitis
        - Autoimmune hepatitis
        
        **Cholestatic Pattern (ALP, Bilirubin ⬆️⬆️):**
        - Bile duct obstruction
        - Primary biliary cholangitis
        - Drugs (antibiotics, steroids)
        - Infiltrative diseases
        
        **Mixed Pattern (All elevated):**
        - Sepsis
        - CHF with liver congestion
        - Cirrhosis
        """)
