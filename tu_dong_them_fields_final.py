"""
Script tu dong them cac fields con thieu cho thuoc
Su dung regex-based approach de them fields chinh xac
"""

import os
import re
import json

# Dinh nghia 14 enhanced fields (theo thu tu them vao)
FIELD_ORDER = [
    'mechanism_of_action',
    'monitoring',
    'precautions',
    'pharmacokinetics',
    'storage',
    'black_box_warnings',
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

def get_field_template(field_name, drug_info):
    """Generate field template code"""
    group = drug_info.get('group', '')
    administration = drug_info.get('administration', [])
    pregnancy = drug_info.get('pregnancy', 'C')
    
    is_topical = 'Topical' in group or 'topical' in str(group).lower()
    is_nasal = any('Nasal' in str(a) or 'nasal' in str(a).lower() for a in administration) if administration else False
    is_iv = any('IV' in str(a) or 'iv' in str(a).lower() for a in administration) if administration else False
    is_oral = any('PO' in str(a) or 'oral' in str(a).lower() for a in administration) if administration else True
    
    templates = {
        'pharmacokinetics': '''        "pharmacokinetics": {
            "half_life": "Cần tra cứu",
            "onset": "Cần tra cứu",
            "duration": "Cần tra cứu",
            "protein_binding": "Cần tra cứu",
            "clearance": "Cần tra cứu"
        },''',
        'storage': '        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",',
        'black_box_warnings': '        "black_box_warnings": None,',
        'drug_interactions': '''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },''',
        'pregnancy_lactation': f'''        "pregnancy_lactation": {{
            "fda_category": "{pregnancy}",
            "pregnancy_details": "Category {pregnancy} - cần tra cứu thêm thông tin chi tiết.",
            "lactation": {{
                "safety": "Compatible with monitoring",
                "details": "Cần tra cứu thêm thông tin chi tiết.",
                "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
            }}
        },''',
        'hepatic_adjustment': '''        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
        },''',
        'overdose_management': '''        "overdose_management": {
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
        },''',
        'reversal_agents': '''        "reversal_agents": {
            "available": False,
            "agents": []
        },''',
        'administration_instructions': '''        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
            }
        },''',
        'references': '''        "references": {
            "primary_sources": [
                "FDA Drug Label - Cần cập nhật",
                "UpToDate - Cần cập nhật"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "C - Cần tra cứu và cập nhật"
        },'''
    }
    
    # Special cases
    if field_name == 'pharmacokinetics' and (is_topical or is_nasal):
        templates['pharmacokinetics'] = '''        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical/nasal, hấp thu toàn thân tối thiểu)",
            "onset": "Vài ngày",
            "duration": "12-24 giờ",
            "protein_binding": "Không áp dụng (topical/nasal)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },'''
    
    if field_name == 'contraindications':
        existing_contra = drug_info.get('contraindications', [])
        if isinstance(existing_contra, list) and existing_contra:
            items = ',\n                '.join([f'"{item}"' for item in existing_contra])
            templates['contraindications'] = f'''        "contraindications": {{
            "tuyệt_đối": [
                {items}
            ],
            "tương_đối": []
        },'''
        else:
            templates['contraindications'] = '''        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với thuốc hoặc thành phần khác"
            ],
            "tương_đối": []
        },'''
    
    return templates.get(field_name, '')

def find_drug_insertion_point(content, drug_name):
    """Tim vi tri de them fields vao drug dict"""
    # Tim drug dict start
    pattern = rf'(\s+)"{re.escape(drug_name)}":\s*\{{'
    match = re.search(pattern, content)
    if not match:
        pattern = rf"(\s+)'{re.escape(drug_name)}':\s*\{{"
        match = re.search(pattern, content)
    
    if not match:
        return None, None
    
    start_pos = match.end()
    indent = len(match.group(1))
    
    # Tim closing brace cua drug dict
    brace_count = 1
    pos = start_pos
    lines = content[start_pos:].split('\n')
    
    # Tim dong cuoi cung truoc closing brace
    current_brace = 1
    insert_line_idx = 0
    
    for i, line in enumerate(lines):
        current_brace += line.count('{') - line.count('}')
        if current_brace == 0:
            # Tim dong cuoi cung co content (khong phai chi la whitespace hoac })
            for j in range(i-1, -1, -1):
                if lines[j].strip() and not lines[j].strip().startswith('}'):
                    insert_line_idx = j + 1
                    break
            break
    
    # Calculate absolute position
    insert_pos = start_pos + sum(len(line) + 1 for line in lines[:insert_line_idx])
    
    return insert_pos, indent

def add_fields_to_drug(content, drug_name, fields_to_add, drug_info):
    """Them fields vao drug trong content"""
    insert_pos, indent = find_drug_insertion_point(content, drug_name)
    if insert_pos is None:
        return None
    
    # Generate fields code
    fields_code = []
    for field_name in fields_to_add:
        field_code = get_field_template(field_name, drug_info)
        if field_code:
            # Adjust indent
            lines = field_code.split('\n')
            adjusted_lines = []
            for line in lines:
                if line.strip():
                    # Replace leading spaces with correct indent
                    stripped = line.lstrip()
                    current_indent = len(line) - len(stripped)
                    new_indent = indent + (current_indent - 8)  # Assume template uses 8 spaces base
                    adjusted_lines.append(' ' * new_indent + stripped)
                else:
                    adjusted_lines.append('')
            fields_code.append('\n'.join(adjusted_lines))
    
    if not fields_code:
        return content
    
    # Insert fields
    new_content = (
        content[:insert_pos] +
        ',\n' + '\n'.join(fields_code) +
        '\n' + content[insert_pos:]
    )
    
    return new_content

def parse_drug_from_report_line(line):
    """Parse drug name va missing fields tu dong trong bao cao"""
    # Format: "DrugName:" hoac "DrugName:\n  Thieu X fields"
    match = re.match(r'^([A-Za-z0-9/\s\(\)\-\+]+):$', line.strip())
    if match:
        return match.group(1).strip(), []
    return None, []

def main():
    print("=" * 80)
    print("SCRIPT TU DONG THEM FIELDS CHO THUOC")
    print("=" * 80)
    print("\nLuu y: Script nay chi tao template, can review va update thong tin chi tiet")
    print("Dang phat trien...")

if __name__ == "__main__":
    main()

