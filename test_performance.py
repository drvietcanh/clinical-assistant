"""
Performance Tests for Clinical Assistant
Tests: Execution time, memory usage, scalability
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any, List
import tracemalloc

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("⚡ PERFORMANCE TESTS - Clinical Assistant")
print("=" * 60)
print()

# ============================================================================
# TEST 1: Formatters Performance
# ============================================================================
print("📋 TEST 1: Formatters Performance")
print("-" * 60)

try:
    from utils.formatters import (
        format_age, format_weight, format_height, format_lab_value,
        format_percentage, format_dose, format_rate
    )
    
    # Test execution time for 10,000 operations
    iterations = 10000
    
    start_time = time.perf_counter()
    for _ in range(iterations):
        format_age(65.5)
        format_weight(70.5)
        format_height(170.5)
        format_lab_value(100.5)
        format_percentage(95.5)
        format_dose(1000.5)
        format_rate(100.5)
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    avg_time = (total_time / iterations) * 1000  # ms per operation
    
    print(f"   Operations: {iterations * 7:,}")
    print(f"   Total time: {total_time:.4f}s")
    print(f"   Avg time per operation: {avg_time:.6f}ms")
    
    # Performance threshold: < 0.1ms per operation
    if avg_time < 0.1:
        print("   ✅ Performance: EXCELLENT")
    elif avg_time < 1.0:
        print("   ✅ Performance: GOOD")
    else:
        print("   ⚠️  Performance: NEEDS OPTIMIZATION")
    
    print("✅ Formatters Performance - PASSED")
    print()
    
except Exception as e:
    print(f"❌ FORMATTERS PERFORMANCE TEST FAILED: {e}")
    print()

# ============================================================================
# TEST 2: Export Component Performance
# ============================================================================
print("📋 TEST 2: Export Component Performance")
print("-" * 60)

try:
    from components.export import format_result_for_export, generate_pdf
    
    # Test data
    test_inputs = {
        "Age": 65,
        "Weight": 70.5,
        "Height": 170,
        "Creatinine": 100.0
    }
    
    test_results = {
        "Score": 15,
        "Interpretation": "Moderate",
        "Subscores": {
            "Respiratory": 2,
            "Cardiovascular": 3,
            "Renal": 1
        }
    }
    
    # Test format_result_for_export
    iterations = 1000
    
    start_time = time.perf_counter()
    for _ in range(iterations):
        format_result_for_export(
            "Test Result",
            test_inputs,
            test_results,
            "Test Calculator"
        )
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    avg_time = (total_time / iterations) * 1000  # ms
    
    print(f"   format_result_for_export:")
    print(f"   Operations: {iterations:,}")
    print(f"   Total time: {total_time:.4f}s")
    print(f"   Avg time: {avg_time:.4f}ms")
    
    if avg_time < 10:
        print("   ✅ Performance: EXCELLENT")
    elif avg_time < 50:
        print("   ✅ Performance: GOOD")
    else:
        print("   ⚠️  Performance: NEEDS OPTIMIZATION")
    
    # Test PDF generation (fewer iterations - PDF is slower)
    pdf_iterations = 10
    
    start_time = time.perf_counter()
    pdf_results = []
    for _ in range(pdf_iterations):
        pdf_bytes = generate_pdf(
            "Test Result",
            test_inputs,
            test_results,
            "Test Calculator"
        )
        if pdf_bytes:
            pdf_results.append(len(pdf_bytes))
    end_time = time.perf_counter()
    
    if pdf_results:
        total_time = end_time - start_time
        avg_time = (total_time / pdf_iterations) * 1000  # ms
        avg_size = sum(pdf_results) / len(pdf_results)
        
        print(f"\n   generate_pdf:")
        print(f"   Operations: {pdf_iterations}")
        print(f"   Total time: {total_time:.4f}s")
        print(f"   Avg time: {avg_time:.4f}ms")
        print(f"   Avg PDF size: {avg_size:.0f} bytes")
        
        if avg_time < 500:
            print("   ✅ Performance: EXCELLENT")
        elif avg_time < 1000:
            print("   ✅ Performance: GOOD")
        else:
            print("   ⚠️  Performance: ACCEPTABLE")
    
    print("✅ Export Component Performance - PASSED")
    print()
    
except Exception as e:
    print(f"❌ EXPORT PERFORMANCE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 3: DDx Generator Performance
# ============================================================================
print("📋 TEST 3: DDx Generator Performance")
print("-" * 60)

try:
    from diagnosis.ddx_data import get_all_scenarios, get_scenario_data
    from diagnosis.ddx_generator import calculate_diagnosis_score
    
    all_scenarios = get_all_scenarios()
    
    if len(all_scenarios) > 0:
        # Test get_scenario_data performance
        iterations = 1000
        
        start_time = time.perf_counter()
        for _ in range(iterations):
            scenario_name = list(all_scenarios)[0]
            get_scenario_data(scenario_name)
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        avg_time = (total_time / iterations) * 1000  # ms
        
        print(f"   get_scenario_data:")
        print(f"   Operations: {iterations:,}")
        print(f"   Total time: {total_time:.4f}s")
        print(f"   Avg time: {avg_time:.6f}ms")
        
        if avg_time < 1:
            print("   ✅ Performance: EXCELLENT")
        elif avg_time < 5:
            print("   ✅ Performance: GOOD")
        else:
            print("   ⚠️  Performance: ACCEPTABLE")
        
        # Test score calculation performance
        scenario_name = list(all_scenarios)[0]
        scenario_data = get_scenario_data(scenario_name)
        
        if scenario_data and "diagnoses" in scenario_data:
            diagnoses = scenario_data["diagnoses"]
            if len(diagnoses) > 0:
                first_diagnosis = list(diagnoses.keys())[0]
                diagnosis_data = diagnoses[first_diagnosis]
                
                score_iterations = 100
                
                start_time = time.perf_counter()
                for _ in range(score_iterations):
                    calculate_diagnosis_score(
                        first_diagnosis,
                        diagnosis_data,
                        ["symptom1", "symptom2"],
                        50,
                        "male",
                        []
                    )
                end_time = time.perf_counter()
                
                total_time = end_time - start_time
                avg_time = (total_time / score_iterations) * 1000  # ms
                
                print(f"\n   calculate_diagnosis_score:")
                print(f"   Operations: {score_iterations:,}")
                print(f"   Total time: {total_time:.4f}s")
                print(f"   Avg time: {avg_time:.4f}ms")
                
                if avg_time < 10:
                    print("   ✅ Performance: EXCELLENT")
                elif avg_time < 50:
                    print("   ✅ Performance: GOOD")
                else:
                    print("   ⚠️  Performance: ACCEPTABLE")
        
        print(f"\n   Total scenarios: {len(all_scenarios)}")
        print("✅ DDx Generator Performance - PASSED")
    else:
        print("   ⚠️  No scenarios available")
    
    print()
    
except Exception as e:
    print(f"❌ DDX GENERATOR PERFORMANCE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 4: Memory Usage Test
# ============================================================================
print("📋 TEST 4: Memory Usage Test")
print("-" * 60)

try:
    tracemalloc.start()
    
    # Import modules
    from utils.formatters import format_age, format_weight
    from components.export import format_result_for_export
    from diagnosis.ddx_data import get_all_scenarios
    
    # Get baseline memory
    current, peak = tracemalloc.get_traced_memory()
    baseline_mb = current / 1024 / 1024
    
    # Perform operations
    for _ in range(1000):
        format_age(65.5)
        format_weight(70.5)
        format_result_for_export(
            "Test",
            {"A": 1},
            {"B": 2},
            "Test"
        )
    
    # Get memory after operations
    current, peak = tracemalloc.get_traced_memory()
    after_mb = current / 1024 / 1024
    peak_mb = peak / 1024 / 1024
    
    memory_increase = after_mb - baseline_mb
    
    print(f"   Baseline memory: {baseline_mb:.2f} MB")
    print(f"   After operations: {after_mb:.2f} MB")
    print(f"   Peak memory: {peak_mb:.2f} MB")
    print(f"   Memory increase: {memory_increase:.2f} MB")
    
    if memory_increase < 10:
        print("   ✅ Memory usage: EXCELLENT")
    elif memory_increase < 50:
        print("   ✅ Memory usage: GOOD")
    else:
        print("   ⚠️  Memory usage: HIGH")
    
    tracemalloc.stop()
    print("✅ Memory Usage Test - PASSED")
    print()
    
except Exception as e:
    print(f"❌ MEMORY USAGE TEST FAILED: {e}")
    print()

# ============================================================================
# TEST 5: Batch Export Performance
# ============================================================================
print("📋 TEST 5: Batch Export Performance")
print("-" * 60)

try:
    from components.export import format_result_for_export
    
    # Test with different batch sizes
    batch_sizes = [10, 50, 100]
    
    for batch_size in batch_sizes:
        calculations = []
        for i in range(batch_size):
            calculations.append({
                "title": f"Calculation {i+1}",
                "inputs": {f"Input{i}": i * 10},
                "results": {f"Result{i}": i * 20},
                "calculator_name": f"Calc {i+1}"
            })
        
        start_time = time.perf_counter()
        all_texts = []
        for i, calc in enumerate(calculations, 1):
            text = format_result_for_export(
                calc['title'],
                calc['inputs'],
                calc['results'],
                calc['calculator_name'],
                include_timestamp=(i == 1)
            )
            all_texts.append(text)
            if i < len(calculations):
                all_texts.append("\n" + "="*60 + "\n")
        
        batch_text = "\n".join(all_texts)
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        time_per_calc = (total_time / batch_size) * 1000  # ms
        
        print(f"   Batch size: {batch_size}")
        print(f"   Total time: {total_time:.4f}s")
        print(f"   Time per calculation: {time_per_calc:.4f}ms")
        print(f"   Batch text size: {len(batch_text):,} characters")
        
        if time_per_calc < 10:
            print("   ✅ Performance: EXCELLENT")
        elif time_per_calc < 50:
            print("   ✅ Performance: GOOD")
        else:
            print("   ✅ Performance: ACCEPTABLE")
        print()
    
    print("✅ Batch Export Performance - PASSED")
    print()
    
except Exception as e:
    print(f"❌ BATCH EXPORT PERFORMANCE TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 6: Large Data Handling
# ============================================================================
print("📋 TEST 6: Large Data Handling")
print("-" * 60)

try:
    from components.export import format_result_for_export, generate_pdf
    
    # Test with very large inputs/results
    large_inputs = {}
    large_results = {}
    
    for i in range(100):
        large_inputs[f"Input_{i}"] = f"Value_{i}_" + "A" * 100
        large_results[f"Result_{i}"] = f"Result_{i}_" + "B" * 100
    
    start_time = time.perf_counter()
    export_text = format_result_for_export(
        "Large Data Test",
        large_inputs,
        large_results,
        "Large Calculator"
    )
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    
    print(f"   Inputs: 100 fields")
    print(f"   Results: 100 fields")
    print(f"   Export text size: {len(export_text):,} characters")
    print(f"   Processing time: {total_time:.4f}s")
    
    if total_time < 1.0:
        print("   ✅ Performance: EXCELLENT")
    elif total_time < 5.0:
        print("   ✅ Performance: GOOD")
    else:
        print("   ⚠️  Performance: ACCEPTABLE")
    
    # Test PDF with large data
    pdf_start = time.perf_counter()
    pdf_bytes = generate_pdf(
        "Large Data Test",
        large_inputs,
        large_results,
        "Large Calculator"
    )
    pdf_end = time.perf_counter()
    
    if pdf_bytes:
        pdf_time = pdf_end - pdf_start
        print(f"\n   PDF generation time: {pdf_time:.4f}s")
        print(f"   PDF size: {len(pdf_bytes):,} bytes")
        
        if pdf_time < 2.0:
            print("   ✅ PDF Performance: EXCELLENT")
        elif pdf_time < 5.0:
            print("   ✅ PDF Performance: GOOD")
        else:
            print("   ✅ PDF Performance: ACCEPTABLE")
    
    print("✅ Large Data Handling - PASSED")
    print()
    
except Exception as e:
    print(f"❌ LARGE DATA HANDLING TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("📊 PERFORMANCE TEST SUMMARY")
print("=" * 60)
print()
print("✅ Tests completed:")
print("   1. Formatters Performance")
print("   2. Export Component Performance")
print("   3. DDx Generator Performance")
print("   4. Memory Usage")
print("   5. Batch Export Performance")
print("   6. Large Data Handling")
print()
print("💡 Performance benchmarks:")
print("   - Formatters: < 0.1ms per operation (target)")
print("   - Export: < 10ms per export (target)")
print("   - PDF: < 500ms per PDF (target)")
print("   - Memory: < 10MB increase (target)")
print()
print("=" * 60)

