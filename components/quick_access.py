"""
Quick Access Menu - Fast navigation to frequently used features
Add to sidebar for easy access
"""

import streamlit as st

def render_quick_access_menu():
    """
    Render quick access menu in sidebar
    Provides shortcuts to most used features
    """
    st.markdown("### ⚡ Quick Access")
    
    # Most used clinical tools
    with st.expander("🩺 Clinical Tools", expanded=False):
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📊 Scores", use_container_width=True, key="qa_scores"):
                st.switch_page("pages/01_📊_Scores.py")
            if st.button("🔬 Labs", use_container_width=True, key="qa_labs"):
                st.switch_page("pages/05_🔬_Labs_and_Calculators.py")
            if st.button("💊 Drugs", use_container_width=True, key="qa_drugs"):
                st.switch_page("pages/07_💊_Drug_Database.py")
        
        with col2:
            if st.button("📋 Protocols", use_container_width=True, key="qa_protocols"):
                st.switch_page("pages/04_📋_Protocols.py")
            if st.button("🧭 Decision", use_container_width=True, key="qa_decision"):
                st.switch_page("pages/10_🧭_Decision_Support.py")
            if st.button("🫁 Critical", use_container_width=True, key="qa_critical"):
                st.switch_page("pages/09_🫁_Critical_Care.py")
    
    # Information resources
    with st.expander("📚 Resources", expanded=False):
        if st.button("📋 Guidelines", use_container_width=True, key="qa_guidelines"):
            st.switch_page("pages/15_📋_Guidelines_Tracker.py")
        if st.button("📖 Diseases", use_container_width=True, key="qa_diseases"):
            st.switch_page("pages/16_📖_Disease_Encyclopedia.py")
        if st.button("📚 Articles", use_container_width=True, key="qa_articles"):
            st.switch_page("pages/12_📚_In_Depth_Articles.py")
    
    # Utilities
    with st.expander("🔧 Utilities", expanded=False):
        if st.button("🔍 Search", use_container_width=True, key="qa_search"):
            st.switch_page("pages/20_🔍_Global_Search.py")
        if st.button("⚙️ Settings", use_container_width=True, key="qa_settings"):
            st.switch_page("pages/23_⚙️_Settings.py")


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
