"""
Main Menu Personalized Recommendations Component
Recommend calculators based on usage, profile, time, and similar calculators
"""

import streamlit as st
from datetime import datetime
from config.calculators import ALL_CALCULATORS
from config.user_profile import get_current_profile


def get_recommendations_based_on_usage(max_items: int = 6):
    """Get recommendations based on usage patterns"""
    usage_stats = st.session_state.get('usage_stats', {})
    calculations_by_calc = usage_stats.get('calculations_by_calculator', {})
    calculations_by_category = usage_stats.get('calculations_by_category', {})
    
    recommendations = []
    
    # If user has used calculators, recommend similar ones from same category
    if calculations_by_category:
        # Find most used category
        top_category = max(calculations_by_category.items(), key=lambda x: x[1])[0]
        
        # Find calculators in that category that haven't been used
        used_calc_ids = set(calculations_by_calc.keys())
        for calc_id, calc_info in ALL_CALCULATORS.items():
            if calc_id not in used_calc_ids:
                if calc_info.get('category', '') == top_category:
                    recommendations.append({
                        'id': calc_id,
                        'name': calc_info.get('name', ''),
                        'icon': calc_info.get('icon', '📊'),
                        'category': calc_info.get('category', ''),
                        'page': calc_info.get('page', 'Scores'),
                        'reason': f'Cùng nhóm với {top_category}'
                    })
                    if len(recommendations) >= max_items:
                        break
    
    return recommendations


def get_recommendations_based_on_profile(max_items: int = 6):
    """Get recommendations based on user profile (Nội/ICU)"""
    profile = get_current_profile()
    
    recommendations = []
    
    if profile == "icu":
        # ICU profile: recommend critical care calculators
        icu_calculators = ['sofa', 'gcs', 'qsofa', 'apache2', 'saps2', 'sirs']
        for calc_id in icu_calculators[:max_items]:
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                recommendations.append({
                    'id': calc_id,
                    'name': calc_info.get('name', ''),
                    'icon': calc_info.get('icon', '📊'),
                    'category': calc_info.get('category', ''),
                    'page': calc_info.get('page', 'Scores'),
                    'reason': 'Phù hợp với ICU'
                })
    else:
        # Nội profile: recommend internal medicine calculators
        noi_calculators = ['ascvd', 'cha2ds2vasc', 'hasbled', 'grace', 'timi', 'heart']
        for calc_id in noi_calculators[:max_items]:
            if calc_id in ALL_CALCULATORS:
                calc_info = ALL_CALCULATORS[calc_id]
                recommendations.append({
                    'id': calc_id,
                    'name': calc_info.get('name', ''),
                    'icon': calc_info.get('icon', '📊'),
                    'category': calc_info.get('category', ''),
                    'page': calc_info.get('page', 'Scores'),
                    'reason': 'Phù hợp với Nội khoa'
                })
    
    return recommendations


def get_recommendations_based_on_time(max_items: int = 6):
    """Get recommendations based on time of day"""
    current_hour = datetime.now().hour
    
    recommendations = []
    
    if 5 <= current_hour < 12:
        # Morning: recommend common screening/assessment tools
        morning_calcs = ['ascvd', 'cha2ds2vasc', 'frailty', 'mna']
    elif 12 <= current_hour < 18:
        # Afternoon: recommend diagnostic/decision tools
        afternoon_calcs = ['grace', 'timi', 'heart', 'wells']
    else:
        # Evening/Night: recommend emergency/critical care tools
        evening_calcs = ['sofa', 'gcs', 'qsofa', 'sirs']
    
    calc_list = locals().get(f"{['morning', 'afternoon', 'evening'][current_hour // 6]}_calcs", [])
    
    for calc_id in calc_list[:max_items]:
        if calc_id in ALL_CALCULATORS:
            calc_info = ALL_CALCULATORS[calc_id]
            recommendations.append({
                'id': calc_id,
                'name': calc_info.get('name', ''),
                'icon': calc_info.get('icon', '📊'),
                'category': calc_info.get('category', ''),
                'page': calc_info.get('page', 'Scores'),
                'reason': 'Phù hợp thời điểm'
            })
    
    return recommendations


def get_similar_calculators(calc_id: str, max_items: int = 4):
    """Get calculators similar to the given one"""
    if calc_id not in ALL_CALCULATORS:
        return []
    
    target_calc = ALL_CALCULATORS[calc_id]
    target_category = target_calc.get('category', '')
    
    similar = []
    for cid, cinfo in ALL_CALCULATORS.items():
        if cid != calc_id and cinfo.get('category', '') == target_category:
            similar.append({
                'id': cid,
                'name': cinfo.get('name', ''),
                'icon': cinfo.get('icon', '📊'),
                'category': cinfo.get('category', ''),
                'page': cinfo.get('page', 'Scores'),
                'reason': f'Cùng nhóm với {target_calc.get("name", "")}'
            })
            if len(similar) >= max_items:
                break
    
    return similar


def render_recommendations(max_items: int = 6):
    """Render personalized recommendations section"""
    st.markdown("### 💡 Gợi ý cho bạn")
    
    # Get recommendations from different sources
    usage_recs = get_recommendations_based_on_usage(max_items // 2)
    profile_recs = get_recommendations_based_on_profile(max_items // 2)
    time_recs = get_recommendations_based_on_time(max_items // 3)
    
    # Combine and deduplicate
    all_recs = {}
    for rec in usage_recs + profile_recs + time_recs:
        if rec['id'] not in all_recs:
            all_recs[rec['id']] = rec
    
    recommendations = list(all_recs.values())[:max_items]
    
    # Filter out already favorited
    favorites = st.session_state.get('favorites', [])
    recommendations = [r for r in recommendations if r['id'] not in favorites]
    
    if recommendations:
        st.caption("Dựa trên cách bạn sử dụng và chuyên khoa của bạn")
        
        # Display as grid
        num_cols = min(3, len(recommendations))
        cols = st.columns(num_cols)
        
        for idx, rec in enumerate(recommendations[:max_items]):
            with cols[idx % num_cols]:
                st.markdown(
                    f"""
                    <div class="calculator-card" style="text-align: center; padding: 20px; margin-bottom: 12px;">
                        <div style="font-size: 3rem; margin-bottom: 8px;">{rec['icon']}</div>
                        <div style="font-weight: 600; font-size: 1rem; margin-bottom: 4px; color: var(--text-primary);">
                            {rec['name']}
                        </div>
                        <div style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 8px;">
                            {rec['category']}
                        </div>
                        <div style="font-size: 0.75rem; color: var(--text-secondary); font-style: italic;">
                            {rec.get('reason', '')}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                page_path_map = {
                    'Scores': 'pages/01_📊_Scores.py',
                    'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                    'Drugs': 'pages/07_💊_Drug_Database.py',
                    'Protocols': 'pages/04_📋_Protocols.py',
                }
                page_path = page_path_map.get(rec['page'], 'pages/01_📊_Scores.py')
                
                if st.button(f"Mở {rec['name'][:15]}", key=f"rec_{rec['id']}", use_container_width=True, type="primary"):
                    st.session_state['preset_calculator'] = rec['id']
                    st.session_state['switch_to_scores'] = True
                    st.rerun()
    else:
        st.info("""
        **Chưa có gợi ý**
        
        Bắt đầu sử dụng calculators để nhận gợi ý cá nhân hóa!
        """)


def render_you_might_also_like(calc_id: str = None):
    """Render 'You might also like' section for a specific calculator"""
    if not calc_id:
        # Use most recently used calculator
        recently_used = st.session_state.get('recently_used', [])
        if not recently_used:
            return
        calc_id = recently_used[0]
    
    similar = get_similar_calculators(calc_id, max_items=4)
    
    if similar:
        st.markdown("#### Bạn có thể cũng thích")
        cols = st.columns(min(4, len(similar)))
        
        for idx, rec in enumerate(similar):
            with cols[idx]:
                st.markdown(
                    f"""
                    <div style="text-align: center; padding: 16px; border: 1px solid var(--border-color); border-radius: 8px;">
                        <div style="font-size: 2.5rem; margin-bottom: 8px;">{rec['icon']}</div>
                        <div style="font-weight: 600; font-size: 0.9rem; margin-bottom: 4px;">
                            {rec['name']}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                page_path_map = {
                    'Scores': 'pages/01_📊_Scores.py',
                    'Labs': 'pages/05_🔬_Labs_and_Calculators.py',
                    'Drugs': 'pages/07_💊_Drug_Database.py',
                    'Protocols': 'pages/04_📋_Protocols.py',
                }
                page_path = page_path_map.get(rec['page'], 'pages/01_📊_Scores.py')
                
                if st.button("Mở", key=f"similar_{rec['id']}", use_container_width=True):
                    st.session_state['preset_calculator'] = rec['id']
                    st.session_state['switch_to_scores'] = True
                    st.rerun()
