"""
Dosing Schedule Generator
Generate visual timeline for antibiotic dosing schedule
"""

import streamlit as st
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import re


def parse_frequency(frequency: str) -> Optional[int]:
    """
    Parse frequency string to hours
    
    Args:
        frequency: Frequency string (e.g., "q12h", "q8h", "q6h", "q24h", "BID", "TID", "QID")
    
    Returns:
        Hours between doses or None if cannot parse
    """
    frequency = frequency.upper().strip()
    
    # Handle qXh format
    q_match = re.search(r'Q(\d+)H', frequency)
    if q_match:
        return int(q_match.group(1))
    
    # Handle common abbreviations
    frequency_map = {
        'Q12H': 12,
        'Q8H': 8,
        'Q6H': 6,
        'Q24H': 24,
        'Q48H': 48,
        'BID': 12,  # Twice daily
        'TID': 8,   # Three times daily
        'QID': 6,   # Four times daily
        'QD': 24,   # Once daily
        'ONCE DAILY': 24,
        'TWICE DAILY': 12,
        'THREE TIMES DAILY': 8,
        'FOUR TIMES DAILY': 6
    }
    
    return frequency_map.get(frequency)


def generate_dosing_schedule(
    drug_name: str,
    dose: str,
    frequency: str,
    start_time: datetime,
    duration_days: int = 7
) -> List[Dict[str, Any]]:
    """
    Generate dosing schedule timeline
    
    Args:
        drug_name: Name of antibiotic
        dose: Dose amount (e.g., "1000mg", "500mg")
        frequency: Frequency string (e.g., "q12h", "q8h")
        start_time: Start time for first dose
        duration_days: Duration in days (default 7)
    
    Returns:
        List of {time, dose, day, day_name} dicts
    """
    interval_hours = parse_frequency(frequency)
    
    if interval_hours is None:
        return []
    
    schedule = []
    current_time = start_time
    end_time = start_time + timedelta(days=duration_days)
    day_number = 1
    
    while current_time <= end_time:
        schedule.append({
            'time': current_time,
            'dose': dose,
            'day': day_number,
            'day_name': current_time.strftime('%A'),
            'formatted_time': current_time.strftime('%H:%M'),
            'formatted_date': current_time.strftime('%Y-%m-%d')
        })
        
        current_time += timedelta(hours=interval_hours)
        
        # Update day number if crossed midnight
        if current_time.date() > schedule[-1]['time'].date():
            day_number += 1
    
    return schedule


def render_dosing_schedule(
    drug_name: str,
    dose: str,
    frequency: str,
    start_time: Optional[datetime] = None,
    duration_days: int = 7,
    patient_info: Optional[Dict[str, Any]] = None
) -> None:
    """
    Render visual dosing schedule timeline
    
    Args:
        drug_name: Name of antibiotic
        dose: Dose amount
        frequency: Frequency string
        start_time: Start time (default: current time rounded to next hour)
        duration_days: Duration in days
        patient_info: Optional patient information dict
    """
    if start_time is None:
        # Default to next hour
        now = datetime.now()
        start_time = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    
    schedule = generate_dosing_schedule(drug_name, dose, frequency, start_time, duration_days)
    
    if not schedule:
        st.error(f"⚠️ Không thể parse frequency: {frequency}. Vui lòng sử dụng format: q12h, q8h, q6h, q24h, BID, TID, QID")
        return
    
    st.markdown("---")
    st.markdown(f"### 📅 Lịch Dùng Thuốc: {drug_name}")
    
    # Patient info summary
    if patient_info:
        col1, col2, col3 = st.columns(3)
        with col1:
            if 'weight' in patient_info:
                st.metric("Cân nặng", f"{patient_info['weight']:.1f} kg")
        with col2:
            if 'crcl' in patient_info:
                st.metric("CrCl", f"{patient_info['crcl']:.1f} mL/min")
        with col3:
            st.metric("Liều", dose)
    
    st.markdown(f"**Tần suất:** {frequency} | **Bắt đầu:** {start_time.strftime('%Y-%m-%d %H:%M')} | **Thời gian:** {duration_days} ngày")
    
    st.markdown("---")
    
    # Group by day
    current_day = None
    for item in schedule:
        if current_day != item['day']:
            if current_day is not None:
                st.markdown("---")
            current_day = item['day']
            st.markdown(f"#### 📆 Ngày {item['day']} - {item['formatted_date']} ({item['day_name']})")
        
        # Visual timeline item
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            padding: 12px 20px;
            border-radius: 8px;
            margin: 8px 0;
            border-left: 4px solid #1976d2;
        ">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 1.5em;">💉</span>
                <div style="flex: 1;">
                    <strong style="font-size: 1.1em; color: #1976d2;">{item['formatted_time']}</strong>
                    <span style="margin-left: 10px; color: #666;">{item['dose']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Summary
    st.markdown("---")
    st.info(f"""
    **📊 Tóm tắt:**
    - Tổng số liều: **{len(schedule)}** liều
    - Khoảng cách: **{parse_frequency(frequency)}** giờ
    - Thời gian điều trị: **{duration_days}** ngày
    """)
    
    # Export buttons
    st.markdown("---")
    st.markdown("### 📥 Xuất Lịch")
    try:
        from .export import render_export_buttons
        
        # Format schedule for export
        schedule_html = f"""
        <h2>📅 Lịch Dùng Thuốc: {drug_name}</h2>
        <p><strong>Liều:</strong> {dose} | <strong>Tần suất:</strong> {frequency}</p>
        <p><strong>Bắt đầu:</strong> {start_time.strftime('%Y-%m-%d %H:%M')} | <strong>Thời gian:</strong> {duration_days} ngày</p>
        <hr>
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: #f5f5f5;">
                    <th style="padding: 10px; border: 1px solid #ddd;">Ngày</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Thời gian</th>
                    <th style="padding: 10px; border: 1px solid #ddd;">Liều</th>
                </tr>
            </thead>
            <tbody>
        """
        
        for item in schedule:
            schedule_html += f"""
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;">Ngày {item['day']} - {item['formatted_date']}</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{item['formatted_time']}</td>
                    <td style="padding: 8px; border: 1px solid #ddd;">{item['dose']}</td>
                </tr>
            """
        
        schedule_html += """
            </tbody>
        </table>
        """
        
        # Text version for clipboard
        schedule_text = f"""
Lịch Dùng Thuốc: {drug_name}
Liều: {dose} | Tần suất: {frequency}
Bắt đầu: {start_time.strftime('%Y-%m-%d %H:%M')} | Thời gian: {duration_days} ngày

"""
        for item in schedule:
            schedule_text += f"Ngày {item['day']} - {item['formatted_date']} {item['formatted_time']}: {item['dose']}\n"
        
        # Excel data
        schedule_data = [
            {
                'Ngày': f"Ngày {item['day']}",
                'Ngày tháng': item['formatted_date'],
                'Thời gian': item['formatted_time'],
                'Liều': item['dose']
            }
            for item in schedule
        ]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            from components.export_pdf import render_pdf_export_button
            render_pdf_export_button(
                title=f"Lịch Dùng Thuốc - {drug_name}",
                content=schedule_html,
                filename=f"schedule_{drug_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                button_text="📄 PDF"
            )
        
        with col2:
            from .export import copy_to_clipboard
            # Generate unique key using drug_name and start_time
            copy_key = f"schedule_copy_{drug_name.replace(' ', '_')}_{start_time.strftime('%Y%m%d_%H%M%S')}"
            copy_to_clipboard(schedule_text, "📋 Copy", key=copy_key)
        
        with col3:
            from .export import export_to_excel
            export_to_excel(
                schedule_data,
                filename=f"schedule_{drug_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                sheet_name="Lịch dùng thuốc"
            )
    except ImportError:
        st.info("💡 Tính năng xuất sẽ được thêm trong phiên bản tương lai")


__all__ = [
    'parse_frequency',
    'generate_dosing_schedule',
    'render_dosing_schedule',
]
