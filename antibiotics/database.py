"""
Antibiotic Database and Lookup Functions - Optimized Version
Tích hợp database kháng sinh với công cụ tra cứu và tính liều
Đã tối ưu: loại bỏ trùng lặp, compact view, expandable details, integrated dosing calculator
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .dosing_calculator import (
    calculate_adjusted_dose, 
    get_renal_category,
    calculate_detailed_dose,
    check_warnings,
    calculate_ibw,
    calculate_abw,
    calculate_bmi
)


def search_antibiotics(query, max_results=None):
    """Enhanced search antibiotics by name, Vietnamese name, group, or indication with scoring"""
    query_lower = query.lower()
    results = []
    
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        score = 0.0
        
        # Search in name (highest priority)
        if query_lower in ab_name.lower():
            if query_lower == ab_name.lower():
                score = 1.0  # Exact match
            elif ab_name.lower().startswith(query_lower):
                score = 0.9  # Starts with query
            else:
                score = 0.8  # Contains query
            results.append((ab_name, ab_data, score))
            continue
        
        # Search in Vietnamese name
        if 'vietnamese_name' in ab_data:
            vn_name_lower = ab_data['vietnamese_name'].lower()
            if query_lower in vn_name_lower:
                score = 0.7
                results.append((ab_name, ab_data, score))
                continue
        
        # Search in group
        if 'group' in ab_data:
            group_lower = ab_data['group'].lower()
            if query_lower in group_lower:
                score = 0.6
                results.append((ab_name, ab_data, score))
                continue
        
        # Search in indications
        if 'indications' in ab_data:
            for indication in ab_data['indications']:
                if query_lower in indication.lower():
                    score = 0.5
                    results.append((ab_name, ab_data, score))
                    break
    
    # Sort by score (descending)
    results.sort(key=lambda x: x[2], reverse=True)
    
    # Return just (name, data) tuples for backward compatibility
    if max_results:
        return [(name, data) for name, data, score in results[:max_results]]
    return [(name, data) for name, data, score in results]


def get_antibiotic_autocomplete_suggestions(query, max_suggestions=5):
    """
    Get autocomplete suggestions for antibiotic search
    Returns list of antibiotic names matching query
    """
    if not query or len(query) < 1:
        # Popular antibiotics
        return ["Vancomycin", "Ceftriaxone", "Piperacillin-Tazobactam", "Meropenem", "Levofloxacin"]
    
    query_lower = query.lower()
    suggestions = []
    seen = set()
    
    # Search in names first (most relevant)
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        if query_lower in ab_name.lower():
            if ab_name not in seen:
                suggestions.append(ab_name)
                seen.add(ab_name)
                if len(suggestions) >= max_suggestions:
                    break
    
    # If not enough, search in Vietnamese names
    if len(suggestions) < max_suggestions:
        for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
            if ab_name in seen:
                continue
            if 'vietnamese_name' in ab_data:
                vn_names = ab_data['vietnamese_name'].split(',')
                for vn_name in vn_names:
                    if query_lower in vn_name.strip().lower():
                        suggestions.append(ab_name)
                        seen.add(ab_name)
                        break
                if len(suggestions) >= max_suggestions:
                    break
    
    return suggestions


def get_recent_searches():
    """Get recent antibiotic searches from session state"""
    return st.session_state.get('recent_antibiotic_searches', [])


def add_to_recent_searches(query):
    """Add search query to recent searches (max 10)"""
    if 'recent_antibiotic_searches' not in st.session_state:
        st.session_state.recent_antibiotic_searches = []
    
    recent = st.session_state.recent_antibiotic_searches
    
    # Remove if already exists
    if query in recent:
        recent.remove(query)
    
    # Add to beginning
    recent.insert(0, query)
    
    # Keep only last 10
    st.session_state.recent_antibiotic_searches = recent[:10]


def filter_antibiotics(group_filter="Tất cả", route_filter="Tất cả", aware_filter="Tất cả"):
    """Filter antibiotics by group, route, and AWaRe classification"""
    filtered = {}
    
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        # Group filter
        if group_filter != "Tất cả":
            if ab_data.get('group', 'Khác') != group_filter:
                continue
        
        # Route filter
        if route_filter != "Tất cả":
            if route_filter not in ab_data.get('administration', []):
                continue
        
        # AWaRe filter
        if aware_filter != "Tất cả":
            if ab_data.get('aware_classification', '') != aware_filter:
                continue
        
        filtered[ab_name] = ab_data
    
    return filtered


def render_compact_antibiotic_card(ab_name, ab_data, key_prefix=""):
    """Render a compact card for antibiotic list view"""
    vn_name = ab_data.get('vietnamese_name', '').split(',')[0] if ab_data.get('vietnamese_name') else ''
    admin = ab_data.get('administration', [])
    aware = ab_data.get('aware_classification', '')
    has_calc = ab_name in ["Vancomycin", "Gentamicin", "Amikacin"]
    group = ab_data.get('group', 'Khác')
    
    # Admin icons
    admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
    admin_str = " ".join([admin_icons.get(a, "") for a in admin[:3]])
    
    # AWaRe badge
    aware_colors = {
        "ACCESS": "#4CAF50",
        "WATCH": "#FF9800",
        "RESERVE": "#F44336"
    }
    aware_badge = ""
    if aware:
        badge_color = aware_colors.get(aware, "#999")
        aware_badge = f'<span style="background-color: {badge_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold; margin-left: 8px;">{aware}</span>'
    
    # Calculator badge
    calc_badge = ""
    if has_calc:
        calc_badge = '<span style="background-color: #9C27B0; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.75em; font-weight: bold;">🧮</span>'
    
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
                    <strong style='color: #1976D2; font-size: 1.05em; margin-right: 8px;'>{ab_name}</strong>
                    {aware_badge}
                    {calc_badge}
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
        if st.button("📖 Chi tiết", key=f"{key_prefix}detail_{ab_name}", use_container_width=True):
            st.session_state['view_antibiotic'] = ab_name
            st.rerun()
    
    return ab_name


def render_quick_dosing_calculator(ab_name, ab_data, key_prefix=""):
    """
    Compact dosing calculator for embedding in antibiotic detail view
    Returns calculation result or None
    """
    st.markdown("---")
    
    # Modern card header
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        margin: 15px 0 10px 0;
    '>
        <h4 style='margin: 0; color: white;'>🧮 Tính Liều Cho Bệnh Nhân</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Check for imported CrCl/eGFR
    imported_crcl = st.session_state.get('patient_crcl', None)
    imported_egfr = st.session_state.get('patient_egfr', None)
    
    # Compact input form
    col1, col2, col3 = st.columns(3)
    
    with col1:
        weight = st.number_input(
            "Cân nặng (kg)",
            min_value=10.0,
            max_value=200.0,
            value=70.0,
            step=1.0,
            key=f"{key_prefix}dosing_weight",
            help="Cân nặng thực tế của bệnh nhân"
        )
    
    with col2:
        # CrCl input with import option
        if imported_crcl:
            use_imported = st.checkbox(
                f"📥 Dùng CrCl đã tính: {imported_crcl:.1f}",
                value=True,
                key=f"{key_prefix}use_crcl"
            )
            if use_imported:
                crcl = imported_crcl
                st.caption(f"✅ {crcl:.1f} mL/min")
            else:
                crcl = st.number_input(
                    "CrCl (mL/min)",
                    min_value=0.0,
                    max_value=200.0,
                    value=float(imported_crcl),
                    step=1.0,
                    key=f"{key_prefix}crcl",
                    help="Creatinine Clearance"
                )
        else:
            crcl = st.number_input(
                "CrCl (mL/min)",
                min_value=0.0,
                max_value=200.0,
                value=60.0,
                step=1.0,
                key=f"{key_prefix}crcl",
                help="Creatinine Clearance. Dùng eGFR Calculator để tính chính xác"
            )
    
    with col3:
        indication = st.selectbox(
            "Chỉ định:",
            ["Chuẩn", "Nhiễm khuẩn nặng", "Viêm màng não"],
            key=f"{key_prefix}indication",
            help="Loại nhiễm khuẩn"
        )
    
    # Calculate button
    if st.button(
        f"🧮 Tính Liều {ab_name}",
        type="primary",
        use_container_width=True,
        key=f"{key_prefix}calc_btn"
    ):
        indication_map = {
            "Chuẩn": "standard",
            "Nhiễm khuẩn nặng": "severe",
            "Viêm màng não": "meningitis"
        }
        indication_code = indication_map.get(indication, "standard")
        
        # Calculate adjusted dose
        result = calculate_adjusted_dose(
            ab_name,
            crcl,
            egfr=imported_egfr,
            indication=indication_code
        )
        
        if "error" not in result:
            # Store result in session for display
            st.session_state[f"{key_prefix}dosing_result"] = result
            st.session_state[f"{key_prefix}dosing_weight"] = weight
            st.session_state[f"{key_prefix}dosing_crcl"] = crcl
            st.session_state[f"{key_prefix}dosing_indication"] = indication_code
            st.rerun()
        else:
            st.error(result["error"])
    
    # Display results if available
    if f"{key_prefix}dosing_result" in st.session_state:
        result = st.session_state[f"{key_prefix}dosing_result"]
        weight_used = st.session_state.get(f"{key_prefix}dosing_weight", weight)
        crcl_used = st.session_state.get(f"{key_prefix}dosing_crcl", crcl)
        
        # Results card
        st.markdown("---")
        st.markdown("### 📊 Kết Quả Tính Liều:")
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("CrCl", f"{crcl_used:.1f} mL/min")
        with col2:
            renal_cat = result.get('renal_category', 'normal')
            cat_labels = {
                'normal': '✅ Bình thường',
                '30_60': '⚠️ Suy nhẹ-vừa',
                '15_30': '🔴 Suy nặng',
                'under_15': '🚨 Rất nặng'
            }
            st.metric("Phân loại", cat_labels.get(renal_cat, 'N/A'))
        with col3:
            if result.get('icu_factor', 1.0) > 1.0:
                st.metric("Hệ số ICU", f"x{result['icu_factor']:.2f}")
        
        # Adjustment recommendation
        st.success(f"**💡 Khuyến cáo:** {result['adjustment']}")
        
        # Detailed dose calculation
        height_default = 170  # Default for quick calc
        sex_default = "Nam"
        ibw = calculate_ibw(height_default, sex_default)
        bmi = calculate_bmi(weight_used, height_default)
        is_obese = bmi > 30 or weight_used > ibw * 1.25
        abw = calculate_abw(weight_used, ibw) if is_obese else weight_used
        
        detailed = calculate_detailed_dose(
            ab_name, weight_used, ibw, abw, crcl_used,
            indication=st.session_state.get(f"{key_prefix}dosing_indication", "standard"),
            is_pediatric=False
        )
        
        if detailed and detailed.get('calculated_dose_mg'):
            st.markdown("#### 💉 Liều Tính Được:")
            col1, col2 = st.columns(2)
            with col1:
                st.info(f"**Liều:** {detailed['calculated_dose_mg']:.0f} mg")
            with col2:
                if detailed.get('interval_hours'):
                    st.info(f"**Khoảng cách:** Mỗi {detailed['interval_hours']:.0f} giờ")
        
        # Full renal guide
        if result.get('full_renal_guide'):
            with st.expander("📋 Bảng Điều Chỉnh Đầy Đủ", expanded=False):
                renal_guide = result['full_renal_guide']
                renal_table = []
                
                if 'normal' in renal_guide:
                    renal_table.append({"CrCl": "≥ 60", "Điều chỉnh": renal_guide['normal']})
                if '30_60' in renal_guide:
                    renal_table.append({"CrCl": "30-59", "Điều chỉnh": renal_guide['30_60']})
                if '15_30' in renal_guide:
                    renal_table.append({"CrCl": "15-29", "Điều chỉnh": renal_guide['15_30']})
                if 'under_15' in renal_guide:
                    renal_table.append({"CrCl": "< 15", "Điều chỉnh": renal_guide['under_15']})
                
                if renal_table:
                    st.dataframe(pd.DataFrame(renal_table), use_container_width=True, hide_index=True)
        
        # Link to full calculator
        st.info("💡 **Cần tính chi tiết hơn?** Dùng công cụ **'🧮 Tính Liều Theo eGFR/CrCl'** ở menu để nhập đầy đủ thông tin (chiều cao, giới tính, ICU, HD, etc.)")
        
        # Clear button
        if st.button("🗑️ Xóa kết quả", key=f"{key_prefix}clear_result"):
            keys_to_remove = [
                f"{key_prefix}dosing_result",
                f"{key_prefix}dosing_weight",
                f"{key_prefix}dosing_crcl",
                f"{key_prefix}dosing_indication"
            ]
            for key in keys_to_remove:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()


def display_antibiotic_info(ab_name, ab_data):
    """Display detailed antibiotic information in expandable format"""
    
    with st.expander(f"💊 **{ab_name}** - Thông tin chi tiết", expanded=True):
        # Header info
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if 'vietnamese_name' in ab_data:
                st.markdown(f"**Tên biệt dược:** {ab_data['vietnamese_name']}")
            
            if 'group' in ab_data:
                st.markdown(f"**Nhóm:** {ab_data['group']}")
        
        with col2:
            if 'administration' in ab_data:
                admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
                admin_display = " / ".join([f"{admin_icons.get(route, '')} {route}" for route in ab_data['administration']])
                st.markdown(f"**Đường dùng:** {admin_display}")
            
            if 'aware_classification' in ab_data:
                aware_colors = {"ACCESS": "🟢", "WATCH": "🟡", "RESERVE": "🔴"}
                aware_name = ab_data['aware_classification']
                st.markdown(f"**AWaRe:** {aware_colors.get(aware_name, '')} {aware_name}")
        
        st.markdown("---")
        
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
        
        # Dosage - Compact layout
        if 'dosage' in ab_data:
            st.markdown("### 💉 Liều dùng:")
            
            dosage = ab_data['dosage']
            
            # Adult dosages
            adult_doses = []
            if 'adult_iv' in dosage:
                adult_doses.append(f"**IV:** {dosage['adult_iv']}")
            if 'adult_im' in dosage:
                adult_doses.append(f"**IM:** {dosage['adult_im']}")
            if 'adult_po' in dosage:
                adult_doses.append(f"**PO:** {dosage['adult_po']}")
            if 'adult_standard' in dosage:
                adult_doses.append(f"**Liều chuẩn:** {dosage['adult_standard']}")
            if 'adult_severe' in dosage:
                adult_doses.append(f"**Nhiễm khuẩn nặng:** {dosage['adult_severe']}")
            
            if adult_doses:
                col1, col2 = st.columns(2)
                mid = len(adult_doses) // 2 + len(adult_doses) % 2
                for i, dose in enumerate(adult_doses[:mid]):
                    with col1:
                        st.info(dose)
                for i, dose in enumerate(adult_doses[mid:], start=mid):
                    with col2:
                        st.info(dose)
            
            # Pediatric dosages
            if 'pediatric_iv' in dosage:
                st.warning(f"**Trẻ em (IV):** {dosage['pediatric_iv']}")
            
            if 'notes' in dosage:
                st.caption(f"💡 {dosage['notes']}")
        
        st.markdown("---")
        
        # Renal adjustment - Table format
        if 'renal_adjustment' in ab_data:
            st.markdown("### 🫘 Điều chỉnh theo chức năng thận:")
            
            renal = ab_data['renal_adjustment']
            renal_data = []
            
            if 'normal' in renal:
                renal_data.append({"CrCl": "≥ 60", "Điều chỉnh": renal['normal']})
            if '30_60' in renal:
                renal_data.append({"CrCl": "30-60", "Điều chỉnh": renal['30_60']})
            if '15_30' in renal:
                renal_data.append({"CrCl": "15-30", "Điều chỉnh": renal['15_30']})
            if 'under_15' in renal:
                renal_data.append({"CrCl": "< 15", "Điều chỉnh": renal['under_15']})
            if 'hemodialysis' in renal:
                renal_data.append({"CrCl": "Lọc máu", "Điều chỉnh": renal['hemodialysis']})
            
            if renal_data:
                st.dataframe(pd.DataFrame(renal_data), use_container_width=True, hide_index=True)
        
        # Side effects
        if 'side_effects' in ab_data:
            st.markdown("### ⚠️ Tác dụng phụ:")
            for se in ab_data['side_effects']:
                st.markdown(f"- {se}")
        
        # Monitoring
        if 'monitoring' in ab_data:
            st.markdown(f"### 📊 Theo dõi: {ab_data['monitoring']}")
        
        # Interactions
        if 'interactions' in ab_data:
            st.markdown("### 🔗 Tương tác thuốc:")
            for inter in ab_data['interactions']:
                st.markdown(f"- {inter}")
        
        # Pregnancy
        if 'pregnancy' in ab_data:
            st.markdown(f"### 🤰 **An toàn thai kỳ:** {ab_data['pregnancy']}")
        
        # Integrated Quick Dosing Calculator
        st.markdown("---")
        render_quick_dosing_calculator(ab_name, ab_data, key_prefix=f"info_{ab_name}_")


def render_database():
    """Unified Antibiotic Database - Search, Browse, Detail View, and Integrated Dosing Calculator"""
    
    ab_count = len(ANTIBIOTICS_DATABASE)
    
    # Modern header with gradient
    st.markdown(f"""
    <div style='
        background: linear-gradient(135deg, #0EA5E9 0%, #0288D1 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.2em;'>🔍 Tra Cứu & Dữ Liệu Kháng Sinh</h1>
        <p style='margin: 10px 0 0 0; color: rgba(255,255,255,0.9); font-size: 1.1em;'>
            Database <strong>{ab_count}</strong> kháng sinh tiêm truyền thông dụng • Tích hợp tính liều tự động
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick info
    with st.expander("ℹ️ Thông tin về database", expanded=False):
        st.info(f"""
        **Cơ sở dữ liệu bao gồm:**
        - ✅ {ab_count} kháng sinh tiêm truyền (IV/IM) thông dụng tại Việt Nam
        - ✅ Tên biệt dược và tên chung
        - ✅ Liều dùng chi tiết (người lớn, trẻ em, nhiễm khuẩn nặng)
        - ✅ Điều chỉnh theo chức năng thận/gan
        - ✅ Chỉ định, chống chỉ định, tác dụng phụ
        - ✅ Tương tác thuốc và phân loại AWaRe
        - ✅ Dựa trên guidelines: IDSA, ASHP, WHO AWaRe 2023
        """)
    
    st.markdown("---")
    
    # ========== SEARCH & FILTER SECTION ==========
    st.markdown("### 🔍 Tìm Kiếm")
    
    # Enhanced search with autocomplete suggestions
    search_query = st.text_input(
        "🔍 Tìm kiếm kháng sinh:",
        placeholder="Nhập tên thuốc, biệt dược, nhóm, hoặc chỉ định...",
        key="ab_search_main",
        help="Tìm kiếm theo tên kháng sinh, tên biệt dược, nhóm thuốc, hoặc chỉ định lâm sàng"
    )
    
    # Show autocomplete suggestions
    if search_query and len(search_query) >= 1:
        suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
        if suggestions:
            st.caption("💡 **Gợi ý:**")
            suggestion_cols = st.columns(min(5, len(suggestions)))
            for idx, suggestion in enumerate(suggestions):
                with suggestion_cols[idx]:
                    if st.button(suggestion, key=f"autocomplete_{suggestion}", use_container_width=True):
                        st.session_state.ab_search_main = suggestion
                        st.rerun()
    
    # Recent searches
    recent_searches = get_recent_searches()
    if recent_searches and not search_query:
        st.caption("🕐 **Tìm kiếm gần đây:**")
        recent_cols = st.columns(min(5, len(recent_searches)))
        for idx, recent in enumerate(recent_searches[:5]):
            with recent_cols[idx]:
                if st.button(f"↩️ {recent}", key=f"recent_{recent}", use_container_width=True):
                    st.session_state.ab_search_main = recent
                    st.rerun()
    
    # View mode selector
    view_mode = st.radio(
        "Chế độ:",
        ["🔍 Tìm kiếm", "📋 Duyệt tất cả"],
        key="view_mode",
        help="Chế độ tìm kiếm hoặc duyệt toàn bộ danh sách",
        horizontal=True
    )
    
    # Filters (only for browse mode)
    if view_mode == "📋 Duyệt tất cả":
        st.markdown("**🔽 Bộ lọc:**")
        col1, col2, col3 = st.columns(3)
        
        all_groups = sorted(list(set([ab.get('group', 'Khác') for ab in ANTIBIOTICS_DATABASE.values()])))
        
        with col1:
            filter_group = st.selectbox(
                "Nhóm:",
                ["Tất cả"] + all_groups,
                key="filter_group_main"
            )
        
        with col2:
            filter_route = st.selectbox(
                "Đường dùng:",
                ["Tất cả", "IV", "IM", "PO"],
                key="filter_route_main"
            )
        
        with col3:
            filter_aware = st.selectbox(
                "AWaRe:",
                ["Tất cả", "ACCESS", "WATCH", "RESERVE"],
                key="filter_aware_main"
            )
    
    st.markdown("---")
    
    # ========== RESULTS SECTION ==========
    
    # Handle view antibiotic from session state
    if 'view_antibiotic' in st.session_state:
        selected_ab = st.session_state['view_antibiotic']
        if selected_ab in ANTIBIOTICS_DATABASE:
            st.markdown("### 📖 Thông tin chi tiết")
            display_antibiotic_info(selected_ab, ANTIBIOTICS_DATABASE[selected_ab])
            st.markdown("---")
            if st.button("⬅️ Quay lại danh sách"):
                del st.session_state['view_antibiotic']
                st.rerun()
            return
    
    # Search mode
    if view_mode == "🔍 Tìm kiếm":
        if search_query:
            # Add to recent searches
            add_to_recent_searches(search_query)
            
            results = search_antibiotics(search_query)
            
            if results:
                st.success(f"✅ Tìm thấy **{len(results)}** kết quả cho '{search_query}'")
                st.markdown("---")
                
                # Display compact list
                for idx, (ab_name, ab_data) in enumerate(results):
                    render_compact_antibiotic_card(ab_name, ab_data, key_prefix=f"search_{idx}_")
                    if idx < len(results) - 1:
                        st.markdown("<hr style='margin: 10px 0; border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)
            else:
                st.warning(f"❌ Không tìm thấy kết quả nào cho '{search_query}'")
                
                # Show autocomplete suggestions as fallback
                suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
                if suggestions:
                    st.info("💡 **Gợi ý tìm kiếm:**")
                    sugg_cols = st.columns(min(5, len(suggestions)))
                    for idx, suggestion in enumerate(suggestions):
                        with sugg_cols[idx]:
                            if st.button(suggestion, key=f"sugg_{suggestion}", use_container_width=True):
                                st.session_state.ab_search_main = suggestion
                                st.rerun()
                else:
                    st.info("💡 **Gợi ý:** Thử tìm với tên thuốc, biệt dược, nhóm thuốc (ví dụ: Beta-lactam), hoặc chỉ định (ví dụ: MRSA, Sepsis, UTI)")
        else:
            # Empty state with popular searches
            st.info("👆 **Nhập từ khóa để tìm kiếm** (ví dụ: Vancomycin, Ceftriaxone, MRSA, Sepsis)")
            st.markdown("---")
            
            # Show popular/quick links
            st.markdown("### ⚡ Truy cập nhanh:")
            popular = ["Vancomycin", "Ceftriaxone", "Piperacillin-Tazobactam", "Meropenem", "Levofloxacin"]
            cols = st.columns(len(popular))
            for col, ab_name in zip(cols, popular):
                if ab_name in ANTIBIOTICS_DATABASE:
                    with col:
                        if st.button(f"💊 {ab_name}", key=f"quick_{ab_name}", use_container_width=True):
                            st.session_state['view_antibiotic'] = ab_name
                            add_to_recent_searches(ab_name)
                            st.rerun()
    
    # Browse mode
    else:
        # Apply filters
        filtered_ab = filter_antibiotics(
            filter_group if view_mode == "📋 Duyệt tất cả" else "Tất cả",
            filter_route if view_mode == "📋 Duyệt tất cả" else "Tất cả",
            filter_aware if view_mode == "📋 Duyệt tất cả" else "Tất cả"
        )
        
        if filtered_ab:
            st.success(f"📋 Hiển thị **{len(filtered_ab)}** kháng sinh")
            st.markdown("---")
            
            # Display as compact list
            st.markdown("### 📚 Danh sách kháng sinh:")
            
            # Group by category for better organization
            groups_dict = {}
            for ab_name, ab_data in filtered_ab.items():
                group = ab_data.get('group', 'Khác')
                if group not in groups_dict:
                    groups_dict[group] = []
                groups_dict[group].append((ab_name, ab_data))
            
            # Display by group
            for group in sorted(groups_dict.keys()):
                if len(groups_dict) > 1:
                    st.markdown(f"#### {group} ({len(groups_dict[group])} thuốc)")
                
                for idx, (ab_name, ab_data) in enumerate(sorted(groups_dict[group], key=lambda x: x[0])):
                    render_compact_antibiotic_card(ab_name, ab_data, key_prefix=f"browse_{group}_{idx}_")
                    if idx < len(groups_dict[group]) - 1:
                        st.markdown("<hr style='margin: 8px 0; border: none; border-top: 1px solid #f0f0f0;'>", unsafe_allow_html=True)
                
                if group != list(groups_dict.keys())[-1]:
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.warning("❌ Không có kháng sinh nào thỏa mãn bộ lọc")
            if st.button("🔄 Xóa bộ lọc"):
                st.rerun()


def render_antibiotic_lookup():
    """Legacy function - redirects to render_database for backward compatibility"""
    render_database()
