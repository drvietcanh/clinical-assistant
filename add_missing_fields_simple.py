"""
Script đơn giản để bổ sung các field còn thiếu cho thuốc
Tập trung vào enhanced fields vì core fields thường cần điền thủ công
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple
import shutil
from datetime import datetime

# Enhanced fields và templates
ENHANCED_FIELDS_TEMPLATES = {
    "mechanism_of_action": '        "mechanism_of_action": "",',
    "monitoring": '        "monitoring": [],',
    "precautions": '        "precautions": [],',
    "pharmacokinetics": '''        "pharmacokinetics": {
            "half_life": "",
            "onset": "",
            "duration": "",
            "protein_binding": "",
            "clearance": ""
        },''',
    "storage": '        "storage": "",',
    "black_box_warnings": '        "black_box_warnings": None,',
    "drug_interactions": '''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },''',
    "pregnancy_lactation": '''        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation_details": ""
        },''',
    "hepatic_adjustment": '''        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": ""
        },''',
    "overdose_management": '''        "overdose_management": {
            "symptoms": [],
            "treatment": "",
            "antidote": None
        },''',
    "reversal_agents": '''        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": ""
        },''',
    "administration_instructions": '''        "administration_instructions": {
            "preparation": "",
            "administration": "",
            "monitoring": []
        },''',
    "references": '''        "references": {
            "primary": [],
            "guidelines": [],
            "other": []
        },''',
}

def find_drug_section(content: str, drug_name: str) -> Tuple[int, int]:
    """Tìm vị trí của một thuốc trong content"""
    # Pattern: "DrugName": { ... }
    pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
    match = re.search(pattern, content)
    
    if not match:
        return None, None
    
    start_pos = match.end() - 1  # Vị trí của {
    
    # Tìm vị trí kết thúc của dict
    brace_count = 0
    in_string = False
    string_char = None
    i = start_pos
    
    while i < len(content):
        char = content[i]
        
        # Xử lý string
        if char in ['"', "'"]:
            # Kiểm tra escape
            if i > 0 and content[i-1] == '\\':
                i += 1
                continue
            
            if not in_string:
                in_string = True
                string_char = char
            elif char == string_char:
                in_string = False
                string_char = None
        
        if not in_string:
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    return start_pos, i + 1
        
        i += 1
    
    return None, None

def check_field_exists(content: str, drug_start: int, drug_end: int, field_name: str) -> bool:
    """Kiểm tra xem field đã tồn tại chưa"""
    drug_section = content[drug_start:drug_end]
    pattern = rf'["\']{re.escape(field_name)}["\']\s*:'
    return bool(re.search(pattern, drug_section))

def add_fields_to_drug(
    file_path: Path,
    drug_name: str,
    missing_fields: List[str],
    dry_run: bool = True
) -> bool:
    """Thêm các field còn thiếu vào một thuốc"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines(keepends=True)
        
        # Tìm vị trí của drug
        start_pos, end_pos = find_drug_section(content, drug_name)
        if start_pos is None:
            if not dry_run:
                print(f"  [LOI] Khong tim thay thuoc {drug_name} trong {file_path.name}")
            return False
        
        # Tìm dòng tương ứng
        start_line = content[:start_pos].count('\n')
        end_line = content[:end_pos].count('\n')
        
        # Kiểm tra các field đã tồn tại chưa
        fields_to_add = []
        for field in missing_fields:
            if not check_field_exists(content, start_pos, end_pos, field):
                fields_to_add.append(field)
        
        if not fields_to_add:
            if dry_run:
                print(f"  [SKIP] {drug_name}: Tat ca field da co san")
            elif not dry_run:
                print(f"  [INFO] {drug_name} trong {file_path.name}: Khong co field nao can them (co the da co)")
            return False
        
        if dry_run:
            print(f"\n  [DRY-RUN] {file_path.name} - {drug_name}:")
            print(f"    Se them: {', '.join(fields_to_add)}")
            return True
        
        if not dry_run:
            print(f"  [INFO] {drug_name}: Se them {len(fields_to_add)} fields: {', '.join(fields_to_add[:3])}{'...' if len(fields_to_add) > 3 else ''}")
        
        # Tìm vị trí chèn (trước dòng đóng })
        insert_line = end_line - 1
        
        # Tìm dòng cuối cùng có nội dung (không phải chỉ có })
        while insert_line > start_line:
            line = lines[insert_line].strip()
            if line and line != '}' and not line.startswith('#'):
                # Đảm bảo có comma
                if not line.endswith(',') and not line.endswith('{'):
                    lines[insert_line] = lines[insert_line].rstrip() + ',\n'
                break
            insert_line -= 1
        
        # Tạo code cho các field mới
        new_fields = []
        for field in fields_to_add:
            if field in ENHANCED_FIELDS_TEMPLATES:
                new_fields.append(ENHANCED_FIELDS_TEMPLATES[field])
        
        if not new_fields:
            return False
        
        # Chèn vào
        insert_pos = insert_line + 1
        new_code = '\n'.join(new_fields) + '\n'
        lines.insert(insert_pos, new_code)
        
        # Ghi lại
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        print(f"  [OK] Da them {len(fields_to_add)} fields vao {drug_name} trong {file_path.name}")
        return True
        
    except Exception as e:
        if not dry_run:
            print(f"  [LOI] {file_path.name} - {drug_name}: {e}")
        return False

def find_drug_file(drug_name: str) -> Path:
    """Tìm file chứa một thuốc"""
    base_path = Path("drugs/drug_modules")
    
    for py_file in sorted(base_path.rglob("*.py")):
        if py_file.name == "__init__.py" or py_file.name.endswith(".backup"):
            continue
        
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Tìm drug bằng regex
            pattern = rf'["\']{re.escape(drug_name)}["\']\s*:\s*\{{'
            if not re.search(pattern, content):
                continue
            
            # Tìm drug section
            drug_start, drug_end = find_drug_section(content, drug_name)
            if drug_start is None:
                continue
            
            # Kiểm tra xem có phải là drug thực sự (có 'group' hoặc 'vietnamese_name')
            drug_section = content[drug_start:drug_end]
            # Tìm cả single và double quotes
            if ('"group"' in drug_section or "'group'" in drug_section or 
                '"vietnamese_name"' in drug_section or "'vietnamese_name'" in drug_section):
                return py_file
        except Exception:
            pass
    
    return None

def main():
    """Main function"""
    import sys
    
    print("\n" + "=" * 70)
    print("BO SUNG FIELD CON THIEU CHO THUOC")
    print("=" * 70)
    print()
    
    # Cho phép chạy với tham số command line
    dry_run = True  # Mặc định là dry-run để an toàn
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--execute" or sys.argv[1] == "-e":
            dry_run = False
        elif sys.argv[1] == "--dry-run" or sys.argv[1] == "-d":
            dry_run = True
    
    if not dry_run:
        # Tạo backup
        backup_dir = Path("backups") / datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir.mkdir(parents=True, exist_ok=True)
        print(f"\nDang tao backup tai: {backup_dir}")
    else:
        print("\n[DRY-RUN MODE] Chi hien thi, khong sua file")
        print("De thuc thi, chay: python add_missing_fields_simple.py --execute")
    
    print("\nDang tim cac thuoc thieu enhanced fields...")
    
    # Import từ script check
    import sys
    sys.path.insert(0, str(Path.cwd()))
    
    try:
        from check_missing_fields_final import load_all_drugs, check_drug_fields
        
        # Load drugs từ check_missing_fields_final
        all_drugs = load_all_drugs()
        print(f"Tim thay {len(all_drugs)} thuoc")
        
        # Tìm các thuốc thiếu enhanced fields
        # Lọc bỏ các field names (không phải tên thuốc)
        drugs_to_fix = []
        
        for drug_name, fields in all_drugs.items():
            # CHỈ xử lý nếu có 'group' HOẶC 'vietnamese_name' (là thuốc thực sự)
            # Nếu không có cả hai, đó không phải là thuốc
            if 'group' not in fields and 'vietnamese_name' not in fields:
                continue
            
            # Lọc bỏ các field names (thường là lowercase với nhiều dấu gạch dưới)
            # Nhưng vẫn cho phép nếu có 'group' hoặc 'vietnamese_name'
            is_field_name = (
                drug_name.islower() and 
                '_' in drug_name and 
                drug_name.count('_') >= 2 and
                drug_name not in ['iv', 'po', 'im', 'sc']  # exceptions
            )
            
            # Nếu trông giống field name nhưng không có group/vietnamese_name, bỏ qua
            if is_field_name:
                continue
            
            result = check_drug_fields(drug_name, fields)
            if result['missing_enhanced']:
                drugs_to_fix.append((drug_name, result['missing_enhanced']))
        
        if not drugs_to_fix:
            print("\n[OK] Khong co thuoc nao thieu enhanced fields!")
            return
        
        print(f"\nTim thay {len(drugs_to_fix)} thuoc thieu enhanced fields")
        if len(drugs_to_fix) <= 20:
            print("Danh sach thuoc:")
            for drug_name, missing_fields in drugs_to_fix:
                print(f"  - {drug_name}: thieu {len(missing_fields)} fields")
        
        if dry_run:
            print("\n[DRY-RUN MODE] Se hien thi cac thay doi se duoc thuc hien:")
            print(f"Tong so thuoc se xu ly: {len(drugs_to_fix)}")
        else:
            print(f"\nSe xu ly {len(drugs_to_fix)} thuoc...")
        
        # Xử lý từng thuốc
        fixed_count = 0
        failed_count = 0
        processed_files = set()
        skipped_non_drugs = 0
        not_found_drugs = []  # Lưu danh sách thuốc không tìm thấy file
        
        for drug_name, missing_fields in drugs_to_fix:
            # Lọc bỏ các field names và giá trị không phải thuốc
            # Các field names thường là lowercase với nhiều dấu gạch dưới
            is_likely_field_name = (
                drug_name.islower() and 
                drug_name.count('_') >= 2 and 
                drug_name not in ['iv', 'po', 'im', 'sc']
            )
            
            # Danh sách các giá trị không phải thuốc
            non_drug_values = [
                'oral', 'im', 'sc', 'inhaled', 'inhalation', 'iv', 'po',
                'risk_flags', 'organ_toxicity', 'pediatric_dosing', 
                'geriatric_dosing', 'brand_names', 'cost_estimate',
                'contraindications_detail', 'reversal_agents', 'dosage',
                'renal_adjustment', 'pharmacokinetics', 'drug_interactions',
                'references', 'pregnancy_lactation', 'hepatic_adjustment',
                'overdose_management', 'administration_instructions'
            ]
            
            if is_likely_field_name or drug_name in non_drug_values:
                skipped_non_drugs += 1
                if dry_run and skipped_non_drugs <= 5:
                    print(f"  [SKIP] Bo qua (khong phai thuoc): {drug_name}")
                continue
            
            # Tìm file chứa thuốc
            file_path = find_drug_file(drug_name)
            
            if not file_path:
                not_found_drugs.append(drug_name)
                if dry_run and len(not_found_drugs) <= 10:  # Chỉ in 10 đầu tiên trong dry-run
                    print(f"  [WARNING] Khong tim thay file: {drug_name}")
                elif not dry_run:
                    print(f"\n[WARNING] Khong tim thay file chua thuoc: {drug_name}")
                failed_count += 1
                continue
            
            if not dry_run:
                print(f"\n[DANG XU LY] {drug_name} trong {file_path.name}")
            
            if not dry_run and file_path not in processed_files:
                # Backup file lần đầu tiên
                backup_file = backup_dir / f"{file_path.name}.backup"
                shutil.copy2(file_path, backup_file)
                processed_files.add(file_path)
            
            success = add_fields_to_drug(file_path, drug_name, missing_fields, dry_run)
            
            if success:
                fixed_count += 1
            else:
                failed_count += 1
        
        # Tóm tắt
        print("\n" + "=" * 70)
        print("TOM TAT")
        print("=" * 70)
        print(f"\nDa xu ly: {fixed_count + failed_count} thuoc")
        print(f"  - Thanh cong: {fixed_count}")
        print(f"  - That bai: {failed_count}")
        if skipped_non_drugs > 0:
            print(f"  - Bo qua (khong phai thuoc): {skipped_non_drugs}")
        if not_found_drugs:
            print(f"\n  [INFO] {len(not_found_drugs)} thuoc khong tim thay file:")
            if len(not_found_drugs) <= 20:
                for drug in not_found_drugs:
                    print(f"    - {drug}")
            else:
                for drug in not_found_drugs[:20]:
                    print(f"    - {drug}")
                print(f"    ... va {len(not_found_drugs) - 20} thuoc khac")
        
        if not dry_run and fixed_count > 0:
            print(f"\nBackup duoc luu tai: {backup_dir}")
            print("Ban co the restore neu can.")
        
    except ImportError as e:
        print(f"\n[LOI] Khong the import check_missing_fields_final: {e}")
        print("Vui long chay check_missing_fields_final.py truoc.")
    except Exception as e:
        print(f"\n[LOI] {e}")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()

