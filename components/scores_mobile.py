"""
Scores Mobile Optimization Component
Mobile-friendly layout and responsive design improvements for Scores page
"""

import streamlit as st


def apply_mobile_css():
    """Apply mobile-optimized CSS for Scores page"""
    mobile_css = """
    <style>
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        /* Sidebar optimization */
        .css-1d391kg {
            padding: 0.5rem;
        }
        
        /* Button sizing */
        .stButton > button {
            min-height: 44px; /* Touch-friendly */
            font-size: 0.9rem;
            padding: 0.5rem 1rem;
        }
        
        /* Input fields */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select {
            min-height: 44px;
            font-size: 1rem; /* Prevent zoom on iOS */
        }
        
        /* Radio buttons - larger touch targets */
        .stRadio > div {
            gap: 0.75rem;
        }
        
        .stRadio > div > label {
            padding: 0.75rem;
            min-height: 44px;
            border-radius: 8px;
        }
        
        /* Cards and containers */
        .element-container {
            margin-bottom: 1rem;
        }
        
        /* Charts - responsive */
        .js-plotly-plot {
            width: 100% !important;
        }
        
        /* Tables - scrollable */
        .stDataFrame {
            overflow-x: auto;
            display: block;
        }
        
        /* Related calculators - stack on mobile */
        [data-testid="column"] {
            width: 100% !important;
            margin-bottom: 1rem;
        }
        
        /* Search suggestions - full width */
        .stButton > button {
            width: 100%;
        }
        
        /* Favorites section - compact */
        .favorites-section {
            max-height: 300px;
            overflow-y: auto;
        }
        
        /* Hide less important elements on mobile */
        .mobile-hide {
            display: none;
        }
        
        /* Compact info boxes */
        .stInfo, .stSuccess, .stWarning, .stError {
            padding: 0.75rem;
            font-size: 0.9rem;
        }
    }
    
    /* Tablet optimization */
    @media (min-width: 769px) and (max-width: 1024px) {
        .stButton > button {
            min-height: 40px;
        }
        
        [data-testid="column"] {
            width: 50% !important;
        }
    }
    
    /* Touch-friendly interactions */
    @media (hover: none) and (pointer: coarse) {
        /* Larger touch targets */
        button, a, input, select {
            min-height: 44px;
        }
        
        /* Remove hover effects on touch devices */
        button:hover {
            opacity: 1;
        }
        
        /* Active state for touch */
        button:active {
            opacity: 0.7;
            transform: scale(0.98);
        }
    }
    
    /* Landscape mobile optimization */
    @media (max-width: 768px) and (orientation: landscape) {
        .mobile-page-header {
            padding: 0.5rem 1rem;
        }
        
        .mobile-header-title h1 {
            font-size: 1.1rem;
        }
    }
    
    /* Dark mode mobile adjustments */
    [data-theme="dark"] @media (max-width: 768px) {
        .stSidebar {
            background-color: #1e1e1e;
        }
        
        .stButton > button {
            background-color: #2d2d2d;
            color: #e0e0e0;
        }
    }
    </style>
    """
    st.markdown(mobile_css, unsafe_allow_html=True)


def render_mobile_search_optimized():
    """Render mobile-optimized search interface"""
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Search input - larger on mobile */
        .stTextInput input {
            font-size: 16px !important; /* Prevent zoom on iOS */
        }
        
        /* Search suggestions - full width buttons */
        .search-suggestion-button {
            width: 100%;
            margin-bottom: 0.5rem;
            text-align: left;
            padding: 0.75rem 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_mobile_filters():
    """Render mobile-optimized filters"""
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Filter expander - full width */
        .streamlit-expanderHeader {
            font-size: 0.95rem;
            padding: 0.75rem;
        }
        
        /* Multiselect - larger touch targets */
        .stMultiSelect > div > div {
            min-height: 44px;
        }
        
        /* Checkbox - larger */
        .stCheckbox > label {
            padding: 0.5rem;
            font-size: 0.95rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_mobile_calculator_list():
    """Optimize calculator list for mobile"""
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Radio buttons - larger and stacked */
        .stRadio > div {
            flex-direction: column;
        }
        
        .stRadio > div > label {
            width: 100%;
            padding: 1rem;
            margin-bottom: 0.5rem;
            border: 1px solid var(--border);
            border-radius: 8px;
        }
        
        /* Calculator name - truncate on mobile */
        .calculator-name {
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
            max-width: 100%;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_mobile_results():
    """Optimize results display for mobile"""
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Results section - better spacing */
        .results-section {
            padding: 1rem;
        }
        
        /* Charts - responsive */
        .js-plotly-plot {
            height: 300px !important;
        }
        
        /* Tables - horizontal scroll */
        table {
            display: block;
            overflow-x: auto;
            white-space: nowrap;
        }
        
        /* Export buttons - stack vertically */
        .export-buttons {
            flex-direction: column;
        }
        
        .export-buttons > * {
            width: 100%;
            margin-bottom: 0.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def render_mobile_sidebar_optimization():
    """Optimize sidebar for mobile"""
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        /* Sidebar - full width when open */
        .css-1d391kg {
            width: 100%;
            max-width: 100%;
        }
        
        /* Sidebar sections - better spacing */
        .sidebar-section {
            margin-bottom: 1.5rem;
        }
        
        /* Favorites - scrollable */
        .favorites-list {
            max-height: 200px;
            overflow-y: auto;
            -webkit-overflow-scrolling: touch;
        }
        
        /* Theme toggle - full width */
        .theme-toggle-button {
            width: 100%;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def init_mobile_optimizations():
    """Initialize all mobile optimizations"""
    apply_mobile_css()
    render_mobile_search_optimized()
    render_mobile_filters()
    render_mobile_calculator_list()
    render_mobile_results()
    render_mobile_sidebar_optimization()


def render_mobile_bottom_navigation():
    """Render bottom navigation for mobile (optional)"""
    st.markdown("""
    <style>
    @media (max-width: 768px) {
        .mobile-bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--card-bg);
            border-top: 1px solid var(--border);
            padding: 0.5rem;
            display: flex;
            justify-content: space-around;
            z-index: 1000;
            box-shadow: 0 -2px 8px rgba(0,0,0,0.1);
        }
        
        .mobile-bottom-nav button {
            flex: 1;
            padding: 0.75rem;
            border: none;
            background: transparent;
            font-size: 0.85rem;
            color: var(--text-primary);
        }
        
        .mobile-bottom-nav button:active {
            background: var(--border);
        }
        
        /* Add padding to main content to avoid overlap */
        .main .block-container {
            padding-bottom: 60px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

