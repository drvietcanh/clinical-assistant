"""
Lincosamide Antibiotics
"""
LINCOSAMIDE_ANTIBIOTICS = {
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
        "contraindications_detail": {
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
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có C. difficile hoặc phản ứng dị ứng nghiêm trọng. Điều trị C. difficile nếu có."},
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
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "Low",
            "organ_toxicity": {"gastrointestinal": "High (C. difficile colitis)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Skin and Soft Tissue Infections",
            "IDSA Guidelines - Anaerobic Infections",
            "IDSA Guidelines - Clostridium difficile Infection",
            "IDSA Guidelines - Odontogenic Infections",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
}

__all__ = ['LINCOSAMIDE_ANTIBIOTICS']
