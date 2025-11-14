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
    page_title="Tra Cứu Thuốc",
    page_icon="💊",
    description="Cơ sở dữ liệu thuốc toàn diện, tính liều theo thận, kiểm tra tương tác, tương thích IV"
)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("⚙️ Chọn Công Cụ")
    
    # Check if should switch to dosing calculator from drug detail view
    if st.session_state.get('switch_to_dosing_calculator', False):
        # Force switch to dosing calculator
        st.session_state['switch_to_dosing_calculator'] = False
        # Set function_type directly via rerun (will be handled in routing)
        if 'drug_db_function_type' not in st.session_state:
            st.session_state['drug_db_function_type'] = str("🧮 Tính Liều Theo eGFR/CrCl (Kháng Sinh)")
    
    # Use saved function_type or default
    saved_function_type = st.session_state.get('drug_db_function_type', None)
    default_index = 0
    menu_options = [
        "💊 Tra Cứu Thuốc (Tất Cả)",
        "🧮 Tính Liều Theo eGFR/CrCl (Kháng Sinh)",
        "📊 So Sánh Thuốc Trực Quan",
        "📅 Tạo Lịch Trình Liều Dùng",
        "💉 Kiểm Tra Tương Thích IV",
        "🔍 Kiểm Tra Tương Tác Thuốc"
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
    **📚 Cơ sở dữ liệu:**
    - Tất cả các nhóm thuốc thông dụng
    - Cardiovascular, Diabetes, Analgesic
    - Respiratory, Neurology, Psychiatry
    - Tương tác thuốc, Tương thích IV
    - Lịch trình liều dùng
    - **Tính liều theo chức năng thận (CrCl/eGFR)**
    
    **💡 Lưu ý:**
    - Tính liều theo thận hiện tại dành cho **kháng sinh**
    - TDM: Xem module "📊 TDM" để tính toán nồng độ thuốc
    """)

# ========== MAIN CONTENT ==========

# Check if should switch to comparison from drug detail view
if st.session_state.get('switch_to_comparison', False):
    st.session_state['switch_to_comparison'] = False
    if 'drug_db_function_type' not in st.session_state:
        st.session_state['drug_db_function_type'] = str("📊 So Sánh Thuốc Trực Quan")
    # Preset drugs if available
    if 'preset_comparison_drugs' in st.session_state:
        st.session_state['visual_selected_drugs'] = st.session_state['preset_comparison_drugs']
        del st.session_state['preset_comparison_drugs']

# Route to appropriate function
if "Tra Cứu Thuốc" in function_type:
    render_drug_database()

elif "Tính Liều Theo eGFR" in function_type or "CrCl" in function_type:
    render_dosing_calculator()

elif "So Sánh Thuốc Trực Quan" in function_type:
    render_visual_comparison()

elif "Lịch Trình Liều Dùng" in function_type:
    render_dosing_schedule_generator()

elif "Tương Thích IV" in function_type:
    render_iv_compatibility_checker()

elif "Tương Tác" in function_type:
    render_interaction_checker()

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

