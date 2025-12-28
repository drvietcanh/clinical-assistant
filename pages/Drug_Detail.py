"""
Drug Detail Page - Dedicated page for individual drug information
Trang riêng biệt hiển thị thông tin chi tiết từng thuốc
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from drugs.drug_database import DRUG_DATABASE
from drugs.drug_info_components.detail_view import display_drug_info

# Standard page setup
setup_page(
    page_title="Chi tiết thuốc",
    page_icon="💊",
    description="Thông tin chi tiết về thuốc",
    mobile_header=True
)

# Load mobile CSS if exists
try:
    from pathlib import Path
    css_file = Path(__file__).parent.parent / "static" / "drug_detail_mobile.css"
    if css_file.exists():
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

# Breadcrumbs
try:
    from components.mobile_page_wrapper import render_breadcrumbs
    render_breadcrumbs([
        ("Trang chủ", "/"),
        ("Thuốc", "pages/07_💊_Drug_Database.py"),
        ("Chi tiết", None)
    ])
except ImportError:
    pass

# Get drug name from session state
drug_name = st.session_state.get('view_drug_name')

# If still no drug name, show error
if not drug_name:
    st.error("❌ Không tìm thấy thông tin thuốc. Vui lòng quay lại trang tra cứu thuốc.")
    if st.button("🔙 Quay lại trang tra cứu thuốc"):
        st.switch_page("pages/07_💊_Drug_Database.py")
    st.stop()

# Get drug data
drug_data = DRUG_DATABASE.get(drug_name)

if not drug_data:
    st.error(f"❌ Không tìm thấy thông tin cho thuốc: **{drug_name}**")
    if st.button("🔙 Quay lại trang tra cứu thuốc"):
        st.switch_page("pages/07_💊_Drug_Database.py")
    st.stop()

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Chi tiết thuốc")
    
    # Quick actions
    st.subheader("⚡ Thao tác nhanh")
    
    if st.button("🔙 Quay lại", use_container_width=True, type="primary"):
        st.switch_page("pages/07_💊_Drug_Database.py")
    
    if st.button("🔍 Tìm thuốc khác", use_container_width=True):
        st.switch_page("pages/07_💊_Drug_Database.py")
    
    st.markdown("---")
    
    # Drug quick info
    st.subheader("📋 Thông tin nhanh")
    
    if 'vietnamese_name' in drug_data:
        st.markdown(f"**Tên biệt dược:** {drug_data['vietnamese_name']}")
    
    if 'group' in drug_data:
        st.markdown(f"**Nhóm:** {drug_data['group']}")
    
    if 'administration' in drug_data:
        admin_icons = {'IV': '💉', 'IM': '💊', 'PO': '🍽️', 
                      'Inhalation': '🌬️', 'SC': '💉', 'Rectal': '📦'}
        admin_display = ' / '.join([
            f"{admin_icons.get(route, '')} {route}" 
            for route in drug_data['administration']
        ])
        st.markdown(f"**Đường dùng:** {admin_display}")
    
    if 'pregnancy' in drug_data:
        preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
        preg = drug_data['pregnancy']
        st.markdown(f"**Thai kỳ:** {preg_icons.get(preg, '')} {preg}")
    
    st.markdown("---")
    
    # Related actions
    st.subheader("🔗 Liên kết")
    
    if st.button("📊 So sánh thuốc", use_container_width=True):
        st.session_state['switch_to_comparison'] = True
        st.session_state['preset_comparison_drugs'] = [drug_name]
        st.switch_page("pages/07_💊_Drug_Database.py")
    
    # Check if drug is antibiotic
    try:
        from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
        is_antibiotic = drug_name in ANTIBIOTICS_DATABASE
        if is_antibiotic:
            if st.button("🧮 Tính liều theo CrCl", use_container_width=True):
                st.session_state['preset_antibiotic_name'] = drug_name
                st.session_state['switch_to_dosing_calculator'] = True
                st.switch_page("pages/07_💊_Drug_Database.py")
    except ImportError:
        pass
    
    # Check if drug has TDM
    try:
        from drugs.drug_utils.tdm_mapping import has_tdm
        if has_tdm(drug_name):
            if st.button("📊 TDM Calculator", use_container_width=True):
                st.session_state['preset_tdm_drug'] = drug_name
                st.session_state['switch_to_tdm'] = True
                st.switch_page("pages/08_📊_TDM.py")
    except ImportError:
        pass

# ========== MAIN CONTENT ==========

# Enhanced header with badges, icons, and quick actions (inspired by Drugs.com & Epocrates)
# Determine drug category color
category_colors = {
    'cardiovascular': '#E91E63', 'diabetes': '#9C27B0', 'gastrointestinal': '#FF9800',
    'respiratory': '#00BCD4', 'neurological': '#3F51B5', 'psychiatry': '#673AB7',
    'analgesic': '#F44336', 'antimicrobial': '#4CAF50', 'hematology': '#9C27B0'
}
drug_group = drug_data.get('group', '').lower()
header_color = '#667eea'  # Default
for cat, color in category_colors.items():
    if cat in drug_group:
        header_color = color
        break

# Check for black box warning
has_black_box = 'black_box_warnings' in drug_data and drug_data.get('black_box_warnings')

# Pregnancy category badge
preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
preg = drug_data.get('pregnancy', '')
preg_badge = f"<span style='background: rgba(255,255,255,0.3); padding: 4px 10px; border-radius: 12px; font-size: 0.85em; margin-left: 10px;'>{preg_icons.get(preg, '')} Thai kỳ: {preg}</span>" if preg else ""

# Administration badges
admin_icons = {'IV': '💉', 'IM': '💊', 'PO': '🍽️', 'Inhalation': '🌬️', 'SC': '💉', 'Rectal': '📦'}
admin_routes = drug_data.get('administration', [])
admin_badges = ' '.join([
    f"<span style='background: rgba(255,255,255,0.25); padding: 4px 8px; border-radius: 8px; font-size: 0.8em; margin-right: 5px;'>{admin_icons.get(route, '')} {route}</span>"
    for route in admin_routes[:3]
])

# Black box warning indicator
bb_warning_badge = ""
if has_black_box:
    bb_warning_badge = """
    <div style='background: #DC2626; color: white; padding: 8px 15px; border-radius: 8px; margin-top: 15px; display: inline-block; font-weight: bold; font-size: 0.9em;'>
        ⚠️ CẢNH BÁO HỘP ĐEN
    </div>
    """

st.markdown(
    f"""
    <div style='
        background: linear-gradient(135deg, {header_color} 0%, {header_color}dd 100%);
        color: white;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
    '>
        <div style='display: flex; align-items: flex-start; justify-content: space-between; flex-wrap: wrap; gap: 20px;'>
            <div style='flex: 1; min-width: 300px;'>
                <div style='display: flex; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;'>
                    <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: bold;'>
                        💊 {drug_name}
                    </h1>
                    {preg_badge}
                </div>
                {f"<p style='margin: 8px 0 12px 0; color: rgba(255,255,255,0.95); font-size: 1.3em; font-weight: 500;'>{drug_data.get('vietnamese_name', '')}</p>" if drug_data.get('vietnamese_name') else ''}
                {f"<p style='margin: 0 0 15px 0; color: rgba(255,255,255,0.9); font-size: 1.05em;'>{drug_data.get('group', '')}</p>" if drug_data.get('group') else ''}
                <div style='margin: 15px 0;'>
                    {admin_badges}
                </div>
                {bb_warning_badge}
            </div>
            <div style='text-align: right; min-width: 150px;'>
                <div style='background: rgba(255,255,255,0.2); padding: 15px 20px; border-radius: 12px; backdrop-filter: blur(10px);'>
                    <div style='font-size: 0.85em; opacity: 0.9; margin-bottom: 5px;'>Trang chi tiết</div>
                    <div style='font-size: 2em; font-weight: bold;'>📖</div>
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Quick Action Buttons (inspired by Epocrates)
st.markdown("---")
action_cols = st.columns([1, 1, 1, 1])
with action_cols[0]:
    if st.button("📊 So sánh", use_container_width=True, type="secondary"):
        st.session_state['switch_to_comparison'] = True
        st.session_state['preset_comparison_drugs'] = [drug_name]
        st.switch_page("pages/07_💊_Drug_Database.py")
with action_cols[1]:
    try:
        from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
        is_antibiotic = drug_name in ANTIBIOTICS_DATABASE
        if is_antibiotic:
            if st.button("🧮 Tính liều", use_container_width=True, type="secondary"):
                st.session_state['preset_antibiotic_name'] = drug_name
                st.session_state['switch_to_dosing_calculator'] = True
                st.switch_page("pages/07_💊_Drug_Database.py")
        else:
            st.empty()
    except ImportError:
        st.empty()
with action_cols[2]:
    try:
        from drugs.drug_utils.tdm_mapping import has_tdm
        if has_tdm(drug_name):
            if st.button("📊 TDM", use_container_width=True, type="secondary"):
                st.session_state['preset_tdm_drug'] = drug_name
                st.session_state['switch_to_tdm'] = True
                st.switch_page("pages/08_📊_TDM.py")
        else:
            st.empty()
    except ImportError:
        st.empty()
with action_cols[3]:
    if st.button("🔍 Tương tác", use_container_width=True, type="secondary"):
        st.session_state['switch_to_interaction_checker'] = True
        st.session_state['preset_interaction_drugs'] = [drug_name]
        st.switch_page("pages/07_💊_Drug_Database.py")

st.markdown("---")

# At-a-Glance Summary Box (inspired by Epocrates quick facts)
top_indications = drug_data.get('indications', [])[:3]
standard_dose = ""
if 'dosage' in drug_data:
    dosage = drug_data['dosage']
    if 'adult' in dosage:
        standard_dose = dosage['adult']
    elif 'adult_po' in dosage:
        standard_dose = dosage['adult_po']
    elif 'adult_iv' in dosage:
        standard_dose = dosage['adult_iv']

if top_indications or standard_dose:
    st.markdown(
        f"""
        <div style='
            background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
            border: 2px solid #e2e8f0;
            border-left: 5px solid #3B82F6;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        '>
            <h3 style='margin: 0 0 15px 0; color: #1e293b; font-size: 1.3em; display: flex; align-items: center;'>
                <span style='font-size: 1.5em; margin-right: 10px;'>⚡</span>
                Thông Tin Nhanh
            </h3>
            <div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;'>
                {f"""
                <div style='background: white; padding: 15px; border-radius: 8px; border-left: 3px solid #10B981;'>
                    <div style='color: #065f46; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>📋 Chỉ định chính</div>
                    <ul style='margin: 0; padding-left: 20px; color: #047857;'>
                        {''.join([f'<li style="margin: 5px 0;">{ind}</li>' for ind in top_indications])}
                    </ul>
                </div>
                """ if top_indications else ""}
                {f"""
                <div style='background: white; padding: 15px; border-radius: 8px; border-left: 3px solid #3B82F6;'>
                    <div style='color: #1e40af; font-size: 0.85em; font-weight: bold; margin-bottom: 5px;'>💊 Liều chuẩn người lớn</div>
                    <div style='color: #1e3a8a; font-size: 1em; font-weight: 500;'>{standard_dose}</div>
                </div>
                """ if standard_dose else ""}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Display drug information using the enhanced detail view (without duplicate header)
display_drug_info(drug_name, drug_data, show_header=False)

# Related Drugs Section (suggest drugs from same group)
st.markdown("---")
drug_group = drug_data.get('group', '')
if drug_group:
    # Find drugs in the same group (DRUG_DATABASE already imported at top)
    related_drugs = [
        (name, data) for name, data in DRUG_DATABASE.items()
        if name != drug_name and data.get('group', '') == drug_group
    ]
    
    if related_drugs:
        # Limit to 6 related drugs
        related_drugs = related_drugs[:6]
        st.markdown("### 💊 Thuốc cùng nhóm")
        st.caption(f"Các thuốc khác trong nhóm **{drug_group}**")
        
        # Display as cards in grid
        num_cols = 3
        cols = st.columns(num_cols)
        for idx, (rel_name, rel_data) in enumerate(related_drugs):
            with cols[idx % num_cols]:
                rel_vn_name = rel_data.get('vietnamese_name', '')
                st.markdown(
                    f"""
                    <div style='
                        background: white;
                        border: 1px solid #e2e8f0;
                        border-radius: 8px;
                        padding: 15px;
                        margin: 8px 0;
                        cursor: pointer;
                        transition: all 0.2s;
                        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    ' onmouseover="this.style.borderColor='#3B82F6'; this.style.boxShadow='0 2px 6px rgba(59,130,246,0.2)';"
                       onmouseout="this.style.borderColor='#e2e8f0'; this.style.boxShadow='0 1px 3px rgba(0,0,0,0.1)';">
                        <div style='color: #1e40af; font-weight: bold; font-size: 1em; margin-bottom: 5px;'>💊 {rel_name}</div>
                        {f"<div style='color: #64748b; font-size: 0.85em; margin-bottom: 8px;'>{rel_vn_name}</div>" if rel_vn_name else ""}
                        <div style='color: #94a3b8; font-size: 0.8em;'>{drug_group.split(' - ')[0] if ' - ' in drug_group else drug_group}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                if st.button(f"Xem {rel_name}", key=f"related_{rel_name}", use_container_width=True):
                    st.session_state['view_drug_name'] = rel_name
                    st.rerun()

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🔙 Quay lại", use_container_width=True):
        st.switch_page("pages/07_💊_Drug_Database.py")
with col2:
    if st.button("🔍 Tìm thuốc khác", use_container_width=True):
        st.switch_page("pages/07_💊_Drug_Database.py")
with col3:
    try:
        from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE
        is_antibiotic = drug_name in ANTIBIOTICS_DATABASE
        if is_antibiotic:
            if st.button("🧮 Tính liều", use_container_width=True):
                st.session_state['preset_antibiotic_name'] = drug_name
                st.session_state['switch_to_dosing_calculator'] = True
                st.switch_page("pages/07_💊_Drug_Database.py")
    except ImportError:
        pass

# Standard footer
render_standard_footer(disclaimer=True)

