"""
Drug Search Functions - Wrapper
Re-exports search functions from drugs.search for use in drug_info_components
"""

# Import all search functions from parent module
from ..search import (
    search_drugs,
    search_drugs_with_filters,
    get_drug_autocomplete_suggestions,
    get_recent_searches,
    add_recent_search,
    search_by_group,
    search_by_indication,
    search_by_side_effect,
    search_by_contraindication,
    save_search,
    get_saved_searches,
    load_saved_search,
    delete_saved_search,
    highlight_search_term,
    get_related_interactions
)

__all__ = [
    'search_drugs',
    'search_drugs_with_filters',
    'get_drug_autocomplete_suggestions',
    'get_recent_searches',
    'add_recent_search',
    'search_by_group',
    'search_by_indication',
    'search_by_side_effect',
    'search_by_contraindication',
    'save_search',
    'get_saved_searches',
    'load_saved_search',
    'delete_saved_search',
    'highlight_search_term',
    'get_related_interactions'
]

