"""
Công cụ quản lý thuốc
Tìm file chứa thuốc, gợi ý nơi đặt thuốc mới, kiểm tra trùng lặp, validate
"""
import ast
import json
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any
from collections import defaultdict
import unicodedata

from .drug_index_system import DrugIndex

class DrugManager:
    """Công cụ quản lý thuốc"""
    
    def __init__(self):
        """Khởi tạo DrugManager"""
        self.index = DrugIndex()
        self.drug_locations: Dict[str, List[str]] = defaultdict(list)
        self._build_location_index()
    
    def _normalize_text(self, text: str) -> str:
        """Chuẩn hóa text"""
        if not text:
            return ""
        text = unicodedata.normalize('NFD', text)
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        return text.lower().strip()
    
    def _build_location_index(self):
        """Xây dựng index vị trí file"""
        for drug_name, drug_info in self.index.drugs.items():
            file_path = drug_info.get('file', '')
            if file_path:
                self.drug_locations[drug_name].append(file_path)
    
    def find_drug_file(self, drug_name: str) -> Optional[List[str]]:
        """
        Tìm file chứa thuốc
        
        Args:
            drug_name: Tên thuốc
        
        Returns:
            Danh sách đường dẫn file hoặc None
        """
        # Tìm exact match
        if drug_name in self.drug_locations:
            return self.drug_locations[drug_name]
        
        # Tìm fuzzy match
        normalized_query = self._normalize_text(drug_name)
        results = []
        
        for name, files in self.drug_locations.items():
            normalized_name = self._normalize_text(name)
            if normalized_query in normalized_name or normalized_name in normalized_query:
                results.extend(files)
        
        return results if results else None
    
    def suggest_placement(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Gợi ý nơi đặt thuốc mới
        
        Args:
            drug_data: Dữ liệu thuốc mới (cần có 'group' hoặc 'indications')
        
        Returns:
            Dict chứa gợi ý: module, file, category
        """
        suggestion = {
            'module': 'miscellaneous',
            'file': 'miscellaneous.py',
            'category': 'other',
            'confidence': 'low',
            'reason': 'No specific group or indication found'
        }
        
        # Phân tích group
        group = drug_data.get('group', '').lower()
        if group:
            # Map group to module
            module_mapping = {
                'cardiovascular': 'cardiovascular',
                'cardiac': 'cardiovascular',
                'hypertension': 'cardiovascular',
                'heart': 'cardiovascular',
                'diabetes': 'diabetes',
                'diabetic': 'diabetes',
                'antimicrobial': 'antimicrobial',
                'antibiotic': 'antimicrobial',
                'antifungal': 'antimicrobial',
                'antiviral': 'antimicrobial',
                'analgesic': 'analgesics',
                'pain': 'analgesics',
                'respiratory': 'respiratory',
                'asthma': 'respiratory',
                'copd': 'respiratory',
                'neurological': 'neurological',
                'neurology': 'neurological',
                'seizure': 'neurological',
                'epilepsy': 'neurological',
                'oncology': 'oncology',
                'cancer': 'oncology',
                'chemotherapy': 'oncology',
                'gastrointestinal': 'gastrointestinal',
                'gi': 'gastrointestinal',
                'hematology': 'hematology',
                'blood': 'hematology',
                'anticoagulant': 'hematology',
                'dermatology': 'dermatology',
                'skin': 'dermatology',
                'topical': 'dermatology',
                'ophthalmology': 'ophthalmology',
                'eye': 'ophthalmology',
                'urology': 'urology',
                'obstetrics': 'obstetrics_gynecology',
                'gynecology': 'obstetrics_gynecology',
                'contraceptive': 'obstetrics_gynecology',
                'hormone': 'obstetrics_gynecology',
                'emergency': 'emergency',
                'icu': 'emergency',
                'supportive': 'supportive',
            }
            
            for keyword, module in module_mapping.items():
                if keyword in group:
                    suggestion['module'] = module
                    suggestion['confidence'] = 'high'
                    suggestion['reason'] = f"Group contains '{keyword}'"
                    break
        
        # Phân tích indications
        indications = drug_data.get('indications', [])
        if isinstance(indications, list):
            indication_text = ' '.join(str(ind) for ind in indications).lower()
            
            indication_mapping = {
                'diabetes': 'diabetes',
                'hypertension': 'cardiovascular',
                'infection': 'antimicrobial',
                'pain': 'analgesics',
                'asthma': 'respiratory',
                'seizure': 'neurological',
                'cancer': 'oncology',
            }
            
            for keyword, module in indication_mapping.items():
                if keyword in indication_text and suggestion['confidence'] == 'low':
                    suggestion['module'] = module
                    suggestion['confidence'] = 'medium'
                    suggestion['reason'] = f"Indication contains '{keyword}'"
                    break
        
        # Xác định file cụ thể trong module
        module_path = Path(f"drugs/drug_modules/{suggestion['module']}")
        if module_path.is_dir():
            # Module có subfolder
            suggestion['file'] = f"{suggestion['module']}/other_{suggestion['module']}.py"
        else:
            # Module là file đơn
            suggestion['file'] = f"{suggestion['module']}.py"
        
        return suggestion
    
    def find_duplicates(self) -> Dict[str, List[str]]:
        """
        Tìm thuốc trùng lặp (cùng tên nhưng ở file khác)
        
        Returns:
            Dict: {drug_name: [file_paths]}
        """
        duplicates = {}
        
        for drug_name, files in self.drug_locations.items():
            if len(files) > 1:
                # Kiểm tra xem có phải là cùng một thuốc không
                unique_files = list(set(files))
                if len(unique_files) > 1:
                    duplicates[drug_name] = unique_files
        
        return duplicates
    
    def validate_drug_structure(self, drug_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate cấu trúc thuốc
        
        Args:
            drug_data: Dữ liệu thuốc
        
        Returns:
            Dict chứa kết quả validation
        """
        result = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'missing_fields': [],
            'extra_fields': [],
        }
        
        # 14 field chuẩn
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
        
        ALL_FIELDS = STANDARD_14_FIELDS + ADDITIONAL_8_FIELDS
        
        # Kiểm tra field bắt buộc
        required_fields = ["group", "vietnamese_name", "administration", "indications"]
        for field in required_fields:
            if field not in drug_data:
                result['valid'] = False
                result['errors'].append(f"Missing required field: {field}")
                result['missing_fields'].append(field)
        
        # Kiểm tra field chuẩn
        for field in STANDARD_14_FIELDS:
            if field not in drug_data:
                result['warnings'].append(f"Missing standard field: {field}")
                result['missing_fields'].append(field)
        
        # Kiểm tra field không hợp lệ
        known_fields = set(ALL_FIELDS) | {
            'risk_flags', 'organ_toxicity', 'pediatric_dosing', 'geriatric_dosing',
            'brand_names', 'cost_estimate', 'contraindications_detail', 'renal_adjustment',
            'last_updated', 'evidence_level', 'analysis', 'drug_interactions_detail'
        }
        
        for field in drug_data.keys():
            if field not in known_fields:
                result['warnings'].append(f"Unknown field: {field}")
                result['extra_fields'].append(field)
        
        # Kiểm tra kiểu dữ liệu
        if 'administration' in drug_data:
            if not isinstance(drug_data['administration'], list):
                result['warnings'].append("'administration' should be a list")
        
        if 'indications' in drug_data:
            if not isinstance(drug_data['indications'], list):
                result['warnings'].append("'indications' should be a list")
        
        return result
    
    def check_drug_exists(self, drug_name: str) -> bool:
        """
        Kiểm tra thuốc đã tồn tại chưa
        
        Args:
            drug_name: Tên thuốc
        
        Returns:
            True nếu đã tồn tại
        """
        return drug_name in self.index.drugs
    
    def get_drug_module(self, drug_name: str) -> Optional[str]:
        """
        Lấy module của thuốc
        
        Args:
            drug_name: Tên thuốc
        
        Returns:
            Tên module hoặc None
        """
        drug_info = self.index.get_drug_info(drug_name)
        if drug_info:
            return drug_info.get('module')
        return None
    
    def export_drug(self, drug_name: str, format: str = 'json') -> Optional[str]:
        """
        Export thuốc ra file
        
        Args:
            drug_name: Tên thuốc
            format: Format export ('json' hoặc 'python')
        
        Returns:
            Nội dung export hoặc None
        """
        drug_info = self.index.get_drug_info(drug_name)
        if not drug_info:
            return None
        
        if format == 'json':
            return json.dumps({drug_name: drug_info}, indent=2, ensure_ascii=False)
        elif format == 'python':
            # Format Python dict
            lines = [f'    "{drug_name}": {{']
            for key, value in drug_info.items():
                if isinstance(value, str):
                    lines.append(f'        "{key}": {json.dumps(value, ensure_ascii=False)},')
                elif isinstance(value, list):
                    lines.append(f'        "{key}": {json.dumps(value, ensure_ascii=False)},')
                else:
                    lines.append(f'        "{key}": {json.dumps(value, ensure_ascii=False)},')
            lines.append('    },')
            return '\n'.join(lines)
        
        return None
    
    def import_drug(self, drug_data: Dict[str, Any], target_file: Optional[str] = None) -> Dict[str, Any]:
        """
        Import thuốc vào hệ thống (gợi ý)
        
        Args:
            drug_data: Dữ liệu thuốc
            target_file: File đích (nếu None sẽ gợi ý)
        
        Returns:
            Dict chứa thông tin import
        """
        result = {
            'success': False,
            'suggested_file': None,
            'validation': None,
            'duplicate_check': None,
        }
        
        # Validate
        validation = self.validate_drug_structure(drug_data)
        result['validation'] = validation
        
        if not validation['valid']:
            result['message'] = 'Drug structure is invalid'
            return result
        
        # Kiểm tra trùng lặp
        drug_name = None
        for key in drug_data.keys():
            if key and not key.startswith('_'):
                drug_name = key
                break
        
        if drug_name:
            if self.check_drug_exists(drug_name):
                result['duplicate_check'] = {
                    'exists': True,
                    'locations': self.find_drug_file(drug_name)
                }
                result['message'] = f'Drug "{drug_name}" already exists'
                return result
        
        # Gợi ý file
        if not target_file:
            suggestion = self.suggest_placement(drug_data)
            result['suggested_file'] = suggestion['file']
            result['suggested_module'] = suggestion['module']
            result['confidence'] = suggestion['confidence']
        else:
            result['suggested_file'] = target_file
        
        result['success'] = True
        result['message'] = 'Ready to import'
        
        return result


# Convenience function
def get_drug_manager() -> DrugManager:
    """Lấy DrugManager instance"""
    return DrugManager()


if __name__ == "__main__":
    # Test
    manager = get_drug_manager()
    
    # Test find file
    files = manager.find_drug_file("Metformin")
    print(f"Metformin files: {files}")
    
    # Test suggest placement
    new_drug = {
        "group": "Cardiovascular - ACE Inhibitor",
        "indications": ["Hypertension", "Heart failure"]
    }
    suggestion = manager.suggest_placement(new_drug)
    print(f"Suggestion: {suggestion}")
    
    # Test duplicates
    duplicates = manager.find_duplicates()
    print(f"Duplicates: {len(duplicates)}")

