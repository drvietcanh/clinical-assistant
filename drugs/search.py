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


def search_drugs_with_filters(query="", filters=None):
    """
    Search drugs with advanced filters
    filters: dict with keys: groups, routes, pregnancy, requires_monitoring, has_renal_adjustment, has_black_box
    """
    if filters is None:
        filters = {}
    
    # First, get base results from query
    if query:
        base_results = search_drugs(query)
        # Convert to dict for easier filtering
        base_drugs = {name: data for name, data in base_results}
    else:
        base_drugs = DRUG_DATABASE
    
    results = []
    
    for drug_name, drug_data in base_drugs.items():
        # Filter by groups
        if 'groups' in filters and filters['groups']:
            if 'group' not in drug_data:
                continue
            group_match = False
            for filter_group in filters['groups']:
                if filter_group.lower() in drug_data['group'].lower():
                    group_match = True
                    break
            if not group_match:
                continue
        
        # Filter by routes
        if 'routes' in filters and filters['routes']:
            if 'administration' not in drug_data:
                continue
            route_match = False
            for filter_route in filters['routes']:
                if filter_route in drug_data['administration']:
                    route_match = True
                    break
            if not route_match:
                continue
        
        # Filter by pregnancy category
        if 'pregnancy' in filters and filters['pregnancy'] and filters['pregnancy'] != "All":
            if 'pregnancy' not in drug_data:
                continue
            if drug_data['pregnancy'] != filters['pregnancy']:
                continue
        
        # Filter by requires monitoring
        if 'requires_monitoring' in filters and filters['requires_monitoring']:
            if 'monitoring' not in drug_data or not drug_data['monitoring']:
                continue
        
        # Filter by has renal adjustment
        if 'has_renal_adjustment' in filters and filters['has_renal_adjustment']:
            if 'renal_adjustment' not in drug_data or not drug_data['renal_adjustment']:
                continue
        
        # Filter by has black box warning
        if 'has_black_box' in filters and filters['has_black_box']:
            if 'black_box_warnings' not in drug_data or not drug_data['black_box_warnings']:
                continue
        
        results.append((drug_name, drug_data))
    
    return results


def highlight_search_term(text, query):
    """Highlight search term in text"""
    if not query or not text:
        return text
    
    import re
    # Escape special regex characters
    escaped_query = re.escape(query)
    # Case-insensitive pattern
    pattern = re.compile(escaped_query, re.IGNORECASE)
    # Replace with highlighted version
    highlighted = pattern.sub(
        lambda m: f"<mark style='background: #fef08a; padding: 2px 4px; border-radius: 3px; font-weight: 600;'>{m.group()}</mark>",
        text
    )
    return highlighted


def save_search(name, query, filters=None):
    """Save search with name, query, and filters"""
    if 'drug_saved_searches' not in st.session_state:
        st.session_state.drug_saved_searches = {}
    
    st.session_state.drug_saved_searches[name] = {
        'query': query,
        'filters': filters or {}
    }


def get_saved_searches():
    """Get all saved searches"""
    if 'drug_saved_searches' not in st.session_state:
        st.session_state.drug_saved_searches = {}
    return st.session_state.drug_saved_searches


def load_saved_search(name):
    """Load saved search by name"""
    if 'drug_saved_searches' not in st.session_state:
        return None, None
    saved = st.session_state.drug_saved_searches.get(name)
    if saved:
        return saved.get('query', ''), saved.get('filters', {})
    return None, None


def delete_saved_search(name):
    """Delete saved search by name"""
    if 'drug_saved_searches' not in st.session_state:
        return
    if name in st.session_state.drug_saved_searches:
        del st.session_state.drug_saved_searches[name]
