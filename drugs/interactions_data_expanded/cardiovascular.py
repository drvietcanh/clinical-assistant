"""
Cardiovascular Drug Interactions
Expanded database for cardiovascular drug interactions
Based on Micromedex, Lexicomp, AHFS Drug Information
"""

# Severity constants
SEVERITY_MAJOR = "Major"
SEVERITY_MODERATE = "Moderate"
SEVERITY_MINOR = "Minor"

CARDIOVASCULAR_INTERACTIONS = {
    # ========== ACE INHIBITORS ==========
    
    # ACE Inhibitor + Potassium (already in main file)
    ("ACE Inhibitor", "Potassium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "ACE inhibitor + kali bổ sung có thể gây tăng kali máu nguy hiểm",
        "clinical_significance": "Kali máu có thể tăng >5.5 mEq/L, nguy cơ rối loạn nhịp tim, đặc biệt ở bệnh nhân suy thận.",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu định kỳ",
        "references": "Micromedex"
    },
    
    # ACE Inhibitor + Spironolactone (already in main file)
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
    
    ("ACE Inhibitor", "Eplerenone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu thường xuyên",
        "references": "Micromedex"
    },
    
    ("ACE Inhibitor", "Triamterene"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu",
        "references": "Micromedex"
    },
    
    ("ACE Inhibitor", "Amiloride"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu",
        "references": "Micromedex"
    },
    
    ("ACE Inhibitor", "Lithium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "ACE inhibitor làm giảm đào thải lithium, tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Theo dõi nồng độ lithium khi bắt đầu/dừng ACE inhibitor. Cân nhắc giảm liều lithium",
        "references": "Micromedex"
    },
    
    ("ACE Inhibitor", "NSAID"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID làm giảm tác dụng hạ huyết áp của ACE inhibitor và tăng nguy cơ suy thận",
        "description": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
        "management": "Thận trọng khi dùng chung. Theo dõi huyết áp và chức năng thận",
        "references": "Micromedex"
    },
    
    ("ACE Inhibitor", "Diuretic"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng hạ huyết áp, có thể gây hạ huyết áp quá mức",
        "description": "Tăng nguy cơ hạ huyết áp",
        "management": "Thận trọng khi bắt đầu. Có thể cần giảm liều diuretic",
        "references": "Micromedex"
    },
    
    # ========== ARBs (Angiotensin Receptor Blockers) ==========
    
    ("ARB", "Potassium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "ARB + kali bổ sung có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu định kỳ",
        "references": "Micromedex"
    },
    
    ("ARB", "Spironolactone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu thường xuyên",
        "references": "Micromedex"
    },
    
    ("ARB", "Eplerenone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng nguy cơ tăng kali máu",
        "description": "Có thể gây tăng kali máu nguy hiểm",
        "management": "Thận trọng khi dùng chung. Theo dõi kali máu",
        "references": "Micromedex"
    },
    
    ("ARB", "Lithium"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "ARB có thể tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Theo dõi nồng độ lithium khi dùng ARB",
        "references": "Micromedex"
    },
    
    ("ARB", "NSAID"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "NSAID làm giảm tác dụng hạ huyết áp của ARB và tăng nguy cơ suy thận",
        "description": "Giảm hiệu quả hạ huyết áp, tăng nguy cơ suy thận",
        "management": "Thận trọng khi dùng chung. Theo dõi huyết áp và chức năng thận",
        "references": "Micromedex"
    },
    
    # ========== BETA-BLOCKERS ==========
    
    ("Beta-blocker", "Calcium Channel Blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế tim, có thể gây block nhĩ thất",
        "description": "Tăng nguy cơ block nhĩ thất, suy tim",
        "management": "Thận trọng khi dùng chung. Theo dõi nhịp tim và ECG",
        "references": "Micromedex"
    },
    
    ("Beta-blocker", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế tim, có thể gây block nhĩ thất",
        "description": "Tăng nguy cơ block nhĩ thất",
        "management": "Thận trọng khi dùng chung. Theo dõi nhịp tim",
        "references": "Micromedex"
    },
    
    ("Beta-blocker", "Insulin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Beta-blocker che giấu triệu chứng hạ đường huyết và làm giảm phản ứng phục hồi",
        "description": "Tăng nguy cơ hạ đường huyết nặng",
        "clinical_significance": "Beta-blocker che giấu triệu chứng hạ đường huyết (nhịp tim nhanh, run tay). Bệnh nhân có thể không nhận biết hạ đường huyết.",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết sát. Giáo dục bệnh nhân về triệu chứng hạ đường huyết",
        "references": "Micromedex"
    },
    
    ("Beta-blocker", "Sulfonylurea"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Beta-blocker che giấu triệu chứng hạ đường huyết",
        "description": "Tăng nguy cơ hạ đường huyết nặng",
        "management": "Thận trọng khi dùng chung. Theo dõi đường huyết",
        "references": "Micromedex"
    },
    
    ("Beta-blocker", "Verapamil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế tim, có thể gây block nhĩ thất nặng",
        "description": "Tăng nguy cơ block nhĩ thất, suy tim",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi nhịp tim và ECG sát",
        "references": "Micromedex"
    },
    
    ("Beta-blocker", "Diltiazem"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế tim",
        "description": "Tăng nguy cơ block nhĩ thất",
        "management": "Thận trọng khi dùng chung. Theo dõi nhịp tim",
        "references": "Micromedex"
    },
    
    ("Beta-blocker", "Clonidine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng hạ huyết áp, tăng nguy cơ khi ngừng clonidine đột ngột",
        "description": "Tăng nguy cơ hạ huyết áp, phản ứng cai nghiện",
        "management": "Thận trọng khi dùng chung. Không ngừng clonidine đột ngột",
        "references": "Micromedex"
    },
    
    # ========== CALCIUM CHANNEL BLOCKERS (CCBs) ==========
    
    ("Diltiazem", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Diltiazem ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin, cân nhắc giảm liều digoxin",
        "references": "Micromedex"
    },
    
    ("Verapamil", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Verapamil ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Giảm liều digoxin 30-50% khi dùng verapamil. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Verapamil", "Beta-blocker"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng ức chế tim, có thể gây block nhĩ thất nặng",
        "description": "Tăng nguy cơ block nhĩ thất, suy tim",
        "management": "Tránh dùng chung nếu có thể. Nếu cần: theo dõi nhịp tim và ECG sát",
        "references": "Micromedex"
    },
    
    ("Diltiazem", "Beta-blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế tim",
        "description": "Tăng nguy cơ block nhĩ thất",
        "management": "Thận trọng khi dùng chung. Theo dõi nhịp tim",
        "references": "Micromedex"
    },
    
    ("Amlodipine", "Simvastatin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Amlodipine ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày",
        "references": "FDA, Micromedex"
    },
    
    ("Verapamil", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Verapamil ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA, Micromedex"
    },
    
    ("Diltiazem", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Diltiazem ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA, Micromedex"
    },
    
    # ========== DIGOXIN ==========
    
    # Digoxin + Amiodarone (already in main file)
    ("Digoxin", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone ức chế P-gp, làm tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin (buồn nôn, rối loạn nhịp tim)",
        "clinical_significance": "Nồng độ digoxin có thể tăng 2-3 lần. Nguy cơ ngộ độc digoxin nặng.",
        "management": "Giảm liều digoxin 50% khi bắt đầu amiodarone. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Verapamil"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Verapamil ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Giảm liều digoxin 30-50% khi dùng verapamil. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Diltiazem"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Diltiazem ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin, cân nhắc giảm liều digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin, cân nhắc giảm liều digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Clarithromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Clarithromycin ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi nồng độ digoxin, cân nhắc giảm liều digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Quinidine"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Quinidine ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Giảm liều digoxin 50% khi dùng quinidine. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Rifampin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Rifampin cảm ứng P-gp, giảm nồng độ digoxin",
        "description": "Giảm hiệu quả digoxin",
        "management": "Tăng liều digoxin khi dùng rifampin. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Digoxin", "Cholestyramine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Cholestyramine giảm hấp thu digoxin",
        "description": "Giảm hiệu quả digoxin",
        "management": "Cách xa ít nhất 2 giờ",
        "references": "Micromedex"
    },
    
    # ========== AMIODARONE ==========
    
    ("Amiodarone", "Digoxin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone ức chế P-gp, làm tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin (buồn nôn, rối loạn nhịp tim)",
        "clinical_significance": "Nồng độ digoxin có thể tăng 2-3 lần. Nguy cơ ngộ độc digoxin nặng.",
        "management": "Giảm liều digoxin 50% khi bắt đầu amiodarone. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Amiodarone", "Simvastatin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân, có thể tử vong",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA"
    },
    
    ("Amiodarone", "Warfarin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone ức chế CYP2C9, tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết nặng",
        "clinical_significance": "INR có thể tăng đáng kể. Nguy cơ xuất huyết nặng.",
        "management": "Giảm liều warfarin 30-50% khi bắt đầu amiodarone. Theo dõi INR 2-3 lần/tuần",
        "references": "Micromedex"
    },
    
    ("Amiodarone", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim (torsades de pointes)",
        "management": "Tránh dùng với thuốc kéo dài QT khác",
        "references": "FDA, Micromedex"
    },
    
    ("Amiodarone", "Beta-blocker"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng tác dụng ức chế tim",
        "description": "Tăng nguy cơ block nhĩ thất, suy tim",
        "management": "Thận trọng khi dùng chung. Theo dõi nhịp tim",
        "references": "Micromedex"
    },
    
    # ========== STATINS ==========
    
    # Atorvastatin + Clarithromycin (already in main file)
    ("Atorvastatin", "Clarithromycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Clarithromycin ức chế CYP3A4, tăng nồng độ atorvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "clinical_significance": "Nguy cơ tiêu cơ vân tăng 10-15 lần. Có thể gây suy thận cấp, tử vong.",
        "management": "Tránh dùng chung. Nếu cần: giảm liều atorvastatin 50-75%, theo dõi CK",
        "alternatives": {
            "for_clarithromycin": ["Azithromycin", "Doxycycline"],
            "for_atorvastatin": ["Pravastatin", "Rosuvastatin"]
        },
        "references": "FDA, Micromedex"
    },
    
    # Simvastatin + Amiodarone (already in main file)
    ("Simvastatin", "Amiodarone"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Amiodarone ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân, có thể tử vong",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA"
    },
    
    ("Simvastatin", "Verapamil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Verapamil ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA, Micromedex"
    },
    
    ("Simvastatin", "Diltiazem"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Diltiazem ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày hoặc chuyển statin khác",
        "references": "FDA, Micromedex"
    },
    
    ("Simvastatin", "Amlodipine"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Amlodipine ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin xuống tối đa 20mg/ngày",
        "references": "FDA, Micromedex"
    },
    
    ("Simvastatin", "Erythromycin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Erythromycin ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều simvastatin hoặc chuyển statin khác",
        "references": "FDA, Micromedex"
    },
    
    ("Simvastatin", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP3A4, tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng chung. Nếu cần: giảm liều simvastatin",
        "references": "FDA, Micromedex"
    },
    
    ("Atorvastatin", "Erythromycin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Erythromycin ức chế CYP3A4, tăng nồng độ atorvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Thận trọng khi dùng chung. Theo dõi CK",
        "references": "Micromedex"
    },
    
    ("Atorvastatin", "Ketoconazole"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Ketoconazole ức chế CYP3A4, tăng nồng độ atorvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng chung. Nếu cần: giảm liều atorvastatin",
        "references": "FDA, Micromedex"
    },
    
    ("Rosuvastatin", "Gemfibrozil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Gemfibrozil tăng nồng độ rosuvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Giảm liều rosuvastatin hoặc tránh dùng chung",
        "references": "FDA, Micromedex"
    },
    
    ("Simvastatin", "Gemfibrozil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Gemfibrozil tăng nồng độ simvastatin",
        "description": "Tăng nguy cơ tiêu cơ vân",
        "management": "Tránh dùng chung. Nếu cần: giảm liều simvastatin",
        "references": "FDA, Micromedex"
    },
    
    # ========== DIURETICS ==========
    
    ("Furosemide", "Digoxin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Furosemide gây hạ kali máu, tăng nguy cơ ngộ độc digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Theo dõi kali máu và nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Furosemide", "Aminoglycoside"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Tăng độc tính thận và thần kinh thính giác",
        "description": "Tăng nguy cơ suy thận và điếc",
        "management": "Thận trọng khi dùng chung. Theo dõi chức năng thận",
        "references": "Micromedex"
    },
    
    ("Hydrochlorothiazide", "Lithium"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Thiazide làm giảm đào thải lithium, tăng nồng độ lithium",
        "description": "Tăng nguy cơ độc tính lithium",
        "management": "Giảm liều lithium 30-50% khi dùng thiazide. Theo dõi nồng độ lithium",
        "references": "Micromedex"
    },
    
    ("Spironolactone", "ACE Inhibitor"): {
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
    
    # ========== ANTIARRHYTHMICS ==========
    
    ("Quinidine", "Digoxin"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Quinidine ức chế P-gp, tăng nồng độ digoxin",
        "description": "Tăng nguy cơ ngộ độc digoxin",
        "management": "Giảm liều digoxin 50% khi dùng quinidine. Theo dõi nồng độ digoxin",
        "references": "Micromedex"
    },
    
    ("Quinidine", "Warfarin"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Có thể tăng tác dụng warfarin",
        "description": "Tăng nguy cơ xuất huyết",
        "management": "Theo dõi INR khi dùng quinidine",
        "references": "Micromedex"
    },
    
    ("Sotalol", "QT Prolonging Drugs"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Sotalol kéo dài QT, tăng nguy cơ khi dùng với thuốc kéo dài QT khác",
        "description": "Tăng nguy cơ rối loạn nhịp tim (torsades de pointes)",
        "management": "Tránh dùng với thuốc kéo dài QT khác",
        "references": "FDA, Micromedex"
    },
    
    ("Flecainide", "Amiodarone"): {
        "severity": SEVERITY_MODERATE,
        "mechanism": "Amiodarone ức chế chuyển hóa flecainide",
        "description": "Tăng nồng độ flecainide",
        "management": "Giảm liều flecainide khi dùng amiodarone",
        "references": "Micromedex"
    },
    
    # ========== NITRATES ==========
    
    ("Nitrate", "Sildenafil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng giãn mạch, gây hạ huyết áp nặng",
        "description": "Tăng nguy cơ hạ huyết áp nặng, có thể tử vong",
        "clinical_significance": "Hạ huyết áp có thể rất nặng, gây sốc, tử vong.",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 24 giờ",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Nitrate", "Tadalafil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng giãn mạch, gây hạ huyết áp nặng",
        "description": "Tăng nguy cơ hạ huyết áp nặng",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 48 giờ",
        "references": "FDA Black Box Warning, Micromedex"
    },
    
    ("Nitrate", "Vardenafil"): {
        "severity": SEVERITY_MAJOR,
        "mechanism": "Tăng tác dụng giãn mạch, gây hạ huyết áp nặng",
        "description": "Tăng nguy cơ hạ huyết áp nặng",
        "management": "TRÁNH DÙNG CHUNG. Cách xa ít nhất 24 giờ",
        "references": "FDA Black Box Warning, Micromedex"
    },
}

