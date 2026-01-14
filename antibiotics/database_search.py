"""
Antibiotic Database - Search Functions
Search, filter, and autocomplete functions for antibiotic database
"""

import streamlit as st
from .antibiotics_data import ANTIBIOTICS_DATABASE

"""
Antibiotic Database and Lookup Functions - Optimized Version
Tích hợp database kháng sinh với công cụ tra cứu và tính liều
Đã tối ưu: loại bỏ trùng lặp, compact view, expandable details, integrated dosing calculator
"""

import streamlit as st
import pandas as pd
from .antibiotics_data import ANTIBIOTICS_DATABASE
from .dosing_calculator import (
    calculate_adjusted_dose, 
    get_renal_category,
    calculate_detailed_dose,
    check_warnings,
    calculate_ibw,
    calculate_abw,
    calculate_bmi
)


def search_antibiotics(query, max_results=None):
    """
    Enhanced search antibiotics by name, Vietnamese name, group, or indication with scoring
    Results are cached for performance
    """
    if not query or len(query.strip()) == 0:
        return []
    
    query_lower = query.lower().strip()
    
    # Check cache
    cache_key = f'_search_cache_{query_lower}_{max_results}'
    if cache_key in st.session_state:
        return st.session_state[cache_key]
    
    results = []
    
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        score = 0.0
        
        # Search in name (highest priority)
        if query_lower in ab_name.lower():
            if query_lower == ab_name.lower():
                score = 1.0  # Exact match
            elif ab_name.lower().startswith(query_lower):
                score = 0.9  # Starts with query
            else:
                score = 0.8  # Contains query
            results.append((ab_name, ab_data, score))
            continue
        
        # Search in Vietnamese name
        if 'vietnamese_name' in ab_data:
            vn_name_lower = ab_data['vietnamese_name'].lower()
            if query_lower in vn_name_lower:
                score = 0.7
                results.append((ab_name, ab_data, score))
                continue
        
        # Search in group
        if 'group' in ab_data:
            group_lower = ab_data['group'].lower()
            if query_lower in group_lower:
                score = 0.6
                results.append((ab_name, ab_data, score))
                continue
        
        # Search in indications
        if 'indications' in ab_data:
            for indication in ab_data['indications']:
                if query_lower in indication.lower():
                    score = 0.5
                    results.append((ab_name, ab_data, score))
                    break
    
    # Sort by score (descending)
    results.sort(key=lambda x: x[2], reverse=True)
    
    # Return just (name, data) tuples for backward compatibility
    final_results = [(name, data) for name, data, score in results]
    if max_results:
        final_results = final_results[:max_results]
    
    # Cache results (limit cache size to prevent memory issues)
    if len(st.session_state.get('_search_cache_keys', [])) < 50:
        st.session_state[cache_key] = final_results
        if '_search_cache_keys' not in st.session_state:
            st.session_state['_search_cache_keys'] = []
        st.session_state['_search_cache_keys'].append(cache_key)
    elif cache_key not in st.session_state:
        # Remove oldest cache entry
        if st.session_state.get('_search_cache_keys'):
            oldest_key = st.session_state['_search_cache_keys'].pop(0)
            if oldest_key in st.session_state:
                del st.session_state[oldest_key]
            st.session_state[cache_key] = final_results
            st.session_state['_search_cache_keys'].append(cache_key)
    
    return final_results


def get_antibiotic_autocomplete_suggestions(query, max_suggestions=5):
    """
    Get autocomplete suggestions for antibiotic search
    Returns list of antibiotic names matching query
    """
    if not query or len(query) < 1:
        # Popular antibiotics
        return ["Vancomycin", "Ceftriaxone", "Piperacillin-Tazobactam", "Meropenem", "Levofloxacin"]
    
    query_lower = query.lower()
    suggestions = []
    seen = set()
    
    # Search in names first (most relevant)
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        if query_lower in ab_name.lower():
            if ab_name not in seen:
                suggestions.append(ab_name)
                seen.add(ab_name)
                if len(suggestions) >= max_suggestions:
                    break
    
    # If not enough, search in Vietnamese names
    if len(suggestions) < max_suggestions:
        for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
            if ab_name in seen:
                continue
            if 'vietnamese_name' in ab_data:
                vn_names = ab_data['vietnamese_name'].split(',')
                for vn_name in vn_names:
                    if query_lower in vn_name.strip().lower():
                        suggestions.append(ab_name)
                        seen.add(ab_name)
                        break
                if len(suggestions) >= max_suggestions:
                    break
    
    return suggestions


def get_recent_searches():
    """Get recent antibiotic searches from session state"""
    return st.session_state.get('recent_antibiotic_searches', [])


def add_to_recent_searches(query):
    """Add search query to recent searches (max 10)"""
    if 'recent_antibiotic_searches' not in st.session_state:
        st.session_state.recent_antibiotic_searches = []
    
    recent = st.session_state.recent_antibiotic_searches
    
    # Remove if already exists
    if query in recent:
        recent.remove(query)
    
    # Add to beginning
    recent.insert(0, query)
    
    # Keep only last 10
    st.session_state.recent_antibiotic_searches = recent[:10]


def highlight_search_terms(text, query):
    """
    Highlight search terms in text using HTML
    Returns HTML string with highlighted terms
    """
    if not text or not query:
        return str(text) if text else ""
    
    import re
    import html
    
    # Escape HTML in text
    text_escaped = html.escape(str(text))
    query_escaped = html.escape(query)
    
    # Case-insensitive search and replace
    pattern = re.compile(re.escape(query_escaped), re.IGNORECASE)
    highlighted = pattern.sub(
        lambda m: f'<mark style="background-color: #FFEB3B; padding: 2px 4px; border-radius: 3px; font-weight: 600;">{m.group()}</mark>',
        text_escaped
    )
    
    return highlighted


def filter_antibiotics(group_filter="Tất cả", route_filter="Tất cả", aware_filter="Tất cả", 
                      pregnancy_filter="Tất cả", tdm_filter="Tất cả", frequency_filter="Tất cả"):
    """
    Filter antibiotics by group, route, AWaRe classification, pregnancy safety, TDM requirement, and dosing frequency
    
    Args:
        group_filter: Filter by antibiotic group
        route_filter: Filter by administration route (IV, IM, PO)
        aware_filter: Filter by AWaRe classification (ACCESS, WATCH, RESERVE)
        pregnancy_filter: Filter by FDA pregnancy category (A, B, C, D, X)
        tdm_filter: Filter by TDM requirement (Có, Không)
        frequency_filter: Filter by dosing frequency (q24h, q12h, q8h, q6h, Liên tục)
    
    Returns:
        Dict of filtered antibiotics
    """
    filtered = {}
    
    # TDM-requiring antibiotics (common ones)
    tdm_antibiotics = {"Vancomycin", "Gentamicin", "Tobramycin", "Amikacin", "Teicoplanin"}
    
    for ab_name, ab_data in ANTIBIOTICS_DATABASE.items():
        # Group filter
        if group_filter != "Tất cả":
            if ab_data.get('group', 'Khác') != group_filter:
                continue
        
        # Route filter
        if route_filter != "Tất cả":
            if route_filter not in ab_data.get('administration', []):
                continue
        
        # AWaRe filter
        if aware_filter != "Tất cả":
            if ab_data.get('aware_classification', '') != aware_filter:
                continue
        
        # Pregnancy filter
        if pregnancy_filter != "Tất cả":
            pregnancy_cat = ab_data.get('pregnancy', '')
            if not pregnancy_cat:
                enhanced = ab_data.get('enhanced_fields', {})
                if enhanced:
                    preg_lact = enhanced.get('pregnancy_lactation', {})
                    pregnancy_cat = preg_lact.get('fda_category', '')
            
            if pregnancy_cat != pregnancy_filter:
                continue
        
        # TDM filter (Phase 3)
        if tdm_filter != "Tất cả":
            requires_tdm = ab_name in tdm_antibiotics or ab_data.get('has_dosing_calculator', False)
            if tdm_filter == "Có" and not requires_tdm:
                continue
            if tdm_filter == "Không" and requires_tdm:
                continue
        
        # Frequency filter (Phase 3) - check in dosing info
        if frequency_filter != "Tất cả":
            # Check in dosing information
            dosing_info = ab_data.get('dosing', {})
            if isinstance(dosing_info, dict):
                # Check adult dosing
                adult_dosing = dosing_info.get('adult', {})
                if isinstance(adult_dosing, dict):
                    standard_dosing = adult_dosing.get('standard', {})
                    if isinstance(standard_dosing, dict):
                        interval = standard_dosing.get('interval', '')
                        frequency_lower = interval.lower()
                        
                        # Map frequency filter to intervals
                        frequency_map = {
                            "q24h": ["q24h", "24h", "once daily", "once"],
                            "q12h": ["q12h", "12h", "bid", "twice daily"],
                            "q8h": ["q8h", "8h", "tid", "three times daily"],
                            "q6h": ["q6h", "6h", "qid", "four times daily"],
                            "Liên tục": ["continuous", "infusion", "liên tục"]
                        }
                        
                        filter_intervals = frequency_map.get(frequency_filter, [])
                        if not any(freq in frequency_lower for freq in filter_intervals):
                            continue
            
            # If no dosing info found, skip this filter (don't exclude)
        
        filtered[ab_name] = ab_data
    
    return filtered

