"""
Demo script for data management features
Avoids streamlit dependency
"""
import sys
import io

# Fix encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Mock streamlit
class MockStreamlit:
    def __getattr__(self, name):
        return lambda *args, **kwargs: None

sys.modules['streamlit'] = MockStreamlit()

print("=" * 80)
print("DEMO CAC TINH NANG QUAN LY DU LIEU THUOC")
print("=" * 80)

# Test 1: Quality Check
print("\n1. KIEM TRA CHAT LUONG DU LIEU")
print("-" * 80)
try:
    from drugs.data_quality_manager import check_all_quality, calculate_quality_metrics
    
    # Quick check (limit to avoid too much output)
    print("Dang kiem tra...")
    errors = check_all_quality()
    
    # Group by severity
    by_severity = {"error": 0, "warning": 0, "info": 0}
    for error in errors:
        by_severity[error.severity] += 1
    
    print(f"Tim thay {len(errors)} van de:")
    print(f"  - Errors: {by_severity['error']}")
    print(f"  - Warnings: {by_severity['warning']}")
    print(f"  - Info: {by_severity['info']}")
    
    # Metrics
    metrics = calculate_quality_metrics()
    print(f"\nDiem chat luong: {metrics['quality_score']:.1f}/100")
    print(f"Ty le loi: {metrics['error_rate']:.1f}%")
    print(f"Thuoc co loi: {metrics['drugs_with_errors']}")
except Exception as e:
    print(f"Loi: {e}")
    import traceback
    traceback.print_exc()

# Test 2: Integrity Check
print("\n2. KIEM TRA TINH TOAN VEN")
print("-" * 80)
try:
    from drugs.data_integrity_checker import check_all_integrity
    
    print("Dang kiem tra...")
    result = check_all_integrity()
    print(f"Tong so van de: {result['total_issues']}")
    print(f"Thuoc bi anh huong: {result['drugs_affected']}")
    print(f"Errors: {result['summary']['errors']}")
    print(f"Warnings: {result['summary']['warnings']}")
    print(f"Info: {result['summary']['info']}")
except Exception as e:
    print(f"Loi: {e}")

# Test 3: Search
print("\n3. TIM KIEM NANG CAO")
print("-" * 80)
try:
    from drugs.data_search_enhancer import fuzzy_search_drugs, get_search_suggestions
    
    # Fuzzy search
    print("Fuzzy search 'metform'...")
    results = fuzzy_search_drugs("metform", threshold=0.5, limit=5)
    print(f"Tim thay {len(results)} ket qua:")
    for drug_name, score, _ in results[:3]:
        print(f"  - {drug_name} (do tuong dong: {score:.1%})")
    
    # Suggestions
    suggestions = get_search_suggestions("metform", limit=3)
    print(f"\nGoi y cho 'metform': {suggestions}")
except Exception as e:
    print(f"Loi: {e}")

# Test 4: Duplicates
print("\n4. TIM THUOC TRUNG LAP")
print("-" * 80)
try:
    from drugs.drug_manager import list_duplicate_drugs
    
    print("Dang tim kiem...")
    duplicates = list_duplicate_drugs()
    print(f"Tim thay {len(duplicates)} thuoc trung lap")
    if duplicates:
        print("Vi du (3 dau tien):")
        for dup in duplicates[:3]:
            print(f"  - {dup['drug_name']}: xuat hien trong {dup['count']} modules")
except Exception as e:
    print(f"Loi: {e}")

# Test 5: Missing Fields
print("\n5. TIM THUOC THIEU FIELDS")
print("-" * 80)
try:
    from drugs.enhanced_fields_manager import find_drugs_needing_fields
    
    print("Dang tim kiem thuoc thieu drug_interactions...")
    results = find_drugs_needing_fields(["drug_interactions"], limit=5)
    print(f"Tim thay {len(results)} thuoc thieu drug_interactions")
    if results:
        print("Vi du (3 dau tien):")
        for drug_name, missing_fields, file_path in results[:3]:
            print(f"  - {drug_name}: thieu {', '.join(missing_fields)}")
except Exception as e:
    print(f"Loi: {e}")

print("\n" + "=" * 80)
print("DEMO HOAN TAT")
print("=" * 80)
print("\nSu dung CLI de xem chi tiet:")
print("  python -m drugs.data_management_cli quality")
print("  python -m drugs.data_management_cli integrity")
print("  python -m drugs.data_management_cli search 'metformin' --fuzzy")
print("  python -m drugs.data_management_cli metrics")

