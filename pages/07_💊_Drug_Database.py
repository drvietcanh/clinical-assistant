"""
Drug Database Module - Comprehensive Drug Lookup
Main Router - Imports from drugs module
Independent module for all drug lookups (not just antibiotics)
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

from drugs import (
    render_drug_database,
    render_interaction_checker,
    render_iv_compatibility_checker,
    render_visual_comparison,
    render_dosing_schedule_generator
)
from antibiotics import render_dosing_calculator

# Standard page setup with mobile optimizations
setup_page(
    page_title="Cơ sở dữ liệu thuốc",
    page_icon="💊",
    description="Cơ sở dữ liệu thuốc toàn diện, tính liều theo thận, kiểm tra tương tác, tương thích IV",
    mobile_header=True
)

# Breadcrumbs
try:
    from components.mobile_page_wrapper import render_breadcrumbs
    render_breadcrumbs([
        ("Trang chủ", "/"),
        ("Thuốc", None)
    ])
except ImportError:
    pass

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Thuốc & Liều dùng")
    st.caption("**Cơ sở dữ liệu thuốc** – entry chính của nhóm *💊 Thuốc & Liều dùng*.")
    
    # Note: Sub-modules are now integrated via tabs in main content
    st.info("💡 **Lưu ý:** Các chức năng Antibiotics, Pill Identifier và TDM đã được tích hợp vào tabs ở nội dung chính.")
    
    st.markdown("---")
    st.subheader("⚙️ Chọn công cụ")
    
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
    render_info_box(
        """
        **📚 Cơ sở dữ liệu thuốc (entry chính):**
        - Tra cứu toàn bộ thuốc (tên, nhóm, dược động, lưu ý lâm sàng)
        - Tính liều theo chức năng thận (CrCl/eGFR) cho kháng sinh
        - So sánh thuốc, lịch trình liều dùng, tương tác & tương thích IV
        
        **💊 Nhóm Thuốc & Liều dùng:**
        - **Cơ sở dữ liệu thuốc (trang hiện tại)**
        - **Kháng sinh (chuyên sâu)**: so sánh, phác đồ, stewardship
        - **TDM - Theo dõi nồng độ thuốc**: vancomycin, aminoglycoside, thuốc độc hẹp
        
        **💉 Vắc xin & lịch tiêm:** xem module **\"💉 Tiêm chủng và Vắc xin\"** trong nhóm Tiêm chủng.
        """,
        type="info",
        title="Thông tin Module"
    )

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

# Main tabs for integrated sub-modules
tab1, tab2, tab3, tab4 = st.tabs([
    "💊 Database", 
    "💊 Antibiotics", 
    "💊 Pill Identifier", 
    "📊 TDM"
])

with tab1:
    # Main Drug Database functionality
    # Route to appropriate function
    # Use case-insensitive matching to avoid Unicode case issues
    function_type_lower = function_type.lower()

    if "tra cứu thuốc" in function_type_lower:
        # Master-Detail Layout: List on left, Detail on right
        # Get selected drug from session state
        selected_drug_name = st.session_state.get('view_drug_name') or st.session_state.get('selected_drug')
        
        # Add CSS for responsive layout
        st.markdown("""
        <style>
        @media (max-width: 768px) {
            /* Mobile: Stack columns vertically */
            .drug-detail-column {
                margin-top: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # For desktop with drug selected, use 2-column layout
        # For mobile or when no drug selected, use single column
        if selected_drug_name:
            # Two-column layout (desktop with drug selected)
            col_list, col_detail = st.columns([3, 2])
            
            with col_list:
                render_drug_database()
            
            with col_detail:
                st.markdown("### 📖 Chi tiết thuốc")
                try:
                    from drugs.drug_database import DRUG_DATABASE
                    from drugs.drug_info_components.detail_view import display_drug_info
                    
                    # Try case-insensitive lookup
                    drug_found = selected_drug_name in DRUG_DATABASE
                    drug_name_normalized = selected_drug_name
                    
                    if not drug_found:
                        for db_drug_name in DRUG_DATABASE.keys():
                            if str(db_drug_name).lower() == str(selected_drug_name).lower():
                                drug_name_normalized = db_drug_name
                                drug_found = True
                                break
                    
                    if drug_found and drug_name_normalized in DRUG_DATABASE:
                        drug_data = DRUG_DATABASE[drug_name_normalized]
                        # Add clear button
                        if st.button("❌ Đóng", key="close_drug_detail", use_container_width=True):
                            if 'view_drug_name' in st.session_state:
                                del st.session_state['view_drug_name']
                            if 'selected_drug' in st.session_state:
                                del st.session_state['selected_drug']
                            st.rerun()
                        display_drug_info(drug_name_normalized, drug_data, show_header=True)
                    else:
                        st.warning(f"Không tìm thấy thuốc: {selected_drug_name}")
                        if st.button("🔙 Quay lại", key="back_from_detail", use_container_width=True):
                            if 'view_drug_name' in st.session_state:
                                del st.session_state['view_drug_name']
                            if 'selected_drug' in st.session_state:
                                del st.session_state['selected_drug']
                            st.rerun()
                except Exception as e:
                    st.error(f"Lỗi hiển thị chi tiết: {str(e)}")
        else:
            # Single column layout when no drug selected
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

with tab2:
    # Antibiotics sub-module
    st.info("💊 **Kháng sinh (chuyên sâu)** - So sánh & phác đồ điều trị kháng sinh")
    st.markdown("""
    Chức năng Antibiotics cho phép bạn:
    - So sánh các kháng sinh theo nhóm và phổ kháng khuẩn
    - Xem phác đồ điều trị kháng sinh theo bệnh lý
    - Tính liều kháng sinh theo chức năng thận
    - Tư vấn về antibiotic stewardship
    """)
    
    # Show quick access to antibiotics page
    if st.button("Mở trang Antibiotics đầy đủ", use_container_width=True, type="primary"):
        st.switch_page("pages/02_💊_Antibiotics.py")
    
    # Also show the dosing calculator here
    st.markdown("---")
    st.markdown("### 🧮 Tính liều kháng sinh theo eGFR/CrCl")
    render_dosing_calculator()

with tab3:
    # Pill Identifier sub-module
    st.info("💊 **Pill Identifier** - Nhận diện thuốc qua đặc điểm vật lý")
    st.markdown("""
    Chức năng Pill Identifier cho phép bạn:
    - Nhận diện thuốc qua màu sắc, hình dạng, ký hiệu
    - Tìm kiếm thuốc theo đặc điểm vật lý
    - Xem thông tin chi tiết về thuốc
    """)
    
    if st.button("Mở Pill Identifier", use_container_width=True, type="primary"):
        st.switch_page("pages/21_💊_Pill_Identifier.py")
    
    # Try to import and show pill identifier if available
    try:
        from pill_identifier import render_pill_identifier_search
        st.markdown("---")
        render_pill_identifier_search()
    except ImportError:
        st.info("Vui lòng truy cập trang Pill Identifier riêng biệt để sử dụng đầy đủ chức năng.")

with tab4:
    # TDM sub-module
    st.info("📊 **TDM - Theo dõi nồng độ thuốc** - Tính toán và theo dõi nồng độ thuốc")
    st.markdown("""
    Chức năng TDM cho phép bạn:
    - Tính toán nồng độ thuốc (Vancomycin, Aminoglycoside, etc.)
    - Theo dõi nồng độ thuốc trong máu
    - Điều chỉnh liều dựa trên nồng độ
    """)
    
    if st.button("Mở trang TDM đầy đủ", use_container_width=True, type="primary"):
        st.switch_page("pages/08_📊_TDM.py")
    
    # Try to import and show TDM calculator if available
    try:
        from tdm import render_tdm_calculator
        st.markdown("---")
        render_tdm_calculator()
    except ImportError:
        st.info("Vui lòng truy cập trang TDM riêng biệt để sử dụng đầy đủ chức năng.")

# ========== FOOTER ==========
render_standard_footer(disclaimer=False)

