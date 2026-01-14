#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto Supplement Pregnancy Categories
Bổ sung tự động pregnancy categories dựa trên kiến thức y khoa đáng tin cậy
"""

import json
import sys
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import shutil

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from drugs.drug_database import DRUG_DATABASE
except ImportError:
    sys.path.insert(0, str(Path(__file__).parent))
    from drug_database import DRUG_DATABASE


# FDA Pregnancy Categories dựa trên nhóm thuốc và kiến thức y khoa
PREGNANCY_CATEGORIES = {
    # ACE Inhibitors - Category D
    "Enalapril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi (oligohydramnios, thận suy, dị tật xương)",
    "Lisinopril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi (oligohydramnios, thận suy, dị tật xương)",
    "Benazepril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Captopril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Ramipril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Fosinopril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Quinapril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Perindopril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Trandolapril": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    
    # ARBs - Category D
    "Losartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi (oligohydramnios, thận suy, dị tật xương)",
    "Telmisartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Valsartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Irbesartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Candesartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Olmesartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    "Azilsartan": "D - Chống chỉ định trong thai kỳ do nguy cơ gây hại cho thai nhi",
    
    # Statins - Category X
    "Simvastatin": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    "Pravastatin": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    "Atorvastatin": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    "Rosuvastatin": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    "Lovastatin": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    "Fluvastatin": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    
    # Diabetes - Metformin - Category B
    "Metformin": "B - Không có bằng chứng về nguy cơ ở người. Có thể sử dụng trong thai kỳ cho đái tháo đường thai kỳ",
    
    # Insulin - Category B
    "Insulin": "B - Không có bằng chứng về nguy cơ ở người. An toàn trong thai kỳ",
    
    # SGLT2 Inhibitors - Category C
    "Empagliflozin": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Dapagliflozin": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Canagliflozin": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    
    # Sulfonylureas - Category C
    "Gliclazide": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Glipizide": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Glimepiride": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Glyburide": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    
    # TZDs - Category C
    "Pioglitazone": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Rosiglitazone": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    
    # GLP-1 Agonists - Category C
    "Liraglutide": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Semaglutide": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Dulaglutide": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Exenatide": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    
    # PPIs - Category B
    "Omeprazole": "B - Không có bằng chứng về nguy cơ ở người. Có thể sử dụng trong thai kỳ",
    "Esomeprazole": "B - Không có bằng chứng về nguy cơ ở người. Có thể sử dụng trong thai kỳ",
    "Lansoprazole": "B - Không có bằng chứng về nguy cơ ở người. Có thể sử dụng trong thai kỳ",
    "Pantoprazole": "B - Không có bằng chứng về nguy cơ ở người. Có thể sử dụng trong thai kỳ",
    "Rabeprazole": "B - Không có bằng chứng về nguy cơ ở người. Có thể sử dụng trong thai kỳ",
    
    # Antiemetics
    "Ondansetron": "B - Không có bằng chứng về nguy cơ ở người. Sử dụng phổ biến trong thai kỳ",
    "Domperidone": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    
    # GI Drugs
    "Bismuth subsalicylate": "C - Chứa salicylate, tránh trong thai kỳ",
    "Ranitidine": "B - Không có bằng chứng về nguy cơ ở người",
    "Sucralfate": "B - Không có bằng chứng về nguy cơ ở người",
    "Sulfasalazine": "B - Có thể sử dụng trong thai kỳ với bổ sung folic acid",
    
    # Opioids - Category C
    "Hydrocodone": "C - Nguy cơ không thể loại trừ. Tránh trong thai kỳ nếu có thể",
    "Codeine": "C - Nguy cơ không thể loại trừ. Tránh trong thai kỳ nếu có thể",
    "Morphine": "C - Nguy cơ không thể loại trừ. Tránh trong thai kỳ nếu có thể",
    "Oxycodone": "C - Nguy cơ không thể loại trừ. Tránh trong thai kỳ nếu có thể",
    
    # Triptans - Category C
    "Rizatriptan": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Sumatriptan": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Zolmitriptan": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    
    # Respiratory
    "Montelukast": "B - Không có bằng chứng về nguy cơ ở người",
    "Nedocromil": "B - Không có bằng chứng về nguy cơ ở người",
    "Formoterol": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Olodaterol": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Salmeterol": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Vilanterol": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Ipratropium": "B - Không có bằng chứng về nguy cơ ở người",
    "Umeclidinium": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Beclomethasone inhaled": "C - Corticosteroid, thận trọng trong thai kỳ",
    "Budesonide inhaled": "B - Corticosteroid, có thể sử dụng trong thai kỳ",
    "Ciclesonide": "C - Corticosteroid, thận trọng trong thai kỳ",
    "Fluticasone inhaled": "C - Corticosteroid, thận trọng trong thai kỳ",
    
    # Neurological
    "Carbamazepine": "D - Có bằng chứng về nguy cơ dị tật bẩm sinh",
    "Topiramate": "D - Có bằng chứng về nguy cơ dị tật bẩm sinh",
    "Fluoxetine": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Donepezil": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    "Memantine": "B - Không có bằng chứng về nguy cơ ở người",
    "Rivastigmine": "B - Không có bằng chứng về nguy cơ ở người",
    
    # Supplements
    "Calcium": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
    "Diphenhydramine": "B - Không có bằng chứng về nguy cơ ở người",
    
    # Anesthesia
    "Etomidate": "C - Nguy cơ không thể loại trừ",
    "Ketamine": "C - Nguy cơ không thể loại trừ",
    "Propofol": "B - Không có bằng chứng về nguy cơ ở người",
    "Cisatracurium": "C - Nguy cơ không thể loại trừ",
    "Rocuronium": "C - Nguy cơ không thể loại trừ",
    "Succinylcholine": "C - Nguy cơ không thể loại trừ",
    
    # Antibiotics
    "Amoxicillin-clavulanate": "B - Không có bằng chứng về nguy cơ ở người",
    "Ceftriaxone": "B - Không có bằng chứng về nguy cơ ở người",
    "Azithromycin": "B - Không có bằng chứng về nguy cơ ở người",
    "Clarithromycin": "C - Nguy cơ không thể loại trừ. Tránh trong thai kỳ nếu có thể",
    "Hydroxychloroquine": "C - Nguy cơ không thể loại trừ. Có thể sử dụng cho bệnh tự miễn",
    "Amoxicillin suspension": "B - Không có bằng chứng về nguy cơ ở người",
    
    # Endocrinology
    "Levothyroxine": "A - Không có nguy cơ trong các nghiên cứu có đối chứng. An toàn trong thai kỳ",
    "Methimazole": "D - Có bằng chứng về nguy cơ. Thận trọng trong thai kỳ",
    "Propylthiouracil": "D - Có bằng chứng về nguy cơ. Thận trọng trong thai kỳ",
    
    # Corticosteroids
    "Prednisone": "C - Nguy cơ không thể loại trừ. Có thể sử dụng khi cần thiết",
    "Betamethasone": "C - Nguy cơ không thể loại trừ. Có thể sử dụng khi cần thiết",
    "Dexamethasone": "C - Nguy cơ không thể loại trừ. Có thể sử dụng khi cần thiết",
    
    # Bone
    "Alendronate": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    
    # Oncology
    "Tamoxifen": "D - Có bằng chứng về nguy cơ. Chống chỉ định trong thai kỳ",
    "Anastrozole": "X - Chống chỉ định tuyệt đối trong thai kỳ",
    "Imatinib": "D - Có bằng chứng về nguy cơ. Chống chỉ định trong thai kỳ",
    "Erlotinib": "D - Có bằng chứng về nguy cơ. Chống chỉ định trong thai kỳ",
    
    # Emergency
    "Atropine": "C - Nguy cơ không thể loại trừ",
    "Lidocaine": "B - Không có bằng chứng về nguy cơ ở người",
    
    # IV Fluids
    "Sodium Chloride 0.9%": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định",
    "Ringer Lactate": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định",
    "Albumin (Human)": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định",
    "HES 130/0.4": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    
    # Supplements
    "Vitamin D3 (Cholecalciferol)": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
    "Allopurinol": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
    "Colchicine": "D - Có bằng chứng về nguy cơ. Tránh trong thai kỳ",
    "Febuxostat": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
    
    # Immunosuppressants
    "Cyclosporine": "C - Nguy cơ không thể loại trừ. Có thể sử dụng khi cần thiết",
    "Mycophenolate": "D - Có bằng chứng về nguy cơ dị tật bẩm sinh. Chống chỉ định trong thai kỳ",
    "Tacrolimus": "C - Nguy cơ không thể loại trừ. Có thể sử dụng khi cần thiết",
    "Leflunomide": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    "Methotrexate": "X - Chống chỉ định tuyệt đối trong thai kỳ do nguy cơ dị tật bẩm sinh",
    
    # Local Anesthetics
    "Bupivacaine": "C - Nguy cơ không thể loại trừ",
    "Levobupivacaine": "C - Nguy cơ không thể loại trừ",
    
    # Vaccines
    "VAT (Tetanus Vaccine)": "C - Nguy cơ không thể loại trừ. Khuyến nghị trong thai kỳ",
    "Verorab (Rabies Vaccine)": "C - Nguy cơ không thể loại trừ. Khuyến nghị khi có chỉ định",
    "Influenza Vaccine": "B - Không có bằng chứng về nguy cơ ở người. Khuyến nghị trong thai kỳ",
    "Hepatitis B Vaccine": "C - Nguy cơ không thể loại trừ. Khuyến nghị khi có chỉ định",
    "SAT (Tetanus Antitoxin)": "C - Nguy cơ không thể loại trừ",
    "SAR (Rabies Antiserum)": "C - Nguy cơ không thể loại trừ",
    "Snake Antivenom (Luc Tre)": "C - Nguy cơ không thể loại trừ. Sử dụng khi cần thiết",
    "Snake Antivenom (Ho Dat)": "C - Nguy cơ không thể loại trừ. Sử dụng khi cần thiết",
    
    # Toxicology
    "Acetylcysteine": "B - Không có bằng chứng về nguy cơ ở người",
    "Pralidoxime": "C - Nguy cơ không thể loại trừ",
    "Vitamin K1": "C - Nguy cơ không thể loại trừ. An toàn khi sử dụng đúng chỉ định",
    "Ethanol": "D - Có bằng chứng về nguy cơ. Chỉ sử dụng khi cần thiết (giải độc methanol)",
    "Thiamine (Vitamin B1)": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
    "Cyanocobalamin (Vitamin B12)": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
    "Vitamin C (Ascorbic Acid)": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
    "Zoledronic Acid": "D - Có bằng chứng về nguy cơ. Không khuyến nghị trong thai kỳ",
    "Pyridoxine (Vitamin B6)": "A - Không có nguy cơ trong các nghiên cứu có đối chứng",
}


def find_drug_module_file(drug_name: str) -> Optional[Path]:
    """Tìm file module chứa thuốc"""
    drug_data = DRUG_DATABASE.get(drug_name, {})
    if not isinstance(drug_data, dict):
        return None
    
    group = drug_data.get("group", "")
    
    # Map group to module directory
    modules_dir = Path(__file__).parent / "drug_modules"
    
    # Try to find in main module files first
    module_mapping = {
        "Cardiovascular": "cardiovascular",
        "Diabetes": "diabetes",
        "Gastrointestinal": "gastrointestinal",
        "Analgesics": "analgesics",
        "Respiratory": "respiratory",
        "Neurological": "neurological",
        "Hematology": "hematology",
        "Supportive": "supportive",
        "Antimicrobial": "antimicrobial",
        "Metabolic": "metabolic",
        "Endocrinology": "endocrinology",
        "Oncology": "oncology",
        "Emergency": "emergency",
        "Urology": "urology",
        "Dermatology": "dermatology",
        "Ophthalmology": "ophthalmology",
        "Obstetrics": "obstetrics_gynecology",
        "ENT": "ent_oral_nasal_combinations",
        "Miscellaneous": "miscellaneous",
        "Anesthesia": "anesthesia",
        "Vaccines": "vaccines",
        "Toxicology": "toxicology",
        "Allergy": "allergy",
        "Nutrition": "nutrition",
        "Rheumatology": "rheumatology",
        "Immunology": "immunology"
    }
    
    for key, module_name in module_mapping.items():
        if key.lower() in group.lower():
            # Try main file
            module_file = modules_dir / f"{module_name}.py"
            if module_file.exists():
                try:
                    with open(module_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                            return module_file
                except:
                    pass
            
            # Try subdirectory
            subdir = modules_dir / module_name
            if subdir.exists() and subdir.is_dir():
                module_file = subdir / f"{module_name}.py"
                if module_file.exists():
                    try:
                        with open(module_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                                return module_file
                    except:
                        pass
    
    # Search all files
    for py_file in modules_dir.rglob("*.py"):
        if py_file.name.startswith("__"):
            continue
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if f'"{drug_name}"' in content or f"'{drug_name}'" in content:
                    return py_file
        except:
            continue
    
    return None


def backup_file(file_path: Path) -> Path:
    """Tạo backup file"""
    backup_dir = file_path.parent / ".backups"
    backup_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = backup_dir / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    shutil.copy2(file_path, backup_file)
    return backup_file


def update_drug_in_file(file_path: Path, drug_name: str, field: str, value: str) -> bool:
    """Cập nhật field trong file module"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find drug entry
        # Pattern: "DrugName": { ... }
        pattern = rf'"{re.escape(drug_name)}"\s*:\s*\{{'
        match = re.search(pattern, content)
        
        if not match:
            return False
        
        start_pos = match.end()
        
        # Find the closing brace for this drug
        brace_count = 1
        pos = start_pos
        while pos < len(content) and brace_count > 0:
            if content[pos] == '{':
                brace_count += 1
            elif content[pos] == '}':
                brace_count -= 1
            pos += 1
        
        drug_section = content[start_pos:pos-1]
        
        # Check if field already exists
        field_pattern = rf'"{re.escape(field)}"\s*:'
        if re.search(field_pattern, drug_section):
            # Update existing field
            # Find the field and replace its value
            field_match = re.search(rf'"{re.escape(field)}"\s*:\s*([^,}}]+)', drug_section)
            if field_match:
                old_value = field_match.group(1).strip()
                new_section = drug_section.replace(
                    f'"{field}": {old_value}',
                    f'"{field}": {json.dumps(value, ensure_ascii=False)}'
                )
                content = content[:start_pos] + new_section + content[pos-1:]
            else:
                return False
        else:
            # Add new field (find a good place to insert - after a comma)
            # Insert after the first field or before the closing brace
            insert_pos = drug_section.find(',')
            if insert_pos == -1:
                insert_pos = 0
            else:
                insert_pos += 1
            
            new_field = f'\n    "{field}": {json.dumps(value, ensure_ascii=False)},'
            drug_section = drug_section[:insert_pos] + new_field + drug_section[insert_pos:]
            content = content[:start_pos] + drug_section + content[pos-1:]
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"Error updating {drug_name} in {file_path}: {e}")
        return False


def main():
    """Main function"""
    print("Đang bổ sung pregnancy categories...")
    
    # Load priority data
    priority_file = Path(__file__).parent / "manual_supplementation_priority.json"
    if not priority_file.exists():
        print("⚠️  Chưa có file priority. Chạy manual_supplementation_analyzer.py trước.")
        return
    
    with open(priority_file, 'r', encoding='utf-8') as f:
        priority_data = json.load(f)
    
    # Get drugs missing pregnancy
    p0_drugs = priority_data.get("priorities", {}).get("P0", {}).get("pregnancy", {}).get("drugs", [])
    
    updated_count = 0
    not_found_count = 0
    no_category_count = 0
    
    results = {
        "updated": [],
        "not_found_in_file": [],
        "no_category": []
    }
    
    for drug_info in p0_drugs:
        drug_name = drug_info["name"]
        
        # Check if we have category
        if drug_name not in PREGNANCY_CATEGORIES:
            print(f"⚠️  {drug_name}: Không có category trong database")
            results["no_category"].append(drug_name)
            no_category_count += 1
            continue
        
        category = PREGNANCY_CATEGORIES[drug_name]
        
        # Find module file
        module_file = find_drug_module_file(drug_name)
        if not module_file:
            print(f"⚠️  {drug_name}: Không tìm thấy file module")
            results["not_found_in_file"].append(drug_name)
            not_found_count += 1
            continue
        
        # Backup
        backup_path = backup_file(module_file)
        
        # Update
        success = update_drug_in_file(module_file, drug_name, "pregnancy", category)
        
        if success:
            print(f"✅ {drug_name}: Đã cập nhật pregnancy = {category[:50]}...")
            results["updated"].append({
                "drug": drug_name,
                "file": str(module_file),
                "backup": str(backup_file),
                "category": category
            })
            updated_count += 1
        else:
            print(f"❌ {drug_name}: Lỗi khi cập nhật")
    
    # Save results
    results_file = Path(__file__).parent / "pregnancy_supplement_results.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*60)
    print("TỔNG KẾT")
    print("="*60)
    print(f"Đã cập nhật: {updated_count} thuốc")
    print(f"Không tìm thấy file: {not_found_count} thuốc")
    print(f"Không có category: {no_category_count} thuốc")
    print(f"Tổng cộng: {len(p0_drugs)} thuốc")
    print("="*60)
    print(f"\nKết quả chi tiết: {results_file}")


if __name__ == "__main__":
    main()
