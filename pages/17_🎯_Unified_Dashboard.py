"""
Unified Dashboard - Integration of Project Tracker & Guidelines Tracker
Comprehensive overview of project progress and guideline implementation
"""

import streamlit as st
import json
from pathlib import Path
from datetime import datetime
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from guidelines.data import get_all_guidelines, get_category_list

# Try to import tracker utils
try:
    from utils.tracker_utils import (
        calculate_phase_health,
        calculate_overall_progress,
        get_upcoming_milestones,
        generate_progress_report
    )
    TRACKER_UTILS_AVAILABLE = True
except ImportError:
    TRACKER_UTILS_AVAILABLE = False

# Standard page setup
setup_page(
    page_title="Unified Dashboard",
    page_icon="🎯",
    description="Tổng quan dự án và guidelines implementation"
)

# Custom CSS
st.markdown("""
<style>
/* Unified Dashboard Styles */
.unified-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    margin: 12px 0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.unified-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    transform: translateY(-2px);
    transition: all 0.3s;
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 20px 0;
}

.metric-box {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 24px;
    border-radius: 12px;
    text-align: center;
}

.metric-box.secondary {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.metric-box.success {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.metric-box.warning {
    background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
}

.metric-value {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 8px 0;
}

.metric-label {
    font-size: 0.9rem;
    opacity: 0.95;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.integration-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: #f0f7ff;
    border: 1px solid #0066CC;
    border-radius: 8px;
    color: #0066CC;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s;
}

.integration-link:hover {
    background: #e1effe;
    transform: translateX(4px);
}

.priority-matrix {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin: 16px 0;
}

.priority-cell {
    padding: 16px;
    border-radius: 8px;
    border: 2px solid #e0e0e0;
}

.priority-high {
    background: #fff3e0;
    border-color: #ff9800;
}

.priority-medium {
    background: #e3f2fd;
    border-color: #2196f3;
}

.priority-low {
    background: #f1f8e9;
    border-color: #8bc34a;
}
</style>
""", unsafe_allow_html=True)

# Load project data
DATA_FILE = Path("project_tracker_data.json")

def load_project_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {'phases': [], 'tasks': [], 'milestones': [], 'updates': []}

project_data = load_project_data()

# Load guidelines data
all_guidelines = get_all_guidelines()

# Hero section
render_hero(
    title="Unified Dashboard",
    subtitle="🎯 Project & Guidelines Overview",
    description="Tổng quan toàn diện về tiến độ dự án và triển khai guidelines",
    icon="🎯",
    gradient=("#667eea", "#764ba2")
)

# Sidebar
with st.sidebar:
    st.header("🎯 Unified Dashboard")
    
    view_mode = st.radio(
        "Chế độ xem:",
        ["Overview", "Project Focus", "Guidelines Focus", "Integration Matrix"],
        key="unified_view_mode"
    )
    
    st.markdown("---")
    
    # Quick stats
    total_phases = len(project_data.get('phases', []))
    total_guidelines = len(all_guidelines)
    
    st.metric("Project Phases", total_phases)
    st.metric("Guidelines", total_guidelines)
    
    st.markdown("---")
    
    render_info_box("""
    **🎯 Unified Dashboard:**
    - Tổng quan project + guidelines
    - Implementation tracking
    - Cross-referencing
    - Priority matrix
    
    **💡 Features:**
    - Combined metrics
    - Integration status
    - Smart recommendations
    """, type="info", title="About")

# Main content
if view_mode == "Overview":
    # Try to render personalized dashboard widgets
    try:
        from components.dashboard_widgets import render_dashboard_layout
        with st.expander("🏠 Personalized Dashboard", expanded=True):
            render_dashboard_layout(
                show_quick_access=True,
                show_activity=True,
                show_recommendations=True,
                show_stats=True
            )
        st.markdown("---")
    except ImportError:
        pass

if view_mode == "Overview":
    st.markdown("### 📊 Combined Overview")
    
    # Top-level metrics
    st.markdown('<div class="metric-grid">', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Project Phases</div>
            <div class="metric-value">{}</div>
        </div>
        """.format(total_phases), unsafe_allow_html=True)
    
    with col2:
        completed_phases = len([p for p in project_data.get('phases', []) if p.get('status') == 'completed'])
        st.markdown("""
        <div class="metric-box secondary">
            <div class="metric-label">Completed</div>
            <div class="metric-value">{}</div>
        </div>
        """.format(completed_phases), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box success">
            <div class="metric-label">Guidelines</div>
            <div class="metric-value">{}</div>
        </div>
        """.format(total_guidelines), unsafe_allow_html=True)
    
    with col4:
        # Mock implementation count
        implemented = 45  # This would come from actual data
        st.markdown("""
        <div class="metric-box warning">
            <div class="metric-label">Implemented</div>
            <div class="metric-value">{}</div>
        </div>
        """.format(implemented), unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project Progress Section
    st.markdown("### 📈 Project Progress")
    
    if TRACKER_UTILS_AVAILABLE and project_data.get('phases'):
        overall_progress = calculate_overall_progress(project_data.get('phases', []))
        st.progress(overall_progress / 100)
        st.caption(f"Overall Progress: {overall_progress:.1f}%")
    else:
        st.info("No project data available. Add phases in Project Tracker.")
    
    # Guidelines Coverage Section
    st.markdown("### 📋 Guidelines Coverage")
    
    # Group guidelines by category
    categories = {}
    for guideline in all_guidelines:
        cat = guideline.category
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(guideline)
    
    # Display coverage by category
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### By Specialty")
        for cat, guides in sorted(categories.items())[:5]:
            st.metric(cat, len(guides))
    
    with col2:
        st.markdown("#### Recent Guidelines")
        recent = sorted(all_guidelines, key=lambda x: x.year, reverse=True)[:5]
        for g in recent:
            st.caption(f"**{g.year}** - {g.title_vn[:50]}...")
    
    st.markdown("---")
    
    # Integration Status
    st.markdown("### 🔗 Integration Status")
    
    st.markdown("""
    <div class="unified-card">
        <h4>📊 Project ↔ Guidelines Integration</h4>
        <p><strong>Status:</strong> 🔄 In Development</p>
        <p><strong>Features Ready:</strong></p>
        <ul>
            <li>✅ Project Tracker with Smart Insights</li>
            <li>✅ Guidelines Tracker with Search</li>
            <li>🔄 Cross-referencing (In Progress)</li>
            <li>📅 Unified Dashboard (This Page - Prototype)</li>
            <li>📅 Implementation Tracking (Planned)</li>
        </ul>
        <p><strong>Next Steps:</strong></p>
        <ul>
            <li>Link guidelines to project phases</li>
            <li>Track implementation status</li>
            <li>Add automated notifications</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick Links
    st.markdown("### 🔗 Quick Links")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Open Project Tracker", use_container_width=True):
            st.switch_page("pages/16_📊_Project_Tracker.py")
    
    with col2:
        if st.button("📋 Open Guidelines Tracker", use_container_width=True):
            st.switch_page("pages/15_📋_Guidelines_Tracker.py")

elif view_mode == "Project Focus":
    st.markdown("### 📊 Project-Centric View")
    
    phases = project_data.get('phases', [])
    
    if not phases:
        st.info("No project phases yet. Add phases in Project Tracker.")
    else:
        for phase in phases:
            with st.expander(f"{phase['name']} ({phase.get('progress', 0)}%)"):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.markdown(f"**Description:** {phase.get('description', 'N/A')}")
                    st.markdown(f"**Timeline:** {phase.get('start_date', 'N/A')} → {phase.get('end_date', 'N/A')}")
                    st.markdown(f"**Status:** {phase.get('status', 'not_started')}")
                    
                    if TRACKER_UTILS_AVAILABLE:
                        health, color = calculate_phase_health(phase)
                        st.markdown(f"**Health:** :{health}:")
                
                with col2:
                    st.markdown("**Related Guidelines:**")
                    # Mock data - would be real links
                    st.caption("🔗 SSC Sepsis 2024")
                    st.caption("🔗 AHA Heart Failure 2023")
                    st.caption("➕ Add guideline link")

elif view_mode == "Guidelines Focus":
    st.markdown("### 📋 Guidelines-Centric View")
    
    # Filter by category
    selected_category = st.selectbox(
        "Filter by Specialty:",
        ["All"] + get_category_list()
    )
    
    # Filter guidelines
    if selected_category == "All":
        filtered_guidelines = all_guidelines
    else:
        filtered_guidelines = [g for g in all_guidelines if g.category == selected_category]
    
    st.success(f"Showing {len(filtered_guidelines)} guidelines")
    
    # Display guidelines with implementation status
    for guideline in filtered_guidelines[:10]:  # Show first 10
        with st.expander(f"{guideline.title_vn} ({guideline.year})"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Organization:** {guideline.organization}")
                st.markdown(f"**Category:** {guideline.category}")
                if guideline.description:
                    st.markdown(f"**Description:** {guideline.description}")
            
            with col2:
                st.markdown("**Implementation:**")
                # Mock implementation status
                st.caption("📊 Status: Not Started")
                st.caption("📅 Target: Q2 2025")
                st.caption("🔗 Phase: Phase 2")
                
                if st.button("Link to Phase", key=f"link_{guideline.id}"):
                    st.info("Feature coming soon!")

elif view_mode == "Integration Matrix":
    st.markdown("### 🎯 Priority Matrix")
    
    st.markdown("""
    <div class="priority-matrix">
        <div class="priority-cell priority-high">
            <h4>🔴 High Priority</h4>
            <p><strong>Guidelines:</strong></p>
            <ul>
                <li>SSC Sepsis 2024</li>
                <li>AHA Heart Failure 2023</li>
                <li>ESC Hypertension 2024</li>
            </ul>
            <p><strong>Phase:</strong> Phase 1-2</p>
        </div>
        
        <div class="priority-cell priority-medium">
            <h4>🟡 Medium Priority</h4>
            <p><strong>Guidelines:</strong></p>
            <ul>
                <li>GOLD COPD 2025</li>
                <li>KDIGO CKD 2020</li>
                <li>ADA Diabetes 2024</li>
            </ul>
            <p><strong>Phase:</strong> Phase 2-3</p>
        </div>
        
        <div class="priority-cell priority-low">
            <h4>🟢 Low Priority</h4>
            <p><strong>Guidelines:</strong></p>
            <ul>
                <li>GINA Asthma 2024</li>
                <li>Older guidelines</li>
                <li>Specialty-specific</li>
            </ul>
            <p><strong>Phase:</strong> Phase 3-4</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Implementation Roadmap
    st.markdown("### 🗺️ Implementation Roadmap")
    
    roadmap_data = {
        "Q1 2025": ["Setup infrastructure", "Phase 1 planning"],
        "Q2 2025": ["Implement high-priority guidelines", "Phase 1-2 execution"],
        "Q3 2025": ["Medium-priority guidelines", "Phase 3 planning"],
        "Q4 2025": ["Low-priority guidelines", "Phase 4 completion"]
    }
    
    for quarter, items in roadmap_data.items():
        with st.expander(f"📅 {quarter}"):
            for item in items:
                st.markdown(f"- {item}")

# Additional Info
st.markdown("---")
st.markdown("### 💡 About This Dashboard")

st.markdown("""
<div class="unified-card">
    <h4>🎯 Unified Dashboard - Prototype</h4>
    <p>This is a <strong>prototype</strong> of the unified dashboard that will integrate:</p>
    <ul>
        <li><strong>Project Tracker</strong> - Development progress and phases</li>
        <li><strong>Guidelines Tracker</strong> - Clinical guidelines database</li>
    </ul>
    
    <p><strong>Planned Features:</strong></p>
    <ul>
        <li>✅ Combined metrics and overview</li>
        <li>✅ Cross-referencing between projects and guidelines</li>
        <li>✅ Implementation status tracking</li>
        <li>✅ Priority matrix for planning</li>
        <li>🔄 Automated notifications (coming soon)</li>
        <li>🔄 Advanced analytics (coming soon)</li>
    </ul>
    
    <p><strong>See full integration plan:</strong> <code>docs/TRACKER_INTEGRATION_PLAN.md</code></p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
render_standard_footer(disclaimer=False)
