"""
Labs & Calculators Module - Combined
Main Router - Lab panels, reference ranges, and clinical calculators
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

# Import lab panels
from labs import (
    render_cbc,
    render_bmp,
    render_cmp,
    render_lft,
    render_lipid,
    render_cardiac_markers,
    render_coag,
    render_thyroid,
    render_abg,
    render_trend_analysis,
    render_panel_calculator
)

# Import calculators
from scores.metabolism.bmi_ibw_bsa import render as render_bmi_ibw_bsa
from scores.metabolism.osmolality import render as render_osmolality
from scores.metabolism.anion_gap import render as render_anion_gap
from scores.metabolism.corrected_calcium import render as render_corrected_calcium
from scores.metabolism.fena import render as render_fena
from scores.metabolism.hba1c_eag import render as render_hba1c_eag
from scores.metabolism.winter_formula import render as render_winter_formula
from scores.metabolism.free_t4_index import render as render_free_t4_index
from scores.nephrology.egfr import render as render_egfr

# Standard page setup
setup_page(
    page_title="Labs & Calculators",
    page_icon="🔬",
    description="Tra cứu giá trị xét nghiệm, giải thích kết quả và tính toán công thức lâm sàng"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("📋 Chọn Loại")
    
    category = st.radio(
        "Loại công cụ:",
        [
            "🧮 Calculators",
            "🔬 Lab Panels",
            "📈 Lab Enhancement"
        ],
        index=0,
        help="Calculators: Tính toán công thức lâm sàng\nLab Panels: Tra cứu và giải thích giá trị xét nghiệm\nLab Enhancement: Trend analysis và panel calculator"
    )
    
    st.markdown("---")
    
    if category == "🧮 Calculators":
        st.subheader("🧮 Chọn Calculator")
        
        calculator_type = st.selectbox(
            "Calculator:",
            [
                "📏 BMI | IBW | BSA",
                "🧪 eGFR/GFR Calculator",
                "💧 Osmolality & Gap",
                "⚖️ Anion Gap",
                "🦴 Corrected Calcium",
                "🧪 FENa",
                "📊 HbA1c ↔ eAG",
                "🌡️ Winter Formula",
                "🔬 Free T4 Index"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.info("""
        **💡 Các calculator thông dụng:**
        
        **Cơ thể:**
        - BMI, IBW, BSA
        
        **Chức năng thận:**
        - eGFR (chẩn đoán CKD)
        
        **Xét nghiệm:**
        - Osmolality, Anion Gap
        - Corrected Ca, FENa
        - HbA1c, T4 Index
        
        **💊 Liên Quan:** Các calculator này cần thiết cho điều chỉnh liều thuốc
        """)
    
    elif category == "🔬 Lab Panels":
        st.subheader("📋 Chọn Panel")
        
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
            ],
            label_visibility="collapsed"
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
    
    elif category == "📈 Lab Enhancement":
        st.subheader("📈 Chọn Tính Năng")
        
        enhancement_type = st.selectbox(
            "Tính năng:",
            [
                "📈 Lab Trend Analysis",
                "🧮 Lab Panel Calculator"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.info("""
        **📈 Lab Enhancement Features:**
        
        **Trend Analysis:**
        - Serial lab monitoring
        - Trend visualization
        - Pattern recognition
        
        **Panel Calculator:**
        - Multi-lab interpretation
        - Auto-pattern detection
        - Critical value alerts
        """)
    
    st.markdown("---")
    st.caption("**Version:** 2.0")
    st.caption("**Updated:** 2025-01-31")

# ========== MAIN CONTENT ==========

# Display category info
if category == "🧮 Calculators":
    st.info(f"""
    **Calculator:** {calculator_type}
    
    **Hướng dẫn:**
    1. Nhập các giá trị đầu vào
    2. Xem kết quả tính toán
    3. Kiểm tra các panel xét nghiệm Liên Quan để tra cứu khoảng giá trị tham chiếu
    """)
    
    # Quick Links to related lab panels
    st.markdown("### 🔗 Liên Quan - Lab Panels")
    link_cols = st.columns(5)
    
    if "eGFR" in calculator_type or "GFR" in calculator_type:
        with link_cols[0]:
            if st.button("📋 BMP (Creatinine)", use_container_width=True):
                st.session_state.show_panel = "bmp"
    
    if "Anion Gap" in calculator_type:
        with link_cols[1]:
            if st.button("📋 BMP (Na, Cl, HCO3)", use_container_width=True):
                st.session_state.show_panel = "bmp"
    
    if "Corrected" in calculator_type or "Calcium" in calculator_type:
        with link_cols[2]:
            if st.button("📋 CMP (Ca, Albumin)", use_container_width=True):
                st.session_state.show_panel = "cmp"
    
    if "FENa" in calculator_type:
        with link_cols[3]:
            if st.button("📋 BMP (Na, Creatinine)", use_container_width=True):
                st.session_state.show_panel = "bmp"
    
    if "T4" in calculator_type or "Free" in calculator_type:
        with link_cols[4]:
            if st.button("📋 Thyroid Panel", use_container_width=True):
                st.session_state.show_panel = "thyroid"
    
    st.markdown("---")
    
    # Handle show panel request
    if hasattr(st.session_state, 'show_panel'):
        panel = st.session_state.show_panel
        st.markdown("### 🔬 Lab Panel Liên Quan")
        
        if panel == "bmp":
            render_bmp()
        elif panel == "cmp":
            render_cmp()
        elif panel == "thyroid":
            render_thyroid()
        
        del st.session_state.show_panel
    
    # Route to appropriate calculator
    if "BMI" in calculator_type or "IBW" in calculator_type or "BSA" in calculator_type:
        render_bmi_ibw_bsa()
    elif "eGFR" in calculator_type or "GFR" in calculator_type:
        render_egfr()
    elif "Osmolality" in calculator_type:
        render_osmolality()
    elif "Anion Gap" in calculator_type:
        render_anion_gap()
    elif "Corrected" in calculator_type or "Calcium" in calculator_type:
        render_corrected_calcium()
    elif "FENa" in calculator_type:
        render_fena()
    elif "HbA1c" in calculator_type or "eAG" in calculator_type:
        render_hba1c_eag()
    elif "Winter" in calculator_type:
        render_winter_formula()
    elif "T4" in calculator_type or "Free" in calculator_type:
        render_free_t4_index()

elif category == "🔬 Lab Panels":
    st.info(f"""
    **Lab Panel:** {lab_panel.split(' - ')[1] if ' - ' in lab_panel else lab_panel}
    
    **Hướng dẫn:** 
    1. Nhập giá trị xét nghiệm của bệnh nhân
    2. Xem giải thích tự động
    3. Kiểm tra khoảng giá trị tham chiếu
    4. Sử dụng Quick Actions bên dưới để tính toán các giá trị Liên Quan
    """)
    
    # Quick Actions section (for integration)
    st.markdown("### 🔗 Quick Actions")
    quick_cols = st.columns(4)
    
    if "BMP" in lab_panel or "CMP" in lab_panel:
        with quick_cols[0]:
            if st.button("🧪 Tính eGFR", use_container_width=True):
                st.session_state.quick_action = "egfr"
        with quick_cols[1]:
            if st.button("⚖️ Tính Anion Gap", use_container_width=True):
                st.session_state.quick_action = "anion_gap"
        with quick_cols[2]:
            if st.button("💧 Tính Osmolality", use_container_width=True):
                st.session_state.quick_action = "osmolality"
    
    if "CMP" in lab_panel:
        with quick_cols[3]:
            if st.button("🦴 Tính Corrected Ca", use_container_width=True):
                st.session_state.quick_action = "corrected_ca"
    
    if "Thyroid" in lab_panel:
        with quick_cols[0]:
            if st.button("🔬 Tính Free T4 Index", use_container_width=True):
                st.session_state.quick_action = "free_t4"
    
    st.markdown("---")
    
    # Route to appropriate lab panel
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
    
    # Handle quick actions
    if hasattr(st.session_state, 'quick_action'):
        action = st.session_state.quick_action
        st.markdown("---")
        st.markdown("### 🧮 Calculator từ Quick Action")
        
        if action == "egfr":
            render_egfr()
        elif action == "anion_gap":
            render_anion_gap()
        elif action == "osmolality":
            render_osmolality()
        elif action == "corrected_ca":
            render_corrected_calcium()
        elif action == "free_t4":
            render_free_t4_index()
        
        # Clear quick action
        del st.session_state.quick_action

elif category == "📈 Lab Enhancement":
    if "Trend Analysis" in enhancement_type:
        render_trend_analysis()
    elif "Panel Calculator" in enhancement_type:
        render_panel_calculator()

# ========== FOOTER ==========
render_standard_footer(disclaimer=True)

# Additional lab-specific warning
st.warning("""
**⚠️ Lưu Ý Quan Trọng về Lab:**
- Khoảng giá trị tham chiếu có thể khác nhau giữa các phòng xét nghiệm
- Luôn so sánh với khoảng giá trị của phòng xét nghiệm địa phương bạn
- Giá trị nguy kịch cần đối chiếu lâm sàng ngay lập tức
""")

