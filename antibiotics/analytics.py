"""
Analytics & History
Theo dõi lịch sử sử dụng và thống kê
"""

import streamlit as st
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import json

# Session state keys for analytics
ANALYTICS_KEYS = {
    "usage_history": "antibiotic_usage_history",
    "search_history": "antibiotic_search_history",
    "calculation_history": "antibiotic_calculation_history",
    "view_history": "antibiotic_view_history",
}


def log_usage(action: str, antibiotic_name: str, details: Optional[Dict] = None):
    """Log antibiotic usage action"""
    if ANALYTICS_KEYS["usage_history"] not in st.session_state:
        st.session_state[ANALYTICS_KEYS["usage_history"]] = []
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,  # "view", "calculate", "search", "compare"
        "antibiotic": antibiotic_name,
        "details": details or {}
    }
    
    history = st.session_state[ANALYTICS_KEYS["usage_history"]]
    history.append(entry)
    
    # Keep only last 1000 entries
    if len(history) > 1000:
        history = history[-1000:]
    
    st.session_state[ANALYTICS_KEYS["usage_history"]] = history


def get_usage_stats(days: int = 30) -> Dict:
    """Get usage statistics for the last N days"""
    if ANALYTICS_KEYS["usage_history"] not in st.session_state:
        return {
            "total_actions": 0,
            "most_viewed": [],
            "most_calculated": [],
            "actions_by_type": {},
            "daily_usage": []
        }
    
    history = st.session_state[ANALYTICS_KEYS["usage_history"]]
    cutoff_date = datetime.now() - timedelta(days=days)
    
    # Filter by date
    recent_history = [
        entry for entry in history
        if datetime.fromisoformat(entry["timestamp"]) >= cutoff_date
    ]
    
    # Count actions by type
    actions_by_type = {}
    antibiotic_views = {}
    antibiotic_calculations = {}
    
    for entry in recent_history:
        action = entry["action"]
        actions_by_type[action] = actions_by_type.get(action, 0) + 1
        
        if action == "view":
            ab_name = entry["antibiotic"]
            antibiotic_views[ab_name] = antibiotic_views.get(ab_name, 0) + 1
        elif action == "calculate":
            ab_name = entry["antibiotic"]
            antibiotic_calculations[ab_name] = antibiotic_calculations.get(ab_name, 0) + 1
    
    # Get most viewed
    most_viewed = sorted(
        antibiotic_views.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
    
    # Get most calculated
    most_calculated = sorted(
        antibiotic_calculations.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
    
    # Daily usage
    daily_usage = {}
    for entry in recent_history:
        date = datetime.fromisoformat(entry["timestamp"]).date()
        daily_usage[date] = daily_usage.get(date, 0) + 1
    
    daily_usage_list = [
        {"date": str(date), "count": count}
        for date, count in sorted(daily_usage.items())
    ]
    
    return {
        "total_actions": len(recent_history),
        "most_viewed": most_viewed,
        "most_calculated": most_calculated,
        "actions_by_type": actions_by_type,
        "daily_usage": daily_usage_list,
        "period_days": days
    }


def render_analytics():
    """Render Analytics Dashboard UI"""
    
    st.markdown("### 📊 Analytics & Thống Kê")
    st.caption("Theo dõi lịch sử sử dụng và thống kê về kháng sinh")
    
    # Initialize if needed
    if ANALYTICS_KEYS["usage_history"] not in st.session_state:
        st.session_state[ANALYTICS_KEYS["usage_history"]] = []
        st.info("💡 Chưa có dữ liệu. Sử dụng các tính năng để tạo dữ liệu thống kê.")
    
    # Period selection
    period_days = st.selectbox(
        "Chọn khoảng thời gian:",
        options=[7, 30, 90, 365],
        format_func=lambda x: f"{x} ngày",
        key="analytics_period"
    )
    
    # Get statistics
    stats = get_usage_stats(period_days)
    
    if stats["total_actions"] == 0:
        st.info("💡 Chưa có dữ liệu trong khoảng thời gian này.")
        return
    
    # Summary metrics
    st.markdown("---")
    st.markdown("#### 📈 Tổng Quan")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tổng số thao tác", stats["total_actions"])
    
    with col2:
        views = stats["actions_by_type"].get("view", 0)
        st.metric("Lượt xem", views)
    
    with col3:
        calculations = stats["actions_by_type"].get("calculate", 0)
        st.metric("Tính liều", calculations)
    
    with col4:
        searches = stats["actions_by_type"].get("search", 0)
        st.metric("Tìm kiếm", searches)
    
    # Most viewed antibiotics
    st.markdown("---")
    st.markdown("#### 🔝 Kháng Sinh Được Xem Nhiều Nhất")
    
    if stats["most_viewed"]:
        for idx, (ab_name, count) in enumerate(stats["most_viewed"], 1):
            medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"{idx}."
            st.markdown(f"{medal} **{ab_name}**: {count} lượt xem")
    else:
        st.info("Chưa có dữ liệu")
    
    # Most calculated antibiotics
    st.markdown("---")
    st.markdown("#### 🧮 Kháng Sinh Được Tính Liều Nhiều Nhất")
    
    if stats["most_calculated"]:
        for idx, (ab_name, count) in enumerate(stats["most_calculated"], 1):
            medal = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else f"{idx}."
            st.markdown(f"{medal} **{ab_name}**: {count} lần tính")
    else:
        st.info("Chưa có dữ liệu")
    
    # Actions by type chart
    st.markdown("---")
    st.markdown("#### 📊 Phân Bố Theo Loại Thao Tác")
    
    if stats["actions_by_type"]:
        try:
            import plotly.express as px
            
            action_data = [
                {"Loại": action, "Số lượng": count}
                for action, count in stats["actions_by_type"].items()
            ]
            
            fig = px.pie(
                action_data,
                values="Số lượng",
                names="Loại",
                title="Phân bố thao tác"
            )
            st.plotly_chart(fig, use_container_width=True)
        except ImportError:
            # Fallback to text
            for action, count in stats["actions_by_type"].items():
                st.markdown(f"- **{action}**: {count}")
    
    # Daily usage chart
    st.markdown("---")
    st.markdown("#### 📅 Sử Dụng Theo Ngày")
    
    if stats["daily_usage"]:
        try:
            import plotly.express as px
            import pandas as pd
            
            df = pd.DataFrame(stats["daily_usage"])
            df["date"] = pd.to_datetime(df["date"])
            
            fig = px.bar(
                df,
                x="date",
                y="count",
                title="Số lượng thao tác theo ngày",
                labels={"date": "Ngày", "count": "Số lượng"}
            )
            st.plotly_chart(fig, use_container_width=True)
        except ImportError:
            # Fallback to text
            for entry in stats["daily_usage"][-10:]:  # Show last 10 days
                st.markdown(f"- **{entry['date']}**: {entry['count']} thao tác")
    
    # Export data
    st.markdown("---")
    st.markdown("#### 💾 Xuất Dữ Liệu")
    
    if st.button("📥 Xuất dữ liệu JSON", use_container_width=True):
        json_data = json.dumps(stats, indent=2, ensure_ascii=False)
        st.download_button(
            label="💾 Tải JSON",
            data=json_data,
            file_name=f"antibiotic_analytics_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json",
            use_container_width=True
        )
    
    # Clear data option
    st.markdown("---")
    with st.expander("🗑️ Xóa Dữ Liệu", expanded=False):
        st.warning("⚠️ Xóa dữ liệu sẽ không thể khôi phục")
        if st.button("🗑️ Xóa tất cả dữ liệu", type="secondary"):
            st.session_state[ANALYTICS_KEYS["usage_history"]] = []
            st.success("✅ Đã xóa dữ liệu")
            st.rerun()
