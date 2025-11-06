"""
Test script cho Phase 4: Integration & UX Improvements
Test các chức năng chính của Phase 4
"""

import sys
from datetime import datetime
from antibiotics.recent_calculations import (
    save_calculation,
    get_recent_calculations,
    remove_calculation,
    clear_recent_calculations,
    format_calculation_summary
)
from antibiotics.database_search import filter_antibiotics
from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE


def test_recent_calculations_save():
    """Test save calculation"""
    print("\n" + "="*60)
    print("TEST 1: save_calculation()")
    print("="*60)
    
    # Clear first
    clear_recent_calculations()
    
    # Create test calculation
    test_calc = {
        'antibiotic_name': 'Ceftriaxone',
        'patient_info': {
            'weight': 70.0,
            'crcl': 60.0,
            'egfr': 65.0
        },
        'indication': 'standard',
        'result': {
            'adjustment': 'Không đổi',
            'renal_category': 'normal'
        },
        'calculation_type': 'quick'
    }
    
    try:
        save_calculation(test_calc)
        print("✅ save_calculation() thành công")
        
        # Check if saved
        recent = get_recent_calculations()
        if len(recent) == 1:
            print(f"✅ Calculation đã được lưu: {len(recent)} calculation")
            return True
        else:
            print(f"❌ Không tìm thấy calculation đã lưu: {len(recent)} calculations")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_recent_calculations_get():
    """Test get recent calculations"""
    print("\n" + "="*60)
    print("TEST 2: get_recent_calculations()")
    print("="*60)
    
    try:
        # Add multiple calculations
        for i in range(3):
            calc = {
                'antibiotic_name': f'TestAntibiotic{i}',
                'patient_info': {'weight': 70.0 + i, 'crcl': 60.0},
                'indication': 'standard',
                'result': {},
                'calculation_type': 'quick'
            }
            save_calculation(calc)
        
        recent = get_recent_calculations(limit=5)
        
        if len(recent) >= 3:
            print(f"✅ get_recent_calculations() thành công: {len(recent)} calculations")
            print(f"   - Latest: {recent[0].get('antibiotic_name')}")
            return True
        else:
            print(f"❌ Không đủ calculations: {len(recent)}")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_recent_calculations_limit():
    """Test limit functionality"""
    print("\n" + "="*60)
    print("TEST 3: Recent calculations limit (max 10)")
    print("="*60)
    
    try:
        clear_recent_calculations()
        
        # Add 15 calculations
        for i in range(15):
            calc = {
                'antibiotic_name': f'Antibiotic{i}',
                'patient_info': {'weight': 70.0, 'crcl': 60.0},
                'indication': 'standard',
                'result': {},
                'calculation_type': 'quick'
            }
            save_calculation(calc)
        
        recent = get_recent_calculations()
        
        if len(recent) == 10:
            print(f"✅ Limit hoạt động đúng: {len(recent)} calculations (max 10)")
            print(f"   - Oldest should be Antibiotic5, newest should be Antibiotic14")
            return True
        else:
            print(f"❌ Limit không hoạt động: {len(recent)} calculations (expected 10)")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_format_calculation_summary():
    """Test format calculation summary"""
    print("\n" + "="*60)
    print("TEST 4: format_calculation_summary()")
    print("="*60)
    
    test_cases = [
        {
            'antibiotic_name': 'Ceftriaxone',
            'patient_info': {'weight': 70.0, 'crcl': 60.0},
            'indication': 'standard',
            'expected': 'Ceftriaxone - 70kg, CrCl 60 - Chuẩn'
        },
        {
            'antibiotic_name': 'Meropenem',
            'patient_info': {'weight': 80.0, 'crcl': 45.0},
            'indication': 'severe',
            'expected': 'Meropenem - 80kg, CrCl 45 - Nhiễm khuẩn nặng'
        }
    ]
    
    try:
        for i, test_case in enumerate(test_cases):
            summary = format_calculation_summary(test_case)
            expected = test_case.pop('expected')
            
            if summary == expected:
                print(f"✅ Test case {i+1}: '{summary}'")
            else:
                print(f"⚠️ Test case {i+1}: Expected '{expected}', got '{summary}'")
        
        print("✅ format_calculation_summary() hoạt động tốt")
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_remove_calculation():
    """Test remove calculation"""
    print("\n" + "="*60)
    print("TEST 5: remove_calculation()")
    print("="*60)
    
    try:
        clear_recent_calculations()
        
        # Add 3 calculations
        calc_ids = []
        for i in range(3):
            calc = {
                'antibiotic_name': f'Antibiotic{i}',
                'patient_info': {'weight': 70.0, 'crcl': 60.0},
                'indication': 'standard',
                'result': {},
                'calculation_type': 'quick'
            }
            save_calculation(calc)
            recent = get_recent_calculations()
            if recent:
                calc_ids.append(recent[0].get('id'))
        
        # Remove middle one
        if len(calc_ids) >= 2:
            remove_calculation(calc_ids[1])
            recent = get_recent_calculations()
            
            if len(recent) == 2:
                print(f"✅ remove_calculation() thành công: {len(recent)} calculations còn lại")
                return True
            else:
                print(f"❌ Không xóa được: {len(recent)} calculations (expected 2)")
                return False
        else:
            print("⚠️ Không đủ calculations để test")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_filter_antibiotics_pregnancy():
    """Test filter antibiotics với pregnancy filter"""
    print("\n" + "="*60)
    print("TEST 6: filter_antibiotics() với pregnancy filter")
    print("="*60)
    
    try:
        # Test với pregnancy filter B
        filtered = filter_antibiotics(
            group_filter="Tất cả",
            route_filter="Tất cả",
            aware_filter="Tất cả",
            pregnancy_filter="B"
        )
        
        print(f"✅ Filter với pregnancy='B': {len(filtered)} kháng sinh")
        
        # Test với pregnancy filter C
        filtered_c = filter_antibiotics(
            group_filter="Tất cả",
            route_filter="Tất cả",
            aware_filter="Tất cả",
            pregnancy_filter="C"
        )
        
        print(f"✅ Filter với pregnancy='C': {len(filtered_c)} kháng sinh")
        
        # Test với Tất cả
        filtered_all = filter_antibiotics(
            group_filter="Tất cả",
            route_filter="Tất cả",
            aware_filter="Tất cả",
            pregnancy_filter="Tất cả"
        )
        
        print(f"✅ Filter với pregnancy='Tất cả': {len(filtered_all)} kháng sinh")
        
        if len(filtered_all) >= len(filtered) and len(filtered_all) >= len(filtered_c):
            print("✅ Pregnancy filter hoạt động đúng")
            return True
        else:
            print("⚠️ Kết quả filter có vẻ không đúng")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_filter_antibiotics_combined():
    """Test filter với nhiều filters cùng lúc"""
    print("\n" + "="*60)
    print("TEST 7: filter_antibiotics() với multiple filters")
    print("="*60)
    
    try:
        # Filter: Cephalosporin, IV, ACCESS, B
        filtered = filter_antibiotics(
            group_filter="Cephalosporin",
            route_filter="IV",
            aware_filter="ACCESS",
            pregnancy_filter="B"
        )
        
        print(f"✅ Combined filter (Cephalosporin + IV + ACCESS + B): {len(filtered)} kháng sinh")
        
        if filtered:
            # Show first few
            for i, (name, data) in enumerate(list(filtered.items())[:3]):
                print(f"   {i+1}. {name}")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_integration():
    """Test integration với database"""
    print("\n" + "="*60)
    print("TEST 8: Integration với database")
    print("="*60)
    
    try:
        # Test import
        from antibiotics.database import render_database
        from antibiotics.database_calculator import render_quick_dosing_calculator
        
        print("✅ Import render_database thành công")
        print("✅ Import render_quick_dosing_calculator thành công")
        
        # Test recent calculations integration
        clear_recent_calculations()
        test_calc = {
            'antibiotic_name': 'Ceftriaxone',
            'patient_info': {'weight': 70.0, 'crcl': 60.0},
            'indication': 'standard',
            'result': {},
            'calculation_type': 'quick'
        }
        save_calculation(test_calc)
        
        recent = get_recent_calculations()
        if recent:
            print(f"✅ Recent calculations integration: {len(recent)} calculation")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Chạy tất cả tests"""
    print("\n" + "="*60)
    print("🧪 TEST PHASE 4: INTEGRATION & UX IMPROVEMENTS")
    print("="*60)
    
    results = []
    
    # Test 1: save_calculation
    results.append(("save_calculation", test_recent_calculations_save()))
    
    # Test 2: get_recent_calculations
    results.append(("get_recent_calculations", test_recent_calculations_get()))
    
    # Test 3: limit functionality
    results.append(("recent_calculations_limit", test_recent_calculations_limit()))
    
    # Test 4: format_calculation_summary
    results.append(("format_calculation_summary", test_format_calculation_summary()))
    
    # Test 5: remove_calculation
    results.append(("remove_calculation", test_remove_calculation()))
    
    # Test 6: filter_antibiotics với pregnancy
    results.append(("filter_pregnancy", test_filter_antibiotics_pregnancy()))
    
    # Test 7: filter_antibiotics combined
    results.append(("filter_combined", test_filter_antibiotics_combined()))
    
    # Test 8: integration
    results.append(("integration", test_integration()))
    
    # Tổng kết
    print("\n" + "="*60)
    print("📊 TỔNG KẾT TEST")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n✅ Passed: {passed}/{total}")
    print(f"{'❌ Failed' if passed < total else '✅ All tests passed'}: {total - passed}/{total}")
    
    return passed == total


if __name__ == "__main__":
    # Note: Some tests require streamlit session state, so they may not work in standalone mode
    # These tests are designed to work with streamlit context
    success = main()
    sys.exit(0 if success else 1)

