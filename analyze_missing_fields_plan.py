#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phân tích toàn diện các thuốc thiếu field và tạo kế hoạch làm việc
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
        if py_file.name == "__init__.py":
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
    """Phân tích các thuốc thiếu field"""
    
    # Đọc báo cáo
    with open("missing_fields_report.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
    
    # Tổng hợp theo field
    field_analysis = {}
    for field in priority_fields:
        missing_drugs = data["missing_fields"].get(field, [])
        # Loại bỏ "references" nếu có (không phải tên thuốc)
        missing_drugs = [d for d in missing_drugs if d != "references"]
        
        # Tìm file cho mỗi thuốc
        drugs_with_files = []
        for drug in missing_drugs:
            file_path = find_drug_file(drug)
            module = get_module_from_file(file_path)
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
    drug_missing_fields = defaultdict(set)
    
    for field in priority_fields:
        for drug in field_analysis[field]["drugs"]:
            drug_missing_count[drug] += 1
            drug_missing_fields[drug].add(field)
    
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
        "summary": {
            field: {
                "count": field_analysis[field]["total"],
                "modules_affected": len(field_analysis[field]["by_module"]),
                "files_affected": len(field_analysis[field]["by_file"])
            }
            for field in priority_fields
        }
    }

def create_work_sessions(analysis: Dict) -> List[Dict]:
    """Tạo các phiên làm việc nhỏ"""
    sessions = []
    session_id = 1
    
    priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
    
    for field in priority_fields:
        field_data = analysis["field_analysis"][field]
        
        # Nhóm theo file để xử lý cùng lúc
        for file_path, drugs in field_data["by_file"].items():
            if file_path == "Unknown":
                continue
            
            # Chia nhỏ nếu quá nhiều thuốc (mỗi session 10-15 thuốc)
            chunk_size = 12
            for i in range(0, len(drugs), chunk_size):
                chunk = drugs[i:i+chunk_size]
                sessions.append({
                    "session_id": session_id,
                    "field": field,
                    "file": file_path,
                    "module": get_module_from_file(file_path),
                    "drugs": chunk,
                    "count": len(chunk),
                    "priority": "high" if field in ["renal_adjustment", "drug_interactions"] else "medium"
                })
                session_id += 1
        
        # Xử lý Unknown files riêng
        unknown_drugs = [d["drug"] for d in field_data["drugs_with_locations"] if d["file"] == "Unknown"]
        if unknown_drugs:
            for i in range(0, len(unknown_drugs), chunk_size):
                chunk = unknown_drugs[i:i+chunk_size]
                sessions.append({
                    "session_id": session_id,
                    "field": field,
                    "file": "Unknown (cần tìm)",
                    "module": "Unknown",
                    "drugs": chunk,
                    "count": len(chunk),
                    "priority": "medium"
                })
                session_id += 1
    
    return sessions

def generate_report(analysis: Dict, sessions: List[Dict]):
    """Tạo báo cáo markdown"""
    
    md = """# Kế Hoạch Bổ Sung Fields Cho Dữ Liệu Thuốc

## Tổng Quan

"""
    md += f"- **Tổng số thuốc trong database**: {analysis['total_drugs']}\n"
    md += f"- **Tổng số phiên làm việc**: {len(sessions)}\n\n"
    
    md += "## Thống Kê Theo Field\n\n"
    md += "| Field | Số thuốc thiếu | Số module bị ảnh hưởng | Số file bị ảnh hưởng |\n"
    md += "|-------|----------------|------------------------|----------------------|\n"
    
    for field, stats in analysis["summary"].items():
        md += f"| `{field}` | {stats['count']} | {stats['modules_affected']} | {stats['files_affected']} |\n"
    
    md += "\n## Chi Tiết Theo Field\n\n"
    
    priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
    for field in priority_fields:
        field_data = analysis["field_analysis"][field]
        md += f"### {field} ({field_data['total']} thuốc)\n\n"
        
        # Top modules
        sorted_modules = sorted(field_data["by_module"].items(), key=lambda x: len(x[1]), reverse=True)
        md += "**Top 10 modules có nhiều thuốc thiếu nhất:**\n\n"
        for module, drugs in sorted_modules[:10]:
            md += f"- `{module}`: {len(drugs)} thuốc\n"
        
        md += "\n"
    
    md += "\n## Danh Sách Thuốc Thiếu Nhiều Field\n\n"
    md += "Các thuốc thiếu từ 2 field trở lên (ưu tiên xử lý):\n\n"
    md += "| Thuốc | Số field thiếu | Các field thiếu |\n"
    md += "|-------|----------------|------------------|\n"
    
    for drug, count, fields in analysis["drugs_missing_multiple"][:30]:
        fields_str = ", ".join(sorted(fields))
        md += f"| {drug} | {count} | {fields_str} |\n"
    
    md += "\n## Kế Hoạch Làm Việc Theo Phiên\n\n"
    md += f"Tổng cộng **{len(sessions)}** phiên làm việc nhỏ.\n\n"
    
    # Nhóm sessions theo field
    by_field = defaultdict(list)
    for session in sessions:
        by_field[session["field"]].append(session)
    
    for field in priority_fields:
        if field not in by_field:
            continue
        
        field_sessions = by_field[field]
        md += f"### {field} ({len(field_sessions)} phiên)\n\n"
        
        # Nhóm theo module
        by_module = defaultdict(list)
        for session in field_sessions:
            by_module[session["module"]].append(session)
        
        for module, module_sessions in sorted(by_module.items()):
            if module == "Unknown":
                continue
            md += f"#### Module: {module}\n\n"
            for session in module_sessions[:5]:  # Hiển thị 5 đầu tiên
                md += f"**Phiên {session['session_id']}**: {session['count']} thuốc trong `{Path(session['file']).name}`\n"
                md += f"- Danh sách: {', '.join(session['drugs'][:5])}"
                if len(session['drugs']) > 5:
                    md += f" và {len(session['drugs']) - 5} thuốc khác"
                md += "\n\n"
        
        if "Unknown" in by_module:
            md += f"#### Cần tìm file ({len(by_module['Unknown'])} phiên)\n\n"
    
    md += "\n## Hướng Dẫn Thực Hiện\n\n"
    md += "1. **Làm theo từng phiên**: Mỗi phiên xử lý 10-15 thuốc trong cùng một file\n"
    md += "2. **Sử dụng template**: Copy từ thuốc tương tự trong cùng nhóm\n"
    md += "3. **Kiểm tra sau mỗi phiên**: Chạy `python check_missing_fields_comprehensive.py`\n"
    md += "4. **Ưu tiên**: Xử lý các thuốc thiếu nhiều field trước\n\n"
    
    return md

def main():
    print("Đang phân tích dữ liệu thiếu field...")
    analysis = analyze_missing_fields()
    
    print("Đang tạo kế hoạch làm việc...")
    sessions = create_work_sessions(analysis)
    
    print("Đang tạo báo cáo...")
    report = generate_report(analysis, sessions)
    
    # Lưu báo cáo
    with open("FIELD_ENHANCEMENT_PLAN.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    # Lưu dữ liệu JSON
    output = {
        "analysis": analysis,
        "sessions": sessions
    }
    
    with open("field_enhancement_plan.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Đã tạo kế hoạch:")
    print(f"   - FIELD_ENHANCEMENT_PLAN.md")
    print(f"   - field_enhancement_plan.json")
    print(f"\n📊 Tóm tắt:")
    print(f"   - Tổng số thuốc: {analysis['total_drugs']}")
    for field, stats in analysis["summary"].items():
        print(f"   - {field}: {stats['count']} thuốc thiếu")
    print(f"   - Tổng số phiên: {len(sessions)}")

if __name__ == "__main__":
    main()
