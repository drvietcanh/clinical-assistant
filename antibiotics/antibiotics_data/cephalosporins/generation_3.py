"""
Cephalosporins - Generation 3
"""

GENERATION_3 = {
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

