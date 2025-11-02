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
}

