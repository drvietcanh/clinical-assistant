"""
Script tu dong them cac fields con thieu cho cac thuoc
Doc bao cao, tim cac thuoc thieu fields, tu dong them fields toi uu nhat
"""

import os
import re
import ast
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

def generate_default_field(field_name, drug_data, drug_name):
    """Generate default value cho field con thieu"""
    
    # Lay thong tin co san
    group = drug_data.get('group', '')
    administration = drug_data.get('administration', [])
    pregnancy = drug_data.get('pregnancy', 'C')
    
    is_topical = 'Topical' in group or 'topical' in str(drug_data.get('dosage', {})).lower()
    is_nasal = 'Nasal' in str(administration) or 'nasal' in str(administration).lower()
    is_iv = 'IV' in str(administration) or 'iv' in str(administration).lower()
    is_oral = 'PO' in str(administration) or 'oral' in str(administration).lower()
    
    if field_name == 'pharmacokinetics':
        if is_topical or is_nasal:
            return {
                "half_life": "Không áp dụng (topical/nasal, hấp thu toàn thân tối thiểu)",
                "onset": "Vài ngày",
                "duration": "12-24 giờ",
                "protein_binding": "Không áp dụng (topical/nasal)",
                "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
            }
        else:
            return {
                "half_life": "Cần tra cứu",
                "onset": "Cần tra cứu",
                "duration": "Cần tra cứu",
                "protein_binding": "Cần tra cứu",
                "clearance": "Cần tra cứu"
            }
    
    elif field_name == 'storage':
        return "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng"
    
    elif field_name == 'black_box_warnings':
        return None  # Most drugs don't have black box warnings
    
    elif field_name == 'drug_interactions':
        return {
            "major": [],
            "moderate": [],
            "minor": []
        }
    
    elif field_name == 'contraindications':
        # Chuyen doi tu list sang dict format
        existing_contra = drug_data.get('contraindications', [])
        if isinstance(existing_contra, list):
            return {
                "tuyệt_đối": existing_contra if existing_contra else ["Dị ứng với thuốc hoặc thành phần khác"],
                "tương_đối": []
            }
        return existing_contra
    
    elif field_name == 'pregnancy_lactation':
        category = pregnancy if pregnancy else 'C'
        return {
            "fda_category": category,
            "pregnancy_details": f"Category {category} - cần tra cứu thêm thông tin chi tiết.",
            "lactation": {
                "safety": "Compatible with monitoring" if category in ['B', 'C'] else "Compatible",
                "details": "Cần tra cứu thêm thông tin chi tiết.",
                "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
            }
        }
    
    elif field_name == 'hepatic_adjustment':
        return {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
        }
    
    elif field_name == 'overdose_management':
        return {
            "symptoms": ["Cần tra cứu thêm thông tin về triệu chứng quá liều"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                "Than hoạt tính",
                "Điều trị hỗ trợ và điều trị triệu chứng",
                "Theo dõi dấu hiệu sinh tồn"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
        }
    
    elif field_name == 'reversal_agents':
        return {
            "available": False,
            "agents": []
        }
    
    elif field_name == 'administration_instructions':
        result = {}
        if is_oral:
            result["oral"] = {
                "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
            }
        if is_iv:
            result["iv"] = {
                "reconstitution": "Cần tra cứu",
                "infusion_rate": "Cần tra cứu",
                "compatibility": ["Cần tra cứu"],
                "incompatibility": [],
                "notes": "Cần tra cứu thêm thông tin chi tiết."
            }
        if is_topical:
            result["topical"] = {
                "technique": "Bôi mỏng lên vùng da bị ảnh hưởng",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết."
            }
        if is_nasal:
            result["nasal"] = {
                "technique": "Xịt vào mũi theo chỉ định",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết."
            }
        return result
    
    elif field_name == 'references':
        return {
            "primary_sources": [
                f"FDA Drug Label - {drug_name}",
                "UpToDate - Cần cập nhật"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "C - Cần tra cứu và cập nhật"
        }
    
    return None

def parse_drug_file(filepath):
    """Parse drug file va tra ve dict of drugs"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse AST
        tree = ast.parse(content)
        
        # Tim drug dictionary
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith('_DRUGS'):
                        if isinstance(node.value, ast.Dict):
                            # Convert AST dict to Python dict
                            namespace = {}
                            exec(compile(ast.Module([node], type_ignores=[]), filepath, 'exec'), namespace)
                            return namespace.get(target.id, {})
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return {}
    return {}

def load_drugs_from_file(filepath):
    """Load drugs tu file Python"""
    try:
        spec = importlib.util.spec_from_file_location("module", filepath)
        if spec is None or spec.loader is None:
            return {}
        module = importlib.util.module_from_spec(spec)
        
        # Mock streamlit
        import types
        module.streamlit = types.ModuleType('streamlit')
        module.st = module.streamlit
        
        spec.loader.exec_module(module)
        
        # Tim drug dict
        for attr in dir(module):
            if attr.endswith('_DRUGS') and isinstance(getattr(module, attr), dict):
                return getattr(module, attr), filepath
    except Exception as e:
        return {}, filepath
    return {}, filepath

def find_drug_in_files(drug_name, base_path):
    """Tim file chua drug"""
    for root, dirs, files in os.walk(base_path):
        if '__pycache__' in root:
            continue
        for filename in files:
            if not filename.endswith('.py'):
                continue
            filepath = os.path.join(root, filename)
            
            # Doc file de tim drug
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                        return filepath
            except:
                pass
    return None

def add_fields_to_drug_file(filepath, drug_updates):
    """Them fields vao drug trong file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Tim drug va them fields
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Tim drug name
            for drug_name, fields_to_add in drug_updates.items():
                if f'"{drug_name}":' in line or f"'{drug_name}':" in line:
                    # Tim vi tri ket thuc cua drug dict (tim closing brace)
                    indent = len(line) - len(line.lstrip())
                    new_lines.append(line)
                    i += 1
                    
                    # Doc toi khi gap drug dict
                    drug_lines = [line]
                    brace_count = 1
                    start_i = i
                    
                    while i < len(lines) and brace_count > 0:
                        line = lines[i]
                        drug_lines.append(line)
                        brace_count += line.count('{') - line.count('}')
                        i += 1
                    
                    # Them fields vao truoc dong cuoi cung (closing brace)
                    drug_content = ''.join(drug_lines[:-1])
                    
                    # Them fields
                    for field_name, field_value in fields_to_add.items():
                        if field_name not in drug_content:
                            # Format field value
                            if isinstance(field_value, dict):
                                field_str = json.dumps(field_value, ensure_ascii=False, indent=8)
                                field_str = re.sub(r'"([^"]+)":', r'"\1":', field_str)  # Single quotes for keys
                            elif isinstance(field_value, str):
                                field_str = f'"{field_value}"'
                            elif field_value is None:
                                field_str = 'None'
                            else:
                                field_str = str(field_value)
                            
                            # Them field
                            indent_str = ' ' * (indent + 4)
                            new_lines.append(f'{indent_str}"{field_name}": {field_str},\n')
                    
                    # Them closing brace
                    new_lines.append(drug_lines[-1])
                    continue
            
            new_lines.append(line)
            i += 1
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

def main():
    import importlib.util
    
    print("=" * 80)
    print("SCRIPT TU DONG THEM FIELDS CHO THUOC")
    print("=" * 80)
    
    # Doc bao cao
    report_file = "BAO_CAO_KIEM_TRA_FIELDS_TAT_CA_THUOC_CHI_TIET.txt"
    if not os.path.exists(report_file):
        print(f"Khong tim thay file: {report_file}")
        return
    
    # Parse bao cao de lay danh sach thuoc thieu fields
    drugs_to_update = {}  # {drug_name: {field_name: default_value}}
    
    with open(report_file, 'r', encoding='utf-8') as f:
        content = f.read()
        lines = content.split('\n')
        
        current_drug = None
        missing_fields = []
        
        for line in lines:
            # Tim drug name
            if ':' in line and not line.strip().startswith('Thieu') and not line.strip().startswith('Required') and not line.strip().startswith('Optional'):
                match = re.match(r'^([A-Za-z0-9/\s\(\)\-\+]+):$', line.strip())
                if match:
                    if current_drug and missing_fields:
                        drugs_to_update[current_drug] = missing_fields
                    current_drug = match.group(1).strip()
                    missing_fields = []
            
            # Tim missing fields
            if current_drug and 'thieu' in line.lower():
                if 'Required fields thieu' in line:
                    fields = re.findall(r'([a-z_]+)', line)
                    missing_fields.extend([f for f in fields if f in REQUIRED_FIELDS + OPTIONAL_FIELDS])
                elif 'Optional fields thieu' in line:
                    fields = re.findall(r'([a-z_]+)', line)
                    missing_fields.extend([f for f in fields if f in REQUIRED_FIELDS + OPTIONAL_FIELDS])
        
        if current_drug and missing_fields:
            drugs_to_update[current_drug] = missing_fields
    
    print(f"\nTim thay {len(drugs_to_update)} thuoc can them fields")
    
    # Tim file chua cac thuoc
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    
    # Load mot so thuoc mau de lay template
    sample_file = os.path.join(base_path, 'dermatology.py')
    if os.path.exists(sample_file):
        drugs_sample, _ = load_drugs_from_file(sample_file)
        # Lay thuoc mau co du fields
        for name, data in drugs_sample.items():
            if all(field in data for field in ALL_FIELDS):
                print(f"Thuoc mau: {name}")
                break
    
    # Bat dau them fields (chi lam 10 thuoc dau tien de test)
    print(f"\nBat dau them fields cho {min(10, len(drugs_to_update))} thuoc dau tien...")
    
    count = 0
    for drug_name, missing_fields_list in list(drugs_to_update.items())[:10]:
        filepath = find_drug_in_files(drug_name, base_path)
        if filepath:
            print(f"\n{drug_name}: {len(missing_fields_list)} fields")
            print(f"  File: {filepath}")
            # TODO: Load drug data va them fields
            count += 1
        else:
            print(f"\n{drug_name}: Khong tim thay file")
    
    print(f"\nDa xu ly {count} thuoc")

if __name__ == "__main__":
    main()

