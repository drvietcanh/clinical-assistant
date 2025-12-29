"""
Protocol Timeline Component
Visual timeline for time-sensitive protocols
"""

import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime, timedelta


def render_timeline_item(
    time_label: str,
    title: str,
    description: str,
    status: str = "pending",  # pending, completed, urgent
    icon: str = "⏱️"
):
    """
    Render a single timeline item.
    
    Args:
        time_label: Time label (e.g., "0-1 hour", "Within 1 hour")
        title: Step title
        description: Step description
        status: Status (pending, completed, urgent)
        icon: Icon for the step
    """
    status_class = f"timeline-{status}"
    status_colors = {
        "pending": "#6C757D",
        "completed": "#28A745",
        "urgent": "#DC3545"
    }
    color = status_colors.get(status, "#6C757D")
    
    html = f"""
    <div class="protocol-timeline-item {status_class}" style="margin-bottom: 1.5rem;">
        <div style="display: flex; align-items: start; gap: 1rem;">
            <div style="flex-shrink: 0; width: 60px; text-align: center;">
                <div style="
                    background: {color};
                    color: white;
                    padding: 0.5rem;
                    border-radius: 8px;
                    font-weight: 600;
                    font-size: 0.875rem;
                ">{time_label}</div>
            </div>
            <div style="flex: 1;">
                <div style="
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                    margin-bottom: 0.5rem;
                ">
                    <span style="font-size: 1.25rem;">{icon}</span>
                    <h4 style="margin: 0; color: {color}; font-size: 1.1rem;">{title}</h4>
                </div>
                <p style="margin: 0; color: #6C757D; line-height: 1.6;">{description}</p>
            </div>
        </div>
    </div>
    """
    
    st.markdown(html, unsafe_allow_html=True)


def render_protocol_timeline(steps: List[Dict]):
    """
    Render a complete timeline for time-sensitive protocol.
    
    Args:
        steps: List of step dicts with keys: time_label, title, description, status, icon
    """
    st.markdown("### ⏱️ Timeline Điều Trị")
    
    for step in steps:
        render_timeline_item(
            time_label=step.get("time_label", ""),
            title=step.get("title", ""),
            description=step.get("description", ""),
            status=step.get("status", "pending"),
            icon=step.get("icon", "⏱️")
        )


def render_sepsis_1hour_timeline():
    """Render Sepsis 1-Hour Bundle timeline."""
    steps = [
        {
            "time_label": "0-1h",
            "title": "Đo Lactate",
            "description": "Lactate >2 mmol/L = septic shock. Đo lại sau 2-4h nếu tăng.",
            "status": "urgent",
            "icon": "🩸"
        },
        {
            "time_label": "0-1h",
            "title": "Cấy máu trước kháng sinh",
            "description": "2 bộ cấy máu từ 2 vị trí khác nhau. Cấy dịch từ ổ nhiễm nếu có.",
            "status": "urgent",
            "icon": "🧪"
        },
        {
            "time_label": "0-1h",
            "title": "Kháng sinh phổ rộng",
            "description": "Trong vòng 1 giờ. Theo guideline địa phương. Liều đủ, đường IV.",
            "status": "urgent",
            "icon": "💊"
        },
        {
            "time_label": "0-3h",
            "title": "Truyền dịch nhanh",
            "description": "30 mL/kg crystalloid trong 3 giờ đầu. Ringer Lactate hoặc Normal Saline.",
            "status": "urgent",
            "icon": "💉"
        },
        {
            "time_label": "Nếu cần",
            "title": "Vasopressor",
            "description": "Nếu MAP <65 mmHg sau truyền dịch. Norepinephrine là thuốc đầu tay. Mục tiêu MAP ≥65 mmHg.",
            "status": "pending",
            "icon": "📊"
        }
    ]
    
    render_protocol_timeline(steps)


def render_stroke_timeline():
    """Render Stroke protocol timeline."""
    steps = [
        {
            "time_label": "0-10min",
            "title": "Đánh giá nhanh",
            "description": "NIHSS, CT scan, labs cơ bản",
            "status": "urgent",
            "icon": "🔍"
        },
        {
            "time_label": "0-60min",
            "title": "Door-to-needle",
            "description": "tPA nếu đủ tiêu chuẩn. Không quá 60 phút từ khi đến viện.",
            "status": "urgent",
            "icon": "💉"
        },
        {
            "time_label": "0-6h",
            "title": "Mechanical Thrombectomy",
            "description": "Nếu đủ tiêu chuẩn. Tối đa 6 giờ từ khi khởi phát.",
            "status": "urgent",
            "icon": "🔧"
        }
    ]
    
    render_protocol_timeline(steps)


def render_progress_indicator(current_step: int, total_steps: int, step_names: List[str] = None):
    """
    Render progress indicator for multi-step protocol.
    
    Args:
        current_step: Current step number (1-indexed)
        total_steps: Total number of steps
        step_names: Optional list of step names
    """
    progress = (current_step / total_steps) * 100
    
    st.markdown("### 📊 Tiến Độ Điều Trị")
    
    # Progress bar
    st.progress(progress / 100)
    st.caption(f"Bước {current_step}/{total_steps} ({progress:.0f}%)")
    
    # Step list
    if step_names:
        st.markdown("**Các bước:**")
        for i, name in enumerate(step_names, 1):
            if i < current_step:
                st.markdown(f"✅ ~~{i}. {name}~~")
            elif i == current_step:
                st.markdown(f"🔄 **{i}. {name}** (Đang thực hiện)")
            else:
                st.markdown(f"⏳ {i}. {name}")


def render_countdown_timer(target_time: datetime, label: str = "Thời gian còn lại"):
    """
    Render countdown timer (requires JavaScript for real-time updates).
    This is a simplified version - full implementation would need JS.
    
    Args:
        target_time: Target datetime
        label: Label for the timer
    """
    remaining = target_time - datetime.now()
    
    if remaining.total_seconds() > 0:
        hours = int(remaining.total_seconds() // 3600)
        minutes = int((remaining.total_seconds() % 3600) // 60)
        seconds = int(remaining.total_seconds() % 60)
        
        st.markdown(f"### ⏰ {label}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Giờ", hours)
        with col2:
            st.metric("Phút", minutes)
        with col3:
            st.metric("Giây", seconds)
        
        if remaining.total_seconds() < 3600:  # Less than 1 hour
            st.warning("⚠️ Thời gian còn lại dưới 1 giờ!")
    else:
        st.error("⏰ Đã quá thời gian!")

