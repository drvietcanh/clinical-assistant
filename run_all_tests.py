"""
Test Runner - Run All Test Suites
Executes all test files and generates comprehensive report
"""

import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 80)
print("🧪 CLINICAL ASSISTANT - COMPREHENSIVE TEST SUITE")
print("=" * 80)
print()
print(f"Test Run Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Test files to run
test_files = [
    ("Basic Functionality", "test_new_features.py"),
    ("Extended Tests", "test_new_features_extended.py"),
    ("Performance Tests", "test_performance.py"),
    ("Integration Tests", "test_integration.py"),
    ("Stress Tests", "test_stress.py"),
    ("Module Tests", "test_modules.py"),
    ("Regression Tests", "test_regression.py"),
]

results = []
total_start_time = time.perf_counter()

for test_name, test_file in test_files:
    test_path = project_root / test_file
    
    if not test_path.exists():
        print(f"⚠️  {test_name}: File not found ({test_file})")
        results.append((test_name, "SKIPPED", 0, "File not found"))
        continue
    
    print("=" * 80)
    print(f"Running: {test_name} ({test_file})")
    print("=" * 80)
    print()
    
    start_time = time.perf_counter()
    
    try:
        # Run test file
        result = subprocess.run(
            [sys.executable, str(test_path)],
            cwd=str(project_root),
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout per test
        )
        
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        if result.returncode == 0:
            status = "PASSED"
            print(f"✅ {test_name}: PASSED ({duration:.2f}s)")
        else:
            status = "FAILED"
            print(f"❌ {test_name}: FAILED ({duration:.2f}s)")
        
        results.append((test_name, status, duration, result.stdout))
        
    except subprocess.TimeoutExpired:
        status = "TIMEOUT"
        print(f"⏱️  {test_name}: TIMEOUT (>5 minutes)")
        results.append((test_name, status, 300, "Timeout"))
    except Exception as e:
        status = "ERROR"
        print(f"❌ {test_name}: ERROR - {e}")
        results.append((test_name, status, 0, str(e)))
    
    print()

total_end_time = time.perf_counter()
total_duration = total_end_time - total_start_time

# Summary
print("=" * 80)
print("📊 TEST SUITE SUMMARY")
print("=" * 80)
print()

passed = sum(1 for _, status, _, _ in results if status == "PASSED")
failed = sum(1 for _, status, _, _ in results if status == "FAILED")
skipped = sum(1 for _, status, _, _ in results if status == "SKIPPED")
timeout = sum(1 for _, status, _, _ in results if status == "TIMEOUT")
error = sum(1 for _, status, _, _ in results if status == "ERROR")
total = len(results)

print(f"Total Test Suites: {total}")
print(f"✅ Passed: {passed}")
print(f"❌ Failed: {failed}")
print(f"⏱️  Timeout: {timeout}")
print(f"⚠️  Skipped: {skipped}")
print(f"❌ Error: {error}")
print()
print(f"Total Duration: {total_duration:.2f}s")
print()

# Detailed results
print("Detailed Results:")
print("-" * 80)
for test_name, status, duration, output in results:
    status_icon = {
        "PASSED": "✅",
        "FAILED": "❌",
        "SKIPPED": "⚠️",
        "TIMEOUT": "⏱️",
        "ERROR": "❌"
    }.get(status, "❓")
    
    print(f"{status_icon} {test_name:30s} {status:10s} {duration:8.2f}s")

print()
print("=" * 80)
print(f"Test Run Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

# Exit code
if failed > 0 or error > 0:
    sys.exit(1)
else:
    sys.exit(0)

