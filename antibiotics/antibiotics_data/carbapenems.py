"""
Carbapenems - Beta-lactam Antibiotics
"""

CARBAPENEMS = {
    "Meropenem": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Meropenem, Meronem, Meropen, Merrem, Mero, Meronam, Meropen, Mepenem",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn bệnh viện nặng",
            "Viêm phổi bệnh viện (HAP, VAP) - IDSA 2024",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Viêm màng não do vi khuẩn",
            "Nhiễm khuẩn đa kháng (MDR)",
            "Nhiễm khuẩn do ESBL-producing bacteria",
            "Nhiễm khuẩn do Pseudomonas aeruginosa (liều cao)",
            "Sốc nhiễm khuẩn (empiric therapy)"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng penicillin (phản ứng chéo cao 50%)"
        ],
        "dosage": {
            "adult_standard": "1g IV mỗi 8 giờ",
            "adult_severe": "1g IV mỗi 8 giờ hoặc 2g IV mỗi 8 giờ (nhiễm khuẩn rất nặng)",
            "adult_extended": "1g IV mỗi 8 giờ (extended infusion 3 giờ) - IDSA 2024 cho nhiễm khuẩn nặng/Pseudomonas",
            "adult_meningitis": "2g IV mỗi 8 giờ",
            "adult_pseudomonas": "2g IV mỗi 8 giờ (extended infusion 3h) - IDSA 2024",
            "adult_hap_vap": "1g IV mỗi 8 giờ hoặc extended infusion - IDSA 2024 HAP/VAP",
            "pediatric": "60mg/kg/ngày chia 3 lần (max 2g/liều)",
            "pediatric_meningitis": "120mg/kg/ngày chia 3 lần (max 2g/liều)",
            "notes": "IDSA 2024: Extended infusion (3h) tối ưu PK/PD, đặc biệt cho Pseudomonas và nhiễm khuẩn nặng. Standard infusion 30 phút hoặc bolus 5-20 phút. Phổ rộng nhất trong carbapenem"
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

    "Ertapenem": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Ertapenem, Invanz, Ertapen, Ertax, Ertam, Invance, Ertaz",
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

    "Meropenem-Vaborbactam": {
        "group": "Beta-lactam - Carbapenem + Beta-lactamase inhibitor",
        "vietnamese_name": "Meropenem-Vaborbactam, Vabomere, Meropenem-Vaborbactam",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn do CRE (Carbapenem-resistant Enterobacteriaceae)",
            "Viêm phổi bệnh viện do KPC",
            "Nhiễm khuẩn huyết do CRE",
            "Nhiễm khuẩn phức tạp ổ bụng"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng penicillin nặng"
        ],
        "dosage": {
            "adult_standard": "4g (2g meropenem + 2g vaborbactam) IV mỗi 8 giờ",
            "adult_renal_30_50": "2g IV mỗi 8 giờ",
            "adult_renal_15_30": "2g IV mỗi 12 giờ",
            "adult_renal_under_15": "1g IV mỗi 12 giờ",
            "notes": "Thuốc mới, đắt tiền. Chỉ dùng khi CRE được xác nhận hoặc nghi ngờ cao"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Giảm liều 50% và tăng interval",
            "under_15": "Giảm liều mạnh hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Co giật (hiếm, nếu suy thận)"
        ],
        "interactions": [
            "Valproic acid: giảm nồng độ valproic acid",
            "Probenecid: không dùng"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "C"
    },

    "Doripenem": {
        "group": "Beta-lactam - Carbapenem",
        "vietnamese_name": "Doripenem, Doribax",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Viêm phổi bệnh viện (HAP)",
            "Nhiễm khuẩn do ESBL-producing Enterobacteriaceae",
            "Nhiễm khuẩn do P. aeruginosa"
        ],
        "contraindications": [
            "Dị ứng carbapenem/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "500mg IV mỗi 8 giờ (1.5g/ngày)",
            "severe_iv": "1g IV mỗi 8 giờ (3g/ngày)",
            "pediatric_iv": "Không khuyến cáo cho trẻ <18 tuổi",
            "notes": "Truyền IV trong 1-4 giờ (truyền chậm hơn Meropenem). Phổ rộng nhưng ít tác dụng phụ hơn Imipenem"
        },
        "renal_adjustment": {
            "normal": "500mg mỗi 8 giờ",
            "30_60": "250mg mỗi 8 giờ",
            "15_30": "250mg mỗi 12 giờ",
            "under_15": "250mg mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Đau đầu",
            "Buồn nôn",
            "Phát ban",
            "Co giật (hiếm, ít hơn Imipenem)"
        ],
        "interactions": [
            "Valproic acid: giảm nồng độ valproic acid đáng kể",
            "Probenecid: tăng nồng độ doripenem"
        ],
        "monitoring": "Theo dõi co giật ở bệnh nhân có nguy cơ",
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

}

__all__ = ['CARBAPENEMS']
