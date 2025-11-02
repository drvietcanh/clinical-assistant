"""
Enhanced State Management
Type-safe state management with save/load functionality
"""

import streamlit as st
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field, asdict
import json


@dataclass
class AppState:
    """
    Application state container with type safety
    
    Attributes:
        favorites: List of favorite calculator IDs
        recently_used: List of recently used calculator IDs (most recent first)
        total_calculations: Total number of calculations performed
        user_preferences: User preferences dictionary
        search_history: Recent search queries
    """
    favorites: List[str] = field(default_factory=list)
    recently_used: List[str] = field(default_factory=list)
    total_calculations: int = 0
    user_preferences: Dict[str, Any] = field(default_factory=dict)
    search_history: List[str] = field(default_factory=list)
    
    # Maximum sizes
    MAX_RECENTLY_USED = 20
    MAX_SEARCH_HISTORY = 10
    
    def add_favorite(self, calc_id: str) -> None:
        """Add calculator to favorites"""
        if calc_id not in self.favorites:
            self.favorites.append(calc_id)
    
    def remove_favorite(self, calc_id: str) -> None:
        """Remove calculator from favorites"""
        if calc_id in self.favorites:
            self.favorites.remove(calc_id)
    
    def add_recently_used(self, calc_id: str) -> None:
        """Add calculator to recently used (most recent first)"""
        # Remove if already exists
        if calc_id in self.recently_used:
            self.recently_used.remove(calc_id)
        
        # Add to beginning
        self.recently_used.insert(0, calc_id)
        
        # Limit size
        if len(self.recently_used) > self.MAX_RECENTLY_USED:
            self.recently_used = self.recently_used[:self.MAX_RECENTLY_USED]
    
    def add_search_history(self, query: str) -> None:
        """Add search query to history"""
        if not query or not query.strip():
            return
        
        query = query.strip()
        
        # Remove if already exists
        if query in self.search_history:
            self.search_history.remove(query)
        
        # Add to beginning
        self.search_history.insert(0, query)
        
        # Limit size
        if len(self.search_history) > self.MAX_SEARCH_HISTORY:
            self.search_history = self.search_history[:self.MAX_SEARCH_HISTORY]
    
    def increment_calculations(self) -> None:
        """Increment calculation counter"""
        self.total_calculations += 1
    
    def set_preference(self, key: str, value: Any) -> None:
        """Set user preference"""
        self.user_preferences[key] = value
    
    def get_preference(self, key: str, default: Any = None) -> Any:
        """Get user preference"""
        return self.user_preferences.get(key, default)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert state to dictionary"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AppState':
        """Create state from dictionary"""
        return cls(**data)
    
    def to_json(self) -> str:
        """Convert state to JSON string"""
        return json.dumps(self.to_dict(), indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'AppState':
        """Create state from JSON string"""
        data = json.loads(json_str)
        return cls.from_dict(data)


def initialize_state() -> AppState:
    """
    Initialize application state from session state
    
    Returns:
        AppState instance
    """
    return AppState(
        favorites=st.session_state.get('favorites', []),
        recently_used=st.session_state.get('recently_used', []),
        total_calculations=st.session_state.get('total_calculations', 0),
        user_preferences=st.session_state.get('user_preferences', {}),
        search_history=st.session_state.get('search_history', [])
    )


def save_state_to_session(state: AppState) -> None:
    """
    Save state to session state
    
    Args:
        state: AppState instance to save
    """
    st.session_state['favorites'] = state.favorites
    st.session_state['recently_used'] = state.recently_used
    st.session_state['total_calculations'] = state.total_calculations
    st.session_state['user_preferences'] = state.user_preferences
    st.session_state['search_history'] = state.search_history


def get_state() -> AppState:
    """
    Get current application state
    
    Returns:
        AppState instance (from session state)
    """
    # Initialize if not exists
    if 'favorites' not in st.session_state:
        st.session_state['favorites'] = []
    if 'recently_used' not in st.session_state:
        st.session_state['recently_used'] = []
    if 'total_calculations' not in st.session_state:
        st.session_state['total_calculations'] = 0
    if 'user_preferences' not in st.session_state:
        st.session_state['user_preferences'] = {}
    if 'search_history' not in st.session_state:
        st.session_state['search_history'] = []
    
    return initialize_state()


def update_state(callback) -> None:
    """
    Update state using a callback function
    
    Args:
        callback: Function that takes AppState and modifies it
    
    Example:
        >>> def add_fav(state):
        ...     state.add_favorite("sofa")
        >>> update_state(add_fav)
    """
    state = get_state()
    callback(state)
    save_state_to_session(state)


# Convenience functions that match existing API
def add_to_favorites(calc_id: str) -> None:
    """Add calculator to favorites"""
    def callback(state: AppState):
        state.add_favorite(calc_id)
    update_state(callback)


def remove_from_favorites(calc_id: str) -> None:
    """Remove calculator from favorites"""
    def callback(state: AppState):
        state.remove_favorite(calc_id)
    update_state(callback)


def add_to_recently_used(calc_id: str) -> None:
    """Add calculator to recently used"""
    def callback(state: AppState):
        state.add_recently_used(calc_id)
    update_state(callback)


def add_to_search_history(query: str) -> None:
    """Add search query to history"""
    def callback(state: AppState):
        state.add_search_history(query)
    update_state(callback)


def increment_calculations() -> None:
    """Increment calculation counter"""
    def callback(state: AppState):
        state.increment_calculations()
    update_state(callback)


__all__ = [
    'AppState',
    'initialize_state',
    'save_state_to_session',
    'get_state',
    'update_state',
    'add_to_favorites',
    'remove_from_favorites',
    'add_to_recently_used',
    'add_to_search_history',
    'increment_calculations',
]

