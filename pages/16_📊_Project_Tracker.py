"""
Project Tracker Dashboard
Track development progress, tasks, and milestones
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from utils.tracker_utils import (
    calculate_phase_health,
    calculate_overall_progress,
    get_upcoming_milestones,
    get_overdue_phases,
    generate_progress_report,
    suggest_next_actions,
    export_to_markdown
)
import json
from pathlib import Path

# Standard page setup
setup_page(
    page_title="Project Tracker",
    page_icon="📊",
    description="Theo dõi tiến độ phát triển dự án Clinical Assistant"
)

# Custom CSS for project tracker
st.markdown("""
<style>
/* Progress Bar Styles */
.progress-container {
    background: #f0f2f6;
    border-radius: 10px;
    padding: 4px;
    margin: 8px 0;
}

.progress-bar {
    background: linear-gradient(90deg, #4CAF50 0%, #45a049 100%);
    height: 24px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: 600;
    font-size: 0.85rem;
    transition: width 0.3s ease;
}

/* Status Badge Styles */
.status-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 2px;
}

.status-completed { background: #d4edda; color: #155724; }
.status-in-progress { background: #fff3cd; color: #856404; }
.status-not-started { background: #e2e3e5; color: #383d41; }
.status-blocked { background: #f8d7da; color: #721c24; }

/* Task Card Styles */
.task-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    margin: 8px 0;
    transition: all 0.2s;
}

.task-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}

/* Metric Card */
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin: 8px 0;
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 8px 0;
}

.metric-label {
    font-size: 0.9rem;
    opacity: 0.9;
}

/* Timeline Styles */
.timeline-item {
    border-left: 3px solid #667eea;
    padding-left: 20px;
    margin-left: 10px;
    margin-bottom: 20px;
    position: relative;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -8px;
    top: 0;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #667eea;
}

.timeline-date {
    font-size: 0.85rem;
    color: #666;
    font-weight: 600;
}

.timeline-content {
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

# Data file path
DATA_FILE = Path("project_tracker_data.json")

# Initialize session state
if 'project_data' not in st.session_state:
    st.session_state.project_data = {
        'phases': [],
        'tasks': [],
        'milestones': [],
        'updates': []
    }

# Load data from file if exists
def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return st.session_state.project_data

# Save data to file
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    st.session_state.project_data = data

# Load data on startup
project_data = load_data()

# Default phases if empty
if not project_data.get('phases'):
    project_data['phases'] = [
        {
            'id': 'phase1',
            'name': 'Phase 1: Quick Wins & Critical Features',
            'description': 'UI/UX improvements, Mobile optimization, DIRC Calculator',
            'start_date': '2025-02-01',
            'end_date': '2025-04-30',
            'status': 'not_started',
            'progress': 0
        },
        {
            'id': 'phase2',
            'name': 'Phase 2: Core Improvements',
            'description': 'ICU Tools, Drug Database Expansion, Search Enhancement',
            'start_date': '2025-05-01',
            'end_date': '2025-07-31',
            'status': 'not_started',
            'progress': 0
        },
        {
            'id': 'phase3',
            'name': 'Phase 3: Advanced Features',
            'description': 'Export improvements, Clinical Content, Advanced Analytics',
            'start_date': '2025-08-01',
            'end_date': '2025-10-31',
            'status': 'not_started',
            'progress': 0
        },
        {
            'id': 'phase4',
            'name': 'Phase 4: Infrastructure',
            'description': 'Performance optimization, Security, Scalability',
            'start_date': '2025-11-01',
            'end_date': '2026-01-31',
            'status': 'not_started',
            'progress': 0
        }
    ]
    save_data(project_data)

# Hero section
render_hero(
    title="Project Tracker Dashboard",
    subtitle="📊 Theo dõi tiến độ phát triển",
    description="Quản lý và theo dõi tiến độ phát triển Clinical Assistant với dashboard trực quan",
    icon="📊",
    gradient=("#667eea", "#764ba2")
)

# Sidebar
with st.sidebar:
    st.header("📊 Project Tracker")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Dashboard", "Phases", "Tasks", "Timeline", "Settings"],
        key="tracker_view_mode"
    )
    
    st.markdown("---")
    
    # Quick stats
    total_phases = len(project_data.get('phases', []))
    completed_phases = len([p for p in project_data.get('phases', []) if p.get('status') == 'completed'])
    
    st.metric("Total Phases", total_phases)
    st.metric("Completed", completed_phases)
    st.metric("Overall Progress", f"{(completed_phases/total_phases*100) if total_phases > 0 else 0:.0f}%")
    
    st.markdown("---")
    
    render_info_box("""
    **📊 Project Tracker:**
    - Theo dõi tiến độ các phases
    - Quản lý tasks và milestones
    - Timeline visualization
    - Progress tracking
    
    **💡 Tips:**
    - Cập nhật tiến độ thường xuyên
    - Đánh dấu tasks hoàn thành
    - Thêm notes cho các updates
    """, type="info", title="Hướng dẫn")

# Main content based on view mode
if view_mode == "Dashboard":
    st.markdown("### 📈 Project Overview")
    
    # Overall metrics
    col1, col2, col3, col4 = st.columns(4)
    
    phases = project_data.get('phases', [])
    total_phases = len(phases)
    completed = len([p for p in phases if p.get('status') == 'completed'])
    in_progress = len([p for p in phases if p.get('status') == 'in_progress'])
    not_started = len([p for p in phases if p.get('status') == 'not_started'])
    
    with col1:
        st.metric("Total Phases", total_phases)
    with col2:
        st.metric("✅ Completed", completed)
    with col3:
        st.metric("🔄 In Progress", in_progress)
    with col4:
        st.metric("⏳ Not Started", not_started)
    
    st.markdown("---")
    
    # Phase progress
    st.markdown("### 📊 Phase Progress")
    
    for phase in phases:
        with st.container():
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{phase['name']}**")
                st.caption(f"{phase['start_date']} → {phase['end_date']}")
                
                # Progress bar
                progress = phase.get('progress', 0)
                st.markdown(f"""
                <div class="progress-container">
                    <div class="progress-bar" style="width: {progress}%">
                        {progress}%
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                status = phase.get('status', 'not_started')
                status_map = {
                    'completed': ('✅', 'Completed', 'status-completed'),
                    'in_progress': ('🔄', 'In Progress', 'status-in-progress'),
                    'not_started': ('⏳', 'Not Started', 'status-not-started'),
                    'blocked': ('🚫', 'Blocked', 'status-blocked')
                }
                icon, label, css_class = status_map.get(status, ('⏳', 'Unknown', 'status-not-started'))
                st.markdown(f'<span class="status-badge {css_class}">{icon} {label}</span>', unsafe_allow_html=True)
            
            if phase.get('description'):
                st.caption(phase['description'])
            
            st.markdown("---")
    
    # Smart Insights Section
    st.markdown("### 💡 Smart Insights")
    
    # Generate suggestions
    suggestions = suggest_next_actions(project_data)
    
    # Display suggestions in an info box
    if suggestions:
        suggestions_text = "\n".join([f"- {s}" for s in suggestions])
        render_info_box(suggestions_text, type="info", title="Recommended Actions")
    
    # Upcoming milestones
    upcoming = get_upcoming_milestones(phases, days=30)
    if upcoming:
        st.markdown("#### 📅 Upcoming Milestones (Next 30 Days)")
        for milestone in upcoming:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**{milestone['phase_name']}**")
            with col2:
                st.caption(f"Due in {milestone['days_until']} days")
            with col3:
                st.caption(f"{milestone['progress']}% complete")
    
    # Overdue phases
    overdue = get_overdue_phases(phases)
    if overdue:
        st.markdown("#### ⚠️ Overdue Phases")
        for phase in overdue:
            st.warning(f"**{phase['phase_name']}** - {phase['days_overdue']} days overdue ({phase['progress']}% complete)")
    
    # Phase Health Summary
    st.markdown("#### 🏥 Phase Health")
    health_counts = {'on_track': 0, 'at_risk': 0, 'behind': 0, 'completed': 0, 'blocked': 0}
    for phase in phases:
        health, _ = calculate_phase_health(phase)
        if health in health_counts:
            health_counts[health] += 1
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("✅ On Track", health_counts['on_track'])
    with col2:
        st.metric("⚠️ At Risk", health_counts['at_risk'])
    with col3:
        st.metric("🔴 Behind", health_counts['behind'])
    with col4:
        st.metric("✅ Completed", health_counts['completed'])
    with col5:
        st.metric("🚫 Blocked", health_counts['blocked'])
    
    st.markdown("---")
    
    # Recent updates
    st.markdown("### 📝 Recent Updates")
    
    updates = project_data.get('updates', [])
    if updates:
        for update in updates[-5:]:  # Show last 5 updates
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-date">{update.get('date', 'N/A')}</div>
                <div class="timeline-content">
                    <strong>{update.get('title', 'Update')}</strong><br>
                    {update.get('description', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Chưa có updates nào. Thêm update đầu tiên ở tab Settings!")

elif view_mode == "Phases":
    st.markdown("### 📋 Phase Management")
    
    # Add new phase
    with st.expander("➕ Add New Phase"):
        with st.form("add_phase_form"):
            phase_name = st.text_input("Phase Name", placeholder="e.g., Phase 5: New Features")
            phase_desc = st.text_area("Description", placeholder="Brief description of this phase")
            
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("Start Date")
            with col2:
                end_date = st.date_input("End Date")
            
            if st.form_submit_button("Add Phase"):
                new_phase = {
                    'id': f"phase{len(project_data['phases']) + 1}",
                    'name': phase_name,
                    'description': phase_desc,
                    'start_date': start_date.strftime('%Y-%m-%d'),
                    'end_date': end_date.strftime('%Y-%m-%d'),
                    'status': 'not_started',
                    'progress': 0
                }
                project_data['phases'].append(new_phase)
                save_data(project_data)
                st.success(f"✅ Added phase: {phase_name}")
                st.rerun()
    
    st.markdown("---")
    
    # Edit existing phases
    st.markdown("### Edit Phases")
    
    for idx, phase in enumerate(project_data.get('phases', [])):
        with st.expander(f"{phase['name']} ({phase.get('progress', 0)}%)"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                new_progress = st.slider(
                    "Progress",
                    0, 100,
                    phase.get('progress', 0),
                    key=f"progress_{idx}"
                )
                
                new_status = st.selectbox(
                    "Status",
                    ['not_started', 'in_progress', 'completed', 'blocked'],
                    index=['not_started', 'in_progress', 'completed', 'blocked'].index(phase.get('status', 'not_started')),
                    key=f"status_{idx}"
                )
            
            with col2:
                if st.button("💾 Save", key=f"save_{idx}"):
                    project_data['phases'][idx]['progress'] = new_progress
                    project_data['phases'][idx]['status'] = new_status
                    save_data(project_data)
                    st.success("✅ Saved!")
                    st.rerun()
                
                if st.button("🗑️ Delete", key=f"delete_{idx}"):
                    project_data['phases'].pop(idx)
                    save_data(project_data)
                    st.success("✅ Deleted!")
                    st.rerun()

elif view_mode == "Tasks":
    st.markdown("### ✅ Task Management")
    st.info("Task management feature coming soon! This will allow you to create and track individual tasks within each phase.")

elif view_mode == "Timeline":
    st.markdown("### 📅 Project Timeline")
    
    # Create timeline visualization
    phases = project_data.get('phases', [])
    
    if phases:
        for phase in sorted(phases, key=lambda x: x.get('start_date', '')):
            st.markdown(f"""
            <div class="timeline-item">
                <div class="timeline-date">{phase.get('start_date', 'N/A')} - {phase.get('end_date', 'N/A')}</div>
                <div class="timeline-content">
                    <strong>{phase['name']}</strong> ({phase.get('progress', 0)}%)<br>
                    <small>{phase.get('description', '')}</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No phases to display in timeline.")

elif view_mode == "Settings":
    st.markdown("### ⚙️ Settings & Updates")
    
    # Add update
    with st.expander("📝 Add Project Update"):
        with st.form("add_update_form"):
            update_title = st.text_input("Update Title", placeholder="e.g., Completed Phase 1")
            update_desc = st.text_area("Description", placeholder="What was accomplished?")
            update_date = st.date_input("Date", value=datetime.now())
            
            if st.form_submit_button("Add Update"):
                new_update = {
                    'date': update_date.strftime('%Y-%m-%d'),
                    'title': update_title,
                    'description': update_desc
                }
                if 'updates' not in project_data:
                    project_data['updates'] = []
                project_data['updates'].append(new_update)
                save_data(project_data)
                st.success("✅ Update added!")
                st.rerun()
    
    st.markdown("---")
    
    # Export/Import data
    st.markdown("### 💾 Data Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📥 Export Data"):
            st.download_button(
                label="Download JSON",
                data=json.dumps(project_data, ensure_ascii=False, indent=2),
                file_name=f"project_tracker_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    with col2:
        uploaded_file = st.file_uploader("📤 Import Data", type=['json'])
        if uploaded_file:
            imported_data = json.load(uploaded_file)
            if st.button("Confirm Import"):
                save_data(imported_data)
                st.success("✅ Data imported successfully!")
                st.rerun()
    
    st.markdown("---")
    
    # Export Progress Report
    st.markdown("### 📊 Export Progress Report")
    
    if st.button("📄 Generate Markdown Report"):
        try:
            report_path = export_to_markdown(project_data, "project_progress_report.md")
            st.success(f"✅ Report generated: {report_path}")
            
            # Show download button
            with open(report_path, 'r', encoding='utf-8') as f:
                report_content = f.read()
            
            st.download_button(
                label="📥 Download Report",
                data=report_content,
                file_name=f"project_report_{datetime.now().strftime('%Y%m%d')}.md",
                mime="text/markdown"
            )
            
            # Show preview
            with st.expander("👁️ Preview Report"):
                st.markdown(report_content)
        except Exception as e:
            st.error(f"Error generating report: {e}")
    
    st.markdown("---")
    
    # Reset data
    if st.button("🔄 Reset to Default", type="secondary"):
        if st.checkbox("I understand this will delete all data"):
            project_data = {
                'phases': [],
                'tasks': [],
                'milestones': [],
                'updates': []
            }
            save_data(project_data)
            st.success("✅ Data reset!")
            st.rerun()

# Footer
st.markdown("---")
render_standard_footer(disclaimer=False)
