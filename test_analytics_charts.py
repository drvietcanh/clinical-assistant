"""
Test script for Analytics Dashboard Chart Rendering
Tests chart height calculations and rendering logic
"""

import sys
from datetime import datetime, timedelta

# Mock streamlit for testing
class MockSessionState:
    def __init__(self):
        self.analytics_data = {
            'calculations': [],
            'calculator_counts': {},
            'specialty_counts': {},
            'daily_counts': {}
        }
    
    def __contains__(self, key):
        return hasattr(self, key)
    
    def get(self, key, default=None):
        return getattr(self, key, default) if hasattr(self, key) else default

class MockStreamlit:
    session_state = MockSessionState()
    
    @staticmethod
    def markdown(*args, **kwargs):
        pass
    
    @staticmethod
    def info(*args, **kwargs):
        pass
    
    @staticmethod
    def metric(*args, **kwargs):
        pass
    
    @staticmethod
    def columns(n):
        return [MockStreamlit() for _ in range(n)]
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        pass

sys.modules['streamlit'] = MockStreamlit()
import streamlit as st

# Import analytics functions
from components.analytics import (
    get_daily_usage,
    get_peak_usage_hours,
    get_total_calculations,
    get_most_used_calculators,
    get_specialty_breakdown
)


def test_chart_height_calculation():
    """Test chart height calculation logic"""
    print("Testing chart height calculation...")
    
    # Test case 1: All zeros
    values = [0, 0, 0, 0, 0, 0, 0]
    max_value = max(values) if values and max(values) > 0 else 1
    
    results = []
    for value in values:
        if max_value > 0 and value > 0:
            height_pct = min((value / max_value * 100), 100)
            if height_pct < 4:
                height_pct = 4
            min_height_px = 4
        else:
            height_pct = 0
            min_height_px = 0
        results.append((value, height_pct, min_height_px))
    
    print(f"  Test 1 (all zeros): {results}")
    assert all(h == 0 and m == 0 for _, h, m in results), "All zeros should have height 0"
    print("  ✅ Pass")
    
    # Test case 2: One value
    values = [0, 0, 0, 5, 0, 0, 0]
    max_value = max(values) if values and max(values) > 0 else 1
    
    results = []
    for value in values:
        if max_value > 0 and value > 0:
            height_pct = min((value / max_value * 100), 100)
            if height_pct < 4:
                height_pct = 4
            min_height_px = 4
        else:
            height_pct = 0
            min_height_px = 0
        results.append((value, height_pct, min_height_px))
    
    print(f"  Test 2 (one value): {results}")
    assert results[3][1] >= 4 and results[3][2] == 4, "Non-zero value should have min height"
    assert all(h == 0 and m == 0 for _, h, m in results[:3] + results[4:]), "Zeros should have height 0"
    print("  ✅ Pass")
    
    # Test case 3: Small values
    values = [1, 1, 1, 1, 1, 1, 1]
    max_value = max(values) if values and max(values) > 0 else 1
    
    results = []
    for value in values:
        if max_value > 0 and value > 0:
            height_pct = min((value / max_value * 100), 100)
            if height_pct < 4:
                height_pct = 4
            min_height_px = 4
        else:
            height_pct = 0
            min_height_px = 0
        results.append((value, height_pct, min_height_px))
    
    print(f"  Test 3 (small values): {results}")
    assert all(h >= 4 and m == 4 for _, h, m in results), "All non-zero values should have min height 4"
    print("  ✅ Pass")
    
    # Test case 4: Large values
    values = [0, 10, 20, 30, 40, 50, 0]
    max_value = max(values) if values and max(values) > 0 else 1
    
    results = []
    for value in values:
        if max_value > 0 and value > 0:
            height_pct = min((value / max_value * 100), 100)
            if height_pct < 4:
                height_pct = 4
            min_height_px = 4
        else:
            height_pct = 0
            min_height_px = 0
        results.append((value, height_pct, min_height_px))
    
    print(f"  Test 4 (large values): {results}")
    assert results[6][1] == 0 and results[6][2] == 0, "Zero should have height 0"
    assert results[5][1] == 100 and results[5][2] == 4, "Max value should have height 100%"
    print("  ✅ Pass")


def test_analytics_functions():
    """Test analytics functions with mock data"""
    print("\nTesting analytics functions...")
    
    # Setup mock data
    st.session_state.analytics_data = {
        'calculations': [
            {
                'id': i,
                'calculator_id': f'test_{i % 3}',
                'calculator_name': f'Test Calculator {i % 3}',
                'specialty': 'Cardiology' if i % 2 == 0 else 'Emergency',
                'timestamp': datetime.now().isoformat(),
                'date': datetime.now().strftime('%Y-%m-%d'),
                'hour': 10 + (i % 5),
                'day_of_week': 'Monday'
            }
            for i in range(10)
        ],
        'calculator_counts': {
            'test_0': {'count': 4, 'name': 'Test Calculator 0'},
            'test_1': {'count': 3, 'name': 'Test Calculator 1'},
            'test_2': {'count': 3, 'name': 'Test Calculator 2'},
        },
        'specialty_counts': {
            'Cardiology': 5,
            'Emergency': 5,
        },
        'daily_counts': {
            datetime.now().strftime('%Y-%m-%d'): 10
        }
    }
    
    # Test get_total_calculations
    total = get_total_calculations()
    print(f"  Total calculations: {total}")
    assert total == 10, f"Expected 10, got {total}"
    print("  ✅ Pass")
    
    # Test get_most_used_calculators
    most_used = get_most_used_calculators(limit=3)
    print(f"  Most used: {most_used}")
    assert len(most_used) == 3, f"Expected 3, got {len(most_used)}"
    assert most_used[0]['count'] == 4, "First should have count 4"
    print("  ✅ Pass")
    
    # Test get_specialty_breakdown
    specialty = get_specialty_breakdown()
    print(f"  Specialty breakdown: {specialty}")
    assert 'Cardiology' in specialty, "Cardiology should be in breakdown"
    assert specialty['Cardiology'] == 5, "Cardiology should have count 5"
    print("  ✅ Pass")
    
    # Test get_daily_usage
    daily = get_daily_usage(days=7)
    print(f"  Daily usage: {len(daily)} days")
    assert len(daily) == 7, f"Expected 7 days, got {len(daily)}"
    print("  ✅ Pass")
    
    # Test get_peak_usage_hours
    hours = get_peak_usage_hours()
    print(f"  Peak hours: {len(hours)} hours")
    assert len(hours) > 0, "Should have at least one hour"
    print("  ✅ Pass")


if __name__ == '__main__':
    print("=" * 60)
    print("Analytics Dashboard Chart Rendering Tests")
    print("=" * 60)
    
    try:
        test_chart_height_calculation()
        test_analytics_functions()
        
        print("\n" + "=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

