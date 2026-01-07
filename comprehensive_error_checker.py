#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Error Checker - Kiểm tra lỗi toàn diện cho ứng dụng y tế
Tìm và báo cáo tất cả các loại lỗi: syntax, import, cấu trúc dữ liệu, validation, type checking, chất lượng dữ liệu

Author: Clinical IT Team
Version: 1.0.0
Date: 2025-02-18
"""

import ast
import sys
import json
import importlib
import traceback
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional, Set
from collections import defaultdict
from datetime import datetime
import re

# Field definitions
REQUIRED_BASIC_FIELDS = [
    "group", "vietnamese_name", "administration", "indications", "dosage",
    "side_effects", "contraindications", "interactions", "pregnancy"
]

ENHANCED_FIELDS = [
    "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics",
    "storage", "black_box_warnings", "drug_interactions", "contraindications_detail",
    "pregnancy_lactation", "hepatic_adjustment", "renal_adjustment",
    "overdose_management", "reversal_agents", "administration_instructions"
]

FIELD_TYPES = {
    "group": str,
    "vietnamese_name": str,
    "administration": list,
    "indications": list,
    "dosage": (dict, str),
    "side_effects": list,
    "contraindications": (list, dict),
    "interactions": list,
    "pregnancy": str,
    "risk_flags": dict,
    "guideline_tags": list,
    "monitoring": list,
    "precautions": (list, dict),
    "pharmacokinetics": dict,
    "storage": str,
    "black_box_warnings": (str, type(None)),
    "drug_interactions": dict,
    "pregnancy_lactation": dict,
    "hepatic_adjustment": dict,
    "renal_adjustment": dict,
    "overdose_management": dict,
    "reversal_agents": (dict, type(None)),
    "administration_instructions": dict,
}


class ComprehensiveErrorChecker:
    """Class để kiểm tra lỗi toàn diện cho ứng dụng"""
    
    def __init__(self, base_path: Optional[Path] = None):
        """
        Khởi tạo checker
        
        Args:
            base_path: Đường dẫn gốc của project (mặc định: current directory)
        """
        self.base_path = base_path or Path.cwd()
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        self.info = defaultdict(list)
        self.stats = {
            "total_files_checked": 0,
            "total_drugs_checked": 0,
            "syntax_errors": 0,
            "import_errors": 0,
            "structure_errors": 0,
            "field_errors": 0,
            "type_errors": 0,
            "quality_issues": 0,
            "file_structure_errors": 0,
            "config_errors": 0,
        }
        self.report_data = {
            "timestamp": datetime.now().isoformat(),
            "summary": {},
            "errors": {},
            "warnings": {},
            "info": {},
        }
    
    def is_field_empty(self, value: Any) -> bool:
        """Kiểm tra field có rỗng không"""
        if value is None:
            return True
        if isinstance(value, str):
            return not value.strip()
        try:
            return len(value) == 0
        except TypeError:
            return False
    
    def check_syntax_errors(self) -> List[Dict]:
        """
        Kiểm tra lỗi syntax trong tất cả file Python
        
        Returns:
            List các lỗi syntax tìm được
        """
        print("=" * 70)
        print("1. KIỂM TRA SYNTAX ERRORS")
        print("=" * 70)
        
        errors = []
        paths_to_check = [
            self.base_path / "drugs" / "drug_modules",
            self.base_path / "pages",
            self.base_path / "components",
            self.base_path / "config",
            self.base_path / "utils",
        ]
        
        for base_dir in paths_to_check:
            if not base_dir.exists():
                continue
            
            for py_file in sorted(base_dir.rglob("*.py")):
                # Skip backup files và __pycache__
                if (py_file.name.endswith(".backup") or 
                    "__pycache__" in str(py_file) or
                    py_file.name.startswith(".")):
                    continue
                
                self.stats["total_files_checked"] += 1
                
                try:
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    ast.parse(content)
                except SyntaxError as e:
                    error_info = {
                        'file': str(py_file.relative_to(self.base_path)),
                        'type': 'syntax',
                        'line': e.lineno,
                        'column': e.offset,
                        'message': e.msg,
                        'text': e.text.strip() if e.text else None,
                    }
                    errors.append(error_info)
                    self.errors['syntax'].append(error_info)
                    self.stats["syntax_errors"] += 1
                except Exception as e:
                    error_info = {
                        'file': str(py_file.relative_to(self.base_path)),
                        'type': 'syntax_read_error',
                        'message': str(e),
                    }
                    errors.append(error_info)
                    self.errors['syntax'].append(error_info)
                    self.stats["syntax_errors"] += 1
        
        if errors:
            print(f"\n[LỖI] Tìm thấy {len(errors)} file có lỗi syntax:")
            for err in errors[:10]:  # Hiển thị 10 lỗi đầu tiên
                print(f"  - {err['file']}: Line {err.get('line', '?')} - {err['message']}")
            if len(errors) > 10:
                print(f"  ... và {len(errors) - 10} lỗi khác")
        else:
            print("\n[OK] Không có lỗi syntax nào")
        
        return errors
    
    def check_import_errors(self) -> List[Dict]:
        """
        Kiểm tra lỗi import trong các modules chính
        
        Returns:
            List các lỗi import tìm được
        """
        print("\n" + "=" * 70)
        print("2. KIỂM TRA IMPORT ERRORS")
        print("=" * 70)
        
        errors = []
        
        # Modules để kiểm tra
        modules_to_check = [
            # Main modules
            'drugs.drug_database',
            'drugs.drug_modules',
            # Drug module categories
            'drugs.drug_modules.cardiovascular',
            'drugs.drug_modules.diabetes',
            'drugs.drug_modules.gastrointestinal',
            'drugs.drug_modules.analgesics',
            'drugs.drug_modules.respiratory',
            'drugs.drug_modules.neurological',
            'drugs.drug_modules.hematology',
            'drugs.drug_modules.supportive',
            'drugs.drug_modules.antimicrobial',
            'drugs.drug_modules.metabolic',
            'drugs.drug_modules.endocrinology',
            'drugs.drug_modules.oncology',
            'drugs.drug_modules.emergency',
            'drugs.drug_modules.urology',
            'drugs.drug_modules.dermatology',
            'drugs.drug_modules.ophthalmology',
            'drugs.drug_modules.obstetrics_gynecology',
            'drugs.drug_modules.ent_oral_nasal_combinations',
            'drugs.drug_modules.miscellaneous',
            'drugs.drug_modules.anesthesia',
            'drugs.drug_modules.allergy',
            'drugs.drug_modules.nutrition',
            'drugs.drug_modules.toxicology',
            'drugs.drug_modules.vaccines',
            'drugs.drug_modules.immunology',
            'drugs.drug_modules.rheumatology',
            'drugs.drug_modules.psychiatry',
            # Config modules
            'config.app_config',
            'config.navigation_config',
            # Utils
            'utils.cache_helpers',
        ]
        
        sys.path.insert(0, str(self.base_path))
        
        for module_name in modules_to_check:
            try:
                importlib.import_module(module_name)
            except ImportError as e:
                error_info = {
                    'module': module_name,
                    'type': 'import',
                    'message': str(e),
                }
                errors.append(error_info)
                self.errors['import'].append(error_info)
                self.stats["import_errors"] += 1
            except SyntaxError as e:
                error_info = {
                    'module': module_name,
                    'type': 'import_syntax',
                    'line': e.lineno,
                    'message': e.msg,
                }
                errors.append(error_info)
                self.errors['import'].append(error_info)
                self.stats["import_errors"] += 1
            except Exception as e:
                error_info = {
                    'module': module_name,
                    'type': 'import_error',
                    'message': str(e),
                    'traceback': traceback.format_exc(),
                }
                errors.append(error_info)
                self.errors['import'].append(error_info)
                self.stats["import_errors"] += 1
        
        if errors:
            print(f"\n[LỖI] Tìm thấy {len(errors)} lỗi import:")
            for err in errors[:10]:
                print(f"  - {err['module']}: {err['message']}")
            if len(errors) > 10:
                print(f"  ... và {len(errors) - 10} lỗi khác")
        else:
            print("\n[OK] Tất cả các module import thành công")
        
        return errors
    
    def check_drug_database_structure(self) -> List[Dict]:
        """
        Kiểm tra cấu trúc DRUG_DATABASE
        
        Returns:
            List các lỗi cấu trúc tìm được
        """
        print("\n" + "=" * 70)
        print("3. KIỂM TRA CẤU TRÚC DRUG DATABASE")
        print("=" * 70)
        
        errors = []
        
        try:
            sys.path.insert(0, str(self.base_path))
            from drugs.drug_database import DRUG_DATABASE
            
            if not DRUG_DATABASE:
                error_info = {
                    'type': 'structure',
                    'message': 'DRUG_DATABASE is empty',
                }
                errors.append(error_info)
                self.errors['structure'].append(error_info)
                self.stats["structure_errors"] += 1
            else:
                drug_count = len(DRUG_DATABASE)
                self.stats["total_drugs_checked"] = drug_count
                print(f"\n[OK] DRUG_DATABASE có {drug_count} thuốc")
                
                # Kiểm tra duplicate keys
                seen_keys = set()
                duplicates = []
                for drug_name in DRUG_DATABASE.keys():
                    if drug_name in seen_keys:
                        duplicates.append(drug_name)
                    else:
                        seen_keys.add(drug_name)
                
                if duplicates:
                    error_info = {
                        'type': 'duplicate_keys',
                        'message': f'Found {len(duplicates)} duplicate drug keys',
                        'duplicates': duplicates[:10],
                    }
                    errors.append(error_info)
                    self.errors['structure'].append(error_info)
                    self.stats["structure_errors"] += 1
                    print(f"\n[LỖI] Tìm thấy {len(duplicates)} thuốc trùng key")
                
                # Kiểm tra cấu trúc dictionary hợp lệ
                invalid_structure = []
                for drug_name, drug_data in list(DRUG_DATABASE.items())[:100]:  # Check first 100
                    if not isinstance(drug_data, dict):
                        invalid_structure.append(drug_name)
                
                if invalid_structure:
                    error_info = {
                        'type': 'invalid_structure',
                        'message': f'Found {len(invalid_structure)} drugs with invalid structure',
                        'drugs': invalid_structure[:10],
                    }
                    errors.append(error_info)
                    self.errors['structure'].append(error_info)
                    self.stats["structure_errors"] += 1
                    print(f"\n[LỖI] Tìm thấy {len(invalid_structure)} thuốc có cấu trúc không hợp lệ")
        
        except ImportError as e:
            error_info = {
                'type': 'import',
                'message': f'Cannot import DRUG_DATABASE: {e}',
            }
            errors.append(error_info)
            self.errors['structure'].append(error_info)
            self.stats["structure_errors"] += 1
        except Exception as e:
            error_info = {
                'type': 'structure',
                'message': f'Error checking database structure: {e}',
                'traceback': traceback.format_exc(),
            }
            errors.append(error_info)
            self.errors['structure'].append(error_info)
            self.stats["structure_errors"] += 1
        
        if not errors:
            print("\n[OK] Cấu trúc database hợp lệ")
        
        return errors
    
    def validate_drug_fields(self) -> Dict[str, Any]:
        """
        Kiểm tra và validate các fields của thuốc
        
        Returns:
            Dict chứa kết quả validation
        """
        print("\n" + "=" * 70)
        print("4. KIỂM TRA VALIDATION FIELDS")
        print("=" * 70)
        
        results = {
            'missing_basic_fields': [],
            'missing_enhanced_fields': [],
            'empty_fields': [],
            'field_stats': defaultdict(int),
        }
        
        try:
            sys.path.insert(0, str(self.base_path))
            from drugs.drug_database import DRUG_DATABASE
            
            for drug_name, drug_data in DRUG_DATABASE.items():
                if not isinstance(drug_data, dict):
                    continue
                
                # Kiểm tra basic fields
                for field in REQUIRED_BASIC_FIELDS:
                    if field not in drug_data:
                        results['missing_basic_fields'].append({
                            'drug': drug_name,
                            'field': field,
                        })
                        self.errors['field'].append({
                            'drug': drug_name,
                            'type': 'missing_basic_field',
                            'field': field,
                        })
                        self.stats["field_errors"] += 1
                    elif self.is_field_empty(drug_data[field]):
                        results['empty_fields'].append({
                            'drug': drug_name,
                            'field': field,
                        })
                        self.errors['field'].append({
                            'drug': drug_name,
                            'type': 'empty_field',
                            'field': field,
                        })
                        self.stats["field_errors"] += 1
                    else:
                        results['field_stats'][field] += 1
                
                # Kiểm tra enhanced fields
                for field in ENHANCED_FIELDS:
                    value = drug_data.get(field)
                    if value is None:
                        results['missing_enhanced_fields'].append({
                            'drug': drug_name,
                            'field': field,
                        })
                        self.warnings['field'].append({
                            'drug': drug_name,
                            'type': 'missing_enhanced_field',
                            'field': field,
                        })
                    elif self.is_field_empty(value):
                        results['empty_fields'].append({
                            'drug': drug_name,
                            'field': field,
                        })
                        self.warnings['field'].append({
                            'drug': drug_name,
                            'type': 'empty_enhanced_field',
                            'field': field,
                        })
                    else:
                        results['field_stats'][field] += 1
            
            # Báo cáo
            if results['missing_basic_fields']:
                print(f"\n[LỖI] Tìm thấy {len(results['missing_basic_fields'])} thuốc thiếu basic fields")
                for item in results['missing_basic_fields'][:5]:
                    print(f"  - {item['drug']}: thiếu '{item['field']}'")
                if len(results['missing_basic_fields']) > 5:
                    print(f"  ... và {len(results['missing_basic_fields']) - 5} lỗi khác")
            
            if results['missing_enhanced_fields']:
                print(f"\n[WARNING] Tìm thấy {len(results['missing_enhanced_fields'])} thuốc thiếu enhanced fields")
            
            if results['empty_fields']:
                print(f"\n[WARNING] Tìm thấy {len(results['empty_fields'])} thuốc có fields rỗng")
            
            if not results['missing_basic_fields']:
                print("\n[OK] Tất cả thuốc đều có đủ basic fields")
        
        except Exception as e:
            error_info = {
                'type': 'validation_error',
                'message': f'Error validating fields: {e}',
                'traceback': traceback.format_exc(),
            }
            self.errors['field'].append(error_info)
            self.stats["field_errors"] += 1
            print(f"\n[LỖI] Lỗi khi validate fields: {e}")
        
        return results
    
    def check_data_types(self) -> List[Dict]:
        """
        Kiểm tra kiểu dữ liệu của các fields
        
        Returns:
            List các lỗi type tìm được
        """
        print("\n" + "=" * 70)
        print("5. KIỂM TRA DATA TYPES")
        print("=" * 70)
        
        errors = []
        
        try:
            sys.path.insert(0, str(self.base_path))
            from drugs.drug_database import DRUG_DATABASE
            
            for drug_name, drug_data in DRUG_DATABASE.items():
                if not isinstance(drug_data, dict):
                    continue
                
                for field, expected_type in FIELD_TYPES.items():
                    value = drug_data.get(field)
                    if value is None:
                        continue  # Skip missing fields (đã check ở validate_drug_fields)
                    
                    if isinstance(expected_type, tuple):
                        if not any(isinstance(value, t) for t in expected_type):
                            error_info = {
                                'drug': drug_name,
                                'field': field,
                                'expected': [t.__name__ if hasattr(t, '__name__') else str(t) for t in expected_type],
                                'got': type(value).__name__,
                            }
                            errors.append(error_info)
                            self.errors['type'].append(error_info)
                            self.stats["type_errors"] += 1
                    else:
                        if not isinstance(value, expected_type):
                            error_info = {
                                'drug': drug_name,
                                'field': field,
                                'expected': expected_type.__name__,
                                'got': type(value).__name__,
                            }
                            errors.append(error_info)
                            self.errors['type'].append(error_info)
                            self.stats["type_errors"] += 1
            
            if errors:
                print(f"\n[LỖI] Tìm thấy {len(errors)} lỗi type:")
                for err in errors[:10]:
                    print(f"  - {err['drug']}.{err['field']}: mong đợi {err['expected']}, nhận được {err['got']}")
                if len(errors) > 10:
                    print(f"  ... và {len(errors) - 10} lỗi khác")
            else:
                print("\n[OK] Tất cả fields đều có kiểu dữ liệu đúng")
        
        except Exception as e:
            error_info = {
                'type': 'type_check_error',
                'message': f'Error checking types: {e}',
                'traceback': traceback.format_exc(),
            }
            errors.append(error_info)
            self.errors['type'].append(error_info)
            self.stats["type_errors"] += 1
            print(f"\n[LỖI] Lỗi khi check types: {e}")
        
        return errors
    
    def check_data_quality(self) -> List[Dict]:
        """
        Kiểm tra chất lượng dữ liệu: duplicates, empty values, invalid formats
        
        Returns:
            List các vấn đề chất lượng tìm được
        """
        print("\n" + "=" * 70)
        print("6. KIỂM TRA CHẤT LƯỢNG DỮ LIỆU")
        print("=" * 70)
        
        issues = []
        
        try:
            sys.path.insert(0, str(self.base_path))
            from drugs.drug_database import DRUG_DATABASE
            
            # Kiểm tra thuốc trùng lặp (theo key fields)
            seen_drugs = {}
            duplicates = []
            
            for drug_name, drug_data in DRUG_DATABASE.items():
                if not isinstance(drug_data, dict):
                    continue
                
                # Tạo signature từ key fields
                key_fields = (
                    drug_data.get('group', ''),
                    drug_data.get('vietnamese_name', ''),
                    str(drug_data.get('administration', [])),
                )
                
                if key_fields in seen_drugs:
                    duplicates.append({
                        'drug1': seen_drugs[key_fields],
                        'drug2': drug_name,
                        'key_fields': key_fields,
                    })
                else:
                    seen_drugs[key_fields] = drug_name
            
            if duplicates:
                for dup in duplicates:
                    issue_info = {
                        'type': 'duplicate_drug',
                        'drug1': dup['drug1'],
                        'drug2': dup['drug2'],
                    }
                    issues.append(issue_info)
                    self.warnings['quality'].append(issue_info)
                    self.stats["quality_issues"] += 1
                print(f"\n[WARNING] Tìm thấy {len(duplicates)} cặp thuốc có thể trùng lặp")
                for dup in duplicates[:5]:
                    print(f"  - {dup['drug1']} và {dup['drug2']}")
            
            # Kiểm tra Vietnamese capitalization
            vietnamese_caps_issues = []
            for drug_name, drug_data in DRUG_DATABASE.items():
                if not isinstance(drug_data, dict):
                    continue
                
                vietnamese_name = drug_data.get('vietnamese_name', '')
                if isinstance(vietnamese_name, str) and vietnamese_name:
                    # Kiểm tra chữ cái đầu tiên của từ phải viết hoa
                    words = vietnamese_name.split()
                    for word in words:
                        if word and word[0].islower() and word[0].isalpha():
                            vietnamese_caps_issues.append({
                                'drug': drug_name,
                                'word': word,
                            })
                            break
            
            if vietnamese_caps_issues:
                print(f"\n[WARNING] Tìm thấy {len(vietnamese_caps_issues)} thuốc có vấn đề về capitalization")
                for issue in vietnamese_caps_issues[:5]:
                    print(f"  - {issue['drug']}: từ '{issue['word']}'")
            
            if not issues and not vietnamese_caps_issues:
                print("\n[OK] Chất lượng dữ liệu tốt")
        
        except Exception as e:
            issue_info = {
                'type': 'quality_check_error',
                'message': f'Error checking quality: {e}',
                'traceback': traceback.format_exc(),
            }
            issues.append(issue_info)
            self.errors['quality'].append(issue_info)
            self.stats["quality_issues"] += 1
            print(f"\n[LỖI] Lỗi khi check quality: {e}")
        
        return issues
    
    def check_file_structure(self) -> List[Dict]:
        """
        Kiểm tra cấu trúc file: __init__.py, file paths, naming conventions
        
        Returns:
            List các lỗi cấu trúc file tìm được
        """
        print("\n" + "=" * 70)
        print("7. KIỂM TRA CẤU TRÚC FILE")
        print("=" * 70)
        
        errors = []
        
        # Kiểm tra __init__.py trong các packages
        required_init_files = [
            "drugs/drug_modules/__init__.py",
            "drugs/drug_modules/cardiovascular/__init__.py",
            "drugs/drug_modules/diabetes/__init__.py",
            "drugs/drug_modules/gastrointestinal/__init__.py",
            "drugs/drug_modules/analgesics/__init__.py",
            "drugs/drug_modules/respiratory/__init__.py",
            "drugs/drug_modules/neurological/__init__.py",
            "drugs/drug_modules/hematology/__init__.py",
            "drugs/drug_modules/supportive/__init__.py",
            "drugs/drug_modules/antimicrobial/__init__.py",
            "drugs/drug_modules/metabolic/__init__.py",
            "drugs/drug_modules/endocrinology/__init__.py",
            "drugs/drug_modules/oncology/__init__.py",
            "drugs/drug_modules/emergency/__init__.py",
            "drugs/drug_modules/urology/__init__.py",
            "drugs/drug_modules/dermatology/__init__.py",
            "drugs/drug_modules/ophthalmology/__init__.py",
            "drugs/drug_modules/obstetrics_gynecology/__init__.py",
            "drugs/drug_modules/ent_oral_nasal_combinations/__init__.py",
            "drugs/drug_modules/miscellaneous/__init__.py",
            "drugs/drug_modules/anesthesia/__init__.py",
            "drugs/drug_modules/allergy/__init__.py",
            "drugs/drug_modules/nutrition/__init__.py",
            "drugs/drug_modules/toxicology/__init__.py",
            "drugs/drug_modules/vaccines/__init__.py",
            "drugs/drug_modules/immunology/__init__.py",
            "drugs/drug_modules/rheumatology/__init__.py",
            "drugs/drug_modules/psychiatry/__init__.py",
        ]
        
        missing_files = []
        for file_path in required_init_files:
            full_path = self.base_path / file_path
            if not full_path.exists():
                missing_files.append(file_path)
                error_info = {
                    'type': 'missing_init_file',
                    'file': file_path,
                }
                errors.append(error_info)
                self.errors['file_structure'].append(error_info)
                self.stats["file_structure_errors"] += 1
        
        if missing_files:
            print(f"\n[LỖI] Thiếu {len(missing_files)} file __init__.py:")
            for f in missing_files[:10]:
                print(f"  - {f}")
            if len(missing_files) > 10:
                print(f"  ... và {len(missing_files) - 10} file khác")
        else:
            print("\n[OK] Tất cả các file __init__.py đều tồn tại")
        
        return errors
    
    def check_configuration(self) -> List[Dict]:
        """
        Kiểm tra các file cấu hình
        
        Returns:
            List các lỗi config tìm được
        """
        print("\n" + "=" * 70)
        print("8. KIỂM TRA CẤU HÌNH")
        print("=" * 70)
        
        errors = []
        
        # Kiểm tra app_config.py
        try:
            sys.path.insert(0, str(self.base_path))
            from config.app_config import APP_CONFIG
            
            # Kiểm tra các keys bắt buộc
            required_keys = ['version', 'last_updated', 'pages']
            for key in required_keys:
                if key not in APP_CONFIG:
                    error_info = {
                        'type': 'missing_config_key',
                        'config': 'app_config',
                        'key': key,
                    }
                    errors.append(error_info)
                    self.errors['config'].append(error_info)
                    self.stats["config_errors"] += 1
            
            # Kiểm tra page paths tồn tại
            if 'pages' in APP_CONFIG:
                missing_pages = []
                for page_id, page_info in APP_CONFIG['pages'].items():
                    if hasattr(page_info, 'page_path'):
                        page_path = self.base_path / page_info.page_path
                        if not page_path.exists():
                            missing_pages.append({
                                'page_id': page_id,
                                'path': page_info.page_path,
                            })
                            error_info = {
                                'type': 'missing_page_file',
                                'page_id': page_id,
                                'path': page_info.page_path,
                            }
                            errors.append(error_info)
                            self.errors['config'].append(error_info)
                            self.stats["config_errors"] += 1
                
                if missing_pages:
                    print(f"\n[LỖI] Tìm thấy {len(missing_pages)} page file không tồn tại")
                    for page in missing_pages[:5]:
                        print(f"  - {page['page_id']}: {page['path']}")
            
            print("\n[OK] Cấu hình hợp lệ")
        
        except ImportError as e:
            error_info = {
                'type': 'config_import_error',
                'config': 'app_config',
                'message': str(e),
            }
            errors.append(error_info)
            self.errors['config'].append(error_info)
            self.stats["config_errors"] += 1
            print(f"\n[LỖI] Không thể import app_config: {e}")
        except Exception as e:
            error_info = {
                'type': 'config_error',
                'message': str(e),
                'traceback': traceback.format_exc(),
            }
            errors.append(error_info)
            self.errors['config'].append(error_info)
            self.stats["config_errors"] += 1
            print(f"\n[LỖI] Lỗi khi check config: {e}")
        
        return errors
    
    def check_page_modules(self) -> List[Dict]:
        """
        Kiểm tra các page modules có thể import được
        
        Returns:
            List các lỗi page modules tìm được
        """
        print("\n" + "=" * 70)
        print("9. KIỂM TRA PAGE MODULES")
        print("=" * 70)
        
        errors = []
        pages_dir = self.base_path / "pages"
        
        if not pages_dir.exists():
            print("\n[WARNING] Thư mục pages không tồn tại")
            return errors
        
        sys.path.insert(0, str(self.base_path))
        
        for page_file in sorted(pages_dir.glob("*.py")):
            if page_file.name.startswith("_"):
                continue  # Skip private files
            
            module_name = f"pages.{page_file.stem}"
            
            try:
                importlib.import_module(module_name)
            except Exception as e:
                error_info = {
                    'type': 'page_import_error',
                    'page': str(page_file.relative_to(self.base_path)),
                    'module': module_name,
                    'message': str(e),
                }
                errors.append(error_info)
                self.errors['pages'].append(error_info)
                self.stats["import_errors"] += 1
        
        if errors:
            print(f"\n[LỖI] Tìm thấy {len(errors)} page không thể import:")
            for err in errors[:10]:
                print(f"  - {err['page']}: {err['message']}")
        else:
            print("\n[OK] Tất cả pages đều có thể import được")
        
        return errors
    
    def check_components(self) -> List[Dict]:
        """
        Kiểm tra các components có thể import được
        
        Returns:
            List các lỗi components tìm được
        """
        print("\n" + "=" * 70)
        print("10. KIỂM TRA COMPONENTS")
        print("=" * 70)
        
        errors = []
        components_dir = self.base_path / "components"
        
        if not components_dir.exists():
            print("\n[WARNING] Thư mục components không tồn tại")
            return errors
        
        sys.path.insert(0, str(self.base_path))
        
        # Chỉ check một số components quan trọng
        important_components = [
            'components.search',
            'components.favorites',
            'components.recently_used',
            'components.sidebar_navigation',
            'components.drug_cards',
        ]
        
        for component_name in important_components:
            try:
                importlib.import_module(component_name)
            except Exception as e:
                error_info = {
                    'type': 'component_import_error',
                    'component': component_name,
                    'message': str(e),
                }
                errors.append(error_info)
                self.errors['components'].append(error_info)
                self.stats["import_errors"] += 1
        
        if errors:
            print(f"\n[LỖI] Tìm thấy {len(errors)} component không thể import:")
            for err in errors:
                print(f"  - {err['component']}: {err['message']}")
        else:
            print("\n[OK] Tất cả components quan trọng đều có thể import được")
        
        return errors
    
    def generate_report(self) -> Dict[str, Any]:
        """
        Tạo báo cáo tổng hợp
        
        Returns:
            Dict chứa báo cáo chi tiết
        """
        # Tổng hợp stats
        total_errors = sum(len(errors) for errors in self.errors.values())
        total_warnings = sum(len(warnings) for warnings in self.warnings.values())
        
        self.report_data['summary'] = {
            'timestamp': self.report_data['timestamp'],
            'total_files_checked': self.stats['total_files_checked'],
            'total_drugs_checked': self.stats['total_drugs_checked'],
            'total_errors': total_errors,
            'total_warnings': total_warnings,
            'stats': self.stats,
        }
        
        self.report_data['errors'] = dict(self.errors)
        self.report_data['warnings'] = dict(self.warnings)
        self.report_data['info'] = dict(self.info)
        
        return self.report_data
    
    def save_json_report(self, output_file: Optional[Path] = None) -> Path:
        """
        Lưu báo cáo ra file JSON
        
        Args:
            output_file: Đường dẫn file output (mặc định: error_report_TIMESTAMP.json)
        
        Returns:
            Path đến file đã lưu
        """
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.base_path / f"error_report_{timestamp}.json"
        
        report = self.generate_report()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False, default=str)
        
        return output_file
    
    def save_html_report(self, output_file: Optional[Path] = None) -> Path:
        """
        Lưu báo cáo ra file HTML
        
        Args:
            output_file: Đường dẫn file output (mặc định: error_report_TIMESTAMP.html)
        
        Returns:
            Path đến file đã lưu
        """
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.base_path / f"error_report_{timestamp}.html"
        
        report = self.generate_report()
        summary = report['summary']
        
        html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo Cáo Kiểm Tra Lỗi - {summary['timestamp']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .summary-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .summary-card.error {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }}
        .summary-card.warning {{
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            color: #333;
        }}
        .summary-card.success {{
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            color: #333;
        }}
        .summary-card h3 {{
            margin: 0 0 10px 0;
            font-size: 2em;
        }}
        .summary-card p {{
            margin: 0;
            font-size: 0.9em;
        }}
        .section {{
            margin: 30px 0;
        }}
        .section h2 {{
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 10px;
        }}
        .error-list {{
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 15px;
            margin: 10px 0;
        }}
        .error-item {{
            padding: 10px;
            margin: 5px 0;
            border-left: 3px solid #e74c3c;
            background: #fdf2f2;
        }}
        .warning-item {{
            padding: 10px;
            margin: 5px 0;
            border-left: 3px solid #f39c12;
            background: #fef9e7;
        }}
        .info-item {{
            padding: 10px;
            margin: 5px 0;
            border-left: 3px solid #3498db;
            background: #ebf5fb;
        }}
        .timestamp {{
            color: #7f8c8d;
            font-size: 0.9em;
            text-align: right;
            margin-top: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Báo Cáo Kiểm Tra Lỗi Toàn Diện</h1>
        <div class="timestamp">Thời gian: {summary['timestamp']}</div>
        
        <div class="summary">
            <div class="summary-card">
                <h3>{summary['total_files_checked']}</h3>
                <p>File đã kiểm tra</p>
            </div>
            <div class="summary-card">
                <h3>{summary['total_drugs_checked']}</h3>
                <p>Thuốc đã kiểm tra</p>
            </div>
            <div class="summary-card error">
                <h3>{summary['total_errors']}</h3>
                <p>Lỗi</p>
            </div>
            <div class="summary-card warning">
                <h3>{summary['total_warnings']}</h3>
                <p>Cảnh báo</p>
            </div>
        </div>
"""
        
        # Thêm phần errors
        if report['errors']:
            html_content += '<div class="section"><h2>❌ Lỗi</h2>\n'
            for error_type, errors_list in sorted(report['errors'].items()):
                if errors_list:
                    html_content += f'<h3>{error_type.replace("_", " ").title()} ({len(errors_list)} lỗi)</h3>\n'
                    html_content += '<div class="error-list">\n'
                    for err in errors_list[:20]:  # Hiển thị tối đa 20 lỗi mỗi loại
                        err_str = json.dumps(err, ensure_ascii=False, indent=2, default=str)
                        html_content += f'<div class="error-item"><pre>{err_str}</pre></div>\n'
                    if len(errors_list) > 20:
                        html_content += f'<p>... và {len(errors_list) - 20} lỗi khác</p>\n'
                    html_content += '</div>\n'
            html_content += '</div>\n'
        
        # Thêm phần warnings
        if report['warnings']:
            html_content += '<div class="section"><h2>⚠️ Cảnh Báo</h2>\n'
            for warning_type, warnings_list in sorted(report['warnings'].items()):
                if warnings_list:
                    html_content += f'<h3>{warning_type.replace("_", " ").title()} ({len(warnings_list)} cảnh báo)</h3>\n'
                    html_content += '<div class="error-list">\n'
                    for warn in warnings_list[:20]:
                        warn_str = json.dumps(warn, ensure_ascii=False, indent=2, default=str)
                        html_content += f'<div class="warning-item"><pre>{warn_str}</pre></div>\n'
                    if len(warnings_list) > 20:
                        html_content += f'<p>... và {len(warnings_list) - 20} cảnh báo khác</p>\n'
                    html_content += '</div>\n'
            html_content += '</div>\n'
        
        # Thêm stats table
        html_content += '<div class="section"><h2>📊 Thống Kê Chi Tiết</h2>\n'
        html_content += '<table>\n'
        html_content += '<tr><th>Loại</th><th>Số lượng</th></tr>\n'
        for stat_name, stat_value in sorted(summary['stats'].items()):
            html_content += f'<tr><td>{stat_name.replace("_", " ").title()}</td><td>{stat_value}</td></tr>\n'
        html_content += '</table>\n'
        html_content += '</div>\n'
        
        html_content += """
    </div>
</body>
</html>
"""
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return output_file
    
    def run_all_checks(self, skip_checks: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Chạy tất cả các kiểm tra
        
        Args:
            skip_checks: List các kiểm tra cần skip (ví dụ: ['syntax', 'import'])
        
        Returns:
            Dict chứa kết quả tất cả kiểm tra
        """
        skip_checks = skip_checks or []
        
        print("\n" + "=" * 70)
        print("KIỂM TRA LỖI TOÀN DIỆN")
        print("=" * 70)
        print(f"Thời gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Base path: {self.base_path}")
        print()
        
        results = {}
        
        # Chạy các kiểm tra
        if 'syntax' not in skip_checks:
            results['syntax'] = self.check_syntax_errors()
        
        if 'import' not in skip_checks:
            results['import'] = self.check_import_errors()
        
        if 'structure' not in skip_checks:
            results['structure'] = self.check_drug_database_structure()
        
        if 'fields' not in skip_checks:
            results['fields'] = self.validate_drug_fields()
        
        if 'types' not in skip_checks:
            results['types'] = self.check_data_types()
        
        if 'quality' not in skip_checks:
            results['quality'] = self.check_data_quality()
        
        if 'file_structure' not in skip_checks:
            results['file_structure'] = self.check_file_structure()
        
        if 'config' not in skip_checks:
            results['config'] = self.check_configuration()
        
        if 'pages' not in skip_checks:
            results['pages'] = self.check_page_modules()
        
        if 'components' not in skip_checks:
            results['components'] = self.check_components()
        
        # Tổng hợp và in summary
        print("\n" + "=" * 70)
        print("TỔNG HỢP")
        print("=" * 70)
        
        total_errors = sum(len(errors) for errors in self.errors.values())
        total_warnings = sum(len(warnings) for warnings in self.warnings.values())
        
        print(f"\nTổng số file đã kiểm tra: {self.stats['total_files_checked']}")
        print(f"Tổng số thuốc đã kiểm tra: {self.stats['total_drugs_checked']}")
        print(f"\nTổng số lỗi: {total_errors}")
        print(f"Tổng số cảnh báo: {total_warnings}")
        
        print("\nPhân loại lỗi:")
        for error_type, errors_list in sorted(self.errors.items()):
            if errors_list:
                print(f"  - {error_type}: {len(errors_list)} lỗi")
        
        if total_errors == 0 and total_warnings == 0:
            print("\n[OK] HỆ THỐNG KHÔNG CÓ LỖI NÀO!")
            print("  Tất cả các kiểm tra đều thành công.")
        else:
            print("\n[LỖI] Phát hiện lỗi trong hệ thống!")
            print("  Xem chi tiết ở trên hoặc trong file báo cáo JSON.")
        
        print("\n" + "=" * 70)
        
        return results


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Comprehensive Error Checker')
    parser.add_argument('--skip', nargs='+', help='Skip các kiểm tra (syntax, import, structure, fields, types, quality, file_structure, config, pages, components)')
    parser.add_argument('--output', type=str, help='Đường dẫn file output JSON')
    parser.add_argument('--base-path', type=str, help='Đường dẫn gốc của project')
    
    args = parser.parse_args()
    
    base_path = Path(args.base_path) if args.base_path else Path.cwd()
    checker = ComprehensiveErrorChecker(base_path=base_path)
    
    # Chạy tất cả kiểm tra
    results = checker.run_all_checks(skip_checks=args.skip)
    
    # Lưu báo cáo
    output_file = Path(args.output) if args.output else None
    json_file = checker.save_json_report(output_file)
    
    # Tạo HTML report với tên tương ứng
    if output_file:
        html_output = output_file.parent / (output_file.stem + ".html")
    else:
        html_output = None
    html_file = checker.save_html_report(html_output)
    
    print(f"\nBáo cáo JSON đã được lưu tại: {json_file}")
    print(f"Báo cáo HTML đã được lưu tại: {html_file}")


if __name__ == "__main__":
    main()
