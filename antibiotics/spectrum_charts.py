"""
Visual Drug Spectrum Charts
Tạo biểu đồ phổ tác dụng trực quan cho kháng sinh
Sử dụng Plotly để tạo interactive charts
"""

import streamlit as st
from typing import Dict, List, Optional
from .antibiotics_data import ANTIBIOTICS_DATABASE

try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Spectrum data organized by organism groups
SPECTRUM_DATA = {
    "Gram-positive": {
        "Staphylococcus aureus (MSSA)": ["Vancomycin", "Cefazolin", "Ceftriaxone", "Clindamycin", "Linezolid"],
        "Staphylococcus aureus (MRSA)": ["Vancomycin", "Linezolid", "Daptomycin", "Tigecycline"],
        "Streptococcus pneumoniae": ["Penicillin", "Ceftriaxone", "Vancomycin", "Levofloxacin"],
        "Enterococcus faecalis": ["Ampicillin", "Vancomycin", "Linezolid"],
        "Enterococcus faecium": ["Vancomycin", "Linezolid", "Daptomycin"],
        "Coagulase-negative staphylococci": ["Vancomycin", "Cefazolin"],
    },
    "Gram-negative": {
        "E. coli": ["Ceftriaxone", "Ciprofloxacin", "Piperacillin-Tazobactam", "Meropenem"],
        "Klebsiella pneumoniae": ["Ceftriaxone", "Piperacillin-Tazobactam", "Meropenem", "Amikacin"],
        "Pseudomonas aeruginosa": ["Piperacillin-Tazobactam", "Ceftazidime", "Meropenem", "Ciprofloxacin"],
        "Acinetobacter baumannii": ["Meropenem", "Amikacin", "Colistin"],
        "Haemophilus influenzae": ["Ceftriaxone", "Azithromycin", "Levofloxacin"],
        "Neisseria meningitidis": ["Ceftriaxone", "Penicillin"],
    },
    "Atypical": {
        "Mycoplasma pneumoniae": ["Azithromycin", "Doxycycline", "Levofloxacin"],
        "Chlamydia pneumoniae": ["Azithromycin", "Doxycycline", "Levofloxacin"],
        "Legionella pneumophila": ["Azithromycin", "Levofloxacin"],
    },
    "Anaerobic": {
        "Bacteroides fragilis": ["Metronidazole", "Piperacillin-Tazobactam", "Meropenem"],
        "Clostridium difficile": ["Metronidazole", "Vancomycin (PO)", "Fidaxomicin"],
        "Clostridium perfringens": ["Penicillin", "Clindamycin", "Metronidazole"],
    },
}

# Color coding for spectrum coverage
SPECTRUM_COLORS = {
    "excellent": "#4caf50",  # Green
    "good": "#8bc34a",  # Light green
    "moderate": "#ffc107",  # Yellow
    "poor": "#ff9800",  # Orange
    "none": "#f44336",  # Red
}


def get_antibiotic_spectrum(antibiotic_name: str) -> Dict:
    """
    Get spectrum coverage for an antibiotic
    
    Returns:
        dict with organism groups and coverage level
    """
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        return {}
    
    ab_data = ANTIBIOTICS_DATABASE[antibiotic_name]
    spectrum_info = {}
    
    # Check coverage for each organism group
    for group, organisms in SPECTRUM_DATA.items():
        coverage_count = 0
        total_organisms = len(organisms)
        
        for organism, effective_drugs in organisms.items():
            if antibiotic_name in effective_drugs:
                coverage_count += 1
        
        if total_organisms > 0:
            coverage_percent = (coverage_count / total_organisms) * 100
            
            if coverage_percent >= 80:
                level = "excellent"
            elif coverage_percent >= 60:
                level = "good"
            elif coverage_percent >= 40:
                level = "moderate"
            elif coverage_percent > 0:
                level = "poor"
            else:
                level = "none"
            
            spectrum_info[group] = {
                "coverage_percent": coverage_percent,
                "coverage_count": coverage_count,
                "total_organisms": total_organisms,
                "level": level
            }
    
    return spectrum_info


def create_spectrum_bar_chart(antibiotic_name: str) -> Optional[go.Figure]:
    """Create a bar chart showing spectrum coverage by organism group"""
    
    if not PLOTLY_AVAILABLE:
        return None
    
    spectrum_info = get_antibiotic_spectrum(antibiotic_name)
    
    if not spectrum_info:
        return None
    
    groups = list(spectrum_info.keys())
    coverage_percents = [spectrum_info[g]["coverage_percent"] for g in groups]
    colors = [SPECTRUM_COLORS[spectrum_info[g]["level"]] for g in groups]
    
    fig = go.Figure(data=[
        go.Bar(
            x=groups,
            y=coverage_percents,
            marker_color=colors,
            text=[f"{p:.0f}%" for p in coverage_percents],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Coverage: %{y:.1f}%<extra></extra>',
        )
    ])
    
    fig.update_layout(
        title=f"Phổ Tác Dụng: {antibiotic_name}",
        xaxis_title="Nhóm Vi Khuẩn",
        yaxis_title="Tỷ lệ Bao Phủ (%)",
        yaxis=dict(range=[0, 100]),
        height=400,
        showlegend=False,
        template="plotly_white",
    )
    
    return fig


def create_spectrum_radar_chart(antibiotic_name: str) -> Optional[go.Figure]:
    """Create a radar chart showing spectrum coverage"""
    
    if not PLOTLY_AVAILABLE:
        return None
    
    spectrum_info = get_antibiotic_spectrum(antibiotic_name)
    
    if not spectrum_info:
        return None
    
    groups = list(spectrum_info.keys())
    coverage_percents = [spectrum_info[g]["coverage_percent"] for g in groups]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=coverage_percents,
        theta=groups,
        fill='toself',
        name=antibiotic_name,
        line_color='#1976D2',
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=True,
        title=f"Phổ Tác Dụng (Radar Chart): {antibiotic_name}",
        height=500,
    )
    
    return fig


def create_comparison_chart(antibiotic_names: List[str]) -> Optional[go.Figure]:
    """Create a comparison chart for multiple antibiotics"""
    
    if not PLOTLY_AVAILABLE or not antibiotic_names:
        return None
    
    # Get all groups
    all_groups = list(SPECTRUM_DATA.keys())
    
    fig = go.Figure()
    
    colors_list = px.colors.qualitative.Set3[:len(antibiotic_names)]
    
    for idx, ab_name in enumerate(antibiotic_names):
        spectrum_info = get_antibiotic_spectrum(ab_name)
        
        if not spectrum_info:
            continue
        
        coverage_percents = [spectrum_info.get(g, {}).get("coverage_percent", 0) for g in all_groups]
        
        fig.add_trace(go.Bar(
            name=ab_name,
            x=all_groups,
            y=coverage_percents,
            marker_color=colors_list[idx],
        ))
    
    fig.update_layout(
        title="So Sánh Phổ Tác Dụng",
        xaxis_title="Nhóm Vi Khuẩn",
        yaxis_title="Tỷ lệ Bao Phủ (%)",
        barmode='group',
        height=500,
        template="plotly_white",
    )
    
    return fig


def render_spectrum_charts(antibiotic_name: Optional[str] = None):
    """Render spectrum charts UI"""
    
    st.markdown("### 📊 Biểu Đồ Phổ Tác Dụng")
    st.caption("Trực quan hóa phổ tác dụng của kháng sinh theo nhóm vi khuẩn")
    
    if not PLOTLY_AVAILABLE:
        st.error("⚠️ Plotly không khả dụng. Vui lòng cài đặt: `pip install plotly`")
        return
    
    # Antibiotic selection
    if antibiotic_name is None:
        antibiotic_list = sorted(list(ANTIBIOTICS_DATABASE.keys()))
        selected_ab = st.selectbox(
            "Chọn kháng sinh:",
            options=antibiotic_list,
            key="spectrum_chart_ab_select"
        )
    else:
        selected_ab = antibiotic_name
    
    if not selected_ab or selected_ab not in ANTIBIOTICS_DATABASE:
        st.warning("⚠️ Vui lòng chọn kháng sinh")
        return
    
    # Get spectrum info
    spectrum_info = get_antibiotic_spectrum(selected_ab)
    
    if not spectrum_info:
        st.info("💡 Không có dữ liệu phổ tác dụng cho kháng sinh này")
        return
    
    # Display spectrum summary
    st.markdown("#### 📋 Tóm Tắt Phổ Tác Dụng")
    
    cols = st.columns(len(spectrum_info))
    for idx, (group, info) in enumerate(spectrum_info.items()):
        with cols[idx]:
            color = SPECTRUM_COLORS[info["level"]]
            st.markdown(f"""
            <div style='
                background: {color};
                color: white;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
            '>
                <h4 style='margin: 0 0 5px 0; color: white;'>{group}</h4>
                <p style='margin: 0; font-size: 1.5em; font-weight: bold;'>{info["coverage_percent"]:.0f}%</p>
                <p style='margin: 5px 0 0 0; font-size: 0.9em;'>{info["coverage_count"]}/{info["total_organisms"]} vi khuẩn</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Chart type selection
    chart_type = st.radio(
        "Loại biểu đồ:",
        ["📊 Bar Chart", "🕸️ Radar Chart"],
        horizontal=True,
        key="spectrum_chart_type"
    )
    
    # Create and display chart
    if chart_type == "📊 Bar Chart":
        fig = create_spectrum_bar_chart(selected_ab)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
    else:
        fig = create_spectrum_radar_chart(selected_ab)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
    
    # Detailed organism coverage
    st.markdown("---")
    st.markdown("#### 🔬 Chi Tiết Theo Từng Vi Khuẩn")
    
    for group, organisms in SPECTRUM_DATA.items():
        with st.expander(f"📋 {group}", expanded=False):
            for organism, effective_drugs in organisms.items():
                is_effective = selected_ab in effective_drugs
                icon = "✅" if is_effective else "❌"
                color = "#4caf50" if is_effective else "#f44336"
                
                st.markdown(f"""
                <div style='margin: 5px 0;'>
                    <span style='color: {color}; font-weight: bold;'>{icon}</span>
                    <strong>{organism}</strong>
                    {f'<span style="color: #666; font-size: 0.9em;"> - Có hiệu quả</span>' if is_effective else '<span style="color: #666; font-size: 0.9em;"> - Không hiệu quả</span>'}
                </div>
                """, unsafe_allow_html=True)
    
    # Comparison mode
    st.markdown("---")
    st.markdown("#### 🔬 So Sánh Nhiều Kháng Sinh")
    
    compare_mode = st.checkbox("Bật chế độ so sánh", key="spectrum_compare_mode")
    
    if compare_mode:
        antibiotic_list = sorted(list(ANTIBIOTICS_DATABASE.keys()))
        selected_abs = st.multiselect(
            "Chọn kháng sinh để so sánh (tối đa 5):",
            options=antibiotic_list,
            default=[selected_ab] if selected_ab else [],
            max_selections=5,
            key="spectrum_compare_select"
        )
        
        if len(selected_abs) >= 2:
            fig = create_comparison_chart(selected_abs)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("💡 Chọn ít nhất 2 kháng sinh để so sánh")


def render_spectrum_chart_inline(antibiotic_name: str):
    """Render a compact spectrum chart inline (for use in other views)"""
    
    if not PLOTLY_AVAILABLE:
        return
    
    spectrum_info = get_antibiotic_spectrum(antibiotic_name)
    
    if not spectrum_info:
        return
    
    # Create compact bar chart
    groups = list(spectrum_info.keys())
    coverage_percents = [spectrum_info[g]["coverage_percent"] for g in groups]
    colors = [SPECTRUM_COLORS[spectrum_info[g]["level"]] for g in groups]
    
    fig = go.Figure(data=[
        go.Bar(
            x=groups,
            y=coverage_percents,
            marker_color=colors,
            text=[f"{p:.0f}%" for p in coverage_percents],
            textposition='outside',
            hovertemplate='<b>%{x}</b><br>Coverage: %{y:.1f}%<extra></extra>',
        )
    ])
    
    fig.update_layout(
        title=f"Phổ Tác Dụng: {antibiotic_name}",
        xaxis_title="Nhóm Vi Khuẩn",
        yaxis_title="Tỷ lệ Bao Phủ (%)",
        yaxis=dict(range=[0, 100]),
        height=300,
        showlegend=False,
        template="plotly_white",
        margin=dict(l=50, r=50, t=50, b=50),
    )
    
    st.plotly_chart(fig, use_container_width=True)
