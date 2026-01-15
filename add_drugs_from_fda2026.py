#!/usr/bin/env python3
"""
Script to add drugs from FDA2026.csv to appropriate module files
Skips all drugs from 2021
"""

import csv
import json
import os
import re
from datetime import datetime
from pathlib import Path

BASE_DIR = Path("drugs/drug_modules")
CSV_FILE = "FDA2026.csv"

def read_module_file(module_path):
    """Đọc nội dung file module"""
    full_path = BASE_DIR / module_path
    if not full_path.exists():
        print(f"⚠️  File không tồn tại: {full_path}")
        return None
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def find_insertion_point(content, drug_dict_name):
    """Tìm vị trí để chèn thuốc mới vào dictionary"""
    # Tìm pattern: "DrugName": { ... },
    pattern = rf'"{drug_dict_name}":\s*\{{'
    if re.search(pattern, content):
        print(f"⚠️  Thuốc {drug_dict_name} đã tồn tại trong file")
        return None
    
    # Tìm vị trí cuối cùng của dictionary (trước dấu })
    matches = list(re.finditer(r'    \},\s*\n', content))
    if matches:
        # Lấy vị trí sau dấu }, của entry cuối cùng
        last_match = matches[-1]
        return last_match.end()
    
    # Nếu không tìm thấy, tìm dấu } cuối cùng của dictionary
    match = re.search(r'(\}\s*\n\s*__all__)', content)
    if match:
        return match.start()
    
    return None

def format_drug_entry(drug_entry):
    """Format drug entry thành string Python dictionary"""
    indent = "        "
    
    def format_value(value, level=0):
        if isinstance(value, dict):
            lines = ["{"]
            for k, v in value.items():
                key_str = f'"{k}"' if isinstance(k, str) else str(k)
                val_str = format_value(v, level + 1)
                lines.append(f'{indent * (level + 1)}{key_str}: {val_str},')
            lines.append(f'{indent * level}}}')
            return "\n".join(lines)
        elif isinstance(value, list):
            if not value:
                return "[]"
            lines = ["["]
            for item in value:
                item_str = format_value(item, level + 1)
                lines.append(f'{indent * (level + 1)}{item_str},')
            lines.append(f'{indent * level}]')
            return "\n".join(lines)
        elif isinstance(value, str):
            # Escape quotes và newlines
            escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
            return f'"{escaped}"'
        elif isinstance(value, bool):
            return "True" if value else "False"
        elif value is None:
            return "None"
        else:
            return str(value)
    
    # Format toàn bộ entry
    drug_name = drug_entry["drug_info"]["drug_name"]
    # Tạo key cho dictionary (loại bỏ spaces và special chars)
    dict_key = drug_name.replace(" ", "").replace("-", "").replace(".", "").replace("/", "")
    
    formatted = f'    "{dict_key}": {format_value(drug_entry["entry"], 1)},\n'
    return formatted

def check_drug_exists(module_path, drug_name, active_ingredient):
    """Kiểm tra xem thuốc đã tồn tại trong module chưa"""
    content = read_module_file(module_path)
    if content is None:
        return False
    
    # Tạo dict key từ drug name
    dict_key = drug_name.replace(" ", "").replace("-", "").replace(".", "").replace("/", "")
    
    # Kiểm tra bằng dict key
    if f'"{dict_key}"' in content:
        return True
    
    # Kiểm tra bằng brand name
    if f'"{drug_name}"' in content:
        return True
    
    # Kiểm tra bằng active ingredient (lấy phần đầu)
    base_ingredient = active_ingredient.split()[0].split("-")[0].lower()
    if base_ingredient in content.lower():
        # Kiểm tra kỹ hơn - có thể là false positive
        pattern = rf'\b{re.escape(base_ingredient)}\b'
        if re.search(pattern, content, re.IGNORECASE):
            return True
    
    return False

def map_category_to_module(category, indication, active_ingredient, brand_name):
    """Map Vietnamese category to module path based on category, indication, and active ingredient"""
    category_lower = category.lower()
    indication_lower = indication.lower()
    active_lower = active_ingredient.lower()
    brand_lower = brand_name.lower()
    
    # Oncology drugs
    if category_lower == "ung bướu" or any(word in indication_lower for word in ["cancer", "carcinoma", "leukemia", "lymphoma", "myeloma", "tumor", "oncology", "glioma", "astrocytoma"]):
        if "vedotin" in active_lower or "tesirine" in active_lower or "adc" in active_lower or "deruxtecan" in active_lower:
            return "oncology/monoclonal_antibodies_adcs.py"
        elif "inib" in active_lower or "inhibitor" in active_lower:
            return "oncology/targeted_therapy_tkis.py"
        elif "mab" in active_lower or "-" in active_lower:
            # Check if it's a monoclonal antibody
            if any(x in active_lower for x in ["mab", "monoclonal", "antibody"]):
                return "oncology/monoclonal_antibodies_adcs.py"
            else:
                return "oncology/basic_oncology.py"
        elif "imaging" in indication_lower or "identify" in indication_lower or "detect" in indication_lower:
            return "miscellaneous/biological/other_biological.py"
        else:
            return "oncology/basic_oncology.py"
    
    # Neurological/Psychiatry
    if category_lower == "thần kinh/tâm thần":
        if "migraine" in indication_lower:
            return "neurological/migraine_cgrp_drugs.py"
        elif "alzheimer" in indication_lower or "dementia" in indication_lower:
            return "neurological/alzheimer_dementia_drugs.py"
        elif "multiple sclerosis" in indication_lower or " ms " in indication_lower:
            return "neurological/multiple_sclerosis_drugs.py"
        elif "adhd" in indication_lower or "attention deficit" in indication_lower:
            return "psychiatry_other/adhd_anxiolytics.py"
        elif "insomnia" in indication_lower or "sleep" in indication_lower:
            return "neurological/sleep_medications.py"
        elif "schizophrenia" in indication_lower or "bipolar" in indication_lower:
            return "psychiatry/antipsychotics.py"
        elif "depression" in indication_lower or "depressive" in indication_lower:
            return "psychiatry/mood_stabilizers.py"
        elif "seizure" in indication_lower or "epilepsy" in indication_lower:
            return "neurological/anticonvulsants.py"
        else:
            return "neurological/anticonvulsants.py"
    
    # Cardiovascular
    if category_lower == "tim mạch":
        if "pcsk9" in active_lower or "inclisiran" in active_lower or "pcsk" in active_lower:
            return "cardiovascular/pcsk9_inhibitors.py"
        elif "cholesterol" in indication_lower or "hypercholesterolemia" in indication_lower or "ldl" in indication_lower:
            return "cardiovascular/pcsk9_inhibitors.py"
        elif "heart failure" in indication_lower or "cardiomyopathy" in indication_lower:
            return "cardiovascular/other_cv.py"
        elif "hypertension" in indication_lower or "blood pressure" in indication_lower:
            return "cardiovascular/other_cv.py"
        elif "glaucoma" in indication_lower or "intraocular pressure" in indication_lower:
            return "ophthalmology/anti_glaucoma.py"
        elif "ischemia" in indication_lower or "infarction" in indication_lower or "myocardial" in indication_lower:
            return "miscellaneous/biological/other_biological.py"  # Diagnostic
        else:
            return "cardiovascular/other_cv.py"
    
    # Hematology
    if category_lower == "huyết học":
        if "hemophilia" in indication_lower:
            return "hematology/other_hematology.py"
        elif "anemia" in indication_lower:
            return "hematology/anemia.py"
        elif "neutropenia" in indication_lower or "neutrophil" in indication_lower:
            return "hematology/growth_factors.py"
        elif "thrombocytopenia" in indication_lower or "platelet" in indication_lower:
            return "hematology/other_hematology.py"
        elif "myelofibrosis" in indication_lower or "polycythemia" in indication_lower:
            return "hematology/other_hematology.py"
        else:
            return "hematology/other_hematology.py"
    
    # Infectious disease
    if category_lower == "truyền nhiễm/kháng sinh":
        if "hiv" in indication_lower:
            if "integrase" in active_lower or "cabotegravir" in active_lower or "lenacapavir" in active_lower or "bictegravir" in active_lower or "dolutegravir" in active_lower or "raltegravir" in active_lower:
                return "antimicrobial/antivirals/hiv_arvs/integrase_inhibitors.py"
            else:
                return "antimicrobial/antivirals/hiv_arvs.py"
        elif "cmv" in indication_lower or "cytomegalovirus" in indication_lower:
            return "antimicrobial/antivirals/cmv.py"
        elif "candidiasis" in indication_lower or "candida" in indication_lower:
            return "antimicrobial/antifungals/azoles.py"
        elif "pneumonia" in indication_lower or "uti" in indication_lower or "urinary tract" in indication_lower:
            return "antimicrobial/antibiotics/beta_lactams.py"
        elif "gonorrhea" in indication_lower:
            return "antimicrobial/antibiotics/beta_lactams.py"
        elif "helicobacter" in indication_lower or "h. pylori" in indication_lower:
            return "gastrointestinal/proton_pump_inhibitors.py"
        elif "covid" in indication_lower:
            return "antimicrobial/antivirals/influenza.py"
        elif "rsv" in indication_lower or "respiratory syncytial" in indication_lower:
            return "antimicrobial/antivirals/influenza.py"
        else:
            return "antimicrobial/antibiotics/others.py"
    
    # Diabetes/Endocrinology
    if category_lower == "nội tiết/đtđ":
        if "diabetes" in indication_lower or "diabetic" in indication_lower or "glycemic" in indication_lower or "blood sugar" in indication_lower:
            if "gliflozin" in active_lower or "sglt2" in active_lower:
                return "diabetes/sglt2_inhibitors.py"
            elif "glp" in active_lower or "tirzepatide" in active_lower or "semaglutide" in active_lower:
                return "diabetes/glp1_agonists.py"
            else:
                return "diabetes/other_antidiabetics.py"
        elif "growth hormone" in indication_lower or "short stature" in indication_lower:
            return "endocrinology_other/growth_hormone.py"
        elif "acromegaly" in indication_lower:
            return "endocrinology_other/growth_hormone.py"
        else:
            return "diabetes/other_antidiabetics.py"
    
    # Urology/Kidney
    if category_lower == "thận - tiết niệu":
        if "nephropathy" in indication_lower or "proteinuria" in indication_lower:
            return "miscellaneous/immunosuppressants.py"
        elif "anemia" in indication_lower and "kidney" in indication_lower:
            return "hematology/anemia.py"
        elif "hyperoxaluria" in indication_lower or "oxalate" in indication_lower:
            return "miscellaneous/immunosuppressants.py"
        elif "hepatorenal" in indication_lower:
            return "miscellaneous/immunosuppressants.py"
        else:
            return "miscellaneous/immunosuppressants.py"
    
    # Respiratory
    if category_lower == "hô hấp":
        if "asthma" in indication_lower:
            if "mab" in active_lower or "-" in active_lower:
                return "respiratory/respiratory_biologics.py"
            else:
                return "respiratory/respiratory_biologics.py"
        elif "copd" in indication_lower or "pulmonary" in indication_lower or "bronchiectasis" in indication_lower:
            return "respiratory/respiratory_biologics.py"
        elif "rsv" in indication_lower or "respiratory syncytial" in indication_lower:
            return "antimicrobial/antivirals/influenza.py"
        elif "pulmonary function" in indication_lower or "imaging" in indication_lower:
            return "miscellaneous/biological/other_biological.py"
        else:
            return "respiratory/respiratory_biologics.py"
    
    # Dermatology
    if category_lower == "da liễu":
        if "psoriasis" in indication_lower:
            if "mab" in active_lower or "-" in active_lower:
                return "miscellaneous/biological/monoclonal_antibodies.py"
            else:
                return "dermatology/other_topical.py"
        elif "atopic dermatitis" in indication_lower or "dermatitis" in indication_lower:
            if "mab" in active_lower or "-" in active_lower:
                return "miscellaneous/biological/monoclonal_antibodies.py"
            else:
                return "dermatology/other_topical.py"
        elif "eczema" in indication_lower:
            return "dermatology/other_topical.py"
        elif "urticaria" in indication_lower:
            return "dermatology/other_topical.py"
        else:
            return "dermatology/other_topical.py"
    
    # Ophthalmology
    if category_lower == "mắt":
        if "glaucoma" in indication_lower or "intraocular pressure" in indication_lower:
            return "ophthalmology/anti_glaucoma.py"
        elif "macular" in indication_lower or "retina" in indication_lower:
            return "ophthalmology/anti_inflammatory.py"
        elif "dry eye" in indication_lower:
            return "ophthalmology/lubricants.py"
        else:
            return "ophthalmology/anti_inflammatory.py"
    
    # Obstetrics/Gynecology
    if category_lower == "sản phụ khoa":
        if "pregnancy" in indication_lower or "contraception" in indication_lower or "contraceptive" in indication_lower:
            return "obstetrics_gynecology/contraceptives.py"
        elif "menopause" in indication_lower or "hot flash" in indication_lower or "vasomotor" in indication_lower:
            return "obstetrics_gynecology/hormone_replacement.py"
        else:
            return "obstetrics_gynecology/hormone_replacement.py"
    
    # Gastrointestinal
    if category_lower == "tiêu hóa - gan mật":
        if "colitis" in indication_lower or "crohn" in indication_lower or "ibd" in indication_lower:
            if "mab" in active_lower or "-" in active_lower:
                return "miscellaneous/biological/monoclonal_antibodies.py"
            else:
                return "gastrointestinal/jak_inhibitors.py"
        elif "hepatitis" in indication_lower or "liver" in indication_lower or "steatohepatitis" in indication_lower:
            return "gastrointestinal/other_gi_drugs.py"
        elif "pylori" in indication_lower or "helicobacter" in indication_lower:
            return "gastrointestinal/proton_pump_inhibitors.py"
        else:
            return "gastrointestinal/other_gi_drugs.py"
    
    # Diagnostic imaging
    if category_lower == "chẩn đoán hình ảnh":
        return "miscellaneous/biological/other_biological.py"
    
    # "Khác" category - need to analyze indication
    if category_lower == "khác":
        # Check indication for clues
        if "migraine" in indication_lower:
            return "neurological/migraine_cgrp_drugs.py"
        elif "alzheimer" in indication_lower or "dementia" in indication_lower:
            return "neurological/alzheimer_dementia_drugs.py"
        elif "multiple sclerosis" in indication_lower:
            return "neurological/multiple_sclerosis_drugs.py"
        elif "myasthenia gravis" in indication_lower:
            return "miscellaneous/biological/monoclonal_antibodies.py"
        elif "lupus" in indication_lower:
            return "miscellaneous/biological/monoclonal_antibodies.py"
        elif "psoriasis" in indication_lower or "dermatitis" in indication_lower:
            return "miscellaneous/biological/monoclonal_antibodies.py"
        elif "asthma" in indication_lower:
            return "respiratory/respiratory_biologics.py"
        elif "growth hormone" in indication_lower or "short stature" in indication_lower or "achondroplasia" in indication_lower:
            return "endocrinology_other/growth_hormone.py"
        elif "hypoglycemia" in indication_lower:
            return "emergency/hypoglycemia.py"
        elif "deficiency" in indication_lower or "dystrophy" in indication_lower or "syndrome" in indication_lower:
            return "miscellaneous/biological/other_biological.py"
        elif "imaging" in indication_lower or "detect" in indication_lower or "identify" in indication_lower:
            return "miscellaneous/biological/other_biological.py"
        elif "pain" in indication_lower:
            return "analgesics/opioid_agonist_weaks.py"
        elif "depression" in indication_lower or "depressive" in indication_lower:
            return "psychiatry/mood_stabilizers.py"
        elif "schizophrenia" in indication_lower:
            return "psychiatry/antipsychotics.py"
        elif "mab" in active_lower or "-" in active_lower:
            return "miscellaneous/biological/monoclonal_antibodies.py"
        else:
            return "miscellaneous/biological/other_biological.py"
    
    # Default
    return "miscellaneous/biological/other_biological.py"

def create_drug_entry(row):
    """Tạo cấu trúc dữ liệu đầy đủ cho một thuốc từ CSV row"""
    year = row[0]
    active_ingredient = row[1]
    brand_name = row[2]
    category = row[3]
    mechanism = row[4] if len(row) > 4 else ""
    indication = row[5] if len(row) > 5 else ""
    
    # Extract base name from active ingredient
    base_name = active_ingredient.split()[0].split("-")[0].split(",")[0].capitalize()
    
    # Determine administration route (default to PO, will be adjusted based on drug type)
    administration = ["PO"]
    if "ophthalmic" in active_ingredient.lower() or "eye" in indication.lower():
        administration = ["Ophthalmic"]
    elif "topical" in indication.lower() or "cream" in indication.lower():
        administration = ["Topical"]
    elif "inject" in indication.lower() or "iv" in indication.lower() or "subcutaneous" in indication.lower():
        administration = ["IV", "SC"]
    elif "inhale" in indication.lower() or "inhalation" in indication.lower():
        administration = ["Inhalation"]
    
    entry = {
        "group": f"FDA Approved {year}",
        "vietnamese_name": f"{base_name}, {brand_name}",
        "administration": administration,
        "indications": [indication] if indication else ["Theo chỉ định của bác sĩ"],
        "contraindications": [
            f"Dị ứng {base_name.lower()} hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_standard": "Theo chỉ định của bác sĩ",
            "notes": f"FDA phê duyệt {year}. {indication}"
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Cần bổ sung thông tin từ tài liệu FDA"
        ],
        "interactions": [
            "Cần bổ sung thông tin từ tài liệu FDA"
        ],
        "pregnancy": "C",
        "mechanism_of_action": f"{base_name} được FDA phê duyệt {year} để {indication.lower()}. {mechanism if mechanism else 'Cần bổ sung thông tin chi tiết về cơ chế tác dụng.'}",
        "monitoring": [
            "Theo dõi đáp ứng điều trị",
            "Theo dõi tác dụng phụ"
        ],
        "precautions": [
            f"Dị ứng {base_name.lower()}",
            "Cần bổ sung thông tin từ tài liệu FDA"
        ],
        "pharmacokinetics": {
            "half_life": "Cần bổ sung",
            "onset": "Cần bổ sung",
            "duration": "Cần bổ sung",
            "protein_binding": "Cần bổ sung",
            "metabolism": "Cần bổ sung",
            "clearance": "Cần bổ sung"
        },
        "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
        "black_box_warnings": "Cần kiểm tra tài liệu FDA",
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                f"Dị ứng {base_name.lower()} hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": []
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                "recommendation": "Thận trọng khi cho con bú"
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Cần bổ sung thông tin từ tài liệu FDA"
        },
        "overdose_management": {
            "symptoms": ["Cần bổ sung"],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": ["Điều trị hỗ trợ"],
            "monitoring": "Theo dõi dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Cần bổ sung",
                "timing": "Cần bổ sung"
            }
        },
        "references": {
            "primary_sources": [
                f"FDA Drug Label - {base_name} ({brand_name})",
                f"FDA Approval Date: {year}",
                f"FDA-approved use: {indication}"
            ],
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "evidence_level": f"A - FDA-approved {year}"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Clinical response", "Adverse effects"]
        },
        "guideline_tags": [
            f"FDA Drug Information - {base_name} ({brand_name})"
        ],
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    }
    
    return entry

def add_drug_to_module(module_path, drug_entry):
    """Thêm thuốc vào file module"""
    content = read_module_file(module_path)
    if content is None:
        return False
    
    drug_name = drug_entry["drug_info"]["drug_name"]
    dict_key = drug_name.replace(" ", "").replace("-", "").replace(".", "").replace("/", "")
    
    # Kiểm tra xem thuốc đã tồn tại chưa
    if f'"{dict_key}"' in content:
        print(f"  ⚠️  {drug_name} đã tồn tại trong {module_path}")
        return False
    
    # Tìm vị trí chèn
    insertion_point = find_insertion_point(content, dict_key)
    if insertion_point is None:
        print(f"  ❌ Không tìm thấy vị trí chèn cho {drug_name}")
        return False
    
    # Format entry
    formatted_entry = format_drug_entry(drug_entry)
    
    # Chèn vào vị trí
    new_content = content[:insertion_point] + formatted_entry + content[insertion_point:]
    
    # Ghi lại file
    full_path = BASE_DIR / module_path
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"  ✅ Đã thêm {drug_name} vào {module_path}")
    return True

def read_csv_and_process():
    """Đọc CSV và xử lý dữ liệu"""
    if not os.path.exists(CSV_FILE):
        print(f"❌ Không tìm thấy file {CSV_FILE}")
        return None
    
    drugs = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header
        
        for row in reader:
            if len(row) < 6:
                continue
            
            year = row[0]
            # Bỏ qua thuốc năm 2021
            if year == "2021":
                continue
            
            active_ingredient = row[1]
            brand_name = row[2]
            category = row[3]
            mechanism = row[4] if len(row) > 4 else ""
            indication = row[5] if len(row) > 5 else ""
            
            # Map category to module
            module_path = map_category_to_module(category, indication, active_ingredient, brand_name)
            
            # Tạo drug entry
            entry = create_drug_entry(row)
            
            drugs.append({
                "drug_info": {
                    "year": year,
                    "active_ingredient": active_ingredient,
                    "drug_name": brand_name,
                    "category": category,
                    "mechanism": mechanism,
                    "indication": indication
                },
                "module": module_path,
                "entry": entry
            })
    
    return drugs

def main():
    """Main function"""
    print("=" * 80)
    print("Script để thêm các thuốc mới từ FDA2026.csv vào module files")
    print("Bỏ qua tất cả thuốc năm 2021")
    print("=" * 80)
    
    # Đọc và xử lý CSV
    print("\n📖 Đang đọc CSV...")
    drugs = read_csv_and_process()
    
    if drugs is None:
        return
    
    print(f"\nTổng số thuốc cần xử lý (2022-2026): {len(drugs)}")
    
    # Kiểm tra thuốc đã tồn tại
    print("\n🔍 Đang kiểm tra thuốc đã tồn tại...")
    new_drugs = []
    existing_drugs = []
    
    for drug in drugs:
        drug_name = drug["drug_info"]["drug_name"]
        active_ingredient = drug["drug_info"]["active_ingredient"]
        module_path = drug["module"]
        
        if check_drug_exists(module_path, drug_name, active_ingredient):
            existing_drugs.append(drug)
            print(f"  ⚠️  {drug_name} đã tồn tại trong {module_path}")
        else:
            new_drugs.append(drug)
    
    print(f"\n📊 Thống kê:")
    print(f"  - Tổng số: {len(drugs)}")
    print(f"  - Đã tồn tại: {len(existing_drugs)}")
    print(f"  - Cần thêm: {len(new_drugs)}")
    
    # Nhóm theo module
    by_module = {}
    for drug in new_drugs:
        module = drug["module"]
        if module not in by_module:
            by_module[module] = []
        by_module[module].append(drug)
    
    print(f"\n📁 Số module cần cập nhật: {len(by_module)}")
    
    # Tạo file JSON trung gian
    output_data = {
        "summary": {
            "total": len(drugs),
            "existing": len(existing_drugs),
            "new": len(new_drugs),
            "modules_affected": len(by_module)
        },
        "new_drugs": new_drugs
    }
    
    output_file = "drugs_2022_2026_to_add.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Đã tạo file JSON: {output_file}")
    
    # Hỏi xem có muốn thêm vào modules không
    print("\n" + "=" * 80)
    print("Bạn có muốn thêm các thuốc này vào các file module không?")
    print("(Chạy script add_drugs_to_modules.py với file JSON này để thêm)")
    print("=" * 80)
    
    # Thêm vào modules
    print("\n➕ Đang thêm thuốc vào modules...")
    success_count = 0
    fail_count = 0
    
    for module, module_drugs in by_module.items():
        print(f"\n📁 Module: {module} ({len(module_drugs)} thuốc)")
        for drug in module_drugs:
            drug_name = drug["drug_info"]["drug_name"]
            print(f"  ➕ Đang thêm: {drug_name}...")
            if add_drug_to_module(module, drug):
                success_count += 1
            else:
                fail_count += 1
    
    print("\n" + "=" * 80)
    print(f"✅ Thành công: {success_count}")
    print(f"❌ Thất bại: {fail_count}")
    print("=" * 80)

if __name__ == "__main__":
    main()
