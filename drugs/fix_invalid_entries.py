#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Invalid Entries
Loại bỏ các entries không hợp lệ trong DRUG_DATABASE (các entry là tên field, không phải tên thuốc)
"""

import sys
from pathlib import Path
from typing import List, Set
import shutil
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
    )
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
    )


def get_invalid_entries() -> List[str]:
    """Lấy danh sách entries không hợp lệ"""
    all_field_names = (
        STANDARD_14_FIELDS + 
        ADDITIONAL_8_FIELDS + 
        ADDITIONAL_COMMON_FIELDS +
        ["administration_instructions", "contraindications_detail", "renal_adjustment"]
    )
    
    invalid = []
    for key in DRUG_DATABASE.keys():
        if key.lower() in [f.lower() for f in all_field_names]:
            invalid.append(key)
        elif not isinstance(DRUG_DATABASE[key], dict):
            invalid.append(key)
    
    return invalid


def fix_drug_database_file(dry_run: bool = True) -> dict:
    """Sửa file drug_database.py để loại bỏ entries không hợp lệ"""
    db_file = project_root / "drugs" / "drug_database.py"
    
    if not db_file.exists():
        return {"error": "File không tồn tại"}
    
    # Create backup
    if not dry_run:
        backup_path = db_file.with_suffix(db_file.suffix + f".backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        shutil.copy2(db_file, backup_path)
        print(f"✅ Đã tạo backup: {backup_path}")
    
    # Read file
    with open(db_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find _NON_DRUG_KEYS list
    invalid_entries = get_invalid_entries()
    
    # Check if entries are already in _NON_DRUG_KEYS
    lines = content.splitlines()
    non_drug_keys_start = None
    non_drug_keys_end = None
    
    for i, line in enumerate(lines):
        if '_NON_DRUG_KEYS = [' in line:
            non_drug_keys_start = i
        elif non_drug_keys_start is not None and ']' in line and i > non_drug_keys_start:
            non_drug_keys_end = i
            break
    
    if non_drug_keys_start is None:
        return {"error": "Không tìm thấy _NON_DRUG_KEYS"}
    
    # Add missing entries to _NON_DRUG_KEYS
    if not dry_run:
        # Read current _NON_DRUG_KEYS
        current_keys = []
        for i in range(non_drug_keys_start + 1, non_drug_keys_end):
            line = lines[i].strip()
            if line.startswith('"') or line.startswith("'"):
                key = line.strip('",\'')
                current_keys.append(key)
        
        # Add new keys
        new_keys = [k for k in invalid_entries if k not in current_keys]
        
        if new_keys:
            # Rebuild _NON_DRUG_KEYS section
            new_section = ['_NON_DRUG_KEYS = [']
            all_keys = sorted(set(current_keys + invalid_entries))
            for key in all_keys:
                new_section.append(f'    "{key}",')
            new_section.append(']')
            
            # Replace section
            new_lines = (
                lines[:non_drug_keys_start] +
                new_section +
                lines[non_drug_keys_end + 1:]
            )
            
            # Write back
            with open(db_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(new_lines))
            
            return {
                "success": True,
                "added_keys": new_keys,
                "total_keys": len(all_keys)
            }
    
    return {
        "success": True,
        "dry_run": True,
        "invalid_entries": invalid_entries
    }


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Loại bỏ entries không hợp lệ")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự sửa file")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa file")
    else:
        print("EXECUTE MODE - Sẽ sửa file và tạo backup")
    print("=" * 80)
    print()
    
    # Get invalid entries
    invalid_entries = get_invalid_entries()
    print(f"📋 Tìm thấy {len(invalid_entries)} entries không hợp lệ:")
    for entry in invalid_entries:
        print(f"  - {entry}")
    print()
    
    # Fix file
    result = fix_drug_database_file(dry_run=dry_run)
    
    if "error" in result:
        print(f"❌ Lỗi: {result['error']}")
        return
    
    if dry_run:
        print("✅ Dry run hoàn thành")
        print("⚠️  Sử dụng --execute để thực sự sửa file")
    else:
        if result.get("success"):
            print("✅ Đã cập nhật file drug_database.py")
            if "added_keys" in result:
                print(f"   Đã thêm {len(result['added_keys'])} keys vào _NON_DRUG_KEYS")
                for key in result["added_keys"]:
                    print(f"     - {key}")
    
    # Verify
    print("\n📊 Kiểm tra lại DRUG_DATABASE...")
    try:
        # Reload to verify
        import importlib
        import drugs.drug_database as db_module
        importlib.reload(db_module)
        from drugs.drug_database import DRUG_DATABASE
        
        remaining_invalid = get_invalid_entries()
        if remaining_invalid:
            print(f"⚠️  Vẫn còn {len(remaining_invalid)} entries không hợp lệ:")
            for entry in remaining_invalid:
                print(f"  - {entry}")
        else:
            print("✅ Không còn entries không hợp lệ!")
            print(f"✅ Tổng số thuốc hợp lệ: {len(DRUG_DATABASE)}")
    except Exception as e:
        print(f"⚠️  Không thể reload module: {e}")
        print("   Cần restart Python để kiểm tra")


if __name__ == "__main__":
    main()
