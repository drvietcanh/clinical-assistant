"""
Advanced Search Features
- Multiple keywords search
- Drug interactions search
- Contraindications search
- Saved search queries
"""

import streamlit as st
from typing import List, Tuple, Dict, Any, Optional, Set
from .drug_database import DRUG_DATABASE
from .search_optimized import search_drugs_optimized
from utils.search_utils import fuzzy_match, calculate_search_score
import logging

logger = logging.getLogger(__name__)


def search_by_multiple_keywords(
    keywords: List[str],
    operator: str = "AND",  # "AND" or "OR"
    max_results: Optional[int] = None
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Search drugs by multiple keywords with AND/OR logic
    
    Args:
        keywords: List of search keywords
        operator: "AND" (all keywords must match) or "OR" (any keyword matches)
        max_results: Maximum number of results
    
    Returns:
        List of (drug_name, drug_data) tuples
    """
    if not keywords:
        return []
    
    try:
        # Search for each keyword
        keyword_results: Dict[str, Set[str]] = {}
        for keyword in keywords:
            results = search_drugs_optimized(keyword, use_index=True)
            keyword_results[keyword] = {name for name, _ in results}
        
        # Combine results based on operator
        if operator.upper() == "AND":
            # All keywords must match
            if not keyword_results:
                return []
            common_drugs = keyword_results[keywords[0]]
            for keyword in keywords[1:]:
                common_drugs = common_drugs.intersection(keyword_results.get(keyword, set()))
            result_names = list(common_drugs)
        else:  # OR
            # Any keyword matches
            result_names = set()
            for keyword in keywords:
                result_names.update(keyword_results.get(keyword, set()))
            result_names = list(result_names)
        
        # Get full drug data
        results = [(name, DRUG_DATABASE[name]) for name in result_names if name in DRUG_DATABASE]
        
        if max_results:
            return results[:max_results]
        return results
        
    except Exception as e:
        logger.error(f"Error in search_by_multiple_keywords: {e}", exc_info=True)
        return []


def search_by_interactions(
    drug_name: str,
    interaction_type: Optional[str] = None  # "major", "moderate", "minor", None for all
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Search drugs that interact with a given drug
    
    Args:
        drug_name: Name of the drug to check interactions
        interaction_type: Filter by interaction severity
    
    Returns:
        List of (drug_name, drug_data) tuples that interact
    """
    if drug_name not in DRUG_DATABASE:
        return []
    
    try:
        drug_data = DRUG_DATABASE[drug_name]
        interactions = drug_data.get('interactions', [])
        
        if not interactions:
            return []
        
        # Filter by interaction type if specified
        if interaction_type:
            interactions = [
                i for i in interactions
                if i.get('severity', '').lower() == interaction_type.lower()
            ]
        
        # Get interacting drug names
        interacting_drugs = []
        for interaction in interactions:
            interacting_drug = interaction.get('drug', '')
            if interacting_drug and interacting_drug in DRUG_DATABASE:
                interacting_drugs.append((interacting_drug, DRUG_DATABASE[interacting_drug]))
        
        return interacting_drugs
        
    except Exception as e:
        logger.error(f"Error in search_by_interactions: {e}", exc_info=True)
        return []


def search_by_contraindications(
    condition: str,
    max_results: Optional[int] = None
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Search drugs contraindicated for a condition
    
    Args:
        condition: Medical condition
        max_results: Maximum number of results
    
    Returns:
        List of (drug_name, drug_data) tuples
    """
    if not condition:
        return []
    
    try:
        condition_lower = condition.lower()
        results = []
        
        for drug_name, drug_data in DRUG_DATABASE.items():
            contraindications = drug_data.get('contraindications', [])
            
            # Check if condition matches any contraindication
            for contraindication in contraindications:
                if condition_lower in contraindication.lower():
                    results.append((drug_name, drug_data))
                    break
        
        if max_results:
            return results[:max_results]
        return results
        
    except Exception as e:
        logger.error(f"Error in search_by_contraindications: {e}", exc_info=True)
        return []


def save_search_query(name: str, query: str, filters: Optional[Dict[str, Any]] = None):
    """Save a search query for later use"""
    if 'saved_drug_searches' not in st.session_state:
        st.session_state.saved_drug_searches = {}
    
    st.session_state.saved_drug_searches[name] = {
        'query': query,
        'filters': filters or {},
        'timestamp': st.session_state.get('current_time', '')
    }


def get_saved_search_queries() -> Dict[str, Dict[str, Any]]:
    """Get all saved search queries"""
    return st.session_state.get('saved_drug_searches', {})


def load_saved_search(name: str) -> Optional[Tuple[str, Optional[Dict[str, Any]]]]:
    """Load a saved search query"""
    saved = st.session_state.get('saved_drug_searches', {})
    if name in saved:
        search_data = saved[name]
        return search_data.get('query', ''), search_data.get('filters')
    return None, None


def delete_saved_search(name: str):
    """Delete a saved search query"""
    if 'saved_drug_searches' in st.session_state:
        if name in st.session_state.saved_drug_searches:
            del st.session_state.saved_drug_searches[name]


__all__ = [
    'search_by_multiple_keywords',
    'search_by_interactions',
    'search_by_contraindications',
    'save_search_query',
    'get_saved_search_queries',
    'load_saved_search',
    'delete_saved_search',
]

