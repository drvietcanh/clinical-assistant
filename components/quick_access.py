"""
Quick Access Menu - Fast navigation to frequently used features
Add to sidebar for easy access
"""

import streamlit as st
from config.app_config import get_module_info
from config.user_profile import get_current_profile


def _get_module(module_id: str):
    """Safely get module info, returning None on error."""
    try:
        return get_module_info(module_id)
    except Exception:
        return None


def render_quick_access_menu():
    """
    Render quick access menu in sidebar
    Provides shortcuts to most used features, customized by profile (Nội / ICU)
    """
    st.markdown("### ⚡ Quick Access")

    profile = get_current_profile()  # "noi" or "icu"

    # -------- Clinical tools (Scores, Labs, Critical care, Protocols, Drug DB) --------
    with st.expander("🩺 Clinical Tools", expanded=False):
        col1, col2 = st.columns(2)

        scores = _get_module("scores")
        labs = _get_module("labs")
        critical = _get_module("critical_care")
        protocols = _get_module("protocols")
        decision = _get_module("phase2_features")
        drug_db = _get_module("drug_database")
        tdm = _get_module("tdm")
        antibiotics = _get_module("antibiotics")
        icu_bundles = _get_module("icu_bundles")  # optional, if added to APP_CONFIG

        if profile == "icu":
            # ICU: ưu tiên Hồi sức, Sepsis bundle, Scores ICU, Labs
            with col1:
                if critical and st.button(
                    f"{critical.icon} {critical.title}", use_container_width=True, key="qa_critical"
                ):
                    st.switch_page(critical.page_path)
                if scores and st.button(
                    f"{scores.icon} {scores.title}", use_container_width=True, key="qa_scores_icu"
                ):
                    st.switch_page(scores.page_path)
                if labs and st.button(
                    f"{labs.icon} {labs.title}", use_container_width=True, key="qa_labs_icu"
                ):
                    st.switch_page(labs.page_path)

            with col2:
                if icu_bundles and st.button(
                    f"🧵 Bundles ICU", use_container_width=True, key="qa_icu_bundles"
                ):
                    st.switch_page(icu_bundles.page_path)
                if protocols and st.button(
                    f"{protocols.icon} {protocols.title}",
                    use_container_width=True,
                    key="qa_protocols_icu",
                ):
                    st.switch_page(protocols.page_path)
                if antibiotics and st.button(
                    f"{antibiotics.icon} Kháng sinh",
                    use_container_width=True,
                    key="qa_antibiotics_icu",
                ):
                    st.switch_page(antibiotics.page_path)
                if tdm and st.button(
                    f"{tdm.icon} {tdm.title}", use_container_width=True, key="qa_tdm_icu"
                ):
                    st.switch_page(tdm.page_path)
        else:
            # Nội: ưu tiên Scores nội khoa, Drug DB, Decision Support, Labs
            with col1:
                if scores and st.button(
                    f"{scores.icon} {scores.title}", use_container_width=True, key="qa_scores_noi"
                ):
                    st.switch_page(scores.page_path)
                if drug_db and st.button(
                    f"{drug_db.icon} {drug_db.title}", use_container_width=True, key="qa_drugs_noi"
                ):
                    st.switch_page(drug_db.page_path)
                if labs and st.button(
                    f"{labs.icon} {labs.title}", use_container_width=True, key="qa_labs_noi"
                ):
                    st.switch_page(labs.page_path)

            with col2:
                if decision and st.button(
                    f"{decision.icon} {decision.title}",
                    use_container_width=True,
                    key="qa_decision_noi",
                ):
                    st.switch_page(decision.page_path)
                if protocols and st.button(
                    f"{protocols.icon} {protocols.title}",
                    use_container_width=True,
                    key="qa_protocols_noi",
                ):
                    st.switch_page(protocols.page_path)
                if critical and st.button(
                    f"{critical.icon} {critical.title}",
                    use_container_width=True,
                    key="qa_critical_noi",
                ):
                    st.switch_page(critical.page_path)

    # -------- Information resources (Diagnosis, Guidelines, ICD, Articles, Patient education) --------
    with st.expander("📚 Reference & Knowledge", expanded=False):
        guidelines = _get_module("guidelines_tracker")
        diagnosis = _get_module("diagnosis")
        disease_ency = _get_module("disease_encyclopedia")
        icd10 = _get_module("icd10_lookup")
        articles = _get_module("in_depth_articles")
        patient_edu = _get_module("patient_education")

        # Nội: nhấn mạnh tim mạch, nội tiết, bệnh mạn (Diagnosis + Articles)
        # ICU: nhấn mạnh Critical Care guidelines & disease encyclopedia
        order = []
        if profile == "icu":
            order = [guidelines, diagnosis, disease_ency, icd10, articles, patient_edu]
        else:
            order = [diagnosis, guidelines, icd10, disease_ency, articles, patient_edu]

        for idx, module in enumerate(order):
            if not module:
                continue
            key = f"qa_ref_{idx}_{module.id}"
            if st.button(f"{module.icon} {module.title}", use_container_width=True, key=key):
                st.switch_page(module.page_path)

    # -------- Utilities & system tools --------
    with st.expander("🔧 Utilities & System", expanded=False):
        global_search = _get_module("global_search")
        settings = _get_module("settings")
        analytics = _get_module("analytics")
        ai_assistant = _get_module("ai_assistant")

        if global_search and st.button(
            f"{global_search.icon} Global Search", use_container_width=True, key="qa_search"
        ):
            st.switch_page(global_search.page_path)
        if ai_assistant and st.button(
            f"{ai_assistant.icon} {ai_assistant.title}",
            use_container_width=True,
            key="qa_ai",
        ):
            st.switch_page(ai_assistant.page_path)
        if settings and st.button(
            f"{settings.icon} {settings.title}", use_container_width=True, key="qa_settings"
        ):
            st.switch_page(settings.page_path)
        if analytics and st.button(
            f"{analytics.icon} {analytics.title}", use_container_width=True, key="qa_analytics"
        ):
            st.switch_page(analytics.page_path)


def render_recent_items():
    """
    Render recent items in sidebar
    Shows last accessed pages/items
    """
    st.markdown("### 🕐 Recent")
    
    # Initialize recent items in session state
    if 'recent_items' not in st.session_state:
        st.session_state.recent_items = []
    
    if st.session_state.recent_items:
        for item in st.session_state.recent_items[-5:]:  # Show last 5
            st.caption(f"• {item}")
    else:
        st.caption("No recent items")


def render_favorites():
    """
    Render favorites in sidebar
    Shows bookmarked items
    """
    st.markdown("### ⭐ Favorites")
    
    # Initialize favorites in session state
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
    
    if st.session_state.favorites:
        for fav in st.session_state.favorites[:5]:  # Show first 5
            st.caption(f"⭐ {fav}")
    else:
        st.caption("No favorites yet")
        st.caption("Click ⭐ to add favorites")


def add_to_recent(item_name: str):
    """
    Add item to recent items
    
    Args:
        item_name: Name of the item to add
    """
    if 'recent_items' not in st.session_state:
        st.session_state.recent_items = []
    
    # Remove if already exists
    if item_name in st.session_state.recent_items:
        st.session_state.recent_items.remove(item_name)
    
    # Add to beginning
    st.session_state.recent_items.insert(0, item_name)
    
    # Keep only last 50
    st.session_state.recent_items = st.session_state.recent_items[:50]


def add_to_favorites(item_name: str):
    """
    Add item to favorites
    
    Args:
        item_name: Name of the item to add
    """
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
    
    if item_name not in st.session_state.favorites:
        st.session_state.favorites.append(item_name)


def remove_from_favorites(item_name: str):
    """
    Remove item from favorites
    
    Args:
        item_name: Name of the item to remove
    """
    if 'favorites' in st.session_state:
        if item_name in st.session_state.favorites:
            st.session_state.favorites.remove(item_name)


def render_breadcrumbs(path: list):
    """
    Render breadcrumbs navigation
    
    Args:
        path: List of page names in order
    """
    breadcrumb_html = ' → '.join([f'<span style="color: #666;">{p}</span>' for p in path])
    st.markdown(f'<div style="font-size: 0.85rem; margin-bottom: 16px;">{breadcrumb_html}</div>', 
                unsafe_allow_html=True)


def render_page_footer_links():
    """
    Render footer with useful links
    """
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**About**")
        st.caption("[Documentation](docs/)")
        st.caption("[Version Info]()")
    
    with col2:
        st.markdown("**Help**")
        st.caption("[User Guide](docs/PROJECT_TRACKER_GUIDE.md)")
        st.caption("[Quick Ref](docs/PROJECT_TRACKER_QUICK_REF.md)")
    
    with col3:
        st.markdown("**Feedback**")
        st.caption("[Report Issue]()")
        st.caption("[Suggest Feature]()")
    
    with col4:
        st.markdown("**Connect**")
        st.caption("[GitHub](https://github.com)")
        st.caption("[Contact]()")


def render_related_items(items: list):
    """
    Render related items section
    
    Args:
        items: List of related item names
    """
    if items:
        st.markdown("### 🔗 Related")
        
        for item in items:
            st.caption(f"• {item}")


# Example usage in a page:
"""
from components.quick_access import (
    render_quick_access_menu,
    render_recent_items,
    render_favorites,
    add_to_recent,
    render_breadcrumbs,
    render_page_footer_links,
    render_related_items
)

# In sidebar
with st.sidebar:
    render_quick_access_menu()
    st.markdown("---")
    render_recent_items()
    st.markdown("---")
    render_favorites()

# In main content
render_breadcrumbs(["Home", "Clinical Tools", "Scores"])

# Track page view
add_to_recent("CHA2DS2-VASc Score")

# Show related items
render_related_items([
    "HAS-BLED Score",
    "Atrial Fibrillation Protocol",
    "Anticoagulation Guidelines"
])

# Footer
render_page_footer_links()
"""
