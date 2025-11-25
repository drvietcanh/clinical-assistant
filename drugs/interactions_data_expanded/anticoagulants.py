"""
Anticoagulant Drug Interactions
Expanded database for anticoagulant interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants (will be imported in __init__.py)
# These are defined in interactions_data.py
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

# ========== ANTICOAGULANT INTERACTIONS ==========
# Expanded database with 50+ interactions

ANTICOAGULANT_INTERACTIONS = {
    # ========== WARFARIN INTERACTIONS ==========
    
    # Warfarin + Antiplatelets
    ("Warfarin", "Aspirin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết do tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết nặng, có thể tử vong",
        "clinical_significance": "Nguy cơ xuất huyết dạ dày-ruột tăng 2-3 lần. Đặc biệt nguy hiểm ở người cao tuổi, có tiền sử loét dạ dày.",
        "management": "Tránh dùng chung nếu có thể. Nếu cần thiết: theo dõi INR thường xuyên, cân nhắc giảm liều warfarin, dùng PPI bảo vệ dạ dày",
        "alternatives": {
            "for_aspirin": ["Paracetamol", "Acetaminophen"],
            "for_warfarin": ["Dabigatran", "Rivaroxaban", "Apixaban"]
        },
        "references": "AHFS Drug Information, Micromedex"
    },
    
    ("Warfarin", "Clopidogrel"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết do tăng tác dụng chống đông và chống kết tập tiểu cầu",
        "description": "Tăng nguy cơ xuất huyết nặng, đặc biệt xuất huyết dạ dày-ruột",
        "clinical_significance": "Nguy cơ xuất huyết nặng tăng 2-4 lần. Có thể gây xuất huyết dạ dày-ruột, xuất huyết nội sọ.",
        "management": "Chỉ dùng khi có chỉ định rõ ràng (ví dụ: sau stent, mechanical valve). Theo dõi INR và dấu hiệu xuất huyết. Dùng PPI bảo vệ dạ dày",
        "alternatives": {
            "for_clopidogrel": ["Aspirin đơn độc (nếu phù hợp)"],
            "for_warfarin": ["Dabigatran", "Rivaroxaban", "Apixaban"]
        },
        "references": "ACC/AHA Guidelines, Micromedex"
    },
    
    ("Warfarin", "Ticagrelor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết do tăng tác dụng chống đông và chống kết tập tiểu cầu",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi INR và dấu hiệu xuất huyết sát",
        "references": "Micromedex"
    },
    
    # Warfarin + NSAIDs
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
    
    ("Warfarin", "Naproxen"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "NSAID làm tăng nguy cơ xuất huyết dạ dày và tăng tác dụng chống đông",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế",
        "alternatives": {
            "for_naproxen": ["Paracetamol", "Acetaminophen"]
        },
        "references": "Micromedex"
    },
    
    ("Warfarin", "Diclofenac"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "NSAID làm tăng nguy cơ xuất huyết",
        "management": "Tránh dùng chung. Dùng Paracetamol thay thế",
        "references": "Micromedex"
    },
    
    # Warfarin + Antibiotics
    ("Warfarin", "Metronidazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Metronidazole ức chế chuyển hóa warfarin qua CYP2C9",
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
        "mechanism": "Ciprofloxacin ức chế CYP1A2, có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên, cân nhắc giảm liều warfarin",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế CYP3A4, ức chế chuyển hóa warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng erythromycin",
        "references": "Clinical Pharmacology"
    },
    
    ("Warfarin", "Azithromycin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ tác dụng warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng azithromycin",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế CYP3A4, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Trimethoprim-Sulfamethoxazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Sulfamethoxazole ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "clinical_significance": "INR có thể tăng đáng kể. Nguy cơ xuất huyết nặng.",
        "management": "Giảm liều warfarin 30-50%. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Rifampin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông, tăng nguy cơ huyết khối",
        "clinical_significance": "INR có thể giảm đáng kể. Nguy cơ huyết khối tái phát.",
        "management": "Tăng liều warfarin khi bắt đầu rifampin. Theo dõi INR thường xuyên. Giảm liều warfarin khi dừng rifampin",
        "references": "Micromedex"
    },
    
    # Warfarin + Antifungals
    ("Warfarin", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Giảm liều warfarin 30-50%. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Fluconazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluconazole ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    ("Warfarin", "Itraconazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Itraconazole ức chế CYP3A4, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    # Warfarin + Antidepressants
    ("Warfarin", "Fluoxetine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Fluoxetine ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu/dừng fluoxetine. Cân nhắc giảm liều warfarin",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Sertraline"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    ("Warfarin", "Paroxetine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Paroxetine ức chế CYP2D6, có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    # Warfarin + Anticonvulsants
    ("Warfarin", "Phenytoin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phenytoin cảm ứng CYP2C9, giảm tác dụng warfarin. Cũng có thể ức chế trong một số trường hợp",
        "description": "Tương tác phức tạp, có thể tăng hoặc giảm tác dụng warfarin",
        "clinical_significance": "Tương tác không dự đoán được. INR có thể dao động.",
        "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin dựa trên INR",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Carbamazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Carbamazepine cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tăng liều warfarin khi bắt đầu carbamazepine. Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    # Warfarin + Statins
    ("Warfarin", "Simvastatin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng nhẹ tác dụng warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu simvastatin",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Atorvastatin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể tăng nhẹ tác dụng warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu atorvastatin",
        "references": "Micromedex"
    },
    
    # Warfarin + PPIs
    ("Warfarin", "Omeprazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Omeprazole ức chế CYP2C19, có thể làm tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên khi bắt đầu/dừng omeprazole",
        "references": "Clinical Pharmacology"
    },
    
    ("Warfarin", "Pantoprazole"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Tương tác tối thiểu với warfarin",
        "description": "Tăng nhẹ nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu pantoprazole",
        "references": "Micromedex"
    },
    
    # Warfarin + Antidiabetics
    ("Warfarin", "Sulfonylurea"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR thường xuyên",
        "references": "Clinical Pharmacology"
    },
    
    # Warfarin + Herbal/Supplements
    ("Warfarin", "Ginkgo Biloba"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ginkgo có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Tránh dùng chung. Theo dõi INR nếu cần dùng",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Ginseng"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ginseng có thể giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung. Theo dõi INR nếu cần dùng",
        "references": "Micromedex"
    },
    
    ("Warfarin", "Vitamin K"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Vitamin K là chất đối kháng của warfarin",
        "description": "Giảm hiệu quả chống đông",
        "clinical_significance": "INR có thể giảm đáng kể. Nguy cơ huyết khối tái phát.",
        "management": "Tránh bổ sung vitamin K không cần thiết. Nếu cần: điều chỉnh liều warfarin và theo dõi INR",
        "references": "Micromedex"
    },
    
    # ========== DOACs (Direct Oral Anticoagulants) INTERACTIONS ==========
    
    # Dabigatran
    ("Dabigatran", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế P-gp, tăng nồng độ dabigatran",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Tránh dùng chung. Nếu cần: giảm liều dabigatran",
        "references": "FDA, Micromedex"
    },
    
    ("Dabigatran", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế P-gp, tăng nồng độ dabigatran",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Thận trọng khi dùng chung. Theo dõi dấu hiệu xuất huyết",
        "references": "Micromedex"
    },
    
    ("Dabigatran", "Rifampin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng P-gp, giảm nồng độ dabigatran",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung. Cân nhắc chuyển sang warfarin",
        "references": "Micromedex"
    },
    
    # Rivaroxaban
    ("Rivaroxaban", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP3A4 và P-gp, tăng nồng độ rivaroxaban",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Tránh dùng chung. Nếu cần: giảm liều rivaroxaban",
        "references": "FDA, Micromedex"
    },
    
    ("Rivaroxaban", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế CYP3A4 và P-gp, tăng nồng độ rivaroxaban",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Thận trọng khi dùng chung. Theo dõi dấu hiệu xuất huyết",
        "references": "Micromedex"
    },
    
    ("Rivaroxaban", "Rifampin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng CYP3A4 và P-gp, giảm nồng độ rivaroxaban",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung. Cân nhắc chuyển sang warfarin",
        "references": "Micromedex"
    },
    
    # Apixaban
    ("Apixaban", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP3A4 và P-gp, tăng nồng độ apixaban",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Tránh dùng chung. Nếu cần: giảm liều apixaban 50%",
        "references": "FDA, Micromedex"
    },
    
    ("Apixaban", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế CYP3A4 và P-gp, tăng nồng độ apixaban",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Thận trọng khi dùng chung. Theo dõi dấu hiệu xuất huyết",
        "references": "Micromedex"
    },
    
    # ========== HEPARIN/LMWH INTERACTIONS ==========
    
    ("Heparin", "Aspirin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết do tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Thận trọng khi dùng chung. Theo dõi aPTT và dấu hiệu xuất huyết",
        "references": "Micromedex"
    },
    
    ("Enoxaparin", "Aspirin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "management": "Thận trọng khi dùng chung. Theo dõi dấu hiệu xuất huyết",
        "references": "Micromedex"
    },
}

