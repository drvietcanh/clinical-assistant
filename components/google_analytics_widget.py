"""
Google Analytics Widget Component
Hiển thị lượt truy cập và thống kê từ Google Analytics trên trang web
"""

import streamlit as st
import streamlit.components.v1 as components
from config.app_config import APP_CONFIG
from components.google_analytics_api import (
    get_ga_credentials,
    get_ga_property_id,
    get_analytics_data,
    render_analytics_setup_guide,
    GA_API_AVAILABLE
)


def render_google_analytics_stats():
    """
    Render Google Analytics statistics widget
    Hiển thị lượt truy cập từ Google Analytics
    """
    ga_id = APP_CONFIG.get("google_analytics_id", "")
    
    if not ga_id or ga_id == "G-XXXXXXXXXX":
        return
    
    st.markdown("---")
    st.markdown("### 📊 Thống kê truy cập")
    
    # Hiển thị widget Google Analytics
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        text-align: center;
    ">
        <h3 style="color: white; margin: 0 0 10px 0;">📈 Google Analytics</h3>
        <p style="color: rgba(255,255,255,0.9); margin: 0;">
            Theo dõi lượt truy cập và thống kê chi tiết tại 
            <a href="https://analytics.google.com/" target="_blank" style="color: white; text-decoration: underline;">
                Google Analytics Dashboard
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Embed Google Analytics Embed API
    st.markdown(f"""
    <div id="ga-stats-container" style="margin: 20px 0;">
        <iframe 
            src="https://analytics.google.com/analytics/web/#/p{ga_id.replace('G-', '')}/reports/intelligenthome"
            width="100%" 
            height="400" 
            frameborder="0"
            style="border-radius: 8px;"
            title="Google Analytics Stats"
        ></iframe>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **Lưu ý:** Để xem thống kê chi tiết, vui lòng đăng nhập vào [Google Analytics](https://analytics.google.com/)")


def render_google_analytics_badge():
    """
    Render a simple badge showing Google Analytics is active
    Hiển thị badge đơn giản cho biết Google Analytics đang hoạt động
    """
    ga_id = APP_CONFIG.get("google_analytics_id", "")
    
    if not ga_id or ga_id == "G-XXXXXXXXXX":
        return
    
    badge_html = f"""
    <div style="
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: rgba(102, 126, 234, 0.9);
        color: white;
        padding: 10px 15px;
        border-radius: 20px;
        font-size: 0.85rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 1000;
        cursor: pointer;
        transition: all 0.3s ease;
    " 
    onmouseover="this.style.background='rgba(102, 126, 234, 1)'; this.style.transform='scale(1.05)';"
    onmouseout="this.style.background='rgba(102, 126, 234, 0.9)'; this.style.transform='scale(1)';"
    onclick="window.open('https://analytics.google.com/', '_blank');"
    title="Xem Google Analytics Dashboard"
    >
        📊 Analytics Active
    </div>
    """
    components.html(badge_html, height=0, scrolling=False)


def render_google_analytics_counter():
    """
    Render a simple page view counter với số liệu thực tế từ Google Analytics API
    Hiển thị bộ đếm lượt truy cập đơn giản
    """
    ga_id = APP_CONFIG.get("google_analytics_id", "")
    
    if not ga_id or ga_id == "G-XXXXXXXXXX":
        return
    
    st.markdown("---")
    
    # Header section
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(102,126,234,0.2);
    ">
        <h2 style="color: white; margin: 0 0 10px 0; font-size: 2rem;">📊 Thống kê truy cập</h2>
        <p style="color: rgba(255,255,255,0.95); margin: 0; font-size: 1rem;">
            Theo dõi lượt truy cập và thống kê từ Google Analytics
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Thử lấy số liệu thực tế từ API
    analytics_data = None
    if GA_API_AVAILABLE:
        credentials = get_ga_credentials()
        property_id = get_ga_property_id()
        
        if credentials and property_id:
            with st.spinner("Đang tải số liệu từ Google Analytics..."):
                analytics_data = get_analytics_data(property_id, credentials, days=30)
    
    # Hiển thị số liệu thực tế nếu có
    if analytics_data:
        st.success("✅ Đã kết nối với Google Analytics API!")
        
        # Metrics row
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "👥 Người Dùng (30 ngày)",
                f"{analytics_data['total_users']:,}",
                help="Tổng số người dùng trong 30 ngày qua"
            )
        
        with col2:
            st.metric(
                "🔄 Sessions",
                f"{analytics_data['total_sessions']:,}",
                help="Tổng số phiên truy cập"
            )
        
        with col3:
            st.metric(
                "📄 Lượt Xem Trang",
                f"{analytics_data['total_pageviews']:,}",
                help="Tổng số lượt xem trang"
            )
        
        with col4:
            st.metric(
                "⚡ Đang Online",
                f"{analytics_data['realtime_users']}",
                help="Số người dùng đang truy cập (realtime)"
            )
        
        st.caption(f"📅 Dữ liệu từ {analytics_data['date_range']['start']} đến {analytics_data['date_range']['end']}")
        st.markdown("---")
    else:
        # Không hiển thị gì nếu chưa có dữ liệu
        pass
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 25px;
            background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
            border-radius: 12px;
            border: 2px solid #1976d2;
            box-shadow: 0 2px 8px rgba(25,118,210,0.15);
            transition: transform 0.2s;
        ">
            <div style="font-size: 3rem; font-weight: bold; color: #1976d2; margin-bottom: 10px;">
                📊
            </div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #1976d2; margin-bottom: 5px;">
                Google Analytics
            </div>
            <div style="font-size: 0.95rem; color: #666; margin-top: 8px;">
                ✅ Đang theo dõi
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 25px;
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            border-radius: 12px;
            border: 2px solid #4caf50;
            box-shadow: 0 2px 8px rgba(76,175,80,0.15);
        ">
            <div style="font-size: 3rem; font-weight: bold; color: #4caf50; margin-bottom: 10px;">
                🔍
            </div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #4caf50; margin-bottom: 5px;">
                Measurement ID
            </div>
            <div style="font-size: 0.9rem; color: #666; margin-top: 8px; font-family: 'Courier New', monospace; background: rgba(255,255,255,0.7); padding: 8px; border-radius: 6px;">
                {ga_id}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 25px;
            background: linear-gradient(135deg, #fff3e0 0%, #ffe0b2 100%);
            border-radius: 12px;
            border: 2px solid #ff9800;
            box-shadow: 0 2px 8px rgba(255,152,0,0.15);
        ">
            <div style="font-size: 3rem; font-weight: bold; color: #ff9800; margin-bottom: 10px;">
                📈
            </div>
            <div style="font-size: 1.3rem; font-weight: bold; color: #ff9800; margin-bottom: 5px;">
                Xem Dashboard
            </div>
            <div style="font-size: 0.95rem; color: #666; margin-top: 8px;">
                <a href="https://analytics.google.com/" target="_blank" 
                   style="color: #ff9800; text-decoration: none; font-weight: bold; padding: 8px 16px; background: rgba(255,152,0,0.1); border-radius: 6px; display: inline-block;">
                    Mở Analytics →
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)
    

