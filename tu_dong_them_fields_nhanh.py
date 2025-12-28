"""
Script tu dong them cac fields con thieu - PHIEN BAN NHANH NHAT
Su dung pattern matching don gian de them fields vao cuoi drug dict (truoc closing brace)
"""

import os
import re

def get_field_code(field_name, is_topical=False, is_nasal=False, is_oral=True, is_iv=False, pregnancy='C', contraindications_list=None):
    """Generate field code - template based"""
    
    if field_name == 'pharmacokinetics':
        if is_topical or is_nasal:
            return '''        "pharmacokinetics": {
            "half_life": "Không áp dụng (topical/nasal, hấp thu toàn thân tối thiểu)",
            "onset": "Vài ngày",
            "duration": "12-24 giờ",
            "protein_binding": "Không áp dụng (topical/nasal)",
            "clearance": "Hấp thu toàn thân tối thiểu từ dạng tại chỗ."
        },'''
        else:
            return '''        "pharmacokinetics": {
            "half_life": "Cần tra cứu",
            "onset": "Cần tra cứu",
            "duration": "Cần tra cứu",
            "protein_binding": "Cần tra cứu",
            "clearance": "Cần tra cứu"
        },'''
    
    elif field_name == 'storage':
        return '        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",'
    
    elif field_name == 'black_box_warnings':
        return '        "black_box_warnings": None,'
    
    elif field_name == 'drug_interactions':
        return '''        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },'''
    
    elif field_name == 'contraindications':
        if contraindications_list:
            items_str = ',\n                '.join([f'"{item}"' for item in contraindications_list])
            result = '        "contraindications": {\n            "tuyệt_đối": [\n                ' + items_str + '\n            ],\n            "tương_đối": []\n        },'
            return result
        else:
            return '''        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với thuốc hoặc thành phần khác"
            ],
            "tương_đối": []
        },'''
    
    elif field_name == 'pregnancy_lactation':
        preg_cat = pregnancy
        result = '        "pregnancy_lactation": {\n            "fda_category": "' + preg_cat + '",\n            "pregnancy_details": "Category ' + preg_cat + ' - cần tra cứu thêm thông tin chi tiết.",\n            "lactation": {\n                "safety": "Compatible with monitoring",\n                "details": "Cần tra cứu thêm thông tin chi tiết.",\n                "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."\n            }\n        },'
        return result
    
    elif field_name == 'hepatic_adjustment':
        return '''        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
        },'''
    
    elif field_name == 'overdose_management':
        return '''        "overdose_management": {
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
        },'''
    
    elif field_name == 'reversal_agents':
        return '''        "reversal_agents": {
            "available": False,
            "agents": []
        },'''
    
    elif field_name == 'administration_instructions':
        parts = []
        if is_oral:
            parts.append('''            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn (trừ khi có chỉ định khác)",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết về cách dùng."
            }''')
        if is_iv:
            parts.append('''            "iv": {
                "reconstitution": "Cần tra cứu",
                "infusion_rate": "Cần tra cứu",
                "compatibility": ["Cần tra cứu"],
                "incompatibility": [],
                "notes": "Cần tra cứu thêm thông tin chi tiết."
            }''')
        if is_topical:
            parts.append('''            "topical": {
                "technique": "Bôi mỏng lên vùng da bị ảnh hưởng",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết."
            }''')
        if is_nasal:
            parts.append('''            "nasal": {
                "technique": "Xịt vào mũi theo chỉ định",
                "timing": "Theo chỉ định của bác sĩ",
                "notes": "Cần tra cứu thêm thông tin chi tiết."
            }''')
        
        if parts:
            result = '        "administration_instructions": {\n' + ',\n'.join(parts) + '\n        },'
            return result
        else:
            return '''        "administration_instructions": {},'''
    
    elif field_name == 'references':
        return '''        "references": {
            "primary_sources": [
                "FDA Drug Label - Cần cập nhật",
                "UpToDate - Cần cập nhật"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "C - Cần tra cứu và cập nhật"
        },'''
    
    return ''

def add_fields_to_file(filepath, drug_name, fields_to_add):
    """Them fields vao drug trong file - cach don gian nhat"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tim drug dict
        pattern = rf'(\s+)"{re.escape(drug_name)}":\s*\{{'
        match = re.search(pattern, content)
        if not match:
            pattern = rf"(\s+)'{re.escape(drug_name)}':\s*\{{"
            match = re.search(pattern, content)
        
        if not match:
            return False, f"Khong tim thay {drug_name}"
        
        # Tim closing brace cua drug dict (tim tu start_pos)
        start_pos = match.end()
        brace_count = 1
        pos = start_pos
        
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
                if brace_count == 0:
                    # Tim vi tri them fields (truoc closing brace, sau dong cuoi cung)
                    # Backtrack de tim dong cuoi cung co content
                    insert_pos = pos
                    temp_pos = pos - 1
                    
                    # Skip whitespace
                    while temp_pos > start_pos and content[temp_pos] in ' \t\n\r':
                        temp_pos -= 1
                    
                    # Tim newline truoc do
                    while temp_pos > start_pos and content[temp_pos] != '\n':
                        temp_pos -= 1
                    
                    insert_pos = temp_pos + 1
                    
                    # Detect drug type from existing content (simple heuristics)
                    drug_content = content[start_pos:pos]
                    is_topical = 'topical' in drug_content.lower() or '"Topical"' in drug_content
                    is_nasal = 'nasal' in drug_content.lower() or '"Nasal"' in drug_content
                    is_iv = '"IV"' in drug_content or '"iv"' in drug_content
                    is_oral = not is_topical and not is_nasal and not is_iv
                    
                    # Get pregnancy category
                    preg_match = re.search(r'"pregnancy":\s*"([A-Z])"', drug_content)
                    pregnancy = preg_match.group(1) if preg_match else 'C'
                    
                    # Get contraindications list if exists
                    contra_match = re.search(r'"contraindications":\s*\[(.*?)\]', drug_content, re.DOTALL)
                    contraindications_list = None
                    if contra_match:
                        items = re.findall(r'"([^"]+)"', contra_match.group(1))
                        if items:
                            contraindications_list = items
                    
                    # Generate fields code
                    fields_code = []
                    for field_name in fields_to_add:
                        field_code = get_field_code(
                            field_name, 
                            is_topical=is_topical,
                            is_nasal=is_nasal,
                            is_oral=is_oral,
                            is_iv=is_iv,
                            pregnancy=pregnancy,
                            contraindications_list=contraindications_list
                        )
                        if field_code:
                            fields_code.append(field_code)
                    
                    if fields_code:
                        # Insert fields
                        new_content = (
                            content[:insert_pos] +
                            ',\n' + '\n'.join(fields_code) + '\n' +
                            content[insert_pos:]
                        )
                        
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        return True, f"Da them {len(fields_code)} fields"
                    else:
                        return False, "Khong generate duoc fields"
            pos += 1
        
        return False, "Khong tim thay closing brace"
    except Exception as e:
        return False, f"Loi: {e}"

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
                    if f'"{drug_name}":' in content or f"'{drug_name}':" in content:
                        return filepath
            except:
                pass
    return None

def main():
    print("=" * 80)
    print("SCRIPT TU DONG THEM FIELDS - PHIEN BAN NHANH")
    print("=" * 80)
    print("\nScript nay se them cac fields template vao cac thuoc")
    print("LUU Y: Cac fields duoc them la TEMPLATE, can review va update thong tin chi tiet sau")
    
    # Test voi 1 thuoc
    base_path = os.path.join(os.path.dirname(__file__), 'drugs', 'drug_modules')
    drug_name = "Bromocriptine"  # Test
    fields_to_add = ['black_box_warnings', 'drug_interactions', 'pregnancy_lactation']
    
    filepath = find_drug_file(drug_name, base_path)
    if filepath:
        print(f"\nTim thay {drug_name} trong {filepath}")
        success, msg = add_fields_to_file(filepath, drug_name, fields_to_add)
        print(f"Ket qua: {msg}")
    else:
        print(f"\nKhong tim thay {drug_name}")

if __name__ == "__main__":
    main()

