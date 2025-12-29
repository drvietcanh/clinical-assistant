"""
Final drug count report - counts from module files directly
Avoids import issues by reading files
"""
import re
from pathlib import Path
from collections import defaultdict

def count_drug_entries_in_file(file_path):
    """Count top-level drug dictionary entries in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count lines that match: "Drug Name": { at the start (top-level entries)
        # Pattern: start of line, optional whitespace, quote, drug name, quote, colon, whitespace, {
        pattern = r'^\s*["\']([^"\']+)["\']\s*:\s*\{'
        matches = re.findall(pattern, content, re.MULTILINE)
        return len(matches), matches
    except Exception as e:
        return 0, []

# Analyze all modules
base = Path("drugs/drug_modules")
module_counts = {}
all_drug_names = set()
duplicates = defaultdict(list)

module_files = {
    "Cardiovascular": base / "cardiovascular" / "__init__.py",
    "Diabetes": base / "diabetes" / "__init__.py",
    "Gastrointestinal": base / "gastrointestinal" / "__init__.py",
    "Analgesics": base / "analgesics" / "__init__.py",
    "Respiratory": base / "respiratory" / "__init__.py",
    "Neurological": base / "neurological" / "__init__.py",
    "Hematology": base / "hematology.py",
    "Supportive": base / "supportive" / "__init__.py",
    "Antimicrobial": base / "antimicrobial" / "__init__.py",
    "Metabolic": base / "metabolic" / "__init__.py",
    "Endocrinology": base / "endocrinology.py",
    "Oncology": base / "oncology" / "__init__.py",
    "Emergency": base / "emergency" / "__init__.py",
    "Urology": base / "urology.py",
    "Dermatology": base / "dermatology.py",
    "Ophthalmology": base / "ophthalmology.py",
    "Obstetrics/Gynecology": base / "obstetrics_gynecology.py",
    "ENT/Oral/Nasal": base / "ent_oral_nasal_combinations.py",
    "Miscellaneous": base / "miscellaneous" / "__init__.py",
}

print("=" * 70)
print("BAO CAO SO LUONG THUOC - DEM TU CAC FILE MODULE")
print("=" * 70)
print()
print("Dang dem thuoc tu cac file module...")
print("(Dem so dong co dinh nghia thuoc o cap top-level)")
print()

total_count = 0

for module_name, file_path in sorted(module_files.items(), key=lambda x: x[0]):
    count = 0
    drug_names = []
    
    if file_path.exists():
        # Count in main file
        file_count, file_names = count_drug_entries_in_file(file_path)
        count += file_count
        drug_names.extend(file_names)
        
        # Also check subdirectories
        if file_path.parent.is_dir() and file_path.name in ["__init__.py", "endocrinology.py"]:
            for subfile in file_path.parent.rglob("*.py"):
                if subfile.name not in ["__init__.py"] and not subfile.name.endswith(".backup"):
                    subcount, subnames = count_drug_entries_in_file(subfile)
                    count += subcount
                    drug_names.extend(subnames)
    
    module_counts[module_name] = count
    total_count += count
    
    # Track duplicates
    for drug_name in drug_names:
        if drug_name in all_drug_names:
            duplicates[drug_name].append(module_name)
        else:
            all_drug_names.add(drug_name)
            duplicates[drug_name] = [module_name]

# Print results
print(f"{'Module':<30} {'So luong':<12}")
print("-" * 70)

for name in sorted(module_counts.keys(), key=lambda x: module_counts[x], reverse=True):
    count = module_counts[name]
    print(f"{name:<30} {count:<12}")

print("-" * 70)
print(f"{'TONG (tong so dinh nghia)':<30} {total_count:<12}")
print(f"{'TONG (thuoc duy nhat)':<30} {len(all_drug_names):<12}")
print()

# Check duplicates
dup_count = sum(1 for v in duplicates.values() if len(v) > 1)
if dup_count > 0:
    print(f"Luu y: Co {dup_count} thuoc xuat hien trong nhieu module:")
    for drug_name, modules in list(duplicates.items())[:10]:
        if len(modules) > 1:
            print(f"  - {drug_name}: {', '.join(modules)}")
    if dup_count > 10:
        print(f"  ... va {dup_count - 10} thuoc trung lap khac")

print()
print("=" * 70)
print("KET LUAN:")
print(f"  - Tong so dinh nghia thuoc trong cac module: {total_count}")
print(f"  - So thuoc duy nhat (khong trung): {len(all_drug_names)}")
print()
print("Luu y:")
print("  - So luong tren la uoc tinh tu cac file module")
print("  - De co so chinh xac 100%, can chay trong moi truong co streamlit")
print("  - Co the co mot so thuoc xuat hien trong nhieu module (duplicates)")
print("  - DRUG_DATABASE se merge tat ca va loai bo trung lap")
print("=" * 70)

