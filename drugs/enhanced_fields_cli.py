"""
Enhanced Fields CLI - Command line interface để quản lý Enhanced Fields
"""

import sys
import argparse
from .enhanced_fields_index import (
    find_drugs_with_field,
    find_drugs_missing_fields,
    find_drugs_with_complete_fields,
    get_drug_field_status,
    search_fields_by_content,
    get_field_statistics,
    print_field_statistics,
    ALL_ENHANCED_FIELDS,
    FIELD_METADATA,
)
from .enhanced_fields_manager import (
    find_drugs_needing_fields,
    get_field_completion_report,
    suggest_field_content,
    generate_field_code,
    validate_drug_fields,
    export_field_completion_report,
)

def cmd_stats(args):
    """Thống kê fields"""
    print_field_statistics()

def cmd_missing(args):
    """Tìm thuốc thiếu fields"""
    fields = args.fields if args.fields else ALL_ENHANCED_FIELDS
    
    results = find_drugs_needing_fields(fields, limit=args.limit)
    
    if not results:
        print(f"\nKhông tìm thấy thuốc thiếu fields: {', '.join(fields)}")
        return
    
    print(f"\nTìm thấy {len(results)} thuốc thiếu fields:\n")
    print(f"{'Thuốc':<40} {'Fields thiếu':<30} {'File':<50}")
    print("-" * 120)
    
    for drug_name, missing_fields, file_path in results:
        missing_str = ", ".join(missing_fields[:3])
        if len(missing_fields) > 3:
            missing_str += f" (+{len(missing_fields)-3})"
        print(f"{drug_name:<40} {missing_str:<30} {file_path[:48]:<50}")

def cmd_status(args):
    """Trạng thái fields của một thuốc"""
    status = get_drug_field_status(args.drug_name)
    
    if not status:
        print(f"\nKhông tìm thấy thuốc '{args.drug_name}'")
        return
    
    print(f"\nTrạng thái fields của '{args.drug_name}':\n")
    
    # Group by category
    core_fields = [f for f in ALL_ENHANCED_FIELDS if FIELD_METADATA.get(f, {}).get("category") == "core"]
    extended_fields = [f for f in ALL_ENHANCED_FIELDS if FIELD_METADATA.get(f, {}).get("category") == "extended"]
    
    print("=== 6 FIELDS CƠ BẢN ===")
    for field in core_fields:
        has = "✓" if status.get(field, False) else "✗"
        print(f"  {has} {field}")
    
    print("\n=== 8 FIELDS BỔ SUNG ===")
    for field in extended_fields:
        has = "✓" if status.get(field, False) else "✗"
        print(f"  {has} {field}")
    
    # Summary
    total = len([f for f in status.values() if f])
    print(f"\nTổng: {total}/14 fields")

def cmd_search(args):
    """Tìm kiếm trong nội dung fields"""
    results = search_fields_by_content(args.query, args.field)
    
    if not results:
        print(f"\nKhông tìm thấy kết quả với từ khóa '{args.query}'")
        return
    
    print(f"\nTìm thấy {len(results)} kết quả:\n")
    print(f"{'Thuốc':<30} {'Field':<25} {'Nội dung':<50}")
    print("-" * 110)
    
    for drug_name, field_name, content in results[:args.limit]:
        content_short = content[:47] + "..." if len(content) > 50 else content
        print(f"{drug_name:<30} {field_name:<25} {content_short:<50}")
    
    if len(results) > args.limit:
        print(f"\n... và {len(results) - args.limit} kết quả khác")

def cmd_suggest(args):
    """Gợi ý nội dung cho field"""
    suggestion = suggest_field_content(args.drug_name, args.field)
    
    if not suggestion:
        print(f"\nKhông có gợi ý cho {args.field} của {args.drug_name}")
        return
    
    print(f"\nGợi ý cho {args.field} của {args.drug_name}:\n")
    print("Nội dung gợi ý:")
    import json
    print(json.dumps(suggestion["suggestions"], ensure_ascii=False, indent=2))
    print(f"\nLưu ý: {suggestion['note']}")

def cmd_validate(args):
    """Validate fields của thuốc"""
    is_valid, errors = validate_drug_fields(args.drug_name)
    
    if is_valid:
        print(f"\n✓ Thuốc '{args.drug_name}' có fields hợp lệ")
    else:
        print(f"\n✗ Thuốc '{args.drug_name}' có lỗi:")
        for error in errors:
            print(f"  - {error}")

def cmd_complete(args):
    """Liệt kê thuốc đủ fields"""
    drugs = find_drugs_with_complete_fields(count=args.count)
    
    print(f"\nTìm thấy {len(drugs)} thuốc có đủ {args.count} fields:\n")
    
    for i, drug_name in enumerate(drugs[:args.limit], 1):
        print(f"  {i}. {drug_name}")
    
    if len(drugs) > args.limit:
        print(f"\n... và {len(drugs) - args.limit} thuốc khác")

def cmd_report(args):
    """Xuất báo cáo"""
    output_file = export_field_completion_report(args.output)
    print(f"\nĐã xuất báo cáo ra file: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Enhanced Fields Management CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Thống kê fields')
    
    # Missing command
    missing_parser = subparsers.add_parser('missing', help='Tìm thuốc thiếu fields')
    missing_parser.add_argument('--fields', nargs='+', help='Fields cần kiểm tra')
    missing_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Trạng thái fields của thuốc')
    status_parser.add_argument('drug_name', help='Tên thuốc')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Tìm kiếm trong fields')
    search_parser.add_argument('query', help='Từ khóa tìm kiếm')
    search_parser.add_argument('--field', help='Giới hạn trong field cụ thể')
    search_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Suggest command
    suggest_parser = subparsers.add_parser('suggest', help='Gợi ý nội dung field')
    suggest_parser.add_argument('drug_name', help='Tên thuốc')
    suggest_parser.add_argument('field', help='Tên field')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate fields')
    validate_parser.add_argument('drug_name', help='Tên thuốc')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Thuốc đủ fields')
    complete_parser.add_argument('--count', type=int, default=14, help='Số fields cần có')
    complete_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Xuất báo cáo')
    report_parser.add_argument('--output', default='field_completion_report.json', help='File output')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    commands = {
        'stats': cmd_stats,
        'missing': cmd_missing,
        'status': cmd_status,
        'search': cmd_search,
        'suggest': cmd_suggest,
        'validate': cmd_validate,
        'complete': cmd_complete,
        'report': cmd_report,
    }
    
    commands[args.command](args)

if __name__ == '__main__':
    main()

