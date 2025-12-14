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

    },

    "Imipenem-cilastatin": {
        "group": "Antibiotic - Carbapenem",
        "vietnamese_name": "Imipenem-cilastatin, Primaxin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn nặng đa kháng",
            "Nhiễm khuẩn bệnh viện",
            "Nhiễm khuẩn ổ bụng",
            "Nhiễm khuẩn huyết",
            "Nhiễm khuẩn da và mô mềm",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Viêm phổi bệnh viện"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng beta-lactam nặng",
            "Dị ứng imipenem hoặc cilastatin"
        ],
        "dosage": {
            "adult_standard": "500mg-1g IV mỗi 6-8 giờ (tỷ lệ 1:1 imipenem:cilastatin)",
            "adult_severe": "1g IV mỗi 6-8 giờ",
            "adult_mild": "250-500mg IV mỗi 6-8 giờ",
            "adult_im": "500-750mg IM mỗi 12 giờ",
            "pediatric_iv": "15-25mg/kg IV mỗi 6 giờ (tối đa 1g mỗi liều)",
            "notes": "Tỷ lệ cố định: 1 phần imipenem : 1 phần cilastatin. Cilastatin bảo vệ imipenem khỏi bị phân hủy bởi dehydropeptidase I ở thận. Truyền IV trong 20-30 phút (liều ≤500mg) hoặc 40-60 phút (liều >500mg)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250-500mg IV mỗi 6-8 giờ",
            "under_30": "250mg IV mỗi 6-8 giờ (CrCl 20-30) hoặc 250mg IV mỗi 12 giờ (CrCl <20)",
            "hemodialysis": "250mg IV sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Co giật (đặc biệt ở liều cao, suy thận, bệnh nhân có tiền sử co giật)",
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng men gan",
            "Giảm bạch cầu (hiếm)",
            "Viêm tĩnh mạch tại vị trí tiêm"
        ],
        "interactions": [
            "Valproate: giảm nồng độ valproate đáng kể (có thể giảm 50-70%)",
            "Ganciclovir: tăng nguy cơ co giật",
            "Probenecid: tăng nồng độ imipenem",
            "Warfarin: có thể tăng INR"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Imipenem: carbapenem phổ rất rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), đặc biệt PBP-2. Phổ kháng khuẩn rất rộng: Gram-dương (Staphylococcus, Streptococcus, Enterococcus - một số), Gram-âm (Enterobacteriaceae, Pseudomonas aeruginosa, Acinetobacter), và kỵ khí (Bacteroides, Clostridium). Cilastatin: ức chế dehydropeptidase I ở thận, bảo vệ imipenem khỏi bị phân hủy, tăng nồng độ trong nước tiểu và giảm độc tính thận. Không có hoạt tính kháng khuẩn riêng. Tỷ lệ cố định 1:1. Đặc điểm: phổ rộng nhất trong các carbapenem, nhưng nguy cơ co giật cao hơn meropenem.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận, đặc biệt quan trọng",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu co giật (đặc biệt ở liều cao, suy thận, bệnh nhân có tiền sử co giật) - QUAN TRỌNG",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Công thức máu (CBC) - hiếm giảm bạch cầu",
            "Nồng độ valproate nếu đang dùng (imipenem-cilastatin làm giảm nồng độ valproate đáng kể)"
        ],
        "precautions": [
            "NGUY CƠ CO GIẬT - cao hơn meropenem, đặc biệt ở liều cao (>2g/ngày), suy thận, bệnh nhân có tiền sử co giật, bệnh lý thần kinh trung ương",
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - quan trọng để tránh co giật",
            "Không dùng ở bệnh nhân dị ứng carbapenem hoặc beta-lactam nặng",
            "TRÁNH DÙNG với valproate (giảm nồng độ valproate đáng kể, có thể gây co giật)",
            "TRÁNH DÙNG với ganciclovir (tăng nguy cơ co giật)",
            "Pha trong NS hoặc D5W, truyền IV trong 20-30 phút (liều ≤500mg) hoặc 40-60 phút (liều >500mg)",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ (imipenem và cilastatin)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q6-8h",
            "protein_binding": "20% (imipenem), 40% (cilastatin)",
            "metabolism": "Imipenem: bị phân hủy bởi dehydropeptidase I ở thận (nếu không có cilastatin). Cilastatin: ức chế dehydropeptidase I, bảo vệ imipenem.",
            "clearance": "Chủ yếu qua thận (70% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 1 giờ, hoặc trong tủ lạnh 4 giờ. Không đông lạnh.",
        "black_box_warnings": "NGUY CƠ CO GIẬT - cao hơn các carbapenem khác, đặc biệt ở liều cao (>2g/ngày), suy thận, bệnh nhân có tiền sử co giật, bệnh lý thần kinh trung ương. Phải điều chỉnh liều theo chức năng thận. TRÁNH DÙNG với valproate (giảm nồng độ valproate đáng kể).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate (Valproic acid, Divalproex)",
                    "mechanism": "Imipenem-cilastatin ức chế hấp thu và tăng thải trừ valproate, làm giảm nồng độ valproate trong máu đáng kể (có thể giảm 50-70%).",
                    "effect": "Giảm nồng độ valproate nghiêm trọng, tăng nguy cơ co giật (do mất tác dụng chống co giật của valproate)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi nồng độ valproate chặt chẽ, tăng liều valproate nếu cần, hoặc dùng thuốc chống co giật khác. Nguy cơ co giật cao."
                },
                {
                    "drug": "Ganciclovir",
                    "mechanism": "Cả hai đều có nguy cơ co giật, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ co giật nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu co giật, điều chỉnh liều nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết imipenem qua thận, làm tăng nồng độ và thời gian bán thải của imipenem.",
                    "effect": "Tăng nồng độ imipenem, tăng nguy cơ tác dụng phụ (co giật, độc tính thần kinh)",
                    "management": "GIẢM LIỀU imipenem-cilastatin hoặc tăng khoảng cách liều. Theo dõi chặt chẽ dấu hiệu độc tính. Không khuyến cáo dùng cùng."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Imipenem-cilastatin có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K, tăng tác dụng của warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng imipenem-cilastatin. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng imipenem, cilastatin, hoặc các carbapenem khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam nặng (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với carbapenem trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều đáng kể, tăng nguy cơ co giật",
                "Bệnh nhân có tiền sử co giật - tăng nguy cơ co giật",
                "Bệnh lý thần kinh trung ương - tăng nguy cơ co giật",
                "Dùng với valproate - giảm nồng độ valproate đáng kể, tăng nguy cơ co giật",
                "Dùng với ganciclovir - tăng nguy cơ co giật",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Imipenem-cilastatin phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ (co giật ở thai nhi). Không có nghiên cứu đầy đủ trên phụ nữ có thai. Carbapenem có thể qua nhau thai. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm trùng nặng. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết. Meropenem có thể là lựa chọn an toàn hơn trong thai kỳ (phân loại B).",
            "lactation": {
                "safety": "Compatible",
                "details": "Imipenem và cilastatin bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ. Nồng độ trong sữa mẹ thấp và không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú. Imipenem-cilastatin bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Imipenem và cilastatin chủ yếu thải qua thận, không phụ thuộc vào chức năng gan.",
            "moderate": "Thận trọng, nhưng không cần điều chỉnh liều thường quy. Imipenem và cilastatin chủ yếu thải qua thận. Theo dõi chức năng gan nếu có triệu chứng.",
            "severe": "Thận trọng, nhưng không cần điều chỉnh liều thường quy. Imipenem và cilastatin chủ yếu thải qua thận. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.",
            "notes": "Imipenem và cilastatin chủ yếu thải qua thận (70% bài tiết nguyên dạng), chỉ một phần nhỏ chuyển hóa ở gan. Không cần điều chỉnh liều ở suy gan. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng thần kinh: Co giật (NGUY HIỂM, đặc biệt ở liều cao, suy thận)",
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thận: Suy thận cấp, tăng creatinine (hiếm với liều thông thường)",
                "Triệu chứng da: Phát ban, mày đay",
                "Triệu chứng nghiêm trọng: Co giật, suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều imipenem-cilastatin. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay imipenem-cilastatin nếu đang truyền",
                "Điều trị co giật (QUAN TRỌNG):",
                "  - Benzodiazepine (diazepam, lorazepam) IV",
                "  - Phenobarbital nếu cần",
                "  - Theo dõi hô hấp (nguy cơ suy hô hấp)",
                "  - Điều chỉnh liều imipenem-cilastatin nếu tiếp tục dùng",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ imipenem và cilastatin)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ imipenem và cilastatin nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) liên tục trong ít nhất 24-48 giờ sau khi ngừng imipenem-cilastatin. Theo dõi lâu hơn nếu có biến chứng (co giật, độc tính thần kinh, nhiễm C. difficile). Đặc biệt theo dõi dấu hiệu co giật."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV/IM",
                "timing": "N/A - chỉ có dạng IV/IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 100ml cho liều 250-500mg, 100-200ml cho liều >500mg. Nồng độ pha: 2.5-5mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 20-30 phút (liều ≤500mg) hoặc 40-60 phút (liều >500mg). Tốc độ: 100ml/20 phút = 5ml/phút (liều ≤500mg) hoặc 200ml/60 phút = ~3.3ml/phút (liều >500mg). KHÔNG truyền quá nhanh (tăng nguy cơ co giật).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "Truyền IV trong 20-30 phút (liều ≤500mg) hoặc 40-60 phút (liều >500mg). KHÔNG truyền quá nhanh (tăng nguy cơ co giật). Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            },
            "im": {
                "reconstitution": "Pha với nước cất vô trùng hoặc lidocaine 1% (để giảm đau). Thể tích: 2-3ml cho liều 500-750mg.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi). Tránh tiêm vào mạch máu.",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ tiêm. Tiêm sâu vào cơ. Không tiêm vào mạch máu."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <3 tháng tuổi (dữ liệu hạn chế, nguy cơ co giật). Nếu cần: 20mg/kg IV mỗi 12 giờ.",
            "infants": "3 tháng - 1 tuổi: 15-25mg/kg IV mỗi 6 giờ (tối đa 1g mỗi liều). Theo dõi chức năng thận, dấu hiệu co giật.",
            "children": "1-12 tuổi: 15-25mg/kg IV mỗi 6 giờ (tối đa 1g mỗi liều). Điều chỉnh liều theo CrCl nếu suy thận. Theo dõi dấu hiệu co giật.",
            "adolescents": "≥12 tuổi: Liều người lớn. 500mg-1g IV mỗi 6-8 giờ.",
            "notes": "Tính liều theo imipenem (không tính cilastatin). Tỷ lệ cố định 1:1. Điều chỉnh liều theo chức năng thận. Đặc biệt theo dõi dấu hiệu co giật (nguy cơ cao hơn meropenem)."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể có suy thận phổ biến hơn, cần điều chỉnh liều. Tăng nguy cơ co giật ở suy thận, bệnh lý thần kinh trung ương.",
            "dose_adjustment": "Điều chỉnh liều theo chức năng thận: CrCl 30-60 → 250-500mg mỗi 6-8 giờ, CrCl <30 → 250mg mỗi 6-8 giờ (CrCl 20-30) hoặc 250mg mỗi 12 giờ (CrCl <20). Thận trọng ở bệnh nhân có tiền sử co giật.",
            "monitoring": "Theo dõi chức năng thận (creatinine, CrCl) thường xuyên. Đặc biệt theo dõi dấu hiệu co giật (nguy cơ cao hơn meropenem). Theo dõi dấu hiệu nhiễm trùng. Theo dõi tiêu chảy (có thể là nhiễm C. difficile)."
        },
        "brand_names": {
            "vietnam": ["Primaxin", "Imipenem-cilastatin", "Imipenem-cilastatin Stada"],
            "common": ["Primaxin", "Imipenem-cilastatin"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "80,000 - 200,000 VND/lọ (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Imipenem-cilastatin generic thường rẻ hơn (80,000-150,000 VND/lọ 500mg). Primaxin (brand) thường đắt hơn (150,000-200,000 VND/lọ 500mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Primaxin (imipenem-cilastatin)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Imipenem-cilastatin: Drug Information",
                "Medscape - Imipenem-cilastatin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Imipenem-cilastatin Monograph",
                "Micromedex - Imipenem-cilastatin Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Ertapenem": {
        "group": "Antibiotic - Carbapenem",
        "vietnamese_name": "Ertapenem, Invanz",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn da và mô mềm phức tạp",
            "Viêm phổi cộng đồng",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn phụ khoa phức tạp",
            "Nhiễm khuẩn huyết"
        ],
        "contraindications": [
            "Dị ứng carbapenem",
            "Dị ứng beta-lactam nặng",
            "Dị ứng ertapenem"
        ],
        "dosage": {
            "adult_standard": "1g IV/IM x 1 lần/ngày",
            "adult_severe": "1g IV x 1 lần/ngày",
            "pediatric_iv": "15mg/kg IV x 2 lần/ngày (tối đa 1g/ngày) - trẻ 3 tháng - 12 tuổi",
            "pediatric_im": "15mg/kg IM x 2 lần/ngày (tối đa 1g/ngày) - trẻ 3 tháng - 12 tuổi",
            "notes": "Ưu điểm: dùng 1 lần/ngày (do half-life dài). Không hiệu quả với Pseudomonas aeruginosa, Enterococcus, Acinetobacter (khác với meropenem và imipenem). Phù hợp cho nhiễm trùng cộng đồng và một số nhiễm trùng bệnh viện."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "500mg IV/IM x 1 lần/ngày",
            "under_30": "500mg IV/IM x 1 lần/ngày",
            "hemodialysis": "500mg IV/IM x 1 lần/ngày (sau lọc máu)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Đau đầu",
            "Tăng men gan (hiếm)",
            "Viêm tĩnh mạch tại vị trí tiêm",
            "Đau tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Valproate: giảm nồng độ valproate",
            "Probenecid: tăng nồng độ ertapenem",
            "Warfarin: có thể tăng INR"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Ertapenem là carbapenem phổ rộng, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs). Phổ kháng khuẩn: Gram-dương (Staphylococcus, Streptococcus), Gram-âm (Enterobacteriaceae - E. coli, Klebsiella, Proteus, Serratia), và kỵ khí (Bacteroides, Clostridium). KHÔNG hiệu quả với Pseudomonas aeruginosa, Enterococcus, Acinetobacter (khác với meropenem và imipenem). Đặc điểm: half-life dài (4 giờ) cho phép dùng 1 lần/ngày, phù hợp cho nhiễm trùng cộng đồng và một số nhiễm trùng bệnh viện. Không cần cilastatin (không bị phân hủy bởi dehydropeptidase I).",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Nồng độ valproate nếu đang dùng (ertapenem làm giảm nồng độ valproate)"
        ],
        "precautions": [
            "Phải điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Không dùng ở bệnh nhân dị ứng carbapenem hoặc beta-lactam nặng",
            "KHÔNG hiệu quả với Pseudomonas aeruginosa, Enterococcus, Acinetobacter - không dùng cho nhiễm trùng do các vi khuẩn này",
            "TRÁNH DÙNG với valproate (giảm nồng độ valproate)",
            "Pha trong NS hoặc D5W, truyền IV trong 30 phút",
            "IM: pha với lidocaine 1% để giảm đau",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "4 giờ (dài, cho phép dùng 1 lần/ngày)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "85-95% (cao)",
            "metabolism": "Một phần trong gan (thủy phân)",
            "clearance": "Chủ yếu qua thận (38% bài tiết nguyên dạng), một phần qua gan, cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 6 giờ, hoặc trong tủ lạnh 24 giờ. Không đông lạnh.",
        "black_box_warnings": "TRÁNH DÙNG với valproate - giảm nồng độ valproate đáng kể, có thể gây co giật. KHÔNG hiệu quả với Pseudomonas aeruginosa, Enterococcus, Acinetobacter.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate (Valproic acid, Divalproex)",
                    "mechanism": "Ertapenem ức chế hấp thu và tăng thải trừ valproate, làm giảm nồng độ valproate trong máu đáng kể (có thể giảm 50-70%).",
                    "effect": "Giảm nồng độ valproate nghiêm trọng, tăng nguy cơ co giật (do mất tác dụng chống co giật của valproate)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi nồng độ valproate chặt chẽ, tăng liều valproate nếu cần, hoặc dùng thuốc chống co giật khác. Nguy cơ co giật cao."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ertapenem qua thận, làm tăng nồng độ và thời gian bán thải của ertapenem.",
                    "effect": "Tăng nồng độ ertapenem, tăng nguy cơ tác dụng phụ",
                    "management": "GIẢM LIỀU ertapenem hoặc tăng khoảng cách liều. Theo dõi chặt chẽ dấu hiệu độc tính. Không khuyến cáo dùng cùng."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Ertapenem có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm giảm sản xuất vitamin K, tăng tác dụng của warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng ertapenem. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ertapenem hoặc các carbapenem khác - phản ứng chéo cao với tất cả beta-lactam",
                "Dị ứng beta-lactam nặng (penicillin, cephalosporin, carbapenem) - phản ứng chéo cao",
                "Sốc phản vệ với carbapenem trước đây"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều",
                "Dùng với valproate - giảm nồng độ valproate đáng kể, tăng nguy cơ co giật",
                "Nhiễm trùng do Pseudomonas aeruginosa, Enterococcus, Acinetobacter - KHÔNG hiệu quả, không dùng",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Ertapenem phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Carbapenem được sử dụng trong nhiễm trùng nặng ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ. Tuy nhiên, nên dùng liều thấp nhất hiệu quả và tránh dùng không cần thiết.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ertapenem bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ. Nồng độ trong sữa mẹ thấp và không đáng kể.",
                "recommendation": "Có thể dùng khi cho con bú. Ertapenem bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Ertapenem chuyển hóa một phần qua gan nhưng không đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
            "severe": "Thận trọng, có thể cần giảm liều. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng. Tuy nhiên, suy gan nặng có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận.",
            "notes": "Ertapenem chuyển hóa một phần qua gan (thủy phân) nhưng thải trừ chủ yếu qua thận (38% bài tiết nguyên dạng qua nước tiểu). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Không cần điều chỉnh liều thường quy ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thần kinh: Đau đầu, chóng mặt (hiếm co giật, khác với imipenem)",
                "Triệu chứng thận: Suy thận cấp, tăng creatinine (hiếm với liều thông thường)",
                "Triệu chứng da: Phát ban, mày đay"
            ],
            "antidote": "Không có antidote đặc hiệu cho quá liều ertapenem. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ertapenem nếu đang truyền",
                "Điều trị triệu chứng tiêu hóa:",
                "  - Chống nôn nếu cần",
                "  - Truyền dịch nếu mất nước",
                "  - Theo dõi điện giải",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Điều chỉnh điện giải",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ ertapenem)",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis có thể loại bỏ ertapenem nếu suy thận nặng"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn (huyết áp, nhịp tim, nhịp thở, SpO2) trong ít nhất 24-48 giờ sau khi ngừng ertapenem. Theo dõi lâu hơn nếu có biến chứng (nhiễm C. difficile)."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV/IM",
                "timing": "N/A - chỉ có dạng IV/IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 50ml cho liều 1g. Nồng độ pha: 20mg/ml (1g/50ml). Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "Truyền IV trong 30 phút. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            },
            "im": {
                "reconstitution": "Pha với nước cất vô trùng hoặc lidocaine 1% (để giảm đau). Thể tích: 3.2ml cho liều 1g.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi). Tránh tiêm vào mạch máu.",
                "notes": "Pha với lidocaine 1% để giảm đau tại chỗ tiêm. Tiêm sâu vào cơ. Không tiêm vào mạch máu. Có thể đau tại chỗ tiêm."
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <3 tháng tuổi (dữ liệu hạn chế).",
            "infants": "3 tháng - 1 tuổi: 15mg/kg IV/IM x 2 lần/ngày (tối đa 1g/ngày). Theo dõi chức năng thận.",
            "children": "1-12 tuổi: 15mg/kg IV/IM x 2 lần/ngày (tối đa 1g/ngày). Điều chỉnh liều theo CrCl nếu suy thận.",
            "adolescents": "≥13 tuổi: Liều người lớn. 1g IV/IM x 1 lần/ngày.",
            "notes": "Tính liều theo cân nặng. Điều chỉnh liều theo chức năng thận. Ưu điểm: dùng 1 lần/ngày ở người lớn (do half-life dài). Trẻ em: dùng 2 lần/ngày."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể có suy thận phổ biến hơn, cần điều chỉnh liều.",
            "dose_adjustment": "Điều chỉnh liều theo chức năng thận: CrCl 30-60 → 500mg x 1 lần/ngày, CrCl <30 → 500mg x 1 lần/ngày.",
            "monitoring": "Theo dõi chức năng thận (creatinine, CrCl) thường xuyên. Theo dõi dấu hiệu nhiễm trùng. Theo dõi tiêu chảy (có thể là nhiễm C. difficile)."
        },
        "brand_names": {
            "vietnam": ["Invanz", "Ertapenem", "Ertapenem Stada"],
            "common": ["Invanz", "Ertapenem"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "150,000 - 300,000 VND/lọ (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Ertapenem generic thường rẻ hơn (150,000-250,000 VND/lọ 1g). Invanz (brand) thường đắt hơn (250,000-300,000 VND/lọ 1g)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Invanz (ertapenem)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Ertapenem: Drug Information",
                "Medscape - Ertapenem Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Ertapenem Monograph",
                "Micromedex - Ertapenem Drug Information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },

    "Penicillin G": {
        "group": "Antibiotic - Penicillin (Natural)",
        "vietnamese_name": "Penicillin G, Benzylpenicillin",
        "administration": ["IV", "IM"],
        "indications": [
            "Nhiễm khuẩn do Streptococcus (viêm họng, viêm phổi, nhiễm khuẩn da)",
            "Nhiễm khuẩn do Treponema pallidum (giang mai)",
            "Nhiễm khuẩn do Neisseria meningitidis (viêm màng não)",
            "Nhiễm khuẩn do Clostridium (uốn ván, hoại thư)",
            "Nhiễm khuẩn do Actinomyces",
            "Viêm nội tâm mạc do Streptococcus nhạy cảm"
        ],
        "contraindications": [
            "Dị ứng penicillin",
            "Dị ứng beta-lactam"
        ],
        "dosage": {
            "adult_standard": "1-4 triệu đơn vị IV mỗi 4-6 giờ",
            "adult_severe": "4-6 triệu đơn vị IV mỗi 4 giờ",
            "adult_meningitis": "4 triệu đơn vị IV mỗi 4 giờ",
            "adult_syphilis": "2.4 triệu đơn vị IM x 1 liều (early), 2.4 triệu đơn vị IM mỗi tuần x 3 tuần (late)",
            "adult_endocarditis": "4-6 triệu đơn vị IV mỗi 4 giờ",
            "notes": "1 triệu đơn vị = 600mg. Pha trong NS hoặc D5W, truyền IV trong 30-60 phút"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%",
            "hemodialysis": "Bổ sung liều sau lọc máu"
        },
        "side_effects": [
            "Phát ban dị ứng",
            "Sốc phản vệ (hiếm nhưng nguy hiểm)",
            "Co giật (liều cao, suy thận)",
            "Viêm tĩnh mạch tại vị trí tiêm",
            "Tiêu chảy",
            "Nhiễm nấm thứ phát"
        ],
        "interactions": [
            "Probenecid: tăng nồng độ penicillin G (giảm thải trừ qua thận)",
            "Warfarin: có thể tăng INR",
            "Methotrexate: tăng nồng độ methotrexate",
            "Aminoglycosides: có thể bị bất hoạt khi pha chung"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Penicillin G (benzylpenicillin) là penicillin tự nhiên đầu tiên, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), ngăn cản quá trình cross-linking của peptidoglycan. Phổ kháng khuẩn: Gram-dương (Streptococcus, Staphylococcus nhạy cảm, Clostridium, Actinomyces), một số Gram-âm (Neisseria meningitidis, Neisseria gonorrhoeae nhạy cảm), và xoắn khuẩn (Treponema pallidum). Không hiệu quả với vi khuẩn sản xuất beta-lactamase. Phải dùng đường tiêm (IV/IM) vì bị phá hủy bởi acid dạ dày.",
        "monitoring": [
            "Dấu hiệu dị ứng (phát ban, sốc phản vệ) - đặc biệt quan trọng",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng thận (creatinine, CrCl) - điều chỉnh liều",
            "Dấu hiệu co giật (liều cao, suy thận)",
            "Đường huyết (có thể tăng hoặc giảm)",
            "Điện giải (natri - mỗi 1 triệu đơn vị chứa 1.7 mEq natri)"
        ],
        "precautions": [
            "Phải test dị ứng trước khi dùng (nếu có tiền sử dị ứng penicillin)",
            "Có thể gây sốc phản vệ - chuẩn bị epinephrine",
            "Điều chỉnh liều theo chức năng thận (CrCl) - đặc biệt quan trọng",
            "Hàm lượng natri cao (1.7 mEq/1 triệu đơn vị) - thận trọng ở suy tim, tăng huyết áp",
            "Nguy cơ co giật ở liều cao, suy thận, bệnh nhân có tiền sử co giật",
            "Không pha chung với aminoglycosides (truyền riêng biệt)",
            "Pha trong NS hoặc D5W, truyền IV trong 30-60 phút",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài"
        ],
        "pharmacokinetics": {
            "half_life": "0.5-1 giờ (bình thường), 7-10 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều 1-4 triệu đơn vị q4-6h",
            "protein_binding": "45-65%",
            "clearance": "Chủ yếu qua thận (60-90% bài tiết nguyên dạng), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Có thể gây sốc phản vệ nghiêm trọng, đặc biệt ở bệnh nhân có tiền sử dị ứng penicillin. Co giật có thể xảy ra ở liều cao hoặc suy thận.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của penicillin G, làm giảm thải trừ và tăng nồng độ penicillin G trong máu.",
                    "effect": "Tăng nồng độ penicillin G, tăng thời gian bán hủy, tăng hiệu quả nhưng cũng tăng nguy cơ độc tính",
                    "management": "Có thể dùng cùng để tăng nồng độ penicillin G (ví dụ: trong điều trị giang mai). Theo dõi dấu hiệu độc tính (co giật)."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Penicillin G có thể ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính (giảm bạch cầu, độc thận, viêm niêm mạc)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ nồng độ methotrexate, công thức máu, chức năng thận. Có thể cần giảm liều methotrexate."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Penicillin G có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Aminoglycosides có thể bị bất hoạt về mặt hóa học bởi penicillin G khi pha chung.",
                    "effect": "Giảm hiệu quả kháng khuẩn của aminoglycosides nếu pha chung",
                    "management": "Không pha chung. Truyền riêng biệt. Tuy nhiên, có thể dùng cùng nhau (synergy) nếu truyền riêng."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng penicillin (phản ứng nghiêm trọng, sốc phản vệ)",
                "Dị ứng beta-lactam (phản ứng chéo)"
            ],
            "tương_đối": [
                "Suy thận nặng (cần giảm liều đáng kể)",
                "Tiền sử co giật (tăng nguy cơ co giật)",
                "Suy tim (hàm lượng natri cao)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Penicillin G được coi là an toàn trong thai kỳ. Đã được sử dụng rộng rãi trong nhiều thập kỷ. Lựa chọn đầu tay cho nhiều nhiễm khuẩn trong thai kỳ, đặc biệt giang mai.",
            "lactation": {
                "safety": "Compatible",
                "details": "Penicillin G bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu dị ứng hoặc tiêu chảy."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Penicillin G thải chủ yếu qua thận, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (đặc biệt ở suy thận, liều cao)",
                "Rối loạn điện giải (natri cao)",
                "Viêm tĩnh mạch tại vị trí tiêm",
                "Phản ứng dị ứng nặng (sốc phản vệ)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: chống co giật, điều chỉnh điện giải",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "Điều trị co giật: Benzodiazepine (lorazepam, diazepam), phenobarbital nếu cần",
                "Điều chỉnh điện giải nếu cần",
                "Điều trị sốc phản vệ nếu có: Epinephrine, corticosteroids, antihistamines",
                "Theo dõi chức năng thận, điện giải",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "Chức năng thận (creatinine, CrCl), điện giải (Na, K), dấu hiệu co giật, dấu hiệu dị ứng, huyết áp, nhịp tim"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV/IM",
                "timing": "N/A - chỉ có dạng IV/IM"
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 50-100ml cho liều 1-4 triệu đơn vị. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 30-60 phút. Tốc độ: 50ml/30-60 phút.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "Truyền IV trong 30-60 phút. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha."
            },
            "im": {
                "reconstitution": "Pha với nước cất vô trùng. Thể tích: 1-2ml cho liều 2.4 triệu đơn vị.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi). Tránh tiêm vào mạch máu.",
                "notes": "Tiêm sâu vào cơ. Không tiêm vào mạch máu. Có thể đau tại chỗ tiêm. Dùng cho điều trị giang mai."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Penicillin G",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Penicillin G: Drug Information",
                "CDC Guidelines - Syphilis Treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều thập kỷ"
        }
    }
}

__all__ = ['BETA_LACTAM_ANTIBIOTICS']

