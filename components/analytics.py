"""
Usage Analytics Dashboard Component
Track and display usage statistics, charts, and insights
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import json
import csv
from io import StringIO


# Calculator to specialty mapping
CALCULATOR_SPECIALTY_MAP = {
    # Cardiology
    "chads2_vasc": "Cardiology",
    "has_bled": "Cardiology",
    "grace": "Cardiology",
    "timi": "Cardiology",
    "wells": "Cardiology",
    "perc": "Cardiology",
    "nyha": "Cardiology",
    
    # Emergency/Critical Care
    "sofa": "Emergency",
    "apache": "Emergency",
    "news2": "Emergency",
    "qsofa": "Emergency",
    "sirs": "Emergency",
    
    # Nephrology
    "egfr": "Nephrology",
    "fena": "Nephrology",
    "mdrd": "Nephrology",
    "ckd_epi": "Nephrology",
    
    # Neurology
    "mrs": "Neurology",
    "nihss": "Neurology",
    "glasgow": "Neurology",
    
    # Hematology
    "four_ts": "Hematology",
    "dic_score": "Hematology",
    
    # Metabolism
    "bmi": "Metabolism",
    "bsa": "Metabolism",
    
    # Default
    "default": "Other"
}


def get_calculator_specialty(calc_id: str) -> str:
    """Get specialty for a calculator"""
    return CALCULATOR_SPECIALTY_MAP.get(calc_id, CALCULATOR_SPECIALTY_MAP["default"])


def track_calculation(
    calculator_id: str,
    calculator_name: Optional[str] = None,
    inputs: Optional[Dict[str, Any]] = None,
    results: Optional[Dict[str, Any]] = None
) -> None:
    """
    Track a calculation event
    
    Args:
        calculator_id: ID of the calculator
        calculator_name: Name of the calculator
        inputs: Optional input values
        results: Optional result values
    """
    if 'analytics_data' not in st.session_state:
        st.session_state.analytics_data = {
            'calculations': [],
            'calculator_counts': {},
            'specialty_counts': {},
            'daily_counts': {}
        }
    
    analytics = st.session_state.analytics_data
    
    # Create calculation record
    calculation_record = {
        'id': len(analytics['calculations']),
        'calculator_id': calculator_id,
        'calculator_name': calculator_name or calculator_id,
        'specialty': get_calculator_specialty(calculator_id),
        'timestamp': datetime.now().isoformat(),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'hour': datetime.now().hour,
        'day_of_week': datetime.now().strftime('%A')
    }
    
    # Add to calculations list
    analytics['calculations'].append(calculation_record)
    
    # Update calculator counts
    if calculator_id not in analytics['calculator_counts']:
        analytics['calculator_counts'][calculator_id] = {
            'count': 0,
            'name': calculator_name or calculator_id
        }
    analytics['calculator_counts'][calculator_id]['count'] += 1
    
    # Update specialty counts
    specialty = calculation_record['specialty']
    if specialty not in analytics['specialty_counts']:
        analytics['specialty_counts'][specialty] = 0
    analytics['specialty_counts'][specialty] += 1
    
    # Update daily counts
    date = calculation_record['date']
    if date not in analytics['daily_counts']:
        analytics['daily_counts'][date] = 0
    analytics['daily_counts'][date] += 1
    
    # Limit calculations history to last 1000
    if len(analytics['calculations']) > 1000:
        analytics['calculations'] = analytics['calculations'][-1000:]


def get_total_calculations() -> int:
    """Get total number of calculations"""
    if 'analytics_data' not in st.session_state:
        return 0
    return len(st.session_state.analytics_data.get('calculations', []))


def get_most_used_calculators(limit: int = 10) -> List[Dict[str, Any]]:
    """Get most used calculators"""
    if 'analytics_data' not in st.session_state:
        return []
    
    calculator_counts = st.session_state.analytics_data.get('calculator_counts', {})
    
    # Sort by count
    sorted_calcs = sorted(
        calculator_counts.items(),
        key=lambda x: x[1]['count'],
        reverse=True
    )
    
    return [
        {
            'id': calc_id,
            'name': data['name'],
            'count': data['count']
        }
        for calc_id, data in sorted_calcs[:limit]
    ]


def get_specialty_breakdown() -> Dict[str, int]:
    """Get specialty breakdown"""
    if 'analytics_data' not in st.session_state:
        return {}
    
    return st.session_state.analytics_data.get('specialty_counts', {})


def get_daily_usage(days: int = 30) -> Dict[str, int]:
    """Get daily usage for last N days"""
    if 'analytics_data' not in st.session_state:
        return {}
    
    daily_counts = st.session_state.analytics_data.get('daily_counts', {})
    
    # Get last N days
    end_date = datetime.now()
    result = {}
    
    for i in range(days):
        date = (end_date - timedelta(days=i)).strftime('%Y-%m-%d')
        result[date] = daily_counts.get(date, 0)
    
    return result


def get_peak_usage_hours() -> Dict[int, int]:
    """Get usage by hour of day"""
    if 'analytics_data' not in st.session_state:
        return {}
    
    calculations = st.session_state.analytics_data.get('calculations', [])
    hour_counts = {}
    
    for calc in calculations:
        hour = calc.get('hour', 0)
        hour_counts[hour] = hour_counts.get(hour, 0) + 1
    
    return hour_counts


def export_analytics_to_csv() -> str:
    """Export analytics data to CSV string"""
    if 'analytics_data' not in st.session_state:
        return ""
    
    calculations = st.session_state.analytics_data.get('calculations', [])
    
    if not calculations:
        return ""
    
    # Create CSV
    output = StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow([
        'ID', 'Calculator ID', 'Calculator Name', 'Specialty',
        'Date', 'Hour', 'Day of Week', 'Timestamp'
    ])
    
    # Data
    for calc in calculations:
        writer.writerow([
            calc.get('id', ''),
            calc.get('calculator_id', ''),
            calc.get('calculator_name', ''),
            calc.get('specialty', ''),
            calc.get('date', ''),
            calc.get('hour', ''),
            calc.get('day_of_week', ''),
            calc.get('timestamp', '')
        ])
    
    return output.getvalue()


def render_analytics_dashboard() -> None:
    """Render complete analytics dashboard"""
    
    st.markdown("""
    <div style='
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px 25px;
        border-radius: 20px;
        margin-bottom: 30px;
        text-align: center;
        box-shadow: 0 8px 24px rgba(102,126,234,0.25);
    '>
        <h1 style='margin: 0; color: white; font-size: 2.5em; font-weight: 700;'>📊 Usage Analytics Dashboard</h1>
        <p style='margin: 12px 0 0 0; color: rgba(255,255,255,0.95); font-size: 1.15em;'>
            Insights và thống kê sử dụng ứng dụng
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize analytics if needed
    if 'analytics_data' not in st.session_state:
        st.session_state.analytics_data = {
            'calculations': [],
            'calculator_counts': {},
            'specialty_counts': {},
            'daily_counts': {}
        }
    
    # Stats Section
    st.markdown("### 📊 Your Stats")
    
    total_calcs = get_total_calculations()
    most_used = get_most_used_calculators(limit=1)
    specialty_breakdown = get_specialty_breakdown()
    
    # Calculate specialty focus
    if specialty_breakdown:
        total_specialty = sum(specialty_breakdown.values())
        top_specialty = max(specialty_breakdown.items(), key=lambda x: x[1])
        specialty_focus = f"{top_specialty[0]} ({top_specialty[1]/total_specialty*100:.0f}%)" if total_specialty > 0 else "N/A"
    else:
        specialty_focus = "N/A"
    
    # This week calculations
    daily_usage = get_daily_usage(days=7)
    this_week = sum(daily_usage.values())
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Calculations",
            total_calcs,
            delta=None
        )
    
    with col2:
        most_used_name = most_used[0]['name'] if most_used else "N/A"
        most_used_count = most_used[0]['count'] if most_used else 0
        st.metric(
            "Most Used",
            most_used_name,
            delta=f"{most_used_count}x" if most_used_count > 0 else None
        )
    
    with col3:
        st.metric(
            "Specialty Focus",
            specialty_focus.split(" (")[0] if "(" in specialty_focus else specialty_focus,
            delta=specialty_focus.split("(")[1].replace(")", "") if "(" in specialty_focus else None
        )
    
    with col4:
        st.metric(
            "This Week",
            this_week,
            delta="calculations"
        )
    
    st.markdown("---")
    
    # Charts Section
    st.markdown("### 📈 Charts")
    
    # Most Used Calculators
    if most_used:
        st.markdown("#### 🏆 Most Used Calculators")
        most_used_data = get_most_used_calculators(limit=10)
        
        # Create simple bar chart using HTML
        max_count = max([calc['count'] for calc in most_used_data]) if most_used_data else 1
        
        chart_html = "<div style='margin: 1rem 0;'>"
        for calc in most_used_data:
            width_pct = (calc['count'] / max_count * 100) if max_count > 0 else 0
            chart_html += f"""
            <div style="margin: 0.5rem 0;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="flex: 1; min-width: 150px; font-size: 0.9rem;">{calc['name']}</div>
                    <div style="flex: 2; background: #e3f2fd; border-radius: 4px; height: 24px; position: relative;">
                        <div style="background: #1976d2; height: 100%; width: {width_pct}%; border-radius: 4px; display: flex; align-items: center; justify-content: flex-end; padding-right: 8px; color: white; font-size: 0.75rem; font-weight: bold;">
                            {calc['count']}
                        </div>
                    </div>
                </div>
            </div>
            """
        chart_html += "</div>"
        st.markdown(chart_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Specialty Breakdown
    if specialty_breakdown:
        st.markdown("#### 🏥 Specialty Breakdown")
        
        specialty_data = sorted(specialty_breakdown.items(), key=lambda x: x[1], reverse=True)
        total_specialty = sum(specialty_breakdown.values())
        
        specialty_html = "<div style='margin: 1rem 0;'>"
        for specialty, count in specialty_data:
            pct = (count / total_specialty * 100) if total_specialty > 0 else 0
            specialty_html += f"""
            <div style="margin: 0.5rem 0;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="flex: 1; min-width: 120px; font-size: 0.9rem;">{specialty}</div>
                    <div style="flex: 2; background: #f3e5f5; border-radius: 4px; height: 24px; position: relative;">
                        <div style="background: #7b1fa2; height: 100%; width: {pct}%; border-radius: 4px; display: flex; align-items: center; justify-content: flex-end; padding-right: 8px; color: white; font-size: 0.75rem; font-weight: bold;">
                            {count} ({pct:.1f}%)
                        </div>
                    </div>
                </div>
            </div>
            """
        specialty_html += "</div>"
        st.markdown(specialty_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Daily Usage (Last 7 days)
    st.markdown("#### 📅 Daily Usage (Last 7 Days)")
    daily_usage = get_daily_usage(days=7)
    
    if daily_usage:
        # Create simple line chart representation
        dates = sorted(daily_usage.keys())
        values = [daily_usage[date] for date in dates]
        max_value = max(values) if values and max(values) > 0 else 1
        
        # Ensure we have at least 7 days of data
        if len(dates) < 7:
            # Fill missing days with 0
            end_date = datetime.now()
            all_dates = []
            for i in range(7):
                date = (end_date - timedelta(days=i)).strftime('%Y-%m-%d')
                all_dates.insert(0, date)
            dates = all_dates
            values = [daily_usage.get(date, 0) for date in dates]
            max_value = max(values) if values and max(values) > 0 else 1
        
        chart_html = "<div style='margin: 1rem 0; height: 200px; display: flex; align-items: flex-end; gap: 8px; border-bottom: 2px solid #dee2e6; padding-bottom: 1rem;'>"
        for date, value in zip(dates, values):
            # Calculate height percentage (minimum 4px for visibility, max 100%)
            if max_value > 0:
                height_pct = min((value / max_value * 100), 100)
            else:
                height_pct = 0
            
            # Ensure minimum height for visibility
            if height_pct < 4 and value > 0:
                height_pct = 4
            
            # Format date for display (day of month)
            day_display = date.split('-')[2] if '-' in date else date[-2:]
            
            chart_html += f"""
            <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 4px;">
                <div style="background: #4caf50; width: 100%; height: {height_pct}%; min-height: {4 if value > 0 else 0}px; border-radius: 4px 4px 0 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 4px; color: white; font-size: 0.7rem; font-weight: bold;">
                    {value if value > 0 else ''}
                </div>
                <div style="font-size: 0.7rem; color: #666; transform: rotate(-45deg); transform-origin: top left; white-space: nowrap;">
                    {day_display}
                </div>
            </div>
            """
        chart_html += "</div>"
        st.markdown(chart_html, unsafe_allow_html=True)
    else:
        st.info("📊 Chưa có dữ liệu sử dụng. Hãy sử dụng các công cụ để xem thống kê!")
    
    st.markdown("---")
    
    # Peak Usage Hours
    st.markdown("#### ⏰ Peak Usage Hours")
    hour_counts = get_peak_usage_hours()
    
    if hour_counts:
        # Create hourly chart
        hours = list(range(24))
        hour_values = [hour_counts.get(h, 0) for h in hours]
        max_hour_value = max(hour_values) if hour_values and max(hour_values) > 0 else 1
        
        chart_html = "<div style='margin: 1rem 0; height: 150px; display: flex; align-items: flex-end; gap: 2px; border-bottom: 2px solid #dee2e6; padding-bottom: 1rem;'>"
        for hour, value in zip(hours, hour_values):
            # Calculate height percentage
            if max_hour_value > 0:
                height_pct = min((value / max_hour_value * 100), 100)
            else:
                height_pct = 0
            
            # Ensure minimum height for visibility
            if height_pct < 2 and value > 0:
                height_pct = 2
            
            chart_html += f"""
            <div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 2px;">
                <div style="background: #ff9800; width: 100%; height: {height_pct}%; min-height: {2 if value > 0 else 0}px; border-radius: 2px 2px 0 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 2px; color: white; font-size: 0.6rem; font-weight: bold;">
                    {value if value > 0 else ''}
                </div>
                <div style="font-size: 0.6rem; color: #666; writing-mode: vertical-rl; text-orientation: mixed;">
                    {hour}h
                </div>
            </div>
            """
        chart_html += "</div>"
        st.markdown(chart_html, unsafe_allow_html=True)
    else:
        st.info("📊 Chưa có dữ liệu sử dụng theo giờ. Hãy sử dụng các công cụ để xem thống kê!")
    
    st.markdown("---")
    
    # Export Section
    st.markdown("### 📥 Export Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv_data = export_analytics_to_csv()
        if csv_data:
            st.download_button(
                label="📥 Xuất CSV",
                data=csv_data,
                file_name=f"analytics_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.info("No data to export")
    
    with col2:
        if st.button("🗑️ Xóa Thống Kê", use_container_width=True):
            if 'analytics_data' in st.session_state:
                st.session_state.analytics_data = {
                    'calculations': [],
                    'calculator_counts': {},
                    'specialty_counts': {},
                    'daily_counts': {}
                }
                st.success("Analytics cleared!")
                st.rerun()
    
    # Info
    with st.expander("ℹ️ About Analytics"):
        st.info("""
        **Analytics Tracking:**
        - Tất cả dữ liệu được lưu locally trong session (không gửi lên server)
        - Không lưu PHI (Protected Health Information)
        - Chỉ track: calculator ID, timestamp, specialty
        - Dữ liệu sẽ mất khi clear session hoặc đóng browser
        
        **Privacy:**
        - 100% anonymous
        - Không track thông tin cá nhân
        - Chỉ dùng để cải thiện trải nghiệm người dùng
        """)

