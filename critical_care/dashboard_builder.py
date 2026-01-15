"""
Customizable Dashboard Builder
Drag-and-drop widgets for custom dashboard layouts
"""

import streamlit as st
from typing import List, Dict, Optional
import json


# Available widgets
AVAILABLE_WIDGETS = {
    "Alerts Summary": {
        "icon": "🚨",
        "description": "Tóm tắt cảnh báo",
        "size": "medium"
    },
    "Ventilator Status": {
        "icon": "🫁",
        "description": "Trạng thái máy thở",
        "size": "large"
    },
    "ABG Values": {
        "icon": "🩸",
        "description": "Giá trị ABG",
        "size": "medium"
    },
    "Fluid Balance": {
        "icon": "💧",
        "description": "Cân bằng dịch",
        "size": "medium"
    },
    "Sedation Status": {
        "icon": "💤",
        "description": "Trạng thái an thần",
        "size": "small"
    },
    "Scoring Systems": {
        "icon": "📊",
        "description": "Hệ thống đánh giá",
        "size": "medium"
    },
    "Quick Actions": {
        "icon": "⚡",
        "description": "Hành động nhanh",
        "size": "large"
    },
    "Recent Calculations": {
        "icon": "🕐",
        "description": "Tính toán gần đây",
        "size": "medium"
    }
}


def init_dashboard_config():
    """Initialize dashboard configuration"""
    if 'dashboard_config' not in st.session_state:
        st.session_state['dashboard_config'] = {
            'widgets': [],
            'layout': 'grid',
            'columns': 3
        }


def save_dashboard_config():
    """Save dashboard configuration"""
    config = st.session_state.get('dashboard_config', {})
    # In real implementation, save to file or database
    return config


def load_dashboard_config() -> Dict:
    """Load dashboard configuration"""
    return st.session_state.get('dashboard_config', {
        'widgets': [],
        'layout': 'grid',
        'columns': 3
    })


def render_widget(widget_type: str, config: Optional[Dict] = None):
    """Render a dashboard widget"""
    widget_info = AVAILABLE_WIDGETS.get(widget_type)
    
    if not widget_info:
        return
    
    if widget_type == "Alerts Summary":
        from critical_care.clinical_alerts import render_alerts_summary
        summary = render_alerts_summary()
        if summary:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("🚨", summary.get('critical', 0))
            with col2:
                st.metric("⚠️", summary.get('warning', 0))
            with col3:
                st.metric("ℹ️", summary.get('info', 0))
            with col4:
                st.metric("📊", summary.get('total', 0))
    
    elif widget_type == "Ventilator Status":
        st.markdown("#### 🫁 Máy thở")
        if 'patient_data' in st.session_state:
            vent_data = st.session_state['patient_data'].get('ventilator', {})
            if vent_data:
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Mode:** {vent_data.get('mode', 'N/A')}")
                    st.write(f"**Vt:** {vent_data.get('vt_ml', 0):.0f} mL")
                    st.write(f"**RR:** {vent_data.get('rr', 0):.0f} /min")
                with col2:
                    st.write(f"**PEEP:** {vent_data.get('peep', 0):.0f} cmH2O")
                    st.write(f"**FiO2:** {vent_data.get('fio2', 0):.1f}")
                    st.write(f"**Plateau:** {vent_data.get('plateau', 0):.1f} cmH2O")
            else:
                st.info("Chưa có dữ liệu máy thở")
    
    elif widget_type == "ABG Values":
        st.markdown("#### 🩸 ABG")
        if 'patient_data' in st.session_state:
            abg_data = st.session_state['patient_data'].get('abg', {})
            if abg_data:
                st.write(f"**pH:** {abg_data.get('ph', 0):.2f}")
                st.write(f"**PaCO2:** {abg_data.get('paco2', 0):.1f} mmHg")
                st.write(f"**PaO2:** {abg_data.get('pao2', 0):.1f} mmHg")
                st.write(f"**P/F:** {abg_data.get('pf_ratio', 0):.0f}")
            else:
                st.info("Chưa có dữ liệu ABG")
    
    elif widget_type == "Fluid Balance":
        st.markdown("#### 💧 Cân bằng dịch")
        if 'patient_data' in st.session_state:
            fluid_data = st.session_state['patient_data'].get('fluid', {})
            if fluid_data:
                balance = fluid_data.get('balance', 0)
                st.metric("Balance", f"{balance:+.0f} mL/24h")
            else:
                st.info("Chưa có dữ liệu dịch")
    
    elif widget_type == "Sedation Status":
        st.markdown("#### 💤 An thần")
        if 'patient_data' in st.session_state:
            sed_data = st.session_state['patient_data'].get('sedation', {})
            if sed_data:
                rass = sed_data.get('rass', None)
                if rass is not None:
                    st.metric("RASS", f"{rass}")
                else:
                    st.info("Chưa có RASS")
            else:
                st.info("Chưa có dữ liệu an thần")
    
    elif widget_type == "Scoring Systems":
        st.markdown("#### 📊 Scoring")
        if st.button("Mở Scoring Systems", use_container_width=True):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.rerun()
    
    elif widget_type == "Quick Actions":
        st.markdown("#### ⚡ Hành động nhanh")
        actions = [
            ("💧", "Fluid", "💧 Fluid Therapy"),
            ("💉", "Vasopressor", "💉 Vasopressors"),
            ("🫁", "Ventilator", "🫁 Ventilator Management"),
            ("💤", "Sedation", "💤 Sedation & Analgesia")
        ]
        cols = st.columns(2)
        for idx, (icon, label, tool) in enumerate(actions):
            with cols[idx % 2]:
                if st.button(f"{icon} {label}", key=f"quick_{idx}", use_container_width=True):
                    st.session_state['critical_care_tool_selection'] = tool
                    st.rerun()
    
    elif widget_type == "Recent Calculations":
        st.markdown("#### 🕐 Gần đây")
        st.info("Tính năng đang phát triển")


def render_dashboard_builder():
    """Render dashboard builder interface"""
    st.header("🎨 Dashboard Builder")
    st.caption("Tạo dashboard tùy chỉnh với drag-and-drop widgets")
    
    init_dashboard_config()
    
    config = load_dashboard_config()
    
    st.markdown("---")
    
    # Layout settings
    st.markdown("### ⚙️ Cài đặt layout")
    
    col1, col2 = st.columns(2)
    
    with col1:
        layout_type = st.selectbox(
            "Loại layout:",
            ["Grid", "List", "Custom"],
            key="dashboard_layout"
        )
    
    with col2:
        num_columns = st.number_input(
            "Số cột:",
            min_value=1,
            max_value=6,
            value=config.get('columns', 3),
            key="dashboard_columns"
        )
    
    st.markdown("---")
    
    # Widget selection
    st.markdown("### 📦 Chọn widgets")
    
    available_widgets = list(AVAILABLE_WIDGETS.keys())
    selected_widgets = st.multiselect(
        "Chọn widgets để thêm:",
        available_widgets,
        default=config.get('widgets', []),
        format_func=lambda x: f"{AVAILABLE_WIDGETS[x]['icon']} {x}",
        key="selected_widgets"
    )
    
    # Save configuration
    if st.button("💾 Lưu cấu hình", use_container_width=True):
        st.session_state['dashboard_config'] = {
            'widgets': selected_widgets,
            'layout': layout_type.lower(),
            'columns': num_columns
        }
        st.success("✅ Đã lưu cấu hình!")
    
    st.markdown("---")
    
    # Preview dashboard
    st.markdown("### 👁️ Xem trước dashboard")
    
    if selected_widgets:
        # Render widgets in grid
        if layout_type == "Grid":
            # Calculate rows needed
            rows = (len(selected_widgets) + num_columns - 1) // num_columns
            
            for row in range(rows):
                cols = st.columns(num_columns)
                for col_idx in range(num_columns):
                    widget_idx = row * num_columns + col_idx
                    if widget_idx < len(selected_widgets):
                        with cols[col_idx]:
                            widget_type = selected_widgets[widget_idx]
                            with st.container():
                                st.markdown(f"**{AVAILABLE_WIDGETS[widget_type]['icon']} {widget_type}**")
                                render_widget(widget_type)
        else:
            # List layout
            for widget_type in selected_widgets:
                with st.expander(f"{AVAILABLE_WIDGETS[widget_type]['icon']} {widget_type}"):
                    render_widget(widget_type)
    else:
        st.info("Chọn widgets để xem trước")
    
    st.markdown("---")
    
    # Reset button
    if st.button("🔄 Reset về mặc định", use_container_width=True):
        st.session_state['dashboard_config'] = {
            'widgets': [],
            'layout': 'grid',
            'columns': 3
        }
        st.rerun()
