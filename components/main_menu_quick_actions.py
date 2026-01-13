"""
Main Menu Quick Actions Widget
Big action buttons for most common tasks, profile-based (Nội/ICU)
"""

import streamlit as st
from config.user_profile import get_current_profile


def render_quick_actions_widget(max_items: int = 6):
    """Render quick actions widget with big buttons"""
    profile = get_current_profile()  # "noi" or "icu"
    
    # Define quick actions based on profile
    if profile == "icu":
        quick_actions = [
            {
                'icon': '🫁',
                'title': 'Hồi sức',
                'description': 'SOFA, GCS, qSOFA',
                'page': 'pages/09_🫁_Critical_Care.py',
                'color': '#E91E63'
            },
            {
                'icon': '💊',
                'title': 'Kháng sinh',
                'description': 'Liều dùng & TDM',
                'page': 'pages/02_💊_Antibiotics.py',
                'color': '#9C27B0'
            },
            {
                'icon': '📊',
                'title': 'Thang điểm',
                'description': 'Scores ICU',
                'page': 'pages/01_📊_Scores.py',
                'color': '#2196F3'
            },
            {
                'icon': '🔬',
                'title': 'Xét nghiệm',
                'description': 'Labs & ABG',
                'page': 'pages/05_🔬_Labs_and_Calculators.py',
                'color': '#00BCD4'
            },
            {
                'icon': '📋',
                'title': 'Phác đồ',
                'description': 'Protocols & Bundles',
                'page': 'pages/04_📋_Protocols.py',
                'color': '#4CAF50'
            },
            {
                'icon': '⚠️',
                'title': 'Tương tác',
                'description': 'Drug Interactions',
                'page': 'pages/07_💊_Drug_Database.py',
                'color': '#FF9800'
            },
        ]
    else:  # Nội
        quick_actions = [
            {
                'icon': '📊',
                'title': 'Thang điểm',
                'description': 'ASCVD, CHA2DS2-VASc',
                'page': 'pages/01_📊_Scores.py',
                'color': '#2196F3'
            },
            {
                'icon': '💊',
                'title': 'Thuốc',
                'description': 'Database & Liều dùng',
                'page': 'pages/07_💊_Drug_Database.py',
                'color': '#9C27B0'
            },
            {
                'icon': '⚠️',
                'title': 'Tương tác',
                'description': 'Drug Interactions',
                'page': 'pages/07_💊_Drug_Database.py',
                'color': '#FF9800'
            },
            {
                'icon': '🧮',
                'title': 'Tính toán',
                'description': 'CrCl, eGFR',
                'page': 'pages/05_🔬_Labs_and_Calculators.py',
                'color': '#00BCD4'
            },
            {
                'icon': '🩺',
                'title': 'Chẩn đoán',
                'description': 'Differential Diagnosis',
                'page': 'pages/06_🩺_Diagnosis.py',
                'color': '#4CAF50'
            },
            {
                'icon': '🧭',
                'title': 'Hỗ trợ',
                'description': 'Decision Support',
                'page': 'pages/10_🧭_Decision_Support.py',
                'color': '#607D8B'
            },
        ]
    
    # Limit to max_items
    quick_actions = quick_actions[:max_items]
    
    # Render as grid
    st.markdown("### ⚡ Truy cập nhanh")
    st.caption("Các công cụ thường dùng nhất")
    
    # Responsive grid: 3 columns on desktop, 2 on tablet, 1 on mobile
    num_cols = min(3, len(quick_actions))
    cols = st.columns(num_cols)
    
    for idx, action in enumerate(quick_actions):
        with cols[idx % num_cols]:
            # Create gradient background
            gradient_color = action['color']
            
            st.markdown(
                f"""
                <div class="quick-action-button" 
                     style="background: linear-gradient(135deg, {gradient_color} 0%, {gradient_color}dd 100%);
                            padding: 1.5rem;
                            border-radius: 12px;
                            text-align: center;
                            color: white;
                            cursor: pointer;
                            transition: all 0.3s;
                            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                            margin-bottom: 1rem;">
                    <div class="quick-action-icon" style="font-size: 3rem; margin-bottom: 0.5rem;">
                        {action['icon']}
                    </div>
                    <div style="font-weight: 600; font-size: 1.1rem; margin-bottom: 0.25rem;">
                        {action['title']}
                    </div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">
                        {action['description']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if st.button(
                f"Mở {action['title']}",
                key=f"qa_action_{idx}",
                use_container_width=True,
                type="primary"
            ):
                st.switch_page(action['page'])
