"""
Drug Index System - Hệ thống chỉ mục thuốc
Giúp tìm kiếm, sắp xếp và quản lý thuốc dễ dàng
"""

from typing import Dict, List, Tuple, Optional
from collections import defaultdict
import re

# Import all drug modules
from .drug_modules import (
    CARDIOVASCULAR_DRUGS,
    DIABETES_DRUGS,
    GASTROINTESTINAL_DRUGS,
    ANALGESICS_DRUGS,
    RESPIRATORY_DRUGS,
    NEUROLOGICAL_DRUGS,
    HEMATOLOGY_DRUGS,
    SUPPORTIVE_DRUGS,
    ANTIMICROBIAL_DRUGS,
    METABOLIC_DRUGS,
    ENDOCRINOLOGY_DRUGS,
    ONCOLOGY_DRUGS,
    EMERGENCY_DRUGS,
    UROLOGY_DRUGS,
    DERMATOLOGY_DRUGS,
    OPHTHALMOLOGY_DRUGS,
    OBSTETRICS_GYNECOLOGY_DRUGS,
    ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    MISCELLANEOUS_DRUGS,
)

# Module metadata - Thông tin về mỗi module để dễ tìm kiếm và quản lý
MODULE_METADATA = {
    "Cardiovascular": {
        "code": "CV",
        "description": "Thuốc tim mạch: huyết áp, rối loạn nhịp, suy tim, lipid máu",
        "keywords": ["tim", "mach", "huyet ap", "nhip tim", "cholesterol", "statin"],
        "subcategories": ["ACE inhibitors", "ARBs", "Beta-blockers", "Calcium blockers", 
                         "Diuretics", "Antiarrhythmics", "Anticoagulants", "Statins"],
        "file_path": "drugs/drug_modules/cardiovascular/",
        "priority": 1  # Độ ưu tiên khi tìm kiếm
    },
    "Diabetes": {
        "code": "DM",
        "description": "Thuốc đái tháo đường: insulin, metformin, GLP-1, SGLT2",
        "keywords": ["dai thao duong", "insulin", "metformin", "duong huyet"],
        "subcategories": ["Insulins", "Biguanides", "Sulfonylureas", "GLP-1 agonists", 
                         "SGLT2 inhibitors", "DPP-4 inhibitors"],
        "file_path": "drugs/drug_modules/diabetes/",
        "priority": 1
    },
    "Antimicrobial": {
        "code": "AM",
        "description": "Kháng sinh, kháng virus, kháng nấm, kháng lao",
        "keywords": ["khang sinh", "antibiotic", "virus", "nam", "lao"],
        "subcategories": ["Antibiotics", "Antivirals", "Antifungals", "Antituberculars"],
        "file_path": "drugs/drug_modules/antimicrobial/",
        "priority": 1
    },
    "Neurological": {
        "code": "NEURO",
        "description": "Thuốc thần kinh và tâm thần: động kinh, trầm cảm, lo âu, Parkinson",
        "keywords": ["than kinh", "tam than", "dong kinh", "tram cam", "parkinson"],
        "subcategories": ["Anticonvulsants", "Antidepressants", "Antipsychotics", 
                         "Benzodiazepines", "Parkinson's drugs"],
        "file_path": "drugs/drug_modules/neurological/",
        "priority": 1
    },
    "Gastrointestinal": {
        "code": "GI",
        "description": "Thuốc tiêu hóa: PPI, H2 blockers, nhuận tràng, chống nôn",
        "keywords": ["tieu hoa", "ppi", "loet da day", "tao bon", "non"],
        "subcategories": ["PPIs", "H2 blockers", "Laxatives", "Antiemetics", "IBD drugs"],
        "file_path": "drugs/drug_modules/gastrointestinal/",
        "priority": 2
    },
    "Analgesics": {
        "code": "ANAL",
        "description": "Thuốc giảm đau: NSAIDs, opioid, paracetamol",
        "keywords": ["giam dau", "dau", "opioid", "nsaid", "paracetamol"],
        "subcategories": ["NSAIDs", "Opioids", "Paracetamol", "Migraine drugs"],
        "file_path": "drugs/drug_modules/analgesics/",
        "priority": 2
    },
    "Respiratory": {
        "code": "RESP",
        "description": "Thuốc hô hấp: hen, COPD, ho",
        "keywords": ["ho hap", "hen", "copd", "ho", "kho tho"],
        "subcategories": ["Bronchodilators", "Corticosteroids", "Antitussives"],
        "file_path": "drugs/drug_modules/respiratory/",
        "priority": 2
    },
    "Oncology": {
        "code": "ONC",
        "description": "Thuốc ung thư: hóa trị, điều trị đích, miễn dịch",
        "keywords": ["ung thu", "hoa tri", "chemotherapy", "targeted therapy"],
        "subcategories": ["Chemotherapy", "Targeted therapy", "Immunotherapy", "Hormone therapy"],
        "file_path": "drugs/drug_modules/oncology/",
        "priority": 2
    },
    "Emergency": {
        "code": "EMER",
        "description": "Thuốc cấp cứu: epinephrine, atropine, naloxone",
        "keywords": ["cap cuu", "emergency", "epinephrine", "atropine"],
        "subcategories": ["Catecholamines", "Antidotes", "Electrolytes"],
        "file_path": "drugs/drug_modules/emergency/",
        "priority": 3
    },
    "Hematology": {
        "code": "HEM",
        "description": "Thuốc huyết học: chống đông, chống kết tập tiểu cầu",
        "keywords": ["huyet hoc", "chong dong", "warfarin", "heparin"],
        "subcategories": ["Anticoagulants", "Antiplatelets", "Thrombolytics"],
        "file_path": "drugs/drug_modules/hematology.py",
        "priority": 2
    },
    "Endocrinology": {
        "code": "ENDO",
        "description": "Thuốc nội tiết: corticosteroid, hormone, loãng xương",
        "keywords": ["noi tiet", "corticosteroid", "hormone", "loang xuong"],
        "subcategories": ["Corticosteroids", "Sex hormones", "Osteoporosis"],
        "file_path": "drugs/drug_modules/endocrinology/",
        "priority": 2
    },
    "Metabolic": {
        "code": "MET",
        "description": "Thuốc chuyển hóa: tuyến giáp, rối loạn chuyển hóa",
        "keywords": ["chuyen hoa", "tuyen giap", "thyroid"],
        "subcategories": ["Thyroid hormones", "Antithyroid"],
        "file_path": "drugs/drug_modules/metabolic/",
        "priority": 3
    },
    "Supportive": {
        "code": "SUP",
        "description": "Thuốc hỗ trợ: vitamin, khoáng chất, dịch truyền",
        "keywords": ["ho tro", "vitamin", "khoang chat", "truyen"],
        "subcategories": ["Vitamins", "Minerals", "IV fluids"],
        "file_path": "drugs/drug_modules/supportive/",
        "priority": 3
    },
    "Urology": {
        "code": "URO",
        "description": "Thuốc tiết niệu: BPH, rối loạn tiểu tiện",
        "keywords": ["tiet nieu", "bph", "tieu tien"],
        "subcategories": ["BPH drugs", "Urinary antispasmodics"],
        "file_path": "drugs/drug_modules/urology.py",
        "priority": 3
    },
    "Dermatology": {
        "code": "DERM",
        "description": "Thuốc da liễu: kem, thuốc bôi, điều trị da",
        "keywords": ["da lieu", "kem", "thuoc boi", "da"],
        "subcategories": ["Topicals", "Systemic dermatology"],
        "file_path": "drugs/drug_modules/dermatology.py",
        "priority": 3
    },
    "Ophthalmology": {
        "code": "OPH",
        "description": "Thuốc mắt: nhỏ mắt, điều trị bệnh mắt",
        "keywords": ["mat", "nho mat", "benh mat"],
        "subcategories": ["Eye drops", "Ocular treatments"],
        "file_path": "drugs/drug_modules/ophthalmology.py",
        "priority": 3
    },
    "Obstetrics/Gynecology": {
        "code": "OBGYN",
        "description": "Thuốc sản phụ khoa: thai kỳ, sinh sản",
        "keywords": ["san phu khoa", "thai ky", "sinh san"],
        "subcategories": ["Pregnancy drugs", "Contraceptives", "Hormone therapy"],
        "file_path": "drugs/drug_modules/obstetrics_gynecology.py",
        "priority": 3
    },
    "ENT/Oral/Nasal": {
        "code": "ENT",
        "description": "Thuốc tai mũi họng, miệng, mũi",
        "keywords": ["tai mui hong", "mieng", "mui"],
        "subcategories": ["ENT combinations"],
        "file_path": "drugs/drug_modules/ent_oral_nasal_combinations.py",
        "priority": 3
    },
    "Miscellaneous": {
        "code": "MISC",
        "description": "Thuốc khác: không phân loại rõ",
        "keywords": ["khac", "miscellaneous"],
        "subcategories": ["Various"],
        "file_path": "drugs/drug_modules/miscellaneous/",
        "priority": 4
    },
}

# Map module names to drug dictionaries
DRUG_MODULES = {
    "Cardiovascular": CARDIOVASCULAR_DRUGS,
    "Diabetes": DIABETES_DRUGS,
    "Gastrointestinal": GASTROINTESTINAL_DRUGS,
    "Analgesics": ANALGESICS_DRUGS,
    "Respiratory": RESPIRATORY_DRUGS,
    "Neurological": NEUROLOGICAL_DRUGS,
    "Hematology": HEMATOLOGY_DRUGS,
    "Supportive": SUPPORTIVE_DRUGS,
    "Antimicrobial": ANTIMICROBIAL_DRUGS,
    "Metabolic": METABOLIC_DRUGS,
    "Endocrinology": ENDOCRINOLOGY_DRUGS,
    "Oncology": ONCOLOGY_DRUGS,
    "Emergency": EMERGENCY_DRUGS,
    "Urology": UROLOGY_DRUGS,
    "Dermatology": DERMATOLOGY_DRUGS,
    "Ophthalmology": OPHTHALMOLOGY_DRUGS,
    "Obstetrics/Gynecology": OBSTETRICS_GYNECOLOGY_DRUGS,
    "ENT/Oral/Nasal": ENT_ORAL_NASAL_COMBINATIONS_DRUGS,
    "Miscellaneous": MISCELLANEOUS_DRUGS,
}

# Build search index
_search_index = None

def _build_search_index():
    """Xây dựng chỉ mục tìm kiếm"""
    global _search_index
    if _search_index is not None:
        return _search_index
    
    index = {
        "by_name": {},  # drug_name -> [(module, drug_data)]
        "by_keyword": defaultdict(list),  # keyword -> [(module, drug_name, drug_data)]
        "by_group": defaultdict(list),  # group -> [(module, drug_name, drug_data)]
        "by_indication": defaultdict(list),  # indication -> [(module, drug_name, drug_data)]
    }
    
    for module_name, drugs in DRUG_MODULES.items():
        for drug_name, drug_data in drugs.items():
            # Index by name
            drug_name_lower = drug_name.lower()
            if drug_name_lower not in index["by_name"]:
                index["by_name"][drug_name_lower] = []
            index["by_name"][drug_name_lower].append((module_name, drug_data))
            
            # Index by group
            group = drug_data.get("group", "")
            if group:
                index["by_group"][group.lower()].append((module_name, drug_name, drug_data))
            
            # Index by indications
            indications = drug_data.get("indications", [])
            for indication in indications:
                index["by_indication"][indication.lower()].append((module_name, drug_name, drug_data))
            
            # Index by Vietnamese name
            vn_name = drug_data.get("vietnamese_name", "")
            if vn_name:
                for word in vn_name.lower().split():
                    index["by_keyword"][word].append((module_name, drug_name, drug_data))
    
    _search_index = index
    return index

def search_drugs(query: str, 
                 module: Optional[str] = None,
                 search_by: str = "name") -> List[Tuple[str, str, Dict]]:
    """
    Tìm kiếm thuốc
    
    Args:
        query: Từ khóa tìm kiếm
        module: Giới hạn trong module cụ thể (tùy chọn)
        search_by: Cách tìm kiếm - "name", "keyword", "group", "indication", "all"
    
    Returns:
        List of (drug_name, module_name, drug_data)
    """
    index = _build_search_index()
    query_lower = query.lower()
    results = []
    seen = set()
    
    modules_to_search = {module: DRUG_MODULES[module]} if module and module in DRUG_MODULES else DRUG_MODULES
    
    if search_by in ["name", "all"]:
        # Tìm theo tên thuốc
        for drug_name_lower, matches in index["by_name"].items():
            if query_lower in drug_name_lower:
                for mod_name, drug_data in matches:
                    if mod_name in modules_to_search:
                        key = (drug_name_lower, mod_name)
                        if key not in seen:
                            seen.add(key)
                            # Get original drug name
                            for orig_name in DRUG_MODULES[mod_name].keys():
                                if orig_name.lower() == drug_name_lower:
                                    results.append((orig_name, mod_name, drug_data))
                                    break
    
    if search_by in ["keyword", "all"]:
        # Tìm theo từ khóa
        for keyword, matches in index["by_keyword"].items():
            if query_lower in keyword:
                for mod_name, drug_name, drug_data in matches:
                    if mod_name in modules_to_search:
                        key = (drug_name.lower(), mod_name)
                        if key not in seen:
                            seen.add(key)
                            results.append((drug_name, mod_name, drug_data))
    
    if search_by in ["group", "all"]:
        # Tìm theo nhóm
        for group, matches in index["by_group"].items():
            if query_lower in group:
                for mod_name, drug_name, drug_data in matches:
                    if mod_name in modules_to_search:
                        key = (drug_name.lower(), mod_name)
                        if key not in seen:
                            seen.add(key)
                            results.append((drug_name, mod_name, drug_data))
    
    if search_by in ["indication", "all"]:
        # Tìm theo chỉ định
        for indication, matches in index["by_indication"].items():
            if query_lower in indication:
                for mod_name, drug_name, drug_data in matches:
                    if mod_name in modules_to_search:
                        key = (drug_name.lower(), mod_name)
                        if key not in seen:
                            seen.add(key)
                            results.append((drug_name, mod_name, drug_data))
    
    # Sort by module priority
    results.sort(key=lambda x: MODULE_METADATA.get(x[1], {}).get("priority", 99))
    
    return results

def find_drug_location(drug_name: str) -> List[Tuple[str, str]]:
    """
    Tìm vị trí file chứa thuốc
    
    Returns:
        List of (module_name, file_path)
    """
    locations = []
    drug_name_lower = drug_name.lower()
    
    for module_name, drugs in DRUG_MODULES.items():
        if drug_name_lower in [name.lower() for name in drugs.keys()]:
            metadata = MODULE_METADATA.get(module_name, {})
            file_path = metadata.get("file_path", f"drugs/drug_modules/{module_name.lower()}/")
            locations.append((module_name, file_path))
    
    return locations

def get_module_info(module_name: str) -> Dict:
    """Lấy thông tin về module"""
    return MODULE_METADATA.get(module_name, {})

def list_all_modules(sort_by: str = "name") -> List[Dict]:
    """
    Liệt kê tất cả modules với thông tin
    
    Args:
        sort_by: "name", "priority", "count"
    """
    modules = []
    for module_name in DRUG_MODULES.keys():
        metadata = MODULE_METADATA.get(module_name, {}).copy()
        metadata["name"] = module_name
        metadata["count"] = len(DRUG_MODULES[module_name])
        modules.append(metadata)
    
    if sort_by == "name":
        modules.sort(key=lambda x: x["name"])
    elif sort_by == "priority":
        modules.sort(key=lambda x: x.get("priority", 99))
    elif sort_by == "count":
        modules.sort(key=lambda x: x["count"], reverse=True)
    
    return modules

def get_drugs_by_module(module_name: str, sort_by: str = "name") -> Dict:
    """
    Lấy tất cả thuốc trong module, có thể sắp xếp
    
    Args:
        module_name: Tên module
        sort_by: "name", "group"
    """
    drugs = DRUG_MODULES.get(module_name, {})
    
    if sort_by == "name":
        return dict(sorted(drugs.items()))
    elif sort_by == "group":
        # Sort by group, then by name
        sorted_items = sorted(drugs.items(), 
                            key=lambda x: (x[1].get("group", ""), x[0]))
        return dict(sorted_items)
    
    return drugs

def suggest_module_for_drug(drug_name: str, drug_data: Dict) -> str:
    """
    Gợi ý module phù hợp cho thuốc mới
    
    Dựa trên group, indications, keywords
    """
    drug_lower = drug_name.lower()
    group = drug_data.get("group", "").lower()
    indications = [ind.lower() for ind in drug_data.get("indications", [])]
    
    scores = {}
    
    for module_name, metadata in MODULE_METADATA.items():
        score = 0
        keywords = [kw.lower() for kw in metadata.get("keywords", [])]
        
        # Check keywords
        for keyword in keywords:
            if keyword in drug_lower or any(keyword in ind for ind in indications):
                score += 2
        
        # Check group
        subcategories = [sub.lower() for sub in metadata.get("subcategories", [])]
        for subcat in subcategories:
            if subcat in group:
                score += 3
        
        if score > 0:
            scores[module_name] = score
    
    if scores:
        return max(scores.items(), key=lambda x: x[1])[0]
    
    return "Miscellaneous"

