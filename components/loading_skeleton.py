"""
Loading Skeleton Component
Shows skeleton loading states for better UX
"""

import streamlit as st


def render_card_skeleton(count: int = 3) -> None:
    """
    Render skeleton cards for loading state
    
    Args:
        count: Number of skeleton cards to show
    """
    st.markdown("""
    <style>
    .skeleton-card {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
        animation: skeleton-loading 1.5s ease-in-out infinite;
    }
    
    .skeleton-line {
        height: 12px;
        background: linear-gradient(90deg, 
            var(--border) 0%, 
            rgba(255,255,255,0.1) 50%, 
            var(--border) 100%);
        background-size: 200% 100%;
        border-radius: 4px;
        margin-bottom: 0.75rem;
        animation: skeleton-shimmer 1.5s ease-in-out infinite;
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
    
    @keyframes skeleton-shimmer {
        0% {
            background-position: -200% 0;
        }
        100% {
            background-position: 200% 0;
        }
    }
    
    @keyframes skeleton-loading {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.7;
        }
    }
    
    [data-theme="dark"] .skeleton-line {
        background: linear-gradient(90deg, 
            var(--border) 0%, 
            rgba(255,255,255,0.05) 50%, 
            var(--border) 100%);
        background-size: 200% 100%;
    }
    </style>
    """, unsafe_allow_html=True)
    
    cols = st.columns(min(3, count))
    for idx in range(count):
        with cols[idx % len(cols)]:
            st.markdown(f"""
            <div class="skeleton-card">
                <div class="skeleton-line long" style="height: 20px; margin-bottom: 0.5rem;"></div>
                <div class="skeleton-line medium" style="height: 16px; margin-bottom: 0.5rem;"></div>
                <div class="skeleton-line short" style="height: 14px;"></div>
            </div>
            """, unsafe_allow_html=True)


def render_list_skeleton(count: int = 5) -> None:
    """
    Render skeleton list items for loading state
    
    Args:
        count: Number of skeleton items to show
    """
    st.markdown("""
    <style>
    .skeleton-list-item {
        background: var(--card-bg);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        animation: skeleton-loading 1.5s ease-in-out infinite;
    }
    
    .skeleton-avatar {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: var(--border);
        flex-shrink: 0;
        animation: skeleton-shimmer 1.5s ease-in-out infinite;
    }
    
    .skeleton-content {
        flex: 1;
    }
    </style>
    """, unsafe_allow_html=True)
    
    for _ in range(count):
        st.markdown("""
        <div class="skeleton-list-item">
            <div class="skeleton-avatar"></div>
            <div class="skeleton-content">
                <div class="skeleton-line long" style="height: 16px; margin-bottom: 0.5rem;"></div>
                <div class="skeleton-line medium" style="height: 12px;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)


def render_table_skeleton(rows: int = 5, cols: int = 4) -> None:
    """
    Render skeleton table for loading state
    
    Args:
        rows: Number of rows
        cols: Number of columns
    """
    st.markdown("""
    <style>
    .skeleton-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 1rem;
    }
    
    .skeleton-table th,
    .skeleton-table td {
        padding: 0.75rem;
        border: 1px solid var(--border);
        text-align: left;
    }
    
    .skeleton-table th {
        background: var(--primary);
        color: white;
    }
    
    .skeleton-table td {
        background: var(--card-bg);
    }
    
    .skeleton-table .skeleton-line {
        height: 14px;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    header_html = "<table class='skeleton-table'><thead><tr>"
    for _ in range(cols):
        header_html += "<th><div class='skeleton-line short'></div></th>"
    header_html += "</tr></thead><tbody>"
    
    # Rows
    for _ in range(rows):
        header_html += "<tr>"
        for _ in range(cols):
            header_html += "<td><div class='skeleton-line medium'></div></td>"
        header_html += "</tr>"
    
    header_html += "</tbody></table>"
    
    st.markdown(header_html, unsafe_allow_html=True)

