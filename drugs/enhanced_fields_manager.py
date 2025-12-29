"""
Enhanced Fields Manager - Quản lý và sửa chữa Enhanced Fields
Công cụ để bổ sung, sửa chữa fields dễ dàng
"""

from typing import Dict, List, Tuple, Optional
from pathlib import Path
import json
from .enhanced_fields_index import (
    get_field_index,
    find_drugs_missing_fields,
    find_drugs_with_field,
    get_drug_field_status,
    ALL_ENHANCED_FIELDS,
    FIELD_METADATA,
    get_field_template,
)
from .drug_manager import find_drug_file
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

def find_drugs_needing_fields(field_names: List[str], limit: int = 20) -> List[Tuple[str, List[str], str]]:
    """
    Tìm thuốc cần bổ sung fields và vị trí file
    
    Args:
        field_names: List fields cần kiểm tra
        limit: Số lượng kết quả tối đa
    
    Returns:
        List of (drug_name, missing_fields, file_path)
    """
    missing_drugs = find_drugs_missing_fields(field_names, missing_all=False)
    results = []
    
    for drug_name, missing_fields in missing_drugs[:limit]:
        file_path = find_drug_file(drug_name)
        file_str = str(file_path) if file_path else "Không tìm thấy"
        results.append((drug_name, missing_fields, file_str))
    
    return results

def get_field_completion_report() -> Dict:
    """
    Báo cáo hoàn thiện fields
    
    Returns:
        Dict với thông tin chi tiết
    """
    index = get_field_index()
    
    report = {
        "summary": {
            "total_drugs": len(DRUG_DATABASE),
            "complete_drugs": len(index["complete_drugs"]),
            "incomplete_drugs": len(index["incomplete_drugs"]),
        },
        "by_field": {},
        "by_drug": {},
        "priority_drugs": [],  # Drugs missing core fields
    }
    
    # By field
    for field in ALL_ENHANCED_FIELDS:
        has_count = len(find_drugs_with_field(field, has_field=True))
        missing_count = len(find_drugs_with_field(field, has_field=False))
        missing_drugs = find_drugs_with_field(field, has_field=False)[:10]
        
        report["by_field"][field] = {
            "has": has_count,
            "missing": missing_count,
            "coverage": (has_count / len(DRUG_DATABASE) * 100) if len(DRUG_DATABASE) > 0 else 0,
            "missing_drugs_sample": missing_drugs,
        }
    
    # By drug
    for drug_name, missing_fields in index["incomplete_drugs"]:
        report["by_drug"][drug_name] = {
            "missing_count": len(missing_fields),
            "missing_fields": missing_fields,
            "file_path": str(find_drug_file(drug_name)) if find_drug_file(drug_name) else None,
        }
        
        # Priority: missing core fields
        core_missing = [f for f in missing_fields if FIELD_METADATA.get(f, {}).get("category") == "core"]
        if core_missing:
            report["priority_drugs"].append({
                "drug_name": drug_name,
                "missing_core_fields": core_missing,
                "file_path": str(find_drug_file(drug_name)) if find_drug_file(drug_name) else None,
            })
    
    return report

def suggest_field_content(drug_name: str, field_name: str) -> Optional[Dict]:
    """
    Gợi ý nội dung cho field dựa trên thông tin hiện có
    
    Args:
        drug_name: Tên thuốc
        field_name: Tên field cần gợi ý
    
    Returns:
        Dict với gợi ý hoặc None
    """
    if drug_name not in DRUG_DATABASE:
        return None
    
    drug_data = DRUG_DATABASE[drug_name].copy()
    if drug_name in EXTRA_ENHANCED_FIELDS:
        drug_data.update(EXTRA_ENHANCED_FIELDS[drug_name])
    
    suggestions = {}
    
    # Gợi ý dựa trên field
    if field_name == "contraindications":
        # Gợi ý từ contraindications list hiện có
        if "contraindications" in drug_data and isinstance(drug_data["contraindications"], list):
            suggestions["tuyệt_đối"] = drug_data["contraindications"]
            suggestions["tương_đối"] = []
    
    elif field_name == "drug_interactions":
        # Gợi ý từ interactions list hiện có
        if "interactions" in drug_data and isinstance(drug_data["interactions"], list):
            suggestions["major"] = []
            suggestions["moderate"] = []
            suggestions["minor"] = [
                {"drug": item, "mechanism": "Cần tra cứu", "effect": "Cần tra cứu", "management": "Cần tra cứu"}
                for item in drug_data["interactions"]
            ]
    
    elif field_name == "pregnancy_lactation":
        # Gợi ý từ pregnancy field hiện có
        if "pregnancy" in drug_data:
            suggestions["fda_category"] = drug_data["pregnancy"]
            suggestions["pregnancy_details"] = f"Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ cho {drug_name}."
            suggestions["lactation"] = {
                "safety": "Cần tra cứu",
                "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
            }
    
    elif field_name == "hepatic_adjustment":
        # Gợi ý dựa trên metabolism
        pk = drug_data.get("pharmacokinetics", {})
        metabolism = pk.get("metabolism", "").lower() if isinstance(pk, dict) else ""
        
        if "gan" in metabolism or "liver" in metabolism or "hepatic" in metabolism:
            suggestions["mild"] = "Thận trọng (chuyển hóa qua gan)"
            suggestions["moderate"] = "Thận trọng, có thể giảm liều"
            suggestions["severe"] = "Thận trọng, giảm liều hoặc chống chỉ định"
        else:
            suggestions["mild"] = "Không đổi"
            suggestions["moderate"] = "Không đổi"
            suggestions["severe"] = "Thận trọng"
        
        suggestions["notes"] = f"{drug_name} {'chuyển hóa qua gan' if 'gan' in metabolism else 'thải trừ chủ yếu qua thận'}. Suy gan có thể ảnh hưởng đến chuyển hóa."
    
    elif field_name == "overdose_management":
        # Template chung
        suggestions["symptoms"] = ["Cần tra cứu thêm thông tin về triệu chứng quá liều"]
        suggestions["antidote"] = "Không có antidote đặc hiệu" if field_name != "reversal_agents" else None
        suggestions["treatment"] = [
            "Ngừng ngay thuốc",
            "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
            "Than hoạt tính",
            "Điều trị hỗ trợ và điều trị triệu chứng",
            "Theo dõi dấu hiệu sinh tồn"
        ]
        suggestions["monitoring"] = "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
    
    if suggestions:
        return {
            "field": field_name,
            "suggestions": suggestions,
            "template": get_field_template(field_name),
            "note": "Đây là gợi ý dựa trên thông tin hiện có. Cần tra cứu và bổ sung thêm."
        }
    
    return None

def generate_field_code(drug_name: str, field_name: str, field_value: Dict) -> str:
    """
    Tạo code Python để thêm field vào enhanced_fields_overrides.py
    
    Args:
        drug_name: Tên thuốc
        field_name: Tên field
        field_value: Giá trị field
    
    Returns:
        String code Python
    """
    # Format field_value as Python dict
    field_str = json.dumps(field_value, ensure_ascii=False, indent=8)
    # Convert to Python dict format
    field_str = field_str.replace('"', '"').replace("'", "'")
    
    code = f'''# Add {field_name} for {drug_name}
EXTRA_ENHANCED_FIELDS.setdefault("{drug_name}", {{}})["{field_name}"] = {field_str}
'''
    return code

def validate_drug_fields(drug_name: str) -> Tuple[bool, List[str]]:
    """
    Validate tất cả fields của một thuốc
    
    Returns:
        (is_valid, list_of_errors)
    """
    from .enhanced_fields_schema import validate_enhanced_fields
    
    if drug_name not in DRUG_DATABASE:
        return False, [f"Thuốc '{drug_name}' không tồn tại trong database"]
    
    drug_data = DRUG_DATABASE[drug_name].copy()
    if drug_name in EXTRA_ENHANCED_FIELDS:
        drug_data.update(EXTRA_ENHANCED_FIELDS[drug_name])
    
    # Extract enhanced fields
    enhanced_fields = {k: v for k, v in drug_data.items() if k in ALL_ENHANCED_FIELDS}
    
    is_valid, errors = validate_enhanced_fields(drug_name, enhanced_fields)
    return is_valid, errors

def export_field_completion_report(output_file: str = "field_completion_report.json"):
    """Xuất báo cáo hoàn thiện fields"""
    report = get_field_completion_report()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    return output_file

