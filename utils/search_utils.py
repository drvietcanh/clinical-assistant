"""
Shared Search Utilities
Common search functions extracted for reuse
"""

from typing import List, Tuple, Dict, Any, Optional
from difflib import SequenceMatcher
import logging

logger = logging.getLogger(__name__)


def fuzzy_match(query: str, text: str, threshold: float = 0.6) -> float:
    """
    Calculate fuzzy matching score between query and text
    
    Args:
        query: Search query
        text: Text to match against
        threshold: Minimum similarity threshold
    
    Returns:
        Similarity score (0-1)
    """
    try:
        query_lower = query.lower()
        text_lower = text.lower()
        
        # Exact match gets highest score
        if query_lower in text_lower:
            return 1.0
        
        # Word-level matching
        query_words = query_lower.split()
        text_words = text_lower.split()
        
        word_matches = sum(1 for qw in query_words if any(qw in tw or tw in qw for tw in text_words))
        word_score = word_matches / len(query_words) if query_words else 0
        
        # Character-level similarity
        char_score = SequenceMatcher(None, query_lower, text_lower).ratio()
        
        # Combined score (weighted)
        combined_score = (word_score * 0.6 + char_score * 0.4)
        
        return combined_score if combined_score >= threshold else 0.0
    except Exception as e:
        logger.error(f"Error in fuzzy_match: {e}", exc_info=True)
        return 0.0


def calculate_search_score(
    query: str,
    name: str,
    category: str = "",
    vietnamese_name: str = "",
    boost_factor: float = 0.0
) -> float:
    """
    Calculate search relevance score for a drug/calculator
    
    Args:
        query: Search query
        name: Primary name
        category: Category name
        vietnamese_name: Vietnamese name (optional)
        boost_factor: Additional boost (0-1)
    
    Returns:
        Relevance score (0-1)
    """
    query_lower = query.lower()
    score = 0.0
    
    # Exact match in name (highest priority)
    if query_lower == name.lower():
        score = 1.0
    elif name.lower().startswith(query_lower):
        score = 0.9
    elif query_lower in name.lower():
        score = 0.8
    
    # Match in category
    elif category and query_lower in category.lower():
        score = 0.7
    
    # Match in Vietnamese name
    elif vietnamese_name and query_lower in vietnamese_name.lower():
        score = 0.6
    
    # Fuzzy matching
    else:
        name_score = fuzzy_match(query, name)
        category_score = fuzzy_match(query, category) if category else 0
        vn_score = fuzzy_match(query, vietnamese_name) if vietnamese_name else 0
        score = max(name_score, category_score * 0.7, vn_score * 0.6)
    
    # Apply boost
    if boost_factor > 0:
        score = min(1.0, score + boost_factor)
    
    return score


def filter_by_category(
    items: List[Tuple[str, Dict[str, Any]]],
    category_filter: Optional[str] = None,
    category_key: str = 'category'
) -> List[Tuple[str, Dict[str, Any]]]:
    """
    Filter items by category
    
    Args:
        items: List of (id, data) tuples
        category_filter: Category to filter by
        category_key: Key in data dict for category
    
    Returns:
        Filtered list
    """
    if not category_filter:
        return items
    
    category_lower = category_filter.lower()
    return [
        (item_id, item_data)
        for item_id, item_data in items
        if item_data.get(category_key, '').lower() == category_lower
    ]


def sort_by_relevance(
    results: List[Tuple[str, Dict[str, Any], float]],
    reverse: bool = True
) -> List[Tuple[str, Dict[str, Any], float]]:
    """
    Sort search results by relevance score
    
    Args:
        results: List of (id, data, score) tuples
        reverse: Sort descending (highest score first)
    
    Returns:
        Sorted list
    """
    return sorted(results, key=lambda x: x[2], reverse=reverse)


def highlight_search_terms(text: str, query: str) -> str:
    """
    Highlight search terms in text
    
    Args:
        text: Text to highlight
        query: Search query
    
    Returns:
        HTML with highlighted terms
    """
    if not query or not text:
        return text
    
    try:
        import re
        escaped_query = re.escape(query)
        pattern = re.compile(escaped_query, re.IGNORECASE)
        highlighted = pattern.sub(
            lambda m: f"<mark style='background: #fef08a; padding: 2px 4px; border-radius: 3px; font-weight: 600;'>{m.group()}</mark>",
            text
        )
        return highlighted
    except Exception as e:
        logger.error(f"Error in highlight_search_terms: {e}", exc_info=True)
        return text


__all__ = [
    'fuzzy_match',
    'calculate_search_score',
    'filter_by_category',
    'sort_by_relevance',
    'highlight_search_terms',
]

