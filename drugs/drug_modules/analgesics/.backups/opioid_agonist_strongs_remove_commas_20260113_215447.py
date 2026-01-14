"""Analgesic and Pain Medications
Active module - contains all analgesic drug data"""

# Opioid Agonist (Strong)s

OPIOID_AGONIST_STRONGS_DRUGS = {
    "Fentanyl": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Fentanyl, Duragesic",
        "administration": ["IV", "IM", "Transdermal", "Intranasal", "Buccal"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau mạn tính nặng (transdermal patch)",
            "Gây mê (IV)",
            "Đau cấp tính nặng (IV, intranasal, buccal)"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ",
            "Không dùng transdermal ở bệnh nhân chưa dùng opioid (chưa dung nạp)"
        ],
        "dosage": {
            "adult_iv_bolus": "25-100mcg IV mỗi 30-60 phút khi cần",
            "adult_iv_continuous": "25-100mcg/giờ truyền liên tục",
            "adult_transdermal": "25-100mcg/giờ patch, thay mỗi 72 giờ",
            "adult_intranasal": "100-200mcg xịt mũi khi cần",
            "adult_buccal": "100-400mcg ngậm trong miệng khi cần",
            "elderly": "Giảm liều 25-50%",
            "notes": "Mạnh gấp 50-100 lần morphine. Tác dụng nhanh nhưng ngắn (IV). Transdermal: tác dụng chậm, kéo dài."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp nặng (nguy hiểm, đặc biệt với transdermal patch)",
            "Buồn nôn, nôn",
            "Táo bón",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Rigid chest (co cứng ngực - với IV liều cao)",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp nặng",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp",
            "CYP3A4 inhibitors: tăng nồng độ fentanyl"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Fentanyl là opioid mu-receptor agonist mạnh, mạnh gấp 50-100 lần morphine. Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Fentanyl có tác dụng nhanh (IV: 1-2 phút), ngắn (30-60 phút IV), nhưng có thể tích lũy ở mô mỡ. Transdermal patch: hấp thu chậm qua da, tác dụng kéo dài 72 giờ, nhưng có thể tích lũy và gây ức chế hô hấp kéo dài sau khi tháo patch.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - QUAN TRỌNG NHẤT, đặc biệt với transdermal patch",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Co đồng tử (miosis)",
            "Dấu hiệu rigid chest (co cứng ngực) với IV liều cao",
            "Với transdermal patch: theo dõi ít nhất 24 giờ sau khi tháo patch (có thể tích lũy)",
            "Chức năng thận (tích lũy ở suy thận)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt với transdermal patch (tích lũy, tác dụng kéo dài)",
            "KHÔNG dùng transdermal patch cho bệnh nhân chưa dùng opioid (chưa dung nạp) - nguy cơ ức chế hô hấp nặng",
            "Với transdermal patch: theo dõi ít nhất 24 giờ sau khi tháo patch (có thể tích lũy trong mô mỡ)",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần (tăng nguy cơ ức chế hô hấp nặng)",
            "Dự phòng táo bón từ đầu",
            "Thận trọng ở suy thận (tích lũy)",
            "Thận trọng ở suy gan (giảm chuyển hóa)",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài",
            "Với IV liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant"
        ],
        "pharmacokinetics": {
            "half_life": "IV: 2-4 giờ; Transdermal: 17 giờ (sau khi tháo patch)",
            "onset": "IV: 1-2 phút; IM: 7-15 phút; Transdermal: 12-24 giờ; Intranasal: 5-10 phút; Buccal: 15-30 phút",
            "duration": "IV: 30-60 phút; Transdermal: 72 giờ (patch); Intranasal: 1-2 giờ; Buccal: 2-4 giờ",
            "protein_binding": "80-85%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành norfentanyl (inactive)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ). Tích lũy ở mô mỡ (đặc biệt với transdermal patch)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Transdermal patch: bảo quản trong bao bì kín, tránh nhiệt độ cao. Để xa tầm tay trẻ em (nguy cơ quá liều nghiêm trọng).",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt với transdermal patch (tích lũy, tác dụng kéo dài sau khi tháo patch). KHÔNG dùng transdermal patch cho bệnh nhân chưa dùng opioid. Fentanyl có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều fentanyl, theo dõi hô hấp liên tục, có naloxone sẵn sàng"
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng fentanyl"
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin, erythromycin)",
                    "mechanism": "Ức chế chuyển hóa fentanyl qua CYP3A4, tăng nồng độ fentanyl",
                    "effect": "Tăng nồng độ fentanyl, tăng nguy cơ ức chế hô hấp nặng",
                    "management": "Giảm liều fentanyl 50-75%. Theo dõi hô hấp chặt chẽ. Đặc biệt nguy hiểm với transdermal patch."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Cảm ứng enzyme chuyển hóa fentanyl, giảm nồng độ",
                    "effect": "Giảm hiệu quả fentanyl",
                    "management": "Có thể cần tăng liều fentanyl"
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fentanyl hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng hoặc suy hô hấp cấp tính",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ (do tăng CO2)",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Transdermal patch: bệnh nhân chưa dùng opioid (chưa dung nạp)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều 50-75%, tăng khoảng cách liều",
                "Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)",
                "Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)",
                "Trẻ em <12 tuổi - nguy cơ ức chế hô hấp",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện",
                "Suy tim - tăng nguy cơ ức chế hô hấp",
                "Bệnh phổi tắc nghẽn mạn tính (COPD) - tăng nguy cơ ức chế hô hấp",
                "Dùng với CYP3A4 inhibitors - tăng nguy cơ ức chế hô hấp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ cho điều trị đau nặng. Tam cá nguyệt 3: Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Fentanyl bài tiết vào sữa mẹ ở nồng độ thấp. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ, đặc biệt ở trẻ sơ sinh. Với transdermal patch: nồng độ trong sữa mẹ thấp hơn so với IV.",
                "recommendation": "Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ, bú kém). Tránh dùng liều cao hoặc kéo dài. Dùng liều thấp nhất hiệu quả."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 25-50%",
            "severe": "Giảm liều 50% hoặc tránh dùng",
            "notes": "Fentanyl chuyển hóa ở gan qua CYP3A4 thành norfentanyl (inactive). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Rigid chest (co cứng ngực) với IV liều cao",
                "Với transdermal patch: có thể xảy ra sau khi tháo patch (tích lũy)"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với fentanyl",
                "Với transdermal patch: THÁO NGAY patch, rửa da bằng nước và xà phòng",
                "Theo dõi hô hấp liên tục ít nhất 24 giờ (đặc biệt với transdermal patch do tích lũy)",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Nếu rigid chest: có thể cần muscle relaxant (succinylcholine)"
            ],
            "monitoring": "Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Với transdermal patch: theo dõi ít nhất 24-48 giờ sau khi tháo patch do tích lũy."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng",
                    "notes": "Naloxone có half-life ngắn (1 giờ) so với fentanyl (2-4 giờ IV, 17 giờ transdermal). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp, đặc biệt với transdermal patch."
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha với 50-100ml NS hoặc D5W cho truyền liên tục. Hoặc tiêm trực tiếp IV",
                "infusion_rate": "Tiêm IV chậm trong 2-5 phút. Truyền liên tục: 25-100mcg/giờ (tùy liều)",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": ["Alkaline solutions"],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần. Với liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant."
            },
            "im": {
                "notes": "Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm. Tác dụng bắt đầu 7-15 phút."
            },
            "transdermal": {
                "technique": "Dán patch lên da sạch, khô, không có lông (ngực, lưng, cánh tay trên). Thay patch mỗi 72 giờ. Không cắt patch.",
                "timing": "Thay patch mỗi 72 giờ. Tác dụng bắt đầu sau 12-24 giờ. Theo dõi ít nhất 24 giờ sau khi tháo patch.",
                "after_use": "THÁO NGAY nếu có dấu hiệu quá liều. Rửa da bằng nước và xà phòng sau khi tháo patch.",
                "notes": "KHÔNG dùng cho bệnh nhân chưa dùng opioid. Tác dụng kéo dài sau khi tháo patch (tích lũy trong mô mỡ)."
            },
            "intranasal": {
                "technique": "Xịt vào một bên mũi, nhắm mắt và miệng khi xịt.",
                "timing": "Khi cần, có thể lặp lại sau 2 giờ nếu cần.",
                "notes": "Tác dụng nhanh (5-10 phút). Có thể gây vị đắng trong miệng."
            },
            "buccal": {
                "technique": "Đặt viên/băng dán trong miệng, giữa má và nướu. Để tan tự nhiên, không nhai hoặc nuốt.",
                "timing": "Khi cần, có thể lặp lại sau 4 giờ nếu cần.",
                "notes": "Tác dụng bắt đầu 15-30 phút, kéo dài 2-4 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fentanyl (Duragesic, Actiq, etc.)",
                "UpToDate - Fentanyl: Drug information",
                "Lexicomp - Fentanyl monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used in anesthesia and pain management"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Respiratory depression (life-threatening)", "Accumulation with transdermal patch (up to 24h after removal)", "Rigid chest syndrome (with high IV doses)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory rate and SpO2 - CRITICAL (especially with transdermal)", "Level of consciousness", "Blood pressure", "Signs of rigid chest (with IV high doses)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Opioid Addiction and Respiratory Depression",
            "FDA Drug Safety Communication - Fentanyl Transdermal Patch",
            "ISMP High Alert Medications - Opioids",
            "WHO Guidelines - Cancer Pain Management",
            "CDC Guidelines - Opioid Prescribing"
        ]
    },
    "Hydromorphone": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Hydromorphone, Dilaudid",
        "administration": ["PO", "IV", "IM", "SC"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau cấp tính nặng",
            "Đau mạn tính nặng"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ"
        ],
        "dosage": {
            "adult_po": "2-4mg mỗi 4-6 giờ khi cần",
            "adult_iv": "0.5-2mg mỗi 3-4 giờ hoặc 0.2-1mg/giờ truyền liên tục",
            "adult_im_sc": "1-2mg mỗi 4-6 giờ",
            "opioid_naive": "1-2mg PO hoặc 0.5mg IV",
            "opioid_tolerant": "Liều cao hơn, dựa trên liều opioid trước đó",
            "notes": "Mạnh hơn morphine (tỷ lệ 5:1). Theo dõi hô hấp chặt chẽ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm)",
            "Buồn nôn, nôn",
            "Táo bón (rất thường gặp)",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Opioid mu-receptor agonist mạnh. Hydromorphone là dẫn xuất của morphine, mạnh hơn morphine khoảng 5 lần (tỷ lệ 5:1). Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Hydromorphone có thời gian tác dụng ngắn hơn morphine một chút.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim",
            "Co đồng tử (miosis)",
            "Dấu hiệu táo bón (rất thường gặp, cần dự phòng)",
            "Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần",
            "Dự phòng táo bón từ đầu",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài",
            "Hydromorphone mạnh hơn morphine 5 lần - cần điều chỉnh liều cẩn thận"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ",
            "onset": "IV: 5-10 phút; IM: 15-30 phút; PO: 30-60 phút",
            "duration": "3-4 giờ",
            "protein_binding": "8-19%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều hydromorphone, theo dõi hô hấp liên tục."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng hydromorphone hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều 50-75%",
                "Suy gan nặng - giảm liều 25-50%",
                "Người cao tuổi - giảm liều 25-50%",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Hydromorphone bài tiết vào sữa mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Theo dõi trẻ sát."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Tránh dùng hoặc dùng liều rất thấp",
            "notes": "Hydromorphone chuyển hóa ở gan. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm"
            ],
            "antidote": "Naloxone (opioid antagonist)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp NGAY LẬP TỨC",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần",
                "Theo dõi liên tục hô hấp, ý thức, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần"
            ],
            "monitoring": "Theo dõi liên tục hô hấp, ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Naloxone"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm buồn nôn nhẹ.",
                "timing": "Mỗi 4-6 giờ khi cần."
            },
            "iv": {
                "infusion_rate": "Truyền chậm: 2-5 phút",
                "compatibility": ["0.9% NaCl", "D5W"],
                "notes": "Theo dõi hô hấp chặt chẽ trong khi truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Hydromorphone (Dilaudid)",
                "UpToDate - Hydromorphone: Drug information",
                "Lexicomp - Hydromorphone monograph"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved, extensive clinical data"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Respiratory depression (life-threatening)", "5x more potent than morphine - dose adjustment critical"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory rate and SpO2 - CRITICAL", "Level of consciousness", "Blood pressure"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Opioid Addiction and Respiratory Depression",
            "ISMP High Alert Medications - Opioids",
            "DEA Schedule II Controlled Substance",
            "WHO Guidelines - Cancer Pain Management",
            "CDC Guidelines - Opioid Prescribing"
        ]
    },

    "Meperidine":     {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Meperidine, Pethidine, Demerol",
        "administration": [
            "PO",
            "IV",
            "IM",
            "SC"
    ],
        "indications": [
            "Đau nặng",
            "Đau sau phẫu thuật",
            "Đau cấp tính"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng meperidine hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Dùng MAO inhibitor trong vòng 14 ngày - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng - CHỐNG CHỈ ĐỊNH (tích lũy normeperidine)",
                "Dùng lâu dài (>48 giờ) - CHỐNG CHỈ ĐỊNH (tích lũy normeperidine)"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng, tránh dùng",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - giảm liều"
    ],
        },
        "dosage": {
            "adult_po": "50-150mg mỗi 3-4 giờ (tối đa 600mg/ngày)",
            "adult_iv_im": "25-100mg IV/IM mỗi 3-4 giờ",
            "notes": """Ít dùng hiện nay do tích lũy normeperidine (active metabolite độc, gây co giật). Chỉ dùng ngắn hạn (<48 giờ).""",
        },
        "side_effects": [
            "Ức chế hô hấp",
            "Co giật (do tích lũy normeperidine, đặc biệt ở suy thận)",
            "Buồn nôn, nôn",
            "Táo bón",
            "Buồn ngủ, lú lẫn",
            "Nguy cơ nghiện/lệ thuộc",
            "Tích lũy normeperidine ở suy thận → nguy cơ co giật cao"
    ],
        "interactions": [
            "MAO inhibitor: CHỐNG CHỈ ĐỊNH (nguy cơ phản ứng nghiêm trọng)",
            "Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "Rifampin: giảm nồng độ meperidine"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Opioid mu-receptor agonist, tác dụng tương tự morphine nhưng ngắn hơn. Meperidine được chuyển hóa thành normeperidine (active metabolite) → tích lũy ở suy thận → gây co giật. ĐẶC ĐIỂM: (1) Ít dùng hiện nay do nguy cơ co giật (tích lũy normeperidine), (2) CHỈ dùng ngắn hạn (<48 giờ), (3) CHỐNG CHỈ ĐỊNH ở suy thận (tích lũy normeperidine), (4) CHỐNG CHỈ ĐỊNH với MAO inhibitor (phản ứng nghiêm trọng).""",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2)",
            "Mức độ đau",
            "Mức độ ý thức",
            "Dấu hiệu co giật (đặc biệt ở suy thận, dùng >48 giờ)",
            "Chức năng thận (creatinine, BUN) - QUAN TRỌNG (tích lũy normeperidine)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (<48 giờ) - CHỐNG CHỈ ĐỊNH dùng lâu dài",
            "CHỐNG CHỈ ĐỊNH ở suy thận (tích lũy normeperidine → co giật)",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor (phản ứng nghiêm trọng)",
            "Nguy cơ co giật do tích lũy normeperidine - đặc biệt ở suy thận, dùng >48 giờ",
            "Ít dùng hiện nay - ưu tiên dùng morphine hoặc opioid khác",
            "Khởi đầu với liều thấp",
            "Tránh dùng với benzodiazepine, rượu"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ (meperidine), 15-20 giờ (normeperidine - tích lũy)",
            "onset": "10-15 phút (IV), 30-45 phút (PO)",
            "duration": "2-4 giờ",
            "protein_binding": "60-80%",
            "clearance": "Gan (chuyển hóa thành normeperidine), thận (thải trừ normeperidine - tích lũy ở suy thận)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Bảo quản an toàn, tránh xa tầm tay trẻ em.",
        "black_box_warnings": """CHỐNG CHỈ ĐỊNH dùng lâu dài (>48 giờ) - tích lũy normeperidine gây co giật. CHỐNG CHỈ ĐỊNH ở suy thận - tích lũy normeperidine. CHỐNG CHỈ ĐỊNH với MAO inhibitor - phản ứng nghiêm trọng. Nguy cơ nghiện, lạm dụng, và lệ thuộc.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng nghiêm trọng",
                    "effect": "Có thể gây tăng thân nhiệt, tăng huyết áp, co giật, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Ngừng MAOI ít nhất 14 ngày trước khi dùng meperidine.",
                },
    {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI.",
                }
                ],
            "moderate": [
    {
                    "drug": "Rifampin",
                    "mechanism": "Cảm ứng enzyme chuyển hóa meperidine",
                    "effect": "Giảm nồng độ meperidine, giảm hiệu quả",
                    "management": "Có thể cần tăng liều meperidine.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng meperidine hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Dùng MAO inhibitor trong vòng 14 ngày - CHỐNG CHỈ ĐỊNH",
                "Suy thận nặng - CHỐNG CHỈ ĐỊNH (tích lũy normeperidine)",
                "Dùng lâu dài (>48 giờ) - CHỐNG CHỈ ĐỊNH (tích lũy normeperidine)"
    ],
            "tương_đối": [
                "Suy thận trung bình - thận trọng, tránh dùng",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - giảm liều"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "CHỐNG CHỈ ĐỊNH - tránh dùng (tích lũy normeperidine)",
            "under_30": "CHỐNG CHỈ ĐỊNH - tránh dùng (tích lũy normeperidine → co giật)",
            "dialysis": "CHỐNG CHỈ ĐỊNH - tránh dùng",
            "notes": """CHỐNG CHỈ ĐỊNH ở suy thận. Meperidine chuyển hóa thành normeperidine (active metabolite) tích lũy ở suy thận và gây co giật. Dùng thuốc opioid khác (morphine, fentanyl) thay thế.""",
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ, nhưng chỉ dùng ngắn hạn (<48 giờ).",
            "lactation": {
                "safety": "Caution",
                "details": "Meperidine và normeperidine bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú. Tránh dùng lâu dài.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, giảm liều (chuyển hóa qua gan)",
            "notes": "Meperidine chuyển hóa ở gan thành normeperidine. Suy gan có thể ảnh hưởng đến chuyển hóa.",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng",
                "Buồn ngủ sâu, hôn mê",
                "Co giật (do tích lũy normeperidine)",
                "Đồng tử co nhỏ (miosis)",
                "Hạ huyết áp"
    ],
            "antidote": "Naloxone (Narcan) - opioid antagonist, nhưng không đảo ngược co giật do normeperidine",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút",
                "Nếu co giật: benzodiazepine (diazepam, lorazepam)",
                "Theo dõi liên tục: ý thức, hô hấp, tim mạch",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp nặng",
                "Lưu ý: Naloxone đảo ngược tác dụng opioid nhưng không đảo ngược co giật do normeperidine"
    ],
            "monitoring": """Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch, dấu hiệu co giật. Theo dõi ít nhất 4-6 giờ sau liều naloxone cuối.""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone (Narcan)",
                    "mechanism": "Opioid antagonist, đảo ngược tác dụng opioid",
                    "indication": "Quá liều meperidine gây ức chế hô hấp",
                    "dose": "0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút",
                    "caution": """Naloxone đảo ngược tác dụng opioid nhưng không đảo ngược co giật do normeperidine. Cần điều trị co giật riêng nếu có.""",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": "Mỗi 3-4 giờ. CHỈ dùng ngắn hạn (<48 giờ). Liều tối đa: 600mg/ngày.",
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W",
                "infusion_rate": "Tiêm IV chậm (2-3 phút)",
                "compatibility": [
                    "NS",
                    "D5W"
    ],
                "incompatibility": [],
                "notes": "CHỈ dùng ngắn hạn (<48 giờ). Theo dõi hô hấp chặt chẽ.",
            },
            "im": {
                "notes": "Tiêm bắp sâu. CHỈ dùng ngắn hạn (<48 giờ).",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Meperidine (Demerol)",
                "UpToDate - Meperidine: Drug information"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, nhưng ít dùng hiện nay",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Respiratory rate", "Sedation", "Constipation"],
            },
            "guideline_tags": [
                "CDC 2022 Opioid Prescribing Guidelines",
                "FDA Black Box Warning - Opioid addiction, abuse, misuse",
            ]
    },
    "Methadone":     {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Methadone, Dolophine",
        "administration": [
            "PO",
            "IV",
            "IM"
    ],
        "indications": [
            "Đau nặng",
            "Cai nghiện opioid (maintenance therapy)",
            "Đau mạn tính",
            "Đau ung thư"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng methadone hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ"
    ],
            "tương_đối": [
                "Suy thận nặng - thận trọng, giảm liều",
                "Suy gan nặng - thận trọng, giảm liều (chuyển hóa qua gan)",
                "QT kéo dài - tránh dùng hoặc theo dõi ECG sát",
                "Dùng với thuốc kéo dài QT - tránh dùng chung",
                "Người cao tuổi - giảm liều (tăng nhạy cảm, tăng nguy cơ tích lũy)"
    ],
        },
        "dosage": {
            "adult_pain_po": "2.5-10mg mỗi 6-8 giờ (khởi đầu), điều chỉnh theo đáp ứng",
            "adult_pain_iv_im": "2.5-10mg IV/IM mỗi 6-8 giờ",
            "adult_maintenance": "20-120mg/ngày PO (cai nghiện opioid)",
            "notes": """Half-life dài (15-60 giờ) → tích lũy, nguy cơ quá liều. Khởi đầu thấp, tăng dần chậm. QT kéo dài có thể xảy ra.""",
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm, có thể kéo dài do half-life dài)",
            "Kéo dài QT interval (nguy cơ torsades de pointes)",
            "Buồn nôn, nôn",
            "Táo bón",
            "Buồn ngủ, lú lẫn",
            "Tích lũy (do half-life dài) → nguy cơ quá liều",
            "Nguy cơ nghiện/lệ thuộc"
    ],
        "interactions": [
            "Benzodiazepine: tăng nguy cơ ức chế hô hấp nặng",
            "MAO inhibitor: chống chỉ định",
            "Thuốc kéo dài QT: tăng nguy cơ torsades de pointes",
            "CYP3A4 inhibitors: tăng nồng độ methadone",
            "Rifampin: giảm nồng độ methadone"
    ],
        ',
        "pregnancy": "C",
        ',
        "mechanism_of_action": """Opioid mu-receptor agonist mạnh, tương tự morphine. Methadone có đặc điểm: (1) Half-life dài (15-60 giờ) → tích lũy, nguy cơ quá liều, nhưng hiệu quả kéo dài, (2) Có thể kéo dài QT interval → nguy cơ torsades de pointes, (3) Chuyển hóa qua CYP3A4, CYP2B6, CYP2D6, (4) Dùng cho cai nghiện opioid (maintenance therapy) do tác dụng kéo dài và giảm craving. Được dùng cho đau nặng và cai nghiện opioid.""",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - QUAN TRỌNG (nguy cơ tích lũy)",
            "ECG - theo dõi QT interval (nguy cơ kéo dài QT, torsades de pointes)",
            "Mức độ đau",
            "Mức độ ý thức",
            "Dấu hiệu tích lũy/quá liều (tăng buồn ngủ, giảm nhịp thở)",
            "Chức năng thận, gan (chuyển hóa qua gan)"
    ],
        "precautions": [
            "Half-life dài (15-60 giờ) → TÍCH LŨY, nguy cơ quá liều cao, đặc biệt trong vài ngày đầu",
            "Khởi đầu với liều thấp (2.5-10mg), tăng dần CHẬM (mỗi 5-7 ngày)",
            "NGUY CƠ QUÁ LIỀY cao trong 1-2 tuần đầu do tích lũy",
            "Kéo dài QT interval → theo dõi ECG, nguy cơ torsades de pointes",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitor",
            "Tránh dùng với benzodiazepine, rượu (tăng nguy cơ ức chế hô hấp nặng)",
            "Tránh dùng với thuốc kéo dài QT khác",
            "Cần có naloxone sẵn sàng (nhưng half-life methadone dài → có thể cần nhiều liều naloxone)",
            "Dùng cho cai nghiện: phải được quản lý bởi chương trình điều trị chuyên khoa"
    ],
        "pharmacokinetics": {
            "half_life": "15-60 giờ (rất dài, tích lũy)",
            "onset": "30-60 phút (PO), 10-20 phút (IV/IM)",
            "duration": "4-8 giờ (đau), nhưng tích lũy do half-life dài",
            "protein_binding": "85-90%",
            "clearance": "Gan (chuyển hóa qua CYP3A4, CYP2B6, CYP2D6), thận (thải trừ)",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm. Bảo quản an toàn, tránh xa tầm tay trẻ em (nguy cơ quá liều gây tử vong).""",
        "black_box_warnings": """Nguy cơ nghiện, lạm dụng, và lệ thuộc. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine hoặc rượu. Half-life dài (15-60 giờ) → tích lũy, nguy cơ quá liều cao trong vài ngày đầu. Nguy cơ kéo dài QT interval và torsades de pointes.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều methadone, theo dõi hô hấp liên tục.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng methadone.",
                },
    {
                    "drug": "Thuốc kéo dài QT (Amiodarone, Sotalol, Haloperidol, Chlorpromazine, Macrolides)",
                    "mechanism": "Tác dụng hiệp đồng kéo dài QT interval",
                    "effect": "Tăng nguy cơ torsades de pointes",
                    "management": "Tránh dùng chung. Nếu bắt buộc: theo dõi ECG sát, đảm bảo K+ và Mg2+ bình thường.",
                }
                ],
            "moderate": [
    {
                    "drug": "CYP3A4 inhibitors (Ketoconazole, Clarithromycin, Erythromycin, Ritonavir)",
                    "mechanism": "Ức chế chuyển hóa methadone",
                    "effect": "Tăng nồng độ methadone, tăng tác dụng phụ",
                    "management": "Giảm liều methadone. Theo dõi tác dụng phụ.",
                },
    {
                    "drug": "Rifampin, Carbamazepine, Phenytoin",
                    "mechanism": "Cảm ứng enzyme chuyển hóa methadone",
                    "effect": "Giảm nồng độ methadone, giảm hiệu quả",
                    "management": "Có thể cần tăng liều methadone. Theo dõi đáp ứng.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng methadone hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Dùng MAO inhibitor trong vòng 14 ngày",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ"
    ],
            "tương_đối": [
                "Suy thận nặng - thận trọng, giảm liều",
                "Suy gan nặng - thận trọng, giảm liều (chuyển hóa qua gan)",
                "QT kéo dài - tránh dùng hoặc theo dõi ECG sát",
                "Dùng với thuốc kéo dài QT - tránh dùng chung",
                "Người cao tuổi - giảm liều (tăng nhạy cảm, tăng nguy cơ tích lũy)"
    ],
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, giảm liều (thải trừ qua thận)",
            "dialysis": "Thận trọng, giảm liều. Methadone không được lọc sạch hiệu quả qua thẩm phân máu.",
            "notes": """Methadone thải trừ qua thận. Suy thận có thể tăng nguy cơ tích lũy, đặc biệt khi kết hợp với half-life dài. Giảm liều và theo dõi chặt chẽ ở suy thận.""",
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Category C. Có thể dùng nếu lợi ích > nguy cơ. Khi dùng cho cai nghiện opioid trong thai kỳ: có thể giảm nguy cơ hội chứng cai ở trẻ sơ sinh so với tiếp tục dùng heroin/opioid khác. Tuy nhiên, vẫn có nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng gần cuối thai kỳ.""",
            "lactation": {
                "safety": "Caution",
                "details": """Methadone bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ tương đương khoảng 1-3% liều mẹ. Có thể gây tác dụng phụ ở trẻ (buồn ngủ, bú kém, ức chế hô hấp).""",
                "recommendation": """Có thể cho con bú nhưng cần theo dõi trẻ về dấu hiệu tác dụng phụ (buồn ngủ, bú kém, ức chế hô hấp). Đặc biệt thận trọng ở trẻ sơ sinh.""",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều (chuyển hóa qua gan)",
            "notes": """Methadone chuyển hóa ở gan qua CYP3A4, CYP2B6, CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy và tác dụng phụ.""",
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (triệu chứng chính, có thể kéo dài do half-life dài)",
                "Buồn ngủ sâu, hôn mê",
                "Đồng tử co nhỏ (miosis)",
                "Hạ huyết áp, nhịp tim chậm",
                "Kéo dài QT interval, torsades de pointes (hiếm)"
    ],
            "antidote": "Naloxone (Narcan) - opioid antagonist, nhưng có thể cần nhiều liều do half-life methadone dài",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp ngay lập tức (quan trọng nhất)",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần",
                "Do half-life methadone dài → có thể cần truyền naloxone liên tục hoặc lặp lại nhiều lần",
                "Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch, ECG (QT interval)",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp nặng",
                "Điều trị hạ huyết áp: truyền dịch, vasopressors nếu cần",
                "Theo dõi ít nhất 24-48 giờ do half-life methadone dài (15-60 giờ)"
    ],
            "monitoring": """Theo dõi liên tục: ý thức, hô hấp (nhịp thở, SpO2), tim mạch, ECG (QT interval). Theo dõi ít nhất 24-48 giờ do half-life dài.""",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Naloxone (Narcan)",
                    "mechanism": "Opioid antagonist, đảo ngược tác dụng opioid",
                    "indication": "Quá liều methadone gây ức chế hô hấp",
                    "dose": """0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút. Có thể cần truyền liên tục do half-life methadone dài.""",
                    "caution": """Half-life naloxone ngắn (30-90 phút) nhưng half-life methadone dài (15-60 giờ) → có thể cần nhiều liều hoặc truyền liên tục.""",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với thức ăn hoặc không",
                "timing": """Mỗi 6-8 giờ. Khởi đầu với liều thấp (2.5-10mg), tăng dần CHẬM (mỗi 5-7 ngày). Dùng cho cai nghiện: phải được quản lý bởi chương trình điều trị chuyên khoa.""",
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W",
                "infusion_rate": "Tiêm IV chậm (2-3 phút). Hoặc truyền liên tục.",
                "compatibility": [
                    "NS",
                    "D5W"
    ],
                "incompatibility": [],
                "notes": "Theo dõi hô hấp chặt chẽ. Khởi đầu với liều thấp.",
            },
            "im": {
                "notes": "Tiêm bắp sâu. Theo dõi hô hấp chặt chẽ.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methadone (Dolophine)",
                "UpToDate - Methadone: Drug information",
                "SAMHSA Guidelines - Opioid Treatment Programs"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
    },
    "Morphine": {'group': 'Analgesic - Opioid Agonist (Strong)', 'vietnamese_name':
        'Morphine', 'administration': ['PO', 'IV', 'IM', 'SC'], 'indications':
        ['Đau nặng (ung thư, sau phẫu thuật)', 'Đau cấp tính nặng',
        'Đau mạn tính nặng', 'Khó thở do suy tim', 'Cơn đau do hồi sức'],
        'contraindications': ['Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng', 'Hen phế quản nặng', 'Tắc ruột cơ học',
        'Tăng áp lực nội sọ', 'Suy gan nặng'], 'dosage': {'adult_po_immediate':
        '10-30mg mỗi 4 giờ khi cần', 'adult_po_extended':
        '15-30mg x 2 lần/ngày (MS Contin)', 'adult_iv':
        '2.5-5mg IV mỗi 3-4 giờ hoặc 0.8-10mg/giờ truyền liên tục',
        'adult_im_sc': '5-15mg mỗi 4 giờ', 'elderly': 'Giảm liều 25-50%',
        'notes': 'Thuốc chuẩn vàng cho đau nặng. Theo dõi hô hấp chặt chẽ'},
        'renal_adjustment': {'normal': 'Không đổi', '30_60': 'Giảm liều 25-50%',
        'under_30': 'Giảm liều 50-75%, tăng khoảng cách liều'}, 'side_effects':
        ['Ức chế hô hấp (nguy hiểm)', 'Buồn nôn, nôn',
        'Táo bón (rất thường gặp)', 'Ngứa', 'Buồn ngủ, lú lẫn',
        'Co đồng tử (miosis)', 'Hạ huyết áp', 'Ức chế tiết ADH (SIADH)',
        'Nguy cơ nghiện, lệ thuộc'], 'interactions': [
        'Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp',
        'MAO inhibitor: nguy hiểm - tránh dùng',
        'Rượu: tăng nguy cơ ức chế hô hấp', 'Cimetidine: tăng nồng độ morphine'
        ], 'pregnancy':
        'C - D trong 3 tháng cuối (gây hội chứng cai ở trẻ sơ sinh)',
        'mechanism_of_action':
        'Opioid mu-receptor agonist mạnh. Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Tăng ngưỡng đau, giảm đáp ứng cảm xúc với đau. Tác động lên brainstem → giảm trung tâm hô hấp. Tác động lên đường tiêu hóa → giảm nhu động ruột, tăng trương lực cơ thắt.'
        , 'monitoring': [
        'Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất',
        'Mức độ đau (thang điểm đau)',
        'Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)',
        'Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)',
        'Co đồng tử (miosis) - dấu hiệu đặc trưng của opioid',
        'Dấu hiệu táo bón (rất thường gặp, cần dự phòng)',
        'Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)',
        'Chức năng thận (tích lũy ở suy thận do tích tụ active metabolite)'],
        'precautions': [
        'Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi, suy thận, suy gan'
        , 'Khởi đầu với liều thấp, tăng dần theo đáp ứng',
        'Cần có naloxone sẵn sàng để đảo ngược nếu quá liều',
        'Tránh dùng với benzodiazepine, rượu, thuốc an thần (tăng nguy cơ ức chế hô hấp nặng)'
        , 'Dự phòng táo bón từ đầu (dùng thuốc nhuận tràng)',
        'Thận trọng ở suy thận (tích lũy active metabolite morphine-6-glucuronide - có thể gây ức chế hô hấp kéo dài)'
        , 'Thận trọng ở suy gan (giảm chuyển hóa)',
        'Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài - cần đánh giá định kỳ',
        'Không dùng trong tăng áp lực nội sọ (tăng CO2 → tăng áp lực nội sọ)',
        'Không dùng trong tắc ruột cơ học (tăng trương lực cơ thắt)'],
        'pharmacokinetics': {'half_life': '2-4 giờ', 'onset':
        'IV: 5-10 phút; IM: 15-30 phút; PO: 30-60 phút', 'duration':
        '3-7 giờ (IV), 4-7 giờ (IM), 3-6 giờ (PO)', 'protein_binding': '20-35%',
        'clearance':
        'Chủ yếu qua thận (morphine-6-glucuronide tích lũy ở suy thận)'},
        'storage':
        'Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em (nguy cơ quá liều).'
        , 'black_box_warnings':
        'Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt khi dùng với benzodiazepine hoặc rượu. Morphine có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ.'
        , 'drug_interactions': {'major': [{'drug':
        'Benzodiazepine, thuốc an thần, rượu', 'mechanism':
        'Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp',
        'effect': 'Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong',
        'management':
        'TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều morphine, theo dõi hô hấp liên tục, có naloxone sẵn sàng'
        }, {'drug': 'MAO inhibitors', 'mechanism':
        'Tăng nguy cơ phản ứng tương tác nghiêm trọng', 'effect':
        'Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng',
        'management':
        'CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng morphine'}],
        'moderate': [{'drug': 'Cimetidine', 'mechanism':
        'Ức chế chuyển hóa morphine qua gan', 'effect':
        'Tăng nồng độ morphine, tăng nguy cơ ức chế hô hấp', 'management':
        'Giảm liều morphine 25-50%. Theo dõi hô hấp chặt chẽ'}, {'drug':
        'Rifampin', 'mechanism': 'Cảm ứng enzyme chuyển hóa morphine', 'effect':
        'Giảm hiệu quả morphine', 'management': 'Có thể cần tăng liều morphine'
        }, {'drug': 'Phenothiazine, haloperidol', 'mechanism':
        'Tăng ức chế hệ thần kinh trung ương', 'effect':
        'Tăng nguy cơ ức chế hô hấp, hạ huyết áp', 'management':
        'Thận trọng. Giảm liều morphine, theo dõi hô hấp'}], 'minor': []},
        'contraindications': {'tuyệt_đối': ['Dị ứng morphine hoặc opioid',
        'Ngộ độc cấp tính rượu, thuốc an thần, opioid',
        'Suy hô hấp nặng hoặc suy hô hấp cấp tính',
        'Hen phế quản nặng không kiểm soát', 'Tắc ruột cơ học',
        'Tăng áp lực nội sọ (do tăng CO2)',
        'Dùng MAO inhibitor trong vòng 14 ngày'], 'tương_đối': [
        'Suy thận nặng (CrCl <30) - giảm liều 50-75%, tăng khoảng cách liều (tích lũy morphine-6-glucuronide)'
        , 'Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)',
        'Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)',
        'Trẻ em <12 tuổi - nguy cơ ức chế hô hấp',
        'Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện',
        'Suy tim - tăng nguy cơ ức chế hô hấp',
        'Bệnh phổi tắc nghẽn mạn tính (COPD) - tăng nguy cơ ức chế hô hấp']},
        'pregnancy_lactation': {'fda_category': 'C - D trong tam cá nguyệt 3',
        'pregnancy_details':
        'Tam cá nguyệt 1-2: Có thể dùng nếu lợi ích > nguy cơ cho điều trị đau nặng. Tam cá nguyệt 3: Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng kéo dài. Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.'
        , 'lactation': {'safety': 'Caution', 'details':
        'Morphine bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong sữa mẹ tương đương khoảng 0.8-3% liều mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ, đặc biệt ở trẻ sơ sinh.'
        , 'recommendation':
        'Thận trọng khi cho con bú. Nếu dùng, theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ, bú kém). Tránh dùng liều cao hoặc kéo dài. Dùng liều thấp nhất hiệu quả.'
        }}, 'hepatic_adjustment': {'mild': 'Không đổi', 'moderate':
        'Giảm liều 25-50%', 'severe': 'Giảm liều 50% hoặc tránh dùng', 'notes':
        'Morphine chuyển hóa ở gan qua glucuronidation thành morphine-6-glucuronide (active, mạnh hơn morphine) và morphine-3-glucuronide (inactive). Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy.'
        }, 'overdose_management': {'symptoms': [
        'Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)',
        'Giảm ý thức, hôn mê', 'Co đồng tử (miosis) - dấu hiệu đặc trưng',
        'Hạ huyết áp', 'Nhịp tim chậm', 'Táo bón nặng',
        'Co giật (hiếm, ở trẻ em hoặc liều rất cao)'], 'antidote':
        'Naloxone (opioid antagonist) - đảo ngược tác dụng opioid', 'treatment':
        ['Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT',
        'Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)',
        'Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại',
        'Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với morphine (2-4 giờ)'
        'Theo dõi hô hấp liên tục ít nhất 24 giờ (do half-life dài của morphine-6-glucuronide)'
        , 'Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp',
        'Than hoạt tính nếu uống trong vòng 1-2 giờ (nhưng cần cẩn thận về nguy cơ hôn mê)'
        , 'Theo dõi ECG, huyết áp, nhịp tim liên tục'], 'monitoring':
        'Nhịp thở, SpO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 24 giờ do half-life dài của active metabolite morphine-6-glucuronide'
        }, 'reversal_agents': {'available': True, 'agents': [{'name':
        'Naloxone', 'indication':
        'Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)',
        'dose':
        '0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng'
        , 'notes':
        'Naloxone có half-life ngắn (1 giờ) so với morphine (2-4 giờ) và morphine-6-glucuronide (dài hơn). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp.'
        }]}, 'administration_instructions': {'oral': {'with_food':
        'Có thể dùng với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn'
        , 'timing':
        'Mỗi 4 giờ khi cần (immediate release) hoặc 2 lần/ngày (extended release MS Contin)'
        }, 'iv': {'reconstitution':
        'Pha với 50-100ml NS hoặc D5W cho truyền liên tục. Hoặc tiêm trực tiếp IV',
        'infusion_rate':
        'Tiêm IV chậm trong 2-5 phút. Truyền liên tục: 0.8-10mg/giờ (tùy liều)',
        'compatibility': ['NS', 'D5W', "Ringer's Lactate"], 'incompatibility':
        ['Alkaline solutions'], 'notes':
        'Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần.'
        }, 'im': {'notes':
        'Tiêm bắp sâu. Có thể gây đau tại chỗ tiêm. Tác dụng bắt đầu 15-30 phút.'
        }, 'sc': {'notes':
        'Tiêm dưới da. Có thể gây kích ứng tại chỗ. Tác dụng bắt đầu 15-30 phút.'
        }},         'references': {'primary_sources': [
        'FDA Drug Label - Morphine sulfate',
        'UpToDate - Morphine: Drug information',
        'Lexicomp - Morphine monograph',
        "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"],
        'last_updated': '2025-01-06', 'evidence_level':
        'High - FDA-approved, extensive clinical data, gold standard for severe pain'
        },
        'risk_flags': {
            'high_alert': True,
            'narrow_therapeutic_index': False,
            'bleeding_risk': False,
            'organ_toxicity': ['Respiratory depression (life-threatening)', 'Accumulation of active metabolite (morphine-6-glucuronide) in renal failure'],
            'qt_prolongation': False,
            'hepatotoxicity': False,
            'nephrotoxicity': False,
            'requires_monitoring': ['Respiratory rate and SpO2 - CRITICAL', 'Level of consciousness', 'Blood pressure', 'Renal function (CrCl) - accumulation risk']
        },
        'guideline_tags': [
            'FDA Black Box Warning - Opioid Addiction and Respiratory Depression',
            'ISMP High Alert Medications - Opioids',
            'WHO Guidelines - Cancer Pain Management',
            'CDC Guidelines - Opioid Prescribing',
            'ASHP Guidelines - Opioid Safety'
        ]},
    
    "Oxycodone": {
        "group": "Analgesic - Opioid Agonist (Strong)",
        "vietnamese_name": "Oxycodone, OxyContin, Roxicodone",
        "administration": ["PO", "IV"],
        "indications": [
            "Đau nặng (ung thư, sau phẫu thuật)",
            "Đau cấp tính nặng",
            "Đau mạn tính nặng"
        ],
        "contraindications": [
            "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
            "Suy hô hấp nặng",
            "Hen phế quản nặng",
            "Tắc ruột cơ học",
            "Tăng áp lực nội sọ"
        ],
        "dosage": {
            "adult_po_immediate": "5-15mg mỗi 4-6 giờ khi cần",
            "adult_po_extended": "10-20mg x 2 lần/ngày (OxyContin)",
            "adult_iv": "0.03-0.1mg/kg mỗi 3-4 giờ",
            "opioid_naive": "5mg PO mỗi 4-6 giờ",
            "opioid_tolerant": "Liều cao hơn, dựa trên liều opioid trước đó",
            "notes": "Mạnh hơn morphine khi uống (tỷ lệ 1.5:1). Theo dõi hô hấp chặt chẽ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Giảm liều 50-75%, tăng khoảng cách liều"
        },
        "side_effects": [
            "Ức chế hô hấp (nguy hiểm)",
            "Buồn nôn, nôn",
            "Táo bón (rất thường gặp)",
            "Ngứa",
            "Buồn ngủ, lú lẫn",
            "Co đồng tử (miosis)",
            "Hạ huyết áp",
            "Nguy cơ nghiện, lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Opioid mu-receptor agonist mạnh. Tương tự morphine nhưng có sinh khả dụng uống tốt hơn (60-87% so với 20-30% của morphine). Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. Oxycodone mạnh hơn morphine khi uống (tỷ lệ 1.5:1) do sinh khả dụng tốt hơn.",
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - quan trọng nhất",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim",
            "Co đồng tử (miosis)",
            "Dấu hiệu táo bón (rất thường gặp, cần dự phòng)",
            "Dấu hiệu nghiện/lệ thuộc (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt ở liều đầu tiên, người cao tuổi",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, rượu, thuốc an thần",
            "Dự phòng táo bón từ đầu",
            "Nguy cơ nghiện/lệ thuộc nếu dùng kéo dài",
            "Oxycodone có nguy cơ lạm dụng cao - cần theo dõi chặt chẽ"
        ],
        "pharmacokinetics": {
            "half_life": "3-5 giờ",
            "onset": "PO: 15-30 phút; IV: 5-10 phút",
            "duration": "3-6 giờ (immediate release), 12 giờ (extended release)",
            "protein_binding": "38-45%",
            "clearance": "Gan (chuyển hóa qua CYP3A4, CYP2D6), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Để xa tầm tay trẻ em.",
        "black_box_warnings": "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong. Oxycodone có nguy cơ lạm dụng cao - cần theo dõi chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu phải dùng, giảm liều oxycodone, theo dõi hô hấp liên tục."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oxycodone hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng",
                "Hen phế quản nặng không kiểm soát",
                "Tắc ruột cơ học",
                "Tăng áp lực nội sọ"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều 50-75%",
                "Suy gan nặng - giảm liều 25-50%",
                "Người cao tuổi - giảm liều 25-50%",
                "Tiền sử nghiện/lạm dụng chất - nguy cơ tái nghiện"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Nguy cơ hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối. Tránh dùng kéo dài trong 3 tháng cuối nếu có thể.",
            "lactation": {
                "safety": "Caution",
                "details": "Oxycodone bài tiết vào sữa mẹ. Có thể gây ức chế hô hấp và buồn ngủ ở trẻ bú mẹ.",
                "recommendation": "Thận trọng khi dùng khi cho con bú. Theo dõi trẻ sát."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Giảm liều 25-50%",
            "severe": "Tránh dùng hoặc dùng liều rất thấp",
            "notes": "Oxycodone chuyển hóa ở gan qua CYP3A4 và CYP2D6. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm"
            ],
            "antidote": "Naloxone (opioid antagonist)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn. Hỗ trợ hô hấp NGAY LẬP TỨC",
                "Naloxone: 0.4-2mg IV/IM/SC, có thể lặp lại mỗi 2-3 phút nếu cần",
                "Theo dõi liên tục hô hấp, ý thức, huyết áp",
                "Hỗ trợ hô hấp: thở máy nếu suy hô hấp",
                "Điều trị hạ huyết áp: truyền dịch, vận mạch nếu cần"
            ],
            "monitoring": "Theo dõi liên tục hô hấp, ý thức, huyết áp, nhịp tim"
        },
        "reversal_agents": {
            "available": True,
            "agents": ["Naloxone"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm buồn nôn nhẹ.",
                "timing": "Immediate release: mỗi 4-6 giờ khi cần. Extended release: x 2 lần/ngày. KHÔNG nghiền hoặc nhai extended release tablets."
            },
            "iv": {
                "infusion_rate": "Truyền chậm: 2-5 phút",
                "compatibility": ["0.9% NaCl", "D5W"],
                "notes": "Theo dõi hô hấp chặt chẽ trong khi truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Oxycodone (OxyContin, Roxicodone)",
                "UpToDate - Oxycodone: Drug information",
                "Lexicomp - Oxycodone monograph"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - FDA-approved"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory rate", "Sedation", "Constipation"]
        },
        "guideline_tags": [
            "CDC 2022 Opioid Prescribing Guidelines",
            "FDA Black Box Warning - Opioid addiction, abuse, misuse",
            "ISMP High Alert Medications - Opioids"
        ]
    },

    "Remifentanil": {
        "group": "Analgesic - Opioid Agonist (Strong) - Ultra-short acting (ICU/Anesthesia)",
        "vietnamese_name": "Remifentanil, Ultiva",
        "brand_names": {
            "common": ["Ultiva"],
            "vietnam": ["Remifentanil", "Ultiva"]
        },
        "administration": ["IV"],
        "indications": [
            "Gây mê toàn thân (induction và maintenance)",
            "Giảm đau trong phẫu thuật (intraoperative analgesia)",
            "An thần và giảm đau cho bệnh nhân thở máy trong ICU",
            "An thần cho thủ thuật (procedural sedation)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với remifentanil hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng không có hỗ trợ hô hấp",
                "Dùng MAO inhibitor trong vòng 14 ngày"
            ],
            "tương_đối": [
                "Suy thận nặng - không cần chỉnh liều (chuyển hóa ngoài gan/thận)",
                "Suy gan nặng - không cần chỉnh liều (chuyển hóa ngoài gan)",
                "Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)",
                "Bệnh nhân opioid-naive - khởi đầu liều thấp",
                "Bệnh nhân béo phì - tính liều theo cân nặng lý tưởng (IBW)"
            ]
        },
        "dosage": {
            "adult_anesthesia_induction": "0.5-1 mcg/kg IV bolus (có thể dùng đến 2 mcg/kg cho intubation)",
            "adult_anesthesia_maintenance": "0.05-2 mcg/kg/phút truyền liên tục (tùy mức độ đau và phẫu thuật)",
            "adult_icu_sedation": "0.05-0.15 mcg/kg/phút truyền liên tục",
            "adult_procedural_sedation": "0.5-1 mcg/kg bolus, sau đó 0.05-0.1 mcg/kg/phút",
            "elderly": "Giảm liều 25-50%",
            "obese": "Tính liều theo cân nặng lý tưởng (IBW), không theo cân nặng thực",
            "notes": "Remifentanil có half-life rất ngắn (3-10 phút) do chuyển hóa nhanh bởi esterase trong máu và mô. Tác dụng kết thúc nhanh sau khi ngừng truyền (không tích lũy). Cần truyền liên tục, không dùng bolus đơn độc cho giảm đau kéo dài."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Không cần chỉnh liều (chuyển hóa ngoài gan/thận).",
            "under_30": "Không cần chỉnh liều (chuyển hóa ngoài gan/thận).",
            "notes": "Remifentanil được chuyển hóa bởi esterase trong máu và mô, không phụ thuộc gan/thận. Không tích lũy ở suy thận hoặc suy gan."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Không cần chỉnh liều.",
            "severe": "Không cần chỉnh liều (chuyển hóa ngoài gan).",
            "notes": "Remifentanil được chuyển hóa bởi esterase trong máu và mô, không phụ thuộc chức năng gan. Không tích lũy ở suy gan."
        },
        "side_effects": [
            "Ức chế hô hấp nặng (nguy hiểm, đặc biệt với bolus nhanh)",
            "Rigid chest (co cứng ngực) - đặc biệt với bolus liều cao",
            "Buồn nôn, nôn (thường gặp)",
            "Hạ huyết áp, nhịp tim chậm (bradycardia)",
            "Ngứa",
            "Co đồng tử (miosis)",
            "Buồn ngủ, lú lẫn",
            "Tăng áp lực nội sọ (với liều cao)",
            "Nguy cơ nghiện/lệ thuộc (nhưng ít hơn do dùng ngắn hạn)"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp nặng",
            "Propofol: hiệp đồng an thần và ức chế hô hấp - giảm liều cả hai",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Thuốc chẹn beta: tăng nguy cơ nhịp tim chậm",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        ',
        "pregnancy": "C - D trong 3 tháng cuối",
        ',
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng trong gây mê phẫu thuật nếu cần. Tam cá nguyệt 3: Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Thường dùng trong gây mê phẫu thuật.",
            "lactation": {
                "safety": "Caution",
                "details": "Remifentanil bài tiết vào sữa mẹ ở nồng độ thấp. Do half-life rất ngắn, nồng độ trong sữa giảm nhanh sau khi ngừng truyền.",
                "recommendation": "Có thể cho con bú sau vài giờ khi mẹ tỉnh táo. Theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ)."
            }
        },
        "mechanism_of_action": (
            "Remifentanil là opioid mu-receptor agonist mạnh, mạnh tương đương fentanyl. "
            "Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, "
            "kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. "
            "Đặc điểm độc đáo: Remifentanil được chuyển hóa bởi esterase không đặc hiệu trong máu và mô, "
            "không phụ thuộc gan/thận, có half-life rất ngắn (3-10 phút). "
            "Tác dụng kết thúc nhanh sau khi ngừng truyền (không tích lũy), "
            "làm cho remifentanil lý tưởng cho gây mê có kiểm soát và ICU sedation."
        ),
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - QUAN TRỌNG NHẤT",
            "EtCO2 (end-tidal CO2) trong gây mê",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Co đồng tử (miosis)",
            "Dấu hiệu rigid chest (co cứng ngực) với bolus liều cao",
            "Áp lực nội sọ (nếu có monitoring)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt với bolus nhanh hoặc liều cao",
            "Rigid chest (co cứng ngực) với bolus liều cao - có thể cần muscle relaxant",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, propofol, rượu (tăng nguy cơ ức chế hô hấp nặng)",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Truyền liên tục - không dùng bolus đơn độc cho giảm đau kéo dài",
            "Ở bệnh nhân béo phì: tính liều theo cân nặng lý tưởng (IBW), không theo cân nặng thực",
            "Người cao tuổi: giảm liều 25-50% (tăng nhạy cảm)",
            "Theo dõi huyết động chặt chẽ (có thể gây hạ huyết áp, nhịp tim chậm)"
        ],
        "pharmacokinetics": {
            "half_life": "3-10 phút (rất ngắn, không tích lũy)",
            "onset": "Rất nhanh (30-60 giây với IV bolus)",
            "duration": "Rất ngắn (3-10 phút sau khi ngừng truyền)",
            "protein_binding": "~70%",
            "metabolism": "Esterase không đặc hiệu trong máu và mô (không phụ thuộc gan/thận)",
            "clearance": "Rất nhanh, không tích lũy. Chuyển hóa thành remifentanil acid (inactive), thải trừ qua thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Sau khi pha: ổn định trong 24 giờ ở nhiệt độ phòng. Bảo quản trong tủ lạnh (2-8°C) có thể kéo dài đến 4 giờ sau khi pha.",
        "black_box_warnings": (
            "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. "
            "Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt với bolus nhanh hoặc liều cao. "
            "Remifentanil có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, propofol, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "Giảm liều remifentanil và thuốc an thần. Theo dõi hô hấp liên tục, có naloxone sẵn sàng."
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng remifentanil"
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chẹn beta",
                    "mechanism": "Cộng hưởng tác dụng làm chậm nhịp tim",
                    "effect": "Tăng nguy cơ nhịp tim chậm nặng",
                    "management": "Theo dõi nhịp tim chặt chẽ, có thể cần atropine hoặc glycopyrrolate"
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Rigid chest (co cứng ngực) với bolus liều cao"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "NGỪNG NGAY truyền remifentanil",
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Lưu ý: Do half-life remifentanil rất ngắn (3-10 phút), tác dụng có thể tự hồi phục nhanh sau khi ngừng truyền. Naloxone có thể không cần thiết nếu chỉ ngừng truyền.",
                "Nếu rigid chest: có thể cần muscle relaxant (succinylcholine)",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Atropine hoặc glycopyrrolate nếu nhịp tim chậm nặng"
            ],
            "monitoring": "Nhịp thở, SpO2, EtCO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Do half-life ngắn, theo dõi ít nhất 30-60 phút sau khi ngừng truyền."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV.",
                    "notes": "Lưu ý: Do half-life remifentanil rất ngắn (3-10 phút), tác dụng có thể tự hồi phục nhanh sau khi ngừng truyền. Naloxone có thể không cần thiết nếu chỉ ngừng truyền và hỗ trợ hô hấp."
                }
            ]
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ thường dùng: 20-50 mcg/ml cho truyền liên tục.",
                "infusion_rate": "Bolus: tiêm IV chậm trong 30-60 giây. Truyền liên tục: 0.05-2 mcg/kg/phút (tùy chỉnh theo đáp ứng).",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": ["Alkaline solutions"],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần. Với bolus liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant. Truyền liên tục - không dùng bolus đơn độc cho giảm đau kéo dài."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Remifentanil (Ultiva)",
                "UpToDate - Remifentanil: Drug information",
                "Lexicomp - Remifentanil monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used in anesthesia and ICU"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Respiratory depression (life-threatening)", "Rigid chest syndrome (with high bolus doses)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory rate and SpO2 - CRITICAL", "EtCO2 (in anesthesia)", "Level of consciousness", "Blood pressure and heart rate", "Signs of rigid chest (with bolus doses)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Opioid Addiction and Respiratory Depression",
            "ISMP High Alert Medications - Opioids",
            "ASA Guidelines - Anesthesia Practice",
            "SCCM ICU Sedation Guidelines"
        ]
    },

    "Sufentanil": {
        "group": "Analgesic - Opioid Agonist (Strong) - Very potent (Anesthesia)",
        "vietnamese_name": "Sufentanil, Sufenta",
        "brand_names": {
            "common": ["Sufenta"],
            "vietnam": ["Sufentanil", "Sufenta"]
        },
        "administration": ["IV", "Epidural", "Intrathecal"],
        "indications": [
            "Gây mê toàn thân (induction và maintenance) - đặc biệt phẫu thuật tim mạch",
            "Giảm đau trong phẫu thuật (intraoperative analgesia)",
            "Giảm đau sau phẫu thuật (postoperative analgesia) - epidural/intrathecal",
            "Giảm đau sản khoa (obstetric analgesia) - epidural"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với sufentanil hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng không có hỗ trợ hô hấp",
                "Dùng MAO inhibitor trong vòng 14 ngày"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều 25-50% (tích lũy)",
                "Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)",
                "Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)",
                "Bệnh nhân opioid-naive - khởi đầu liều thấp",
                "Bệnh nhân béo phì - tính liều theo cân nặng lý tưởng (IBW)"
            ]
        },
        "dosage": {
            "adult_anesthesia_induction": "0.3-2 mcg/kg IV bolus (có thể dùng đến 8 mcg/kg cho phẫu thuật tim)",
            "adult_anesthesia_maintenance": "0.3-1.5 mcg/kg/giờ truyền liên tục hoặc bolus 10-25 mcg khi cần",
            "adult_epidural_analgesia": "10-50 mcg epidural, có thể lặp lại mỗi 6-12 giờ",
            "adult_intrathecal_analgesia": "2.5-10 mcg intrathecal (một liều)",
            "adult_obstetric_epidural": "10-15 mcg epidural với local anesthetic",
            "elderly": "Giảm liều 25-50%",
            "obese": "Tính liều theo cân nặng lý tưởng (IBW), không theo cân nặng thực",
            "notes": "Sufentanil mạnh gấp 5-10 lần fentanyl. Tác dụng nhanh, kéo dài hơn fentanyl. Đặc biệt hữu ích trong phẫu thuật tim mạch do ổn định huyết động tốt."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều 25-50% (tích lũy).",
            "under_30": "Giảm liều 50% (tích lũy).",
            "notes": "Sufentanil chuyển hóa ở gan, tích lũy ở suy thận. Cần giảm liều và theo dõi sát ở suy thận."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Giảm liều 25-50%.",
            "severe": "Giảm liều 50% hoặc tránh dùng.",
            "notes": "Sufentanil chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "side_effects": [
            "Ức chế hô hấp nặng (nguy hiểm, đặc biệt với bolus nhanh)",
            "Rigid chest (co cứng ngực) - đặc biệt với bolus liều cao",
            "Buồn nôn, nôn (thường gặp)",
            "Hạ huyết áp, nhịp tim chậm (bradycardia)",
            "Ngứa (đặc biệt với epidural/intrathecal)",
            "Co đồng tử (miosis)",
            "Buồn ngủ, lú lẫn",
            "Tăng áp lực nội sọ (với liều cao)",
            "Ứ đọng nước tiểu (với epidural/intrathecal)",
            "Nguy cơ nghiện/lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp nặng",
            "Propofol: hiệp đồng an thần và ức chế hô hấp - giảm liều cả hai",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Thuốc chẹn beta: tăng nguy cơ nhịp tim chậm",
            "CYP3A4 inhibitors: tăng nồng độ sufentanil",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        ',
        "pregnancy": "C - D trong 3 tháng cuối",
        ',
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng trong gây mê phẫu thuật nếu cần. Tam cá nguyệt 3: Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Thường dùng trong gây mê phẫu thuật và giảm đau sản khoa (epidural).",
            "lactation": {
                "safety": "Caution",
                "details": "Sufentanil bài tiết vào sữa mẹ ở nồng độ thấp. Với epidural/intrathecal: nồng độ trong sữa rất thấp.",
                "recommendation": "Có thể cho con bú sau vài giờ khi mẹ tỉnh táo. Theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ)."
            }
        },
        "mechanism_of_action": (
            "Sufentanil là opioid mu-receptor agonist rất mạnh, mạnh gấp 5-10 lần fentanyl và 500-1000 lần morphine. "
            "Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, "
            "kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. "
            "Sufentanil có tác dụng nhanh (IV: 1-3 phút), kéo dài hơn fentanyl (30-60 phút IV). "
            "Đặc biệt hữu ích trong phẫu thuật tim mạch do ổn định huyết động tốt và giảm đau mạnh."
        ),
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - QUAN TRỌNG NHẤT",
            "EtCO2 (end-tidal CO2) trong gây mê",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Co đồng tử (miosis)",
            "Dấu hiệu rigid chest (co cứng ngực) với bolus liều cao",
            "Áp lực nội sọ (nếu có monitoring)",
            "Với epidural/intrathecal: theo dõi ngứa, ứ đọng nước tiểu"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt với bolus nhanh hoặc liều cao",
            "Rigid chest (co cứng ngực) với bolus liều cao - có thể cần muscle relaxant",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, propofol, rượu (tăng nguy cơ ức chế hô hấp nặng)",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Ở bệnh nhân béo phì: tính liều theo cân nặng lý tưởng (IBW), không theo cân nặng thực",
            "Người cao tuổi: giảm liều 25-50% (tăng nhạy cảm)",
            "Theo dõi huyết động chặt chẽ (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Với epidural/intrathecal: theo dõi ngứa, ứ đọng nước tiểu, ức chế hô hấp"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (IV), có thể kéo dài hơn với liều cao",
            "onset": "Rất nhanh (1-3 phút với IV bolus)",
            "duration": "30-60 phút (IV), kéo dài hơn với liều cao",
            "protein_binding": "~93%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành N-dealkyl sufentanil (inactive)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ). Tích lũy ở suy thận và suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Sau khi pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. "
            "Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt với bolus nhanh hoặc liều cao. "
            "Sufentanil có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, propofol, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "Giảm liều sufentanil và thuốc an thần. Theo dõi hô hấp liên tục, có naloxone sẵn sàng."
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng sufentanil"
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa sufentanil qua CYP3A4, tăng nồng độ",
                    "effect": "Tăng nồng độ sufentanil, tăng nguy cơ ức chế hô hấp nặng",
                    "management": "Giảm liều sufentanil 50-75%. Theo dõi hô hấp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chẹn beta",
                    "mechanism": "Cộng hưởng tác dụng làm chậm nhịp tim",
                    "effect": "Tăng nguy cơ nhịp tim chậm nặng",
                    "management": "Theo dõi nhịp tim chặt chẽ, có thể cần atropine hoặc glycopyrrolate"
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Cảm ứng enzyme chuyển hóa sufentanil, giảm nồng độ",
                    "effect": "Giảm hiệu quả sufentanil",
                    "management": "Có thể cần tăng liều sufentanil"
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Rigid chest (co cứng ngực) với bolus liều cao"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "NGỪNG NGAY truyền sufentanil",
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với sufentanil",
                "Nếu rigid chest: có thể cần muscle relaxant (succinylcholine)",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Atropine hoặc glycopyrrolate nếu nhịp tim chậm nặng"
            ],
            "monitoring": "Nhịp thở, SpO2, EtCO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 4-6 giờ sau khi ngừng truyền do half-life 2-3 giờ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng",
                    "notes": "Naloxone có half-life ngắn (1 giờ) so với sufentanil (2-3 giờ). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp."
                }
            ]
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ thường dùng: 5-50 mcg/ml cho truyền liên tục.",
                "infusion_rate": "Bolus: tiêm IV chậm trong 1-3 phút. Truyền liên tục: 0.3-1.5 mcg/kg/giờ (tùy chỉnh theo đáp ứng).",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": ["Alkaline solutions"],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần. Với bolus liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant."
            },
            "epidural": {
                "technique": "Tiêm qua catheter epidural. Thường phối hợp với local anesthetic (bupivacaine, ropivacaine).",
                "timing": "Có thể lặp lại mỗi 6-12 giờ nếu cần.",
                "notes": "Theo dõi ngứa, ứ đọng nước tiểu, ức chế hô hấp. Cần có naloxone sẵn sàng."
            },
            "intrathecal": {
                "technique": "Tiêm qua kim intrathecal. Thường dùng một liều duy nhất.",
                "timing": "Một liều duy nhất, tác dụng kéo dài 12-24 giờ.",
                "notes": "Theo dõi ngứa, ứ đọng nước tiểu, ức chế hô hấp. Cần có naloxone sẵn sàng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sufentanil (Sufenta)",
                "UpToDate - Sufentanil: Drug information",
                "Lexicomp - Sufentanil monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used in anesthesia, especially cardiac surgery"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Respiratory depression (life-threatening)", "Rigid chest syndrome (with high bolus doses)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory rate and SpO2 - CRITICAL", "EtCO2 (in anesthesia)", "Level of consciousness", "Blood pressure and heart rate", "Signs of rigid chest (with bolus doses)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Opioid Addiction and Respiratory Depression",
            "ISMP High Alert Medications - Opioids",
            "ASA Guidelines - Anesthesia Practice",
            "Cardiac Anesthesia Guidelines"
        ]
    },

    "Alfentanil": {
        "group": "Analgesic - Opioid Agonist (Strong) - Short-acting (Anesthesia)",
        "vietnamese_name": "Alfentanil, Alfenta",
        "brand_names": {
            "common": ["Alfenta"],
            "vietnam": ["Alfentanil", "Alfenta"]
        },
        "administration": ["IV"],
        "indications": [
            "Gây mê toàn thân (induction và maintenance)",
            "Giảm đau trong phẫu thuật ngắn (intraoperative analgesia)",
            "An thần cho thủ thuật ngắn (procedural sedation)"
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với alfentanil hoặc opioid",
                "Ngộ độc cấp tính rượu, thuốc an thần, opioid",
                "Suy hô hấp nặng không có hỗ trợ hô hấp",
                "Dùng MAO inhibitor trong vòng 14 ngày"
            ],
            "tương_đối": [
                "Suy thận nặng - giảm liều 25-50% (tích lũy)",
                "Suy gan nặng - giảm liều 25-50% (giảm chuyển hóa)",
                "Người cao tuổi - giảm liều 25-50% (tăng nhạy cảm)",
                "Bệnh nhân opioid-naive - khởi đầu liều thấp",
                "Bệnh nhân béo phì - tính liều theo cân nặng lý tưởng (IBW)"
            ]
        },
        "dosage": {
            "adult_anesthesia_induction": "8-20 mcg/kg IV bolus (có thể dùng đến 50 mcg/kg cho intubation)",
            "adult_anesthesia_maintenance": "0.5-3 mcg/kg/phút truyền liên tục hoặc bolus 5-10 mcg/kg khi cần",
            "adult_procedural_sedation": "5-10 mcg/kg bolus, sau đó 0.5-1 mcg/kg/phút",
            "elderly": "Giảm liều 25-50%",
            "obese": "Tính liều theo cân nặng lý tưởng (IBW), không theo cân nặng thực",
            "notes": "Alfentanil mạnh bằng 1/4 fentanyl (tỷ lệ 4:1 với fentanyl). Tác dụng nhanh, ngắn hơn fentanyl. Thích hợp cho phẫu thuật ngắn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều.",
            "30_60": "Giảm liều 25-50% (tích lũy).",
            "under_30": "Giảm liều 50% (tích lũy).",
            "notes": "Alfentanil chuyển hóa ở gan, tích lũy ở suy thận. Cần giảm liều và theo dõi sát ở suy thận."
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều.",
            "moderate": "Giảm liều 25-50%.",
            "severe": "Giảm liều 50% hoặc tránh dùng.",
            "notes": "Alfentanil chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nguy cơ tích lũy."
        },
        "side_effects": [
            "Ức chế hô hấp nặng (nguy hiểm, đặc biệt với bolus nhanh)",
            "Rigid chest (co cứng ngực) - đặc biệt với bolus liều cao",
            "Buồn nôn, nôn (thường gặp)",
            "Hạ huyết áp, nhịp tim chậm (bradycardia)",
            "Ngứa",
            "Co đồng tử (miosis)",
            "Buồn ngủ, lú lẫn",
            "Tăng áp lực nội sọ (với liều cao)",
            "Nguy cơ nghiện/lệ thuộc"
        ],
        "interactions": [
            "Thuốc an thần/Benzodiazepine: tăng nguy cơ ức chế hô hấp nặng",
            "Propofol: hiệp đồng an thần và ức chế hô hấp - giảm liều cả hai",
            "MAO inhibitor: nguy hiểm - tránh dùng",
            "Thuốc chẹn beta: tăng nguy cơ nhịp tim chậm",
            "CYP3A4 inhibitors: tăng nồng độ alfentanil",
            "Rượu: tăng nguy cơ ức chế hô hấp"
        ],
        ',
        "pregnancy": "C - D trong 3 tháng cuối",
        ',
        "pregnancy_lactation": {
            "fda_category": "C - D trong tam cá nguyệt 3",
            "pregnancy_details": "Tam cá nguyệt 1-2: Có thể dùng trong gây mê phẫu thuật nếu cần. Tam cá nguyệt 3: Nguy cơ ức chế hô hấp ở trẻ sơ sinh nếu dùng gần ngày sinh. Thường dùng trong gây mê phẫu thuật.",
            "lactation": {
                "safety": "Caution",
                "details": "Alfentanil bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể cho con bú sau vài giờ khi mẹ tỉnh táo. Theo dõi trẻ sát (dấu hiệu ức chế hô hấp, buồn ngủ)."
            }
        },
        "mechanism_of_action": (
            "Alfentanil là opioid mu-receptor agonist mạnh, mạnh bằng 1/4 fentanyl (tỷ lệ 4:1 với fentanyl) và 25-50 lần morphine. "
            "Gắn với mu-opioid receptors trong hệ thần kinh trung ương và ngoại vi, "
            "kích hoạt tín hiệu G-protein, dẫn đến giảm dẫn truyền đau, giảm nhận thức đau, an thần, và ức chế hô hấp. "
            "Alfentanil có tác dụng nhanh (IV: 1-2 phút), ngắn hơn fentanyl (15-30 phút IV). "
            "Thích hợp cho phẫu thuật ngắn do tác dụng nhanh và ngắn."
        ),
        "monitoring": [
            "Nhịp thở và độ bão hòa oxy (SpO2) liên tục - QUAN TRỌNG NHẤT",
            "EtCO2 (end-tidal CO2) trong gây mê",
            "Mức độ đau (thang điểm đau)",
            "Mức độ ý thức (dấu hiệu quá liều: giảm ý thức, thở chậm)",
            "Huyết áp và nhịp tim (có thể gây hạ huyết áp, nhịp tim chậm)",
            "Co đồng tử (miosis)",
            "Dấu hiệu rigid chest (co cứng ngực) với bolus liều cao",
            "Áp lực nội sọ (nếu có monitoring)"
        ],
        "precautions": [
            "Nguy cơ ức chế hô hấp NẶNG - đặc biệt với bolus nhanh hoặc liều cao",
            "Rigid chest (co cứng ngực) với bolus liều cao - có thể cần muscle relaxant",
            "Cần có naloxone sẵn sàng để đảo ngược nếu quá liều",
            "Tránh dùng với benzodiazepine, propofol, rượu (tăng nguy cơ ức chế hô hấp nặng)",
            "Khởi đầu với liều thấp, tăng dần theo đáp ứng",
            "Ở bệnh nhân béo phì: tính liều theo cân nặng lý tưởng (IBW), không theo cân nặng thực",
            "Người cao tuổi: giảm liều 25-50% (tăng nhạy cảm)",
            "Theo dõi huyết động chặt chẽ (có thể gây hạ huyết áp, nhịp tim chậm)"
        ],
        "pharmacokinetics": {
            "half_life": "1-2 giờ (IV), ngắn hơn fentanyl",
            "onset": "Rất nhanh (1-2 phút với IV bolus)",
            "duration": "15-30 phút (IV), ngắn hơn fentanyl",
            "protein_binding": "~92%",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành noralfentanil (inactive)",
            "clearance": "Gan (chuyển hóa), thận (thải trừ). Tích lũy ở suy thận và suy gan."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh đông lạnh. Sau khi pha: ổn định trong 24 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "Nguy cơ nghiện, lạm dụng, và lệ thuộc - chỉ dùng khi thực sự cần thiết. "
            "Nguy cơ ức chế hô hấp nặng có thể dẫn đến tử vong, đặc biệt với bolus nhanh hoặc liều cao. "
            "Alfentanil có thể gây hội chứng cai ở trẻ sơ sinh nếu dùng trong 3 tháng cuối thai kỳ."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Benzodiazepine, thuốc an thần, propofol, rượu",
                    "mechanism": "Tăng ức chế hệ thần kinh trung ương, đặc biệt trung tâm hô hấp",
                    "effect": "Tăng nguy cơ ức chế hô hấp nặng, có thể tử vong",
                    "management": "Giảm liều alfentanil và thuốc an thần. Theo dõi hô hấp liên tục, có naloxone sẵn sàng."
                },
                {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ phản ứng tương tác nghiêm trọng",
                    "effect": "Có thể gây hội chứng serotonin, tăng huyết áp, nguy hiểm tính mạng",
                    "management": "CHỐNG CHỈ ĐỊNH. Ngừng MAOI ít nhất 14 ngày trước khi dùng alfentanil"
                },
                {
                    "drug": "CYP3A4 inhibitors (ketoconazole, itraconazole, ritonavir, clarithromycin)",
                    "mechanism": "Ức chế chuyển hóa alfentanil qua CYP3A4, tăng nồng độ",
                    "effect": "Tăng nồng độ alfentanil, tăng nguy cơ ức chế hô hấp nặng",
                    "management": "Giảm liều alfentanil 50-75%. Theo dõi hô hấp chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chẹn beta",
                    "mechanism": "Cộng hưởng tác dụng làm chậm nhịp tim",
                    "effect": "Tăng nguy cơ nhịp tim chậm nặng",
                    "management": "Theo dõi nhịp tim chặt chẽ, có thể cần atropine hoặc glycopyrrolate"
                },
                {
                    "drug": "CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Cảm ứng enzyme chuyển hóa alfentanil, giảm nồng độ",
                    "effect": "Giảm hiệu quả alfentanil",
                    "management": "Có thể cần tăng liều alfentanil"
                }
            ],
            "minor": []
        },
        "overdose_management": {
            "symptoms": [
                "Ức chế hô hấp nặng (thở chậm <12 lần/phút, ngừng thở)",
                "Giảm ý thức, hôn mê",
                "Co đồng tử (miosis)",
                "Hạ huyết áp",
                "Nhịp tim chậm",
                "Rigid chest (co cứng ngực) với bolus liều cao"
            ],
            "antidote": "Naloxone (opioid antagonist) - đảo ngược tác dụng opioid",
            "treatment": [
                "NGỪNG NGAY truyền alfentanil",
                "Đảm bảo đường thở, hỗ trợ hô hấp (thở máy nếu cần) - QUAN TRỌNG NHẤT",
                "Naloxone: 0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg)",
                "Nếu không có IV: 0.4-2mg IM/SC, có thể lặp lại",
                "Nếu quá liều nặng: có thể cần truyền naloxone liên tục (0.4-0.8mg/giờ) do half-life ngắn (1 giờ) so với alfentanil",
                "Nếu rigid chest: có thể cần muscle relaxant (succinylcholine)",
                "Hỗ trợ huyết động: truyền dịch, vasopressor nếu hạ huyết áp",
                "Atropine hoặc glycopyrrolate nếu nhịp tim chậm nặng"
            ],
            "monitoring": "Nhịp thở, SpO2, EtCO2, ý thức, ECG, huyết áp, nhịp tim liên tục. Theo dõi ít nhất 2-4 giờ sau khi ngừng truyền do half-life 1-2 giờ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Naloxone",
                    "indication": "Đảo ngược tác dụng opioid (ức chế hô hấp, giảm ý thức, hạ huyết áp)",
                    "dose": "0.4-2mg IV, lặp lại mỗi 2-3 phút đến khi đáp ứng (tối đa 10mg). IM/SC: 0.4-2mg nếu không có IV. Truyền liên tục: 0.4-0.8mg/giờ nếu quá liều nặng",
                    "notes": "Naloxone có half-life ngắn (1 giờ) so với alfentanil (1-2 giờ). Có thể cần truyền liên tục hoặc lặp lại liều để tránh tái phát ức chế hô hấp."
                }
            ]
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ thường dùng: 50-500 mcg/ml cho truyền liên tục.",
                "infusion_rate": "Bolus: tiêm IV chậm trong 1-2 phút. Truyền liên tục: 0.5-3 mcg/kg/phút (tùy chỉnh theo đáp ứng).",
                "compatibility": ["NS", "D5W", "Ringer's Lactate"],
                "incompatibility": ["Alkaline solutions"],
                "notes": "Theo dõi hô hấp chặt chẽ khi dùng IV. Cần có naloxone sẵn sàng. Khởi đầu với liều thấp, tăng dần. Với bolus liều cao: có thể gây rigid chest (co cứng ngực) - cần dùng muscle relaxant."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Alfentanil (Alfenta)",
                "UpToDate - Alfentanil: Drug information",
                "Lexicomp - Alfentanil monograph",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used in anesthesia"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Respiratory depression (life-threatening)", "Rigid chest syndrome (with high bolus doses)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Respiratory rate and SpO2 - CRITICAL", "EtCO2 (in anesthesia)", "Level of consciousness", "Blood pressure and heart rate", "Signs of rigid chest (with bolus doses)"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Opioid Addiction and Respiratory Depression",
            "ISMP High Alert Medications - Opioids",
            "ASA Guidelines - Anesthesia Practice"
        ]
    },
}

__all__ = ['OPIOID_AGONIST_STRONGS_DRUGS']
