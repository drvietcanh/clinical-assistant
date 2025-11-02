"""
UI Components for Clinical Assistant
"""

from .search import render_search
from .favorites import render_favorites
from .recently_used import render_recently_used
from .stats import render_stats, render_updates, render_tips

__all__ = [
    'render_search',
    'render_favorites',
    'render_recently_used',
    'render_stats',
    'render_updates',
    'render_tips',
]

