"""
Main Menu Stats Dashboard Component
Modern stats dashboard with visual charts, usage trends, and analytics
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from config.calculators import ALL_CALCULATORS
from collections import Counter


def get_usage_stats():
    """Get usage statistics from session state"""
    usage_stats = st.session_state.get('usage_stats', {
        'total_calculations': 0,
        'calculations_by_category': {},
        'most_used_calculator': None,
        'calculations_by_date': [],
        'calculations_by_calculator': {}
    })
    return usage_stats


def calculate_category_breakdown():
    """Calculate calculator breakdown by category"""
    categories = {}
    for calc_id, calc_info in ALL_CALCULATORS.items():
        category = calc_info.get('category', 'Khác')
        if category not in categories:
            categories[category] = []
        categories[category].append({
            'id': calc_id,
            'name': calc_info.get('name', ''),
            'icon': calc_info.get('icon', '📊')
        })
    return categories


def render_main_menu_stats():
    """Render modern stats dashboard with charts"""
    usage_stats = get_usage_stats()
    
    st.markdown("### 📊 Thống kê sử dụng")
    
    # Quick stats row
    col1, col2, col3, col4 = st.columns(4)
    
    total_calcs = usage_stats.get('total_calculations', 0)
    total_favorites = len(st.session_state.get('favorites', []))
    total_recent = len(st.session_state.get('recently_used', []))
    total_calculators = len(ALL_CALCULATORS)
    
    with col1:
        st.metric("Tổng tính toán", total_calcs, delta=f"{total_calcs} lần" if total_calcs > 0 else None)
    
    with col2:
        st.metric("Calculators", total_calculators, delta="Sẵn sàng")
    
    with col3:
        st.metric("Yêu thích", total_favorites, delta=f"+{total_favorites}" if total_favorites > 0 else "Thêm thêm")
    
    with col4:
        st.metric("Gần đây", total_recent, delta="Đã dùng" if total_recent > 0 else "Chưa có")
    
    st.markdown("---")
    
    # Charts section
    chart_tab1, chart_tab2, chart_tab3 = st.tabs(["📈 Phân bổ theo nhóm", "⭐ Top Calculators", "📅 Xu hướng"])
    
    with chart_tab1:
        render_category_breakdown_chart()
    
    with chart_tab2:
        render_top_calculators_list()
    
    with chart_tab3:
        render_usage_trends()


def render_category_breakdown_chart():
    """Render pie/bar chart showing calculator breakdown by category"""
    categories = calculate_category_breakdown()
    
    # Prepare data for chart
    category_names = []
    category_counts = []
    
    for category, calculators in categories.items():
        category_names.append(category)
        category_counts.append(len(calculators))
    
    if category_names:
        # Create DataFrame
        df = pd.DataFrame({
            'Nhóm': category_names,
            'Số lượng': category_counts
        })
        
        # Sort by count
        df = df.sort_values('Số lượng', ascending=False)
        
        # Display bar chart
        st.bar_chart(df.set_index('Nhóm'))
        
        # Also show as metrics
        st.markdown("#### Chi tiết theo nhóm")
        cols = st.columns(min(4, len(category_names)))
        for idx, (category, count) in enumerate(zip(df['Nhóm'], df['Số lượng'])):
            with cols[idx % len(cols)]:
                st.metric(category, count)
    else:
        st.info("Chưa có dữ liệu phân bổ")


def render_top_calculators_list():
    """Render list of top calculators with usage stats"""
    usage_stats = get_usage_stats()
    calculations_by_calc = usage_stats.get('calculations_by_calculator', {})
    
    # Get most used calculators
    if calculations_by_calc:
        # Sort by usage count
        sorted_calcs = sorted(
            calculations_by_calc.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
        
        st.markdown("#### Top 10 Calculators được dùng nhiều nhất")
        
        # Create DataFrame for display
        calc_data = []
        for calc_id, count in sorted_calcs:
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                calc_data.append({
                    'Calculator': calc_info.get('name', calc_id),
                    'Icon': calc_info.get('icon', '📊'),
                    'Nhóm': calc_info.get('category', ''),
                    'Số lần dùng': count
                })
        
        if calc_data:
            df = pd.DataFrame(calc_data)
            
            # Display as table with styling
            for idx, row in df.iterrows():
                col1, col2, col3 = st.columns([1, 4, 2])
                with col1:
                    st.markdown(f"<div style='font-size: 2rem; text-align: center;'>{row['Icon']}</div>", unsafe_allow_html=True)
                with col2:
                    st.markdown(f"**{row['Calculator']}**")
                    st.caption(row['Nhóm'])
                with col3:
                    st.metric("", row['Số lần dùng'], delta="lần")
                st.markdown("---")
        else:
            st.info("Chưa có dữ liệu sử dụng")
    else:
        st.info("""
        **Chưa có dữ liệu sử dụng**
        
        Bắt đầu sử dụng các calculators để xem thống kê ở đây!
        """)
        
        # Show default popular calculators
        st.markdown("#### 💡 Gợi ý: Các calculators phổ biến")
        default_popular = ['ascvd', 'cha2ds2vasc', 'sofa', 'gcs', 'qsofa']
        cols = st.columns(min(5, len(default_popular)))
        for idx, calc_id in enumerate(default_popular[:5]):
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                with cols[idx]:
                    st.markdown(
                        f"""
                        <div style="text-align: center; padding: 12px; border: 1px solid var(--border-color); border-radius: 8px;">
                            <div style="font-size: 2rem;">{calc_info.get('icon', '📊')}</div>
                            <div style="font-size: 0.85rem; margin-top: 4px;">{calc_info.get('name', '')}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


def render_usage_trends():
    """Render usage trends over time"""
    usage_stats = get_usage_stats()
    calculations_by_date = usage_stats.get('calculations_by_date', [])
    
    if calculations_by_date:
        # Prepare data for line chart
        dates = []
        counts = []
        
        # Get last 7 days
        today = datetime.now().date()
        last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
        
        date_counts = Counter()
        for date_str, count in calculations_by_date:
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                if date_obj in last_7_days:
                    date_counts[date_obj] += count
            except Exception:
                pass
        
        # Fill in missing dates with 0
        for date_obj in last_7_days:
            dates.append(date_obj.strftime('%d/%m'))
            counts.append(date_counts.get(date_obj, 0))
        
        if dates:
            df = pd.DataFrame({
                'Ngày': dates,
                'Số lần tính': counts
            })
            
            st.line_chart(df.set_index('Ngày'))
            
            # Summary
            total_week = sum(counts)
            avg_per_day = total_week / 7 if len(counts) > 0 else 0
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Tổng tuần này", total_week)
            with col2:
                st.metric("Trung bình/ngày", f"{avg_per_day:.1f}")
        else:
            st.info("Chưa có dữ liệu xu hướng")
    else:
        st.info("""
        **Chưa có dữ liệu xu hướng**
        
        Dữ liệu xu hướng sẽ được cập nhật khi bạn sử dụng các calculators.
        """)
        
        # Show sample chart
        sample_dates = [(datetime.now() - timedelta(days=i)).strftime('%d/%m') for i in range(6, -1, -1)]
        sample_data = pd.DataFrame({
            'Ngày': sample_dates,
            'Số lần tính': [0] * 7
        })
        st.line_chart(sample_data.set_index('Ngày'))
        st.caption("Biểu đồ mẫu - sẽ cập nhật khi có dữ liệu")


def render_personal_stats():
    """Render personal statistics for the user"""
    usage_stats = get_usage_stats()
    total_calcs = usage_stats.get('total_calculations', 0)
    most_used = usage_stats.get('most_used_calculator')
    calculations_by_category = usage_stats.get('calculations_by_category', {})
    
    st.markdown("### 📊 Thống kê cá nhân")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Tổng tính toán", total_calcs)
    
    with col2:
        if most_used and most_used in ALL_CALCULATORS:
            calc_name = ALL_CALCULATORS[most_used].get('name', 'N/A')
            st.metric("Dùng nhiều nhất", calc_name)
        else:
            st.metric("Dùng nhiều nhất", "Chưa có")
    
    with col3:
        if calculations_by_category:
            top_category = max(calculations_by_category.items(), key=lambda x: x[1])[0]
            st.metric("Nhóm yêu thích", top_category)
        else:
            st.metric("Nhóm yêu thích", "Chưa có")
    
    # Category breakdown
    if calculations_by_category:
        st.markdown("#### Phân bổ theo nhóm")
        category_df = pd.DataFrame({
            'Nhóm': list(calculations_by_category.keys()),
            'Số lần': list(calculations_by_category.values())
        })
        category_df = category_df.sort_values('Số lần', ascending=False)
        st.bar_chart(category_df.set_index('Nhóm'))
