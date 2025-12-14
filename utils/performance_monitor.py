"""
Performance Monitoring Utilities
Track and log performance metrics
"""

import time
import logging
from typing import Dict, List, Optional, Callable, Any, Tuple
from functools import wraps
from datetime import datetime
import streamlit as st

logger = logging.getLogger(__name__)


class PerformanceMonitor:
    """Track performance metrics"""
    
    def __init__(self):
        self.metrics: Dict[str, List[float]] = {}
        self.operation_times: Dict[str, List[float]] = {}
    
    def record_operation(self, operation_name: str, duration: float):
        """Record operation duration"""
        if operation_name not in self.operation_times:
            self.operation_times[operation_name] = []
        self.operation_times[operation_name].append(duration)
        
        # Keep only last 100 measurements
        if len(self.operation_times[operation_name]) > 100:
            self.operation_times[operation_name] = self.operation_times[operation_name][-100:]
    
    def get_stats(self, operation_name: str) -> Optional[Dict[str, float]]:
        """Get statistics for an operation"""
        if operation_name not in self.operation_times:
            return None
        
        times = self.operation_times[operation_name]
        if not times:
            return None
        
        return {
            'count': len(times),
            'min': min(times),
            'max': max(times),
            'avg': sum(times) / len(times),
            'total': sum(times)
        }
    
    def get_slow_operations(self, threshold: float = 1.0) -> List[Tuple[str, Dict[str, float]]]:
        """Get operations slower than threshold"""
        slow_ops = []
        for op_name, times in self.operation_times.items():
            if times:
                avg_time = sum(times) / len(times)
                if avg_time > threshold:
                    slow_ops.append((op_name, self.get_stats(op_name)))
        
        return sorted(slow_ops, key=lambda x: x[1]['avg'] if x[1] else 0, reverse=True)
    
    def clear(self):
        """Clear all metrics"""
        self.metrics.clear()
        self.operation_times.clear()


# Global monitor instance
_monitor = PerformanceMonitor()


def get_performance_monitor() -> PerformanceMonitor:
    """Get global performance monitor instance"""
    return _monitor


def measure_time(operation_name: Optional[str] = None, log: bool = True):
    """
    Decorator to measure function execution time
    
    Args:
        operation_name: Name for the operation (defaults to function name)
        log: Whether to log the measurement
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            op_name = operation_name or func.__name__
            start_time = time.time()
            
            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                
                # Record in monitor
                _monitor.record_operation(op_name, duration)
                
                # Log if enabled
                if log and duration > 0.5:  # Only log slow operations
                    logger.info(f"Operation '{op_name}' took {duration:.3f}s")
                
                return result
            except Exception as e:
                duration = time.time() - start_time
                logger.error(f"Operation '{op_name}' failed after {duration:.3f}s: {e}", exc_info=True)
                raise
        
        return wrapper
    return decorator


def track_search_performance(query: str, result_count: int, duration: float):
    """Track search operation performance"""
    _monitor.record_operation('search', duration)
    
    # Log slow searches
    if duration > 0.5:
        logger.warning(f"Slow search: '{query}' returned {result_count} results in {duration:.3f}s")
    
    # Store in session state for analytics
    if 'search_performance' not in st.session_state:
        st.session_state.search_performance = []
    
    st.session_state.search_performance.append({
        'query': query,
        'result_count': result_count,
        'duration': duration,
        'timestamp': datetime.now().isoformat()
    })
    
    # Keep only last 50 searches
    if len(st.session_state.search_performance) > 50:
        st.session_state.search_performance = st.session_state.search_performance[-50:]


def get_performance_summary() -> Dict[str, Any]:
    """Get performance summary"""
    return {
        'operations': {
            op_name: _monitor.get_stats(op_name)
            for op_name in _monitor.operation_times.keys()
        },
        'slow_operations': _monitor.get_slow_operations(threshold=0.5)
    }


__all__ = [
    'PerformanceMonitor',
    'get_performance_monitor',
    'measure_time',
    'track_search_performance',
    'get_performance_summary',
]

