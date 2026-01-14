"""
Scores UI View Component
Modern UI components for displaying calculators with cards, filters, and navigation
"""

import streamlit as st
from typing import List, Dict, Optional
from scores.config import SCORES_BY_SPECIALTY
from scores.specialty_groups import (
    get_all_groups,
    get_specialties_in_group,
    get_group_for_specialty
)


def is_daily_use(info: dict) -> bool:
    """Check if calculator is marked as daily use"""
    desc = info.get("desc", "") or ""
    return "DÙNG HÀNG NGÀY" in desc or "⭐" in desc


def render_calculator_card(score_id: str, score_info: dict, specialty: str, key_prefix: str = ""):
    """Render a single calculator card with mobile optimization"""
    
    import streamlit as st
    
    # Determine badges
    badges = []
    if is_daily_use(score_info):
        badges.append("⭐ Daily Use")
    if "🆕" in score_info.get("name", "") or "MỚI" in score_info.get("desc", ""):
        badges.append("🆕 New")
    if "⭐⭐⭐" in score_info.get("name", "") or "⭐⭐⭐" in score_info.get("desc", ""):
        badges.append("🔥 Important")
    
    status = score_info.get("status", "✅")
    
    # Extract icon from specialty name (first emoji)
    specialty_icon = "📊"
    if specialty:
        # Try to extract emoji from specialty name
        import re
        emoji_match = re.search(r'[\U0001F300-\U0001F9FF]', specialty)
        if emoji_match:
            specialty_icon = emoji_match.group()
    
    # Mobile-optimized card CSS
    st.markdown("""
    <style>
    .calculator-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.2s;
    }
    @media (max-width: 768px) {
        .calculator-card {
            padding: 12px;
            margin-bottom: 1rem;
        }
        .calculator-card h4 {
            font-size: 1em !important;
        }
        .calculator-card p {
            font-size: 0.8em !important;
        }
        .calculator-card .icon {
            font-size: 1.5em !important;
        }
    }
    @media (hover: hover) {
        .calculator-card:hover {
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
            transform: translateY(-2px);
        }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Defensive check: ensure score_info fields are strings
    score_name = str(score_info.get('name', score_id)) if score_info.get('name') is not None else str(score_id)
    score_desc = str(score_info.get('desc', '')) if score_info.get('desc') is not None else ''
    if len(score_desc) > 100:
        score_desc = score_desc[:100] + "..."
    
    # Card container
    with st.container():
        # Card HTML
        card_html = f"""
        <div class="calculator-card">
            <div style='display: flex; align-items: start; gap: 12px; margin-bottom: 8px;'>
                <div class="icon" style='font-size: 2em; flex-shrink: 0;'>{specialty_icon}</div>
                <div style='flex: 1; min-width: 0;'>
                    <h4 style='margin: 0 0 4px 0; color: #212121; font-size: 1.1em; font-weight: 600; word-wrap: break-word;'>{score_name}</h4>
                    <p style='margin: 0; color: #666; font-size: 0.85em; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;'>{score_desc}</p>
                </div>
            </div>
            <div style='display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px;'>
                <span style='background: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 12px; font-size: 0.7em; font-weight: 500;'>{status}</span>
        """
        
        for badge in badges:
            if "Daily Use" in badge:
                card_html += '<span style="background: #fff3e0; color: #f57c00; padding: 2px 8px; border-radius: 12px; font-size: 0.7em; font-weight: 500;">⭐ Daily Use</span>'
            elif "New" in badge:
                card_html += '<span style="background: #e8f5e9; color: #2e7d32; padding: 2px 8px; border-radius: 12px; font-size: 0.7em; font-weight: 500;">🆕 New</span>'
            elif "Important" in badge:
                card_html += '<span style="background: #ffebee; color: #c62828; padding: 2px 8px; border-radius: 12px; font-size: 0.7em; font-weight: 500;">🔥 Important</span>'
        
        card_html += "</div></div>"
        
        st.markdown(card_html, unsafe_allow_html=True)
        
        # Button to use calculator - mobile optimized
        button_key = f"{key_prefix}_use_{score_id}_{specialty}"
        button_text = "▶️ Use" if len(score_name) > 20 else f"▶️ {score_name[:15]}..."
        
        if st.button(button_text, key=button_key, use_container_width=True):
            # Store selection and rerun
            st.session_state.selected_score_id = score_id
            st.session_state.selected_specialty = specialty
            
            # Track recent
            try:
                from components.scores_recent import add_to_recent
                add_to_recent(specialty, score_id, score_name)
            except ImportError:
                pass
            
            st.rerun()


def render_specialty_group(group_id: str, group_info: dict, specialty_grouping: Dict):
    """Render a specialty group with calculators"""
    
    specialties_in_group = get_specialties_in_group(group_id)
    
    # Get all calculators in this group
    all_calculators = []
    for specialty in specialties_in_group:
        if specialty in SCORES_BY_SPECIALTY:
            for score_id, score_info in SCORES_BY_SPECIALTY[specialty].items():
                all_calculators.append({
                    "specialty": specialty,
                    "score_id": score_id,
                    "score_info": score_info
                })
    
    if not all_calculators:
        return
    
    # Defensive check: ensure icon and name are strings
    group_icon = str(group_info.get('icon', '📁')) if group_info.get('icon') is not None else "📁"
    group_name = str(group_info.get('name', 'Category')) if group_info.get('name') is not None else "Category"
    
    # Safely format the expander label
    expander_label = f"{group_icon} **{group_name}** ({len(all_calculators)} calculators)"
    
    # Render group header
    # Note: `st.expander` does not support `key` in some Streamlit versions,
    # so we avoid passing a key here to prevent TypeError.
    with st.expander(
        expander_label,
        expanded=group_info.get("default_expanded", False),
    ):
        st.caption(group_info.get("description", ""))
        
        # Render calculators in grid
        # Responsive columns: 1 on mobile, 2 on tablet, 3 on desktop
        # Use CSS to handle responsive layout
        st.markdown("""
        <style>
        @media (max-width: 768px) {
            .calculator-grid {
                display: grid;
                grid-template-columns: 1fr;
                gap: 1rem;
            }
        }
        @media (min-width: 769px) and (max-width: 1024px) {
            .calculator-grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 1rem;
            }
        }
        @media (min-width: 1025px) {
            .calculator-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Calculate number of columns based on screen size (fallback)
        num_cols = 3  # Default for desktop
        
        for i in range(0, len(all_calculators), num_cols):
            cols = st.columns(num_cols)
            for j, col in enumerate(cols):
                if i + j < len(all_calculators):
                    calc = all_calculators[i + j]
                    with col:
                        render_calculator_card(
                            calc["score_id"],
                            calc["score_info"],
                            calc["specialty"],
                            key_prefix=f"{group_id}_{calc['score_id']}"
                        )


def render_quick_access_section():
    """Render quick access section (Most Used, Recent, Favorites)"""
    
    import streamlit as st
    
    tab1, tab2, tab3 = st.tabs(["⭐ Most Used", "🕐 Recent", "❤️ Favorites"])
    
    with tab1:
        st.info("💡 Most used calculators based on usage statistics")
        # Get calculators marked as "Daily Use"
        daily_use_calcs = []
        for specialty, scores in SCORES_BY_SPECIALTY.items():
            for score_id, score_info in scores.items():
                if is_daily_use(score_info):
                    daily_use_calcs.append({
                        "specialty": specialty,
                        "score_id": score_id,
                        "score_info": score_info
                    })
        
        if daily_use_calcs:
            # Display in grid
            num_cols = 3
            for i in range(0, min(len(daily_use_calcs), 12), num_cols):
                cols = st.columns(num_cols)
                for j, col in enumerate(cols):
                    if i + j < len(daily_use_calcs):
                        calc = daily_use_calcs[i + j]
                        with col:
                            render_calculator_card(
                                calc["score_id"],
                                calc["score_info"],
                                calc["specialty"],
                                key_prefix=f"most_used_{calc['score_id']}"
                            )
        else:
            st.info("No daily use calculators found")
    
    with tab2:
        st.info("💡 Recently viewed calculators")
        try:
            from components.scores_recent import get_recent_calculators
            recent_list = get_recent_calculators(10)
            
            if recent_list:
                num_cols = 3
                for i in range(0, len(recent_list), num_cols):
                    cols = st.columns(num_cols)
                    for j, col in enumerate(cols):
                        if i + j < len(recent_list):
                            calc_info = recent_list[i + j]
                            specialty_name = calc_info.get('specialty', '')
                            score_id = calc_info.get('score_id', '')
                            
                            # Find calculator info
                            if specialty_name in SCORES_BY_SPECIALTY and score_id in SCORES_BY_SPECIALTY[specialty_name]:
                                score_info = SCORES_BY_SPECIALTY[specialty_name][score_id]
                                with col:
                                    render_calculator_card(
                                        score_id,
                                        score_info,
                                        specialty_name,
                                        key_prefix=f"recent_{score_id}"
                                    )
                            else:
                                with col:
                                    st.markdown(f"• {calc_info.get('name', 'Unknown')}")
            else:
                st.info("No recent calculators. Start using calculators to see them here.")
        except ImportError:
            st.info("Recent tracking chưa được kích hoạt.")
    
    with tab3:
        st.info("💡 Your favorite calculators")
        # Use favorites from existing component
        from components.scores_favorites import get_favorite_scores
        favorites = get_favorite_scores()
        
        if favorites:
            favorite_calcs = []
            for specialty_name, score_id in favorites:
                if specialty_name in SCORES_BY_SPECIALTY and score_id in SCORES_BY_SPECIALTY[specialty_name]:
                    favorite_calcs.append({
                        "specialty": specialty_name,
                        "score_id": score_id,
                        "score_info": SCORES_BY_SPECIALTY[specialty_name][score_id]
                    })
            
            if favorite_calcs:
                num_cols = 3
                for i in range(0, len(favorite_calcs), num_cols):
                    cols = st.columns(num_cols)
                    for j, col in enumerate(cols):
                        if i + j < len(favorite_calcs):
                            calc = favorite_calcs[i + j]
                            with col:
                                render_calculator_card(
                                    calc["score_id"],
                                    calc["score_info"],
                                    calc["specialty"],
                                    key_prefix=f"favorite_{calc['score_id']}"
                                )
            else:
                st.info("No favorite calculators yet. Click the ⭐ button on any calculator to add it to favorites.")
        else:
            st.info("No favorite calculators yet. Click the ⭐ button on any calculator to add it to favorites.")


def render_filters_sidebar():
    """Render enhanced filters sidebar"""
    
    st.markdown("### 🔧 Filters")
    
    # By Status
    filter_status = st.multiselect(
        "Status:",
        ["✅", "🚧", "📋"],
        default=["✅"],
        key="filter_status_enhanced"
    )
    
    # By Usage
    filter_usage = st.multiselect(
        "Usage:",
        ["⭐ Daily Use", "🆕 New", "🔥 Popular"],
        default=[],
        key="filter_usage"
    )
    
    # By Category (if we have this data)
    filter_category = st.multiselect(
        "Category:",
        ["Risk Scores", "Severity Scores", "Prognostic Scores", "Diagnostic Scores"],
        default=[],
        key="filter_category"
    )
    
    return {
        "status": filter_status,
        "usage": filter_usage,
        "category": filter_category
    }


def filter_calculators(calculators: List[Dict], filters: dict) -> List[Dict]:
    """Filter calculators based on filter criteria"""
    
    results = calculators
    
    # Status filter
    if filters.get("status"):
        results = [c for c in results if c["score_info"].get("status") in filters["status"]]
    
    # Usage filter
    if filters.get("usage"):
        filtered_results = []
        for calc in results:
            score_info = calc["score_info"]
            if "⭐ Daily Use" in filters["usage"] and is_daily_use(score_info):
                filtered_results.append(calc)
            elif "🆕 New" in filters["usage"] and ("🆕" in score_info.get("name", "") or "MỚI" in score_info.get("desc", "")):
                filtered_results.append(calc)
            elif "🔥 Popular" in filters["usage"] and "⭐⭐⭐" in score_info.get("name", ""):
                filtered_results.append(calc)
        
        if filtered_results:
            results = filtered_results
    
    return results
