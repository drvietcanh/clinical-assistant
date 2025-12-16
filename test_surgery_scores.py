"""
Test script for Surgery & Anesthesia scoring systems
Kiểm tra tất cả các thang điểm trong chuyên ngành Phẫu Thuật & Gây Mê
"""

import sys
from scores.config import SCORES_BY_SPECIALTY
from scores.surgery import render_surgery_calculator

def test_imports():
    """Test 1: Kiểm tra imports"""
    print("=" * 60)
    print("TEST 1: Kiểm tra imports")
    print("=" * 60)
    
    try:
        from scores.surgery import render_surgery_calculator
        from scores.surgery.asa import render as render_asa
        from scores.surgery.aldrete import render as render_aldrete
        from scores.surgery.mallampati import render as render_mallampati
        from scores.surgery.rcri import render as render_rcri
        from scores.surgery.caprini import render as render_caprini
        from scores.surgery.possum import render as render_possum
        from scores.surgery.apfel_ponv import render as render_apfel_ponv
        from scores.surgery.koivuranta_ponv import render as render_koivuranta_ponv
        from scores.surgery.wilson_risk import render as render_wilson_risk
        from scores.surgery.el_ganzouri import render as render_el_ganzouri
        from scores.surgery.lemon import render as render_lemon
        from scores.surgery.cormack_lehane import render as render_cormack_lehane
        from scores.surgery.ramsay import render as render_ramsay
        from scores.surgery.rass import render as render_rass
        from scores.surgery.riker_sas import render as render_riker_sas
        from scores.surgery.padss import render as render_padss
        from scores.surgery.ariscat import render as render_ariscat
        from scores.surgery.cam_icu import render as render_cam_icu
        from scores.surgery.four_at import render as render_four_at
        
        # New scores
        from scores.surgery.surgical_apgar import render as render_surgical_apgar
        from scores.surgery.sort import render as render_sort
        from scores.surgery.gupta_cardiac import render as render_gupta_cardiac
        from scores.surgery.goldman_cardiac import render as render_goldman_cardiac
        
        print("✅ Tất cả imports thành công!")
        return True
    except Exception as e:
        print(f"❌ Lỗi import: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_config():
    """Test 2: Kiểm tra config"""
    print("\n" + "=" * 60)
    print("TEST 2: Kiểm tra config")
    print("=" * 60)
    
    try:
        surgery_scores = SCORES_BY_SPECIALTY.get("🔪 Phẫu Thuật & Gây Mê (Surgery/Anesthesia)", {})
        
        print(f"Tổng số thang điểm: {len(surgery_scores)}")
        print("\nDanh sách thang điểm:")
        for i, (score_id, score_info) in enumerate(surgery_scores.items(), 1):
            status = score_info.get("status", "❓")
            name = score_info.get("name", "N/A")
            desc = score_info.get("desc", "N/A")
            print(f"  {i:2d}. {status} {score_id:25s} - {name}")
        
        # Check new scores
        new_scores = ["Surgical Apgar", "SORT", "Gupta Cardiac", "Goldman Cardiac"]
        print("\n✅ Kiểm tra thang điểm mới:")
        for score_id in new_scores:
            if score_id in surgery_scores:
                print(f"  ✅ {score_id} - Có trong config")
            else:
                print(f"  ❌ {score_id} - KHÔNG có trong config")
        
        return True
    except Exception as e:
        print(f"❌ Lỗi config: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_calculation_functions():
    """Test 3: Kiểm tra calculation functions"""
    print("\n" + "=" * 60)
    print("TEST 3: Kiểm tra calculation functions")
    print("=" * 60)
    
    test_results = []
    
    # Test Surgical Apgar
    try:
        from scores.surgery.surgical_apgar import calculate_surgical_apgar
        result = calculate_surgical_apgar(2, 2, 2)  # Max score
        assert result['total_score'] == 6
        assert result['risk'] in ["Nguy cơ thấp", "Nguy cơ trung bình", "Nguy cơ cao"]
        print("✅ Surgical Apgar - calculate_surgical_apgar()")
        test_results.append(True)
    except Exception as e:
        print(f"❌ Surgical Apgar - {str(e)}")
        test_results.append(False)
    
    # Test SORT
    try:
        from scores.surgery.sort import calculate_sort
        result = calculate_sort(0, 1, 0, False, 0, False)  # Low risk
        assert 'risk_score' in result
        assert 'risk_percentage' in result
        print("✅ SORT - calculate_sort()")
        test_results.append(True)
    except Exception as e:
        print(f"❌ SORT - {str(e)}")
        test_results.append(False)
    
    # Test Gupta Cardiac
    try:
        from scores.surgery.gupta_cardiac import calculate_gupta_cardiac
        result = calculate_gupta_cardiac(0, False, False, False, False, 0)  # No risk
        assert result['risk_score'] == 0
        assert result['risk_percentage'] == 0.4
        print("✅ Gupta Cardiac - calculate_gupta_cardiac()")
        test_results.append(True)
    except Exception as e:
        print(f"❌ Gupta Cardiac - {str(e)}")
        test_results.append(False)
    
    # Test Goldman Cardiac
    try:
        from scores.surgery.goldman_cardiac import calculate_goldman_cardiac
        result = calculate_goldman_cardiac(
            False, False, False, False, False, False,
            False, False, False, False, False, False
        )  # No risk
        assert result['total_score'] == 0
        assert result['risk_class'] == "Class I"
        print("✅ Goldman Cardiac - calculate_goldman_cardiac()")
        test_results.append(True)
    except Exception as e:
        print(f"❌ Goldman Cardiac - {str(e)}")
        test_results.append(False)
    
    # Test other scores
    other_scores = [
        ("Apfel PONV", "scores.surgery.apfel_ponv", "calculate_apfel_ponv", (False, False, False, False)),
        ("Koivuranta PONV", "scores.surgery.koivuranta_ponv", "calculate_koivuranta_ponv", (False, False, False, 30, 0)),
        ("Wilson Risk", "scores.surgery.wilson_risk", "calculate_wilson_risk", (0, 0, 0, 0, 0)),
        ("LEMON", "scores.surgery.lemon", "calculate_lemon", (0, 0, 0, 0, 0)),
        ("ARISCAT", "scores.surgery.ariscat", "calculate_ariscat", (50, 95, False, False, 0, 60, False)),
    ]
    
    for score_name, module_path, func_name, test_args in other_scores:
        try:
            module = __import__(module_path, fromlist=[func_name])
            func = getattr(module, func_name)
            result = func(*test_args)
            assert isinstance(result, dict)
            print(f"✅ {score_name} - {func_name}()")
            test_results.append(True)
        except Exception as e:
            print(f"❌ {score_name} - {str(e)}")
            test_results.append(False)
    
    success_rate = sum(test_results) / len(test_results) * 100
    print(f"\n📊 Tỷ lệ thành công: {success_rate:.1f}% ({sum(test_results)}/{len(test_results)})")
    
    return all(test_results)

def test_routing():
    """Test 4: Kiểm tra routing"""
    print("\n" + "=" * 60)
    print("TEST 4: Kiểm tra routing")
    print("=" * 60)
    
    test_scores = [
        "ASA",
        "Aldrete Score",
        "Mallampati",
        "RCRI",
        "Caprini",
        "P-POSSUM",
        "Apfel PONV",
        "Koivuranta PONV",
        "Wilson Risk",
        "El-Ganzouri",
        "LEMON",
        "Cormack-Lehane",
        "Ramsay",
        "RASS",
        "Riker SAS",
        "PADSS",
        "ARISCAT",
        "CAM-ICU",
        "4AT",
        "Surgical Apgar",  # New
        "SORT",  # New
        "Gupta Cardiac",  # New
        "Goldman Cardiac",  # New
    ]
    
    success_count = 0
    for score_id in test_scores:
        try:
            # Check if render function exists (without actually calling it)
            render_surgery_calculator(score_id)
            print(f"✅ {score_id:25s} - Routing OK")
            success_count += 1
        except Exception as e:
            print(f"❌ {score_id:25s} - {str(e)}")
    
    print(f"\n📊 Routing thành công: {success_count}/{len(test_scores)}")
    return success_count == len(test_scores)

def main():
    """Main test function"""
    print("\n" + "=" * 60)
    print("🧪 TEST TẤT CẢ THANG ĐIỂM PHẪU THUẬT & GÂY MÊ")
    print("=" * 60)
    
    results = []
    
    # Run all tests
    results.append(("Imports", test_imports()))
    results.append(("Config", test_config()))
    results.append(("Calculation Functions", test_calculation_functions()))
    results.append(("Routing", test_routing()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TỔNG KẾT")
    print("=" * 60)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n🎉 TẤT CẢ TEST ĐỀU PASS!")
    else:
        print("\n⚠️  MỘT SỐ TEST FAIL - Vui lòng kiểm tra lại")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)




