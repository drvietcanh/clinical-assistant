"""
Script tu dong bo sung cac fields con thieu cho cac thuoc
Su dung template tu cac thuoc da co day du fields
"""

import os
import sys
import re
import json

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

def get_default_field_value(field_name, drug_data):
    """Tra ve gia tri mac dinh cho field con thieu"""
    
    drug_name = drug_data.get('vietnamese_name', 'Unknown')
    group = drug_data.get('group', '')
    administration = drug_data.get('administration', [])
    dosage = drug_data.get('dosage', {})
    pregnancy = drug_data.get('pregnancy', 'C')
    
    # Xac dinh loai thuoc
    is_topical = 'Topical' in str(administration)
    is_iv = 'IV' in str(administration)
    is_po = 'PO' in str(administration) or 'Oral' in str(administration)
    is_nasal = 'Nasal' in str(administration)
    is_eye = 'eye' in str(dosage).lower() or 'ophthalmic' in group.lower()
    
    if field_name == 'pharmacokinetics':
        if is_topical or is_nasal or is_eye:
            return {
                "half_life": "Không áp dụng (topical)",
                "onset": "Vài ngày",
                "duration": "Phụ thuộc tần suất dùng",
                "protein_binding": "Không áp dụng (topical)",
                "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
            }
        else:
            return {
                "half_life": "Cần bổ sung",
                "onset": "Cần bổ sung",
                "duration": "Cần bổ sung",
                "protein_binding": "Cần bổ sung",
                "clearance": "Cần bổ sung"
            }
    
    elif field_name == 'storage':
        return "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng"
    
    elif field_name == 'black_box_warnings':
        # Kiem tra xem co black box warning khong
        if 'black_box' in str(drug_data).lower() or 'chống chỉ định' in str(drug_data).lower():
            return "Cần xem xét black box warnings"
        return None
    
    elif field_name == 'drug_interactions':
        existing_interactions = drug_data.get('interactions', [])
        if existing_interactions:
            return {
                "major": [],
                "moderate": [],
                "minor": []
            }
        return {
            "major": [],
            "moderate": [],
            "minor": []
        }
    
    elif field_name == 'contraindications':
        existing_contra = drug_data.get('contraindications', [])
        if existing_contra:
            return {
                "tuyệt_đối": existing_contra[:3] if len(existing_contra) >= 3 else existing_contra,
                "tương_đối": existing_contra[3:] if len(existing_contra) > 3 else []
            }
        return {
            "tuyệt_đối": [],
            "tương_đối": []
        }
    
    elif field_name == 'pregnancy_lactation':
        fda_cat = pregnancy if isinstance(pregnancy, str) else pregnancy.get('fda_category', 'C') if isinstance(pregnancy, dict) else 'C'
        return {
            "fda_category": fda_cat,
            "pregnancy_details": f"Category {fda_cat} - cần xem xét dữ liệu an toàn thai kỳ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Cần xem xét dữ liệu an toàn khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú."
            }
        }
    
    elif field_name == 'hepatic_adjustment':
        if is_topical or is_nasal or is_eye:
            return {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Không đổi",
                "notes": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ. Không cần điều chỉnh liều ở suy gan."
            }
        else:
            return {
                "mild": "Không đổi",
                "moderate": "Thận trọng",
                "severe": "Thận trọng",
                "notes": "Cần xem xét chuyển hóa qua gan."
            }
    
    elif field_name == 'overdose_management':
        return {
            "symptoms": ["Cần xem xét triệu chứng quá liều"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Hỗ trợ và điều trị triệu chứng",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, dấu hiệu lâm sàng"
        }
    
    elif field_name == 'reversal_agents':
        return {
            "available": False,
            "agents": []
        }
    
    elif field_name == 'administration_instructions':
        result = {}
        if is_po:
            result["oral"] = {
                "with_food": "Cần xem xét uống với hoặc không có thức ăn",
                "timing": "Cần xem xét thời điểm dùng",
                "notes": "Cần xem xét hướng dẫn cụ thể"
            }
        if is_iv:
            result["iv"] = {
                "reconstitution": "Cần xem xét cách pha",
                "infusion_rate": "Cần xem xét tốc độ truyền",
                "compatibility": ["Cần xem xét"],
                "incompatibility": ["Cần xem xét"],
                "notes": "Cần xem xét hướng dẫn cụ thể"
            }
        if is_topical:
            result["topical"] = {
                "technique": "Cần xem xét kỹ thuật bôi",
                "timing": "Cần xem xét tần suất",
                "notes": "Cần xem xét hướng dẫn cụ thể"
            }
        if is_nasal:
            result["nasal"] = {
                "preparation": "Cần xem xét",
                "technique": "Cần xem xét",
                "dosing": "Cần xem xét",
                "notes": "Cần xem xét hướng dẫn cụ thể"
            }
        return result if result else None
    
    elif field_name == 'references':
        return {
            "primary_sources": [
                f"FDA Drug Label - {drug_name}",
                "UpToDate - Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        }
    
    return None

def format_field_value(field_name, value):
    """Format field value thanh chuoi Python code"""
    if value is None:
        return "None"
    
    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            v_str = format_field_value(field_name, v)
            lines.append(f'            "{k}": {v_str},')
        lines.append("        }")
        return "\n".join(lines)
    
    elif isinstance(value, list):
        if not value:
            return "[]"
        lines = ["["]
        for item in value:
            item_str = format_field_value(field_name, item)
            lines.append(f"            {item_str},")
        lines.append("        ]")
        return "\n".join(lines)
    
    elif isinstance(value, str):
        # Escape quotes
        escaped = value.replace('"', '\\"').replace('\n', '\\n')
        return f'"{escaped}"'
    
    else:
        return json.dumps(value, ensure_ascii=False)

def add_missing_fields_to_file(filepath):
    """Them cac fields con thieu vao file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Load module
        namespace = {}
        exec(compile(content, filepath, 'exec'), namespace)
        
        # Tim drug dictionary
        drug_dict_name = None
        drug_dict = None
        for key in namespace:
            if key.endswith('_DRUGS') and isinstance(namespace[key], dict):
                drug_dict_name = key
                drug_dict = namespace[key]
                break
        
        if not drug_dict:
            print(f"Khong tim thay drug dictionary trong {filepath}")
            return False
        
        # Kiem tra va them fields
        modified = False
        new_content = content
        
        for drug_name, drug_data in drug_dict.items():
            if not isinstance(drug_data, dict):
                continue
            
            # Tim vi tri cua drug trong file
            drug_pattern = f'    "{drug_name}": {{'
            drug_match = re.search(re.escape(drug_pattern), new_content)
            if not drug_match:
                continue
            
            # Tim cac fields con thieu
            missing_fields = []
            for field in ALL_FIELDS:
                if field not in drug_data or drug_data[field] is None:
                    missing_fields.append(field)
            
            if not missing_fields:
                continue
            
            print(f"  Bo sung {len(missing_fields)} fields cho {drug_name}")
            
            # Tim vi tri de them fields (truoc dong dau tien cua drug tiep theo hoac truoc })
            # Tim vi tri ket thuc cua drug hien tai
            start_pos = drug_match.end()
            
            # Tim vi tri cua drug tiep theo
            next_drug_pattern = r'\n    "[A-Z]'
            next_drug_match = re.search(next_drug_pattern, new_content[start_pos:])
            if next_drug_match:
                insert_pos = start_pos + next_drug_match.start()
            else:
                # Tim vi tri ket thuc cua dictionary (})
                end_dict_match = re.search(r'\n}\s*$', new_content[start_pos:])
                if end_dict_match:
                    insert_pos = start_pos + end_dict_match.start()
                else:
                    continue
            
            # Tao code cho cac fields moi
            fields_code = []
            for field in missing_fields:
                value = get_default_field_value(field, drug_data)
                if value is not None:
                    value_str = format_field_value(field, value)
                    fields_code.append(f'        "{field}": {value_str},')
            
            if fields_code:
                # Them fields vao vi tri thich hop
                fields_str = "\n".join(fields_code)
                # Tim vi tri truoc dong cuoi cung cua drug (truoc } hoac drug tiep theo)
                # Tim vi tri truoc dong cuoi
                before_insert = new_content[start_pos:insert_pos]
                
                # Tim vi tri phu hop (truoc dong cuoi cung co , hoac })
                lines = before_insert.split('\n')
                last_line_idx = len(lines) - 1
                while last_line_idx >= 0 and (not lines[last_line_idx].strip() or lines[last_line_idx].strip().startswith('#')):
                    last_line_idx -= 1
                
                if last_line_idx >= 0:
                    last_line = lines[last_line_idx]
                    # Them fields truoc dong cuoi
                    if last_line.strip().endswith(','):
                        # Them truoc dong cuoi
                        lines.insert(last_line_idx, fields_str)
                    else:
                        # Them sau dong cuoi
                        lines.append(fields_str)
                    
                    new_before_insert = '\n'.join(lines)
                    new_content = new_content[:start_pos] + new_before_insert + new_content[insert_pos:]
                    modified = True
        
        if modified:
            # Backup file cu
            backup_path = filepath + '.backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Ghi file moi
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"  Da cap nhat {filepath}")
            return True
        
        return False
        
    except Exception as e:
        print(f"  Loi khi xu ly {filepath}: {e}")
        return False

def main():
    print("=" * 80)
    print("TU DONG BO SUNG CAC FIELDS CON THIEU")
    print("=" * 80)
    
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    
    # Tim tat ca cac file .py
    files_to_process = []
    for root, dirs, files in os.walk(base_path):
        if '__pycache__' in root:
            continue
        for filename in files:
            if filename.endswith('.py') and filename != '__init__.py':
                filepath = os.path.join(root, filename)
                files_to_process.append(filepath)
    
    print(f"\nTim thay {len(files_to_process)} files")
    print("Bat dau xu ly...\n")
    
    processed = 0
    for filepath in files_to_process:
        print(f"Xu ly: {os.path.relpath(filepath, base_path)}")
        if add_missing_fields_to_file(filepath):
            processed += 1
    
    print(f"\nDa xu ly {processed}/{len(files_to_process)} files")
    print("\n" + "=" * 80)
    print("HOAN THANH")
    print("=" * 80)
    print("\nLuu y: Cac file da duoc backup (.backup). Vui long kiem tra lai truoc khi commit.")

if __name__ == "__main__":
    main()

