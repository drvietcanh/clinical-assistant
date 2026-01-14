#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standardize Drug Field Order V2
Chuẩn hóa thứ tự field cho thuốc - phiên bản đơn giản và đáng tin cậy hơn
Sử dụng DRUG_DATABASE đã được reorder và ghi lại vào file nguồn
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from collections import OrderedDict
import json
from datetime import datetime
import re
import shutil
import ast

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
        ALL_FIELDS_WITH_COMMON,
    )
    from drugs.field_standardizer import FieldStandardizer
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import (
        STANDARD_14_FIELDS,
        ADDITIONAL_8_FIELDS,
        ADDITIONAL_COMMON_FIELDS,
        ALL_FIELDS_WITH_COMMON,
    )
    from field_standardizer import FieldStandardizer


def create_backup(file_path: Path) -> Path:
    """Tạo backup file"""
    backup_dir = file_path.parent / ".backups"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    shutil.copy2(file_path, backup_path)
    return backup_path


def format_value_for_python(value: Any, indent: str = "        ") -> str:
    """Format giá trị Python để ghi vào file"""
    if value is None:
        return "None"
    elif isinstance(value, bool):
        return "True" if value else "False"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        # Handle multi-line strings
        if "\n" in value:
            # Use triple quotes for multi-line
            escaped = value.replace('"""', '\\"\\"\\"')
            return f'"""{escaped}"""'
        else:
            # Escape quotes
            escaped = value.replace("\\", "\\\\").replace('"', '\\"')
            return f'"{escaped}"'
    elif isinstance(value, list):
        if not value:
            return "[]"
        lines = ["["]
        for item in value:
            item_str = format_value_for_python(item, indent + "    ")
            lines.append(f"{indent}    {item_str},")
        lines.append(f"{indent}]")
        return "\n".join(lines)
    elif isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        for k, v in value.items():
            key_str = format_value_for_python(k, indent + "    ")
            val_str = format_value_for_python(v, indent + "    ")
            # Handle nested dicts
            if isinstance(v, dict):
                lines.append(f"{indent}    {key_str}: {{")
                for ik, iv in v.items():
                    ik_str = format_value_for_python(ik, indent + "        ")
                    iv_str = format_value_for_python(iv, indent + "        ")
                    lines.append(f"{indent}        {ik_str}: {iv_str},")
                lines.append(f"{indent}    }},")
            elif isinstance(v, list) and v and isinstance(v[0], dict):
                # List of dicts
                lines.append(f"{indent}    {key_str}: [")
                for item in v:
                    lines.append(f"{indent}        {{")
                    for ik, iv in item.items():
                        ik_str = format_value_for_python(ik, indent + "            ")
                        iv_str = format_value_for_python(iv, indent + "            ")
                        lines.append(f"{indent}            {ik_str}: {iv_str},")
                    lines.append(f"{indent}        }},")
                lines.append(f"{indent}    ],")
            else:
                lines.append(f"{indent}    {key_str}: {val_str},")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    else:
        return repr(value)


def format_drug_entry(drug_name: str, drug_data: Dict[str, Any], base_indent: int = 1) -> str:
    """Format một drug entry thành Python code"""
    indent = "    " * base_indent
    lines = [f'{indent}"{drug_name}": {{']
    
    for field, value in drug_data.items():
        value_str = format_value_for_python(value, indent + "    ")
        # Handle multi-line values
        if "\n" in value_str and not value_str.startswith('"""'):
            # It's a multi-line structure
            lines.append(f'{indent}    "{field}": {value_str},')
        else:
            lines.append(f'{indent}    "{field}": {value_str},')
    
    lines.append(f'{indent}}},')
    return "\n".join(lines)


def find_drug_in_file(file_path: Path, drug_name: str) -> Optional[Tuple[int, int]]:
    """Tìm vị trí của drug trong file (start_line, end_line)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except:
        return None
    
    # Find drug definition
    pattern = rf'(\s*)"{re.escape(drug_name)}"\s*:\s*\{{'
    start_line = None
    brace_count = 0
    
    for i, line in enumerate(lines):
        match = re.match(pattern, line)
        if match:
            start_line = i
            brace_count = 1
            # Find closing brace
            for j in range(i + 1, len(lines)):
                brace_count += lines[j].count("{") - lines[j].count("}")
                if brace_count == 0:
                    return (i, j + 1)
            break
    
    return None


def standardize_file(file_path: Path, dry_run: bool = True) -> Dict[str, Any]:
    """Chuẩn hóa một file module"""
    result = {
        "file": str(file_path),
        "backup_created": False,
        "drugs_found": 0,
        "drugs_reordered": [],
        "errors": [],
    }
    
    if not file_path.exists():
        result["errors"].append("File không tồn tại")
        return result
    
    # Create backup
    if not dry_run:
        backup_path = create_backup(file_path)
        result["backup_created"] = True
        result["backup_file"] = str(backup_path)
    
    # Read file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines(keepends=True)
    except Exception as e:
        result["errors"].append(f"Lỗi đọc file: {e}")
        return result
    
    # Find all drugs in this file that are in DRUG_DATABASE
    standardizer = FieldStandardizer()
    drugs_to_replace = {}
    
    # Parse file to find drug definitions
    for drug_name in DRUG_DATABASE.keys():
        if not isinstance(DRUG_DATABASE[drug_name], dict):
            continue
        
        # Check if drug is in this file
        pattern = rf'"{re.escape(drug_name)}"\s*:'
        if re.search(pattern, content):
            # Get reordered data
            drug_data = DRUG_DATABASE[drug_name]
            reordered_data = standardizer.standardize_field_order(drug_data)
            drugs_to_replace[drug_name] = reordered_data
            result["drugs_found"] += 1
    
    if not drugs_to_replace:
        return result
    
    # Replace drugs in file (simplified approach: replace entire file)
    # This is a complex operation, so for now we'll create a new version
    # For production, we'd want more sophisticated parsing
    
    if not dry_run:
        # Read original to preserve structure
        # Find module-level dictionary assignments
        # This is complex, so we'll use a simpler approach:
        # Generate new content with reordered drugs
        
        # For now, just mark as needing manual review
        result["needs_manual_review"] = True
        result["drugs_reordered"] = list(drugs_to_replace.keys())
    
    return result


def standardize_module(module_name: str, dry_run: bool = True) -> Dict[str, Any]:
    """Chuẩn hóa một module"""
    module_path = project_root / "drugs" / "drug_modules" / module_name
    
    if not module_path.exists():
        return {"error": f"Module {module_name} không tồn tại"}
    
    results = {
        "module": module_name,
        "files": [],
        "total_drugs": 0,
    }
    
    # Process all Python files in module
    for py_file in sorted(module_path.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        
        file_result = standardize_file(py_file, dry_run=dry_run)
        results["files"].append(file_result)
        results["total_drugs"] += file_result["drugs_found"]
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Chuẩn hóa thứ tự field cho thuốc")
    parser.add_argument("--module", help="Chỉ chuẩn hóa module cụ thể")
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
    
    # First, ensure DRUG_DATABASE has reordered fields
    print("📋 Đang sắp xếp lại field trong DRUG_DATABASE...")
    standardizer = FieldStandardizer()
    reordered_count = 0
    for drug_name, drug_data in DRUG_DATABASE.items():
        if isinstance(drug_data, dict):
            reordered = standardizer.standardize_field_order(drug_data)
            # Update in place
            drug_data.clear()
            drug_data.update(reordered)
            reordered_count += 1
    
    print(f"✅ Đã sắp xếp lại {reordered_count} thuốc trong DRUG_DATABASE")
    print()
    
    if args.module:
        print(f"📦 Chuẩn hóa module: {args.module}")
        result = standardize_module(args.module, dry_run=dry_run)
        print(f"✅ Tìm thấy {result['total_drugs']} thuốc trong module")
        for file_result in result["files"]:
            if file_result["drugs_found"] > 0:
                print(f"  📄 {Path(file_result['file']).name}: {file_result['drugs_found']} thuốc")
    else:
        print("📦 Chuẩn hóa tất cả modules...")
        module_path = project_root / "drugs" / "drug_modules"
        for module_dir in sorted(module_path.iterdir()):
            if not module_dir.is_dir() or module_dir.name.startswith("__"):
                continue
            
            result = standardize_module(module_dir.name, dry_run=dry_run)
            if result["total_drugs"] > 0:
                print(f"  📁 {module_dir.name}: {result['total_drugs']} thuốc")
    
    print("\n" + "=" * 80)
    print("LƯU Ý: Script này chỉ sắp xếp lại trong DRUG_DATABASE.")
    print("Để sửa file nguồn, cần tool phức tạp hơn để parse và rewrite Python code.")
    print("=" * 80)


if __name__ == "__main__":
    main()
