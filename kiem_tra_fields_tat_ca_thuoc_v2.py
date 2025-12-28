"""
Script kiem tra tat ca cac thuoc co du 14 enhanced fields khong
Doc truc tiep tu cac file Python trong drug_modules
"""

import os
import re
import ast

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

def find_drug_dicts_in_file(filepath):
    """Tim tat ca cac drug dictionaries trong mot file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse AST
        tree = ast.parse(content)
        
        # Tim cac dictionary assignment
        drug_dicts = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        if isinstance(node.value, ast.Dict):
                            # Convert AST dict to actual dict (simple case)
                            try:
                                dict_val = {}
                                for k, v in zip(node.value.keys, node.value.values):
                                    if isinstance(k, ast.Constant) and isinstance(v, ast.Dict):
                                        dict_val[k.value] = {}
                                        # Get keys from drug dict
                                        if v.keys:
                                            for dk in v.keys:
                                                if isinstance(dk, ast.Constant):
                                                    dict_val[k.value][dk.value] = None  # Placeholder
                                if dict_val:
                                    drug_dicts[target.id] = dict_val
                            except:
                                pass
        
        return drug_dicts
    except Exception as e:
        return {}

def load_drugs_from_python_file(filepath):
    """Load drugs bang cach exec file Python trong mot namespace rieng"""
    drugs = {}
    try:
        # Doc file
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Tao namespace rieng
        namespace = {}
        
        # Exec code trong namespace
        exec(compile(code, filepath, 'exec'), namespace)
        
        # Tim cac dictionary ket thuc bang _DRUGS
        for key, value in namespace.items():
            if key.endswith('_DRUGS') and isinstance(value, dict):
                drugs.update(value)
        
        return drugs
    except Exception as e:
        # Ignore errors (cac module co the can import khac)
        return {}

def scan_all_drug_modules():
    """Quet tat ca cac file trong drug_modules"""
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    all_drugs = {}
    
    # Files truc tiep trong drug_modules
    direct_files = [
        'dermatology.py',
        'ophthalmology.py',
        'urology.py',
        'other.py',
        'analgesics.py',
        'antimicrobial.py',
        'cardiovascular.py',
        'diabetes.py',
        'emergency.py',
        'endocrinology_other.py',
        'gastrointestinal.py',
        'hematology.py',
        'infectious_other.py',
        'metabolic.py',
        'miscellaneous.py',
        'neurological.py',
        'oncology.py',
        'psychiatry_other.py',
        'respiratory.py',
        'supportive.py',
        'cardiovascular_other.py',
        'ent_oral_nasal_combinations.py',
        'obstetrics_gynecology.py',
    ]
    
    # Load tu cac file truc tiep
    for filename in direct_files:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            drugs = load_drugs_from_python_file(filepath)
            if drugs:
                all_drugs.update(drugs)
                print(f"Loaded {len(drugs)} drugs from {filename}")
    
    # Load tu cac __init__.py trong subdirectories
    subdirs = [
        'cardiovascular',
        'diabetes',
        'gastrointestinal',
        'analgesics',
        'respiratory',
        'neurological',
        'supportive',
        'antimicrobial',
        'metabolic',
        'oncology',
        'emergency',
        'endocrinology_other',
        'infectious_other',
        'psychiatry_other',
        'cardiovascular_other',
        'miscellaneous',
    ]
    
    for subdir in subdirs:
        init_file = os.path.join(base_path, subdir, '__init__.py')
        if os.path.exists(init_file):
            drugs = load_drugs_from_python_file(init_file)
            if drugs:
                all_drugs.update(drugs)
                print(f"Loaded {len(drugs)} drugs from {subdir}/__init__.py")
    
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
    print("\nDang quet cac file trong drug_modules...")
    all_drugs = scan_all_drug_modules()
    TOTAL_DRUGS = len(all_drugs)
    
    if TOTAL_DRUGS == 0:
        print("Khong load duoc thuoc nao. Co the co loi trong qua trinh doc file.")
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
    for drug_name, drug_data in sorted(all_drugs.items()):
        if not isinstance(drug_data, dict):
            continue
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

