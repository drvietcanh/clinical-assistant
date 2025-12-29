"""
Drug CLI - Command line interface để quản lý thuốc
Sử dụng: python -m drugs.drug_cli <command> [args]
"""

import sys
import argparse
from .drug_index import (
    search_drugs,
    find_drug_location,
    get_module_info,
    list_all_modules,
    get_drugs_by_module,
    MODULE_METADATA,
)
from .drug_manager import (
    find_drug_file,
    list_duplicate_drugs,
    get_module_statistics,
    export_module_structure,
    suggest_drug_placement,
)

def cmd_search(args):
    """Tìm kiếm thuốc"""
    results = search_drugs(args.query, args.module, args.by)
    
    if not results:
        print(f"Không tìm thấy thuốc nào với từ khóa '{args.query}'")
        return
    
    print(f"\nTìm thấy {len(results)} thuốc:\n")
    print(f"{'Tên thuốc':<40} {'Module':<25} {'Nhóm':<30}")
    print("-" * 100)
    
    for drug_name, module_name, drug_data in results[:args.limit]:
        group = drug_data.get("group", "N/A")
        print(f"{drug_name:<40} {module_name:<25} {group[:30]:<30}")
    
    if len(results) > args.limit:
        print(f"\n... và {len(results) - args.limit} kết quả khác")

def cmd_find(args):
    """Tìm vị trí file chứa thuốc"""
    locations = find_drug_location(args.drug_name)
    
    if not locations:
        print(f"Không tìm thấy thuốc '{args.drug_name}'")
        return
    
    print(f"\nThuốc '{args.drug_name}' được tìm thấy trong:\n")
    for module_name, file_path in locations:
        print(f"  Module: {module_name}")
        print(f"  File: {file_path}")
        
        # Try to find exact file
        exact_file = find_drug_file(args.drug_name)
        if exact_file:
            print(f"  File chính xác: {exact_file}")
        print()

def cmd_list_modules(args):
    """Liệt kê tất cả modules"""
    modules = list_all_modules(args.sort)
    
    print(f"\n{'Module':<30} {'Code':<8} {'Số lượng':<12} {'Mô tả':<50}")
    print("-" * 100)
    
    for module in modules:
        name = module.get("name", "")
        code = module.get("code", "")
        count = module.get("count", 0)
        desc = module.get("description", "")[:48]
        print(f"{name:<30} {code:<8} {count:<12} {desc:<50}")

def cmd_module_info(args):
    """Thông tin chi tiết về module"""
    info = get_module_info(args.module)
    
    if not info:
        print(f"Không tìm thấy module '{args.module}'")
        return
    
    print(f"\nThông tin module: {args.module}\n")
    print(f"Code: {info.get('code', 'N/A')}")
    print(f"Mô tả: {info.get('description', 'N/A')}")
    print(f"File path: {info.get('file_path', 'N/A')}")
    print(f"Độ ưu tiên: {info.get('priority', 'N/A')}")
    print(f"\nTừ khóa: {', '.join(info.get('keywords', []))}")
    print(f"\nDanh mục con:")
    for subcat in info.get('subcategories', []):
        print(f"  - {subcat}")
    
    # List drugs in module
    drugs = get_drugs_by_module(args.module, "name")
    print(f"\nSố thuốc: {len(drugs)}")
    if args.show_drugs:
        print("\nDanh sách thuốc:")
        for i, drug_name in enumerate(list(drugs.keys())[:20], 1):
            print(f"  {i}. {drug_name}")
        if len(drugs) > 20:
            print(f"  ... và {len(drugs) - 20} thuốc khác")

def cmd_duplicates(args):
    """Tìm thuốc trùng lặp"""
    duplicates = list_duplicate_drugs()
    
    if not duplicates:
        print("\nKhông có thuốc trùng lặp")
        return
    
    print(f"\nTìm thấy {len(duplicates)} thuốc trùng lặp:\n")
    print(f"{'Tên thuốc':<40} {'Số module':<12} {'Modules':<50}")
    print("-" * 110)
    
    for dup in duplicates[:args.limit]:
        drug_name = dup["drug_name"]
        count = dup["count"]
        modules = ", ".join(dup["modules"])
        print(f"{drug_name:<40} {count:<12} {modules[:48]:<50}")
    
    if len(duplicates) > args.limit:
        print(f"\n... và {len(duplicates) - args.limit} thuốc trùng lặp khác")

def cmd_statistics(args):
    """Thống kê tổng quan"""
    stats = get_module_statistics()
    
    print("\n" + "=" * 80)
    print("THỐNG KÊ HỆ THỐNG THUỐC")
    print("=" * 80)
    
    total = sum(s["count"] for s in stats.values())
    print(f"\nTổng số thuốc: {total}")
    print(f"Số module: {len(stats)}\n")
    
    # Sort by count
    sorted_stats = sorted(stats.items(), key=lambda x: x[1]["count"], reverse=True)
    
    print(f"{'Module':<30} {'Code':<8} {'Số lượng':<12} {'%':<10}")
    print("-" * 80)
    
    for module_name, data in sorted_stats:
        count = data["count"]
        percentage = (count / total * 100) if total > 0 else 0
        code = data.get("code", "")
        print(f"{module_name:<30} {code:<8} {count:<12} {percentage:>6.1f}%")

def cmd_export(args):
    """Xuất cấu trúc module"""
    output_file = export_module_structure(args.output)
    print(f"\nĐã xuất cấu trúc module ra file: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Drug Database Management CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Tìm kiếm thuốc')
    search_parser.add_argument('query', help='Từ khóa tìm kiếm')
    search_parser.add_argument('--module', help='Giới hạn trong module')
    search_parser.add_argument('--by', choices=['name', 'keyword', 'group', 'indication', 'all'],
                               default='all', help='Cách tìm kiếm')
    search_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Find command
    find_parser = subparsers.add_parser('find', help='Tìm file chứa thuốc')
    find_parser.add_argument('drug_name', help='Tên thuốc')
    
    # List modules command
    list_parser = subparsers.add_parser('list', help='Liệt kê modules')
    list_parser.add_argument('--sort', choices=['name', 'priority', 'count'],
                            default='name', help='Cách sắp xếp')
    
    # Module info command
    info_parser = subparsers.add_parser('info', help='Thông tin module')
    info_parser.add_argument('module', help='Tên module')
    info_parser.add_argument('--show-drugs', action='store_true', help='Hiển thị danh sách thuốc')
    
    # Duplicates command
    dup_parser = subparsers.add_parser('duplicates', help='Tìm thuốc trùng lặp')
    dup_parser.add_argument('--limit', type=int, default=20, help='Số kết quả tối đa')
    
    # Statistics command
    stats_parser = subparsers.add_parser('stats', help='Thống kê')
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Xuất cấu trúc')
    export_parser.add_argument('--output', default='drug_module_structure.json',
                              help='File output')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    commands = {
        'search': cmd_search,
        'find': cmd_find,
        'list': cmd_list_modules,
        'info': cmd_module_info,
        'duplicates': cmd_duplicates,
        'stats': cmd_statistics,
        'export': cmd_export,
    }
    
    commands[args.command](args)

if __name__ == '__main__':
    main()

