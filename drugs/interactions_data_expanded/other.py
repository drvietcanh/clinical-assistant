"""
Other Drug Interactions
Expanded database for other drug class interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

OTHER_INTERACTIONS = {
    # ========== CORTICOSTEROIDS ==========
    
    ("Corticosteroid", "NSAID"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ xuất huyết dạ dày-ruột",
        "description": "Tăng nguy cơ xuất huyết dạ dày-ruột nặng",
        "management": "Thận trọng khi dùng chung. Dùng PPI bảo vệ dạ dày",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid có thể tăng hoặc giảm tác dụng warfarin",
        "description": "Tác dụng không dự đoán được",
        "management": "Theo dõi INR khi bắt đầu/dừng corticosteroid",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Insulin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid làm tăng đường huyết, giảm tác dụng insulin",
        "description": "Giảm hiệu quả insulin",
        "management": "Tăng liều insulin khi dùng corticosteroid. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Antidiabetic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid làm tăng đường huyết",
        "description": "Giảm hiệu quả thuốc hạ đường huyết",
        "management": "Tăng liều thuốc hạ đường huyết. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid gây giữ natri, giảm tác dụng lợi tiểu",
        "description": "Giảm hiệu quả lợi tiểu",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Corticosteroid", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Corticosteroid gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi kali máu và nồng độ digoxin",
        "references": "Micromedex"
    },
    
    # ========== ANTIHISTAMINES ==========
    
    ("Diphenhydramine", "Benzodiazepine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng an thần, ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp",
        "management": "Tránh dùng chung. Nếu cần: dùng liều thấp, theo dõi sát",
        "references": "Micromedex"
    },
    
    ("Diphenhydramine", "Alcohol"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ quá mức, suy hô hấp",
        "management": "Tránh uống rượu khi dùng diphenhydramine",
        "references": "Micromedex"
    },
    
    ("Diphenhydramine", "Opioid"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ suy hô hấp",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Loratadine", "Ketoconazole"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ketoconazole ức chế chuyển hóa loratadine",
        "description": "Tăng nồng độ loratadine",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    # ========== ANTICONVULSANTS ==========
    
    ("Phenytoin", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phenytoin cảm ứng CYP2C9, giảm tác dụng warfarin. Cũng có thể ức chế trong một số trường hợp",
        "description": "Tương tác phức tạp, có thể tăng hoặc giảm tác dụng warfarin",
        "clinical_significance": "Tương tác không dự đoán được. INR có thể dao động.",
        "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin dựa trên INR",
        "references": "Micromedex"
    },
    
    ("Phenytoin", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Phenytoin cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Phenytoin", "Folic Acid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Folic acid có thể giảm nồng độ phenytoin",
        "description": "Giảm hiệu quả phenytoin",
        "management": "Theo dõi nồng độ phenytoin khi bổ sung folic acid",
        "references": "Micromedex"
    },
    
    ("Carbamazepine", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Carbamazepine cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tăng liều warfarin khi bắt đầu carbamazepine. Theo dõi INR thường xuyên",
        "references": "Micromedex"
    },
    
    ("Carbamazepine", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Carbamazepine cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Carbamazepine", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa carbamazepine, tăng nồng độ carbamazepine",
        "description": "Tăng nguy cơ độc tính carbamazepine",
        "management": "Theo dõi nồng độ carbamazepine, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Valproic Acid", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Valproic acid có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng valproic acid",
        "references": "Micromedex"
    },
    
    ("Valproic Acid", "Aspirin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ xuất huyết",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },

    ("Levetiracetam", "Warfarin"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Tương tác nhỏ, không đáng kể",
        "description": "Tương tác tối thiểu",
        "management": "Theo dõi INR nếu cần",
        "references": "Micromedex"
    },
    
    ("Topiramate", "Oral Contraceptive"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Topiramate có thể giảm hiệu quả tránh thai",
        "description": "Giảm hiệu quả tránh thai",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung",
        "references": "Micromedex"
    },
    
    ("Lamotrigine", "Oral Contraceptive"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Oral contraceptive giảm nồng độ lamotrigine",
        "description": "Giảm hiệu quả lamotrigine",
        "management": "Tăng liều lamotrigine khi dùng oral contraceptive",
        "references": "Micromedex"
    },
    
    ("Valproic Acid", "Lamotrigine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Valproic acid tăng nồng độ lamotrigine",
        "description": "Tăng nguy cơ phát ban nặng, hội chứng Stevens-Johnson",
        "management": "Giảm liều lamotrigine khi dùng valproic acid",
        "references": "FDA, Micromedex"
    },
    
    ("Phenytoin", "Valproic Acid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tương tác phức tạp, có thể tăng hoặc giảm nồng độ",
        "description": "Tác dụng không dự đoán được",
        "management": "Theo dõi nồng độ cả hai thuốc",
        "references": "Micromedex"
    },
    
    # ========== ORAL CONTRACEPTIVES ==========
    
    ("Oral Contraceptive", "Antibiotics"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Một số kháng sinh làm giảm hiệu quả tránh thai",
        "description": "Rifampin, một số kháng sinh phổ rộng có thể giảm hiệu quả",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung khi dùng kháng sinh",
        "references": "Clinical Pharmacology"
    },
    
    ("Oral Contraceptive", "Rifampin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Rifampin cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "clinical_significance": "Hiệu quả tránh thai giảm đáng kể. Nguy cơ có thai cao.",
        "management": "Khuyên dùng biện pháp tránh thai bổ sung (barrier method) hoặc chuyển sang biện pháp khác",
        "references": "Micromedex"
    },
    
    ("Oral Contraceptive", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng oral contraceptive",
        "references": "Micromedex"
    },
    
    # ========== THYROID HORMONES ==========
    
    ("Thyroid Hormone", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Thyroid hormone tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu/dừng thyroid hormone",
        "references": "Micromedex"
    },
    
    ("Thyroid Hormone", "Cholestyramine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 4 giờ",
        "references": "Micromedex"
    },
    
    ("Thyroid Hormone", "Iron"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Iron giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Thyroid Hormone", "Calcium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Calcium giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== THEOPHYLLINE ==========
    
    ("Theophylline", "Ciprofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ciprofloxacin ức chế chuyển hóa theophylline, tăng nồng độ theophylline",
        "description": "Tăng nguy cơ ngộ độc theophylline (co giật, rối loạn nhịp tim)",
        "clinical_significance": "Nồng độ theophylline có thể tăng 2-3 lần. Nguy cơ co giật, rối loạn nhịp tim, tử vong.",
        "management": "Giảm liều theophylline 30-50%. Theo dõi nồng độ theophylline. Cân nhắc dùng levofloxacin thay thế",
        "alternatives": {
            "for_ciprofloxacin": ["Levofloxacin", "Moxifloxacin"]
        },
        "references": "Micromedex"
    },
    
    ("Theophylline", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Cimetidine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cimetidine ức chế chuyển hóa theophylline",
        "description": "Tăng nồng độ theophylline",
        "management": "Theo dõi nồng độ theophylline, cân nhắc giảm liều",
        "references": "Micromedex"
    },
    
    ("Theophylline", "Rifampin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng chuyển hóa theophylline",
        "description": "Giảm nồng độ theophylline",
        "management": "Tăng liều theophylline khi dùng rifampin. Theo dõi nồng độ theophylline",
        "references": "Micromedex"
    },
    
    # ========== IRON ==========
    
    ("Iron", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với quinolone, giảm hấp thu",
        "description": "Giảm đáng kể hấp thu quinolone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Iron", "Tetracycline"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với tetracycline, giảm hấp thu",
        "description": "Giảm hấp thu tetracycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Iron", "Thyroid Hormone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Iron giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Iron", "Levofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Iron chelate với levofloxacin, giảm hấp thu",
        "description": "Giảm hấp thu levofloxacin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== CALCIUM ==========
    
    ("Calcium", "Quinolone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Calcium chelate với quinolone, giảm hấp thu",
        "description": "Giảm hấp thu quinolone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Calcium", "Tetracycline"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Calcium chelate với tetracycline, giảm hấp thu",
        "description": "Giảm hấp thu tetracycline",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Calcium", "Thyroid Hormone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Calcium giảm hấp thu thyroid hormone",
        "description": "Giảm hiệu quả thyroid hormone",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    ("Calcium", "Ceftriaxone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ceftriaxone kết hợp với calcium tạo kết tủa không tan",
        "description": "Nguy cơ kết tủa trong phổi, thận, có thể tử vong",
        "management": "KHÔNG trộn ceftriaxone với calcium trong cùng một đường truyền. Cách xa ít nhất 48 giờ nếu dùng IV calcium",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    # ========== HERBAL/SUPPLEMENTS ==========
    
    ("Ginkgo Biloba", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ginkgo có thể tăng tác dụng chống đông",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Tránh dùng chung. Theo dõi INR nếu cần dùng",
        "references": "Micromedex"
    },
    
    ("Ginseng", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Ginseng có thể giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung. Theo dõi INR nếu cần dùng",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng CYP2C9, giảm tác dụng warfarin",
        "description": "Giảm hiệu quả chống đông",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "Oral Contraceptive"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "St. John's Wort cảm ứng chuyển hóa estrogen, giảm hiệu quả tránh thai",
        "description": "Giảm đáng kể hiệu quả tránh thai",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("St. John's Wort", "SSRI"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ hội chứng serotonin",
        "description": "Tăng nguy cơ hội chứng serotonin",
        "management": "Tránh dùng chung",
        "references": "Micromedex"
    },
    
    ("Vitamin K", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Vitamin K là chất đối kháng của warfarin",
        "description": "Giảm hiệu quả chống đông",
        "clinical_significance": "INR có thể giảm đáng kể. Nguy cơ huyết khối tái phát.",
        "management": "Tránh bổ sung vitamin K không cần thiết. Nếu cần: điều chỉnh liều warfarin và theo dõi INR",
        "references": "Micromedex"
    },

    # ========== BRONCHODILATORS ==========
    
    ("Albuterol", "Beta-blocker"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Beta-blocker đối kháng tác dụng của albuterol",
        "description": "Giảm hiệu quả điều trị hen suyễn",
        "management": "Tránh dùng beta-blocker không chọn lọc ở bệnh nhân hen",
        "references": "Micromedex"
    },
    
    ("Salmeterol", "Beta-blocker"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Beta-blocker đối kháng tác dụng của salmeterol",
        "description": "Giảm hiệu quả điều trị",
        "management": "Tránh dùng beta-blocker không chọn lọc",
        "references": "Micromedex"
    },
    
    ("Formoterol", "Beta-blocker"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Beta-blocker đối kháng tác dụng của formoterol",
        "description": "Giảm hiệu quả điều trị",
        "management": "Tránh dùng beta-blocker không chọn lọc",
        "references": "Micromedex"
    },
    
    # ========== MUSCLE RELAXANTS ==========
    
    ("Baclofen", "Opioid"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế thần kinh trung ương",
        "description": "Tăng nguy cơ buồn ngủ, suy hô hấp",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Tizanidine", "Ciprofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ciprofloxacin ức chế chuyển hóa tizanidine",
        "description": "Tăng nồng độ tizanidine, tăng nguy cơ hạ huyết áp",
        "management": "Tránh dùng chung. Nếu cần: giảm liều tizanidine",
        "references": "FDA, Micromedex"
    },
    
    ("Tizanidine", "CYP1A2 Inhibitor"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "CYP1A2 inhibitor tăng nồng độ tizanidine",
        "description": "Tăng nguy cơ hạ huyết áp",
        "management": "Tránh dùng chung hoặc giảm liều tizanidine",
        "references": "Micromedex"
    },
    
    # ========== ANTIEMETICS ==========
    
    ("Ondansetron", "QT Prolonging Drug"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ kéo dài QT interval",
        "description": "Tăng nguy cơ rối loạn nhịp tim",
        "management": "Thận trọng khi dùng chung. Theo dõi ECG",
        "references": "FDA, Micromedex"
    },
    
    ("Metoclopramide", "Antipsychotic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ rối loạn vận động",
        "description": "Tăng nguy cơ rối loạn vận động ngoại tháp",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },
    
    ("Metoclopramide", "Dopamine Antagonist"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng nguy cơ rối loạn vận động",
        "description": "Tăng nguy cơ rối loạn vận động",
        "management": "Thận trọng khi dùng chung",
        "references": "Micromedex"
    },

    # ========== LAXATIVES ==========
    
    ("Laxative", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Laxative có thể giảm hấp thu digoxin",
        "description": "Giảm hiệu quả digoxin",
        "management": "Cách xa thời gian dùng. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Laxative", "Oral Medication"): {
        "severity": SEVERITY_MINOR,
        "mechanism": "Có thể giảm hấp thu thuốc uống",
        "description": "Giảm hấp thu một số thuốc",
        "management": "Cách xa thời gian dùng thuốc khác",
        "references": "Micromedex"
    },

    # ========== GOUT AGENTS (General) ==========

    ("Colchicine", "Clarithromycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Clarithromycin ức chế chuyển hóa colchicine",
        "description": "Tăng nồng độ colchicine, tăng nguy cơ độc tính",
        "management": "Tránh dùng chung. Nếu cần: giảm liều colchicine",
        "references": "FDA, Micromedex"
    },
    
    ("Colchicine", "Cyclosporine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Cyclosporine ức chế chuyển hóa colchicine",
        "description": "Tăng nồng độ colchicine",
        "management": "Tránh dùng chung hoặc giảm liều colchicine",
        "references": "Micromedex"
    },
    
    ("Allopurinol", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Allopurinol có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi bắt đầu/dừng allopurinol",
        "references": "Micromedex"
    }
}
