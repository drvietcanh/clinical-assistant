"""
Mobile Skeleton Loading Components
Skeleton screens for better perceived performance on mobile
"""

import streamlit as st


def render_skeleton_card(count: int = 1):
    """
    Render skeleton loading cards
    
    Args:
        count: Number of skeleton cards to render
    """
    st.markdown(
        """
        <style>
        .skeleton-card {
            background: var(--card-bg, #fff);
            border: 1px solid var(--border, #e0e0e0);
            border-radius: 12px;
            padding: 1rem;
            margin-bottom: 1rem;
            animation: skeleton-pulse 1.5s ease-in-out infinite;
        }
        
        .skeleton-line {
            height: 16px;
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            border-radius: 4px;
            margin-bottom: 0.75rem;
            animation: skeleton-shimmer 1.5s infinite;
        }
        
        .skeleton-line.short {
            width: 60%;
        }
        
        .skeleton-line.medium {
            width: 80%;
        }
        
        .skeleton-line.long {
            width: 100%;
        }
        
        .skeleton-avatar {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            animation: skeleton-shimmer 1.5s infinite;
            margin-bottom: 0.75rem;
        }
        
        @keyframes skeleton-shimmer {
            0% {
                background-position: -200% 0;
            }
            100% {
                background-position: 200% 0;
            }
        }
        
        @keyframes skeleton-pulse {
            0%, 100% {
                opacity: 1;
            }
            50% {
                opacity: 0.8;
            }
        }
        
        [data-theme="dark"] .skeleton-line,
        [data-theme="dark"] .skeleton-avatar {
            background: linear-gradient(90deg, #2a2a2a 25%, #1a1a1a 50%, #2a2a2a 75%);
            background-size: 200% 100%;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    for i in range(count):
        skeleton_html = """
        <div class="skeleton-card">
            <div class="skeleton-avatar"></div>
            <div class="skeleton-line long"></div>
            <div class="skeleton-line medium"></div>
            <div class="skeleton-line short"></div>
        </div>
        """
        st.markdown(skeleton_html, unsafe_allow_html=True)


def render_skeleton_table(rows: int = 5, cols: int = 4):
    """
    Render skeleton loading table
    
    Args:
        rows: Number of skeleton rows
        cols: Number of skeleton columns
    """
    st.markdown(
        """
        <style>
        .skeleton-table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }
        
        .skeleton-table th,
        .skeleton-table td {
            padding: 12px;
            border-bottom: 1px solid var(--border, #e0e0e0);
        }
        
        .skeleton-table-cell {
            height: 16px;
            background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
            background-size: 200% 100%;
            border-radius: 4px;
            animation: skeleton-shimmer 1.5s infinite;
        }
        
        @keyframes skeleton-shimmer {
            0% {
                background-position: -200% 0;
            }
            100% {
                background-position: 200% 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    table_html = '<table class="skeleton-table"><thead><tr>'
    for _ in range(cols):
        table_html += '<th><div class="skeleton-table-cell"></div></th>'
    table_html += '</tr></thead><tbody>'
    
    for _ in range(rows):
        table_html += '<tr>'
        for _ in range(cols):
            table_html += '<td><div class="skeleton-table-cell"></div></td>'
        table_html += '</tr>'
    
    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)
