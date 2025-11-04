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
    """Enhanced search antibiotics by name, Vietnamese name, group, or indication with scoring"""
    query_lower = query.lower()
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
    if max_results:
        return [(name, data) for name, data, score in results[:max_results]]
    return [(name, data) for name, data, score in results]


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


def filter_antibiotics(group_filter="Tất cả", route_filter="Tất cả", aware_filter="Tất cả"):
    """Filter antibiotics by group, route, and AWaRe classification"""
    filtered = {}
    
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
        
        filtered[ab_name] = ab_data
    
    return filtered

