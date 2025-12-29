"""
Script phan tich toan bo cau truc thuoc trong database
"""
import os
import sys
import importlib.util
import types
import re
from collections import defaultdict

def load_module_direct(filepath, module_name=None):
    """Load module tu file Python va tra ve tat ca cac _DRUGS dictionaries"""
    all_drugs = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        namespace = {
            '__name__': module_name or os.path.basename(filepath),
            '__file__': filepath,
        }
        
        # Mock streamlit if needed
        if 'import streamlit' in code or 'import streamlit as' in code:
            code = code.replace('import streamlit', '# import streamlit')
            code = code.replace('import streamlit as st', '# import streamlit as st')
            namespace['streamlit'] = types.ModuleType('streamlit')
            namespace['st'] = namespace['streamlit']
        
        try:
            compiled = compile(code, filepath, 'exec')
            exec(compiled, namespace)
        except SyntaxError as e:
            return {}, str(e)
        except Exception as e:
            return {}, str(e)
        
        for key, value in namespace.items():
            if key.endswith('_DRUGS') and isinstance(value, dict):
                all_drugs.update(value)
        
        return all_drugs, None
    except Exception as e:
        return {}, str(e)

def scan_directory_recursive(base_path):
    """Quet de quy tat ca cac file .py trong thu muc"""
    all_drugs = {}
    drug_file_map = {}  # drug_name -> filepath
    file_stats = {}  # filepath -> {count, errors}
    errors = []
    
    for root, dirs, files in os.walk(base_path):
        if '__pycache__' in root:
            continue
        
        for filename in files:
            if not filename.endswith('.py'):
                continue
            
            if filename == '__init__.py' and root == base_path:
                continue
            
            filepath = os.path.join(root, filename)
            relative_path = os.path.relpath(filepath, base_path)
            
            drugs, error = load_module_direct(filepath, relative_path.replace(os.sep, '.'))
            if drugs:
                all_drugs.update(drugs)
                for drug_name in drugs.keys():
                    if drug_name in drug_file_map:
                        # Duplicate found
                        errors.append(f"DUPLICATE: {drug_name} in both {drug_file_map[drug_name]} and {filepath}")
                    drug_file_map[drug_name] = filepath
                file_stats[filepath] = {'count': len(drugs), 'error': error}
            elif error:
                file_stats[filepath] = {'count': 0, 'error': error}
                errors.append(f"ERROR in {filepath}: {error}")
    
    return all_drugs, drug_file_map, file_stats, errors

def analyze_drug_structure(all_drugs):
    """Phan tich cau truc cua cac thuoc"""
    stats = {
        'total': len(all_drugs),
        'by_group': defaultdict(int),
        'by_administration': defaultdict(int),
        'fields_analysis': defaultdict(int),
        'missing_fields': defaultdict(list),
    }
    
    for drug_name, drug_data in all_drugs.items():
        if not isinstance(drug_data, dict):
            continue
        
        # Group analysis
        group = drug_data.get('group', 'Unknown')
        stats['by_group'][group] += 1
        
        # Administration analysis
        admin = drug_data.get('administration', [])
        if isinstance(admin, list):
            for a in admin:
                stats['by_administration'][str(a)] += 1
        else:
            stats['by_administration'][str(admin)] += 1
        
        # Fields analysis
        required_fields = [
            'mechanism_of_action', 'monitoring', 'precautions',
            'pharmacokinetics', 'storage', 'black_box_warnings'
        ]
        optional_fields = [
            'drug_interactions', 'contraindications', 'pregnancy_lactation',
            'hepatic_adjustment', 'renal_adjustment', 'overdose_management',
            'reversal_agents', 'administration_instructions', 'references'
        ]
        
        for field in required_fields + optional_fields:
            if field in drug_data and drug_data[field] is not None:
                stats['fields_analysis'][field] += 1
            else:
                stats['missing_fields'][field].append(drug_name)
    
    return stats

def main():
    print("=" * 80)
    print("PHAN TICH TOAN BO CAU TRUC THUOC")
    print("=" * 80)
    print()
    
    base_path = 'drugs'
    if not os.path.exists(base_path):
        print(f"Khong tim thay thu muc: {base_path}")
        return
    
    print("Dang quet toan bo thu muc drugs...")
    all_drugs, drug_file_map, file_stats, errors = scan_directory_recursive(base_path)
    
    print(f"\nTong so thuoc tim thay: {len(all_drugs)}")
    print(f"Tong so file: {len(file_stats)}")
    print(f"Tong so loi: {len(errors)}")
    
    if errors:
        print("\nCAC LOI PHAT HIEN:")
        for error in errors[:20]:
            print(f"  - {error}")
        if len(errors) > 20:
            print(f"  ... va {len(errors) - 20} loi khac")
    
    # Phan tich cau truc
    print("\nDang phan tich cau truc...")
    stats = analyze_drug_structure(all_drugs)
    
    # Thong ke theo file
    print("\n" + "=" * 80)
    print("THONG KE THEO FILE")
    print("=" * 80)
    sorted_files = sorted(file_stats.items(), key=lambda x: x[1]['count'], reverse=True)
    for filepath, info in sorted_files[:30]:
        rel_path = os.path.relpath(filepath, base_path)
        print(f"{rel_path:60s} {info['count']:3d} thuoc")
        if info.get('error'):
            print(f"  ERROR: {info['error']}")
    
    # Thong ke theo nhom
    print("\n" + "=" * 80)
    print("THONG KE THEO NHOM (Top 20)")
    print("=" * 80)
    sorted_groups = sorted(stats['by_group'].items(), key=lambda x: x[1], reverse=True)
    for group, count in sorted_groups[:20]:
        print(f"{group:50s} {count:3d} thuoc")
    
    # Thong ke fields
    print("\n" + "=" * 80)
    print("THONG KE FIELDS")
    print("=" * 80)
    for field, count in sorted(stats['fields_analysis'].items(), key=lambda x: x[1], reverse=True):
        missing = len(stats['missing_fields'][field])
        print(f"{field:30s} Co: {count:3d}  Thieu: {missing:3d}  ({count*100//len(all_drugs)}%)")
    
    # Ghi ket qua ra file
    output_file = "PHAN_TICH_TOAN_BO_THUOC.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("PHAN TICH TOAN BO CAU TRUC THUOC\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Tong so thuoc: {len(all_drugs)}\n")
        f.write(f"Tong so file: {len(file_stats)}\n")
        f.write(f"Tong so loi: {len(errors)}\n\n")
        
        if errors:
            f.write("CAC LOI PHAT HIEN:\n")
            for error in errors:
                f.write(f"  - {error}\n")
            f.write("\n")
        
        f.write("THONG KE THEO FILE:\n")
        for filepath, info in sorted_files:
            rel_path = os.path.relpath(filepath, base_path)
            f.write(f"{rel_path}: {info['count']} thuoc\n")
            if info.get('error'):
                f.write(f"  ERROR: {info['error']}\n")
        
        f.write("\nTHONG KE THEO NHOM:\n")
        for group, count in sorted_groups:
            f.write(f"{group}: {count} thuoc\n")
        
        f.write("\nTHONG KE FIELDS:\n")
        for field, count in sorted(stats['fields_analysis'].items(), key=lambda x: x[1], reverse=True):
            missing = len(stats['missing_fields'][field])
            f.write(f"{field}: Co {count}, Thieu {missing}\n")
    
    print(f"\nDa ghi ket qua chi tiet vao: {output_file}")
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()

