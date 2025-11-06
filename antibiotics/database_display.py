"""
Antibiotic Database - Display Functions
UI components for displaying antibiotic information
"""

import streamlit as st
import html
import pandas as pd
import re
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .database_calculator import render_quick_dosing_calculator
from .database_export import _render_antibiotic_export

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


def _sanitize_key(text):
    """
    Sanitize text for use in Streamlit session state keys and widget keys.
    Removes or replaces special characters that are not allowed in keys.
    
    Args:
        text: Text to sanitize
        
    Returns:
        Sanitized string safe for use in keys
    """
    if not text:
        return ""
    # Convert to string and replace problematic characters
    safe = str(text)
    # Replace spaces, hyphens, slashes, and other special chars with underscore
    safe = safe.replace(" ", "_").replace("-", "_").replace("/", "_")
    safe = safe.replace("\\", "_").replace("(", "_").replace(")", "_")
    safe = safe.replace("[", "_").replace("]", "_").replace("{", "_")
    safe = safe.replace("}", "_").replace(".", "_").replace(",", "_")
    safe = safe.replace(":", "_").replace(";", "_").replace("!", "_")
    safe = safe.replace("?", "_").replace("@", "_").replace("#", "_")
    safe = safe.replace("$", "_").replace("%", "_").replace("^", "_")
    safe = safe.replace("&", "_").replace("*", "_").replace("+", "_")
    safe = safe.replace("=", "_").replace("|", "_").replace("~", "_")
    # Remove any remaining non-alphanumeric characters except underscore
    safe = re.sub(r'[^a-zA-Z0-9_]', '_', safe)
    # Remove multiple consecutive underscores
    safe = re.sub(r'_+', '_', safe)
    # Remove leading/trailing underscores
    safe = safe.strip('_')
    # Ensure it doesn't start with a number (Streamlit requirement)
    if safe and safe[0].isdigit():
        safe = f"key_{safe}"
    return safe



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
        
        # Sanitize ab_name for key_prefix to avoid session state errors
        safe_ab_name = _sanitize_key(ab_name)
        render_quick_dosing_calculator(ab_name, ab_data, key_prefix=f"info_{safe_ab_name}_")
        
        # Export section
        if show_export:
            st.markdown("---")
            _render_antibiotic_export(ab_name, ab_data)



