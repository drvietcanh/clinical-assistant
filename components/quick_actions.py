"""
Quick Actions Component
Fast access buttons for common actions
"""

import streamlit as st
from typing import List, Dict, Optional


def get_quick_actions() -> List[Dict]:
    """Get list of quick actions"""
    return [
        {
            "id": "search_drug",
            "label": "Tìm thuốc",
            "icon": "💊",
            "page": "pages/07_💊_Drug_Database.py",
            "color": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        },
        {
            "id": "calculate_score",
            "label": "Tính score",
            "icon": "📊",
            "page": "pages/01_📊_Scores.py",
            "color": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
        },
        {
            "id": "view_guideline",
            "label": "Xem guideline",
            "icon": "📋",
            "page": "pages/04_📋_Protocols.py",
            "color": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
        },
        {
            "id": "drug_interaction",
            "label": "Tương tác thuốc",
            "icon": "⚗️",
            "page": "pages/07_💊_Drug_Database.py",
            "color": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
        },
    ]


def render_quick_actions(
    max_items: int = 4,
    layout: str = "horizontal"
) -> None:
    """
    Render quick actions bar
    
    Args:
        max_items: Maximum number of actions to show
        layout: "horizontal" or "grid"
    """
    actions = get_quick_actions()[:max_items]
    
    if layout == "horizontal":
        cols = st.columns(len(actions))
        for idx, action in enumerate(actions):
            with cols[idx]:
                st.markdown(f"""
                <div class="quick-action-btn" style="
                    background: {action['color']};
                    border-radius: 12px;
                    padding: 1rem;
                    text-align: center;
                    color: white;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                    min-height: 80px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                " onclick="window.location.href='{action['page']}'">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{action['icon']}</div>
                    <div style="font-size: 0.85rem; font-weight: 600;">{action['label']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    elif layout == "grid":
        num_cols = min(2, len(actions))
        cols = st.columns(num_cols)
        for idx, action in enumerate(actions):
            with cols[idx % num_cols]:
                st.markdown(f"""
                <div class="quick-action-btn" style="
                    background: {action['color']};
                    border-radius: 12px;
                    padding: 1.25rem;
                    text-align: center;
                    color: white;
                    cursor: pointer;
                    transition: all 0.2s ease;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                    margin-bottom: 1rem;
                " onclick="window.location.href='{action['page']}'">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{action['icon']}</div>
                    <div style="font-size: 0.9rem; font-weight: 600;">{action['label']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # Add CSS for quick actions
    st.markdown("""
    <style>
    .quick-action-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }
    
    .quick-action-btn:active {
        transform: scale(0.98);
    }
    
    @media (max-width: 768px) {
        .quick-action-btn {
            min-height: 70px !important;
            padding: 0.75rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

