"""
Enhanced Analytics Features
- Export to PDF
- Trend analysis
- Comparison between periods
- More detailed charts
"""

import streamlit as st
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from components.analytics import (
    get_total_calculations,
    get_most_used_calculators,
    get_specialty_breakdown,
    get_daily_usage,
    get_peak_usage_hours,
    export_analytics_to_csv
)
import logging

logger = logging.getLogger(__name__)


def calculate_trend(
    current_period: Dict[str, int],
    previous_period: Dict[str, int]
) -> Dict[str, float]:
    """
    Calculate trend between two periods
    
    Args:
        current_period: Current period data (date -> count)
        previous_period: Previous period data (date -> count)
    
    Returns:
        Dictionary with trend metrics
    """
    try:
        current_total = sum(current_period.values())
        previous_total = sum(previous_period.values())
        
        if previous_total == 0:
            change_pct = 100.0 if current_total > 0 else 0.0
        else:
            change_pct = ((current_total - previous_total) / previous_total) * 100
        
        return {
            'current_total': current_total,
            'previous_total': previous_total,
            'change': current_total - previous_total,
            'change_pct': change_pct,
            'trend': 'up' if change_pct > 0 else 'down' if change_pct < 0 else 'stable'
        }
    except Exception as e:
        logger.error(f"Error calculating trend: {e}", exc_info=True)
        return {
            'current_total': 0,
            'previous_total': 0,
            'change': 0,
            'change_pct': 0.0,
            'trend': 'stable'
        }


def compare_periods(
    days_current: int = 7,
    days_previous: int = 7
) -> Dict[str, Any]:
    """
    Compare usage between two periods
    
    Args:
        days_current: Number of days for current period
        days_previous: Number of days for previous period
    
    Returns:
        Comparison data
    """
    try:
        # Get current period
        current_end = datetime.now()
        current_start = current_end - timedelta(days=days_current)
        current_usage = get_daily_usage(days=days_current)
        
        # Get previous period
        previous_end = current_start
        previous_start = previous_end - timedelta(days=days_previous)
        
        # Get previous period data from session state
        if 'analytics_data' in st.session_state:
            analytics = st.session_state.analytics_data
            daily_counts = analytics.get('daily_counts', {})
            
            previous_usage = {}
            for i in range(days_previous):
                date = (previous_end - timedelta(days=i)).strftime('%Y-%m-%d')
                previous_usage[date] = daily_counts.get(date, 0)
        else:
            previous_usage = {}
        
        # Calculate trends
        trend = calculate_trend(current_usage, previous_usage)
        
        # Get calculator trends
        current_calcs = get_most_used_calculators(limit=10)
        # Note: Previous period calculator data would need to be stored separately
        
        return {
            'current_period': {
                'days': days_current,
                'usage': current_usage,
                'total': trend['current_total']
            },
            'previous_period': {
                'days': days_previous,
                'usage': previous_usage,
                'total': trend['previous_total']
            },
            'trend': trend,
            'top_calculators': current_calcs
        }
    except Exception as e:
        logger.error(f"Error comparing periods: {e}", exc_info=True)
        return {}


def export_analytics_to_pdf() -> Optional[bytes]:
    """
    Export analytics data to PDF
    
    Returns:
        PDF bytes or None if error
    """
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from io import BytesIO
        
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        story = []
        styles = getSampleStyleSheet()
        
        # Title
        title = Paragraph("Analytics Report", styles['Title'])
        story.append(title)
        story.append(Spacer(1, 0.2*inch))
        
        # Date
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_para = Paragraph(f"Generated: {date_str}", styles['Normal'])
        story.append(date_para)
        story.append(Spacer(1, 0.2*inch))
        
        # Total calculations
        total = get_total_calculations()
        total_para = Paragraph(f"Total Calculations: {total}", styles['Heading2'])
        story.append(total_para)
        story.append(Spacer(1, 0.1*inch))
        
        # Most used calculators
        most_used = get_most_used_calculators(limit=10)
        if most_used:
            story.append(Paragraph("Most Used Calculators", styles['Heading2']))
            story.append(Spacer(1, 0.1*inch))
            
            data = [['Calculator', 'Count']]
            for calc in most_used:
                data.append([calc['name'], str(calc['count'])])
            
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
            story.append(Spacer(1, 0.2*inch))
        
        # Specialty breakdown
        specialty = get_specialty_breakdown()
        if specialty:
            story.append(Paragraph("Specialty Breakdown", styles['Heading2']))
            story.append(Spacer(1, 0.1*inch))
            
            data = [['Specialty', 'Count']]
            for spec, count in sorted(specialty.items(), key=lambda x: x[1], reverse=True):
                data.append([spec, str(count)])
            
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 14),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
        
    except ImportError:
        logger.warning("reportlab not available, PDF export disabled")
        return None
    except Exception as e:
        logger.error(f"Error exporting to PDF: {e}", exc_info=True)
        return None


def render_trend_analysis():
    """Render trend analysis section"""
    st.markdown("#### 📈 Trend Analysis")
    
    try:
        comparison = compare_periods(days_current=7, days_previous=7)
        
        if not comparison:
            st.info("Không đủ dữ liệu để phân tích xu hướng")
            return
        
        trend = comparison.get('trend', {})
        current_total = trend.get('current_total', 0)
        previous_total = trend.get('previous_total', 0)
        change = trend.get('change', 0)
        change_pct = trend.get('change_pct', 0.0)
        trend_direction = trend.get('trend', 'stable')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "This Week",
                current_total,
                delta=f"{change} ({change_pct:+.1f}%)"
            )
        
        with col2:
            st.metric(
                "Last Week",
                previous_total
            )
        
        with col3:
            trend_icon = "📈" if trend_direction == 'up' else "📉" if trend_direction == 'down' else "➡️"
            st.metric(
                "Trend",
                trend_direction.title(),
                delta=trend_icon
            )
        
    except Exception as e:
        logger.error(f"Error rendering trend analysis: {e}", exc_info=True)
        st.error("Lỗi khi phân tích xu hướng")


__all__ = [
    'calculate_trend',
    'compare_periods',
    'export_analytics_to_pdf',
    'render_trend_analysis',
]

