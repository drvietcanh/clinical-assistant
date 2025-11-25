"""
Responsive Table Component
Mobile-optimized tables with horizontal scroll and card view
"""

import streamlit as st
import pandas as pd
from typing import Optional


def render_responsive_table(
    data: pd.DataFrame,
    use_card_view: bool = True,
    card_view_breakpoint: int = 480,
    **kwargs
):
    """
    Render a responsive table that adapts to mobile screens
    
    Args:
        data: DataFrame to display
        use_card_view: Whether to use card view on very small screens
        card_view_breakpoint: Screen width breakpoint for card view (px)
        **kwargs: Additional arguments passed to st.dataframe
    
    Returns:
        None (renders table)
    """
    # Add responsive wrapper CSS
    st.markdown(
        f"""
        <style>
        .responsive-table-wrapper {{
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            margin: 1rem 0;
            border-radius: 8px;
            border: 1px solid var(--border);
        }}
        
        @media (max-width: {card_view_breakpoint}px) {{
            .responsive-table-wrapper {{
                border: none;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # For very small screens, show card view if enabled
    if use_card_view:
        st.markdown(
            f"""
            <div class="responsive-table-wrapper">
            """,
            unsafe_allow_html=True
        )
    
    # Render table
    st.dataframe(data, **kwargs)
    
    if use_card_view:
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Add mobile-friendly note for large tables
    if len(data.columns) > 5:
        st.caption("💡 **Mẹo di động:** Vuốt ngang để xem tất cả cột")


def render_table_cards(data: pd.DataFrame, title: Optional[str] = None):
    """
    Render table data as cards on mobile (alternative view)
    Each row becomes a card
    
    Args:
        data: DataFrame to display
        title: Optional title for the table
    """
    if title:
        st.subheader(title)
    
    st.markdown(
        """
        <style>
        .table-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        .table-card-row {
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid var(--border);
        }
        
        .table-card-row:last-child {
            border-bottom: none;
        }
        
        .table-card-label {
            font-weight: 600;
            color: var(--text-secondary);
            flex: 1;
        }
        
        .table-card-value {
            flex: 2;
            text-align: right;
            color: var(--text-primary);
        }
        
        @media (min-width: 769px) {
            .table-card-container {
                display: none;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Render cards for mobile
    st.markdown('<div class="table-card-container">', unsafe_allow_html=True)
    
    for idx, row in data.iterrows():
        card_html = '<div class="table-card">'
        for col in data.columns:
            value = row[col]
            card_html += f"""
            <div class="table-card-row">
                <span class="table-card-label">{col}:</span>
                <span class="table-card-value">{value}</span>
            </div>
            """
        card_html += '</div>'
        st.markdown(card_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Render regular table for desktop (hidden on mobile)
    st.markdown(
        """
        <style>
        @media (max-width: 768px) {
            .desktop-table {
                display: none;
            }
        }
        </style>
        <div class="desktop-table">
        """,
        unsafe_allow_html=True
    )
    st.dataframe(data, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

