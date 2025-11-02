"""
Antibiotic Database - Common Injectable Antibiotics in Vietnam
Ưu tiên kháng sinh tiêm truyền (IV/IM) thông dụng tại Việt Nam
"""

ANTIBIOTICS_DATABASE = {
    # ========== BETA-LACTAMS - PENICILLINS ==========
    "Penicillin G": {
        "group": "Beta-lactam - Penicillin",
        "vietnamese_name": "Penicillin G, Bicilin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do liên cầu nhóm A, B, C, G",
            "Giang mai (Treponema pallidum)",
            "Nhiễm khuẩn răng miệng (Peptostreptococcus)",
            "Viêm màng não do phế cầu (liều cao IV)"
        ],
        "contraindications": [
            "Dị ứng penicillin (phản vệ)",
            "Sốc phản vệ với beta-lactam trước đây"
        ],
        "dosage": {
            "adult_iv": "2-4 triệu đơn vị IV mỗi 4-6 giờ (2-24 triệu đơn vị/ngày)",
            "adult_im": "600,000 - 1.2 triệu đơn vị IM x 1 lần/ngày (Bicilin)",
            "pediatric_iv": "100,000-400,000 đơn vị/kg/ngày chia 4-6 lần",
            "pediatric_im": "25,000-50,000 đơn vị/kg x 1 lần/ngày (Bicilin)",
            "meningitis_iv": "18-24 triệu đơn vị/ngày chia 4 lần (liều cao)",
            "notes": "Penicillin G natri (IV) - không ổn định, phải pha ngay trước dùng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "1-2 triệu đơn vị mỗi 12 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Phản ứng dị ứng: phát ban, sốt, sốc phản vệ",
            "Rối loạn điện giải (natri cao nếu dùng liều lớn)",
            "Co giật (liều rất cao, suy thận)",
            "Viêm tĩnh mạch (IV)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ penicillin (dùng chung để tăng nồng độ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Methotrexate: giảm thanh thải"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B - An toàn trong thai kỳ"
    },
    
    "Ampicillin": {
        "group": "Beta-lactam - Aminopenicillin",
        "vietnamese_name": "Ampicillin, Ampiclox, Ampix",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn hô hấp",
            "Nhiễm khuẩn do Listeria monocytogenes",
            "Viêm màng não do Listeria (liều cao)"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Nhiễm trùng do beta-lactamase"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 4-6 giờ (4-12g/ngày)",
            "adult_im": "500mg-1g IM mỗi 6-8 giờ",
            "meningitis_iv": "2g IV mỗi 4 giờ (12g/ngày)",
            "pediatric_iv": "100-200mg/kg/ngày chia 4-6 lần",
            "meningitis_ped": "200-300mg/kg/ngày chia 4-6 lần",
            "notes": "Phổ rộng hơn penicillin G nhưng không kháng beta-lactamase"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50% hoặc tăng khoảng cách",
            "under_15": "1g mỗi 12 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến)",
            "Phát ban (đặc biệt bệnh tăng bạch cầu đơn nhân)",
            "Viêm đại tràng giả mạc (hiếm)",
            "Phản ứng dị ứng"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Allopurinol: tăng nguy cơ phát ban",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    "Ampicillin-Sulbactam": {
        "group": "Beta-lactam - Penicillin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ampicillin-Sulbactam, Unasyn, Sultamicillin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện (HAP, VAP)",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn do vi khuẩn kỵ khí + aerobe"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Suy gan nặng (sulbactam)"
        ],
        "dosage": {
            "adult_iv": "1.5-3g (1g ampicillin + 0.5g sulbactam) IV mỗi 6-8 giờ",
            "adult_im": "1.5g IM mỗi 8-12 giờ",
            "severe_iv": "3g IV mỗi 6 giờ (12g/ngày)",
            "pediatric_iv": "100-200mg/kg/ngày (theo ampicillin) chia 4 lần",
            "notes": "Tỷ lệ 2:1 (ampicillin:sulbactam)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1.5g mỗi 8 giờ",
            "15_30": "1.5g mỗi 12 giờ",
            "under_15": "1.5g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Giống ampicillin",
            "Viêm tĩnh mạch (IV)",
            "Tiêu chảy"
        ],
        "interactions": [
            "Giống ampicillin",
            "Probenecid: tăng nồng độ cả 2"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
    
    "Amoxicillin-Clavulanate": {
        "group": "Beta-lactam - Penicillin + Beta-lactamase inhibitor",
        "vietnamese_name": "Amoxicillin-Clavulanate, Augmentin, Amoxiclav, Clavophar",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường hô hấp trên/dưới",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Viêm gan do amoxicillin-clavulanate trước đây"
        ],
        "dosage": {
            "adult_iv": "1.2g (1g amoxicillin + 0.2g clavulanate) IV mỗi 8 giờ",
            "adult_po_standard": "875/125mg PO x 2 lần/ngày",
            "adult_po_high": "1000/125mg PO x 3 lần/ngày (nhiễm khuẩn nặng)",
            "pediatric_iv": "30mg/kg (theo amoxicillin) mỗi 8 giờ",
            "pediatric_po": "25-45mg/kg/ngày (theo amoxicillin) chia 2-3 lần",
            "notes": "Tỷ lệ thường 7:1 hoặc 14:1 (amoxicillin:clavulanate)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "875/125mg mỗi 12 giờ (PO) hoặc 1.2g IV mỗi 12 giờ"
        },
        "side_effects": [
            "Tiêu chảy (20-30%)",
            "Buồn nôn, nôn",
            "Viêm gan (hiếm, đặc biệt nam giới >65 tuổi)",
            "Phát ban"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ amoxicillin",
            "Warfarin: tăng nguy cơ chảy máu",
            "Allopurinol: tăng phát ban"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    "Piperacillin-Tazobactam": {
        "group": "Beta-lactam - Extended-spectrum Penicillin + Inhibitor",
        "vietnamese_name": "Piperacillin-Tazobactam, Tazocin, Pip-Taz",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng (HAP, VAP)",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn do Pseudomonas aeruginosa",
            "Nhiễm khuẩn do vi khuẩn kỵ khí"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Suy thận nặng không lọc máu"
        ],
        "dosage": {
            "adult_standard": "4.5g (4g piperacillin + 0.5g tazobactam) IV mỗi 8 giờ",
            "adult_severe": "4.5g IV mỗi 6 giờ (18g/ngày)",
            "adult_sepsis": "4.5g IV mỗi 6 giờ + thuốc khác",
            "pediatric": "112.5mg/kg (theo piperacillin) IV mỗi 8 giờ",
            "notes": "Thường dùng kết hợp với aminoglycoside trong nhiễm khuẩn nghi ngờ Pseudomonas"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "4.5g mỗi 8 giờ",
            "15_30": "4.5g mỗi 12 giờ",
            "under_15": "4.5g mỗi 12 giờ + lọc máu sau liều",
            "hemodialysis": "2.25g sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (11%)",
            "Phát ban",
            "Giảm bạch cầu, giảm tiểu cầu",
            "Viêm tĩnh mạch (cần pha loãng)",
            "Tăng natri máu (nhiều natri trong chế phẩm)"
        ],
        "interactions": [
            "Vancomycin: giảm nồng độ vancomycin (tăng khoảng cách)",
            "Aminoglycosides: không pha cùng (mất hoạt tính aminoglycoside)",
            "Methotrexate: giảm thanh thải",
            "Heparin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
    
    # ========== BETA-LACTAMS - CEPHALOSPORINS ==========
    "Cefazolin": {
        "group": "Beta-lactam - Cephalosporin thế hệ 1",
        "vietnamese_name": "Cefazolin, Kefzol, Cephazolin",
        "administration": ["IV", "IM"],
        "indications": [
            "Dự phòng phẫu thuật",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin (phản vệ)",
            "Dị ứng penicillin nặng (phản ứng chéo 10%)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 8 giờ",
            "adult_im": "500mg-1g IM mỗi 8 giờ",
            "prophylaxis_iv": "1-2g IV trước mổ (lặp lại nếu mổ >4 giờ)",
            "pediatric_iv": "25-100mg/kg/ngày chia 3-4 lần",
            "notes": "Thời gian bán thải dài (1.8h) nên dùng mỗi 8h"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50% hoặc tăng khoảng cách",
            "under_15": "500mg-1g mỗi 24-48 giờ"
        },
        "side_effects": [
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Đau tại chỗ tiêm (IM)",
            "Tiêu chảy"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    "Ceftriaxone": {
        "group": "Beta-lactam - Cephalosporin thế hệ 3",
        "vietnamese_name": "Ceftriaxone, Rocephin, Oritaxim",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn huyết",
            "Viêm màng não",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn phức tạp",
            "Bệnh lậu",
            "Bệnh Lyme"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Tăng bilirubin ở trẻ sơ sinh (gắn albumin)",
            "Dị ứng penicillin (phản ứng chéo 10%)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV/IM x 1 lần/ngày",
            "adult_severe": "2g IV x 1-2 lần/ngày",
            "adult_meningitis": "2g IV mỗi 12 giờ (4g/ngày)",
            "adult_gonorrhea": "250mg IM x 1 liều",
            "pediatric_standard": "50-100mg/kg/ngày chia 1-2 lần (max 2g/ngày)",
            "pediatric_meningitis": "100mg/kg/ngày chia 1-2 lần (max 4g/ngày)",
            "notes": "Thời gian bán thải dài (8h) nên dùng 1-2 lần/ngày. Không cần điều chỉnh thận nhẹ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi (thải qua gan)",
            "under_15": "Giảm liều nếu suy gan + suy thận"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Tăng transaminase (thường nhẹ, tạm thời)",
            "Sỏi mật (liều cao, dài ngày) - hòa tan khi ngừng",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Calcium: kết tủa (không pha cùng trong cùng bộ truyền)",
            "Vancomycin: không pha cùng",
            "Probenecid: không ảnh hưởng (thải qua gan)"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    "Ceftazidime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 3",
        "vietnamese_name": "Ceftazidime, Fortum, Tazidime",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do Pseudomonas aeruginosa",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn ở bệnh nhân suy giảm miễn dịch",
            "Nhiễm khuẩn huyết nghi ngờ Pseudomonas"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 8 giờ",
            "adult_severe": "2g IV mỗi 8 giờ (6g/ngày)",
            "adult_pseudomonas": "2g IV mỗi 8 giờ + aminoglycoside",
            "pediatric": "100-150mg/kg/ngày chia 3 lần (max 6g/ngày)",
            "cystic_fibrosis": "100-150mg/kg/ngày chia 3 lần",
            "notes": "Hoạt động tốt nhất chống Pseudomonas trong cephalosporin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 12 giờ",
            "15_30": "1g mỗi 12 giờ",
            "under_15": "1g mỗi 24-48 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch",
            "Tăng transaminase"
        ],
        "interactions": [
            "Aminoglycosides: không pha cùng",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
    
    "Cefepime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 4",
        "vietnamese_name": "Cefepime, Maxipime, Cefepim",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn do Pseudomonas (khi ceftazidime không có)",
            "Sốt giảm bạch cầu hạt"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Suy thận nặng (nguy cơ rối loạn thần kinh)"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 12 giờ",
            "adult_severe": "2g IV mỗi 8 giờ",
            "adult_neutropenia": "2g IV mỗi 8 giờ",
            "pediatric": "100-150mg/kg/ngày chia 2-3 lần (max 6g/ngày)",
            "notes": "Phổ rộng hơn ceftriaxone, hoạt động tốt chống Pseudomonas"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 12 giờ",
            "15_30": "1-2g mỗi 24 giờ",
            "under_15": "1g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Rối loạn thần kinh (lú lẫn, co giật) - đặc biệt suy thận",
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Aminoglycosides: không pha cùng",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
    
    # ========== CARBAPENEMS ==========
    "Meropenem": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Meropenem, Meronem, Meropen",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng",
            "Viêm phổi bệnh viện (HAP, VAP)",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Viêm màng não do vi khuẩn",
            "Nhiễm khuẩn đa kháng",
            "Nhiễm khuẩn do ESBL-producing bacteria"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng penicillin (phản ứng chéo cao 50%)"
        ],
        "dosage": {
            "adult_standard": "1g IV mỗi 8 giờ",
            "adult_severe": "1g IV mỗi 8 giờ hoặc 2g IV mỗi 8 giờ (nhiễm khuẩn rất nặng)",
            "adult_meningitis": "2g IV mỗi 8 giờ",
            "adult_pseudomonas": "2g IV mỗi 8 giờ",
            "pediatric": "60mg/kg/ngày chia 3 lần (max 2g/liều)",
            "pediatric_meningitis": "120mg/kg/ngày chia 3 lần (max 2g/liều)",
            "notes": "Infusion 30 phút hoặc bolus 5-20 phút. Phổ rộng nhất trong carbapenem"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1g mỗi 12 giờ",
            "15_30": "500mg-1g mỗi 12 giờ",
            "under_15": "500mg mỗi 24 giờ hoặc lọc máu",
            "hemodialysis": "500mg-1g sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (2-12%)",
            "Buồn nôn, nôn",
            "Phát ban (1-3%)",
            "Co giật (0.5-2%, đặc biệt suy thận)",
            "Viêm tĩnh mạch",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Valproic acid: GIẢM nồng độ valproic acid (nguy cơ co giật)",
            "Probenecid: tăng nồng độ meropenem",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },
    
    "Imipenem-Cilastatin": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Imipenem-Cilastatin, Tienam, Imipenem",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng",
            "Nhiễm khuẩn đa kháng",
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn ổ bụng"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Suy thận nặng (CrCl < 5) - nguy cơ co giật",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_iv": "500mg-1g IV mỗi 6-8 giờ (max 4g/ngày)",
            "adult_im": "500-750mg IM mỗi 12 giờ",
            "adult_severe": "1g IV mỗi 6-8 giờ",
            "pediatric_iv": "60-100mg/kg/ngày chia 4 lần (max 4g/ngày)",
            "notes": "Phải có cilastatin để bảo vệ imipenem khỏi bị phá hủy ở thận"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "500mg mỗi 8 giờ",
            "15_30": "500mg mỗi 12 giờ",
            "under_15": "250-500mg mỗi 12 giờ (tránh nếu có thể)",
            "hemodialysis": "250-500mg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Co giật (1-3%, đặc biệt suy thận, liều cao)",
            "Tiêu chảy",
            "Buồn nôn",
            "Phát ban",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Ganciclovir: tăng nguy cơ co giật",
            "Valproic acid: giảm nồng độ valproic acid",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },
    
    # ========== AMINOGLYCOSIDES ==========
    "Gentamicin": {
        "group": "Aminoglycoside",
        "vietnamese_name": "Gentamicin, Gentamycin, Garamycin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn huyết nghi ngờ Gram âm",
            "Nhiễm khuẩn do Pseudomonas",
            "Viêm nội tâm mạc",
            "Dự phòng phẫu thuật (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng (dùng với thận trọng)",
            "Rối loạn thần kinh tai"
        ],
        "dosage": {
            "adult_iv_once_daily": "5-7mg/kg IV x 1 lần/ngày (dựa trên cân nặng thực tế)",
            "adult_iv_tid": "1-2mg/kg IV mỗi 8 giờ (liều cũ, ít dùng)",
            "adult_im": "1-2mg/kg IM mỗi 8 giờ",
            "adult_obese_abw": "5-7mg/kg IV x 1 lần/ngày (dựa trên ABW)",
            "pediatric": "7.5mg/kg IV x 1 lần/ngày hoặc 2.5mg/kg mỗi 8 giờ",
            "notes": "Ưu tiên dùng 1 lần/ngày (ODD) - hiệu quả cao hơn, độc tính thấp hơn. Phải monitor nồng độ!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Giảm liều mạnh hoặc tránh nếu có thể",
            "hemodialysis": "1-2mg/kg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Độc thận (10-25%) - tăng creatinine, AKI",
            "Độc tai (2-25%) - điếc, ù tai, mất thăng bằng",
            "Tê liệt thần kinh cơ (hiếm)",
            "Tăng creatinin máu"
        ],
        "interactions": [
            "Vancomycin: tăng độc thận (cẩn trọng khi dùng chung)",
            "Furosemide: tăng độc tai",
            "Ciclosporin: tăng độc thận",
            "Beta-lactams: không pha cùng (mất hoạt tính)"
        ],
        "monitoring": "Bắt buộc: Peak và Trough levels, Creatinine hàng ngày, thính giác",
        "aware_classification": "ACCESS",
        "pregnancy": "D - Độc thai nhi"
    },
    
    "Amikacin": {
        "group": "Aminoglycoside",
        "vietnamese_name": "Amikacin, Amikacin, Amikin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đa kháng (MDR)",
            "Nhiễm khuẩn do vi khuẩn kháng gentamicin/tobramycin",
            "Nhiễm khuẩn huyết nghi ngờ Gram âm kháng",
            "Viêm phổi bệnh viện nặng"
        ],
        "contraindications": [
            "Dị ứng aminoglycoside",
            "Suy thận nặng",
            "Rối loạn thần kinh tai"
        ],
        "dosage": {
            "adult_iv_once_daily": "15-20mg/kg IV x 1 lần/ngày",
            "adult_iv_tid": "7.5mg/kg IV mỗi 8 giờ",
            "adult_im": "7.5mg/kg IM mỗi 8 giờ",
            "adult_obese_abw": "15-20mg/kg IV x 1 lần/ngày (dựa trên ABW)",
            "pediatric": "15-20mg/kg IV x 1 lần/ngày",
            "notes": "Liều cao hơn gentamicin (15-20mg/kg vs 5-7mg/kg). Ưu tiên ODD. Monitor nồng độ!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Tránh hoặc giảm liều mạnh",
            "hemodialysis": "7.5mg/kg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Độc thận (tương tự gentamicin)",
            "Độc tai",
            "Giống gentamicin nhưng có thể ít hơn ở liều tương đương"
        ],
        "interactions": [
            "Giống gentamicin",
            "Vancomycin: tăng độc thận",
            "Beta-lactams: không pha cùng"
        ],
        "monitoring": "Bắt buộc: Peak/Trough, Creatinine, thính giác",
        "aware_classification": "WATCH",
        "pregnancy": "D"
    },
    
    # ========== GLYCOPEPTIDES ==========
    "Vancomycin": {
        "group": "Glycopeptide",
        "vietnamese_name": "Vancomycin, Vancomycin, Vancocin",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do MRSA",
            "Viêm màng não do S. pneumoniae kháng penicillin",
            "Nhiễm khuẩn do Enterococcus kháng ampicillin",
            "Viêm đại tràng giả mạc (PO)",
            "Dự phòng phẫu thuật"
        ],
        "contraindications": [
            "Dị ứng vancomycin",
            "Suy thận nặng (phải điều chỉnh liều)"
        ],
        "dosage": {
            "adult_iv_standard": "15-20mg/kg IV mỗi 8-12 giờ (dựa trên CrCl)",
            "adult_iv_load": "20-25mg/kg IV x 1 liều đầu (loading dose)",
            "adult_iv_obese": "Dựa trên ABW, thường 20-25mg/kg",
            "adult_po_cdiff": "125-500mg PO x 4 lần/ngày",
            "pediatric_iv": "40-60mg/kg/ngày chia 4 lần hoặc 15mg/kg mỗi 6 giờ",
            "notes": "Phải truyền tĩnh mạch chậm (≥60 phút) để tránh Red Man Syndrome. Monitor Trough level!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều hoặc tăng khoảng cách 12-24h",
            "15_30": "Giảm liều 50% hoặc mỗi 24-48h",
            "under_15": "Liều thấp mỗi 48-72h hoặc lọc máu",
            "hemodialysis": "15-20mg/kg sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Red Man Syndrome (phản ứng histamine - truyền quá nhanh)",
            "Độc thận (15-30%) - đặc biệt với aminoglycoside",
            "Độc tai",
            "Thrombophlebitis",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Piperacillin-tazobactam: giảm nồng độ vancomycin (tăng khoảng cách)",
            "Furosemide: tăng độc tai",
            "Anesthetic agents: tăng nguy cơ hạ huyết áp"
        ],
        "monitoring": "Bắt buộc: Trough level (mục tiêu 10-20 mg/L), Creatinine, thính giác",
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },
    
    # ========== FLUOROQUINOLONES ==========
    "Ciprofloxacin": {
        "group": "Fluoroquinolone",
        "vietnamese_name": "Ciprofloxacin, Cipro, Ciprobay",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường tiêu hóa",
            "Nhiễm khuẩn do Pseudomonas",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng quinolone",
            "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
            "Có thai, cho con bú"
        ],
        "dosage": {
            "adult_iv_standard": "400mg IV mỗi 12 giờ",
            "adult_iv_severe": "400mg IV mỗi 8 giờ",
            "adult_po_standard": "500-750mg PO x 2 lần/ngày",
            "adult_po_uti": "250-500mg PO x 2 lần/ngày",
            "pediatric_iv": "10-15mg/kg IV mỗi 12 giờ (chỉ khi thực sự cần)",
            "notes": "Tránh dùng quinolone nếu có lựa chọn khác (nguy cơ tác dụng phụ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "200-400mg mỗi 12 giờ",
            "under_15": "200mg mỗi 12 giờ hoặc tránh"
        },
        "side_effects": [
            "Rối loạn thần kinh trung ương (lú lẫn, co giật, mất ngủ)",
            "Đứt gân (Achilles)",
            "Rối loạn nhịp tim (QT kéo dài)",
            "Tăng đường huyết/hạ đường huyết",
            "Phát ban, nhạy cảm ánh sáng"
        ],
        "interactions": [
            "Antacids, Sucralfate: giảm hấp thu (cách 2-4 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Theophylline: tăng nồng độ theophylline",
            "Probenecid: tăng nồng độ ciprofloxacin"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },
    
    "Levofloxacin": {
        "group": "Fluoroquinolone",
        "vietnamese_name": "Levofloxacin, Levaquin, Tavanic",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Viêm xoang",
            "Nhiễm khuẩn da và mô mềm"
        ],
        "contraindications": [
            "Dị ứng quinolone",
            "Trẻ em <18 tuổi",
            "QT kéo dài",
            "Có thai, cho con bú"
        ],
        "dosage": {
            "adult_iv_standard": "500-750mg IV x 1 lần/ngày",
            "adult_po_standard": "500-750mg PO x 1 lần/ngày",
            "adult_severe": "750mg IV/PO x 1 lần/ngày",
            "adult_uti": "250-500mg PO x 1 lần/ngày",
            "notes": "Dùng 1 lần/ngày, tiện lợi hơn ciprofloxacin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250-500mg mỗi 24 giờ",
            "15_30": "250mg mỗi 24 giờ",
            "under_15": "250mg mỗi 48 giờ hoặc tránh"
        },
        "side_effects": [
            "Giống ciprofloxacin",
            "Đứt gân",
            "Rối loạn thần kinh",
            "QT kéo dài"
        ],
        "interactions": [
            "Giống ciprofloxacin",
            "Antacids: giảm hấp thu",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },
    
    # ========== MACROLIDES ==========
    "Azithromycin": {
        "group": "Macrolide",
        "vietnamese_name": "Azithromycin, Zithromax, Azitro",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường hô hấp trên",
            "Nhiễm Chlamydia, Mycoplasma",
            "Nhiễm khuẩn đường tiết niệu do Chlamydia"
        ],
        "contraindications": [
            "Dị ứng macrolide",
            "QT kéo dài",
            "Rối loạn nhịp tim"
        ],
        "dosage": {
            "adult_iv": "500mg IV x 1 lần/ngày",
            "adult_po_standard": "500mg PO ngày 1, sau đó 250mg/ngày x 4 ngày",
            "adult_po_single": "1g PO x 1 liều (Chlamydia)",
            "adult_po_extended": "500mg PO x 1 lần/ngày (nhiễm khuẩn kéo dài)",
            "pediatric_iv": "10mg/kg IV x 1 lần/ngày",
            "pediatric_po": "10mg/kg PO ngày 1 (max 500mg), sau đó 5mg/kg/ngày x 4 ngày",
            "notes": "Thời gian bán thải dài (68h), dùng 1 lần/ngày. Không cần điều chỉnh thận nhẹ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Buồn nôn, tiêu chảy",
            "QT kéo dài",
            "Rối loạn nhịp tim",
            "Viêm gan (hiếm)",
            "Nhạy cảm ánh sáng"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Digoxin: tăng nồng độ digoxin",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Antacids: giảm hấp thu PO (cách 2 giờ)"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== LINCOSAMIDES ==========
    "Clindamycin": {
        "group": "Lincosamide",
        "vietnamese_name": "Clindamycin, Dalacin, Clindamycin",
        "administration": ["IV", "IM", "PO"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn răng miệng",
            "Viêm phúc mạc do kỵ khí",
            "Dự phòng phẫu thuật"
        ],
        "contraindications": [
            "Dị ứng clindamycin",
            "Viêm đại tràng giả mạc trước đây"
        ],
        "dosage": {
            "adult_iv": "600-900mg IV mỗi 8 giờ",
            "adult_im": "600mg IM mỗi 12 giờ",
            "adult_po": "150-450mg PO x 3-4 lần/ngày",
            "adult_severe": "900mg IV mỗi 8 giờ",
            "pediatric_iv": "20-40mg/kg/ngày chia 3-4 lần",
            "pediatric_po": "10-25mg/kg/ngày chia 3-4 lần",
            "notes": "Hoạt động tốt chống kỵ khí Gram dương và âm"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Tiêu chảy (20%)",
            "Viêm đại tràng giả mạc (1-10%) - do C. difficile",
            "Phát ban",
            "Viêm tĩnh mạch (IV)"
        ],
        "interactions": [
            "Erythromycin: đối kháng (không dùng chung)",
            "Neuromuscular blockers: tăng tác dụng"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== METRONIDAZOLE ==========
    "Metronidazole": {
        "group": "Nitroimidazole",
        "vietnamese_name": "Metronidazole, Flagyl, Metronidazol",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Viêm phúc mạc",
            "Nhiễm khuẩn ổ bụng",
            "Viêm đại tràng giả mạc (C. difficile)",
            "Nhiễm Trichomonas, Giardia, Amebiasis"
        ],
        "contraindications": [
            "Dị ứng metronidazole",
            "Tam cá nguyệt đầu thai kỳ (tránh nếu có thể)"
        ],
        "dosage": {
            "adult_iv": "500mg IV mỗi 8 giờ hoặc 1g IV mỗi 12 giờ",
            "adult_po": "500mg PO x 3 lần/ngày hoặc 1g PO x 2 lần/ngày",
            "adult_cdiff": "500mg PO x 3 lần/ngày x 10-14 ngày",
            "pediatric_iv": "30mg/kg/ngày chia 3 lần",
            "pediatric_po": "30-50mg/kg/ngày chia 3 lần",
            "notes": "Hoạt động tốt chống kỵ khí, đặc biệt B. fragilis"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều 50% hoặc tránh"
        },
        "side_effects": [
            "Vị kim loại, buồn nôn",
            "Nhức đầu",
            "Phản ứng giống disulfiram (nếu uống rượu)",
            "Rối loạn thần kinh ngoại biên (dài ngày)",
            "Nước tiểu sẫm màu (bình thường)"
        ],
        "interactions": [
            "Rượu: phản ứng giống disulfiram (buồn nôn, nôn, đỏ mặt)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Lithium: tăng độc tính lithium",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== LINEZOLID ==========
    "Linezolid": {
        "group": "Oxazolidinone",
        "vietnamese_name": "Linezolid, Zyvox, Linezolid",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do VRE (Vancomycin-resistant Enterococcus)",
            "Nhiễm khuẩn do MRSA",
            "Viêm phổi bệnh viện do MRSA",
            "Nhiễm khuẩn da và mô mềm do MRSA"
        ],
        "contraindications": [
            "Dị ứng linezolid",
            "Dùng MAOIs (phenelzine, selegiline)",
            "Suy tủy xương"
        ],
        "dosage": {
            "adult_iv": "600mg IV mỗi 12 giờ",
            "adult_po": "600mg PO x 2 lần/ngày",
            "pediatric": "10mg/kg IV/PO mỗi 8 giờ (max 600mg/liều)",
            "notes": "Sinh khả dụng PO = 100% (có thể chuyển IV ↔ PO). Dùng tối đa 28 ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi"
        },
        "side_effects": [
            "Giảm tiểu cầu, giảm bạch cầu (10-30%, đặc biệt >14 ngày)",
            "Rối loạn thần kinh (viêm dây thần kinh thị giác, ngoại biên)",
            "Nhiễm toan lactic (hiếm nhưng nặng)",
            "Nhức đầu, buồn nôn"
        ],
        "interactions": [
            "MAOIs: phản ứng tăng huyết áp nguy hiểm",
            "SSRIs: hội chứng serotonin",
            "Adrenergic agents: tăng huyết áp",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "Huyết đồ hàng tuần (nếu >14 ngày), thị giác nếu kéo dài",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },
    
    # ========== COLISTIN ==========
    "Colistin": {
        "group": "Polymyxin",
        "vietnamese_name": "Colistin, Colistin, Colimycin",
        "administration": ["IV", "Inhalation"],
        "indications": [
            "Nhiễm khuẩn đa kháng (XDR) do Gram âm",
            "Nhiễm khuẩn do Pseudomonas, Acinetobacter kháng",
            "Viêm phổi do XDR Gram âm",
            "Nhiễm khuẩn huyết do XDR"
        ],
        "contraindications": [
            "Dị ứng colistin",
            "Suy thận nặng (phải điều chỉnh liều)",
            "Nhược cơ (myasthenia gravis)"
        ],
        "dosage": {
            "adult_iv_loading": "9 triệu đơn vị (300mg CBA) IV x 1 liều đầu",
            "adult_iv_maintenance": "9 triệu đơn vị (300mg CBA) IV chia 2-3 lần/ngày",
            "adult_iv_severe": "9 triệu đơn vị mỗi 8 giờ",
            "adult_inhalation": "1-2 triệu đơn vị khí dung x 2-3 lần/ngày",
            "pediatric_iv": "5-9 triệu đơn vị/kg/ngày chia 2-3 lần",
            "notes": "Đơn vị: 1mg CBA = 30,000 IU. Phải có loading dose. Monitor độc thận chặt chẽ!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Giảm liều mạnh hoặc tránh",
            "hemodialysis": "6 triệu đơn vị sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Độc thận nặng (50-70%) - AKI",
            "Độc thần kinh (tê liệt thần kinh cơ, suy hô hấp)",
            "Viêm phổi do hít",
            "Phản ứng tại chỗ (inhalation)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Curariform agents: tăng tê liệt thần kinh cơ",
            "Diuretics: tăng độc thận"
        ],
        "monitoring": "Bắt buộc: Creatinine hàng ngày, xét nghiệm chức năng thận, thần kinh",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },
    
    # ========== CEPHALOSPORINS - Thế hệ 2 ==========
    "Cefuroxime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 2",
        "vietnamese_name": "Cefuroxime, Zinacef, Cefurox",
        "administration": ["IV", "IM"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm xương tủy"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo)"
        ],
        "dosage": {
            "adult_iv": "750mg-1.5g IV mỗi 8 giờ",
            "adult_im": "750mg IM mỗi 8 giờ",
            "adult_severe": "1.5g IV mỗi 8 giờ",
            "pediatric_iv": "75-150mg/kg/ngày chia 3 lần (max 6g/ngày)",
            "notes": "Phổ rộng hơn cefazolin, kháng beta-lactamase tốt hơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "750mg mỗi 12 giờ",
            "under_15": "750mg mỗi 24 giờ"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== CEPHALOSPORINS - Thế hệ 3 - Ceftazidime-Avibactam ==========
    "Ceftazidime-Avibactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ceftazidime-Avibactam, Avycaz, Zavicefta",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn đa kháng (MDR/XDR)",
            "Nhiễm khuẩn do ESBL-producing Gram âm",
            "Nhiễm khuẩn do KPC-producing bacteria",
            "Viêm phổi bệnh viện do MDR",
            "Nhiễm khuẩn ổ bụng phức tạp do MDR"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "2.5g (2g ceftazidime + 0.5g avibactam) IV mỗi 8 giờ",
            "adult_severe": "2.5g IV mỗi 8 giờ (không tăng liều)",
            "adult_renal": "Giảm liều theo CrCl: 1.25g mỗi 12 giờ nếu CrCl 31-50, 1.25g mỗi 24 giờ nếu CrCl 16-30",
            "pediatric": "62.5mg/kg (theo ceftazidime) IV mỗi 8 giờ",
            "notes": "Thuốc mới, đắt tiền. Chỉ dùng khi không còn lựa chọn khác (MDR/XDR)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1.25g mỗi 12 giờ",
            "15_30": "1.25g mỗi 24 giờ",
            "under_15": "1.25g mỗi 48 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tăng transaminase"
        ],
        "interactions": [
            "Giống ceftazidime",
            "Probenecid: không nên dùng chung"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },
    
    # ========== CARBAPENEMS - Ertapenem ==========
    "Ertapenem": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Ertapenem, Invanz, Ertapenem",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn do ESBL-producing bacteria"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng penicillin nặng",
            "Không dùng cho Pseudomonas (không hoạt động)"
        ],
        "dosage": {
            "adult_iv": "1g IV x 1 lần/ngày",
            "adult_im": "1g IM x 1 lần/ngày",
            "pediatric": "15mg/kg IV/IM x 2 lần/ngày (max 1g/liều)",
            "notes": "Ưu điểm: dùng 1 lần/ngày. Nhược điểm: không hoạt động chống Pseudomonas, Acinetobacter"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "500mg mỗi 24 giờ",
            "15_30": "500mg mỗi 24 giờ",
            "under_15": "500mg mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Đau tại chỗ tiêm (IM)",
            "Co giật (hiếm hơn meropenem/imipenem)"
        ],
        "interactions": [
            "Valproic acid: giảm nồng độ valproic acid",
            "Probenecid: tăng nồng độ ertapenem"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },
    
    # ========== LIPOPEPTIDES ==========
    "Daptomycin": {
        "group": "Lipopeptide",
        "vietnamese_name": "Daptomycin, Cubicin, Daptomycin",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm do MRSA",
            "Nhiễm khuẩn huyết do MRSA",
            "Viêm nội tâm mạc do MRSA/VRE",
            "Nhiễm khuẩn do VRE (Enterococcus kháng vancomycin)"
        ],
        "contraindications": [
            "Dị ứng daptomycin",
            "Viêm cơ trước đây do daptomycin"
        ],
        "dosage": {
            "adult_skin": "4mg/kg IV x 1 lần/ngày (nhiễm khuẩn da)",
            "adult_bacteremia": "6mg/kg IV x 1 lần/ngày (nhiễm khuẩn huyết)",
            "adult_endocarditis": "6-10mg/kg IV x 1 lần/ngày",
            "adult_obese": "Dựa trên ABW, không dùng cân nặng thực tế",
            "pediatric": "Không khuyến cáo <18 tuổi",
            "notes": "Phải truyền tĩnh mạch chậm (≥30 phút). Monitor CPK hàng tuần!"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc mỗi 48 giờ",
            "15_30": "Mỗi 48 giờ",
            "under_15": "Mỗi 48 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Viêm cơ (CPK tăng) - nguy hiểm, phải ngừng",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tiêu chảy"
        ],
        "interactions": [
            "Statins: tăng nguy cơ viêm cơ (ngừng statin khi dùng)",
            "Cyclosporine: tăng nồng độ daptomycin"
        ],
        "monitoring": "Bắt buộc: CPK hàng tuần, ngừng nếu CPK >5x ULN hoặc có triệu chứng viêm cơ",
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },
    
    # ========== GLYCYLCYCLINES ==========
    "Tigecycline": {
        "group": "Glycylcycline",
        "vietnamese_name": "Tigecycline, Tygacil, Tigecycline",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn đa kháng (MDR)",
            "Nhiễm khuẩn do Acinetobacter baumannii",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Viêm phổi bệnh viện do MDR"
        ],
        "contraindications": [
            "Dị ứng tigecycline",
            "Trẻ em <8 tuổi (ảnh hưởng răng)",
            "Tam cá nguyệt 2-3 thai kỳ (ảnh hưởng răng thai nhi)"
        ],
        "dosage": {
            "adult_loading": "100mg IV x 1 liều đầu",
            "adult_maintenance": "50mg IV mỗi 12 giờ",
            "adult_severe": "100mg IV mỗi 12 giờ (off-label, cân nhắc)",
            "pediatric": "2mg/kg IV loading, sau đó 1mg/kg mỗi 12 giờ (max 50mg/liều)",
            "notes": "Phổ rộng chống MDR. CẢNH BÁO: Tăng tỷ lệ tử vong trong nghiên cứu (FDA black box)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi",
            "under_15": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn (20-30%)",
            "Tiêu chảy",
            "Tăng nguy cơ tử vong (đặc biệt nhiễm khuẩn huyết, viêm phổi)",
            "Tăng bilirubin, transaminase",
            "Phát ban"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "D - Gây đổi màu răng"
    },
    
    # ========== PHOSPHONIC ACID ==========
    "Fosfomycin": {
        "group": "Phosphonic Acid",
        "vietnamese_name": "Fosfomycin, Fosfomycin, Monuril",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu không biến chứng (PO)",
            "Nhiễm khuẩn đường tiết niệu phức tạp (IV)",
            "Nhiễm khuẩn do MDR Gram âm (kết hợp)",
            "Viêm bể thận cấp"
        ],
        "contraindications": [
            "Dị ứng fosfomycin",
            "Suy thận nặng (CrCl < 10) - IV"
        ],
        "dosage": {
            "adult_po_uti": "3g PO x 1 liều (nhiễm khuẩn tiết niệu đơn giản)",
            "adult_iv": "12-24g IV chia 3-4 lần/ngày (nhiễm khuẩn nặng)",
            "adult_iv_severe": "12g IV mỗi 8 giờ hoặc 16g IV mỗi 8 giờ",
            "pediatric_po": "Không dùng <12 tuổi",
            "pediatric_iv": "200-300mg/kg/ngày chia 3-4 lần",
            "notes": "PO: liều đơn cho UTI. IV: dùng cho nhiễm khuẩn nặng, thường kết hợp"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc tránh (IV)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Tăng transaminase"
        ],
        "interactions": [
            "Metoclopramide: giảm nồng độ fosfomycin PO",
            "Cần cách 2 giờ trước uống"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
    
    # ========== BETA-LACTAMS - Cephalosporin thế hệ 3 khác ==========
    "Cefotaxime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 3",
        "vietnamese_name": "Cefotaxime, Claforan, Cefotaxime",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn huyết",
            "Viêm màng não do vi khuẩn",
            "Viêm phổi",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn bệnh viện"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "1-2g IV mỗi 6-8 giờ",
            "adult_severe": "2g IV mỗi 6-8 giờ (8-12g/ngày)",
            "adult_meningitis": "2g IV mỗi 4-6 giờ",
            "adult_im": "1g IM mỗi 12 giờ",
            "pediatric": "100-200mg/kg/ngày chia 3-4 lần (max 12g/ngày)",
            "pediatric_meningitis": "200-300mg/kg/ngày chia 4-6 lần",
            "notes": "Tương tự ceftriaxone nhưng thời gian bán thải ngắn hơn, dùng nhiều lần/ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 12 giờ",
            "15_30": "1g mỗi 12 giờ",
            "under_15": "1g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tăng transaminase"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== MONOBACTAMS ==========
    "Aztreonam": {
        "group": "Beta-lactam - Monobactam",
        "vietnamese_name": "Aztreonam, Azactam, Aztreonam",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do Pseudomonas",
            "Nhiễm khuẩn do Gram âm",
            "Dị ứng penicillin nặng (an toàn, không phản ứng chéo)",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn ổ bụng"
        ],
        "contraindications": [
            "Dị ứng aztreonam",
            "Không hoạt động chống Gram dương và kỵ khí"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 6-8 giờ",
            "adult_im": "1g IM mỗi 8 giờ",
            "adult_severe": "2g IV mỗi 6-8 giờ",
            "pediatric": "90-120mg/kg/ngày chia 3-4 lần (max 8g/ngày)",
            "notes": "An toàn cho người dị ứng penicillin (không phản ứng chéo). Chỉ hoạt động chống Gram âm"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc lọc máu"
        },
        "side_effects": [
            "Phát ban",
            "Tiêu chảy",
            "Viêm tĩnh mạch",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },
    
    # ========== CEPHALOSPORINS - Thế hệ 5 ==========
    "Ceftaroline": {
        "group": "Beta-lactam - Cephalosporin thế hệ 5",
        "vietnamese_name": "Ceftaroline, Teflaro, Ceftaroline",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn da và mô mềm do MRSA",
            "Viêm phổi cộng đồng do MRSA",
            "Nhiễm khuẩn do MRSA (khi vancomycin không phù hợp)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "600mg IV mỗi 12 giờ",
            "adult_impaired": "400mg IV mỗi 12 giờ (CrCl 30-50)",
            "adult_severe_renal": "400mg IV mỗi 24 giờ (CrCl <30)",
            "pediatric": "Không khuyến cáo <18 tuổi",
            "notes": "Cephalosporin duy nhất hoạt động chống MRSA. Đắt tiền, chỉ dùng khi cần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "400mg mỗi 12 giờ",
            "15_30": "400mg mỗi 24 giờ",
            "under_15": "300mg mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch",
            "Tăng transaminase"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },
    
    # ========== TETRACYCLINES - Doxycycline IV ==========
    "Doxycycline": {
        "group": "Tetracycline",
        "vietnamese_name": "Doxycycline, Vibramycin, Doxycycline",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do Rickettsia, Mycoplasma, Chlamydia",
            "Sốt rét (kết hợp)",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn đường tiết niệu do Chlamydia"
        ],
        "contraindications": [
            "Dị ứng tetracycline",
            "Trẻ em <8 tuổi (ảnh hưởng răng)",
            "Tam cá nguyệt 2-3 thai kỳ (ảnh hưởng răng thai nhi)"
        ],
        "dosage": {
            "adult_iv": "100mg IV mỗi 12 giờ hoặc 200mg IV x 1 lần/ngày",
            "adult_po": "100mg PO x 2 lần/ngày",
            "adult_po_loading": "200mg PO x 1 liều đầu, sau đó 100mg x 2 lần/ngày",
            "pediatric_iv": "4.4mg/kg ngày 1, sau đó 2.2mg/kg mỗi 12 giờ (max 100mg/liều)",
            "notes": "Tránh dùng với sữa, antacids (giảm hấp thu). Tăng nhạy cảm ánh sáng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (thải qua gan)",
            "15_30": "Không đổi",
            "under_15": "Không đổi"
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Nhạy cảm ánh sáng (bắt buộc dùng kem chống nắng)",
            "Rối loạn thực quản (nuốt với nước nhiều)",
            "Phát ban",
            "Đổi màu răng (trẻ em, thai nhi)"
        ],
        "interactions": [
            "Antacids, Sắt, Canxi: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Isotretinoin: tăng áp lực nội sọ",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "D - Đổi màu răng thai nhi"
    },
    
    # ========== SULFONAMIDES ==========
    "Trimethoprim-Sulfamethoxazole": {
        "group": "Sulfonamide",
        "vietnamese_name": "Trimethoprim-Sulfamethoxazole, Bactrim, Cotrimoxazol",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp (Pneumocystis jirovecii)",
            "Nhiễm khuẩn do MRSA",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm Toxoplasma (kết hợp)"
        ],
        "contraindications": [
            "Dị ứng sulfonamide",
            "Thiếu G6PD (tan máu)",
            "Suy thận nặng (CrCl < 15)",
            "Suy gan nặng",
            "Tam cá nguyệt cuối thai kỳ (kernicterus)"
        ],
        "dosage": {
            "adult_iv": "8-10mg/kg (theo TMP) IV mỗi 6-12 giờ",
            "adult_po_standard": "160/800mg (1 viên DS) PO x 2 lần/ngày",
            "adult_po_pcp": "15-20mg/kg (theo TMP) PO mỗi 6-8 giờ",
            "adult_mrsa": "160/800mg PO x 2-4 lần/ngày",
            "pediatric_iv": "8-10mg/kg (theo TMP) IV mỗi 6-12 giờ",
            "pediatric_po": "8-10mg/kg (theo TMP) PO x 2 lần/ngày",
            "notes": "Tỷ lệ 1:5 (TMP:Sulfa). IV: truyền chậm ≥60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Tránh hoặc giảm liều mạnh",
            "under_15": "Chống chỉ định"
        },
        "side_effects": [
            "Phát ban, Stevens-Johnson (nguy hiểm)",
            "Giảm bạch cầu, giảm tiểu cầu",
            "Tan máu (thiếu G6PD)",
            "Tăng K+ máu (đặc biệt suy thận)",
            "Tăng creatinine (tăng creatinine không phải suy thận thật)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu mạnh",
            "Methotrexate: tăng độc tính",
            "ACE inhibitors: tăng K+ máu",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "D - Kernicterus ở tam cá nguyệt cuối"
    },
    
    # ========== CHLORAMPHENICOL ==========
    "Chloramphenicol": {
        "group": "Phenicol",
        "vietnamese_name": "Chloramphenicol, Chloramphenicol, Cloran",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm màng não do H. influenzae (khi ampicillin kháng)",
            "Nhiễm khuẩn do Salmonella typhi (sốt thương hàn)",
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn mắt (tại chỗ)"
        ],
        "contraindications": [
            "Dị ứng chloramphenicol",
            "Suy gan nặng",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_iv": "50-100mg/kg/ngày chia 4 lần (max 4g/ngày)",
            "adult_po": "50mg/kg/ngày chia 4 lần",
            "adult_meningitis": "100mg/kg/ngày chia 4 lần",
            "pediatric": "50-75mg/kg/ngày chia 4 lần",
            "pediatric_meningitis": "75-100mg/kg/ngày chia 4 lần",
            "notes": "Thuốc độc, chỉ dùng khi thực sự cần. Monitor huyết đồ chặt chẽ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Tránh"
        },
        "side_effects": [
            "Suy tủy xương (hiếm nhưng nặng - aplastic anemia)",
            "Gray baby syndrome (trẻ sơ sinh - ngừng tim mạch)",
            "Giảm bạch cầu, giảm tiểu cầu",
            "Tăng transaminase"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Phenytoin: tăng nồng độ phenytoin",
            "Paracetamol: tăng độc tính"
        ],
        "monitoring": "Bắt buộc: Huyết đồ 2 lần/tuần, ngừng nếu giảm bạch cầu/tiểu cầu",
        "aware_classification": "ACCESS",
        "pregnancy": "C"
    },
    
    # ========== BETA-LACTAMS - Penicillin + Beta-lactamase inhibitor ==========
    "Amoxicillin-Clavulanate": {
        "group": "Beta-lactam - Penicillin + Beta-lactamase inhibitor",
        "vietnamese_name": "Amoxicillin-Clavulanate, Augmentin, Amoclav",
        "administration": ["IV", "PO"],
        "indications": [
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn răng miệng"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Tiền sử viêm gan do amoxicillin-clavulanate",
            "Viêm gan đang hoạt động"
        ],
        "dosage": {
            "adult_iv": "1.2g (1g amoxicillin + 0.2g clavulanate) IV mỗi 8 giờ",
            "adult_iv_severe": "2.2g IV mỗi 8 giờ hoặc 1.2g IV mỗi 6 giờ",
            "adult_po": "875/125mg PO x 2 lần/ngày hoặc 500/125mg PO x 3 lần/ngày",
            "pediatric_iv": "30mg/kg (theo amoxicillin) IV mỗi 8 giờ",
            "pediatric_po": "25-45mg/kg (theo amoxicillin) PO x 2-3 lần/ngày",
            "notes": "Augmentin. Clavulanate bảo vệ amoxicillin khỏi beta-lactamase. Phổ rộng"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy (10-15%)",
            "Phát ban",
            "Viêm gan (hiếm, do clavulanate)",
            "Nhiễm nấm Candida",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ amoxicillin",
            "Warfarin: tăng nguy cơ chảy máu",
            "Allopurinol: tăng nguy cơ phát ban"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    "Ampicillin-Sulbactam": {
        "group": "Beta-lactam - Penicillin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ampicillin-Sulbactam, Unasyn, Ampicillin-Sulbactam",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phổi",
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn bệnh viện"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Nhiễm mononucleosis (tăng phát ban)"
        ],
        "dosage": {
            "adult_standard": "1.5g (1g ampicillin + 0.5g sulbactam) IV/IM mỗi 6-8 giờ",
            "adult_severe": "3g IV mỗi 6 giờ",
            "adult_im": "1.5g IM mỗi 6-8 giờ",
            "pediatric": "100-200mg/kg/ngày (theo ampicillin) chia 4 lần",
            "notes": "Sulbactam bảo vệ ampicillin. Tốt chống vi khuẩn kỵ khí"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1.5g mỗi 12 giờ",
            "15_30": "1.5g mỗi 24 giờ",
            "under_15": "1.5g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban (đặc biệt nhiễm mononucleosis)",
            "Nhiễm nấm Candida",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu",
            "Allopurinol: tăng nguy cơ phát ban"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== CARBAPENEMS - Imipenem-Cilastatin ==========
    "Imipenem-Cilastatin": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Imipenem-Cilastatin, Primaxin, Tienam",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng",
            "Nhiễm khuẩn đa kháng",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Viêm phổi bệnh viện"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng penicillin nặng (phản ứng chéo 50%)"
        ],
        "dosage": {
            "adult_standard": "500mg-1g IV mỗi 6-8 giờ",
            "adult_severe": "1g IV mỗi 6-8 giờ hoặc 500mg IV mỗi 6 giờ",
            "adult_pseudomonas": "1g IV mỗi 6-8 giờ",
            "pediatric": "60-100mg/kg/ngày chia 4 lần (max 4g/ngày)",
            "notes": "Cilastatin bảo vệ imipenem khỏi bị phân hủy bởi dehydropeptidase. Phổ rộng nhất, nguy cơ co giật cao"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "500mg mỗi 8-12 giờ",
            "15_30": "500mg mỗi 12 giờ",
            "under_15": "250-500mg mỗi 12-24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Co giật (2-4%, đặc biệt suy thận, liều cao)",
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Giảm bạch cầu (hiếm)"
        ],
        "interactions": [
            "Valproic acid: giảm nồng độ valproic acid",
            "Ganciclovir: tăng nguy cơ co giật",
            "Probenecid: không dùng (cilastatin đã ức chế enzyme)"
        ],
        "monitoring": "Cảnh báo: Co giật - giảm liều hoặc đổi thuốc nếu có",
        "aware_classification": "WATCH",
        "pregnancy": "C"
    },
    
    # ========== LINCOSAMIDES ==========
    "Clindamycin": {
        "group": "Lincosamide",
        "vietnamese_name": "Clindamycin, Cleocin, Clindamycin",
        "administration": ["IV", "IM", "PO"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kỵ khí",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phổi do vi khuẩn kỵ khí",
            "Viêm nội tâm mạc do vi khuẩn kỵ khí",
            "Nhiễm khuẩn răng miệng",
            "Viêm mô tế bào"
        ],
        "contraindications": [
            "Dị ứng clindamycin",
            "Viêm đại tràng giả mạc trước đây"
        ],
        "dosage": {
            "adult_iv": "600-900mg IV mỗi 8 giờ",
            "adult_iv_severe": "900mg IV mỗi 8 giờ hoặc 600mg IV mỗi 6 giờ",
            "adult_im": "600mg IM mỗi 12 giờ",
            "adult_po": "150-450mg PO x 3-4 lần/ngày",
            "pediatric_iv": "20-40mg/kg/ngày chia 3-4 lần (max 4.5g/ngày)",
            "pediatric_po": "10-25mg/kg/ngày chia 3-4 lần",
            "notes": "Tốt chống vi khuẩn kỵ khí, đặc biệt Bacteroides. Nguy cơ viêm đại tràng giả mạc (C. difficile)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Viêm đại tràng giả mạc (C. difficile) - nguy hiểm",
            "Tiêu chảy",
            "Phát ban",
            "Viêm tĩnh mạch (IV)",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Neuromuscular blocking agents: tăng tê liệt",
            "Erythromycin: đối kháng (không dùng chung)"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== MACROLIDES - Erythromycin IV ==========
    "Erythromycin": {
        "group": "Macrolide",
        "vietnamese_name": "Erythromycin, Erythromycin, Erythrocin",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do Chlamydia, Mycoplasma, Legionella",
            "Nhiễm khuẩn đường hô hấp",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm nội tâm mạc do Streptococcus"
        ],
        "contraindications": [
            "Dị ứng erythromycin",
            "Rối loạn nhịp tim (QT kéo dài)",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_iv": "1-4g IV chia 4 lần/ngày",
            "adult_iv_standard": "500mg-1g IV mỗi 6 giờ",
            "adult_po": "250-500mg PO x 2-4 lần/ngày",
            "pediatric_iv": "20-50mg/kg/ngày chia 4 lần",
            "pediatric_po": "30-50mg/kg/ngày chia 3-4 lần",
            "notes": "Macrolide đầu tiên. Nguy cơ viêm tĩnh mạch cao (IV), QT kéo dài, tương tác nhiều"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Viêm tĩnh mạch (IV - rất thường gặp)",
            "QT kéo dài, rối loạn nhịp tim",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Rối loạn thính giác (liều cao)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu",
            "Cyclosporine: tăng nồng độ cyclosporine",
            "Digoxin: tăng nồng độ digoxin",
            "Theophylline: tăng nồng độ theophylline",
            "Statins: tăng nguy cơ tiêu cơ vân"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },
    
    # ========== OXAZOLIDINONES ==========
    "Linezolid": {
        "group": "Oxazolidinone",
        "vietnamese_name": "Linezolid, Zyvox, Linezolid",
        "administration": ["IV", "PO"],
        "indications": [
            "Nhiễm khuẩn do MRSA (da, mô mềm, phổi)",
            "Nhiễm khuẩn do VRE",
            "Viêm phổi bệnh viện do MRSA",
            "Nhiễm khuẩn da và mô mềm do MRSA"
        ],
        "contraindications": [
            "Dị ứng linezolid",
            "Dùng MAOIs (cách 2 tuần)",
            "Hội chứng serotonin (khi dùng SSRI/SNRI)"
        ],
        "dosage": {
            "adult_iv": "600mg IV mỗi 12 giờ",
            "adult_po": "600mg PO x 2 lần/ngày",
            "adult_severe": "600mg IV mỗi 12 giờ (không tăng liều)",
            "pediatric_iv": "10mg/kg IV mỗi 8-12 giờ (max 600mg/liều)",
            "pediatric_po": "10mg/kg PO x 2 lần/ngày (max 600mg/liều)",
            "notes": "Thuốc mới, đắt tiền. Chống MRSA/VRE. CẢNH BÁO: Nguy cơ ức chế tủy xương (giảm tiểu cầu) - không dùng >28 ngày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Giảm tiểu cầu (15-30% nếu dùng >14 ngày)",
            "Giảm bạch cầu (hiếm)",
            "Viêm dây thần kinh ngoại vi (dùng kéo dài)",
            "Tăng lactate máu (hiếm nhưng nặng)",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "SSRI/SNRI: hội chứng serotonin",
            "MAOIs: nguy hiểm",
            "Warfarin: tăng nguy cơ chảy máu",
            "Tyramine-rich foods: tăng huyết áp"
        ],
        "monitoring": "Bắt buộc: Huyết đồ 2 lần/tuần, lactate máu nếu có triệu chứng, ngừng nếu giảm tiểu cầu",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },
    
    # ========== STREPTOGRAMINS ==========
    "Quinupristin-Dalfopristin": {
        "group": "Streptogramin",
        "vietnamese_name": "Quinupristin-Dalfopristin, Synercid, Quinupristin-Dalfopristin",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn do VRE (Enterococcus faecium)",
            "Nhiễm khuẩn da và mô mềm do MRSA",
            "Nhiễm khuẩn do MRSA khi vancomycin thất bại"
        ],
        "contraindications": [
            "Dị ứng streptogramin",
            "Suy gan nặng"
        ],
        "dosage": {
            "adult_standard": "7.5mg/kg IV mỗi 8-12 giờ",
            "adult_severe": "7.5mg/kg IV mỗi 8 giờ",
            "pediatric": "7.5mg/kg IV mỗi 8-12 giờ",
            "notes": "Thuốc mới, đắt tiền. Chỉ hoạt động chống Enterococcus faecium (VRE), không hoạt động chống E. faecalis. Phải truyền qua central line"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "15_30": "Không đổi",
            "under_15": "Không đổi (thải qua gan)"
        },
        "side_effects": [
            "Viêm tĩnh mạch (thường gặp - phải dùng central line)",
            "Đau khớp, đau cơ (arthralgia, myalgia)",
            "Phát ban",
            "Tăng bilirubin, transaminase",
            "Buồn nôn, nôn"
        ],
        "interactions": [
            "Cyclosporine: tăng nồng độ cyclosporine",
            "CYP3A4 substrates: tăng nồng độ"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },
    
    # ========== POLYPEPTIDES - Colistin ==========
    "Colistin": {
        "group": "Polypeptide",
        "vietnamese_name": "Colistin, Colistin, Colistimethate",
        "administration": ["IV", "IM", "Inhalation"],
        "indications": [
            "Nhiễm khuẩn do MDR/XDR Gram âm (Pseudomonas, Acinetobacter)",
            "Viêm phổi bệnh viện do MDR",
            "Nhiễm khuẩn huyết do MDR",
            "Khi không còn lựa chọn khác"
        ],
        "contraindications": [
            "Dị ứng colistin",
            "Bệnh nhược cơ (myasthenia gravis)",
            "Suy thận nặng (phải điều chỉnh liều chặt chẽ)"
        ],
        "dosage": {
            "adult_iv_load": "6-9 triệu đơn vị (MU) IV loading, sau đó",
            "adult_iv_maintenance": "4.5-6 MU IV mỗi 12 giờ (theo CrCl)",
            "adult_iv_cmg": "2.5-5mg/kg (theo colistin base) IV mỗi 12 giờ",
            "adult_inhalation": "75-150mg (1-2 MU) x 2-3 lần/ngày",
            "pediatric_iv": "5mg/kg/ngày (theo colistin base) chia 2-3 lần",
            "notes": "Thuốc độc, chỉ dùng cuối cùng khi không còn lựa chọn. Phải tính liều theo CBA (colistin base activity) hoặc MU. Monitor độc thận/độc thần kinh chặt chẽ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50-75%",
            "under_15": "Giảm liều mạnh hoặc tránh"
        },
        "side_effects": [
            "Độc thận (30-50%) - nguy hiểm",
            "Độc thần kinh (paresthesia, rối loạn cảm giác, yếu cơ)",
            "Co giật (hiếm)",
            "Suy hô hấp (neuromuscular blockade)",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Neuromuscular blocking agents: tăng tê liệt",
            "Diuretics: tăng độc thận"
        ],
        "monitoring": "Bắt buộc: Creatinine hàng ngày, xét nghiệm thần kinh, cân nhắc TDM",
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },
}

