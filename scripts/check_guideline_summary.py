"""
Script tạo báo cáo tổng hợp ngắn gọn về guideline

Sử dụng:
    python scripts/check_guideline_summary.py
"""

from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import sys

# Import từ script chính
sys.path.insert(0, str(Path(__file__).parent))
from check_guideline_updates import GuidelineChecker, ARTICLES_DIR, CURRENT_YEAR

def create_summary():
    """Tạo báo cáo tổng hợp ngắn gọn"""
    checker = GuidelineChecker(ARTICLES_DIR)
    results = checker.scan_all_articles()
    
    # Thống kê
    needs_check = [r for r in results if r.get("needs_check", False)]
    no_check_needed = [r for r in results if not r.get("needs_check", False) and "error" not in r]
    
    # Thống kê guideline
    guideline_years = defaultdict(list)
    guideline_count = Counter()
    
    for result in results:
        if "error" in result:
            continue
        for guideline in result.get("guidelines", []):
            name = guideline["name"]
            year = guideline["year"]
            guideline_years[name].append(year)
            guideline_count[f"{name}"] += 1
    
    # Tạo báo cáo
    print("=" * 60)
    print("BÁO CÁO TỔNG HỢP GUIDELINE")
    print(f"Ngày: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Năm hiện tại: {CURRENT_YEAR}")
    print("=" * 60)
    print()
    
    print(f"📊 Tổng quan:")
    print(f"   - Tổng số file: {len(results)}")
    print(f"   - Cần kiểm tra: {len(needs_check)} ({len(needs_check)/len(results)*100:.1f}%)")
    print(f"   - Không cần kiểm tra: {len(no_check_needed)} ({len(no_check_needed)/len(results)*100:.1f}%)")
    print()
    
    print("🔍 Top guideline cần kiểm tra:")
    guideline_needs_check = defaultdict(int)
    for result in needs_check:
        for guideline in result.get("guidelines", []):
            name = guideline["name"]
            year = guideline["year"]
            guideline_needs_check[f"{name} {year}"] += 1
    
    for guideline, count in sorted(guideline_needs_check.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"   - {guideline}: {count} file")
    print()
    
    print("✅ Guideline mới nhất (top 15):")
    guideline_latest = {}
    for name, years in guideline_years.items():
        latest_year = max(years)
        guideline_latest[name] = latest_year
    
    for name, year in sorted(guideline_latest.items(), key=lambda x: x[1], reverse=True)[:15]:
        count = len([y for y in guideline_years[name] if y == year])
        print(f"   - {name} {year}: {count} file")
    print()
    
    print("⚠️  Guideline cũ nhất cần chú ý (top 10):")
    guideline_oldest = {}
    for name, years in guideline_years.items():
        oldest_year = min(years)
        guideline_oldest[name] = oldest_year
    
    for name, year in sorted(guideline_oldest.items(), key=lambda x: x[1])[:10]:
        count = len([y for y in guideline_years[name] if y == year])
        age = CURRENT_YEAR - year
        print(f"   - {name} {year} (đã {age} năm): {count} file")
    print()
    
    print("📋 File cần ưu tiên kiểm tra (top 10):")
    # Sắp xếp theo số lượng guideline cũ
    needs_check_sorted = sorted(needs_check, 
                                key=lambda x: len(x.get("reasons", [])), 
                                reverse=True)[:10]
    
    for i, result in enumerate(needs_check_sorted, 1):
        guidelines_str = ", ".join([f"{g['name']} {g['year']}" for g in result.get("guidelines", [])[:3]])
        print(f"   {i}. {result['file']}")
        print(f"      Guideline: {guidelines_str}")
        print(f"      Lý do: {len(result.get('reasons', []))} lý do")
    print()
    
    print("=" * 60)
    print(f"💡 Gợi ý: Chạy 'python scripts/check_guideline_updates.py' để xem báo cáo chi tiết")
    print("=" * 60)

if __name__ == "__main__":
    create_summary()

