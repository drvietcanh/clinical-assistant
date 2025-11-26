"""
Lab Trend Analysis Module
Serial lab monitoring với trend visualization và pattern recognition
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
from .normal_ranges import get_normal_range, is_critical, interpret_value, ALL_RANGES


def detect_trend(values: List[float]) -> str:
    """
    Detect trend direction from lab values
    
    Args:
        values: List of lab values over time
    
    Returns:
        Trend: "improving", "worsening", "stable", or "fluctuating"
    """
    if len(values) < 2:
        return "insufficient_data"
    
    if len(values) == 2:
        if values[1] > values[0] * 1.1:
            return "increasing"
        elif values[1] < values[0] * 0.9:
            return "decreasing"
        else:
            return "stable"
    
    # For 3+ values, use linear regression approach
    # Calculate average change
    changes = []
    for i in range(1, len(values)):
        if values[i-1] != 0:
            change_pct = ((values[i] - values[i-1]) / values[i-1]) * 100
            changes.append(change_pct)
    
    if not changes:
        return "stable"
    
    avg_change = sum(changes) / len(changes)
    
    # Check for fluctuation (high variance)
    variance = sum((c - avg_change) ** 2 for c in changes) / len(changes)
    
    if variance > 50:  # High variance = fluctuating
        return "fluctuating"
    elif avg_change > 5:
        return "increasing"
    elif avg_change < -5:
        return "decreasing"
    else:
        return "stable"


def interpret_trend(test_name: str, trend: str, values: List[float], normal_range: Optional[Dict] = None) -> str:
    """
    Clinical interpretation of trend
    
    Args:
        test_name: Name of lab test
        trend: Trend direction
        values: List of values
        normal_range: Normal range dict
    
    Returns:
        Clinical interpretation string
    """
    if not values:
        return ""
    
    current_value = values[-1]
    previous_value = values[-2] if len(values) > 1 else None
    
    # Get test info
    test_info = ALL_RANGES.get(test_name, {})
    test_label = test_info.get("label", test_name)
    
    # Check if value is in normal range
    is_normal = False
    if normal_range:
        min_val = normal_range.get("min")
        max_val = normal_range.get("max")
        if min_val is not None and max_val is not None:
            is_normal = min_val <= current_value <= max_val
        elif max_val is not None:
            is_normal = current_value <= max_val
    
    # Critical check
    is_crit = is_critical(test_name, current_value)
    
    interpretations = []
    
    # Trend interpretation
    if trend == "increasing":
        if is_crit:
            interpretations.append(f"⚠️ **Tăng nhanh và đạt mức nguy hiểm** - {test_label} đang tăng và vượt ngưỡng nguy hiểm")
        elif not is_normal:
            interpretations.append(f"⬆️ **Đang tăng** - {test_label} tiếp tục tăng, cần theo dõi sát")
        else:
            interpretations.append(f"📈 **Tăng nhẹ** - {test_label} đang tăng nhưng vẫn trong giới hạn bình thường")
    
    elif trend == "decreasing":
        if is_crit:
            interpretations.append(f"⚠️ **Giảm nhanh và đạt mức nguy hiểm** - {test_label} đang giảm và vượt ngưỡng nguy hiểm")
        elif not is_normal:
            interpretations.append(f"⬇️ **Đang giảm** - {test_label} tiếp tục giảm, cần theo dõi sát")
        else:
            interpretations.append(f"📉 **Giảm nhẹ** - {test_label} đang giảm nhưng vẫn trong giới hạn bình thường")
    
    elif trend == "stable":
        if is_crit:
            interpretations.append(f"⚠️ **Ổn định ở mức nguy hiểm** - {test_label} duy trì ở mức nguy hiểm")
        elif not is_normal:
            interpretations.append(f"➡️ **Ổn định** - {test_label} duy trì ở mức bất thường, cần điều trị")
        else:
            interpretations.append(f"✓ **Ổn định** - {test_label} duy trì trong giới hạn bình thường")
    
    elif trend == "fluctuating":
        interpretations.append(f"📊 **Dao động** - {test_label} dao động, cần đánh giá nguyên nhân")
    
    # Add change percentage if available
    if previous_value and previous_value != 0:
        change_pct = ((current_value - previous_value) / previous_value) * 100
        if abs(change_pct) > 10:
            interpretations.append(f"Thay đổi: {change_pct:+.1f}% so với lần trước")
    
    return " | ".join(interpretations) if interpretations else "Không có dữ liệu đủ để đánh giá"


def plot_lab_trend(
    test_name: str,
    dates: List[datetime],
    values: List[float],
    gender: str = "male",
    age: Optional[int] = None
) -> go.Figure:
    """
    Plot trend chart for a lab test
    
    Args:
        test_name: Name of lab test
        dates: List of dates
        values: List of values
        gender: Gender for normal range
        age: Age for normal range
    
    Returns:
        Plotly figure
    """
    test_info = ALL_RANGES.get(test_name, {})
    test_label = test_info.get("label", test_name)
    unit = test_info.get("unit", "")
    
    # Get normal range
    normal_range = get_normal_range(test_name, gender, age)
    min_val = normal_range.get("min") if normal_range else None
    max_val = normal_range.get("max") if normal_range else None
    
    # Get critical values
    critical_low = test_info.get("critical_low")
    critical_high = test_info.get("critical_high")
    
    # Create figure
    fig = go.Figure()
    
    # Plot values
    fig.add_trace(go.Scatter(
        x=dates,
        y=values,
        mode='lines+markers',
        name=test_label,
        line=dict(color='#1f77b4', width=2),
        marker=dict(size=8, color='#1f77b4'),
        hovertemplate=f'<b>{test_label}</b><br>' +
                      'Date: %{x}<br>' +
                      f'Value: %{{y:.2f}} {unit}<br>' +
                      '<extra></extra>'
    ))
    
    # Add normal range shading
    if min_val is not None and max_val is not None:
        fig.add_hrect(
            y0=min_val,
            y1=max_val,
            fillcolor="green",
            opacity=0.1,
            layer="below",
            line_width=0,
            annotation_text="Normal Range",
            annotation_position="top left"
        )
    
    # Add critical value lines
    if critical_low is not None:
        fig.add_hline(
            y=critical_low,
            line_dash="dash",
            line_color="red",
            opacity=0.7,
            annotation_text="Critical Low",
            annotation_position="right"
        )
    
    if critical_high is not None:
        fig.add_hline(
            y=critical_high,
            line_dash="dash",
            line_color="red",
            opacity=0.7,
            annotation_text="Critical High",
            annotation_position="right"
        )
    
    # Update layout
    fig.update_layout(
        title=f"Trend Analysis: {test_label}",
        xaxis_title="Date",
        yaxis_title=f"{test_label} ({unit})",
        hovermode='x unified',
        height=400,
        showlegend=False
    )
    
    return fig


def plot_multi_trends(
    trends_data: Dict[str, Tuple[List[datetime], List[float]]],
    gender: str = "male",
    age: Optional[int] = None
) -> go.Figure:
    """
    Plot multiple lab trends in subplots
    
    Args:
        trends_data: Dict of {test_name: (dates, values)}
        gender: Gender for normal ranges
        age: Age for normal ranges
    
    Returns:
        Plotly figure with subplots
    """
    num_tests = len(trends_data)
    if num_tests == 0:
        return None
    
    # Calculate grid
    cols = 2
    rows = (num_tests + 1) // 2
    
    # Create subplots
    fig = make_subplots(
        rows=rows,
        cols=cols,
        subplot_titles=[ALL_RANGES.get(name, {}).get("label", name) for name in trends_data.keys()],
        vertical_spacing=0.15,
        horizontal_spacing=0.1
    )
    
    for idx, (test_name, (dates, values)) in enumerate(trends_data.items(), 1):
        row = (idx - 1) // cols + 1
        col = (idx - 1) % cols + 1
        
        test_info = ALL_RANGES.get(test_name, {})
        test_label = test_info.get("label", test_name)
        unit = test_info.get("unit", "")
        
        # Get normal range
        normal_range = get_normal_range(test_name, gender, age)
        min_val = normal_range.get("min") if normal_range else None
        max_val = normal_range.get("max") if normal_range else None
        
        # Plot values
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=values,
                mode='lines+markers',
                name=test_label,
                line=dict(color='#1f77b4', width=2),
                marker=dict(size=6),
                showlegend=False
            ),
            row=row,
            col=col
        )
        
        # Add normal range
        if min_val is not None and max_val is not None:
            fig.add_hrect(
                y0=min_val,
                y1=max_val,
                fillcolor="green",
                opacity=0.1,
                layer="below",
                line_width=0,
                row=row,
                col=col
            )
        
        # Update y-axis label
        fig.update_yaxes(title_text=f"{unit}", row=row, col=col)
    
    # Update layout
    fig.update_layout(
        title="Multi-Lab Trend Analysis",
        height=300 * rows,
        hovermode='x unified'
    )
    
    fig.update_xaxes(title_text="Date")
    
    return fig


def render():
    """Render Lab Trend Analysis UI"""
    st.subheader("📈 Lab Trend Analysis")
    st.caption("Theo dõi xu hướng xét nghiệm theo thời gian - Serial Lab Monitoring")
    
    # Instructions
    with st.expander("ℹ️ Hướng dẫn sử dụng"):
        st.markdown("""
        **Lab Trend Analysis** cho phép bạn:
        
        1. **Nhập nhiều giá trị xét nghiệm** theo thời gian
        2. **Xem biểu đồ xu hướng** (line charts)
        3. **Nhận cảnh báo giá trị nguy hiểm**
        4. **Nhận diện pattern** (cải thiện/xấu đi/ổn định)
        5. **Giải thích lâm sàng** tự động
        
        **Cách sử dụng:**
        - Chọn loại xét nghiệm
        - Nhập giá trị và ngày thực hiện
        - Xem biểu đồ và phân tích tự động
        """)
    
    # Gender and age
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Giới tính:", ["Nam", "Nữ"], key="trend_gender")
        gender_key = "male" if gender == "Nam" else "female"
    
    with col2:
        age = st.number_input("Tuổi (nếu cần):", min_value=0, max_value=120, value=None, key="trend_age")
    
    st.markdown("---")
    
    # Test selection
    st.markdown("#### 📋 Chọn Xét Nghiệm")
    
    # Get available tests
    available_tests = sorted([name for name in ALL_RANGES.keys() if ALL_RANGES[name].get("label")])
    
    test_name = st.selectbox(
        "Xét nghiệm:",
        available_tests,
        format_func=lambda x: ALL_RANGES[x].get("label", x),
        key="trend_test_select"
    )
    
    if not test_name:
        st.info("Vui lòng chọn xét nghiệm")
        return
    
    test_info = ALL_RANGES[test_name]
    test_label = test_info.get("label", test_name)
    unit = test_info.get("unit", "")
    
    st.markdown("---")
    
    # Data entry
    st.markdown("#### 📝 Nhập Dữ Liệu")
    
    # Number of entries
    num_entries = st.number_input(
        "Số lần xét nghiệm:",
        min_value=2,
        max_value=20,
        value=3,
        key="trend_num_entries"
    )
    
    # Data entry form
    entries = []
    for i in range(num_entries):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            date = st.date_input(
                f"Ngày {i+1}:",
                value=datetime.now().date() - timedelta(days=(num_entries - i - 1)),
                key=f"trend_date_{i}"
            )
        
        with col2:
            value = st.number_input(
                f"Giá trị {i+1} ({unit}):",
                min_value=0.0,
                value=float(test_info.get("normal", {}).get("min", 0)) if test_info.get("normal") else 0.0,
                step=0.1,
                format="%.2f",
                key=f"trend_value_{i}"
            )
        
        entries.append((date, value))
    
    # Sort by date
    entries.sort(key=lambda x: x[0])
    
    # Extract dates and values
    dates = [datetime.combine(d, datetime.min.time()) for d, _ in entries]
    values = [v for _, v in entries]
    
    if len(values) < 2:
        st.warning("Cần ít nhất 2 giá trị để phân tích xu hướng")
        return
    
    st.markdown("---")
    
    # Analysis
    st.markdown("#### 📊 Phân Tích Xu Hướng")
    
    # Detect trend
    trend = detect_trend(values)
    
    # Get normal range
    normal_range = get_normal_range(test_name, gender_key, age)
    
    # Clinical interpretation
    interpretation = interpret_trend(test_name, trend, values, normal_range)
    
    # Display results
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Giá trị hiện tại", f"{values[-1]:.2f} {unit}")
    
    with col2:
        trend_emoji = {
            "increasing": "📈 Tăng",
            "decreasing": "📉 Giảm",
            "stable": "➡️ Ổn định",
            "fluctuating": "📊 Dao động",
            "insufficient_data": "❓"
        }
        st.metric("Xu hướng", trend_emoji.get(trend, trend))
    
    with col3:
        current_interpret = interpret_value(test_name, values[-1], gender_key, age)
        st.metric("Trạng thái", current_interpret)
    
    # Interpretation
    if interpretation:
        st.info(f"**Giải thích lâm sàng:** {interpretation}")
    
    # Critical alert
    if is_critical(test_name, values[-1]):
        st.error(f"⚠️ **CẢNH BÁO:** Giá trị {test_label} đang ở mức nguy hiểm!")
    
    # Normal range info
    if normal_range:
        min_val = normal_range.get("min")
        max_val = normal_range.get("max")
        if min_val is not None and max_val is not None:
            st.caption(f"Giới hạn bình thường: {min_val:.2f} - {max_val:.2f} {unit}")
    
    st.markdown("---")
    
    # Plot chart
    st.markdown("#### 📈 Biểu Đồ Xu Hướng")
    
    fig = plot_lab_trend(test_name, dates, values, gender_key, age)
    st.plotly_chart(fig, use_container_width=True)
    
    # Data table
    with st.expander("📋 Xem Dữ Liệu"):
        df = pd.DataFrame({
            "Ngày": [d.strftime("%Y-%m-%d") for d in dates],
            f"{test_label} ({unit})": values,
            "Giải thích": [interpret_value(test_name, v, gender_key, age) for v in values]
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

