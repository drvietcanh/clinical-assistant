"""
Cephalosporins - Beta-lactam Antibiotics
"""

CEPHALOSPORINS = {
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
        "vietnamese_name": "Ceftriaxone, Rocephin, Oritaxim, Cefaxone, Triaxone, Ceftri, Rophin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn huyết",
            "Viêm màng não",
            "Viêm phổi cộng đồng (CAP)",
            "Viêm phổi bệnh viện (HAP) - nhẹ đến trung bình",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Viêm xương tủy",
            "Nhiễm khuẩn ổ bụng (phối hợp metronidazole)",
            "Bệnh lậu (Neisseria gonorrhoeae)",
            "Bệnh Lyme (Borrelia burgdorferi)",
            "Sốt thương hàn (Salmonella typhi)"
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
        "vietnamese_name": "Ceftazidime, Fortum, Tazidime, Cefpime, Fortaz, Ceftaz",
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
        "vietnamese_name": "Cefepime, Maxipime, Cefepim, Maxipim, Cefomax, Cepime, Cefepimax, Cepim",
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

    "Ceftazidime-Avibactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ceftazidime-Avibactam, Avycaz, Zavicefta, Avibactam, Zavi, Ceftaz-Avi",
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

    "Cephalexin": {
        "group": "Beta-lactam - Cephalosporin thế hệ 1",
        "vietnamese_name": "Cephalexin, Keflex, Cephalexin",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn răng miệng"
        ],
        "contraindications": [
            "Dị ứng cephalosporin (phản ứng chéo với penicillin)",
            "Sốc phản vệ với beta-lactam"
        ],
        "dosage": {
            "adult_po": "250-500mg PO x 4 lần/ngày",
            "adult_severe": "500mg-1g PO x 4 lần/ngày",
            "pediatric_po": "25-50mg/kg/ngày chia 4 lần",
            "notes": "Cephalosporin PO thông dụng nhất. Không có dạng IV"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh hoặc tránh"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Buồn nôn",
            "Nhiễm nấm Candida"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cefadroxil": {
        "group": "Beta-lactam - Cephalosporin thế hệ 1",
        "vietnamese_name": "Cefadroxil, Cefadroxil, Duricef",
        "administration": ["PO"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường hô hấp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Sốc phản vệ với beta-lactam"
        ],
        "dosage": {
            "adult_po": "1-2g PO x 1-2 lần/ngày",
            "pediatric_po": "30mg/kg/ngày chia 2 lần",
            "notes": "Dùng 1-2 lần/ngày (thuận tiện hơn Cephalexin)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "Giảm liều mạnh"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phát ban",
            "Buồn nôn"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Ceftolozane-Tazobactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Ceftolozane-Tazobactam, Zerbaxa, Ceftolozane-Tazobactam",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn bệnh viện do P. aeruginosa MDR",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn đường tiết niệu phức tạp"
        ],
        "contraindications": [
            "Dị ứng cephalosporin",
            "Dị ứng penicillin nặng (phản ứng chéo)"
        ],
        "dosage": {
            "adult_standard": "1.5g (1g ceftolozane + 0.5g tazobactam) IV mỗi 8 giờ",
            "adult_renal_30_50": "750mg IV mỗi 8 giờ",
            "adult_renal_15_30": "375mg IV mỗi 8 giờ",
            "adult_renal_under_15": "Loading 750mg, sau đó 375mg mỗi 8 giờ",
            "pediatric": "30mg/kg (theo ceftolozane) IV mỗi 8 giờ",
            "notes": "Thuốc mới, rất tốt chống P. aeruginosa. Đắt tiền. Cần điều chỉnh liều theo CrCl"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Giảm liều 75%",
            "under_15": "Giảm liều mạnh hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng transaminase"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ"
        ],
        "aware_classification": "RESERVE",
        "pregnancy": "B"
    },

    "Cefoperazone": {
        "group": "Beta-lactam - Cephalosporin (3rd gen)",
        "vietnamese_name": "Cefoperazone, Cefobid, Cefobact",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu",
            "Nhiễm khuẩn đường hô hấp",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn ổ bụng (phối hợp metronidazole)",
            "Nhiễm khuẩn do P. aeruginosa"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Tiền sử sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "2g IV mỗi 8-12 giờ (4-6g/ngày)",
            "adult_im": "1-2g IM mỗi 12 giờ",
            "pediatric_iv": "50-200mg/kg/ngày chia 2-4 lần",
            "severe_iv": "3-4g IV mỗi 8 giờ (9-12g/ngày)",
            "notes": "Bài tiết qua mật cao - ưu điểm trong nhiễm khuẩn đường mật"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "1-2g mỗi 12 giờ (không cần điều chỉnh nhiều do bài tiết mật)"
        },
        "side_effects": [
            "Rối loạn đông máu (hypoprothrombinemia) - bổ sung vitamin K",
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch",
            "Phản ứng disulfiram nếu uống rượu"
        ],
        "interactions": [
            "Rượu: phản ứng giống disulfiram (đỏ mặt, nôn, tim đập nhanh)",
            "Warfarin: tăng nguy cơ chảy máu (cần theo dõi PT/INR)",
            "Heparin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "PT/INR, đông máu trong điều trị dài ngày",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Cefoperazone-Sulbactam": {
        "group": "Beta-lactam - Cephalosporin + Beta-lactamase inhibitor",
        "vietnamese_name": "Cefoperazone-Sulbactam, Sulperazone, Cefazone-S, Sulzone, Cefpera-S, Sulcef, Cefoperazone-Sul",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn bệnh viện (HAP, VAP)",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn do vi khuẩn kháng beta-lactamase",
            "Nhiễm khuẩn do P. aeruginosa"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "2g-1g (Cefoperazone-Sulbactam) IV mỗi 8-12 giờ",
            "adult_im": "1g-0.5g IM mỗi 12 giờ",
            "pediatric_iv": "40-80mg/kg/ngày (tính theo Cefoperazone) chia 2-3 lần",
            "severe_iv": "3g-1.5g IV mỗi 8 giờ",
            "notes": "Tỷ lệ 2:1 (Cefoperazone:Sulbactam), phổ rộng hơn Cefoperazone đơn"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "1g-0.5g mỗi 12 giờ"
        },
        "side_effects": [
            "Rối loạn đông máu (giống Cefoperazone)",
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram",
            "Warfarin: tăng nguy cơ chảy máu",
            "Vitamin K: bổ sung nếu điều trị dài ngày"
        ],
        "monitoring": "PT/INR, đông máu",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Ceftizoxime": {
        "group": "Beta-lactam - Cephalosporin (3rd Generation)",
        "vietnamese_name": "Ceftizoxime, Cefizox",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn đường hô hấp dưới",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn ổ bụng (phối hợp metronidazole)",
            "Nhiễm khuẩn phụ khoa"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 8-12 giờ (2-4g/ngày)",
            "adult_im": "1-2g IM mỗi 8-12 giờ",
            "pediatric_iv": "50-150mg/kg/ngày chia 3-4 lần (tối đa 6g/ngày)",
            "adult_iv_severe": "2g IV mỗi 8 giờ (6g/ngày)",
            "notes": "Phổ hoạt động tương tự ceftriaxone, nhưng không có tác dụng kéo dài"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 12 giờ",
            "15_30": "0.5-1g mỗi 12 giờ",
            "under_15": "0.5-1g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Phản ứng dị ứng",
            "Tiêu chảy",
            "Viêm tĩnh mạch",
            "Rối loạn chức năng gan nhẹ"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ceftizoxime",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "LFT, công thức máu",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Cefotetan": {
        "group": "Beta-lactam - Cephamycin",
        "vietnamese_name": "Cefotetan, Cefotan",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng (phẫu thuật)",
            "Nhiễm khuẩn phụ khoa",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Phẫu thuật đại tràng (prophylaxis)",
            "Nhiễm khuẩn do vi khuẩn kỵ khí + gram âm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam",
            "Phụ nữ có thai (chống chỉ định)"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 12 giờ (2-4g/ngày)",
            "adult_im": "1-2g IM mỗi 12 giờ",
            "prophylaxis_iv": "1-2g IV trước phẫu thuật",
            "adult_iv_severe": "2g IV mỗi 12 giờ (4g/ngày)",
            "notes": "Phổ rộng bao gồm kỵ khí. Có disulfiram-like effect. Chống chỉ định thai kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 24 giờ",
            "15_30": "1-2g mỗi 24 giờ",
            "under_15": "0.5-1g mỗi 24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Phản ứng disulfiram (rượu)",
            "Rối loạn đông máu (hypoprothrombinemia)",
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Rượu: phản ứng disulfiram (đỏ mặt, nôn, tim đập nhanh)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Vitamin K: cần bổ sung trong điều trị dài ngày"
        ],
        "monitoring": "PT/INR, dấu hiệu chảy máu",
        "aware_classification": "WATCH",
        "pregnancy": "X - Chống chỉ định trong thai kỳ (gây quái thai trong thí nghiệm)",
        "notes": "Chống chỉ định thai kỳ. Phản ứng disulfiram với rượu. Phổ kỵ khí tốt"
    },

    "Cefoxitin": {
        "group": "Beta-lactam - Cephamycin",
        "vietnamese_name": "Cefoxitin, Mefoxin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn phụ khoa",
            "Viêm nội mạc tử cung",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn da và mô mềm có kỵ khí",
            "Phẫu thuật đại tràng (prophylaxis)"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "1-2g IV mỗi 6-8 giờ (3-8g/ngày)",
            "adult_im": "1-2g IM mỗi 6-8 giờ",
            "prophylaxis_iv": "1-2g IV trước phẫu thuật",
            "adult_iv_severe": "2g IV mỗi 6 giờ (8g/ngày)",
            "pediatric_iv": "80-160mg/kg/ngày chia 4-6 lần (tối đa 12g/ngày)",
            "notes": "Phổ rộng bao gồm kỵ khí. Tương tự cefotetan nhưng an toàn hơn trong thai kỳ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g mỗi 8-12 giờ",
            "15_30": "1-2g mỗi 12 giờ",
            "under_15": "0.5-1g mỗi 12-24 giờ hoặc lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Phản ứng dị ứng",
            "Viêm tĩnh mạch",
            "Rối loạn chức năng gan nhẹ"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ cefoxitin",
            "Warfarin: tăng nguy cơ chảy máu (ít hơn cefotetan)"
        ],
        "monitoring": "LFT, công thức máu",
        "aware_classification": "WATCH",
        "pregnancy": "B"
    },

    "Ceftobiprole": {
        "group": "Beta-lactam - Cephalosporin (5th Generation)",
        "vietnamese_name": "Ceftobiprole, Zevtera, Mabelio",
        "administration": ["IV"],
        "indications": [
            "Viêm phổi bệnh viện (HAP)",
            "Viêm phổi thở máy (VAP)",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "MRSA (Methicillin-Resistant S. aureus)",
            "Nhiễm khuẩn do P. aeruginosa",
            "Nhiễm khuẩn do vi khuẩn gram dương và gram âm"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam"
        ],
        "dosage": {
            "adult_iv": "500mg IV mỗi 8 giờ (truyền trong 2 giờ)",
            "adult_iv_severe": "500mg IV mỗi 8 giờ",
            "notes": "Phổ rộng bao gồm MRSA và P. aeruginosa. Phải truyền trong 2 giờ (không bolus)"
        },
        "renal_adjustment": {
            "normal": "500mg mỗi 8 giờ",
            "30_60": "500mg mỗi 12 giờ",
            "15_30": "250mg mỗi 12 giờ",
            "under_15": "250mg mỗi 24 giờ hoặc lọc máu (liều sau lọc máu)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phản ứng dị ứng",
            "Rối loạn vị giác",
            "Viêm tĩnh mạch"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ ceftobiprole",
            "Warfarin: tăng nguy cơ chảy máu (theo dõi PT/INR)"
        ],
        "monitoring": "LFT, công thức máu, dấu hiệu nhiễm trùng",
        "aware_classification": "RESERVE",
        "pregnancy": "B - Dữ liệu hạn chế nhưng không thấy nguy cơ rõ ràng",
        "notes": "Cephalosporin thế hệ 5, phổ rộng bao gồm MRSA và P. aeruginosa. Phải truyền trong 2 giờ (không bolus)"
    },

    "Cefixime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 3 (Oral)",
        "vietnamese_name": "Cefixime, Suprax, Cefix, Cefim, Fixime, Cefspan, Cefixoral, Cefixon",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng nhẹ-trung bình",
            "Viêm tai giữa",
            "Viêm họng/amidan do liên cầu",
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "Bệnh lậu không biến chứng",
            "Nhiễm khuẩn đường hô hấp trên"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Sốc phản vệ beta-lactam",
            "Trẻ sơ sinh < 6 tháng"
        ],
        "dosage": {
            "adult_standard": "400mg PO x 1 lần/ngày hoặc 200mg PO x 2 lần/ngày",
            "adult_severe": "400mg PO x 2 lần/ngày",
            "adult_gonorrhea": "400mg PO x 1 liều",
            "pediatric_standard": "8mg/kg/ngày chia 1-2 lần (max 400mg/ngày)",
            "pediatric_otitis": "8-16mg/kg/ngày chia 1-2 lần",
            "notes": "Dùng với thức ăn hoặc không, hấp thu tốt. Phổ rộng hơn cephalexin"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25% hoặc dùng mỗi 12-24h",
            "15_30": "Giảm liều 50%",
            "under_15": "200mg mỗi 24 giờ"
        },
        "side_effects": [
            "Tiêu chảy (10-20%)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Phát ban",
            "Nhức đầu"
        ],
        "interactions": [
            "Antacids: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "monitoring": "LFT, công thức máu (nếu dùng dài ngày)",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cefdinir": {
        "group": "Beta-lactam - Cephalosporin thế hệ 3 (Oral)",
        "vietnamese_name": "Cefdinir, Omnicef, Cefdin, Cednir, Cefd, Cefdine, Cefdix, Cefdinex",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng nhẹ-trung bình",
            "Viêm tai giữa",
            "Viêm xoang cấp",
            "Viêm họng/amidan do liên cầu",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu không biến chứng"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Trẻ sơ sinh < 6 tháng"
        ],
        "dosage": {
            "adult_standard": "300mg PO x 2 lần/ngày hoặc 600mg PO x 1 lần/ngày",
            "adult_otitis_sinus": "300mg PO x 2 lần/ngày",
            "pediatric_standard": "14mg/kg/ngày chia 1-2 lần (max 600mg/ngày)",
            "pediatric_otitis": "14mg/kg/ngày chia 2 lần (max 300mg/liều)",
            "notes": "Hấp thu tốt, không bị ảnh hưởng bởi thức ăn. Phổ rộng bao gồm H. influenzae"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "300mg mỗi 24 giờ",
            "15_30": "300mg mỗi 24 giờ",
            "under_15": "300mg mỗi 24-48 giờ"
        },
        "side_effects": [
            "Tiêu chảy (3-8%)",
            "Buồn nôn",
            "Đau đầu",
            "Phát ban",
            "Nhiễm nấm âm đạo (phụ nữ)"
        ],
        "interactions": [
            "Sắt: giảm hấp thu (cách 2 giờ)",
            "Antacids: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "LFT nếu dùng dài ngày",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cefaclor": {
        "group": "Beta-lactam - Cephalosporin thế hệ 2 (Oral)",
        "vietnamese_name": "Cefaclor, Ceclor, Cefaclor, Cefador, Cefalor, Ceclor, Cefac, Cefaclorin",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng nhẹ",
            "Viêm tai giữa",
            "Viêm xoang cấp",
            "Viêm họng/amidan",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin"
        ],
        "dosage": {
            "adult_standard": "250-500mg PO x 3 lần/ngày",
            "adult_severe": "500mg PO x 3 lần/ngày",
            "pediatric_standard": "20-40mg/kg/ngày chia 3 lần (max 1g/ngày)",
            "pediatric_otitis": "40mg/kg/ngày chia 3 lần",
            "notes": "Cephalosporin thế hệ 2, phổ trung bình. Dùng với thức ăn để giảm khó chịu dạ dày"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "15_30": "Giảm liều 50%",
            "under_15": "250mg mỗi 12-24 giờ"
        },
        "side_effects": [
            "Tiêu chảy (2-3%)",
            "Buồn nôn, nôn",
            "Phát ban",
            "Nhức đầu",
            "Rối loạn chức năng gan (hiếm)"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "monitoring": "LFT nếu có triệu chứng",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

    "Cefpodoxime": {
        "group": "Beta-lactam - Cephalosporin thế hệ 3 (Oral)",
        "vietnamese_name": "Cefpodoxime, Vantin, Cefpodox, Podoxime, Cefpomax, Cefpod, Cefpodoxine",
        "administration": ["PO"],
        "indications": [
            "Viêm phổi cộng đồng nhẹ-trung bình",
            "Viêm tai giữa",
            "Viêm xoang cấp",
            "Nhiễm khuẩn đường tiết niệu không biến chứng",
            "Nhiễm khuẩn da và mô mềm",
            "Viêm họng/amidan do liên cầu"
        ],
        "contraindications": [
            "Dị ứng cephalosporin/penicillin",
            "Trẻ sơ sinh < 2 tháng"
        ],
        "dosage": {
            "adult_standard": "200mg PO x 2 lần/ngày",
            "adult_severe": "400mg PO x 2 lần/ngày",
            "adult_uti": "100mg PO x 2 lần/ngày",
            "pediatric_standard": "10mg/kg/ngày chia 2 lần (max 400mg/ngày)",
            "pediatric_otitis": "10mg/kg/ngày chia 2 lần (max 400mg/ngày)",
            "notes": "Dùng với thức ăn để tăng hấp thu. Phổ rộng bao gồm H. influenzae, Moraxella"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50%",
            "15_30": "Giảm liều 50%",
            "under_15": "100mg mỗi 24 giờ"
        },
        "side_effects": [
            "Tiêu chảy (7-15%)",
            "Buồn nôn, nôn",
            "Đau bụng",
            "Phát ban",
            "Nhức đầu"
        ],
        "interactions": [
            "Antacids: giảm hấp thu (cách 2 giờ)",
            "Warfarin: tăng nguy cơ chảy máu",
            "Probenecid: tăng nồng độ"
        ],
        "monitoring": "LFT nếu dùng dài ngày",
        "aware_classification": "ACCESS",
        "pregnancy": "B"
    },

}

__all__ = ['CEPHALOSPORINS']
