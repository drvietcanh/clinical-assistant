"""
Penicillins - Beta-lactam Antibiotics
"""

PENICILLINS = {
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

    "Piperacillin-Tazobactam": {
        "group": "Beta-lactam - Extended-spectrum Penicillin + Inhibitor",
        "vietnamese_name": "Piperacillin-Tazobactam, Tazocin, Pip-Taz, Zosyn, Pip-Tazo, Tazactam, Piprazid",
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
            "adult_extended": "4.5g IV mỗi 8 giờ (extended infusion 4 giờ) - IDSA 2024 HAP/VAP guidelines",
            "adult_sepsis": "4.5g IV mỗi 6 giờ hoặc extended infusion 4.5g mỗi 8 giờ",
            "adult_hap_vap": "4.5g IV mỗi 6 giờ hoặc 4.5g extended infusion mỗi 8 giờ - IDSA 2024",
            "pediatric": "112.5mg/kg (theo piperacillin) IV mỗi 8 giờ",
            "notes": "IDSA 2024 HAP/VAP: Extended infusion (4h) tối ưu hơn bolus trong nhiễm khuẩn nặng. Thường dùng kết hợp với aminoglycoside trong nhiễm khuẩn nghi ngờ Pseudomonas"
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

    "Oxacillin": {
        "group": "Beta-lactam - Penicillin (Anti-staphylococcal)",
        "vietnamese_name": "Oxacillin, Prostaphlin, Oxapen",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do MSSA (Methicillin-Sensitive S. aureus)",
            "Viêm tủy xương do tụ cầu",
            "Viêm nội tâm mạc do tụ cầu",
            "Nhiễm khuẩn da và mô mềm do tụ cầu",
            "Viêm phổi do tụ cầu"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Nhiễm khuẩn do MRSA (cần vancomycin/daptomycin)",
            "Nhiễm khuẩn do beta-hemolytic streptococci nhạy cảm (ưu tiên penicillin G)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 4-6 giờ (4-12g/ngày)",
            "adult_im": "500mg-1g IM mỗi 4-6 giờ",
            "pediatric_iv": "100-200mg/kg/ngày chia 4-6 lần",
            "meningitis_iv": "2g IV mỗi 4 giờ",
            "endocarditis_iv": "2g IV mỗi 4 giờ",
            "notes": "Không kháng MRSA - chỉ dùng cho MSSA. Liều cao cần truyền chậm (1-2 giờ)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "15_30": "Giảm liều 50%",
            "under_15": "1g mỗi 8 giờ"
        },
        "side_effects": [
            "Viêm tĩnh mạch (thường gặp)",
            "Tăng transaminase, vàng da (hiếm)",
            "Viêm thận kẽ (hiếm)",
            "Giảm bạch cầu, giảm tiểu cầu",
            "Phản ứng dị ứng"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ oxacillin",
            "Warfarin: có thể tăng tác dụng"
        ],
        "monitoring": "LFT (AST/ALT), công thức máu nếu điều trị dài ngày",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Flucloxacillin": {
        "group": "Beta-lactam - Penicillin (Anti-staphylococcal)",
        "vietnamese_name": "Flucloxacillin, Floxapen, Fluclocid",
        "administration": ["IV", "IM", "PO"],
        "indications": [
            "Nhiễm khuẩn do MSSA",
            "Viêm tủy xương do tụ cầu",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm phổi do tụ cầu"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "MRSA (không hiệu quả)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 6 giờ",
            "adult_im": "500mg-1g IM mỗi 6 giờ",
            "adult_po": "250-500mg PO mỗi 6 giờ",
            "pediatric_iv": "50-100mg/kg/ngày chia 4 lần",
            "pediatric_po": "25-50mg/kg/ngày chia 4 lần",
            "notes": "Hấp thu tốt qua đường uống, thường dùng để điều trị ngoại trú"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25%",
            "15_30": "Giảm liều 50%",
            "under_15": "500mg mỗi 8 giờ (IV/IM), 250mg PO mỗi 8 giờ"
        },
        "side_effects": [
            "Tiêu chảy (đường uống)",
            "Viêm tĩnh mạch (IV)",
            "Tăng transaminase",
            "Phản ứng dị ứng"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Nafcillin": {
        "group": "Beta-lactam - Penicillin (Anti-staphylococcal)",
        "vietnamese_name": "Nafcillin, Unipen, Nafcil",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn do MSSA (Methicillin-Sensitive S. aureus)",
            "Viêm nội tâm mạc do tụ cầu",
            "Viêm tủy xương do tụ cầu",
            "Viêm phổi do tụ cầu",
            "Nhiễm khuẩn da và mô mềm do tụ cầu"
        ],
        "contraindications": [
            "Dị ứng penicillin/nafcillin",
            "Sốc phản vệ với beta-lactam",
            "Nhiễm MRSA (cần vancomycin/daptomycin)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 4-6 giờ (4-12g/ngày)",
            "adult_iv_severe": "2g IV mỗi 4 giờ (12g/ngày) - viêm nội tâm mạc, nhiễm khuẩn nặng",
            "pediatric_iv": "50-200mg/kg/ngày chia 4-6 lần (tối đa 12g/ngày)",
            "meningitis_iv": "200-300mg/kg/ngày chia 4-6 lần",
            "notes": "Ưu tiên cho MSSA. Không dùng cho MRSA. Pha trong nước muối sinh lý hoặc D5W"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi (bài tiết chủ yếu qua gan)",
            "15_30": "Không đổi (bài tiết chủ yếu qua gan)",
            "under_15": "Không đổi (bài tiết chủ yếu qua gan)"
        },
        "side_effects": [
            "Viêm tĩnh mạch (phải dùng đường truyền lớn, pha loãng)",
            "Tăng bạch cầu ái toan",
            "Rối loạn chức năng gan (tăng transaminase)",
            "Giảm bạch cầu trung tính",
            "Phản ứng dị ứng"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ nafcillin",
            "Warfarin: giảm hiệu quả (cảm ứng CYP450)",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "monitoring": "Công thức máu, LFT, dấu hiệu viêm tĩnh mạch",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Amoxicillin": {
        "group": "Beta-lactam - Aminopenicillin (Oral)",
        "vietnamese_name": "Amoxicillin, Amoxil, Trimox, Amox, Amoxi, Amoxicil, Amoxipen, Amoxi-Cap",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng nhẹ",
            "Viêm tai giữa",
            "Viêm xoang cấp",
            "Viêm họng/amidan do liên cầu",
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "Nhiễm H. pylori (kết hợp)",
            "Phòng viêm nội tâm mạc"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Sốc phản vệ với beta-lactam",
            "Nhiễm trùng do beta-lactamase (dùng amoxicillin-clavulanate)"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 3 lần/ngày hoặc 500-875mg PO x 2 lần/ngày",
            "adult_severe": "875-1000mg PO x 2 lần/ngày",
            "adult_hpylori": "1g PO x 2 lần/ngày (kết hợp clarithromycin, PPI)",
            "pediatric_standard": "25-50mg/kg/ngày chia 3 lần (max 3g/ngày)",
            "pediatric_otitis": "80-90mg/kg/ngày chia 2-3 lần (max 3g/ngày)",
            "notes": "Phổ rộng hơn penicillin G. Dùng với thức ăn hoặc không. Hấp thu tốt (90%)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "500mg mỗi 12-24 giờ"
        },
        "side_effects": [
            "Tiêu chảy (5-10%)",
            "Buồn nôn, nôn",
            "Phát ban (đặc biệt trong bệnh tăng bạch cầu đơn nhân)",
            "Viêm đại tràng giả mạc (hiếm)",
            "Phản ứng dị ứng"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Allopurinol: tăng nguy cơ phát ban",
            "Oral contraceptives: giảm hiệu quả",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "LFT, công thức máu nếu dùng dài ngày",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

}

__all__ = ['PENICILLINS']
