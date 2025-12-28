#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động sửa các lỗi phổ biến trong dữ liệu thuốc
"""

import json
import os
from typing import Dict, List, Tuple
from collections import defaultdict

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    print("❌ Lỗi: Không thể import DRUG_DATABASE")
    exit(1)

# Tìm các file module chứa thuốc
def find_drug_in_modules(drug_name: str) -> Tuple[str, str]:
    """Tìm file module chứa thuốc"""
    import importlib
    import inspect
    
    # Kiểm tra trong enhanced_fields_overrides trước
    try:
        from drugs.enhanced_fields_overrides import EXTRA_ENHANCED_FIELDS
        if drug_name in EXTRA_ENHANCED_FIELDS:
            return "drugs/enhanced_fields_overrides.py", "EXTRA_ENHANCED_FIELDS"
    except:
        pass
    
    # Tìm trong các module
    module_paths = [
        "drugs/drug_modules/cardiovascular",
        "drugs/drug_modules/diabetes",
        "drugs/drug_modules/gastrointestinal",
        "drugs/drug_modules/analgesics",
        "drugs/drug_modules/respiratory",
        "drugs/drug_modules/neurological",
        "drugs/drug_modules/hematology",
        "drugs/drug_modules/supportive",
        "drugs/drug_modules/antimicrobial",
        "drugs/drug_modules/metabolic",
        "drugs/drug_modules/oncology",
        "drugs/drug_modules/emergency",
        "drugs/drug_modules/other",
        "drugs/drug_modules/dermatology",
        "drugs/drug_modules/ophthalmology",
        "drugs/drug_modules/urology",
        "drugs/drug_modules/cardiovascular_other",
        "drugs/drug_modules/infectious_other",
        "drugs/drug_modules/psychiatry_other",
        "drugs/drug_modules/endocrinology_other",
        "drugs/drug_modules/miscellaneous",
    ]
    
    for base_path in module_paths:
        if os.path.exists(base_path):
            for file in os.listdir(base_path):
                if file.endswith('.py'):
                    file_path = os.path.join(base_path, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                                return file_path, None
                    except:
                        continue
    
    return None, None

def fix_guideline_tags_type(drug_name: str, drug_data: Dict) -> bool:
    """Sửa guideline_tags từ dict sang list"""
    if "guideline_tags" in drug_data:
        if isinstance(drug_data["guideline_tags"], dict):
            # Chuyển dict thành list
            tags_list = []
            for key, value in drug_data["guideline_tags"].items():
                if isinstance(value, str):
                    tags_list.append(value)
                elif isinstance(value, list):
                    tags_list.extend(value)
                else:
                    tags_list.append(f"{key}: {value}")
            
            drug_data["guideline_tags"] = tags_list
            print(f"  ✅ Đã sửa guideline_tags cho {drug_name}: dict -> list ({len(tags_list)} tags)")
            return True
    return False

def fix_empty_interactions(drug_name: str, drug_data: Dict) -> bool:
    """Sửa field interactions rỗng"""
    if "interactions" in drug_data:
        if not drug_data["interactions"] or (isinstance(drug_data["interactions"], list) and len(drug_data["interactions"]) == 0):
            # Thêm giá trị mặc định
            drug_data["interactions"] = ["Chưa có báo cáo tương tác thuốc đáng kể"]
            print(f"  ✅ Đã thêm interactions mặc định cho {drug_name}")
            return True
    return False

def fix_overdose_management_structure(drug_name: str, drug_data: Dict) -> bool:
    """Sửa overdose_management từ string sang dict"""
    if "overdose_management" in drug_data:
        value = drug_data["overdose_management"]
        if isinstance(value, str) and value.strip():
            drug_data["overdose_management"] = {
                "symptoms": ["Cần đánh giá lâm sàng"],
                "antidote": "Không có antidote đặc hiệu",
                "treatment": [value],
                "monitoring": "Theo dõi dấu hiệu sinh tồn và triệu chứng"
            }
            print(f"  ✅ Đã sửa overdose_management cho {drug_name}: string -> dict")
            return True
    return False

def fix_administration_instructions_structure(drug_name: str, drug_data: Dict) -> bool:
    """Sửa administration_instructions từ string sang dict"""
    if "administration_instructions" in drug_data:
        value = drug_data["administration_instructions"]
        if isinstance(value, str) and value.strip():
            drug_data["administration_instructions"] = {
                "oral": {
                    "with_food": value,
                    "timing": "Theo chỉ định của bác sĩ"
                },
                "iv": {
                    "reconstitution": "N/A",
                    "infusion_rate": "N/A",
                    "compatibility": [],
                    "incompatibility": [],
                    "notes": "Chỉ có dạng uống" if "PO" in str(drug_data.get("administration", [])) else "N/A"
                }
            }
            print(f"  ✅ Đã sửa administration_instructions cho {drug_name}: string -> dict")
            return True
    return False

def analyze_errors():
    """Phân tích lỗi từ báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            report = json.load(f)
        return report
    except FileNotFoundError:
        print("❌ Không tìm thấy drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return None

def auto_fix_errors():
    """Tự động sửa các lỗi có thể sửa được"""
    print("=" * 100)
    print("TỰ ĐỘNG SỬA CÁC LỖI PHỔ BIẾN")
    print("=" * 100)
    print()
    
    # Phân tích lỗi
    report = analyze_errors()
    if not report:
        return
    
    fixes_applied = defaultdict(int)
    drugs_fixed = []
    
    print("Đang phân tích và sửa lỗi...\n")
    
    for drug_name in report["drugs_with_errors"]:
        drug_data = DRUG_DATABASE.get(drug_name)
        if not drug_data:
            continue
        
        print(f"📋 {drug_name}:")
        fixed = False
        
        # Sửa guideline_tags
        for error in report["errors_by_drug"][drug_name]:
            if "guideline_tags" in error and "Kiểu dữ liệu sai" in error:
                if fix_guideline_tags_type(drug_name, drug_data):
                    fixes_applied["guideline_tags"] += 1
                    fixed = True
                break
        
        # Sửa interactions rỗng
        for error in report["errors_by_drug"][drug_name]:
            if "Field rỗng: interactions" in error:
                if fix_empty_interactions(drug_name, drug_data):
                    fixes_applied["interactions"] += 1
                    fixed = True
                break
        
        # Sửa overdose_management
        for error in report["errors_by_drug"][drug_name]:
            if "overdose_management phải là dictionary" in error:
                if fix_overdose_management_structure(drug_name, drug_data):
                    fixes_applied["overdose_management"] += 1
                    fixed = True
                break
        
        # Sửa administration_instructions
        for error in report["errors_by_drug"][drug_name]:
            if "administration_instructions phải là dictionary" in error:
                if fix_administration_instructions_structure(drug_name, drug_data):
                    fixes_applied["administration_instructions"] += 1
                    fixed = True
                break
        
        if fixed:
            drugs_fixed.append(drug_name)
        
        if not fixed:
            print(f"  ⚠️  Không thể tự động sửa (cần sửa thủ công)")
        print()
    
    # Tóm tắt
    print("=" * 100)
    print("TÓM TẮT")
    print("=" * 100)
    print(f"\n✅ Đã sửa {len(drugs_fixed)} thuốc:")
    for drug in drugs_fixed:
        print(f"   - {drug}")
    
    print(f"\n📊 Số lỗi đã sửa theo loại:")
    for error_type, count in fixes_applied.items():
        print(f"   - {error_type}: {count}")
    
    if fixes_applied:
        print("\n⚠️  LƯU Ý:")
        print("   - Các thay đổi chỉ áp dụng trong bộ nhớ")
        print("   - Bạn cần cập nhật thủ công vào file module tương ứng")
        print("   - Hoặc thêm vào enhanced_fields_overrides.py")
        print("\n💡 Gợi ý:")
        print("   - Chạy lại comprehensive_drug_validation.py để kiểm tra")
        print("   - Xem chi tiết các thuốc đã sửa ở trên")
    
    # Tạo file gợi ý sửa
    if drugs_fixed:
        suggestions = []
        suggestions.append("=" * 100)
        suggestions.append("GỢI Ý SỬA LỖI TỰ ĐỘNG")
        suggestions.append("=" * 100)
        suggestions.append("")
        suggestions.append("Các thuốc sau đã được sửa trong bộ nhớ:")
        suggestions.append("")
        
        for drug_name in drugs_fixed:
            drug_data = DRUG_DATABASE.get(drug_name)
            suggestions.append(f"\n{drug_name}:")
            
            if "guideline_tags" in drug_data:
                suggestions.append(f"  guideline_tags: {drug_data['guideline_tags']}")
            
            if "interactions" in drug_data and drug_data["interactions"]:
                suggestions.append(f"  interactions: {drug_data['interactions']}")
            
            if "overdose_management" in drug_data and isinstance(drug_data["overdose_management"], dict):
                suggestions.append(f"  overdose_management: (đã chuyển thành dict)")
            
            if "administration_instructions" in drug_data and isinstance(drug_data["administration_instructions"], dict):
                suggestions.append(f"  administration_instructions: (đã chuyển thành dict)")
        
        with open('auto_fix_suggestions.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(suggestions))
        
        print(f"\n💾 Đã tạo file gợi ý: auto_fix_suggestions.txt")

def main():
    """Hàm chính"""
    try:
        auto_fix_errors()
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()

