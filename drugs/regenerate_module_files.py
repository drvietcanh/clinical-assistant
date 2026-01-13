#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenerate Module Files from Reordered DRUG_DATABASE
Tạo lại file module từ DRUG_DATABASE đã được sắp xếp lại field
Approach an toàn hơn: đọc DRUG_DATABASE và tạo lại file thay vì sửa file hiện có
"""

import sys
from pathlib import Path
from typing import Dict, List, Any, Set
from collections import OrderedDict
import json
from datetime import datetime
import re
import shutil
import ast
import astor

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


def create_backup(file_path: Path) -> Path:
    """Tạo backup file"""
    backup_dir = file_path.parent / ".backups"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    shutil.copy2(file_path, backup_path)
    return backup_path


def find_drugs_in_file(file_path: Path) -> Set[str]:
    """Tìm tất cả drug names trong file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return set()
    
    # Find all drug definitions: "DrugName": {
    pattern = r'"([A-Z][^"]+)":\s*\{'
    matches = re.findall(pattern, content)
    return set(matches)


def get_module_variable_name(file_path: Path) -> str:
    """Lấy tên biến module từ file (ví dụ: ACE_INHIBITORS từ ace_inhibitors.py)"""
    # Try to parse AST to find module-level dict assignment
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        if isinstance(node.value, ast.Dict):
                            return target.id
    except:
        pass
    
    # Fallback: guess from filename
    name = file_path.stem.upper().replace('-', '_')
    # Convert camelCase or snake_case to UPPER_SNAKE_CASE
    name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    return name.upper()


def format_drug_dict_ast(drug_name: str, drug_data: Dict[str, Any]) -> ast.Dict:
    """Tạo AST node cho drug dictionary"""
    keys = []
    values = []
    
    for field, value in drug_data.items():
        keys.append(ast.Constant(value=field))
        values.append(value_to_ast(value))
    
    return ast.Dict(keys=keys, values=values)


def value_to_ast(value: Any) -> ast.AST:
    """Convert Python value to AST node"""
    if value is None:
        return ast.Constant(value=None)
    elif isinstance(value, bool):
        return ast.Constant(value=value)
    elif isinstance(value, (int, float, str)):
        return ast.Constant(value=value)
    elif isinstance(value, list):
        elts = [value_to_ast(item) for item in value]
        return ast.List(elts=elts)
    elif isinstance(value, dict):
        keys = [ast.Constant(value=k) for k in value.keys()]
        values = [value_to_ast(v) for v in value.values()]
        return ast.Dict(keys=keys, values=values)
    else:
        return ast.Constant(value=repr(value))


def regenerate_module_file(file_path: Path, dry_run: bool = True) -> Dict[str, Any]:
    """Tạo lại file module từ DRUG_DATABASE"""
    result = {
        "file": str(file_path),
        "backup_created": False,
        "drugs_found": 0,
        "drugs_included": [],
        "errors": [],
    }
    
    if not file_path.exists():
        result["errors"].append("File không tồn tại")
        return result
    
    # Find drugs in this file
    drugs_in_file = find_drugs_in_file(file_path)
    if not drugs_in_file:
        return result
    
    # Get drugs from DRUG_DATABASE
    module_drugs = OrderedDict()
    for drug_name in sorted(drugs_in_file):
        if drug_name in DRUG_DATABASE:
            module_drugs[drug_name] = DRUG_DATABASE[drug_name]
            result["drugs_found"] += 1
            result["drugs_included"].append(drug_name)
    
    if not module_drugs:
        return result
    
    # Create backup
    if not dry_run:
        backup_path = create_backup(file_path)
        result["backup_created"] = True
        result["backup_file"] = str(backup_path)
    
    # Read original file to preserve header comments and docstring
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        result["errors"].append(f"Lỗi đọc file: {e}")
        return result
    
    # Extract header (everything before first dict assignment)
    header_lines = []
    in_header = True
    for line in original_content.splitlines():
        if re.match(r'^\s*[A-Z_][A-Z0-9_]*\s*=\s*\{', line):
            in_header = False
        if in_header:
            header_lines.append(line)
    
    header = "\n".join(header_lines)
    if header_lines:
        header += "\n\n"
    
    # Get module variable name
    var_name = get_module_variable_name(file_path)
    
    # Generate new content
    if not dry_run:
        # Build AST for module dict
        dict_keys = [ast.Constant(value=name) for name in module_drugs.keys()]
        dict_values = [format_drug_dict_ast(name, data) for name, data in module_drugs.items()]
        module_dict = ast.Dict(keys=dict_keys, values=dict_values)
        
        # Create assignment: VAR_NAME = {...}
        assign = ast.Assign(
            targets=[ast.Name(id=var_name, ctx=ast.Store())],
            value=module_dict
        )
        
        # Create module AST
        module_ast = ast.Module(body=[assign], type_ignores=[])
        
        # Convert to code
        try:
            new_code = astor.to_source(module_ast)
            # Format with header
            new_content = header + new_code
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        except Exception as e:
            result["errors"].append(f"Lỗi tạo lại file: {e}")
    
    return result


def regenerate_module(module_name: str, dry_run: bool = True) -> Dict[str, Any]:
    """Tạo lại tất cả files trong module"""
    module_path = project_root / "drugs" / "drug_modules" / module_name
    
    if not module_path.exists():
        return {"error": f"Module {module_name} không tồn tại"}
    
    results = {
        "module": module_name,
        "files": [],
        "total_drugs": 0,
    }
    
    # Process all Python files
    for py_file in sorted(module_path.rglob("*.py")):
        if py_file.name == "__init__.py":
            continue
        
        file_result = regenerate_module_file(py_file, dry_run=dry_run)
        results["files"].append(file_result)
        results["total_drugs"] += file_result["drugs_found"]
    
    return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Tạo lại file module từ DRUG_DATABASE đã reorder")
    parser.add_argument("--module", help="Chỉ tạo lại module cụ thể")
    parser.add_argument("--file", help="Chỉ tạo lại file cụ thể")
    parser.add_argument("--dry-run", action="store_true", default=True,
                       help="Dry run mode")
    parser.add_argument("--execute", action="store_true",
                       help="Thực sự tạo lại file")
    
    args = parser.parse_args()
    dry_run = not args.execute
    
    print("=" * 80)
    if dry_run:
        print("DRY RUN MODE - Không tạo lại file")
    else:
        print("EXECUTE MODE - Sẽ tạo lại file và tạo backup")
    print("=" * 80)
    print()
    
    if args.file:
        file_path = project_root / args.file
        if not file_path.exists():
            print(f"❌ File không tồn tại: {file_path}")
            return
        
        result = regenerate_module_file(file_path, dry_run=dry_run)
        print(f"\n📄 File: {Path(result['file']).name}")
        print(f"  ✅ Tìm thấy: {result['drugs_found']} thuốc")
        if result['drugs_included']:
            print(f"  📋 Thuốc sẽ được bao gồm:")
            for drug in result['drugs_included'][:10]:
                print(f"    - {drug}")
            if len(result['drugs_included']) > 10:
                print(f"    ... và {len(result['drugs_included']) - 10} thuốc khác")
        if result['errors']:
            print(f"  ❌ Lỗi: {', '.join(result['errors'])}")
    
    elif args.module:
        print(f"📦 Tạo lại module: {args.module}")
        result = regenerate_module(args.module, dry_run=dry_run)
        if "error" in result:
            print(f"❌ {result['error']}")
            return
        
        print(f"\n✅ Kết quả:")
        print(f"  📄 Files: {len([f for f in result['files'] if f['drugs_found'] > 0])}")
        print(f"  💊 Tổng số thuốc: {result['total_drugs']}")
        
        for file_result in result["files"]:
            if file_result["drugs_found"] > 0:
                print(f"\n  📄 {Path(file_result['file']).name}:")
                print(f"    - {file_result['drugs_found']} thuốc")
    
    else:
        print("📦 Tạo lại tất cả modules...")
        module_path = project_root / "drugs" / "drug_modules"
        for module_dir in sorted(module_path.iterdir()):
            if not module_dir.is_dir() or module_dir.name.startswith("__"):
                continue
            
            result = regenerate_module(module_dir.name, dry_run=dry_run)
            if result["total_drugs"] > 0:
                print(f"  📁 {module_dir.name}: {result['total_drugs']} thuốc")
    
    if dry_run:
        print("\n⚠️  Đây là DRY RUN. Sử dụng --execute để thực sự tạo lại file.")


if __name__ == "__main__":
    main()
