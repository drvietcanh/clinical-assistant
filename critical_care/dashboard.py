"""
Critical Care Quick Dashboard
Quick access to all critical care tools
"""

import streamlit as st
from components.ui.results import render_result_box, render_result_card
from components.ui.cards import render_clickable_dashboard_card

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
    
    st.markdown("## 🏠 Critical Care Dashboard")
    st.markdown("""
    Trang tổng quan - Truy cập nhanh tất cả công cụ hồi sức
    """)
    
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

