"""
Score Charts Component
Provides visual charts for clinical calculators and scores
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Dict, Optional, Tuple
from components.risk_color_coding import get_risk_color


def render_risk_bar_chart(
    value: float,
    thresholds: Dict[str, float],
    max_value: float = 100,
    title: str = "Risk Level",
    show_value: bool = True
):
    """
    Render a horizontal bar chart showing risk level.
    
    Args:
        value: Current risk value
        thresholds: Dict with risk thresholds
        max_value: Maximum value for scale
        title: Chart title
        show_value: Show value on chart
    """
    # Determine risk level and color
    percentage = (value / max_value) * 100 if max_value > 0 else 0
    
    if percentage <= 20:
        risk_level = 'very_low'
    elif percentage <= 40:
        risk_level = 'low'
    elif percentage <= 60:
        risk_level = 'moderate'
    elif percentage <= 80:
        risk_level = 'high'
    else:
        risk_level = 'very_high'
    
    color_info = get_risk_color(risk_level)
    
    fig = go.Figure()
    
    # Main bar
    fig.add_trace(go.Bar(
        x=[value],
        y=[title],
        orientation='h',
        marker=dict(
            color=color_info['color'],
            line=dict(color=color_info['color'], width=2)
        ),
        text=[f"{value:.1f}%" if show_value else ""],
        textposition='inside',
        name='Risk Level'
    ))
    
    # Threshold markers
    for threshold_name, threshold_value in thresholds.items():
        if threshold_value <= max_value:
            fig.add_vline(
                x=threshold_value,
                line_dash="dash",
                line_color="gray",
                annotation_text=threshold_name,
                annotation_position="top"
            )
    
    fig.update_layout(
        title=title,
        xaxis_title="Risk Score",
        yaxis_title="",
        height=150,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_risk_stratification_chart(
    risk_data: List[Dict],
    title: str = "Risk Stratification",
    x_label: str = "Risk Level",
    y_label: str = "Percentage"
):
    """
    Render a bar chart showing risk stratification.
    
    Args:
        risk_data: List of dicts with 'level', 'value', 'label' keys
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
    """
    levels = [item['level'] for item in risk_data]
    values = [item['value'] for item in risk_data]
    labels = [item.get('label', item['level']) for item in risk_data]
    colors = [get_risk_color(item['level'])['color'] for item in risk_data]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=levels,
        y=values,
        text=labels,
        textposition='auto',
        marker=dict(
            color=colors,
            line=dict(color='white', width=1)
        ),
        name='Risk Distribution'
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_risk_pie_chart(
    risk_data: List[Dict],
    title: str = "Risk Distribution"
):
    """
    Render a pie chart showing risk distribution.
    
    Args:
        risk_data: List of dicts with 'level', 'value', 'label' keys
        title: Chart title
    """
    labels = [item.get('label', item['level']) for item in risk_data]
    values = [item['value'] for item in risk_data]
    colors = [get_risk_color(item['level'])['color'] for item in risk_data]
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.4,  # Donut chart
        marker=dict(colors=colors, line=dict(color='white', width=2)),
        textinfo='label+percent',
        textposition='outside'
    )])
    
    fig.update_layout(
        title=title,
        height=400,
        showlegend=True,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_comparison_chart(
    data: List[Dict],
    title: str = "Comparison",
    x_label: str = "Category",
    y_label: str = "Value"
):
    """
    Render a comparison bar chart.
    
    Args:
        data: List of dicts with 'label', 'value', 'color' (optional) keys
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
    """
    labels = [item['label'] for item in data]
    values = [item['value'] for item in data]
    colors = [item.get('color', '#3b82f6') for item in data]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=labels,
        y=values,
        marker=dict(color=colors),
        text=[f"{v:.1f}" for v in values],
        textposition='auto',
        name='Values'
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_trend_line_chart(
    data: List[Tuple[float, float]],
    title: str = "Trend Over Time",
    x_label: str = "Time",
    y_label: str = "Value"
):
    """
    Render a line chart showing trends.
    
    Args:
        data: List of (x, y) tuples
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
    """
    x_values = [point[0] for point in data]
    y_values = [point[1] for point in data]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=x_values,
        y=y_values,
        mode='lines+markers',
        name='Trend',
        line=dict(color='#3b82f6', width=2),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_risk_gauge_chart(
    value: float,
    min_value: float = 0,
    max_value: float = 100,
    thresholds: Optional[Dict[str, float]] = None,
    title: str = "Risk Score"
):
    """
    Render a gauge/speedometer chart for risk visualization.
    
    Args:
        value: Current value
        min_value: Minimum value
        max_value: Maximum value
        thresholds: Optional risk thresholds
        title: Chart title
    """
    # Determine risk level
    percentage = ((value - min_value) / (max_value - min_value)) * 100 if max_value > min_value else 0
    
    if percentage <= 20:
        risk_level = 'very_low'
    elif percentage <= 40:
        risk_level = 'low'
    elif percentage <= 60:
        risk_level = 'moderate'
    elif percentage <= 80:
        risk_level = 'high'
    else:
        risk_level = 'very_high'
    
    color_info = get_risk_color(risk_level)
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title},
        delta={'reference': (max_value + min_value) / 2},
        gauge={
            'axis': {'range': [min_value, max_value]},
            'bar': {'color': color_info['color']},
            'steps': [
                {'range': [min_value, max_value * 0.2], 'color': get_risk_color('very_low')['bg']},
                {'range': [max_value * 0.2, max_value * 0.4], 'color': get_risk_color('low')['bg']},
                {'range': [max_value * 0.4, max_value * 0.6], 'color': get_risk_color('moderate')['bg']},
                {'range': [max_value * 0.6, max_value * 0.8], 'color': get_risk_color('high')['bg']},
                {'range': [max_value * 0.8, max_value], 'color': get_risk_color('very_high')['bg']}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': max_value * 0.8
            }
        }
    ))
    
    fig.update_layout(height=300)
    
    st.plotly_chart(fig, use_container_width=True)


def render_score_comparison_table(
    scores: List[Dict],
    title: str = "Score Comparison"
):
    """
    Render a comparison table with color coding.
    
    Args:
        scores: List of dicts with 'name', 'value', 'risk_level' keys
        title: Table title
    """
    st.subheader(title)
    
    # Create table data
    table_data = []
    for score in scores:
        risk_level = score.get('risk_level', 'moderate')
        color_info = get_risk_color(risk_level)
        
        table_data.append({
            'Calculator': score['name'],
            'Value': f"{score['value']:.2f}",
            'Risk Level': risk_level,
            'Color': color_info['color']
        })
    
    # Display as markdown table
    st.markdown("| Calculator | Value | Risk Level |")
    st.markdown("|-----------|-------|------------|")
    
    for row in table_data:
        st.markdown(f"| {row['Calculator']} | {row['Value']} | {row['Risk Level']} |")
    
    # Also show as colored badges
    for score in scores:
        risk_level = score.get('risk_level', 'moderate')
        color_info = get_risk_color(risk_level)
        
        col1, col2, col3 = st.columns([3, 2, 2])
        with col1:
            st.write(f"**{score['name']}**")
        with col2:
            st.write(f"{score['value']:.2f}")
        with col3:
            st.markdown(
                f"<div style='background-color: {color_info['bg']}; color: {color_info['color']}; "
                f"padding: 0.25rem 0.5rem; border-radius: 0.25rem; display: inline-block;'>"
                f"{color_info['text']}</div>",
                unsafe_allow_html=True
            )

