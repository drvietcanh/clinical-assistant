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
        # Full-width Detail View Layout (Epocrates/Micromedex style)
        # Get selected drug from session state
        selected_drug_name = st.session_state.get('view_drug_name') or st.session_state.get('selected_drug')
        
        # Add CSS for responsive layout and full-width detail view
        st.markdown("""
        <style>
        /* Full-width detail view styling */
        .drug-detail-container {
            width: 100%;
            max-width: 100%;
        }
        
        /* Improve spacing for tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px;
            flex-wrap: wrap;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 10px 16px;
            font-size: 0.95em;
            white-space: nowrap;
        }
        
        /* Better card spacing */
        .drug-info-card {
            margin-bottom: 20px;
        }
        
        /* Responsive design for mobile */
        @media (max-width: 768px) {
            .drug-detail-container {
                padding: 10px;
            }
            
            .drug-detail-header {
                padding: 15px !important;
            }
            
            .drug-detail-header h2 {
                font-size: 1.5em !important;
            }
            
            /* Scrollable tabs with visual indicator */
            .stTabs [data-baseweb="tab-list"] {
                gap: 4px;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                scrollbar-width: thin;
                position: relative;
            }
            
            /* Visual indicator for scrollable tabs */
            .stTabs [data-baseweb="tab-list"]::after {
                content: '→';
                position: absolute;
                right: 0;
                top: 50%;
                transform: translateY(-50%);
                background: linear-gradient(to right, transparent, rgba(255,255,255,0.9));
                padding: 0 10px;
                pointer-events: none;
                color: #666;
                font-size: 1.2em;
            }
            
            .stTabs [data-baseweb="tab"] {
                padding: 10px 14px;
                font-size: 0.85em;
                min-width: auto;
                white-space: nowrap;
            }
            
            /* Stack quick actions on mobile */
            .quick-actions-container {
                flex-direction: column;
            }
            
            /* Better spacing on mobile */
            .drug-info-section {
                margin-bottom: 20px;
            }
            
            /* Improve button sizes on mobile - larger touch targets */
            button {
                min-height: 44px;
                font-size: 0.95em;
                padding: 10px 16px;
            }
            
            /* Larger input fields on mobile */
            input, select, textarea {
                font-size: 16px; /* Prevents zoom on iOS */
                min-height: 44px;
            }
            
            /* Better card spacing on mobile */
            .drug-info-card {
                margin-bottom: 15px;
                padding: 12px;
            }
        }
        
        /* Tablet optimization */
        @media (min-width: 769px) and (max-width: 1024px) {
            .stTabs [data-baseweb="tab"] {
                padding: 10px 14px;
                font-size: 0.9em;
            }
        }
        
        /* Better print styles */
        @media print {
            .stTabs [data-baseweb="tab-list"] {
                display: none;
            }
            
            .drug-detail-header {
                page-break-after: avoid;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Full-width detail view when drug is selected
        if selected_drug_name:
            # Back button and navigation bar
            col_back, col_title, col_actions = st.columns([1, 3, 1])
            
            with col_back:
                if st.button("← Quay lại", key="back_to_list", use_container_width=True, type="secondary"):
                    # Use pop() instead of del for safer session state management
                    st.session_state.pop('view_drug_name', None)
                    st.session_state.pop('selected_drug', None)
                    st.rerun()
            
            with col_title:
                st.markdown("### 📖 Chi tiết thuốc")
            
            with col_actions:
                st.empty()  # Reserved for future quick actions
            
            st.markdown("---")
            
            # Full-width detail view
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
                    # Display full-width drug info
                    display_drug_info(drug_name_normalized, drug_data, show_header=True)
                    
                    # Navigation hint at bottom
                    st.markdown("---")
                    st.info("💡 Tìm kiếm thuốc khác? Sử dụng nút '← Quay lại' ở trên hoặc chọn thuốc từ danh sách")
                else:
                    st.warning(f"Không tìm thấy thuốc: {selected_drug_name}")
                    if st.button("🔙 Quay lại danh sách", key="back_from_detail", use_container_width=True):
                        st.session_state.pop('view_drug_name', None)
                        st.session_state.pop('selected_drug', None)
                        st.rerun()
            except ImportError as e:
                st.error(f"Lỗi import module: {str(e)}")
                st.info("💡 Vui lòng kiểm tra lại cấu hình hệ thống")
                if st.button("🔙 Quay lại", key="back_from_import_error", use_container_width=True):
                    st.session_state.pop('view_drug_name', None)
                    st.session_state.pop('selected_drug', None)
                    st.rerun()
            except KeyError as e:
                st.error(f"Lỗi truy cập dữ liệu: Không tìm thấy key '{str(e)}' trong database")
                st.info("💡 Thuốc này có thể thiếu một số thông tin")
                if st.button("🔙 Quay lại", key="back_from_key_error", use_container_width=True):
                    st.session_state.pop('view_drug_name', None)
                    st.session_state.pop('selected_drug', None)
                    st.rerun()
            except Exception as e:
                import traceback
                st.error(f"Lỗi hiển thị chi tiết: {str(e)}")
                with st.expander("🔍 Chi tiết lỗi (dành cho developer)", expanded=False):
                    st.code(traceback.format_exc())
                if st.button("🔙 Quay lại", key="back_from_error", use_container_width=True):
                    st.session_state.pop('view_drug_name', None)
                    st.session_state.pop('selected_drug', None)
                    st.rerun()
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
    
    # Handle switch to interaction checker from quick actions
    if st.session_state.get('switch_to_interaction', False):
        st.session_state['switch_to_interaction'] = False
        if 'drug_db_function_type' not in st.session_state:
            st.session_state['drug_db_function_type'] = str("🔍 Kiểm tra tương tác thuốc")
        st.rerun()

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

