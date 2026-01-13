#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Standardize Drug Field Order
Chuẩn hóa thứ tự field cho thuốc trong các file module
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
import astor  # Will try to import, fallback if not available

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

# Try to import astor for AST to code conversion
try:
    import astor
    HAS_ASTOR = True
except ImportError:
    HAS_ASTOR = False


def create_backup(file_path: Path) -> Path:
    """Tạo backup file"""
    backup_dir = file_path.parent / ".backups"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    shutil.copy2(file_path, backup_path)
    return backup_path


def format_python_dict_value(value: Any, indent: int = 0) -> str:
    """Format giá trị Python dict thành string"""
    indent_str = "    " * indent
    
    if value is None:
        return "None"
    elif isinstance(value, bool):
        return "True" if value else "False"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        # Check if multi-line
        if "\n" in value:
            escaped = value.replace('"""', '\\"\\"\\"')
            return f'"""{escaped}"""'
        else:
            escaped = value.replace("\\", "\\\\").replace('"', '\\"')
            return f'"{escaped}"'
    elif isinstance(value, list):
        if not value:
            return "[]"
        lines = ["["]
        for item in value:
            item_str = format_python_dict_value(item, indent + 1)
            lines.append(f"{indent_str}    {item_str},")
        lines.append(f"{indent_str}]")
        return "\n".join(lines)
    elif isinstance(value, dict):
        if not value:
            return "{}"
        lines = ["{"]
        for k, v in value.items():
            key_str = format_python_dict_value(k, indent + 1)
            if isinstance(v, dict):
                val_lines = format_python_dict_value(v, indent + 1).split("\n")
                lines.append(f"{indent_str}    {key_str}: {{")
                for vl in val_lines[1:-1]:  # Skip first { and last }
                    lines.append(f"{indent_str}    {vl}")
                lines.append(f"{indent_str}    }},")
            elif isinstance(v, list) and v and isinstance(v[0], dict):
                lines.append(f"{indent_str}    {key_str}: [")
                for item in v:
                    item_lines = format_python_dict_value(item, indent + 2).split("\n")
                    lines.append(f"{indent_str}        {{")
                    for il in item_lines[1:-1]:
                        lines.append(f"{indent_str}        {il}")
                    lines.append(f"{indent_str}        }},")
                lines.append(f"{indent_str}    ],")
            else:
                val_str = format_python_dict_value(v, indent + 1)
                lines.append(f"{indent_str}    {key_str}: {val_str},")
        lines.append(f"{indent_str}}}")
        return "\n".join(lines)
    else:
        return repr(value)


def format_drug_dict(drug_name: str, drug_data: Dict[str, Any], base_indent: int = 1) -> str:
    """Format một drug dictionary thành Python code"""
    indent = "    " * base_indent
    lines = [f'{indent}"{drug_name}": {{']
    
    for field, value in drug_data.items():
        value_str = format_python_dict_value(value, base_indent + 1)
        # Check if value_str is multi-line
        if "\n" in value_str:
            lines.append(f'{indent}    "{field}": {value_str},')
        else:
            lines.append(f'{indent}    "{field}": {value_str},')
    
    lines.append(f'{indent}}},')
    return "\n".join(lines)


def standardize_file_simple(file_path: Path, dry_run: bool = True) -> Dict[str, Any]:
    """
    Chuẩn hóa file đơn giản: tìm và thay thế drug definitions
    Approach: Đọc file, tìm drug definitions bằng regex, thay thế
    """
    result = {
        "file": str(file_path),
        "backup_created": False,
        "drugs_found": 0,
        "drugs_reordered": [],
        "errors": [],
        "warnings": [],
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
    except Exception as e:
        result["errors"].append(f"Lỗi đọc file: {e}")
        return result
    
    # First, ensure DRUG_DATABASE has reordered fields
    standardizer = FieldStandardizer()
    
    # Find all drugs in this file
    # Pattern: "DrugName": {
    drug_pattern = r'"([A-Z][^"]+)":\s*\{'
    matches = list(re.finditer(drug_pattern, content))
    
    if not matches:
        return result
    
    # For each drug found, check if it's in DRUG_DATABASE and needs reordering
    new_content = content
    offset = 0  # Track offset from replacements
    
    for match in reversed(matches):  # Process backwards to maintain positions
        drug_name = match.group(1)
        
        if drug_name not in DRUG_DATABASE:
            continue
        
        drug_data = DRUG_DATABASE[drug_name]
        if not isinstance(drug_data, dict):
            continue
        
        # Check if needs reordering
        current_keys = list(drug_data.keys())
        standard_keys = [k for k in ALL_FIELDS_WITH_COMMON if k in current_keys]
        
        # Check order
        is_ordered = True
        last_pos = -1
        for field in ALL_FIELDS_WITH_COMMON:
            if field in current_keys:
                current_pos = current_keys.index(field)
                if current_pos < last_pos:
                    is_ordered = False
                    break
                last_pos = current_pos
        
        if is_ordered:
            continue  # Already ordered
        
        # Get reordered data
        reordered_data = standardizer.standardize_field_order(drug_data)
        
        # Find the drug definition boundaries
        start_pos = match.start() + offset
        brace_count = 1
        end_pos = start_pos + len(match.group(0))
        
        # Find closing brace
        i = end_pos
        while i < len(new_content) and brace_count > 0:
            if new_content[i] == '{':
                brace_count += 1
            elif new_content[i] == '}':
                brace_count -= 1
            i += 1
        
        if brace_count == 0:
            # Found complete drug definition
            # Format new drug entry
            # Get indentation from original
            line_start = new_content.rfind('\n', 0, start_pos) + 1
            indent_match = re.match(r'(\s*)', new_content[line_start:start_pos])
            base_indent = len(indent_match.group(1)) if indent_match else 0
            indent_level = base_indent // 4
            
            new_drug_code = format_drug_dict(drug_name, OrderedDict(reordered_data), indent_level)
            
            # Replace
            if not dry_run:
                new_content = new_content[:start_pos] + new_drug_code + new_content[i:]
                offset += len(new_drug_code) - (i - start_pos)
            
            result["drugs_found"] += 1
            result["drugs_reordered"].append(drug_name)
        else:
            result["warnings"].append(f"Không tìm thấy closing brace cho {drug_name}")
    
    # Write back if not dry run
    if not dry_run and result["drugs_reordered"]:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            result["errors"].append(f"Lỗi ghi file: {e}")
    
    return result


def standardize_module(module_name: str, dry_run: bool = True) -> Dict[str, Any]:
    """Chuẩn hóa một module"""
    module_path = project_root / "drugs" / "drug_modules" / module_name
    
    if not module_path.exists():
        return {"error": f"Module {module_name} không tồn tại"}
    
    # First, ensure all drugs in DRUG_DATABASE are reordered
    print(f"  📋 Đang sắp xếp lại field trong DRUG_DATABASE cho module {module_name}...")
    standardizer = FieldStandardizer()
    reordered_count = 0
    
    # Find drugs in this module
    module_drugs = []
    for drug_name, drug_data in DRUG_DATABASE.items():
        if isinstance(drug_data, dict):
            # Check if drug is in this module by checking file
            # For now, reorder all
            reordered = standardizer.standardize_field_order(drug_data)
            drug_data.clear()
            drug_data.update(reordered)
            reordered_count += 1
    
    results = {
        "module": module_name,
        "files": [],
        "total_drugs": 0,
        "reordered_in_memory": reordered_count,
    }
    
    # Process all Python files in module
    for py_file in sorted(module_path.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        
        file_result = standardize_file_simple(py_file, dry_run=dry_run)
        results["files"].append(file_result)
        results["total_drugs"] += file_result["drugs_found"]
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Chuẩn hóa thứ tự field cho thuốc")
    parser.add_argument("--module", help="Chỉ chuẩn hóa module cụ thể (ví dụ: cardiovascular)")
    parser.add_argument("--file", help="Chỉ chuẩn hóa file cụ thể")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode (không sửa file)")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự sửa file (override --dry-run)")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không sửa file")
    else:
        print("EXECUTE MODE - Sẽ sửa file và tạo backup")
    print("=" * 80)
    print()
    
    if args.file:
        # Process single file
        file_path = project_root / args.file
        if not file_path.exists():
            print(f"❌ File không tồn tại: {file_path}")
            return
        
        result = standardize_file_simple(file_path, dry_run=dry_run)
        print(f"\n📄 File: {Path(result['file']).name}")
        print(f"  ✅ Tìm thấy: {result['drugs_found']} thuốc")
        print(f"  📋 Đã sắp xếp lại: {len(result['drugs_reordered'])} thuốc")
        if result['drugs_reordered']:
            for drug in result['drugs_reordered'][:10]:
                print(f"    - {drug}")
            if len(result['drugs_reordered']) > 10:
                print(f"    ... và {len(result['drugs_reordered']) - 10} thuốc khác")
        if result['errors']:
            print(f"  ❌ Lỗi: {', '.join(result['errors'])}")
        if result['warnings']:
            print(f"  ⚠️  Cảnh báo: {len(result['warnings'])}")
    
    elif args.module:
        # Process module
        print(f"📦 Chuẩn hóa module: {args.module}")
        result = standardize_module(args.module, dry_run=dry_run)
        if "error" in result:
            print(f"❌ {result['error']}")
            return
        
        print(f"\n✅ Kết quả:")
        print(f"  📋 Đã sắp xếp lại trong memory: {result['reordered_in_memory']} thuốc")
        print(f"  📄 Files đã xử lý: {len([f for f in result['files'] if f['drugs_found'] > 0])}")
        print(f"  💊 Tổng số thuốc trong module: {result['total_drugs']}")
        
        for file_result in result["files"]:
            if file_result["drugs_found"] > 0:
                print(f"\n  📄 {Path(file_result['file']).name}:")
                print(f"    - Tìm thấy: {file_result['drugs_found']} thuốc")
                print(f"    - Đã sắp xếp lại: {len(file_result['drugs_reordered'])} thuốc")
    
    else:
        print("📦 Chuẩn hóa tất cả modules...")
        print("⚠️  Lưu ý: Quá trình này có thể mất nhiều thời gian")
        print()
        
        module_path = project_root / "drugs" / "drug_modules"
        all_results = {}
        
        for module_dir in sorted(module_path.iterdir()):
            if not module_dir.is_dir() or module_dir.name.startswith("__"):
                continue
            
            print(f"\n📁 Module: {module_dir.name}")
            result = standardize_module(module_dir.name, dry_run=dry_run)
            all_results[module_dir.name] = result
            print(f"  ✅ {result['total_drugs']} thuốc")
        
        # Summary
        print("\n" + "=" * 80)
        print("TÓM TẮT")
        print("=" * 80)
        total_drugs = sum(r['total_drugs'] for r in all_results.values())
        total_files = sum(len([f for f in r['files'] if f['drugs_found'] > 0]) for r in all_results.values())
        print(f"Tổng số files đã xử lý: {total_files}")
        print(f"Tổng số thuốc đã sắp xếp lại: {total_drugs}")
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự sửa file.")


if __name__ == "__main__":
    main()
