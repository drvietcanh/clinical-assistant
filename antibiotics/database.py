"""
Antibiotic Database and Lookup Functions
Tích hợp database kháng sinh với công cụ tra cứu và tính liều
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .dosing_calculator import calculate_adjusted_dose, get_renal_category


def search_antibiotics(query):
    """
    Search antibiotics by name, Vietnamese name, group, or indication
    """
    query_lower = query.lower()
    results = []
    
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        # Search in name
        if query_lower in ab_name.lower():
            results.append((ab_name, ab_data))
            continue
        
        # Search in Vietnamese name
        if 'vietnamese_name' in ab_data:
            if query_lower in ab_data['vietnamese_name'].lower():
                results.append((ab_name, ab_data))
                continue
        
        # Search in group
        if 'group' in ab_data:
            if query_lower in ab_data['group'].lower():
                results.append((ab_name, ab_data))
                continue
        
        # Search in indications
        if 'indications' in ab_data:
            for indication in ab_data['indications']:
                if query_lower in indication.lower():
                    results.append((ab_name, ab_data))
                    break
    
    return results


def display_antibiotic_info(ab_name, ab_data):
    """Display detailed antibiotic information"""
    
    st.markdown(f"## 💊 {ab_name}")
    
    if 'vietnamese_name' in ab_data:
        st.markdown(f"**Tên biệt dược tại Việt Nam:** {ab_data['vietnamese_name']}")
    
    if 'group' in ab_data:
        st.markdown(f"**Nhóm:** {ab_data['group']}")
    
    st.markdown("---")
    
    # Administration
    if 'administration' in ab_data:
        admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
        admin_display = " / ".join([f"{admin_icons.get(route, '')} {route}" for route in ab_data['administration']])
        st.markdown(f"**Đường dùng:** {admin_display}")
    
    # Indications
    if 'indications' in ab_data:
        st.markdown("### 📋 Chỉ định:")
        for ind in ab_data['indications']:
            st.markdown(f"- {ind}")
    
    # Contraindications
    if 'contraindications' in ab_data:
        st.markdown("### ⛔ Chống chỉ định:")
        for contr in ab_data['contraindications']:
            st.markdown(f"- ❌ {contr}")
    
    st.markdown("---")
    
    # Dosage
    if 'dosage' in ab_data:
        st.markdown("### 💉 Liều dùng:")
        
        dosage = ab_data['dosage']
        
        col1, col2 = st.columns(2)
        
        with col1:
            if 'adult_iv' in dosage:
                st.markdown(f"**Người lớn (IV):**")
                st.info(f"{dosage['adult_iv']}")
            
            if 'adult_im' in dosage:
                st.markdown(f"**Người lớn (IM):**")
                st.info(f"{dosage['adult_im']}")
            
            if 'adult_po' in dosage:
                st.markdown(f"**Người lớn (PO):**")
                st.info(f"{dosage['adult_po']}")
        
        with col2:
            if 'adult_severe' in dosage:
                st.markdown(f"**Nhiễm khuẩn nặng:**")
                st.warning(f"{dosage['adult_severe']}")
            
            if 'adult_standard' in dosage:
                st.markdown(f"**Liều chuẩn:**")
                st.info(f"{dosage['adult_standard']}")
            
            if 'pediatric_iv' in dosage:
                st.markdown(f"**Trẻ em (IV):**")
                st.info(f"{dosage['pediatric_iv']}")
        
        if 'notes' in dosage:
            st.markdown(f"💡 **Lưu ý:** {dosage['notes']}")
    
    st.markdown("---")
    
    # Renal adjustment
    if 'renal_adjustment' in ab_data:
        st.markdown("### 🫘 Điều chỉnh theo chức năng thận:")
        
        renal = ab_data['renal_adjustment']
        
        col1, col2 = st.columns(2)
        
        with col1:
            if 'normal' in renal:
                st.markdown(f"**CrCl ≥ 60:** {renal['normal']}")
            
            if '30_60' in renal:
                st.markdown(f"**CrCl 30-60:** {renal['30_60']}")
        
        with col2:
            if '15_30' in renal:
                st.markdown(f"**CrCl 15-30:** {renal['15_30']}")
            
            if 'under_15' in renal:
                st.markdown(f"**CrCl < 15:** {renal['under_15']}")
            
            if 'hemodialysis' in renal:
                st.markdown(f"**Lọc máu:** {renal['hemodialysis']}")
    
    st.markdown("---")
    
    # Side effects
    if 'side_effects' in ab_data:
        st.markdown("### ⚠️ Tác dụng phụ:")
        for se in ab_data['side_effects']:
            st.markdown(f"- {se}")
    
    # Monitoring
    if 'monitoring' in ab_data:
        st.markdown(f"### 📊 Theo dõi: {ab_data['monitoring']}")
    
    st.markdown("---")
    
    # Interactions
    if 'interactions' in ab_data:
        st.markdown("### 🔗 Tương tác thuốc:")
        for inter in ab_data['interactions']:
            st.markdown(f"- {inter}")
    
    # AWaRe classification
    if 'aware_classification' in ab_data:
        aware_colors = {
            "ACCESS": "🟢",
            "WATCH": "🟡",
            "RESERVE": "🔴"
        }
        aware_name = ab_data['aware_classification']
        st.markdown(f"### {aware_colors.get(aware_name, '')} **AWaRe Classification:** {aware_name}")
    
    # Pregnancy
    if 'pregnancy' in ab_data:
        st.markdown(f"### 🤰 **An toàn thai kỳ:** {ab_data['pregnancy']}")


def render_antibiotic_lookup():
    """Antibiotic Lookup Tool with search and detailed info"""
    
    st.markdown("""
    <h2 style='text-align: center; color: #0EA5E9;'>🔍 Tra Cứu Kháng Sinh</h2>
    <p style='text-align: center;'><em>Tìm kiếm thông tin kháng sinh theo tên, biệt dược, chỉ định</em></p>
    """, unsafe_allow_html=True)
    
    st.info("""
    **Tra cứu kháng sinh bao gồm:**
    - ✅ Liều dùng chuẩn (IV/IM/PO)
    - ✅ Điều chỉnh theo chức năng thận
    - ✅ Chỉ định & Chống chỉ định
    - ✅ Tác dụng phụ
    - ✅ Tương tác thuốc
    - ✅ Liên kết đến công cụ tính liều (Vancomycin, Aminoglycoside)
    """)
    
    st.markdown("---")
    
    # Search bar
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input(
            "🔍 Tìm kiếm kháng sinh:",
            placeholder="Ví dụ: Ceftriaxone, Rocephin, Vancomycin, MRSA, Sepsis...",
            key="ab_search"
        )
    
    with col2:
        show_all = st.checkbox("Hiển thị tất cả", key="show_all_ab")
    
    st.markdown("---")
    
    # Get all antibiotic names for quick access
    all_antibiotics = list(ANTIBIOTICS_DATABASE.keys())
    
    # Search or display all
    if show_all:
        selected_ab = st.selectbox(
            "Chọn kháng sinh để xem chi tiết:",
            [""] + all_antibiotics,
            format_func=lambda x: "--- Chọn kháng sinh ---" if x == "" else x,
            key="ab_select"
        )
        
        if selected_ab:
            display_antibiotic_info(selected_ab, ANTIBIOTICS_DATABASE[selected_ab])
    
    elif search_query:
        results = search_antibiotics(search_query)
        
        if results:
            st.success(f"Tìm thấy **{len(results)}** kết quả cho '{search_query}'")
            
            # Display results as beautiful cards
            for ab_name, ab_data in results:
                # Create a card for each result
                vn_name = ab_data.get('vietnamese_name', '').split(',')[0] if ab_data.get('vietnamese_name') else ''
                admin = ab_data.get('administration', [])
                aware = ab_data.get('aware_classification', '')
                has_calc = ab_name in ["Vancomycin", "Gentamicin", "Amikacin"]
                
                # Admin icons
                admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
                admin_str = " ".join([admin_icons.get(a, "") + " " + a for a in admin])
                
                # AWaRe badge
                aware_colors = {
                    "ACCESS": "#4CAF50",
                    "WATCH": "#FF9800",
                    "RESERVE": "#F44336"
                }
                aware_badge = ""
                if aware:
                    badge_color = aware_colors.get(aware, "#999")
                    aware_badge = f'<span style="background-color: {badge_color}; color: white; padding: 4px 10px; border-radius: 15px; font-size: 0.8em; font-weight: bold; margin-left: 10px;">{aware}</span>'
                
                # Header card
                st.markdown(f"""
                <div style='
                    background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 100%);
                    color: white;
                    padding: 20px;
                    border-radius: 15px;
                    margin: 20px 0;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                '>
                    <h2 style='margin: 0; color: white; display: inline-block;'>💊 {ab_name}</h2>
                    {aware_badge}
                    {f"<p style='margin: 10px 0 5px 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>{vn_name}</p>" if vn_name else ""}
                    <p style='margin: 5px 0 0 0; color: rgba(255,255,255,0.8); font-size: 0.95em;'>{admin_str}</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Display full info
                display_antibiotic_info(ab_name, ab_data)
                
                # Quick dosing calculator integration
                st.markdown("---")
                st.markdown("### 🧮 Tính Liều Theo eGFR/CrCl")
                
                # Get patient info if available from session state, otherwise use defaults
                patient_crcl = st.session_state.get('patient_crcl', None)
                patient_egfr = st.session_state.get('patient_egfr', None)
                
                if patient_crcl is not None:
                    st.info(f"**CrCl đã tính:** {patient_crcl:.1f} mL/min | **eGFR:** {patient_egfr:.1f} mL/min/1.73m²" if patient_egfr else f"**CrCl đã tính:** {patient_crcl:.1f} mL/min")
                
                    if st.button(f"🧮 Tính liều {ab_name} cho CrCl = {patient_crcl:.1f} mL/min", use_container_width=True, type="primary", key=f"quick_calc_{ab_name}"):
                        renal_category = get_renal_category(patient_crcl, patient_egfr)
                        result = calculate_adjusted_dose(ab_name, patient_crcl, patient_egfr, indication="standard")
                        
                        if "error" not in result:
                            st.markdown("---")
                            st.markdown("#### 📊 Kết Quả Tính Liều:")
                            st.success(f"**Điều chỉnh liều:** {result['adjustment']}")
                            
                            if result.get('full_renal_guide'):
                                st.markdown("**Bảng điều chỉnh đầy đủ:**")
                                renal_guide = result['full_renal_guide']
                                renal_info = []
                                if 'normal' in renal_guide:
                                    renal_info.append(f"✅ CrCl ≥ 60: {renal_guide['normal']}")
                                if '30_60' in renal_guide:
                                    renal_info.append(f"⚠️ CrCl 30-59: {renal_guide['30_60']}")
                                if '15_30' in renal_guide:
                                    renal_info.append(f"🔴 CrCl 15-29: {renal_guide['15_30']}")
                                if 'under_15' in renal_guide:
                                    renal_info.append(f"🚨 CrCl < 15: {renal_guide['under_15']}")
                                
                                for info in renal_info:
                                    st.markdown(f"- {info}")
                
                # Universal dosing calculator info
                st.info("💡 Sử dụng công cụ **'🧮 Tính Liều Theo eGFR/CrCl'** ở menu để tính liều tự động với thông số bệnh nhân cụ thể")
                
                if len(results) > 1 and ab_name != results[-1][0]:
                    st.markdown("<hr style='margin: 30px 0; border: none; border-top: 2px solid #e0e0e0;'>", unsafe_allow_html=True)
        else:
            st.warning(f"Không tìm thấy kháng sinh nào cho '{search_query}'")
            st.info("💡 Thử tìm kiếm với: tên thuốc, biệt dược, hoặc chỉ định (ví dụ: MRSA, Sepsis)")
    
    else:
        # Show quick access categories with beautiful cards
        st.markdown("### 📚 Kháng Sinh Theo Nhóm:")
        
        # Group antibiotics by category
        groups = {}
        for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
            group = ab_data.get('group', 'Khác')
            if group not in groups:
                groups[group] = []
            groups[group].append((ab_name, ab_data))
        
        # Group colors for visual distinction
        group_colors = {
            "Beta-lactam - Penicillin": "#E3F2FD",
            "Beta-lactam - Aminopenicillin": "#E1F5FE",
            "Beta-lactam - Penicillin + Beta-lactamase inhibitor": "#E0F2F1",
            "Beta-lactam - Extended-spectrum Penicillin + Inhibitor": "#F3E5F5",
            "Beta-lactam - Cephalosporin thế hệ 1": "#FFF3E0",
            "Beta-lactam - Cephalosporin thế hệ 3": "#FFE0B2",
            "Beta-lactam - Cephalosporin thế hệ 4": "#FFCCBC",
            "Beta-lactam - Carbapenem": "#F8BBD0",
            "Aminoglycoside": "#C5E1A5",
            "Glycopeptide": "#BBDEFB",
            "Fluoroquinolone": "#FFCDD2",
            "Macrolide": "#D1C4E9",
            "Lincosamide": "#DCEDC8",
            "Nitroimidazole": "#FFE082",
            "Oxazolidinone": "#F48FB1",
            "Polymyxin": "#90CAF9",
        }
        
        # AWaRe badge colors
        aware_colors = {
            "ACCESS": "#4CAF50",
            "WATCH": "#FF9800",
            "RESERVE": "#F44336"
        }
        
        # Display groups with beautiful cards
        for group, ab_list in sorted(groups.items()):
            group_bg = group_colors.get(group, "#F5F5F5")
            
            st.markdown(f"""
            <div style='background-color: {group_bg}; padding: 15px; border-radius: 10px; margin: 15px 0; border-left: 5px solid #0EA5E9;'>
                <h4 style='margin: 0; color: #1976D2;'>{group}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            # Display antibiotics as cards in grid
            num_cols = 3
            cols = st.columns(num_cols)
            
            for idx, (ab_name, ab_data) in enumerate(sorted(ab_list, key=lambda x: x[0])):
                with cols[idx % num_cols]:
                    # Get antibiotic data
                    vn_name = ab_data.get('vietnamese_name', '').split(',')[0] if ab_data.get('vietnamese_name') else ''
                    admin = ab_data.get('administration', [])
                    aware = ab_data.get('aware_classification', '')
                    has_calc = ab_name in ["Vancomycin", "Gentamicin", "Amikacin"]
                    
                    # Admin icons
                    admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
                    admin_str = " ".join([admin_icons.get(a, "") for a in admin[:2]])
                    
                    # AWaRe badge
                    aware_badge = ""
                    if aware:
                        badge_color = aware_colors.get(aware, "#999")
                        aware_badge = f'<span style="background-color: {badge_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.7em; font-weight: bold;">{aware}</span>'
                    
                    # Calculator badge
                    calc_badge = ""
                    if has_calc:
                        calc_badge = '<span style="background-color: #9C27B0; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.7em; font-weight: bold;">🧮 Tính liều</span>'
                    
                    # Card HTML
                    card_html = f"""
                    <div style='
                        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
                        border: 2px solid #e0e0e0;
                        border-radius: 12px;
                        padding: 15px;
                        margin: 10px 0;
                        cursor: pointer;
                        transition: all 0.3s;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    '
                    onmouseover="this.style.borderColor='#0EA5E9'; this.style.boxShadow='0 4px 8px rgba(0,0,0,0.2)';"
                    onmouseout="this.style.borderColor='#e0e0e0'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.1)';">
                        <h4 style='margin: 0 0 8px 0; color: #1976D2; font-size: 1.1em;'>{ab_name}</h4>
                        {f"<p style='margin: 5px 0; color: #666; font-size: 0.9em;'>{vn_name}</p>" if vn_name else ""}
                        <p style='margin: 8px 0; font-size: 0.85em; color: #888;'>{admin_str}</p>
                        <div style='margin-top: 10px; display: flex; gap: 5px; flex-wrap: wrap;'>
                            {aware_badge}
                            {calc_badge}
                        </div>
                    </div>
                    """
                    
                    st.markdown(card_html, unsafe_allow_html=True)
                    
                    # Button to view details
                    if st.button(f"📖 Xem chi tiết", key=f"view_{ab_name}", use_container_width=True):
                        st.session_state['selected_antibiotic'] = ab_name
                        st.rerun()
        
        # Show selected antibiotic if any
        if 'selected_antibiotic' in st.session_state:
            selected = st.session_state['selected_antibiotic']
            if selected in ANTIBIOTICS_DATABASE:
                st.markdown("---")
                display_antibiotic_info(selected, ANTIBIOTICS_DATABASE[selected])
                


def render_database():
    """Antibiotic Database Viewer - Full list (now integrated with lookup)"""
    
    ab_count = len(ANTIBIOTICS_DATABASE)
    
    # Tabs for search vs full list
    tab1, tab2 = st.tabs(["🔍 Tra Cứu", "📊 Danh Sách Đầy Đủ"])
    
    with tab1:
        render_antibiotic_lookup()
    
    with tab2:
        st.markdown(f"""
        <h2 style='text-align: center; color: #0EA5E9;'>📊 Cơ Sở Dữ Liệu Kháng Sinh</h2>
        <p style='text-align: center;'><em>Danh sách đầy đủ {ab_count} kháng sinh tiêm truyền thông dụng</em></p>
        """, unsafe_allow_html=True)
        st.info(f"""
    **Cơ sở dữ liệu bao gồm:**
        - ✅ {ab_count} kháng sinh tiêm truyền (IV/IM) thông dụng
        - ✅ Tên biệt dược tại Việt Nam
        - ✅ Liều dùng chi tiết theo từng tình huống
        - ✅ Điều chỉnh theo chức năng thận/gan
        - ✅ Dựa trên guidelines quốc tế (IDSA, ASHP, WHO AWaRe)
        """)
    
    st.markdown("---")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_group = st.selectbox(
            "Lọc theo nhóm:",
            ["Tất cả"] + list(set([ab.get('group', 'Khác') for ab in ANTIBIOTICS_DATABASE.values()])),
            key="filter_group"
        )
    
    with col2:
        filter_route = st.selectbox(
            "Lọc theo đường dùng:",
            ["Tất cả", "IV", "IM", "PO"],
            key="filter_route"
        )
    
    with col3:
        filter_aware = st.selectbox(
            "AWaRe Classification:",
            ["Tất cả", "ACCESS", "WATCH", "RESERVE"],
            key="filter_aware"
        )
    
    st.markdown("---")
    
    # Filter antibiotics
    filtered_ab = {}
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        # Group filter
        if filter_group != "Tất cả":
            if ab_data.get('group', 'Khác') != filter_group:
                continue
        
        # Route filter
        if filter_route != "Tất cả":
            if filter_route not in ab_data.get('administration', []):
                continue
        
        # AWaRe filter
        if filter_aware != "Tất cả":
            if ab_data.get('aware_classification', '') != filter_aware:
                continue
        
        filtered_ab[ab_name] = ab_data
    
    # Display as table
    st.markdown(f"### 📋 Danh sách ({len(filtered_ab)} kháng sinh):")
    
    # Create DataFrame for display
    table_data = []
    for ab_name, ab_data in sorted(filtered_ab.items()):
        table_data.append({
            "Tên kháng sinh": ab_name,
            "Biệt dược VN": ab_data.get('vietnamese_name', ''),
            "Nhóm": ab_data.get('group', ''),
            "Đường dùng": ", ".join(ab_data.get('administration', [])),
            "AWaRe": ab_data.get('aware_classification', ''),
            "Có tính liều": "✅" if ab_name in ["Vancomycin", "Gentamicin", "Amikacin"] else ""
        })
    
    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Click to view details
    st.markdown("### 🔍 Xem chi tiết:")
    selected = st.selectbox(
        "Chọn kháng sinh:",
        [""] + list(filtered_ab.keys()),
        format_func=lambda x: "--- Chọn để xem chi tiết ---" if x == "" else x,
        key="db_select"
    )
    
    if selected:
        st.markdown("---")
        display_antibiotic_info(selected, filtered_ab[selected])
        
