"""
Smoke Test Script for Clinical Assistant
Quick validation that app can start and critical modules load without errors
"""

import sys
import importlib
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Test that critical modules can be imported"""
    print("🔍 Testing critical imports...")
    
    critical_modules = [
        "streamlit",
        "pandas",
        "numpy",
        "app",
        "scores.config",
        "scores.cardiology",
        "drugs.drug_database",
        "config.theme",
        "utils.page_helper",
    ]
    
    failed = []
    for module_name in critical_modules:
        try:
            importlib.import_module(module_name)
            print(f"  ✅ {module_name}")
        except Exception as e:
            print(f"  ❌ {module_name}: {e}")
            failed.append(module_name)
    
    return len(failed) == 0

def test_syntax():
    """Test that main Python files have valid syntax"""
    print("\n🔍 Testing syntax...")
    
    critical_files = [
        "app.py",
        "pages/01_📊_Scores.py",
        "pages/07_💊_Drug_Database.py",
        "scores/config.py",
        "scores/cardiology/__init__.py",
    ]
    
    failed = []
    for file_path in critical_files:
        path = Path(file_path)
        if not path.exists():
            print(f"  ⚠️  {file_path} - File not found")
            continue
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                code = f.read()
            compile(code, file_path, 'exec')
            print(f"  ✅ {file_path}")
        except SyntaxError as e:
            print(f"  ❌ {file_path}: {e}")
            failed.append(file_path)
        except Exception as e:
            print(f"  ⚠️  {file_path}: {e}")
    
    return len(failed) == 0

def test_config():
    """Test that config files are valid"""
    print("\n🔍 Testing config...")
    
    try:
        from scores.config import SCORES_BY_SPECIALTY
        score_count = sum(len(scores) for scores in SCORES_BY_SPECIALTY.values())
        print(f"  ✅ scores/config.py - {score_count} calculators registered")
        
        from scores.specialty_groups import SPECIALTY_GROUPS
        print(f"  ✅ scores/specialty_groups.py - {len(SPECIALTY_GROUPS)} groups")
        
        return True
    except Exception as e:
        print(f"  ❌ Config test failed: {e}")
        return False

def main():
    """Run all smoke tests"""
    print("=" * 60)
    print("🚀 Clinical Assistant - Smoke Test")
    print("=" * 60)
    
    results = []
    
    results.append(("Imports", test_imports()))
    results.append(("Syntax", test_syntax()))
    results.append(("Config", test_config()))
    
    print("\n" + "=" * 60)
    print("📊 Results Summary")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("✅ All smoke tests passed!")
        return 0
    else:
        print("❌ Some tests failed. Please review errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
