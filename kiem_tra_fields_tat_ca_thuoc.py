"""
Script kiem tra tat ca cac thuoc co du 14 enhanced fields khong
14 fields bao gom:
- 6 required: mechanism_of_action, monitoring, precautions, pharmacokinetics, storage, black_box_warnings
- 8 optional: drug_interactions, contraindications, pregnancy_lactation, hepatic_adjustment, 
             renal_adjustment, overdose_management, reversal_agents, administration_instructions, references
"""

import sys
import os
import importlib.util

# Dinh nghia 14 enhanced fields
REQUIRED_FIELDS = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings'
]

OPTIONAL_FIELDS = [
    'drug_interactions',
    'contraindications',
    'pregnancy_lactation',
    'hepatic_adjustment',
    'renal_adjustment',
    'overdose_management',
    'reversal_agents',
    'administration_instructions',
    'references'
]

ALL_FIELDS = REQUIRED_FIELDS + OPTIONAL_FIELDS

def load_module_drugs(module_path, drug_dict_name):
    """Load drugs tu mot module"""
    try:
        spec = importlib.util.spec_from_file_location("module", module_path)
        if spec is None or spec.loader is None:
            return {}
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, drug_dict_name, {})
    except Exception as e:
        print(f"Error loading {module_path}: {e}")
        return {}

def load_all_drugs():
    """Load tat ca cac thuoc tu drug_modules"""
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    all_drugs = {}
    
    # Danh sach modules can load
    modules_to_load = [
        ('cardiovascular', '__init__.py', 'CARDIOVASCULAR_DRUGS'),
        ('diabetes', '__init__.py', 'DIABETES_DRUGS'),
        ('gastrointestinal', '__init__.py', 'GASTROINTESTINAL_DRUGS'),
        ('analgesics', '__init__.py', 'ANALGESICS_DRUGS'),
        ('respiratory', '__init__.py', 'RESPIRATORY_DRUGS'),
        ('neurological', '__init__.py', 'NEUROLOGICAL_DRUGS'),
        ('hematology', '__init__.py', 'HEMATOLOGY_DRUGS'),
        ('supportive', '__init__.py', 'SUPPORTIVE_DRUGS'),
        ('antimicrobial', '__init__.py', 'ANTIMICROBIAL_DRUGS'),
        ('metabolic', '__init__.py', 'METABOLIC_DRUGS'),
        ('oncology', '__init__.py', 'ONCOLOGY_DRUGS'),
        ('emergency', '__init__.py', 'EMERGENCY_DRUGS'),
        ('other', '__init__.py', 'OTHER_DRUGS'),
        ('urology', '__init__.py', 'UROLOGY_DRUGS'),
        ('dermatology.py', '', 'DERMATOLOGY_DRUGS'),
        ('ophthalmology.py', '', 'OPHTHALMOLOGY_DRUGS'),
        ('cardiovascular_other', '__init__.py', 'CARDIOVASCULAR_OTHER_DRUGS'),
        ('infectious_other', '__init__.py', 'INFECTIOUS_OTHER_DRUGS'),
        ('psychiatry_other', '__init__.py', 'PSYCHIATRY_OTHER_DRUGS'),
        ('endocrinology_other', '__init__.py', 'ENDOCRINOLOGY_OTHER_DRUGS'),
        ('miscellaneous', '__init__.py', 'MISCELLANEOUS_DRUGS'),
    ]
    
    for module_info in modules_to_load:
        if len(module_info) == 2:  # File truc tiep
            module_file = module_info[0]
            dict_name = module_info[1]
            module_path = os.path.join(base_path, module_file)
        else:  # Module co __init__.py
            module_dir, init_file, dict_name = module_info
            module_path = os.path.join(base_path, module_dir, init_file)
        
        if os.path.exists(module_path):
            drugs = load_module_drugs(module_path, dict_name)
            if drugs:
                all_drugs.update(drugs)
                print(f"Loaded {len(drugs)} drugs from {module_path}")
    
    return all_drugs

def check_drug_fields(drug_name, drug_data):
    """Kiem tra fields cua mot thuoc"""
    missing_required = []
    missing_optional = []
    
    # Kiem tra required fields
    for field in REQUIRED_FIELDS:
        if field not in drug_data or drug_data[field] is None:
            missing_required.append(field)
    
    # Kiem tra optional fields
    for field in OPTIONAL_FIELDS:
        if field not in drug_data or drug_data[field] is None:
            missing_optional.append(field)
    
    total_missing = len(missing_required) + len(missing_optional)
    
    return {
        'drug_name': drug_name,
        'missing_required': missing_required,
        'missing_optional': missing_optional,
        'total_missing': total_missing,
        'has_all_fields': total_missing == 0
    }

def main():
    print("=" * 80)
    print("KIEM TRA 14 ENHANCED FIELDS CHO TAT CA THUOC")
    print("=" * 80)
    
    # Load all drugs
    print("\nDang load du lieu thuoc...")
    DRUG_DATABASE = load_all_drugs()
    TOTAL_DRUGS = len(DRUG_DATABASE)
    
    if TOTAL_DRUGS == 0:
        print("Khong load duoc thuoc nao. Co the co loi trong qua trinh import.")
        return
    
    print(f"\nTong so thuoc: {TOTAL_DRUGS}")
    print(f"\n14 Fields:")
    print(f"  - 6 Required: {', '.join(REQUIRED_FIELDS)}")
    print(f"  - 8 Optional: {', '.join(OPTIONAL_FIELDS)}")
    print("\n" + "=" * 80)
    
    results = []
    drugs_with_all_fields = 0
    drugs_missing_fields = 0
    
    # Kiem tra tung thuoc
    for drug_name, drug_data in sorted(DRUG_DATABASE.items()):
        result = check_drug_fields(drug_name, drug_data)
        results.append(result)
        
        if result['has_all_fields']:
            drugs_with_all_fields += 1
        else:
            drugs_missing_fields += 1
    
    # Sap xep ket qua: thuoc thieu nhieu field nhat truoc
    results.sort(key=lambda x: x['total_missing'], reverse=True)
    
    # Tong ket
    print("\n" + "=" * 80)
    print("TONG KET")
    print("=" * 80)
    print(f"Tong so thuoc: {TOTAL_DRUGS}")
    print(f"Thuoc co du 14 fields: {drugs_with_all_fields} ({drugs_with_all_fields/TOTAL_DRUGS*100:.1f}%)")
    print(f"Thuoc thieu fields: {drugs_missing_fields} ({drugs_missing_fields/TOTAL_DRUGS*100:.1f}%)")
    
    # Thong ke theo so field thieu
    print("\n" + "=" * 80)
    print("THONG KE THEO SO FIELD THIEU")
    print("=" * 80)
    
    missing_count = {}
    for result in results:
        if not result['has_all_fields']:
            count = result['total_missing']
            missing_count[count] = missing_count.get(count, 0) + 1
    
    for count in sorted(missing_count.keys(), reverse=True):
        print(f"Thieu {count} fields: {missing_count[count]} thuoc")
    
    # Danh sach thuoc thieu fields (chi hien thi 20 thuoc dau tien)
    print("\n" + "=" * 80)
    print("DANH SACH THUOC THIEU FIELDS (20 thuoc dau tien)")
    print("=" * 80)
    
    for i, result in enumerate(results[:20]):
        if not result['has_all_fields']:
            print(f"\n{i+1}. {result['drug_name']}:")
            print(f"   Thieu {result['total_missing']} fields")
            if result['missing_required']:
                print(f"   Required fields thieu ({len(result['missing_required'])}): {', '.join(result['missing_required'][:3])}")
            if result['missing_optional']:
                print(f"   Optional fields thieu ({len(result['missing_optional'])}): {', '.join(result['missing_optional'][:3])}")
    
    # Xuat file bao cao chi tiet
    report_file = "BAO_CAO_KIEM_TRA_FIELDS_TAT_CA_THUOC_CHI_TIET.txt"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("BAO CAO KIEM TRA 14 ENHANCED FIELDS CHO TAT CA THUOC\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Tong so thuoc: {TOTAL_DRUGS}\n")
        f.write(f"Thuoc co du 14 fields: {drugs_with_all_fields} ({drugs_with_all_fields/TOTAL_DRUGS*100:.1f}%)\n")
        f.write(f"Thuoc thieu fields: {drugs_missing_fields} ({drugs_missing_fields/TOTAL_DRUGS*100:.1f}%)\n\n")
        
        f.write("=" * 80 + "\n")
        f.write("THONG KE THEO SO FIELD THIEU\n")
        f.write("=" * 80 + "\n\n")
        for count in sorted(missing_count.keys(), reverse=True):
            f.write(f"Thieu {count} fields: {missing_count[count]} thuoc\n")
        
        f.write("\n" + "=" * 80 + "\n")
        f.write("DANH SACH CHI TIET THUOC THIEU FIELDS\n")
        f.write("=" * 80 + "\n\n")
        
        for result in results:
            if not result['has_all_fields']:
                f.write(f"{result['drug_name']}:\n")
                f.write(f"  Thieu {result['total_missing']} fields\n")
                if result['missing_required']:
                    f.write(f"  Required fields thieu ({len(result['missing_required'])}): {', '.join(result['missing_required'])}\n")
                if result['missing_optional']:
                    f.write(f"  Optional fields thieu ({len(result['missing_optional'])}): {', '.join(result['missing_optional'])}\n")
                f.write("\n")
    
    print(f"\nDa xuat bao cao chi tiet ra file: {report_file}")
    
    # Tao danh sach de len ke hoach
    planning_file = "KE_HOACH_BO_SUNG_FIELDS_THEO_PHIEN.md"
    with open(planning_file, 'w', encoding='utf-8') as f:
        f.write("# Kế Hoạch Bổ Sung Fields Theo Phiên\n\n")
        f.write(f"**Ngày tạo:** 2025-02-05\n")
        f.write(f"**Tổng số thuốc thiếu fields:** {drugs_missing_fields}\n")
        f.write(f"**Tổng số thuốc:** {TOTAL_DRUGS}\n\n")
        f.write("---\n\n")
        
        # Phân loại theo số field thiếu
        drugs_by_missing_count = {}
        for result in results:
            if not result['has_all_fields']:
                count = result['total_missing']
                if count not in drugs_by_missing_count:
                    drugs_by_missing_count[count] = []
                drugs_by_missing_count[count].append(result)
        
        # Tạo kế hoạch theo phiên (mỗi phiên ~20-30 thuốc)
        session = 1
        drugs_per_session = 25
        
        for count in sorted(drugs_by_missing_count.keys(), reverse=True):
            drugs_list = drugs_by_missing_count[count]
            
            # Chia thành các phiên
            for i in range(0, len(drugs_list), drugs_per_session):
                session_drugs = drugs_list[i:i+drugs_per_session]
                
                priority = "Cao" if count >= 10 else "Trung binh" if count >= 5 else "Thap"
                
                f.write(f"## Phiên {session}: Thuốc thiếu {count} fields ({len(session_drugs)} thuốc)\n\n")
                f.write(f"**Ưu tiên:** {priority}\n\n")
                
                for drug_result in session_drugs:
                    f.write(f"- [ ] **{drug_result['drug_name']}** - Thiếu {drug_result['total_missing']} fields\n")
                    if drug_result['missing_required']:
                        f.write(f"  - Required thiếu: {', '.join(drug_result['missing_required'])}\n")
                    if drug_result['missing_optional']:
                        missing_opt = drug_result['missing_optional']
                        f.write(f"  - Optional thiếu: {', '.join(missing_opt[:5])}")
                        if len(missing_opt) > 5:
                            f.write(f", ... ({len(missing_opt)-5} fields khác)")
                        f.write("\n")
                f.write("\n")
                session += 1
        
        f.write("---\n\n")
        f.write("## Tổng Kết\n\n")
        f.write(f"- Tổng số phiên: {session - 1}\n")
        f.write(f"- Trung bình: ~{drugs_per_session} thuốc/phiên\n")
        f.write(f"- Ưu tiên: Bắt đầu với các thuốc thiếu nhiều fields nhất\n\n")
    
    print(f"Da tao ke hoach theo phien: {planning_file}")
    print("\n" + "=" * 80)
    print("HOAN THANH")
    print("=" * 80)

if __name__ == "__main__":
    main()
