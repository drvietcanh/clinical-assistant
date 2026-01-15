"""
Critical Care Quick Dashboard
Quick access to all critical care tools
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.cards import render_clickable_dashboard_card
from critical_care.patient_dashboard import render_patient_dashboard
from critical_care.clinical_alerts import render_clinical_alerts, render_alerts_summary

# Try to use enhanced version if available
try:
    from critical_care.dashboard_enhanced import render_enhanced_critical_care_dashboard
    USE_ENHANCED = True
except ImportError:
    USE_ENHANCED = False


def render_critical_care_dashboard():
    """Render quick access dashboard for critical care tools"""
    
    # Use enhanced version if available
    if USE_ENHANCED:
        return render_enhanced_critical_care_dashboard()
    
    # Main tabs for dashboard
    main_tabs = st.tabs([
        "🏠 Tổng quan",
        "🏥 Bệnh nhân",
        "🚨 Cảnh báo"
    ])
    
    # Tab 1: Overview
    with main_tabs[0]:
        st.markdown("## 🏠 Critical Care Dashboard")
        st.markdown("""
        Trang tổng quan - Truy cập nhanh tất cả công cụ hồi sức
        """)
        
        # Alerts summary
        alerts_summary = render_alerts_summary()
        if alerts_summary and alerts_summary.get('total', 0) > 0:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🚨 Nghiêm trọng", alerts_summary.get('critical', 0), delta=None)
            with col2:
                st.metric("⚠️ Cảnh báo", alerts_summary.get('warning', 0), delta=None)
            with col3:
                st.metric("ℹ️ Thông tin", alerts_summary.get('info', 0), delta=None)
            with col4:
                st.metric("📊 Tổng cộng", alerts_summary.get('total', 0), delta=None)
            
            if alerts_summary.get('critical', 0) > 0:
                st.error(f"⚠️ Có {alerts_summary.get('critical', 0)} cảnh báo nghiêm trọng. Vui lòng xem tab 'Cảnh báo'.")
        
        st.markdown("---")
    
    # Quick access cards - Now clickable!
    st.markdown("### ⚡ Truy cập nhanh")
    st.caption("Click vào card để mở công cụ tương ứng")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_clickable_dashboard_card(
            title="Fluid Therapy",
            description="Dịch truyền & điện giải",
            icon="💧",
            gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            action_key="critical_care_tool_selection",
            action_value="💧 Fluid Therapy",
            tooltip="Tính toán dịch truyền, bù dịch, và điều chỉnh điện giải"
        )
    
    with col2:
        render_clickable_dashboard_card(
            title="Vasopressors",
            description="Hướng dẫn liều",
            icon="💉",
            gradient="linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
            action_key="critical_care_tool_selection",
            action_value="💉 Vasopressors",
            tooltip="Hướng dẫn liều và titration vasopressor"
        )
    
    with col3:
        render_clickable_dashboard_card(
            title="Transfusion",
            description="Truyền máu",
            icon="🩸",
            gradient="linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            action_key="critical_care_tool_selection",
            action_value="🩸 Transfusion",
            tooltip="Tính toán truyền máu và chế phẩm máu"
        )
    
    with col4:
        render_clickable_dashboard_card(
            title="Sedation",
            description="An thần & giảm đau",
            icon="💤",
            gradient="linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
            action_key="critical_care_tool_selection",
            action_value="💤 Sedation & Analgesia",
            tooltip="Giao thức an thần và giảm đau"
        )
    
    st.markdown("---")
    
    # Scoring systems - Now clickable!
    st.markdown("### 📊 Scoring Systems")
    st.caption("Click để mở hệ thống đánh giá")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #667eea; margin-bottom: 10px;">
            <strong>📊 Đánh giá độ nặng:</strong><br>
            • APACHE II<br>
            • SOFA<br>
            • SAPS II
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Mở", key="scoring_severity", use_container_width=True, help="Mở hệ thống đánh giá độ nặng (APACHE II, SOFA, SAPS II)"):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.session_state['scoring_calc_to_open'] = 'apache2'  # Mở tab APACHE II (tab đầu tiên của severity)
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #f5576c; margin-bottom: 10px;">
            <strong>🧠 Đánh giá thần kinh:</strong><br>
            • GCS<br>
            • RASS<br>
            • CAM-ICU
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧠 Mở", key="scoring_neuro", use_container_width=True, help="Mở hệ thống đánh giá thần kinh (GCS, RASS, CAM-ICU)"):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.session_state['scoring_calc_to_open'] = 'gcs'  # Mở tab GCS (tab đầu tiên của neurological)
            st.rerun()
    
    with col3:
        st.markdown("""
        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #4facfe; margin-bottom: 10px;">
            <strong>🧪 Đánh giá thận:</strong><br>
            • AKI Staging (KDIGO)<br>
            • RIFLE
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧪 Mở", key="scoring_renal", use_container_width=True, help="Mở hệ thống đánh giá thận (AKI Staging, RIFLE)"):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.session_state['scoring_calc_to_open'] = 'aki'  # Mở tab AKI Staging
            st.rerun()
    
    st.markdown("---")
    
    # Clinical scenarios quick links - Now clickable!
    st.markdown("### 🎯 Tình huống lâm sàng")
    st.caption("Click để mở protocol tương ứng")
    
    scenarios = [
        {
            "title": "Sepsis",
            "icon": "🦠",
            "description": "Quản lý nhiễm trùng huyết",
            "tool_value": "🦠 Sepsis Protocols",
            "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        },
        {
            "title": "ARDS",
            "icon": "🫁",
            "description": "Hội chứng suy hô hấp cấp",
            "tool_value": "🫁 ARDS Protocols",
            "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
        },
        {
            "title": "Shock",
            "icon": "💉",
            "description": "Sốc - Huyết động không ổn định",
            "tool_value": "💉 Shock Management",
            "gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
        },
        {
            "title": "Delirium",
            "icon": "🧠",
            "description": "Mê sảng ở ICU",
            "tool_value": "📊 Scoring Systems",  # Will show CAM-ICU
            "gradient": "linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)"
        }
    ]
    
    cols = st.columns(4)
    for idx, scenario in enumerate(scenarios):
        with cols[idx]:
            st.markdown(f"""
            <div style="padding: 15px; background: white; border-radius: 8px; border: 2px solid #e5e7eb; text-align: center; margin-bottom: 10px;">
                <div style="font-size: 2rem; margin-bottom: 5px;">{scenario['icon']}</div>
                <div style="font-weight: bold; margin-bottom: 5px;">{scenario['title']}</div>
                <div style="font-size: 0.85rem; color: #6b7280;">{scenario['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{scenario['icon']} Mở", key=f"scenario_{scenario['title']}", use_container_width=True, help=f"Mở {scenario['title']} protocol"):
                st.session_state['critical_care_tool_selection'] = scenario['tool_value']
                st.rerun()
    
    st.markdown("---")
    
    # Recent calculations (placeholder)
    st.markdown("### 🕐 Tính toán gần đây")
    st.info("""
    **Tính năng đang phát triển:**
    - Lưu lịch sử tính toán
    - Truy cập nhanh các tính toán trước đó
    - Export kết quả
    """)
    
    st.markdown("---")
    
    # Quick tips
    st.markdown("### 💡 Mẹo sử dụng")
    
    tips = [
        "💧 **Fluid Therapy:** Sử dụng Holliday-Segar cho maintenance, tính deficit cho hypernatremia",
        "💉 **Vasopressors:** Bắt đầu với Norepinephrine, theo dõi MAP và lactate",
        "🩸 **Transfusion:** Tuân thủ MTP protocol, theo dõi hemoglobin và coagulation",
        "💤 **Sedation:** Mục tiêu RASS -1 to -2 cho hầu hết bệnh nhân, đánh giá hàng ngày",
        "📊 **Scoring:** SOFA hàng ngày cho sepsis, APACHE II cho tiên lượng ICU"
    ]
    
    for tip in tips:
        st.markdown(f"- {tip}")
    
    # Tab 2: Patient Dashboard
    with main_tabs[1]:
        render_patient_dashboard()
    
    # Tab 3: Clinical Alerts
    with main_tabs[2]:
        render_clinical_alerts()
        
        # Workflow links section
        st.markdown("---")
        st.markdown("### 🔗 Liên kết workflow")
        st.caption("Chuyển nhanh giữa các công cụ liên quan")
        
        workflow_groups = [
            {
                "title": "🫁 Hô hấp",
                "tools": [
                    ("🫁 Ventilator Management", "🫁 Ventilator Management"),
                    ("🫁 ARDS Protocols", "🫁 ARDS Protocols"),
                    ("💤 Sedation & Analgesia", "💤 Sedation & Analgesia"),
                    ("📊 RASS Calculator", "📊 Scoring Systems")
                ]
            },
            {
                "title": "💧 Huyết động",
                "tools": [
                    ("💧 Fluid Therapy", "💧 Fluid Therapy"),
                    ("💉 Vasopressors", "💉 Vasopressors"),
                    ("💉 Shock Management", "💉 Shock Management"),
                    ("🩺 RRT Calculator", "🩺 RRT Calculator")
                ]
            },
            {
                "title": "🦠 Nhiễm trùng",
                "tools": [
                    ("🦠 Sepsis Protocols", "🦠 Sepsis Protocols"),
                    ("📊 SOFA Score", "📊 Scoring Systems"),
                    ("🩸 Transfusion", "🩸 Transfusion")
                ]
            }
        ]
        
        for group in workflow_groups:
            st.markdown(f"#### {group['title']}")
            cols = st.columns(len(group['tools']))
            for idx, (label, tool_value) in enumerate(group['tools']):
                with cols[idx]:
                    if st.button(label, key=f"workflow_{group['title']}_{idx}", use_container_width=True):
                        st.session_state['critical_care_tool_selection'] = tool_value
                        if tool_value == "📊 Scoring Systems":
                            if "RASS" in label:
                                st.session_state['scoring_calc_to_open'] = 'rass'
                            elif "SOFA" in label:
                                st.session_state['scoring_calc_to_open'] = 'sofa'
                        st.rerun()
            st.markdown("---")

