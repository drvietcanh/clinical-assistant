"""
Drug Interaction Database
Database of common drug interactions for Vietnamese healthcare
Based on clinical guidelines and Vietnamese drug availability
"""

from difflib import SequenceMatcher
from typing import Optional, List, Tuple, Dict

# Interaction severity levels
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

# Import expanded interactions
try:
    from .interactions_data_expanded import EXPANDED_INTERACTIONS
    _EXPANDED_LOADED = True
except ImportError:
    _EXPANDED_LOADED = False
    EXPANDED_INTERACTIONS = {}

# Import drug database for fuzzy matching
try:
    from .drug_database import DRUG_DATABASE
    from .drug_utils.groups import DRUG_GROUPS
    _DRUG_DB_LOADED = True
except ImportError:
    _DRUG_DB_LOADED = False
    DRUG_DATABASE = {}
    DRUG_GROUPS = {}

# Drug interaction database (original + expanded)
DRUG_INTERACTIONS = {
    # ========== ANTICOAGULANTS ==========
    ("Warfarin", "Aspirin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết do tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết nặng, có thể tử vong",
        "management": "Tránh dùng chung nếu có thể. Nếu cần thiết: theo dõi INR thường xuyên, cân nhắc giảm liều warfarin",
        "references": "AHFS Drug Information, Micromedex"
    },
    ("Warfarin", "Ibuprofen"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "NSAID làm tăng nguy cơ xuất huyết dạ dày và tăng tác dụng chống đông",
        "clinical_significance": "Nguy cơ xuất huyết dạ dày-ruột tăng 2-4 lần. Có thể gây xuất huyết nặng, đặc biệt ở người cao tuổi.",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế nếu cần giảm đau/sốt",
        "alternatives": {
            "for_ibuprofen": ["Paracetamol", "Acetaminophen"],
            "for_warfarin": ["Dabigatran", "Rivaroxaban", "Apixaban"]
        },
        "references": "Micromedex"
    },
    ("Warfarin", "Omeprazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng nồng độ warfarin",
        "description": "Omeprazole ức chế CYP2C19, có thể làm tăng tác dụng warfarin",
        "management": "Theo dõi INR thường xuyên khi bắt đầu/dừng omeprazole",
        "references": "Clinical Pharmacology"
    },
    
    # ========== ANTIBIOTICS ==========
    ("Warfarin", "Metronidazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế chuyển hóa warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "clinical_significance": "INR có thể tăng 2-3 lần. Nguy cơ xuất huyết nặng, đặc biệt trong 1-2 tuần đầu.",
        "management": "Giảm liều warfarin 30-50% khi dùng metronidazole. Theo dõi INR 2-3 lần/tuần",
        "alternatives": {
            "for_metronidazole": ["Clindamycin", "Vancomycin (nếu phù hợp)"],
            "for_warfarin": ["Dabigatran", "Rivaroxaban"]
        },
        "references": "AHFS Drug Information"
    },
    ("Warfarin", "Ciprofloxacin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên, cân nhắc giảm liều warfarin",
        "references": "Micromedex"
    },
    ("Warfarin", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ức chế chuyển hóa warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng erythromycin",
        "references": "Clinical Pharmacology"
    },
    
    # ========== ANTIDEPRESSANTS ==========
    ("Fluoxetine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluoxetine ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu/dừng fluoxetine. Cân nhắc giảm liều warfarin",
        "references": "Micromedex"
    },
    ("Sertraline", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    ("Fluoxetine", "Tramadol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ co giật, nhầm lẫn, hôn mê",
        "management": "Tránh dùng chung. Nếu cần thiết: dùng liều thấp, theo dõi sát",
        "references": "Micromedex"
    },
    
    # ========== ANTIHYPERTENSIVES ==========
    ("ACE Inhibitor", "Potassium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "ACE inhibitor + kali bổ sung có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu định kỳ",
        "references": "Micromedex"
    },
    ("ACE Inhibitor", "Spironolactone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu và suy thận",
        "description": "Có thể gây tăng kali máu nguy hiểm",
        "clinical_significance": "Kali máu có thể tăng >5.5 mEq/L, nguy cơ rối loạn nhịp tim, đặc biệt ở bệnh nhân suy thận.",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi kali máu và chức năng thận thường xuyên",
        "alternatives": {
            "for_spironolactone": ["Furosemide", "Hydrochlorothiazide"],
            "for_ace_inhibitor": ["ARB (Losartan, Valsartan)"]
        },
        "references": "AHFS Drug Information"
    },
    ("Digoxin", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone làm tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin (buồn nôn, rối loạn nhịp tim)",
        "management": "Giảm liều digoxin 50% khi bắt đầu amiodarone. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    # ========== ANTIDIABETICS ==========
    ("Metformin", "Contrast Media"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ nhiễm toan lactic",
        "description": "Metformin + thuốc cản quang có thể gây nhiễm toan lactic nguy hiểm",
        "management": "Ngừng metformin 48 giờ trước và sau khi tiêm thuốc cản quang. Kiểm tra creatinine",
        "references": "FDA, ACR Guidelines"
    },
    ("Sulfonylurea", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    # ========== STATINS ==========
    ("Atorvastatin", "Clarithromycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tiêu cơ vân",
        "description": "Clarithromycin ức chế chuyển hóa atorvastatin",
        "clinical_significance": "Nguy cơ tiêu cơ vân tăng 10-15 lần. Có thể gây suy thận cấp, tử vong.",
        "management": "Tránh dùng chung. Nếu cần: giảm liều atorvastatin 50-75%, theo dõi CK",
        "alternatives": {
            "for_clarithromycin": ["Azithromycin", "Doxycycline"],
            "for_atorvastatin": ["Pravastatin", "Rosuvastatin"]
        },
        "references": "FDA, Micromedex"
    },
    ("Simvastatin", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tiêu cơ vân",
        "description": "Tăng nguy cơ tiêu cơ vân, có thể tử vong",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA"
    },
    
    # ========== ANTIFUNGALS ==========
    ("Ketoconazole", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Giảm liều warfarin 30-50%. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    ("Fluconazole", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    # ========== PROTON PUMP INHIBITORS ==========
    ("Omeprazole", "Clopidogrel"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Giảm tác dụng chống kết tập tiểu cầu của clopidogrel",
        "description": "Có thể làm giảm hiệu quả phòng ngừa đột quỵ/nhồi máu cơ tim",
        "management": "Cân nhắc dùng PPI khác (pantoprazole, lansoprazole) hoặc H2 blocker",
        "references": "FDA"
    },
    
    # ========== ANTIHISTAMINES ==========
    ("Diphenhydramine", "Benzodiazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng an thần, ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp, theo dõi sát",
        "references": "Micromedex"
    },
    
    # ========== ANTIPLATELETS ==========
    ("Aspirin", "Clopidogrel"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "Dual antiplatelet therapy - tăng nguy cơ xuất huyết nhưng có chỉ định trong một số trường hợp",
        "management": "Chỉ dùng khi có chỉ định (sau stent, ACS). Theo dõi dấu hiệu xuất huyết",
        "references": "ACC/AHA Guidelines"
    },
    
    # ========== ORAL CONTRACEPTIVES ==========
    ("Oral Contraceptive", "Antibiotics"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Một số kháng sinh làm giảm hiệu quả tránh thai",
        "description": "Rifampin, một số kháng sinh phổ rộng có thể giảm hiệu quả",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung khi dùng kháng sinh",
        "references": "Clinical Pharmacology"
    },
    
    # ========== QUINOLONES ==========
    ("Ciprofloxacin", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Giảm hấp thu ciprofloxacin",
        "description": "Antacid (Ca, Mg, Al) giảm đáng kể hấp thu ciprofloxacin",
        "management": "Cách xa ít nhất 2 giờ. Tốt nhất: dùng antacid 2 giờ sau ciprofloxacin",
        "references": "Micromedex"
    },
    
    # ========== METHOTREXATE ==========
    ("Methotrexate", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính methotrexate",
        "description": "NSAID làm giảm đào thải methotrexate, tăng nguy cơ độc tính",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp NSAID, theo dõi công thức máu, chức năng gan thận",
        "references": "Micromedex"
    },
    ("Methotrexate", "Trimethoprim-Sulfamethoxazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng độc tính methotrexate",
        "description": "Tăng nguy cơ giảm bạch cầu, thiếu máu, nhiễm độc gan thận",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi công thức máu thường xuyên",
        "references": "AHFS Drug Information"
    },
}

# Merge with expanded interactions
if _EXPANDED_LOADED:
    DRUG_INTERACTIONS.update(EXPANDED_INTERACTIONS)

# Alternative drug names mapping (Vietnamese names, brand names, etc.)
DRUG_ALIASES = {
    "Aspirin": ["Aspirin", "Acetylsalicylic acid", "ASA", "Aspirin"],
    "Warfarin": ["Warfarin", "Coumadin", "Marevan"],
    "Ibuprofen": ["Ibuprofen", "Brufen", "Advil"],
    "Omeprazole": ["Omeprazole", "Losec", "Omez"],
    "Metronidazole": ["Metronidazole", "Flagyl", "Metronidazol"],
    "Ciprofloxacin": ["Ciprofloxacin", "Cipro", "Cifran"],
    "Fluoxetine": ["Fluoxetine", "Prozac", "Fluoxetin"],
    "Tramadol": ["Tramadol", "Tramal", "Tramadon"],
    "Digoxin": ["Digoxin", "Lanoxin", "Digoxine"],
    "Amiodarone": ["Amiodarone", "Cordarone", "Amiodaron"],
    "Metformin": ["Metformin", "Glucophage", "Metformin HCl"],
    "Atorvastatin": ["Atorvastatin", "Lipitor", "Atorvastatin"],
    "Simvastatin": ["Simvastatin", "Zocor", "Simvastatin"],
    "Clarithromycin": ["Clarithromycin", "Klacid", "Clarithromycin"],
    "Ketoconazole": ["Ketoconazole", "Nizoral", "Ketoconazol"],
    "Fluconazole": ["Fluconazole", "Diflucan", "Fluconazol"],
    "Clopidogrel": ["Clopidogrel", "Plavix", "Clopidogrel"],
    "Diphenhydramine": ["Diphenhydramine", "Benadryl", "Diphenhydramin"],
    "Methotrexate": ["Methotrexate", "MTX", "Methotrexat"],
}

# Drug class mappings - maps specific drugs to their therapeutic classes
# Used for class-based interaction checking (e.g., "ACE Inhibitor" matches all ACE inhibitors)
DRUG_CLASS_MAPPINGS = {
    # ACE Inhibitors
    "ACE Inhibitor": ["Captopril", "Enalapril", "Enalaprilat", "Lisinopril", "Ramipril", 
                      "Perindopril", "Fosinopril", "Benazepril", "Quinapril", "Trandolapril"],
    
    # ARBs (Angiotensin Receptor Blockers)
    "ARB": ["Losartan", "Valsartan", "Irbesartan", "Candesartan", "Telmisartan", 
            "Olmesartan", "Azilsartan", "Eprosartan"],
    
    # Beta-blockers
    "Beta-blocker": ["Metoprolol", "Propranolol", "Atenolol", "Bisoprolol", "Carvedilol",
                     "Labetalol", "Nadolol", "Pindolol", "Timolol", "Esmolol", "Nebivolol"],
    
    # Calcium Channel Blockers
    "CCB": ["Amlodipine", "Nifedipine", "Felodipine", "Isradipine", "Nicardipine", 
            "Diltiazem", "Verapamil"],
    "Calcium Channel Blocker": ["Amlodipine", "Nifedipine", "Felodipine", "Isradipine", 
                                "Nicardipine", "Diltiazem", "Verapamil"],
    
    # Statins
    "Statins": ["Atorvastatin", "Simvastatin", "Rosuvastatin", "Pravastatin", "Lovastatin",
                "Fluvastatin", "Pitavastatin"],
    
    # NSAIDs
    "NSAID": ["Ibuprofen", "Naproxen", "Diclofenac", "Indomethacin", "Ketorolac", 
              "Meloxicam", "Celecoxib", "Etoricoxib", "Piroxicam", "Mefenamic acid"],
    
    # SSRIs
    "SSRI": ["Fluoxetine", "Sertraline", "Paroxetine", "Citalopram", "Escitalopram", "Fluvoxamine"],
    
    # SNRIs
    "SNRI": ["Venlafaxine", "Duloxetine", "Desvenlafaxine", "Milnacipran"],
    
    # PPIs
    "PPI": ["Omeprazole", "Pantoprazole", "Lansoprazole", "Esomeprazole", "Rabeprazole", "Dexlansoprazole"],
    
    # H2 Blockers
    "H2 Blockers": ["Cimetidine", "Ranitidine", "Famotidine", "Nizatidine"],
    "H2 Blocker": ["Cimetidine", "Ranitidine", "Famotidine", "Nizatidine"],
    
    # Diuretics
    "Diuretic": ["Furosemide", "Hydrochlorothiazide", "Chlorthalidone", "Indapamide", 
                 "Bumetanide", "Torsemide", "Spironolactone", "Eplerenone", "Triamterene", "Amiloride"],
    
    # Sulfonylureas
    "Sulfonylurea": ["Glibenclamide", "Gliclazide", "Glimepiride", "Glipizide", "Tolbutamide", "Chlorpropamide"],
    
    # SGLT2 Inhibitors
    "SGLT2 Inhibitor": ["Canagliflozin", "Dapagliflozin", "Empagliflozin", "Ertugliflozin"],
    
    # DPP-4 Inhibitors
    "DPP-4 Inhibitor": ["Sitagliptin", "Saxagliptin", "Linagliptin", "Vildagliptin", "Alogliptin"],
    
    # GLP-1 Agonists
    "GLP-1 Agonist": ["Liraglutide", "Semaglutide", "Exenatide", "Dulaglutide", "Lixisenatide"],
    
    # TZDs
    "TZD": ["Pioglitazone", "Rosiglitazone"],
    
    # Alpha-glucosidase Inhibitors
    "Alpha-glucosidase Inhibitor": ["Acarbose", "Miglitol"],
    
    # Corticosteroids
    "Corticosteroid": ["Prednisone", "Prednisolone", "Methylprednisolone", "Dexamethasone", 
                       "Hydrocortisone", "Betamethasone", "Triamcinolone"],
    
    # Antifungals - Azoles
    "Azole Antifungal": ["Ketoconazole", "Fluconazole", "Itraconazole", "Voriconazole", "Posaconazole"],
    
    # Macrolides
    "Macrolide": ["Erythromycin", "Azithromycin", "Clarithromycin", "Roxithromycin"],
    
    # Quinolones
    "Quinolone": ["Ciprofloxacin", "Levofloxacin", "Moxifloxacin", "Ofloxacin", "Norfloxacin"],
    
    # Tetracyclines
    "Tetracycline": ["Doxycycline", "Minocycline", "Tetracycline", "Tigecycline"],
}


def _fuzzy_match(query: str, target: str, threshold: float = 0.8) -> float:
    """
    Calculate fuzzy matching score between two strings
    
    Args:
        query: Query string
        target: Target string
        threshold: Minimum similarity threshold
    
    Returns:
        Similarity score (0.0 to 1.0)
    """
    query_lower = query.lower().strip()
    target_lower = target.lower().strip()
    
    # Exact match
    if query_lower == target_lower:
        return 1.0
    
    # Starts with
    if target_lower.startswith(query_lower) or query_lower.startswith(target_lower):
        return 0.95
    
    # Contains
    if query_lower in target_lower or target_lower in query_lower:
        return 0.9
    
    # Sequence matcher
    similarity = SequenceMatcher(None, query_lower, target_lower).ratio()
    
    return similarity if similarity >= threshold else 0.0


def _find_best_drug_match(drug_name: str, threshold: float = 0.75) -> Optional[str]:
    """
    Find best matching drug name from database using fuzzy matching
    
    Args:
        drug_name: Drug name to match
        threshold: Minimum similarity threshold
    
    Returns:
        Best matching drug name or None
    """
    if not _DRUG_DB_LOADED or not DRUG_DATABASE:
        return None
    
    drug_lower = drug_name.strip().lower()
    best_match = None
    best_score = 0.0
    
    # Search in drug database
    for db_drug_name in DRUG_DATABASE.keys():
        score = _fuzzy_match(drug_name, db_drug_name, threshold=threshold)
        if score > best_score:
            best_score = score
            best_match = db_drug_name
    
    # Also search in Vietnamese names
    for db_drug_name, drug_data in DRUG_DATABASE.items():
        if 'vietnamese_name' in drug_data:
            vn_name = drug_data['vietnamese_name']
            score = _fuzzy_match(drug_name, vn_name, threshold=threshold)
            if score > best_score:
                best_score = score
                best_match = db_drug_name
    
    return best_match if best_score >= threshold else None


def get_drug_classes(drug_name: str) -> List[str]:
    """
    Get drug classes for a specific drug
    
    Args:
        drug_name: Drug name
    
    Returns:
        List of drug class names
    """
    classes = []
    drug_normalized = normalize_drug_name(drug_name)
    
    # Check direct class mappings
    for class_name, drugs_in_class in DRUG_CLASS_MAPPINGS.items():
        if drug_normalized in drugs_in_class:
            classes.append(class_name)
    
    # Check DRUG_GROUPS
    if _DRUG_DB_LOADED and DRUG_GROUPS:
        for group_name, drugs_in_group in DRUG_GROUPS.items():
            if drug_normalized in drugs_in_group:
                # Map group names to class names if needed
                if group_name == "Cardiovascular":
                    # Check if it's an ACE inhibitor, ARB, etc.
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("ACE Inhibitor", []):
                        classes.append("ACE Inhibitor")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("ARB", []):
                        classes.append("ARB")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("Beta-blocker", []):
                        classes.append("Beta-blocker")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("CCB", []):
                        classes.append("CCB")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("Statins", []):
                        classes.append("Statins")
                elif group_name == "Diabetes":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Sulfonylurea", []):
                        classes.append("Sulfonylurea")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("SGLT2 Inhibitor", []):
                        classes.append("SGLT2 Inhibitor")
                elif group_name == "Gastrointestinal":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("PPI", []):
                        classes.append("PPI")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("H2 Blockers", []):
                        classes.append("H2 Blockers")
                elif group_name == "Analgesics":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("NSAID", []):
                        classes.append("NSAID")
                elif group_name == "Neurology/Psychiatry":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("SSRI", []):
                        classes.append("SSRI")
                    elif drug_normalized in DRUG_CLASS_MAPPINGS.get("SNRI", []):
                        classes.append("SNRI")
    
    return list(set(classes))  # Remove duplicates


def normalize_drug_name(drug_name: str, use_fuzzy: bool = True) -> str:
    """
    Normalize drug name to canonical form with fuzzy matching support
    
    Args:
        drug_name: Drug name to normalize
        use_fuzzy: Whether to use fuzzy matching if exact match not found
    
    Returns:
        Canonical drug name or original if not found
    """
    if not drug_name or not drug_name.strip():
        return drug_name
    
    drug_lower = drug_name.strip().lower()
    drug_original = drug_name.strip()
    
    # 1. Check exact match in DRUG_INTERACTIONS keys
    for (d1, d2) in DRUG_INTERACTIONS.keys():
        if drug_original == d1 or drug_original == d2:
            return drug_original
    
    # 2. Check aliases
    for canonical, aliases in DRUG_ALIASES.items():
        if drug_lower in [a.lower() for a in aliases]:
            return canonical
    
    # 3. If exact match with canonical name
    if drug_original in DRUG_ALIASES:
        return drug_original
    
    # 4. Check in drug database (exact match)
    if _DRUG_DB_LOADED and DRUG_DATABASE:
        if drug_original in DRUG_DATABASE:
            return drug_original
        
        # Check Vietnamese names
        for db_drug_name, drug_data in DRUG_DATABASE.items():
            if 'vietnamese_name' in drug_data:
                if drug_data['vietnamese_name'].lower() == drug_lower:
                    return db_drug_name
    
    # 5. Fuzzy matching (if enabled)
    if use_fuzzy and _DRUG_DB_LOADED:
        fuzzy_match = _find_best_drug_match(drug_original, threshold=0.75)
        if fuzzy_match:
            return fuzzy_match
    
    # Return original if no match
    return drug_original


def get_interaction(drug1: str, drug2: str, check_classes: bool = True) -> Optional[dict]:
    """
    Get interaction between two drugs with class-based matching support
    
    Args:
        drug1: First drug name
        drug2: Second drug name
        check_classes: Whether to check class-based interactions
    
    Returns:
        Interaction dictionary or None if no interaction
    """
    # Normalize drug names
    norm1 = normalize_drug_name(drug1)
    norm2 = normalize_drug_name(drug2)
    
    # 1. Check direct drug-drug interaction (both orders)
    interaction = DRUG_INTERACTIONS.get((norm1, norm2))
    if interaction:
        return interaction
    
    interaction = DRUG_INTERACTIONS.get((norm2, norm1))
    if interaction:
        return interaction
    
    # 2. Check class-based interactions
    if check_classes:
        # Get classes for both drugs
        classes1 = get_drug_classes(norm1)
        classes2 = get_drug_classes(norm2)
        
        # Check drug1 vs drug2's classes
        for class2 in classes2:
            interaction = DRUG_INTERACTIONS.get((norm1, class2))
            if interaction:
                return interaction
            interaction = DRUG_INTERACTIONS.get((class2, norm1))
            if interaction:
                return interaction
        
        # Check drug2 vs drug1's classes
        for class1 in classes1:
            interaction = DRUG_INTERACTIONS.get((norm2, class1))
            if interaction:
                return interaction
            interaction = DRUG_INTERACTIONS.get((class1, norm2))
            if interaction:
                return interaction
        
        # Check class1 vs class2
        for class1 in classes1:
            for class2 in classes2:
                interaction = DRUG_INTERACTIONS.get((class1, class2))
                if interaction:
                    return interaction
                interaction = DRUG_INTERACTIONS.get((class2, class1))
                if interaction:
                    return interaction
    
    return None


def check_interactions(drug_list: list) -> list:
    """
    Check all pairwise interactions in a drug list
    
    Args:
        drug_list: List of drug names
    
    Returns:
        List of interaction dictionaries with drug pairs
    """
    interactions = []
    checked_pairs = set()
    
    for i, drug1 in enumerate(drug_list):
        for j, drug2 in enumerate(drug_list[i+1:], start=i+1):
            # Avoid checking same drug
            if drug1.lower() == drug2.lower():
                continue
            
            # Avoid duplicate checks
            pair = tuple(sorted([drug1, drug2]))
            if pair in checked_pairs:
                continue
            
            checked_pairs.add(pair)
            
            interaction = get_interaction(drug1, drug2)
            if interaction:
                interaction['drug1'] = drug1
                interaction['drug2'] = drug2
                interactions.append(interaction)
    
    # Sort by severity (Major > Moderate > Minor)
    severity_order = {SEVERITY_MAJOR: 0, SEVERITY_MODERATE: 1, SEVERITY_MINOR: 2}
    interactions.sort(key=lambda x: severity_order.get(x['severity'], 3))
    
    return interactions


def get_drug_autocomplete_suggestions(query: str, max_results: int = 10) -> List[str]:
    """
    Get autocomplete suggestions for drug names
    
    Args:
        query: Search query
        max_results: Maximum number of results
    
    Returns:
        List of suggested drug names
    """
    if not query or len(query.strip()) < 1:
        # Return popular drugs
        popular_drugs = [
            "Warfarin", "Aspirin", "Metformin", "Omeprazole", "Ibuprofen",
            "Atorvastatin", "Amlodipine", "Metoprolol", "Digoxin", "Insulin"
        ]
        return popular_drugs[:max_results]
    
    query_lower = query.strip().lower()
    suggestions = []
    seen = set()
    
    # 1. Exact matches in DRUG_INTERACTIONS
    for (d1, d2) in DRUG_INTERACTIONS.keys():
        for drug in [d1, d2]:
            if drug.lower().startswith(query_lower) and drug not in seen:
                suggestions.append(drug)
                seen.add(drug)
                if len(suggestions) >= max_results:
                    return suggestions
    
    # 2. Search in drug database
    if _DRUG_DB_LOADED and DRUG_DATABASE:
        # Exact matches first
        for drug_name in DRUG_DATABASE.keys():
            if drug_name.lower().startswith(query_lower) and drug_name not in seen:
                suggestions.append(drug_name)
                seen.add(drug_name)
                if len(suggestions) >= max_results:
                    return suggestions
        
        # Contains matches
        for drug_name in DRUG_DATABASE.keys():
            if query_lower in drug_name.lower() and drug_name not in seen:
                suggestions.append(drug_name)
                seen.add(drug_name)
                if len(suggestions) >= max_results:
                    return suggestions
        
        # Vietnamese name matches
        for drug_name, drug_data in DRUG_DATABASE.items():
            if drug_name in seen:
                continue
            if 'vietnamese_name' in drug_data:
                vn_name = drug_data['vietnamese_name'].lower()
                if query_lower in vn_name or vn_name.startswith(query_lower):
                    suggestions.append(drug_name)
                    seen.add(drug_name)
                    if len(suggestions) >= max_results:
                        return suggestions
    
    # 3. Fuzzy matches
    if len(suggestions) < max_results and _DRUG_DB_LOADED:
        fuzzy_results = []
        for drug_name in DRUG_DATABASE.keys():
            if drug_name in seen:
                continue
            score = _fuzzy_match(query, drug_name, threshold=0.6)
            if score > 0:
                fuzzy_results.append((drug_name, score))
        
        fuzzy_results.sort(key=lambda x: x[1], reverse=True)
        for drug_name, _ in fuzzy_results[:max_results - len(suggestions)]:
            suggestions.append(drug_name)
    
    return suggestions[:max_results]

