"""
Analytics Dashboard - Usage statistics and insights
Track app usage, popular features, and user engagement
"""

import streamlit as st
import json
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero

# Standard page setup
setup_page(
    page_title="Analytics",
    page_icon="📈",
    description="Usage statistics and insights"
)

# Custom CSS
st.markdown("""
<style>
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 24px;
    border-radius: 12px;
    text-align: center;
    margin: 8px 0;
}

.metric-card.secondary {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.metric-card.success {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
}

.metric-card.warning {
    background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
}

.chart-container {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    margin: 16px 0;
}
</style>
""", unsafe_allow_html=True)

# Analytics data file
ANALYTICS_FILE = Path("analytics_data.json")

# Load analytics data
def load_analytics():
    if ANALYTICS_FILE.exists():
        with open(ANALYTICS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {
        'page_views': {},
        'feature_usage': {},
        'search_queries': [],
        'user_sessions': [],
        'errors': []
    }

# Save analytics data
def save_analytics(data):
    with open(ANALYTICS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Track page view
def track_page_view(page_name: str):
    analytics = load_analytics()
    
    if page_name not in analytics['page_views']:
        analytics['page_views'][page_name] = 0
    
    analytics['page_views'][page_name] += 1
    save_analytics(analytics)

# Track feature usage
def track_feature_usage(feature_name: str):
    analytics = load_analytics()
    
    if feature_name not in analytics['feature_usage']:
        analytics['feature_usage'][feature_name] = 0
    
    analytics['feature_usage'][feature_name] += 1
    save_analytics(analytics)

# Track search query
def track_search(query: str):
    analytics = load_analytics()
    
    analytics['search_queries'].append({
        'query': query,
        'timestamp': datetime.now().isoformat()
    })
    
    # Keep only last 1000 searches
    analytics['search_queries'] = analytics['search_queries'][-1000:]
    save_analytics(analytics)

# Load data
analytics_data = load_analytics()

# Hero section
render_hero(
    title="Analytics Dashboard",
    subtitle="📈 Usage Statistics",
    description="Track app usage, popular features, and user engagement",
    icon="📈",
    gradient=("#667eea", "#764ba2")
)

# Sidebar
with st.sidebar:
    st.header("📈 Analytics")
    
    view_mode = st.radio(
        "View:",
        ["Overview", "Pages", "Features", "Search", "Trends"],
        key="analytics_view"
    )
    
    st.markdown("---")
    
    # Time range
    time_range = st.selectbox(
        "Time Range:",
        ["Last 7 days", "Last 30 days", "Last 90 days", "All time"],
        key="time_range"
    )
    
    st.markdown("---")
    
    render_info_box("""
    **📈 Analytics:**
    - Track usage patterns
    - Popular features
    - Search trends
    - User engagement
    
    **💡 Note:**
    - Data is anonymized
    - Privacy-focused
    - Local storage only
    """, type="info", title="About")

# Main content
if view_mode == "Overview":
    st.markdown("### 📊 Overview")
    
    # Top metrics
    col1, col2, col3, col4 = st.columns(4)
    
    total_page_views = sum(analytics_data['page_views'].values())
    total_features = sum(analytics_data['feature_usage'].values())
    total_searches = len(analytics_data['search_queries'])
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div style="font-size: 0.9rem; opacity: 0.9;">Page Views</div>
            <div style="font-size: 2.5rem; font-weight: 700; margin: 8px 0;">{total_page_views}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card secondary">
            <div style="font-size: 0.9rem; opacity: 0.9;">Features Used</div>
            <div style="font-size: 2.5rem; font-weight: 700; margin: 8px 0;">{total_features}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card success">
            <div style="font-size: 0.9rem; opacity: 0.9;">Searches</div>
            <div style="font-size: 2.5rem; font-weight: 700; margin: 8px 0;">{total_searches}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        unique_pages = len(analytics_data['page_views'])
        st.markdown(f"""
        <div class="metric-card warning">
            <div style="font-size: 0.9rem; opacity: 0.9;">Unique Pages</div>
            <div style="font-size: 2.5rem; font-weight: 700; margin: 8px 0;">{unique_pages}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Top pages
    st.markdown("### 📊 Top Pages")
    
    if analytics_data['page_views']:
        top_pages = sorted(analytics_data['page_views'].items(), 
                          key=lambda x: x[1], reverse=True)[:10]
        
        for idx, (page, views) in enumerate(top_pages, 1):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.markdown(f"**#{idx}**")
            with col2:
                st.markdown(f"{page}")
            with col3:
                st.markdown(f"**{views}** views")
    else:
        st.info("No page view data yet")
    
    st.markdown("---")
    
    # Top features
    st.markdown("### 🎯 Top Features")
    
    if analytics_data['feature_usage']:
        top_features = sorted(analytics_data['feature_usage'].items(), 
                             key=lambda x: x[1], reverse=True)[:10]
        
        for idx, (feature, uses) in enumerate(top_features, 1):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.markdown(f"**#{idx}**")
            with col2:
                st.markdown(f"{feature}")
            with col3:
                st.markdown(f"**{uses}** uses")
    else:
        st.info("No feature usage data yet")

elif view_mode == "Pages":
    st.markdown("### 📄 Page Analytics")
    
    if analytics_data['page_views']:
        # Sort by views
        sorted_pages = sorted(analytics_data['page_views'].items(), 
                             key=lambda x: x[1], reverse=True)
        
        # Display all pages
        for page, views in sorted_pages:
            with st.expander(f"{page} - {views} views"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Total Views", views)
                
                with col2:
                    # Calculate percentage
                    percentage = (views / total_page_views * 100) if total_page_views > 0 else 0
                    st.metric("% of Total", f"{percentage:.1f}%")
                
                # Progress bar
                st.progress(views / max(analytics_data['page_views'].values()))
    else:
        st.info("No page view data available")

elif view_mode == "Features":
    st.markdown("### 🎯 Feature Analytics")
    
    if analytics_data['feature_usage']:
        # Sort by usage
        sorted_features = sorted(analytics_data['feature_usage'].items(), 
                                key=lambda x: x[1], reverse=True)
        
        # Display all features
        for feature, uses in sorted_features:
            with st.expander(f"{feature} - {uses} uses"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Total Uses", uses)
                
                with col2:
                    # Calculate percentage
                    percentage = (uses / total_features * 100) if total_features > 0 else 0
                    st.metric("% of Total", f"{percentage:.1f}%")
                
                # Progress bar
                st.progress(uses / max(analytics_data['feature_usage'].values()))
    else:
        st.info("No feature usage data available")

elif view_mode == "Search":
    st.markdown("### 🔍 Search Analytics")
    
    if analytics_data['search_queries']:
        # Analyze search queries
        queries = [q['query'] for q in analytics_data['search_queries']]
        query_counts = Counter(queries)
        
        st.markdown(f"**Total Searches:** {len(queries)}")
        st.markdown(f"**Unique Queries:** {len(query_counts)}")
        
        st.markdown("---")
        
        # Top searches
        st.markdown("### 🔥 Top Searches")
        
        top_searches = query_counts.most_common(20)
        
        for idx, (query, count) in enumerate(top_searches, 1):
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.markdown(f"**#{idx}**")
            with col2:
                st.markdown(f"_{query}_")
            with col3:
                st.markdown(f"**{count}** times")
        
        st.markdown("---")
        
        # Recent searches
        st.markdown("### 🕐 Recent Searches")
        
        recent = analytics_data['search_queries'][-20:]
        for search in reversed(recent):
            st.caption(f"• {search['query']} - {search['timestamp'][:10]}")
    else:
        st.info("No search data available")

elif view_mode == "Trends":
    st.markdown("### 📈 Trends")
    
    st.info("Trend analysis coming soon!")
    
    st.markdown("""
    **Planned Features:**
    - Daily/Weekly/Monthly trends
    - Growth charts
    - User engagement metrics
    - Feature adoption rates
    - Search trend analysis
    """)

# Data management
st.markdown("---")
st.markdown("### 💾 Data Management")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Export Analytics"):
        analytics_json = json.dumps(analytics_data, ensure_ascii=False, indent=2)
        st.download_button(
            label="Download JSON",
            data=analytics_json,
            file_name=f"analytics_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )

with col2:
    if st.button("🔄 Refresh Data"):
        st.rerun()

with col3:
    if st.button("🗑️ Clear Analytics", type="secondary"):
        if st.checkbox("Confirm clear all analytics data"):
            empty_data = {
                'page_views': {},
                'feature_usage': {},
                'search_queries': [],
                'user_sessions': [],
                'errors': []
            }
            save_analytics(empty_data)
            st.success("✅ Analytics data cleared!")
            st.rerun()

# Footer
st.markdown("---")
render_standard_footer(disclaimer=False)
