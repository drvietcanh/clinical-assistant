"""
Drug Interaction Database
Database of common drug interactions for Vietnamese healthcare
Based on clinical guidelines and Vietnamese drug availability
"""

# Interaction severity levels
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

# Drug interaction database
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
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế nếu cần giảm đau/sốt",
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
        "management": "Giảm liều warfarin 30-50% khi dùng metronidazole. Theo dõi INR 2-3 lần/tuần",
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
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi kali máu và chức năng thận thường xuyên",
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
        "management": "Tránh dùng chung. Nếu cần: giảm liều atorvastatin 50-75%, theo dõi CK",
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


def normalize_drug_name(drug_name: str) -> str:
    """
    Normalize drug name to canonical form
    
    Args:
        drug_name: Drug name to normalize
    
    Returns:
        Canonical drug name or original if not found
    """
    drug_lower = drug_name.strip().lower()
    
    # Check aliases
    for canonical, aliases in DRUG_ALIASES.items():
        if drug_lower in [a.lower() for a in aliases]:
            return canonical
    
    # If exact match with canonical name
    if drug_name in DRUG_ALIASES:
        return drug_name
    
    # Return original if no match
    return drug_name


def get_interaction(drug1: str, drug2: str) -> dict:
    """
    Get interaction between two drugs
    
    Args:
        drug1: First drug name
        drug2: Second drug name
    
    Returns:
        Interaction dictionary or None if no interaction
    """
    # Normalize drug names
    norm1 = normalize_drug_name(drug1)
    norm2 = normalize_drug_name(drug2)
    
    # Check both orders
    interaction = DRUG_INTERACTIONS.get((norm1, norm2))
    if interaction:
        return interaction
    
    interaction = DRUG_INTERACTIONS.get((norm2, norm1))
    if interaction:
        return interaction
    
    # Check for class-based interactions
    # (e.g., "ACE Inhibitor" with specific drugs)
    for (d1, d2), interaction in DRUG_INTERACTIONS.items():
        if (norm1 == d1 or norm2 == d1) and (norm2 == d2 or norm1 == d2):
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

