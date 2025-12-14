"""
Optimized Drug Search Functions
- Caching for search results
- Index-based search for faster lookups
- Error logging
"""

import streamlit as st
from difflib import SequenceMatcher
from typing import List, Tuple, Dict, Any, Optional
import logging
from functools import lru_cache
from utils.search_utils import fuzzy_match, calculate_search_score
from utils.performance_monitor import measure_time, track_search_performance

# Setup logging
logger = logging.getLogger(__name__)

# Try to use streamlit cache, fallback to lru_cache
try:
    from streamlit.runtime.caching import cache_data_api
    
    def _cache_search(func):
        """Cache search results using streamlit cache"""
        @st.cache_data(ttl=300, max_entries=100)  # Cache 5 minutes, max 100 entries
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)
        return cached_func
except (ImportError, AttributeError):
    # Fallback to lru_cache if streamlit cache not available
    def _cache_search(func):
        @lru_cache(maxsize=100)
        def cached_func(*args, **kwargs):
            return func(*args, **kwargs)
        return cached_func


# Index cache for groups/keywords
_GROUP_INDEX: Optional[Dict[str, List[str]]] = None
_KEYWORD_INDEX: Optional[Dict[str, List[str]]] = None


def _build_group_index():
    """Build index for group-based search - O(1) lookup"""
    global _GROUP_INDEX
    
    if _GROUP_INDEX is None:
        try:
            from .drug_database import DRUG_DATABASE
            
            _GROUP_INDEX = {}
            for drug_name, drug_data in DRUG_DATABASE.items():
                if 'group' in drug_data:
                    group = drug_data['group'].lower()
                    if group not in _GROUP_INDEX:
                        _GROUP_INDEX[group] = []
                    _GROUP_INDEX[group].append(drug_name)
            
            logger.info(f"Built group index with {len(_GROUP_INDEX)} groups")
        except Exception as e:
            logger.error(f"Error building group index: {e}", exc_info=True)
            _GROUP_INDEX = {}
    
    return _GROUP_INDEX


def _build_keyword_index():
    """Build index for keyword-based search"""
    global _KEYWORD_INDEX
    
    if _KEYWORD_INDEX is None:
        try:
            from .drug_database import DRUG_DATABASE
            
            _KEYWORD_INDEX = {}
            for drug_name, drug_data in DRUG_DATABASE.items():
                # Index by drug name words
                name_words = drug_name.lower().split()
                for word in name_words:
                    if len(word) > 2:  # Only index words > 2 chars
                        if word not in _KEYWORD_INDEX:
                            _KEYWORD_INDEX[word] = []
                        _KEYWORD_INDEX[word].append(drug_name)
                
                # Index by Vietnamese name words
                if 'vietnamese_name' in drug_data:
                    vn_words = drug_data['vietnamese_name'].lower().split()
                    for word in vn_words:
                        if len(word) > 2:
                            if word not in _KEYWORD_INDEX:
                                _KEYWORD_INDEX[word] = []
                            if drug_name not in _KEYWORD_INDEX[word]:
                                _KEYWORD_INDEX[word].append(drug_name)
            
            logger.info(f"Built keyword index with {len(_KEYWORD_INDEX)} keywords")
        except Exception as e:
            logger.error(f"Error building keyword index: {e}", exc_info=True)
            _KEYWORD_INDEX = {}
    
    return _KEYWORD_INDEX


def similarity_score(str1: str, str2: str) -> float:
    """Calculate similarity score between two strings (deprecated - use fuzzy_match)"""
    return fuzzy_match(str1, str2)


@_cache_search
@measure_time(operation_name='search_drugs_optimized')
def search_drugs_optimized(
    query: str,
    max_results: Optional[int] = None,
    use_index: bool = True
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Optimized search drugs with caching and indexing
    
    Args:
        query: Search query
        max_results: Maximum number of results
        use_index: Use index-based search for faster lookup
    
    Returns:
        List of (drug_name, drug_data) tuples sorted by relevance
    """
    if not query:
        return []
    
    try:
        query_lower = query.lower().strip()
        results = []
        
        # Use index for faster lookup if enabled
        if use_index and len(query_lower) > 2:
            keyword_index = _build_keyword_index()
            candidate_drugs = set()
            
            # Get candidates from index
            query_words = query_lower.split()
            for word in query_words:
                if word in keyword_index:
                    candidate_drugs.update(keyword_index[word])
            
            # Search only in candidates (much faster)
            search_space = candidate_drugs if candidate_drugs else None
        else:
            search_space = None
        
        from .drug_database import DRUG_DATABASE
        
        # Determine search space
        if search_space:
            items_to_search = [(name, DRUG_DATABASE[name]) for name in search_space if name in DRUG_DATABASE]
        else:
            items_to_search = DRUG_DATABASE.items()
        
        for drug_name, drug_data in items_to_search:
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
        result_tuples = [(name, data) for name, data, score in results]
        
        if max_results:
            return result_tuples[:max_results]
        return result_tuples
        
    except Exception as e:
        logger.error(f"Error in search_drugs_optimized: {e}", exc_info=True)
        return []


def search_by_group_optimized(group_keywords: List[str]) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Optimized search by group using index - O(1) lookup instead of O(n)
    
    Args:
        group_keywords: List of group keywords to search
    
    Returns:
        List of (drug_name, drug_data) tuples
    """
    if not group_keywords:
        return []
    
    try:
        group_index = _build_group_index()
        from .drug_database import DRUG_DATABASE
        
        results = []
        keywords_lower = [kw.lower() for kw in group_keywords]
        seen_drugs = set()
        
        # Use index for O(1) lookup
        for keyword in keywords_lower:
            # Direct group match
            if keyword in group_index:
                for drug_name in group_index[keyword]:
                    if drug_name not in seen_drugs:
                        results.append((drug_name, DRUG_DATABASE[drug_name]))
                        seen_drugs.add(drug_name)
            
            # Partial group match
            for group, drug_names in group_index.items():
                if keyword in group:
                    for drug_name in drug_names:
                        if drug_name not in seen_drugs:
                            results.append((drug_name, DRUG_DATABASE[drug_name]))
                            seen_drugs.add(drug_name)
        
        return results
        
    except Exception as e:
        logger.error(f"Error in search_by_group_optimized: {e}", exc_info=True)
        return []


@_cache_search
def get_drug_autocomplete_suggestions_optimized(
    query: str,
    max_suggestions: int = 5
) -> List[str]:
    """
    Optimized autocomplete with caching and indexing
    
    Args:
        query: Search query
        max_suggestions: Maximum number of suggestions
    
    Returns:
        List of drug names
    """
    if not query or len(query) < 1:
        # Popular drugs
        return ["Metformin", "Omeprazole", "Paracetamol", "Ibuprofen", "Aspirin"]
    
    try:
        query_lower = query.lower()
        suggestions = []
        seen = set()
        
        # Use keyword index for faster lookup
        keyword_index = _build_keyword_index()
        
        if len(query_lower) > 2 and query_lower in keyword_index:
            # Direct keyword match
            for drug_name in keyword_index[query_lower]:
                if drug_name not in seen:
                    suggestions.append(drug_name)
                    seen.add(drug_name)
                    if len(suggestions) >= max_suggestions:
                        break
        
        # If not enough, search in names
        if len(suggestions) < max_suggestions:
            from .drug_database import DRUG_DATABASE
            for drug_name, drug_data in DRUG_DATABASE.items():
                if drug_name in seen:
                    continue
                if query_lower in drug_name.lower():
                    suggestions.append(drug_name)
                    seen.add(drug_name)
                    if len(suggestions) >= max_suggestions:
                        break
        
        # If still not enough, use fuzzy matching
        if len(suggestions) < max_suggestions:
            from .drug_database import DRUG_DATABASE
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
        
    except Exception as e:
        logger.error(f"Error in get_drug_autocomplete_suggestions_optimized: {e}", exc_info=True)
        return []


def clear_search_cache():
    """Clear search cache (useful for testing or when database updates)"""
    global _GROUP_INDEX, _KEYWORD_INDEX
    _GROUP_INDEX = None
    _KEYWORD_INDEX = None
    
    # Clear streamlit cache if available
    try:
        st.cache_data.clear()
    except:
        pass
    
    logger.info("Search cache cleared")


__all__ = [
    'search_drugs_optimized',
    'search_by_group_optimized',
    'get_drug_autocomplete_suggestions_optimized',
    'clear_search_cache',
    '_build_group_index',
    '_build_keyword_index',
]

