"""
Settings - User preferences and app configuration
Manage user settings, preferences, and data
"""

import streamlit as st
import json
from pathlib import Path
from datetime import datetime
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

# Standard page setup
setup_page(
    page_title="Settings",
    page_icon="⚙️",
    description="Cài đặt và tùy chỉnh Clinical Assistant"
)

# Custom CSS
st.markdown("""
<style>
.settings-section {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    margin: 16px 0;
}

.settings-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #333;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.setting-item {
    padding: 12px 0;
    border-bottom: 1px solid #f0f0f0;
}

.setting-item:last-child {
    border-bottom: none;
}
</style>
""", unsafe_allow_html=True)

# Settings file
SETTINGS_FILE = Path("user_settings.json")

# Load settings
def load_settings():
    if SETTINGS_FILE.exists():
        with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'units': {
            'creatinine': 'mg/dL',
            'cholesterol': 'mg/dL',
            'glucose': 'mg/dL',
            'weight': 'kg',
            'height': 'cm'
        },
        'display': {
            'theme': 'Light',
            'language': 'Vietnamese',
            'items_per_page': 20
        },
        'notifications': {
            'guideline_updates': True,
            'drug_alerts': True,
            'system_notifications': True
        },
        'privacy': {
            'save_history': True,
            'save_favorites': True,
            'analytics': True
        }
    }

# Save settings
def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)
    st.session_state.settings = settings

# Initialize settings
if 'settings' not in st.session_state:
    st.session_state.settings = load_settings()

settings = st.session_state.settings

# Hero section
render_hero(
    title="Settings",
    subtitle="⚙️ Cài đặt & Tùy chỉnh",
    description="Quản lý preferences, units, và app configuration",
    icon="⚙️",
    gradient=("#667eea", "#764ba2")
)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    setting_category = st.radio(
        "Category:",
        ["Units", "Display", "Notifications", "Privacy", "Data Management", "About"],
        key="settings_category"
    )
    
    st.markdown("---")
    
    render_info_box("""
    **⚙️ Settings:**
    - Customize units
    - Display preferences
    - Notifications
    - Privacy settings
    - Data management
    
    **💡 Tip:**
    - Changes save automatically
    - Export settings for backup
    """, type="info", title="Help")

# Main content
if setting_category == "Units":
    st.markdown("### 📏 Unit Preferences")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">🧪 Laboratory Units</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        creatinine_unit = st.selectbox(
            "Creatinine:",
            ["mg/dL", "µmol/L"],
            index=0 if settings['units']['creatinine'] == 'mg/dL' else 1,
            key="creatinine_unit"
        )
        settings['units']['creatinine'] = creatinine_unit
        
        cholesterol_unit = st.selectbox(
            "Cholesterol:",
            ["mg/dL", "mmol/L"],
            index=0 if settings['units']['cholesterol'] == 'mg/dL' else 1,
            key="cholesterol_unit"
        )
        settings['units']['cholesterol'] = cholesterol_unit
    
    with col2:
        glucose_unit = st.selectbox(
            "Glucose:",
            ["mg/dL", "mmol/L"],
            index=0 if settings['units']['glucose'] == 'mg/dL' else 1,
            key="glucose_unit"
        )
        settings['units']['glucose'] = glucose_unit
    
    # End of lab units section
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📐 Physical Measurements</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight_unit = st.selectbox(
            "Weight:",
            ["kg", "lbs"],
            index=0 if settings['units']['weight'] == 'kg' else 1,
            key="weight_unit"
        )
        settings['units']['weight'] = weight_unit
    
    with col2:
        height_unit = st.selectbox(
            "Height:",
            ["cm", "inches"],
            index=0 if settings['units']['height'] == 'cm' else 1,
            key="height_unit"
        )
        settings['units']['height'] = height_unit
    
    # End of physical measurements section
    st.markdown("---")
    
    if st.button("💾 Save Unit Settings", type="primary"):
        save_settings(settings)
        st.success("✅ Unit settings saved!")

elif setting_category == "Display":
    st.markdown("### 🎨 Display Preferences")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">🎨 Appearance</div>', unsafe_allow_html=True)
    
    theme = st.selectbox(
        "Theme:",
        ["Light", "Dark", "Auto"],
        index=["Light", "Dark", "Auto"].index(settings['display']['theme']),
        key="theme"
    )
    settings['display']['theme'] = theme
    
    language = st.selectbox(
        "Language:",
        ["Vietnamese", "English"],
        index=0 if settings['display']['language'] == 'Vietnamese' else 1,
        key="language"
    )
    settings['display']['language'] = language
    
    # End of appearance section
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📄 Pagination</div>', unsafe_allow_html=True)
    
    items_per_page = st.slider(
        "Items per page:",
        min_value=10,
        max_value=50,
        value=settings['display']['items_per_page'],
        step=5,
        key="items_per_page"
    )
    settings['display']['items_per_page'] = items_per_page
    
    # End of pagination section
    st.markdown("---")
    
    if st.button("💾 Save Display Settings", type="primary"):
        save_settings(settings)
        st.success("✅ Display settings saved!")

elif setting_category == "Notifications":
    st.markdown("### 🔔 Notification Preferences")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">🔔 Notification Types</div>', unsafe_allow_html=True)
    
    guideline_updates = st.checkbox(
        "Guideline Updates",
        value=settings['notifications']['guideline_updates'],
        key="guideline_updates"
    )
    settings['notifications']['guideline_updates'] = guideline_updates
    st.caption("Get notified when guidelines are updated")
    
    drug_alerts = st.checkbox(
        "Drug Alerts",
        value=settings['notifications']['drug_alerts'],
        key="drug_alerts"
    )
    settings['notifications']['drug_alerts'] = drug_alerts
    st.caption("Important drug safety alerts")
    
    system_notifications = st.checkbox(
        "System Notifications",
        value=settings['notifications']['system_notifications'],
        key="system_notifications"
    )
    settings['notifications']['system_notifications'] = system_notifications
    st.caption("App updates and maintenance")
    
    # End of notifications section
    st.markdown("---")
    
    if st.button("💾 Save Notification Settings", type="primary"):
        save_settings(settings)
        st.success("✅ Notification settings saved!")

elif setting_category == "Privacy":
    st.markdown("### 🔒 Privacy Settings")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">🔒 Data Privacy</div>', unsafe_allow_html=True)
    
    save_history = st.checkbox(
        "Save Search History",
        value=settings['privacy']['save_history'],
        key="save_history"
    )
    settings['privacy']['save_history'] = save_history
    st.caption("Keep track of your searches")
    
    save_favorites = st.checkbox(
        "Save Favorites",
        value=settings['privacy']['save_favorites'],
        key="save_favorites"
    )
    settings['privacy']['save_favorites'] = save_favorites
    st.caption("Remember your bookmarked items")
    
    analytics = st.checkbox(
        "Usage Analytics",
        value=settings['privacy']['analytics'],
        key="analytics"
    )
    settings['privacy']['analytics'] = analytics
    st.caption("Help improve the app by sharing anonymous usage data")
    
    # End of data privacy section
    st.markdown("---")
    
    if st.button("💾 Save Privacy Settings", type="primary"):
        save_settings(settings)
        st.success("✅ Privacy settings saved!")

elif setting_category == "Data Management":
    st.markdown("### 💾 Data Management")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📥 Export Settings</div>', unsafe_allow_html=True)
    
    if st.button("📥 Export All Settings"):
        settings_json = json.dumps(settings, ensure_ascii=False, indent=2)
        st.download_button(
            label="Download Settings JSON",
            data=settings_json,
            file_name=f"clinical_assistant_settings_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )
    
    # End of export settings section
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📤 Import Settings</div>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload Settings JSON", type=['json'])
    if uploaded_file:
        imported_settings = json.load(uploaded_file)
        if st.button("Confirm Import"):
            save_settings(imported_settings)
            st.success("✅ Settings imported successfully!")
            st.rerun()
    
    # End of import settings section
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">🗑️ Clear Data</div>', unsafe_allow_html=True)
    
    st.warning("⚠️ These actions cannot be undone!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Clear Search History", type="secondary"):
            if 'recent_searches' in st.session_state:
                st.session_state.recent_searches = []
            st.success("✅ Search history cleared!")
    
    with col2:
        if st.button("Clear Favorites", type="secondary"):
            if 'favorites' in st.session_state:
                st.session_state.favorites = []
            st.success("✅ Favorites cleared!")
    
    # End of clear data section
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">🔄 Reset Settings</div>', unsafe_allow_html=True)
    
    if st.button("🔄 Reset to Default", type="secondary"):
        if st.checkbox("I understand this will reset all settings"):
            default_settings = load_settings()
            save_settings(default_settings)
            st.success("✅ Settings reset to default!")
            st.rerun()
    
    # End of reset settings section

elif setting_category == "About":
    st.markdown("### ℹ️ About Clinical Assistant")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📱 App Information</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Version:** 2.0 Enhanced")
        st.markdown("**Last Updated:** 2026-01-01")
        st.markdown("**Platform:** Streamlit")
    
    with col2:
        st.markdown("**Total Pages:** 24")
        st.markdown("**Features:** 50+")
        st.markdown("**Status:** Production Ready")
    
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">👥 Credits</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Developed by:** Clinical Assistant Team  
    **Medical Advisor:** Clinical IT Team  
    **Contributors:** Open source community
    
    **Technologies:**
    - Streamlit - Web framework
    - Python - Programming language
    - Pandas - Data analysis
    - NumPy - Numerical computing
    """)
    
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📄 License</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **License:** MIT License
    
    **Disclaimer:** This tool is for clinical support only and does NOT replace clinical judgment.
    - For reference only
    - Always verify with local guidelines
    - Use clinical judgment
    - Individualize for each patient
    """)
    
    st.markdown("---")
    
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.markdown('<div class="settings-title">📞 Support</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Documentation:** See `docs/` folder  
    **Issues:** GitHub Issues  
    **Questions:** Contact development team  
    **Feedback:** Submit via GitHub
    """)
    
    st.markdown("---")

# Footer
st.markdown("---")
render_standard_footer(disclaimer=False)
