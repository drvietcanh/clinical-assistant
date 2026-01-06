"""
Main Menu Styles
Centralized CSS for the Main Menu page to keep layout and styling maintainable.
"""

import streamlit as st


def inject_main_menu_styles() -> None:
    """Inject CSS styles used on the Main Menu page."""
    st.markdown(
        """
<style>
.main-menu-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.search-section {
    margin-bottom: 30px;
}

.stats-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin: 10px 0;
}

.stats-card h3 {
    color: white;
    margin: 0;
}

.stats-card p {
    color: rgba(255, 255, 255, 0.9);
    margin: 5px 0;
}

.quick-access-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin: 20px 0;
}

.category-card {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s;
}

.category-card:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}
</style>
        """,
        unsafe_allow_html=True,
    )

