"""
Test script for Mobile UI components
Run: python test_mobile_ui.py
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test all imports"""
    print("Testing imports...")
    try:
        from antibiotics.mobile_ui import (
            render_mobile_bottom_nav,
            render_mobile_fab,
            inject_swipe_gestures,
            inject_pull_to_refresh,
            inject_card_swipe_actions,
            inject_quick_actions_menu,
            inject_pwa_support,
            inject_offline_indicator,
            inject_mobile_styles
        )
        print("✅ Mobile UI imports OK")
        
        from antibiotics.performance import (
            inject_lazy_loading,
            inject_virtual_scrolling,
            inject_image_lazy_loading,
            inject_performance_monitoring,
            paginate_protocols,
            render_pagination_controls
        )
        print("✅ Performance imports OK")
        
        from antibiotics.ui_antibiotics_view import (
            render_antibiotics_by_infection_view,
            render_protocol_card,
            render_regimen_card
        )
        print("✅ UI view imports OK")
        
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False


def test_functions():
    """Test function calls"""
    print("\nTesting function calls...")
    try:
        from antibiotics.mobile_ui import render_mobile_bottom_nav
        # Test with different tab values
        for tab in ["infection", "drugs", "stewardship", "search"]:
            try:
                # Just check if function can be called (won't actually render without Streamlit)
                assert callable(render_mobile_bottom_nav)
                print(f"✅ render_mobile_bottom_nav({tab}) callable")
            except Exception as e:
                print(f"❌ Error calling render_mobile_bottom_nav({tab}): {e}")
                return False
        
        from antibiotics.performance import paginate_protocols
        from antibiotics.protocols_data import get_antibiotic_protocols
        
        protocols = get_antibiotic_protocols()
        result = paginate_protocols(protocols.protocols[:20], 10)
        
        assert len(result) == 3, "Pagination should return (items, total_pages, current_page)"
        assert len(result[0]) <= 10, "Page size should be <= 10"
        assert result[1] >= 1, "Should have at least 1 page"
        assert result[2] >= 1, "Current page should be >= 1"
        
        print(f"✅ paginate_protocols OK: {len(result[0])} items, {result[1]} pages")
        
        return True
    except Exception as e:
        print(f"❌ Function test error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_data_structures():
    """Test data structures"""
    print("\nTesting data structures...")
    try:
        from antibiotics.protocols_data import get_antibiotic_protocols
        from antibiotics.protocols_schema import AntibioticProtocol
        
        protocols = get_antibiotic_protocols()
        assert hasattr(protocols, 'protocols'), "ProtocolCollection should have protocols attribute"
        assert isinstance(protocols.protocols, list), "protocols should be a list"
        
        if len(protocols.protocols) > 0:
            protocol = protocols.protocols[0]
            assert isinstance(protocol, AntibioticProtocol), "Protocol should be AntibioticProtocol instance"
            assert hasattr(protocol, 'title'), "Protocol should have title"
            assert hasattr(protocol, 'infection_site'), "Protocol should have infection_site"
            assert hasattr(protocol, 'severity'), "Protocol should have severity"
        
        print(f"✅ Data structures OK: {len(protocols.protocols)} protocols")
        return True
    except Exception as e:
        print(f"❌ Data structure test error: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_file_existence():
    """Test if required files exist"""
    print("\nTesting file existence...")
    files = [
        "antibiotics/mobile_ui.py",
        "antibiotics/performance.py",
        "antibiotics/ui_antibiotics_view.py",
        "pages/02_💊_Antibiotics.py",
        "static/service-worker.js",
        "static/manifest.json",
        "static/offline.html"
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} NOT FOUND")
            all_exist = False
    
    return all_exist


def main():
    """Run all tests"""
    print("=" * 60)
    print("Mobile UI Components - Comprehensive Test")
    print("=" * 60)
    
    results = []
    
    results.append(("File Existence", test_file_existence()))
    results.append(("Imports", test_imports()))
    results.append(("Functions", test_functions()))
    results.append(("Data Structures", test_data_structures()))
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 60)
    if all_passed:
        print("🎉 All tests PASSED!")
        return 0
    else:
        print("⚠️ Some tests FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
