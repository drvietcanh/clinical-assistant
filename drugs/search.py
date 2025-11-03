"""
Drug Search Functions
Enhanced search with autocomplete, recent searches, and smart scoring
Similar to antibiotics search but for general drug database
"""

import streamlit as st
from difflib import SequenceMatcher
from .drug_database import DRUG_DATABASE, DRUG_GROUPS


def similarity_score(str1, str2):
    """Calculate similarity score between two strings"""
    return SequenceMatcher(None, str1.lower(), str2.lower()).ratio()


def search_drugs(query, max_results=None):
    """Enhanced search drugs by name, Vietnamese name, group, or indication with scoring"""
    if not query:
        return []
    
    query_lower = query.lower().strip()
    results = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        score = 0.0
        
        # Search in name (highest priority)
        if query_lower in drug_name.lower():
            if query_lower == drug_name.lower():
                score = 1.0  # Exact match
            elif drug_name.lower().startswith(query_lower):
                score = 0.9  # Starts with query
            else:
                score = 0.8  # Contains query
            results.append((drug_name, drug_data, score))
            continue
        
        # Search in Vietnamese name
        if 'vietnamese_name' in drug_data:
            vn_name_lower = drug_data['vietnamese_name'].lower()
            if query_lower in vn_name_lower:
                score = 0.7
                results.append((drug_name, drug_data, score))
                continue
        
        # Search in group
        if 'group' in drug_data:
            group_lower = drug_data['group'].lower()
            if query_lower in group_lower:
                score = 0.6
                results.append((drug_name, drug_data, score))
                continue
        
        # Search in indications
        if 'indications' in drug_data:
            for indication in drug_data['indications']:
                if query_lower in indication.lower():
                    score = 0.5
                    results.append((drug_name, drug_data, score))
                    break
    
    # Sort by score (descending)
    results.sort(key=lambda x: x[2], reverse=True)
    
    # Return just (name, data) tuples for backward compatibility
    if max_results:
        return [(name, data) for name, data, score in results[:max_results]]
    return [(name, data) for name, data, score in results]


def get_drug_autocomplete_suggestions(query, max_suggestions=5):
    """
    Get autocomplete suggestions for drug search
    Returns list of drug names matching query
    """
    if not query or len(query) < 1:
        # Popular drugs
        return ["Metformin", "Omeprazole", "Paracetamol", "Ibuprofen", "Aspirin"]
    
    query_lower = query.lower()
    suggestions = []
    seen = set()
    
    # Search in names first (most relevant)
    for drug_name, drug_data in DRUG_DATABASE.items():
        if query_lower in drug_name.lower():
            if drug_name not in seen:
                suggestions.append(drug_name)
                seen.add(drug_name)
                if len(suggestions) >= max_suggestions:
                    break
    
    # If not enough, search in Vietnamese names
    if len(suggestions) < max_suggestions:
        for drug_name, drug_data in DRUG_DATABASE.items():
            if drug_name in seen:
                continue
            if 'vietnamese_name' in drug_data:
                vn_name_lower = drug_data['vietnamese_name'].lower()
                if query_lower in vn_name_lower:
                    suggestions.append(drug_name)
                    seen.add(drug_name)
                    if len(suggestions) >= max_suggestions:
                        break
    
    # If still not enough, use fuzzy matching
    if len(suggestions) < max_suggestions:
        fuzzy_results = []
        for drug_name, drug_data in DRUG_DATABASE.items():
            if drug_name in seen:
                continue
            sim = similarity_score(query, drug_name)
            if sim > 0.5:
                fuzzy_results.append((drug_name, sim))
        
        fuzzy_results.sort(key=lambda x: x[1], reverse=True)
        for drug_name, _ in fuzzy_results[:max_suggestions - len(suggestions)]:
            suggestions.append(drug_name)
    
    return suggestions


def get_recent_searches(max_recent=10):
    """Get recent drug searches from session state"""
    if 'drug_recent_searches' not in st.session_state:
        st.session_state.drug_recent_searches = []
    return st.session_state.drug_recent_searches[-max_recent:]


def add_recent_search(query):
    """Add a search query to recent searches"""
    if 'drug_recent_searches' not in st.session_state:
        st.session_state.drug_recent_searches = []
    
    # Remove if already exists
    if query in st.session_state.drug_recent_searches:
        st.session_state.drug_recent_searches.remove(query)
    
    # Add to front
    st.session_state.drug_recent_searches.insert(0, query)
    
    # Limit to max 10
    if len(st.session_state.drug_recent_searches) > 10:
        st.session_state.drug_recent_searches = st.session_state.drug_recent_searches[:10]


def get_popular_drugs():
    """Get popular/common drugs"""
    return [
        "Metformin", "Omeprazole", "Paracetamol", "Ibuprofen", "Aspirin",
        "Atorvastatin", "Metoprolol", "Amlodipine", "Losartan", "Furosemide"
    ]


def search_by_group(group_name):
    """Search drugs by group name"""
    results = []
    for drug_name, drug_data in DRUG_DATABASE.items():
        if 'group' in drug_data:
            if group_name.lower() in drug_data['group'].lower():
                results.append((drug_name, drug_data))
    return results


def search_by_indication(indication_query):
    """Search drugs by indication"""
    indication_lower = indication_query.lower()
    results = []
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        if 'indications' in drug_data:
            for indication in drug_data['indications']:
                if indication_lower in indication.lower():
                    results.append((drug_name, drug_data))
                    break
    
    return results

