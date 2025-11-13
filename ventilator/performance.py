"""
Performance Optimization Utilities - PHIÊN 6
Lazy loading và performance monitoring
"""

import streamlit as st
from typing import Any, Callable, Optional
import time


def lazy_import(module_name: str, import_func: Callable) -> Any:
    """
    Lazy import module chỉ khi cần
    
    Args:
        module_name: Tên module
        import_func: Function để import module
    
    Returns:
        Module object
    """
    cache_key = f"_lazy_import_{module_name}"
    
    if cache_key not in st.session_state:
        st.session_state[cache_key] = import_func()
    
    return st.session_state[cache_key]


def measure_performance(func: Callable) -> Callable:
    """
    Decorator để đo thời gian thực thi function
    
    Usage:
        @measure_performance
        def slow_function():
            ...
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        
        # Log nếu quá chậm (>0.1s)
        if elapsed > 0.1:
            st.session_state.setdefault('_performance_log', []).append({
                'function': func.__name__,
                'elapsed': elapsed,
                'args': str(args)[:50],
                'kwargs': str(kwargs)[:50]
            })
        
        return result
    
    return wrapper


def get_performance_log() -> list:
    """Lấy performance log"""
    return st.session_state.get('_performance_log', [])


def clear_performance_log():
    """Xóa performance log"""
    if '_performance_log' in st.session_state:
        del st.session_state['_performance_log']


def render_performance_info():
    """Hiển thị thông tin performance (chỉ trong dev mode)"""
    if st.session_state.get('_dev_mode', False):
        log = get_performance_log()
        if log:
            with st.expander("⚡ Performance Log (Dev Mode)"):
                st.json(log[-10:])  # Show last 10 entries

