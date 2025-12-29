"""
Accurate drug count by importing modules directly
Bypasses drugs.__init__ to avoid streamlit dependency
"""
import sys
import importlib.util
from pathlib import Path

def import_module_direct(file_path, module_name):
    """Import module directly from file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        return None
    
    module = importlib.util.module_from_spec(spec)
    # Set package to allow relative imports
    if file_path.parent.name == "drug_modules":
        module.__package__ = "drugs.drug_modules"
    elif "drug_modules" in str(file_path.parent):
        module.__package__ = f"drugs.drug_modules.{file_path.parent.name}"
    
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None

def count_drugs():
    """Count drugs from all modules"""
    base = Path("drugs/drug_modules")
    
    # Import main modules
    modules = {}
    
    # Try importing cardiovascular
    cv_file = base / "cardiovascular" / "__init__.py"
    if cv_file.exists():
        try:
            cv_mod = import_module_direct(cv_file, "cardiovascular")
            if cv_mod and hasattr(cv_mod, 'CARDIOVASCULAR_DRUGS'):
                modules['Cardiovascular'] = cv_mod.CARDIOVASCULAR_DRUGS
        except Exception as e:
            print(f"Error importing cardiovascular: {e}")
    
    # Try importing other modules similarly
    module_files = {
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
    
    # Simple approach: read the final merged DRUG_DATABASE
    # by executing drug_database.py in a controlled way
    print("Dang doc tu drug_database.py...")
    
    db_file = Path("drugs/drug_database.py")
    if db_file.exists():
        # Read and extract the merge section
        with open(db_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all module imports and try to get their dicts
        import re
        
        # Extract module names from imports
        import_pattern = r'from \.drug_modules import \((.*?)\)'
        match = re.search(import_pattern, content, re.DOTALL)
        
        if match:
            imports = match.group(1)
            # Extract variable names
            var_pattern = r'(\w+_DRUGS)'
            var_names = re.findall(var_pattern, imports)
            
            print(f"\nTim thay {len(var_names)} modules trong drug_database.py")
            print("Cac modules:", ", ".join(var_names[:10]), "...")
    
    # Alternative: Count unique drug names from all module files
    print("\n" + "=" * 70)
    print("KIEM TRA SO LUONG THUOC - PHUONG PHAP DEM TRUC TIEP")
    print("=" * 70)
    print()
    print("Dang dem thuoc tu cac file module...")
    print("(Phuong phap nay dem so dong co dinh nghia thuoc: 'Ten thuoc': {)")
    print()
    
    all_drug_names = set()
    module_counts = {}
    
    # Read each module file and extract drug names
    for name, file_path in module_files.items():
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Count lines that look like drug definitions: "Drug Name": {
                count = 0
                drug_names_in_file = []
                
                for line in lines:
                    # Pattern: "Drug Name": { or 'Drug Name': {
                    if re.match(r'^\s*["\']([^"\']+)["\']\s*:\s*\{', line):
                        drug_name = re.search(r'["\']([^"\']+)["\']', line).group(1)
                        drug_names_in_file.append(drug_name)
                        all_drug_names.add(drug_name)
                        count += 1
                
                # Also check subdirectories
                if file_path.parent.is_dir() and file_path.name in ["__init__.py", "endocrinology.py"]:
                    for subfile in file_path.parent.rglob("*.py"):
                        if subfile.name not in ["__init__.py"] and not subfile.name.endswith(".backup"):
                            try:
                                with open(subfile, 'r', encoding='utf-8') as sf:
                                    sublines = sf.readlines()
                                for line in sublines:
                                    if re.match(r'^\s*["\']([^"\']+)["\']\s*:\s*\{', line):
                                        drug_name = re.search(r'["\']([^"\']+)["\']', line).group(1)
                                        drug_names_in_file.append(drug_name)
                                        all_drug_names.add(drug_name)
                                        count += 1
                            except:
                                pass
                
                module_counts[name] = count
                
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                module_counts[name] = 0
    
    # Print results
    print(f"{'Module':<30} {'So luong':<12}")
    print("-" * 70)
    
    total = 0
    for name in sorted(module_counts.keys(), key=lambda x: module_counts[x], reverse=True):
        count = module_counts[name]
        total += count
        print(f"{name:<30} {count:<12}")
    
    print("-" * 70)
    print(f"{'TONG (tong so dong dinh nghia)':<30} {total:<12}")
    print(f"{'TONG (thuoc duy nhat)':<30} {len(all_drug_names):<12}")
    print()
    print("=" * 70)
    print(f"KET QUA CUOI CUNG:")
    print(f"  - Tong so dong dinh nghia thuoc: {total}")
    print(f"  - So thuoc duy nhat (khong trung): {len(all_drug_names)}")
    print("=" * 70)
    
    if total != len(all_drug_names):
        print(f"\nLuu y: Co {total - len(all_drug_names)} dinh nghia trung lap")
        print("       (Mot thuoc co the xuat hien trong nhieu module)")

if __name__ == "__main__":
    count_drugs()

