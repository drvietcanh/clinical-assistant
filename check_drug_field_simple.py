"""
Script đơn giản để kiểm tra field của một hoặc nhiều thuốc
Dễ sử dụng, dễ tìm kiếm
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))

from drug_manager import DrugManager

def main():
    """Main function"""
    manager = DrugManager()
    
    print("\n" + "=" * 70)
    print("KIEM TRA FIELD CUA THUOC")
    print("=" * 70)
    print()
    
    if len(sys.argv) < 2:
        print("Cach su dung:")
        print("  python check_drug_field_simple.py <ten_thuoc>")
        print("  python check_drug_field_simple.py <ten_thuoc> --all")
        print("  python check_drug_field_simple.py --list-missing <field_name>")
        print("  python check_drug_field_simple.py --stats")
        print()
        print("Vi du:")
        print("  python check_drug_field_simple.py Gentamicin")
        print("  python check_drug_field_simple.py --list-missing references")
        print("  python check_drug_field_simple.py --stats")
        return
    
    arg = sys.argv[1]
    
    if arg == '--stats':
        stats = manager.get_statistics()
        print(f"Tong so thuoc: {stats['total_drugs']}")
        print()
        
        # Thống kê theo loại field
        print("THIEU CORE FIELDS:")
        for field in ['group', 'vietnamese_name', 'administration', 'indications', 'dosage']:
            stat = stats['fields_stats'][field]
            if stat['missing'] > 0:
                print(f"  - {field}: {stat['missing']} thuoc thieu ({stat['percentage']}% co)")
        
        print("\nTHIEU EXTENDED FIELDS:")
        for field in ['side_effects', 'contraindications', 'interactions', 'pregnancy']:
            stat = stats['fields_stats'][field]
            if stat['missing'] > 0:
                print(f"  - {field}: {stat['missing']} thuoc thieu ({stat['percentage']}% co)")
        
        print("\nTHIEU ENHANCED FIELDS (top 10):")
        enhanced_stats = []
        for field in ['mechanism_of_action', 'monitoring', 'precautions', 'pharmacokinetics',
                     'storage', 'black_box_warnings', 'drug_interactions', 'pregnancy_lactation',
                     'hepatic_adjustment', 'overdose_management', 'reversal_agents',
                     'administration_instructions', 'references']:
            stat = stats['fields_stats'][field]
            if stat['missing'] > 0:
                enhanced_stats.append((field, stat))
        
        enhanced_stats.sort(key=lambda x: x[1]['missing'], reverse=True)
        for field, stat in enhanced_stats[:10]:
            print(f"  - {field}: {stat['missing']} thuoc thieu ({stat['percentage']}% co)")
    
    elif arg == '--list-missing':
        if len(sys.argv) < 3:
            print("Can chi dinh ten field")
            print("Vi du: python check_drug_field_simple.py --list-missing references")
            return
        
        field_name = sys.argv[2]
        drugs = manager.find_drugs_missing_field(field_name)
        
        print(f"\nTim thay {len(drugs)} thuoc thieu field '{field_name}':")
        if len(drugs) <= 50:
            for drug in drugs:
                print(f"  - {drug}")
        else:
            for drug in drugs[:50]:
                print(f"  - {drug}")
            print(f"  ... va {len(drugs) - 50} thuoc khac")
    
    else:
        # Tìm kiếm thuốc
        drug_name = arg
        show_all = len(sys.argv) > 2 and sys.argv[2] == '--all'
        
        # Tìm kiếm (có thể là partial match)
        results = manager.search_drug(drug_name)
        
        if not results:
            print(f"Khong tim thay thuoc nao matching '{drug_name}'")
            print("\nGoi y: Thu dung ten chinh xac hoac mot phan ten thuoc")
            return
        
        if len(results) > 1 and not show_all:
            print(f"Tim thay {len(results)} thuoc matching '{drug_name}':")
            for drug in results[:10]:
                print(f"  - {drug['name']}")
            if len(results) > 10:
                print(f"  ... va {len(results) - 10} thuoc khac")
            print("\nDe xem chi tiet, chay voi --all hoac ten chinh xac")
            return
        
        # Hiển thị chi tiết
        for drug_info in results:
            drug_name = drug_info['name']
            result = manager.check_drug_fields(drug_name)
            
            print(f"\n{'=' * 70}")
            print(f"THUOC: {drug_name}")
            print(f"FILE: {result['file']}")
            print(f"{'=' * 70}")
            
            if result['has_all_fields']:
                print("\n✅ TAT CA FIELD DEU CO DAY DU!")
            else:
                print(f"\nThieu {result['total_missing']} fields:")
                
                if result['missing_core']:
                    print(f"\n  ❌ CORE FIELDS ({len(result['missing_core'])}):")
                    for field in result['missing_core']:
                        print(f"    - {field}")
                
                if result['missing_extended']:
                    print(f"\n  ⚠️  EXTENDED FIELDS ({len(result['missing_extended'])}):")
                    for field in result['missing_extended']:
                        print(f"    - {field}")
                
                if result['missing_enhanced']:
                    print(f"\n  ℹ️  ENHANCED FIELDS ({len(result['missing_enhanced'])}):")
                    for field in result['missing_enhanced']:
                        print(f"    - {field}")
            
            if len(results) > 1:
                print()

if __name__ == "__main__":
    main()

