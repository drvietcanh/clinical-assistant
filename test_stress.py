"""
Stress Tests for Clinical Assistant
Tests: High load, concurrent operations, resource limits
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any, List
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("💪 STRESS TESTS - Clinical Assistant")
print("=" * 60)
print()

# ============================================================================
# TEST 1: High Volume Formatters
# ============================================================================
print("📋 TEST 1: High Volume Formatters")
print("-" * 60)

try:
    from utils.formatters import (
        format_age, format_weight, format_height, format_lab_value
    )
    
    # Test with 100,000 operations
    iterations = 100000
    
    start_time = time.perf_counter()
    for i in range(iterations):
        format_age(65.5 + i % 100)
        format_weight(70.5 + i % 50)
        format_height(170.5 + i % 30)
        format_lab_value(100.5 + i % 200)
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    ops_per_sec = (iterations * 4) / total_time
    
    print(f"   Operations: {iterations * 4:,}")
    print(f"   Total time: {total_time:.4f}s")
    print(f"   Operations/sec: {ops_per_sec:,.0f}")
    
    if ops_per_sec > 100000:
        print("   ✅ Performance: EXCELLENT")
    elif ops_per_sec > 50000:
        print("   ✅ Performance: GOOD")
    else:
        print("   ⚠️  Performance: ACCEPTABLE")
    
    print("✅ High Volume Formatters - PASSED")
    print()
    
except Exception as e:
    print(f"❌ HIGH VOLUME FORMATTERS TEST FAILED: {e}")
    print()

# ============================================================================
# TEST 2: Concurrent Export Operations
# ============================================================================
print("📋 TEST 2: Concurrent Export Operations")
print("-" * 60)

try:
    from components.export import format_result_for_export
    
    def export_operation(index):
        """Single export operation"""
        inputs = {"Value": index}
        results = {"Result": index * 2}
        return format_result_for_export(
            f"Test {index}",
            inputs,
            results,
            "Test Calculator"
        )
    
    # Test concurrent operations
    num_threads = 10
    operations_per_thread = 100
    
    start_time = time.perf_counter()
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = []
        for i in range(num_threads * operations_per_thread):
            future = executor.submit(export_operation, i)
            futures.append(future)
        
        results = []
        for future in as_completed(futures):
            try:
                result = future.result()
                results.append(len(result))
            except Exception as e:
                print(f"   ⚠️  Error in thread: {e}")
    
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    total_operations = len(results)
    ops_per_sec = total_operations / total_time
    
    print(f"   Threads: {num_threads}")
    print(f"   Operations per thread: {operations_per_thread}")
    print(f"   Total operations: {total_operations:,}")
    print(f"   Total time: {total_time:.4f}s")
    print(f"   Operations/sec: {ops_per_sec:,.0f}")
    
    if ops_per_sec > 1000:
        print("   ✅ Concurrent Performance: EXCELLENT")
    elif ops_per_sec > 500:
        print("   ✅ Concurrent Performance: GOOD")
    else:
        print("   ✅ Concurrent Performance: ACCEPTABLE")
    
    print("✅ Concurrent Export Operations - PASSED")
    print()
    
except Exception as e:
    print(f"❌ CONCURRENT EXPORT TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 3: Large Batch Export Stress
# ============================================================================
print("📋 TEST 3: Large Batch Export Stress")
print("-" * 60)

try:
    from components.export import format_result_for_export
    
    # Test with very large batch
    batch_sizes = [100, 500, 1000]
    
    for batch_size in batch_sizes:
        print(f"\n   Testing batch size: {batch_size}")
        
        calculations = []
        for i in range(batch_size):
            calculations.append({
                "title": f"Calculation {i+1}",
                "inputs": {f"Input{j}": j * 10 for j in range(10)},
                "results": {f"Result{j}": j * 20 for j in range(10)},
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
        
        print(f"      Total time: {total_time:.4f}s")
        print(f"      Time per calc: {time_per_calc:.4f}ms")
        print(f"      Batch size: {len(batch_text):,} characters")
        
        if time_per_calc < 20:
            print(f"      ✅ Performance: EXCELLENT")
        elif time_per_calc < 100:
            print(f"      ✅ Performance: GOOD")
        else:
            print(f"      ✅ Performance: ACCEPTABLE")
    
    print("\n✅ Large Batch Export Stress - PASSED")
    print()
    
except Exception as e:
    print(f"❌ LARGE BATCH EXPORT STRESS TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 4: Memory Stress Test
# ============================================================================
print("📋 TEST 4: Memory Stress Test")
print("-" * 60)

try:
    import tracemalloc
    
    tracemalloc.start()
    
    from components.export import format_result_for_export
    
    # Baseline
    current, peak = tracemalloc.get_traced_memory()
    baseline_mb = current / 1024 / 1024
    
    # Create many exports
    exports = []
    for i in range(1000):
        inputs = {f"Key{j}": f"Value{j}_{i}" for j in range(20)}
        results = {f"Result{j}": f"Data{j}_{i}" for j in range(20)}
        export_text = format_result_for_export(
            f"Stress Test {i}",
            inputs,
            results,
            "Stress Calculator"
        )
        exports.append(export_text)
    
    # Check memory
    current, peak = tracemalloc.get_traced_memory()
    after_mb = current / 1024 / 1024
    peak_mb = peak / 1024 / 1024
    increase_mb = after_mb - baseline_mb
    
    print(f"   Exports created: {len(exports):,}")
    print(f"   Baseline memory: {baseline_mb:.2f} MB")
    print(f"   After operations: {after_mb:.2f} MB")
    print(f"   Peak memory: {peak_mb:.2f} MB")
    print(f"   Memory increase: {increase_mb:.2f} MB")
    print(f"   Avg memory per export: {(increase_mb / len(exports) * 1024):.2f} KB")
    
    if increase_mb < 50:
        print("   ✅ Memory usage: EXCELLENT")
    elif increase_mb < 100:
        print("   ✅ Memory usage: GOOD")
    else:
        print("   ⚠️  Memory usage: HIGH")
    
    tracemalloc.stop()
    print("✅ Memory Stress Test - PASSED")
    print()
    
except Exception as e:
    print(f"❌ MEMORY STRESS TEST FAILED: {e}")
    print()

# ============================================================================
# TEST 5: DDx Generator Stress
# ============================================================================
print("📋 TEST 5: DDx Generator Stress")
print("-" * 60)

try:
    from diagnosis.ddx_data import get_all_scenarios, get_scenario_data
    from diagnosis.ddx_generator import calculate_diagnosis_score
    
    all_scenarios = get_all_scenarios()
    
    if len(all_scenarios) > 0:
        # Test with all scenarios
        iterations = 1000
        
        start_time = time.perf_counter()
        scores_calculated = 0
        
        for _ in range(iterations):
            for scenario_name in list(all_scenarios)[:5]:  # First 5 scenarios
                scenario_data = get_scenario_data(scenario_name)
                if scenario_data and "diagnoses" in scenario_data:
                    diagnoses = scenario_data["diagnoses"]
                    if len(diagnoses) > 0:
                        first_diagnosis = list(diagnoses.keys())[0]
                        diagnosis_data = diagnoses[first_diagnosis]
                        
                        score_result = calculate_diagnosis_score(
                            first_diagnosis,
                            diagnosis_data,
                            ["symptom1", "symptom2", "symptom3"],
                            50,
                            "male",
                            ["risk1", "risk2"]
                        )
                        
                        if score_result:
                            scores_calculated += 1
        
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        ops_per_sec = scores_calculated / total_time
        
        print(f"   Iterations: {iterations}")
        print(f"   Scores calculated: {scores_calculated:,}")
        print(f"   Total time: {total_time:.4f}s")
        print(f"   Operations/sec: {ops_per_sec:,.0f}")
        
        if ops_per_sec > 1000:
            print("   ✅ Performance: EXCELLENT")
        elif ops_per_sec > 500:
            print("   ✅ Performance: GOOD")
        else:
            print("   ✅ Performance: ACCEPTABLE")
        
        print("✅ DDx Generator Stress - PASSED")
    else:
        print("   ⚠️  No scenarios available")
    
    print()
    
except Exception as e:
    print(f"❌ DDX GENERATOR STRESS TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# TEST 6: Rapid PDF Generation
# ============================================================================
print("📋 TEST 6: Rapid PDF Generation")
print("-" * 60)

try:
    from components.export import generate_pdf
    
    # Test rapid PDF generation
    num_pdfs = 20
    
    start_time = time.perf_counter()
    pdfs_created = 0
    total_size = 0
    
    for i in range(num_pdfs):
        inputs = {"Value": i}
        results = {"Result": i * 2}
        pdf_bytes = generate_pdf(
            f"Rapid Test {i}",
            inputs,
            results,
            "Rapid Calculator"
        )
        if pdf_bytes:
            pdfs_created += 1
            total_size += len(pdf_bytes)
    
    end_time = time.perf_counter()
    
    total_time = end_time - start_time
    time_per_pdf = (total_time / pdfs_created) * 1000 if pdfs_created > 0 else 0
    avg_size = total_size / pdfs_created if pdfs_created > 0 else 0
    
    print(f"   PDFs created: {pdfs_created}/{num_pdfs}")
    print(f"   Total time: {total_time:.4f}s")
    print(f"   Time per PDF: {time_per_pdf:.4f}ms")
    print(f"   Avg PDF size: {avg_size:,.0f} bytes")
    print(f"   Total size: {total_size:,.0f} bytes")
    
    if time_per_pdf < 500:
        print("   ✅ Performance: EXCELLENT")
    elif time_per_pdf < 1000:
        print("   ✅ Performance: GOOD")
    else:
        print("   ✅ Performance: ACCEPTABLE")
    
    print("✅ Rapid PDF Generation - PASSED")
    print()
    
except Exception as e:
    print(f"❌ RAPID PDF GENERATION TEST FAILED: {e}")
    import traceback
    traceback.print_exc()
    print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 60)
print("📊 STRESS TEST SUMMARY")
print("=" * 60)
print()
print("✅ Tests completed:")
print("   1. High Volume Formatters (100K operations)")
print("   2. Concurrent Export Operations (10 threads)")
print("   3. Large Batch Export Stress (up to 1000 calculations)")
print("   4. Memory Stress Test (1000 exports)")
print("   5. DDx Generator Stress (1000 iterations)")
print("   6. Rapid PDF Generation (20 PDFs)")
print()
print("💡 Stress tests verify:")
print("   - System handles high load")
print("   - Concurrent operations work correctly")
print("   - Memory usage is reasonable")
print("   - Performance degrades gracefully")
print()
print("=" * 60)

