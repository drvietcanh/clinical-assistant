"""
Drug Interaction Database
Contains clinically significant drug-drug interactions
"""

# Interaction severity levels
SEVERITY_MAJOR = "Major"        # Avoid combination - life-threatening
SEVERITY_MODERATE = "Moderate"  # Monitor closely
SEVERITY_MINOR = "Minor"        # Minimal clinical significance

# Drug Interaction Database
# Format: (Drug1, Drug2): {severity, effect, mechanism, management, references}
DRUG_INTERACTIONS = {
    
    # ==================== MAJOR INTERACTIONS ====================
    
    ("Warfarin", "Aspirin"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
        "mechanism": "Cả hai đều ức chế tiểu cầu và đông máu. Aspirin ức chế COX-1 → Giảm TXA2 → Giảm kết tập tiểu cầu. Warfarin ức chế vitamin K → Giảm yếu tố đông máu II, VII, IX, X.",
        "management": "TRÁNH dùng chung nếu có thể. Nếu bắt buộc: Giảm liều Warfarin, theo dõi INR sát (mỗi tuần), theo dõi dấu hiệu chảy máu (phân đen, nôn máu, chảy máu nướu răng).",
        "references": ["UpToDate", "Micromedex", "FDA Label"]
    },
    
    ("Warfarin", "NSAIDs"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng nguy cơ chảy máu tiêu hóa và chảy máu nghiêm trọng",
        "mechanism": "NSAIDs ức chế COX → Giảm prostaglandin bảo vệ niêm mạc dạ dày + Ức chế tiểu cầu. Warfarin tăng thời gian đông máu.",
        "management": "Tránh NSAIDs. Dùng Acetaminophen thay thế cho giảm đau. Nếu bắt buộc dùng NSAIDs: Dùng thời gian ngắn nhất, liều thấp nhất, kèm PPI bảo vệ dạ dày, theo dõi INR.",
        "references": ["UpToDate", "Micromedex"]
    },
    
    ("Metformin", "Iodinated Contrast"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Nguy cơ toan lactic (Lactic acidosis) - Có thể tử vong",
        "mechanism": "Thuốc cản quang có iodine có thể gây suy thận cấp → Giảm thải Metformin → Tích lũy Metformin → Toan lactic.",
        "management": "NGỪNG Metformin trước chụp CT/MRI có thuốc cản quang. Ngừng ít nhất 48h trước. Kiểm tra chức năng thận sau chụp. Chỉ dùng lại Metformin khi chức năng thận bình thường (ít nhất 48-72h sau chụp).",
        "references": ["FDA Label", "ACR Guidelines"]
    },
    
    ("ACE Inhibitors", "Spironolactone"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng kali máu nghiêm trọng (Hyperkalemia) - Nguy cơ rối loạn nhịp tim",
        "mechanism": "ACE-I giảm Aldosterone → Giữ K+. Spironolactone chống Aldosterone → Giữ K+. Tác dụng cộng hưởng.",
        "management": "Theo dõi K+ máu sát (mỗi 1-2 tuần khi bắt đầu, sau đó mỗi tháng). Nếu K+ >5.5 mEq/L: Giảm liều hoặc ngừng một trong hai thuốc. Tránh thực phẩm giàu K+ (chuối, cam, cà chua). Cân nhắc dùng Furosemide thay Spironolactone.",
        "references": ["UpToDate", "RALES Trial"]
    },
    
    ("Statins", "Gemfibrozil"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng nguy cơ myopathy và rhabdomyolysis (Tiêu cơ vân) nghiêm trọng",
        "mechanism": "Gemfibrozil ức chế UGT1A1 và OATP1B1 → Tăng nồng độ statin → Độc cơ.",
        "management": "TRÁNH dùng chung Gemfibrozil với bất kỳ statin nào. Nếu cần fibrate: Dùng Fenofibrate (ít tương tác hơn). Theo dõi CK, triệu chứng đau cơ, nước tiểu sẫm màu.",
        "references": ["FDA Black Box Warning", "ACC/AHA Guidelines"]
    },
    
    ("MAOIs", "SSRIs"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Hội chứng Serotonin (Serotonin syndrome) - Có thể tử vong",
        "mechanism": "MAOIs ức chế phân hủy serotonin. SSRIs tăng serotonin. → Tích lũy serotonin quá mức.",
        "management": "CHỐNG CHỈ ĐỊNH tuyệt đối. Ngừng MAOI ít nhất 14 ngày trước khi bắt đầu SSRI. Ngừng SSRI ít nhất 5 tuần (Fluoxetine) hoặc 2 tuần (SSRI khác) trước khi bắt đầu MAOI.",
        "references": ["FDA Contraindication", "Sternbach Criteria"]
    },
    
    ("Digoxin", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng nồng độ Digoxin → Độc Digoxin (buồn nôn, rối loạn nhịp, rối loạn thị giác)",
        "mechanism": "Amiodarone ức chế P-glycoprotein → Giảm thải Digoxin qua thận và ruột.",
        "management": "Giảm liều Digoxin 50% khi bắt đầu Amiodarone. Theo dõi nồng độ Digoxin (mục tiêu 0.5-0.9 ng/mL). Theo dõi triệu chứng độc Digoxin, ECG, K+ máu.",
        "references": ["UpToDate", "ACC/AHA AF Guidelines"]
    },
    
    ("Methotrexate", "NSAIDs"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng độc tính Methotrexate (suy tủy, độc gan, độc thận)",
        "mechanism": "NSAIDs giảm thải Methotrexate qua thận (ức chế bài tiết ống thận). NSAIDs cũng giảm GFR → Giảm lọc Methotrexate.",
        "management": "Tránh NSAIDs khi dùng Methotrexate liều cao (>20mg/tuần hoặc liều hóa trị). Với liều thấp (RA): Có thể dùng NSAIDs nhưng theo dõi CBC, AST/ALT, Cr thường xuyên. Dùng Acetaminophen thay thế nếu có thể.",
        "references": ["FDA Label", "ACR Guidelines"]
    },
    
    ("Theophylline", "Ciprofloxacin"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Tăng nồng độ Theophylline → Độc tính (co giật, rối loạn nhịp)",
        "mechanism": "Ciprofloxacin ức chế CYP1A2 → Giảm chuyển hóa Theophylline.",
        "management": "Giảm liều Theophylline 50% khi bắt đầu Ciprofloxacin. Theo dõi nồng độ Theophylline (mục tiêu 5-15 mcg/mL). Cân nhắc dùng quinolone khác (Levofloxacin ít tương tác hơn).",
        "references": ["FDA Label", "Micromedex"]
    },
    
    ("Clopidogrel", "Omeprazole"): {
        "severity": SEVERITY_MAJOR,
        "effect": "Giảm hiệu quả Clopidogrel → Tăng nguy cơ nhồi máu cơ tim, đột quỵ",
        "mechanism": "Omeprazole ức chế CYP2C19 → Giảm chuyển hóa Clopidogrel thành dạng hoạt động.",
        "management": "TRÁNH Omeprazole và Esomeprazole. Nếu cần PPI: Dùng Pantoprazole (ít tương tác). Hoặc dùng H2 blocker (Famotidine). Uống cách xa nhau ít nhất 12h nếu bắt buộc dùng.",
        "references": ["FDA Warning", "ACC/AHA Guidelines"]
    },
    
    # ==================== MODERATE INTERACTIONS ====================
    
    ("Levothyroxine", "Calcium"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Giảm hấp thu Levothyroxine → Giảm hiệu quả điều trị suy giáp",
        "mechanism": "Calcium chelate với Levothyroxine trong đường tiêu hóa → Giảm hấp thu.",
        "management": "Uống cách xa nhau ít nhất 4 giờ. Levothyroxine lúc đói (sáng sớm), Calcium sau ăn hoặc tối.",
        "references": ["FDA Label", "ATA Guidelines"]
    },
    
    ("Levothyroxine", "Iron"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Giảm hấp thu Levothyroxine",
        "mechanism": "Tương tự Calcium - Iron chelate với Levothyroxine.",
        "management": "Uống cách xa nhau ít nhất 4 giờ.",
        "references": ["FDA Label"]
    },
    
    ("Levothyroxine", "PPIs"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Giảm hấp thu Levothyroxine (cần môi trường acid)",
        "mechanism": "PPIs tăng pH dạ dày → Giảm hòa tan Levothyroxine.",
        "management": "Theo dõi TSH thường xuyên hơn. Có thể cần tăng liều Levothyroxine. Uống cách xa nhau nếu có thể.",
        "references": ["Endocrine Practice"]
    },
    
    ("Statins", "Fibrates"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Tăng nguy cơ myopathy (nhẹ hơn so với Gemfibrozil)",
        "mechanism": "Cả hai đều có nguy cơ myopathy. Tác dụng cộng hưởng.",
        "management": "Nếu dùng chung: Dùng Fenofibrate (an toàn hơn Gemfibrozil). Theo dõi CK, triệu chứng đau cơ. Giáo dục bệnh nhân về dấu hiệu myopathy.",
        "references": ["ACC/AHA Guidelines"]
    },
    
    ("Metformin", "Alcohol"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Tăng nguy cơ toan lactic, hạ đường huyết",
        "mechanism": "Alcohol ức chế gluconeogenesis + Metformin giảm sản xuất glucose gan.",
        "management": "Tránh uống rượu nhiều. Nếu uống: Uống vừa phải (1-2 đơn vị/ngày), uống kèm thức ăn.",
        "references": ["ADA Guidelines"]
    },
    
    ("ACE Inhibitors", "NSAIDs"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Giảm hiệu quả hạ huyết áp của ACE-I, tăng nguy cơ suy thận cấp",
        "mechanism": "NSAIDs ức chế prostaglandin → Co mạch thận → Giảm GFR. ACE-I giãn tiểu động mạch thận → Giảm GFR. Tác dụng cộng hưởng.",
        "management": "Tránh NSAIDs nếu có thể. Dùng Acetaminophen thay thế. Nếu bắt buộc: Theo dõi huyết áp, Cr, K+ thường xuyên. Dùng liều thấp nhất, thời gian ngắn nhất.",
        "references": ["JNC 8", "KDIGO Guidelines"]
    },
    
    ("Amlodipine", "Simvastatin"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Tăng nồng độ Simvastatin → Tăng nguy cơ myopathy",
        "mechanism": "Amlodipine ức chế CYP3A4 → Giảm chuyển hóa Simvastatin.",
        "management": "Giới hạn liều Simvastatin ≤20mg/ngày khi dùng với Amlodipine. Hoặc chuyển sang statin khác (Atorvastatin, Rosuvastatin ít tương tác hơn).",
        "references": ["FDA Label"]
    },
    
    ("Metformin", "Contrast Dye"): {
        "severity": SEVERITY_MODERATE,
        "effect": "Nguy cơ suy thận và toan lactic",
        "mechanism": "Contrast có thể gây suy thận → Tích lũy Metformin.",
        "management": "Ngừng Metformin 48h trước và sau chụp. Kiểm tra Cr sau chụp.",
        "references": ["ACR Guidelines"]
    },
    
    # ==================== MINOR INTERACTIONS ====================
    
    ("Levothyroxine", "Coffee"): {
        "severity": SEVERITY_MINOR,
        "effect": "Giảm hấp thu Levothyroxine nhẹ",
        "mechanism": "Coffee có thể ảnh hưởng hấp thu.",
        "management": "Uống Levothyroxine với nước lọc. Tránh coffee trong 30-60 phút sau uống thuốc.",
        "references": ["Thyroid Journal"]
    },
    
    ("Antibiotics", "Oral Contraceptives"): {
        "severity": SEVERITY_MINOR,
        "effect": "Giảm hiệu quả thuốc tránh thai (chủ yếu với Rifampin)",
        "mechanism": "Một số kháng sinh (Rifampin) cảm ứng CYP3A4 → Tăng chuyển hóa estrogen.",
        "management": "Dùng thêm biện pháp tránh thai cơ học (bao cao su) khi dùng kháng sinh. Đặc biệt quan trọng với Rifampin.",
        "references": ["CDC Guidelines"]
    },
}


# Helper functions
def get_interaction(drug1: str, drug2: str):
    """
    Get interaction between two drugs
    
    Args:
        drug1: First drug name
        drug2: Second drug name
    
    Returns:
        Interaction dict or None
    """
    # Try both orders
    pair1 = (drug1, drug2)
    pair2 = (drug2, drug1)
    
    return DRUG_INTERACTIONS.get(pair1) or DRUG_INTERACTIONS.get(pair2)


def get_all_interactions_for_drug(drug_name: str):
    """
    Get all interactions for a specific drug
    
    Args:
        drug_name: Drug name
    
    Returns:
        List of (other_drug, interaction) tuples
    """
    interactions = []
    
    for (drug1, drug2), interaction in DRUG_INTERACTIONS.items():
        if drug1 == drug_name:
            interactions.append((drug2, interaction))
        elif drug2 == drug_name:
            interactions.append((drug1, interaction))
    
    return interactions


def get_interactions_by_severity(severity: str):
    """
    Get all interactions of a specific severity
    
    Args:
        severity: "Major", "Moderate", or "Minor"
    
    Returns:
        List of ((drug1, drug2), interaction) tuples
    """
    return [
        (pair, interaction)
        for pair, interaction in DRUG_INTERACTIONS.items()
        if interaction['severity'] == severity
    ]


# Statistics
def get_interaction_statistics():
    """Get statistics about interaction database"""
    total = len(DRUG_INTERACTIONS)
    major = len(get_interactions_by_severity(SEVERITY_MAJOR))
    moderate = len(get_interactions_by_severity(SEVERITY_MODERATE))
    minor = len(get_interactions_by_severity(SEVERITY_MINOR))
    
    # Get unique drugs
    unique_drugs = set()
    for drug1, drug2 in DRUG_INTERACTIONS.keys():
        unique_drugs.add(drug1)
        unique_drugs.add(drug2)
    
    return {
        'total_interactions': total,
        'major': major,
        'moderate': moderate,
        'minor': minor,
        'unique_drugs': len(unique_drugs),
        'drugs_with_interactions': sorted(list(unique_drugs))
    }


__all__ = [
    'DRUG_INTERACTIONS',
    'SEVERITY_MAJOR',
    'SEVERITY_MODERATE',
    'SEVERITY_MINOR',
    'get_interaction',
    'get_all_interactions_for_drug',
    'get_interactions_by_severity',
    'get_interaction_statistics'
]
