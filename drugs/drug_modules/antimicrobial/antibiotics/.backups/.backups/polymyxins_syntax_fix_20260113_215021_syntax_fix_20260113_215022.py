"""
Polymyxin Antibiotics
Colistin (Polymyxin E)
Kháng sinh cuối cùng cho MDR Gram-âm
"""

POLYMYXIN_ANTIBIOTICS = {
    "Colistin":     {
        "group": "Antibiotic - Polymyxin",
        "vietnamese_name": "Colistin, Colistimethate sodium, Coly-Mycin",
        "administration": [
            "IV",
            "IM",
            "Inhaled",
            "Intrathecal"
    ],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kháng đa thuốc (MDR) Gram-âm",
            "Pseudomonas aeruginosa kháng đa thuốc",
            "Acinetobacter baumannii kháng đa thuốc",
            "Klebsiella pneumoniae kháng carbapenem (CRE)",
            "E. coli kháng carbapenem",
            "Nhiễm khuẩn huyết do MDR Gram-âm",
            "Viêm phổi bệnh viện do MDR Gram-âm",
            "Nhiễm khuẩn đường tiết niệu do MDR Gram-âm",
            "Viêm màng não do MDR Gram-âm (intrathecal)",
            "Nhiễm khuẩn phổi mãn tính ở bệnh nhân xơ nang (CF) - dạng hít"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với colistin hoặc polymyxin",
                "Myasthenia gravis - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, cần điều chỉnh liều",
                "Suy thận cấp - thận trọng",
                "Độc thận đang hoạt động",
                "Độc thần kinh đang hoạt động"
    ],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng colistin hoặc polymyxin",
                "Myasthenia gravis - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, cần điều chỉnh liều",
                "Suy thận cấp - thận trọng"
    ],
        },
        "dosage": {
            "adult_iv_standard": "2.5-5 mg/kg/ngày IV (tính theo colistin base), chia 2-3 lần",
            "adult_iv_severe": "5-6 mg/kg/ngày IV, chia 2-3 lần",
            "adult_iv_meningitis": "5-6 mg/kg/ngày IV, chia 2-3 lần + intrathecal",
            "adult_inhaled_cf": "75-150mg x 2 lần/ngày (dạng hít)",
            "adult_intrathecal": "5-10mg intrathecal x 1 lần/ngày (viêm màng não)",
            "notes": """Liều tính theo colistin base. Colistimethate sodium (CMS) chuyển thành colistin trong cơ thể. Cần điều chỉnh liều theo chức năng thận. Độc thận và độc thần kinh cao.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM nếu có thể",
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp, có thể không hồi phục",
            "Độc thần kinh (neurotoxicity) - tê bì, yếu cơ, rối loạn cảm giác, co giật, suy hô hấp (neuromuscular blockade)",
            "Block thần kinh-cơ (neuromuscular blockade) - suy hô hấp, nguy hiểm tính mạng",
            "Phát ban",
            "Sốt",
            "Ho, khó thở (dạng hít)",
            "Đau tại chỗ tiêm"
    ],
        "interactions": [
            "Aminoglycosides: tăng độc thận và độc thần kinh",
            "Thuốc giãn cơ (neuromuscular blocking agents): tăng nguy cơ suy hô hấp",
            "Vancomycin: có thể tăng độc thận",
            "Furosemide: có thể tăng độc thận",
            "Cisplatin: tăng độc thận"
    ],
        "pregnancy": "C - Sử dụng nếu lợi ích > nguy cơ (độc thận, độc thần kinh)",
        "mechanism_of_action": """Colistin là polymyxin kháng sinh, gắn với lipopolysaccharide (LPS) của màng ngoài vi khuẩn Gram-âm, phá vỡ tính toàn vẹn màng và gây chết tế bào. Tác động như một chất tẩy rửa (detergent), làm rò rỉ nội dung tế bào. Phổ kháng khuẩn: Gram-âm mạnh (Pseudomonas aeruginosa, Acinetobacter baumannii, Klebsiella pneumoniae, E. coli - kể cả các chủng kháng carbapenem CRE), không có hoạt tính với Gram-dương hoặc kỵ khí. Đặc điểm: kháng sinh cuối cùng cho MDR Gram-âm, độc thận và độc thần kinh cao, cần điều chỉnh liều theo chức năng thận. CHỐNG CHỈ ĐỊNH trong myasthenia gravis (nguy cơ neuromuscular blockade).""",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR, BUN) - BẮT BUỘC: hàng ngày, đặc biệt quan trọng vì độc thận cao",
            "Dấu hiệu độc thần kinh: tê bì, yếu cơ, rối loạn cảm giác, co giật, suy hô hấp",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Điện giải (natri, kali, magie) - có thể gây hạ natri, hạ kali",
            "Chức năng hô hấp (nếu có dấu hiệu neuromuscular blockade)",
            "Dấu hiệu suy hô hấp (neuromuscular blockade) - nguy hiểm tính mạng",
            "TDM (nếu có thể) - nồng độ colistin trong huyết thanh"
    ],
        "precautions": [
            "Độc thận và độc thần kinh - RẤT CAO, có thể không hồi phục",
            "CHỐNG CHỈ ĐỊNH trong myasthenia gravis - nguy cơ neuromuscular blockade, suy hô hấp",
            "Điều chỉnh liều theo chức năng thận (eGFR) - QUAN TRỌNG",
            "Theo dõi chức năng thận hàng ngày - bắt buộc",
            "Theo dõi dấu hiệu độc thần kinh (tê bì, yếu cơ, suy hô hấp) - nguy hiểm tính mạng",
            "Tránh dùng với aminoglycosides - tăng độc thận và độc thần kinh",
            "Tránh dùng với thuốc giãn cơ - tăng nguy cơ suy hô hấp",
            "Tránh dùng với thuốc độc thận khác (vancomycin, furosemide, cisplatin)",
            "Thận trọng ở người cao tuổi, suy thận, có tiền sử bệnh thần kinh",
            "Dạng hít: dùng cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính, ít độc tính toàn thân hơn",
            "Intrathecal: chỉ dùng cho viêm màng não do MDR Gram-âm, cần thận trọng",
            "Pha trong NS hoặc D5W, truyền IV trong 30-60 phút"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (bình thường), 10-20 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q8-12h (bình thường), q24-48h (suy thận)",
            "protein_binding": "50%",
            "metabolism": "Chuyển hóa một phần (colistimethate → colistin)",
            "clearance": "Chủ yếu qua thận (70-80% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.2-0.3 L/kg",
        },
        "storage": """Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.""",
        "black_box_warnings": """Độc thận và độc thần kinh - RẤT CAO, có thể không hồi phục. CHỐNG CHỈ ĐỊNH trong myasthenia gravis (nguy cơ neuromuscular blockade, suy hô hấp). Chỉ dùng khi không còn lựa chọn khác (MDR Gram-âm). Cần điều chỉnh liều theo chức năng thận và theo dõi sát.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều độc thận và độc thần kinh, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận và độc thần kinh nặng, có thể không hồi phục",
                    "management": "TRÁNH dùng đồng thời. Nếu bắt buộc, theo dõi chức năng thận và thần kinh sát, giảm liều nếu cần.",
                },
    {
                    "drug": "Thuốc giãn cơ (Neuromuscular Blocking Agents: Succinylcholine, Rocuronium, Vecuronium)",
                    "mechanism": "Colistin tăng tác dụng thuốc giãn cơ, gây neuromuscular blockade",
                    "effect": "Tăng nguy cơ suy hô hấp, nguy hiểm tính mạng",
                    "management": """TRÁNH dùng đồng thời. Nếu bắt buộc (phẫu thuật), theo dõi hô hấp sát, có thể cần giảm liều thuốc giãn cơ.""",
                },
    {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời.",
                },
    {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide có thể tăng độc thận của colistin",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời.",
                }
                ],
            "moderate": [],
            "minor": [],
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Colistin (Coly-Mycin)",
                "IDSA Guidelines - Antimicrobial Therapy, MDR Gram-negative",
                "UpToDate - Colistin: Drug Information",
                "Medscape - Colistin Drug Reference",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Colistin Monograph",
                "Micromedex - Colistin Drug Information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": True,
            "bleeding_risk": "Low",
            "organ_toxicity": {
                "renal": "High",
                "neurological": "High (neurotoxicity, neuromuscular blockade)",
            },
        },
        "guideline_tags": [
            "IDSA Guidelines - Multidrug-Resistant Gram-Negative Infections",
            "IDSA Guidelines - Carbapenem-Resistant Enterobacteriaceae",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "WHO Essential Medicines List"
    ],
        "last_updated": "2025-02-18",
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Sử dụng nếu lợi ích vượt trội nguy cơ. Colistin có thể qua nhau thai. Độc thận và độc thần kinh cao. CHỈ dùng khi không còn lựa chọn khác (MDR Gram-âm đe dọa tính mạng).""",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây độc tính ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú. Cân nhắc ngừng cho bú tạm thời hoặc đổi thuốc khác.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều.",
            "notes": "Colistin không chuyển hóa đáng kể qua gan, thải trừ chủ yếu qua thận.",
        },
        "overdose_management": {
            "symptoms": [
                "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp",
                "Độc thần kinh (neurotoxicity) - tê bì, yếu cơ, co giật",
                "Block thần kinh-cơ (neuromuscular blockade) - suy hô hấp, nguy hiểm tính mạng"
    ],
            "antidote": "Calcium gluconate cho neuromuscular blockade.",
            "treatment": [
                "Ngừng colistin ngay",
                "Đo chức năng thận ngay",
                "Nếu độc thận: truyền dịch tích cực, theo dõi chức năng thận, hemodialysis nếu cần",
                "Nếu neuromuscular blockade: đảm bảo đường thở, hỗ trợ hô hấp, calcium gluconate",
                "Theo dõi dấu hiệu độc thần kinh"
    ],
            "monitoring": "Creatinine, eGFR, BUN, dấu hiệu độc thần kinh, chức năng hô hấp, điện giải.",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                "Calcium gluconate",
                "Calcium chloride"
    ],
            "notes": "Calcium có thể đối kháng neuromuscular blockade.",
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha trong NaCl 0.9% hoặc D5W.",
                "infusion_rate": "Truyền IV trong 30-60 phút.",
                "notes": """Điều chỉnh liều theo chức năng thận. Theo dõi chức năng thận hàng ngày. Tránh dùng với aminoglycosides hoặc thuốc giãn cơ.""",
            },
            "inhaled": {
                "notes": "Dạng hít cho bệnh nhân xơ nang (CF) để điều trị nhiễm Pseudomonas mãn tính.",
            },
        },
    },
    "Polymyxin B": {
        "group": "Antibiotic - Polymyxin",
        "vietnamese_name": "Polymyxin B",
        "administration": ["IV", "IM", "Topical", "Ophthalmic"],
        "indications": [
            "Nhiễm khuẩn do vi khuẩn kháng đa thuốc (MDR) Gram-âm",
            "Pseudomonas aeruginosa kháng đa thuốc",
            "Acinetobacter baumannii kháng đa thuốc",
            "Klebsiella pneumoniae kháng carbapenem (CRE)",
            "E. coli kháng carbapenem",
            "Nhiễm khuẩn huyết do MDR Gram-âm",
            "Viêm phổi bệnh viện do MDR Gram-âm",
            "Nhiễm khuẩn da và mô mềm (dạng bôi)",
            "Nhiễm khuẩn mắt (dạng nhỏ mắt)",
            "Viêm màng não do MDR Gram-âm (intrathecal)"
        ],
        "contraindications": [
            "Dị ứng polymyxin B hoặc colistin",
            "Myasthenia gravis - CHỐNG CHỈ ĐỊNH",
            "Suy thận nặng (CrCl <30) - thận trọng, cần điều chỉnh liều",
            "Suy thận cấp - thận trọng"
        ],
        "dosage": {
            "adult_iv_standard": "1.5-2.5 mg/kg/ngày IV (tính theo polymyxin B base), chia 2 lần",
            "adult_iv_severe": "2.5-3 mg/kg/ngày IV, chia 2 lần",
            "adult_iv_meningitis": "2.5-3 mg/kg/ngày IV, chia 2 lần + intrathecal",
            "adult_im": "2.5-3 mg/kg/ngày IM, chia 2 lần",
            "adult_topical": "Bôi tại chỗ 2-4 lần/ngày",
            "adult_ophthalmic": "1-2 giọt x 4-6 lần/ngày",
            "adult_intrathecal": "5mg intrathecal x 1 lần/ngày (viêm màng não)",
            "notes": "Liều tính theo polymyxin B base. Tương tự colistin nhưng liều khác. Cần điều chỉnh liều theo chức năng thận. Độc thận và độc thần kinh cao."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc tăng khoảng cách",
            "under_30": "Giảm liều 50-75% hoặc tăng khoảng cách đáng kể",
            "hemodialysis": "Liều sau lọc máu, cần TDM nếu có thể"
        },
        "side_effects": [
            "Độc thận (nephrotoxicity) - tăng creatinine, suy thận cấp, có thể không hồi phục",
            "Độc thần kinh (neurotoxicity) - tê bì, yếu cơ, rối loạn cảm giác, co giật, suy hô hấp (neuromuscular blockade)",
            "Block thần kinh-cơ (neuromuscular blockade) - suy hô hấp, nguy hiểm tính mạng",
            "Phát ban",
            "Sốt",
            "Đau tại chỗ tiêm",
            "Kích ứng tại chỗ (dạng bôi, nhỏ mắt)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận và độc thần kinh",
            "Thuốc giãn cơ (neuromuscular blocking agents): tăng nguy cơ suy hô hấp",
            "Vancomycin: có thể tăng độc thận",
            "Furosemide: có thể tăng độc thận",
            "Cisplatin: tăng độc thận"
        ],
        ',
        "pregnancy": "C - Sử dụng nếu lợi ích > nguy cơ (độc thận, độc thần kinh)",
        ',
        "mechanism_of_action": "Polymyxin B là polymyxin kháng sinh, tương tự colistin. Gắn với lipopolysaccharide (LPS) của màng ngoài vi khuẩn Gram-âm, phá vỡ tính toàn vẹn màng và gây chết tế bào. Tác động như một chất tẩy rửa (detergent), làm rò rỉ nội dung tế bào. Phổ kháng khuẩn: Gram-âm mạnh (Pseudomonas aeruginosa, Acinetobacter baumannii, Klebsiella pneumoniae, E. coli - kể cả các chủng kháng carbapenem CRE), không có hoạt tính với Gram-dương hoặc kỵ khí. Đặc điểm: kháng sinh cuối cùng cho MDR Gram-âm, độc thận và độc thần kinh cao, cần điều chỉnh liều theo chức năng thận. CHỐNG CHỈ ĐỊNH trong myasthenia gravis (nguy cơ neuromuscular blockade). Khác với colistin: polymyxin B dùng trực tiếp (không cần chuyển đổi), có thể dùng dạng bôi và nhỏ mắt.",
        "monitoring": [
            "Chức năng thận (creatinine, eGFR, BUN) - BẮT BUỘC: hàng ngày, đặc biệt quan trọng vì độc thận cao",
            "Dấu hiệu độc thần kinh: tê bì, yếu cơ, rối loạn cảm giác, co giật, suy hô hấp",
            "Dấu hiệu nhiễm trùng (sốt, WBC, triệu chứng lâm sàng)",
            "Cấy máu và cấy từ vị trí nhiễm trùng",
            "Điện giải (natri, kali, magie) - có thể gây hạ natri, hạ kali",
            "Chức năng hô hấp (nếu có dấu hiệu neuromuscular blockade)",
            "Dấu hiệu suy hô hấp (neuromuscular blockade) - nguy hiểm tính mạng",
            "TDM (nếu có thể) - nồng độ polymyxin B trong huyết thanh"
        ],
        "precautions": [
            "Độc thận và độc thần kinh - RẤT CAO, có thể không hồi phục",
            "CHỐNG CHỈ ĐỊNH trong myasthenia gravis - nguy cơ neuromuscular blockade, suy hô hấp",
            "Điều chỉnh liều theo chức năng thận (eGFR) - QUAN TRỌNG",
            "Theo dõi chức năng thận hàng ngày - bắt buộc",
            "Theo dõi dấu hiệu độc thần kinh (tê bì, yếu cơ, suy hô hấp) - nguy hiểm tính mạng",
            "Tránh dùng với aminoglycosides - tăng độc thận và độc thần kinh",
            "Tránh dùng với thuốc giãn cơ - tăng nguy cơ suy hô hấp",
            "Tránh dùng với thuốc độc thận khác (vancomycin, furosemide, cisplatin)",
            "Thận trọng ở người cao tuổi, suy thận, có tiền sử bệnh thần kinh",
            "Dạng bôi: chỉ dùng cho nhiễm khuẩn da và mô mềm tại chỗ, ít độc tính toàn thân",
            "Dạng nhỏ mắt: chỉ dùng cho nhiễm khuẩn mắt, ít độc tính toàn thân",
            "Intrathecal: chỉ dùng cho viêm màng não do MDR Gram-âm, cần thận trọng",
            "Pha trong NS hoặc D5W, truyền IV trong 30-60 phút"
        ],
        "pharmacokinetics": {
            "half_life": "4-6 giờ (bình thường), 20-30 giờ (suy thận nặng)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Liều q12h (bình thường), q24-48h (suy thận)",
            "protein_binding": "50%",
            "metabolism": "Không chuyển hóa đáng kể",
            "clearance": "Chủ yếu qua thận (60-70% bài tiết nguyên dạng), cần điều chỉnh thận",
            "volume_of_distribution": "0.1-0.2 L/kg"
        },
        "storage": "Bảo quản bột khô ở nhiệt độ phòng (20-25°C). Sau khi pha: bảo quản ở nhiệt độ phòng 24 giờ, hoặc trong tủ lạnh 7 ngày. Không đông lạnh.",
        "black_box_warnings": "Độc thận và độc thần kinh - RẤT CAO, có thể không hồi phục. CHỐNG CHỈ ĐỊNH trong myasthenia gravis (nguy cơ neuromuscular blockade, suy hô hấp). Chỉ dùng khi không còn lựa chọn khác (MDR Gram-âm). Cần điều chỉnh liều theo chức năng thận và theo dõi sát.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (Gentamicin, Amikacin, Tobramycin)",
                    "mechanism": "Cả hai đều độc thận và độc thần kinh, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận và độc thần kinh nặng, có thể không hồi phục",
                    "management": "TRÁNH dùng đồng thời. Nếu bắt buộc, theo dõi chức năng thận và thần kinh sát, giảm liều nếu cần."
                },
                {
                    "drug": "Thuốc giãn cơ (Neuromuscular Blocking Agents: Succinylcholine, Rocuronium, Vecuronium)",
                    "mechanism": "Polymyxin B tăng tác dụng thuốc giãn cơ, gây neuromuscular blockade",
                    "effect": "Tăng nguy cơ suy hô hấp, nguy hiểm tính mạng",
                    "management": "TRÁNH dùng đồng thời. Nếu bắt buộc (phẫu thuật), theo dõi hô hấp sát, có thể cần giảm liều thuốc giãn cơ."
                },
                {
                    "drug": "Vancomycin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Furosemide",
                    "mechanism": "Furosemide có thể tăng độc thận của polymyxin B",
                    "effect": "Tăng nguy cơ độc thận",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời."
                },
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều độc thận, tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ độc thận nặng",
                    "management": "Theo dõi chức năng thận sát nếu dùng đồng thời."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng polymyxin B hoặc colistin",
                "Myasthenia gravis - CHỐNG CHỈ ĐỊNH (nguy cơ neuromuscular blockade, suy hô hấp)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều",
                "Suy thận cấp - thận trọng",
                "Bệnh nhân cao tuổi - tăng nhạy cảm",
                "Có tiền sử bệnh thần kinh - tăng nguy cơ độc thần kinh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Polymyxin B là thuốc phân loại C. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Polymyxin B có độc thận và độc thần kinh cao. Nhiễm khuẩn MDR nặng có thể gây nguy hiểm cho cả mẹ và thai nhi nếu không điều trị. Chỉ dùng khi không còn lựa chọn khác và lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Không biết polymyxin B có bài tiết vào sữa mẹ hay không. Thời gian bán thải 4-6 giờ, protein binding 50%. Có thể bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Thận trọng khi cho con bú. Nếu cần, ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều (thải trừ chủ yếu qua thận)",
            "notes": "Polymyxin B không chuyển hóa đáng kể, thải trừ chủ yếu qua thận. Không cần điều chỉnh liều ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Độc thận nặng (suy thận cấp)",
                "Độc thần kinh nặng (co giật, suy hô hấp do neuromuscular blockade)",
                "Block thần kinh-cơ (suy hô hấp, nguy hiểm tính mạng)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ. Neostigmine có thể giúp đảo ngược neuromuscular blockade.",
            "treatment": [
                "Ngừng polymyxin B ngay lập tức",
                "Hỗ trợ hô hấp: Đặt nội khí quản, thở máy nếu có neuromuscular blockade",
                "Nếu neuromuscular blockade:",
                "  - Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV (đảo ngược block)",
                "  - Hoặc Sugammadex (nếu dùng với rocuronium/vecuronium)",
                "Nếu độc thận:",
                "  - Bù dịch (NS, LR)",
                "  - Tránh thuốc độc thận khác",
                "  - Lọc máu (hemodialysis) nếu suy thận nặng",
                "Nếu co giật:",
                "  - Benzodiazepine (diazepam, lorazepam) IV",
                "  - Phenytoin hoặc fosphenytoin IV nếu cần",
                "Lọc máu (hemodialysis) - polymyxin B có thể được loại bỏ một phần",
                "Theo dõi: Chức năng thận, thần kinh, hô hấp liên tục"
            ],
            "monitoring": "Theo dõi chức năng thận, thần kinh, hô hấp liên tục cho đến khi hồi phục. Theo dõi lâu hơn nếu có biến chứng."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "agent": "Neostigmine + Glycopyrrolate",
                    "mechanism": "Neostigmine ức chế cholinesterase, tăng acetylcholine, đảo ngược neuromuscular blockade. Glycopyrrolate chống nhịp chậm.",
                    "indication": "Neuromuscular blockade do polymyxin B",
                    "dose": "Neostigmine 0.04-0.07 mg/kg IV + Glycopyrrolate 0.01 mg/kg IV",
                    "caution": "Chỉ hiệu quả khi block nhẹ đến vừa. Nếu block sâu, cần hỗ trợ thông khí cho đến khi hồi phục."
                }
            ],
            "notes": "Neostigmine có thể giúp đảo ngược neuromuscular blockade. Nếu block sâu, cần hỗ trợ thông khí cho đến khi hồi phục."
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha bột: 500,000 units (50mg) trong 5ml NS = 100,000 units/ml (10mg/ml), sau đó pha loãng trong 100-250ml NS hoặc D5W.",
                "infusion_rate": "Standard: 1.5-2.5 mg/kg/ngày IV chia 2 lần, truyền trong 30-60 phút. Severe: 2.5-3 mg/kg/ngày IV chia 2 lần.",
                "compatibility": ["NS (0.9% NaCl)", "D5W (5% Dextrose)"],
                "incompatibility": [
                    "Không trộn với các thuốc khác. Tiêm bolus riêng biệt hoặc dùng đường truyền riêng cho infusion."
                ],
                "notes": "QUAN TRỌNG: 1) Độc thận và độc thần kinh RẤT CAO, 2) CHỐNG CHỈ ĐỊNH trong myasthenia gravis, 3) Điều chỉnh liều theo chức năng thận, 4) Theo dõi chức năng thận hàng ngày, 5) Theo dõi dấu hiệu độc thần kinh (tê bì, yếu cơ, suy hô hấp), 6) Tránh dùng với aminoglycosides và thuốc giãn cơ."
            },
            "im": {
                "reconstitution": "Pha bột: 500,000 units (50mg) trong 2ml NS = 250,000 units/ml (25mg/ml).",
                "injection_site": "Cơ lớn (đùi, cánh tay).",
                "notes": "IM: 2.5-3 mg/kg/ngày chia 2 lần. Tiêm sâu vào cơ, không tiêm vào mỡ dưới da. Có thể gây đau tại chỗ tiêm."
            },
            "topical": {
                "reconstitution": "Dùng dạng bôi sẵn có hoặc pha bột với nước.",
                "dose": "Bôi tại chỗ 2-4 lần/ngày.",
                "notes": "Chỉ dùng cho nhiễm khuẩn da và mô mềm tại chỗ. Ít độc tính toàn thân hơn so với IV/IM."
            },
            "ophthalmic": {
                "reconstitution": "Dùng dạng nhỏ mắt sẵn có.",
                "dose": "1-2 giọt x 4-6 lần/ngày.",
                "notes": "Chỉ dùng cho nhiễm khuẩn mắt. Ít độc tính toàn thân hơn so với IV/IM."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Polymyxin B",
                "IDSA Guidelines - Antimicrobial Therapy, MDR Gram-negative",
                "UpToDate - Polymyxin B: Drug Information",
                "Medscape - Polymyxin B Drug Reference"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, IDSA guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": True,
            "icu_critical_care_only": True,
            "bleeding_risk": "Low",
            "organ_toxicity": {"renal": "High", "neurological": "High (neurotoxicity, neuromuscular blockade)"}
        },
        "guideline_tags": [
            "IDSA Guidelines - Multidrug-Resistant Gram-Negative Infections",
            "IDSA Guidelines - Carbapenem-Resistant Enterobacteriaceae",
            "IDSA Guidelines - Hospital-Acquired Pneumonia",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18",
    },
}

__all__ = ['POLYMYXIN_ANTIBIOTICS']

























