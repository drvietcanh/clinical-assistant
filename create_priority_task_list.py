#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo danh sách công việc ưu tiên dựa trên kết quả validation
"""

import json
from typing import Dict, List
from collections import defaultdict

def load_validation_report():
    """Đọc báo cáo validation"""
    try:
        with open('drug_validation_report.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy drug_validation_report.json")
        print("   Vui lòng chạy comprehensive_drug_validation.py trước")
        return None

def create_priority_tasks(report: Dict):
    """Tạo danh sách công việc ưu tiên"""
    
    stats = report["summary"]
    field_completion = report["field_completion"]
    errors_by_drug = report["errors_by_drug"]
    warnings_by_drug = report["warnings_by_drug"]
    
    tasks = []
    
    # Ưu tiên 1: Sửa lỗi nghiêm trọng
    if errors_by_drug:
        tasks.append({
            "priority": "CRITICAL",
            "title": "Sửa các lỗi nghiêm trọng",
            "count": len(errors_by_drug),
            "description": "Các lỗi này ảnh hưởng đến tính toàn vẹn dữ liệu",
            "items": []
        })
        
        for drug_name in sorted(errors_by_drug.keys()):
            errors = errors_by_drug[drug_name]
            task_item = {
                "drug": drug_name,
                "errors": errors[:3],  # 3 lỗi đầu
                "total_errors": len(errors)
            }
            tasks[0]["items"].append(task_item)
    
    # Ưu tiên 2: Bổ sung contraindications_detail (thiếu nhiều nhất)
    contraindications_missing = field_completion.get("contraindications_detail", {}).get("missing", 0)
    if contraindications_missing > 0:
        missing_drugs = []
        for drug, warnings in warnings_by_drug.items():
            for warning in warnings:
                if "contraindications_detail" in warning:
                    missing_drugs.append(drug)
                    break
        
        tasks.append({
            "priority": "HIGH",
            "title": f"Bổ sung contraindications_detail ({contraindications_missing} thuốc)",
            "count": contraindications_missing,
            "description": "Field quan trọng cho an toàn thuốc, thiếu nhiều nhất (52%)",
            "items": sorted(missing_drugs)[:20]  # 20 đầu tiên
        })
    
    # Ưu tiên 3: Bổ sung reversal_agents
    reversal_missing = field_completion.get("reversal_agents", {}).get("missing", 0)
    if reversal_missing > 0:
        missing_drugs = []
        for drug, warnings in warnings_by_drug.items():
            for warning in warnings:
                if "reversal_agents" in warning:
                    missing_drugs.append(drug)
                    break
        
        tasks.append({
            "priority": "HIGH",
            "title": f"Bổ sung reversal_agents ({reversal_missing} thuốc)",
            "count": reversal_missing,
            "description": "Quan trọng cho các thuốc có antidote, đặc biệt ICU/emergency",
            "items": sorted(missing_drugs)[:20]
        })
    
    # Ưu tiên 4: Bổ sung black_box_warnings
    black_box_missing = field_completion.get("black_box_warnings", {}).get("missing", 0)
    if black_box_missing > 0:
        missing_drugs = []
        for drug, warnings in warnings_by_drug.items():
            for warning in warnings:
                if "black_box_warnings" in warning:
                    missing_drugs.append(drug)
                    break
        
        tasks.append({
            "priority": "MEDIUM",
            "title": f"Bổ sung black_box_warnings ({black_box_missing} thuốc)",
            "count": black_box_missing,
            "description": "Cảnh báo đặc biệt quan trọng cho an toàn",
            "items": sorted(missing_drugs)[:20]
        })
    
    # Ưu tiên 5: Bổ sung các enhanced fields còn lại
    other_missing_fields = []
    for field, data in field_completion.items():
        if field not in ["contraindications_detail", "reversal_agents", "black_box_warnings"]:
            missing = data.get("missing", 0)
            if missing > 0 and data.get("percentage", 100) < 95:
                other_missing_fields.append({
                    "field": field,
                    "missing": missing,
                    "percentage": data.get("percentage", 0)
                })
    
    if other_missing_fields:
        other_missing_fields.sort(key=lambda x: x["missing"], reverse=True)
        tasks.append({
            "priority": "MEDIUM",
            "title": "Bổ sung các enhanced fields còn lại",
            "count": sum(f["missing"] for f in other_missing_fields),
            "description": "Các field còn thiếu để đạt >95%",
            "items": [f"{f['field']}: thiếu {f['missing']} thuốc ({100-f['percentage']:.1f}%)" 
                     for f in other_missing_fields[:10]]
        })
    
    return tasks

def generate_task_report(tasks: List[Dict]):
    """Tạo báo cáo công việc"""
    
    output = []
    output.append("=" * 100)
    output.append("DANH SÁCH CÔNG VIỆC ƯU TIÊN")
    output.append("=" * 100)
    output.append("")
    output.append(f"Tổng số nhóm công việc: {len(tasks)}")
    output.append("")
    
    priority_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
    priority_icons = {
        "CRITICAL": "🔴",
        "HIGH": "🟠",
        "MEDIUM": "🟡",
        "LOW": "🟢"
    }
    
    for priority in priority_order:
        priority_tasks = [t for t in tasks if t["priority"] == priority]
        if not priority_tasks:
            continue
        
        output.append("=" * 100)
        output.append(f"{priority_icons.get(priority, '•')} ƯU TIÊN {priority}")
        output.append("=" * 100)
        output.append("")
        
        for i, task in enumerate(priority_tasks, 1):
            output.append(f"{i}. {task['title']}")
            output.append(f"   Mô tả: {task['description']}")
            output.append(f"   Số lượng: {task['count']}")
            output.append("")
            
            if task.get("items"):
                if isinstance(task["items"][0], dict):
                    # Lỗi chi tiết
                    output.append("   Chi tiết:")
                    for item in task["items"][:10]:  # 10 đầu tiên
                        output.append(f"      • {item['drug']}:")
                        for error in item.get("errors", []):
                            output.append(f"        - {error}")
                        if item.get("total_errors", 0) > len(item.get("errors", [])):
                            output.append(f"        ... và {item['total_errors'] - len(item.get('errors', []))} lỗi khác")
                    if len(task["items"]) > 10:
                        output.append(f"      ... và {len(task['items']) - 10} thuốc khác")
                else:
                    # Danh sách thuốc
                    output.append("   Danh sách thuốc (20 đầu tiên):")
                    for drug in task["items"][:20]:
                        output.append(f"      • {drug}")
                    if len(task["items"]) > 20:
                        output.append(f"      ... và {len(task['items']) - 20} thuốc khác")
                output.append("")
    
    return "\n".join(output)

def generate_markdown_tasks(tasks: List[Dict]):
    """Tạo file markdown với danh sách công việc"""
    
    md = []
    md.append("# 📋 Danh Sách Công Việc Ưu Tiên")
    md.append("")
    md.append(f"**Tổng số nhóm công việc:** {len(tasks)}")
    md.append("")
    md.append("---")
    md.append("")
    
    priority_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW"]
    priority_headers = {
        "CRITICAL": "🔴 CRITICAL - Cần sửa ngay",
        "HIGH": "🟠 HIGH - Ưu tiên cao",
        "MEDIUM": "🟡 MEDIUM - Ưu tiên trung bình",
        "LOW": "🟢 LOW - Ưu tiên thấp"
    }
    
    for priority in priority_order:
        priority_tasks = [t for t in tasks if t["priority"] == priority]
        if not priority_tasks:
            continue
        
        md.append(f"## {priority_headers.get(priority, priority)}")
        md.append("")
        
        for i, task in enumerate(priority_tasks, 1):
            md.append(f"### {i}. {task['title']}")
            md.append("")
            md.append(f"**Mô tả:** {task['description']}")
            md.append("")
            md.append(f"**Số lượng:** {task['count']}")
            md.append("")
            
            if task.get("items"):
                if isinstance(task["items"][0], dict):
                    md.append("**Chi tiết:**")
                    md.append("")
                    for item in task["items"][:10]:
                        md.append(f"- **{item['drug']}:**")
                        for error in item.get("errors", []):
                            md.append(f"  - {error}")
                else:
                    md.append("**Danh sách thuốc:**")
                    md.append("")
                    for drug in task["items"][:20]:
                        md.append(f"- {drug}")
                    if len(task["items"]) > 20:
                        md.append(f"- ... và {len(task['items']) - 20} thuốc khác")
                md.append("")
        
        md.append("---")
        md.append("")
    
    return "\n".join(md)

def main():
    """Hàm chính"""
    print("Đang tạo danh sách công việc ưu tiên...")
    
    report = load_validation_report()
    if not report:
        return
    
    tasks = create_priority_tasks(report)
    
    # Tạo báo cáo text
    task_report = generate_task_report(tasks)
    with open('priority_tasks.txt', 'w', encoding='utf-8') as f:
        f.write(task_report)
    print("✅ Đã tạo: priority_tasks.txt")
    
    # Tạo file markdown
    md_tasks = generate_markdown_tasks(tasks)
    with open('priority_tasks.md', 'w', encoding='utf-8') as f:
        f.write(md_tasks)
    print("✅ Đã tạo: priority_tasks.md")
    
    # Tạo file JSON
    with open('priority_tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    print("✅ Đã tạo: priority_tasks.json")
    
    print()
    print("=" * 100)
    print("TÓM TẮT")
    print("=" * 100)
    print(f"\nTổng số nhóm công việc: {len(tasks)}")
    
    for priority in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        priority_tasks = [t for t in tasks if t["priority"] == priority]
        if priority_tasks:
            total_count = sum(t["count"] for t in priority_tasks)
            print(f"  {priority}: {len(priority_tasks)} nhóm, {total_count} công việc")

if __name__ == '__main__':
    main()

