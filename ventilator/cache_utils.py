"""
Cache Utilities for Ventilator Module - PHIÊN 6
Tối ưu hiệu suất bằng cách cache calculations
"""

import streamlit as st
from functools import lru_cache
from typing import Any, Callable, Optional
import hashlib
import json


def get_cache_key(*args, **kwargs) -> str:
    """
    Tạo cache key từ arguments
    
    Args:
        *args: Positional arguments
        **kwargs: Keyword arguments
    
    Returns:
        Cache key string
    """
    # Convert args và kwargs thành string để hash
    key_data = {
        'args': args,
        'kwargs': kwargs
    }
    key_str = json.dumps(key_data, sort_keys=True, default=str)
    return hashlib.md5(key_str.encode()).hexdigest()


def cached_calculation(func: Callable) -> Callable:
    """
    Decorator để cache calculation results trong session state
    
    Usage:
        @cached_calculation
        def calculate_pbw(sex, height):
            ...
    """
    def wrapper(*args, **kwargs):
        cache_key = f"vent_cache_{func.__name__}_{get_cache_key(*args, **kwargs)}"
        
        # Kiểm tra cache
        if cache_key in st.session_state:
            return st.session_state[cache_key]
        
        # Tính toán và cache
        result = func(*args, **kwargs)
        st.session_state[cache_key] = result
        return result
    
    return wrapper


def clear_calculation_cache():
    """Xóa tất cả cached calculations"""
    keys_to_remove = [key for key in st.session_state.keys() if key.startswith("vent_cache_")]
    for key in keys_to_remove:
        del st.session_state[key]


def get_cache_size() -> int:
    """Lấy số lượng cached items"""
    return len([key for key in st.session_state.keys() if key.startswith("vent_cache_")])


# LRU Cache cho pure functions (không dùng session state)
@lru_cache(maxsize=128)
def cached_pbw(sex: str, height: float) -> float:
    """Cached PBW calculation"""
    if sex == "Nam":
        return round(50 + 0.91 * (height - 152.4), 1)
    else:
        return round(45.5 + 0.91 * (height - 152.4), 1)


@lru_cache(maxsize=128)
def cached_driving_pressure(plateau: float, peep: float) -> Optional[float]:
    """Cached driving pressure calculation"""
    if plateau > 0 and peep >= 0:
        return plateau - peep
    return None


@lru_cache(maxsize=128)
def cached_pf_ratio(po2: float, fio2: float) -> Optional[float]:
    """Cached P/F ratio calculation"""
    if po2 and fio2 and fio2 > 0:
        return po2 / (fio2 / 100)
    return None

