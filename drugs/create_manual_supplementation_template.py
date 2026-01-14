#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create Manual Supplementation Templates
Tạo template bổ sung thủ công cho từng thuốc cần bổ sung
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Set
from datetime import datetime
from collections import defaultdict

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
    from drugs.field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE
    from field_validator import STANDARD_14_FIELDS, ADDITIONAL_8_FIELDS


def load_priority_data() -> Dict[str, Any]:
    """Load dữ liệu ưu tiên từ analyzer"""
    priority_file = Path(__file__).parent / "manual_supplementation_priority.json"
    
    if not priority_file.exists():
        print("⚠️  Chưa có file priority. Chạy manual_supplementation_analyzer.py trước.")
        return {}
    
    with open(priority_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_drug_current_data(drug_name: str) -> Dict[str, Any]:
    """Lấy dữ liệu hiện tại của thuốc"""
    drug_data = DRUG_DATABASE.get(drug_name, {})
    if not isinstance(drug_data, dict):
        return {}
    
    return drug_data.copy()


def identify_missing_fields(drug_name: str, priority_data: Dict[str, Any]) -> List[str]:
    """Xác định các field cần bổ sung cho thuốc"""
    missing_fields = []
    
    # Check all priorities
    for priority in ["P0", "P1", "P2", "P3"]:
        priority_info = priority_data.get("priorities", {}).get(priority, {})
        for field, field_data in priority_info.items():
            drugs = field_data.get("drugs", [])
            if any(d["name"] == drug_name for d in drugs):
                if field not in missing_fields:
                    missing_fields.append(field)
    
    return missing_fields


def check_field_empty(drug_data: Dict[str, Any], field: str) -> bool:
    """Kiểm tra field có rỗng không"""
    if field not in drug_data:
        return True
    
    value = drug_data[field]
    
    if value is None:
        return True
    
    if isinstance(value, str):
        return not value.strip() or value.strip() == "Đang cập nhật"
    
    if isinstance(value, (list, dict)):
        return len(value) == 0
    
    return False


def create_drug_template(drug_name: str, missing_fields: List[str], priority_data: Dict[str, Any]) -> Dict[str, Any]:
    """Tạo template cho một thuốc"""
    drug_data = get_drug_current_data(drug_name)
    
    # Determine priority level
    priority_level = None
    for p in ["P0", "P1", "P2", "P3"]:
        priority_info = priority_data.get("priorities", {}).get(p, {})
        for field, field_data in priority_info.items():
            drugs = field_data.get("drugs", [])
            if any(d["name"] == drug_name for d in drugs):
                priority_level = p
                break
        if priority_level:
            break
    
    template = {
        "drug_name": drug_name,
        "group": drug_data.get("group", "Unknown"),
        "vietnamese_name": drug_data.get("vietnamese_name", ""),
        "priority": priority_level or "P3",
        "status": "pending",  # pending, in_progress, completed, skipped
        "fields_to_supplement": missing_fields,
        "fields_completed": [],
        "fields_skipped": [],
        "current_data": {
            field: drug_data.get(field, None) 
            for field in missing_fields
        },
        "supplementation_data": {},  # Will be filled during manual work
        "sources_checked": [],  # List of sources checked
        "notes": "",
        "created_date": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
        "completed_by": ""
    }
    
    return template


def get_field_guidelines(field: str) -> Dict[str, Any]:
    """Lấy hướng dẫn bổ sung cho từng field"""
    guidelines = {
        "pregnancy": {
            "format": "string",
            "example": "D - Chống chỉ định trong thai kỳ",
            "valid_values": ["A", "B", "C", "D", "X"],
            "sources": ["FDA Pregnancy Categories", "UpToDate Pregnancy Safety", "Package insert"],
            "notes": "Ưu tiên FDA category. Nếu không tìm thấy → đánh dấu BỎ QUA"
        },
        "dosage": {
            "format": "dict",
            "example": {
                "adult": "10-40mg x 1-2 lần/ngày",
                "adult_initial": "10mg x 1 lần/ngày",
                "pediatric": "...",
                "notes": "..."
            },
            "sources": ["Package insert", "UpToDate Dosing", "FDA Labeling"],
            "notes": "Bổ sung đầy đủ liều cho các trường hợp"
        },
        "side_effects": {
            "format": "list of strings",
            "example": ["Ho khan", "Tăng kali máu", "Hạ huyết áp"],
            "sources": ["Package insert", "UpToDate", "FDA Labeling"],
            "notes": "Bổ sung ít nhất 3-5 tác dụng phụ phổ biến nhất. Ưu tiên tác dụng phụ nghiêm trọng"
        },
        "contraindications": {
            "format": "list of strings hoặc dict",
            "example": ["Dị ứng", "Có thai"],
            "example_dict": {"tuyệt_đối": ["Dị ứng thuốc", "Có thai"], "tương_đối": ["Suy thận trung bình"]},
            "sources": ["Package insert", "FDA Labeling", "UpToDate"],
            "notes": "Bổ sung chống chỉ định tuyệt đối trước"
        },
        "interactions": {
            "format": "list of strings",
            "example": ["Kali bổ sung: tăng nguy cơ tăng kali máu"],
            "sources": ["Drug interactions database", "UpToDate", "Package insert"],
            "notes": "Bổ sung tương tác quan trọng nhất"
        },
        "storage": {
            "format": "string",
            "example": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
            "sources": ["Package insert", "FDA Labeling"],
            "notes": "Có thể dùng giá trị mặc định theo nhóm thuốc nếu không tìm thấy"
        },
        "pregnancy_lactation": {
            "format": "dict",
            "example": {
                "fda_category": "D",
                "pregnancy_details": "...",
                "lactation": {"safety": "Caution", "details": "..."}
            },
            "sources": ["UpToDate", "FDA Labeling"],
            "notes": "Field khuyến nghị, có thể bỏ qua nếu không tìm thấy"
        },
        "administration_instructions": {
            "format": "dict",
            "example": {
                "oral": {"with_food": "...", "timing": "..."}
            },
            "sources": ["Package insert", "FDA Labeling"],
            "notes": "Field khuyến nghị, có thể bỏ qua nếu không tìm thấy"
        },
        "references": {
            "format": "dict",
            "example": {
                "primary_sources": ["UpToDate", "FDA Labeling"],
                "last_updated": "2026-01-13",
                "evidence_level": "A"
            },
            "sources": ["Nguồn đã sử dụng"],
            "notes": "Ghi chú nguồn tham khảo đã sử dụng"
        },
        "black_box_warnings": {
            "format": "string hoặc None",
            "example": "CHỐNG CHỈ ĐỊNH trong thai kỳ...",
            "example_none": None,
            "sources": ["FDA Labeling"],
            "notes": "Có thể None nếu không có black box warning"
        }
    }
    
    return guidelines.get(field, {
        "format": "unknown",
        "sources": [],
        "notes": "Kiểm tra field_validator.py để biết format chính xác"
    })


def create_all_templates(priority_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """Tạo template cho tất cả thuốc cần bổ sung"""
    all_drugs = set()
    
    # Collect all drugs from all priorities
    for priority in ["P0", "P1", "P2", "P3"]:
        priority_info = priority_data.get("priorities", {}).get(priority, {})
        for field, field_data in priority_info.items():
            drugs = field_data.get("drugs", [])
            for drug in drugs:
                all_drugs.add(drug["name"])
    
    templates = {}
    
    for drug_name in sorted(all_drugs):
        missing_fields = identify_missing_fields(drug_name, priority_data)
        if missing_fields:
            template = create_drug_template(drug_name, missing_fields, priority_data)
            templates[drug_name] = template
    
    return templates


def create_workbook(templates: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Tạo workbook tổng hợp tất cả template"""
    workbook = {
        "created_date": datetime.now().isoformat(),
        "total_drugs": len(templates),
        "statistics": {
            "by_priority": defaultdict(int),
            "by_status": defaultdict(int),
            "by_field": defaultdict(int)
        },
        "templates": templates
    }
    
    # Calculate statistics
    for drug_name, template in templates.items():
        priority = template.get("priority", "P3")
        status = template.get("status", "pending")
        fields = template.get("fields_to_supplement", [])
        
        workbook["statistics"]["by_priority"][priority] += 1
        workbook["statistics"]["by_status"][status] += 1
        
        for field in fields:
            workbook["statistics"]["by_field"][field] += 1
    
    # Convert defaultdict to dict
    workbook["statistics"]["by_priority"] = dict(workbook["statistics"]["by_priority"])
    workbook["statistics"]["by_status"] = dict(workbook["statistics"]["by_status"])
    workbook["statistics"]["by_field"] = dict(workbook["statistics"]["by_field"])
    
    return workbook


def save_individual_templates(templates: Dict[str, Dict[str, Any]], output_dir: Path):
    """Lưu template riêng cho từng thuốc"""
    output_dir.mkdir(exist_ok=True)
    
    for drug_name, template in templates.items():
        # Sanitize filename
        safe_name = drug_name.replace("/", "_").replace("\\", "_").replace(" ", "_")
        template_file = output_dir / f"{safe_name}.json"
        
        # Add field guidelines
        template_with_guidelines = template.copy()
        template_with_guidelines["field_guidelines"] = {}
        
        for field in template["fields_to_supplement"]:
            template_with_guidelines["field_guidelines"][field] = get_field_guidelines(field)
        
        with open(template_file, 'w', encoding='utf-8') as f:
            json.dump(template_with_guidelines, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Đã lưu {len(templates)} template riêng vào {output_dir}")


def main():
    """Main function"""
    print("Đang tạo template bổ sung thủ công...")
    
    # Load priority data
    priority_data = load_priority_data()
    if not priority_data:
        return
    
    # Create all templates
    templates = create_all_templates(priority_data)
    print(f"✅ Đã tạo {len(templates)} template")
    
    # Create workbook
    workbook = create_workbook(templates)
    
    # Save workbook
    workbook_file = Path(__file__).parent / "manual_supplementation_workbook.json"
    with open(workbook_file, 'w', encoding='utf-8') as f:
        json.dump(workbook, f, ensure_ascii=False, indent=2)
    print(f"✅ Đã lưu workbook: {workbook_file}")
    
    # Save individual templates
    templates_dir = Path(__file__).parent / "manual_supplementation_templates"
    save_individual_templates(templates, templates_dir)
    
    # Print summary
    print("\n" + "="*60)
    print("TỔNG KẾT TEMPLATE")
    print("="*60)
    print(f"Tổng số thuốc: {len(templates)}")
    print("\nTheo mức độ ưu tiên:")
    for priority, count in sorted(workbook["statistics"]["by_priority"].items()):
        print(f"  {priority}: {count} thuốc")
    print("\nTheo field:")
    for field, count in sorted(workbook["statistics"]["by_field"].items(), key=lambda x: -x[1]):
        print(f"  {field}: {count} thuốc")
    print("="*60)


if __name__ == "__main__":
    main()
