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
    show_scroll_indicators: bool = True,
    sticky_header: bool = True,
    **kwargs
):
    """
    Render a responsive table that adapts to mobile screens
    
    Args:
        data: DataFrame to display
        use_card_view: Whether to use card view on very small screens
        card_view_breakpoint: Screen width breakpoint for card view (px)
        show_scroll_indicators: Show visual indicators for horizontal scroll
        sticky_header: Make header sticky when scrolling vertically
        **kwargs: Additional arguments passed to st.dataframe
    
    Returns:
        None (renders table)
    """
    table_id = f"responsive-table-{hash(str(data.columns))}"
    
    # Add responsive wrapper CSS
    st.markdown(
        f"""
        <style>
        .responsive-table-wrapper-{table_id} {{
            position: relative;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            margin: 1rem 0;
            border-radius: 8px;
            border: 1px solid var(--border, #e0e0e0);
        }}
        
        /* Scroll indicators */
        .responsive-table-wrapper-{table_id}::before,
        .responsive-table-wrapper-{table_id}::after {{
            content: '';
            position: absolute;
            top: 0;
            bottom: 0;
            width: 20px;
            pointer-events: none;
            z-index: 1;
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        
        .responsive-table-wrapper-{table_id}::before {{
            left: 0;
            background: linear-gradient(to right, rgba(255,255,255,0.9), transparent);
        }}
        
        .responsive-table-wrapper-{table_id}::after {{
            right: 0;
            background: linear-gradient(to left, rgba(255,255,255,0.9), transparent);
        }}
        
        .responsive-table-wrapper-{table_id}.scroll-left::before,
        .responsive-table-wrapper-{table_id}.scroll-right::after {{
            opacity: 1;
        }}
        
        /* Sticky header */
        @media (max-width: 768px) {{
            .responsive-table-wrapper-{table_id} table thead {{
                position: sticky;
                top: 0;
                z-index: 10;
                background: white;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            
            [data-theme="dark"] .responsive-table-wrapper-{table_id} table thead {{
                background: #1e1e1e;
            }}
        }}
        
        @media (max-width: {card_view_breakpoint}px) {{
            .responsive-table-wrapper-{table_id} {{
                border: none;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Add JavaScript for scroll indicators
    if show_scroll_indicators:
        st.markdown(
            f"""
            <script>
            (function() {{
                const wrapper = document.querySelector('.responsive-table-wrapper-{table_id}');
                if (!wrapper) return;
                
                function updateScrollIndicators() {{
                    const scrollLeft = wrapper.scrollLeft;
                    const scrollWidth = wrapper.scrollWidth;
                    const clientWidth = wrapper.clientWidth;
                    
                    wrapper.classList.toggle('scroll-left', scrollLeft > 0);
                    wrapper.classList.toggle('scroll-right', scrollLeft < scrollWidth - clientWidth - 1);
                }}
                
                wrapper.addEventListener('scroll', updateScrollIndicators);
                window.addEventListener('resize', updateScrollIndicators);
                updateScrollIndicators();
            }})();
            </script>
            """,
            unsafe_allow_html=True
        )
    
    # Render table with wrapper
    st.markdown(f'<div class="responsive-table-wrapper-{table_id}">', unsafe_allow_html=True)
    st.dataframe(data, **kwargs)
    st.markdown('</div>', unsafe_allow_html=True)
    
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
            value = str(row[col]) if pd.notna(row[col]) else ''
            # Truncate long values
            if len(value) > 50:
                value = value[:47] + '...'
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
            .desktop-table-container {
                display: none;
            }
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
    st.markdown('<div class="desktop-table-container">', unsafe_allow_html=True)
    st.dataframe(data, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

