"""
Field Standardizer
Chuẩn hóa thứ tự field, bổ sung field thiếu, sửa format, chuẩn hóa cấu trúc field
"""
from typing import Dict, List, Set, Optional, Any
from collections import OrderedDict
import sys
from pathlib import Path

from .field_validator import (
    STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS, ALL_FIELDS,
    FieldValidator, get_field_validator
)

# Import mapping rules
sys.path.insert(0, str(Path(__file__).parent.parent))
try:
    from field_structure_mapping_rules import (
        standardize_pregnancy_lactation,
        standardize_hepatic_adjustment,
        standardize_overdose_management,
        standardize_contraindications,
        standardize_drug_interactions,
        standardize_administration_instructions,
        standardize_references,
        standardize_field,
        standardize_all_fields as standardize_all_field_structures
    )
except ImportError:
    # Fallback nếu không import được
    def standardize_pregnancy_lactation(value): return value
    def standardize_hepatic_adjustment(value): return value
    def standardize_overdose_management(value): return value
    def standardize_contraindications(value): return value
    def standardize_drug_interactions(value): return value
    def standardize_administration_instructions(value): return value
    def standardize_references(value): return value
    def standardize_field(field_name, value): return value
    def standardize_all_field_structures(drug_data): return drug_data

class FieldStandardizer:
    """Field Standardizer"""
    
    def __init__(self):
        """Khởi tạo standardizer"""
        self.validator = get_field_validator()
    
    def standardize_field_order(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chuẩn hóa thứ tự field theo thứ tự chuẩn
        
        Args:
            drug_data: Dữ liệu thuốc
        
        Returns:
            Dict với field đã sắp xếp lại
        """
        standardized = OrderedDict()
        
        # Thêm các field chuẩn theo thứ tự
        for field in STANDARD_14_FIELDS:
            if field in drug_data:
                standardized[field] = drug_data[field]
        
        # Thêm các field bổ sung theo thứ tự
        for field in ADDITIONAL_8_FIELDS:
            if field in drug_data:
                standardized[field] = drug_data[field]
        
        # Thêm các field khác (không trong danh sách chuẩn)
        for key, value in drug_data.items():
            if key not in ALL_FIELDS:
                standardized[key] = value
        
        return dict(standardized)
    
    def add_missing_fields(self, drug_data: Dict[str, Any], 
                          include_additional: bool = False,
                          use_templates: bool = True) -> Dict[str, Any]:
        """
        Bổ sung field thiếu
        
        Args:
            drug_data: Dữ liệu thuốc
            include_additional: Có bổ sung field bổ sung không
            use_templates: Có dùng template không
        
        Returns:
            Dict với field đã bổ sung
        """
        result = drug_data.copy()
        
        # Template cho các field
        templates = {
            "group": "",
            "vietnamese_name": "",
            "administration": [],
            "indications": [],
            "dosage": {},
            "side_effects": [],
            "contraindications": [],
            "interactions": [],
            "pregnancy": "",
            "mechanism_of_action": "",
            "monitoring": [],
            "precautions": [],
            "pharmacokinetics": {},
            "storage": "",
            "black_box_warnings": None,
            "drug_interactions": {"major": [], "moderate": [], "minor": []},
            "pregnancy_lactation": {
                "fda_category": "",
                "pregnancy_details": "",
                "lactation": {
                    "safety": "",
                    "details": "",
                    "recommendation": ""
                }
            },
            "hepatic_adjustment": {
                "mild": "",
                "moderate": "",
                "severe": "",
                "notes": ""
            },
            "overdose_management": {
                "symptoms": [],
                "antidote": "",
                "treatment": [],
                "monitoring": ""
            },
            "reversal_agents": None,
            "administration_instructions": {},
            "references": {
                "primary_sources": [],
                "last_updated": "",
                "evidence_level": ""
            },
        }
        
        # Bổ sung field chuẩn thiếu
        for field in STANDARD_14_FIELDS:
            if field not in result:
                if use_templates and field in templates:
                    # Deep copy template
                    import copy
                    result[field] = copy.deepcopy(templates[field])
                else:
                    # Use default based on type
                    if field in ["group", "vietnamese_name", "pregnancy", "mechanism_of_action", "storage"]:
                        result[field] = ""
                    elif field in ["administration", "indications", "side_effects", "contraindications", 
                                  "interactions", "monitoring", "precautions"]:
                        result[field] = []
                    elif field == "dosage":
                        result[field] = {}
                    elif field == "pharmacokinetics":
                        result[field] = {}
        
        # Bổ sung field bổ sung thiếu
        if include_additional:
            for field in ADDITIONAL_8_FIELDS:
                if field not in result:
                    if use_templates and field in templates:
                        import copy
                        result[field] = copy.deepcopy(templates[field])
                    else:
                        if field == "black_box_warnings":
                            result[field] = None
                        elif field == "reversal_agents":
                            result[field] = None
                        elif field in ["drug_interactions", "pregnancy_lactation", "hepatic_adjustment",
                                     "overdose_management", "administration_instructions", "references"]:
                            result[field] = {}
        
        return result
    
    def fix_field_format(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Sửa format field không đúng
        
        Args:
            drug_data: Dữ liệu thuốc
        
        Returns:
            Dict với format đã sửa
        """
        result = drug_data.copy()
        
        # Fix administration
        if "administration" in result:
            if isinstance(result["administration"], str):
                # Convert string to list
                result["administration"] = [result["administration"]]
            elif not isinstance(result["administration"], list):
                result["administration"] = []
        
        # Fix indications
        if "indications" in result:
            if isinstance(result["indications"], str):
                result["indications"] = [result["indications"]]
            elif not isinstance(result["indications"], list):
                result["indications"] = []
        
        # Fix side_effects
        if "side_effects" in result:
            if isinstance(result["side_effects"], str):
                result["side_effects"] = [result["side_effects"]]
            elif not isinstance(result["side_effects"], list):
                result["side_effects"] = []
        
        # Fix contraindications
        if "contraindications" in result:
            if isinstance(result["contraindications"], str):
                result["contraindications"] = [result["contraindications"]]
            # Keep as dict if it's already a dict (with tuyệt_đối/tương_đối)
        
        # Fix interactions
        if "interactions" in result:
            if isinstance(result["interactions"], str):
                result["interactions"] = [result["interactions"]]
            # Keep as dict if it's already a dict
        
        # Fix monitoring
        if "monitoring" in result:
            if isinstance(result["monitoring"], str):
                result["monitoring"] = [result["monitoring"]]
            elif not isinstance(result["monitoring"], list):
                result["monitoring"] = []
        
        # Fix precautions
        if "precautions" in result:
            if isinstance(result["precautions"], str):
                result["precautions"] = [result["precautions"]]
            # Keep as dict if it's already a dict
        
        # Fix dosage
        if "dosage" in result:
            if isinstance(result["dosage"], str):
                # Try to parse or create simple dict
                result["dosage"] = {"adult": result["dosage"]}
            elif not isinstance(result["dosage"], dict):
                result["dosage"] = {}
        
        # Fix pharmacokinetics
        if "pharmacokinetics" in result:
            if not isinstance(result["pharmacokinetics"], dict):
                result["pharmacokinetics"] = {}
        
        # Fix drug_interactions
        if "drug_interactions" in result:
            if not isinstance(result["drug_interactions"], dict):
                result["drug_interactions"] = {"major": [], "moderate": [], "minor": []}
            else:
                # Ensure structure
                if "major" not in result["drug_interactions"]:
                    result["drug_interactions"]["major"] = []
                if "moderate" not in result["drug_interactions"]:
                    result["drug_interactions"]["moderate"] = []
                if "minor" not in result["drug_interactions"]:
                    result["drug_interactions"]["minor"] = []
        
        return result
    
    def standardize_field_structure(self, field_name: str, value: Any) -> Any:
        """
        Chuẩn hóa cấu trúc của một field cụ thể
        
        Args:
            field_name: Tên field
            value: Giá trị hiện tại
        
        Returns:
            Giá trị đã chuẩn hóa
        """
        return standardize_field(field_name, value)
    
    def standardize_pregnancy_lactation_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc pregnancy_lactation"""
        if 'pregnancy_lactation' in drug_data:
            drug_data['pregnancy_lactation'] = standardize_pregnancy_lactation(drug_data['pregnancy_lactation'])
        return drug_data
    
    def standardize_hepatic_adjustment_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc hepatic_adjustment"""
        if 'hepatic_adjustment' in drug_data:
            drug_data['hepatic_adjustment'] = standardize_hepatic_adjustment(drug_data['hepatic_adjustment'])
        return drug_data
    
    def standardize_overdose_management_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc overdose_management"""
        if 'overdose_management' in drug_data:
            drug_data['overdose_management'] = standardize_overdose_management(drug_data['overdose_management'])
        return drug_data
    
    def standardize_contraindications_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc contraindications"""
        if 'contraindications' in drug_data:
            drug_data['contraindications'] = standardize_contraindications(drug_data['contraindications'])
        return drug_data
    
    def standardize_drug_interactions_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc drug_interactions"""
        if 'drug_interactions' in drug_data:
            drug_data['drug_interactions'] = standardize_drug_interactions(drug_data['drug_interactions'])
        return drug_data
    
    def standardize_administration_instructions_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc administration_instructions"""
        if 'administration_instructions' in drug_data:
            drug_data['administration_instructions'] = standardize_administration_instructions(drug_data['administration_instructions'])
        return drug_data
    
    def standardize_references_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """Chuẩn hóa cấu trúc references"""
        if 'references' in drug_data:
            drug_data['references'] = standardize_references(drug_data['references'])
        return drug_data
    
    def standardize_all_field_structures(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Chuẩn hóa cấu trúc của tất cả các field
        
        Args:
            drug_data: Dữ liệu thuốc
        
        Returns:
            Dữ liệu thuốc với tất cả field đã chuẩn hóa cấu trúc
        """
        return standardize_all_field_structures(drug_data)
    
    def standardize_drug(self, drug_data: Dict[str, Any], 
                        include_additional: bool = False,
                        fix_format: bool = True,
                        reorder: bool = True,
                        standardize_structures: bool = False) -> Dict[str, Any]:
        """
        Chuẩn hóa toàn bộ thuốc
        
        Args:
            drug_data: Dữ liệu thuốc
            include_additional: Có bổ sung field bổ sung không
            fix_format: Có sửa format không
            reorder: Có sắp xếp lại thứ tự không
            standardize_structures: Có chuẩn hóa cấu trúc field không
        
        Returns:
            Dict đã chuẩn hóa
        """
        result = drug_data.copy()
        
        # Bổ sung field thiếu
        result = self.add_missing_fields(result, include_additional=include_additional)
        
        # Chuẩn hóa cấu trúc field (nếu được yêu cầu)
        if standardize_structures:
            result = self.standardize_all_field_structures(result)
        
        # Sửa format
        if fix_format:
            result = self.fix_field_format(result)
        
        # Sắp xếp lại thứ tự
        if reorder:
            result = self.standardize_field_order(result)
        
        return result
    
    def standardize_multiple_drugs(self, drugs_data: Dict[str, Dict[str, Any]],
                                   include_additional: bool = False,
                                   fix_format: bool = True,
                                   reorder: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Chuẩn hóa nhiều thuốc
        
        Args:
            drugs_data: Dict {drug_name: drug_data}
            include_additional: Có bổ sung field bổ sung không
            fix_format: Có sửa format không
            reorder: Có sắp xếp lại thứ tự không
        
        Returns:
            Dict {drug_name: standardized_drug_data}
        """
        results = {}
        for drug_name, drug_data in drugs_data.items():
            results[drug_name] = self.standardize_drug(
                drug_data,
                include_additional=include_additional,
                fix_format=fix_format,
                reorder=reorder
            )
        return results
    
    def generate_change_report(self, original: Dict[str, Any], 
                              standardized: Dict[str, Any]) -> Dict[str, Any]:
        """
        Tạo báo cáo thay đổi
        
        Args:
            original: Dữ liệu gốc
            standardized: Dữ liệu đã chuẩn hóa
        
        Returns:
            Dict chứa báo cáo thay đổi
        """
        report = {
            'fields_added': [],
            'fields_removed': [],
            'fields_reordered': False,
            'fields_modified': [],
            'format_fixed': [],
        }
        
        original_keys = set(original.keys())
        standardized_keys = set(standardized.keys())
        
        # Fields added
        report['fields_added'] = list(standardized_keys - original_keys)
        
        # Fields removed (shouldn't happen, but check)
        report['fields_removed'] = list(original_keys - standardized_keys)
        
        # Check if order changed
        original_order = [k for k in original.keys() if k in ALL_FIELDS]
        standardized_order = [k for k in standardized.keys() if k in ALL_FIELDS]
        if original_order != standardized_order:
            report['fields_reordered'] = True
        
        # Check for format changes
        for key in original_keys & standardized_keys:
            if original[key] != standardized[key]:
                # Check if it's a format fix
                if isinstance(original[key], str) and isinstance(standardized[key], list):
                    report['format_fixed'].append(f"{key}: str -> list")
                elif isinstance(original[key], (list, str)) and isinstance(standardized[key], dict):
                    report['format_fixed'].append(f"{key}: {type(original[key]).__name__} -> dict")
                else:
                    report['fields_modified'].append(key)
        
        return report


# Convenience function
def get_field_standardizer() -> FieldStandardizer:
    """Lấy FieldStandardizer instance"""
    return FieldStandardizer()


if __name__ == "__main__":
    # Test
    standardizer = get_field_standardizer()
    
    test_drug = {
        "group": "Test Group",
        "vietnamese_name": "Test Drug",
        "administration": "PO",  # Should be list
        "indications": "Test",  # Should be list
        "dosage": {"adult": "100mg"},
    }
    
    standardized = standardizer.standardize_drug(test_drug, include_additional=False)
    print(f"Standardized: {standardized}")
    
    report = standardizer.generate_change_report(test_drug, standardized)
    print(f"Change report: {report}")

