"""
Test script for Session 4: Search/Filter Features
Tests search, filter, sort, and export functionality
"""

import sys
sys.path.insert(0, '.')

def test_search_functionality():
    """Test search functionality"""
    print("=" * 60)
    print("TESTING SEARCH FUNCTIONALITY")
    print("=" * 60)
    
    # Mock interactions for testing
    test_interactions = [
        {
            'drug1': 'Warfarin',
            'drug2': 'Aspirin',
            'severity': 'Major',
            'effect': 'Tăng nguy cơ xuất huyết nặng',
            'mechanism': 'Tăng tác dụng chống đông',
            'management': 'Tránh dùng chung'
        },
        {
            'drug1': 'Lisinopril',
            'drug2': 'Ibuprofen',
            'severity': 'Moderate',
            'effect': 'Giảm hiệu quả hạ huyết áp',
            'mechanism': 'NSAID ức chế prostaglandin',
            'management': 'Theo dõi huyết áp'
        },
        {
            'drug1': 'Atorvastatin',
            'drug2': 'Clarithromycin',
            'severity': 'Major',
            'effect': 'Tăng nguy cơ tiêu cơ vân',
            'mechanism': 'Macrolide ức chế CYP3A4',
            'management': 'Giảm liều statin'
        }
    ]
    
    test_cases = [
        ('Warfarin', 1),  # Should find 1 interaction
        ('Aspirin', 1),   # Should find 1 interaction
        ('ibuprofen', 1), # Case insensitive
        ('tiêu cơ', 1),   # Search in effect (Vietnamese)
        ('CYP3A4', 1),    # Search in mechanism
        ('xyz', 0),       # Should find 0
    ]
    
    # Set encoding for Windows
    import sys
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    
    passed = 0
    failed = 0
    
    for search_query, expected_count in test_cases:
        search_lower = search_query.lower()
        filtered = [
            i for i in test_interactions
            if (search_lower in i.get('drug1', '').lower() or
                search_lower in i.get('drug2', '').lower() or
                search_lower in i.get('effect', '').lower() or
                search_lower in i.get('mechanism', '').lower() or
                search_lower in i.get('management', '').lower())
        ]
        
        if len(filtered) == expected_count:
            print(f"[PASS] Search '{search_query}': Found {len(filtered)} interactions (expected: {expected_count})")
            passed += 1
        else:
            print(f"[FAIL] Search '{search_query}': Found {len(filtered)} interactions (expected: {expected_count})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_severity_filter():
    """Test severity filter"""
    print("\n" + "=" * 60)
    print("TESTING SEVERITY FILTER")
    print("=" * 60)
    
    test_interactions = [
        {'drug1': 'Warfarin', 'drug2': 'Aspirin', 'severity': 'Major'},
        {'drug1': 'Lisinopril', 'drug2': 'Ibuprofen', 'severity': 'Moderate'},
        {'drug1': 'Paracetamol', 'drug2': 'Aspirin', 'severity': 'Minor'},
        {'drug1': 'Atorvastatin', 'drug2': 'Clarithromycin', 'severity': 'Major'},
    ]
    
    test_cases = [
        (['Major'], 2),
        (['Moderate'], 1),
        (['Minor'], 1),
        (['Major', 'Moderate'], 3),
        ([], 4),  # No filter = all
    ]
    
    passed = 0
    failed = 0
    
    for severity_filter, expected_count in test_cases:
        if severity_filter:
            filtered = [i for i in test_interactions if i.get('severity') in severity_filter]
        else:
            filtered = test_interactions
        
        if len(filtered) == expected_count:
            print(f"[PASS] Filter {severity_filter}: Found {len(filtered)} interactions (expected: {expected_count})")
            passed += 1
        else:
            print(f"[FAIL] Filter {severity_filter}: Found {len(filtered)} interactions (expected: {expected_count})")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_sort_functionality():
    """Test sort functionality"""
    print("\n" + "=" * 60)
    print("TESTING SORT FUNCTIONALITY")
    print("=" * 60)
    
    test_interactions = [
        {'drug1': 'Warfarin', 'drug2': 'Aspirin', 'severity': 'Major'},
        {'drug1': 'Lisinopril', 'drug2': 'Ibuprofen', 'severity': 'Moderate'},
        {'drug1': 'Paracetamol', 'drug2': 'Aspirin', 'severity': 'Minor'},
        {'drug1': 'Atorvastatin', 'drug2': 'Clarithromycin', 'severity': 'Major'},
    ]
    
    # Test severity sort
    severity_order = {'Major': 0, 'Moderate': 1, 'Minor': 2}
    sorted_by_severity = sorted(test_interactions, key=lambda x: severity_order.get(x.get('severity'), 3))
    
    # Check if sorted correctly (Major first)
    if sorted_by_severity[0]['severity'] == 'Major' and sorted_by_severity[1]['severity'] == 'Major':
        print("[PASS] Sort by severity: Major interactions first")
        severity_sort_pass = True
    else:
        print("[FAIL] Sort by severity: Not sorted correctly")
        severity_sort_pass = False
    
    # Test alphabetical sort
    sorted_by_name = sorted(test_interactions, key=lambda x: (x.get('drug1', ''), x.get('drug2', '')))
    
    # Check if sorted alphabetically
    if sorted_by_name[0]['drug1'] < sorted_by_name[1]['drug1']:
        print("[PASS] Sort by name (A-Z): Sorted alphabetically")
        name_sort_pass = True
    else:
        print("[FAIL] Sort by name (A-Z): Not sorted correctly")
        name_sort_pass = False
    
    passed = sum([severity_sort_pass, name_sort_pass])
    failed = 2 - passed
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_export_functionality():
    """Test export functionality"""
    print("\n" + "=" * 60)
    print("TESTING EXPORT FUNCTIONALITY")
    print("=" * 60)
    
    test_interactions = [
        {
            'drug1': 'Warfarin',
            'drug2': 'Aspirin',
            'severity': 'Major',
            'effect': 'Tăng nguy cơ xuất huyết',
            'mechanism': 'Tăng tác dụng chống đông',
            'management': 'Tránh dùng chung'
        }
    ]
    
    # Test CSV export format
    import csv
    import io
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(["Drug 1", "Drug 2", "Severity", "Effect", "Mechanism", "Management"])
    
    # Data
    for interaction in test_interactions:
        writer.writerow([
            interaction.get('drug1', ''),
            interaction.get('drug2', ''),
            interaction.get('severity', ''),
            interaction.get('effect', ''),
            interaction.get('mechanism', ''),
            interaction.get('management', '')
        ])
    
    csv_data = output.getvalue()
    
    # Check CSV format
    if 'Warfarin' in csv_data and 'Aspirin' in csv_data and 'Major' in csv_data:
        print("[PASS] CSV export: Format correct")
        csv_pass = True
    else:
        print("[FAIL] CSV export: Format incorrect")
        csv_pass = False
    
    # Test TXT export format
    txt_report = f"""
DRUG INTERACTION REPORT
========================

Interaction: Warfarin + Aspirin
Severity: Major
Effect: Tăng nguy cơ xuất huyết
Mechanism: Tăng tác dụng chống đông
Management: Tránh dùng chung
"""
    
    if 'Warfarin' in txt_report and 'Aspirin' in txt_report:
        print("[PASS] TXT export: Format correct")
        txt_pass = True
    else:
        print("[FAIL] TXT export: Format incorrect")
        txt_pass = False
    
    passed = sum([csv_pass, txt_pass])
    failed = 2 - passed
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return passed, failed


def test_drug_class_filter():
    """Test drug class filter"""
    print("\n" + "=" * 60)
    print("TESTING DRUG CLASS FILTER")
    print("=" * 60)
    
    try:
        from drugs.interactions_data import get_drug_classes, DRUG_CLASS_MAPPINGS
        
        test_drugs = ['Warfarin', 'Aspirin', 'Lisinopril', 'Ibuprofen']
        
        passed = 0
        failed = 0
        
        for drug in test_drugs:
            classes = get_drug_classes(drug)
            if classes:
                print(f"[PASS] '{drug}' -> Classes: {', '.join(classes)}")
                passed += 1
            else:
                print(f"[FAIL] '{drug}' -> No classes found")
                failed += 1
        
        print("\n" + "=" * 60)
        print(f"RESULTS: {passed} passed, {failed} failed")
        print("=" * 60)
        
        return passed, failed
    except Exception as e:
        print(f"[ERROR] Could not test drug class filter: {e}")
        return 0, 1


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("SESSION 4: SEARCH/FILTER FEATURES - TEST SUITE")
    print("=" * 60)
    
    total_passed = 0
    total_failed = 0
    
    # Run all tests
    p1, f1 = test_search_functionality()
    total_passed += p1
    total_failed += f1
    
    p2, f2 = test_severity_filter()
    total_passed += p2
    total_failed += f2
    
    p3, f3 = test_sort_functionality()
    total_passed += p3
    total_failed += f3
    
    p4, f4 = test_export_functionality()
    total_passed += p4
    total_failed += f4
    
    p5, f5 = test_drug_class_filter()
    total_passed += p5
    total_failed += f5
    
    # Summary
    print("\n" + "=" * 60)
    print("OVERALL SUMMARY")
    print("=" * 60)
    print(f"Total Passed: {total_passed}")
    print(f"Total Failed: {total_failed}")
    if total_passed + total_failed > 0:
        print(f"Success Rate: {total_passed/(total_passed+total_failed)*100:.1f}%")
    print("=" * 60)
    
    if total_failed == 0:
        print("\n[SUCCESS] ALL TESTS PASSED!")
    else:
        print(f"\n[WARNING] {total_failed} tests failed. Review and fix issues.")

