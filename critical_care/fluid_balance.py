"""
Fluid Balance Tracking
Time-based fluid input/output tracking with trends and alerts
"""

import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
from components.ui.results import render_result_box, render_result_card
from components.ui.alerts import render_info_alert, render_warning_alert, render_error_alert


def init_fluid_balance_state():
    """Initialize fluid balance state in session_state"""
    if 'fluid_balance_entries' not in st.session_state:
        st.session_state['fluid_balance_entries'] = []


def add_fluid_entry(time: datetime, fluid_in: float, fluid_out: float, notes: str = ""):
    """Add a fluid balance entry"""
    init_fluid_balance_state()
    
    entry = {
        'time': time,
        'fluid_in': fluid_in,
        'fluid_out': fluid_out,
        'balance': fluid_in - fluid_out,
        'notes': notes
    }
    
    st.session_state['fluid_balance_entries'].append(entry)
    
    # Sort by time
    st.session_state['fluid_balance_entries'].sort(key=lambda x: x['time'])


def get_fluid_balance_dataframe() -> pd.DataFrame:
    """Get fluid balance entries as DataFrame"""
    init_fluid_balance_state()
    
    if not st.session_state['fluid_balance_entries']:
        return pd.DataFrame()
    
    df = pd.DataFrame(st.session_state['fluid_balance_entries'])
    
    # Calculate cumulative
    df['cumulative_in'] = df['fluid_in'].cumsum()
    df['cumulative_out'] = df['fluid_out'].cumsum()
    df['cumulative_balance'] = df['cumulative_in'] - df['cumulative_out']
    
    return df


def calculate_24h_balance(df: pd.DataFrame, current_time: datetime = None) -> dict:
    """Calculate 24-hour fluid balance"""
    if df.empty:
        return {
            'total_in': 0,
            'total_out': 0,
            'balance': 0,
            'urine_output': 0
        }
    
    if current_time is None:
        current_time = datetime.now()
    
    # Filter last 24 hours
    cutoff_time = current_time - timedelta(hours=24)
    df_24h = df[df['time'] >= cutoff_time]
    
    if df_24h.empty:
        return {
            'total_in': 0,
            'total_out': 0,
            'balance': 0,
            'urine_output': 0
        }
    
    total_in = df_24h['fluid_in'].sum()
    total_out = df_24h['fluid_out'].sum()
    balance = total_in - total_out
    
    # Estimate urine output (assuming fluid_out includes urine)
    # In real implementation, would have separate urine tracking
    urine_output = total_out * 0.7  # Assume 70% of output is urine
    
    return {
        'total_in': total_in,
        'total_out': total_out,
        'balance': balance,
        'urine_output': urine_output
    }


def check_fluid_balance_alerts(balance_24h: dict, weight_kg: float = None) -> list:
    """Check for fluid balance alerts"""
    alerts = []
    
    balance = balance_24h['balance']
    urine_output = balance_24h.get('urine_output', 0)
    
    # Positive balance alerts
    if balance > 2000:
        alerts.append({
            'priority': 'error',
            'message': f'Dư dịch nhiều ({balance:+.0f} mL/24h)',
            'recommendation': 'Cân nhắc lợi tiểu, hạn chế dịch vào'
        })
    elif balance > 1000:
        alerts.append({
            'priority': 'warning',
            'message': f'Dư dịch ({balance:+.0f} mL/24h)',
            'recommendation': 'Theo dõi sát, cân nhắc hạn chế dịch'
        })
    
    # Negative balance alerts
    if balance < -2000:
        alerts.append({
            'priority': 'error',
            'message': f'Thiếu dịch nhiều ({balance:+.0f} mL/24h)',
            'recommendation': 'Đánh giá thể tích tuần hoàn, cân nhắc bù dịch'
        })
    elif balance < -1000:
        alerts.append({
            'priority': 'warning',
            'message': f'Thiếu dịch ({balance:+.0f} mL/24h)',
            'recommendation': 'Đánh giá thể tích tuần hoàn'
        })
    
    # Urine output alerts (if weight provided)
    if weight_kg and weight_kg > 0:
        uo_ml_per_kg_per_h = (urine_output / 24) / weight_kg if urine_output > 0 else 0
        
        if uo_ml_per_kg_per_h < 0.3:
            alerts.append({
                'priority': 'error',
                'message': f'Lượng nước tiểu rất thấp ({uo_ml_per_kg_per_h:.2f} mL/kg/h)',
                'recommendation': 'Đánh giá AKI, cân nhắc RRT'
            })
        elif uo_ml_per_kg_per_h < 0.5:
            alerts.append({
                'priority': 'warning',
                'message': f'Lượng nước tiểu thấp ({uo_ml_per_kg_per_h:.2f} mL/kg/h)',
                'recommendation': 'Theo dõi sát, đánh giá thể tích tuần hoàn'
            })
    
    return alerts


def render_fluid_balance_tracker():
    """Render fluid balance tracking interface"""
    st.header("💧 Theo dõi cân bằng dịch")
    st.caption("Theo dõi dịch vào/ra theo thời gian với cảnh báo tự động")
    
    init_fluid_balance_state()
    
    st.markdown("---")
    
    # Add new entry
    st.markdown("### ➕ Thêm mục nhập")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        entry_time = st.datetime_input(
            "Thời gian:",
            value=datetime.now(),
            key="fluid_entry_time"
        )
    
    with col2:
        fluid_in = st.number_input(
            "Dịch vào (mL):",
            min_value=0.0,
            value=0.0,
            key="fluid_in"
        )
    
    with col3:
        fluid_out = st.number_input(
            "Dịch ra (mL):",
            min_value=0.0,
            value=0.0,
            key="fluid_out"
        )
    
    notes = st.text_input("Ghi chú (tùy chọn):", key="fluid_notes")
    
    if st.button("➕ Thêm mục nhập", use_container_width=True):
        add_fluid_entry(entry_time, fluid_in, fluid_out, notes)
        st.success("✅ Đã thêm mục nhập!")
        st.rerun()
    
    st.markdown("---")
    
    # Display entries
    df = get_fluid_balance_dataframe()
    
    if df.empty:
        st.info("Chưa có mục nhập. Vui lòng thêm mục nhập ở trên.")
        return
    
    # 24-hour summary
    st.markdown("### 📊 Tóm tắt 24 giờ")
    
    balance_24h = calculate_24h_balance(df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_result_card(
            title="Dịch vào",
            value=f"{balance_24h['total_in']:.0f}",
            unit="mL",
            color="info",
            subtitle="24 giờ"
        )
    
    with col2:
        render_result_card(
            title="Dịch ra",
            value=f"{balance_24h['total_out']:.0f}",
            unit="mL",
            color="info",
            subtitle="24 giờ"
        )
    
    with col3:
        balance_color = 'error' if abs(balance_24h['balance']) > 2000 else ('warning' if abs(balance_24h['balance']) > 1000 else 'success')
        render_result_card(
            title="Cân bằng",
            value=f"{balance_24h['balance']:+.0f}",
            unit="mL",
            color=balance_color,
            subtitle="24 giờ"
        )
    
    with col4:
        weight = st.number_input("Cân nặng (kg):", min_value=0.0, value=70.0, key="fluid_weight")
        if weight > 0:
            uo_per_kg = (balance_24h['urine_output'] / 24) / weight if balance_24h['urine_output'] > 0 else 0
            uo_color = 'error' if uo_per_kg < 0.3 else ('warning' if uo_per_kg < 0.5 else 'success')
            render_result_card(
                title="Lượng nước tiểu",
                value=f"{uo_per_kg:.2f}",
                unit="mL/kg/h",
                color=uo_color,
                subtitle="Target: >0.5 mL/kg/h"
            )
    
    # Alerts
    alerts = check_fluid_balance_alerts(balance_24h, weight)
    
    if alerts:
        st.markdown("### 🚨 Cảnh báo")
        for alert in alerts:
            if alert['priority'] == 'error':
                render_error_alert(alert['message'], alert['recommendation'])
            elif alert['priority'] == 'warning':
                render_warning_alert(alert['message'], alert['recommendation'])
    
    st.markdown("---")
    
    # Cumulative balance chart
    st.markdown("### 📈 Biểu đồ xu hướng")
    
    if len(df) > 1:
        # Prepare data for chart
        chart_df = df[['time', 'cumulative_balance']].copy()
        chart_df = chart_df.set_index('time')
        
        st.line_chart(chart_df)
    else:
        st.info("Cần ít nhất 2 mục nhập để hiển thị biểu đồ.")
    
    st.markdown("---")
    
    # Recent entries table
    st.markdown("### 📋 Mục nhập gần đây")
    
    # Display in reverse chronological order
    display_df = df[['time', 'fluid_in', 'fluid_out', 'balance', 'notes']].copy()
    display_df = display_df.sort_values('time', ascending=False)
    display_df['time'] = display_df['time'].dt.strftime('%Y-%m-%d %H:%M')
    display_df.columns = ['Thời gian', 'Dịch vào (mL)', 'Dịch ra (mL)', 'Cân bằng (mL)', 'Ghi chú']
    
    st.dataframe(display_df, use_container_width=True, height=300)
    
    # Delete entry
    if len(df) > 0:
        st.markdown("### 🗑️ Xóa mục nhập")
        
        entry_to_delete = st.selectbox(
            "Chọn mục nhập để xóa:",
            options=range(len(df)),
            format_func=lambda x: f"{df.iloc[x]['time'].strftime('%Y-%m-%d %H:%M')} - Cân bằng: {df.iloc[x]['balance']:+.0f} mL",
            key="delete_entry"
        )
        
        if st.button("🗑️ Xóa mục nhập đã chọn", use_container_width=True):
            st.session_state['fluid_balance_entries'].pop(entry_to_delete)
            st.success("✅ Đã xóa mục nhập!")
            st.rerun()
        
        if st.button("🗑️ Xóa tất cả", use_container_width=True, type="secondary"):
            st.session_state['fluid_balance_entries'] = []
            st.success("✅ Đã xóa tất cả mục nhập!")
            st.rerun()


def render_fluid_balance_integration():
    """Render fluid balance integration with fluid calculator"""
    st.markdown("### 🔗 Tích hợp với Fluid Calculator")
    
    st.info("""
    **Tính năng tích hợp:**
    - Tự động tính deficit dựa trên cân bằng dịch
    - Recommendations dựa trên xu hướng
    - Cảnh báo khi mất cân bằng
    """)
    
    if st.button("💧 Mở Fluid Calculator", use_container_width=True):
        st.session_state['critical_care_tool_selection'] = "💧 Fluid Therapy"
        st.rerun()


def render_fluid_balance():
    """Main function to render fluid balance tracking"""
    tabs = st.tabs([
        "📊 Theo dõi",
        "🔗 Tích hợp"
    ])
    
    with tabs[0]:
        render_fluid_balance_tracker()
    
    with tabs[1]:
        render_fluid_balance_integration()
