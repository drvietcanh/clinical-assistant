"""
Beta-lactam Antibiotics
Penicillin/Beta-lactamase Inhibitor and Carbapenem
"""

BETA_LACTAM_ANTIBIOTICS = {
    "Aztreonam": {
        "group": "Antibiotic - Monobactam",
        "vietnamese_name": "Aztreonam, Azactam",
        "administration": ["IV", "IM", "Inhaled"],
        "indications": [
            "Nhiễm khuẩn Gram âm nặng (bệnh viện)",
            "Nhiễm khuẩn huyết do Gram âm",
            "Viêm phổi bệnh viện do Gram âm",
            "Nhiễm khuẩn đường tiết niệu phức tạp",
            "Nhiễm khuẩn ổ bụng (kết hợp với thuốc kỵ khí)",
            "Viêm phổi do Pseudomonas aeruginosa (kháng sinh mạn tính) - dạng hít",
            "Bệnh nhân dị ứng penicillin (KHÔNG có phản ứng chéo)"
        ],
        "contraindications": [
            "Dị ứng aztreonam",
            "Dị ứng beta-lactam (thận trọng, nhưng thường an toàn)"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng aztreonam"
            ],
            "tương_đối": [
                "Dị ứng beta-lactam (thận trọng, nhưng thường an toàn do không có phản ứng chéo)"
            ]
        },
        "black_box_warnings": "Không có cảnh báo hộp đen đặc biệt. Tuy nhiên, cần thận trọng ở bệnh nhân suy thận nặng.",
        "dosage": {
            "adult_iv_standard": "1-2g IV mỗi 8-12 giờ",
            "adult_iv_severe": "2g IV mỗi 6-8 giờ",
            "adult_iv_max": "2g IV mỗi 6 giờ (tối đa 8g/ngày)",
            "adult_im": "1g IM mỗi 8-12 giờ",
            "adult_inhaled": "75mg x 3 lần/ngày (dạng hít, cho viêm phổi mạn tính do Pseudomonas)",
            "pediatric_iv": "30mg/kg IV mỗi 6-8 giờ (tối đa 120mg/kg/ngày)",
            "notes": "Pha trong 50-100ml NS hoặc D5W, truyền trong 20-60 phút. KHÔNG có phản ứng chéo với penicillin (an toàn cho bệnh nhân dị ứng penicillin)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "1-2g IV mỗi 12 giờ",
            "under_30": "0.5-1g IV mỗi 12 giờ",
            "hemodialysis": "0.5-1g IV sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Phát ban (hiếm)",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Tăng men gan (hiếm)",
            "Giảm tiểu cầu (hiếm)",
            "Phản ứng tại chỗ tiêm (IM)"
        ],
        "interactions": [
            "Aminoglycosides: tác dụng hiệp đồng (có thể dùng kết hợp)",
            "Clindamycin, Metronidazole: dùng kết hợp cho nhiễm khuẩn hỗn hợp (Gram âm + kỵ khí)"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Aztreonam là monobactam (chỉ có vòng beta-lactam đơn, không có vòng thiazolidine như penicillin hoặc dihydrothiazine như cephalosporin). Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding protein 3 (PBP-3) của vi khuẩn Gram âm. Phổ kháng khuẩn: chỉ hiệu quả với vi khuẩn Gram âm (Enterobacteriaceae, Pseudomonas aeruginosa, Haemophilus influenzae, Neisseria), KHÔNG hiệu quả với vi khuẩn Gram dương hoặc kỵ khí. ĐẶC ĐIỂM QUAN TRỌNG: KHÔNG có phản ứng chéo với penicillin hoặc cephalosporin (cấu trúc khác), nên an toàn cho bệnh nhân dị ứng penicillin. Đây là lựa chọn quan trọng cho bệnh nhân dị ứng penicillin cần điều trị nhiễm khuẩn Gram âm.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Chức năng gan (ALT, AST, bilirubin) - hiếm tăng men gan",
            "Công thức máu (tiểu cầu) - hiếm giảm tiểu cầu",
            "Dấu hiệu dị ứng (phát ban) - hiếm nhưng cần theo dõi",
            "Đáp ứng điều trị (sốt, triệu chứng nhiễm khuẩn)"
        ],
        "precautions": [
            "KHÔNG có phản ứng chéo với penicillin - an toàn cho bệnh nhân dị ứng penicillin",
            "Chỉ hiệu quả với vi khuẩn Gram âm - KHÔNG dùng đơn độc cho nhiễm khuẩn hỗn hợp",
            "Nhiễm khuẩn hỗn hợp (Gram âm + kỵ khí): kết hợp với clindamycin hoặc metronidazole",
            "Nhiễm khuẩn hỗn hợp (Gram âm + Gram dương): kết hợp với vancomycin hoặc linezolid",
            "Điều chỉnh liều theo chức năng thận",
            "Dạng hít: chỉ dùng cho viêm phổi mạn tính do Pseudomonas (cystic fibrosis)"
        ],
        "pharmacokinetics": {
            "half_life": "1.5-2 giờ",
            "onset": "Ngay lập tức sau khi truyền",
            "duration": "8-12 giờ (phụ thuộc liều và chức năng thận)",
            "protein_binding": "56%",
            "clearance": "Thận (60-70% thải trừ qua thận dạng nguyên dạng), gan (30-40% chuyển hóa)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch đã pha: ổn định trong 24 giờ ở nhiệt độ phòng, 48 giờ ở 2-8°C.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Tác dụng hiệp đồng chống vi khuẩn Gram âm",
                    "effect": "Tăng hiệu quả điều trị (synergistic effect)",
                    "management": "Có thể dùng kết hợp cho nhiễm khuẩn Gram âm nặng. Theo dõi chức năng thận (cả hai đều độc với thận)."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng aztreonam"
            ],
            "tương_đối": [
                "Dị ứng beta-lactam - thận trọng, nhưng thường an toàn (không có phản ứng chéo)",
                "Suy thận nặng - giảm liều",
                "Suy gan nặng - thận trọng (chuyển hóa một phần ở gan)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Aztreonam là thuốc phân loại B. Không có bằng chứng về nguy cơ dị tật thai nhi trong các nghiên cứu trên động vật. Không có nghiên cứu đầy đủ trên phụ nữ có thai, nhưng aztreonam được sử dụng trong thai kỳ và có vẻ an toàn. Nhiễm khuẩn nặng có thể gây nguy hiểm cho cả mẹ và thai nhi nếu không điều trị.",
            "lactation": {
                "safety": "Compatible",
                "details": "Aztreonam bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Aztreonam bài tiết vào sữa mẹ ở nồng độ thấp và không gây hại cho trẻ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng (chuyển hóa một phần ở gan)",
            "severe": "Thận trọng, có thể tăng tác dụng (giảm chuyển hóa)",
            "notes": "Aztreonam chuyển hóa một phần ở gan (30-40%). Suy gan có thể làm giảm chuyển hóa, nhưng ảnh hưởng ít hơn so với suy thận (thải trừ chủ yếu qua thận)."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật (hiếm, thường ở suy thận nặng)",
                "Rối loạn thần kinh (hiếm)",
                "Tăng men gan (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng aztreonam",
                "Hỗ trợ hô hấp: Thở oxy, nếu cần hỗ trợ thông khí cơ học",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam, lorazepam) IV",
                "  - Phenytoin hoặc fosphenytoin IV nếu cần",
                "Lọc máu (hemodialysis) nếu suy thận nặng và tích lũy",
                "Theo dõi: Chức năng thận, gan, thần kinh"
            ],
            "monitoring": "Theo dõi chức năng thận, gan, thần kinh liên tục cho đến khi hồi phục."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột: 1g trong 10ml NS = 100mg/ml, sau đó pha loãng trong 50-100ml NS hoặc D5W.",
                "infusion_rate": "Standard: 1-2g IV mỗi 8-12 giờ, truyền trong 20-60 phút. Severe: 2g IV mỗi 6-8 giờ. Tối đa: 2g IV mỗi 6 giờ (8g/ngày).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)", "LR (Lactated Ringer's)"],
                "incompatibility": [
                    "Không trộn với nafcillin, metronidazole (kết tủa). Dùng đường truyền riêng."
                ],
                "notes": "QUAN TRỌNG: 1) KHÔNG có phản ứng chéo với penicillin - an toàn cho bệnh nhân dị ứng penicillin, 2) Chỉ hiệu quả với vi khuẩn Gram âm, 3) Nhiễm khuẩn hỗn hợp: kết hợp với clindamycin/metronidazole (kỵ khí) hoặc vancomycin/linezolid (Gram dương), 4) Điều chỉnh liều theo chức năng thận, 5) Pha trong 50-100ml NS hoặc D5W, truyền trong 20-60 phút."
            },
            "im": {
                "reconstitution": "Pha bột: 1g trong 3ml NS = 333mg/ml.",
                "injection_site": "Cơ lớn (đùi, cánh tay).",
                "notes": "IM: 1g mỗi 8-12 giờ. Tiêm sâu vào cơ, không tiêm vào mỡ dưới da. Có thể gây đau tại chỗ tiêm."
            },
            "inhaled": {
                "reconstitution": "Dùng dạng hít sẵn có (75mg/lần).",
                "dose": "75mg x 3 lần/ngày (cách nhau 4 giờ), khí dung qua nebulizer.",
                "notes": "Chỉ dùng cho viêm phổi mạn tính do Pseudomonas (cystic fibrosis). Không dùng cho nhiễm khuẩn cấp tính. Theo dõi chức năng phổi."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aztreonam (Azactam)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Aztreonam: Drug Information",
                "Allergy Guidelines - Beta-lactam Allergy",
                "Medscape - Aztreonam Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, allergy guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Gram-Negative Infections",
            "IDSA Guidelines - Complicated Urinary Tract Infections"
        ]
    },
    
    "Cefiderocol": {
        "group": "Antibiotic - Siderophore Cephalosporin",
        "vietnamese_name": "Cefiderocol, Fetroja",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn đường tiết niệu phức tạp (cUTI) - Gram-âm kháng thuốc",
            "Viêm phổi bệnh viện (HABP/VABP) - Gram-âm kháng thuốc",
            "Nhiễm khuẩn Gram-âm kháng carbapenem (CRE) - Acinetobacter, Pseudomonas, Enterobacteriaceae",
            "Nhiễm khuẩn Gram-âm đa kháng (MDR) - khi các kháng sinh khác không hiệu quả"
        ],
        "contraindications": [
            "Dị ứng cefiderocol hoặc cephalosporin",
            "Dị ứng beta-lactam nặng"
        ],
        "dosage": {
            "adult_cuti": "2g IV mỗi 8 giờ (truyền trong 3 giờ)",
            "adult_habp_vabp": "2g IV mỗi 8 giờ (truyền trong 3 giờ)",
            "notes": "Cefiderocol là kháng sinh mới (FDA 2019), đặc biệt hiệu quả với Gram-âm kháng carbapenem. Truyền trong 3 giờ để tối ưu hóa hiệu quả. Điều chỉnh liều theo chức năng thận."
        },
        "renal_adjustment": {
            "normal": "Không đổi (CrCl ≥60: 2g IV mỗi 8 giờ)",
            "30_60": "1.5g IV mỗi 8 giờ (CrCl 30-59)",
            "under_30": "1g IV mỗi 8 giờ (CrCl 15-29), 0.75g IV mỗi 8 giờ (CrCl <15)",
            "hemodialysis": "0.75g IV mỗi 8 giờ (sau lọc máu)"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Tăng men gan",
            "Viêm tĩnh mạch tại chỗ tiêm",
            "Nhiễm C. difficile",
            "Tăng nguy cơ tử vong (trong HABP/VABP) - FDA warning"
        ],
        "interactions": [
            "Aminoglycosides: tác dụng hiệp đồng",
            "Probenecid: tăng nồng độ cefiderocol"
        ],
        "pregnancy": "B - Thận trọng",
        "mechanism_of_action": "Cefiderocol là siderophore cephalosporin (kháng sinh beta-lactam mới, FDA 2019). Có cơ chế đặc biệt: (1) Cephalosporin: ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), (2) Siderophore: cefiderocol có nhóm siderophore, gắn với sắt (Fe3+), được vận chuyển vào tế bào vi khuẩn qua hệ thống vận chuyển sắt (iron transport system) của vi khuẩn. Cơ chế này cho phép cefiderocol vượt qua các cơ chế kháng thuốc (porin loss, efflux pumps, beta-lactamase) và đạt nồng độ cao trong tế bào vi khuẩn. ĐẶC ĐIỂM: (1) Đặc biệt hiệu quả với Gram-âm kháng carbapenem (CRE) - Acinetobacter baumannii, Pseudomonas aeruginosa, Enterobacteriaceae (Klebsiella, E. coli), (2) Phổ rộng Gram-âm (bao gồm ESBL, AmpC, carbapenemase-producing), (3) Truyền trong 3 giờ để tối ưu hóa hiệu quả, (4) FDA warning về tăng nguy cơ tử vong trong HABP/VABP (cần cân nhắc kỹ), (5) Điều chỉnh liều theo chức năng thận (CrCl).",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR, CrCl) - điều chỉnh liều theo thận, QUAN TRỌNG",
            "Dấu hiệu nhiễm trùng (sốt, WBC, CRP)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu nhiễm C. difficile",
            "Dấu hiệu tử vong (trong HABP/VABP) - FDA warning"
        ],
        "precautions": [
            "FDA warning về tăng nguy cơ tử vong trong HABP/VABP - cần cân nhắc kỹ trước khi dùng",
            "PHẢI điều chỉnh liều theo chức năng thận (CrCl) - QUAN TRỌNG",
            "Truyền trong 3 giờ (không nhanh hơn) để tối ưu hóa hiệu quả",
            "Chỉ dùng cho nhiễm khuẩn Gram-âm kháng thuốc khi các kháng sinh khác không hiệu quả",
            "Nguy cơ nhiễm C. difficile - theo dõi tiêu chảy",
            "Theo dõi nhiễm nấm thứ phát khi dùng kéo dài",
            "Pha trong NS hoặc D5W, truyền qua đường truyền riêng"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), kéo dài ở suy thận",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "8 giờ (liều q8h)",
            "protein_binding": "40-60%",
            "metabolism": "Chuyển hóa tối thiểu",
            "clearance": "Chủ yếu qua thận (60-70% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.2-0.3 L/kg"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Sau khi pha: bảo quản ở nhiệt độ phòng 4 giờ, hoặc trong tủ lạnh 24 giờ.",
        "black_box_warnings": "FDA warning: Tăng nguy cơ tử vong trong viêm phổi bệnh viện (HABP/VABP) so với các kháng sinh khác. Cần cân nhắc kỹ trước khi dùng cho HABP/VABP. Chỉ dùng khi các kháng sinh khác không phù hợp.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết cefiderocol ở thận, làm tăng nồng độ cefiderocol.",
                    "effect": "Tăng nồng độ cefiderocol, tăng nguy cơ tác dụng phụ",
                    "management": "Không khuyến cáo dùng đồng thời. Nếu bắt buộc, giảm liều cefiderocol và theo dõi sát."
                }
            ],
            "minor": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Tác dụng hiệp đồng chống lại vi khuẩn Gram-âm.",
                    "effect": "Tăng hiệu quả kháng khuẩn",
                    "management": "Có thể dùng kết hợp để tăng hiệu quả. Theo dõi chức năng thận và nồng độ aminoglycoside."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng cefiderocol hoặc cephalosporin",
                "Dị ứng beta-lactam nặng (phản ứng chéo có thể xảy ra)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <15) - cần giảm liều đáng kể",
                "HABP/VABP - FDA warning về tăng nguy cơ tử vong, cần cân nhắc kỹ",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng cefiderocol hoặc cephalosporin",
                "Dị ứng beta-lactam nặng (phản ứng chéo có thể xảy ra)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <15) - cần giảm liều đáng kể",
                "HABP/VABP - FDA warning về tăng nguy cơ tử vong, cần cân nhắc kỹ",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Cefiderocol là thuốc phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Cefiderocol được sử dụng trong nhiễm trùng nặng ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Cefiderocol bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ thấp và không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Cefiderocol bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều. Cefiderocol chuyển hóa tối thiểu qua gan, thải trừ chủ yếu qua thận.",
            "moderate": "Không cần điều chỉnh liều.",
            "severe": "Không cần điều chỉnh liều. Thải trừ chủ yếu qua thận, không tích lũy ở suy gan.",
            "notes": "Cefiderocol chuyển hóa tối thiểu qua gan, thải trừ chủ yếu qua thận (60-70% bài tiết nguyên dạng). Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật",
                "Tăng men gan",
                "Phát ban",
                "Tiêu chảy"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay cefiderocol nếu đang truyền",
                "Điều trị co giật: Benzodiazepine (diazepam, lorazepam)",
                "Hỗ trợ hô hấp nếu cần",
                "Lọc máu: Hemodialysis có thể loại bỏ cefiderocol nếu suy thận nặng",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, chức năng gan, dấu hiệu co giật trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có co giật, phản ứng dị ứng nghiêm trọng, hoặc C. difficile."},
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột khô với nước cất vô trùng hoặc NS. Nồng độ thường dùng: 50 mg/ml. Lắc kỹ để hòa tan hoàn toàn.",
                "infusion_rate": "Truyền IV trong 3 giờ (QUAN TRỌNG: không nhanh hơn). Không truyền nhanh hơn 3 giờ.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng hoặc flush kỹ giữa các thuốc."
                ],
                "notes": "QUAN TRỌNG: 1) Truyền trong 3 giờ (không nhanh hơn), 2) Điều chỉnh liều theo chức năng thận (CrCl), 3) FDA warning về tăng nguy cơ tử vong trong HABP/VABP, 4) Chỉ dùng cho nhiễm khuẩn Gram-âm kháng thuốc."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cefiderocol (Fetroja)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Cefiderocol: Drug Information",
                "Medscape - Cefiderocol Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels (2019), IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "High"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Ventilator-Associated Pneumonia",
            "IDSA Guidelines - Multidrug-Resistant Gram-Negative Infections"
        ]
    },
    "Doripenem": {
        "group": "Antibiotic - Carbapenem",
        "vietnamese_name": "Doripenem, Doribax",
        "administration": ["IV"],
        "indications": [
            "Nhiễm khuẩn ổ bụng phức tạp",
            "Nhiễm khuẩn đường tiết niệu phức tạp (bao gồm viêm bể thận)",
            "Viêm phổi bệnh viện",
            "Nhiễm khuẩn nặng đa kháng",
            "Nhiễm khuẩn do Pseudomonas aeruginosa"
        ],
        "contraindications": [
            "Dị ứng doripenem",
            "Dị ứng carbapenem",
            "Dị ứng beta-lactam nặng"
        ],
        "dosage": {
            "adult_standard": "500mg IV mỗi 8 giờ",
            "adult_severe": "500mg IV mỗi 6 giờ hoặc 1g IV mỗi 8 giờ",
            "adult_pneumonia": "500mg IV mỗi 8 giờ",
            "adult_uti": "500mg IV mỗi 8 giờ",
            "notes": "Truyền trong 60 phút (liều 500mg) hoặc 120 phút (liều 1g). Tương tự meropenem nhưng có thể hiệu quả hơn với một số chủng Pseudomonas kháng meropenem."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "250mg IV mỗi 8 giờ",
            "under_30": "250mg IV mỗi 12 giờ",
            "hemodialysis": "250mg IV sau mỗi lần lọc máu"
        },
        "side_effects": [
            "Tiêu chảy",
            "Buồn nôn, nôn",
            "Phát ban",
            "Đau đầu",
            "Co giật (hiếm, ít hơn imipenem)",
            "Tăng men gan (hiếm)",
            "Viêm tĩnh mạch tại chỗ tiêm"
        ],
        "interactions": [
            "Valproate: giảm nồng độ valproate (có thể gây co giật)",
            "Probenecid: tăng nồng độ doripenem"
        ],
        "pregnancy": "B - An toàn trong thai kỳ",
        "mechanism_of_action": "Doripenem là carbapenem kháng sinh beta-lactam, tương tự meropenem. Ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), đặc biệt PBP-2 và PBP-3, dẫn đến ly giải tế bào vi khuẩn. Phổ kháng khuẩn rộng, bao phủ cả vi khuẩn Gram-dương, Gram-âm (bao gồm Pseudomonas aeruginosa), và kỵ khí. Kháng được nhiều beta-lactamase do có cấu trúc vòng beta-lactam bền vững. Đặc điểm: (1) Tương tự meropenem về phổ và hiệu quả, (2) Có thể hiệu quả hơn với một số chủng Pseudomonas kháng meropenem, (3) Ít gây co giật hơn imipenem, (4) Truyền trong 60-120 phút (chậm hơn meropenem), (5) Không cần cilastatin (không bị phân hủy bởi dehydropeptidase I).",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR) - điều chỉnh liều theo thận",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Dấu hiệu nhiễm C. difficile",
            "Chức năng gan (ALT, AST) - hiếm viêm gan",
            "Dấu hiệu co giật (hiếm, ít hơn imipenem)",
            "Nồng độ valproate nếu đang dùng (doripenem làm giảm nồng độ valproate)"
        ],
        "precautions": [
            "PHẢI điều chỉnh liều theo chức năng thận (eGFR) - quan trọng",
            "Truyền trong 60 phút (liều 500mg) hoặc 120 phút (liều 1g) - chậm hơn meropenem",
            "Nguy cơ co giật tăng ở suy thận nặng và bệnh nhân có tiền sử co giật (ít hơn imipenem)",
            "TRÁNH dùng với valproate (giảm nồng độ valproate, tăng nguy cơ co giật)",
            "Theo dõi nhiễm C. difficile",
            "Không pha trộn với các thuốc khác",
            "Có thể hiệu quả hơn với một số chủng Pseudomonas kháng meropenem"
        ],
        "pharmacokinetics": {
            "half_life": "1 giờ",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "8 giờ (liều q8h)",
            "protein_binding": "8%",
            "clearance": "Thận (70% bài tiết nguyên dạng qua nước tiểu), cần điều chỉnh thận"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 1 giờ, hoặc trong tủ lạnh 8 giờ. Dùng ngay sau khi pha.",
        "black_box_warnings": "Nguy cơ co giật, đặc biệt ở suy thận nặng và bệnh nhân có tiền sử co giật. TRÁNH dùng với valproate (giảm nồng độ valproate, tăng nguy cơ co giật).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Valproate (Valproic acid)",
                    "mechanism": "Doripenem ức chế hấp thu valproate và tăng chuyển hóa valproate, làm giảm nồng độ valproate trong máu đáng kể",
                    "effect": "Giảm nồng độ valproate 60-90%, tăng nguy cơ co giật (nguy hiểm tính mạng ở bệnh nhân động kinh)",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc: (1) Theo dõi nồng độ valproate thường xuyên, (2) Tăng liều valproate 2-3 lần, (3) Cân nhắc dùng thuốc chống co giật khác (phenytoin, levetiracetam), (4) Theo dõi dấu hiệu co giật chặt chẽ, (5) Cân nhắc dừng doripenem nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết doripenem ở ống thận, tăng nồng độ doripenem",
                    "effect": "Tăng nồng độ doripenem, tăng nguy cơ tác dụng phụ",
                    "management": "Tránh dùng đồng thời. Nếu bắt buộc, giảm liều doripenem."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng doripenem",
                "Dị ứng carbapenem",
                "Dị ứng beta-lactam nặng (sốc phản vệ)"
            ],
            "tương_đối": [
                "Dị ứng cephalosporin - phản ứng chéo 5-10%, thận trọng",
                "Suy thận nặng (CrCl <30) - cần điều chỉnh liều",
                "Dùng với valproate - giảm nồng độ valproate đáng kể, tăng nguy cơ co giật",
                "Bệnh nhân có tiền sử co giật - tăng nguy cơ co giật",
                "Tiền sử nhiễm C. difficile - tăng nguy cơ tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Doripenem là thuốc phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Các nghiên cứu trên người không cho thấy nguy cơ tăng dị tật bẩm sinh. Carbapenem được sử dụng trong nhiễm trùng nặng ở phụ nữ có thai và được coi là an toàn khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Doripenem bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Doripenem bài tiết vào sữa mẹ ở nồng độ thấp và không gây tác dụng phụ ở trẻ bú mẹ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)",
            "notes": "Doripenem thải trừ chủ yếu qua thận (70% bài tiết nguyên dạng). Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng tiêu hóa: Buồn nôn, nôn, tiêu chảy",
                "Triệu chứng thần kinh: Đau đầu, chóng mặt, co giật (hiếm)",
                "Triệu chứng thận: Suy thận cấp, tăng creatinine (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay doripenem nếu đang truyền",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam, lorazepam) IV",
                "  - Phenytoin hoặc fosphenytoin IV nếu cần",
                "Điều trị suy thận cấp nếu có:",
                "  - Bù dịch đầy đủ",
                "  - Lọc máu nếu cần (hemodialysis có thể loại bỏ doripenem)",
                "Theo dõi: Dấu hiệu sinh tồn, chức năng thận, thần kinh"
            ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, chức năng thận, thần kinh trong 24-48 giờ."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có reversal agent đặc hiệu. Điều trị hỗ trợ."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột khô trong NS hoặc D5W: 500mg pha trong 10ml = 50mg/ml. Sau đó pha loãng trong 100ml NS hoặc D5W để truyền.",
                "infusion_rate": "Truyền IV trong 60 phút (liều 500mg) hoặc 120 phút (liều 1g). Không truyền nhanh hơn. Liều: 500mg IV mỗi 8 giờ (bình thường), 250mg IV mỗi 8-12 giờ (suy thận).",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Dùng đường truyền riêng hoặc flush trước/sau khi truyền thuốc khác."
                ],
                "notes": "QUAN TRỌNG: 1) PHẢI điều chỉnh liều theo chức năng thận (eGFR), 2) Truyền trong 60-120 phút (chậm hơn meropenem), 3) Nguy cơ co giật tăng ở suy thận nặng, 4) TRÁNH dùng với valproate (giảm nồng độ valproate), 5) Theo dõi nhiễm C. difficile, 6) Có thể hiệu quả hơn với một số chủng Pseudomonas kháng meropenem."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Doripenem (Doribax)",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Doripenem: Drug Information",
                "Medscape - Doripenem Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"neurological": "Moderate (seizures)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Complicated Intra-abdominal Infections",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Hospital-Acquired Pneumonia"
        ]
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
        ],',
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
        "contraindications_detail": {
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
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng hoặc C. difficile."},
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
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"neurological": "Moderate (seizures)", "renal": "Moderate"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Complicated Intra-abdominal Infections",
            "IDSA Guidelines - Complicated Skin and Soft Tissue Infections",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Community-Acquired Pneumonia"
        ]
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
        ],',
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
        "contraindications_detail": {
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
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có co giật, phản ứng dị ứng nghiêm trọng, hoặc C. difficile."},
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
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"neurological": "High (seizures)", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Ventilator-Associated Pneumonia",
            "IDSA Guidelines - Complicated Intra-abdominal Infections",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Febrile Neutropenia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
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
    ],',
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
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"neurological": "Moderate (seizures)", "renal": "Low"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Ventilator-Associated Pneumonia",
            "IDSA Guidelines - Complicated Intra-abdominal Infections",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "IDSA Guidelines - Febrile Neutropenia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

    "Penicillin G":     {
        "group": "Antibiotic - Penicillin (Natural)",
        "vietnamese_name": "Penicillin G, Benzylpenicillin",
        "administration": [
            "IV",
            "IM"
    ],
        "indications": [
            "Nhiễm khuẩn do Streptococcus (viêm họng, viêm phổi, nhiễm khuẩn da)",
            "Nhiễm khuẩn do Treponema pallidum (giang mai)",
            "Nhiễm khuẩn do Neisseria meningitidis (viêm màng não)",
            "Nhiễm khuẩn do Clostridium (uốn ván, hoại thư)",
            "Nhiễm khuẩn do Actinomyces",
            "Viêm nội tâm mạc do Streptococcus nhạy cảm"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng penicillin (phản ứng nghiêm trọng, sốc phản vệ)",
                "Dị ứng beta-lactam (phản ứng chéo)"
    ],
            "tương_đối": [
                "Suy thận nặng (cần giảm liều đáng kể)",
                "Tiền sử co giật (tăng nguy cơ co giật)",
                "Suy tim (hàm lượng natri cao)"
    ],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng penicillin",
                "Dị ứng beta-lactam",
                "Tiền sử sốc phản vệ với penicillin"
    ],
            "tương_đối": [],
        },
        "reversal_agents": None,
        "dosage": {
            "adult_standard": "1-4 triệu đơn vị IV mỗi 4-6 giờ",
            "adult_severe": "4-6 triệu đơn vị IV mỗi 4 giờ",
            "adult_meningitis": "4 triệu đơn vị IV mỗi 4 giờ",
            "adult_syphilis": "2.4 triệu đơn vị IM x 1 liều (early), 2.4 triệu đơn vị IM mỗi tuần x 3 tuần (late)",
            "adult_endocarditis": "4-6 triệu đơn vị IV mỗi 4 giờ",
            "notes": "1 triệu đơn vị = 600mg. Pha trong NS hoặc D5W, truyền IV trong 30-60 phút",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%",
            "hemodialysis": "Bổ sung liều sau lọc máu",
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
        "mechanism_of_action": """Penicillin G (benzylpenicillin) là penicillin tự nhiên đầu tiên, ức chế tổng hợp thành tế bào vi khuẩn bằng cách gắn với penicillin-binding proteins (PBPs), ngăn cản quá trình cross-linking của peptidoglycan. Phổ kháng khuẩn: Gram-dương (Streptococcus, Staphylococcus nhạy cảm, Clostridium, Actinomyces), một số Gram-âm (Neisseria meningitidis, Neisseria gonorrhoeae nhạy cảm), và xoắn khuẩn (Treponema pallidum). Không hiệu quả với vi khuẩn sản xuất beta-lactamase. Phải dùng đường tiêm (IV/IM) vì bị phá hủy bởi acid dạ dày.""",
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
            "clearance": "Chủ yếu qua thận (60-90% bài tiết nguyên dạng), cần điều chỉnh thận",
        },
        "storage": """Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.""",
        "black_box_warnings": """Có thể gây sốc phản vệ nghiêm trọng, đặc biệt ở bệnh nhân có tiền sử dị ứng penicillin. Co giật có thể xảy ra ở liều cao hoặc suy thận.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Probenecid",
                    "mechanism": """Probenecid ức chế bài tiết ống thận của penicillin G, làm giảm thải trừ và tăng nồng độ penicillin G trong máu.""",
                    "effect": "Tăng nồng độ penicillin G, tăng thời gian bán hủy, tăng hiệu quả nhưng cũng tăng nguy cơ độc tính",
                    "management": """Có thể dùng cùng để tăng nồng độ penicillin G (ví dụ: trong điều trị giang mai). Theo dõi dấu hiệu độc tính (co giật).""",
                },
    {
                    "drug": "Methotrexate",
                    "mechanism": """Penicillin G có thể ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate.""",
                    "effect": "Tăng nồng độ methotrexate, tăng nguy cơ độc tính (giảm bạch cầu, độc thận, viêm niêm mạc)",
                    "management": """TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi chặt chẽ nồng độ methotrexate, công thức máu, chức năng thận. Có thể cần giảm liều methotrexate.""",
                }
                ],
            "moderate": [
    {
                    "drug": "Warfarin",
                    "mechanism": """Penicillin G có thể ức chế tổng hợp vitamin K phụ thuộc vào hệ vi khuẩn đường ruột, làm giảm sản xuất các yếu tố đông máu phụ thuộc vitamin K.""",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin.",
                },
    {
                    "drug": "Aminoglycosides (Gentamicin, Tobramycin, Amikacin)",
                    "mechanism": "Aminoglycosides có thể bị bất hoạt về mặt hóa học bởi penicillin G khi pha chung.",
                    "effect": "Giảm hiệu quả kháng khuẩn của aminoglycosides nếu pha chung",
                    "management": "Không pha chung. Truyền riêng biệt. Tuy nhiên, có thể dùng cùng nhau (synergy) nếu truyền riêng.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": """Penicillin G được coi là an toàn trong thai kỳ. Đã được sử dụng rộng rãi trong nhiều thập kỷ. Lựa chọn đầu tay cho nhiều nhiễm khuẩn trong thai kỳ, đặc biệt giang mai.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Penicillin G bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.""",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu dị ứng hoặc tiêu chảy.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Penicillin G thải chủ yếu qua thận, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan.",
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
            "monitoring": """Chức năng thận (creatinine, CrCl), điện giải (Na, K), dấu hiệu co giật, dấu hiệu dị ứng, huyết áp, nhịp tim""",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - chỉ có dạng IV/IM",
                "timing": "N/A - chỉ có dạng IV/IM",
            },
            "iv": {
                "reconstitution": """Pha với NS (0.9% NaCl) hoặc D5W (5% Dextrose). Thể tích pha: 50-100ml cho liều 1-4 triệu đơn vị. Lắc kỹ để hòa tan hoàn toàn.""",
                "infusion_rate": "Truyền IV trong 30-60 phút. Tốc độ: 50ml/30-60 phút.",
                "compatibility": [
                    "NS (0.9% NaCl)",
                    "D5W (5% Dextrose)",
                    "Ringer's Lactate"
    ],
                "incompatibility": [
                    "Aminoglycosides - có thể bị bất hoạt khi pha chung, truyền riêng biệt",
                    "Amphotericin B - không tương thích",
                    "Các thuốc có tính kiềm hoặc acid mạnh"
    ],
                "notes": """Truyền IV trong 30-60 phút. Theo dõi phản ứng tại chỗ tiêm (viêm tĩnh mạch). Dùng ngay sau khi pha. Không bảo quản lâu sau khi pha.""",
            },
            "im": {
                "reconstitution": "Pha với nước cất vô trùng. Thể tích: 1-2ml cho liều 2.4 triệu đơn vị.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi). Tránh tiêm vào mạch máu.",
                "notes": "Tiêm sâu vào cơ. Không tiêm vào mạch máu. Có thể đau tại chỗ tiêm. Dùng cho điều trị giang mai.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Penicillin G",
                "IDSA Guidelines - Antimicrobial Therapy",
                "UpToDate - Penicillin G: Drug Information",
                "CDC Guidelines - Syphilis Treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều thập kỷ",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {
                "hepatic": "Low",
                "renal": "Low",
                "neurological": "Moderate (co giật ở liều cao/suy thận)",
            },
        },
        "guideline_tags": [
            "IDSA Guidelines - Infective Endocarditis",
            "IDSA Guidelines - Bacterial Meningitis",
            "CDC Guidelines - Syphilis Treatment",
            "WHO Essential Medicines List",
            "IDSA Guidelines - Skin and Soft Tissue Infections"
    ],
        "last_updated": "2025-02-18",
    },
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
    ],',
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
        "contraindications_detail": {
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
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có phản ứng dị ứng nghiêm trọng hoặc C. difficile."},
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
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Moderate",
            "organ_toxicity": {"hepatic": "Low", "renal": "Low", "hematologic": "Moderate (giảm prothrombin)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "IDSA Guidelines - Ventilator-Associated Pneumonia",
            "IDSA Guidelines - Intra-abdominal Infections",
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Complicated Urinary Tract Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },

}

__all__ = ['BETA_LACTAM_ANTIBIOTICS']

