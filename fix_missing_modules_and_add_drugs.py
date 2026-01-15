#!/usr/bin/env python3
"""
Script to fix missing modules and add remaining drugs (2022-2026)
- Updates mapping to use existing files where appropriate
- Creates new modules where needed
- Adds drugs to appropriate modules
"""

import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

BASE_DIR = Path("drugs/drug_modules")
CSV_FILE = "FDA2026.csv"

# Import functions from add_drugs_from_fda2026
import sys
sys.path.insert(0, str(Path.cwd()))
from add_drugs_from_fda2026 import format_drug_entry, read_module_file, find_insertion_point, add_drug_to_module

# Updated mapping for missing modules
MODULE_MAPPING = {
    "antimicrobial/antibiotics/other_antibiotics.py": "antimicrobial/antibiotics/others.py",
    "antimicrobial/antivirals/other_antivirals.py": "antimicrobial/antivirals/influenza.py",
    "gastrointestinal/antacids_ppi.py": "gastrointestinal/proton_pump_inhibitors.py",
    "gastrointestinal/ibd_drugs.py": "gastrointestinal/jak_inhibitors.py",
    "gastrointestinal/liver_disease.py": "gastrointestinal/other_gi_drugs.py",
    "obstetrics_gynecology/hormone_therapy.py": "obstetrics_gynecology/hormone_replacement.py",
    "psychiatry/antidepressants.py": "psychiatry/mood_stabilizers.py",
}

# Modules to create
MODULES_TO_CREATE = {
    "miscellaneous/other.py": {
        "description": "Miscellaneous Drugs - Other\nFDA Approved Drugs 2022-2026",
        "dict_name": "OTHER_MISCELLANEOUS_DRUGS"
    },
    "miscellaneous/rare_diseases.py": {
        "description": "Miscellaneous Drugs - Rare Diseases\nFDA Approved Drugs 2022-2026",
        "dict_name": "RARE_DISEASES_DRUGS"
    },
    "oncology/other_oncology.py": {
        "description": "Oncology Drugs - Other Oncology\nFDA Approved Drugs 2022-2026",
        "dict_name": "OTHER_ONCOLOGY_DRUGS"
    },
    "urology/kidney_disease.py": {
        "description": "Urology Drugs - Kidney Disease\nFDA Approved Drugs 2022-2026",
        "dict_name": "KIDNEY_DISEASE_DRUGS"
    }
}

def create_module_file(module_path: str, drugs: List[Dict], description: str, dict_name: str):
    """Create a new module file"""
    full_path = BASE_DIR / module_path
    
    # Create directory if needed
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Get years
    years = sorted(set(d["drug_info"]["year"] for d in drugs))
    years_str = ", ".join(years)
    
    # Format drug entries
    drug_entries = []
    for drug in drugs:
        formatted = format_drug_entry(drug)
        drug_entries.append(formatted)
    
    drug_entries_str = "".join(drug_entries).rstrip().rstrip(",")
    
    # Create content
    content = f'''"""
{description}
"""

from typing import Dict, Any


{dict_name}: Dict[str, Dict[str, Any]] = {{
{drug_entries_str}
}}

__all__ = ['{dict_name}']
'''
    
    # Write file
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ Đã tạo: {module_path} ({len(drugs)} thuốc)")
    return True

def update_mapping_in_script():
    """Update mapping in add_drugs_from_fda2026.py to use correct modules"""
    script_path = Path("add_drugs_from_fda2026.py")
    
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update mappings
    for old_module, new_module in MODULE_MAPPING.items():
        # Replace in map_category_to_module function
        pattern = rf'return\s+"{re.escape(old_module)}"'
        replacement = f'return "{new_module}"'
        content = re.sub(pattern, replacement, content)
    
    # Write back
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("✅ Đã cập nhật mapping trong add_drugs_from_fda2026.py")

def main():
    """Main function"""
    print("=" * 80)
    print("Xử lý các module còn thiếu và thêm thuốc")
    print("=" * 80)
    
    # Read JSON
    json_file = Path("drugs_2022_2026_to_add.json")
    if not json_file.exists():
        print(f"❌ Không tìm thấy {json_file}")
        return
    
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    new_drugs = data.get("new_drugs", [])
    print(f"\n📖 Tổng số thuốc: {len(new_drugs)}")
    
    # Group by module
    by_module = {}
    for drug in new_drugs:
        module = drug["module"]
        
        # Apply mapping if needed
        if module in MODULE_MAPPING:
            module = MODULE_MAPPING[module]
            drug["module"] = module  # Update in drug data
        
        if module not in by_module:
            by_module[module] = []
        by_module[module].append(drug)
    
    # Separate into existing and new modules
    existing_modules = {}
    new_modules = {}
    
    for module, drugs in by_module.items():
        full_path = BASE_DIR / module
        if full_path.exists():
            existing_modules[module] = drugs
        elif module in MODULES_TO_CREATE:
            new_modules[module] = drugs
        else:
            print(f"⚠️  Module không xác định: {module} ({len(drugs)} thuốc)")
    
    print(f"\n📊 Phân loại:")
    print(f"  - Module đã tồn tại: {len(existing_modules)}")
    print(f"  - Module cần tạo mới: {len(new_modules)}")
    
    # Create new modules
    if new_modules:
        print(f"\n📁 Đang tạo các module mới...")
        for module, drugs in new_modules.items():
            info = MODULES_TO_CREATE[module]
            create_module_file(
                module,
                drugs,
                info["description"],
                info["dict_name"]
            )
    
    # Add drugs to existing modules
    print(f"\n➕ Đang thêm thuốc vào các module đã tồn tại...")
    success_count = 0
    fail_count = 0
    
    for module, drugs in existing_modules.items():
        print(f"\n📁 Module: {module} ({len(drugs)} thuốc)")
        for drug in drugs:
            drug_name = drug["drug_info"]["drug_name"]
            print(f"  ➕ Đang thêm: {drug_name}...")
            if add_drug_to_module(module, drug):
                success_count += 1
            else:
                fail_count += 1
    
    # Add drugs to newly created modules (they're already in the file)
    print(f"\n✅ Các module mới đã chứa thuốc")
    
    print("\n" + "=" * 80)
    print(f"📊 Tổng kết:")
    print(f"  - Module đã tồn tại: {len(existing_modules)}")
    print(f"  - Module mới tạo: {len(new_modules)}")
    print(f"  - Thuốc thêm vào module có sẵn: {success_count}")
    print(f"  - Thuốc thất bại: {fail_count}")
    print(f"  - Thuốc trong module mới: {sum(len(d) for d in new_modules.values())}")
    print("=" * 80)
    
    # Update mapping in script
    print(f"\n🔧 Đang cập nhật mapping...")
    update_mapping_in_script()

if __name__ == "__main__":
    main()
