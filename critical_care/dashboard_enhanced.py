"""
Enhanced Critical Care Dashboard
Advanced features: hover effects, recent items, quick stats, search integration
Optimized with caching, lazy loading, and performance improvements
"""

import streamlit as st
from functools import lru_cache
from typing import Dict, List, Optional
from components.ui.cards import render_clickable_dashboard_card
from components.recently_used import render_recently_used
from config.calculators import ALL_CALCULATORS

# Cache critical care calculator list (static data)
@st.cache_data(ttl=3600)  # Cache 1 hour
def get_critical_care_calculators() -> List[str]:
    """Get list of critical care calculator IDs (cached)"""
    return [
        'apache2', 'sofa', 'sofa2', 'saps2', 'mods',
        'gcs', 'kdigo', 'rifle'
    ]


def render_dashboard_styles():
    """Inject enhanced CSS styles for dashboard (cached)"""
    # Cache styles in session state to avoid re-rendering
    if 'dashboard_styles_injected' not in st.session_state:
        st.markdown("""
        <style>
    /* Enhanced Card Hover Effects */
    .dashboard-card-container {
        position: relative;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .dashboard-card-container:hover {
        transform: translateY(-4px);
    }
    
    .dashboard-card-container:hover .dashboard-card {
        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }
    
    /* Clickable Button Styling */
    .dashboard-clickable-button {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        width: 100%;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .dashboard-clickable-button:hover {
        opacity: 0.9;
    }
    
    .dashboard-clickable-button:active {
        transform: scale(0.98);
    }
    
    /* Scoring Card Styling */
    .scoring-card {
        padding: 15px;
        background: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-bottom: 10px;
    }
    
    .scoring-card:hover {
        background: #e9ecef;
        transform: translateX(4px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Scenario Card Styling */
    .scenario-card {
        padding: 15px;
        background: white;
        border-radius: 8px;
        border: 2px solid #e5e7eb;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .scenario-card:hover {
        border-color: #667eea;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.15);
        transform: translateY(-2px);
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 10px 0;
    }
    
    .stat-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .dashboard-card-container {
            margin-bottom: 15px;
        }
    }
    
    /* Animation for new items */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .dashboard-card-container {
        animation: slideIn 0.3s ease-out;
    }
    
    /* Performance optimizations */
    .dashboard-card, .scoring-card, .scenario-card {
        will-change: transform;
        backface-visibility: hidden;
    }
    
    /* Reduced motion for accessibility */
    @media (prefers-reduced-motion: reduce) {
        .dashboard-card-container,
        .scoring-card,
        .scenario-card {
            animation: none;
            transition: none;
        }
    }
    
    /* Better focus states for keyboard navigation */
    .dashboard-card:focus-visible,
    .scoring-card:focus-visible,
    .scenario-card:focus-visible {
        outline: 3px solid #667eea;
        outline-offset: 2px;
    }
    </style>
    """, unsafe_allow_html=True)
        st.session_state['dashboard_styles_injected'] = True


def get_critical_care_stats() -> Dict[str, int]:
    """Get statistics for critical care tools (optimized)"""
    recently_used = st.session_state.get('recently_used', [])
    favorites = st.session_state.get('favorites', [])
    
    # Use cached calculator list
    critical_care_calcs = set(get_critical_care_calculators())
    
    # Optimized: use set intersection for faster lookup
    used_critical_care = [calc for calc in recently_used if calc in critical_care_calcs]
    
    return {
        'recent_count': len(recently_used),
        'favorites_count': len(favorites),
        'critical_care_used': len(used_critical_care),
        'total_calculations': st.session_state.get('total_calculations', 0)
    }


def render_quick_stats():
    """Render quick statistics cards"""
    stats = get_critical_care_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <div class="stat-value">{stats['recent_count']}</div>
            <div class="stat-label">Sử dụng gần đây</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);">
            <div class="stat-value">{stats['favorites_count']}</div>
            <div class="stat-label">Yêu thích</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);">
            <div class="stat-value">{stats['critical_care_used']}</div>
            <div class="stat-label">Hồi sức đã dùng</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-card" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);">
            <div class="stat-value">{stats['total_calculations']}</div>
            <div class="stat-label">Tổng tính toán</div>
        </div>
        """, unsafe_allow_html=True)


def render_enhanced_critical_care_dashboard():
    """Render enhanced critical care dashboard with advanced features (optimized)"""
    
    # Inject styles (cached)
    render_dashboard_styles()
    
    # Header with better visual hierarchy
    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h2 style="margin: 0; color: #1f2937; font-size: 2rem;">🏠 Critical Care Dashboard</h2>
        <p style="margin: 8px 0 0 0; color: #6b7280; font-size: 1rem;">Trang tổng quan - Truy cập nhanh tất cả công cụ hồi sức</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick search integration
    col_search, col_refresh = st.columns([4, 1])
    with col_search:
        search_query = st.text_input(
            "🔍 Tìm kiếm công cụ",
            placeholder="Gõ tên calculator (ví dụ: SOFA, APACHE, GCS)...",
            key="dashboard_search",
            help="Tìm kiếm nhanh các công cụ hồi sức"
        )
    
    with col_refresh:
        st.markdown("<br>", unsafe_allow_html=True)  # Align button
        if st.button("🔄", help="Làm mới dashboard", key="refresh_dashboard"):
            # Clear cache if needed
            if 'dashboard_styles_injected' in st.session_state:
                del st.session_state['dashboard_styles_injected']
            st.rerun()
    
    # Show search results if query exists
    if search_query:
        from components.search import search_calculators
        results = search_calculators(search_query, max_results=10)
        
        # Filter for critical care calculators only
        critical_care_calcs = set(get_critical_care_calculators())
        critical_care_results = [(calc_id, calc_info, score) for calc_id, calc_info, score in results 
                                if calc_id in critical_care_calcs]
        
        if critical_care_results:
            st.success(f"✅ Tìm thấy {len(critical_care_results)} công cụ hồi sức")
            st.markdown("---")
            
            # Display results in grid
            num_cols = min(3, len(critical_care_results))
            cols = st.columns(num_cols)
            
            for idx, (calc_id, calc_info, score) in enumerate(critical_care_results[:6]):  # Show max 6
                with cols[idx % num_cols]:
                    st.markdown(f"""
                    <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; text-align: center; border: 2px solid #e5e7eb; margin-bottom: 10px;">
                        <div style="font-size: 2rem; margin-bottom: 8px;">{calc_info.get('icon', '📊')}</div>
                        <div style="font-weight: bold; font-size: 1rem; margin-bottom: 5px;">{calc_info['name']}</div>
                        <div style="font-size: 0.85rem; color: #6b7280;">{calc_info.get('category', '')}</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button("▶️ Mở", key=f"search_result_{calc_id}", use_container_width=True):
                        from utils.state import add_to_recently_used
                        add_to_recently_used(calc_id)
                        page = calc_info.get('page', 'Scores')
                        page_path_map = {
                            'Scores': 'pages/01_📊_Scores.py',
                            'Critical Care': 'pages/09_🫁_Critical_Care.py',
                        }
                        page_path = page_path_map.get(page, 'pages/01_📊_Scores.py')
                        st.switch_page(page_path)
        else:
            st.warning(f"⚠️ Không tìm thấy công cụ hồi sức nào với từ khóa '{search_query}'. Thử từ khóa khác hoặc xem tất cả công cụ bên dưới.")
            st.markdown("---")
    
    # Quick Stats (optimized) - Only show if no search query
    if not search_query:
        st.markdown("---")
        st.markdown("### 📊 Thống kê nhanh")
        render_quick_stats()
    
    st.markdown("---")
    
    # Quick access cards - Enhanced with better styling
    st.markdown("### ⚡ Truy cập nhanh")
    st.caption("Click vào card để mở công cụ tương ứng")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_clickable_dashboard_card(
            title="Fluid Therapy",
            description="Dịch truyền & điện giải",
            icon="💧",
            gradient="linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
            action_key="critical_care_tool_selection",
            action_value="💧 Fluid Therapy",
            tooltip="Tính toán dịch truyền, bù dịch, và điều chỉnh điện giải"
        )
    
    with col2:
        render_clickable_dashboard_card(
            title="Vasopressors",
            description="Hướng dẫn liều",
            icon="💉",
            gradient="linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
            action_key="critical_care_tool_selection",
            action_value="💉 Vasopressors",
            tooltip="Hướng dẫn liều và titration vasopressor"
        )
    
    with col3:
        render_clickable_dashboard_card(
            title="Transfusion",
            description="Truyền máu",
            icon="🩸",
            gradient="linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)",
            action_key="critical_care_tool_selection",
            action_value="🩸 Transfusion",
            tooltip="Tính toán truyền máu và chế phẩm máu"
        )
    
    with col4:
        render_clickable_dashboard_card(
            title="Sedation",
            description="An thần & giảm đau",
            icon="💤",
            gradient="linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)",
            action_key="critical_care_tool_selection",
            action_value="💤 Sedation & Analgesia",
            tooltip="Giao thức an thần và giảm đau"
        )
    
    # Scoring systems - Enhanced (hide if searching)
    if not search_query:
        st.markdown("---")
        st.markdown("### 📊 Scoring Systems")
        st.caption("Click để mở hệ thống đánh giá")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="scoring-card" style="border-left-color: #667eea; margin-bottom: 10px;">
            <strong>📊 Đánh giá độ nặng:</strong><br>
            • APACHE II<br>
            • SOFA<br>
            • SAPS II
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Mở", key="scoring_severity", use_container_width=True, help="Mở hệ thống đánh giá độ nặng (APACHE II, SOFA, SAPS II)"):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.session_state['scoring_calc_to_open'] = 'apache2'  # Mở tab APACHE II (tab đầu tiên của severity)
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="scoring-card" style="border-left-color: #f5576c; margin-bottom: 10px;">
            <strong>🧠 Đánh giá thần kinh:</strong><br>
            • GCS<br>
            • RASS<br>
            • CAM-ICU
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧠 Mở", key="scoring_neuro", use_container_width=True, help="Mở hệ thống đánh giá thần kinh (GCS, RASS, CAM-ICU)"):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.session_state['scoring_calc_to_open'] = 'gcs'  # Mở tab GCS (tab đầu tiên của neurological)
            st.rerun()
    
    with col3:
        st.markdown("""
        <div class="scoring-card" style="border-left-color: #4facfe; margin-bottom: 10px;">
            <strong>🧪 Đánh giá thận:</strong><br>
            • AKI Staging (KDIGO)<br>
            • RIFLE
        </div>
        """, unsafe_allow_html=True)
        if st.button("🧪 Mở", key="scoring_renal", use_container_width=True, help="Mở hệ thống đánh giá thận (AKI Staging, RIFLE)"):
            st.session_state['critical_care_tool_selection'] = "📊 Scoring Systems"
            st.session_state['scoring_calc_to_open'] = 'aki'  # Mở tab AKI Staging
            st.rerun()
    
    # Clinical scenarios - Enhanced (hide if searching)
    if not search_query:
        st.markdown("---")
        st.markdown("### 🎯 Tình huống lâm sàng")
        st.caption("Click để mở protocol tương ứng")
    
    scenarios = [
        {
            "title": "Sepsis",
            "icon": "🦠",
            "description": "Quản lý nhiễm trùng huyết",
            "tool_value": "🦠 Sepsis Protocols",
            "color": "#667eea"
        },
        {
            "title": "ARDS",
            "icon": "🫁",
            "description": "Hội chứng suy hô hấp cấp",
            "tool_value": "🫁 ARDS Protocols",
            "color": "#f5576c"
        },
        {
            "title": "Shock",
            "icon": "💉",
            "description": "Sốc - Huyết động không ổn định",
            "tool_value": "💉 Shock Management",
            "color": "#4facfe"
        },
        {
            "title": "Delirium",
            "icon": "🧠",
            "description": "Mê sảng ở ICU",
            "tool_value": "📊 Scoring Systems",
            "color": "#43e97b"
        }
    ]
    
    cols = st.columns(4)
    for idx, scenario in enumerate(scenarios):
        with cols[idx]:
            st.markdown(f"""
            <div class="scenario-card" style="margin-bottom: 10px;">
                <div style="font-size: 2rem; margin-bottom: 5px;">{scenario['icon']}</div>
                <div style="font-weight: bold; margin-bottom: 5px;">{scenario['title']}</div>
                <div style="font-size: 0.85rem; color: #6b7280;">{scenario['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"{scenario['icon']} Mở", key=f"scenario_{scenario['title']}", use_container_width=True, help=f"Mở {scenario['title']} protocol"):
                st.session_state['critical_care_tool_selection'] = scenario['tool_value']
                st.rerun()
    
    # Recent calculations - Optimized with caching (hide if searching)
    if not search_query:
        st.markdown("---")
        st.markdown("### 🕐 Tính toán gần đây")
    
    recently_used = st.session_state.get('recently_used', [])
    if recently_used:
        # Use cached calculator list and set for faster lookup
        critical_care_calcs = set(get_critical_care_calculators())
        critical_care_recent = [calc for calc in recently_used if calc in critical_care_calcs]
        
        if critical_care_recent:
            # Limit to 5 most recent
            recent_to_show = critical_care_recent[:5]
            cols = st.columns(min(5, len(recent_to_show)))
            
            for idx, calc_id in enumerate(recent_to_show):
                if calc_id in ALL_CALCULATORS:
                    calc_info = ALL_CALCULATORS[calc_id]
                    with cols[idx]:
                        # Optimized: Single HTML block
                        st.markdown(f"""
                        <div style="padding: 15px; background: #f8f9fa; border-radius: 8px; text-align: center; border: 2px solid #e5e7eb; transition: all 0.2s ease;">
                            <div style="font-size: 1.5rem; margin-bottom: 5px;">{calc_info.get('icon', '📊')}</div>
                            <div style="font-weight: bold; font-size: 0.9rem; margin-bottom: 5px;">{calc_info['name']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button(f"▶️ Mở", key=f"recent_{calc_id}", use_container_width=True):
                            from utils.state import add_to_recently_used
                            add_to_recently_used(calc_id)
                            page = calc_info.get('page', 'Scores')
                            page_path_map = {
                                'Scores': 'pages/01_📊_Scores.py',
                                'Critical Care': 'pages/09_🫁_Critical_Care.py',
                            }
                            page_path = page_path_map.get(page, 'pages/01_📊_Scores.py')
                            st.switch_page(page_path)
        else:
            st.info("💡 Chưa có tính toán hồi sức gần đây. Bắt đầu sử dụng các công cụ để xem lịch sử ở đây!")
    else:
        st.info("💡 Chưa có lịch sử sử dụng. Bắt đầu dùng calculator để xem lịch sử ở đây!")
    
    st.markdown("---")
    
    # Quick tips - Enhanced with lazy loading
    st.markdown("### 💡 Mẹo sử dụng")
    
    # Cache tips list
    if 'dashboard_tips' not in st.session_state:
        st.session_state.dashboard_tips = [
            "💧 **Fluid Therapy:** Sử dụng Holliday-Segar cho maintenance, tính deficit cho hypernatremia",
            "💉 **Vasopressors:** Bắt đầu với Norepinephrine, theo dõi MAP và lactate",
            "🩸 **Transfusion:** Tuân thủ MTP protocol, theo dõi hemoglobin và coagulation",
            "💤 **Sedation:** Mục tiêu RASS -1 to -2 cho hầu hết bệnh nhân, đánh giá hàng ngày",
            "📊 **Scoring:** SOFA hàng ngày cho sepsis, APACHE II cho tiên lượng ICU",
            "🫁 **Ventilator:** ARDSNet protocol cho ARDS, theo dõi plateau pressure",
            "🦠 **Sepsis:** 3-hour bundle, theo dõi lactate và fluid responsiveness",
            "💉 **Shock:** Phân loại theo type (hypovolemic, cardiogenic, distributive, obstructive)"
        ]
    
    with st.expander("📚 Xem tất cả mẹo", expanded=False):
        for tip in st.session_state.dashboard_tips:
            st.markdown(f"- {tip}")
    
    # Keyboard shortcuts hint
    st.markdown("---")
    with st.expander("⌨️ Keyboard Shortcuts", expanded=False):
        st.markdown("""
        - **Ctrl+K** - Focus search
        - **Esc** - Clear search
        - **/** - Quick search
        - **1-4** - Quick access to first 4 tools (coming soon)
        """)
    
    # Performance info (dev mode only)
    if st.session_state.get('dev_mode', False):
        with st.expander("🔧 Performance Info", expanded=False):
            stats = get_critical_care_stats()
            st.json({
                'recent_count': stats['recent_count'],
                'favorites_count': stats['favorites_count'],
                'critical_care_used': stats['critical_care_used'],
                'cache_status': 'active' if 'dashboard_styles_injected' in st.session_state else 'inactive'
            })

