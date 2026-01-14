#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix All Remaining Patterns
Sửa tất cả các pattern lỗi còn lại một lần
"""

import re
from pathlib import Path
import shutil
from datetime import datetime


def fix_file(file_path: Path) -> int:
    """Sửa lỗi trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        fixes = 0
        
        # Tất cả các pattern cần sửa
        patterns = [
            # ],field' patterns
            (r"\],antidote'", r"],\n        'antidote'"),
            (r"\],treatment'", r"],\n        'treatment'"),
            (r"\],monitoring'", r"],\n        'monitoring'"),
            (r"\],notes'", r"],\n        'notes'"),
            (r"\],lethal_dose'", r"],\n        'lethal_dose'"),
            (r"\],pregnancy_details'", r"],\n        'pregnancy_details'"),
            (r"\],lactation'", r"],\n        'lactation'"),
            (r"\],recommendation'", r"],\n        'recommendation'"),
            (r"\],details'", r"],\n        'details'"),
            (r"\],safety'", r"],\n        'safety'"),
            (r"\],compatibility'", r"],\n        'compatibility'"),
            (r"\],incompatibility'", r"],\n        'incompatibility'"),
            (r"\],reconstitution'", r"],\n        'reconstitution'"),
            (r"\],infusion_rate'", r"],\n        'infusion_rate'"),
            (r"\],with_food'", r"],\n        'with_food'"),
            (r"\],timing'", r"],\n        'timing'"),
            (r"\],considerations'", r"],\n        'considerations'"),
            (r"\],dose_adjustment'", r"],\n        'dose_adjustment'"),
            (r"\],vietnam'", r"],\n        'vietnam'"),
            (r"\],common'", r"],\n        'common'"),
            (r"\],unit'", r"],\n        'unit'"),
            (r"\],range'", r"],\n        'range'"),
            (r"\],note'", r"],\n        'note'"),
            (r"\],primary_sources'", r"],\n        'primary_sources'"),
            (r"\],last_updated'", r"],\n        'last_updated'"),
            (r"\],evidence_level'", r"],\n        'evidence_level'"),
            (r"\],high_alert'", r"],\n        'high_alert'"),
            (r"\],narrow_therapeutic_index'", r"],\n        'narrow_therapeutic_index'"),
            (r"\],bleeding_risk'", r"],\n        'bleeding_risk'"),
            (r"\],organ_toxicity'", r"],\n        'organ_toxicity'"),
            (r"\],qt_prolongation'", r"],\n        'qt_prolongation'"),
            (r"\],hepatotoxicity'", r"],\n        'hepatotoxicity'"),
            (r"\],nephrotoxicity'", r"],\n        'nephrotoxicity'"),
            (r"\],requires_monitoring'", r"],\n        'requires_monitoring'"),
            (r"\],guideline_tags'", r"],\n        'guideline_tags'"),
            (r"\],image_url'", r"],\n        'image_url'"),
            (r"\],image_source'", r"],\n        'image_source'"),
            (r"\],evidence_levels'", r"],\n        'evidence_levels'"),
            (r"\],toxicity_management'", r"],\n        'toxicity_management'"),
            (r"\],symptoms'", r"],\n        'symptoms'"),
            (r"\],name'", r"],\n        'name'"),
            (r"\],dose'", r"],\n        'dose'"),
            (r"\],available'", r"],\n        'available'"),
            (r"\],agents'", r"],\n        'agents'"),
            (r"\],oral'", r"],\n        'oral'"),
            (r"\],iv'", r"],\n        'iv'"),
            (r"\],neonates'", r"],\n        'neonates'"),
            (r"\],infants'", r"],\n        'infants'"),
            (r"\],children'", r"],\n        'children'"),
            (r"\],adolescents'", r"],\n        'adolescents'"),
            (r"\],geriatric_dosing'", r"],\n        'geriatric_dosing'"),
            (r"\],brand_names'", r"],\n        'brand_names'"),
            (r"\],cost_estimate'", r"],\n        'cost_estimate'"),
            (r"\],references'", r"],\n        'references'"),
            (r"\],risk_flags'", r"],\n        'risk_flags'"),
            (r"\],administration_instructions'", r"],\n        'administration_instructions'"),
            (r"\],pediatric_dosing'", r"],\n        'pediatric_dosing'"),
            
            # },field' patterns
            (r"\},antidote'", r"},\n        'antidote'"),
            (r"\},treatment'", r"},\n        'treatment'"),
            (r"\},monitoring'", r"},\n        'monitoring'"),
            (r"\},notes'", r"},\n        'notes'"),
            (r"\},lethal_dose'", r"},\n        'lethal_dose'"),
            (r"\},toxicity_management'", r"},\n        'toxicity_management'"),
            (r"\},reversal_agents'", r"},\n        'reversal_agents'"),
            (r"\},administration_instructions'", r"},\n        'administration_instructions'"),
            (r"\},pediatric_dosing'", r"},\n        'pediatric_dosing'"),
            (r"\},geriatric_dosing'", r"},\n        'geriatric_dosing'"),
            (r"\},brand_names'", r"},\n        'brand_names'"),
            (r"\},cost_estimate'", r"},\n        'cost_estimate'"),
            (r"\},references'", r"},\n        'references'"),
            (r"\},risk_flags'", r"},\n        'risk_flags'"),
            (r"\},evidence_levels'", r"},\n        'evidence_levels'"),
        ]
        
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                fixes += 1
                content = new_content
        
        if content != original_content:
            # Backup
            backup_dir = file_path.parent / ".backups"
            backup_dir.mkdir(exist_ok=True)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = backup_dir / f"{file_path.stem}_all_patterns_fix_{timestamp}{file_path.suffix}"
            shutil.copy2(file_path, backup_path)
            
            # Write
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return fixes
        
        return 0
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 0


def main():
    """Main function"""
    print("="*70)
    print("SỬA TẤT CẢ CÁC PATTERN LỖI CÒN LẠI")
    print("="*70)
    
    modules_dir = Path(__file__).parent / "drug_modules"
    
    # Bỏ qua biguanides.py
    skip_files = {'biguanides.py'}
    
    total_fixes = 0
    files_fixed = []
    
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__") or "backup" in str(py_file).lower():
            continue
        
        if py_file.name in skip_files:
            print(f"⏭️  Bỏ qua {py_file.name}")
            continue
        
        fixes = fix_file(py_file)
        if fixes > 0:
            print(f"✅ {py_file.name}: Sửa {fixes} lỗi")
            files_fixed.append(str(py_file))
            total_fixes += fixes
    
    print("\n" + "="*70)
    print("TỔNG KẾT")
    print("="*70)
    print(f"Đã sửa {total_fixes} lỗi trong {len(files_fixed)} file")
    print("="*70)


if __name__ == "__main__":
    main()
