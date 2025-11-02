"""
Antibiotic Database and Lookup Functions
Tích hợp database kháng sinh với công cụ tra cứu và tính liều
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE


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
            # Add link to dosing calculator if available
            if selected_ab == "Vancomycin":
                st.markdown("---")
                if st.button("🧮 Mở công cụ tính liều Vancomycin", use_container_width=True):
                    st.session_state['vancomycin_calc'] = True
                    st.rerun()
            
            elif selected_ab in ["Gentamicin", "Amikacin"]:
                st.markdown("---")
                if st.button("🧮 Mở công cụ tính liều Aminoglycoside", use_container_width=True):
                    st.session_state['aminoglycoside_calc'] = True
                    st.rerun()
    
    elif search_query:
        results = search_antibiotics(search_query)
        
        if results:
            st.success(f"Tìm thấy **{len(results)}** kết quả cho '{search_query}'")
            
            # Display results
            for ab_name, ab_data in results:
                with st.expander(f"💊 {ab_name} - {ab_data.get('vietnamese_name', '')}", expanded=(len(results) == 1)):
                    display_antibiotic_info(ab_name, ab_data)
                    
                    # Quick links to dosing calculators
                    if ab_name == "Vancomycin":
                        st.markdown("---")
                        if st.button(f"🧮 Tính liều Vancomycin", key=f"calc_{ab_name}"):
                            st.session_state['show_vancomycin_calc'] = True
                    
                    elif ab_name in ["Gentamicin", "Amikacin"]:
                        st.markdown("---")
                        if st.button(f"🧮 Tính liều Aminoglycoside", key=f"calc_{ab_name}"):
                            st.session_state['show_aminoglycoside_calc'] = True
        else:
            st.warning(f"Không tìm thấy kháng sinh nào cho '{search_query}'")
            st.info("💡 Thử tìm kiếm với: tên thuốc, biệt dược, hoặc chỉ định (ví dụ: MRSA, Sepsis)")
    
    else:
        # Show quick access categories
        st.markdown("### 📚 Kháng Sinh Theo Nhóm:")
        
        # Group antibiotics by category
        groups = {}
        for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
            group = ab_data.get('group', 'Khác')
            if group not in groups:
                groups[group] = []
            groups[group].append(ab_name)
        
        # Display in columns
        cols = st.columns(3)
        col_idx = 0
        
        for group, ab_list in groups.items():
            with cols[col_idx % 3]:
                st.markdown(f"#### {group}")
                for ab_name in sorted(ab_list):
                    if st.button(ab_name, key=f"quick_{ab_name}", use_container_width=True):
                        st.session_state['selected_antibiotic'] = ab_name
                        st.rerun()
            
            col_idx += 1
        
        # Show selected antibiotic if any
        if 'selected_antibiotic' in st.session_state:
            selected = st.session_state['selected_antibiotic']
            if selected in ANTIBIOTICS_DATABASE:
                st.markdown("---")
                display_antibiotic_info(selected, ANTIBIOTICS_DATABASE[selected])
                
                # Quick links
                if selected == "Vancomycin":
                    st.markdown("---")
                    if st.button("🧮 Tính liều Vancomycin", use_container_width=True):
                        st.session_state['show_vancomycin_calc'] = True
                
                elif selected in ["Gentamicin", "Amikacin"]:
                    st.markdown("---")
                    if st.button("🧮 Tính liều Aminoglycoside", use_container_width=True):
                        st.session_state['show_aminoglycoside_calc'] = True


def render_database():
    """Antibiotic Database Viewer - Full list"""
    
    ab_count = len(ANTIBIOTICS_DATABASE)
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
        
        # Quick links to calculators
        if selected == "Vancomycin":
            st.markdown("---")
            if st.button("🧮 Mở công cụ tính liều Vancomycin", use_container_width=True):
                st.session_state['show_vancomycin_calc'] = True
        
        elif selected in ["Gentamicin", "Amikacin"]:
            st.markdown("---")
            if st.button("🧮 Mở công cụ tính liều Aminoglycoside", use_container_width=True):
                st.session_state['show_aminoglycoside_calc'] = True
