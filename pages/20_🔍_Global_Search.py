"""
Global Search - Search across all modules
Comprehensive search functionality for Clinical Assistant
"""

import streamlit as st
from utils.page_helper import setup_page, render_standard_footer
from components.ui import render_info_box, render_hero
from guidelines.data import get_all_guidelines
import json
from pathlib import Path

# Standard page setup
setup_page(
    page_title="Global Search",
    page_icon="🔍",
    description="Tìm kiếm toàn bộ Clinical Assistant"
)

# Custom CSS
st.markdown("""
<style>
.search-result {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 16px;
    margin: 12px 0;
    transition: all 0.2s;
}

.search-result:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
    border-color: #0066CC;
}

.result-title {
    color: #0066CC;
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 8px;
}

.result-type {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-right: 8px;
}

.type-drug { background: #e3f2fd; color: #1976d2; }
.type-guideline { background: #f3e5f5; color: #7b1fa2; }
.type-protocol { background: #e8f5e9; color: #388e3c; }
.type-score { background: #fff3e0; color: #f57c00; }
.type-article { background: #fce4ec; color: #c2185b; }

.search-stats {
    background: #f5f5f5;
    padding: 12px;
    border-radius: 8px;
    margin: 16px 0;
}
</style>
""", unsafe_allow_html=True)

# Hero section
render_hero(
    title="Global Search",
    subtitle="🔍 Tìm kiếm toàn diện",
    description="Tìm kiếm drugs, guidelines, protocols, scores, và nhiều hơn nữa",
    icon="🔍",
    gradient=("#4facfe", "#00f2fe")
)

# Sidebar
with st.sidebar:
    st.header("🔍 Global Search")
    
    # Search filters
    st.subheader("🎯 Filters")
    
    search_types = st.multiselect(
        "Loại nội dung:",
        ["All", "Drugs", "Guidelines", "Protocols", "Scores", "Articles", "Diseases"],
        default=["All"]
    )
    
    st.markdown("---")
    
    # Recent searches
    st.subheader("🕐 Recent Searches")
    if 'recent_searches' not in st.session_state:
        st.session_state.recent_searches = []
    
    if st.session_state.recent_searches:
        for search in st.session_state.recent_searches[-5:]:
            if st.button(f"🔍 {search}", key=f"recent_{search}", use_container_width=True):
                st.session_state.search_query = search
                st.rerun()
    else:
        st.caption("No recent searches")
    
    st.markdown("---")
    
    render_info_box("""
    **🔍 Global Search:**
    - Tìm kiếm toàn bộ app
    - Filter theo loại
    - Recent searches
    - Quick access
    
    **💡 Tips:**
    - Use specific terms
    - Try different filters
    - Save favorites
    """, type="info", title="Search Help")

# Main search interface
st.markdown("### 🔍 Search")

# Search box
col1, col2 = st.columns([4, 1])

with col1:
    search_query = st.text_input(
        "Enter search term:",
        placeholder="e.g., aspirin, sepsis, CHA2DS2-VASc...",
        key="main_search",
        label_visibility="collapsed"
    )

with col2:
    if st.button("🔍 Search", use_container_width=True, type="primary"):
        if search_query and search_query not in st.session_state.recent_searches:
            st.session_state.recent_searches.append(search_query)

# Quick search suggestions
if not search_query:
    st.markdown("### 💡 Popular Searches")
    
    popular = [
        "Aspirin", "Sepsis", "CHA2DS2-VASc", "Heart Failure", 
        "Diabetes", "Hypertension", "Antibiotics", "COPD"
    ]
    
    cols = st.columns(4)
    for idx, term in enumerate(popular):
        with cols[idx % 4]:
            if st.button(term, key=f"popular_{term}", use_container_width=True):
                st.session_state.search_query = term
                st.rerun()

# Perform search
if search_query:
    st.markdown("---")
    st.markdown(f"### 📊 Results for: **{search_query}**")
    
    # Search across modules
    results = []
    
    # 1. Search Guidelines
    try:
        guidelines = get_all_guidelines()
        for g in guidelines:
            if search_query.lower() in g.title.lower() or \
               search_query.lower() in g.title_vn.lower() or \
               search_query.lower() in g.organization.lower():
                results.append({
                    'type': 'Guideline',
                    'title': g.title_vn,
                    'subtitle': f"{g.organization} {g.year}",
                    'description': g.description[:200] if g.description else "",
                    'link': "pages/15_📋_Guidelines_Tracker.py"
                })
    except Exception as e:
        pass
    
    # 2. Mock search for other types (would be real in production)
    # Drugs
    if "All" in search_types or "Drugs" in search_types:
        drug_results = [
            {
                'type': 'Drug',
                'title': 'Aspirin',
                'subtitle': 'Antiplatelet agent',
                'description': 'Used for cardiovascular protection and pain relief',
                'link': "pages/07_💊_Drug_Database.py"
            }
        ]
        if any(term in search_query.lower() for term in ['aspirin', 'asa']):
            results.extend(drug_results)
    
    # Protocols
    if "All" in search_types or "Protocols" in search_types:
        protocol_results = [
            {
                'type': 'Protocol',
                'title': 'Sepsis 1-Hour Bundle',
                'subtitle': 'SSC 2021',
                'description': 'Early management of sepsis and septic shock',
                'link': "pages/04_📋_Protocols.py"
            }
        ]
        if 'sepsis' in search_query.lower():
            results.extend(protocol_results)
    
    # Scores
    if "All" in search_types or "Scores" in search_types:
        score_results = [
            {
                'type': 'Score',
                'title': 'CHA2DS2-VASc',
                'subtitle': 'Stroke risk in AF',
                'description': 'Calculate stroke risk in atrial fibrillation',
                'link': "pages/01_📊_Scores.py"
            }
        ]
        if 'cha2ds2' in search_query.lower() or 'stroke' in search_query.lower():
            results.extend(score_results)
    
    # Display results
    if results:
        st.markdown(f"""
        <div class="search-stats">
            <strong>Found {len(results)} results</strong>
        </div>
        """, unsafe_allow_html=True)
        
        for result in results:
            type_class = f"type-{result['type'].lower()}"
            
            st.markdown(f"""
            <div class="search-result">
                <div>
                    <span class="result-type {type_class}">{result['type']}</span>
                </div>
                <div class="result-title">{result['title']}</div>
                <div style="color: #666; font-size: 0.9rem; margin-bottom: 8px;">
                    {result['subtitle']}
                </div>
                <div style="color: #333; font-size: 0.95rem;">
                    {result['description']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("Open →", key=f"open_{result['title']}", use_container_width=True):
                    st.switch_page(result['link'])
    else:
        st.warning(f"No results found for '{search_query}'")
        st.info("💡 Try different search terms or filters")

# Additional features
st.markdown("---")
st.markdown("### ⚡ Quick Access")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📊 Clinical Tools**")
    if st.button("Scores", use_container_width=True):
        st.switch_page("pages/01_📊_Scores.py")
    if st.button("Labs", use_container_width=True):
        st.switch_page("pages/05_🔬_Labs_and_Calculators.py")

with col2:
    st.markdown("**📚 Resources**")
    if st.button("Guidelines", use_container_width=True):
        st.switch_page("pages/15_📋_Guidelines_Tracker.py")
    if st.button("Protocols", use_container_width=True):
        st.switch_page("pages/04_📋_Protocols.py")

with col3:
    st.markdown("**💊 Drugs**")
    if st.button("Drug Database", use_container_width=True):
        st.switch_page("pages/07_💊_Drug_Database.py")
    if st.button("Antibiotics", use_container_width=True):
        st.switch_page("pages/02_💊_Antibiotics.py")

# Footer
st.markdown("---")
render_standard_footer(disclaimer=False)
