"""
Visual Drug Comparison
Create visual charts and graphs for drug comparison
"""

import streamlit as st
import pandas as pd
from typing import List, Dict, Any, Optional

try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False


def render_spectrum_chart(
    comparison_data: List[Dict[str, Any]],
    drugs: List[str]
) -> None:
    """
    Render spectrum comparison chart with real susceptibility data from MIC breakpoints
    
    Args:
        comparison_data: List of drug data dicts
        drugs: List of drug names
    """
    if not PLOTLY_AVAILABLE:
        st.warning("⚠️ Plotly không khả dụng. Vui lòng cài đặt: `pip install plotly`")
        return
    
    st.markdown("### 📊 Biểu Đồ Phổ Tác Dụng (Độ Nhạy Cảm)")
    
    # Get real susceptibility data from MIC breakpoints
    try:
        from .mic_breakpoints import get_common_susceptibility
        from .antibiotics_data import ANTIBIOTICS_DATABASE
    except ImportError:
        st.error("Không thể tải dữ liệu MIC breakpoints")
        return
    
    # Common organisms to compare
    common_organisms = [
        "E. coli",
        "K. pneumoniae", 
        "S. pneumoniae",
        "P. aeruginosa",
        "S. aureus (MSSA)",
        "MRSA",
        "Enterococcus faecalis"
    ]
    
    # Prepare data: drug x organism susceptibility percentages
    chart_data = []
    
    for drug_name in drugs:
        if drug_name not in ANTIBIOTICS_DATABASE:
            continue
        
        suscept_data = get_common_susceptibility(drug_name)
        
        for org in common_organisms:
            # Try to find matching organism in susceptibility data
            org_key = None
            for key in suscept_data.keys() if suscept_data else []:
                if org.lower() in key.lower() or key.lower() in org.lower():
                    org_key = key
                    break
            
            if org_key and suscept_data:
                pattern = suscept_data[org_key]
                # Extract percentage from pattern like "S (85-90%)" or "S (90-95%)"
                percentage = 0
                try:
                    if "S (" in pattern:
                        s_part = pattern.split("S (")[1].split("%")[0]
                        # Handle range like "85-90" -> take average
                        if "-" in s_part:
                            parts = s_part.split("-")
                            percentage = (float(parts[0].strip()) + float(parts[1].strip())) / 2
                        else:
                            percentage = float(s_part.strip())
                    elif "R (" in pattern:
                        r_part = pattern.split("R (")[1].split("%")[0]
                        if "-" in r_part:
                            parts = r_part.split("-")
                            percentage = 100 - (float(parts[0].strip()) + float(parts[1].strip())) / 2
                        else:
                            percentage = 100 - float(r_part.strip())
                except (ValueError, IndexError):
                    percentage = 0
                
                chart_data.append({
                    'Thuốc': drug_name,
                    'Vi khuẩn': org,
                    'Độ nhạy (%)': percentage
                })
    
    if not chart_data:
        st.info("Không có dữ liệu độ nhạy cảm để hiển thị")
        return
    
    df_chart = pd.DataFrame(chart_data)
    
    # Create heatmap
    pivot_df = df_chart.pivot(index='Vi khuẩn', columns='Thuốc', values='Độ nhạy (%)')
    pivot_df = pivot_df.fillna(0)
    
    # Create heatmap
    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        colorscale=[
            [0, '#F44336'],  # Red for low susceptibility
            [0.5, '#FFC107'],  # Yellow for medium
            [1, '#4CAF50']  # Green for high
        ],
        text=[[f"{val:.0f}%" if val > 0 else "" for val in row] for row in pivot_df.values],
        texttemplate='%{text}',
        textfont={"size": 12},
        showscale=True,
        colorbar=dict(
            title="Độ nhạy (%)",
            titleside="right"
        ),
        hovertemplate='<b>%{y}</b><br>%{x}<br>Độ nhạy: %{z:.1f}%<extra></extra>'
    ))
    
    fig.update_layout(
        title='Heatmap Độ Nhạy Cảm - So Sánh Kháng Sinh',
        xaxis_title='Kháng sinh',
        yaxis_title='Vi khuẩn',
        height=400 + len(common_organisms) * 30,
        xaxis={'side': 'bottom'},
        yaxis={'side': 'left'}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add bar chart for better comparison
    st.markdown("#### 📊 Biểu Đồ Cột So Sánh")
    
    # Group by organism
    fig_bar = go.Figure()
    
    organisms = df_chart['Vi khuẩn'].unique()
    colors = px.colors.qualitative.Set3[:len(drugs)]
    
    for i, drug_name in enumerate(drugs):
        drug_data = df_chart[df_chart['Thuốc'] == drug_name]
        percentages = []
        for org in organisms:
            org_data = drug_data[drug_data['Vi khuẩn'] == org]
            if not org_data.empty:
                percentages.append(org_data.iloc[0]['Độ nhạy (%)'])
            else:
                percentages.append(0)
        
        fig_bar.add_trace(go.Bar(
            name=drug_name,
            x=organisms,
            y=percentages,
            marker_color=colors[i % len(colors)],
            text=[f"{p:.0f}%" if p > 0 else "" for p in percentages],
            textposition='outside'
        ))
    
    fig_bar.update_layout(
        title='So Sánh Độ Nhạy Cảm Theo Vi Khuẩn',
        xaxis_title='Vi khuẩn',
        yaxis_title='Độ nhạy (%)',
        barmode='group',
        height=500,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis={'tickangle': -45}
    )
    
    st.plotly_chart(fig_bar, use_container_width=True)


def render_dosing_comparison_chart(
    comparison_data: List[Dict[str, Any]],
    drugs: List[str]
) -> None:
    """
    Render dosing comparison with visual charts
    
    Args:
        comparison_data: List of drug data dicts
        drugs: List of drug names
    """
    if not PLOTLY_AVAILABLE:
        st.warning("⚠️ Plotly không khả dụng. Vui lòng cài đặt: `pip install plotly`")
        return
    
    st.markdown("### 💉 So Sánh Liều Dùng")
    
    try:
        from .antibiotics_data import ANTIBIOTICS_DATABASE
        from .dosing_calculator import calculate_detailed_dose, calculate_ibw, calculate_abw
    except ImportError:
        st.error("Không thể tải dữ liệu dosing")
        return
    
    # Standard patient parameters for comparison
    weight = 70  # kg
    height = 170  # cm
    crcl = 70  # mL/min
    ibw = calculate_ibw(height, "Nam")
    abw = weight
    
    # Prepare dosing data
    dosing_data = []
    for drug_name in drugs:
        if drug_name not in ANTIBIOTICS_DATABASE:
            continue
        
        detailed = calculate_detailed_dose(
            drug_name, weight, ibw, abw, crcl,
            indication="standard",
            is_pediatric=False
        )
        
        if detailed and detailed.get('calculated_dose_mg'):
            dosing_data.append({
                'Thuốc': drug_name,
                'Liều (mg)': detailed['calculated_dose_mg'],
                'Khoảng cách (giờ)': detailed.get('interval_hours', 0),
                'Tần suất': detailed.get('frequency', 'N/A')
            })
    
    if not dosing_data:
        st.info("Không có dữ liệu liều dùng để so sánh")
        return
    
    df_dosing = pd.DataFrame(dosing_data)
    
    # Create bar chart for doses
    fig_dose = go.Figure(data=[
        go.Bar(
            x=df_dosing['Thuốc'],
            y=df_dosing['Liều (mg)'],
            marker_color='#2196F3',
            text=[f"{dose:.0f} mg" for dose in df_dosing['Liều (mg)']],
            textposition='outside'
        )
    ])
    
    fig_dose.update_layout(
        title='So Sánh Liều Dùng (mg)',
        xaxis_title='Kháng sinh',
        yaxis_title='Liều (mg)',
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig_dose, use_container_width=True)
    
    # Create bar chart for intervals
    fig_interval = go.Figure(data=[
        go.Bar(
            x=df_dosing['Thuốc'],
            y=df_dosing['Khoảng cách (giờ)'],
            marker_color='#4CAF50',
            text=[f"{int(interval)}h" if interval > 0 else "N/A" for interval in df_dosing['Khoảng cách (giờ)']],
            textposition='outside'
        )
    ])
    
    fig_interval.update_layout(
        title='So Sánh Khoảng Cách Giữa Các Liều',
        xaxis_title='Kháng sinh',
        yaxis_title='Khoảng cách (giờ)',
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig_interval, use_container_width=True)
    
    # Comparison table
    st.markdown("#### 📋 Bảng So Sánh Chi Tiết")
    st.dataframe(
        df_dosing,
        use_container_width=True,
        hide_index=True
    )
    
    # Add visual comparison notes
    st.info("""
    **💡 Lưu ý:**
    - Liều dùng được tính cho bệnh nhân 70kg, CrCl 70 mL/min, chỉ định chuẩn
    - Liều dùng có thể thay đổi theo chỉ định và chức năng thận
    - Tra cứu chi tiết từng thuốc để xem điều chỉnh theo CrCl
    - Một số thuốc cần điều chỉnh liều trong ICU
    """)


def render_cost_comparison_chart(
    comparison_data: List[Dict[str, Any]],
    drugs: List[str],
    cost_data: Optional[Dict[str, float]] = None
) -> None:
    """
    Render cost comparison chart (if cost data available)
    
    Args:
        comparison_data: List of drug data dicts
        drugs: List of drug names
        cost_data: Optional dict of {drug_name: cost_in_vnd}
    """
    if not cost_data:
        st.info("💡 Dữ liệu chi phí chưa có sẵn. Tính năng này sẽ được bổ sung khi có dữ liệu từ Bộ Y tế.")
        return
    
    if not PLOTLY_AVAILABLE:
        st.warning("⚠️ Plotly không khả dụng. Vui lòng cài đặt: `pip install plotly`")
        return
    
    st.markdown("### 💰 So Sánh Chi Phí")
    
    # Prepare cost data
    cost_chart_data = []
    for drug_name in drugs:
        if drug_name in cost_data:
            cost_chart_data.append({
                'Thuốc': drug_name,
                'Chi phí (VNĐ)': cost_data[drug_name]
            })
    
    if not cost_chart_data:
        st.info("Không có dữ liệu chi phí cho các thuốc được chọn")
        return
    
    df_cost = pd.DataFrame(cost_chart_data)
    
    # Create bar chart
    fig = go.Figure(data=[
        go.Bar(
            x=df_cost['Thuốc'],
            y=df_cost['Chi phí (VNĐ)'],
            marker_color='#4CAF50',
            text=[f"{cost:,.0f} VNĐ" for cost in df_cost['Chi phí (VNĐ)']],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title='So Sánh Chi Phí Điều Trị',
        xaxis_title='Thuốc',
        yaxis_title='Chi phí (VNĐ)',
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_side_effects_heatmap(
    comparison_data: List[Dict[str, Any]],
    drugs: List[str]
) -> None:
    """
    Render side effects comparison heatmap with real data
    
    Args:
        comparison_data: List of drug data dicts
        drugs: List of drug names
    """
    if not PLOTLY_AVAILABLE:
        st.warning("⚠️ Plotly không khả dụng. Vui lòng cài đặt: `pip install plotly`")
        return
    
    st.markdown("### ⚠️ So Sánh Tác Dụng Phụ")
    
    try:
        from .antibiotics_data import ANTIBIOTICS_DATABASE
    except ImportError:
        st.error("Không thể tải dữ liệu antibiotics")
        return
    
    # Common side effects to check (Vietnamese terms)
    common_side_effects = [
        'Độc thận',
        'Độc gan',
        'Rối loạn tiêu hóa',
        'Phản ứng da',
        'Rối loạn máu',
        'QT kéo dài',
        'Độc thần kinh',
        'Độc tai',
        'Dị ứng',
        'Viêm tĩnh mạch'
    ]
    
    # Create heatmap data with severity scoring
    heatmap_data = []
    for drug_name in drugs:
        if drug_name not in ANTIBIOTICS_DATABASE:
            continue
        
        ab_data = ANTIBIOTICS_DATABASE[drug_name]
        side_effects = ab_data.get('side_effects', [])
        side_effects_str = ' '.join(str(se) for se in side_effects).lower()
        
        row = {'Thuốc': drug_name}
        for se in common_side_effects:
            # Check if side effect is mentioned with severity scoring
            se_lower = se.lower()
            score = 0
            
            # Exact match = 2 (high severity)
            if se_lower in side_effects_str:
                score = 2
            # Partial match = 1 (medium severity)
            elif any(se_lower in str(se_item).lower() for se_item in side_effects):
                score = 1
            
            row[se] = score
        
        heatmap_data.append(row)
    
    if not heatmap_data:
        st.info("Không có dữ liệu tác dụng phụ để hiển thị")
        return
    
    df_heatmap = pd.DataFrame(heatmap_data)
    df_heatmap = df_heatmap.set_index('Thuốc')
    
    # Create heatmap with better colorscale
    fig = go.Figure(data=go.Heatmap(
        z=df_heatmap.values,
        x=df_heatmap.columns,
        y=df_heatmap.index,
        colorscale=[
            [0, '#E8F5E9'],  # Light green = no side effect
            [0.5, '#FFF9C4'],  # Yellow = possible
            [1, '#F44336']  # Red = has side effect
        ],
        zmin=0,
        zmax=2,
        showscale=True,
        colorbar=dict(
            title="Mức độ",
            tickvals=[0, 1, 2],
            ticktext=['Không', 'Có thể', 'Có']
        ),
        text=[[['', 'Có thể', 'Có'][int(val)] if val > 0 else '' for val in row] for row in df_heatmap.values],
        texttemplate='%{text}',
        textfont={"size": 10, "color": "black"},
        hovertemplate='<b>%{y}</b><br>%{x}<br>Mức độ: %{z}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Heatmap Tác Dụng Phụ - So Sánh Kháng Sinh',
        xaxis_title='Tác dụng phụ',
        yaxis_title='Kháng sinh',
        height=300 + len(drugs) * 50,
        xaxis={'tickangle': -45}
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add summary table
    st.markdown("#### 📋 Tóm Tắt Tác Dụng Phụ")
    summary_data = []
    for drug_name in drugs:
        if drug_name not in ANTIBIOTICS_DATABASE:
            continue
        
        ab_data = ANTIBIOTICS_DATABASE[drug_name]
        side_effects = ab_data.get('side_effects', [])
        
        # Count side effects
        count = len(side_effects) if side_effects else 0
        
        # Get most common ones
        common_ones = []
        for se in common_side_effects:
            if any(se.lower() in str(se_item).lower() for se_item in side_effects):
                common_ones.append(se)
        
        summary_data.append({
            'Thuốc': drug_name,
            'Số lượng': count,
            'Phổ biến': ', '.join(common_ones[:3]) if common_ones else 'Không có'
        })
    
    if summary_data:
        df_summary = pd.DataFrame(summary_data)
        st.dataframe(df_summary, use_container_width=True, hide_index=True)


def render_visual_comparison_tabs(
    comparison_data: List[Dict[str, Any]],
    drugs: List[str],
    cost_data: Optional[Dict[str, float]] = None
) -> None:
    """
    Render visual comparison with tabs
    
    Args:
        comparison_data: List of drug data dicts
        drugs: List of drug names
        cost_data: Optional cost data
    """
    st.markdown("---")
    st.markdown("### 📊 So Sánh Trực Quan")
    
    tabs = st.tabs([
        "📊 Phổ Tác Dụng",
        "💉 Liều Dùng",
        "💰 Chi Phí",
        "⚠️ Tác Dụng Phụ"
    ])
    
    with tabs[0]:
        render_spectrum_chart(comparison_data, drugs)
    
    with tabs[1]:
        render_dosing_comparison_chart(comparison_data, drugs)
    
    with tabs[2]:
        render_cost_comparison_chart(comparison_data, drugs, cost_data)
    
    with tabs[3]:
        render_side_effects_heatmap(comparison_data, drugs)


__all__ = [
    'render_spectrum_chart',
    'render_dosing_comparison_chart',
    'render_cost_comparison_chart',
    'render_side_effects_heatmap',
    'render_visual_comparison_tabs',
]
