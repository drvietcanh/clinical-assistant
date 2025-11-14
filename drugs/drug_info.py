"""
Drug Information Display Components
UI components for displaying drug information similar to antibiotics
"""

import streamlit as st
import pandas as pd
from .drug_database import DRUG_DATABASE

# Check if drug is antibiotic
try:
    from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
except ImportError:
    ANTIBIOTICS_DATABASE = {}


def render_compact_drug_card(drug_name, drug_data, key_prefix="", search_query=""):
    """Render a compact drug card in list view with optional search highlighting"""
    from .search import highlight_search_term
    
    vn_name = drug_data.get('vietnamese_name', '')
    group = drug_data.get('group', 'Unknown')
    admin = drug_data.get('administration', [])
    admin_str = " / ".join(admin) if admin else "N/A"
    
    # Highlight search terms if query provided
    highlighted_name = highlight_search_term(drug_name, search_query) if search_query else drug_name
    highlighted_vn_name = highlight_search_term(vn_name, search_query) if search_query and vn_name else vn_name
    
    # Group badge color
    group_colors = {
        "Cardiovascular": "#E91E63",
        "Diabetes": "#9C27B0",
        "Gastrointestinal": "#FF9800",
        "Analgesic": "#F44336",
        "Respiratory": "#00BCD4",
        "Neurology": "#3F51B5",
        "Psychiatry": "#673AB7",
    }
    
    # Get color based on group prefix
    badge_color = "#666"
    for group_key, color in group_colors.items():
        if group_key.lower() in group.lower():
            badge_color = color
            break
    
    group_badge = f'<span style="background-color: {badge_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; margin-left: 8px;">{group.split(" - ")[0] if " - " in group else group}</span>'
    
    # Compact card
    card_html = f"""
    <div style='
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 12px 15px;
        margin: 8px 0;
        transition: all 0.2s;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    '>
        <div style='display: flex; justify-content: space-between; align-items: start;'>
            <div style='flex: 1;'>
                <div style='display: flex; align-items: center; margin-bottom: 6px;'>
                    <strong style='color: #1976D2; font-size: 1.05em; margin-right: 8px;'>{highlighted_name}</strong>
                    {group_badge}
                </div>
                {f"<div style='color: #666; font-size: 0.9em; margin-bottom: 4px;'>{highlighted_vn_name}</div>" if vn_name else ""}
                <div style='color: #888; font-size: 0.85em;'>{admin_str} | {group}</div>
            </div>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Button row
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        # Sanitize drug_name for key (remove special characters that might cause issues)
        safe_drug_name = str(drug_name).replace(" ", "_").replace("-", "_").replace("/", "_")
        view_key = f"{key_prefix}view_{safe_drug_name}" if key_prefix else f"view_{safe_drug_name}"
        
        if st.button("📖 Xem chi tiết", key=view_key, use_container_width=True):
            # Use consistent keys without key_prefix for main selection
            st.session_state["selected_drug"] = str(drug_name)  # Ensure it's a string
            st.session_state["show_detail"] = True
            st.rerun()
    
    with col2:
        # Add to comparison button
        compare_key = f"{key_prefix}compare_{safe_drug_name}" if key_prefix else f"compare_{safe_drug_name}"
        if st.button("🔄 So sánh", key=compare_key, use_container_width=True):
            # Add to comparison list
            if 'drug_comparison_list' not in st.session_state:
                st.session_state['drug_comparison_list'] = []
            if drug_name not in st.session_state['drug_comparison_list']:
                st.session_state['drug_comparison_list'].append(drug_name)
                # Limit to 5 drugs
                if len(st.session_state['drug_comparison_list']) > 5:
                    st.session_state['drug_comparison_list'] = st.session_state['drug_comparison_list'][-5:]
                st.success(f"✅ Đã thêm {drug_name} vào danh sách so sánh")
                st.rerun()
            else:
                st.info(f"ℹ️ {drug_name} đã có trong danh sách so sánh")
    
    with col3:
        st.empty()


def _render_quick_facts_box(drug_data):
    """Render quick facts box with key information"""
    facts = []
    
    # Pregnancy
    if 'pregnancy' in drug_data:
        preg_icons = {"A": "🟢", "B": "🟡", "C": "🟠", "D": "🔴", "X": "⚫"}
        preg = drug_data['pregnancy']
        facts.append(f"**Thai kỳ:** {preg_icons.get(preg, '')} {preg}")
    
    # Lactation (if available)
    if 'lactation' in drug_data:
        facts.append(f"**Cho con bú:** {drug_data['lactation']}")
    
    # Half-life
    if 'pharmacokinetics' in drug_data and 'half_life' in drug_data['pharmacokinetics']:
        half_life = drug_data['pharmacokinetics']['half_life']
        facts.append(f"**Half-life:** {half_life}")
    
    # Monitoring summary
    if 'monitoring' in drug_data:
        monitoring_list = drug_data['monitoring']
        if isinstance(monitoring_list, list) and len(monitoring_list) > 0:
            # Take first 2-3 items for summary
            summary = ", ".join(monitoring_list[:3])
            if len(monitoring_list) > 3:
                summary += "..."
            facts.append(f"**Theo dõi:** {summary}")
    
    # Administration
    if 'administration' in drug_data:
        admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️", "SC": "💉", "Rectal": "📦"}
        admin_display = " / ".join([f"{admin_icons.get(route, '')} {route}" for route in drug_data['administration']])
        facts.append(f"**Đường dùng:** {admin_display}")
    
    if not facts:
        return
    
    # Render quick facts box
    facts_html = " | ".join(facts)
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border-left: 4px solid #0EA5E9;
        padding: 15px 20px;
        border-radius: 8px;
        margin: 15px 0;
        box-shadow: 0 2px 4px rgba(14, 165, 233, 0.1);
    '>
        <h4 style='margin: 0 0 10px 0; color: #0369a1; font-size: 1.1em;'>📊 Quick Facts</h4>
        <div style='color: #0c4a6e; font-size: 0.95em; line-height: 1.8;'>
            {facts_html}
        </div>
    </div>
    """, unsafe_allow_html=True)


def _render_black_box_warning(warning_text):
    """Render black box warning with prominent styling"""
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border: 2px solid #dc2626;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(220, 38, 38, 0.2);
    '>
        <h3 style='color: #dc2626; margin: 0 0 10px 0; font-size: 1.2em; display: flex; align-items: center;'>
            <span style='font-size: 1.5em; margin-right: 10px;'>⚠️</span>
            BLACK BOX WARNING
        </h3>
        <p style='color: #991b1b; font-size: 1.05em; margin: 0; line-height: 1.6; font-weight: 500;'>
            {warning_text}
        </p>
    </div>
    """, unsafe_allow_html=True)


def display_drug_info(drug_name, drug_data):
    """Display detailed drug information in tab-based format (Epocrates style)"""
    
    # Header with drug name
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    '>
        <h2 style='margin: 0; color: white; font-size: 1.8em;'>💊 {drug_name}</h2>
        {f"<p style='margin: 8px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1em;'>{drug_data.get('vietnamese_name', '')}</p>" if drug_data.get('vietnamese_name') else ""}
    </div>
    """, unsafe_allow_html=True)
    
    # Tab-based layout
    tab_overview, tab_dosing, tab_safety, tab_interactions, tab_monitoring = st.tabs([
        "📋 Overview", "💊 Dosing", "⚠️ Safety", "🔗 Interactions", "📊 Monitoring"
    ])
    
    # ========== OVERVIEW TAB ==========
    with tab_overview:
        # Black Box Warning (show first if exists)
        if 'black_box_warnings' in drug_data:
            _render_black_box_warning(drug_data['black_box_warnings'])
        
        # Quick Facts Box
        _render_quick_facts_box(drug_data)
        
        # Basic Info
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if 'vietnamese_name' in drug_data:
                st.markdown(f"**📝 Tên biệt dược:** {drug_data['vietnamese_name']}")
            
            if 'group' in drug_data:
                st.markdown(f"**🏷️ Nhóm:** {drug_data['group']}")
        
        with col2:
            if 'administration' in drug_data:
                admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️", "SC": "💉", "Rectal": "📦"}
                admin_display = " / ".join([f"{admin_icons.get(route, '')} {route}" for route in drug_data['administration']])
                st.markdown(f"**💊 Đường dùng:** {admin_display}")
            
            if 'pregnancy' in drug_data:
                preg_icons = {"A": "🟢", "B": "🟡", "C": "🟠", "D": "🔴", "X": "⚫"}
                preg = drug_data['pregnancy']
                st.markdown(f"**🤰 Thai kỳ:** {preg_icons.get(preg, '')} {preg}")
        
        st.markdown("---")
        
        # Indications
        if 'indications' in drug_data:
            st.markdown("### 📋 Chỉ định:")
            for ind in drug_data['indications']:
                st.markdown(f"- {ind}")
        
        # Mechanism of Action
        if 'mechanism_of_action' in drug_data:
            st.markdown("---")
            st.markdown("### 🔬 Cơ chế tác động:")
            st.info(drug_data['mechanism_of_action'])
        
        # Pharmacokinetics
        if 'pharmacokinetics' in drug_data:
            st.markdown("---")
            st.markdown("### 📈 Dược động học (Pharmacokinetics):")
            pk = drug_data['pharmacokinetics']
            pk_data = []
            if 'half_life' in pk:
                pk_data.append({"Thông số": "Thời gian bán hủy", "Giá trị": pk['half_life']})
            if 'onset' in pk:
                pk_data.append({"Thông số": "Thời gian bắt đầu tác dụng", "Giá trị": pk['onset']})
            if 'duration' in pk:
                pk_data.append({"Thông số": "Thời gian tác dụng", "Giá trị": pk['duration']})
            if 'protein_binding' in pk:
                pk_data.append({"Thông số": "Gắn protein", "Giá trị": pk['protein_binding']})
            if 'clearance' in pk:
                pk_data.append({"Thông số": "Thanh thải", "Giá trị": pk['clearance']})
            
            if pk_data:
                st.dataframe(pd.DataFrame(pk_data), use_container_width=True, hide_index=True)
        
        # Storage
        if 'storage' in drug_data:
            st.markdown("---")
            st.markdown("### 📦 Bảo quản:")
            st.info(drug_data['storage'])
    
    # ========== DOSING TAB ==========
    with tab_dosing:
        # Adult Dosing
        if 'dosage' in drug_data:
            st.markdown("### 👤 Liều dùng người lớn:")
            dosage = drug_data['dosage']
            adult_doses = []
            
            if 'adult_htn' in dosage:
                adult_doses.append(f"**Tăng huyết áp:** {dosage['adult_htn']}")
            if 'adult_po' in dosage:
                adult_doses.append(f"**Uống (PO):** {dosage['adult_po']}")
            if 'adult_iv' in dosage:
                adult_doses.append(f"**Tiêm tĩnh mạch (IV):** {dosage['adult_iv']}")
            if 'adult_standard' in dosage:
                adult_doses.append(f"**Liều chuẩn:** {dosage['adult_standard']}")
            if 'adult_loading' in dosage:
                adult_doses.append(f"**Liều nạp:** {dosage['adult_loading']}")
            if 'adult_maintenance' in dosage:
                adult_doses.append(f"**Liều duy trì:** {dosage['adult_maintenance']}")
            
            if adult_doses:
                col1, col2 = st.columns(2)
                mid = len(adult_doses) // 2 + len(adult_doses) % 2
                for i, dose in enumerate(adult_doses[:mid]):
                    with col1:
                        st.info(dose)
                for i, dose in enumerate(adult_doses[mid:], start=mid):
                    with col2:
                        st.info(dose)
            
            if 'notes' in dosage:
                st.caption(f"💡 {dosage['notes']}")
        
        # Pediatric Dosing
        if 'dosage' in drug_data and 'pediatric' in drug_data['dosage']:
            st.markdown("---")
            st.markdown("### 👶 Liều dùng trẻ em:")
            ped_dose = drug_data['dosage']['pediatric']
            st.info(ped_dose)
        
        # Renal adjustment - Table format
        if 'renal_adjustment' in drug_data:
            st.markdown("---")
            st.markdown("### 🫘 Điều chỉnh theo chức năng thận:")
            
            renal = drug_data['renal_adjustment']
            renal_data = []
            
            if 'normal' in renal:
                renal_data.append({"CrCl (mL/min)": "≥ 60", "Điều chỉnh": renal['normal']})
            if '30_60' in renal:
                renal_data.append({"CrCl (mL/min)": "30-60", "Điều chỉnh": renal['30_60']})
            if '15_30' in renal:
                renal_data.append({"CrCl (mL/min)": "15-30", "Điều chỉnh": renal['15_30']})
            if 'under_30' in renal:
                renal_data.append({"CrCl (mL/min)": "< 30", "Điều chỉnh": renal['under_30']})
            if 'under_15' in renal:
                renal_data.append({"CrCl (mL/min)": "< 15", "Điều chỉnh": renal['under_15']})
            if 'hemodialysis' in renal:
                renal_data.append({"CrCl (mL/min)": "Lọc máu", "Điều chỉnh": renal['hemodialysis']})
            
            if renal_data:
                st.dataframe(pd.DataFrame(renal_data), use_container_width=True, hide_index=True)
        
        # Integration: Tính liều theo CrCl (for antibiotics)
        is_antibiotic = drug_name in ANTIBIOTICS_DATABASE
        
        if is_antibiotic:
            st.markdown("---")
            st.markdown("### 🧮 Tính Liều Theo CrCl/eGFR")
            
            col1, col2 = st.columns([2, 1])
            with col1:
                st.info(f"""
                **💡 Tính liều tự động cho {drug_name}:**
                - Dựa trên chức năng thận (CrCl/eGFR)
                - Hỗ trợ HD, PD, béo phì, trẻ em
                - Tính liều chi tiết và cảnh báo tự động
                """)
            with col2:
                # Sanitize drug_name for button key
                safe_calc_key = f"calc_dose_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                if st.button("🧮 Tính Liều Theo CrCl", key=safe_calc_key, use_container_width=True, type="primary"):
                    # Set session state to switch to calculator with preset
                    st.session_state['preset_antibiotic_name'] = drug_name
                    st.session_state['switch_to_dosing_calculator'] = True
                    st.rerun()
            
            st.caption("💡 Click nút trên để mở calculator với thuốc này đã được chọn sẵn")
    
    # ========== SAFETY TAB ==========
    with tab_safety:
        # Contraindications
        if 'contraindications' in drug_data:
            st.markdown("### ⛔ Chống chỉ định:")
            contraindications = drug_data['contraindications']
            
            # Check if it's a dict with tuyệt_đối and tương_đối
            if isinstance(contraindications, dict):
                if 'tuyệt_đối' in contraindications and contraindications['tuyệt_đối']:
                    st.markdown("**🔴 Tuyệt đối:**")
                    for contra in contraindications['tuyệt_đối']:
                        st.markdown(f"- {contra}")
                
                if 'tương_đối' in contraindications and contraindications['tương_đối']:
                    st.markdown("**🟡 Tương đối:**")
                    for contra in contraindications['tương_đối']:
                        st.markdown(f"- {contra}")
            else:
                # Old format: list
                for contra in contraindications:
                    st.markdown(f"- {contra}")
        
        # Side effects
        if 'side_effects' in drug_data:
            st.markdown("---")
            st.markdown("### ⚠️ Tác dụng phụ:")
            for se in drug_data['side_effects']:
                st.markdown(f"- {se}")
        
        # Precautions
        if 'precautions' in drug_data:
            st.markdown("---")
            st.markdown("### ⚠️ Thận trọng:")
            for prec in drug_data['precautions']:
                st.markdown(f"- {prec}")
        
        # Pregnancy
        if 'pregnancy' in drug_data:
            st.markdown("---")
            preg = drug_data['pregnancy']
            preg_descriptions = {
                "A": "An toàn - Nghiên cứu không thấy nguy cơ",
                "B": "An toàn - Nghiên cứu động vật không thấy nguy cơ",
                "C": "Thận trọng - Nguy cơ không thể loại trừ",
                "D": "Nguy cơ - Có bằng chứng nguy cơ, cân nhắc lợi ích",
                "X": "Chống chỉ định - Nguy cơ vượt quá lợi ích"
            }
            desc = preg_descriptions.get(preg, "")
            preg_icons = {"A": "🟢", "B": "🟡", "C": "🟠", "D": "🔴", "X": "⚫"}
            st.markdown(f"### 🤰 **An toàn thai kỳ:** {preg_icons.get(preg, '')} {preg} - {desc}")
        
        # Lactation
        if 'lactation' in drug_data:
            st.markdown("---")
            st.markdown(f"### 🤱 **An toàn cho con bú:** {drug_data['lactation']}")
    
    # ========== INTERACTIONS TAB ==========
    with tab_interactions:
        if 'interactions' in drug_data:
            st.markdown("### 🔗 Tương tác thuốc:")
            for inter in drug_data['interactions']:
                st.markdown(f"- {inter}")
        else:
            st.info("Không có thông tin về tương tác thuốc. Sử dụng công cụ 'Kiểm Tra Tương Tác Thuốc' để kiểm tra chi tiết.")
    
    # ========== MONITORING TAB ==========
    with tab_monitoring:
        # Monitoring checklist
        if 'monitoring' in drug_data:
            st.markdown("### 📊 Theo dõi (Monitoring):")
            monitoring_list = drug_data['monitoring']
            if isinstance(monitoring_list, list):
                for mon in monitoring_list:
                    st.markdown(f"- ✅ {mon}")
            else:
                st.info(monitoring_list)
        
        # TDM Section (Therapeutic Drug Monitoring)
        try:
            from drugs.drug_utils.tdm_mapping import get_tdm_info, has_tdm
            
            if has_tdm(drug_name):
                st.markdown("---")
                st.markdown("### 📊 Theo Dõi Nồng Độ Thuốc (TDM)")
                
                tdm_info = get_tdm_info(drug_name)
                
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    # Display TDM information
                    therapeutic_range = tdm_info.get('therapeutic_range', 'N/A')
                    sampling_time = tdm_info.get('sampling_time', 'N/A')
                    half_life = tdm_info.get('half_life_hours', 'N/A')
                    unit = tdm_info.get('unit', 'N/A')
                    
                    half_life_display = f"{half_life} giờ" if isinstance(half_life, (int, float)) else str(half_life)
                    
                    st.info(f"""
                    **🎯 Khoảng điều trị:** {therapeutic_range}
                    
                    **⏰ Thời điểm lấy mẫu:** {sampling_time}
                    
                    **⏱️ Half-life:** {half_life_display}
                    
                    **📏 Đơn vị:** {unit}
                    """)
                
                with col2:
                    # Button to open TDM calculator
                    safe_tdm_key = f"tdm_calc_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '')}"
                    if st.button("📊 Mở TDM Calculator", key=safe_tdm_key, use_container_width=True, type="primary"):
                        # Set session state to switch to TDM module with preset
                        st.session_state['preset_tdm_drug'] = drug_name
                        st.session_state['switch_to_tdm'] = True
                        st.rerun()
                
                st.caption("💡 Click nút trên để mở TDM calculator với thuốc này đã được chọn sẵn")
        except ImportError:
            # TDM mapping not available, skip
            pass
        except Exception as e:
            # Silently fail if TDM check fails
            pass


def render_drug_database():
    """Main function to render drug database page with search and browse"""
    
    from .search import (
        search_drugs, 
        search_drugs_with_filters,
        get_drug_autocomplete_suggestions,
        get_recent_searches,
        add_recent_search,
        search_by_group,
        save_search,
        get_saved_searches,
        load_saved_search,
        delete_saved_search
    )
    from .drug_database import DRUG_GROUPS
    
    drug_count = len(DRUG_DATABASE)
    
    # Modern header with gradient
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>💊 Tra Cứu Dữ Liệu Thuốc</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Database <strong>{drug_count}</strong> thuốc phổ biến • Tất cả chuyên khoa
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick info
    with st.expander("ℹ️ Thông tin về database", expanded=False):
        st.info(f"""
        **Cơ sở dữ liệu bao gồm:**
        - ✅ {drug_count} thuốc phổ biến tại Việt Nam
        - ✅ Tim mạch, Đái tháo đường, Tiêu hóa, Giảm đau, và nhiều nhóm khác
        - ✅ Tên biệt dược và tên chung
        - ✅ Liều dùng chi tiết
        - ✅ Điều chỉnh theo chức năng thận
        - ✅ Chỉ định, chống chỉ định, tác dụng phụ, tương tác
        """)
    
    # Comparison list display
    if 'drug_comparison_list' in st.session_state and st.session_state['drug_comparison_list']:
        comparison_list = st.session_state['drug_comparison_list']
        st.markdown("### 🔄 Danh Sách So Sánh")
        col_list, col_btn = st.columns([3, 1])
        with col_list:
            comparison_str = ", ".join([f"**{drug}**" for drug in comparison_list])
            st.info(f"📊 Đã chọn {len(comparison_list)} thuốc: {comparison_str}")
        with col_btn:
            if st.button("📊 Mở So Sánh", use_container_width=True, type="primary"):
                # Switch to comparison view
                st.session_state['switch_to_comparison'] = True
                st.session_state['preset_comparison_drugs'] = comparison_list.copy()
                st.rerun()
        
        # Clear comparison button
        if st.button("🗑️ Xóa danh sách", key="clear_comparison"):
            st.session_state['drug_comparison_list'] = []
            st.rerun()
        
        st.markdown("---")
    
    # Search section with autocomplete
    st.markdown("### 🔍 Tìm kiếm thuốc")
    
    # Handle selected suggestion from buttons - trigger automatic search
    if 'drug_search_selected' in st.session_state:
        selected_value = st.session_state.pop('drug_search_selected')
        st.info(f"🔍 Đang tìm: **{selected_value}**")
        # Store in session state to trigger search below without widget update
        st.session_state['_auto_search_trigger'] = selected_value
    
    # Saved searches
    saved_searches = get_saved_searches()
    if saved_searches:
        st.markdown("**⭐ Saved Searches:**")
        saved_cols = st.columns(min(len(saved_searches), 5))
        for idx, (name, saved_data) in enumerate(list(saved_searches.items())[:5]):
            with saved_cols[idx]:
                if st.button(f"⭐ {name}", key=f"saved_{name}", use_container_width=True):
                    query, filters = load_saved_search(name)
                    st.session_state['drug_search_input'] = query or ""
                    st.session_state['drug_filters'] = filters or {}
                    st.session_state['_auto_search_trigger'] = query or ""
                    st.rerun()
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Nhập tên thuốc, nhóm, hoặc chỉ định",
            key="drug_search_input",
            placeholder="Ví dụ: Metformin, Omeprazole, tăng huyết áp...",
            value=st.session_state.get('drug_search_input', '')
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        search_button = st.button("🔍 Tìm", use_container_width=True)
    
    # Advanced Filters
    with st.expander("🔍 Advanced Filters", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        # Initialize filters in session state
        if 'drug_filters' not in st.session_state:
            st.session_state['drug_filters'] = {}
        
        filters = st.session_state['drug_filters']
        
        with col1:
            filter_groups = st.multiselect(
                "Drug Class",
                options=list(DRUG_GROUPS.keys()),
                default=filters.get('groups', []),
                key="filter_groups"
            )
            filter_routes = st.multiselect(
                "Route",
                options=["PO", "IV", "IM", "SC", "Inhalation", "Rectal", "Topical"],
                default=filters.get('routes', []),
                key="filter_routes"
            )
        
        with col2:
            filter_pregnancy = st.selectbox(
                "Pregnancy Category",
                options=["All", "A", "B", "C", "D", "X"],
                index=0 if filters.get('pregnancy', 'All') == 'All' else ["A", "B", "C", "D", "X"].index(filters.get('pregnancy', 'All')) + 1 if filters.get('pregnancy', 'All') in ["A", "B", "C", "D", "X"] else 0,
                key="filter_pregnancy"
            )
            filter_monitoring = st.checkbox(
                "Requires Monitoring",
                value=filters.get('requires_monitoring', False),
                key="filter_monitoring"
            )
        
        with col3:
            filter_renal = st.checkbox(
                "Has Renal Adjustment",
                value=filters.get('has_renal_adjustment', False),
                key="filter_renal"
            )
            filter_black_box = st.checkbox(
                "Has Black Box Warning",
                value=filters.get('has_black_box', False),
                key="filter_black_box"
            )
        
        # Update filters in session state
        st.session_state['drug_filters'] = {
            'groups': filter_groups,
            'routes': filter_routes,
            'pregnancy': filter_pregnancy,
            'requires_monitoring': filter_monitoring,
            'has_renal_adjustment': filter_renal,
            'has_black_box': filter_black_box
        }
        
        # Save search button
        col_save1, col_save2 = st.columns([2, 1])
        with col_save1:
            save_search_name = st.text_input("Save search as:", key="save_search_name", placeholder="e.g., My Search")
        with col_save2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("💾 Save Search", key="save_search_btn", use_container_width=True):
                if save_search_name:
                    save_search(save_search_name, search_query, st.session_state['drug_filters'])
                    st.success(f"✅ Saved: {save_search_name}")
                    st.rerun()
                else:
                    st.warning("Please enter a name for the search")
    
    # Autocomplete suggestions
    if search_query and len(search_query) >= 1:
        suggestions = get_drug_autocomplete_suggestions(search_query, max_suggestions=5)
        if suggestions:
            st.markdown("**Gợi ý:**")
            suggestion_cols = st.columns(min(5, len(suggestions)))
            for idx, suggestion in enumerate(suggestions[:5]):
                with suggestion_cols[idx]:
                    # Sanitize suggestion for key
                    safe_suggestion_key = f"suggest_{str(suggestion).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                    if st.button(f"💊 {suggestion}", key=safe_suggestion_key, use_container_width=True):
                        # Store selected value and rerun
                        st.session_state['drug_search_selected'] = str(suggestion)
                        st.rerun()
    
    # Recent searches
    recent = get_recent_searches()
    if recent:
        st.markdown("**Tìm kiếm gần đây:**")
        recent_cols = st.columns(min(len(recent), 5))
        for idx, recent_query in enumerate(recent[:5]):
            with recent_cols[idx]:
                # Sanitize recent_query for key
                safe_recent_key = f"recent_{str(recent_query).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                if st.button(f"↩️ {recent_query}", key=safe_recent_key, use_container_width=True):
                    # Store selected value and rerun
                    st.session_state['drug_search_selected'] = str(recent_query)
                    st.rerun()
    
    st.markdown("---")
    
    # Handle auto-triggered search from button selections
    # Use auto_search_query if triggered, otherwise use search_query from widget
    auto_search_query = None
    if '_auto_search_trigger' in st.session_state:
        auto_search_query = st.session_state.pop('_auto_search_trigger')
    
    # Search results or browse by group
    # Use auto_search_query if available, otherwise use search_query
    effective_query = auto_search_query if auto_search_query else search_query
    
    # Get filters from session state
    filters = st.session_state.get('drug_filters', {})
    
    if effective_query or search_button or any(filters.values()):
        if effective_query:
            add_recent_search(effective_query)
        
        # Use advanced search with filters
        results = search_drugs_with_filters(effective_query, filters)
        
        if results:
            st.markdown(f"### 📊 Kết quả tìm kiếm ({len(results)} thuốc)")
            
            # Lazy loading với pagination
            page_size = 20
            page_key = 'drug_results_page'
            if page_key not in st.session_state:
                st.session_state[page_key] = 0
            
            current_page = st.session_state[page_key]
            start_idx = current_page * page_size
            end_idx = start_idx + page_size
            page_results = results[start_idx:end_idx]
            
            # Display current page
            for drug_name, drug_data in page_results:
                render_compact_drug_card(drug_name, drug_data, search_query=effective_query)
                
                # Show detail if selected
                selected_key = "selected_drug"
                show_detail_key = "show_detail"
                if st.session_state.get(selected_key) == drug_name and st.session_state.get(show_detail_key, False):
                    display_drug_info(drug_name, drug_data)
                    # Sanitize drug_name for button key
                    safe_close_key = f"close_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                    if st.button("✖️ Đóng", key=safe_close_key):
                        if selected_key in st.session_state:
                            del st.session_state[selected_key]
                        if show_detail_key in st.session_state:
                            st.session_state[show_detail_key] = False
                        st.rerun()
            
            # Pagination controls
            if len(results) > page_size:
                total_pages = (len(results) + page_size - 1) // page_size
                st.markdown("---")
                col_prev, col_info, col_next = st.columns([1, 2, 1])
                
                with col_prev:
                    if st.button("◀️ Trước", disabled=(current_page == 0), use_container_width=True):
                        st.session_state[page_key] = max(0, current_page - 1)
                        st.rerun()
                
                with col_info:
                    st.markdown(f"**Trang {current_page + 1}/{total_pages}** ({start_idx + 1}-{min(end_idx, len(results))} / {len(results)} thuốc)", 
                               unsafe_allow_html=True)
                
                with col_next:
                    if st.button("Tiếp ▶️", disabled=(current_page >= total_pages - 1), use_container_width=True):
                        st.session_state[page_key] = min(total_pages - 1, current_page + 1)
                        st.rerun()
            else:
                # Reset page if results fit in one page
                if page_key in st.session_state:
                    st.session_state[page_key] = 0
        else:
            st.warning("Không tìm thấy thuốc nào. Thử tìm kiếm với từ khóa khác.")
            st.markdown("**Gợi ý:**")
            st.info("- Thử tìm bằng tên chung (generic name)\n- Tìm theo nhóm thuốc (ví dụ: Cardiovascular, Diabetes)\n- Tìm theo chỉ định (ví dụ: tăng huyết áp, đái tháo đường)")
    
    else:
        # Browse by group
        st.markdown("### 📚 Duyệt theo nhóm thuốc")
        
        selected_group = st.selectbox(
            "Chọn nhóm thuốc:",
            ["Tất cả"] + list(DRUG_GROUPS.keys()),
            key="browse_group"
        )
        
        if selected_group == "Tất cả":
            all_drugs = list(DRUG_DATABASE.items())
            st.markdown(f"### 💊 Tất cả thuốc ({len(all_drugs)})")
        else:
            all_drugs = search_by_group(selected_group)
            st.markdown(f"### 💊 {selected_group} ({len(all_drugs)})")
        
        # Display drugs với lazy loading
        page_size = 20
        page_key = 'drug_browse_page'
        if page_key not in st.session_state:
            st.session_state[page_key] = 0
        
        current_page = st.session_state[page_key]
        start_idx = current_page * page_size
        end_idx = start_idx + page_size
        page_drugs = all_drugs[start_idx:end_idx]
        
        # Display current page
        for drug_name, drug_data in page_drugs:
            render_compact_drug_card(drug_name, drug_data, search_query="")
            
            # Show detail if selected
            selected_key = "selected_drug"
            show_detail_key = "show_detail"
            if st.session_state.get(selected_key) == drug_name and st.session_state.get(show_detail_key, False):
                display_drug_info(drug_name, drug_data)
                # Sanitize drug_name for button key
                safe_close_key = f"close_{str(drug_name).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                if st.button("✖️ Đóng", key=safe_close_key):
                    if selected_key in st.session_state:
                        del st.session_state[selected_key]
                    if show_detail_key in st.session_state:
                        st.session_state[show_detail_key] = False
                    st.rerun()
        
        # Pagination controls for browse
        if len(all_drugs) > page_size:
            total_pages = (len(all_drugs) + page_size - 1) // page_size
            st.markdown("---")
            col_prev, col_info, col_next = st.columns([1, 2, 1])
            
            with col_prev:
                if st.button("◀️ Trước", disabled=(current_page == 0), key="browse_prev", use_container_width=True):
                    st.session_state[page_key] = max(0, current_page - 1)
                    st.rerun()
            
            with col_info:
                st.markdown(f"**Trang {current_page + 1}/{total_pages}** ({start_idx + 1}-{min(end_idx, len(all_drugs))} / {len(all_drugs)} thuốc)", 
                           unsafe_allow_html=True)
            
            with col_next:
                if st.button("Tiếp ▶️", disabled=(current_page >= total_pages - 1), key="browse_next", use_container_width=True):
                    st.session_state[page_key] = min(total_pages - 1, current_page + 1)
                    st.rerun()

