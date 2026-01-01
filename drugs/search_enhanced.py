"""
Enhanced Drug Search with Performance Optimization
Version 2.0 - With Search Index and Caching
"""

import streamlit as st
from difflib import SequenceMatcher
from functools import lru_cache
import logging
import time

# Import drug database
try:
    from .drug_database import DRUG_DATABASE, DRUG_GROUPS
except ImportError:
    from drug_database import DRUG_DATABASE, DRUG_GROUPS

# Import search index
try:
    from .drug_search_index import DrugSearchIndex
except ImportError:
    from drug_search_index import DrugSearchIndex

# Setup logger
logger = logging.getLogger(__name__)

# Global search index (lazy initialization)
_search_index = None


def get_search_index():
    """Get or create search index (singleton pattern)"""
    global _search_index
    if _search_index is None:
        logger.info("Initializing drug search index...")
        start_time = time.time()
        _search_index = DrugSearchIndex()
        
        # Use new drug_modules if available, fallback to DRUG_DATABASE
        try:
            from drug_modules import ALL_DRUGS
            _search_index.build_index(ALL_DRUGS)
        except ImportError:
            _search_index.build_index(DRUG_DATABASE)
        
        elapsed = time.time() - start_time
        logger.info(f"Search index built in {elapsed:.2f}s")
    
    return _search_index


# ==================== CACHED FUNCTIONS ====================

@lru_cache(maxsize=256)
def get_drug_cached(drug_name: str):
    """
    Get drug info with caching
    Frequently accessed drugs are cached for instant retrieval
    """
    try:
        from drug_modules import ALL_DRUGS
        return ALL_DRUGS.get(drug_name)
    except ImportError:
        return DRUG_DATABASE.get(drug_name)


@lru_cache(maxsize=128)
def search_by_group_cached(group: str):
    """Cached group search"""
    index = get_search_index()
    drug_names = index.search_by_group(group)
    
    # Get full drug data
    results = []
    for name in drug_names:
        drug_data = get_drug_cached(name)
        if drug_data:
            results.append((name, drug_data, 1.0))  # Score 1.0 for group match
    
    return results


# ==================== ENHANCED SEARCH FUNCTIONS ====================

def search_drugs_fast(query, max_results=None):
    """
    Fast drug search using search index
    Replaces old O(n) linear search with O(1) index lookup
    
    Args:
        query: Search query
        max_results: Maximum results to return
    
    Returns:
        List of (drug_name, drug_data, score) tuples
    """
    if not query:
        return []
    
    try:
        index = get_search_index()
        query_lower = query.lower().strip()
        results = []
        
        # 1. Try exact name match first (O(1))
        exact_match = index.search_by_name(query_lower)
        if exact_match:
            # Find original case name
            for name in DRUG_DATABASE.keys():
                if name.lower() == query_lower:
                    results.append((name, exact_match, 1.0))
                    break
        
        # 2. Try Vietnamese name
        vn_match = index.search_by_vietnamese_name(query_lower)
        if vn_match and not exact_match:
            for name in DRUG_DATABASE.keys():
                drug_data = DRUG_DATABASE[name]
                if drug_data.get('vietnamese_name', '').lower() == query_lower:
                    results.append((name, vn_match, 0.95))
                    break
        
        # 3. Try brand name
        brand_match = index.search_by_brand(query_lower)
        if brand_match and not exact_match and not vn_match:
            for name in DRUG_DATABASE.keys():
                if name.lower() == query_lower:
                    results.append((name, brand_match, 0.9))
                    break
        
        # 4. If no exact match, try autocomplete (partial match)
        if not results:
            suggestions = index.autocomplete(query, limit=20)
            for drug_name in suggestions:
                drug_data = get_drug_cached(drug_name)
                if drug_data:
                    # Score based on how early the match appears
                    if drug_name.lower().startswith(query_lower):
                        score = 0.85
                    else:
                        score = 0.75
                    results.append((drug_name, drug_data, score))
        
        # 5. If still no results, try fuzzy search
        if not results:
            fuzzy_matches = index.fuzzy_search(query, max_results=10)
            for drug_name_lower, similarity in fuzzy_matches:
                # Find original case
                for name in DRUG_DATABASE.keys():
                    if name.lower() == drug_name_lower:
                        drug_data = get_drug_cached(name)
                        if drug_data:
                            results.append((name, drug_data, similarity * 0.7))
                        break
        
        # 6. Search by indication (if query looks like a condition)
        if len(query) > 5:  # Only for longer queries
            indication_matches = index.search_by_indication(query)
            for drug_name in indication_matches[:10]:  # Limit to 10
                if not any(r[0] == drug_name for r in results):  # Avoid duplicates
                    drug_data = get_drug_cached(drug_name)
                    if drug_data:
                        results.append((drug_name, drug_data, 0.6))
        
        # Sort by score (descending)
        results.sort(key=lambda x: x[2], reverse=True)
        
        # Limit results
        if max_results:
            results = results[:max_results]
        
        return results
    
    except Exception as e:
        logger.error(f"Error in fast search: {e}")
        # Fallback to old search
        return search_drugs_legacy(query, max_results)


def search_drugs_legacy(query, max_results=None):
    """
    Legacy O(n) search - Fallback if index fails
    Original implementation from search.py
    """
    if not query:
        return []
    
    try:
        query_lower = query.lower().strip()
        results = []
        
        for drug_name, drug_data in DRUG_DATABASE.items():
            score = 0.0
            
            # Search in name
            if query_lower in drug_name.lower():
                if query_lower == drug_name.lower():
                    score = 1.0
                elif drug_name.lower().startswith(query_lower):
                    score = 0.9
                else:
                    score = 0.8
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
        
        # Sort by score
        results.sort(key=lambda x: x[2], reverse=True)
        
        if max_results:
            results = results[:max_results]
        
        return results
    
    except Exception as e:
        logger.error(f"Error in legacy search: {e}")
        return []


# Main search function - uses fast search by default
def search_drugs(query, max_results=None, use_fast=True):
    """
    Main search function with automatic fallback
    
    Args:
        query: Search query
        max_results: Max results
        use_fast: Use fast indexed search (default True)
    
    Returns:
        List of (drug_name, drug_data, score) tuples
    """
    if use_fast:
        return search_drugs_fast(query, max_results)
    else:
        return search_drugs_legacy(query, max_results)


# ==================== AUTOCOMPLETE ====================

def get_drug_autocomplete_suggestions(query, limit=10):
    """
    Fast autocomplete using search index
    
    Args:
        query: Partial drug name (min 3 chars)
        limit: Max suggestions
    
    Returns:
        List of drug names
    """
    if len(query) < 3:
        return []
    
    try:
        index = get_search_index()
        suggestions = index.autocomplete(query, limit=limit)
        return suggestions
    except Exception as e:
        logger.error(f"Autocomplete error: {e}")
        return []


# ==================== SPECIALIZED SEARCHES ====================

def search_by_group(group_name):
    """
    Search drugs by therapeutic group (cached)
    
    Args:
        group_name: Group name (e.g., "Cardiovascular", "Diabetes")
    
    Returns:
        List of (drug_name, drug_data, score) tuples
    """
    return search_by_group_cached(group_name)


def search_by_indication(indication):
    """
    Search drugs by indication
    
    Args:
        indication: Indication/condition (e.g., "hypertension", "diabetes")
    
    Returns:
        List of (drug_name, drug_data, score) tuples
    """
    try:
        index = get_search_index()
        drug_names = index.search_by_indication(indication)
        
        results = []
        for name in drug_names:
            drug_data = get_drug_cached(name)
            if drug_data:
                results.append((name, drug_data, 0.8))
        
        return results
    except Exception as e:
        logger.error(f"Indication search error: {e}")
        return []


def search_drugs_with_filters(filters):
    """
    Advanced multi-criteria search
    
    Args:
        filters: Dictionary of filters
            {
                'group': 'Cardiovascular',
                'indication': 'hypertension',
                'route': 'PO',
                'exclude_pregnancy_x': True
            }
    
    Returns:
        List of (drug_name, drug_data, score) tuples
    """
    try:
        index = get_search_index()
        drug_names = index.advanced_search(filters)
        
        results = []
        for name in drug_names:
            drug_data = get_drug_cached(name)
            if drug_data:
                results.append((name, drug_data, 0.9))
        
        return results
    except Exception as e:
        logger.error(f"Filter search error: {e}")
        return []


# ==================== UTILITY FUNCTIONS ====================

def get_search_statistics():
    """Get search index statistics"""
    try:
        index = get_search_index()
        return index.get_statistics()
    except Exception as e:
        logger.error(f"Stats error: {e}")
        return {}


def clear_search_cache():
    """Clear LRU caches"""
    get_drug_cached.cache_clear()
    search_by_group_cached.cache_clear()
    logger.info("Search cache cleared")


# ==================== BACKWARD COMPATIBILITY ====================
# Keep old function names for compatibility

def search_by_side_effect(side_effect):
    """Search by side effect (legacy)"""
    return search_drugs(side_effect, max_results=20)


def search_by_contraindication(contraindication):
    """Search by contraindication (legacy)"""
    return search_drugs(contraindication, max_results=20)


def highlight_search_term(text, search_term):
    """Highlight search term in text"""
    if not search_term or not text:
        return text
    
    import re
    pattern = re.compile(re.escape(search_term), re.IGNORECASE)
    return pattern.sub(lambda m: f"**{m.group()}**", text)


# ==================== SESSION STATE FUNCTIONS ====================

def get_recent_searches():
    """Get recent searches from session state"""
    if 'recent_searches' not in st.session_state:
        st.session_state.recent_searches = []
    return st.session_state.recent_searches


def add_recent_search(query):
    """Add to recent searches"""
    if 'recent_searches' not in st.session_state:
        st.session_state.recent_searches = []
    
    # Remove if already exists
    if query in st.session_state.recent_searches:
        st.session_state.recent_searches.remove(query)
    
    # Add to front
    st.session_state.recent_searches.insert(0, query)
    
    # Keep only last 10
    st.session_state.recent_searches = st.session_state.recent_searches[:10]


def save_search(name, filters):
    """Save search with filters"""
    if 'saved_searches' not in st.session_state:
        st.session_state.saved_searches = {}
    st.session_state.saved_searches[name] = filters


def get_saved_searches():
    """Get saved searches"""
    if 'saved_searches' not in st.session_state:
        st.session_state.saved_searches = {}
    return st.session_state.saved_searches


def load_saved_search(name):
    """Load saved search"""
    saved = get_saved_searches()
    return saved.get(name)


def delete_saved_search(name):
    """Delete saved search"""
    if 'saved_searches' in st.session_state:
        if name in st.session_state.saved_searches:
            del st.session_state.saved_searches[name]


def get_related_interactions(drug_name):
    """Get related drug interactions (placeholder)"""
    # TODO: Implement drug interaction database
    return []


# ==================== EXPORTS ====================

__all__ = [
    'search_drugs',
    'search_drugs_fast',
    'search_drugs_legacy',
    'search_drugs_with_filters',
    'get_drug_autocomplete_suggestions',
    'search_by_group',
    'search_by_indication',
    'search_by_side_effect',
    'search_by_contraindication',
    'get_recent_searches',
    'add_recent_search',
    'save_search',
    'get_saved_searches',
    'load_saved_search',
    'delete_saved_search',
    'highlight_search_term',
    'get_related_interactions',
    'get_search_statistics',
    'clear_search_cache',
    'get_drug_cached'
]
