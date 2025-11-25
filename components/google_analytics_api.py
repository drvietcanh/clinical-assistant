"""
Google Analytics API Component
Lấy số liệu thực tế từ Google Analytics Data API (GA4)
"""

import streamlit as st
from typing import Dict, Optional, Any
from datetime import datetime, timedelta
import json
import os

try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import (
        RunReportRequest,
        DateRange,
        Dimension,
        Metric,
    )
    from google.oauth2 import service_account
    GA_API_AVAILABLE = True
except ImportError:
    GA_API_AVAILABLE = False
    # Tạo dummy classes để tránh lỗi khi import
    class BetaAnalyticsDataClient:
        pass
    class RunReportRequest:
        pass
    class DateRange:
        pass
    class Dimension:
        pass
    class Metric:
        pass
    service_account = None


def get_ga_credentials() -> Optional[Any]:
    """
    Lấy Google Analytics credentials từ Streamlit secrets hoặc environment variable
    
    Returns:
        Credentials object hoặc None nếu không có
    """
    if not GA_API_AVAILABLE or service_account is None:
        return None
    
    # Thử lấy từ Streamlit secrets
    try:
        if hasattr(st, 'secrets') and 'google_analytics' in st.secrets:
            ga_secrets = st.secrets['google_analytics']
            
            # Nếu có service account JSON
            if 'service_account_json' in ga_secrets:
                service_account_info = json.loads(ga_secrets['service_account_json'])
                credentials = service_account.Credentials.from_service_account_info(
                    service_account_info,
                    scopes=['https://www.googleapis.com/auth/analytics.readonly']
                )
                return credentials
            
            # Hoặc nếu có path đến file JSON
            elif 'service_account_path' in ga_secrets:
                credentials = service_account.Credentials.from_service_account_file(
                    ga_secrets['service_account_path'],
                    scopes=['https://www.googleapis.com/auth/analytics.readonly']
                )
                return credentials
    except Exception as e:
        st.warning(f"Không thể load credentials từ secrets: {e}")
    
    # Thử lấy từ environment variable
    try:
        service_account_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        if service_account_path and os.path.exists(service_account_path):
            credentials = service_account.Credentials.from_service_account_file(
                service_account_path,
                scopes=['https://www.googleapis.com/auth/analytics.readonly']
            )
            return credentials
    except Exception as e:
        pass
    
    return None


def get_ga_property_id() -> Optional[str]:
    """
    Lấy Google Analytics Property ID từ config hoặc secrets
    
    Returns:
        Property ID (format: properties/123456789) hoặc None
    """
    # Thử lấy từ Streamlit secrets
    try:
        if hasattr(st, 'secrets') and 'google_analytics' in st.secrets:
            ga_secrets = st.secrets['google_analytics']
            if 'property_id' in ga_secrets:
                prop_id = ga_secrets['property_id']
                # Đảm bảo format đúng
                if not prop_id.startswith('properties/'):
                    prop_id = f"properties/{prop_id}"
                return prop_id
    except Exception:
        pass
    
    # Thử lấy từ environment variable
    prop_id = os.getenv('GOOGLE_ANALYTICS_PROPERTY_ID')
    if prop_id:
        if not prop_id.startswith('properties/'):
            prop_id = f"properties/{prop_id}"
        return prop_id
    
    return None


def get_analytics_data(
    property_id: str,
    credentials: Any,
    days: int = 30
) -> Optional[Dict[str, Any]]:
    """
    Lấy dữ liệu từ Google Analytics API
    
    Args:
        property_id: Property ID (format: properties/123456789)
        credentials: Google credentials object
        days: Số ngày để lấy dữ liệu (mặc định 30)
    
    Returns:
        Dictionary chứa các metrics hoặc None nếu lỗi
    """
    if not GA_API_AVAILABLE:
        return None
    
    try:
        # Tạo client
        client = BetaAnalyticsDataClient(credentials=credentials)
        
        # Tính toán date range
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        
        # Request để lấy tổng số users, sessions, page views
        request = RunReportRequest(
            property=property_id,
            date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
            dimensions=[
                Dimension(name="date"),
            ],
            metrics=[
                Metric(name="activeUsers"),
                Metric(name="sessions"),
                Metric(name="screenPageViews"),
            ],
        )
        
        response = client.run_report(request)
        
        # Tính tổng
        total_users = 0
        total_sessions = 0
        total_pageviews = 0
        
        for row in response.rows:
            for i, metric_value in enumerate(row.metric_values):
                value = int(metric_value.value)
                if i == 0:  # activeUsers
                    total_users += value
                elif i == 1:  # sessions
                    total_sessions += value
                elif i == 2:  # screenPageViews
                    total_pageviews += value
        
        # Lấy dữ liệu realtime (last 30 minutes)
        realtime_request = RunReportRequest(
            property=property_id,
            dimensions=[Dimension(name="country")],
            metrics=[
                Metric(name="activeUsers"),
            ],
        )
        
        realtime_response = client.run_realtime_report(realtime_request)
        realtime_users = 0
        for row in realtime_response.rows:
            for metric_value in row.metric_values:
                realtime_users += int(metric_value.value)
        
        return {
            'total_users': total_users,
            'total_sessions': total_sessions,
            'total_pageviews': total_pageviews,
            'realtime_users': realtime_users,
            'date_range': {
                'start': start_date,
                'end': end_date,
                'days': days
            }
        }
        
    except Exception as e:
        st.error(f"Lỗi khi lấy dữ liệu từ Google Analytics: {str(e)}")
        return None


@st.cache_data(ttl=300)  # Cache 5 phút
def get_cached_analytics_data(
    property_id: str,
    credentials_json: str,
    days: int = 30
) -> Optional[Dict[str, Any]]:
    """
    Lấy và cache dữ liệu analytics
    
    Args:
        property_id: Property ID
        credentials_json: JSON string của credentials
        days: Số ngày
    
    Returns:
        Dictionary chứa metrics hoặc None
    """
    try:
        credentials = service_account.Credentials.from_service_account_info(
            json.loads(credentials_json),
            scopes=['https://www.googleapis.com/auth/analytics.readonly']
        )
        return get_analytics_data(property_id, credentials, days)
    except Exception:
        return None


def render_analytics_setup_guide():
    """
    Hiển thị hướng dẫn setup Google Analytics API
    """
    st.markdown("""
    <div style="
        background: #fff3cd;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #ffc107;
        margin: 20px 0;
    ">
        <h4 style="margin: 0 0 15px 0; color: #856404;">🔧 Hướng Dẫn Setup Google Analytics API</h4>
        <p style="margin: 0 0 10px 0; color: #856404;">
            Để hiển thị số liệu thực tế, bạn cần cấu hình Google Analytics API:
        </p>
        <ol style="margin: 0; padding-left: 20px; color: #856404;">
            <li>Tạo Service Account trong Google Cloud Console</li>
            <li>Download JSON credentials file</li>
            <li>Thêm credentials vào Streamlit secrets hoặc environment variable</li>
            <li>Thêm Property ID vào config</li>
        </ol>
        <p style="margin: 10px 0 0 0; color: #856404;">
            <strong>Xem hướng dẫn chi tiết:</strong> 
            <a href="docs/GOOGLE_ANALYTICS_API_SETUP.md" target="_blank" style="color: #856404; text-decoration: underline;">
                docs/GOOGLE_ANALYTICS_API_SETUP.md
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

