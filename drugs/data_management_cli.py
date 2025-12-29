"""
Data Management CLI - Command line interface để quản lý dữ liệu thuốc
Tổng hợp tất cả tính năng quản lý, kiểm tra, tìm kiếm
"""

import sys
import argparse
from .data_quality_manager import (
    check_all_quality,
    calculate_quality_metrics,
    DataQualityError,
)
from .data_integrity_checker import check_all_integrity
from .data_search_enhancer import (
    fuzzy_search_drugs,
    search_by_multiple_criteria,
    get_search_suggestions,
)
from .data_backup_manager import (
    create_backup,
    list_backups,
    restore_backup,
)
from .drug_manager import find_drug_file, list_duplicate_drugs
from .enhanced_fields_manager import find_drugs_needing_fields

def cmd_quality(args):
    """Kiểm tra chất lượng dữ liệu"""
    if args.drug:
        errors = check_all_quality(drug_name=args.drug)
    else:
        errors = check_all_quality()
    
    if not errors:
        print("\n✓ Không có lỗi chất lượng dữ liệu")
        return
    
    # Group by severity
    by_severity = {"error": [], "warning": [], "info": []}
    for error in errors:
        by_severity[error.severity].append(error)
    
    print(f"\nTìm thấy {len(errors)} vấn đề:\n")
    print(f"  Errors: {len(by_severity['error'])}")
    print(f"  Warnings: {len(by_severity['warning'])}")
    print(f"  Info: {len(by_severity['info'])}\n")
    
    # Show errors
    if by_severity["error"]:
        print("=== ERRORS ===")
        for error in by_severity["error"][:args.limit]:
            print(f"  {error}")
    
    # Show warnings
    if by_severity["warning"] and args.show_warnings:
        print("\n=== WARNINGS ===")
        for error in by_severity["warning"][:args.limit]:
            print(f"  {error}")
    
    if len(errors) > args.limit:
        print(f"\n... và {len(errors) - args.limit} vấn đề khác")

def cmd_metrics(args):
    """Chỉ số chất lượng"""
    metrics = calculate_quality_metrics()
    
    print("\n" + "=" * 80)
    print("CHỈ SỐ CHẤT LƯỢNG DỮ LIỆU")
    print("=" * 80)
    print(f"\nTổng số thuốc: {metrics['total_drugs']}")
    print(f"Tổng số lỗi: {metrics['total_errors']}")
    print(f"Điểm chất lượng: {metrics['quality_score']:.1f}/100")
    print(f"Tỷ lệ lỗi: {metrics['error_rate']:.1f}%")
    
    print("\nPhân bố theo mức độ:")
    for severity, count in metrics['by_severity'].items():
        print(f"  {severity}: {count}")
    
    print("\nTop 10 loại lỗi:")
    for error_type, count in metrics['top_issues']:
        print(f"  {error_type}: {count}")

def cmd_integrity(args):
    """Kiểm tra tính toàn vẹn"""
    result = check_all_integrity()
    
    print("\n" + "=" * 80)
    print("KIỂM TRA TÍNH TOÀN VẸN DỮ LIỆU")
    print("=" * 80)
    print(f"\nTổng số vấn đề: {result['total_issues']}")
    print(f"Thuốc bị ảnh hưởng: {result['drugs_affected']}")
    
    print("\nPhân bố theo mức độ:")
    for severity, count in result['by_severity'].items():
        print(f"  {severity}: {count}")
    
    print("\nPhân bố theo loại:")
    for issue_type, count in sorted(result['by_issue_type'].items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {issue_type}: {count}")
    
    if args.show_issues:
        print("\nChi tiết (10 đầu tiên):")
        for issue in result['issues'][:10]:
            print(f"  {issue['drug']}.{issue['field']}: {issue['message']}")

def cmd_search(args):
    """Tìm kiếm nâng cao"""
    if args.fuzzy:
        results = fuzzy_search_drugs(args.query, threshold=args.threshold, limit=args.limit)
        print(f"\nTìm thấy {len(results)} kết quả (fuzzy search):\n")
        print(f"{'Thuốc':<40} {'Độ tương đồng':<15} {'Nhóm':<30}")
        print("-" * 90)
        for drug_name, score, drug_data in results:
            group = drug_data.get("group", "N/A")[:28]
            print(f"{drug_name:<40} {score:>6.2%} {'':<8} {group:<30}")
    else:
        results = search_by_multiple_criteria(
            name=args.query if args.query else None,
            group=args.group,
            indication=args.indication,
            administration=args.administration,
        )
        print(f"\nTìm thấy {len(results)} kết quả:\n")
        print(f"{'Thuốc':<40} {'Nhóm':<30}")
        print("-" * 70)
        for drug_name, drug_data in results[:args.limit]:
            group = drug_data.get("group", "N/A")[:28]
            print(f"{drug_name:<40} {group:<30}")

def cmd_suggest(args):
    """Gợi ý tìm kiếm"""
    suggestions = get_search_suggestions(args.query, limit=args.limit)
    
    if not suggestions:
        print(f"\nKhông có gợi ý cho '{args.query}'")
        return
    
    print(f"\nGợi ý tìm kiếm cho '{args.query}':\n")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"  {i}. {suggestion}")

def cmd_backup(args):
    """Tạo backup"""
    backup_file = create_backup(args.dir, include_overrides=args.include_overrides)
    print(f"\n✓ Đã tạo backup: {backup_file}")

def cmd_list_backups(args):
    """Liệt kê backups"""
    backups = list_backups(args.dir)
    
    if not backups:
        print(f"\nKhông có backup nào trong {args.dir}")
        return
    
    print(f"\nTìm thấy {len(backups)} backup(s):\n")
    print(f"{'File':<50} {'Ngày':<20} {'Số thuốc':<12}")
    print("-" * 85)
    
    for backup in backups[:args.limit]:
        file_name = Path(backup["file"]).name
        date = backup.get("date", "")[:19] if backup.get("date") else ""
        count = backup.get("total_drugs", 0)
        print(f"{file_name:<50} {date:<20} {count:<12}")

def cmd_duplicates(args):
    """Tìm thuốc trùng lặp"""
    duplicates = list_duplicate_drugs()
    
    if not duplicates:
        print("\n✓ Không có thuốc trùng lặp")
        return
    
    print(f"\nTìm thấy {len(duplicates)} thuốc trùng lặp:\n")
    print(f"{'Thuốc':<40} {'Số module':<12} {'Modules':<50}")
    print("-" * 110)
    
    for dup in duplicates[:args.limit]:
        drug_name = dup["drug_name"]
        count = dup["count"]
        modules = ", ".join(dup["modules"])
        print(f"{drug_name:<40} {count:<12} {modules[:48]:<50}")
    
    if len(duplicates) > args.limit:
        print(f"\n... và {len(duplicates) - args.limit} thuốc trùng lặp khác")

def cmd_missing_fields(args):
    """Tìm thuốc thiếu fields"""
    fields = args.fields if args.fields else ["drug_interactions", "pregnancy_lactation"]
    
    results = find_drugs_needing_fields(fields, limit=args.limit)
    
    if not results:
        print(f"\n✓ Không có thuốc thiếu fields: {', '.join(fields)}")
        return
    
    print(f"\nTìm thấy {len(results)} thuốc thiếu fields:\n")
    print(f"{'Thuốc':<40} {'Fields thiếu':<30} {'File':<50}")
    print("-" * 120)
    
    for drug_name, missing_fields, file_path in results:
        missing_str = ", ".join(missing_fields[:2])
        if len(missing_fields) > 2:
            missing_str += f" (+{len(missing_fields)-2})"
        print(f"{drug_name:<40} {missing_str:<30} {file_path[:48]:<50}")

def main():
    parser = argparse.ArgumentParser(description="Drug Data Management CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Quality command
    quality_parser = subparsers.add_parser('quality', help='Kiểm tra chất lượng')
    quality_parser.add_argument('--drug', help='Kiểm tra một thuốc cụ thể')
    quality_parser.add_argument('--show-warnings', action='store_true', help='Hiển thị warnings')
    quality_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Metrics command
    metrics_parser = subparsers.add_parser('metrics', help='Chỉ số chất lượng')
    
    # Integrity command
    integrity_parser = subparsers.add_parser('integrity', help='Kiểm tra tính toàn vẹn')
    integrity_parser.add_argument('--show-issues', action='store_true', help='Hiển thị chi tiết')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Tìm kiếm nâng cao')
    search_parser.add_argument('query', nargs='?', help='Từ khóa tìm kiếm')
    search_parser.add_argument('--fuzzy', action='store_true', help='Fuzzy search')
    search_parser.add_argument('--threshold', type=float, default=0.6, help='Ngưỡng tương đồng')
    search_parser.add_argument('--group', help='Lọc theo nhóm')
    search_parser.add_argument('--indication', help='Lọc theo chỉ định')
    search_parser.add_argument('--administration', help='Lọc theo đường dùng')
    search_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Suggest command
    suggest_parser = subparsers.add_parser('suggest', help='Gợi ý tìm kiếm')
    suggest_parser.add_argument('query', help='Từ khóa')
    suggest_parser.add_argument('--limit', type=int, default=5, help='Số gợi ý')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Tạo backup')
    backup_parser.add_argument('--dir', default='drug_data_backups', help='Thư mục backup')
    backup_parser.add_argument('--include-overrides', action='store_true', default=True, help='Bao gồm overrides')
    
    # List backups command
    list_backups_parser = subparsers.add_parser('list-backups', help='Liệt kê backups')
    list_backups_parser.add_argument('--dir', default='drug_data_backups', help='Thư mục backup')
    list_backups_parser.add_argument('--limit', type=int, default=10, help='Số backup hiển thị')
    
    # Duplicates command
    dup_parser = subparsers.add_parser('duplicates', help='Tìm thuốc trùng lặp')
    dup_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Missing fields command
    missing_parser = subparsers.add_parser('missing-fields', help='Tìm thuốc thiếu fields')
    missing_parser.add_argument('--fields', nargs='+', help='Fields cần kiểm tra')
    missing_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    commands = {
        'quality': cmd_quality,
        'metrics': cmd_metrics,
        'integrity': cmd_integrity,
        'search': cmd_search,
        'suggest': cmd_suggest,
        'backup': cmd_backup,
        'list-backups': cmd_list_backups,
        'duplicates': cmd_duplicates,
        'missing-fields': cmd_missing_fields,
    }
    
    commands[args.command](args)

if __name__ == '__main__':
    main()

