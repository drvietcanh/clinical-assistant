"""
Protocol Progress Tracking Component
Checklist and progress tracking for multi-step protocols
"""

import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime


def get_protocol_progress(protocol_name: str) -> Dict:
    """
    Get progress state for a protocol.
    
    Args:
        protocol_name: Name of the protocol
        
    Returns:
        Dict with progress state
    """
    key = f"protocol_progress_{protocol_name}".replace(" ", "_")
    return st.session_state.get(key, {
        "completed_steps": [],
        "started_at": None,
        "completed_at": None
    })


def save_protocol_progress(protocol_name: str, progress: Dict):
    """
    Save progress state for a protocol.
    
    Args:
        protocol_name: Name of the protocol
        progress: Progress dict to save
    """
    key = f"protocol_progress_{protocol_name}".replace(" ", "_")
    st.session_state[key] = progress


def render_progress_checklist(
    protocol_name: str,
    steps: List[Dict],
    title: str = "📊 Tiến Độ Điều Trị"
):
    """
    Render progress checklist for multi-step protocol.
    
    Args:
        protocol_name: Name of the protocol
        steps: List of step dicts with keys: id, title, description, time_limit
        title: Section title
    """
    progress = get_protocol_progress(protocol_name)
    completed_steps = set(progress.get("completed_steps", []))
    
    # Initialize started_at if first time
    if not progress.get("started_at"):
        progress["started_at"] = datetime.now().isoformat()
        save_protocol_progress(protocol_name, progress)
    
    st.markdown(f"### {title}")
    
    # Progress bar
    total_steps = len(steps)
    completed_count = len(completed_steps)
    progress_percent = (completed_count / total_steps * 100) if total_steps > 0 else 0
    
    st.progress(progress_percent / 100)
    st.caption(f"**Tiến độ:** {completed_count}/{total_steps} bước ({progress_percent:.0f}%)")
    
    st.markdown("---")
    
    # Checklist
    st.markdown("**Danh sách bước:**")
    
    for idx, step in enumerate(steps, 1):
        step_id = step.get("id", f"step_{idx}")
        is_completed = step_id in completed_steps
        
        # Create columns for checkbox and content
        col1, col2 = st.columns([1, 10])
        
        with col1:
            checkbox_key = f"step_{protocol_name}_{step_id}".replace(" ", "_")
            checked = st.checkbox(
                "",
                value=is_completed,
                key=checkbox_key,
                label_visibility="collapsed"
            )
            
            # Update progress when checkbox changes
            if checked != is_completed:
                if checked:
                    completed_steps.add(step_id)
                else:
                    completed_steps.discard(step_id)
                
                progress["completed_steps"] = list(completed_steps)
                
                # Mark as completed if all steps done
                if len(completed_steps) == total_steps:
                    progress["completed_at"] = datetime.now().isoformat()
                
                save_protocol_progress(protocol_name, progress)
                st.rerun()
        
        with col2:
            # Display step with status
            status_icon = "✅" if is_completed else "⏳"
            status_color = "#28A745" if is_completed else "#6C757D"
            
            st.markdown(f"""
            <div style="margin-bottom: 1rem;">
                <span style="color: {status_color}; font-size: 1.2rem;">{status_icon}</span>
                <strong style="color: {status_color};">Bước {idx}: {step.get('title', '')}</strong>
                {f"<p style='color: #6C757D; margin-top: 0.25rem;'>{step.get('description', '')}</p>" if step.get('description') else ''}
                {f"<span style='color: #DC3545; font-size: 0.875rem;'>⏱️ {step.get('time_limit', '')}</span>" if step.get('time_limit') else ''}
            </div>
            """, unsafe_allow_html=True)
    
    # Reset button
    if completed_count > 0:
        st.markdown("---")
        if st.button("🔄 Reset Tiến Độ", key=f"reset_{protocol_name}".replace(" ", "_"), type="secondary"):
            progress = {
                "completed_steps": [],
                "started_at": None,
                "completed_at": None
            }
            save_protocol_progress(protocol_name, progress)
            st.rerun()
    
    # Completion message
    if completed_count == total_steps:
        st.success("🎉 **Hoàn thành!** Tất cả các bước đã được thực hiện.")


def render_sepsis_progress(protocol_name: str = "Sepsis 1-Hour Bundle"):
    """
    Render progress checklist for Sepsis 1-Hour Bundle.
    
    Args:
        protocol_name: Name of the protocol
    """
    steps = [
        {
            "id": "lactate",
            "title": "Đo Lactate",
            "description": "Lactate >2 mmol/L = septic shock. Đo lại sau 2-4h nếu tăng.",
            "time_limit": "Trong 1 giờ"
        },
        {
            "id": "blood_culture",
            "title": "Cấy máu trước kháng sinh",
            "description": "2 bộ cấy máu từ 2 vị trí khác nhau. Cấy dịch từ ổ nhiễm nếu có.",
            "time_limit": "Trong 1 giờ"
        },
        {
            "id": "antibiotics",
            "title": "Kháng sinh phổ rộng",
            "description": "Theo guideline địa phương. Liều đủ, đường IV.",
            "time_limit": "Trong 1 giờ"
        },
        {
            "id": "fluids",
            "title": "Truyền dịch nhanh",
            "description": "30 mL/kg crystalloid. Ringer Lactate hoặc Normal Saline.",
            "time_limit": "Trong 3 giờ đầu"
        },
        {
            "id": "vasopressor",
            "title": "Vasopressor nếu cần",
            "description": "Nếu MAP <65 mmHg sau truyền dịch. Norepinephrine là thuốc đầu tay.",
            "time_limit": "Khi cần"
        }
    ]
    
    render_progress_checklist(protocol_name, steps)


def render_stroke_progress(protocol_name: str = "Stroke Management"):
    """
    Render progress checklist for Stroke protocol.
    
    Args:
        protocol_name: Name of the protocol
    """
    steps = [
        {
            "id": "assessment",
            "title": "Đánh giá nhanh",
            "description": "NIHSS, CT scan, labs cơ bản",
            "time_limit": "0-10 phút"
        },
        {
            "id": "tpa",
            "title": "Door-to-needle",
            "description": "tPA nếu đủ tiêu chuẩn",
            "time_limit": "0-60 phút"
        },
        {
            "id": "thrombectomy",
            "title": "Mechanical Thrombectomy",
            "description": "Nếu đủ tiêu chuẩn",
            "time_limit": "0-6 giờ"
        }
    ]
    
    render_progress_checklist(protocol_name, steps)

