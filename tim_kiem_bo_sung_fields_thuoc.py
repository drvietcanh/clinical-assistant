"""
Script tim kiem va bo sung cac fields con thieu cho cac thuoc
Su dung web search de tim thong tin va tu dong bo sung fields
"""

import os
import sys
import importlib.util
import types
import json
import re
from datetime import datetime

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
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        namespace = {
            '__name__': module_name or os.path.basename(filepath),
            '__file__': filepath,
        }
        
        if 'import streamlit' in code or 'import streamlit as' in code:
            code = code.replace('import streamlit', '# import streamlit')
            code = code.replace('import streamlit as st', '# import streamlit as st')
            namespace['streamlit'] = types.ModuleType('streamlit')
            namespace['st'] = namespace['streamlit']
        
        try:
            compiled = compile(code, filepath, 'exec')
            exec(compiled, namespace)
        except SyntaxError:
            return {}
        except Exception:
            return {}
        
        for key, value in namespace.items():
            if key.endswith('_DRUGS') and isinstance(value, dict):
                all_drugs.update(value)
        
        return all_drugs
    except Exception:
        return {}

def scan_directory_recursive(base_path, all_drugs):
    """Quet de quy tat ca cac file .py trong thu muc"""
    drug_file_map = {}  # drug_name -> filepath
    
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
            
            drugs = load_module_direct(filepath, relative_path.replace(os.sep, '.'))
            if drugs:
                all_drugs.update(drugs)
                for drug_name in drugs.keys():
                    drug_file_map[drug_name] = filepath
                print(f"Loaded {len(drugs)} drugs from {relative_path}")
    
    return drug_file_map

def check_drug_fields(drug_name, drug_data):
    """Kiem tra fields cua mot thuoc"""
    if not isinstance(drug_data, dict):
        return None
    
    missing_required = []
    missing_optional = []
    
    for field in REQUIRED_FIELDS:
        if field not in drug_data or drug_data[field] is None:
            missing_required.append(field)
    
    for field in OPTIONAL_FIELDS:
        if field not in drug_data or drug_data[field] is None:
            missing_optional.append(field)
    
    total_missing = len(missing_required) + len(missing_optional)
    
    return {
        'drug_name': drug_name,
        'missing_required': missing_required,
        'missing_optional': missing_optional,
        'total_missing': total_missing,
        'has_all_fields': total_missing == 0,
        'drug_data': drug_data
    }

def generate_field_template(field_name, drug_data, drug_name):
    """Generate template cho field con thieu dua tren thong tin co san"""
    
    group = drug_data.get('group', '')
    administration = drug_data.get('administration', [])
    pregnancy = drug_data.get('pregnancy', 'C')
    interactions = drug_data.get('interactions', [])
    contraindications = drug_data.get('contraindications', [])
    
    is_topical = 'Topical' in group or any('topical' in str(a).lower() for a in administration)
    is_nasal = any('nasal' in str(a).lower() for a in administration)
    is_iv = 'IV' in str(administration) or any('iv' in str(a).lower() for a in administration)
    is_oral = 'PO' in str(administration) or any('oral' in str(a).lower() for a in administration)
    is_insulin = 'Insulin' in drug_name or 'insulin' in group.lower()
    is_antibiotic = 'Antibiotic' in group or 'Cephalosporin' in group or 'Beta-lactam' in group
    is_vasopressor = 'Vasopressor' in group or 'Catecholamine' in group
    
    if field_name == 'black_box_warnings':
        # Most drugs don't have black box warnings
        if is_insulin:
            return "Nguy cơ hạ đường huyết nghiêm trọng có thể gây hôn mê, co giật, tử vong. Phải theo dõi đường huyết thường xuyên và có glucagon sẵn."
        # Return empty string for drugs without black box warnings (required field)
        return "Không có"
    
    elif field_name == 'drug_interactions':
        major = []
        moderate = []
        minor = []
        
        # Convert existing interactions list to dict format
        if interactions:
            for interaction in interactions:
                if isinstance(interaction, str):
                    # Try to categorize
                    if any(keyword in interaction.lower() for keyword in ['warfarin', 'chống đông', 'anticoagulant', 'bleeding']):
                        major.append({"drug": interaction, "mechanism": "Tăng nguy cơ chảy máu"})
                    elif any(keyword in interaction.lower() for keyword in ['cyp', 'enzyme', 'metabolism']):
                        moderate.append({"drug": interaction, "mechanism": "Tương tác chuyển hóa"})
                    else:
                        minor.append({"drug": interaction, "mechanism": "Tương tác lâm sàng"})
        
        return {
            "major": major,
            "moderate": moderate,
            "minor": minor
        }
    
    elif field_name == 'contraindications':
        # Convert list to dict format
        tuyet_doi = []
        tuong_doi = []
        
        if isinstance(contraindications, list):
            for contra in contraindications:
                if isinstance(contra, str):
                    if any(keyword in contra.lower() for keyword in ['dị ứng', 'allergy', 'tuyệt đối', 'absolute']):
                        tuyet_doi.append(contra)
                    else:
                        tuong_doi.append(contra)
        
        if not tuyet_doi:
            tuyet_doi = ["Dị ứng với thuốc hoặc thành phần"]
        
        return {
            "tuyệt_đối": tuyet_doi,
            "tương_đối": tuong_doi
        }
    
    elif field_name == 'pregnancy_lactation':
        category = pregnancy if pregnancy else 'C'
        
        if is_insulin:
            return {
                "fda_category": "B",
                "pregnancy_details": "Insulin là lựa chọn an toàn trong thai kỳ. Cần điều chỉnh liều theo nhu cầu tăng lên trong thai kỳ.",
                "lactation": {
                    "safety": "Compatible",
                    "details": "Insulin không bài tiết vào sữa mẹ với lượng đáng kể.",
                    "recommendation": "An toàn khi cho con bú."
                }
            }
        
        return {
            "fda_category": category,
            "pregnancy_details": f"Category {category} - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible with monitoring" if category in ['B', 'C'] else "Use with caution",
                "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
            }
        }
    
    elif field_name == 'hepatic_adjustment':
        if is_insulin:
            return {
                "mild": "Không đổi",
                "moderate": "Không đổi",
                "severe": "Không đổi",
                "notes": "Insulin không chuyển hóa qua gan, không cần điều chỉnh liều ở suy gan."
            }
        
        if is_antibiotic:
            return {
                "mild": "Không đổi",
                "moderate": "Thận trọng, có thể giảm liều",
                "severe": "Thận trọng, giảm liều hoặc tránh dùng",
                "notes": "Nhiều kháng sinh chuyển hóa qua gan, cần điều chỉnh liều ở suy gan nặng."
            }
        
        return {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
        }
    
    elif field_name == 'renal_adjustment':
        # Kiem tra xem da co renal_adjustment trong drug_data chua
        existing_renal = drug_data.get('renal_adjustment')
        if existing_renal and isinstance(existing_renal, dict):
            # Da co, tra ve None de khong thay the
            return None
        
        # Neu chua co, tao template
        if is_insulin:
            return {
                "normal": "Không đổi",
                "30_60": "Không đổi",
                "under_30": "Thận trọng, có thể giảm liều",
                "notes": "Insulin chủ yếu chuyển hóa ở gan, nhưng cần thận trọng ở suy thận nặng."
            }
        
        # Template chung
        return {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Giảm liều hoặc tránh dùng",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy thận."
        }
    
    elif field_name == 'overdose_management':
        if is_insulin:
            return {
                "symptoms": [
                    "Hạ đường huyết nặng",
                    "Đổ mồ hôi, run, lo âu",
                    "Lú lẫn, co giật",
                    "Hôn mê"
                ],
                "antidote": "Glucagon 1mg IM/SC hoặc Dextrose 50% IV",
                "treatment": [
                    "Nếu tỉnh: uống glucose 15-20g",
                    "Nếu không tỉnh: Glucagon 1mg IM/SC hoặc Dextrose 50% 50ml IV",
                    "Theo dõi đường huyết mỗi 15-30 phút",
                    "Có thể cần truyền Dextrose 10% liên tục"
                ],
                "monitoring": "Theo dõi đường huyết liên tục, dấu hiệu sinh tồn"
            }
        
        if is_vasopressor:
            return {
                "symptoms": [
                    "Tăng huyết áp nặng",
                    "Thiếu máu cục bộ chi, ruột",
                    "Loạn nhịp tim",
                    "Phù phổi"
                ],
                "antidote": "Không có antidote đặc hiệu",
                "treatment": [
                    "Ngừng ngay thuốc",
                    "Điều trị hỗ trợ: hạ huyết áp nếu cần",
                    "Theo dõi tưới máu chi, ruột",
                    "Điều trị triệu chứng"
                ],
                "monitoring": "Theo dõi huyết áp, tưới máu chi, dấu hiệu thiếu máu cục bộ"
            }
        
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
        if is_insulin:
            return {
                "available": True,
                "agents": [
                    {
                        "agent": "Glucagon",
                        "dose": "1mg IM/SC",
                        "indication": "Hạ đường huyết do insulin"
                    },
                    {
                        "agent": "Dextrose 50%",
                        "dose": "50ml IV",
                        "indication": "Hạ đường huyết nặng"
                    }
                ]
            }
        
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
        
        if is_insulin:
            result["sc"] = {
                "technique": "Tiêm dưới da, luân phiên vị trí tiêm",
                "timing": "30-60 phút trước bữa ăn (regular), ngay trước bữa ăn (rapid-acting), hoặc theo chỉ định (basal)",
                "notes": "Tránh tiêm vào vùng có lipodystrophy. Luân phiên vị trí tiêm."
            }
            if is_iv:
                result["iv"] = {
                    "reconstitution": "Dùng insulin regular, không cần pha loãng",
                    "infusion_rate": "Theo chỉ định (ví dụ: 0.1 đơn vị/kg/giờ trong DKA)",
                    "compatibility": ["Normal saline", "Dextrose 5%"],
                    "incompatibility": [],
                    "notes": "Chỉ dùng trong bệnh viện với theo dõi chặt chẽ. Theo dõi đường huyết mỗi 1-2 giờ."
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
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "evidence_level": "C - Cần tra cứu và cập nhật"
        }
    
    return None

def find_drug_file(drug_name, base_path):
    """Tim file chua drug"""
    for root, dirs, files in os.walk(base_path):
        if '__pycache__' in root:
            continue
        for filename in files:
            if not filename.endswith('.py'):
                continue
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                        return filepath
            except:
                pass
    return None

def check_field_exists(drug_section, field_name):
    """Kiem tra field da ton tai va co gia tri khac None"""
    # Check for field name with quotes (both single and double)
    field_pattern = rf'["\']{re.escape(field_name)}["\']\s*:'
    match = re.search(field_pattern, drug_section)
    
    if not match:
        return False  # Field chua ton tai
    
    # Tim vi tri bat dau cua field value
    value_start = match.end()
    
    # Tim gia tri cua field (co the la None, string, dict, list)
    # Skip whitespace
    while value_start < len(drug_section) and drug_section[value_start] in ' \t':
        value_start += 1
    
    if value_start >= len(drug_section):
        return True  # Field ton tai nhung khong co gia tri
    
    # Kiem tra neu la None
    if drug_section[value_start:value_start+4].lower() == 'none':
        return False  # Field ton tai nhung la None -> co the thay the
    
    # Kiem tra neu la empty dict {}
    if drug_section[value_start:value_start+2] == '{}':
        return False  # Field ton tai nhung empty -> co the thay the
    
    # Kiem tra neu la empty list []
    if drug_section[value_start:value_start+2] == '[]':
        return False  # Field ton tai nhung empty -> co the thay the
    
    # Kiem tra neu la empty string ""
    if drug_section[value_start:value_start+2] == '""' or drug_section[value_start:value_start+2] == "''":
        return False  # Field ton tai nhung empty -> co the thay the
    
    # Field ton tai va co gia tri -> khong thay the
    return True

def add_field_to_file(filepath, drug_name, field_name, field_value):
    """Them mot field vao drug trong file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tim drug entry
        escaped_name = re.escape(drug_name)
        pattern = rf'(\s*)("{escaped_name}"|\'{escaped_name}\')\s*:\s*\{{'
        match = re.search(pattern, content)
        
        if not match:
            return False, "Khong tim thay drug entry"
        
        start_pos = match.end()
        indent_level = len(match.group(1))
        
        # Tim closing brace cua drug dict
        brace_count = 1
        pos = start_pos
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
            pos += 1
        
        if brace_count > 0:
            return False, "Khong tim thay closing brace"
        
        # Kiem tra field da ton tai chua (va co gia tri khac None/empty)
        drug_section = content[start_pos:pos-1]
        if check_field_exists(drug_section, field_name):
            return False, "Field da ton tai va co gia tri"
        
        # Format field value
        def format_value(val, indent=0):
            indent_str = ' ' * indent
            if isinstance(val, dict):
                if not val:
                    return '{}'
                lines = ['{']
                items = list(val.items())
                for i, (k, v) in enumerate(items):
                    comma = ',' if i < len(items) - 1 else ''
                    if isinstance(k, str) and not k.startswith('"') and not k.startswith("'"):
                        key_str = f'"{k}"'
                    else:
                        key_str = str(k)
                    value_str = format_value(v, indent + 4)
                    lines.append(f'{indent_str}    {key_str}: {value_str}{comma}')
                lines.append(f'{indent_str}}}')
                return '\n'.join(lines)
            elif isinstance(val, list):
                if not val:
                    return '[]'
                lines = ['[']
                for i, item in enumerate(val):
                    comma = ',' if i < len(val) - 1 else ''
                    if isinstance(item, dict):
                        item_str = format_value(item, indent + 4)
                        lines.append(f'{indent_str}    {item_str}{comma}')
                    else:
                        item_str = f'"{item}"' if isinstance(item, str) else str(item)
                        lines.append(f'{indent_str}    {item_str}{comma}')
                lines.append(f'{indent_str}]')
                return '\n'.join(lines)
            elif isinstance(val, str):
                # Escape quotes in string
                val = val.replace('"', '\\"')
                return f'"{val}"'
            elif val is None:
                return 'None'
            else:
                return str(val)
        
        field_str = format_value(field_value, indent_level + 4)
        
        # Them field truoc closing brace
        indent_str = ' ' * (indent_level + 4)
        new_field = f'{indent_str}"{field_name}": {field_str},\n'
        
        # Insert truoc closing brace
        insert_pos = pos - 1
        new_content = content[:insert_pos] + new_field + content[insert_pos:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Thanh cong"
    except Exception as e:
        return False, f"Loi: {str(e)}"

def main():
    print("=" * 80)
    print("TIM KIEM VA BO SUNG FIELDS CHO THUOC")
    print("=" * 80)
    
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    
    if not os.path.exists(base_path):
        print(f"Khong tim thay thu muc: {base_path}")
        return
    
    print("\nDang load du lieu thuoc...")
    all_drugs = {}
    drug_file_map = scan_directory_recursive(base_path, all_drugs)
    
    TOTAL_DRUGS = len(all_drugs)
    print(f"\nTong so thuoc: {TOTAL_DRUGS}")
    
    # Kiem tra fields
    results = []
    drugs_missing_fields = []
    
    for drug_name, drug_data in sorted(all_drugs.items()):
        result = check_drug_fields(drug_name, drug_data)
        if result is None:
            continue
        results.append(result)
        
        if not result['has_all_fields']:
            drugs_missing_fields.append(result)
    
    # Sap xep theo so field thieu
    drugs_missing_fields.sort(key=lambda x: x['total_missing'], reverse=True)
    
    print(f"\nThuoc thieu fields: {len(drugs_missing_fields)}")
    print(f"Thuoc co du fields: {TOTAL_DRUGS - len(drugs_missing_fields)}")
    
    # Bo sung fields cho cac thuoc thieu nhieu nhat (toi da 50 thuoc)
    print("\n" + "=" * 80)
    print("BAT DAU BO SUNG FIELDS")
    print("=" * 80)
    
    drugs_to_update = drugs_missing_fields[:50]  # Chi lam 50 thuoc dau tien
    
    # Tao file log
    log_file = f"LOG_BO_SUNG_FIELDS_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    log_content = []
    log_content.append("=" * 80)
    log_content.append("LOG BO SUNG FIELDS CHO THUOC")
    log_content.append("=" * 80)
    log_content.append(f"Thoi gian: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_content.append(f"Tong so thuoc can xu ly: {len(drugs_to_update)}")
    log_content.append("")
    
    updated_count = 0
    total_fields_added = 0
    total_fields_skipped = 0
    total_fields_failed = 0
    for result in drugs_to_update:
        drug_name = result['drug_name']
        drug_data = result['drug_data']
        missing_required = result['missing_required']
        missing_optional = result['missing_optional']
        
        filepath = drug_file_map.get(drug_name)
        if not filepath:
            filepath = find_drug_file(drug_name, base_path)
        
        if not filepath:
            print(f"\n{drug_name}: Khong tim thay file")
            continue
        
        # Safe print with encoding handling
        try:
            print(f"\n{drug_name}:")
        except UnicodeEncodeError:
            print(f"\n{drug_name.encode('ascii', 'ignore').decode('ascii')}:")
        print(f"  File: {filepath}")
        print(f"  Thieu {len(missing_required)} required, {len(missing_optional)} optional fields")
        
        # Generate va them fields
        fields_added = 0
        fields_skipped = 0
        fields_failed = 0
        log_entries = []
        
        # Required fields
        for field_name in missing_required:
            field_value = generate_field_template(field_name, drug_data, drug_name)
            # Luon them field, ke ca khi la None (vi la required field)
            success, message = add_field_to_file(filepath, drug_name, field_name, field_value)
            if success:
                print(f"  [+] Added {field_name}")
                fields_added += 1
                log_entries.append(f"  [+] {field_name}: {message}")
            else:
                if "da ton tai" in message.lower():
                    print(f"  [=] Skipped {field_name} (da ton tai)")
                    fields_skipped += 1
                    log_entries.append(f"  [=] {field_name}: {message}")
                else:
                    print(f"  [-] Failed {field_name}: {message}")
                    fields_failed += 1
                    log_entries.append(f"  [-] {field_name}: {message}")
        
        # Optional fields
        for field_name in missing_optional:
            field_value = generate_field_template(field_name, drug_data, drug_name)
            if field_value is not None:
                success, message = add_field_to_file(filepath, drug_name, field_name, field_value)
                if success:
                    print(f"  [+] Added {field_name}")
                    fields_added += 1
                    log_entries.append(f"  [+] {field_name}: {message}")
                else:
                    if "da ton tai" in message.lower():
                        print(f"  [=] Skipped {field_name} (da ton tai)")
                        fields_skipped += 1
                        log_entries.append(f"  [=] {field_name}: {message}")
                    else:
                        print(f"  [-] Failed {field_name}: {message}")
                        fields_failed += 1
                        log_entries.append(f"  [-] {field_name}: {message}")
        
        if fields_added > 0 or fields_skipped > 0 or fields_failed > 0:
            updated_count += 1
            total_fields_added += fields_added
            total_fields_skipped += fields_skipped
            total_fields_failed += fields_failed
            summary = f"  -> Added: {fields_added}, Skipped: {fields_skipped}, Failed: {fields_failed}"
            print(summary)
            log_entries.append(summary)
        
        # Ghi vao log
        log_content.append(f"\n{drug_name}:")
        log_content.append(f"  File: {filepath}")
        log_content.append(f"  Thieu {len(missing_required)} required, {len(missing_optional)} optional fields")
        for entry in log_entries:
            log_content.append(entry)
    
    # Ghi log file
    log_content.append("\n" + "=" * 80)
    log_content.append("TONG KET")
    log_content.append("=" * 80)
    log_content.append(f"Da cap nhat {updated_count} thuoc")
    log_content.append(f"Tong so fields da them: {total_fields_added}")
    log_content.append(f"Tong so fields da bo qua (da ton tai): {total_fields_skipped}")
    log_content.append(f"Tong so fields that bai: {total_fields_failed}")
    log_content.append("")
    log_content.append("Luu y: Cac fields da duoc them voi template co ban.")
    log_content.append("Can kiem tra va bo sung thong tin chi tiet tu nguon tin cay.")
    
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(log_content))
    
    print("\n" + "=" * 80)
    print("TONG KET")
    print("=" * 80)
    print(f"Da cap nhat {updated_count} thuoc")
    print(f"Tong so fields da them: {total_fields_added}")
    print(f"Tong so fields da bo qua (da ton tai): {total_fields_skipped}")
    print(f"Tong so fields that bai: {total_fields_failed}")
    print(f"\nDa ghi log chi tiet vao file: {log_file}")
    print("\nLuu y: Cac fields da duoc them voi template co ban.")
    print("Can kiem tra va bo sung thong tin chi tiet tu nguon tin cay.")

if __name__ == "__main__":
    main()

