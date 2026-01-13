"""
Field Validator
Validate 14 field chuẩn + 8 field bổ sung, kiểm tra thứ tự và format
"""
from typing import Dict, List, Set, Optional, Any, Tuple
from collections import defaultdict

# 14 field chuẩn theo thứ tự
STANDARD_14_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy",
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
]

# 8 field bổ sung
ADDITIONAL_8_FIELDS = [
    "black_box_warnings", "drug_interactions", "pregnancy_lactation",
    "hepatic_adjustment", "overdose_management", "reversal_agents",
    "administration_instructions", "references"
]

# Các field bổ sung khác được sử dụng rộng rãi (không trong ADDITIONAL_8_FIELDS nhưng quan trọng)
ADDITIONAL_COMMON_FIELDS = [
    "renal_adjustment",  # Điều chỉnh liều suy thận - được sử dụng rộng rãi
    "contraindications_detail",  # Chống chỉ định chi tiết - được sử dụng rộng rãi
]

ALL_FIELDS = STANDARD_14_FIELDS + ADDITIONAL_8_FIELDS
ALL_FIELDS_WITH_COMMON = ALL_FIELDS + ADDITIONAL_COMMON_FIELDS

# Field types
FIELD_TYPES = {
    "group": str,
    "vietnamese_name": str,
    "administration": list,
    "indications": list,
    "dosage": (dict, str),
    "side_effects": list,
    "contraindications": (list, dict),
    "interactions": (list, dict),
    "pregnancy": str,
    "mechanism_of_action": (str, tuple),
    "monitoring": list,
    "precautions": (list, dict),
    "pharmacokinetics": dict,
    "storage": str,
    "black_box_warnings": (str, type(None)),
    "drug_interactions": dict,
    "pregnancy_lactation": dict,
    "hepatic_adjustment": dict,
    "overdose_management": dict,
    "reversal_agents": (dict, type(None)),
    "administration_instructions": dict,
    "references": dict,
    # Additional common fields
    "renal_adjustment": dict,
    "contraindications_detail": dict,
}

class FieldValidator:
    """Field Validator"""
    
    def __init__(self):
        """Khởi tạo validator"""
        pass
    
    def validate_field_exists(self, drug_data: Dict[str, Any], field: str) -> bool:
        """Kiểm tra field có tồn tại không"""
        return field in drug_data
    
    def validate_field_type(self, drug_data: Dict[str, Any], field: str) -> Tuple[bool, Optional[str]]:
        """
        Kiểm tra kiểu dữ liệu của field
        
        Returns:
            (is_valid, error_message)
        """
        if field not in drug_data:
            return True, None  # Không có field thì không kiểm tra type
        
        value = drug_data[field]
        expected_types = FIELD_TYPES.get(field)
        
        if expected_types is None:
            return True, None  # Không có định nghĩa type
        
        # Handle tuple of types
        if isinstance(expected_types, tuple):
            if not any(isinstance(value, t) for t in expected_types):
                return False, f"Field '{field}' should be one of {expected_types}, got {type(value).__name__}"
        else:
            if not isinstance(value, expected_types):
                return False, f"Field '{field}' should be {expected_types.__name__}, got {type(value).__name__}"
        
        return True, None
    
    def validate_field_not_empty(self, drug_data: Dict[str, Any], field: str) -> Tuple[bool, Optional[str]]:
        """Kiểm tra field không rỗng"""
        if field not in drug_data:
            return True, None
        
        value = drug_data[field]
        
        if value is None:
            return True, None  # None is allowed for some fields
        
        if isinstance(value, str):
            if not value.strip():
                return False, f"Field '{field}' is empty"
        elif isinstance(value, (list, dict)):
            if len(value) == 0:
                return False, f"Field '{field}' is empty"
        
        return True, None
    
    def validate_field_order(self, drug_data: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Kiểm tra thứ tự field
        
        Returns:
            (is_correct_order, list_of_out_of_order_fields)
        """
        drug_keys = list(drug_data.keys())
        out_of_order = []
        
        # Tìm vị trí của các field chuẩn trong drug_data
        field_positions = {}
        for i, key in enumerate(drug_keys):
            if key in ALL_FIELDS:
                field_positions[key] = i
        
        # Kiểm tra thứ tự
        last_position = -1
        for field in ALL_FIELDS:
            if field in field_positions:
                current_position = field_positions[field]
                if current_position < last_position:
                    out_of_order.append(field)
                last_position = max(last_position, current_position)
        
        return len(out_of_order) == 0, out_of_order
    
    def validate_field_format(self, drug_data: Dict[str, Any], field: str) -> Tuple[bool, Optional[str]]:
        """
        Kiểm tra format của field
        
        Returns:
            (is_valid, error_message)
        """
        if field not in drug_data:
            return True, None
        
        value = drug_data[field]
        
        # Format checks for specific fields
        if field == "administration":
            if isinstance(value, list):
                valid_routes = ["PO", "IV", "IM", "SC", "Inhalation", "Topical", "Vaginal", "Rectal", "Transdermal"]
                for route in value:
                    if isinstance(route, str) and route not in valid_routes:
                        # Allow custom routes but warn
                        pass
        
        elif field == "pregnancy":
            if isinstance(value, str):
                valid_categories = ["A", "B", "C", "D", "X"]
                if not any(cat in value for cat in valid_categories):
                    return False, f"Field 'pregnancy' should contain FDA category (A, B, C, D, or X)"
        
        elif field == "dosage":
            if isinstance(value, dict):
                # Check for common dosage keys
                common_keys = ["adult", "pediatric", "renal", "hepatic", "notes"]
                # Allow any keys but suggest common ones
        
        elif field == "pharmacokinetics":
            if isinstance(value, dict):
                common_keys = ["half_life", "onset", "duration", "protein_binding", "metabolism", "clearance"]
                # Allow any keys but suggest common ones
        
        return True, None
    
    def validate_all_fields(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate tất cả field
        
        Returns:
            Dict chứa kết quả validation
        """
        result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'missing_standard_fields': [],
            'missing_additional_fields': [],
            'type_errors': [],
            'empty_fields': [],
            'order_issues': [],
            'format_issues': [],
        }
        
        # Kiểm tra field tồn tại
        for field in STANDARD_14_FIELDS:
            if not self.validate_field_exists(drug_data, field):
                result['missing_standard_fields'].append(field)
                result['valid'] = False
                result['errors'].append(f"Missing required field: {field}")
        
        for field in ADDITIONAL_8_FIELDS:
            if not self.validate_field_exists(drug_data, field):
                result['missing_additional_fields'].append(field)
                result['warnings'].append(f"Missing additional field: {field}")
        
        # Kiểm tra type
        for field in ALL_FIELDS:
            if field in drug_data:
                is_valid, error = self.validate_field_type(drug_data, field)
                if not is_valid:
                    result['type_errors'].append(error)
                    result['warnings'].append(error)
        
        # Kiểm tra empty
        for field in STANDARD_14_FIELDS:
            if field in drug_data:
                is_valid, error = self.validate_field_not_empty(drug_data, field)
                if not is_valid:
                    result['empty_fields'].append(field)
                    result['warnings'].append(error)
        
        # Kiểm tra thứ tự
        is_correct_order, out_of_order = self.validate_field_order(drug_data)
        if not is_correct_order:
            result['order_issues'] = out_of_order
            result['warnings'].append(f"Fields out of order: {', '.join(out_of_order)}")
        
        # Kiểm tra format
        for field in ALL_FIELDS:
            if field in drug_data:
                is_valid, error = self.validate_field_format(drug_data, field)
                if not is_valid:
                    result['format_issues'].append(error)
                    result['warnings'].append(error)
        
        return result
    
    def validate_multiple_drugs(self, drugs_data: Dict[str, Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        """
        Validate nhiều thuốc
        
        Args:
            drugs_data: Dict {drug_name: drug_data}
        
        Returns:
            Dict {drug_name: validation_result}
        """
        results = {}
        for drug_name, drug_data in drugs_data.items():
            results[drug_name] = self.validate_all_fields(drug_data)
        return results
    
    def get_validation_summary(self, validation_results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Tạo summary từ validation results
        
        Args:
            validation_results: Kết quả từ validate_multiple_drugs
        
        Returns:
            Summary dict
        """
        summary = {
            'total_drugs': len(validation_results),
            'valid_drugs': 0,
            'invalid_drugs': 0,
            'drugs_with_missing_standard_fields': 0,
            'drugs_with_missing_additional_fields': 0,
            'drugs_with_type_errors': 0,
            'drugs_with_empty_fields': 0,
            'drugs_with_order_issues': 0,
            'drugs_with_format_issues': 0,
            'most_missing_field': defaultdict(int),
        }
        
        for drug_name, result in validation_results.items():
            if result['valid']:
                summary['valid_drugs'] += 1
            else:
                summary['invalid_drugs'] += 1
            
            if result['missing_standard_fields']:
                summary['drugs_with_missing_standard_fields'] += 1
                for field in result['missing_standard_fields']:
                    summary['most_missing_field'][field] += 1
            
            if result['missing_additional_fields']:
                summary['drugs_with_missing_additional_fields'] += 1
            
            if result['type_errors']:
                summary['drugs_with_type_errors'] += 1
            
            if result['empty_fields']:
                summary['drugs_with_empty_fields'] += 1
            
            if result['order_issues']:
                summary['drugs_with_order_issues'] += 1
            
            if result['format_issues']:
                summary['drugs_with_format_issues'] += 1
        
        return summary


# Convenience function
def get_field_validator() -> FieldValidator:
    """Lấy FieldValidator instance"""
    return FieldValidator()


if __name__ == "__main__":
    # Test
    validator = get_field_validator()
    
    test_drug = {
        "group": "Test Group",
        "vietnamese_name": "Test Drug",
        "administration": ["PO"],
        "indications": ["Test indication"],
        "dosage": {"adult": "100mg"},
        "side_effects": ["Nausea"],
        "contraindications": ["Allergy"],
        "interactions": [],
        "pregnancy": "B",
        "mechanism_of_action": "Test mechanism",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {},
        "storage": "Room temperature",
    }
    
    result = validator.validate_all_fields(test_drug)
    print(f"Validation result: {result}")

