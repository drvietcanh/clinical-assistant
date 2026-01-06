"""
Script to find drugs missing risk_flags and guideline_tags
Safe version that skips files with syntax errors
"""

import os
import ast
from pathlib import Path
from typing import List, Dict, Tuple

def check_file_syntax(file_path: Path) -> bool:
    """Check if a Python file has valid syntax"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        return True
    except SyntaxError:
        return False
    except Exception:
        return False

def find_drugs_in_file(file_path: Path) -> List[Tuple[str, Dict]]:
    """
    Find drugs in a Python file and check for risk_flags and guideline_tags
    Returns list of (drug_name, drug_data_dict) tuples
    """
    drugs = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse as AST
        try:
            tree = ast.parse(content)
        except SyntaxError:
            # Skip files with syntax errors
            print(f"⚠️  Skipping {file_path.name} due to syntax error")
            return []
        
        # Look for dictionary definitions
        # This is a simple approach - look for patterns like "drug_name": { ... }
        # We'll use a regex-like approach to find drug entries
        
        # Simple pattern matching for drug entries
        # Look for patterns like '"DrugName": {' or "'DrugName': {"
        import re
        
        # Find all dictionary entries that look like drug definitions
        # Pattern: "DrugName": { ... } or 'DrugName': { ... }
        pattern = r'["\']([^"\']+)["\']\s*:\s*\{'
        matches = re.finditer(pattern, content)
        
        for match in matches:
            drug_name = match.group(1)
            # Try to extract the dictionary content
            # This is simplified - we'll check if risk_flags/guideline_tags exist in the content
            start_pos = match.end()
            
            # Find the matching closing brace
            brace_count = 1
            end_pos = start_pos
            while end_pos < len(content) and brace_count > 0:
                if content[end_pos] == '{':
                    brace_count += 1
                elif content[end_pos] == '}':
                    brace_count -= 1
                end_pos += 1
            
            if brace_count == 0:
                drug_content = content[start_pos:end_pos-1]
                
                # Check for risk_flags and guideline_tags
                has_risk_flags = 'risk_flags' in drug_content
                has_guideline_tags = 'guideline_tags' in drug_content
                
                drugs.append((
                    drug_name,
                    {
                        'has_risk_flags': has_risk_flags,
                        'has_guideline_tags': has_guideline_tags,
                        'file': str(file_path)
                    }
                ))
    
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
    
    return drugs

def scan_drug_modules() -> Dict[str, List[Tuple[str, Dict]]]:
    """Scan all drug module files"""
    drug_modules_dir = Path('drugs/drug_modules')
    
    if not drug_modules_dir.exists():
        print(f"Error: {drug_modules_dir} does not exist")
        return {}
    
    all_drugs = {}
    files_processed = 0
    files_skipped = 0
    
    # Walk through all Python files
    for py_file in drug_modules_dir.rglob('*.py'):
        # Skip __init__.py
        if py_file.name == '__init__.py':
            continue
        
        # Check syntax first
        if not check_file_syntax(py_file):
            print(f"⚠️  Skipping {py_file.relative_to(drug_modules_dir)} due to syntax error")
            files_skipped += 1
            continue
        
        drugs = find_drugs_in_file(py_file)
        if drugs:
            all_drugs[str(py_file.relative_to(drug_modules_dir))] = drugs
            files_processed += 1
    
    print(f"\n✅ Processed {files_processed} files")
    print(f"⚠️  Skipped {files_skipped} files (syntax errors)")
    
    return all_drugs

def main():
    """Main function"""
    print("Scanning drug modules for missing risk_flags and guideline_tags...")
    print("=" * 80)
    
    all_drugs = scan_drug_modules()
    
    # Collect all drugs
    missing_both = []
    missing_risk_flags = []
    missing_guideline_tags = []
    has_both = []
    
    for file_path, drugs in all_drugs.items():
        for drug_name, drug_info in drugs:
            if not drug_info['has_risk_flags'] and not drug_info['has_guideline_tags']:
                missing_both.append((drug_name, drug_info['file']))
            elif not drug_info['has_risk_flags']:
                missing_risk_flags.append((drug_name, drug_info['file']))
            elif not drug_info['has_guideline_tags']:
                missing_guideline_tags.append((drug_name, drug_info['file']))
            else:
                has_both.append((drug_name, drug_info['file']))
    
    total = len(missing_both) + len(missing_risk_flags) + len(missing_guideline_tags) + len(has_both)
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total drugs found: {total}")
    print(f"Has both risk_flags and guideline_tags: {len(has_both)} ({len(has_both)/total*100:.1f}%)" if total > 0 else "0")
    print(f"Missing both: {len(missing_both)} ({len(missing_both)/total*100:.1f}%)" if total > 0 else "0")
    print(f"Missing only risk_flags: {len(missing_risk_flags)} ({len(missing_risk_flags)/total*100:.1f}%)" if total > 0 else "0")
    print(f"Missing only guideline_tags: {len(missing_guideline_tags)} ({len(missing_guideline_tags)/total*100:.1f}%)" if total > 0 else "0")
    
    print("\n" + "=" * 80)
    print("MISSING BOTH (First 20)")
    print("=" * 80)
    for drug_name, file_path in missing_both[:20]:
        print(f"  - {drug_name} ({file_path})")
    if len(missing_both) > 20:
        print(f"  ... and {len(missing_both) - 20} more")
    
    if missing_risk_flags:
        print("\n" + "=" * 80)
        print("MISSING ONLY RISK_FLAGS (First 10)")
        print("=" * 80)
        for drug_name, file_path in missing_risk_flags[:10]:
            print(f"  - {drug_name} ({file_path})")
        if len(missing_risk_flags) > 10:
            print(f"  ... and {len(missing_risk_flags) - 10} more")
    
    if missing_guideline_tags:
        print("\n" + "=" * 80)
        print("MISSING ONLY GUIDELINE_TAGS (First 10)")
        print("=" * 80)
        for drug_name, file_path in missing_guideline_tags[:10]:
            print(f"  - {drug_name} ({file_path})")
        if len(missing_guideline_tags) > 10:
            print(f"  ... and {len(missing_guideline_tags) - 10} more")
    
    # Save to file
    with open("missing_risk_flags_safe_report.txt", "w", encoding="utf-8") as f:
        f.write("MISSING BOTH\n")
        f.write("=" * 80 + "\n")
        for drug_name, file_path in missing_both:
            f.write(f"{drug_name} ({file_path})\n")
        
        if missing_risk_flags:
            f.write("\n\nMISSING ONLY RISK_FLAGS\n")
            f.write("=" * 80 + "\n")
            for drug_name, file_path in missing_risk_flags:
                f.write(f"{drug_name} ({file_path})\n")
        
        if missing_guideline_tags:
            f.write("\n\nMISSING ONLY GUIDELINE_TAGS\n")
            f.write("=" * 80 + "\n")
            for drug_name, file_path in missing_guideline_tags:
                f.write(f"{drug_name} ({file_path})\n")
    
    print(f"\n✅ Report saved to: missing_risk_flags_safe_report.txt")
    print(f"\n📋 Remaining drugs to complete: {len(missing_both) + len(missing_risk_flags) + len(missing_guideline_tags)}")
    
    return {
        'missing_both': missing_both,
        'missing_risk_flags': missing_risk_flags,
        'missing_guideline_tags': missing_guideline_tags
    }

if __name__ == "__main__":
    main()
