"""
Drug Interaction Database
Database of common drug interactions for Vietnamese healthcare
Based on clinical guidelines and Vietnamese drug availability
"""

from difflib import SequenceMatcher
from typing import Optional, List, Tuple, Dict

from .interaction_schema import (
    normalize_interaction_record,
    validate_interactions_db,
    SEVERITY_VALUES as CANONICAL_SEVERITIES,
    ONSET_VALUES as CANONICAL_ONSETS,
    EVIDENCE_LEVELS as CANONICAL_EVIDENCE,
)

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
    
    # ========== CLASS-BASED INTERACTIONS ==========
    
    # Anticoagulants + Antiplatelets
    ("Anticoagulant", "Antiplatelet"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết do tăng tác dụng chống đông và chống kết tập tiểu cầu",
        "description": "Tăng nguy cơ xuất huyết nặng, đặc biệt xuất huyết dạ dày-ruột và nội sọ",
        "clinical_significance": "Nguy cơ xuất huyết nặng tăng 2-4 lần. Chỉ dùng khi có chỉ định rõ ràng (ví dụ: sau stent với mechanical valve).",
        "management": "Chỉ dùng khi có chỉ định rõ ràng. Theo dõi INR và dấu hiệu xuất huyết sát. Dùng PPI bảo vệ dạ dày.",
        "references": "ACC/AHA Guidelines, Micromedex"
    },
    
    # Anticoagulants + NSAIDs
    ("Anticoagulant", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột và xuất huyết nặng",
        "description": "NSAID làm tăng nguy cơ xuất huyết dạ dày và tăng tác dụng chống đông",
        "clinical_significance": "Nguy cơ xuất huyết dạ dày-ruột tăng 2-4 lần. Đặc biệt nguy hiểm ở người cao tuổi.",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế nếu cần giảm đau/sốt. Nếu bắt buộc: dùng PPI bảo vệ dạ dày, theo dõi INR.",
        "alternatives": {
            "for_nsaid": ["Paracetamol", "Acetaminophen"],
            "for_anticoagulant": ["DOAC (nếu phù hợp)"]
        },
        "references": "Micromedex, AHFS Drug Information"
    },
    
    # QT prolongation clusters
    ("QT Prolonging", "QT Prolonging"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cộng hưởng kéo dài QT, tăng nguy cơ xoắn đỉnh",
        "description": "Kết hợp ≥2 thuốc kéo dài QT làm tăng mạnh nguy cơ xoắn đỉnh",
        "clinical_significance": "Nguy cơ cao hơn khi K+/Mg2+ thấp, nhịp chậm, suy tim, suy gan/thận.",
        "management": "Tránh nếu có thể. Nếu bắt buộc: theo dõi ECG trước và sau, điều chỉnh điện giải, giảm liều/cách khoảng, chọn thuốc thay thế ít kéo dài QT.",
        "monitoring": ["ECG (QTc)", "Điện giải (K, Mg)", "Nhịp tim"],
        "onset": "rapid",
        "evidence_level": "high",
        "references": ["CredibleMeds", "ACC/AHA", "Micromedex"],
    },
    ("Amiodarone", "Macrolide"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone + macrolide đều kéo dài QT; macrolide còn ức chế CYP3A4",
        "description": "Tăng nguy cơ xoắn đỉnh và loạn nhịp thất",
        "management": "Tránh. Nếu bắt buộc: theo dõi ECG, điện giải, cân nhắc azithromycin (ít kéo dài QT hơn) hoặc kháng sinh khác.",
        "monitoring": ["ECG (QTc)", "Điện giải"],
        "onset": "rapid",
        "evidence_level": "high",
        "references": ["CredibleMeds", "ACC/AHA", "Lexicomp"],
    },
    ("Amiodarone", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tác dụng cộng hưởng kéo dài QT",
        "description": "Nguy cơ xoắn đỉnh khi phối hợp amiodarone với fluoroquinolon",
        "management": "Tránh phối hợp. Nếu cần: chọn kháng sinh khác, theo dõi ECG, bổ sung Mg/K.",
        "monitoring": ["ECG (QTc)", "Điện giải"],
        "onset": "rapid",
        "references": ["CredibleMeds", "Micromedex"],
    },
    ("Haloperidol", "Macrolide"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cộng hưởng kéo dài QT, nguy cơ xoắn đỉnh",
        "description": "Tăng nguy cơ loạn nhịp thất nghiêm trọng",
        "management": "Tránh nếu có thể. Nếu bắt buộc: dùng liều thấp, theo dõi ECG liên tục ở ICU.",
        "monitoring": ["ECG (QTc)", "Điện giải"],
        "onset": "rapid",
        "references": ["Micromedex", "APA Guidelines"],
    },
    ("Haloperidol", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cộng hưởng kéo dài QT",
        "description": "Nguy cơ xoắn đỉnh tăng rõ rệt",
        "management": "Tránh. Nếu cần: theo dõi ECG, điều chỉnh yếu tố nguy cơ.",
        "monitoring": ["ECG (QTc)", "Điện giải"],
        "onset": "rapid",
        "references": ["CredibleMeds", "Micromedex"],
    },
    ("Ondansetron", "Quinolone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cộng hưởng kéo dài QT",
        "description": "Tăng nguy cơ kéo dài QTc, đặc biệt IV và liều cao",
        "management": "Hạn chế phối hợp. Nếu cần: dùng liều thấp ondansetron, theo dõi ECG ở bệnh nhân nguy cơ.",
        "monitoring": ["ECG (QTc)", "Điện giải"],
        "onset": "rapid",
        "references": ["FDA Warning", "Micromedex"],
    },

    # ICU sedatives/anesthetics
    ("Propofol", "Opioid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cộng hưởng ức chế thần kinh trung ương và hô hấp",
        "description": "Tăng nguy cơ suy hô hấp, hạ huyết áp sâu khi phối hợp truyền propofol với opioid",
        "management": "Giảm liều từng thuốc, chuẩn bị hỗ trợ hô hấp, theo dõi huyết áp liên tục.",
        "monitoring": ["Huyết áp", "SpO2/EtCO2", "Mức an thần"],
        "onset": "rapid",
        "references": ["ICU Sedation Guidelines", "Micromedex"],
    },
    ("Propofol", "Benzodiazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cộng hưởng ức chế thần kinh trung ương/hô hấp",
        "description": "Nguy cơ tụt huyết áp và suy hô hấp tăng rõ khi phối hợp propofol và benzodiazepine",
        "management": "Tránh chồng thuốc nếu không cần. Nếu phối hợp: giảm liều, theo dõi sát, chuẩn bị thông khí hỗ trợ.",
        "monitoring": ["Huyết áp", "SpO2/EtCO2"],
        "onset": "rapid",
        "references": ["ICU Sedation Guidelines"],
    },
    ("Midazolam", "Azole Antifungal"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Azole ức chế CYP3A4 → tăng nồng độ midazolam",
        "description": "Tăng kéo dài an thần, suy hô hấp, đặc biệt đường IV/ICU",
        "management": "Giảm mạnh liều midazolam hoặc chọn thuốc khác (ví dụ lorazepam). Theo dõi hô hấp/HA.",
        "monitoring": ["SpO2/EtCO2", "Huyết áp"],
        "onset": "rapid",
        "references": ["Lexicomp", "Micromedex"],
    },
    ("Midazolam", "Macrolide"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Macrolide ức chế CYP3A4 → tăng nồng độ midazolam",
        "description": "Kéo dài an thần, nguy cơ ức chế hô hấp",
        "management": "Giảm liều midazolam hoặc chọn kháng sinh khác; theo dõi hô hấp.",
        "monitoring": ["SpO2/EtCO2"],
        "onset": "rapid",
        "references": ["Micromedex"],
    },
    ("Dexmedetomidine", "Beta-blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cộng hưởng giảm nhịp tim/huyết áp",
        "description": "Tăng nguy cơ nhịp chậm, tụt huyết áp",
        "management": "Theo dõi huyết áp/nhịp tim sát; cân nhắc giảm liều một trong hai thuốc.",
        "monitoring": ["Huyết áp", "Nhịp tim"],
        "onset": "rapid",
        "references": ["ICU Sedation Guidelines"],
    },

    # DOACs + Boosted PI (ritonavir/cobicistat)
    ("Rivaroxaban", "Boosted PI"): {
        "severity": "Contraindicated",
        "mechanism": "Ritonavir/cobicistat ức chế mạnh CYP3A4/P-gp → tăng nồng độ DOAC",
        "description": "Nguy cơ xuất huyết nặng",
        "management": "TRÁNH phối hợp. Cân nhắc LMWH hoặc warfarin (theo dõi INR) thay thế.",
        "onset": "rapid",
        "references": ["FDA Label", "EHRA Guide"],
    },
    ("Apixaban", "Boosted PI"): {
        "severity": "Contraindicated",
        "mechanism": "Ức chế mạnh CYP3A4/P-gp → tăng nồng độ apixaban",
        "description": "Nguy cơ xuất huyết nặng",
        "management": "Tránh. Nếu bắt buộc: giảm 50% liều chỉ khi dùng 5–10 mg BID; ưu tiên LMWH/warfarin.",
        "onset": "rapid",
        "references": ["FDA Label", "EHRA Guide"],
    },
    ("Dabigatran", "Boosted PI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ức chế P-gp → tăng nồng độ dabigatran",
        "description": "Tăng nguy cơ xuất huyết, đặc biệt nếu suy thận",
        "management": "Tránh nếu CrCl <50. Nếu dùng: giảm liều và theo dõi xuất huyết.",
        "onset": "rapid",
        "references": ["EHRA Guide"],
    },

    # INSTI + Rifampin (cảm ứng mạnh UGT/CYP)
    ("Bictegravir", "Rifampin"): {
        "severity": "Contraindicated",
        "mechanism": "Rifampin cảm ứng UGT/CYP → giảm mạnh nồng độ bictegravir",
        "description": "Mất hiệu lực kháng virus, nguy cơ kháng thuốc",
        "management": "Tránh phối hợp. Nếu cần rifamycin: dùng rifabutin và điều chỉnh phác đồ ARV.",
        "onset": "rapid",
        "references": ["FDA Label", "WHO HIV/TB"],
    },
    ("Cabotegravir", "Rifampin"): {
        "severity": "Contraindicated",
        "mechanism": "Cảm ứng UGT1A1/1A9 → giảm nồng độ cabotegravir (kể cả LA IM)",
        "description": "Giảm hiệu quả điều trị HIV",
        "management": "Tránh. Nếu cần rifamycin: đổi phác đồ ARV, cân nhắc rifabutin.",
        "onset": "rapid",
        "references": ["FDA Label"],
    },
    ("Rilpivirine", "Rifampin"): {
        "severity": "Contraindicated",
        "mechanism": "Cảm ứng CYP3A → giảm nồng độ rilpivirine",
        "description": "Mất hiệu lực kháng virus",
        "management": "Tránh. Nếu cần rifamycin: chọn phác đồ khác (dolutegravir + rifabutin...).",
        "onset": "rapid",
        "references": ["FDA Label"],
    },
    ("Lopinavir/ritonavir", "Rifampin"): {
        "severity": "Contraindicated",
        "mechanism": "Rifampin cảm ứng mạnh CYP3A → giảm nồng độ PI; ritonavir cũng bị ảnh hưởng",
        "description": "Mất hiệu lực điều trị HIV, nguy cơ kháng thuốc",
        "management": "Tránh. Dùng rifabutin (liều giảm) hoặc đổi phác đồ HIV.",
        "onset": "rapid",
        "references": ["WHO HIV/TB", "FDA Label"],
    },
    ("Atazanavir (boosted)", "Rifampin"): {
        "severity": "Contraindicated",
        "mechanism": "Cảm ứng CYP3A → giảm mạnh nồng độ atazanavir",
        "description": "Mất hiệu lực điều trị HIV",
        "management": "Tránh. Nếu cần rifamycin: rifabutin liều giảm hoặc đổi phác đồ.",
        "onset": "rapid",
        "references": ["WHO HIV/TB"],
    },

    # Atazanavir + PPI
    ("Atazanavir (boosted)", "PPI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng pH dạ dày giảm hấp thu atazanavir",
        "description": "Giảm nồng độ atazanavir, nguy cơ thất bại điều trị",
        "management": "Tránh PPI liều cao; omeprazole ≤20mg nên uống cách ≥12h. Ưu tiên H2 blocker.",
        "onset": "rapid",
        "references": ["FDA Label"],
    },

    # PDE5 inhibitors
    ("PDE5 Inhibitor", "Nitrate"): {
        "severity": "Contraindicated",
        "mechanism": "Cộng hưởng tăng cGMP → tụt huyết áp nghiêm trọng",
        "description": "Tụt huyết áp, ngất, nhồi máu cơ tim",
        "management": "CHỐNG CHỈ ĐỊNH. Không dùng đồng thời hoặc trong vòng 24–48h tùy PDE5i.",
        "onset": "rapid",
        "references": ["ACC/AHA", "FDA"],
    },
    ("PDE5 Inhibitor", "sGC Stimulator"): {
        "severity": "Contraindicated",
        "mechanism": "Tăng cGMP mạnh",
        "description": "Hạ huyết áp nguy hiểm",
        "management": "Chống chỉ định phối hợp với riociguat.",
        "onset": "rapid",
        "references": ["FDA Label"],
    },
    ("PDE5 Inhibitor", "Alpha-blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cộng hưởng giãn mạch",
        "description": "Hạ huyết áp tư thế, chóng mặt/ngất",
        "management": "Bắt đầu PDE5i liều thấp, dùng cách thời gian với alpha-blocker, theo dõi HA.",
        "onset": "rapid",
        "references": ["ACC/AHA"],
    },

    # Statins + Boosted PI
    ("Simvastatin", "Boosted PI"): {
        "severity": "Contraindicated",
        "mechanism": "Ức chế CYP3A4 mạnh → tăng nồng độ simvastatin",
        "description": "Nguy cơ tiêu cơ vân nghiêm trọng",
        "management": "Tránh. Chọn pravastatin/rosuvastatin liều thấp.",
        "onset": "rapid",
        "references": ["FDA", "ACC/AHA"],
    },
    ("Lovastatin", "Boosted PI"): {
        "severity": "Contraindicated",
        "mechanism": "Ức chế CYP3A4 mạnh → tăng nồng độ lovastatin",
        "description": "Nguy cơ tiêu cơ vân",
        "management": "Tránh. Chọn pravastatin/rosuvastatin liều thấp.",
        "onset": "rapid",
        "references": ["FDA", "ACC/AHA"],
    },
    # DOACs + mạnh ức chế/cảm ứng
    ("Rivaroxaban", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế mạnh CYP3A4/P-gp → tăng nồng độ rivaroxaban",
        "description": "Nguy cơ xuất huyết nặng",
        "management": "Tránh phối hợp. Nếu buộc dùng azole: cân nhắc đổi sang LMWH.",
        "monitoring": ["Dấu hiệu xuất huyết", "Hb/Hct nếu điều trị dài ngày"],
        "onset": "rapid",
        "references": ["FDA Label", "Micromedex"],
    },
    ("Apixaban", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ức chế CYP3A4/P-gp → tăng nồng độ apixaban",
        "description": "Nguy cơ xuất huyết nặng",
        "management": "Tránh phối hợp. Nếu dùng: giảm liều apixaban 50% và theo dõi sát.",
        "monitoring": ["Dấu hiệu xuất huyết"],
        "onset": "rapid",
        "references": ["FDA Label", "Micromedex"],
    },
    ("Rivaroxaban", "Rifampin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng CYP3A4/P-gp → giảm nồng độ rivaroxaban",
        "description": "Giảm hiệu quả chống đông, tăng nguy cơ huyết khối",
        "management": "Tránh phối hợp; chọn warfarin hoặc LMWH khi cần dùng rifampin.",
        "onset": "delayed",
        "references": ["FDA Label"],
    },
    ("Apixaban", "Rifampin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cảm ứng CYP3A4/P-gp → giảm nồng độ apixaban",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh; cân nhắc warfarin/LMWH trong thời gian dùng rifampin.",
        "onset": "delayed",
        "references": ["FDA Label"],
    },
    ("Dabigatran", "Amiodarone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Amiodarone ức chế P-gp → tăng nồng độ dabigatran",
        "description": "Tăng nguy cơ xuất huyết, đặc biệt ở bệnh nhân suy thận",
        "management": "Giảm liều dabigatran nếu CrCl 30-50 mL/phút; theo dõi xuất huyết.",
        "onset": "rapid",
        "references": ["EHRA Practical Guide", "Micromedex"],
    },
    ("Dabigatran", "Verapamil"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Verapamil ức chế P-gp → tăng hấp thu dabigatran",
        "description": "Nguy cơ xuất huyết tăng nhẹ-trung bình",
        "management": "Dùng dabigatran 2 giờ trước verapamil hoặc giảm liều; theo dõi xuất huyết.",
        "onset": "rapid",
        "references": ["EHRA Practical Guide"],
    },

    # Statins + Macrolides
    ("Statins", "Macrolide"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Macrolide ức chế CYP3A4 → Tăng nồng độ statin → Tăng nguy cơ tiêu cơ vân",
        "description": "Tăng nguy cơ tiêu cơ vân nghiêm trọng, có thể tử vong",
        "clinical_significance": "Nguy cơ tiêu cơ vân tăng 10-15 lần. Đặc biệt nguy hiểm với Simvastatin, Lovastatin, Atorvastatin.",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: giảm liều statin 50-75%, theo dõi CK, triệu chứng đau cơ. Hoặc chuyển sang Pravastatin/Rosuvastatin (ít tương tác hơn).",
        "alternatives": {
            "for_macrolide": ["Azithromycin (ít tương tác hơn)", "Doxycycline"],
            "for_statins": ["Pravastatin", "Rosuvastatin"]
        },
        "references": "FDA, Micromedex, ACC/AHA Guidelines"
    },
    
    # Statins + Azole Antifungals
    ("Statins", "Azole Antifungal"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Azole antifungal ức chế CYP3A4 → Tăng nồng độ statin → Tăng nguy cơ tiêu cơ vân",
        "description": "Tăng nguy cơ tiêu cơ vân nghiêm trọng",
        "clinical_significance": "Nguy cơ tiêu cơ vân tăng 10-20 lần. Đặc biệt nguy hiểm với Ketoconazole, Itraconazole.",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: giảm liều statin 50-75%, theo dõi CK. Hoặc chuyển sang Pravastatin/Rosuvastatin.",
        "alternatives": {
            "for_azole": ["Terbinafine (nếu phù hợp)", "Amphotericin B (nếu phù hợp)"],
            "for_statins": ["Pravastatin", "Rosuvastatin"]
        },
        "references": "FDA, Micromedex"
    },
    
    # ACE Inhibitors + Potassium-sparing Diuretics
    ("ACE Inhibitor", "Potassium-sparing Diuretic"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cả hai đều giữ kali → Tăng nguy cơ tăng kali máu nguy hiểm",
        "description": "Tăng nguy cơ tăng kali máu nghiêm trọng, có thể gây rối loạn nhịp tim",
        "clinical_significance": "Kali máu có thể tăng >5.5 mEq/L, nguy cơ rối loạn nhịp tim, đặc biệt ở bệnh nhân suy thận.",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi kali máu sát (mỗi 1-2 tuần khi bắt đầu, sau đó mỗi tháng). Nếu K+ >5.5 mEq/L: giảm liều hoặc ngừng một trong hai thuốc.",
        "alternatives": {
            "for_potassium_sparing": ["Furosemide", "Hydrochlorothiazide"],
            "for_ace_inhibitor": ["ARB (Losartan, Valsartan)"]
        },
        "references": "Micromedex, AHFS Drug Information, KDIGO Guidelines"
    },
    
    # ARBs + Potassium-sparing Diuretics
    ("ARB", "Potassium-sparing Diuretic"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cả hai đều giữ kali → Tăng nguy cơ tăng kali máu",
        "description": "Tăng nguy cơ tăng kali máu nghiêm trọng",
        "management": "Theo dõi kali máu sát. Tránh dùng chung nếu có thể.",
        "references": "Micromedex"
    },
    
    # ACE Inhibitors + NSAIDs
    ("ACE Inhibitor", "NSAID"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID ức chế prostaglandin → Co mạch thận → Giảm GFR. ACE-I giãn tiểu động mạch thận → Giảm GFR. Tác dụng cộng hưởng.",
        "description": "Giảm hiệu quả hạ huyết áp của ACE-I, tăng nguy cơ suy thận cấp",
        "clinical_significance": "Có thể gây suy thận cấp, đặc biệt ở bệnh nhân suy thận, cao tuổi, mất nước.",
        "management": "Tránh NSAIDs nếu có thể. Dùng Paracetamol thay thế. Nếu bắt buộc: theo dõi huyết áp, Cr, K+ thường xuyên. Dùng liều thấp nhất, thời gian ngắn nhất.",
        "alternatives": {
            "for_nsaid": ["Paracetamol", "Acetaminophen"]
        },
        "references": "JNC 8, KDIGO Guidelines, Micromedex"
    },
    
    # ARBs + NSAIDs
    ("ARB", "NSAID"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tương tự ACE-I + NSAID",
        "description": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận cấp",
        "management": "Tránh NSAIDs nếu có thể. Theo dõi huyết áp và chức năng thận.",
        "references": "JNC 8, KDIGO Guidelines"
    },
    
    # SSRIs + MAOIs
    ("SSRI", "MAOI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "MAOIs ức chế phân hủy serotonin. SSRIs tăng serotonin. → Tích lũy serotonin quá mức → Hội chứng Serotonin.",
        "description": "Hội chứng Serotonin nghiêm trọng - có thể tử vong",
        "clinical_significance": "Nguy cơ cao gây hội chứng Serotonin với các triệu chứng: kích động, tăng thân nhiệt, co giật, rối loạn nhịp tim, tử vong.",
        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. Ngừng MAOI ít nhất 14 ngày trước khi bắt đầu SSRI. Ngừng SSRI ít nhất 5 tuần (Fluoxetine) hoặc 2 tuần (SSRI khác) trước khi bắt đầu MAOI.",
        "references": "FDA Contraindication, Sternbach Criteria, Micromedex"
    },
    
    # SSRIs + SNRIs
    ("SSRI", "SNRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cả hai đều tăng serotonin → Tăng nguy cơ hội chứng Serotonin",
        "description": "Tăng nguy cơ hội chứng Serotonin",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp, theo dõi sát triệu chứng hội chứng Serotonin.",
        "references": "Micromedex"
    },
    
    # SSRIs + Opioids (Tramadol)
    ("SSRI", "Opioid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "SSRI + Opioid (đặc biệt Tramadol) → Tăng nguy cơ hội chứng Serotonin và co giật",
        "description": "Tăng nguy cơ hội chứng Serotonin và co giật",
        "clinical_significance": "Đặc biệt nguy hiểm với Tramadol. Có thể gây co giật, nhầm lẫn, hôn mê.",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: dùng liều thấp, theo dõi sát. Tránh Tramadol.",
        "alternatives": {
            "for_opioid": ["Morphine", "Codeine (nếu phù hợp)"],
            "for_ssri": ["Mirtazapine (nếu phù hợp)"]
        },
        "references": "Micromedex, FDA Warning"
    },
    
    # Quinolones + Antacids
    ("Quinolone", "Antacid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Antacid (Ca, Mg, Al) chelate với quinolone → Giảm hấp thu quinolone",
        "description": "Giảm đáng kể hấp thu quinolone → Giảm hiệu quả điều trị",
        "management": "Cách xa ít nhất 2 giờ. Tốt nhất: dùng antacid 2 giờ sau quinolone.",
        "references": "Micromedex, FDA Label"
    },
    
    # Metformin + Contrast Media
    ("Metformin", "Contrast Media"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Thuốc cản quang có thể gây suy thận cấp → Giảm thải Metformin → Tích lũy Metformin → Toan lactic.",
        "description": "Nguy cơ toan lactic (Lactic acidosis) - có thể tử vong",
        "clinical_significance": "Nguy cơ toan lactic tăng đáng kể, đặc biệt ở bệnh nhân suy thận, cao tuổi.",
        "management": "NGỪNG Metformin trước chụp CT/MRI có thuốc cản quang. Ngừng ít nhất 48h trước. Kiểm tra chức năng thận sau chụp. Chỉ dùng lại Metformin khi chức năng thận bình thường (ít nhất 48-72h sau chụp).",
        "references": "FDA Label, ACR Guidelines, Micromedex"
    },
    
    # Methotrexate + NSAIDs
    ("Methotrexate", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "NSAID làm giảm đào thải methotrexate qua thận (ức chế bài tiết ống thận). NSAID cũng giảm GFR → Giảm lọc Methotrexate.",
        "description": "Tăng độc tính Methotrexate (suy tủy, độc gan, độc thận)",
        "clinical_significance": "Nguy cơ độc tính tăng đáng kể, đặc biệt với liều cao Methotrexate (>20mg/tuần).",
        "management": "Tránh NSAIDs khi dùng Methotrexate liều cao (>20mg/tuần hoặc liều hóa trị). Với liều thấp (RA): Có thể dùng NSAIDs nhưng theo dõi CBC, AST/ALT, Cr thường xuyên. Dùng Paracetamol thay thế nếu có thể.",
        "alternatives": {
            "for_nsaid": ["Paracetamol", "Acetaminophen"]
        },
        "references": "FDA Label, ACR Guidelines, Micromedex"
    },
    
    # Digoxin + Amiodarone
    ("Digoxin", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone ức chế P-glycoprotein → Giảm thải Digoxin qua thận và ruột → Tăng nồng độ Digoxin",
        "description": "Tăng nồng độ Digoxin → Độc Digoxin (buồn nôn, rối loạn nhịp, rối loạn thị giác)",
        "clinical_significance": "Nồng độ Digoxin có thể tăng 2-3 lần. Nguy cơ độc tính cao.",
        "management": "Giảm liều Digoxin 50% khi bắt đầu Amiodarone. Theo dõi nồng độ Digoxin (mục tiêu 0.5-0.9 ng/mL). Theo dõi triệu chứng độc Digoxin, ECG, K+ máu.",
        "references": "UpToDate, ACC/AHA AF Guidelines, Micromedex"
    },
}

# Merge with expanded interactions
if _EXPANDED_LOADED:
    DRUG_INTERACTIONS.update(EXPANDED_INTERACTIONS)

# Alternative drug names mapping (Vietnamese names, brand names, etc.)
# Expanded with common brand names and Vietnamese names
DRUG_ALIASES = {
    # Anticoagulants
    "Warfarin": ["Warfarin", "Coumadin", "Marevan", "Warfarin sodium", "Warfarin natri"],
    "Aspirin": ["Aspirin", "Acetylsalicylic acid", "ASA", "Aspirin", "Acetyl salicylic acid"],
    "Clopidogrel": ["Clopidogrel", "Plavix", "Clopidogrel bisulfate"],
    "Ticagrelor": ["Ticagrelor", "Brilinta"],
    "Prasugrel": ["Prasugrel", "Effient"],
    "Dabigatran": ["Dabigatran", "Pradaxa"],
    "Rivaroxaban": ["Rivaroxaban", "Xarelto"],
    "Apixaban": ["Apixaban", "Eliquis"],
    "Edoxaban": ["Edoxaban", "Savaysa"],
    
    # NSAIDs & Analgesics
    "Ibuprofen": ["Ibuprofen", "Brufen", "Advil", "Nurofen", "Motrin"],
    "Naproxen": ["Naproxen", "Naprosyn", "Aleve"],
    "Diclofenac": ["Diclofenac", "Voltaren", "Cataflam"],
    "Paracetamol": ["Paracetamol", "Acetaminophen", "Tylenol", "Panadol"],
    "Tramadol": ["Tramadol", "Tramal", "Tramadon", "Ultram"],
    
    # PPIs & GI
    "Omeprazole": ["Omeprazole", "Losec", "Omez", "Prilosec"],
    "Pantoprazole": ["Pantoprazole", "Protonix", "Pantoloc"],
    "Lansoprazole": ["Lansoprazole", "Prevacid", "Lanzor"],
    "Esomeprazole": ["Esomeprazole", "Nexium"],
    "Rabeprazole": ["Rabeprazole", "Aciphex", "Pariet"],
    
    # Antibiotics
    "Amoxicillin": ["Amoxicillin", "Amoxil", "Amoxicilline"],
    "Ciprofloxacin": ["Ciprofloxacin", "Cipro", "Cifran", "Ciprobay"],
    "Levofloxacin": ["Levofloxacin", "Levaquin", "Tavanic"],
    "Azithromycin": ["Azithromycin", "Zithromax", "Azithro"],
    "Clarithromycin": ["Clarithromycin", "Klacid", "Biaxin"],
    "Erythromycin": ["Erythromycin", "Erythrocin"],
    "Metronidazole": ["Metronidazole", "Flagyl", "Metronidazol"],
    "Ceftriaxone": ["Ceftriaxone", "Rocephin"],
    "Cefazolin": ["Cefazolin", "Ancef", "Kefzol"],
    
    # Antifungals
    "Fluconazole": ["Fluconazole", "Diflucan", "Fluconazol"],
    "Ketoconazole": ["Ketoconazole", "Nizoral", "Ketoconazol"],
    "Itraconazole": ["Itraconazole", "Sporanox"],
    "Voriconazole": ["Voriconazole", "Vfend"],
    
    # Antidepressants
    "Fluoxetine": ["Fluoxetine", "Prozac", "Fluoxetin", "Prozac"],
    "Sertraline": ["Sertraline", "Zoloft"],
    "Citalopram": ["Citalopram", "Celexa"],
    "Escitalopram": ["Escitalopram", "Lexapro"],
    "Paroxetine": ["Paroxetine", "Paxil"],
    "Venlafaxine": ["Venlafaxine", "Effexor"],
    "Duloxetine": ["Duloxetine", "Cymbalta"],
    
    # Cardiovascular
    "Digoxin": ["Digoxin", "Lanoxin", "Digoxine"],
    "Amiodarone": ["Amiodarone", "Cordarone", "Amiodaron"],
    "Lisinopril": ["Lisinopril", "Prinivil", "Zestril"],
    "Enalapril": ["Enalapril", "Vasotec"],
    "Losartan": ["Losartan", "Cozaar"],
    "Valsartan": ["Valsartan", "Diovan"],
    "Amlodipine": ["Amlodipine", "Norvasc"],
    "Metoprolol": ["Metoprolol", "Lopressor", "Toprol"],
    "Atenolol": ["Atenolol", "Tenormin"],
    "Carvedilol": ["Carvedilol", "Coreg"],
    "Propranolol": ["Propranolol", "Inderal"],
    
    # Statins
    "Atorvastatin": ["Atorvastatin", "Lipitor"],
    "Simvastatin": ["Simvastatin", "Zocor"],
    "Rosuvastatin": ["Rosuvastatin", "Crestor"],
    "Pravastatin": ["Pravastatin", "Pravachol"],
    
    # Antidiabetics
    "Metformin": ["Metformin", "Glucophage", "Metformin HCl", "Glucophage"],
    "Glibenclamide": ["Glibenclamide", "Glyburide", "Daonil"],
    "Gliclazide": ["Gliclazide", "Diamicron"],
    "Glimepiride": ["Glimepiride", "Amaryl"],
    "Sitagliptin": ["Sitagliptin", "Januvia"],
    "Dapagliflozin": ["Dapagliflozin", "Farxiga"],
    "Empagliflozin": ["Empagliflozin", "Jardiance"],
    "Insulin": ["Insulin", "Humulin", "Novolin"],
    
    # Others
    "Diphenhydramine": ["Diphenhydramine", "Benadryl", "Diphenhydramin"],
    "Methotrexate": ["Methotrexate", "MTX", "Methotrexat", "Trexall"],
    "Prednisone": ["Prednisone", "Deltasone"],
    "Furosemide": ["Furosemide", "Lasix"],
    "Spironolactone": ["Spironolactone", "Aldactone"],
    "Hydrochlorothiazide": ["Hydrochlorothiazide", "HCTZ", "Microzide"],
    "Levothyroxine": ["Levothyroxine", "Synthroid", "Levoxyl"],
    
    # Vietnamese common names (phổ biến ở VN)
    "Paracetamol": ["Paracetamol", "Paracetamol", "Panadol", "Efferalgan", "Hapacol"],
    "Amoxicillin": ["Amoxicillin", "Amoxicillin", "Clamoxyl"],
    "Ciprofloxacin": ["Ciprofloxacin", "Ciprofloxacin", "Cifran"],
    "Omeprazole": ["Omeprazole", "Omeprazole", "Omez", "Losec"],
    "Metformin": ["Metformin", "Metformin", "Glucophage"],
    "Atorvastatin": ["Atorvastatin", "Atorvastatin", "Lipitor"],
    "Amlodipine": ["Amlodipine", "Amlodipine", "Norvasc"],
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
                     "Labetalol", "Nadolol", "Pindolol", "Timolol", "Esmolol", "Nebivolol",
                     "Acebutolol", "Betaxolol"],
    
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
    
    # Anticoagulants
    "Anticoagulant": ["Warfarin", "Dabigatran", "Rivaroxaban", "Apixaban", "Edoxaban", "Heparin", "Enoxaparin"],
    "DOAC": ["Dabigatran", "Rivaroxaban", "Apixaban", "Edoxaban"],  # Direct Oral Anticoagulants
    "LMWH": ["Enoxaparin", "Dalteparin", "Tinzaparin"],  # Low Molecular Weight Heparin
    
    # Antiplatelets
    "Antiplatelet": ["Aspirin", "Clopidogrel", "Ticagrelor", "Prasugrel", "Ticlopidine", "Dipyridamole"],
    
    # Anticonvulsants
    "Anticonvulsant": ["Phenytoin", "Carbamazepine", "Valproate", "Lamotrigine", "Levetiracetam", 
                       "Topiramate", "Gabapentin", "Pregabalin", "Oxcarbazepine"],
    
    # Antipsychotics
    "Antipsychotic": ["Haloperidol", "Risperidone", "Olanzapine", "Quetiapine", "Aripiprazole", 
                      "Clozapine", "Ziprasidone"],
    
    # Benzodiazepines
    "Benzodiazepine": ["Diazepam", "Lorazepam", "Alprazolam", "Clonazepam", "Midazolam", "Temazepam"],
    
    # Antihistamines
    "Antihistamine": ["Diphenhydramine", "Loratadine", "Cetirizine", "Fexofenadine", "Desloratadine", 
                      "Levocetirizine"],
    
    # Beta-lactam Antibiotics
    "Penicillin": ["Amoxicillin", "Ampicillin", "Penicillin G", "Penicillin V", "Amoxicillin-clavulanate"],
    "Cephalosporin": ["Ceftriaxone", "Cefazolin", "Cefuroxime", "Ceftazidime", "Cefepime", "Cephalexin"],
    "Carbapenem": ["Imipenem", "Meropenem", "Ertapenem", "Doripenem"],
    
    # Aminoglycosides
    "Aminoglycoside": ["Gentamicin", "Tobramycin", "Amikacin", "Streptomycin"],
    
    # Antivirals
    "Antiviral": ["Acyclovir", "Valacyclovir", "Oseltamivir", "Ganciclovir", "Valganciclovir", 
                  "Ribavirin", "Lamivudine", "Tenofovir"],
    
    # Immunosuppressants
    "Immunosuppressant": ["Cyclosporine", "Tacrolimus", "Mycophenolate", "Azathioprine", "Sirolimus", 
                          "Everolimus"],
    
    # Chemotherapy
    "Chemotherapy": ["Methotrexate", "Cisplatin", "Carboplatin", "Cyclophosphamide", "Doxorubicin", 
                     "5-Fluorouracil", "Paclitaxel", "Docetaxel"],
    
    # Potassium-sparing Diuretics
    "Potassium-sparing Diuretic": ["Spironolactone", "Eplerenone", "Triamterene", "Amiloride"],
    
    # Loop Diuretics
    "Loop Diuretic": ["Furosemide", "Bumetanide", "Torsemide", "Ethacrynic acid"],
    
    # Thiazide Diuretics
    "Thiazide Diuretic": ["Hydrochlorothiazide", "Chlorthalidone", "Indapamide", "Metolazone"],
    
    # Antiemetics
    "Antiemetic": ["Ondansetron", "Granisetron", "Metoclopramide", "Domperidone", "Prochlorperazine"],
    
    # Opioids
    "Opioid": ["Morphine", "Codeine", "Tramadol", "Fentanyl", "Oxycodone", "Hydrocodone", "Methadone"],
    
    # MAOIs
    "MAOI": ["Phenelzine", "Tranylcypromine", "Isocarboxazid", "Selegiline"],
    
    # TCAs (Tricyclic Antidepressants)
    "TCA": ["Amitriptyline", "Nortriptyline", "Imipramine", "Desipramine", "Doxepin"],
    
    # Antacids
    "Antacid": ["Calcium carbonate", "Magnesium hydroxide", "Aluminum hydroxide", "Sodium bicarbonate"],
    
    # Contrast Media
    "Contrast Media": ["Iodinated contrast", "Gadolinium contrast", "Barium contrast"],

    # Alpha-blockers (uroselective / không chọn lọc)
    "Alpha-blocker": ["Tamsulosin", "Alfuzosin", "Doxazosin", "Terazosin", "Silodosin"],

    # PDE5 Inhibitors
    "PDE5 Inhibitor": ["Sildenafil", "Tadalafil", "Vardenafil", "Avanafil"],

    # Nitrates
    "Nitrate": ["Nitroglycerin", "Isosorbide dinitrate", "Isosorbide mononitrate"],

    # Soluble guanylate cyclase stimulator
    "sGC Stimulator": ["Riociguat"],

    # Protease inhibitors (boosted)
    "Boosted PI": ["Lopinavir/ritonavir", "Darunavir/ritonavir", "Atazanavir (boosted)", "Saquinavir/ritonavir"],

    # Integrase inhibitors
    "INSTI": ["Bictegravir", "Dolutegravir", "Cabotegravir"],

    # QT prolonging agents (high-risk cluster)
    "QT Prolonging": [
        "Amiodarone", "Sotalol", "Dofetilide", "Ibutilide",
        "Haloperidol", "Ziprasidone", "Quetiapine",
        "Ondansetron", "Granisetron",
        "Methadone",
        "Ciprofloxacin", "Levofloxacin", "Moxifloxacin",
        "Clarithromycin", "Erythromycin",
    ],
}


def _fuzzy_match(query: str, target: str, threshold: float = 0.70) -> float:
    """
    Calculate fuzzy matching score between two strings
    Enhanced with better matching algorithms including typo handling
    
    Args:
        query: Query string
        target: Target string
        threshold: Minimum similarity threshold (lowered to 0.70 for better matching)
    
    Returns:
        Similarity score (0.0 to 1.0)
    """
    query_lower = query.lower().strip()
    target_lower = target.lower().strip()
    
    # Exact match
    if query_lower == target_lower:
        return 1.0
    
    # Remove common suffixes/prefixes for better matching
    common_suffixes = [' hcl', ' hydrochloride', ' sodium', ' tablet', ' injection', ' iv', ' oral', 
                       ' mg', ' ml', ' solution', ' capsule', ' tablet', ' syrup', ' cream', ' gel']
    common_prefixes = ['oral ', 'iv ', 'injection ', 'tablet ', 'capsule ']
    
    query_clean = query_lower
    target_clean = target_lower
    
    for suffix in common_suffixes:
        query_clean = query_clean.replace(suffix, '')
        target_clean = target_clean.replace(suffix, '')
    
    for prefix in common_prefixes:
        if query_clean.startswith(prefix):
            query_clean = query_clean[len(prefix):].strip()
        if target_clean.startswith(prefix):
            target_clean = target_clean[len(prefix):].strip()
    
    # Check cleaned versions
    if query_clean == target_clean:
        return 0.98
    
    # Starts with (improved) - check both directions
    if target_clean.startswith(query_clean) or query_clean.startswith(target_clean):
        # Longer match gets higher score
        min_len = min(len(query_clean), len(target_clean))
        max_len = max(len(query_clean), len(target_clean))
        if min_len >= 3:  # Only if meaningful length
            return 0.90 + (min_len / max_len) * 0.05
    
    # Contains (improved) - check both directions
    if query_clean in target_clean or target_clean in query_clean:
        # Longer match gets higher score
        min_len = min(len(query_clean), len(target_clean))
        max_len = max(len(query_clean), len(target_clean))
        if min_len >= 4:  # Only if meaningful length
            return 0.85 + (min_len / max_len) * 0.05
    
    # Word-based matching (better for multi-word drug names)
    query_words = set(query_clean.split())
    target_words = set(target_clean.split())
    if query_words and target_words:
        word_overlap = len(query_words & target_words) / max(len(query_words), len(target_words))
        if word_overlap > 0.5:
            return 0.80 + (word_overlap * 0.15)
        elif word_overlap > 0.3:  # Partial word match
            return 0.70 + (word_overlap * 0.10)
    
    # Character-based similarity (for typos)
    # Check if strings are similar length and have high character overlap
    if abs(len(query_clean) - len(target_clean)) <= 2:  # Allow 1-2 char difference (typos)
        char_overlap = len(set(query_clean) & set(target_clean))
        char_total = len(set(query_clean) | set(target_clean))
        if char_total > 0:
            char_similarity = char_overlap / char_total
            if char_similarity > 0.7:  # High character overlap suggests typo
                # Use sequence matcher for final score
                similarity = SequenceMatcher(None, query_clean, target_clean).ratio()
                return max(similarity, char_similarity * 0.9)
    
    # Sequence matcher (improved with cleaned strings)
    similarity = SequenceMatcher(None, query_clean, target_clean).ratio()
    
    # Also try original strings (in case cleaning removed important info)
    similarity_orig = SequenceMatcher(None, query_lower, target_lower).ratio()
    similarity = max(similarity, similarity_orig)
    
    # Boost score for short strings (more forgiving for short drug names)
    if len(query_clean) <= 5 or len(target_clean) <= 5:
        similarity = min(1.0, similarity * 1.1)
    
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
    Enhanced with better class detection for all drug classes
    
    Args:
        drug_name: Drug name
    
    Returns:
        List of drug class names
    """
    classes = []
    drug_normalized = normalize_drug_name(drug_name)
    
    # Check direct class mappings (case-insensitive)
    for class_name, drugs_in_class in DRUG_CLASS_MAPPINGS.items():
        # Check exact match
        if drug_normalized in drugs_in_class:
            classes.append(class_name)
        # Check case-insensitive match
        elif drug_normalized.lower() in [d.lower() for d in drugs_in_class]:
            classes.append(class_name)
    
    # Check DRUG_GROUPS and map to classes
    if _DRUG_DB_LOADED and DRUG_GROUPS:
        for group_name, drugs_in_group in DRUG_GROUPS.items():
            if drug_normalized in drugs_in_group or drug_normalized.lower() in [d.lower() for d in drugs_in_group]:
                # Map group names to class names
                if group_name == "Cardiovascular":
                    # Check specific cardiovascular classes
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("ACE Inhibitor", []):
                        classes.append("ACE Inhibitor")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("ARB", []):
                        classes.append("ARB")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Beta-blocker", []):
                        classes.append("Beta-blocker")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("CCB", []):
                        classes.append("CCB")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Statins", []):
                        classes.append("Statins")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Anticoagulant", []):
                        classes.append("Anticoagulant")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Antiplatelet", []):
                        classes.append("Antiplatelet")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Digoxin", []):
                        classes.append("Digoxin")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Loop Diuretic", []):
                        classes.append("Loop Diuretic")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Thiazide Diuretic", []):
                        classes.append("Thiazide Diuretic")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Potassium-sparing Diuretic", []):
                        classes.append("Potassium-sparing Diuretic")
                elif group_name == "Diabetes":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Sulfonylurea", []):
                        classes.append("Sulfonylurea")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("SGLT2 Inhibitor", []):
                        classes.append("SGLT2 Inhibitor")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("DPP-4 Inhibitor", []):
                        classes.append("DPP-4 Inhibitor")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("GLP-1 Agonist", []):
                        classes.append("GLP-1 Agonist")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("TZD", []):
                        classes.append("TZD")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Metformin", []):
                        classes.append("Metformin")
                elif group_name == "Gastrointestinal":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("PPI", []):
                        classes.append("PPI")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("H2 Blockers", []):
                        classes.append("H2 Blockers")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Antacid", []):
                        classes.append("Antacid")
                elif group_name == "Analgesics":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("NSAID", []):
                        classes.append("NSAID")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Opioid", []):
                        classes.append("Opioid")
                elif group_name == "Neurology/Psychiatry":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("SSRI", []):
                        classes.append("SSRI")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("SNRI", []):
                        classes.append("SNRI")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("TCA", []):
                        classes.append("TCA")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("MAOI", []):
                        classes.append("MAOI")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Anticonvulsant", []):
                        classes.append("Anticonvulsant")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Antipsychotic", []):
                        classes.append("Antipsychotic")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Benzodiazepine", []):
                        classes.append("Benzodiazepine")
                elif group_name == "Antibiotics" or group_name == "Anti-infectives":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Penicillin", []):
                        classes.append("Penicillin")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Cephalosporin", []):
                        classes.append("Cephalosporin")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Macrolide", []):
                        classes.append("Macrolide")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Quinolone", []):
                        classes.append("Quinolone")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Tetracycline", []):
                        classes.append("Tetracycline")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Aminoglycoside", []):
                        classes.append("Aminoglycoside")
                elif group_name == "Oncology":
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Chemotherapy", []):
                        classes.append("Chemotherapy")
                    if drug_normalized in DRUG_CLASS_MAPPINGS.get("Methotrexate", []):
                        classes.append("Methotrexate")
    
    return list(set(classes))  # Remove duplicates


def normalize_drug_name(drug_name: str, use_fuzzy: bool = True) -> str:
    """
    Normalize drug name to canonical form with fuzzy matching support
    Enhanced with better Vietnamese name and brand name handling
    
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
    
    # 1. Check exact match in DRUG_INTERACTIONS keys (case-insensitive)
    for (d1, d2) in DRUG_INTERACTIONS.keys():
        if drug_original.lower() == d1.lower() or drug_original.lower() == d2.lower():
            return d1 if drug_original.lower() == d1.lower() else d2
    
    # 2. Check aliases (case-insensitive, partial match)
    for canonical, aliases in DRUG_ALIASES.items():
        # Exact match in aliases
        if drug_lower in [a.lower() for a in aliases]:
            return canonical
        # Partial match (contains)
        for alias in aliases:
            if drug_lower in alias.lower() or alias.lower() in drug_lower:
                if len(alias) >= 4:  # Only if meaningful length
                    return canonical
    
    # 3. If exact match with canonical name (case-insensitive)
    for canonical in DRUG_ALIASES.keys():
        if drug_lower == canonical.lower():
            return canonical
    
    # 4. Check in drug database (exact match, case-insensitive)
    if _DRUG_DB_LOADED and DRUG_DATABASE:
        # Exact match
        if drug_original in DRUG_DATABASE:
            return drug_original
        
        # Case-insensitive match
        for db_drug_name in DRUG_DATABASE.keys():
            if db_drug_name.lower() == drug_lower:
                return db_drug_name
        
        # Check Vietnamese names (exact and partial)
        for db_drug_name, drug_data in DRUG_DATABASE.items():
            if 'vietnamese_name' in drug_data:
                vn_name = drug_data['vietnamese_name']
                if vn_name.lower() == drug_lower:
                    return db_drug_name
                # Partial match for Vietnamese names
                if drug_lower in vn_name.lower() or vn_name.lower() in drug_lower:
                    if len(vn_name) >= 3:  # Only if meaningful length
                        return db_drug_name
    
    # 5. Fuzzy matching (if enabled) - improved threshold
    if use_fuzzy and _DRUG_DB_LOADED:
        fuzzy_match = _find_best_drug_match(drug_original, threshold=0.70)  # Lowered threshold for better matching
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
        return normalize_interaction_record(interaction, drug1, drug2)
    
    interaction = DRUG_INTERACTIONS.get((norm2, norm1))
    if interaction:
        return normalize_interaction_record(interaction, drug1, drug2)
    
    # 2. Check class-based interactions
    if check_classes:
        # Get classes for both drugs
        classes1 = get_drug_classes(norm1)
        classes2 = get_drug_classes(norm2)
        
        # Check drug1 vs drug2's classes
        for class2 in classes2:
                interaction = DRUG_INTERACTIONS.get((norm1, class2))
                if interaction:
                    return normalize_interaction_record(interaction, drug1, drug2)
                interaction = DRUG_INTERACTIONS.get((class2, norm1))
                if interaction:
                    return normalize_interaction_record(interaction, drug1, drug2)
        
        # Check drug2 vs drug1's classes
        for class1 in classes1:
                interaction = DRUG_INTERACTIONS.get((norm2, class1))
                if interaction:
                    return normalize_interaction_record(interaction, drug1, drug2)
                interaction = DRUG_INTERACTIONS.get((class1, norm2))
                if interaction:
                    return normalize_interaction_record(interaction, drug1, drug2)
        
        # Check class1 vs class2
        for class1 in classes1:
            for class2 in classes2:
                interaction = DRUG_INTERACTIONS.get((class1, class2))
                if interaction:
                    return normalize_interaction_record(interaction, drug1, drug2)
                interaction = DRUG_INTERACTIONS.get((class2, class1))
                if interaction:
                    return normalize_interaction_record(interaction, drug1, drug2)
    
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
    
    # Sort by severity (Contraindicated > Major > Moderate > Minor > others)
    severity_order = {
        "Contraindicated": 0,
        SEVERITY_MAJOR: 1,
        SEVERITY_MODERATE: 2,
        SEVERITY_MINOR: 3,
    }
    interactions.sort(key=lambda x: severity_order.get(x.get('severity'), 9))
    
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


def validate_interaction_dataset() -> Dict[str, List[str]]:
    """Validate the interaction dictionary against the canonical schema."""
    return validate_interactions_db(DRUG_INTERACTIONS)

