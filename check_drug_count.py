"""
Script to check total drug count in the reorganized database
Reads directly from drug_database.py to avoid streamlit dependency
"""
import ast
import re
from pathlib import Path

def count_drugs_in_dict_code(code):
    """Count drug entries in Python dictionary code"""
    # Count dictionary entries: "Drug Name": {
    pattern = r'"[^"]+":\s*\{'
    matches = re.findall(pattern, code)
    return len(matches)

def analyze_drug_database():
    """Analyze drug database by reading drug_database.py"""
    db_file = Path("drugs/drug_database.py")
    
    if not db_file.exists():
        print("ERROR: drugs/drug_database.py not found")
        return
    
    with open(db_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find DRUG_DATABASE = { ... }
    # Extract the dictionary content
    match = re.search(r'DRUG_DATABASE\s*=\s*\{', content)
    if not match:
        print("ERROR: Could not find DRUG_DATABASE definition")
        return
    
    # Count all drug entries in the merged dictionary
    # Look for all "key": { patterns after DRUG_DATABASE = {
    start_pos = match.end()
    dict_content = content[start_pos:]
    
    # Count entries
    pattern = r'^\s*"[^"]+":\s*\{'
    entries = re.findall(pattern, dict_content, re.MULTILINE)
    
    # Also try to find TOTAL_DRUGS
    total_match = re.search(r'TOTAL_DRUGS\s*=\s*len\(DRUG_DATABASE\)', content)
    if total_match:
        # Try to evaluate it
        try:
            # Extract just the dictionary merging part
            exec_globals = {}
            exec_locals = {}
            # Import the modules directly
            import sys
            sys.path.insert(0, str(Path.cwd()))
            
            # Try to import without going through drugs.__init__
            import importlib.util
            
            def safe_import(module_path, var_name):
                spec = importlib.util.spec_from_file_location("temp_module", module_path)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    # Set parent package to avoid relative import issues
                    module.__package__ = "drugs.drug_modules"
                    try:
                        spec.loader.exec_module(module)
                        return getattr(module, var_name, None)
                    except:
                        return None
                return None
            
            # Count from individual module files
            modules_info = []
            base = Path("drugs/drug_modules")
            
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
            print("KIEM TRA SO LUONG THUOC SAU KHI TO CHUC LAI")
            print("=" * 70)
            print()
            
            total_count = 0
            print(f"{'Module':<30} {'So luong':<12}")
            print("-" * 70)
            
            for name, file_path in sorted(module_files.items(), key=lambda x: x[0]):
                if file_path.exists():
                    # Read file and count dictionary entries
                    with open(file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    
                    # Count "key": { patterns
                    pattern = r'"[^"]+":\s*\{'
                    count = len(re.findall(pattern, file_content))
                    
                    # Also check subdirectories if it's a package
                    if file_path.parent.is_dir() and file_path.name == "__init__.py":
                        for subfile in file_path.parent.rglob("*.py"):
                            if subfile.name != "__init__.py" and not subfile.name.endswith(".backup"):
                                with open(subfile, 'r', encoding='utf-8') as sf:
                                    subcontent = sf.read()
                                subcount = len(re.findall(pattern, subcontent))
                                count += subcount
                    
                    total_count += count
                    print(f"{name:<30} {count:<12}")
            
            print("-" * 70)
            print(f"{'TONG (tu cac module)':<30} {total_count:<12}")
            print()
            
            # Also check DRUG_DATABASE file directly
            db_pattern = r'"[^"]+":\s*\{'
            db_count = len(re.findall(db_pattern, content))
            print(f"{'TONG (tu DRUG_DATABASE.py)':<30} {db_count:<12}")
            print()
            print("=" * 70)
            print(f"KET QUA: Tong so thuoc = {total_count}")
            print("=" * 70)
            print()
            print("Luu y: So luong tren la uoc tinh tu cac file module.")
            print("       De co so chinh xac, can chay trong moi truong co streamlit.")
            
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    analyze_drug_database()
