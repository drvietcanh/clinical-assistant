"""
Script nhanh để kiểm tra module - Chạy: python check_modules.py
"""

from utils.module_analyzer import ModuleAnalyzer
import sys

def main():
    print("=" * 80)
    print("🔍 KIỂM TRA MODULE - PHÂN TÍCH ĐỘ DÀI VÀ ĐỀ XUẤT TÁCH")
    print("=" * 80)
    print()
    
    analyzer = ModuleAnalyzer(".")
    results = analyzer.analyze_all()
    
    # Thống kê
    critical = [r for r in results if r.lines > 800]
    warning = [r for r in results if 500 < r.lines <= 800]
    ok = [r for r in results if r.lines <= 500]
    
    print(f"📊 TỔNG QUAN:")
    print(f"   - 🔴 CRITICAL (>800 dòng): {len(critical)} files")
    print(f"   - 🟡 WARNING (500-800 dòng): {len(warning)} files")
    print(f"   - ✅ OK (≤500 dòng): {len(ok)} files")
    print()
    
    # Top 10
    print("📋 TOP 10 FILE DÀI NHẤT:")
    print("-" * 80)
    for i, r in enumerate(results[:10], 1):
        status = "🔴" if r.lines > 800 else "🟡" if r.lines > 500 else "✅"
        data_info = "📊" if r.has_data_dict else ""
        print(f"{i:2}. {status} {r.lines:5} dòng {data_info:2} | {r.file_path}")
    print()
    
    # Chi tiết các file critical
    if critical:
        print("🔴 CẦN TÁCH NGAY (CRITICAL):")
        print("-" * 80)
        for r in critical[:5]:  # Top 5 critical
            print(f"\n📄 {r.file_path}")
            print(f"   - Dòng: {r.lines} (code: {r.code_lines})")
            print(f"   - Classes: {len(r.classes)}, Functions: {len(r.functions)}")
            if r.has_data_dict:
                print(f"   - Data dict: ~{r.data_dict_size} entries")
            if r.suggestions:
                print(f"   - Gợi ý:")
                for s in r.suggestions[:3]:
                    print(f"     • {s}")
            if r.split_recommendation:
                print(f"   - Đề xuất tách:")
                for line in r.split_recommendation.split('\n')[:5]:
                    print(f"     {line}")
        print()
    
    # Tạo report đầy đủ
    print("📝 Đang tạo báo cáo chi tiết...")
    analyzer.generate_report()
    print("✅ Đã tạo: module_analysis_report.md")
    print()
    
    # Tạo kế hoạch tách
    if critical:
        print("💡 Tạo kế hoạch tách module? (y/n): ", end="")
        if len(sys.argv) > 1 and sys.argv[1] == "--auto":
            create_plan = True
        else:
            try:
                create_plan = input().strip().lower() == 'y'
            except:
                create_plan = False
        
        if create_plan:
            create_split_plan(analyzer, critical)
    
    return analyzer


def create_split_plan(analyzer: ModuleAnalyzer, critical_files: list):
    """Tạo file kế hoạch tách module chi tiết"""
    from pathlib import Path
    from datetime import datetime
    
    plan = []
    plan.append("# KẾ HOẠCH TÁCH MODULE\n\n")
    plan.append(f"**Ngày tạo:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    plan.append("## 📋 TỔNG QUAN\n\n")
    plan.append(f"- **Số file cần tách:** {len(critical_files)}\n")
    plan.append(f"- **Ưu tiên:** Tách theo thứ tự từ file dài nhất\n\n")
    
    plan.append("## 🎯 KẾ HOẠCH CHI TIẾT\n\n")
    
    for i, r in enumerate(critical_files, 1):
        plan.append(f"### {i}. {r.file_path}\n\n")
        plan.append(f"**Thông tin:**\n")
        plan.append(f"- Dòng: {r.lines} (code: {r.code_lines})\n")
        plan.append(f"- Classes: {len(r.classes)}\n")
        plan.append(f"- Functions: {len(r.functions)}\n")
        plan.append(f"- Data dict: {'Có' if r.has_data_dict else 'Không'}\n\n")
        
        plan.append("**Phương án tách:**\n\n")
        
        if r.split_recommendation:
            plan.append("```\n")
            plan.append(r.split_recommendation)
            plan.append("\n```\n\n")
        else:
            # Đề xuất mặc định
            if r.has_data_dict:
                plan.append("1. Tách data dictionary ra file riêng (`.data.py`)\n")
                plan.append("2. Giữ logic và functions trong file gốc\n")
                plan.append("3. Import data từ file mới\n\n")
            elif len(r.classes) > 0:
                plan.append("1. Tách mỗi class ra file riêng\n")
                plan.append("2. Tạo package và `__init__.py` để export\n\n")
            else:
                plan.append("1. Phân tích các nhóm functions\n")
                plan.append("2. Tách theo chức năng (utils, calculators, helpers...)\n\n")
        
        plan.append("**Bước thực hiện:**\n\n")
        plan.append("```\n")
        plan.append("# TODO: Thêm các bước cụ thể\n")
        plan.append("1. [ ] Bước 1\n")
        plan.append("2. [ ] Bước 2\n")
        plan.append("3. [ ] Bước 3\n")
        plan.append("4. [ ] Test sau khi tách\n")
        plan.append("```\n\n")
        plan.append("---\n\n")
    
    plan.append("## ✅ CHECKLIST TỔNG QUAN\n\n")
    for i, r in enumerate(critical_files, 1):
        plan.append(f"- [ ] {r.file_path} ({r.lines} dòng)\n")
    
    # Lưu file
    plan_text = ''.join(plan)
    output_path = Path("module_split_plan.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(plan_text)
    
    print(f"✅ Đã tạo: {output_path}")


if __name__ == "__main__":
    main()

