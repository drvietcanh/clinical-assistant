"""
Guideline Viewer Component
Enhanced viewer for clinical guidelines with search, filter, and decision trees
"""

import streamlit as st
from typing import List, Optional, Dict
from guidelines.data import (
    get_all_guidelines,
    get_guidelines_by_category,
    get_guidelines_by_organization,
    get_category_list,
    get_organization_list,
    Guideline
)
from datetime import datetime


def search_guidelines_enhanced(
    query: str,
    category: Optional[str] = None,
    organization: Optional[str] = None,
    year_min: Optional[int] = None,
    year_max: Optional[int] = None
) -> List[Guideline]:
    """
    Enhanced search for guidelines with multiple filters
    
    Args:
        query: Search query (searches in title, title_vn, description)
        category: Filter by category
        organization: Filter by organization
        year_min: Minimum year
        year_max: Maximum year
    
    Returns:
        List of matching guidelines
    """
    guidelines = get_all_guidelines()
    
    # Apply filters
    if category and category != "All":
        guidelines = [g for g in guidelines if g.category == category]
    
    if organization and organization != "All":
        guidelines = [g for g in guidelines if organization in g.organization]
    
    if year_min:
        guidelines = [g for g in guidelines if g.year >= year_min]
    
    if year_max:
        guidelines = [g for g in guidelines if g.year <= year_max]
    
    # Search query
    if query:
        query_lower = query.lower().strip()
        filtered = []
        for g in guidelines:
            if (query_lower in g.title.lower() or
                query_lower in g.title_vn.lower() or
                query_lower in g.description.lower() or
                any(query_lower in rec.lower() for rec in g.key_recommendations)):
                filtered.append(g)
        guidelines = filtered
    
    # Sort by year (newest first), then by organization
    guidelines.sort(key=lambda x: (x.year, x.organization), reverse=True)
    
    return guidelines


def render_guideline_card(guideline: Guideline, show_details: bool = False):
    """
    Render a guideline card with information
    
    Args:
        guideline: Guideline object
        show_details: Whether to show detailed information
    """
    with st.container():
        # Header
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"### {guideline.title_vn}")
            st.caption(f"{guideline.organization} • {guideline.year} • {guideline.category}")
        
        with col2:
            if guideline.is_high_impact:
                st.markdown("**⭐ Practice Changing**")
        
        # Description
        if guideline.description:
            st.markdown(f"*{guideline.description}*")
        
        # Key recommendations
        if guideline.key_recommendations and show_details:
            st.markdown("**Khuyến nghị chính:**")
            for rec in guideline.key_recommendations:
                st.markdown(f"- {rec}")
        
        # Related tools and protocols
        if guideline.related_tools or guideline.related_protocol:
            st.markdown("**Liên kết:**")
            cols = st.columns(3)
            idx = 0
            
            if guideline.related_protocol:
                with cols[idx % 3]:
                    if st.button(f"📋 {guideline.related_protocol}", key=f"proto_{guideline.id}"):
                        st.switch_page("pages/04_📋_Protocols.py")
                idx += 1
            
            if guideline.related_tools:
                for tool in guideline.related_tools:
                    with cols[idx % 3]:
                        if st.button(f"🔧 {tool['name']}", key=f"tool_{guideline.id}_{idx}"):
                            # Navigate to tool
                            if tool.get('url'):
                                st.switch_page(tool['url'])
                    idx += 1
        
        # URL and metadata
        col1, col2, col3 = st.columns(3)
        with col1:
            if guideline.url:
                st.markdown(f"[🔗 Xem guideline gốc]({guideline.url})")
        with col2:
            if guideline.last_updated:
                st.caption(f"Cập nhật: {guideline.last_updated}")
        with col3:
            st.caption(f"Version: {guideline.version}")
        
        st.markdown("---")


def render_guideline_viewer(
    search_query: str = "",
    category_filter: str = "All",
    organization_filter: str = "All",
    year_min: Optional[int] = None,
    year_max: Optional[int] = None,
    show_details: bool = False
):
    """
    Render enhanced guideline viewer with filters
    
    Args:
        search_query: Search query
        category_filter: Category filter
        organization_filter: Organization filter
        year_min: Minimum year filter
        year_max: Maximum year filter
        show_details: Whether to show detailed information
    """
    # Get filtered guidelines
    guidelines = search_guidelines_enhanced(
        query=search_query,
        category=category_filter,
        organization=organization_filter,
        year_min=year_min,
        year_max=year_max
    )
    
    # Display results count
    st.markdown(f"**Tìm thấy {len(guidelines)} guidelines**")
    
    if not guidelines:
        st.info("Không tìm thấy guidelines nào. Thử thay đổi bộ lọc.")
        return
    
    # Render guidelines
    for guideline in guidelines:
        render_guideline_card(guideline, show_details=show_details)


def render_guideline_filters():
    """
    Render filter controls for guidelines
    Returns filter values
    """
    st.sidebar.markdown("### 🔍 Bộ lọc")
    
    # Category filter
    categories = ["All"] + get_category_list()
    category_filter = st.sidebar.selectbox(
        "Chuyên khoa",
        categories,
        key="guideline_category_filter"
    )
    
    # Organization filter
    organizations = ["All"] + get_organization_list()
    organization_filter = st.sidebar.selectbox(
        "Tổ chức",
        organizations,
        key="guideline_organization_filter"
    )
    
    # Year filter
    all_years = sorted(set(g.year for g in get_all_guidelines()), reverse=True)
    if all_years:
        year_min = st.sidebar.number_input(
            "Năm tối thiểu",
            min_value=min(all_years),
            max_value=max(all_years),
            value=min(all_years),
            key="guideline_year_min"
        )
        year_max = st.sidebar.number_input(
            "Năm tối đa",
            min_value=min(all_years),
            max_value=max(all_years),
            value=max(all_years),
            key="guideline_year_max"
        )
    else:
        year_min = None
        year_max = None
    
    # High impact filter
    show_high_impact_only = st.sidebar.checkbox(
        "Chỉ hiển thị Practice Changing",
        key="guideline_high_impact"
    )
    
    return {
        "category": category_filter,
        "organization": organization_filter,
        "year_min": year_min,
        "year_max": year_max,
        "high_impact_only": show_high_impact_only
    }


def render_guideline_search_bar():
    """
    Render search bar for guidelines
    Returns search query
    """
    search_query = st.text_input(
        "🔍 Tìm kiếm guidelines...",
        key="guideline_search_query",
        placeholder="Nhập từ khóa, tên guideline, hoặc khuyến nghị..."
    )
    return search_query


def get_guideline_statistics() -> Dict:
    """
    Get statistics about guidelines
    
    Returns:
        Dictionary with statistics
    """
    all_guidelines = get_all_guidelines()
    
    stats = {
        "total": len(all_guidelines),
        "by_category": {},
        "by_organization": {},
        "by_year": {},
        "high_impact_count": 0,
        "recent_count": 0  # Last 2 years
    }
    
    current_year = datetime.now().year
    
    for g in all_guidelines:
        # By category
        stats["by_category"][g.category] = stats["by_category"].get(g.category, 0) + 1
        
        # By organization
        orgs = g.organization.split("/")
        for org in orgs:
            stats["by_organization"][org] = stats["by_organization"].get(org, 0) + 1
        
        # By year
        stats["by_year"][g.year] = stats["by_year"].get(g.year, 0) + 1
        
        # High impact
        if g.is_high_impact:
            stats["high_impact_count"] += 1
        
        # Recent (last 2 years)
        if g.year >= current_year - 2:
            stats["recent_count"] += 1
    
    return stats


def render_guideline_statistics():
    """
    Render statistics dashboard for guidelines
    """
    stats = get_guideline_statistics()
    
    st.markdown("### 📊 Thống kê Guidelines")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tổng số", stats["total"])
    
    with col2:
        st.metric("Practice Changing", stats["high_impact_count"])
    
    with col3:
        st.metric("Gần đây (2 năm)", stats["recent_count"])
    
    with col4:
        st.metric("Tổ chức", len(stats["by_organization"]))
    
    # Top categories
    if stats["by_category"]:
        st.markdown("**Top chuyên khoa:**")
        top_categories = sorted(
            stats["by_category"].items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]
        for cat, count in top_categories:
            st.markdown(f"- {cat}: {count} guidelines")
