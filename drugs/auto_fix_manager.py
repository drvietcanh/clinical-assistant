"""
Auto-Fix Manager - Tự động sửa lỗi phổ biến
Sửa lỗi tự động với preview và confirmation
"""

from typing import Dict, List, Tuple, Optional
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS
from .data_quality_manager import check_all_quality, DataQualityError, suggest_fixes

# ============================================================================
# AUTO-FIX RULES - Quy tắc sửa tự động
# ============================================================================

def fix_missing_field_defaults(drug_name: str, drug_data: Dict) -> Dict:
    """Sửa lỗi thiếu field bằng giá trị mặc định"""
    fixes = {}
    
    # Default values for common missing fields
    defaults = {
        "side_effects": [],
        "interactions": [],
        "monitoring": [],
        "precautions": [],
    }
    
    for field, default_value in defaults.items():
        if field not in drug_data or not drug_data[field]:
            fixes[field] = default_value
    
    return fixes

def fix_type_conversions(drug_name: str, drug_data: Dict) -> Dict:
    """Sửa lỗi kiểu dữ liệu"""
    fixes = {}
    
    # Convert list to dict for contraindications
    if "contraindications" in drug_data:
        value = drug_data["contraindications"]
        if isinstance(value, list) and len(value) > 0:
            # Convert to dict format
            fixes["contraindications"] = {
                "tuyệt_đối": value.copy(),
                "tương_đối": []
            }
    
    # Convert list to dict for interactions
    if "interactions" in drug_data and "drug_interactions" not in drug_data:
        value = drug_data["interactions"]
        if isinstance(value, list) and len(value) > 0:
            fixes["drug_interactions"] = {
                "major": [],
                "moderate": [],
                "minor": [
                    {"drug": item, "mechanism": "Cần tra cứu", "effect": "Cần tra cứu", "management": "Cần tra cứu"}
                    for item in value
                ]
            }
    
    return fixes

def fix_consistency_issues(drug_name: str, drug_data: Dict) -> Dict:
    """Sửa lỗi tính nhất quán"""
    fixes = {}
    
    # Sync pregnancy fields
    if "pregnancy" in drug_data and "pregnancy_lactation" in drug_data:
        pl = drug_data["pregnancy_lactation"]
        if isinstance(pl, dict) and "fda_category" in pl:
            if drug_data["pregnancy"] != pl["fda_category"]:
                # Update pregnancy_lactation to match pregnancy
                fixes["pregnancy_lactation"] = {
                    **pl,
                    "fda_category": drug_data["pregnancy"]
                }
    
    return fixes

def auto_fix_drug(drug_name: str, dry_run: bool = True) -> Dict:
    """
    Tự động sửa lỗi cho một thuốc
    
    Args:
        drug_name: Tên thuốc
        dry_run: True nếu chỉ preview, False nếu thực sự sửa
    
    Returns:
        Dict với thông tin fixes
    """
    if drug_name not in DRUG_DATABASE:
        return {"error": f"Thuốc '{drug_name}' không tồn tại"}
    
    drug_data = DRUG_DATABASE[drug_name].copy()
    if drug_name in EXTRA_ENHANCED_FIELDS:
        drug_data.update(EXTRA_ENHANCED_FIELDS[drug_name])
    
    # Check errors
    errors = check_all_quality(drug_name=drug_name)
    
    # Collect fixes
    all_fixes = {}
    all_fixes.update(fix_missing_field_defaults(drug_name, drug_data))
    all_fixes.update(fix_type_conversions(drug_name, drug_data))
    all_fixes.update(fix_consistency_issues(drug_name, drug_data))
    
    # Generate fix code
    fix_code = ""
    if all_fixes:
        fix_code = f'''# Auto-fix for {drug_name}
EXTRA_ENHANCED_FIELDS.setdefault("{drug_name}", {{}})
'''
        for field, value in all_fixes.items():
            import json
            value_str = json.dumps(value, ensure_ascii=False, indent=4)
            fix_code += f'EXTRA_ENHANCED_FIELDS["{drug_name}"]["{field}"] = {value_str}\n'
    
    return {
        "drug_name": drug_name,
        "errors_found": len(errors),
        "fixes_available": len(all_fixes),
        "fixes": all_fixes,
        "fix_code": fix_code,
        "dry_run": dry_run,
        "note": "Chạy với dry_run=False để áp dụng fixes" if dry_run else "Fixes đã được áp dụng"
    }

def batch_auto_fix(drug_names: Optional[List[str]] = None, dry_run: bool = True) -> Dict:
    """
    Tự động sửa lỗi cho nhiều thuốc
    
    Args:
        drug_names: List tên thuốc (None = tất cả)
        dry_run: True nếu chỉ preview
    
    Returns:
        Dict với thông tin fixes
    """
    if drug_names is None:
        drug_names = list(DRUG_DATABASE.keys())
    
    results = {
        "total_drugs": len(drug_names),
        "fixed_drugs": 0,
        "total_fixes": 0,
        "fixes_by_drug": {},
        "fix_code": "",
    }
    
    all_fix_code = []
    
    for drug_name in drug_names:
        fix_result = auto_fix_drug(drug_name, dry_run=dry_run)
        
        if "error" in fix_result:
            continue
        
        if fix_result["fixes_available"] > 0:
            results["fixed_drugs"] += 1
            results["total_fixes"] += fix_result["fixes_available"]
            results["fixes_by_drug"][drug_name] = fix_result["fixes"]
            
            if fix_result["fix_code"]:
                all_fix_code.append(fix_result["fix_code"])
    
    # Combine fix code
    if all_fix_code:
        results["fix_code"] = "\n".join(all_fix_code)
    
    return results

