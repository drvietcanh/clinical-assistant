"""
Quick Actions Component for Homepage Dashboard
Part of Phase 1 UI Modernization - Enhanced with clinical workflow focus
"""

import streamlit as st
from typing import List, Dict


def get_quick_actions() -> List[Dict]:
    """
    Get list of quick actions optimized for clinical workflow
    Based on most common tasks in medical practice
    """
    return [
        {
            "id": "crcl_calculator",
            "label": "Creatinine Clearance",
            "desc": "Tính eGFR/CrCl cho điều chỉnh liều",
            "icon": "🧮",
            "page": "pages/01_📊_Scores.py",
            "color": "#00897B"
        },
        {
            "id": "antibiotic_dosing",
            "label": "Liều Kháng Sinh",
            "desc": "Tra cứu liều và điều chỉnh theo thận",
            "icon": "💊",
            "page": "pages/02_💊_Antibiotics.py",
            "color": "#1976D2"
        },
        {
            "id": "drug_interaction",
            "label": "Tương tác thuốc",
            "desc": "Kiểm tra tương tác và chống chỉ định",
            "icon": "⚠️",
            "page": "pages/07_💊_Drug_Database.py",
            "color": "#FF7043"
        },
        {
            "id": "critical_care",
            "label": "Hồi sức cấp cứu",
            "desc": "Phác đồ và quy trình hồi sức",
            "icon": "🫁",
            "page": "pages/09_🫁_Critical_Care.py",
            "color": "#EF5350"
        }
    ]


def render_quick_actions(max_items: int = 4, layout: str = "cards") -> None:
    """
    Render quick actions with Phase 1 modern design
    
    Args:
        max_items: Maximum number of actions to show (default: 4)
        layout: "cards" (desktop) or "compact" (mobile)
    """
    actions = get_quick_actions()[:max_items]
    
    st.markdown("### ⚡ Truy cập nhanh")
    st.markdown("Các công cụ được sử dụng nhiều nhất")
    
    if layout == "cards":
        # Desktop: 4-column grid with large cards
        cols = st.columns(4)
        
        for idx, (col, action) in enumerate(zip(cols, actions)):
            with col:
                # Styled card with gradient background
                card_html = f"""
                <div style="
                    background: linear-gradient(135deg, {action['color']}15 0%, {action['color']}05 100%);
                    border: 2px solid {action['color']}40;
                    border-radius: 16px;
                    padding: 1.5rem;
                    text-align: center;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    min-height: 180px;
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                " onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 8px 24px rgba(0,0,0,0.15)';" 
                   onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 2px 8px rgba(0,0,0,0.1)';">
                    <div style="font-size: 3rem; margin-bottom: 0.5rem;">{action['icon']}</div>
                    <div>
                        <div style="
                            font-size: 1.1rem;
                            font-weight: 600;
                            color: #263238;
                            margin-bottom: 0.5rem;
                        ">{action['label']}</div>
                        <div style="
                            font-size: 0.85rem;
                            color: #546E7A;
                            line-height: 1.4;
                        ">{action['desc']}</div>
                    </div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                
                # Functional button (visually hidden but clickable)
                if st.button(
                    f"{action['icon']} {action['label']}", 
                    key=f"qa_{action['id']}",
                    use_container_width=True,
                    type="primary" if idx == 0 else "secondary"
                ):
                    st.switch_page(action['page'])
    
    elif layout == "compact":
        # Mobile: 2x2 grid
        row1_cols = st.columns(2)
        row2_cols = st.columns(2)
        
        for idx, action in enumerate(actions):
            col = row1_cols[idx % 2] if idx < 2 else row2_cols[idx % 2]
            with col:
                if st.button(
                    f"{action['icon']} {action['label']}", 
                    key=f"qa_mobile_{action['id']}",
                    use_container_width=True
                ):
                    st.switch_page(action['page'])


def render_quick_actions_horizontal(max_items: int = 4) -> None:
    """
    Render quick actions in horizontal bar (legacy support)
    """
    actions = get_quick_actions()[:max_items]
    cols = st.columns(len(actions))
    
    for idx, action in enumerate(actions):
        with cols[idx]:
            st.markdown(f"""
            <div class="quick-action-btn" style="
                background: linear-gradient(135deg, {action['color']} 0%, {action['color']}dd 100%);
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
            ">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{action['icon']}</div>
                <div style="font-size: 0.85rem; font-weight: 600;">{action['label']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Add hover effects
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
