"""
Script to check which drugs are missing risk_flags and guideline_tags
"""
import ast
import os
from pathlib import Path

def check_drug_file(file_path):
    """Check if a drug file has risk_flags and guideline_tags"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for risk_flags
        has_risk_flags = '"risk_flags"' in content or "'risk_flags'" in content
        
        # Check for guideline_tags
        has_guideline_tags = '"guideline_tags"' in content or "'guideline_tags'" in content
        
        # Try to parse and get drug name
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Dict):
                    for key, value in zip(node.keys, node.values):
                        if isinstance(key, ast.Constant) and isinstance(key.value, str):
                            if key.value and len(key.value) < 100:  # Likely a drug name
                                drug_name = key.value
                                if isinstance(value, ast.Dict):
                                    # Check if this dict has risk_flags or guideline_tags
                                    dict_keys = [k.value if isinstance(k, ast.Constant) else None 
                                                for k in value.keys]
                                    if 'risk_flags' in dict_keys:
                                        has_risk_flags = True
                                    if 'guideline_tags' in dict_keys:
                                        has_guideline_tags = True
                                break
        except:
            pass
        
        return has_risk_flags, has_guideline_tags
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False, False

def find_drug_files():
    """Find all drug files in the drugs directory"""
    drug_files = []
    drugs_dir = Path("drugs")
    
    # Check drug_modules directory
    drug_modules_dir = drugs_dir / "drug_modules"
    if drug_modules_dir.exists():
        for file_path in drug_modules_dir.rglob("*.py"):
            if file_path.name != "__init__.py" and not file_path.name.endswith(".backup"):
                drug_files.append(file_path)
    
    return drug_files

def main():
    """Main function to check missing risk_flags and guideline_tags"""
    drug_files = find_drug_files()
    
    missing_both = []
    missing_risk_flags = []
    missing_guideline_tags = []
    has_both = []
    
    print(f"Checking {len(drug_files)} drug files...")
    
    for file_path in drug_files:
        has_rf, has_gt = check_drug_file(file_path)
        
        if not has_rf and not has_gt:
            missing_both.append(str(file_path))
        elif not has_rf:
            missing_risk_flags.append(str(file_path))
        elif not has_gt:
            missing_guideline_tags.append(str(file_path))
        else:
            has_both.append(str(file_path))
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total files checked: {len(drug_files)}")
    print(f"Has both risk_flags and guideline_tags: {len(has_both)}")
    print(f"Missing both: {len(missing_both)}")
    print(f"Missing only risk_flags: {len(missing_risk_flags)}")
    print(f"Missing only guideline_tags: {len(missing_guideline_tags)}")
    
    print("\n" + "="*80)
    print("MISSING BOTH")
    print("="*80)
    for f in missing_both[:50]:  # Show first 50
        print(f"  - {f}")
    if len(missing_both) > 50:
        print(f"  ... and {len(missing_both) - 50} more")
    
    print("\n" + "="*80)
    print("MISSING ONLY RISK_FLAGS")
    print("="*80)
    for f in missing_risk_flags:
        print(f"  - {f}")
    
    print("\n" + "="*80)
    print("MISSING ONLY GUIDELINE_TAGS")
    print("="*80)
    for f in missing_guideline_tags:
        print(f"  - {f}")
    
    # Save to file
    with open("missing_risk_flags_report.txt", "w", encoding="utf-8") as f:
        f.write("MISSING BOTH\n")
        f.write("="*80 + "\n")
        for file_path in missing_both:
            f.write(f"{file_path}\n")
        
        f.write("\n\nMISSING ONLY RISK_FLAGS\n")
        f.write("="*80 + "\n")
        for file_path in missing_risk_flags:
            f.write(f"{file_path}\n")
        
        f.write("\n\nMISSING ONLY GUIDELINE_TAGS\n")
        f.write("="*80 + "\n")
        for file_path in missing_guideline_tags:
            f.write(f"{file_path}\n")
    
    print(f"\nReport saved to: missing_risk_flags_report.txt")

if __name__ == "__main__":
    main()

