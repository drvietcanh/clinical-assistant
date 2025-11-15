"""
Beta-lactam Antibiotics
Penicillin/Beta-lactamase Inhibitor and Carbapenem
"""

BETA_LACTAM_ANTIBIOTICS = {
    "Piperacillin-tazobactam": {
    "group": "Antibiotic - Penicillin/Beta-lactamase Inhibitor",
    "vietnamese_name": "Piperacillin-tazobactam, Tazocin, Zosyn",
    "administration": ["IV"],
    "indications": [
        "Nhiễm khuẩn nặng (bệnh viện)",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm phổi bệnh viện",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn huyết"
    ],
    "contraindications": [
        "Dị ứng penicillin",
        "Dị ứng beta-lactam"
    ],
    "dosage": {
        "adult_standard": "4.5g IV mỗi 8 giờ",
        "adult_severe": "4.5g IV mỗi 6 giờ",
        "adult_nosocomial_pneumonia": "4.5g IV mỗi 6 giờ",
        "notes": "Liều tối đa: 18g/ngày. Pha trong 50-150ml NS hoặc D5W, truyền trong 30 phút"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "4.5g IV mỗi 8 giờ",
        "under_30": "2.25g IV mỗi 8 giờ",
        "hemodialysis": "2.25g IV mỗi 8 giờ (sau lọc máu)"
    },
    "side_effects": [
        "Tiêu chảy",
        "Buồn nôn, nôn",
        "Phát ban",
        "Tăng men gan",
        "Giảm tiểu cầu (hiếm)",
        "Giảm bạch cầu (hiếm)"
    ],
    "interactions": [
        "Warfarin: có thể tăng INR",
        "Aminoglycosides: không pha chung, truyền riêng"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Piperacillin: penicillin phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Tazobactam: beta-lactamase inhibitor, bảo vệ piperacillin khỏi bị phân hủy bởi beta-lactamase (TEM, SHV, OXA). Kết hợp này mở rộng phổ kháng khuẩn, đặc biệt hiệu quả với Pseudomonas aeruginosa, Enterobacteriaceae (bao gồm một số ESBL), và kỵ khí. Tazobactam không có hoạt tính kháng khuẩn riêng, chỉ có tác dụng bảo vệ.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Điện giải (natri - mỗi 4.5g chứa 2.79 mEq natri, kali - có thể tăng)",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Thời gian prothrombin/PT (hiếm giảm prothrombin)",
            "Số lượng tiểu cầu (hiếm giảm tiểu cầu)",
            "Đường huyết (có thể tăng hoặc giảm)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - đặc biệt quan trọng",
            "Hàm lượng natri cao (2.79 mEq/4.5g) - thận trọng ở suy tim, tăng huyết áp, phù",
            "Không dùng ở bệnh nhân dị ứng penicillins (phản ứng chéo cao)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Có thể gây giảm prothrombin → tăng nguy cơ chảy máu, đặc biệt ở suy thận, suy gan, dùng kéo dài",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút (liều chuẩn) hoặc 3-4 giờ (liều cao/extended infusion)",
            "Extended infusion (3-4 giờ) được khuyến cáo cho Pseudomonas aeruginosa để tối ưu hóa pharmacokinetics/pharmacodynamics (PK/PD)",
            "Không pha trộn với vancomycin (tạo kết tủa)"
        ],
        "pharmacokinetics": {
            "half_life": "0.7-1.2 giờ (piperacillin), 0.7-1 giờ (tazobactam)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 4.5g q6h hoặc q8h, extended infusion q8h",
            "protein_binding": "30% (piperacillin), 20-30% (tazobactam)",
            "metabolism": "Piperacillin: thủy phân một phần, tazobactam: thủy phân",
            "clearance": "Chủ yếu qua thận (68% piperacillin, 80% tazobactam bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, hàm lượng natri cao có thể gây vấn đề ở bệnh nhân suy tim hoặc cần hạn chế natri. Giảm prothrombin có thể gây chảy máu nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Piperacillin-tazobactam có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K. Ngoài ra, có thể ức chế chuyển hóa warfarin.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu, đặc biệt ở bệnh nhân suy thận, suy gan, dùng kéo dài",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng piperacillin-tazobactam). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân suy thận, suy gan, dùng kéo dài (>7 ngày)."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Piperacillin có thể ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính (giảm bạch cầu, độc thận, viêm niêm mạc)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ nồng độ methotrexate, công thức máu, chức năng thận. Có thể cần giảm liều methotrexate hoặc tăng khoảng cách giữa các liều."
                }
            ],
            "moderate": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Ngoài ra, aminoglycosides có thể bị bất hoạt về mặt hóa học bởi beta-lactams khi pha chung.",
                    "effect": "Tăng nguy cơ độc thận, giảm hiệu quả kháng khuẩn của aminoglycosides nếu pha chung",
                    "management": "Không pha chung trong cùng một ống truyền. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ (creatinine, BUN). Có thể cần giảm liều hoặc tăng khoảng cách giữa các liều."
                },
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn. Ngoài ra, có thể tạo kết tủa khi pha chung.",
                    "effect": "Tăng nguy cơ độc thận, kết tủa khi pha chung",
                    "management": "Không pha chung. Truyền riêng biệt. Theo dõi chức năng thận chặt chẽ. Theo dõi nồng độ vancomycin nếu có thể."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của piperacillin, làm giảm thải trừ và tăng nồng độ piperacillin.",
                    "effect": "Tăng nồng độ piperacillin, tăng thời gian bán thải",
                    "management": "Có thể cần giảm liều piperacillin-tazobactam. Theo dõi chức năng thận. Thường không cần điều chỉnh liều thường quy."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc tránh thai đường uống",
                    "mechanism": "Kháng sinh phổ rộng có thể làm giảm hệ vi khuẩn đường ruột, làm giảm tái hấp thu estrogen từ đường ruột.",
                    "effect": "Giảm hiệu quả thuốc tránh thai (hiếm, nhưng có thể xảy ra)",
                    "management": "Khuyến cáo sử dụng biện pháp tránh thai bổ sung (bao cao su) trong khi dùng kháng sinh và 7 ngày sau khi ngừng."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng penicillin hoặc beta-lactam (phản ứng type I - sốc phản vệ, phù mạch, phát ban nặng)",
                "Dị ứng tazobactam",
                "Tiền sử phản ứng dị ứng nặng với beta-lactam (penicillin, cephalosporin, carbapenem)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <20) - cần giảm liều đáng kể, theo dõi chặt chẽ",
                "Suy tim, phù, tăng huyết áp - hàm lượng natri cao (2.79 mEq/4.5g) có thể làm nặng thêm tình trạng",
                "Suy gan nặng - tăng nguy cơ giảm prothrombin và chảy máu",
                "Rối loạn đông máu - tăng nguy cơ chảy máu do giảm prothrombin",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Piperacillin-tazobactam là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Penicillins nói chung được coi là an toàn trong thai kỳ và được sử dụng rộng rãi. Piperacillin-tazobactam có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn nặng. Tuy nhiên, cần thận trọng với hàm lượng natri cao và nguy cơ giảm prothrombin. Nên tránh dùng kéo dài nếu có thể.",
            "lactation": {
                "safety": "Compatible",
                "details": "Piperacillin và tazobactam bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Penicillins nói chung được coi là an toàn khi cho con bú.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Piperacillin và tazobactam không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
            "moderate": "Không cần điều chỉnh liều. Tuy nhiên, cần thận trọng với nguy cơ giảm prothrombin và chảy máu. Theo dõi PT/INR.",
            "severe": "Không cần điều chỉnh liều. Tuy nhiên, tăng nguy cơ giảm prothrombin và chảy máu. Theo dõi PT/INR chặt chẽ. Có thể cần bổ sung vitamin K hoặc điều chỉnh liều thuốc chống đông nếu đang dùng.",
            "notes": "Piperacillin và tazobactam không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận (68% piperacillin, 80% tazobactam bài tiết nguyên dạng). Không cần điều chỉnh liều ở bệnh nhân suy gan. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận. Ngoài ra, suy gan làm tăng nguy cơ giảm prothrombin và chảy máu, cần theo dõi PT/INR."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao)",
                "Triệu chứng điện giải: Tăng natri máu (do hàm lượng natri cao), rối loạn điện giải",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (do giảm prothrombin)",
                "Triệu chứng thận: Suy thận cấp, tăng creatinine (hiếm với liều thông thường)",
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, buồn nôn, nôn",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay piperacillin-tazobactam",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều chỉnh điện giải: Điều chỉnh natri máu nếu tăng natri, bù dịch phù hợp",
                "Điều trị chảy máu:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều thuốc chống đông nếu đang dùng",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ piperacillin và tazobactam)",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ piperacillin và tazobactam nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi dấu hiệu thần kinh (co giật, ý thức), điện giải (natri, kali), PT/INR, chức năng thận (creatinine, BUN, lượng nước tiểu), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có suy thận cấp hoặc rối loạn đông máu."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng - chỉ có dạng IV",
                "timing": "Không áp dụng - chỉ có dạng IV"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 50-150ml cho liều 4.5g. Nồng độ pha: 90mg/ml (4.5g/50ml) đến 30mg/ml (4.5g/150ml). Pha 4.5g trong 50ml = 90mg/ml. Pha 4.5g trong 100ml = 45mg/ml. Pha 4.5g trong 150ml = 30mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Liều chuẩn (4.5g q6h hoặc q8h): Truyền trong 30 phút. Extended infusion (4.5g q8h trong 3-4 giờ): Được khuyến cáo cho Pseudomonas aeruginosa để tối ưu hóa PK/PD. Tốc độ: 50ml/30 phút = ~1.7ml/phút (liều chuẩn), 50ml/3-4 giờ = ~0.25-0.33ml/phút (extended infusion).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Vancomycin - tạo kết tủa, không pha chung",
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Không pha chung với vancomycin (tạo kết tủa), 2) Không pha chung với aminoglycosides (truyền riêng biệt), 3) Điều chỉnh liều theo CrCl, 4) Hàm lượng natri cao (2.79 mEq/4.5g) - thận trọng ở suy tim, 5) Extended infusion (3-4 giờ) được khuyến cáo cho Pseudomonas aeruginosa, 6) Theo dõi PT/INR ở bệnh nhân suy thận, suy gan, dùng kéo dài."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Piperacillin-Tazobactam (Zosyn)",
                "UpToDate - Piperacillin-Tazobactam: Drug Information",
                "Medscape - Piperacillin-Tazobactam Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Piperacillin-Tazobactam Monograph",
                "Micromedex - Piperacillin-Tazobactam Drug Information",
                "IDSA Guidelines - Hospital-Acquired Pneumonia, Intra-abdominal Infections"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }

    },

    "Meropenem": {
    "group": "Antibiotic - Carbapenem",
    "vietnamese_name": "Meropenem, Meronem",
    "administration": ["IV"],
    "indications": [
        "Nhiễm khuẩn nặng đa kháng",
        "Nhiễm khuẩn bệnh viện",
        "Viêm màng não",
        "Nhiễm khuẩn ổ bụng",
        "Nhiễm khuẩn huyết"
    ],
    "contraindications": [
        "Dị ứng carbapenem",
        "Dị ứng beta-lactam nặng"
    ],
    "dosage": {
        "adult_standard": "1g IV mỗi 8 giờ",
        "adult_severe": "1g IV mỗi 6 giờ hoặc 2g IV mỗi 8 giờ",
        "adult_meningitis": "2g IV mỗi 8 giờ",
        "notes": "Truyền trong 15-30 phút. Phổ rộng, dự phòng kháng penicillinase"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "1g IV mỗi 12 giờ",
        "under_30": "500mg-1g IV mỗi 12 giờ",
        "hemodialysis": "500mg-1g IV mỗi 12 giờ (sau lọc máu)"
    },
    "side_effects": [
        "Tiêu chảy",
        "Phát ban",
        "Co giật (liều cao, suy thận)",
        "Tăng men gan",
        "Viêm tĩnh mạch tại chỗ tiêm"
    ],
    "interactions": [
        "Valproate: giảm nồng độ valproate (có thể gây co giật)",
        "Probenecid: tăng nồng độ meropenem"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Carbapenem kháng sinh beta-lactam. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), đặc biệt PBP-2, dẫn đến ly giải tế bào vi khuẩn. Phổ kháng khuẩn rộng, bao phủ cả vi khuẩn Gram-dương, Gram-âm, và kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Đặc biệt hiệu quả với Enterobacteriaceae (bao gồm ESBL-producing), Pseudomonas aeruginosa, và kỵ khí.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP, procalcitonin)",
            "Cấy máu và cấy từ vị trí nhiễm trùng để đánh giá đáp ứng",
            "Dấu hiệu nhiễm trùng thứ phát (nấm, C. difficile)",
            "Co giật (nguy cơ tăng ở suy thận, bệnh thần kinh trung ương)",
            "Chức năng gan (ALT, AST) - hiếm nhưng có thể tăng",
            "Số lượng tiểu cầu (hiếm giảm tiểu cầu)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - giảm liều và tăng khoảng cách liều",
            "Nguy cơ co giật tăng ở: suy thận nặng (CrCl < 25), bệnh thần kinh trung ương, tiền sử co giật",
            "Không dùng ở bệnh nhân dị ứng penicillins hoặc cephalosporins (phản ứng chéo ~1%)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy, phân lỏng",
            "Có thể gây kháng thuốc nếu dùng không đúng chỉ định - chỉ dùng khi thực sự cần",
            "Theo dõi nhiễm nấm thứ phát (đặc biệt Candida) khi dùng kéo dài",
            "Pha trong dung dịch NS hoặc D5W, truyền IV trong 15-30 phút",
            "Không pha trộn với các thuốc khác (có thể tương kỵ)"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (bình thường), 1.5-2.5 giờ (suy thận)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 1g q8h đạt nồng độ hiệu quả",
            "protein_binding": "2% (rất thấp)",
            "metabolism": "Thủy phân trong gan (40%), không qua CYP450",
            "clearance": "Chủ yếu qua thận (70% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 2-4 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ co giật tăng ở suy thận nặng và bệnh nhân có tiền sử co giật. Kháng thuốc có thể phát triển nếu dùng không đúng chỉ định.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate (Valproic acid)",
                    "mechanism": "Meropenem ức chế hấp thu và tăng thải trừ valproate, làm giảm nồng độ valproate trong máu đáng kể (có thể giảm 50-70%).",
                    "effect": "Giảm nồng độ valproate, mất kiểm soát co giật, nguy cơ co giật nặng",
                    "management": "TRÁNH dùng cùng nếu có thể. Nếu bắt buộc: tăng liều valproate, theo dõi nồng độ valproate trong máu thường xuyên, cân nhắc dùng thuốc chống co giật khác. Theo dõi chặt chẽ dấu hiệu co giật."
                },
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết meropenem qua thận, làm tăng nồng độ và thời gian bán thải của meropenem.",
                    "effect": "Tăng nồng độ meropenem, tăng nguy cơ tác dụng phụ (co giật, độc tính thần kinh)",
                    "management": "GIẢM LIỀU meropenem hoặc tăng khoảng cách liều. Theo dõi chặt chẽ dấu hiệu độc tính. Không khuyến cáo dùng cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Meropenem có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K, tăng tác dụng của warfarin.",
                    "effect": "Tăng tác dụng warfarin, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": [
                {
                    "drug": "Các kháng sinh beta-lactam khác",
                    "mechanism": "Có thể có tương tác phụ thuộc thời gian (time-dependent killing), nhưng thường không dùng cùng.",
                    "effect": "Không rõ, thường không dùng cùng",
                    "management": "Không khuyến cáo dùng cùng. Chọn một kháng sinh phù hợp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng meropenem hoặc carbapenem",
                "Dị ứng penicillins hoặc cephalosporins nặng (phản ứng chéo ~1%, nhưng có thể nguy hiểm)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl < 25ml/min) - tăng nguy cơ co giật, cần giảm liều mạnh",
                "Bệnh thần kinh trung ương - tăng nguy cơ co giật",
                "Tiền sử co giật - tăng nguy cơ co giật",
                "Suy gan nặng - thận trọng, mặc dù chủ yếu thải qua thận",
                "Người cao tuổi - tăng nguy cơ co giật, suy thận",
                "Dùng với valproate - giảm nồng độ valproate, mất kiểm soát co giật",
                "Dùng với probenecid - tăng nồng độ meropenem"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Meropenem là thuốc phân loại B. Có một số nghiên cứu trên động vật không cho thấy nguy cơ cho thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Meropenem có thể qua nhau thai, nhưng nồng độ trong máu thai nhi thấp. Được sử dụng trong nhiễm trùng nặng ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ. Nhiễm trùng nặng có thể nguy hiểm cho cả mẹ và thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Meropenem bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ. Nồng độ trong sữa mẹ thấp và không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú. Meropenem bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Meropenem chủ yếu thải qua thận, không phụ thuộc vào chức năng gan.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Thận trọng, nhưng không cần điều chỉnh liều thường quy. Meropenem chủ yếu thải qua thận. Theo dõi chức năng gan nếu có triệu chứng.",
            "notes": "Meropenem chủ yếu thải qua thận (70% bài tiết nguyên dạng), chỉ 40% chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, thận trọng ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (nguy hiểm, đặc biệt ở suy thận nặng)",
                "Độc tính thần kinh trung ương (lú lẫn, kích động)",
                "Tăng men gan (ALT, AST)",
                "Giảm tiểu cầu (hiếm)",
                "Tiêu chảy nặng",
                "Nhiễm C. difficile (tiêu chảy, đau bụng, sốt)"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều meropenem. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay meropenem nếu đang truyền",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam 5-10mg IV, lorazepam 2-4mg IV) - điều trị chính",
                "  - Nếu không đáp ứng: Phenytoin, phenobarbital",
                "  - Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Nếu độc tính thần kinh trung ương:",
                "  - Hỗ trợ tâm lý, an ủi bệnh nhân",
                "  - Theo dõi chặt chẽ, thường tự hồi phục sau khi ngừng thuốc",
                "Nếu nhiễm C. difficile:",
                "  - Ngừng meropenem và các kháng sinh khác nếu có thể",
                "  - Metronidazole 500mg PO x 3 lần/ngày x 10-14 ngày",
                "  - Hoặc Vancomycin 125mg PO x 4 lần/ngày x 10-14 ngày (nếu nặng)",
                "  - Theo dõi dấu hiệu viêm đại tràng giả mạc",
                "Nếu tăng men gan:",
                "  - Ngừng meropenem nếu tăng nặng",
                "  - Theo dõi chức năng gan",
                "  - Thường tự hồi phục sau khi ngừng thuốc",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2 trong ít nhất 24-48 giờ",
                "Có thể cần lọc máu nếu suy thận nặng (meropenem có thể được loại bỏ qua lọc máu)"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) liên tục trong ít nhất 24-48 giờ sau khi ngừng meropenem. Theo dõi lâu hơn nếu có biến chứng (co giật, độc tính thần kinh, nhiễm C. difficile)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu cho meropenem. Điều trị hỗ trợ và điều trị triệu chứng (benzodiazepine cho co giật)."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột khô trong NS hoặc D5W: 500mg pha trong 10ml = 50mg/ml, 1g pha trong 20ml = 50mg/ml. Sau đó pha loãng trong 50-250ml NS hoặc D5W để truyền.",
                "infusion_rate": "Truyền IV trong 15-30 phút. Không truyền nhanh hơn (có thể gây co giật). Liều: 1g IV mỗi 8 giờ (bình thường), 500mg-1g IV mỗi 12 giờ (suy thận).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": ["Không trộn với các thuốc khác. Dùng đường truyền riêng hoặc flush trước/sau khi truyền thuốc khác."],
                "notes": "QUAN TRỌNG: 1) PHẢI điều chỉnh liều theo chức năng thận (eGFR), 2) Truyền trong 15-30 phút (không nhanh hơn), 3) Nguy cơ co giật tăng ở suy thận nặng và bệnh nhân có tiền sử co giật, 4) TRÁNH dùng với valproate (giảm nồng độ valproate), 5) Theo dõi nhiễm C. difficile, 6) Không pha trộn với các thuốc khác."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Meropenem",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Meropenem: Drug Information",
                "Medscape - Meropenem Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Meropenem Monograph",
                "Micromedex - Meropenem Drug Information"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }

    }
}

__all__ = ['BETA_LACTAM_ANTIBIOTICS']

