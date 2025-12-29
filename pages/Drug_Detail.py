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

# Enhanced mobile swipe gestures for drug detail page
st.markdown(
    """
    <script>
    // Enhanced swipe gestures for drug detail page
    (function() {
        let touchStartX = 0;
        let touchEndX = 0;
        let touchStartY = 0;
        let touchEndY = 0;
        let isSwipe = false;
        
        const minSwipeDistance = 80;
        const maxVerticalDistance = 50; // Max vertical movement to consider it a swipe
        
        // Only enable on mobile
        if (window.innerWidth > 768) return;
        
        document.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
            touchStartY = e.changedTouches[0].screenY;
            isSwipe = false;
        }, { passive: true });
        
        document.addEventListener('touchmove', function(e) {
            const currentX = e.changedTouches[0].screenX;
            const currentY = e.changedTouches[0].screenY;
            const deltaX = currentX - touchStartX;
            const deltaY = currentY - touchStartY;
            
            // Show swipe indicator
            if (Math.abs(deltaX) > 30 && Math.abs(deltaX) > Math.abs(deltaY)) {
                isSwipe = true;
                const indicator = document.getElementById('swipe-indicator');
                if (indicator) {
                    indicator.classList.add('show');
                    if (deltaX > 0) {
                        indicator.className = 'swipe-indicator show right';
                        indicator.innerHTML = '← Quay lại';
                    } else {
                        indicator.className = 'swipe-indicator show left';
                        indicator.innerHTML = 'Tiếp theo →';
                    }
                }
            }
        }, { passive: true });
        
        document.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            touchEndY = e.changedTouches[0].screenY;
            
            const deltaX = touchEndX - touchStartX;
            const deltaY = touchEndY - touchStartY;
            
            // Hide swipe indicator
            const indicator = document.getElementById('swipe-indicator');
            if (indicator) {
                indicator.classList.remove('show');
            }
            
            // Only handle horizontal swipes
            if (isSwipe && Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minSwipeDistance && Math.abs(deltaY) < maxVerticalDistance) {
                if (deltaX > 0) {
                    // Swipe right - Go back
                    window.history.back();
                } else {
                    // Swipe left - Could implement forward navigation if needed
                    // For now, do nothing or show hint
                }
            }
            
            isSwipe = false;
        }, { passive: true });
        
        // Create swipe indicator element
        const indicator = document.createElement('div');
        indicator.id = 'swipe-indicator';
        indicator.className = 'swipe-indicator';
        document.body.appendChild(indicator);
        
        // Show swipe hint on first visit (only once per session)
        if (!sessionStorage.getItem('drugDetailSwipeHintShown')) {
            setTimeout(function() {
                const hint = document.createElement('div');
                hint.className = 'swipe-hint';
                hint.innerHTML = '👆 Vuốt sang phải để quay lại';
                document.body.appendChild(hint);
                setTimeout(function() {
                    hint.remove();
                }, 3000);
                sessionStorage.setItem('drugDetailSwipeHintShown', 'true');
            }, 1000);
        }
    })();
    </script>
    """,
    unsafe_allow_html=True
)

# ========== CRITICAL: Get and validate drug_name FIRST ==========
# Get drug name from session state - MUST be at the very top to avoid NameError
drug_name = None
try:
    drug_name = st.session_state.get('view_drug_name', None)
    # Ensure it's a string and strip whitespace
    if drug_name:
        drug_name = str(drug_name).strip()
        if not drug_name:  # Empty string after strip
            drug_name = None
except Exception as e:
    st.error(f"❌ Lỗi khi đọc thông tin thuốc: {str(e)}")
    drug_name = None

# Validate drug_name early - show error page if invalid
if not drug_name:
    st.error("❌ Không tìm thấy thông tin thuốc. Vui lòng quay lại trang tra cứu thuốc.")
    st.info("💡 **Hướng dẫn:** Chọn một thuốc từ danh sách để xem chi tiết")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔙 Quay lại trang tra cứu thuốc", use_container_width=True, type="primary"):
            st.switch_page("pages/07_💊_Drug_Database.py")
    with col2:
        if st.button("🏠 Về trang chủ", use_container_width=True):
            st.switch_page("Home")
    st.stop()

# Validate drug exists in database
if drug_name not in DRUG_DATABASE:
    st.error(f"❌ Không tìm thấy thông tin cho thuốc: **{drug_name}**")
    st.info(f"💡 Thuốc '{drug_name}' không có trong database. Có thể tên thuốc đã thay đổi hoặc bị xóa.")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔙 Quay lại trang tra cứu thuốc", use_container_width=True, type="primary"):
            st.switch_page("pages/07_💊_Drug_Database.py")
    with col2:
        if st.button("🏠 Về trang chủ", use_container_width=True):
            st.switch_page("Home")
    st.stop()

# Get drug data - drug_name is now validated
drug_data = DRUG_DATABASE.get(drug_name)
if not drug_data:
    st.error(f"❌ Dữ liệu thuốc '{drug_name}' không hợp lệ")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔙 Quay lại trang tra cứu thuốc", use_container_width=True, type="primary"):
            st.switch_page("pages/07_💊_Drug_Database.py")
    with col2:
        if st.button("🏠 Về trang chủ", use_container_width=True):
            st.switch_page("Home")
    st.stop()

# Back button using Streamlit navigation (more reliable than history.back())
col1, col2 = st.columns([1, 10])
with col1:
    if st.button("←", help="Quay lại danh sách thuốc", key="back_to_drug_list"):
        st.switch_page("pages/07_💊_Drug_Database.py")
with col2:
    st.markdown(
        f"""
        <div style='margin-bottom: 15px; padding-top: 8px;'>
            <span style='color: #64748b; font-size: 0.95em;'>
                💊 Cơ sở dữ liệu thuốc → {drug_name}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Breadcrumbs (if component available) - drug_name already validated above
try:
    from components.mobile_page_wrapper import render_breadcrumbs
    render_breadcrumbs([
        ("Trang chủ", "/"),
        ("💊 Cơ sở dữ liệu thuốc", "pages/07_💊_Drug_Database.py"),
        (drug_name, None)
    ])
except ImportError:
    pass

# Get drug data - drug_name already validated above
drug_data = DRUG_DATABASE.get(drug_name)

# ========== SIDEBAR ==========
with st.sidebar:
    st.header("💊 Chi tiết thuốc")
    
    # Quick actions - more prominent
    st.markdown("### ⚡ Thao tác nhanh")
    
    if st.button("🔙 Quay lại danh sách", use_container_width=True, type="primary"):
        st.switch_page("pages/07_💊_Drug_Database.py")
    
    if st.button("🔍 Tìm thuốc khác", use_container_width=True, type="secondary"):
        st.switch_page("pages/07_💊_Drug_Database.py")
    
    st.markdown("---")
    
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
action_cols = st.columns([1, 1, 1, 1, 1])
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
with action_cols[4]:
    # Print button
    st.markdown(
        """
        <style>
        .print-button {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            cursor: pointer;
            text-align: center;
            width: 100%;
        }
        .print-button:hover {
            background-color: #e0e0e0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    if st.button("🖨️ In", use_container_width=True, type="secondary"):
        st.markdown(
            """
            <script>
            window.print();
            </script>
            """,
            unsafe_allow_html=True
        )

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

# Enhanced Related Drugs Section (inspired by Epocrates & UpToDate)
st.markdown("---")
drug_group = drug_data.get('group', '')
drug_indications = drug_data.get('indications', [])

# Find related drugs: same group
same_group_drugs = []
if drug_group:
    same_group_drugs = [
        (name, data) for name, data in DRUG_DATABASE.items()
        if name != drug_name and data.get('group', '') == drug_group
    ]
    same_group_drugs = same_group_drugs[:6]  # Limit to 6

# Find alternative drugs: same indications but different group
alternative_drugs = []
if drug_indications:
    # Get first indication to find alternatives
    if len(drug_indications) > 0:
        primary_indication = drug_indications[0].lower()
        alternative_drugs = [
            (name, data) for name, data in DRUG_DATABASE.items()
            if name != drug_name 
            and data.get('group', '') != drug_group  # Different group
            and 'indications' in data
            and any(primary_indication in ind.lower() for ind in data['indications'])
        ]
        alternative_drugs = alternative_drugs[:6]  # Limit to 6

# Display same group drugs
if same_group_drugs:
    st.markdown("### 💊 Thuốc cùng nhóm")
    st.caption(f"Các thuốc khác trong nhóm **{drug_group}**")
    
    # Display as enhanced cards in grid
    num_cols = 3
    cols = st.columns(num_cols)
    for idx, (rel_name, rel_data) in enumerate(same_group_drugs):
        with cols[idx % num_cols]:
            rel_vn_name = rel_data.get('vietnamese_name', '')
            rel_group = rel_data.get('group', '')
            
            # Visual indicators for related drug
            indicators = []
            if 'pregnancy' in rel_data:
                preg = rel_data['pregnancy']
                preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
                indicators.append(f"<span style='font-size: 0.8em;'>{preg_icons.get(preg, '')}</span>")
            if 'black_box_warnings' in rel_data and rel_data.get('black_box_warnings'):
                indicators.append("<span style='font-size: 0.8em;'>⚠️</span>")
            indicators_html = ' '.join(indicators)
            
            st.markdown(
                f"""
                <div style='
                    background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
                    border: 2px solid #e2e8f0;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 8px 0;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
                ' onmouseover="this.style.borderColor='#3B82F6'; this.style.boxShadow='0 4px 12px rgba(59,130,246,0.25)'; this.style.transform='translateY(-2px)';"
                   onmouseout="this.style.borderColor='#e2e8f0'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.08)'; this.style.transform='translateY(0)';">
                    <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;'>
                        <div style='color: #1e40af; font-weight: bold; font-size: 1em; flex: 1;'>💊 {rel_name}</div>
                        <div style='display: flex; gap: 4px; align-items: center;'>{indicators_html}</div>
                    </div>
                    {f"<div style='color: #64748b; font-size: 0.85em; margin-bottom: 6px;'>{rel_vn_name}</div>" if rel_vn_name else ""}
                    <div style='color: #94a3b8; font-size: 0.75em; background: #f1f5f9; padding: 4px 8px; border-radius: 4px; display: inline-block;'>{rel_group.split(' - ')[0] if ' - ' in rel_group else rel_group}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Xem {rel_name}", key=f"related_same_group_{rel_name}", use_container_width=True):
                st.session_state['view_drug_name'] = rel_name
                st.rerun()

# Display alternative drugs (same indication, different group)
if alternative_drugs:
    st.markdown("---")
    st.markdown("### 🔄 Thuốc thay thế (cùng chỉ định)")
    st.caption(f"Các thuốc khác có chỉ định **{drug_indications[0] if drug_indications else 'tương tự'}** nhưng khác nhóm")
    
    # Display as enhanced cards
    num_cols = 3
    cols = st.columns(num_cols)
    for idx, (alt_name, alt_data) in enumerate(alternative_drugs):
        with cols[idx % num_cols]:
            alt_vn_name = alt_data.get('vietnamese_name', '')
            alt_group = alt_data.get('group', '')
            
            # Visual indicators
            indicators = []
            if 'pregnancy' in alt_data:
                preg = alt_data['pregnancy']
                preg_icons = {'A': '🟢', 'B': '🟡', 'C': '🟠', 'D': '🔴', 'X': '⚫'}
                indicators.append(f"<span style='font-size: 0.8em;'>{preg_icons.get(preg, '')}</span>")
            if 'black_box_warnings' in alt_data and alt_data.get('black_box_warnings'):
                indicators.append("<span style='font-size: 0.8em;'>⚠️</span>")
            indicators_html = ' '.join(indicators)
            
            st.markdown(
                f"""
                <div style='
                    background: linear-gradient(135deg, #fef3c7 0%, #ffffff 100%);
                    border: 2px solid #fcd34d;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 8px 0;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
                ' onmouseover="this.style.borderColor='#F59E0B'; this.style.boxShadow='0 4px 12px rgba(245,158,11,0.25)'; this.style.transform='translateY(-2px)';"
                   onmouseout="this.style.borderColor='#fcd34d'; this.style.boxShadow='0 2px 4px rgba(0,0,0,0.08)'; this.style.transform='translateY(0)';">
                    <div style='display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;'>
                        <div style='color: #92400e; font-weight: bold; font-size: 1em; flex: 1;'>💊 {alt_name}</div>
                        <div style='display: flex; gap: 4px; align-items: center;'>{indicators_html}</div>
                    </div>
                    {f"<div style='color: #78350f; font-size: 0.85em; margin-bottom: 6px;'>{alt_vn_name}</div>" if alt_vn_name else ""}
                    <div style='color: #92400e; font-size: 0.75em; background: #fef3c7; padding: 4px 8px; border-radius: 4px; display: inline-block; font-weight: 500;'>{alt_group.split(' - ')[0] if ' - ' in alt_group else alt_group}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if st.button(f"Xem {alt_name}", key=f"related_alternative_{alt_name}", use_container_width=True):
                st.session_state['view_drug_name'] = alt_name
                st.rerun()

# Sticky Footer Navigation (inspired by medical reference sites)
st.markdown("---")
st.markdown(
    """
    <div style='
        position: sticky;
        bottom: 0;
        background: white;
        border-top: 2px solid #e2e8f0;
        padding: 15px 0;
        margin-top: 30px;
        box-shadow: 0 -2px 8px rgba(0,0,0,0.1);
        z-index: 100;
    '>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("🔙 Quay lại danh sách", use_container_width=True, type="primary"):
        st.switch_page("pages/07_💊_Drug_Database.py")
with col2:
    if st.button("🔍 Tìm thuốc khác", use_container_width=True, type="secondary"):
        st.switch_page("pages/07_💊_Drug_Database.py")
with col3:
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

# Standard footer
render_standard_footer(disclaimer=True)

