"""
CLI Tool cho quản lý thuốc
Commands: search, find, check-fields, stats, missing-fields, export
"""
import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from .drug_index_system import DrugIndex, get_drug_index
from .drug_manager_tool import DrugManager, get_drug_manager

def cmd_search(args):
    """Command: search - Tìm kiếm thuốc"""
    index = get_drug_index()
    results = index.search(args.query, fuzzy=args.fuzzy)
    
    if not results:
        print(f"No drugs found matching '{args.query}'")
        return
    
    print(f"Found {len(results)} drug(s):")
    for i, drug_name in enumerate(results[:args.limit], 1):
        drug_info = index.get_drug_info(drug_name)
        if drug_info:
            module = drug_info.get('module', 'unknown')
            group = drug_info.get('group', 'N/A')
            print(f"{i}. {drug_name}")
            print(f"   Module: {module}")
            print(f"   Group: {group}")
            if args.verbose:
                print(f"   File: {drug_info.get('file', 'N/A')}")
        else:
            print(f"{i}. {drug_name}")
        print()

def cmd_find(args):
    """Command: find - Tìm file chứa thuốc"""
    manager = get_drug_manager()
    files = manager.find_drug_file(args.drug_name)
    
    if not files:
        print(f"Drug '{args.drug_name}' not found")
        return
    
    print(f"Drug '{args.drug_name}' found in:")
    for file_path in files:
        print(f"  - {file_path}")

def cmd_check_fields(args):
    """Command: check-fields - Kiểm tra field của thuốc"""
    manager = get_drug_manager()
    index = get_drug_index()
    
    drug_info = index.get_drug_info(args.drug_name)
    if not drug_info:
        print(f"Drug '{args.drug_name}' not found")
        return
    
    # Get full drug data
    try:
        from drugs.drug_database import DRUG_DATABASE
        drug_data = DRUG_DATABASE.get(args.drug_name, {})
    except ImportError:
        drug_data = drug_info
    
    validation = manager.validate_drug_structure(drug_data)
    
    print(f"Field check for '{args.drug_name}':")
    print(f"Valid: {validation['valid']}")
    
    if validation['errors']:
        print("\nErrors:")
        for error in validation['errors']:
            print(f"  - {error}")
    
    if validation['warnings']:
        print("\nWarnings:")
        for warning in validation['warnings']:
            print(f"  - {warning}")
    
    if validation['missing_fields']:
        print("\nMissing fields:")
        for field in validation['missing_fields']:
            print(f"  - {field}")
    
    if validation['extra_fields']:
        print("\nExtra fields:")
        for field in validation['extra_fields']:
            print(f"  - {field}")

def cmd_stats(args):
    """Command: stats - Thống kê"""
    index = get_drug_index()
    stats = index.get_statistics()
    
    if args.module:
        # Stats for specific module
        drugs = index.search_by_module(args.module)
        print(f"Module '{args.module}':")
        print(f"  Total drugs: {len(drugs)}")
        if args.verbose:
            print("\nDrugs:")
            for drug_name in sorted(drugs)[:20]:
                print(f"  - {drug_name}")
    else:
        # Overall stats
        print("Drug System Statistics:")
        print(f"  Total drugs: {stats['total_drugs']}")
        print(f"  Total modules: {stats['total_modules']}")
        print(f"  Total groups: {stats['total_groups']}")
        print(f"  Total indications: {stats['total_indications']}")
        print(f"  Total fields: {stats['total_fields']}")
        
        if args.verbose:
            print("\nModules:")
            for module, count in sorted(stats['modules'].items(), key=lambda x: x[1], reverse=True):
                print(f"  {module}: {count} drugs")
            
            print("\nTop Groups:")
            for group, count in sorted(stats['groups'].items(), key=lambda x: x[1], reverse=True)[:10]:
                print(f"  {group}: {count} drugs")

def cmd_missing_fields(args):
    """Command: missing-fields - Tìm thuốc thiếu field"""
    from check_all_drug_fields_comprehensive import scan_all_drugs, generate_statistics
    
    print("Scanning all drugs...")
    all_drugs = scan_all_drugs()
    
    if args.module and args.module != 'all':
        # Filter by module
        filtered = {}
        for drug_name, drug_info in all_drugs.items():
            module = drug_info.get('file', '').split('/')[2] if '/' in drug_info.get('file', '') else 'unknown'
            if module == args.module:
                filtered[drug_name] = drug_info
        all_drugs = filtered
    
    # Find drugs with missing fields
    STANDARD_14_FIELDS = [
        "group", "vietnamese_name", "administration", "indications", "dosage",
        "side_effects", "contraindications", "interactions", "pregnancy",
        "mechanism_of_action", "monitoring", "precautions", "pharmacokinetics", "storage"
    ]
    
    ADDITIONAL_8_FIELDS = [
        "black_box_warnings", "drug_interactions", "pregnancy_lactation",
        "hepatic_adjustment", "overdose_management", "reversal_agents",
        "administration_instructions", "references"
    ]
    
    missing_drugs = []
    for drug_name, drug_info in all_drugs.items():
        missing_standard = [f for f in STANDARD_14_FIELDS if f not in drug_info.get('fields', [])]
        missing_additional = [f for f in ADDITIONAL_8_FIELDS if f not in drug_info.get('fields', [])]
        
        if missing_standard or (missing_additional and args.include_additional):
            missing_drugs.append({
                'name': drug_name,
                'file': drug_info.get('file', 'N/A'),
                'missing_standard': missing_standard,
                'missing_additional': missing_additional,
                'missing_count': len(missing_standard) + (len(missing_additional) if args.include_additional else 0)
            })
    
    # Sort by missing count
    missing_drugs.sort(key=lambda x: x['missing_count'], reverse=True)
    
    print(f"\nFound {len(missing_drugs)} drugs with missing fields:")
    for drug in missing_drugs[:args.limit]:
        print(f"\n{drug['name']} ({drug['missing_count']} missing):")
        print(f"  File: {drug['file']}")
        if drug['missing_standard']:
            print(f"  Missing standard: {', '.join(drug['missing_standard'])}")
        if drug['missing_additional'] and args.include_additional:
            print(f"  Missing additional: {', '.join(drug['missing_additional'])}")

def cmd_export(args):
    """Command: export - Export dữ liệu"""
    index = get_drug_index()
    manager = get_drug_manager()
    
    if args.drug:
        # Export single drug
        drug_info = index.get_drug_info(args.drug)
        if not drug_info:
            print(f"Drug '{args.drug}' not found")
            return
        
        try:
            from drugs.drug_database import DRUG_DATABASE
            drug_data = DRUG_DATABASE.get(args.drug, {})
        except ImportError:
            drug_data = drug_info
        
        if args.format == 'json':
            output = json.dumps({args.drug: drug_data}, indent=2, ensure_ascii=False)
        else:
            output = manager.export_drug(args.drug, format='python')
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Exported to {args.output}")
        else:
            print(output)
    
    elif args.module:
        # Export module
        drugs = index.search_by_module(args.module)
        if not drugs:
            print(f"No drugs found in module '{args.module}'")
            return
        
        try:
            from drugs.drug_database import DRUG_DATABASE
            module_data = {name: DRUG_DATABASE.get(name, {}) for name in drugs}
        except ImportError:
            module_data = {name: index.get_drug_info(name) for name in drugs}
        
        output = json.dumps(module_data, indent=2, ensure_ascii=False)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Exported {len(drugs)} drugs to {args.output}")
        else:
            print(output)
    
    else:
        # Export all
        print("Exporting all drugs...")
        try:
            from drugs.drug_database import DRUG_DATABASE
            all_data = DRUG_DATABASE
        except ImportError:
            all_data = {name: index.get_drug_info(name) for name in index.drugs.keys()}
        
        output = json.dumps(all_data, indent=2, ensure_ascii=False)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Exported {len(all_data)} drugs to {args.output}")
        else:
            print(output[:1000] + "..." if len(output) > 1000 else output)

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(description='Drug Management CLI Tool')
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # search command
    search_parser = subparsers.add_parser('search', help='Search drugs')
    search_parser.add_argument('query', help='Search query')
    search_parser.add_argument('--fuzzy', action='store_true', help='Use fuzzy search')
    search_parser.add_argument('--limit', type=int, default=10, help='Limit results')
    search_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    search_parser.set_defaults(func=cmd_search)
    
    # find command
    find_parser = subparsers.add_parser('find', help='Find file containing drug')
    find_parser.add_argument('drug_name', help='Drug name')
    find_parser.set_defaults(func=cmd_find)
    
    # check-fields command
    check_parser = subparsers.add_parser('check-fields', help='Check drug fields')
    check_parser.add_argument('drug_name', help='Drug name')
    check_parser.set_defaults(func=cmd_check_fields)
    
    # stats command
    stats_parser = subparsers.add_parser('stats', help='Show statistics')
    stats_parser.add_argument('--module', help='Module name (optional)')
    stats_parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    stats_parser.set_defaults(func=cmd_stats)
    
    # missing-fields command
    missing_parser = subparsers.add_parser('missing-fields', help='Find drugs with missing fields')
    missing_parser.add_argument('--module', default='all', help='Module name (default: all)')
    missing_parser.add_argument('--include-additional', action='store_true', help='Include additional fields')
    missing_parser.add_argument('--limit', type=int, default=20, help='Limit results')
    missing_parser.set_defaults(func=cmd_missing_fields)
    
    # export command
    export_parser = subparsers.add_parser('export', help='Export drugs')
    export_parser.add_argument('--drug', help='Drug name (optional)')
    export_parser.add_argument('--module', help='Module name (optional)')
    export_parser.add_argument('--format', choices=['json', 'python'], default='json', help='Export format')
    export_parser.add_argument('--output', '-o', help='Output file (optional)')
    export_parser.set_defaults(func=cmd_export)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        if args.verbose if hasattr(args, 'verbose') else False:
            traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
