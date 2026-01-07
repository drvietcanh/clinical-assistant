#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phân tích dữ liệu từ missing_fields_report.json và tạo danh sách chi tiết
các thuốc thiếu field theo module/file
"""

import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set

def find_drug_file(drug_name: str) -> str:
    """Tìm file chứa thuốc"""
    drug_modules_path = Path("drugs/drug_modules")
    if not drug_modules_path.exists():
        return "Unknown"
    
    # Search recursively
    for py_file in drug_modules_path.rglob("*.py"):
        if py_file.name == "__init__.py" or ".backup" in py_file.name:
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check for drug name in quotes
                if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                    return str(py_file.relative_to(Path(".")))
        except:
            continue
    
    return "Unknown"

def get_module_from_file(file_path: str) -> str:
    """Lấy tên module từ file path"""
    if file_path == "Unknown":
        return "Unknown"
    
    parts = Path(file_path).parts
    if len(parts) >= 3 and parts[0] == "drugs" and parts[1] == "drug_modules":
        return parts[2]  # Module name
    return "Unknown"

def analyze_missing_fields():
    """Phân tích các thuốc thiếu field và tạo danh sách chi tiết"""
    
    # Đọc báo cáo
    with open("missing_fields_report.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
    
    # Tổng hợp theo field
    field_analysis = {}
    all_drugs_with_locations = {}
    
    for field in priority_fields:
        missing_drugs = data["missing_fields"].get(field, [])
        # Loại bỏ "references" nếu có (không phải tên thuốc)
        missing_drugs = [d for d in missing_drugs if d != "references"]
        
        # Tìm file cho mỗi thuốc
        drugs_with_files = []
        for drug in missing_drugs:
            if drug not in all_drugs_with_locations:
                file_path = find_drug_file(drug)
                module = get_module_from_file(file_path)
                all_drugs_with_locations[drug] = {
                    "file": file_path,
                    "module": module
                }
            else:
                file_path = all_drugs_with_locations[drug]["file"]
                module = all_drugs_with_locations[drug]["module"]
            
            drugs_with_files.append({
                "drug": drug,
                "file": file_path,
                "module": module
            })
        
        # Nhóm theo module
        by_module = defaultdict(list)
        by_file = defaultdict(list)
        
        for item in drugs_with_files:
            by_module[item["module"]].append(item["drug"])
            by_file[item["file"]].append(item["drug"])
        
        field_analysis[field] = {
            "total": len(missing_drugs),
            "drugs": missing_drugs,
            "by_module": dict(by_module),
            "by_file": dict(by_file),
            "drugs_with_locations": drugs_with_files
        }
    
    # Tìm thuốc thiếu nhiều field
    drug_missing_count = defaultdict(int)
    drug_missing_fields = defaultdict(list)
    
    for field in priority_fields:
        for drug in field_analysis[field]["drugs"]:
            drug_missing_count[drug] += 1
            if field not in drug_missing_fields[drug]:
                drug_missing_fields[drug].append(field)
    
    # Sắp xếp theo số field thiếu
    drugs_missing_multiple = sorted(
        [(drug, count, drug_missing_fields[drug]) for drug, count in drug_missing_count.items() if count > 1],
        key=lambda x: x[1],
        reverse=True
    )
    
    return {
        "total_drugs": data["total_drugs"],
        "field_analysis": field_analysis,
        "drugs_missing_multiple": drugs_missing_multiple,
        "all_drugs_with_locations": all_drugs_with_locations,
        "summary": {
            field: {
                "count": field_analysis[field]["total"],
                "modules_affected": len(field_analysis[field]["by_module"]),
                "files_affected": len(field_analysis[field]["by_file"])
            }
            for field in priority_fields
        }
    }

def create_detailed_report(analysis: Dict):
    """Tạo báo cáo chi tiết với danh sách thuốc theo file"""
    
    report = {
        "summary": analysis["summary"],
        "drugs_by_file": {},
        "drugs_by_module": {},
        "priority_drugs": []
    }
    
    # Nhóm tất cả thuốc theo file
    all_files = defaultdict(lambda: {
        "renal_adjustment": [],
        "drug_interactions": [],
        "contraindications_detail": [],
        "reversal_agents": []
    })
    
    for field in ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]:
        field_data = analysis["field_analysis"][field]
        for item in field_data["drugs_with_locations"]:
            file_path = item["file"]
            if file_path != "Unknown":
                all_files[file_path][field].append(item["drug"])
    
    # Tạo danh sách theo file
    for file_path, fields_dict in all_files.items():
        total_drugs = set()
        for field_drugs in fields_dict.values():
            total_drugs.update(field_drugs)
        
        report["drugs_by_file"][file_path] = {
            "total_drugs_missing": len(total_drugs),
            "fields": fields_dict,
            "module": get_module_from_file(file_path)
        }
    
    # Nhóm theo module
    all_modules = defaultdict(lambda: {
        "renal_adjustment": [],
        "drug_interactions": [],
        "contraindications_detail": [],
        "reversal_agents": [],
        "files": set()
    })
    
    for file_path, file_data in report["drugs_by_file"].items():
        module = file_data["module"]
        all_modules[module]["files"].add(file_path)
        for field in ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]:
            all_modules[module][field].extend(file_data["fields"][field])
    
    for module, module_data in all_modules.items():
        total_drugs = set()
        for field in ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]:
            total_drugs.update(module_data[field])
        
        report["drugs_by_module"][module] = {
            "total_drugs_missing": len(total_drugs),
            "fields": {k: sorted(list(set(v))) for k, v in module_data.items() if k != "files"},
            "files": sorted(list(module_data["files"]))
        }
    
    # Thuốc ưu tiên (thiếu nhiều field)
    report["priority_drugs"] = [
        {
            "drug": drug,
            "missing_count": count,
            "missing_fields": list(fields),
            "file": analysis["all_drugs_with_locations"].get(drug, {}).get("file", "Unknown"),
            "module": analysis["all_drugs_with_locations"].get(drug, {}).get("module", "Unknown")
        }
        for drug, count, fields in analysis["drugs_missing_multiple"][:50]
    ]
    
    return report

def main():
    print("Đang phân tích dữ liệu thiếu field...")
    analysis = analyze_missing_fields()
    
    print("Đang tạo báo cáo chi tiết...")
    detailed_report = create_detailed_report(analysis)
    
    # Chuyển đổi sets thành lists cho JSON serialization
    def convert_sets_to_lists(obj):
        if isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, dict):
            return {k: convert_sets_to_lists(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_sets_to_lists(item) for item in obj]
        return obj
    
    # Lưu báo cáo JSON
    with open("detailed_drug_analysis.json", "w", encoding="utf-8") as f:
        json.dump({
            "analysis": convert_sets_to_lists(analysis),
            "detailed_report": convert_sets_to_lists(detailed_report)
        }, f, indent=2, ensure_ascii=False)
    
    # Tạo markdown report
    md = "# Báo Cáo Chi Tiết Thuốc Thiếu Fields\n\n"
    md += f"**Tổng số thuốc**: {analysis['total_drugs']}\n\n"
    
    md += "## Thống Kê Theo Field\n\n"
    md += "| Field | Số thuốc thiếu | Số module | Số file |\n"
    md += "|-------|----------------|-----------|----------|\n"
    for field, stats in analysis["summary"].items():
        md += f"| `{field}` | {stats['count']} | {stats['modules_affected']} | {stats['files_affected']} |\n"
    
    md += "\n## Thuốc Ưu Tiên (Thiếu Nhiều Field)\n\n"
    md += "| Thuốc | Số field thiếu | Các field | File |\n"
    md += "|-------|----------------|-----------|------|\n"
    for item in detailed_report["priority_drugs"][:30]:
        fields_str = ", ".join(item["missing_fields"])
        file_name = Path(item["file"]).name if item["file"] != "Unknown" else "Unknown"
        md += f"| {item['drug']} | {item['missing_count']} | {fields_str} | {file_name} |\n"
    
    md += "\n## Danh Sách Theo File (Top 20)\n\n"
    sorted_files = sorted(
        detailed_report["drugs_by_file"].items(),
        key=lambda x: x[1]["total_drugs_missing"],
        reverse=True
    )[:20]
    
    for file_path, file_data in sorted_files:
        md += f"### {Path(file_path).name}\n\n"
        md += f"**Module**: {file_data['module']}\n\n"
        md += f"**Tổng số thuốc thiếu**: {file_data['total_drugs_missing']}\n\n"
        for field, drugs in file_data["fields"].items():
            if drugs:
                md += f"- **{field}**: {len(drugs)} thuốc - {', '.join(drugs[:5])}"
                if len(drugs) > 5:
                    md += f" và {len(drugs) - 5} thuốc khác"
                md += "\n"
        md += "\n"
    
    with open("detailed_drug_analysis.md", "w", encoding="utf-8") as f:
        f.write(md)
    
    print(f"\n✅ Đã tạo báo cáo:")
    print(f"   - detailed_drug_analysis.json")
    print(f"   - detailed_drug_analysis.md")
    print(f"\n📊 Tóm tắt:")
    print(f"   - Tổng số thuốc: {analysis['total_drugs']}")
    for field, stats in analysis["summary"].items():
        print(f"   - {field}: {stats['count']} thuốc thiếu ({stats['files_affected']} files)")
    print(f"   - Số file cần xử lý: {len(detailed_report['drugs_by_file'])}")

if __name__ == "__main__":
    main()
