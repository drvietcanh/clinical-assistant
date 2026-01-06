"""
Hero Section Component
Standardized hero sections for page headers
"""

import streamlit as st


def render_hero(
    title: str,
    subtitle: str = "",
    description: str = "",
    icon: str = "",
    gradient: tuple = ("#667eea", "#764ba2")
):
    """Render hero section with gradient background"""
    gradient_css = f"linear-gradient(135deg, {gradient[0]} 0%, {gradient[1]} 100%)"
    
    st.markdown(f"""
        <div style="
            background: {gradient_css};
            padding: 3rem 2rem;
            border-radius: 1rem;
            margin-bottom: 2rem;
            color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        ">
            <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                <span style="font-size: 3rem;">{icon}</span>
                <div>
                    <h1 style="margin: 0; font-size: 2.5rem; font-weight: 700;">{title}</h1>
                    <p style="margin: 0; font-size: 1.2rem; opacity: 0.9;">{subtitle}</p>
                </div>
            </div>
            <p style="margin: 0; font-size: 1.1rem; line-height: 1.6; opacity: 0.95;">
                {description}
            </p>
        </div>
    """, unsafe_allow_html=True)
