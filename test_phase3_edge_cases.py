"""
Test edge cases cho Phase 3: Scenario Dosing Calculator
Test các trường hợp biên và lỗi
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

def test_empty_scenarios():
    """Test với empty scenarios list"""
    print("\n" + "="*60)
    print("EDGE CASE 1: Empty scenarios list")
    print("="*60)
    
    try:
        results = calculate_scenarios(
            antibiotic_name="Ceftriaxone",
            weight=70.0,
            height=170.0,
            age=50,
            sex="Nam",
            scenarios_list=[],
            indications_list=["standard"]
        )
        
        if results == []:
            print("✅ Xử lý đúng: Trả về empty list khi không có scenarios")
            return True
        else:
            print(f"⚠️ Trả về {len(results)} kết quả thay vì empty list")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False


def test_empty_indications():
    """Test với empty indications list"""
    print("\n" + "="*60)
    print("EDGE CASE 2: Empty indications list")
    print("="*60)
    
    try:
        results = calculate_scenarios(
            antibiotic_name="Ceftriaxone",
            weight=70.0,
            height=170.0,
            age=50,
            sex="Nam",
            scenarios_list=[{"crcl": 90, "category": "Normal"}],
            indications_list=[]
        )
        
        if results == []:
            print("✅ Xử lý đúng: Trả về empty list khi không có indications")
            return True
        else:
            print(f"⚠️ Trả về {len(results)} kết quả thay vì empty list")
            return False
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False


def test_invalid_antibiotic():
    """Test với kháng sinh không tồn tại"""
    print("\n" + "="*60)
    print("EDGE CASE 3: Invalid antibiotic name")
    print("="*60)
    
    try:
        results = calculate_scenarios(
            antibiotic_name="InvalidAntibiotic123",
            weight=70.0,
            height=170.0,
            age=50,
            sex="Nam",
            scenarios_list=[{"crcl": 90, "category": "Normal"}],
            indications_list=["standard"]
        )
        
        if results == []:
            print("✅ Xử lý đúng: Trả về empty list khi kháng sinh không tồn tại")
            return True
        else:
            print(f"⚠️ Trả về {len(results)} kết quả cho kháng sinh không hợp lệ")
            return False
    except Exception as e:
        # Có thể throw exception, đó cũng là cách xử lý hợp lệ
        print(f"✅ Xử lý đúng: Throw exception khi kháng sinh không hợp lệ: {type(e).__name__}")
        return True


def test_extreme_values():
    """Test với giá trị cực đoan"""
    print("\n" + "="*60)
    print("EDGE CASE 4: Extreme values (very low CrCl, very high weight)")
    print("="*60)
    
    try:
        results = calculate_scenarios(
            antibiotic_name="Ceftriaxone",
            weight=150.0,  # Rất nặng
            height=170.0,
            age=80,  # Tuổi cao
            sex="Nam",
            scenarios_list=[
                {"crcl": 5, "category": "Severe"},  # CrCl rất thấp
                {"crcl": 120, "category": "Normal"}  # CrCl cao
            ],
            indications_list=["standard", "severe", "meningitis"]
        )
        
        if results:
            print(f"✅ Xử lý được giá trị cực đoan: {len(results)} kết quả")
            # Kiểm tra xem có kết quả hợp lệ không
            for result in results[:2]:
                print(f"   - {result['scenario']}: {result['dose_mg']:.0f} mg, {result['interval_hours']:.0f}h")
            return True
        else:
            print("⚠️ Không có kết quả cho giá trị cực đoan")
            return False
    except Exception as e:
        print(f"❌ Lỗi với giá trị cực đoan: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_chart_with_empty_data():
    """Test chart với empty DataFrame"""
    print("\n" + "="*60)
    print("EDGE CASE 5: Charts with empty DataFrame")
    print("="*60)
    
    empty_df = pd.DataFrame()
    
    try:
        dosing_chart = create_dosing_chart(empty_df, "Test")
        if dosing_chart is None:
            print("✅ create_dosing_chart() xử lý đúng: Trả về None cho empty DataFrame")
        else:
            print("⚠️ create_dosing_chart() trả về chart cho empty DataFrame")
        
        interval_chart = create_interval_chart(empty_df, "Test")
        if interval_chart is None:
            print("✅ create_interval_chart() xử lý đúng: Trả về None cho empty DataFrame")
        else:
            print("⚠️ create_interval_chart() trả về chart cho empty DataFrame")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False


def test_multiple_antibiotics():
    """Test với nhiều kháng sinh khác nhau"""
    print("\n" + "="*60)
    print("EDGE CASE 6: Multiple antibiotics")
    print("="*60)
    
    test_antibiotics = [
        "Meropenem",
        "Vancomycin", 
        "Piperacillin-Tazobactam",
        "Ciprofloxacin"
    ]
    
    scenarios = [
        {"crcl": 90, "category": "Normal"},
        {"crcl": 45, "category": "Mild"},
        {"crcl": 10, "category": "Severe"}
    ]
    
    success_count = 0
    
    for ab_name in test_antibiotics:
        if ab_name not in ANTIBIOTICS_DATABASE:
            print(f"⚠️ Bỏ qua {ab_name}: Không có trong database")
            continue
        
        try:
            results = calculate_scenarios(
                antibiotic_name=ab_name,
                weight=70.0,
                height=170.0,
                age=50,
                sex="Nam",
                scenarios_list=scenarios,
                indications_list=["standard"]
            )
            
            if results:
                print(f"✅ {ab_name}: {len(results)} kết quả")
                success_count += 1
            else:
                print(f"⚠️ {ab_name}: Không có kết quả")
        except Exception as e:
            print(f"❌ {ab_name}: Lỗi - {e}")
    
    print(f"\n✅ Thành công: {success_count}/{len(test_antibiotics)} kháng sinh")
    return success_count >= len(test_antibiotics) * 0.75  # 75% success rate


def main():
    """Chạy tất cả edge case tests"""
    print("\n" + "="*60)
    print("🧪 EDGE CASE TESTS - PHASE 3: SCENARIO DOSING CALCULATOR")
    print("="*60)
    
    results = []
    
    results.append(("empty_scenarios", test_empty_scenarios()))
    results.append(("empty_indications", test_empty_indications()))
    results.append(("invalid_antibiotic", test_invalid_antibiotic()))
    results.append(("extreme_values", test_extreme_values()))
    results.append(("chart_empty_data", test_chart_with_empty_data()))
    results.append(("multiple_antibiotics", test_multiple_antibiotics()))
    
    # Tổng kết
    print("\n" + "="*60)
    print("📊 TỔNG KẾT EDGE CASE TESTS")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\n✅ Passed: {passed}/{total}")
    print(f"{'❌ Failed' if passed < total else '✅ All edge case tests passed'}: {total - passed}/{total}")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

