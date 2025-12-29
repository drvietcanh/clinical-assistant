"""
Drug Manager - Công cụ quản lý và sửa chữa thuốc
Giúp thêm, sửa, xóa thuốc dễ dàng
"""

from typing import Dict, List, Optional
from pathlib import Path
import json
from .drug_index import (
    find_drug_location,
    get_module_info,
    search_drugs,
    suggest_module_for_drug,
    DRUG_MODULES,
    MODULE_METADATA,
)

def find_drug_file(drug_name: str) -> Optional[Path]:
    """
    Tìm file chứa thuốc để sửa chữa
    
    Returns:
        Path to file, or None if not found
    """
    locations = find_drug_location(drug_name)
    if not locations:
        return None
    
    # Return first location
    module_name, file_path = locations[0]
    
    # If it's a directory, need to search in subdirectories
    if file_path.endswith("/"):
        base_path = Path(file_path)
        # Search in all Python files
        for py_file in base_path.rglob("*.py"):
            if py_file.name != "__init__.py" and not py_file.name.endswith(".backup"):
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                            return py_file
                except:
                    continue
        return base_path / "__init__.py"
    
    return Path(file_path)

def get_drug_template() -> Dict:
    """Lấy template cho thuốc mới"""
    return {
        "group": "",
        "vietnamese_name": "",
        "administration": [],
        "indications": [],
        "contraindications": [],
        "dosage": {},
        "renal_adjustment": {},
        "side_effects": [],
        "interactions": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {},
        "storage": "",
        "black_box_warnings": "",
    }

def validate_drug_data(drug_data: Dict) -> List[str]:
    """
    Kiểm tra tính hợp lệ của dữ liệu thuốc
    
    Returns:
        List of error messages (empty if valid)
    """
    errors = []
    required_fields = ["group", "indications", "dosage"]
    
    for field in required_fields:
        if field not in drug_data or not drug_data[field]:
            errors.append(f"Thiếu trường bắt buộc: {field}")
    
    if "administration" in drug_data and not isinstance(drug_data["administration"], list):
        errors.append("'administration' phải là list")
    
    if "indications" in drug_data and not isinstance(drug_data["indications"], list):
        errors.append("'indications' phải là list")
    
    return errors

def suggest_drug_placement(drug_name: str, drug_data: Dict) -> Dict:
    """
    Gợi ý nơi đặt thuốc mới
    
    Returns:
        Dict with suggested module and file path
    """
    suggested_module = suggest_module_for_drug(drug_name, drug_data)
    module_info = get_module_info(suggested_module)
    
    return {
        "module": suggested_module,
        "file_path": module_info.get("file_path", ""),
        "reason": f"Dựa trên group '{drug_data.get('group', '')}' và indications"
    }

def list_duplicate_drugs() -> List[Dict]:
    """
    Tìm các thuốc trùng lặp giữa các module
    
    Returns:
        List of {drug_name: str, modules: List[str]}
    """
    drug_to_modules = {}
    
    for module_name, drugs in DRUG_MODULES.items():
        for drug_name in drugs.keys():
            drug_name_lower = drug_name.lower()
            if drug_name_lower not in drug_to_modules:
                drug_to_modules[drug_name_lower] = []
            if module_name not in drug_to_modules[drug_name_lower]:
                drug_to_modules[drug_name_lower].append(module_name)
    
    duplicates = []
    for drug_name_lower, modules in drug_to_modules.items():
        if len(modules) > 1:
            # Get original name
            for module in modules:
                for orig_name in DRUG_MODULES[module].keys():
                    if orig_name.lower() == drug_name_lower:
                        duplicates.append({
                            "drug_name": orig_name,
                            "modules": modules,
                            "count": len(modules)
                        })
                        break
                if duplicates and duplicates[-1]["drug_name"] == orig_name:
                    break
    
    return duplicates

def get_module_statistics() -> Dict:
    """Thống kê chi tiết về các module"""
    stats = {}
    
    for module_name, drugs in DRUG_MODULES.items():
        metadata = MODULE_METADATA.get(module_name, {})
        stats[module_name] = {
            "count": len(drugs),
            "code": metadata.get("code", ""),
            "description": metadata.get("description", ""),
            "file_path": metadata.get("file_path", ""),
            "subcategories": metadata.get("subcategories", []),
            "priority": metadata.get("priority", 99),
        }
    
    return stats

def export_module_structure(output_file: str = "drug_module_structure.json"):
    """Xuất cấu trúc module ra file JSON để dễ xem"""
    structure = {
        "modules": {},
        "total_drugs": 0,
        "duplicates": list_duplicate_drugs()
    }
    
    total = 0
    for module_name, drugs in DRUG_MODULES.items():
        metadata = MODULE_METADATA.get(module_name, {})
        drug_list = sorted(drugs.keys())
        
        structure["modules"][module_name] = {
            "code": metadata.get("code", ""),
            "count": len(drugs),
            "description": metadata.get("description", ""),
            "file_path": metadata.get("file_path", ""),
            "drugs": drug_list[:10],  # First 10 for preview
            "total_drugs": len(drugs)
        }
        total += len(drugs)
    
    structure["total_drugs"] = total
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(structure, f, ensure_ascii=False, indent=2)
    
    return output_file

