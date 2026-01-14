"""
Sleep Medications
Thuốc ngủ / điều trị mất ngủ
Zolpidem, Zaleplon, Eszopiclone, Ramelteon, Suvorexant
"""

SLEEP_MEDICATIONS_DRUGS = {
    "Zolpidem":     {
        "group": "Neurology - Sleep Medication (Non-benzodiazepine GABA-A agonist)",
        "vietnamese_name": "Zolpidem, Stilnox, Ambien",
        "brand_names": {
            "common": ["Ambien", "Ambien CR", "Stilnox", "Edluar", "Intermezzo", "Zolpimist"],
            "vietnam": ["Stilnox", "Zolpidem STADA", "Zolpidem Stella", "Zolpidem"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ ngắn hạn (insomnia)",
            "Khó vào giấc ngủ",
            "Thức giấc giữa đêm"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng zolpidem",
                "Suy hô hấp nặng",
                "Myasthenia gravis nặng",
                "Ngưng thở khi ngủ nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy hô hấp nhẹ đến trung bình - thận trọng",
                "Suy gan trung bình - giảm liều",
                "Người cao tuổi - giảm liều",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "5-10mg x 1 lần/ngày, uống trước khi ngủ 15-30 phút",
            "adult_elderly": "5mg x 1 lần/ngày, uống trước khi ngủ 15-30 phút",
            "adult_hepatic_impairment": "5mg x 1 lần/ngày",
            "notes": "Zolpidem là non-benzodiazepine GABA-A receptor agonist, tác dụng nhanh và ngắn. Dùng ngay trước khi ngủ. KHÔNG lái xe hoặc vận hành máy móc sau khi uống. Nguy cơ nghiện nếu dùng kéo dài. CHỈ dùng ngắn hạn (2-4 tuần).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ vào ngày hôm sau (hangover effect)",
            "Chóng mặt",
            "Mất trí nhớ (amnesia) - đặc biệt nếu thức dậy sau khi uống",
            "Rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Ảo giác",
            "Phụ thuộc/nghiện nếu dùng kéo dài",
            "Hội chứng cai thuốc khi ngừng đột ngột"
    ],
        "interactions": [
            "Alcohol: CHỐNG CHỈ ĐỊNH - tăng nguy cơ ức chế hô hấp, mất trí nhớ, rối loạn hành vi",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế, tăng nguy cơ ức chế hô hấp",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ zolpidem, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine) -> Giảm nồng độ zolpidem"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Zolpidem là non-benzodiazepine GABA-A receptor agonist, tác động chọn lọc lên alpha1 subunit của GABA-A receptors. Khác với benzodiazepines, zolpidem có ái lực cao với alpha1 subunit, dẫn đến tác dụng an thần mạnh hơn và ít tác dụng phụ khác (ít lo âu, ít giãn cơ). Zolpidem có tác dụng nhanh (15-30 phút) và t1/2 ngắn (2-3 giờ), phù hợp cho điều trị mất ngủ. Tuy nhiên, vẫn có nguy cơ nghiện và rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm.""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau",
            "Dấu hiệu rối loạn hành vi khi ngủ (sleepwalking, sleep driving)",
            "Dấu hiệu nghiện/phụ thuộc",
            "Chức năng gan (nếu suy gan)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-4 tuần) - nguy cơ nghiện nếu dùng kéo dài",
            "KHÔNG lái xe hoặc vận hành máy móc sau khi uống - nguy cơ buồn ngủ và mất trí nhớ",
            "CHỐNG CHỈ ĐỊNH với rượu - tăng nguy cơ ức chế hô hấp và rối loạn hành vi",
            "Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Giảm liều ở người cao tuổi và suy gan",
            "Không ngừng đột ngột - hội chứng cai thuốc"
    ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (ngắn)",
            "onset": "15-30 phút",
            "duration": "6-8 giờ",
            "protein_binding": "92%",
            "clearance": "Gan: chuyển hóa (CYP3A4, CYP2C9). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm, có thể xảy ra mà không có dấu hiệu cảnh báo. CHỐNG CHỈ ĐỊNH với rượu. Nguy cơ nghiện nếu dùng kéo dài. KHÔNG lái xe sau khi uống.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ ức chế hô hấp",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp nặng, tăng mất trí nhớ, tăng rối loạn hành vi",
                    "management": "CHỐNG CHỈ ĐỊNH. TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều đáng kể.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa zolpidem",
                    "effect": "Tăng nồng độ zolpidem, tăng tác dụng phụ",
                    "management": "Giảm liều zolpidem 50%.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50% (5mg)",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Zolpidem chuyển hóa ở gan (CYP3A4, CYP2C9). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Hôn mê",
                "Ức chế hô hấp",
                "Mất trí nhớ"
    ],
            "antidote": "Flumazenil (có thể đảo ngược một phần tác dụng)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Flumazenil 0.2mg IV, có thể lặp lại (thận trọng - có thể gây co giật)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Flumazenil",
                    "mechanism": "Đối kháng thụ thể benzodiazepine/GABA-A, đảo ngược tác dụng zolpidem",
                    "indication": "Zolpidem quá liều (ức chế hô hấp, hôn mê)",
                    "dose": "0.2mg IV, có thể lặp lại mỗi 1 phút đến tối đa 3mg",
                    "caution": "Có thể gây co giật, đặc biệt ở bệnh nhân có tiền sử co giật. Tác dụng ngắn, có thể cần lặp lại.",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói hoặc với thức ăn nhẹ",
                "timing": "5-10mg x 1 lần/ngày, uống trước khi ngủ 15-30 phút. KHÔNG lái xe sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ambien (Zolpidem)",
                "UpToDate - Zolpidem: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS", "respiratory"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Respiratory status", "Sleep behaviors"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế, nguy cơ tác dụng phụ cao). Zolpidem không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, té ngã, lú lẫn). Tăng nguy cơ rối loạn hành vi khi ngủ.",
                "dose_adjustment": "Bắt đầu 5mg PO trước khi ngủ. Tối đa 5mg/ngày. Không tăng liều quá 10mg/ngày.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã, rối loạn hành vi khi ngủ.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "5,000 - 20,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Stilnox (brand) thường đắt hơn (15,000-20,000 VND/viên 10mg). Zolpidem generic thường rẻ hơn (5,000-10,000 VND/viên 10mg).",
            }
    },
    "Zaleplon":     {
        "group": "Neurology - Sleep Medication (Non-benzodiazepine GABA-A agonist)",
        "vietnamese_name": "Zaleplon, Sonata",
        "brand_names": {
            "common": ["Sonata"],
            "vietnam": ["Zaleplon", "Sonata"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ ngắn hạn (insomnia)",
            "Khó vào giấc ngủ"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng zaleplon",
                "Suy hô hấp nặng",
                "Myasthenia gravis nặng",
                "Ngưng thở khi ngủ nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy hô hấp nhẹ đến trung bình - thận trọng",
                "Suy gan trung bình - giảm liều",
                "Người cao tuổi - giảm liều",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "10mg x 1 lần/ngày, uống trước khi ngủ hoặc khi khó vào giấc ngủ",
            "adult_elderly": "5mg x 1 lần/ngày",
            "adult_hepatic_impairment": "5mg x 1 lần/ngày",
            "notes": "Zaleplon là non-benzodiazepine GABA-A receptor agonist, tác dụng rất nhanh và rất ngắn (t1/2 ~1 giờ). Dùng khi khó vào giấc ngủ hoặc thức giấc giữa đêm (nếu còn ít nhất 4 giờ trước khi thức dậy). KHÔNG lái xe hoặc vận hành máy móc sau khi uống. Nguy cơ nghiện nếu dùng kéo dài. CHỈ dùng ngắn hạn (2-4 tuần).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ vào ngày hôm sau (ít hơn zolpidem do t1/2 ngắn)",
            "Chóng mặt",
            "Mất trí nhớ (amnesia) - đặc biệt nếu thức dậy sau khi uống",
            "Rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Ảo giác",
            "Phụ thuộc/nghiện nếu dùng kéo dài",
            "Hội chứng cai thuốc khi ngừng đột ngột"
    ],
        "interactions": [
            "Alcohol: CHỐNG CHỈ ĐỊNH - tăng nguy cơ ức chế hô hấp, mất trí nhớ, rối loạn hành vi",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế, tăng nguy cơ ức chế hô hấp",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ zaleplon, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine) -> Giảm nồng độ zaleplon"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Zaleplon là non-benzodiazepine GABA-A receptor agonist, tương tự zolpidem nhưng có t1/2 rất ngắn (~1 giờ). Tác động chọn lọc lên alpha1 subunit của GABA-A receptors. Zaleplon có tác dụng rất nhanh (15 phút) và t1/2 rất ngắn, phù hợp cho điều trị khó vào giấc ngủ. Có thể dùng khi thức giấc giữa đêm nếu còn ít nhất 4 giờ trước khi thức dậy. Ít hangover effect hơn zolpidem do t1/2 ngắn. Tuy nhiên, vẫn có nguy cơ nghiện và rối loạn hành vi khi ngủ.""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau (ít hơn zolpidem)",
            "Dấu hiệu rối loạn hành vi khi ngủ (sleepwalking, sleep driving)",
            "Dấu hiệu nghiện/phụ thuộc",
            "Chức năng gan (nếu suy gan)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-4 tuần) - nguy cơ nghiện nếu dùng kéo dài",
            "KHÔNG lái xe hoặc vận hành máy móc sau khi uống",
            "CHỐNG CHỈ ĐỊNH với rượu - tăng nguy cơ ức chế hô hấp và rối loạn hành vi",
            "Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Giảm liều ở người cao tuổi và suy gan",
            "Có thể dùng khi thức giấc giữa đêm nếu còn ít nhất 4 giờ trước khi thức dậy",
            "Không ngừng đột ngột - hội chứng cai thuốc"
    ],
        "pharmacokinetics": {
            "half_life": "1 giờ (rất ngắn)",
            "onset": "15 phút",
            "duration": "3-4 giờ",
            "protein_binding": "60%",
            "clearance": "Gan: chuyển hóa (CYP3A4). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm. CHỐNG CHỈ ĐỊNH với rượu. Nguy cơ nghiện nếu dùng kéo dài. KHÔNG lái xe sau khi uống.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ ức chế hô hấp",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp nặng, tăng mất trí nhớ, tăng rối loạn hành vi",
                    "management": "CHỐNG CHỈ ĐỊNH. TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều đáng kể.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa zaleplon",
                    "effect": "Tăng nồng độ zaleplon, tăng tác dụng phụ",
                    "management": "Giảm liều zaleplon 50%.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50% (5mg)",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Zaleplon chuyển hóa ở gan (CYP3A4). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Hôn mê",
                "Ức chế hô hấp",
                "Mất trí nhớ"
    ],
            "antidote": "Flumazenil (có thể đảo ngược một phần tác dụng)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Flumazenil 0.2mg IV, có thể lặp lại (thận trọng - có thể gây co giật)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Flumazenil",
                    "mechanism": "Đối kháng thụ thể benzodiazepine/GABA-A, đảo ngược tác dụng zaleplon",
                    "indication": "Zaleplon quá liều (ức chế hô hấp, hôn mê)",
                    "dose": "0.2mg IV, có thể lặp lại mỗi 1 phút đến tối đa 3mg",
                    "caution": "Có thể gây co giật, đặc biệt ở bệnh nhân có tiền sử co giật. Tác dụng ngắn, có thể cần lặp lại.",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói hoặc với thức ăn nhẹ",
                "timing": "10mg x 1 lần/ngày, uống trước khi ngủ hoặc khi khó vào giấc ngủ. Có thể dùng khi thức giấc giữa đêm nếu còn ít nhất 4 giờ trước khi thức dậy. KHÔNG lái xe sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sonata (Zaleplon)",
                "UpToDate - Zaleplon: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS", "respiratory"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Respiratory status", "Sleep behaviors"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế, nguy cơ tác dụng phụ cao). Zaleplon không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, té ngã, lú lẫn). Tăng nguy cơ rối loạn hành vi khi ngủ.",
                "dose_adjustment": "Bắt đầu 5mg PO trước khi ngủ. Tối đa 5mg/ngày. Không tăng liều quá 10mg/ngày.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã, rối loạn hành vi khi ngủ.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "10,000 - 30,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sonata (brand) thường đắt hơn. Zaleplon ít phổ biến hơn zolpidem ở Việt Nam.",
            }
    },
    "Eszopiclone":     {
        "group": "Neurology - Sleep Medication (Non-benzodiazepine GABA-A agonist)",
        "vietnamese_name": "Eszopiclone, Lunesta",
        "brand_names": {
            "common": ["Lunesta"],
            "vietnam": ["Eszopiclone", "Lunesta"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ ngắn hạn (insomnia)",
            "Khó vào giấc ngủ",
            "Thức giấc giữa đêm"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng eszopiclone",
                "Suy hô hấp nặng",
                "Myasthenia gravis nặng",
                "Ngưng thở khi ngủ nặng",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy hô hấp nhẹ đến trung bình - thận trọng",
                "Suy gan trung bình - giảm liều",
                "Người cao tuổi - giảm liều",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện"
    ],
        },
        "dosage": {
            "adult_standard": "1-3mg x 1 lần/ngày, uống trước khi ngủ",
            "adult_elderly": "1-2mg x 1 lần/ngày",
            "adult_hepatic_impairment": "1-2mg x 1 lần/ngày",
            "notes": "Eszopiclone là non-benzodiazepine GABA-A receptor agonist, tác dụng trung bình (t1/2 ~6 giờ). Dùng ngay trước khi ngủ. KHÔNG lái xe hoặc vận hành máy móc sau khi uống. Nguy cơ nghiện nếu dùng kéo dài. CHỈ dùng ngắn hạn (2-4 tuần). Có thể gây vị đắng (metallic taste) - phổ biến.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Vị đắng (metallic taste) - phổ biến",
            "Buồn ngủ vào ngày hôm sau (hangover effect)",
            "Chóng mặt",
            "Mất trí nhớ (amnesia) - đặc biệt nếu thức dậy sau khi uống",
            "Rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Ảo giác",
            "Phụ thuộc/nghiện nếu dùng kéo dài",
            "Hội chứng cai thuốc khi ngừng đột ngột"
    ],
        "interactions": [
            "Alcohol: CHỐNG CHỈ ĐỊNH - tăng nguy cơ ức chế hô hấp, mất trí nhớ, rối loạn hành vi",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế, tăng nguy cơ ức chế hô hấp",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ eszopiclone, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine) -> Giảm nồng độ eszopiclone"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Eszopiclone là non-benzodiazepine GABA-A receptor agonist, tương tự zolpidem nhưng có t1/2 dài hơn (~6 giờ). Tác động chọn lọc lên alpha1 subunit của GABA-A receptors. Eszopiclone có tác dụng trung bình và t1/2 dài hơn zolpidem, phù hợp cho điều trị cả khó vào giấc ngủ và thức giấc giữa đêm. Tuy nhiên, có thể gây hangover effect và vị đắng (metallic taste) - phổ biến. Vẫn có nguy cơ nghiện và rối loạn hành vi khi ngủ.""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau",
            "Vị đắng (metallic taste)",
            "Dấu hiệu rối loạn hành vi khi ngủ (sleepwalking, sleep driving)",
            "Dấu hiệu nghiện/phụ thuộc",
            "Chức năng gan (nếu suy gan)"
    ],
        "precautions": [
            "CHỈ dùng ngắn hạn (2-4 tuần) - nguy cơ nghiện nếu dùng kéo dài",
            "KHÔNG lái xe hoặc vận hành máy móc sau khi uống",
            "CHỐNG CHỈ ĐỊNH với rượu - tăng nguy cơ ức chế hô hấp và rối loạn hành vi",
            "Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Vị đắng (metallic taste) - phổ biến, có thể gây khó chịu",
            "Giảm liều ở người cao tuổi và suy gan",
            "Không ngừng đột ngột - hội chứng cai thuốc"
    ],
        "pharmacokinetics": {
            "half_life": "6 giờ (trung bình)",
            "onset": "30 phút",
            "duration": "6-8 giờ",
            "protein_binding": "52-59%",
            "clearance": "Gan: chuyển hóa (CYP3A4, CYP2E1). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm. CHỐNG CHỈ ĐỊNH với rượu. Nguy cơ nghiện nếu dùng kéo dài. KHÔNG lái xe sau khi uống.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ ức chế hô hấp",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp nặng, tăng mất trí nhớ, tăng rối loạn hành vi",
                    "management": "CHỐNG CHỈ ĐỊNH. TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều đáng kể.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa eszopiclone",
                    "effect": "Tăng nồng độ eszopiclone, tăng tác dụng phụ",
                    "management": "Giảm liều eszopiclone 50%.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Giảm liều 50% (1-2mg)",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Eszopiclone chuyển hóa ở gan (CYP3A4, CYP2E1). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Hôn mê",
                "Ức chế hô hấp",
                "Mất trí nhớ"
    ],
            "antidote": "Flumazenil (có thể đảo ngược một phần tác dụng)",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Flumazenil 0.2mg IV, có thể lặp lại (thận trọng - có thể gây co giật)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch",
        },
        "reversal_agents": {
            "available": True,
            "agents": [
    {
                    "agent": "Flumazenil",
                    "mechanism": "Đối kháng thụ thể benzodiazepine/GABA-A, đảo ngược tác dụng eszopiclone",
                    "indication": "Eszopiclone quá liều (ức chế hô hấp, hôn mê)",
                    "dose": "0.2mg IV, có thể lặp lại mỗi 1 phút đến tối đa 3mg",
                    "caution": "Có thể gây co giật, đặc biệt ở bệnh nhân có tiền sử co giật. Tác dụng ngắn, có thể cần lặp lại.",
                }
                ],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói hoặc với thức ăn nhẹ",
                "timing": "1-3mg x 1 lần/ngày, uống trước khi ngủ. KHÔNG lái xe sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lunesta (Eszopiclone)",
                "UpToDate - Eszopiclone: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS", "respiratory"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Respiratory status", "Sleep behaviors"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế, nguy cơ tác dụng phụ cao). Eszopiclone không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, té ngã, lú lẫn, vị đắng). Tăng nguy cơ rối loạn hành vi khi ngủ.",
                "dose_adjustment": "Bắt đầu 1mg PO trước khi ngủ. Tối đa 1mg/ngày. Không tăng liều quá 2mg/ngày.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã, rối loạn hành vi khi ngủ, vị đắng.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "15,000 - 40,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Lunesta (brand) thường đắt hơn. Eszopiclone ít phổ biến hơn zolpidem ở Việt Nam.",
            }
    },
    "Ramelteon":     {
        "group": "Neurology - Sleep Medication (Melatonin receptor agonist)",
        "vietnamese_name": "Ramelteon, Rozerem",
        "brand_names": {
            "common": ["Rozerem"],
            "vietnam": ["Ramelteon", "Rozerem"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ ngắn hạn (insomnia)",
            "Khó vào giấc ngủ"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ramelteon",
                "Suy gan nặng"
    ],
            "tương_đối": [
                "Suy gan trung bình - thận trọng",
                "Tiền sử trầm cảm - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "8mg x 1 lần/ngày, uống trước khi ngủ 30 phút",
            "notes": "Ramelteon là melatonin receptor agonist, tác động lên melatonin MT1 và MT2 receptors trong suprachiasmatic nucleus (SCN) để điều chỉnh nhịp sinh học. KHÔNG gây nghiện, không gây mất trí nhớ, không gây rối loạn hành vi khi ngủ. Có thể dùng lâu dài hơn các thuốc ngủ khác. Uống trước khi ngủ 30 phút.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Buồn ngủ",
            "Chóng mặt",
            "Mệt mỏi",
            "Trầm cảm (hiếm)",
            "Giảm testosterone (hiếm, ở nam giới)"
    ],
        "interactions": [
            "Thuốc ức chế CYP1A2 (Fluvoxamine) -> Tăng nồng độ ramelteon, giảm liều 50%",
            "Thuốc cảm ứng CYP1A2 (Rifampin, Carbamazepine) -> Giảm nồng độ ramelteon",
            "Alcohol -> Tăng tác dụng an thần"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Ramelteon là melatonin receptor agonist, tác động lên melatonin MT1 và MT2 receptors trong suprachiasmatic nucleus (SCN) - trung tâm điều khiển nhịp sinh học. Ramelteon điều chỉnh nhịp sinh học, giúp bắt đầu giấc ngủ. KHÔNG tác động lên GABA-A receptors (khác với benzodiazepines và z-drugs), do đó KHÔNG gây nghiện, không gây mất trí nhớ, không gây rối loạn hành vi khi ngủ. Có thể dùng lâu dài hơn các thuốc ngủ khác. Tuy nhiên, hiệu quả có thể kém hơn benzodiazepines và z-drugs ở một số bệnh nhân.""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau",
            "Dấu hiệu trầm cảm",
            "Chức năng gan (nếu suy gan)"
    ],
        "precautions": [
            "KHÔNG gây nghiện - có thể dùng lâu dài hơn các thuốc ngủ khác",
            "KHÔNG gây mất trí nhớ hoặc rối loạn hành vi khi ngủ",
            "Thận trọng ở bệnh nhân có tiền sử trầm cảm",
            "Uống trước khi ngủ 30 phút",
            "Thận trọng ở suy gan"
    ],
        "pharmacokinetics": {
            "half_life": "1-2.6 giờ (ngắn)",
            "onset": "30 phút",
            "duration": "6-8 giờ",
            "protein_binding": "82%",
            "clearance": "Gan: chuyển hóa (CYP1A2). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP1A2 mạnh (Fluvoxamine)",
                    "mechanism": "Ức chế chuyển hóa ramelteon",
                    "effect": "Tăng nồng độ ramelteon, tăng tác dụng phụ",
                    "management": "Giảm liều ramelteon 50%.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Ramelteon chuyển hóa ở gan (CYP1A2). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Chóng mặt"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Điều trị hỗ trợ",
                "Theo dõi ý thức",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp, tim mạch",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói hoặc với thức ăn nhẹ",
                "timing": "8mg x 1 lần/ngày, uống trước khi ngủ 30 phút.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Rozerem (Ramelteon)",
                "UpToDate - Ramelteon: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế). Ramelteon không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, té ngã, lú lẫn).",
                "dose_adjustment": "Liều tương tự người trẻ (8mg) nhưng thận trọng hơn. Theo dõi sát tác dụng phụ.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "20,000 - 50,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Rozerem (brand) thường đắt hơn. Ramelteon ít phổ biến ở Việt Nam.",
            }
    },
    "Suvorexant":     {
        "group": "Neurology - Sleep Medication (Orexin receptor antagonist)",
        "vietnamese_name": "Suvorexant, Belsomra",
        "brand_names": {
            "common": ["Belsomra"],
            "vietnam": ["Suvorexant", "Belsomra"],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Mất ngủ (insomnia)",
            "Khó vào giấc ngủ",
            "Thức giấc giữa đêm"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng suvorexant",
                "Narcolepsy (chứng ngủ rũ)"
    ],
            "tương_đối": [
                "Suy gan nặng - thận trọng",
                "Suy thận nặng - thận trọng",
                "Tiền sử nghiện/lạm dụng chất - tăng nguy cơ nghiện",
                "Trầm cảm nặng - thận trọng"
    ],
        },
        "dosage": {
            "adult_standard": "10-20mg x 1 lần/ngày, uống trước khi ngủ tối đa 30 phút",
            "adult_elderly": "10mg x 1 lần/ngày",
            "notes": "Suvorexant là orexin receptor antagonist, ức chế hệ thống orexin (hypocretin) - hệ thống điều khiển sự tỉnh táo. KHÔNG tác động lên GABA-A receptors, do đó ít nguy cơ nghiện và mất trí nhớ hơn benzodiazepines và z-drugs. Có thể dùng lâu dài hơn. Uống trước khi ngủ tối đa 30 phút. CHỐNG CHỈ ĐỊNH ở narcolepsy.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Buồn ngủ vào ngày hôm sau (hangover effect)",
            "Chóng mặt",
            "Mệt mỏi",
            "Rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Ảo giác",
            "Phụ thuộc/nghiện nếu dùng kéo dài (ít hơn benzodiazepines)",
            "Trầm cảm (hiếm)"
    ],
        "interactions": [
            "Alcohol: CHỐNG CHỈ ĐỊNH - tăng nguy cơ ức chế hô hấp, mất trí nhớ, rối loạn hành vi",
            "CNS depressants (Benzodiazepines, Opioids) -> Tăng tác dụng ức chế, tăng nguy cơ ức chế hô hấp",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ suvorexant, giảm liều 50%",
            "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine) -> Giảm nồng độ suvorexant"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Suvorexant là orexin receptor antagonist, ức chế hệ thống orexin (hypocretin) - hệ thống điều khiển sự tỉnh táo trong não. Orexin được sản xuất bởi các tế bào thần kinh trong vùng dưới đồi, kích thích sự tỉnh táo. Suvorexant ức chế orexin receptors → giảm sự tỉnh táo → tăng khả năng ngủ. KHÔNG tác động lên GABA-A receptors (khác với benzodiazepines và z-drugs), do đó ít nguy cơ nghiện và mất trí nhớ hơn. Có thể dùng lâu dài hơn. Tuy nhiên, vẫn có nguy cơ rối loạn hành vi khi ngủ và phụ thuộc (ít hơn benzodiazepines). CHỐNG CHỈ ĐỊNH ở narcolepsy (bệnh nhân narcolepsy đã thiếu orexin).""",
        "monitoring": [
            "Đáp ứng điều trị: cải thiện giấc ngủ",
            "Buồn ngủ vào ngày hôm sau",
            "Dấu hiệu rối loạn hành vi khi ngủ (sleepwalking, sleep driving)",
            "Dấu hiệu nghiện/phụ thuộc",
            "Dấu hiệu trầm cảm"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở narcolepsy",
            "KHÔNG lái xe hoặc vận hành máy móc sau khi uống",
            "CHỐNG CHỈ ĐỊNH với rượu - tăng nguy cơ ức chế hô hấp và rối loạn hành vi",
            "Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm",
            "Thận trọng ở bệnh nhân có tiền sử trầm cảm",
            "Uống trước khi ngủ tối đa 30 phút",
            "Có thể dùng lâu dài hơn benzodiazepines (ít nguy cơ nghiện hơn)"
    ],
        "pharmacokinetics": {
            "half_life": "12 giờ (dài)",
            "onset": "30 phút",
            "duration": "8-10 giờ",
            "protein_binding": "99.5%",
            "clearance": "Gan: chuyển hóa (CYP3A4). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """Nguy cơ rối loạn hành vi khi ngủ (sleepwalking, sleep driving) - hiếm nhưng nguy hiểm. CHỐNG CHỈ ĐỊNH với rượu. CHỐNG CHỈ ĐỊNH ở narcolepsy. KHÔNG lái xe sau khi uống.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Alcohol",
                    "mechanism": "Tăng tác dụng ức chế CNS, tăng nguy cơ ức chế hô hấp",
                    "effect": "Tăng buồn ngủ, tăng nguy cơ ức chế hô hấp nặng, tăng mất trí nhớ, tăng rối loạn hành vi",
                    "management": "CHỐNG CHỈ ĐỊNH. TRÁNH RƯỢU hoàn toàn khi dùng thuốc này.",
                },
    {
                    "drug": "CNS depressants (Benzodiazepines, Opioids)",
                    "mechanism": "Tăng tác dụng ức chế CNS",
                    "effect": "Tăng buồn ngủ, nguy cơ ức chế hô hấp nặng",
                    "management": "Tránh dùng chung hoặc giảm liều đáng kể.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa suvorexant",
                    "effect": "Tăng nồng độ suvorexant, tăng tác dụng phụ",
                    "management": "Giảm liều suvorexant 50%.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây buồn ngủ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, giảm liều",
            "notes": "Suvorexant chuyển hóa ở gan (CYP3A4). Thận trọng ở suy gan.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Hôn mê",
                "Ức chế hô hấp",
                "Mất trí nhớ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Hỗ trợ hô hấp nếu cần",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ý thức, hô hấp (QUAN TRỌNG), tim mạch",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi bụng đói hoặc với thức ăn nhẹ",
                "timing": "10-20mg x 1 lần/ngày, uống trước khi ngủ tối đa 30 phút. KHÔNG lái xe sau khi uống.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Belsomra (Suvorexant)",
                "UpToDate - Suvorexant: Drug information",
                "AASM Guidelines - Insomnia Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
            "risk_flags": {
                "high_alert": True,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": ["CNS", "respiratory"],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["CNS status", "Respiratory status", "Sleep behaviors"],
            },
            "guideline_tags": [
                "FDA Drug Information",
                "UpToDate Drug Information",
                "AASM Guidelines - Insomnia Treatment",
            ],
            "pediatric_dosing": {
                "notes": "Không khuyến cáo cho trẻ em dưới 18 tuổi (dữ liệu hạn chế). Suvorexant không được FDA chấp thuận cho trẻ em.",
            },
            "geriatric_dosing": {
                "considerations": "Người cao tuổi nhạy cảm hơn với tác dụng phụ (buồn ngủ, chóng mặt, té ngã, lú lẫn). Tăng nguy cơ rối loạn hành vi khi ngủ, tê liệt khi ngủ.",
                "dose_adjustment": "Bắt đầu 10mg PO trước khi ngủ. Tối đa 15mg/ngày. Không tăng liều quá 20mg/ngày.",
                "monitoring": "Theo dõi sát tác dụng phụ TKTW, nguy cơ té ngã, rối loạn hành vi khi ngủ, tê liệt khi ngủ, dấu hiệu trầm cảm.",
            },
            "cost_estimate": {
                "unit": "VND",
                "range": "30,000 - 80,000 VND/viên (tùy hàm lượng và thương hiệu)",
                "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Belsomra (brand) thường đắt hơn. Suvorexant ít phổ biến ở Việt Nam.",
            }
    },
}

__all__ = ["SLEEP_MEDICATIONS_DRUGS"]
