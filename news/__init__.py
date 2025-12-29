"""
Medical News & Updates Module
Aggregates medical news from various RSS feeds
"""

from news.rss_feeds import RSS_FEEDS, get_feeds_by_category
from news.aggregator import (
    fetch_latest_news,
    get_news_by_category,
    get_cached_news,
    clear_cache
)

__all__ = [
    'RSS_FEEDS',
    'get_feeds_by_category',
    'fetch_latest_news',
    'get_news_by_category',
    'get_cached_news',
    'clear_cache',
]

