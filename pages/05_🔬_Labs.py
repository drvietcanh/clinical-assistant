"""
Labs Module - Laboratory Values & Interpretation
Main Router - Lab panels and reference ranges
"""

import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from labs import (
    render_cbc,
    render_bmp,
    render_cmp,
    render_lft,
    render_lipid,
    render_cardiac_markers,
    render_coag,
    render_thyroid,
    render_abg
)

st.set_page_config(page_title="Lab Values - Clinical Assistant", page_icon="🔬", layout="wide")

# ========== HEADER ==========
st.title("🔬 Lab Values & Interpretation")
st.markdown("Tra cứu giá trị bình thường và giải thích kết quả xét nghiệm")
st.markdown("---")

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Chọn Panel")
    
    lab_panel = st.selectbox(
        "Lab Panel:",
        [
            "🩸 CBC - Complete Blood Count",
            "🧪 BMP - Basic Metabolic Panel",
            "🧪 CMP - Comprehensive Metabolic Panel",
            "🫀 LFT - Liver Function Tests",
            "💊 Lipid Panel",
            "❤️ Cardiac Markers",
            "🩸 Coagulation Panel",
            "🦋 Thyroid Function Tests",
            "💨 ABG - Arterial Blood Gas"
        ]
    )
    
    st.markdown("---")
    
    st.info("""
    **📚 Features:**
    - Normal ranges
    - Critical values
    - Interpretation guide
    - Common patterns
    
    **💡 Tip:**
    Enter patient values to see automatic interpretation
    """)
    
    st.markdown("---")
    st.caption("**Version:** 1.0")
    st.caption("**Updated:** 2025-10-29")

# ========== MAIN CONTENT ==========

st.info(f"""
**Lab Panel:** {lab_panel.split(' - ')[1] if ' - ' in lab_panel else lab_panel}

**Instructions:** 
1. Enter patient lab values
2. View automatic interpretation
3. Check reference ranges
""")

st.markdown("---")

# Route to appropriate panel
if "CBC" in lab_panel:
    render_cbc()

elif "BMP" in lab_panel and "CMP" not in lab_panel:
    render_bmp()

elif "CMP" in lab_panel:
    render_cmp()

elif "LFT" in lab_panel or "Liver" in lab_panel:
    render_lft()

elif "Lipid" in lab_panel:
    render_lipid()

elif "Cardiac" in lab_panel:
    render_cardiac_markers()

elif "Coag" in lab_panel:
    render_coag()

elif "Thyroid" in lab_panel:
    render_thyroid()

elif "ABG" in lab_panel:
    render_abg()

# ========== FOOTER ==========
st.markdown("---")

st.warning("""
**⚠️ Important Notes:**
- Reference ranges may vary by laboratory
- Always compare with your local lab's ranges
- Critical values require immediate clinical correlation
- This tool is for reference only - not a substitute for clinical judgment
""")

st.caption("📊 Lab values based on standard reference ranges from major clinical laboratories")
st.caption("🗂️ Modular architecture - Easy to add new panels")

