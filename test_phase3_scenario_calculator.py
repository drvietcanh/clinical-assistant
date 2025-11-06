"""
Test script cho Phase 3: Scenario Dosing Calculator
Test các chức năng chính của scenario_dosing_calculator.py
"""

import sys
import pandas as pd
from antibiotics.scenario_dosing_calculator import (
    calculate_scenarios,
    create_dosing_chart,
    create_interval_chart,
    export_to_csv
)
from antibiotics.antibiotics_data import ANTIBIOTICS_DATABASE

def test_calculate_scenarios():
    """Test function calculate_scenarios"""
    print("\n" + "="*60)
    print("TEST 1: calculate_scenarios()")
    print("="*60)
    
    # Test với Ceftriaxone - một kháng sinh phổ biến
    antibiotic_name = "Ceftriaxone"
    
    if antibiotic_name not in ANTIBIOTICS_DATABASE:
        print(f"❌ Không tìm thấy kháng sinh: {antibiotic_name}")
        return False
    
    print(f"✅ Kháng sinh: {antibiotic_name}")
    
    # Test scenarios
    scenarios_list = [
        {"crcl": 90, "category": "Normal"},
        {"crcl": 45, "category": "Mild"},
        {"crcl": 22, "category": "Moderate"},
        {"crcl": 10, "category": "Severe"}
    ]
    
    indications_list = ["standard", "severe"]
    
    print(f"📋 Scenarios: {len(scenarios_list)}")
    print(f"📋 Indications: {indications_list}")
    
    try:
        results = calculate_scenarios(
            antibiotic_name=antibiotic_name,
            weight=70.0,
            height=170.0,
            age=50,
            sex="Nam",
            scenarios_list=scenarios_list,
            indications_list=indications_list
        )
        
        if not results:
            print("❌ Không có kết quả trả về")
            return False
        
        print(f"✅ Tính toán thành công: {len(results)} kết quả")
        
        # Hiển thị một vài kết quả mẫu
        print("\n📊 Kết quả mẫu (3 đầu tiên):")
        for i, result in enumerate(results[:3]):
            print(f"  {i+1}. Scenario: {result['scenario']}, CrCl: {result['crcl']:.1f}, "
                  f"Chỉ định: {result['indication']}, Liều: {result['dose_mg']:.0f} mg, "
                  f"Khoảng cách: {result['interval_hours']:.0f}h")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_create_charts():
    """Test functions tạo biểu đồ"""
    print("\n" + "="*60)
    print("TEST 2: create_dosing_chart() và create_interval_chart()")
    print("="*60)
    
    # Tạo dữ liệu test
    test_data = [
        {"scenario": "Normal", "crcl": 90, "indication": "Chuẩn", "dose_mg": 2000, "interval_hours": 24},
        {"scenario": "Normal", "crcl": 90, "indication": "Nhiễm khuẩn nặng", "dose_mg": 3000, "interval_hours": 12},
        {"scenario": "Mild", "crcl": 45, "indication": "Chuẩn", "dose_mg": 2000, "interval_hours": 24},
        {"scenario": "Mild", "crcl": 45, "indication": "Nhiễm khuẩn nặng", "dose_mg": 3000, "interval_hours": 12},
        {"scenario": "Moderate", "crcl": 22, "indication": "Chuẩn", "dose_mg": 1500, "interval_hours": 24},
        {"scenario": "Severe", "crcl": 10, "indication": "Chuẩn", "dose_mg": 1000, "interval_hours": 48},
    ]
    
    results_df = pd.DataFrame(test_data)
    
    print(f"✅ Tạo DataFrame test: {len(results_df)} rows")
    
    # Test create_dosing_chart
    try:
        dosing_chart = create_dosing_chart(results_df, "Ceftriaxone")
        if dosing_chart:
            print("✅ create_dosing_chart() thành công")
            print(f"   - Chart type: {type(dosing_chart)}")
            print(f"   - Data traces: {len(dosing_chart.data)}")
        else:
            print("⚠️ create_dosing_chart() trả về None (có thể do dữ liệu)")
    except Exception as e:
        print(f"❌ Lỗi create_dosing_chart(): {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Test create_interval_chart
    try:
        interval_chart = create_interval_chart(results_df, "Ceftriaxone")
        if interval_chart:
            print("✅ create_interval_chart() thành công")
            print(f"   - Chart type: {type(interval_chart)}")
            print(f"   - Data traces: {len(interval_chart.data)}")
        else:
            print("⚠️ create_interval_chart() trả về None (có thể do dữ liệu)")
    except Exception as e:
        print(f"❌ Lỗi create_interval_chart(): {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


def test_export_to_csv():
    """Test function export CSV"""
    print("\n" + "="*60)
    print("TEST 3: export_to_csv()")
    print("="*60)
    
    # Tạo dữ liệu test
    test_data = [
        {"scenario": "Normal", "crcl": 90, "indication": "Chuẩn", "dose_mg": 2000, 
         "interval_hours": 24, "frequency": "1x/ngày", "renal_adjustment": "Không đổi", 
         "renal_category": "normal"},
        {"scenario": "Mild", "crcl": 45, "indication": "Chuẩn", "dose_mg": 2000, 
         "interval_hours": 24, "frequency": "1x/ngày", "renal_adjustment": "Không đổi", 
         "renal_category": "30_60"},
    ]
    
    results_df = pd.DataFrame(test_data)
    
    patient_info = {
        'weight': 70.0,
        'height': 170.0,
        'age': 50,
        'sex': 'Nam'
    }
    
    try:
        csv_data = export_to_csv(results_df, patient_info, "Ceftriaxone")
        
        if csv_data:
            print("✅ export_to_csv() thành công")
            print(f"   - CSV length: {len(csv_data)} characters")
            print(f"   - First 200 chars: {csv_data[:200]}...")
            
            # Kiểm tra có chứa các cột cần thiết không
            required_columns = ['Kháng sinh', 'Cân nặng (kg)', 'Chiều cao (cm)', 'Tuổi', 'Giới tính']
            missing = [col for col in required_columns if col not in csv_data]
            if missing:
                print(f"⚠️ Thiếu columns: {missing}")
            else:
                print("✅ Tất cả columns cần thiết đều có")
            
            return True
        else:
            print("❌ export_to_csv() trả về None hoặc empty")
            return False
            
    except Exception as e:
        print(f"❌ Lỗi export_to_csv(): {e}")
        import traceback
        traceback.print_exc()
        return False


def test_integration():
    """Test tích hợp với database"""
    print("\n" + "="*60)
    print("TEST 4: Integration với database")
    print("="*60)
    
    try:
        from antibiotics.database_display import render_scenario_dosing_calculator
        
        print("✅ Import render_scenario_dosing_calculator thành công")
        
        # Kiểm tra một vài kháng sinh phổ biến
        test_antibiotics = ["Ceftriaxone", "Meropenem", "Vancomycin", "Piperacillin-Tazobactam"]
        
        available = []
        missing = []
        
        for ab_name in test_antibiotics:
            if ab_name in ANTIBIOTICS_DATABASE:
                available.append(ab_name)
            else:
                missing.append(ab_name)
        
        print(f"✅ Kháng sinh có trong database: {len(available)}/{len(test_antibiotics)}")
        if available:
            print(f"   - {', '.join(available)}")
        if missing:
            print(f"⚠️ Không tìm thấy: {', '.join(missing)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi integration test: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Chạy tất cả tests"""
    print("\n" + "="*60)
    print("🧪 TEST PHASE 3: SCENARIO DOSING CALCULATOR")
    print("="*60)
    
    results = []
    
    # Test 1: calculate_scenarios
    results.append(("calculate_scenarios", test_calculate_scenarios()))
    
    # Test 2: create_charts
    results.append(("create_charts", test_create_charts()))
    
    # Test 3: export_to_csv
    results.append(("export_to_csv", test_export_to_csv()))
    
    # Test 4: integration
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
    success = main()
    sys.exit(0 if success else 1)

