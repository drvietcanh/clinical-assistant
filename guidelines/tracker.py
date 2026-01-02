"""
Guidelines Tracker Functions
Track and monitor guideline updates
"""

from typing import List, Optional, Dict
from datetime import datetime
from guidelines.data import (
    GUIDELINES_DATABASE,
    get_guidelines_by_category,
    get_guidelines_by_organization,
    Guideline
)


def get_guideline_info(guideline_id: str) -> Optional[Guideline]:
    """
    Get detailed information about a guideline
    
    Args:
        guideline_id: Guideline ID
        
    Returns:
        Guideline object or None
    """
    for guideline in GUIDELINES_DATABASE:
        if guideline.id == guideline_id:
            return guideline
    return None


def check_guideline_updates(year_threshold: int = 2020) -> List[Guideline]:
    """
    Check for guidelines that may need updates
    (Guidelines older than year_threshold)
    
    Args:
        year_threshold: Year threshold for considering guidelines "old"
        
    Returns:
        List of guidelines that may need updates
    """
    return [g for g in GUIDELINES_DATABASE if g.year < year_threshold]


def get_recent_guidelines(limit: int = 10, min_year: int = 2020) -> List[Guideline]:
    """
    Get most recent guidelines
    
    Args:
        limit: Maximum number of guidelines to return
        min_year: Minimum year to include
        
    Returns:
        List of recent guidelines sorted by year
    """
    recent = [g for g in GUIDELINES_DATABASE if g.year >= min_year]
    recent.sort(key=lambda x: x.year, reverse=True)
    return recent[:limit]


def search_guidelines(query: str, category: Optional[str] = None) -> List[Guideline]:
    """
    Search guidelines by title or description
    
    Args:
        query: Search query
        category: Optional category filter
        
    Returns:
        List of matching guidelines
    """
    if not query:
        return []
    
    query_lower = query.lower().strip()
    
    # Get guidelines to search
    guidelines_to_search = get_guidelines_by_category(category) if category else GUIDELINES_DATABASE
    
    results = []
    for guideline in guidelines_to_search:
        # Search in title (English and Vietnamese)
        # Search content (Titles, Description, Org, Content, Protocol)
        search_content = [
            guideline.title,
            guideline.title_vn,
            guideline.description,
            guideline.organization,
            str(guideline.related_protocol) if guideline.related_protocol else ""
        ]
        
        # Add key recommendations to search
        if guideline.key_recommendations:
            search_content.extend(guideline.key_recommendations)
            
        # Check if query is in any of the content
        found = False
        for content in search_content:
            if query_lower in content.lower():
                found = True
                break
        
        if found:
            results.append(guideline)
    
    return results


def get_search_suggestions(query: str, limit: int = 5) -> List[str]:
    """
    Get autocomplete suggestions for search query
    
    Args:
        query: Partial search query
        limit: Maximum number of suggestions
        
    Returns:
        List of suggested search terms
    """
    if not query or len(query) < 2:
        return []
    
    query_lower = query.lower().strip()
    suggestions = set()
    
    # Common search terms
    common_terms = [
        "Heart Failure", "Sepsis", "Diabetes", "Hypertension", "COPD", "Asthma",
        "AHA", "ACC", "ESC", "IDSA", "KDIGO", "GOLD", "GINA", "SSC", "ADA",
        "Cardiology", "Infectious", "Respiratory", "Nephrology", "Endocrinology",
        "Neurology", "Critical Care", "Emergency", "ACS", "AKI", "CKD"
    ]
    
    # Match against common terms
    for term in common_terms:
        if query_lower in term.lower():
            suggestions.add(term)
            if len(suggestions) >= limit:
                break
    
    # Also get suggestions from guideline titles
    for guideline in GUIDELINES_DATABASE:
        if len(suggestions) >= limit:
            break
        title_words = guideline.title_vn.split() + guideline.title.split()
        for word in title_words:
            if len(word) > 3 and query_lower in word.lower():
                suggestions.add(word)
                if len(suggestions) >= limit:
                    break
    
    return sorted(list(suggestions))[:limit]


def get_guidelines_by_year(year: int) -> List[Guideline]:
    """
    Get guidelines from a specific year
    
    Args:
        year: Year to filter by
        
    Returns:
        List of guidelines from that year
    """
    return [g for g in GUIDELINES_DATABASE if g.year == year]


def compare_guideline_versions(guideline_id: str) -> Optional[Dict]:
    """
    Compare different versions of a guideline (if multiple versions exist)
    
    Args:
        guideline_id: Base guideline ID (without year)
        
    Returns:
        Dictionary with version comparison or None
    """
    # Find all guidelines with similar ID (same base)
    base_id = guideline_id.rsplit('_', 1)[0] if '_' in guideline_id else guideline_id
    versions = [g for g in GUIDELINES_DATABASE if base_id in g.id]
    
    if len(versions) < 2:
        return None
    
    versions.sort(key=lambda x: x.year, reverse=True)
    
    return {
        "latest": versions[0],
        "previous": versions[1:] if len(versions) > 1 else [],
        "total_versions": len(versions)
    }

