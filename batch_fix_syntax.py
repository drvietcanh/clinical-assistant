"""
Batch fix common syntax errors in drug_modules files
Focus on the most common errors: missing 'indications': key and missing 'drug': key in drug_interactions
"""
import os
import re
import subprocess
import sys
from pathlib import Path

def fix_missing_indications(content):
    """Fix missing 'indications': key"""
    lines = content.split('\n')
    fixed = False
    
    for i, line in enumerate(lines):
        # Look for pattern: 'administration': [...], followed by strings that look like indications
        if "'administration':" in line and i + 1 < len(lines):
            # Check next few lines for strings that look like indications
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                # Check if this looks like an indications list (starts with ' but no key before it)
                if (next_line.startswith("'") and 
                    not next_line.startswith("'indications':") and
                    not next_line.startswith("'contraindications':") and
                    any(keyword in next_line for keyword in ['Thiếu', 'Bệnh', 'Dự phòng', 'Sau phẫu thuật', 'Còi', 'Loãng'])):
                    # Check if 'indications': is missing in nearby lines
                    context = '\n'.join(lines[max(0, i-2):min(len(lines), j+5)])
                    if "'indications':" not in context:
                        # Find where the list ends (look for ], 'contraindications':)
                        for k in range(j, min(j+10, len(lines))):
                            if "], 'contraindications':" in lines[k]:
                                # Insert 'indications': before the first string
                                lines[j] = "        'indications': [" + lines[j].lstrip()
                                # Fix the closing bracket
                                lines[k] = lines[k].replace("], 'contraindications':", "], 'contraindications':")
                                fixed = True
                                break
                        if fixed:
                            break
            if fixed:
                break
    
    return '\n'.join(lines) if fixed else content

def fix_missing_drug_key(content):
    """Fix missing 'drug': key in drug_interactions"""
    # Pattern: }], 'mechanism': (should be in a list, need to add 'drug': key)
    # But this is complex, so we'll use a simpler approach
    lines = content.split('\n')
    fixed = False
    
    for i, line in enumerate(lines):
        # Look for pattern: }], followed by 'mechanism': on next line
        if line.strip().endswith('}],') and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line.startswith("'mechanism':"):
                # Check if this is inside drug_interactions
                context_before = '\n'.join(lines[max(0, i-20):i+1])
                if "'drug_interactions':" in context_before:
                    # Check if we're in 'major' or 'moderate' list
                    if "'major':" in context_before and "'moderate':" not in context_before[max(0, context_before.rfind("'major':")):]:
                        # This should be in 'moderate' list
                        lines[i] = line.rstrip(',') + "], 'moderate': [{'drug': 'Unknown',"
                        fixed = True
                    elif "'moderate':" in context_before:
                        # This should be another entry in 'moderate' list
                        lines[i+1] = "        {'drug': 'Unknown', " + next_line
                        fixed = True
    
    return '\n'.join(lines) if fixed else content

def fix_file(filepath):
    """Fix a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = fix_missing_indications(content)
        content = fix_missing_drug_key(content)
        
        if content != original:
            # Create backup
            backup_path = str(filepath) + '.batch_fix_backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original)
            
            # Write fixed content
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True
        return False
    except Exception as e:
        print(f"Error fixing {filepath}: {e}")
        return False

def main():
    """Main function"""
    drug_modules_dir = Path("drugs/drug_modules")
    fixed_files = []
    
    print("Batch fixing common syntax errors...")
    print("=" * 60)
    
    # Get list of files with errors from previous run
    error_files = [
        "drugs/drug_modules/anesthesia/local_anesthetics.py",
        "drugs/drug_modules/anesthesia/neuromuscular_blockers.py",
        "drugs/drug_modules/emergency/antiarrhythmics.py",
        "drugs/drug_modules/emergency/anticholinergics.py",
        "drugs/drug_modules/emergency/catecholamine_alpha__beta_agonists.py",
        "drugs/drug_modules/emergency/electrolytes.py",
        "drugs/drug_modules/emergency/local_anesthetic__antiarrhythmic_class_ibs.py",
        "drugs/drug_modules/emergency/opioid_antagonists.py",
        "drugs/drug_modules/endocrinology_other/corticosteroids/long_acting.py",
        "drugs/drug_modules/endocrinology_other/corticosteroids/short_intermediate_acting.py",
        "drugs/drug_modules/infectious_other/beta_lactams.py",
        "drugs/drug_modules/infectious_other/cephalosporins.py",
        "drugs/drug_modules/infectious_other/fluoroquinolones.py",
        "drugs/drug_modules/infectious_other/macrolides.py",
        "drugs/drug_modules/infectious_other/nitroimidazoles.py",
        "drugs/drug_modules/infectious_other/tetracyclines.py",
        "drugs/drug_modules/miscellaneous/analgesicantipyretic.py",
        "drugs/drug_modules/miscellaneous/analgesicantipyreticnsaid.py",
        "drugs/drug_modules/miscellaneous/beta_2_agonist_short_actings.py",
        "drugs/drug_modules/miscellaneous/corticosteroid_inhaleds.py",
        "drugs/drug_modules/miscellaneous/xanthine_oxidase_inhibitors.py",
        "drugs/drug_modules/oncology/alkylating_agents.py",
        "drugs/drug_modules/oncology/anthracyclines.py",
        "drugs/drug_modules/oncology/antimetabolites.py",
        "drugs/drug_modules/oncology/antimetabolite_antifolates.py",
        "drugs/drug_modules/oncology/anti_emetic_5_ht3_antagonists.py",
        "drugs/drug_modules/oncology/basic_oncology.py",
        "drugs/drug_modules/oncology/platinum_compounds.py",
        "drugs/drug_modules/oncology/taxanes.py",
        "drugs/drug_modules/respiratory/short_acting_beta_2_agonist_sabas.py",
        "drugs/drug_modules/supportive/antihistamine_h1_antagonist_2nd_generations.py",
    ]
    
    for filepath in error_files:
        if os.path.exists(filepath):
            if fix_file(filepath):
                fixed_files.append(filepath)
                print(f"✅ Fixed: {filepath}")
    
    print("\n" + "=" * 60)
    print(f"Fixed: {len(fixed_files)} files")
    print("\nNote: Backups created with .batch_fix_backup extension")
    print("\nPlease run find_and_fix_syntax_errors.py again to check remaining errors")

if __name__ == "__main__":
    main()
