"""
Ventilator Trends Visualization - PHIÊN 5
Biểu đồ xu hướng các thông số máy thở theo thời gian
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Dict, Any, Optional
from datetime import datetime
from .history import get_history


def get_trend_data(parameter: str) -> tuple[List[datetime], List[float]]:
    """
    Lấy dữ liệu xu hướng cho một thông số
    
    Args:
        parameter: Tên thông số ('pf_ratio', 'plateau', 'driving_pressure', 'compliance', etc.)
    
    Returns:
        Tuple (timestamps, values)
    """
    history = get_history()
    
    if not history:
        return [], []
    
    timestamps = []
    values = []
    
    for entry in history:
        timestamp = entry['timestamp']
        value = None
        
        # Lấy giá trị từ calculations
        if parameter in entry['calculations']:
            value = entry['calculations'].get(parameter)
        # Hoặc từ vent_settings
        elif parameter in entry['vent_settings']:
            value = entry['vent_settings'].get(parameter)
        # Hoặc từ abg_data
        elif parameter in entry['abg_data']:
            value = entry['abg_data'].get(parameter)
        
        if value is not None and isinstance(value, (int, float)):
            timestamps.append(timestamp)
            values.append(value)
    
    return timestamps, values


def plot_trend(
    parameter: str,
    title: str,
    y_label: str,
    target_range: Optional[tuple[float, float]] = None,
    warning_range: Optional[tuple[float, float]] = None,
    color: str = "blue"
) -> go.Figure:
    """
    Vẽ biểu đồ xu hướng cho một thông số
    
    Args:
        parameter: Tên thông số
        title: Tiêu đề biểu đồ
        y_label: Nhãn trục Y
        target_range: Khoảng giá trị mục tiêu (min, max)
        warning_range: Khoảng giá trị cảnh báo (min, max)
        color: Màu đường biểu đồ
    """
    timestamps, values = get_trend_data(parameter)
    
    if not timestamps:
        return None
    
    fig = go.Figure()
    
    # Vẽ đường xu hướng
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=values,
        mode='lines+markers',
        name=title,
        line=dict(color=color, width=2),
        marker=dict(size=8, color=color),
        hovertemplate=f'<b>{title}</b><br>' +
                      'Thời gian: %{x}<br>' +
                      f'{y_label}: %{{y:.1f}}<extra></extra>'
    ))
    
    # Vẽ vùng mục tiêu
    if target_range:
        fig.add_hrect(
            y0=target_range[0],
            y1=target_range[1],
            fillcolor="green",
            opacity=0.1,
            layer="below",
            line_width=0,
            annotation_text="Mục tiêu",
            annotation_position="top left"
        )
    
    # Vẽ vùng cảnh báo
    if warning_range:
        fig.add_hrect(
            y0=warning_range[0],
            y1=warning_range[1],
            fillcolor="yellow",
            opacity=0.1,
            layer="below",
            line_width=0,
            annotation_text="Cảnh báo",
            annotation_position="top right"
        )
    
    fig.update_layout(
        title=title,
        xaxis_title="Thời gian",
        yaxis_title=y_label,
        hovermode='x unified',
        template='plotly_white',
        height=400,
        showlegend=False
    )
    
    return fig


def plot_pf_ratio_trend() -> Optional[go.Figure]:
    """Biểu đồ xu hướng P/F Ratio"""
    return plot_trend(
        parameter='pf_ratio',
        title='📊 Xu Hướng P/F Ratio',
        y_label='P/F Ratio',
        target_range=(200, 400),
        warning_range=(100, 200),
        color='#1f77b4'
    )


def plot_plateau_trend() -> Optional[go.Figure]:
    """Biểu đồ xu hướng Plateau Pressure"""
    return plot_trend(
        parameter='plateau',
        title='📊 Xu Hướng Plateau Pressure',
        y_label='Plateau Pressure (cmH2O)',
        target_range=(0, 30),
        warning_range=(30, 35),
        color='#ff7f0e'
    )


def plot_driving_pressure_trend() -> Optional[go.Figure]:
    """Biểu đồ xu hướng Driving Pressure"""
    return plot_trend(
        parameter='driving_pressure',
        title='📊 Xu Hướng Driving Pressure',
        y_label='Driving Pressure (cmH2O)',
        target_range=(0, 15),
        warning_range=(15, 18),
        color='#2ca02c'
    )


def plot_compliance_trend() -> Optional[go.Figure]:
    """Biểu đồ xu hướng Compliance"""
    return plot_trend(
        parameter='compliance',
        title='📊 Xu Hướng Compliance',
        y_label='Compliance (mL/cmH2O)',
        target_range=(30, 50),
        warning_range=(20, 30),
        color='#d62728'
    )


def plot_multi_trends() -> Optional[go.Figure]:
    """Biểu đồ tổng hợp nhiều thông số"""
    history = get_history()
    
    if not history:
        return None
    
    # Tạo subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('P/F Ratio', 'Plateau Pressure', 'Driving Pressure', 'Compliance'),
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    # P/F Ratio
    timestamps, values = get_trend_data('pf_ratio')
    if timestamps:
        fig.add_trace(
            go.Scatter(x=timestamps, y=values, mode='lines+markers', name='P/F Ratio',
                      line=dict(color='#1f77b4'), marker=dict(size=6)),
            row=1, col=1
        )
        fig.add_hrect(y0=200, y1=400, fillcolor="green", opacity=0.1, layer="below", line_width=0, row=1, col=1)
    
    # Plateau Pressure
    timestamps, values = get_trend_data('plateau')
    if timestamps:
        fig.add_trace(
            go.Scatter(x=timestamps, y=values, mode='lines+markers', name='Plateau',
                      line=dict(color='#ff7f0e'), marker=dict(size=6)),
            row=1, col=2
        )
        fig.add_hline(y=30, line_dash="dash", line_color="red", opacity=0.5, row=1, col=2)
    
    # Driving Pressure
    timestamps, values = get_trend_data('driving_pressure')
    if timestamps:
        fig.add_trace(
            go.Scatter(x=timestamps, y=values, mode='lines+markers', name='Driving P',
                      line=dict(color='#2ca02c'), marker=dict(size=6)),
            row=2, col=1
        )
        fig.add_hline(y=15, line_dash="dash", line_color="orange", opacity=0.5, row=2, col=1)
    
    # Compliance
    timestamps, values = get_trend_data('compliance')
    if timestamps:
        fig.add_trace(
            go.Scatter(x=timestamps, y=values, mode='lines+markers', name='Compliance',
                      line=dict(color='#d62728'), marker=dict(size=6)),
            row=2, col=2
        )
        fig.add_hrect(y0=30, y1=50, fillcolor="green", opacity=0.1, layer="below", line_width=0, row=2, col=2)
    
    fig.update_layout(
        title_text='📊 Xu Hướng Tổng Hợp',
        height=700,
        showlegend=False,
        template='plotly_white'
    )
    
    fig.update_xaxes(title_text="Thời gian", row=2, col=1)
    fig.update_xaxes(title_text="Thời gian", row=2, col=2)
    fig.update_yaxes(title_text="P/F Ratio", row=1, col=1)
    fig.update_yaxes(title_text="Plateau (cmH2O)", row=1, col=2)
    fig.update_yaxes(title_text="Driving P (cmH2O)", row=2, col=1)
    fig.update_yaxes(title_text="Compliance (mL/cmH2O)", row=2, col=2)
    
    return fig


def render_trends_panel():
    """Hiển thị panel biểu đồ xu hướng"""
    history = get_history()
    
    if not history:
        st.info("📝 Chưa có dữ liệu. Tính toán và lưu để xem biểu đồ xu hướng.")
        return
    
    st.markdown("### 📈 Biểu Đồ Xu Hướng")
    
    # Tùy chọn hiển thị
    view_mode = st.radio(
        "Chế độ hiển thị:",
        ["Tổng hợp", "P/F Ratio", "Plateau Pressure", "Driving Pressure", "Compliance"],
        horizontal=True,
        key="trend_view_mode"
    )
    
    st.markdown("---")
    
    # Hiển thị biểu đồ theo lựa chọn
    if view_mode == "Tổng hợp":
        fig = plot_multi_trends()
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Không có đủ dữ liệu để vẽ biểu đồ tổng hợp")
    
    elif view_mode == "P/F Ratio":
        fig = plot_pf_ratio_trend()
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Chưa có dữ liệu P/F Ratio")
    
    elif view_mode == "Plateau Pressure":
        fig = plot_plateau_trend()
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Chưa có dữ liệu Plateau Pressure")
    
    elif view_mode == "Driving Pressure":
        fig = plot_driving_pressure_trend()
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Chưa có dữ liệu Driving Pressure")
    
    elif view_mode == "Compliance":
        fig = plot_compliance_trend()
        if fig:
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Chưa có dữ liệu Compliance")
    
    # Thống kê nhanh
    st.markdown("---")
    st.markdown("#### 📊 Thống Kê Nhanh")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # P/F Ratio stats
    _, pf_values = get_trend_data('pf_ratio')
    if pf_values:
        with col1:
            st.metric("P/F Ratio", f"{sum(pf_values)/len(pf_values):.0f}", 
                     delta=f"{pf_values[-1] - pf_values[0]:+.0f}" if len(pf_values) > 1 else None)
    
    # Plateau stats
    _, plateau_values = get_trend_data('plateau')
    if plateau_values:
        with col2:
            st.metric("Plateau", f"{sum(plateau_values)/len(plateau_values):.1f} cmH2O",
                     delta=f"{plateau_values[-1] - plateau_values[0]:+.1f}" if len(plateau_values) > 1 else None)
    
    # Driving Pressure stats
    _, dp_values = get_trend_data('driving_pressure')
    if dp_values:
        with col3:
            st.metric("Driving P", f"{sum(dp_values)/len(dp_values):.1f} cmH2O",
                     delta=f"{dp_values[-1] - dp_values[0]:+.1f}" if len(dp_values) > 1 else None)
    
    # Compliance stats
    _, comp_values = get_trend_data('compliance')
    if comp_values:
        with col4:
            st.metric("Compliance", f"{sum(comp_values)/len(comp_values):.1f} mL/cmH2O",
                     delta=f"{comp_values[-1] - comp_values[0]:+.1f}" if len(comp_values) > 1 else None)

