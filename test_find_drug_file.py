"""
Test tìm file chứa thuốc
"""
import re
from pathlib import Path

def find_drug_file(drug_name: str) -> Path:
    """Tìm file chứa một thuốc"""
    base_path = Path("drugs/drug_modules")
    
    found_files = []
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tìm drug bằng regex
            pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
            if re.search(pattern, content):
                found_files.append((py_file, "Found pattern"))
                
                # Kiểm tra xem có phải là drug thực sự
                if ('"group"' in content or "'group'" in content or 
                    '"vietnamese_name"' in content or "'vietnamese_name'" in content):
                    found_files.append((py_file, "Has drug fields"))
                    return py_file, found_files
        except Exception as e:
            found_files.append((py_file, f"Error: {e}"))
    
    return None, found_files

# Test với một vài thuốc
test_drugs = [
    "Losartan/Hydrochlorothiazide",
    "Entecavir",
    "Cephalexin",
    "Amlodipine"
]

print("=" * 70)
print("TEST TIM FILE CHUA THUOC")
print("=" * 70)
print()

for drug in test_drugs:
    print(f"\nTim thuoc: {drug}")
    result, all_found = find_drug_file(drug)
    if result:
        print(f"  [OK] Tim thay trong: {result}")
    else:
        print(f"  [LOI] Khong tim thay file")
        if all_found:
            print(f"  Cac file co chua pattern (nhung khong phai thuoc):")
            for f, reason in all_found[:3]:
                print(f"    - {f.name}: {reason}")

