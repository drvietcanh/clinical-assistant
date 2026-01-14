"""
Antibiotic Database - Display Functions
UI components for displaying antibiotic information
"""

import streamlit as st
import streamlit.components.v1 as components
import html
import pandas as pd
import re
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .database_calculator import render_quick_dosing_calculator
from .scenario_dosing_calculator import render_scenario_dosing_calculator
from .database_export import _render_antibiotic_export
from .mic_breakpoints import get_mic_breakpoints, get_common_susceptibility
from .resistance_patterns import get_antibiotic_resistance_summary

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
    Streamlit keys must: start with letter/underscore, contain only alphanumeric/underscore.
    
    Args:
        text: Text to sanitize
        
    Returns:
        Sanitized string safe for use in keys
    """
    if not text:
        return "key"
    
    # Convert to string and normalize Unicode
    safe = str(text)
    
    # Remove all non-ASCII characters first (Unicode normalization)
    safe = safe.encode('ascii', 'ignore').decode('ascii')
    
    # Replace all non-alphanumeric characters with underscore
    safe = re.sub(r'[^a-zA-Z0-9]', '_', safe)
    
    # Remove multiple consecutive underscores
    safe = re.sub(r'_+', '_', safe)
    
    # Remove leading/trailing underscores
    safe = safe.strip('_')
    
    # Ensure it doesn't start with a number (Streamlit requirement)
    if safe and safe[0].isdigit():
        safe = f"key_{safe}"
    
    # Ensure minimum length and valid characters only
    if not safe or len(safe) == 0:
        safe = "key"
    
    # Limit length to prevent issues (Streamlit has key length limits, typically 200 chars)
    # Use 80 chars to be safe and leave room for suffixes
    if len(safe) > 80:
        safe = safe[:80]
    
    # Final validation: ensure only valid characters (should already be done, but double-check)
    safe = re.sub(r'[^a-zA-Z0-9_]', '', safe)
    
    # Final check: ensure it starts with letter or underscore
    if safe and safe[0].isdigit():
        safe = f"key_{safe}"
    
    return safe


def _make_safe_session_key(prefix, suffix=""):
    """
    Create a safe session state key from prefix and suffix.
    Ensures the entire key is valid for Streamlit session state.
    
    Args:
        prefix: Key prefix (will be sanitized)
        suffix: Key suffix (will be sanitized)
        
    Returns:
        Safe session state key
    """
    # Sanitize both parts
    safe_prefix = _sanitize_key(prefix) if prefix else "key"
    safe_suffix = _sanitize_key(suffix) if suffix else ""
    
    # Combine with underscore
    if safe_suffix:
        full_key = f"{safe_prefix}_{safe_suffix}"
    else:
        full_key = safe_prefix
    
    # Final validation
    full_key = re.sub(r'[^a-zA-Z0-9_]', '', full_key)
    full_key = re.sub(r'_+', '_', full_key)
    full_key = full_key.strip('_')
    
    # Ensure it doesn't start with number
    if full_key and full_key[0].isdigit():
        full_key = f"key_{full_key}"
    
    # Ensure minimum length
    if not full_key:
        full_key = "key"
    
    # Limit total length
    if len(full_key) > 150:
        full_key = full_key[:150]
    
    return full_key



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
    
    # AWaRe badge with enhanced color coding and tooltip
    aware_colors = {
        "ACCESS": {
            "bg": "linear-gradient(135deg, #4CAF50 0%, #45a049 100%)",
            "icon": "🟢",
            "shadow": "0 2px 8px rgba(76, 175, 80, 0.3)"
        },
        "WATCH": {
            "bg": "linear-gradient(135deg, #FF9800 0%, #F57C00 100%)",
            "icon": "🟡",
            "shadow": "0 2px 8px rgba(255, 152, 0, 0.3)"
        },
        "RESERVE": {
            "bg": "linear-gradient(135deg, #F44336 0%, #D32F2F 100%)",
            "icon": "🔴",
            "shadow": "0 2px 8px rgba(244, 67, 54, 0.3)"
        }
    }
    aware_badge = ""
    if aware and aware in aware_colors:
        badge_info = aware_colors[aware]
        aware_badge = f'''<span style="background: {badge_info["bg"]}; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.75em; font-weight: 700; margin-left: 8px; display: inline-flex; align-items: center; gap: 5px; box-shadow: {badge_info["shadow"]}; letter-spacing: 0.3px;" title="WHO AWaRe Classification: {aware}">{badge_info["icon"]} {aware}</span>'''
    
    # Calculator badge with enhanced styling
    calc_badge = ""
    if has_calc:
        calc_badge = '<span style="background: linear-gradient(135deg, #9C27B0 0%, #7B1FA2 100%); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.75em; font-weight: 700; margin-left: 6px; display: inline-flex; align-items: center; gap: 5px; box-shadow: 0 2px 8px rgba(156, 39, 176, 0.3); letter-spacing: 0.3px;" title="Có tính toán liều dùng tích hợp">🧮 Tính liều</span>'
    
    # Check if favorite
    favorites = st.session_state.get('antibiotic_favorites', [])
    is_favorite = ab_name in favorites
    favorite_icon = "⭐" if is_favorite else "☆"
    
    # Enhanced card with modern design: 16px border-radius, better shadows, 20px padding
    # Build HTML string carefully to avoid quote conflicts
    vn_name_html = f"<div style='color: #666; font-size: 0.95em; margin-bottom: 8px; font-style: italic; font-weight: 400;'>{vn_name_escaped}</div>" if vn_name else ""
    indication_html = ""
    if indications:
        indication_text = html.escape(indications[0] if indications else '')
        indication_html = f"<div style='color: #777; font-size: 0.85em; margin-top: 8px; line-height: 1.5; padding: 8px 12px; background: rgba(25,118,210,0.05); border-radius: 8px; border-left: 3px solid #1976D2;'><span style='color: #1976D2; font-weight: 600;'>💡 </span>{indication_text}</div>"
    
    # Escape key_prefix for use in HTML id attribute
    safe_key_prefix = html.escape(str(key_prefix).replace(" ", "_").replace("-", "_"))
    safe_ab_name_for_id = html.escape(str(ab_name).replace(" ", "_").replace("-", "_"))
    
    # Build card HTML in parts to avoid quote conflicts
    card_style = "background: linear-gradient(to bottom, #ffffff 0%, #f8f9fa 100%); border: 1.5px solid #e0e0e0; border-radius: 16px; padding: 20px 22px; margin: 12px 0; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: 0 2px 8px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.05); cursor: pointer; position: relative; overflow: hidden;"
    hover_on = "this.style.boxShadow='0 8px 24px rgba(25,118,210,0.15), 0 4px 8px rgba(0,0,0,0.1)'; this.style.transform='translateY(-3px)'; this.style.borderColor='#1976D2';"
    hover_off = "this.style.boxShadow='0 2px 8px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.05)'; this.style.transform='translateY(0)'; this.style.borderColor='#e0e0e0';"
    
    card_html = f'<div style="{card_style}" onmouseover="{hover_on}" onmouseout="{hover_off}">'
    card_html += '<div style="display: flex; justify-content: space-between; align-items: start; gap: 14px;">'
    card_html += '<div style="flex: 1; min-width: 0;">'
    card_html += '<div style="display: flex; align-items: center; flex-wrap: wrap; margin-bottom: 10px; gap: 8px;">'
    card_html += f'<strong style="color: #1976D2; font-size: 1.25em; margin-right: 6px; font-weight: 700; letter-spacing: -0.3px;">{ab_name_escaped}</strong>'
    card_html += aware_badge
    card_html += calc_badge
    card_html += f'<span style="color: #999; font-size: 1.1em; margin-left: auto; cursor: pointer; transition: transform 0.2s;" title="Yêu thích" id="fav_{safe_key_prefix}_{safe_ab_name_for_id}" onmouseover="this.style.transform=\'scale(1.2)\'" onmouseout="this.style.transform=\'scale(1)\'">{favorite_icon}</span>'
    card_html += '</div>'
    card_html += vn_name_html
    card_html += '<div style="color: #555; font-size: 0.9em; line-height: 1.6; margin-top: 4px;">'
    card_html += f'<span style="font-weight: 600; color: #1976D2;">{admin_str_escaped}</span>'
    card_html += '<span style="color: #ddd; margin: 0 10px; font-weight: 300;">•</span>'
    card_html += f'<span style="color: #666; font-weight: 500;">{group_escaped}</span>'
    card_html += '</div>'
    card_html += indication_html
    card_html += '</div></div></div>'
    
    components.html(card_html, height=150, scrolling=False)
    
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
                # Log usage
                try:
                    from .analytics import log_usage
                    log_usage("unfavorite", ab_name)
                except ImportError:
                    pass
                st.rerun()
        else:
            if st.button("☆", key=fav_key, use_container_width=True, help="Thêm yêu thích"):
                favorites.append(ab_name)
                st.session_state.antibiotic_favorites = favorites
                # Log usage
                try:
                    from .analytics import log_usage
                    log_usage("favorite", ab_name)
                except ImportError:
                    pass
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
    
    # Main content in expander with enhanced design
    with st.expander(f"💊 **{ab_name}** - Thông tin chi tiết", expanded=True):
        # Enhanced header info card with better visual hierarchy
        st.markdown(f"""
        <div style='
            background: linear-gradient(135deg, #f5f7fa 0%, #e3e8f0 50%, #c3cfe2 100%);
            padding: 24px;
            border-radius: 16px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid rgba(25,118,210,0.1);
        '>
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
                aware_name = ab_data['aware_classification']
                aware_info = {
                    "ACCESS": {"icon": "🟢", "color": "#4CAF50", "bg": "rgba(76, 175, 80, 0.1)"},
                    "WATCH": {"icon": "🟡", "color": "#FF9800", "bg": "rgba(255, 152, 0, 0.1)"},
                    "RESERVE": {"icon": "🔴", "color": "#F44336", "bg": "rgba(244, 67, 54, 0.1)"}
                }
                info = aware_info.get(aware_name, {"icon": "", "color": "#666", "bg": "rgba(0,0,0,0.05)"})
                st.markdown(f"""
                <div style='background: {info["bg"]}; padding: 8px 12px; border-radius: 8px; border-left: 3px solid {info["color"]}; margin-top: 8px;'>
                    <strong style='color: {info["color"]};'>🌐 AWaRe:</strong> <span style='font-weight: 700; color: {info["color"]};'>{info["icon"]} {aware_name}</span>
                </div>
                """, unsafe_allow_html=True)
        
        # End of antibiotic header card
        st.markdown("---")
        
        # Indications with enhanced styling
        if 'indications' in ab_data:
            st.markdown("### 📋 Chỉ định:")
            for ind in ab_data['indications']:
                st.markdown(f"""
                <div style='padding: 8px 12px; margin: 4px 0; background: rgba(76, 175, 80, 0.08); border-left: 3px solid #4CAF50; border-radius: 6px;'>
                    ✓ {ind}
                </div>
                """, unsafe_allow_html=True)
        
        # Contraindications with warning styling
        if 'contraindications' in ab_data:
            st.markdown("### ⛔ Chống chỉ định:")
            for contr in ab_data['contraindications']:
                st.markdown(f"""
                <div style='padding: 8px 12px; margin: 4px 0; background: rgba(244, 67, 54, 0.08); border-left: 3px solid #F44336; border-radius: 6px;'>
                    ❌ {contr}
                </div>
                """, unsafe_allow_html=True)
        
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
        
        # MIC Breakpoints & Susceptibility
        st.markdown("---")
        mic_data = get_mic_breakpoints(ab_name)
        if mic_data:
            st.markdown("### 📊 MIC Breakpoints & Độ nhạy:")
            
            # Common susceptibility
            common_suscept = get_common_susceptibility(ab_name)
            if common_suscept:
                st.markdown("**💡 Độ nhạy thường gặp:**")
                for organism, pattern in common_suscept.items():
                    # Color code based on pattern
                    color = "#FF9800"  # Default
                    try:
                        if "S (" in pattern:
                            # Extract percentage from "S (XX%)" or "S (XX-YY%)"
                            s_part = pattern.split("S (")[1].split("%")[0]
                            # Handle range like "95-98" -> take first value
                            s_val = float(s_part.split("-")[0].strip())
                            if s_val >= 80:
                                color = "#4CAF50"
                        elif "R (" in pattern:
                            # Extract percentage from "R (XX%)" or "R (XX-YY%)"
                            r_part = pattern.split("R (")[1].split("%")[0]
                            # Handle range like "60-70" -> take first value
                            r_val = float(r_part.split("-")[0].strip())
                            if r_val >= 50:
                                color = "#F44336"
                    except (ValueError, IndexError, AttributeError):
                        # If parsing fails, use default color
                        color = "#FF9800"
                    
                    st.markdown(f"""
                    <div style='padding: 6px 10px; margin: 4px 0; background: rgba(25,118,210,0.05); border-left: 3px solid {color}; border-radius: 6px;'>
                        <strong>{organism}:</strong> <span style='color: {color}; font-weight: 600;'>{pattern}</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            # MIC breakpoints table
            if 'organisms' in mic_data:
                st.markdown("**📋 Giá trị MIC (CLSI/EUCAST):**")
                mic_table_data = []
                for organism, breakpoints in mic_data['organisms'].items():
                    mic_table_data.append({
                        "Vi khuẩn": organism,
                        "Nhạy cảm (S)": breakpoints.get('sensitive', 'N/A'),
                        "Trung gian (I)": breakpoints.get('intermediate', 'N/A'),
                        "Kháng (R)": breakpoints.get('resistant', 'N/A')
                    })
                
                if mic_table_data:
                    df_mic = pd.DataFrame(mic_table_data)
                    st.dataframe(df_mic, use_container_width=True, hide_index=True)
        
        # Spectrum Chart (Phase 1 Feature)
        st.markdown("---")
        try:
            from .spectrum_charts import render_spectrum_chart_inline
            st.markdown("### 📊 Phổ Tác Dụng (Biểu Đồ)")
            render_spectrum_chart_inline(ab_name)
        except ImportError:
            pass
        
        # Resistance Patterns (Vietnam)
        st.markdown("---")
        resistance_summary = get_antibiotic_resistance_summary(ab_name)
        if resistance_summary:
            st.markdown("### 🦠 Tỷ lệ kháng thuốc (Việt Nam, 2024):")
            for organism, pattern in resistance_summary.items():
                resistant_pct = pattern.get('resistant', 'N/A')
                sensitive_pct = pattern.get('sensitive', 'N/A')
                
                # Color code
                if resistant_pct != 'N/A' and '%' in resistant_pct:
                    try:
                        # Extract percentage, handle range like "60-70%" -> take first value
                        r_val = float(resistant_pct.split('%')[0].split('-')[0].strip())
                        if r_val >= 50:
                            color = "#F44336"
                        elif r_val >= 30:
                            color = "#FF9800"
                        else:
                            color = "#4CAF50"
                    except (ValueError, IndexError, AttributeError):
                        color = "#666"
                else:
                    color = "#666"
                
                st.markdown(f"""
                <div style='padding: 8px 12px; margin: 4px 0; background: rgba(244,67,54,0.05); border-left: 3px solid {color}; border-radius: 6px;'>
                    <strong>{organism}:</strong><br>
                    <span style='color: #F44336;'>Kháng (R): {resistant_pct}</span> | 
                    <span style='color: #4CAF50;'>Nhạy cảm (S): {sensitive_pct}</span>
                </div>
                """, unsafe_allow_html=True)
        
        # Integrated Quick Dosing Calculator
        st.markdown("---")
        
        # Auto-open dosing if requested
        auto_open = st.session_state.get('auto_open_dosing', False)
        if auto_open:
            st.session_state['auto_open_dosing'] = False
        
        # Sanitize ab_name for key_prefix to avoid session state errors
        safe_ab_name = _sanitize_key(ab_name)
        render_quick_dosing_calculator(ab_name, ab_data, key_prefix=f"info_{safe_ab_name}_")
        
        # Scenario Dosing Calculator (Phase 3)
        with st.expander("🧮 Tính liều cho nhiều trường hợp (Scenarios)", expanded=False):
            render_scenario_dosing_calculator(ab_name)
        
        # TDM Calculator (Phase 5 - Task 5.1)
        if ab_name == "Vancomycin":
            from .tdm_integration import render_tdm_calculator
            render_tdm_calculator(ab_name)
        
        # IV Compatibility Checker (Phase 5 - Task 5.3)
        with st.expander("💉 Kiểm tra tương thích IV", expanded=False):
            from .iv_compatibility import render_iv_compatibility_checker
            render_iv_compatibility_checker(ab_name)
        
        # Export section
        if show_export:
            st.markdown("---")
            _render_antibiotic_export(ab_name, ab_data)



