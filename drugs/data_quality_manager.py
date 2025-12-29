"""
Data Quality Manager - Quản lý chất lượng dữ liệu thuốc
Phát hiện và sửa lỗi, đảm bảo tính nhất quán, tránh sai sót
"""

from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict
import re
from .drug_database import DRUG_DATABASE
from .enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS

# ============================================================================
# DATA QUALITY RULES - Quy tắc chất lượng dữ liệu
# ============================================================================

QUALITY_RULES = {
    "required_fields": {
        "core": ["group", "vietnamese_name", "administration", "indications", "dosage"],
        "extended": ["side_effects", "contraindications", "interactions"],
    },
    "field_types": {
        "administration": list,
        "indications": list,
        "contraindications": (list, dict),
        "side_effects": list,
        "interactions": list,
        "monitoring": list,
        "precautions": list,
    },
    "value_constraints": {
        "pregnancy": ["A", "B", "C", "D", "X", ""],
        "administration": ["PO", "IV", "IM", "SC", "Topical", "Inhaled", "Rectal", "Ophthalmic"],
    },
    "format_patterns": {
        "dosage": r"\d+.*(mg|g|ml|units|IU|mcg|μg).*",
        "vietnamese_name": r".*[a-zA-Z].*",  # Phải có ít nhất 1 chữ cái
    },
}

# ============================================================================
# ERROR DETECTION - Phát hiện lỗi
# ============================================================================

class DataQualityError:
    """Lỗi chất lượng dữ liệu"""
    def __init__(self, drug_name: str, error_type: str, field: str, message: str, severity: str = "warning"):
        self.drug_name = drug_name
        self.error_type = error_type
        self.field = field
        self.message = message
        self.severity = severity  # "error", "warning", "info"
    
    def __repr__(self):
        return f"{self.severity.upper()}: {self.drug_name}.{self.field} - {self.message}"

def check_required_fields(drug_name: str, drug_data: Dict) -> List[DataQualityError]:
    """Kiểm tra fields bắt buộc"""
    errors = []
    
    for field in QUALITY_RULES["required_fields"]["core"]:
        if field not in drug_data or not drug_data[field]:
            errors.append(DataQualityError(
                drug_name, "missing_field", field,
                f"Thiếu field bắt buộc: {field}",
                "error"
            ))
    
    return errors

def check_field_types(drug_name: str, drug_data: Dict) -> List[DataQualityError]:
    """Kiểm tra kiểu dữ liệu"""
    errors = []
    
    for field, expected_type in QUALITY_RULES["field_types"].items():
        if field not in drug_data:
            continue
        
        value = drug_data[field]
        if value is None:
            continue
        
        if isinstance(expected_type, tuple):
            if not any(isinstance(value, t) for t in expected_type):
                errors.append(DataQualityError(
                    drug_name, "wrong_type", field,
                    f"Kiểu dữ liệu sai: mong đợi {expected_type}, nhận được {type(value).__name__}",
                    "error"
                ))
        elif not isinstance(value, expected_type):
            errors.append(DataQualityError(
                drug_name, "wrong_type", field,
                f"Kiểu dữ liệu sai: mong đợi {expected_type.__name__}, nhận được {type(value).__name__}",
                "error"
            ))
    
    return errors

def check_value_constraints(drug_name: str, drug_data: Dict) -> List[DataQualityError]:
    """Kiểm tra ràng buộc giá trị"""
    errors = []
    
    for field, allowed_values in QUALITY_RULES["value_constraints"].items():
        if field not in drug_data:
            continue
        
        value = drug_data[field]
        if isinstance(value, list):
            # Check each item in list
            for item in value:
                if item not in allowed_values:
                    errors.append(DataQualityError(
                        drug_name, "invalid_value", field,
                        f"Giá trị không hợp lệ: '{item}' không có trong {allowed_values}",
                        "warning"
                    ))
        elif value not in allowed_values:
            errors.append(DataQualityError(
                drug_name, "invalid_value", field,
                f"Giá trị không hợp lệ: '{value}' không có trong {allowed_values}",
                "warning"
            ))
    
    return errors

def check_duplicates() -> List[DataQualityError]:
    """Kiểm tra thuốc trùng lặp"""
    errors = []
    drug_names_seen = {}
    
    for drug_name, drug_data in DRUG_DATABASE.items():
        drug_name_lower = drug_name.lower()
        
        if drug_name_lower in drug_names_seen:
            original = drug_names_seen[drug_name_lower]
            errors.append(DataQualityError(
                drug_name, "duplicate", "name",
                f"Trùng lặp với '{original}' (case-insensitive)",
                "error"
            ))
        else:
            drug_names_seen[drug_name_lower] = drug_name
    
    return errors

def check_consistency(drug_name: str, drug_data: Dict) -> List[DataQualityError]:
    """Kiểm tra tính nhất quán"""
    errors = []
    
    # Check: nếu có contraindications dict thì không nên có contraindications list
    if isinstance(drug_data.get("contraindications"), dict):
        if "contraindications" in drug_data and isinstance(drug_data.get("contraindications", []), list):
            errors.append(DataQualityError(
                drug_name, "inconsistency", "contraindications",
                "Có cả contraindications dạng dict và list - nên chỉ dùng một",
                "warning"
            ))
    
    # Check: nếu có drug_interactions dict thì không nên có interactions list
    if isinstance(drug_data.get("drug_interactions"), dict):
        if "interactions" in drug_data and isinstance(drug_data.get("interactions"), list):
            errors.append(DataQualityError(
                drug_name, "inconsistency", "interactions",
                "Có cả drug_interactions (dict) và interactions (list) - nên đồng bộ",
                "warning"
            ))
    
    # Check: pregnancy field và pregnancy_lactation dict
    if "pregnancy" in drug_data and "pregnancy_lactation" in drug_data:
        pl = drug_data.get("pregnancy_lactation", {})
        if isinstance(pl, dict) and "fda_category" in pl:
            if drug_data["pregnancy"] != pl["fda_category"]:
                errors.append(DataQualityError(
                    drug_name, "inconsistency", "pregnancy",
                    f"pregnancy='{drug_data['pregnancy']}' khác với pregnancy_lactation.fda_category='{pl['fda_category']}'",
                    "warning"
                ))
    
    return errors

def check_format(drug_name: str, drug_data: Dict) -> List[DataQualityError]:
    """Kiểm tra format"""
    errors = []
    
    # Check dosage format
    if "dosage" in drug_data:
        dosage = drug_data["dosage"]
        if isinstance(dosage, dict):
            for key, value in dosage.items():
                if isinstance(value, str) and not re.search(QUALITY_RULES["format_patterns"]["dosage"], value, re.IGNORECASE):
                    # Warning only, not error
                    errors.append(DataQualityError(
                        drug_name, "format_issue", f"dosage.{key}",
                        f"Format liều có thể không chuẩn: '{value}'",
                        "info"
                    ))
    
    # Check vietnamese_name
    if "vietnamese_name" in drug_data:
        vn_name = drug_data["vietnamese_name"]
        if not re.search(QUALITY_RULES["format_patterns"]["vietnamese_name"], vn_name):
            errors.append(DataQualityError(
                drug_name, "format_issue", "vietnamese_name",
                f"Tên tiếng Việt có thể không hợp lệ: '{vn_name}'",
                "warning"
            ))
    
    return errors

def check_completeness(drug_name: str, drug_data: Dict) -> List[DataQualityError]:
    """Kiểm tra độ đầy đủ"""
    errors = []
    
    # Check empty lists
    for field in ["indications", "contraindications", "side_effects", "monitoring", "precautions"]:
        if field in drug_data:
            value = drug_data[field]
            if isinstance(value, list) and len(value) == 0:
                errors.append(DataQualityError(
                    drug_name, "incomplete", field,
                    f"List rỗng - nên có ít nhất 1 mục",
                    "warning"
                ))
    
    # Check empty strings
    for field in ["mechanism_of_action", "storage"]:
        if field in drug_data:
            value = drug_data[field]
            if isinstance(value, str) and len(value.strip()) < 10:
                errors.append(DataQualityError(
                    drug_name, "incomplete", field,
                    f"Nội dung quá ngắn (<10 ký tự)",
                    "warning"
                ))
    
    return errors

def check_all_quality(drug_name: Optional[str] = None) -> List[DataQualityError]:
    """
    Kiểm tra chất lượng dữ liệu cho tất cả hoặc một thuốc
    
    Args:
        drug_name: Tên thuốc (None = tất cả)
    
    Returns:
        List of DataQualityError
    """
    all_errors = []
    
    drugs_to_check = {drug_name: DRUG_DATABASE[drug_name]} if drug_name else DRUG_DATABASE
    
    # Check duplicates (only once for all)
    if not drug_name:
        all_errors.extend(check_duplicates())
    
    for dname, ddata in drugs_to_check.items():
        # Apply overrides
        if dname in EXTRA_ENHANCED_FIELDS:
            ddata = {**ddata, **EXTRA_ENHANCED_FIELDS[dname]}
        
        all_errors.extend(check_required_fields(dname, ddata))
        all_errors.extend(check_field_types(dname, ddata))
        all_errors.extend(check_value_constraints(dname, ddata))
        all_errors.extend(check_consistency(dname, ddata))
        all_errors.extend(check_format(dname, ddata))
        all_errors.extend(check_completeness(dname, ddata))
    
    return all_errors

# ============================================================================
# AUTO-FIX SUGGESTIONS - Gợi ý sửa tự động
# ============================================================================

def suggest_fixes(error: DataQualityError) -> List[Dict]:
    """Gợi ý cách sửa lỗi"""
    suggestions = []
    
    if error.error_type == "missing_field":
        # Gợi ý thêm field
        suggestions.append({
            "action": "add_field",
            "field": error.field,
            "suggestion": f"Thêm field '{error.field}' với giá trị mặc định",
            "code": f'drug_data["{error.field}"] = ...'  # Placeholder
        })
    
    elif error.error_type == "wrong_type":
        # Gợi ý chuyển đổi type
        suggestions.append({
            "action": "convert_type",
            "field": error.field,
            "suggestion": f"Chuyển đổi {error.field} sang đúng kiểu dữ liệu",
            "code": f'# Convert {error.field} to correct type'
        })
    
    elif error.error_type == "duplicate":
        suggestions.append({
            "action": "merge_or_remove",
            "field": error.field,
            "suggestion": "Gộp hoặc xóa bản trùng lặp",
            "code": "# Review and merge duplicate entries"
        })
    
    elif error.error_type == "inconsistency":
        suggestions.append({
            "action": "synchronize",
            "field": error.field,
            "suggestion": f"Đồng bộ {error.field} - chọn một format",
            "code": f"# Synchronize {error.field} fields"
        })
    
    return suggestions

# ============================================================================
# QUALITY METRICS - Chỉ số chất lượng
# ============================================================================

def calculate_quality_metrics() -> Dict:
    """Tính toán chỉ số chất lượng dữ liệu"""
    all_errors = check_all_quality()
    
    total_drugs = len(DRUG_DATABASE)
    
    # Group by severity
    by_severity = defaultdict(int)
    by_type = defaultdict(int)
    by_drug = defaultdict(list)
    
    for error in all_errors:
        by_severity[error.severity] += 1
        by_type[error.error_type] += 1
        by_drug[error.drug_name].append(error)
    
    # Calculate scores
    error_count = by_severity.get("error", 0)
    warning_count = by_severity.get("warning", 0)
    info_count = by_severity.get("info", 0)
    
    # Quality score (0-100)
    total_issues = error_count * 3 + warning_count * 2 + info_count * 1
    max_possible_issues = total_drugs * 20  # Estimate
    quality_score = max(0, 100 - (total_issues / max_possible_issues * 100))
    
    return {
        "total_drugs": total_drugs,
        "total_errors": len(all_errors),
        "by_severity": dict(by_severity),
        "by_type": dict(by_type),
        "drugs_with_errors": len(by_drug),
        "quality_score": quality_score,
        "error_rate": (error_count / total_drugs * 100) if total_drugs > 0 else 0,
        "top_issues": sorted(by_type.items(), key=lambda x: x[1], reverse=True)[:10],
    }

