"""
Script to find drugs missing risk_flags and guideline_tags
Import each module individually to avoid syntax errors in other files
"""

import sys
import os
from pathlib import Path
from typing import List, Dict, Tuple

# Add drugs directory to path
sys.path.insert(0, str(Path(__file__).parent))

def import_module_safely(module_path: str):
    """Import a module safely, catching syntax errors"""
    try:
        # Import the module
        module = __import__(module_path, fromlist=[''])
        return module
    except SyntaxError as e:
        print(f"⚠️  Syntax error in {module_path}: {e}")
        return None
    except Exception as e:
        print(f"⚠️  Error importing {module_path}: {e}")
        return None

def get_drug_dicts_from_module(module):
    """Extract all drug dictionaries from a module"""
    drug_dicts = []
    
    # Look for variables that are dictionaries and contain drug data
    for attr_name in dir(module):
        if attr_name.startswith('_'):
            continue
        
        attr = getattr(module, attr_name)
        
        # Check if it's a dictionary
        if isinstance(attr, dict):
            # Check if it looks like a drug dictionary (has drug entries)
            # A drug entry typically has keys like "group", "vietnamese_name", etc.
            sample_key = next(iter(attr.keys())) if attr else None
            if sample_key and isinstance(attr[sample_key], dict):
                # Check if the nested dict has drug-like structure
                sample_drug = attr[sample_key]
                if 'group' in sample_drug or 'vietnamese_name' in sample_drug or 'indications' in sample_drug:
                    drug_dicts.append((attr_name, attr))
    
    return drug_dicts

def check_drugs_in_dict(drug_dict: Dict, source: str) -> List[Tuple[str, Dict]]:
    """Check drugs in a dictionary for missing risk_flags and guideline_tags"""
    missing = []
    
    for drug_name, drug_data in drug_dict.items():
        if not isinstance(drug_data, dict):
            continue
        
        has_risk_flags = 'risk_flags' in drug_data and drug_data.get('risk_flags') is not None
        has_guideline_tags = 'guideline_tags' in drug_data and drug_data.get('guideline_tags') is not None
        
        if not has_risk_flags or not has_guideline_tags:
            missing.append((
                drug_name,
                {
                    'has_risk_flags': has_risk_flags,
                    'has_guideline_tags': has_guideline_tags,
                    'source': source
                }
            ))
    
    return missing

def scan_all_modules():
    """Scan all drug modules"""
    drug_modules_dir = Path('drugs/drug_modules')
    
    all_missing = []
    modules_processed = 0
    modules_skipped = 0
    
    # Get all Python files in drug_modules
    for py_file in drug_modules_dir.rglob('*.py'):
        if py_file.name == '__init__.py':
            continue
        
        # Convert file path to module path
        # e.g., drugs/drug_modules/cardiovascular/ace_inhibitors.py
        # -> drugs.drug_modules.cardiovascular.ace_inhibitors
        relative_path = py_file.relative_to(Path('drugs'))
        module_path = str(relative_path).replace(os.sep, '.').replace('.py', '')
        
        # Try to import the module
        module = import_module_safely(module_path)
        if module is None:
            modules_skipped += 1
            continue
        
        # Get drug dictionaries from the module
        drug_dicts = get_drug_dicts_from_module(module)
        
        if drug_dicts:
            for dict_name, drug_dict in drug_dicts:
                missing = check_drugs_in_dict(drug_dict, f"{module_path}.{dict_name}")
                all_missing.extend(missing)
            modules_processed += 1
    
    print(f"\n✅ Processed {modules_processed} modules")
    print(f"⚠️  Skipped {modules_skipped} modules (syntax errors or import errors)")
    
    return all_missing

def main():
    """Main function"""
    print("Finding drugs missing risk_flags and guideline_tags...")
    print("=" * 80)
    
    all_missing = scan_all_modules()
    
    # Categorize
    missing_both = []
    missing_risk_flags = []
    missing_guideline_tags = []
    
    for drug_name, info in all_missing:
        if not info['has_risk_flags'] and not info['has_guideline_tags']:
            missing_both.append((drug_name, info['source']))
        elif not info['has_risk_flags']:
            missing_risk_flags.append((drug_name, info['source']))
        elif not info['has_guideline_tags']:
            missing_guideline_tags.append((drug_name, info['source']))
    
    total_missing = len(missing_both) + len(missing_risk_flags) + len(missing_guideline_tags)
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total drugs missing fields: {total_missing}")
    print(f"Missing both risk_flags and guideline_tags: {len(missing_both)}")
    print(f"Missing only risk_flags: {len(missing_risk_flags)}")
    print(f"Missing only guideline_tags: {len(missing_guideline_tags)}")
    
    print("\n" + "=" * 80)
    print("MISSING BOTH (First 30)")
    print("=" * 80)
    for drug_name, source in missing_both[:30]:
        print(f"  - {drug_name} ({source})")
    if len(missing_both) > 30:
        print(f"  ... and {len(missing_both) - 30} more")
    
    if missing_risk_flags:
        print("\n" + "=" * 80)
        print("MISSING ONLY RISK_FLAGS (First 10)")
        print("=" * 80)
        for drug_name, source in missing_risk_flags[:10]:
            print(f"  - {drug_name} ({source})")
        if len(missing_risk_flags) > 10:
            print(f"  ... and {len(missing_risk_flags) - 10} more")
    
    if missing_guideline_tags:
        print("\n" + "=" * 80)
        print("MISSING ONLY GUIDELINE_TAGS (First 10)")
        print("=" * 80)
        for drug_name, source in missing_guideline_tags[:10]:
            print(f"  - {drug_name} ({source})")
        if len(missing_guideline_tags) > 10:
            print(f"  ... and {len(missing_guideline_tags) - 10} more")
    
    # Save to file
    with open("missing_risk_flags_import_report.txt", "w", encoding="utf-8") as f:
        f.write("MISSING BOTH\n")
        f.write("=" * 80 + "\n")
        for drug_name, source in missing_both:
            f.write(f"{drug_name} ({source})\n")
        
        if missing_risk_flags:
            f.write("\n\nMISSING ONLY RISK_FLAGS\n")
            f.write("=" * 80 + "\n")
            for drug_name, source in missing_risk_flags:
                f.write(f"{drug_name} ({source})\n")
        
        if missing_guideline_tags:
            f.write("\n\nMISSING ONLY GUIDELINE_TAGS\n")
            f.write("=" * 80 + "\n")
            for drug_name, source in missing_guideline_tags:
                f.write(f"{drug_name} ({source})\n")
    
    print(f"\n✅ Report saved to: missing_risk_flags_import_report.txt")
    print(f"\n📋 Focus on missing_both: {len(missing_both)} drugs")
    
    return {
        'missing_both': missing_both,
        'missing_risk_flags': missing_risk_flags,
        'missing_guideline_tags': missing_guideline_tags
    }

if __name__ == "__main__":
    main()
