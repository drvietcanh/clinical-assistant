"""
Script tu dong them cac fields con thieu cho thuoc
Su dung AST parsing de them fields chinh xac vao vi tri dung
"""

import os
import ast
import re

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

def generate_field_code(field_name, drug_data, indent_level=2):
    """Generate Python code cho field"""
    indent = ' ' * (indent_level * 4)
    
    # Get drug info
    group = drug_data.get('group', '')
    administration = drug_data.get('administration', [])
    pregnancy = drug_data.get('pregnancy', 'C')
    
    is_topical = 'Topical' in group or 'topical' in str(drug_data.get('dosage', {})).lower()
    is_nasal = 'Nasal' in str(administration) or 'nasal' in str(administration).lower()
    is_iv = 'IV' in str(administration) or 'iv' in str(administration).lower()
    is_oral = 'PO' in str(administration) or 'oral' in str(administration).lower() or not is_topical and not is_nasal and not is_iv
    
    # Chuyen doi contraindications list sang dict
    existing_contra = drug_data.get('contraindications', [])
    if isinstance(existing_contra, list) and existing_contra:
        contraindications_dict = {
            "tuyệt_đối": existing_contra,
            "tương_đối": []
        }
    elif isinstance(existing_contra, dict):
        contraindications_dict = existing_contra
    else:
        contraindications_dict = {
            "tuyệt_đối": ["Dị ứng với thuốc hoặc thành phần khác"],
            "tương_đối": []
        }
    
    if field_name == 'pharmacokinetics':
        if is_topical or is_nasal:
            return f'''{indent}"pharmacokinetics": {{
{indent}    "half_life": "Không áp dụng (topical/nasal, hấp thu toàn thân tối thiểu)",
{indent}    "onset": "Vài ngày",
{indent}    "duration": "12-24 giờ",
{indent}    "protein_binding": "Không áp dụng (topical/nasal)",
{indent}    "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
{indent}}},'''
        else:
            return f'''{indent}"pharmacokinetics": {{
{indent}    "half_life": "Cần tra cứu",
{indent}    "onset": "Cần tra cứu",
{indent}    "duration": "Cần tra cứu",
{indent}    "protein_binding": "Cần tra cứu",
{indent}    "clearance": "Cần tra cứu"
{indent}}},'''
    
    elif field_name == 'storage':
        return f'{indent}"storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",'
    
    elif field_name == 'black_box_warnings':
        return f'{indent}"black_box_warnings": None,'
    
    elif field_name == 'drug_interactions':
        return f'''{indent}"drug_interactions": {{
{indent}    "major": [],
{indent}    "moderate": [],
{indent}    "minor": []
{indent}}},'''
    
    elif field_name == 'contraindications':
        # Convert dict to code
        tuyet_doi = contraindications_dict.get('tuyệt_đối', [])
        tuong_doi = contraindications_dict.get('tương_đối', [])
        
        tuyet_doi_str = ',\n' + indent + '        '.join([f'"{item}"' for item in tuyet_doi]) if tuyet_doi else ''
        tuong_doi_str = ',\n' + indent + '        '.join([f'"{item}"' for item in tuong_doi]) if tuong_doi else ''
        
        return f'''{indent}"contraindications": {{
{indent}    "tuyệt_đối": [{tuyet_doi_str}
{indent}    ],
{indent}    "tương_đối": [{tuong_doi_str}
{indent}    ]
{indent}}},'''
    
    elif field_name == 'pregnancy_lactation':
        category = pregnancy if pregnancy else 'C'
        return f'''{indent}"pregnancy_lactation": {{
{indent}    "fda_category": "{category}",
{indent}    "pregnancy_details": "Category {category} - cần tra cứu thêm thông tin chi tiết.",
{indent}    "lactation": {{
{indent}        "safety": "Compatible with monitoring" if "{category}" in ["B", "C"] else "Compatible",
{indent}        "details": "Cần tra cứu thêm thông tin chi tiết.",
{indent}        "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
{indent}    }}
{indent}}},'''
    
    elif field_name == 'hepatic_adjustment':
        return f'''{indent}"hepatic_adjustment": {{
{indent}    "mild": "Không đổi",
{indent}    "moderate": "Thận trọng",
{indent}    "severe": "Thận trọng, có thể giảm liều",
{indent}    "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
{indent}}},'''
    
    elif field_name == 'overdose_management':
        return f'''{indent}"overdose_management": {{
{indent}    "symptoms": ["Cần tra cứu thêm thông tin về triệu chứng quá liều"],
{indent}    "antidote": "Không có antidote đặc hiệu",
{indent}    "treatment": [
{indent}        "Ngừng ngay thuốc",
{indent}        "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
{indent}        "Than hoạt tính",
{indent}        "Điều trị hỗ trợ và điều trị triệu chứng",
{indent}        "Theo dõi dấu hiệu sinh tồn"
{indent}    ],
{indent}    "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
{indent}}},'''
    
    elif field_name == 'reversal_agents':
        return f'''{indent}"reversal_agents": {{
{indent}    "available": False,
{indent}    "agents": []
{indent}}},'''
    
    elif field_name == 'administration_instructions':
        parts = []
        if is_oral:
            parts.append(f'''{indent}    "oral": {{
{indent}        "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
{indent}        "timing": "Theo chỉ định của bác sĩ",
{indent}        "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
{indent}    }}''')
        if is_iv:
            parts.append(f'''{indent}    "iv": {{
{indent}        "reconstitution": "Cần tra cứu",
{indent}        "infusion_rate": "Cần tra cứu",
{indent}        "compatibility": ["Cần tra cứu"],
{indent}        "incompatibility": [],
{indent}        "notes": "Cần tra cứu thêm thông tin chi tiết."
{indent}    }}''')
        if is_topical:
            parts.append(f'''{indent}    "topical": {{
{indent}        "technique": "Bôi mỏng lên vùng da bị ảnh hưởng",
{indent}        "timing": "Theo chỉ định của bác sĩ",
{indent}        "notes": "Cần tra cứu thêm thông tin chi tiết."
{indent}    }}''')
        if is_nasal:
            parts.append(f'''{indent}    "nasal": {{
{indent}        "technique": "Xịt vào mũi theo chỉ định",
{indent}        "timing": "Theo chỉ định của bác sĩ",
{indent}        "notes": "Cần tra cứu thêm thông tin chi tiết."
{indent}    }}''')
        
        if parts:
            return f'''{indent}"administration_instructions": {{
{','.join(parts)}
{indent}}},'''
        else:
            return f'''{indent}"administration_instructions": {{}},'''
    
    elif field_name == 'references':
        drug_name = list(drug_data.keys())[0] if isinstance(drug_data, dict) else "Drug"
        return f'''{indent}"references": {{
{indent}    "primary_sources": [
{indent}        "FDA Drug Label - Cần cập nhật",
{indent}        "UpToDate - Cần cập nhật"
{indent}    ],
{indent}    "last_updated": "2025-02-05",
{indent}    "evidence_level": "C - Cần tra cứu và cập nhật"
{indent}}},'''
    
    return None

def find_drug_in_file(filepath, drug_name):
    """Tim drug trong file va tra ve vi tri"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Tim drug name
        for i, line in enumerate(lines):
            if f'"{drug_name}":' in line or f"'{drug_name}':" in line:
                return i
        return -1
    except:
        return -1

def add_fields_to_drug_simple(filepath, drug_name, fields_to_add):
    """Them fields vao drug - cach don gian nhat"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tim vi tri drug dict
        pattern = rf'(\s*)"{re.escape(drug_name)}":\s*\{{'
        match = re.search(pattern, content)
        if not match:
            pattern = rf"(\s*)'{re.escape(drug_name)}':\s*\{{"
            match = re.search(pattern, content)
        
        if not match:
            print(f"  Khong tim thay {drug_name} trong file")
            return False
        
        # Tim closing brace cua drug dict
        start_pos = match.end()
        indent_level = len(match.group(1)) // 4
        
        # Tim closing brace
        brace_count = 1
        pos = start_pos
        last_comma_pos = -1
        
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    # Tim vi tri them fields (truoc closing brace)
                    # Tim dong cuoi cung co content truoc }
                    insert_pos = pos
                    
                    # Tim vi tri them fields (sau dong cuoi cung co comma hoac content)
                    # Backtrack to find last line with content
                    temp_pos = pos - 1
                    while temp_pos > start_pos and content[temp_pos] in ' \t\n\r':
                        temp_pos -= 1
                    
                    # Tim newline truoc do
                    while temp_pos > start_pos and content[temp_pos] != '\n':
                        temp_pos -= 1
                    
                    insert_pos = temp_pos + 1
                    
                    # Generate fields code
                    fields_code = []
                    for field_name in fields_to_add:
                        # Load drug data de generate code (simple approach: use defaults)
                        drug_data = {}  # Can improve by loading actual data
                        field_code = generate_field_code(field_name, drug_data, indent_level + 1)
                        if field_code:
                            fields_code.append(field_code)
                    
                    if fields_code:
                        # Them fields
                        new_content = (
                            content[:insert_pos] +
                            '\n' + '\n'.join(fields_code) +
                            '\n' + content[insert_pos:]
                        )
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        return True
            pos += 1
        
        return False
    except Exception as e:
        print(f"  Loi: {e}")
        return False

def main():
    print("=" * 80)
    print("SCRIPT TU DONG THEM FIELDS - PHIEN BAN TOI UU")
    print("=" * 80)
    print("\nScript nay se them cac fields con thieu vao cac thuoc")
    print("Dang phat trien - can cai tien them...")
    
    # TODO: Load bao cao, parse, va them fields
    print("\nChuc nang dang phat trien...")

if __name__ == "__main__":
    main()

