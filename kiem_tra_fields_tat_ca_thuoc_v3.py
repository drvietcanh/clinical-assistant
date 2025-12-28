"""
Script kiem tra tat ca cac thuoc co du 14 enhanced fields khong
Load tu tat ca cac file trong drug_modules, bao gom ca subdirectories
"""

import os
import sys
import importlib.util
import types

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

def load_module_direct(filepath, module_name=None):
    """Load module tu file Python va tra ve tat ca cac _DRUGS dictionaries"""
    all_drugs = {}
    try:
        # Doc file
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Tao namespace rieng, khong import streamlit
        namespace = {
            '__name__': module_name or os.path.basename(filepath),
            '__file__': filepath,
        }
        
        # Thay the import streamlit bang mock
        if 'import streamlit' in code or 'import streamlit as' in code:
            code = code.replace('import streamlit', '# import streamlit')
            code = code.replace('import streamlit as st', '# import streamlit as st')
            namespace['streamlit'] = types.ModuleType('streamlit')
            namespace['st'] = namespace['streamlit']
        
        # Compile va exec
        try:
            compiled = compile(code, filepath, 'exec')
            exec(compiled, namespace)
        except SyntaxError as e:
            # Bo qua file co loi syntax
            return {}
        except Exception as e:
            # Bo qua cac loi khac
            return {}
        
        # Tim tat ca cac dictionary ket thuc bang _DRUGS
        for key, value in namespace.items():
            if key.endswith('_DRUGS') and isinstance(value, dict):
                all_drugs.update(value)
        
        return all_drugs
    except Exception as e:
        return {}

def scan_directory_recursive(base_path, all_drugs):
    """Quet de quy tat ca cac file .py trong thu muc"""
    for root, dirs, files in os.walk(base_path):
        # Bo qua __pycache__
        if '__pycache__' in root:
            continue
        
        for filename in files:
            if not filename.endswith('.py'):
                continue
            
            # Bo qua __init__.py o root level (co the co dependency issues)
            if filename == '__init__.py' and root == base_path:
                continue
            
            filepath = os.path.join(root, filename)
            relative_path = os.path.relpath(filepath, base_path)
            
            drugs = load_module_direct(filepath, relative_path.replace(os.sep, '.'))
            if drugs:
                all_drugs.update(drugs)
                print(f"Loaded {len(drugs)} drugs from {relative_path}")

def load_all_drugs():
    """Load tat ca cac thuoc tu drug_modules"""
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    
    if not os.path.exists(base_path):
        print(f"Khong tim thay thu muc: {base_path}")
        return {}
    
    all_drugs = {}
    
    print("Dang quet cac file trong drug_modules...")
    scan_directory_recursive(base_path, all_drugs)
    
    return all_drugs

def check_drug_fields(drug_name, drug_data):
    """Kiem tra fields cua mot thuoc"""
    if not isinstance(drug_data, dict):
        return None
    
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
    print("\nDang load du lieu thuoc tu tat ca cac file...")
    all_drugs = load_all_drugs()
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
        result = check_drug_fields(drug_name, drug_data)
        if result is None:
            continue
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
    
    # Danh sach thuoc thieu fields (chi hien thi 30 thuoc dau tien)
    print("\n" + "=" * 80)
    print("DANH SACH THUOC THIEU FIELDS (30 thuoc dau tien)")
    print("=" * 80)
    
    for i, result in enumerate(results[:30]):
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
        
        # Tạo kế hoạch theo phiên (mỗi phiên ~25-30 thuốc)
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

