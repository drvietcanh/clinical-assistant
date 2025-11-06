"""
Antibiotics - Common Oral and IV Antibiotics
"""

ANTIMICROBIAL_ANTIBIOTICS = {
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

    "Clindamycin": {
    "group": "Antibiotic - Lincosamide",
    "vietnamese_name": "Clindamycin, Dalacin",
    "administration": ["PO", "IV", "IM"],
    "indications": [
        "Nhiễm khuẩn kỵ khí",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm phổi do vi khuẩn",
        "Nhiễm khuẩn răng miệng",
        "Sốt do chuột cắn"
    ],
    "contraindications": [
        "Dị ứng clindamycin",
        "Viêm đại tràng giả mạc trước đây"
    ],
    "dosage": {
        "adult_po": "150-450mg x 3-4 lần/ngày",
        "adult_iv": "600-900mg IV mỗi 8 giờ",
        "adult_severe": "900mg IV mỗi 8 giờ",
        "notes": "Có thể gây viêm đại tràng giả mạc (C. difficile). Dùng với thức ăn"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Không đổi",
        "under_30": "Không đổi (không thải qua thận)"
    },
    "side_effects": [
        "Tiêu chảy (phổ biến)",
        "Viêm đại tràng giả mạc (C. difficile - nghiêm trọng)",
        "Buồn nôn, nôn",
        "Phát ban",
        "Rối loạn vị giác"
    ],
    "interactions": [
        "Erythromycin: đối kháng",
        "Neuromuscular blockers: tăng tác dụng"
    ],
    "pregnancy": "B",
        "mechanism_of_action": "Lincosamide kháng sinh. Ức chế tổng hợp protein vi khuẩn bằng cách gắn với tiểu phần 50S của ribosome, ngăn cản quá trình dịch mã. Phổ kháng khuẩn: Gram-dương mạnh (Staphylococcus, Streptococcus, bao gồm một số MRSA), kỵ khí (Bacteroides, Clostridium), và một số vi khuẩn không điển hình. Không hiệu quả với Enterobacteriaceae (Gram-âm). Đặc biệt hiệu quả với kỵ khí và được dùng trong nhiễm trùng răng miệng, xương, và mô mềm.",
        "monitoring": [
            "Dấu hiệu nhiễm trùng (sốt, WBC)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile (tiêu chảy, đau bụng) - nguy cơ CAO",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Số lượng bạch cầu (hiếm giảm bạch cầu, giảm bạch cầu trung tính)",
            "Phản ứng tại chỗ tiêm (viêm tĩnh mạch, đau)",
            "Phát ban (hiếm hội chứng Stevens-Johnson)"
        ],
        "precautions": [
            "Nguy cơ nhiễm C. difficile CAO - đây là một trong những kháng sinh có nguy cơ cao nhất",
            "NGỪNG NGAY nếu có tiêu chảy, đau bụng - có thể là C. difficile",
            "Không dùng cho điều trị dự phòng (trừ một số trường hợp đặc biệt) để giảm nguy cơ C. difficile",
            "Theo dõi sát dấu hiệu nhiễm C. difficile trong và sau khi dùng",
            "Có thể gây giảm bạch cầu trung tính (hiếm nhưng nguy hiểm)",
            "Tương kỵ với nhiều thuốc - không pha trộn",
            "Pha trong NS hoặc D5W, truyền IV trong ít nhất 10-60 phút (tùy liều)",
            "Không dùng cho nhiễm trùng do vi khuẩn Gram-âm (không hiệu quả)",
            "Uống với nước đầy đủ để giảm kích ứng thực quản"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "30-60 phút (PO), ngay lập tức (IV)",
            "duration": "q6h hoặc q8h (PO/IV)",
            "protein_binding": "90-95% (rất cao)",
            "metabolism": "Gan (CYP3A4) - một phần",
            "clearance": "Gan và thận, không cần điều chỉnh thận nhưng thận trọng ở suy gan"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C). Viên nang: tránh ẩm. Dung dịch pha tiêm: sau khi pha, bảo quản ở nhiệt độ phòng 24 giờ.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, nguy cơ nhiễm C. difficile rất cao, có thể gây viêm đại tràng giả mạc nặng, có thể tử vong. Ngừng ngay nếu có tiêu chảy.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Erythromycin",
                    "mechanism": "Cả hai đều gắn với tiểu phần 50S của ribosome, đối kháng cạnh tranh, làm giảm hiệu quả kháng khuẩn của cả hai thuốc.",
                    "effect": "Giảm hiệu quả kháng khuẩn của cả hai thuốc",
                    "management": "TRÁNH DÙNG đồng thời. Chọn một trong hai thuốc. Nếu đã dùng erythromycin, chờ ít nhất 2-3 giờ trước khi dùng clindamycin."
                },
                {
                    "drug": "Neuromuscular blocking agents (Succinylcholine, Vecuronium, Rocuronium)",
                    "mechanism": "Clindamycin có thể tăng cường tác dụng của thuốc giãn cơ, gây tê liệt kéo dài và suy hô hấp.",
                    "effect": "Tăng tác dụng giãn cơ, tăng thời gian tê liệt, tăng nguy cơ suy hô hấp",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi chức năng hô hấp chặt chẽ. Có thể cần giảm liều thuốc giãn cơ. Đảm bảo có thiết bị hỗ trợ hô hấp sẵn sàng."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Clindamycin có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên (ít nhất 2-3 lần/tuần khi bắt đầu dùng clindamycin). Có thể cần giảm liều warfarin. Đặc biệt thận trọng ở bệnh nhân dùng kéo dài (>7 ngày)."
                },
                {
                    "drug": "Kaolin-pectin (thuốc chống tiêu chảy)",
                    "mechanism": "Kaolin-pectin có thể hấp phụ clindamycin, làm giảm hấp thu và giảm nồng độ clindamycin trong máu.",
                    "effect": "Giảm hấp thu clindamycin, giảm hiệu quả kháng khuẩn",
                    "management": "Cách ít nhất 2 giờ giữa clindamycin và kaolin-pectin. Không dùng kaolin-pectin nếu đang điều trị C. difficile (có thể làm nặng bệnh)."
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
                "Dị ứng clindamycin hoặc lincomycin",
                "Viêm đại tràng giả mạc trước đây do C. difficile (tiền sử)"
            ],
            "tương_đối": [
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát",
                "Suy gan nặng - giảm chuyển hóa, tăng nguy cơ tác dụng phụ",
                "Bệnh nhân đang dùng thuốc giãn cơ - tăng nguy cơ tê liệt kéo dài",
                "Bệnh nhân đang dùng warfarin - tăng nguy cơ chảy máu",
                "Nhiễm trùng do vi khuẩn Gram-âm - không hiệu quả"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Clindamycin là thuốc phân loại B. Các nghiên cứu trên động vật không cho thấy nguy cơ dị tật bẩm sinh, nhưng không có nghiên cứu đầy đủ trên phụ nữ có thai. Clindamycin được sử dụng rộng rãi trong thai kỳ và có vẻ an toàn. Có thể được dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong nhiễm khuẩn kỵ khí. Tuy nhiên, cần thận trọng với nguy cơ nhiễm C. difficile, có thể nghiêm trọng trong thai kỳ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Clindamycin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, có thể gây tiêu chảy hoặc phát ban ở trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ sơ sinh về dấu hiệu tiêu chảy, phát ban, hoặc các tác dụng phụ khác. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Clindamycin chuyển hóa một phần qua gan (CYP3A4), nhưng không tích lũy đáng kể.",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan và dấu hiệu tác dụng phụ.",
            "severe": "Giảm liều 25-50% hoặc tăng khoảng cách giữa các liều. Theo dõi chức năng gan chặt chẽ. Có thể cần giảm tần suất dùng (q12h thay vì q8h).",
            "notes": "Clindamycin chuyển hóa một phần qua gan (CYP3A4), nhưng thải trừ chủ yếu qua gan và thận. Không tích lũy đáng kể ở suy gan nhẹ, nhưng có thể tích lũy ở suy gan nặng. Cần điều chỉnh liều ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Tiêu chảy nặng, đau bụng, buồn nôn, nôn (có thể là C. difficile)",
                "Triệu chứng thần kinh: Co giật, rối loạn ý thức (hiếm, thường chỉ với liều rất cao)",
                "Triệu chứng hô hấp: Suy hô hấp (nếu dùng với thuốc giãn cơ)",
                "Triệu chứng chảy máu: Chảy máu kéo dài, tăng INR (khi dùng với warfarin)",
                "Triệu chứng gan: Tăng men gan, viêm gan (hiếm)",
                "Triệu chứng dị ứng: Phát ban, phù mạch, sốc phản vệ (nếu dị ứng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay clindamycin",
                "Điều trị C. difficile nếu có:",
                "  - Ngừng ngay clindamycin",
                "  - Điều trị bằng vancomycin PO hoặc metronidazole PO",
                "  - Bù dịch đầy đủ",
                "  - Theo dõi dấu hiệu viêm đại tràng nặng (sốt, đau bụng, tiêu chảy máu)",
                "Điều trị co giật nếu có: Benzodiazepine (diazepam, lorazepam), phenobarbital",
                "Điều trị suy hô hấp nếu có:",
                "  - Hỗ trợ hô hấp (thở máy nếu cần)",
                "  - Điều trị tê liệt do thuốc giãn cơ nếu có",
                "Điều trị chảy máu nếu có:",
                "  - Bổ sung vitamin K nếu giảm prothrombin",
                "  - Truyền huyết tương tươi đông lạnh (FFP) nếu chảy máu nặng",
                "  - Điều chỉnh liều warfarin nếu đang dùng",
                "Điều trị dị ứng nếu có:",
                "  - Epinephrine nếu sốc phản vệ",
                "  - Antihistamine, corticosteroid",
                "  - Hỗ trợ hô hấp nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lọc máu: Hemodialysis không hiệu quả do protein binding cao (90-95%)"
            ],
            "monitoring": "Theo dõi dấu hiệu C. difficile (tiêu chảy, đau bụng, sốt), dấu hiệu thần kinh (co giật, ý thức), chức năng hô hấp (nếu dùng với thuốc giãn cơ), PT/INR (nếu dùng với warfarin), chức năng gan (ALT, AST), dấu hiệu chảy máu, dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có C. difficile hoặc suy hô hấp."
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày nhưng không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 3-4 lần/ngày (150-450mg mỗi lần). Cách đều trong ngày. Uống với nhiều nước (ít nhất 200ml) để giảm kích ứng thực quản."
            },
            "iv": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 6-12mg/ml. Pha 600mg trong 50ml = 12mg/ml. Pha 900mg trong 50ml = 18mg/ml (quá đậm, không dùng). Pha 900mg trong 100ml = 9mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong ít nhất 10-60 phút (tùy liều). Liều 600mg: truyền trong 10-30 phút. Liều 900mg: truyền trong 30-60 phút. Tốc độ: 50ml/30 phút = ~1.7ml/phút. KHÔNG truyền nhanh (bolus) - tăng nguy cơ viêm tĩnh mạch.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "Ringer's Lactate"],
                "incompatibility": [
                    "Aminophylline - tạo kết tủa, không pha chung",
                    "Phenytoin - tạo kết tủa, không pha chung",
                    "Barbiturates - tạo kết tủa, không pha chung",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
                ],
                "notes": "QUAN TRỌNG: 1) Không pha chung với aminophylline, phenytoin, barbiturates (tạo kết tủa), 2) Truyền chậm (ít nhất 10-60 phút) để giảm viêm tĩnh mạch, 3) Theo dõi sát dấu hiệu C. difficile, 4) Không dùng cho nhiễm trùng do vi khuẩn Gram-âm."
            },
            "im": {
                "reconstitution": "Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Nồng độ pha: 150mg/ml (tối đa). Pha 600mg trong 4ml = 150mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis). Tránh tiêm vào mạch máu.",
                "notes": "Tiêm sâu vào cơ. Có thể gây đau tại chỗ. Liều IM: 600mg mỗi 12 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Clindamycin (Cleocin)",
                "UpToDate - Clindamycin: Drug Information",
                "Medscape - Clindamycin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Clindamycin Monograph",
                "Micromedex - Clindamycin Drug Information",
                "IDSA Guidelines - Skin and Soft Tissue Infections, Anaerobic Infections"
            ],
            "last_updated": "2025-02-03",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }

    },

    "Trimethoprim-sulfamethoxazole": {
    "group": "Antibiotic - Sulfonamide",
    "vietnamese_name": "Trimethoprim-sulfamethoxazole, Bactrim, Septra, Cotrimoxazole",
    "administration": ["PO", "IV"],
    "indications": [
        "Nhiễm khuẩn đường tiết niệu",
        "Viêm phổi do Pneumocystis jirovecii (PJP)",
        "Nhiễm khuẩn do Toxoplasma",
        "Nhiễm khuẩn do MRSA",
        "Nhiễm khuẩn đường hô hấp"
    ],
    "contraindications": [
        "Dị ứng sulfonamide",
        "Suy thận nặng (CrCl <15)",
        "Suy gan nặng",
        "Thiếu máu do thiếu folate",
        "Có thai (gần sinh)"
    ],
    "dosage": {
        "adult_uti": "160/800mg (DS) x 2 lần/ngày",
        "adult_pjp": "160/800mg (DS) x 3-4 lần/ngày",
        "adult_pjp_iv": "15-20mg/kg (TMP) IV mỗi 6-8 giờ",
        "notes": "Tỷ lệ TMP:SMX = 1:5. Dùng với nhiều nước"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "Tránh dùng nếu CrCl <15"
    },
    "side_effects": [
        "Phát ban (thường gặp)",
        "Tăng kali máu",
        "Giảm bạch cầu",
        "Thiếu máu",
        "Tăng creatinine (giả, không phản ánh suy thận)",
        "Độc tính da (SJS/TEN - hiếm nhưng nguy hiểm)"
    ],
    "interactions": [
        "Warfarin: tăng tác dụng",
        "Phenytoin: tăng nồng độ phenytoin",
        "ACE inhibitor: tăng kali máu",
        "Methotrexate: tăng độc tính"
    ],
    "pregnancy": "C - D gần sinh",
    "mechanism_of_action": "Trimethoprim-sulfamethoxazole (TMP-SMX, cotrimoxazole) là kháng sinh kết hợp với tác dụng hiệp đồng (synergistic). Sulfamethoxazole (SMX) là sulfonamide ức chế tổng hợp acid folic ở vi khuẩn bằng cách ức chế enzyme dihydropteroate synthase, ngăn chặn tổng hợp dihydrofolic acid. Trimethoprim (TMP) ức chế enzyme dihydrofolate reductase, ngăn chặn chuyển đổi dihydrofolic acid thành tetrahydrofolic acid, một cofactor cần thiết cho tổng hợp DNA, RNA, và protein. Cả hai chất cùng ức chế con đường tổng hợp acid folic ở hai bước khác nhau, tạo ra tác dụng hiệp đồng mạnh. Tỷ lệ TMP:SMX = 1:5 (160mg TMP : 800mg SMX). Phổ kháng khuẩn: Gram-dương (một số Staphylococcus, Streptococcus), Gram-âm (Enterobacteriaceae, H. influenzae), và một số vi khuẩn không điển hình (Pneumocystis jirovecii, Toxoplasma gondii, Nocardia).",
    "monitoring": [
        "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng) để đánh giá đáp ứng điều trị",
        "Cấy máu và cấy từ vị trí nhiễm trùng (nếu có) để xác định vi khuẩn và độ nhạy cảm",
        "Điện giải (natri, kali) - tăng kali máu (đặc biệt ở người cao tuổi, suy thận, dùng ACE inhibitor/ARB)",
        "Công thức máu (CBC) - giảm bạch cầu, thiếu máu, giảm tiểu cầu (do thiếu folate)",
        "Creatinine - tăng creatinine giả (do ức chế bài tiết creatinine ở ống thận, không phản ánh suy thận thực sự)",
        "Chức năng gan (ALT, AST) - hiếm viêm gan nặng",
        "Dấu hiệu phản ứng dị ứng (phát ban, sốt) - có thể tiến triển thành SJS/TEN",
        "Dấu hiệu SJS/TEN (Stevens-Johnson syndrome, toxic epidermal necrolysis) - phát ban, mụn nước, bong da",
        "Tương tác với warfarin (tăng INR), phenytoin (tăng nồng độ), methotrexate (tăng độc tính)"
    ],
    "precautions": [
        "Phản ứng dị ứng - nguy cơ cao với sulfonamide, đặc biệt SJS/TEN (hiếm nhưng nguy hiểm, có thể tử vong)",
        "NGỪNG NGAY nếu có phát ban, sốt, mụn nước, bong da - có thể là SJS/TEN",
        "Tăng kali máu - đặc biệt ở người cao tuổi, suy thận, dùng ACE inhibitor/ARB, trimethoprim",
        "Không dùng nếu CrCl <15 (tăng nguy cơ tác dụng phụ, không hiệu quả)",
        "Tăng creatinine giả - không phản ánh suy thận thực sự, do ức chế bài tiết creatinine",
        "Thiếu máu, giảm bạch cầu - do ức chế tổng hợp folate, đặc biệt ở bệnh nhân thiếu folate",
        "Không dùng gần sinh (trong 3 tháng cuối thai kỳ) - nguy cơ kernicterus ở trẻ sơ sinh",
        "Uống nhiều nước để tránh kết tinh trong nước tiểu (sulfamethoxazole)",
        "Tương tác với nhiều thuốc: warfarin (tăng INR), phenytoin (tăng nồng độ), methotrexate (tăng độc tính), ACE inhibitor/ARB (tăng kali)",
        "Thận trọng ở bệnh nhân suy gan (chuyển hóa qua gan)",
        "Dùng với thức ăn để giảm kích ứng dạ dày"
    ],
    "pharmacokinetics": {
        "half_life": "8-10 giờ (TMP), 10-12 giờ (SMX)",
        "onset": "2-4 giờ",
        "duration": "q12h (PO), q6-8h (IV cho PJP)",
        "protein_binding": "44% (TMP), 70% (SMX)",
        "clearance": "Gan: chuyển hóa một phần. Thận: bài tiết chủ yếu qua thận (TMP và SMX). Cần điều chỉnh liều ở suy thận (CrCl <30: giảm 50%, CrCl <15: tránh dùng)."
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín. Dạng suspension: bảo quản ở nhiệt độ phòng, lắc kỹ trước khi dùng. IV: bảo quản trong tủ lạnh, để nhiệt độ phòng trước khi pha, dùng trong vòng 6 giờ sau khi pha.",
    "black_box_warnings": "Nguy cơ phản ứng dị ứng nghiêm trọng, bao gồm SJS/TEN, có thể gây tử vong. Nguy cơ tăng ở bệnh nhân có tiền sử dị ứng sulfonamide. Ngừng ngay nếu có phát ban, sốt, mụn nước, bong da.",
    "drug_interactions": {
        "major": [
            {
                "drug": "Warfarin",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa warfarin. Sulfamethoxazole cũng có thể ức chế tổng hợp vitamin K.",
                "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu nghiêm trọng",
                "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng trimethoprim-sulfamethoxazole. Giảm liều warfarin 25-50% khi bắt đầu trimethoprim-sulfamethoxazole. Điều chỉnh liều warfarin theo INR."
            },
            {
                "drug": "Phenytoin",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa phenytoin.",
                "effect": "Tăng nồng độ phenytoin, tăng độc tính (chóng mặt, rung giật, ataxia, co giật)",
                "management": "Theo dõi nồng độ phenytoin. Giảm liều phenytoin khi bắt đầu trimethoprim-sulfamethoxazole. Theo dõi dấu hiệu độc tính phenytoin."
            },
            {
                "drug": "Methotrexate",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế tổng hợp folate, làm tăng độc tính methotrexate. Cũng ức chế bài tiết methotrexate ở ống thận.",
                "effect": "Tăng nồng độ methotrexate, tăng độc tính nghiêm trọng (giảm bạch cầu, thiếu máu, độc gan, độc thận, tử vong)",
                "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, giảm liều methotrexate đáng kể, bổ sung folinic acid (leucovorin), theo dõi chặt chẽ công thức máu, chức năng gan, thận. Ngừng methotrexate nếu có dấu hiệu độc tính."
            }
        ],
        "moderate": [
            {
                "drug": "ACE inhibitor, ARB",
                "mechanism": "Trimethoprim ức chế bài tiết kali ở ống thận, làm tăng kali máu. ACE inhibitor/ARB cũng tăng kali máu.",
                "effect": "Tăng kali máu, tăng nguy cơ rối loạn nhịp tim, đặc biệt ở người cao tuổi, suy thận",
                "management": "Theo dõi kali máu chặt chẽ, đặc biệt ở người cao tuổi, suy thận. Giảm liều hoặc ngừng ACE inhibitor/ARB nếu kali tăng. Điều chỉnh liều trimethoprim-sulfamethoxazole nếu cần."
            },
            {
                "drug": "Digoxin",
                "mechanism": "Trimethoprim-sulfamethoxazole có thể ảnh hưởng đến hệ vi khuẩn đường ruột, làm tăng hấp thu digoxin.",
                "effect": "Tăng nồng độ digoxin, tăng độc tính (buồn nôn, nôn, rối loạn nhịp tim, block AV)",
                "management": "Theo dõi nồng độ digoxin và dấu hiệu độc tính. Giảm liều digoxin nếu cần. Theo dõi ECG."
            },
            {
                "drug": "Sulfonylurea (Glibenclamide, Gliclazide)",
                "mechanism": "Trimethoprim-sulfamethoxazole ức chế CYP2C9, làm giảm chuyển hóa sulfonylurea.",
                "effect": "Tăng nồng độ sulfonylurea, tăng nguy cơ hạ đường huyết",
                "management": "Theo dõi đường huyết chặt chẽ. Giảm liều sulfonylurea khi bắt đầu trimethoprim-sulfamethoxazole. Điều chỉnh liều theo đường huyết."
            }
        ],
        "minor": [
            {
                "drug": "Cyclosporine",
                "mechanism": "Trimethoprim-sulfamethoxazole có thể ảnh hưởng đến chuyển hóa cyclosporine.",
                "effect": "Tăng nhẹ nồng độ cyclosporine",
                "management": "Theo dõi nồng độ cyclosporine. Không cần điều chỉnh liều thường quy."
            }
        ]
    },
    "contraindications": {
        "tuyệt_đối": [
            "Dị ứng trimethoprim, sulfamethoxazole, hoặc các sulfonamide khác - phản ứng chéo cao",
            "Suy thận nặng (CrCl <15) - tăng nguy cơ tác dụng phụ, không hiệu quả",
            "Suy gan nặng - tăng nguy cơ độc tính",
            "Thiếu máu do thiếu folate - tăng nguy cơ thiếu máu nặng, giảm bạch cầu",
            "Có thai (gần sinh, 3 tháng cuối) - nguy cơ kernicterus ở trẻ sơ sinh",
            "Tiền sử SJS/TEN do sulfonamide - nguy cơ tái phát cao, có thể tử vong"
        ],
        "tương_đối": [
            "Dị ứng sulfonamide nhẹ - thận trọng, có thể dùng nếu cần thiết nhưng theo dõi chặt chẽ",
            "Suy thận (CrCl 15-30) - cần giảm liều 50%, theo dõi chặt chẽ",
            "Suy gan - thận trọng, có thể giảm chuyển hóa",
            "Thiếu folate - bổ sung folate trước và trong khi dùng",
            "Người cao tuổi - tăng nguy cơ tăng kali máu, tác dụng phụ",
            "Dùng với ACE inhibitor/ARB - tăng nguy cơ tăng kali máu",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Dùng với phenytoin - tăng độc tính phenytoin",
            "Dùng với methotrexate - tăng độc tính methotrexate nghiêm trọng",
            "Có thai (tam cá nguyệt 1-2) - thận trọng, chỉ dùng khi thực sự cần thiết"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "C (tam cá nguyệt 1-2), D (tam cá nguyệt 3)",
        "pregnancy_details": "Tam cá nguyệt 1-2: Thuốc phân loại C - thận trọng. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh rõ ràng, nhưng dữ liệu còn hạn chế. Có thể dùng khi lợi ích vượt quá nguy cơ, đặc biệt trong điều trị PJP hoặc nhiễm trùng nặng. Tam cá nguyệt 3 (gần sinh): Thuốc phân loại D - CHỐNG CHỈ ĐỊNH. Sulfamethoxazole có thể gây kernicterus ở trẻ sơ sinh (vàng da nặng, tổn thương não). Không dùng trong 3 tháng cuối thai kỳ. Nếu cần điều trị, dùng thuốc khác hoặc trì hoãn đến sau sinh.",
        "lactation": {
            "safety": "Compatible with Caution",
            "details": "Trimethoprim và sulfamethoxazole bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, sulfonamide có thể gây vàng da ở trẻ sơ sinh thiếu tháng hoặc có bệnh gan. Thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu tháng.",
            "recommendation": "Có thể dùng khi cho con bú, nhưng thận trọng ở trẻ sơ sinh < 1 tháng tuổi hoặc thiếu tháng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh nếu dùng liều cao hoặc kéo dài (vàng da, tiêu chảy, phát ban)."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không cần điều chỉnh liều. Trimethoprim và sulfamethoxazole chuyển hóa một phần qua gan nhưng không đáng kể.",
        "moderate": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan trung bình, tăng nồng độ và nguy cơ tác dụng phụ.",
        "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng tối đa. Chuyển hóa có thể giảm đáng kể ở suy gan nặng, tăng nồng độ và nguy cơ độc tính gan nghiêm trọng. Không dùng nếu suy gan nặng.",
        "notes": "Trimethoprim và sulfamethoxazole chuyển hóa một phần qua gan nhưng thải trừ chủ yếu qua thận. Suy gan có thể giảm chuyển hóa, tăng nồng độ và nguy cơ độc tính gan. Tuy nhiên, suy gan nặng là chống chỉ định do nguy cơ độc tính gan nghiêm trọng. Theo dõi chặt chẽ chức năng gan ở suy gan trung bình."
    },
    "overdose_management": {
        "symptoms": [
            "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
            "Triệu chứng thần kinh: Đau đầu, chóng mặt, lú lẫn, co giật (hiếm)",
            "Triệu chứng huyết học: Thiếu máu, giảm bạch cầu, giảm tiểu cầu (do thiếu folate)",
            "Triệu chứng thận: Tăng creatinine (giả), suy thận cấp (hiếm)",
            "Triệu chứng điện giải: Tăng kali máu (đặc biệt với trimethoprim)",
            "Triệu chứng da: Phát ban, mày đay, SJS/TEN (hiếm nhưng nghiêm trọng, có thể tử vong)",
            "Triệu chứng gan: Tăng men gan, viêm gan (hiếm nhưng nghiêm trọng)",
            "Triệu chứng nghiêm trọng: SJS/TEN, suy thận cấp, viêm gan nặng, thiếu máu nặng"
        ],
        "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng. Bổ sung folinic acid (leucovorin) nếu có thiếu máu do thiếu folate.",
        "treatment": [
            "Ngừng ngay trimethoprim-sulfamethoxazole",
            "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
            "Điều trị triệu chứng tiêu hóa:",
            "  - Chống nôn nếu cần",
            "  - Truyền dịch nếu mất nước",
            "  - Theo dõi điện giải",
            "Điều trị tăng kali máu nếu có:",
            "  - Theo dõi kali máu",
            "  - Điều trị tăng kali máu: Calcium gluconate, insulin + glucose, sodium bicarbonate, kayexalate",
            "  - Lọc máu nếu cần",
            "Điều trị thiếu máu/giảm bạch cầu nếu có:",
            "  - Bổ sung folinic acid (leucovorin) 5-15mg/ngày",
            "  - Theo dõi công thức máu",
            "  - Truyền máu nếu cần",
            "Điều trị tăng creatinine (giả) nếu có:",
            "  - Theo dõi creatinine, BUN, lượng nước tiểu",
            "  - Điều trị suy thận cấp nếu có",
            "Điều trị SJS/TEN nếu có:",
            "  - CHUYỂN NGAY khoa da liễu/bỏng",
            "  - Điều trị hỗ trợ (truyền dịch, dinh dưỡng, chăm sóc vết thương)",
            "  - Kháng sinh nếu có nhiễm trùng",
            "  - Corticosteroid (còn tranh cãi)",
            "Điều trị tăng men gan/viêm gan nếu có:",
            "  - Theo dõi ALT, AST, bilirubin",
            "  - Điều trị hỗ trợ gan",
            "  - Nếu viêm gan nặng: điều trị suy gan",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
        ],
        "monitoring": "Theo dõi dấu hiệu sinh tồn, công thức máu (CBC), điện giải (natri, kali), chức năng thận (creatinine, BUN, lượng nước tiểu), chức năng gan (ALT, AST, bilirubin), dấu hiệu da (SJS/TEN) trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng (SJS/TEN, suy thận, viêm gan, thiếu máu)."
    },
    "reversal_agents": None,
    "administration_instructions": {
        "oral": {
            "with_food": "Uống với thức ăn để giảm kích ứng dạ dày. Có thể uống không thức ăn nếu cần nhưng không khuyến nghị.",
            "timing": "Uống 2 lần/ngày (q12h) cho UTI, 3-4 lần/ngày (q6-8h) cho PJP. Uống đều đặn, cách đều nhau trong ngày. Không bỏ liều. Uống nhiều nước để tránh kết tinh trong nước tiểu."
        },
        "iv": {
            "reconstitution": "Pha theo hướng dẫn nhà sản xuất. Thường pha với D5W hoặc NaCl 0.9%. Lắc kỹ để hòa tan hoàn toàn. Dùng trong vòng 6 giờ sau khi pha.",
            "infusion_rate": "Truyền IV trong 60-90 phút (không truyền nhanh hơn). Có thể truyền trong 30-60 phút nếu cần nhưng không khuyến nghị.",
            "compatibility": [
                "D5W (Dextrose 5%)",
                "NaCl 0.9%",
                "Nước cất vô trùng"
            ],
            "incompatibility": [
                "Không trộn với các thuốc khác trong cùng một bơm tiêm hoặc chai truyền",
                "Lactated Ringer's (LR) - không tương thích",
                "Các dung dịch có cation (Al3+, Mg2+, Ca2+) - có thể tạo phức hợp"
            ],
            "notes": "Truyền IV trong 60-90 phút. Không truyền nhanh hơn. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng trong vòng 6 giờ sau khi pha. Không bảo quản lâu sau khi pha."
        }
    },
    "references": {
        "primary_sources": [
            "FDA Label: Bactrim, Septra (trimethoprim-sulfamethoxazole)",
            "UpToDate: Trimethoprim-sulfamethoxazole drug information",
            "Lexicomp: Trimethoprim-sulfamethoxazole monograph",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
            "Sanford Guide to Antimicrobial Therapy"
        ],
        "last_updated": "2025-02-03",
        "evidence_level": "Level 1 - FDA approved, multiple clinical trials, extensive clinical experience"
    }
    },

    "Levofloxacin": {
    "group": "Antibiotic - Fluoroquinolone",
    "vietnamese_name": "Levofloxacin, Tavanic",
    "administration": ["PO", "IV"],
    "indications": [
        "Viêm phổi cộng đồng",
        "Nhiễm khuẩn đường tiết niệu phức tạp",
        "Nhiễm khuẩn da và mô mềm",
        "Viêm xoang",
        "Viêm tuyến tiền liệt do vi khuẩn"
    ],
    "contraindications": [
        "Dị ứng fluoroquinolone",
        "Trẻ em <18 tuổi (trừ trường hợp đặc biệt)",
        "Có thai"
    ],
    "dosage": {
        "adult_po": "500-750mg x 1 lần/ngày",
        "adult_iv": "500-750mg IV x 1 lần/ngày",
        "adult_pneumonia": "500-750mg x 1 lần/ngày x 7-14 ngày",
        "notes": "Uống với nhiều nước. Tránh antacid, sắt trong 2 giờ"
    },
    "renal_adjustment": {
        "normal": "Không đổi",
        "30_60": "Giảm liều 50%",
        "under_30": "250-500mg x 1 lần/ngày"
    },
    "side_effects": [
        "Rối loạn tiêu hóa",
        "Nhức đầu",
        "Rối loạn giấc ngủ",
        "Rối loạn gân (viêm gân, đứt gân)",
        "QT kéo dài",
        "Hạ đường huyết (hiếm)"
    ],
    "interactions": [
        "Antacid/Sắt: giảm hấp thu",
        "Warfarin: tăng nguy cơ chảy máu",
        "Corticosteroid: tăng nguy cơ đứt gân"
    ],
    "pregnancy": "C",
    "mechanism_of_action": "Levofloxacin là fluoroquinolone kháng sinh phổ rộng, là enantiomer L của ofloxacin. Ức chế DNA gyrase (ở vi khuẩn Gram-âm) và topoisomerase IV (ở vi khuẩn Gram-dương), enzyme cần thiết cho sao chép và sửa chữa DNA. Dẫn đến tổn thương DNA và chết tế bào vi khuẩn. Phổ kháng khuẩn: Gram-âm mạnh (Enterobacteriaceae, H. influenzae, Neisseria), một số Gram-dương (Streptococcus pneumoniae - kể cả penicillin-resistant), và vi khuẩn không điển hình (Legionella, Mycoplasma, Chlamydia). Ưu điểm: dùng 1 lần/ngày (half-life dài hơn ciprofloxacin), tác dụng tốt với viêm phổi",
    "monitoring": [
        "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
        "Cấy máu và cấy từ vị trí nhiễm trùng",
        "Tendon (gân) - đau, sưng, đứt gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào",
        "Thần kinh trung ương (mất ngủ, lo âu, kích động, co giật)",
        "Tim mạch (QT kéo dài, rối loạn nhịp tim) - ECG nếu có yếu tố nguy cơ",
        "Đường huyết (tăng hoặc hạ đường huyết - đặc biệt với sulfonylurea)",
        "Chức năng thận (creatinine) - điều chỉnh liều ở suy thận",
        "Chức năng gan (ALT, AST) - hiếm viêm gan nặng"
    ],
    "precautions": [
        "NGỪNG NGAY nếu có đau, sưng gân (nguy cơ đứt gân, đặc biệt gân Achilles)",
        "Nguy cơ đứt gân tăng ở: > 60 tuổi, dùng corticosteroid, ghép tạng, hoạt động thể lực",
        "QT kéo dài → không dùng với các thuốc kéo dài QT khác, bệnh nhân có tiền sử rối loạn nhịp",
        "Co giật → không dùng ở bệnh nhân có tiền sử co giật, tránh dùng với NSAID",
        "Tăng độ nhạy cảm với ánh sáng → tránh ánh nắng trực tiếp, dùng kem chống nắng",
        "Tương tác với nhiều thuốc: giảm hấp thu với antacid, sucralfate, sắt, kẽm (cách 2 giờ)",
        "Hạ đường huyết → thận trọng với sulfonylurea",
        "Không dùng cho trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn",
        "Điều chỉnh liều khi suy thận (giảm liều khi CrCl <50)",
        "Uống nhiều nước để tránh kết tinh trong nước tiểu",
        "Ưu điểm: dùng 1 lần/ngày (compliance tốt hơn ciprofloxacin)"
    ],
    "pharmacokinetics": {
        "half_life": "6-8 giờ (dài hơn ciprofloxacin)",
        "onset": "1-2 giờ (PO), ngay lập tức (IV)",
        "duration": "q24h (1 lần/ngày)",
        "protein_binding": "24-38%",
        "clearance": "Thận (chủ yếu, 80-90% thải nguyên dạng qua nước tiểu), gan (chuyển hóa ít)"
    },
    "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dung dịch IV: bảo quản theo hướng dẫn nhà sản xuất",
    "black_box_warnings": "Nguy cơ đứt gân, viêm gân (đặc biệt gân Achilles) - có thể xảy ra bất cứ lúc nào, kể cả sau khi ngừng thuốc. Ngừng ngay nếu có đau, sưng gân. Nguy cơ tăng ở > 60 tuổi, dùng corticosteroid, ghép tạng. QT kéo dài có thể gây rối loạn nhịp tim nghiêm trọng",
    "drug_interactions": {
        "major": [
            {
                "drug": "Antacids (Aluminum, Magnesium), Sucralfate, Sắt, Kẽm",
                "mechanism": "Cation (Al3+, Mg2+, Fe2+, Zn2+) tạo phức hợp không hòa tan với levofloxacin, giảm hấp thu.",
                "effect": "Giảm hấp thu levofloxacin, giảm nồng độ trong máu, giảm hiệu quả điều trị",
                "management": "Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống levofloxacin. Không uống cùng lúc."
            },
            {
                "drug": "Warfarin",
                "mechanism": "Levofloxacin có thể ảnh hưởng đến chuyển hóa warfarin.",
                "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                "management": "Theo dõi INR chặt chẽ khi bắt đầu, thay đổi liều, hoặc ngừng levofloxacin. Điều chỉnh liều warfarin nếu cần."
            }
        ],
        "moderate": [
            {
                "drug": "Corticosteroid",
                "mechanism": "Cả hai đều tăng nguy cơ đứt gân, tác dụng cộng dồn.",
                "effect": "Tăng nguy cơ viêm gân, đứt gân",
                "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ dấu hiệu đau, sưng gân. Ngừng ngay nếu có đau gân."
            },
            {
                "drug": "NSAID",
                "mechanism": "Cả hai đều có thể gây co giật, tác dụng cộng dồn.",
                "effect": "Tăng nguy cơ co giật",
                "management": "Tránh dùng đồng thời nếu có thể. Thận trọng ở bệnh nhân có tiền sử co giật."
            },
            {
                "drug": "Sulfonylurea",
                "mechanism": "Levofloxacin có thể gây hạ đường huyết.",
                "effect": "Tăng nguy cơ hạ đường huyết",
                "management": "Theo dõi đường huyết. Điều chỉnh liều sulfonylurea nếu cần."
            }
        ],
        "minor": []
    },
    "contraindications": {
        "tuyệt_đối": [
            "Dị ứng levofloxacin hoặc các fluoroquinolone khác",
            "Có thai - chống chỉ định tuyệt đối, nguy cơ tổn thương sụn thai nhi",
            "Trẻ em < 18 tuổi (trừ trường hợp đặc biệt) - nguy cơ tổn thương sụn, viêm khớp",
            "QT kéo dài hoặc rối loạn nhịp tim nặng - tăng nguy cơ loạn nhịp tim nghiêm trọng"
        ],
        "tương_đối": [
            "Bệnh nhân > 60 tuổi - tăng nguy cơ đứt gân, viêm gân",
            "Dùng corticosteroid - tăng nguy cơ đứt gân",
            "Ghép cơ quan - tăng nguy cơ đứt gân",
            "Tiền sử co giật - tăng nguy cơ co giật",
            "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
            "Dùng với warfarin - tăng nguy cơ chảy máu",
            "Hoạt động thể lực nặng - tăng nguy cơ đứt gân"
        ]
    },
    "pregnancy_lactation": {
        "fda_category": "C",
        "pregnancy_details": "Levofloxacin là thuốc phân loại C. Các nghiên cứu trên động vật cho thấy có thể gây tổn thương sụn ở khớp ở thai nhi. Có báo cáo về tổn thương sụn ở trẻ em khi dùng trong thai kỳ. CHỐNG CHỈ ĐỊNH trong thai kỳ trừ khi lợi ích vượt quá nguy cơ rõ ràng và không có lựa chọn khác. Nhiễm trùng nặng có thể gây nguy hiểm cho thai nhi, nhưng nên dùng kháng sinh khác nếu có thể.",
        "lactation": {
            "safety": "Compatible (với thận trọng)",
            "details": "Levofloxacin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ. Tuy nhiên, fluoroquinolone có thể gây tổn thương sụn ở trẻ sơ sinh.",
            "recommendation": "Có thể dùng khi cho con bú với thận trọng. Dùng liều thấp nhất hiệu quả. Theo dõi trẻ sơ sinh. Tránh dùng nếu có lựa chọn khác."
        }
    },
    "hepatic_adjustment": {
        "mild": "Không cần điều chỉnh liều. Levofloxacin chuyển hóa ít qua gan, thải trừ chủ yếu qua thận.",
        "moderate": "Không cần điều chỉnh liều. Thận trọng nếu có suy thận kèm theo.",
        "severe": "Thận trọng, có thể cần giảm liều nhẹ. Chuyển hóa có thể giảm ở suy gan nặng, nhưng thải trừ chủ yếu qua thận nên ít ảnh hưởng.",
        "notes": "Levofloxacin chuyển hóa ít qua gan, thải trừ chủ yếu qua thận (80-90% nguyên dạng). Suy gan có thể giảm chuyển hóa nhẹ nhưng không đáng kể. Tuy nhiên, suy gan có thể kèm theo suy thận, nên cần điều chỉnh liều theo chức năng thận."
    },
    "overdose_management": {
        "symptoms": [
            "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy, đau bụng",
            "Triệu chứng thần kinh: Co giật, kích động, lo âu, mất ngủ, trầm cảm, rối loạn tâm thần",
            "Triệu chứng gân: Đau gân, viêm gân, đứt gân (đặc biệt gân Achilles)",
            "Triệu chứng tim mạch: QT kéo dài, rối loạn nhịp tim, có thể gây tử vong",
            "Triệu chứng chuyển hóa: Hạ hoặc tăng đường huyết",
            "Triệu chứng nghiêm trọng: Rối loạn nhịp tim nghiêm trọng, đứt gân"
        ],
        "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
        "treatment": [
            "Ngừng ngay levofloxacin",
            "Rửa dạ dày hoặc than hoạt nếu uống trong vòng 1-2 giờ (nếu không có chống chỉ định)",
            "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2, ECG",
            "Điều trị co giật nếu có: Benzodiazepine, theo dõi thần kinh chặt chẽ",
            "Điều trị rối loạn nhịp tim nếu có: Theo dõi ECG liên tục, điều trị loạn nhịp nếu cần",
            "Điều trị đau gân nếu có: Ngừng ngay, nghỉ ngơi, chườm lạnh, thuốc giảm đau nếu cần",
            "Điều trị hạ đường huyết nếu có: Truyền glucose, theo dõi đường huyết",
            "Điều trị triệu chứng tiêu hóa: Chống nôn nếu cần, truyền dịch nếu mất nước"
        ],
        "monitoring": "Theo dõi dấu hiệu sinh tồn, ECG, dấu hiệu thần kinh, dấu hiệu gân, đường huyết trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng."
    },
    "reversal_agents": None,
    "administration_instructions": {
        "oral": {
            "with_food": "Có thể uống với hoặc không thức ăn. Uống với nước đầy đủ (ít nhất 1-2 ly nước) để tránh kết tinh trong nước tiểu.",
            "timing": "Uống 1 lần/ngày (q24h), cùng một thời điểm mỗi ngày. Cách ít nhất 2 giờ (tốt nhất 4 giờ) trước hoặc sau khi uống antacid, sucralfate, sắt, kẽm. Không uống cùng lúc với các cation này. Ưu điểm: dùng 1 lần/ngày, compliance tốt hơn ciprofloxacin."
        },
        "iv": {
            "reconstitution": "Pha với NS hoặc D5W. Nồng độ pha: 5mg/ml (tối đa). Pha 500mg trong 100ml dịch = 5mg/ml. Pha 750mg trong 150ml dịch = 5mg/ml.",
            "infusion_rate": "Truyền trong 60 phút (ít nhất 60 phút). Không truyền quá nhanh. Tốc độ: 100ml/60 phút = ~1.7ml/phút. 150ml/60 phút = ~2.5ml/phút.",
            "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
            "incompatibility": ["Không trộn với các thuốc khác trong cùng một ống truyền. Kiểm tra tương thích trước khi pha. Tránh pha với cation (Al3+, Mg2+, Ca2+)."],
            "notes": "Theo dõi chức năng thận, dấu hiệu gân, thần kinh trong quá trình truyền. Có thể gây kích ứng tĩnh mạch - thay đổi vị trí tiêm nếu cần. Liều: 500-750mg x 1 lần/ngày (q24h)."
        }
    },
    "references": {
        "primary_sources": [
            "FDA Drug Label - Levofloxacin (Tavanic)",
            "UpToDate - Levofloxacin: Drug Information",
            "Medscape - Levofloxacin Drug Reference",
            "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
            "Lexicomp Online - Levofloxacin Monograph",
            "Micromedex - Levofloxacin Drug Information",
            "IDSA Guidelines - Antimicrobial Therapy"
        ],
        "last_updated": "2024-12-19",
        "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
    }
    }

}

__all__ = ['ANTIMICROBIAL_ANTIBIOTICS']
