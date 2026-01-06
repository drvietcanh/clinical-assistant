"""
Scores Recent Tracking Component
Track recently viewed calculators
"""

import streamlit as st
from typing import List, Dict, Optional
from scores.config import SCORES_BY_SPECIALTY


def add_to_recent(specialty: str, score_id: str, score_name: str):
    """Add calculator to recent list"""
    if 'recent_calculators' not in st.session_state:
        st.session_state['recent_calculators'] = []
    
    # Create entry
    entry = {
        'specialty': specialty,
        'score_id': score_id,
        'name': score_name
    }
    
    # Remove if already exists
    recent_list = st.session_state['recent_calculators']
    recent_list = [e for e in recent_list if not (e['specialty'] == specialty and e['score_id'] == score_id)]
    
    # Add to front
    recent_list.insert(0, entry)
    
    # Keep only last 20
    st.session_state['recent_calculators'] = recent_list[:20]


def get_recent_calculators(max_items: int = 10) -> List[Dict]:
    """Get recent calculators"""
    if 'recent_calculators' not in st.session_state:
        return []
    
    return st.session_state['recent_calculators'][:max_items]


def clear_recent():
    """Clear recent calculators"""
    if 'recent_calculators' in st.session_state:
        st.session_state['recent_calculators'] = []


def render_recent_list(max_items: int = 10):
    """Render recent calculators list"""
    recent = get_recent_calculators(max_items)
    
    if not recent:
        st.info("No recent calculators. Start using calculators to see them here.")
        return []
    
    return recent
