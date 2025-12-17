"""
Drug Database Module - Comprehensive Drug Lookup
Main Router - Imports from drugs module
Independent module for all drug lookups (not just antibiotics)
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer

from drugs import (
    render_drug_database,
    render_interaction_checker,
    render_iv_compatibility_checker,
    render_visual_comparison,
    render_dosing_schedule_generator
)
from antibiotics import render_dosing_calculator

# Standard page setup
setup_page(
    page_title="Tra cứu thuốc",
    page_icon="💊",
    description="Cơ sở dữ liệu thuốc toàn diện, tính liều theo thận, kiểm tra tương tác, tương thích IV"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn công cụ")
    
    # Check if should switch to dosing calculator from drug detail view
    if st.session_state.get('switch_to_dosing_calculator', False):
        # Force switch to dosing calculator
        st.session_state['switch_to_dosing_calculator'] = False
        # Set function_type directly via rerun (will be handled in routing)
        if 'drug_db_function_type' not in st.session_state:
            st.session_state['drug_db_function_type'] = str("🧮 Tính liều theo eGFR/CrCl (Kháng sinh)")
    
    # Use saved function_type or default
    saved_function_type = st.session_state.get('drug_db_function_type', None)
    default_index = 0
    menu_options = [
        "💊 Tra cứu thuốc (Tất cả)",
        "🧮 Tính liều theo eGFR/CrCl (Kháng sinh)",
        "📊 So sánh thuốc trực quan",
        "📅 Tạo lịch trình liều dùng",
        "💉 Kiểm tra tương thích IV",
        "🔍 Kiểm tra tương tác thuốc"
    ]
    
    if saved_function_type and saved_function_type in menu_options:
        default_index = menu_options.index(saved_function_type)
        # Clear after using
        if 'drug_db_function_type' in st.session_state:
            del st.session_state['drug_db_function_type']
    
    function_type = st.selectbox(
        "Công cụ:",
        menu_options,
        index=default_index,
        key="drug_db_function_selector"
    )
    
    # Save current selection (ensure it's a string to avoid serialization issues)
    # Note: function_type may contain emoji, but Streamlit should handle string values
    if function_type:
        st.session_state['drug_db_function_type'] = str(function_type)
    
    st.markdown("---")
    st.info("""
    **📚 Cơ sở dữ liệu thuốc chính:**
    - Tất cả các nhóm thuốc thông dụng
    - Cardiovascular, Diabetes, Analgesic
    - Respiratory, Neurology, Psychiatry
    - Tương tác thuốc, Tương thích IV
    - Lịch trình liều dùng
    - **Tính liều theo chức năng thận (CrCl/eGFR)** cho kháng sinh
    
    **💡 Liên kết với module Kháng sinh:**
    - Đây là **entry chính** cho mọi vấn đề liên quan đến thuốc.
    - Module "💊 Kháng sinh (chuyên sâu)" cung cấp so sánh nâng cao và phác đồ điều trị.
    - TDM: Xem module "📊 TDM" để tính toán nồng độ thuốc.
    """)

# ========== MAIN CONTENT ==========

# Check if should switch to comparison from drug detail view
if st.session_state.get('switch_to_comparison', False):
    st.session_state['switch_to_comparison'] = False
    if 'drug_db_function_type' not in st.session_state:
        st.session_state['drug_db_function_type'] = str("📊 So sánh thuốc trực quan")
    # Preset drugs if available - use separate key to avoid widget conflict
    if 'preset_comparison_drugs' in st.session_state:
        st.session_state['visual_preset_drugs'] = st.session_state['preset_comparison_drugs']
        del st.session_state['preset_comparison_drugs']

# Route to appropriate function
# Use case-insensitive matching to avoid Unicode case issues
function_type_lower = function_type.lower()

if "tra cứu thuốc" in function_type_lower:
    render_drug_database()

elif "tính liều theo egfr" in function_type_lower or "crcl" in function_type_lower:
    render_dosing_calculator()

elif "so sánh thuốc trực quan" in function_type_lower:
    render_visual_comparison()

elif "lịch trình liều dùng" in function_type_lower:
    render_dosing_schedule_generator()

elif "tương thích iv" in function_type_lower:
    render_iv_compatibility_checker()

elif "tương tác" in function_type_lower:
    render_interaction_checker()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

