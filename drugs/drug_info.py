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


def render_compact_drug_card(drug_name, drug_data, key_prefix=""):
    """Render a compact drug card in list view"""
    vn_name = drug_data.get('vietnamese_name', '')
    group = drug_data.get('group', 'Unknown')
    admin = drug_data.get('administration', [])
    admin_str = " / ".join(admin) if admin else "N/A"
    
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
                    <strong style='color: #1976D2; font-size: 1.05em; margin-right: 8px;'>{drug_name}</strong>
                    {group_badge}
                </div>
                {f"<div style='color: #666; font-size: 0.9em; margin-bottom: 4px;'>{vn_name}</div>" if vn_name else ""}
                <div style='color: #888; font-size: 0.85em;'>{admin_str} | {group}</div>
            </div>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Button row
    col1, col2 = st.columns([1, 3])
    
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
        st.empty()


def display_drug_info(drug_name, drug_data):
    """Display detailed drug information in expandable format"""
    
    with st.expander(f"💊 **{drug_name}** - Thông tin chi tiết", expanded=True):
        # Header info
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if 'vietnamese_name' in drug_data:
                st.markdown(f"**Tên biệt dược:** {drug_data['vietnamese_name']}")
            
            if 'group' in drug_data:
                st.markdown(f"**Nhóm:** {drug_data['group']}")
        
        with col2:
            if 'administration' in drug_data:
                admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️", "SC": "💉", "Rectal": "📦"}
                admin_display = " / ".join([f"{admin_icons.get(route, '')} {route}" for route in drug_data['administration']])
                st.markdown(f"**Đường dùng:** {admin_display}")
            
            if 'pregnancy' in drug_data:
                preg_icons = {"A": "🟢", "B": "🟡", "C": "🟠", "D": "🔴", "X": "⚫"}
                preg = drug_data['pregnancy']
                st.markdown(f"**Thai kỳ:** {preg_icons.get(preg, '')} {preg}")
        
        st.markdown("---")
        
        # Indications
        if 'indications' in drug_data:
            st.markdown("### 📋 Chỉ định:")
            for ind in drug_data['indications']:
                st.markdown(f"- {ind}")
        
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
        
        st.markdown("---")
        
        # Dosage
        if 'dosage' in drug_data:
            st.markdown("### 💊 Liều dùng:")
            dosage = drug_data['dosage']
            adult_doses = []
            
            if 'adult_htn' in dosage:
                adult_doses.append(f"**Tăng huyết áp:** {dosage['adult_htn']}")
            if 'adult_po' in dosage:
                adult_doses.append(f"**Uống:** {dosage['adult_po']}")
            if 'adult_iv' in dosage:
                adult_doses.append(f"**IV:** {dosage['adult_iv']}")
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
        
        st.markdown("---")
        
        # Renal adjustment - Table format
        if 'renal_adjustment' in drug_data:
            st.markdown("### 🫘 Điều chỉnh theo chức năng thận:")
            
            renal = drug_data['renal_adjustment']
            renal_data = []
            
            if 'normal' in renal:
                renal_data.append({"CrCl": "≥ 60", "Điều chỉnh": renal['normal']})
            if '30_60' in renal:
                renal_data.append({"CrCl": "30-60", "Điều chỉnh": renal['30_60']})
            if '15_30' in renal:
                renal_data.append({"CrCl": "15-30", "Điều chỉnh": renal['15_30']})
            if 'under_30' in renal:
                renal_data.append({"CrCl": "< 30", "Điều chỉnh": renal['under_30']})
            if 'under_15' in renal:
                renal_data.append({"CrCl": "< 15", "Điều chỉnh": renal['under_15']})
            if 'hemodialysis' in renal:
                renal_data.append({"CrCl": "Lọc máu", "Điều chỉnh": renal['hemodialysis']})
            
            if renal_data:
                st.dataframe(pd.DataFrame(renal_data), use_container_width=True, hide_index=True)
        
        # Side effects
        if 'side_effects' in drug_data:
            st.markdown("### ⚠️ Tác dụng phụ:")
            for se in drug_data['side_effects']:
                st.markdown(f"- {se}")
        
        # Interactions
        if 'interactions' in drug_data:
            st.markdown("### 🔗 Tương tác thuốc:")
            for inter in drug_data['interactions']:
                st.markdown(f"- {inter}")
        
        # Pregnancy
        if 'pregnancy' in drug_data:
            preg = drug_data['pregnancy']
            preg_descriptions = {
                "A": "An toàn - Nghiên cứu không thấy nguy cơ",
                "B": "An toàn - Nghiên cứu động vật không thấy nguy cơ",
                "C": "Thận trọng - Nguy cơ không thể loại trừ",
                "D": "Nguy cơ - Có bằng chứng nguy cơ, cân nhắc lợi ích",
                "X": "Chống chỉ định - Nguy cơ vượt quá lợi ích"
            }
            desc = preg_descriptions.get(preg, "")
            st.markdown(f"### 🤰 **An toàn thai kỳ:** {preg} - {desc}")
        
        # Black Box Warnings (nếu có)
        if 'black_box_warnings' in drug_data:
            st.markdown("---")
            st.error(f"### ⚠️ **CẢNH BÁO ĐEN (Black Box Warning):**\n\n{drug_data['black_box_warnings']}")
        
        # Mechanism of Action
        if 'mechanism_of_action' in drug_data:
            st.markdown("---")
            st.markdown("### 🔬 Cơ chế tác động:")
            st.info(drug_data['mechanism_of_action'])
        
        # Monitoring
        if 'monitoring' in drug_data:
            st.markdown("---")
            st.markdown("### 📊 Theo dõi (Monitoring):")
            for mon in drug_data['monitoring']:
                st.markdown(f"- {mon}")
        
        # Precautions
        if 'precautions' in drug_data:
            st.markdown("---")
            st.markdown("### ⚠️ Thận trọng:")
            for prec in drug_data['precautions']:
                st.markdown(f"- {prec}")
        
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


def render_drug_database():
    """Main function to render drug database page with search and browse"""
    
    from .search import (
        search_drugs, 
        get_drug_autocomplete_suggestions,
        get_recent_searches,
        add_recent_search,
        search_by_group
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
    
    # Search section with autocomplete
    st.markdown("### 🔍 Tìm kiếm thuốc")
    
    # Handle selected suggestion from buttons - trigger automatic search
    if 'drug_search_selected' in st.session_state:
        selected_value = st.session_state.pop('drug_search_selected')
        st.info(f"🔍 Đang tìm: **{selected_value}**")
        # Store in session state to trigger search below without widget update
        st.session_state['_auto_search_trigger'] = selected_value
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "Nhập tên thuốc, nhóm, hoặc chỉ định",
            key="drug_search_input",
            placeholder="Ví dụ: Metformin, Omeprazole, tăng huyết áp..."
        )
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # Spacing
        search_button = st.button("🔍 Tìm", use_container_width=True)
    
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
    
    if effective_query or search_button:
        if effective_query:
            add_recent_search(effective_query)
            results = search_drugs(effective_query)
            
            if results:
                st.markdown(f"### 📊 Kết quả tìm kiếm ({len(results)} thuốc)")
                for drug_name, drug_data in results:
                    render_compact_drug_card(drug_name, drug_data)
                    
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
        
        # Display drugs
        for drug_name, drug_data in all_drugs:
            render_compact_drug_card(drug_name, drug_data)
            
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

