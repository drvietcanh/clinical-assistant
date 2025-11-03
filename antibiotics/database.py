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


def _escape_html(text):
    """Escape HTML special characters to prevent rendering issues"""
    if not text:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;"))


def render_compact_antibiotic_card(ab_name, ab_data, key_prefix=""):
    """Render an enhanced compact card for antibiotic list view with modern UI"""
    import html
    
    vn_name = ab_data.get('vietnamese_name', '').split(',')[0] if ab_data.get('vietnamese_name') else ''
    admin = ab_data.get('administration', [])
    aware = ab_data.get('aware_classification', '')
    # Check if has dosing calculator (from any antibiotics with dosing support)
    has_calc = ab_data.get('has_dosing_calculator', False) or ab_name in ["Vancomycin", "Gentamicin", "Amikacin", "Tobramycin"]
    group = ab_data.get('group', 'Khác')
    indications = ab_data.get('indications', [])
    
    # Escape all text to prevent HTML rendering issues
    ab_name_escaped = html.escape(ab_name)
    vn_name_escaped = html.escape(vn_name) if vn_name else ""
    group_escaped = html.escape(group)
    
    # Admin icons with labels
    admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
    admin_display = []
    for a in admin[:3]:
        icon = admin_icons.get(a, "")
        admin_display.append(f"{icon} {a}" if icon else a)
    admin_str = " • ".join(admin_display) if admin_display else "N/A"
    admin_str_escaped = html.escape(admin_str)
    
    # AWaRe badge with tooltip
    aware_colors = {
        "ACCESS": {"bg": "#4CAF50", "icon": "🟢"},
        "WATCH": {"bg": "#FF9800", "icon": "🟡"},
        "RESERVE": {"bg": "#F44336", "icon": "🔴"}
    }
    aware_badge = ""
    if aware and aware in aware_colors:
        badge_info = aware_colors[aware]
        aware_badge = f'''<span style="background-color: {badge_info["bg"]}; color: white; padding: 3px 10px; border-radius: 15px; font-size: 0.75em; font-weight: bold; margin-left: 8px; display: inline-flex; align-items: center; gap: 4px;" title="WHO AWaRe: {aware}">{badge_info["icon"]} {aware}</span>'''
    
    # Calculator badge
    calc_badge = ""
    if has_calc:
        calc_badge = '<span style="background: linear-gradient(135deg, #9C27B0 0%, #7B1FA2 100%); color: white; padding: 3px 10px; border-radius: 15px; font-size: 0.75em; font-weight: bold; margin-left: 6px; display: inline-flex; align-items: center; gap: 4px;" title="Có máy tính liều dùng">🧮 Tính liều</span>'
    
    # Check if favorite
    favorites = st.session_state.get('antibiotic_favorites', [])
    is_favorite = ab_name in favorites
    favorite_icon = "⭐" if is_favorite else "☆"
    
    # Enhanced card with hover effect and better styling
    card_html = f"""
    <div style='
        background: linear-gradient(to bottom, #ffffff 0%, #fafafa 100%);
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 16px 18px;
        margin: 10px 0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        cursor: pointer;
    ' onmouseover="this.style.boxShadow='0 4px 12px rgba(25,118,210,0.15)'; this.style.transform='translateY(-2px)'; this.style.borderColor='#1976D2';" 
       onmouseout="this.style.boxShadow='0 2px 4px rgba(0,0,0,0.08)'; this.style.transform='translateY(0)'; this.style.borderColor='#e0e0e0';">
        <div style='display: flex; justify-content: space-between; align-items: start; gap: 12px;'>
            <div style='flex: 1; min-width: 0;'>
                <div style='display: flex; align-items: center; flex-wrap: wrap; margin-bottom: 8px; gap: 6px;'>
                    <strong style='color: #1976D2; font-size: 1.15em; margin-right: 4px; font-weight: 600;'>{ab_name_escaped}</strong>
                    {aware_badge}
                    {calc_badge}
                    <span style='color: #999; font-size: 0.85em; margin-left: auto; cursor: pointer;' title="Yêu thích" id="fav_{key_prefix}_{ab_name_escaped}">{favorite_icon}</span>
                </div>
                {f"<div style='color: #666; font-size: 0.9em; margin-bottom: 6px; font-style: italic;'>{vn_name_escaped}</div>" if vn_name else ""}
                <div style='color: #888; font-size: 0.88em; line-height: 1.5;'>
                    <span style='font-weight: 500;'>{admin_str_escaped}</span>
                    <span style='color: #ccc; margin: 0 8px;'>|</span>
                    <span style='color: #666;'>{group_escaped}</span>
                </div>
                {f"<div style='color: #999; font-size: 0.8em; margin-top: 6px; line-height: 1.4;'><span style='color: #666;'>💡 </span>{html.escape(indications[0] if indications else '')}</div>" if indications else ""}
            </div>
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
    
    # Button row with enhanced actions
    col1, col2, col3 = st.columns([2, 2, 1])
    
    # Sanitize ab_name for keys (remove special characters that might cause issues)
    safe_ab_name = str(ab_name).replace(" ", "_").replace("-", "_").replace("/", "_")
    
    with col1:
        detail_key = f"{key_prefix}detail_{safe_ab_name}" if key_prefix else f"detail_{safe_ab_name}"
        if st.button("📖 Chi tiết", key=detail_key, use_container_width=True, type="primary"):
            st.session_state['view_antibiotic'] = str(ab_name)  # Ensure it's a string
            # Track recently viewed
            if 'recently_viewed_antibiotics' not in st.session_state:
                st.session_state.recently_viewed_antibiotics = []
            recent = st.session_state.recently_viewed_antibiotics
            if ab_name in recent:
                recent.remove(ab_name)
            recent.insert(0, ab_name)
            st.session_state.recently_viewed_antibiotics = recent[:10]
            st.rerun()
    
    with col2:
        if has_calc:
            calc_key = f"{key_prefix}calc_{safe_ab_name}" if key_prefix else f"calc_{safe_ab_name}"
            if st.button("🧮 Tính liều", key=calc_key, use_container_width=True):
                st.session_state['view_antibiotic'] = str(ab_name)  # Ensure it's a string
                st.session_state['auto_open_dosing'] = True
                st.rerun()
    
    with col3:
        # Favorite toggle
        fav_key = f"{key_prefix}fav_{safe_ab_name}" if key_prefix else f"fav_{safe_ab_name}"
        if is_favorite:
            if st.button("⭐", key=fav_key, use_container_width=True, help="Bỏ yêu thích"):
                favorites.remove(ab_name)
                st.session_state.antibiotic_favorites = favorites
                st.rerun()
        else:
            if st.button("☆", key=fav_key, use_container_width=True, help="Thêm yêu thích"):
                favorites.append(ab_name)
                st.session_state.antibiotic_favorites = favorites
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
    """Display detailed antibiotic information with export and quick actions"""
    
    # Initialize favorites if not exists
    if 'antibiotic_favorites' not in st.session_state:
        st.session_state.antibiotic_favorites = []
    
    favorites = st.session_state.antibiotic_favorites
    is_favorite = ab_name in favorites
    
    # Quick Actions Toolbar
    col_actions = st.columns([1, 1, 1, 1, 1, 5])
    with col_actions[0]:
        # Sanitize ab_name for keys
        safe_detail_name = str(ab_name).replace(" ", "_").replace("-", "_").replace("/", "_")
        
        if is_favorite:
            if st.button("⭐", key=f"fav_detail_{safe_detail_name}", help="Bỏ yêu thích"):
                favorites.remove(ab_name)
                st.session_state.antibiotic_favorites = favorites
                st.rerun()
        else:
            if st.button("☆", key=f"fav_detail_{safe_detail_name}", help="Thêm yêu thích"):
                favorites.append(ab_name)
                st.session_state.antibiotic_favorites = favorites
                st.rerun()
    
    with col_actions[4]:
        # Export button - will show expander below
        show_export = st.button("📤 Export", key=f"export_btn_{safe_detail_name}", help="Xuất thông tin")
    
    # Main content in expander
    with st.expander(f"💊 **{ab_name}** - Thông tin chi tiết", expanded=True):
        # Header info with modern card
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); padding: 20px; border-radius: 12px; margin-bottom: 15px;'>
            <div style='display: flex; justify-content: space-between; align-items: start;'>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if 'vietnamese_name' in ab_data:
                st.markdown(f"**🏷️ Tên biệt dược:** {ab_data['vietnamese_name']}")
            
            if 'group' in ab_data:
                st.markdown(f"**📦 Nhóm:** {ab_data['group']}")
        
        with col2:
            if 'administration' in ab_data:
                admin_icons = {"IV": "💉", "IM": "💊", "PO": "🍽️", "Inhalation": "🌬️"}
                admin_display = " / ".join([f"{admin_icons.get(route, '')} {route}" for route in ab_data['administration']])
                st.markdown(f"**💉 Đường dùng:** {admin_display}")
            
            if 'aware_classification' in ab_data:
                aware_colors = {"ACCESS": "🟢", "WATCH": "🟡", "RESERVE": "🔴"}
                aware_name = ab_data['aware_classification']
                st.markdown(f"**🌐 AWaRe:** {aware_colors.get(aware_name, '')} {aware_name}")
        
        st.markdown("</div>", unsafe_allow_html=True)
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
        
        # Auto-open dosing if requested
        auto_open = st.session_state.get('auto_open_dosing', False)
        if auto_open:
            st.session_state['auto_open_dosing'] = False
        
        render_quick_dosing_calculator(ab_name, ab_data, key_prefix=f"info_{ab_name}_")
        
        # Export section
        if show_export:
            st.markdown("---")
            _render_antibiotic_export(ab_name, ab_data)


def _render_antibiotic_export(ab_name, ab_data):
    """Render export section for antibiotic information"""
    from datetime import datetime
    import html
    
    lines = []
    lines.append("=" * 70)
    lines.append(f"THÔNG TIN KHÁNG SINH - {ab_name}")
    lines.append("=" * 70)
    lines.append(f"Ngày xuất: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("-" * 70)
    
    # Basic info
    lines.append(f"\n📋 THÔNG TIN CƠ BẢN:")
    if 'vietnamese_name' in ab_data:
        lines.append(f"  Tên biệt dược: {ab_data['vietnamese_name']}")
    if 'group' in ab_data:
        lines.append(f"  Nhóm: {ab_data['group']}")
    if 'administration' in ab_data:
        lines.append(f"  Đường dùng: {', '.join(ab_data['administration'])}")
    if 'aware_classification' in ab_data:
        lines.append(f"  AWaRe: {ab_data['aware_classification']}")
    
    # Indications
    if 'indications' in ab_data:
        lines.append(f"\n📋 CHỈ ĐỊNH:")
        for ind in ab_data['indications']:
            lines.append(f"  • {ind}")
    
    # Contraindications
    if 'contraindications' in ab_data:
        lines.append(f"\n⛔ CHỐNG CHỈ ĐỊNH:")
        for contr in ab_data['contraindications']:
            lines.append(f"  • {contr}")
    
    # Dosage
    if 'dosage' in ab_data:
        lines.append(f"\n💉 LIỀU DÙNG:")
        dosage = ab_data['dosage']
        if 'adult_iv' in dosage:
            lines.append(f"  IV: {dosage['adult_iv']}")
        if 'adult_im' in dosage:
            lines.append(f"  IM: {dosage['adult_im']}")
        if 'adult_po' in dosage:
            lines.append(f"  PO: {dosage['adult_po']}")
        if 'adult_standard' in dosage:
            lines.append(f"  Liều chuẩn: {dosage['adult_standard']}")
        if 'adult_severe' in dosage:
            lines.append(f"  Nhiễm khuẩn nặng: {dosage['adult_severe']}")
        if 'pediatric_iv' in dosage:
            lines.append(f"  Trẻ em (IV): {dosage['pediatric_iv']}")
    
    # Renal adjustment
    if 'renal_adjustment' in ab_data:
        lines.append(f"\n🫘 ĐIỀU CHỈNH THEO CHỨC NĂNG THẬN:")
        renal = ab_data['renal_adjustment']
        if 'normal' in renal:
            lines.append(f"  CrCl ≥ 60: {renal['normal']}")
        if '30_60' in renal:
            lines.append(f"  CrCl 30-60: {renal['30_60']}")
        if '15_30' in renal:
            lines.append(f"  CrCl 15-30: {renal['15_30']}")
        if 'under_15' in renal:
            lines.append(f"  CrCl < 15: {renal['under_15']}")
    
    # Side effects
    if 'side_effects' in ab_data:
        lines.append(f"\n⚠️ TÁC DỤNG PHỤ:")
        for se in ab_data['side_effects']:
            lines.append(f"  • {se}")
    
    # Monitoring
    if 'monitoring' in ab_data:
        lines.append(f"\n📊 THEO DÕI: {ab_data['monitoring']}")
    
    # Interactions
    if 'interactions' in ab_data:
        lines.append(f"\n🔗 TƯƠNG TÁC THUỐC:")
        for inter in ab_data['interactions']:
            lines.append(f"  • {inter}")
    
    # Pregnancy
    if 'pregnancy' in ab_data:
        lines.append(f"\n🤰 AN TOÀN THAI KỲ: {ab_data['pregnancy']}")
    
    lines.append("\n" + "=" * 70)
    lines.append("⚠️ Lưu ý: Thông tin chỉ mang tính tham khảo")
    lines.append("   Không thay thế đánh giá lâm sàng của bác sĩ")
    lines.append("=" * 70)
    
    export_text = "\n".join(lines)
    
    with st.expander("📤 Export Thông Tin", expanded=True):
        st.markdown("**Preview:**")
        st.code(export_text, language="text")
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.code(export_text, language="text")
            st.success("✅ Chọn và copy text từ khung trên để copy vào clipboard")
        
        with col2:
            # Sanitize ab_name for filename and key
            safe_filename = str(ab_name).replace(' ', '_').replace('-', '_').replace('/', '_')
            safe_download_key = f"download_{safe_filename}"
            filename = f"antibiotic_{safe_filename}"
            st.download_button(
                label="💾 Download TXT",
                data=export_text,
                file_name=f"{filename}.txt",
                mime="text/plain",
                use_container_width=True,
                key=safe_download_key
            )


def render_database():
    """Unified Antibiotic Database - Search, Browse, Detail View, and Integrated Dosing Calculator"""
    
    # Initialize session state
    if 'antibiotic_favorites' not in st.session_state:
        st.session_state.antibiotic_favorites = []
    if 'recently_viewed_antibiotics' not in st.session_state:
        st.session_state.recently_viewed_antibiotics = []
    
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
    
    # Quick info and tabs
    tab_info, tab_favorites, tab_recent = st.tabs(["ℹ️ Database", "⭐ Yêu thích", "🕐 Gần đây"])
    
    with tab_info:
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
    
    with tab_favorites:
        favorites = st.session_state.antibiotic_favorites
        if favorites:
            st.success(f"Bạn có **{len(favorites)}** kháng sinh yêu thích")
            st.markdown("---")
            for ab_name in favorites:
                if ab_name in ANTIBIOTICS_DATABASE:
                    render_compact_antibiotic_card(ab_name, ANTIBIOTICS_DATABASE[ab_name], key_prefix=f"fav_{ab_name}_")
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.info("💡 Chưa có kháng sinh yêu thích. Nhấn ☆ trên card để thêm vào danh sách yêu thích!")
    
    with tab_recent:
        recent = st.session_state.recently_viewed_antibiotics
        if recent:
            st.success(f"Đã xem **{len(recent)}** kháng sinh gần đây")
            st.markdown("---")
            for ab_name in recent:
                if ab_name in ANTIBIOTICS_DATABASE:
                    render_compact_antibiotic_card(ab_name, ANTIBIOTICS_DATABASE[ab_name], key_prefix=f"recent_{ab_name}_")
                    st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.info("💡 Chưa có kháng sinh nào được xem gần đây")
    
    st.markdown("---")
    
    # ========== SEARCH & FILTER SECTION ==========
    st.markdown("### 🔍 Tìm Kiếm")
    
    # Enhanced search with better UI
    col_search, col_clear = st.columns([5, 1])
    
    with col_search:
        search_query = st.text_input(
            "🔍 Tìm kiếm kháng sinh:",
            placeholder="Nhập tên thuốc, biệt dược, nhóm, hoặc chỉ định...",
            key="ab_search_main",
            help="Tìm kiếm theo tên kháng sinh, tên biệt dược, nhóm thuốc, hoặc chỉ định lâm sàng",
            label_visibility="collapsed"
        )
    
    with col_clear:
        if st.button("🗑️", help="Xóa tìm kiếm", use_container_width=True):
            st.session_state.ab_search_main = ""
            st.rerun()
    
    # Show autocomplete suggestions in a nicer format
    if search_query and len(search_query) >= 1:
        suggestions = get_antibiotic_autocomplete_suggestions(search_query, max_suggestions=5)
        if suggestions:
            st.markdown("**💡 Gợi ý tìm kiếm:**")
            suggestion_cols = st.columns(min(5, len(suggestions)))
            for idx, suggestion in enumerate(suggestions):
                with suggestion_cols[idx]:
                    if st.button(f"💊 {suggestion}", key=f"autocomplete_{suggestion}", use_container_width=True):
                        st.session_state.ab_search_main = suggestion
                        add_to_recent_searches(suggestion)
                        st.rerun()
            st.markdown("<br>", unsafe_allow_html=True)
    
    # Recent searches (when no query)
    recent_searches = get_recent_searches()
    if recent_searches and not search_query:
        st.markdown("**🕐 Tìm kiếm gần đây:**")
        recent_cols = st.columns(min(5, len(recent_searches)))
        for idx, recent in enumerate(recent_searches[:5]):
            with recent_cols[idx]:
                if st.button(f"↩️ {recent}", key=f"recent_search_{recent}", use_container_width=True):
                    st.session_state.ab_search_main = recent
                    st.rerun()
        st.markdown("<br>", unsafe_allow_html=True)
    
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
                            # Sanitize suggestion for key
                            safe_sugg_key = f"sugg_{str(suggestion).replace(' ', '_').replace('-', '_').replace('/', '_')}"
                            if st.button(suggestion, key=safe_sugg_key, use_container_width=True):
                                st.session_state.ab_search_main = str(suggestion)
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
                        # Sanitize ab_name for key
                        safe_quick_name = str(ab_name).replace(" ", "_").replace("-", "_").replace("/", "_")
                        if st.button(f"💊 {ab_name}", key=f"quick_{safe_quick_name}", use_container_width=True):
                            st.session_state['view_antibiotic'] = str(ab_name)
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
