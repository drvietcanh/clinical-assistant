#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo kế hoạch các phiên làm việc nhỏ (10-15 thuốc/phiên) theo module và file
"""

import json
from pathlib import Path
from collections import defaultdict

def create_work_sessions():
    """Tạo các phiên làm việc từ dữ liệu phân tích"""
    
    with open("detailed_drug_analysis.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    detailed_report = data["detailed_report"]
    drugs_by_file = detailed_report["drugs_by_file"]
    
    sessions = []
    session_id = 1
    
    priority_fields = ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]
    
    # Ưu tiên các file quan trọng
    priority_files = [
        "drugs/drug_modules/cardiovascular/ace_arb.py",
        "drugs/drug_modules/cardiovascular/statins.py",
        "drugs/drug_modules/diabetes/specific_insulins.py",
        "drugs/drug_modules/diabetes/sglt2_inhibitors.py",
        "drugs/drug_modules/diabetes/glp1_agonists.py",
        "drugs/drug_modules/gastrointestinal/proton_pump_inhibitors.py",
        "drugs/drug_modules/anesthesia/induction_agents.py",
        "drugs/drug_modules/supportive/sedatives_anesthetics_icu.py",
    ]
    
    # Tạo sessions cho từng field trong từng file
    chunk_size = 12  # 10-15 thuốc mỗi phiên
    
    for field in priority_fields:
        # Xử lý priority files trước
        for file_path in priority_files:
            if file_path in drugs_by_file:
                drugs = drugs_by_file[file_path]["fields"].get(field, [])
                if drugs:
                    # Chia nhỏ nếu quá nhiều
                    for i in range(0, len(drugs), chunk_size):
                        chunk = drugs[i:i+chunk_size]
                        sessions.append({
                            "session_id": session_id,
                            "field": field,
                            "file": file_path,
                            "module": drugs_by_file[file_path]["module"],
                            "drugs": chunk,
                            "count": len(chunk),
                            "priority": "high",
                            "is_priority_file": True
                        })
                        session_id += 1
        
        # Xử lý các file còn lại
        for file_path, file_data in drugs_by_file.items():
            if file_path in priority_files:
                continue  # Đã xử lý ở trên
            
            drugs = file_data["fields"].get(field, [])
            if drugs:
                # Chia nhỏ nếu quá nhiều
                for i in range(0, len(drugs), chunk_size):
                    chunk = drugs[i:i+chunk_size]
                    module = file_data["module"]
                    
                    # Xác định priority dựa trên module
                    if module in ["cardiovascular", "diabetes", "gastrointestinal"]:
                        priority = "high"
                    elif module in ["anesthesia", "neurological", "endocrinology"]:
                        priority = "medium"
                    else:
                        priority = "low"
                    
                    sessions.append({
                        "session_id": session_id,
                        "field": field,
                        "file": file_path,
                        "module": module,
                        "drugs": chunk,
                        "count": len(chunk),
                        "priority": priority,
                        "is_priority_file": False
                    })
                    session_id += 1
    
    # Sắp xếp sessions: priority files trước, sau đó theo priority level
    def sort_key(session):
        priority_order = {"high": 0, "medium": 1, "low": 2}
        field_order = {
            "renal_adjustment": 0,
            "drug_interactions": 1,
            "contraindications_detail": 2,
            "reversal_agents": 3
        }
        return (
            not session.get("is_priority_file", False),  # Priority files first
            priority_order.get(session["priority"], 2),
            field_order.get(session["field"], 99),
            session["session_id"]
        )
    
    sessions.sort(key=sort_key)
    
    # Đánh số lại session_id sau khi sắp xếp
    for i, session in enumerate(sessions, 1):
        session["session_id"] = i
    
    return sessions

def generate_session_report(sessions):
    """Tạo báo cáo các phiên làm việc"""
    
    # Thống kê
    stats = {
        "total_sessions": len(sessions),
        "by_field": defaultdict(int),
        "by_priority": defaultdict(int),
        "by_module": defaultdict(int),
        "total_drugs": 0
    }
    
    for session in sessions:
        stats["by_field"][session["field"]] += 1
        stats["by_priority"][session["priority"]] += 1
        stats["by_module"][session["module"]] += 1
        stats["total_drugs"] += session["count"]
    
    # Tạo markdown report
    md = "# Kế Hoạch Các Phiên Làm Việc\n\n"
    md += f"**Tổng số phiên**: {stats['total_sessions']}\n"
    md += f"**Tổng số thuốc cần xử lý**: {stats['total_drugs']}\n\n"
    
    md += "## Thống Kê\n\n"
    md += "### Theo Field\n\n"
    for field, count in sorted(stats["by_field"].items()):
        md += f"- `{field}`: {count} phiên\n"
    
    md += "\n### Theo Priority\n\n"
    for priority, count in sorted(stats["by_priority"].items()):
        md += f"- **{priority}**: {count} phiên\n"
    
    md += "\n### Theo Module (Top 10)\n\n"
    sorted_modules = sorted(stats["by_module"].items(), key=lambda x: x[1], reverse=True)
    for module, count in sorted_modules[:10]:
        md += f"- `{module}`: {count} phiên\n"
    
    md += "\n## Danh Sách Phiên Làm Việc\n\n"
    
    # Nhóm theo field
    by_field = defaultdict(list)
    for session in sessions:
        by_field[session["field"]].append(session)
    
    for field in ["renal_adjustment", "drug_interactions", "contraindications_detail", "reversal_agents"]:
        if field not in by_field:
            continue
        
        field_sessions = by_field[field]
        md += f"### {field} ({len(field_sessions)} phiên)\n\n"
        
        # Nhóm theo module
        by_module = defaultdict(list)
        for session in field_sessions:
            by_module[session["module"]].append(session)
        
        for module in sorted(by_module.keys()):
            module_sessions = by_module[module]
            md += f"#### Module: {module} ({len(module_sessions)} phiên)\n\n"
            
            for session in module_sessions[:10]:  # Hiển thị 10 đầu tiên
                file_name = Path(session["file"]).name
                md += f"**Phiên {session['session_id']}** [{session['priority']}]: "
                md += f"{session['count']} thuốc trong `{file_name}`\n"
                md += f"- Danh sách: {', '.join(session['drugs'][:5])}"
                if len(session['drugs']) > 5:
                    md += f" và {len(session['drugs']) - 5} thuốc khác"
                md += "\n\n"
            
            if len(module_sessions) > 10:
                md += f"*... và {len(module_sessions) - 10} phiên khác*\n\n"
    
    return md, stats

def main():
    print("Đang tạo kế hoạch các phiên làm việc...")
    sessions = create_work_sessions()
    
    print("Đang tạo báo cáo...")
    report_md, stats = generate_session_report(sessions)
    
    # Lưu sessions JSON
    with open("work_sessions.json", "w", encoding="utf-8") as f:
        json.dump({
            "sessions": sessions,
            "statistics": stats
        }, f, indent=2, ensure_ascii=False)
    
    # Lưu markdown report
    with open("work_sessions_plan.md", "w", encoding="utf-8") as f:
        f.write(report_md)
    
    print(f"\n✅ Đã tạo kế hoạch:")
    print(f"   - work_sessions.json")
    print(f"   - work_sessions_plan.md")
    print(f"\n📊 Tóm tắt:")
    print(f"   - Tổng số phiên: {stats['total_sessions']}")
    print(f"   - Tổng số thuốc: {stats['total_drugs']}")
    print(f"   - High priority: {stats['by_priority']['high']} phiên")
    print(f"   - Medium priority: {stats['by_priority']['medium']} phiên")
    print(f"   - Low priority: {stats['by_priority']['low']} phiên")

if __name__ == "__main__":
    main()
