"""
Simple script to find drugs missing risk_flags and guideline_tags
by scanning Python files directly without importing DRUG_DATABASE
"""
import os
import re
from pathlib import Path

def find_drugs_missing_fields():
    """Find drugs missing risk_flags and guideline_tags by scanning files"""
    drug_modules_path = Path("drugs/drug_modules")
    missing_drugs = []
    
    # Pattern to find drug dictionary definitions
    # Look for patterns like "DrugName": { ... }
    drug_pattern = re.compile(r'["\']([^"\']+)["\']:\s*\{', re.MULTILINE)
    
    # Pattern to check if risk_flags exists
    risk_flags_pattern = re.compile(r'"risk_flags"|"risk_flags"', re.MULTILINE)
    
    # Pattern to check if guideline_tags exists
    guideline_tags_pattern = re.compile(r'"guideline_tags"|"guideline_tags"', re.MULTILINE)
    
    # Walk through all Python files in drug_modules
    for py_file in drug_modules_path.rglob("*.py"):
        # Skip __init__.py and backup files
        if "__init__" in py_file.name or "backup" in py_file.name.lower():
            continue
            
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find all drug names in the file
            drug_matches = drug_pattern.findall(content)
            
            # For each drug, check if it has risk_flags and guideline_tags
            for drug_name in drug_matches:
                # Skip if it's a field name (like 'group', 'vietnamese_name', etc.)
                if drug_name in ['group', 'vietnamese_name', 'administration', 'indications', 
                                'contraindications', 'dosage', 'renal_adjustment', 'side_effects',
                                'interactions', 'pregnancy', 'mechanism_of_action', 'monitoring',
                                'precautions', 'pharmacokinetics', 'storage', 'black_box_warnings',
                                'drug_interactions', 'contraindications', 'pregnancy_lactation',
                                'hepatic_adjustment', 'overdose_management', 'reversal_agents',
                                'administration_instructions', 'references', 'risk_flags', 
                                'guideline_tags', 'normal', '30_60', 'under_30', 'mild', 'moderate',
                                'severe', 'notes', 'tuyệt_đối', 'tương_đối', 'fda_category',
                                'pregnancy_details', 'lactation', 'safety', 'details', 
                                'recommendation', 'symptoms', 'antidote', 'treatment', 'monitoring',
                                'available', 'agents', 'oral', 'iv', 'local_anesthesia',
                                'reconstitution', 'infusion_rate', 'compatibility', 'incompatibility',
                                'max_dose', 'primary_sources', 'last_updated', 'evidence_level',
                                'major', 'moderate', 'minor', 'drug', 'mechanism', 'effect', 'management']:
                    continue
                
                # Find the drug's dictionary block
                # Look for the drug name followed by opening brace
                drug_start_pattern = re.compile(
                    rf'["\']{re.escape(drug_name)}["\']:\s*\{{',
                    re.MULTILINE
                )
                
                match = drug_start_pattern.search(content)
                if match:
                    # Find the matching closing brace for this drug's dictionary
                    start_pos = match.end() - 1  # Position of opening brace
                    brace_count = 0
                    end_pos = start_pos
                    
                    for i in range(start_pos, len(content)):
                        if content[i] == '{':
                            brace_count += 1
                        elif content[i] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                end_pos = i
                                break
                    
                    if brace_count == 0:
                        # Extract the drug's dictionary content
                        drug_dict_content = content[start_pos:end_pos+1]
                        
                        # Check if risk_flags and guideline_tags exist
                        has_risk_flags = bool(risk_flags_pattern.search(drug_dict_content))
                        has_guideline_tags = bool(guideline_tags_pattern.search(drug_dict_content))
                        
                        if not has_risk_flags or not has_guideline_tags:
                            missing_drugs.append({
                                'name': drug_name,
                                'file': str(py_file.relative_to(Path.cwd())),
                                'has_risk_flags': has_risk_flags,
                                'has_guideline_tags': has_guideline_tags
                            })
                            
        except Exception as e:
            print(f"Error processing {py_file}: {e}")
            continue
    
    return missing_drugs

if __name__ == "__main__":
    print("Scanning drug_modules for missing risk_flags and guideline_tags...")
    missing = find_drugs_missing_fields()
    
    print(f"\nFound {len(missing)} drugs missing fields:")
    print("="*80)
    
    missing_both = [d for d in missing if not d['has_risk_flags'] and not d['has_guideline_tags']]
    missing_risk_flags_only = [d for d in missing if not d['has_risk_flags'] and d['has_guideline_tags']]
    missing_guideline_tags_only = [d for d in missing if d['has_risk_flags'] and not d['has_guideline_tags']]
    
    print(f"\nMissing BOTH risk_flags and guideline_tags: {len(missing_both)}")
    for drug in missing_both:
        print(f"  - {drug['name']} ({drug['file']})")
    
    if missing_risk_flags_only:
        print(f"\nMissing ONLY risk_flags: {len(missing_risk_flags_only)}")
        for drug in missing_risk_flags_only:
            print(f"  - {drug['name']} ({drug['file']})")
    
    if missing_guideline_tags_only:
        print(f"\nMissing ONLY guideline_tags: {len(missing_guideline_tags_only)}")
        for drug in missing_guideline_tags_only:
            print(f"  - {drug['name']} ({drug['file']})")
    
    # Save to file
    with open("missing_risk_flags_report.txt", "w", encoding="utf-8") as f:
        f.write("DRUGS MISSING RISK_FLAGS AND/OR GUIDELINE_TAGS\n")
        f.write("="*80 + "\n\n")
        f.write(f"Total: {len(missing)} drugs\n\n")
        
        f.write("MISSING BOTH:\n")
        f.write("-"*80 + "\n")
        for drug in missing_both:
            f.write(f"{drug['name']} - {drug['file']}\n")
        
        if missing_risk_flags_only:
            f.write("\n\nMISSING ONLY RISK_FLAGS:\n")
            f.write("-"*80 + "\n")
            for drug in missing_risk_flags_only:
                f.write(f"{drug['name']} - {drug['file']}\n")
        
        if missing_guideline_tags_only:
            f.write("\n\nMISSING ONLY GUIDELINE_TAGS:\n")
            f.write("-"*80 + "\n")
            for drug in missing_guideline_tags_only:
                f.write(f"{drug['name']} - {drug['file']}\n")
    
    print(f"\nReport saved to: missing_risk_flags_report.txt")
