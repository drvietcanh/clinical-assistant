"""
Calculator Enhancement Components
Add educational content, visual aids, and better explanations to calculators
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Optional, Dict, List
import html


def render_calculator_explanation(
    title: str,
    content: str,
    when_to_use: Optional[str] = None,
    limitations: Optional[str] = None,
    clinical_context: Optional[str] = None
):
    """
    Render educational explanation for a calculator.
    
    Args:
        title: Explanation title
        content: Main explanation content
        when_to_use: When to use this calculator
        limitations: Limitations of the calculator
        clinical_context: Clinical context information
    """
    with st.expander(f"📖 {title}", expanded=False):
        st.markdown(content)
        
        if when_to_use:
            st.markdown("---")
            st.markdown("#### 🎯 Khi nào sử dụng")
            st.info(when_to_use)
        
        if clinical_context:
            st.markdown("---")
            st.markdown("#### 🏥 Bối cảnh lâm sàng")
            st.markdown(clinical_context)
        
        if limitations:
            st.markdown("---")
            st.markdown("#### ⚠️ Hạn chế")
            st.warning(limitations)


def render_evidence_citation(
    citation_text: str,
    doi: Optional[str] = None,
    url: Optional[str] = None
):
    """
    Render evidence citation for calculator formula.
    
    Args:
        citation_text: Citation text
        doi: DOI number
        url: URL to paper
    """
    citation_html = f"""
    <div style="
        padding: 8px 12px;
        background: #f8f9fa;
        border-radius: 4px;
        border-left: 3px solid #667eea;
        margin: 8px 0;
        font-size: 0.85rem;
    ">
        <strong>📚 Evidence:</strong> {html.escape(citation_text)}
        {f' <a href="https://doi.org/{doi}" target="_blank" style="color: #1976d2;">DOI</a>' if doi else ''}
        {f' <a href="{html.escape(url)}" target="_blank" style="color: #1976d2;">Link</a>' if url else ''}
    </div>
    """
    
    st.markdown(citation_html, unsafe_allow_html=True)


def render_result_interpretation(
    result: str,
    interpretation: str,
    recommendations: Optional[List[str]] = None,
    risk_level: Optional[str] = None
):
    """
    Render result interpretation with recommendations.
    
    Args:
        result: Calculated result
        interpretation: Interpretation text
        recommendations: List of recommendations
        risk_level: Risk level (low, moderate, high)
    """
    # Risk level colors
    risk_colors = {
        "low": "#4caf50",
        "moderate": "#ff9800",
        "high": "#f44336"
    }
    
    risk_color = risk_colors.get(risk_level, "#666") if risk_level else None
    
    st.markdown("---")
    st.markdown("### 📊 Kết quả & Diễn giải")
    
    # Result display
    col1, col2 = st.columns([1, 2])
    
    with col1:
        if risk_color:
            st.markdown(f"""
            <div style="
                background: {risk_color};
                color: white;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                font-size: 1.5rem;
                font-weight: bold;
            ">
                {html.escape(result)}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.metric("Kết quả", result)
    
    with col2:
        st.markdown(f"**Diễn giải:** {interpretation}")
    
    # Recommendations
    if recommendations:
        st.markdown("---")
        st.markdown("#### 💡 Khuyến nghị")
        for rec in recommendations:
            st.markdown(f"- {rec}")


def render_visual_aid_chart(
    chart_type: str,
    data: Dict,
    title: Optional[str] = None
):
    """
    Render visual aid chart (graph, nomogram, etc.).
    
    Args:
        chart_type: Type of chart ("bar", "line", "scatter", "nomogram")
        data: Chart data
        title: Chart title
    """
    if chart_type == "bar":
        fig = go.Figure(data=[
            go.Bar(
                x=data.get("x", []),
                y=data.get("y", []),
                marker_color=data.get("color", "#667eea")
            )
        ])
    elif chart_type == "line":
        fig = go.Figure(data=[
            go.Scatter(
                x=data.get("x", []),
                y=data.get("y", []),
                mode="lines+markers",
                line=dict(color=data.get("color", "#667eea"))
            )
        ])
    elif chart_type == "scatter":
        fig = go.Figure(data=[
            go.Scatter(
                x=data.get("x", []),
                y=data.get("y", []),
                mode="markers",
                marker=dict(color=data.get("color", "#667eea"))
            )
        ])
    else:
        return
    
    if title:
        fig.update_layout(title=title)
    
    fig.update_layout(
        height=400,
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)


def render_comparison_tool(
    calculator_name: str,
    results: List[Dict],
    comparison_metric: str = "score"
):
    """
    Render comparison tool for multiple calculations.
    
    Args:
        calculator_name: Name of calculator
        results: List of result dicts with 'patient', 'result', 'date'
        comparison_metric: Metric being compared
    """
    st.markdown("### 📊 So sánh kết quả")
    
    if not results:
        st.info("Chưa có kết quả để so sánh. Tính toán nhiều lần để so sánh.")
        return
    
    # Create comparison table
    import pandas as pd
    
    comparison_data = {
        "Bệnh nhân": [r.get("patient", f"#{i+1}") for i, r in enumerate(results)],
        "Kết quả": [r.get("result", "") for r in results],
        "Ngày": [r.get("date", "") for r in results]
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Visual comparison
    if len(results) > 1:
        fig = go.Figure(data=[
            go.Bar(
                x=[r.get("patient", f"#{i+1}") for i, r in enumerate(results)],
                y=[float(str(r.get("result", 0)).replace(",", "")) if str(r.get("result", 0)).replace(".", "").replace(",", "").isdigit() else 0 for r in results],
                marker_color="#667eea"
            )
        ])
        
        fig.update_layout(
            title=f"So sánh {comparison_metric}",
            xaxis_title="Bệnh nhân",
            yaxis_title=comparison_metric,
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

