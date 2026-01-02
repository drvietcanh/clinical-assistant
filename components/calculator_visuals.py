"""
Calculator Visuals Component
Charts, graphs, and nomograms for calculators
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Optional, Tuple
import pandas as pd


def render_score_chart(
    score: float,
    min_score: float,
    max_score: float,
    risk_levels: List[Tuple[float, float, str, str]],
    title: str = "Risk Score"
) -> None:
    """
    Render risk score chart with color-coded risk levels
    
    Args:
        score: Current score value
        min_score: Minimum possible score
        max_score: Maximum possible score
        risk_levels: List of (min, max, label, color) tuples
        title: Chart title
    """
    fig = go.Figure()
    
    # Add risk level bars
    for min_val, max_val, label, color in risk_levels:
        fig.add_trace(go.Bar(
            x=[max_val - min_val],
            y=[title],
            base=min_val,
            marker_color=color,
            name=label,
            showlegend=True,
            text=[label],
            textposition='inside',
            hovertemplate=f"{label}<br>Range: {min_val}-{max_val}<extra></extra>"
        ))
    
    # Add current score marker
    fig.add_trace(go.Scatter(
        x=[score],
        y=[title],
        mode='markers+text',
        marker=dict(
            size=20,
            color='black',
            symbol='diamond',
            line=dict(width=2, color='white')
        ),
        text=[f"Score: {score}"],
        textposition='top center',
        name='Current Score',
        showlegend=False,
        hovertemplate=f"Current Score: {score}<extra></extra>"
    ))
    
    fig.update_layout(
        xaxis=dict(
            range=[min_score, max_score],
            title="Score",
            showgrid=True,
            gridcolor='lightgray'
        ),
        yaxis=dict(showticklabels=False),
        height=200,
        margin=dict(l=20, r=20, t=40, b=20),
        title=title,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_nomogram(
    data: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: Optional[str] = None,
    title: str = "Nomogram"
) -> None:
    """
    Render nomogram chart
    
    Args:
        data: DataFrame with data
        x_col: Column name for x-axis
        y_col: Column name for y-axis
        color_col: Optional column for color coding
        title: Chart title
    """
    if color_col:
        fig = px.scatter(
            data,
            x=x_col,
            y=y_col,
            color=color_col,
            title=title,
            labels={x_col: x_col, y_col: y_col}
        )
    else:
        fig = px.scatter(
            data,
            x=x_col,
            y=y_col,
            title=title,
            labels={x_col: x_col, y_col: y_col}
        )
    
    fig.update_traces(marker_size=10)
    fig.update_layout(height=400)
    
    st.plotly_chart(fig, use_container_width=True)


def render_risk_comparison_chart(
    scores: Dict[str, float],
    title: str = "Risk Comparison"
) -> None:
    """
    Render comparison chart for multiple risk scores
    
    Args:
        scores: Dict mapping score name to value
        title: Chart title
    """
    names = list(scores.keys())
    values = list(scores.values())
    
    fig = go.Figure(data=[
        go.Bar(
            x=names,
            y=values,
            marker_color=px.colors.qualitative.Set3,
            text=values,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="Score Type",
        yaxis_title="Score Value",
        height=400,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_timeline_chart(
    events: List[Dict[str, any]],
    title: str = "Timeline"
) -> None:
    """
    Render timeline chart for clinical events
    
    Args:
        events: List of event dicts with 'time', 'label', 'color' keys
        title: Chart title
    """
    fig = go.Figure()
    
    for event in events:
        fig.add_trace(go.Scatter(
            x=[event['time']],
            y=[0],
            mode='markers+text',
            marker=dict(
                size=15,
                color=event.get('color', 'blue'),
                symbol='circle'
            ),
            text=[event['label']],
            textposition='top center',
            name=event['label'],
            hovertemplate=f"{event['label']}<br>Time: {event['time']}<extra></extra>"
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title="Time",
        yaxis=dict(showticklabels=False, range=[-0.5, 0.5]),
        height=200,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)


# Export
__all__ = [
    'render_score_chart',
    'render_nomogram',
    'render_risk_comparison_chart',
    'render_timeline_chart',
]

