"""
Homepage Component for Doctors
Optimized for mobile-first, fast access to clinical tools
"""

import streamlit as st
from config.calculators import ALL_CALCULATORS
from utils.state import add_to_recently_used
from typing import List, Dict, Optional


def get_recent_items(max_items: int = 5) -> List[Dict]:
    """Get recently used items (calculators, drugs, protocols)"""
    recently_used = st.session_state.get('recently_used', [])
    items = []
    
    for calc_id in recently_used[:max_items]:
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            items.append({
                'id': calc_id,
                'name': calc_info.get('name', ''),
                'icon': calc_info.get('icon', '📊'),
                'category': calc_info.get('category', ''),
                'type': 'calculator',
                'page': calc_info.get('page', 'Scores')
            })
    
    return items


def get_favorite_items(max_items: int = 5) -> List[Dict]:
    """Get favorite items"""
    favorites = st.session_state.get('favorites', [])
    items = []
    
    for calc_id in favorites[:max_items]:
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            items.append({
                'id': calc_id,
                'name': calc_info.get('name', ''),
                'icon': calc_info.get('icon', '📊'),
                'category': calc_info.get('category', ''),
                'type': 'calculator',
                'page': calc_info.get('page', 'Scores')
            })
    
    return items


def get_specialty_recommendations(specialty: Optional[str] = None) -> List[Dict]:
    """Get recommended calculators/scores for a specialty"""
    # Default recommendations if no specialty specified
    default_recommendations = [
        'SOFA', 'APACHE', 'NEWS2', 'CHA2DS2VASc', 'ASCVD', 'eGFR', 'CrCl'
    ]
    
    # Specialty-specific recommendations
    specialty_map = {
        'ICU': ['SOFA', 'APACHE', 'GCS', 'RASS', 'CAM-ICU'],
        'Tim mạch': ['CHA2DS2VASc', 'HAS-BLED', 'ASCVD', 'HEART Score', 'TIMI'],
        'Hô hấp': ['CURB-65', 'BODE', 'GOLD', 'mMRC'],
        'Nhi': ['PIM', 'PRISM', 'PELOD', 'PIM2'],
        'Nội': ['NEWS2', 'qSOFA', 'Wells', 'PERC', 'D-Dimer']
    }
    
    recommendations = specialty_map.get(specialty, default_recommendations)
    items = []
    
    for rec_name in recommendations[:6]:
        # Find calculator by name
        for calc_id, calc_info in ALL_CALCULATORS.items():
            if calc_info.get('name', '').upper() == rec_name.upper():
                items.append({
                    'id': calc_id,
                    'name': calc_info.get('name', ''),
                    'icon': calc_info.get('icon', '📊'),
                    'category': calc_info.get('category', ''),
                    'type': 'calculator',
                    'page': calc_info.get('page', 'Scores')
                })
                break
    
    return items


def render_homepage_doctor():
    """Render optimized homepage for doctors"""
    
    # Initialize user specialty if not set
    if 'user_specialty' not in st.session_state:
        st.session_state.user_specialty = None
    
    # Get user's specialty preference
    specialty = st.session_state.get('user_specialty', None)
    
    # Header with greeting
    col_header1, col_header2 = st.columns([3, 1])
    
    with col_header1:
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <h1 style="font-size: 1.8rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.25rem;">
                Xin chào, BS. 👋
            </h1>
            <p style="color: var(--text-secondary); font-size: 0.95rem; margin: 0;">
                Tìm kiếm nhanh thuốc, thang điểm, guideline
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_header2:
        # Specialty selector dropdown (compact)
        specialties = [
            "Tất cả",
            "ICU",
            "Tim mạch", 
            "Hô hấp",
            "Nhi",
            "Nội",
            "Ngoại",
            "Sản",
            "Cấp cứu"
        ]
        
        current_specialty_idx = 0
        if specialty and specialty in specialties:
            current_specialty_idx = specialties.index(specialty)
        
        selected_specialty = st.selectbox(
            "Chuyên khoa",
            specialties,
            index=current_specialty_idx,
            key="homepage_specialty_selector",
            label_visibility="collapsed",
            help="Chọn chuyên khoa để xem đề xuất phù hợp"
        )
        
        # Update session state
        if selected_specialty != "Tất cả":
            st.session_state.user_specialty = selected_specialty
        else:
            st.session_state.user_specialty = None
        
        # Profile/avatar placeholder (smaller on mobile)
        st.markdown("""
        <div style="text-align: right; margin-top: 0.5rem;">
            <div style="width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        display: inline-flex; align-items: center; justify-content: center; font-size: 1.2rem; color: white;
                        cursor: pointer;" onclick="document.querySelector('[data-testid=\\'stSidebar\\']').click()">
                👨‍⚕️
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Large Search Bar (Hero Section)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2D7DF6 0%, #1976d2 100%); 
                padding: 1.5rem; 
                border-radius: 16px; 
                margin-bottom: 1.5rem;
                box-shadow: 0 4px 12px rgba(45, 125, 246, 0.2);">
        <div style="color: white; text-align: center;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🔍</div>
            <h2 style="color: white; margin-bottom: 0.5rem; font-size: 1.3rem;">Tìm kiếm nhanh</h2>
            <p style="color: rgba(255,255,255,0.9); margin: 0; font-size: 0.9rem;">
                Nhấn <kbd style="background: rgba(255,255,255,0.2); padding: 4px 8px; border-radius: 4px; border: none;">Ctrl+K</kbd> để focus
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Search component (will be rendered by app.py)
    # This is just a placeholder - actual search is handled in app.py
    
    st.markdown("---")
    
    # Recently Used Section
    recent_items = get_recent_items(max_items=5)
    if recent_items:
        st.markdown("### 🕐 Bạn vừa tra cứu")
        st.caption("Các công cụ bạn đã sử dụng gần đây")
        
        # Horizontal scrollable list
        cols = st.columns(min(5, len(recent_items)))
        for idx, item in enumerate(recent_items[:5]):
            with cols[idx]:
                page_path_map = {
                    'Scores': 'pages/01_📊_Scores.py',
                    'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                    'Drugs': 'pages/07_💊_Drug_Database.py',
                    'Protocols': 'pages/04_📋_Protocols.py',
                    'Critical Care': 'pages/09_🫁_Critical_Care.py',
                }
                page_path = page_path_map.get(item['page'], 'pages/01_📊_Scores.py')
                
                st.markdown(f"""
                <div class="recent-item-card" style="
                    background: var(--card-bg);
                    border: 1px solid var(--border);
                    border-radius: 12px;
                    padding: 12px;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    box-shadow: 0 2px 4px var(--shadow);
                " onclick="window.location.href='{page_path}'">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{item['icon']}</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: var(--text-primary); margin-bottom: 0.25rem;">
                        {item['name'][:15]}{'...' if len(item['name']) > 15 else ''}
                    </div>
                    <div style="font-size: 0.7rem; color: var(--text-secondary);">
                        {item['category'][:12]}{'...' if len(item['category']) > 12 else ''}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Quick Actions Bar (if there are favorites)
    favorite_items = get_favorite_items(max_items=3)
    if favorite_items:
        st.markdown("### ⭐ Yêu thích của bạn")
        st.caption("Truy cập nhanh các công cụ bạn hay dùng")
        
        fav_cols = st.columns(min(3, len(favorite_items)))
        for idx, item in enumerate(favorite_items[:3]):
            with fav_cols[idx]:
                page_path_map = {
                    'Scores': 'pages/01_📊_Scores.py',
                    'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                    'Drugs': 'pages/07_💊_Drug_Database.py',
                    'Protocols': 'pages/04_📋_Protocols.py',
                }
                page_path = page_path_map.get(item['page'], 'pages/01_📊_Scores.py')
                
                st.markdown(f"""
                <div class="favorite-quick-card" style="
                    background: linear-gradient(135deg, #fff9e6 0%, #fff5cc 100%);
                    border: 1px solid #ffd54f;
                    border-radius: 12px;
                    padding: 1rem;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    box-shadow: 0 2px 6px rgba(255, 213, 79, 0.3);
                " onclick="window.location.href='{page_path}'">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{item['icon']}</div>
                    <div style="font-size: 0.9rem; font-weight: 600; color: #1B2430; margin-bottom: 0.25rem;">
                        {item['name'][:12]}{'...' if len(item['name']) > 12 else ''}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
    
    # Quick Access Shortcuts (2x2 Grid)
    st.markdown("### ⚡ Truy cập nhanh")
    st.caption("Các công cụ chính trong 1 tap")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Thuốc
        st.markdown("""
        <div class="shortcut-card" style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            color: white;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
            margin-bottom: 1rem;
        " onclick="window.location.href='/pages/07_💊_Drug_Database.py'">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">💊</div>
            <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.25rem;">Thuốc</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Tra cứu thuốc & liều dùng</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Guideline
        st.markdown("""
        <div class="shortcut-card" style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            color: white;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(245, 87, 108, 0.3);
        " onclick="window.location.href='/pages/04_📋_Protocols.py'">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">📋</div>
            <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.25rem;">Guideline</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Phác đồ điều trị</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Thang điểm
        st.markdown("""
        <div class="shortcut-card" style="
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            color: white;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(79, 172, 254, 0.3);
            margin-bottom: 1rem;
        " onclick="window.location.href='/pages/01_📊_Scores.py'">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">📊</div>
            <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.25rem;">Thang điểm</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Tính score & công cụ</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Tương tác thuốc
        st.markdown("""
        <div class="shortcut-card" style="
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            color: white;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(250, 112, 154, 0.3);
        " onclick="window.location.href='/pages/07_💊_Drug_Database.py'">
            <div style="font-size: 3rem; margin-bottom: 0.5rem;">⚗️</div>
            <div style="font-size: 1.1rem; font-weight: 700; margin-bottom: 0.25rem;">Tương tác</div>
            <div style="font-size: 0.85rem; opacity: 0.9;">Tương tác thuốc</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Specialty Recommendations
    if specialty:
        specialty_name = specialty
        recommendations = get_specialty_recommendations(specialty)
        
        if recommendations:
            st.markdown(f"### ⭐ Thường dùng trong {specialty_name}")
            st.caption("Các công cụ được đề xuất cho chuyên khoa của bạn")
            
            # Display recommendations in cards
            num_cols = min(3, len(recommendations))
            cols = st.columns(num_cols)
            
            for idx, item in enumerate(recommendations[:6]):
                with cols[idx % num_cols]:
                    page_path_map = {
                        'Scores': 'pages/01_📊_Scores.py',
                        'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                        'Drugs': 'pages/07_💊_Drug_Database.py',
                        'Protocols': 'pages/04_📋_Protocols.py',
                    }
                    page_path = page_path_map.get(item['page'], 'pages/01_📊_Scores.py')
                    
                    st.markdown(f"""
                    <div class="recommendation-card" style="
                        background: var(--card-bg);
                        border: 1px solid var(--border);
                        border-radius: 12px;
                        padding: 1rem;
                        cursor: pointer;
                        transition: all 0.2s ease;
                        box-shadow: 0 2px 4px var(--shadow);
                        margin-bottom: 0.75rem;
                    " onclick="window.location.href='{page_path}'">
                        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">{item['icon']}</div>
                        <div style="font-size: 0.95rem; font-weight: 600; color: var(--text-primary); margin-bottom: 0.25rem;">
                            {item['name']}
                        </div>
                        <div style="font-size: 0.75rem; color: var(--text-secondary);">
                            {item['category']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
    
    # Add CSS for hover effects and smooth animations
    st.markdown("""
    <style>
    /* Smooth hover effects */
    .recent-item-card:hover, .shortcut-card:hover, .recommendation-card:hover,
    .favorite-quick-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px var(--shadow-hover) !important;
    }
    
    /* Active/press effect for mobile */
    .recent-item-card:active, .shortcut-card:active, .recommendation-card:active,
    .favorite-quick-card:active {
        transform: scale(0.98) translateY(0);
        transition: transform 0.1s ease;
    }
    
    /* Smooth transitions */
    .recent-item-card, .shortcut-card, .recommendation-card,
    .favorite-quick-card {
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        will-change: transform, box-shadow;
    }
    
    /* Mobile optimizations */
    @media (max-width: 768px) {
        .recent-item-card, .shortcut-card, .recommendation-card {
            min-height: 48px; /* Touch-friendly */
            -webkit-tap-highlight-color: rgba(45, 125, 246, 0.1);
        }
        
        /* Remove hover effects on touch devices */
        @media (hover: none) {
            .recent-item-card:hover, .shortcut-card:hover, .recommendation-card:hover {
                transform: none;
            }
        }
    }
    
    /* Loading animation for cards */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .recent-item-card, .shortcut-card, .recommendation-card,
    .favorite-quick-card {
        animation: fadeInUp 0.3s ease-out;
    }
    
    /* Stagger animation for cards */
    .recent-item-card:nth-child(1) { animation-delay: 0.05s; }
    .recent-item-card:nth-child(2) { animation-delay: 0.1s; }
    .recent-item-card:nth-child(3) { animation-delay: 0.15s; }
    .recent-item-card:nth-child(4) { animation-delay: 0.2s; }
    .recent-item-card:nth-child(5) { animation-delay: 0.25s; }
    </style>
    """, unsafe_allow_html=True)

