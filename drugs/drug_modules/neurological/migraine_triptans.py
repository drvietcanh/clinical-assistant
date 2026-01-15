"""
Migraine Triptans (Serotonin 5-HT1B/1D Agonists)
"""

MIGRAINE_TRIPTANS = {
    "Sumatriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Sumatriptan, Imigran",
        "brand_names": {
            "common": [
                "Imitrex",
                "Imigran"
    ],
            "vietnam": [
                "Sumatriptan",
                "Imigran",
                "Sumagran"
    ],
        },
        "administration": [
            "PO",
            "SC",
            "Nasal Spray"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Điều trị Cluster Headache (Dạng tiêm SC)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)"
    ],
        },
        "dosage": {
            "adult_oral": "25, 50, hoặc 100 mg. Có thể lặp lại sau 2 giờ. Tối đa 200 mg/24h.",
            "adult_sc": "6 mg SC. Có thể lặp lại sau 1 giờ. Tối đa 12 mg/24h. (Hiệu quả nhanh nhất).",
            "adult_nasal": "5-20 mg/lần. Lặp lại sau 2 giờ. Tối đa 40 mg/24h.",
            "notes": "Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - thường lành tính nhưng cần phân biệt với tim mạch",
            "Chóng mặt, buồn ngủ",
            "Nóng bừng mặt",
            "Phản ứng tại chỗ tiêm (SC)"
    ],
        "interactions": [
            "MAO Inhibitors: Tăng nồng độ Sumatriptan -> Ngộ độc Serotonin/Tác dụng phụ tim mạch.",
            "Ergotamine (trong vòng 24h): Co mạch quá mức -> Chống chỉ định.",
            "SSRI/SNRI: Về lý thuyết tăng nguy cơ Serotonin Syndrome (hiếm gặp trên lâm sàng)."
    ],
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": """Nhiều dữ liệu (Sumatriptan Registry) cho thấy tương đối an toàn, không tăng nguy cơ dị tật lớn. Ưu tiên dùng nếu cần thiết.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Bài tiết thấp. Có thể bỏ bú 8-12h sau dùng thuốc để an toàn tuyệt đối, nhưng thường được xem là an toàn.""",
                "recommendation": "",
            },
        },
        "mechanism_of_action": """Kích thích thụ thể 5-HT1B/1D gây co mạch máu não (đang bị giãn trong cơn Migraine) và ức chế giải phóng neuropeptide viêm.""",
        "monitoring": [
            "Huyết áp",
            "Dấu hiệu thiếu máu cơ tim (nếu có nguy cơ cao)"
    ],
        "pregnancy": "",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế)",
            "children_2_12": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế). Migraine hiếm ở trẻ em dưới 12 tuổi.",
            "adolescents_12_18": "12-17 tuổi: 25mg PO hoặc 6mg SC. Có thể lặp lại sau 2 giờ (PO) hoặc 1 giờ (SC). Tối đa 200mg/24h (PO) hoặc 12mg/24h (SC).",
            "notes": "CHỐNG CHỈ ĐỊNH với bệnh tim mạch, tăng huyết áp không kiểm soát, đột quỵ/TIA tiền sử. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Dùng càng sớm càng tốt khi bắt đầu cơn đau."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi tăng nguy cơ bệnh tim mạch → CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch. Tăng nguy cơ tác dụng phụ (cảm giác nặng/thắt ngực). Suy gan phổ biến hơn → CHỐNG CHỈ ĐỊNH nếu suy gan nặng.",
            "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch, tăng huyết áp không kiểm soát. Theo dõi chặt chẽ tác dụng phụ tim mạch.",
            "monitoring": "Theo dõi tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - QUAN TRỌNG. Phân biệt với triệu chứng tim mạch thật. Theo dõi huyết áp. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "30,000 - 150,000 VND/viên PO hoặc ống SC (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Sumatriptan generic thường rẻ hơn (30,000-80,000 VND/viên 50mg PO). Imitrex/Imigran (brand) thường đắt hơn (80,000-150,000 VND/viên 50mg PO). Dạng SC: 100,000-200,000 VND/ống 6mg."
        }
    },
    "Rizatriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Rizatriptan, Maxalt",
        "brand_names": {
            "common": [
                "Maxalt",
                "Maxalt-MLT"
    ],
            "vietnam": [
                "Rizatriptan",
                "Maxalt"
    ],
        },
        "administration": [
            "PO",
            "ODT (Viên phân tán)"
    ],
        "indications": [
            "Migraine cấp tính"
    ],
        "dosage": {
            "adult": "5-10 mg. Lặp lại sau 2 giờ. Tối đa 30 mg/24h.",
            "with_propranolol": "Propranolol làm tăng nồng độ Rizatriptan -> Dùng tối đa 5 mg/lần, tối đa 15 mg/24h.",
            "notes": "Khởi phát tác dụng nhanh (hơn Sumatriptan uống).",
        },
        "interactions": [
            "Propranolol: Tăng nồng độ Rizatriptan 70%. Cần giảm liều Rizatriptan."
    ],
        "side_effects": [
            "Buồn ngủ, chóng mặt",
            "Khô miệng"
    ],
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "Kém an toàn hơn Sumatriptan (ít dữ liệu hơn).",
            "lactation": {
                "safety": "Caution",
                "details": "Thận trọng.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "contraindications": [],
        "pregnancy": "",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế)",
            "children_2_12": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế). Migraine hiếm ở trẻ em dưới 12 tuổi.",
            "adolescents_12_18": "12-17 tuổi: 5mg PO. Có thể lặp lại sau 2 giờ. Tối đa 15mg/24h.",
            "notes": "CHỐNG CHỈ ĐỊNH với bệnh tim mạch, tăng huyết áp không kiểm soát, đột quỵ/TIA tiền sử. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Dùng càng sớm càng tốt khi bắt đầu cơn đau."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi tăng nguy cơ bệnh tim mạch → CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch. Tăng nguy cơ tác dụng phụ (cảm giác nặng/thắt ngực). Suy gan phổ biến hơn → CHỐNG CHỈ ĐỊNH nếu suy gan nặng.",
            "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch, tăng huyết áp không kiểm soát. Giảm liều 50% nếu dùng với propranolol. Theo dõi chặt chẽ tác dụng phụ tim mạch.",
            "monitoring": "Theo dõi tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - QUAN TRỌNG. Phân biệt với triệu chứng tim mạch thật. Theo dõi huyết áp. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "40,000 - 180,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Rizatriptan generic thường rẻ hơn (40,000-100,000 VND/viên 10mg). Maxalt (brand) thường đắt hơn (100,000-180,000 VND/viên 10mg)."
        }
    },
    "Zolmitriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Zolmitriptan, Zomig",
        "brand_names": {
            "common": [
                "Zomig"
    ],
            "vietnam": [
                "Zolmitriptan",
                "Zomig"
    ],
        },
        "administration": [
            "PO",
            "Nasal Spray"
    ],
        "indications": [
            "Migraine cấp tính",
            "Cluster Headache (Nasal Spray - ít dùng hơn Sumatriptan SC)"
    ],
        "dosage": {
            "adult_oral": "2.5 mg. Lặp lại sau 2 giờ. Tối đa 10 mg/24h.",
            "adult_nasal": "5 mg. Tối đa 10 mg/24h.",
        },
        "interactions": [
            "Cimetidine: Ức chế chuyển hóa Zolmitriptan."
    ],
        "side_effects": [],
        "contraindications": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Thận trọng trong thai kỳ",
        "mechanism_of_action": "",
        "monitoring": [],
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "",
            "pregnancy_details": "",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "",
            "moderate": "",
            "severe": "",
            "notes": "",
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": None,
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ sơ sinh <1 tháng tuổi (dữ liệu hạn chế)",
            "infants": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế)",
            "children_2_12": "Không khuyến cáo cho trẻ <12 tuổi (dữ liệu hạn chế). Migraine hiếm ở trẻ em dưới 12 tuổi.",
            "adolescents_12_18": "12-17 tuổi: 2.5mg PO hoặc nasal spray. Có thể lặp lại sau 2 giờ. Tối đa 10mg/24h.",
            "notes": "CHỐNG CHỈ ĐỊNH với bệnh tim mạch, tăng huyết áp không kiểm soát, đột quỵ/TIA tiền sử. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Dùng càng sớm càng tốt khi bắt đầu cơn đau."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi tăng nguy cơ bệnh tim mạch → CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch. Tăng nguy cơ tác dụng phụ (cảm giác nặng/thắt ngực). Suy gan phổ biến hơn → CHỐNG CHỈ ĐỊNH nếu suy gan nặng.",
            "dose_adjustment": "Liều tương tự người trẻ nhưng thận trọng hơn. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch, tăng huyết áp không kiểm soát. Theo dõi chặt chẽ tác dụng phụ tim mạch.",
            "monitoring": "Theo dõi tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - QUAN TRỌNG. Phân biệt với triệu chứng tim mạch thật. Theo dõi huyết áp. CHỐNG CHỈ ĐỊNH nếu có bệnh tim mạch."
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "50,000 - 200,000 VND/viên PO hoặc nasal spray (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Zolmitriptan generic thường rẻ hơn (50,000-120,000 VND/viên 2.5mg PO). Zomig (brand) thường đắt hơn (120,000-200,000 VND/viên 2.5mg PO). Dạng nasal spray: 150,000-250,000 VND/lọ."
        }
    },
    "Eletriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Eletriptan, Relpax",
        "brand_names": {
            "common": [
                "Relpax"
    ],
            "vietnam": [
                "Eletriptan",
                "Relpax"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Cluster headache (off-label)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)",
                "Dùng cùng thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)"
    ],
            "relative": [
                "Suy gan trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_oral": "20-40mg x 1 lần. Có thể lặp lại sau 2 giờ. Tối đa 80mg/24h.",
            "notes": "Eletriptan là triptan có tác dụng nhanh và hiệu quả cao. Dùng càng sớm càng tốt khi bắt đầu cơn đau. CHỐNG CHỈ ĐỊNH với thuốc ức chế CYP3A4 mạnh (tăng nồng độ eletriptan, tăng nguy cơ tác dụng phụ tim mạch).",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - thường lành tính nhưng cần phân biệt với tim mạch",
            "Chóng mặt, buồn ngủ",
            "Nóng bừng mặt",
            "Mệt mỏi",
            "Buồn nôn"
    ],
        "interactions": [
            "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole): CHỐNG CHỈ ĐỊNH - tăng nồng độ eletriptan, tăng nguy cơ tác dụng phụ tim mạch",
            "Ergotamine/Dihydroergotamine: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Eletriptan là 5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Eletriptan có tác dụng nhanh (30-60 phút PO) và hiệu quả cao. Chuyển hóa qua CYP3A4 → CHỐNG CHỈ ĐỊNH với thuốc ức chế CYP3A4 mạnh.""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Tác dụng phụ tim mạch (cảm giác nặng/thắt ngực) - phân biệt với triệu chứng tim mạch thật",
            "Huyết áp"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
            "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "Dùng càng sớm càng tốt khi bắt đầu cơn đau (không chờ đến khi đau nặng)",
            "Không dùng để phòng ngừa",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "4 giờ",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "85%",
            "clearance": "Gan: chuyển hóa (CYP3A4). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với thuốc ức chế CYP3A4 mạnh. CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Nguy cơ co mạch mạch vành và mạch máu ngoại vi.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole, Voriconazole)",
                    "mechanism": "Ức chế chuyển hóa eletriptan qua CYP3A4",
                    "effect": "Tăng nồng độ eletriptan, tăng nguy cơ tác dụng phụ tim mạch nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH. Không dùng cùng.",
                },
    {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ",
                    "effect": "Tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                }
                ],
            "moderate": [
    {
                    "drug": "SSRI, SNRI",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin (hiếm)",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ. Có nguy cơ co mạch có thể ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Eletriptan chuyển hóa ở gan (CYP3A4). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch mạch vành (đau ngực, nhồi máu cơ tim)",
                "Co mạch mạch máu ngoại vi",
                "Tăng huyết áp",
                "Chóng mặt, buồn ngủ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "20-40mg x 1 lần khi có cơn migraine. Có thể lặp lại sau 2 giờ nếu cần. Tối đa 80mg/24h. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Relpax (Eletriptan)",
                "UpToDate - Triptans for acute migraine",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "vascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms"],
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AHS Guidelines - Acute Migraine Treatment",
        ],
    },
    "Almotriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Almotriptan, Axert",
        "brand_names": {
            "common": [
                "Axert"
    ],
            "vietnam": [
                "Almotriptan",
                "Axert"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Suy thận nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)"
    ],
            "relative": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_oral": "6.25-12.5mg x 1 lần. Có thể lặp lại sau 2 giờ. Tối đa 25mg/24h.",
            "adult_renal_impairment": "6.25mg x 1 lần. Tối đa 12.5mg/24h.",
            "notes": "Almotriptan là triptan có tác dụng tốt và ít tác dụng phụ hơn một số triptans khác. Dùng càng sớm càng tốt khi bắt đầu cơn đau. Giảm liều ở suy thận.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% (6.25mg)",
            "under_30": "Giảm liều 50% (6.25mg), tối đa 12.5mg/24h"
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - ít hơn một số triptans khác",
            "Chóng mặt, buồn ngủ",
            "Nóng bừng mặt",
            "Mệt mỏi",
            "Buồn nôn"
    ],
        "interactions": [
            "Ergotamine/Dihydroergotamine: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Almotriptan là 5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Almotriptan có tác dụng tốt và ít tác dụng phụ hơn một số triptans khác. Thải trừ qua cả gan và thận → giảm liều ở suy thận.""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Tác dụng phụ tim mạch (cảm giác nặng/thắt ngực)",
            "Chức năng thận (nếu suy thận)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "Giảm liều ở suy thận",
            "Dùng càng sớm càng tốt khi bắt đầu cơn đau",
            "Không dùng để phòng ngừa",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "3-4 giờ",
            "onset": "30-60 phút",
            "duration": "4-6 giờ",
            "protein_binding": "35%",
            "clearance": "Gan: chuyển hóa (MAO-A). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Nguy cơ co mạch mạch vành và mạch máu ngoại vi.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Ức chế chuyển hóa almotriptan qua MAO-A",
                    "effect": "Tăng nồng độ almotriptan, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                }
                ],
            "moderate": [
    {
                    "drug": "SSRI, SNRI",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin (hiếm)",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ. Có nguy cơ co mạch có thể ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Almotriptan chuyển hóa ở gan (MAO-A). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch mạch vành (đau ngực, nhồi máu cơ tim)",
                "Co mạch mạch máu ngoại vi",
                "Tăng huyết áp",
                "Chóng mặt, buồn ngủ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "6.25-12.5mg x 1 lần khi có cơn migraine. Có thể lặp lại sau 2 giờ nếu cần. Tối đa 25mg/24h. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Axert (Almotriptan)",
                "UpToDate - Triptans for acute migraine",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "vascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms", "RFT"],
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AHS Guidelines - Acute Migraine Treatment",
        ],
    },
    "Frovatriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Frovatriptan, Frova",
        "brand_names": {
            "common": [
                "Frova"
    ],
            "vietnam": [
                "Frovatriptan",
                "Frova"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Đau nửa đầu liên quan đến kinh nguyệt (menstrual migraine)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)"
    ],
            "relative": [
                "Suy gan trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_oral": "2.5mg x 1 lần. Có thể lặp lại sau 2 giờ. Tối đa 7.5mg/24h.",
            "adult_menstrual_migraine": "2.5mg x 2 lần/ngày, bắt đầu 2 ngày trước khi có kinh và tiếp tục trong 6 ngày",
            "notes": "Frovatriptan là triptan có t1/2 dài (26 giờ), phù hợp cho đau nửa đầu liên quan đến kinh nguyệt. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness)",
            "Chóng mặt, buồn ngủ",
            "Nóng bừng mặt",
            "Mệt mỏi",
            "Buồn nôn"
    ],
        "interactions": [
            "Ergotamine/Dihydroergotamine: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Frovatriptan là 5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Frovatriptan có t1/2 dài (26 giờ), phù hợp cho đau nửa đầu liên quan đến kinh nguyệt (menstrual migraine) - có thể dùng dự phòng ngắn hạn.""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Tác dụng phụ tim mạch (cảm giác nặng/thắt ngực)",
            "Tần suất đau nửa đầu liên quan đến kinh nguyệt (nếu dùng để dự phòng)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "Dùng càng sớm càng tốt khi bắt đầu cơn đau",
            "Không dùng để phòng ngừa thường xuyên (chỉ dùng cho menstrual migraine)",
            "T1/2 dài - có thể tích lũy nếu dùng nhiều lần",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "26 giờ (dài)",
            "onset": "30-60 phút",
            "duration": "Kéo dài",
            "protein_binding": "15%",
            "clearance": "Gan: chuyển hóa (MAO-A). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Nguy cơ co mạch mạch vành và mạch máu ngoại vi.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Ức chế chuyển hóa frovatriptan qua MAO-A",
                    "effect": "Tăng nồng độ frovatriptan, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                }
                ],
            "moderate": [
    {
                    "drug": "SSRI, SNRI",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin (hiếm)",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ. Có nguy cơ co mạch có thể ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Frovatriptan chuyển hóa ở gan (MAO-A). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch mạch vành (đau ngực, nhồi máu cơ tim)",
                "Co mạch mạch máu ngoại vi",
                "Tăng huyết áp",
                "Chóng mặt, buồn ngủ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "2.5mg x 1 lần khi có cơn migraine. Có thể lặp lại sau 2 giờ nếu cần. Tối đa 7.5mg/24h. Đối với menstrual migraine: 2.5mg x 2 lần/ngày, bắt đầu 2 ngày trước khi có kinh và tiếp tục trong 6 ngày.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Frova (Frovatriptan)",
                "UpToDate - Triptans for acute migraine",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "vascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms"],
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AHS Guidelines - Acute Migraine Treatment",
        ],
    },
    "Naratriptan":     {
        "group": "Neurology - Migraine (Triptan)",
        "vietnamese_name": "Naratriptan, Amerge",
        "brand_names": {
            "common": [
                "Amerge"
    ],
            "vietnam": [
                "Naratriptan",
                "Amerge"
    ],
        },
        "administration": [
            "PO"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Đau nửa đầu liên quan đến kinh nguyệt (menstrual migraine)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Suy thận nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)"
    ],
            "relative": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - giảm liều",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_oral": "1-2.5mg x 1 lần. Có thể lặp lại sau 4 giờ. Tối đa 5mg/24h.",
            "adult_renal_impairment": "1mg x 1 lần. Tối đa 2.5mg/24h.",
            "notes": "Naratriptan là triptan có tác dụng chậm hơn nhưng ít tác dụng phụ hơn. T1/2 dài (5-6 giờ). Giảm liều ở suy thận. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 50% (1mg)",
            "under_30": "Giảm liều 50% (1mg), tối đa 2.5mg/24h"
        },
        "side_effects": [
            "Cảm giác nặng/thắt ngực, cổ họng (Chest tightness) - ít hơn một số triptans khác",
            "Chóng mặt, buồn ngủ",
            "Nóng bừng mặt",
            "Mệt mỏi",
            "Buồn nôn"
    ],
        "interactions": [
            "Ergotamine/Dihydroergotamine: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Naratriptan là 5-HT1B/1D receptor agonist (selective serotonin receptor agonist, triptan). Kích thích 5-HT1B receptors ở mạch máu não → co mạch (giảm giãn mạch trong migraine). Kích thích 5-HT1D receptors → ức chế phóng thích chất trung gian gây viêm (CGRP, substance P) từ dây thần kinh trigeminal. Giảm đau migraine thông qua cả hai cơ chế: co mạch và ức chế viêm thần kinh. Naratriptan có tác dụng chậm hơn nhưng ít tác dụng phụ hơn một số triptans khác. T1/2 dài (5-6 giờ). Thải trừ qua cả gan và thận → giảm liều ở suy thận.""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "Tác dụng phụ tim mạch (cảm giác nặng/thắt ngực)",
            "Chức năng thận (nếu suy thận)"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "Giảm liều ở suy thận",
            "Dùng càng sớm càng tốt khi bắt đầu cơn đau",
            "Không dùng để phòng ngừa",
            "Tác dụng chậm hơn một số triptans khác",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "5-6 giờ (dài)",
            "onset": "1-2 giờ (chậm hơn một số triptans khác)",
            "duration": "4-6 giờ",
            "protein_binding": "28-31%",
            "clearance": "Gan: chuyển hóa (MAO-A). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH với ergotamine/dihydroergotamine trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. Nguy cơ co mạch mạch vành và mạch máu ngoại vi.",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Ergotamine, Dihydroergotamine",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với ergotamine/dihydroergotamine trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Ức chế chuyển hóa naratriptan qua MAO-A",
                    "effect": "Tăng nồng độ naratriptan, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                }
                ],
            "moderate": [
    {
                    "drug": "SSRI, SNRI",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin (hiếm)",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C. Có thể dùng nếu lợi ích > nguy cơ. Có nguy cơ co mạch có thể ảnh hưởng đến thai nhi.",
            "lactation": {
                "safety": "Caution",
                "details": "Bài tiết vào sữa mẹ. Có thể gây tác dụng phụ ở trẻ.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Naratriptan chuyển hóa ở gan (MAO-A). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch mạch vành (đau ngực, nhồi máu cơ tim)",
                "Co mạch mạch máu ngoại vi",
                "Tăng huyết áp",
                "Chóng mặt, buồn ngủ"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers)",
                "Rửa dạ dày nếu trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "1-2.5mg x 1 lần khi có cơn migraine. Có thể lặp lại sau 4 giờ nếu cần. Tối đa 5mg/24h. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Amerge (Naratriptan)",
                "UpToDate - Triptans for acute migraine",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "vascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms", "RFT"],
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AHS Guidelines - Acute Migraine Treatment",
        ],
    },
    "Dihydroergotamine":     {
        "group": "Neurology - Migraine (Ergot Alkaloid)",
        "vietnamese_name": "Dihydroergotamine, DHE, Migranal",
        "brand_names": {
            "common": [
                "Migranal",
                "DHE-45"
    ],
            "vietnam": [
                "Dihydroergotamine",
                "DHE",
                "Migranal"
    ],
        },
        "administration": [
            "IM",
            "IV",
            "Nasal Spray"
    ],
        "indications": [
            "Cắt cơn đau đầu Migraine cấp tính (có hoặc không có aura)",
            "Cluster headache",
            "Status migrainosus (migraine kéo dài >72 giờ)"
    ],
        "contraindications": {
            "absolute": [
                "Bệnh mạch vành, Đau thắt ngực, Nhồi máu cơ tim cũ",
                "Tăng huyết áp không kiểm soát",
                "Đột quỵ hoặc TIA tiền sử",
                "Bệnh mạch máu ngoại vi",
                "Suy gan nặng",
                "Suy thận nặng",
                "Dùng cùng MAO Inhibitors (trong 14 ngày)",
                "Dùng cùng triptans (trong 24 giờ)",
                "Nhiễm trùng huyết",
                "Phụ nữ có thai"
    ],
            "relative": [
                "Suy gan trung bình - thận trọng",
                "Suy thận trung bình - thận trọng",
                "Rối loạn nhịp tim - thận trọng"
    ],
        },
        "dosage": {
            "adult_im": "1mg IM. Có thể lặp lại sau 1 giờ. Tối đa 3mg/24h.",
            "adult_iv": "0.5-1mg IV. Có thể lặp lại sau 1 giờ. Tối đa 3mg/24h.",
            "adult_nasal": "0.5mg mỗi lỗ mũi (tổng 1mg). Có thể lặp lại sau 15 phút. Tối đa 4mg/24h.",
            "notes": "Dihydroergotamine là ergot alkaloid, tác dụng mạnh và kéo dài. Dùng khi triptans không hiệu quả hoặc chống chỉ định. CHỐNG CHỈ ĐỊNH với triptans trong 24 giờ. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai. Dùng càng sớm càng tốt khi bắt đầu cơn đau.",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "CHỐNG CHỈ ĐỊNH"
        },
        "side_effects": [
            "Co mạch mạch vành (đau ngực, nhồi máu cơ tim) - nghiêm trọng",
            "Co mạch mạch máu ngoại vi - nghiêm trọng",
            "Tăng huyết áp",
            "Buồn nôn, nôn - phổ biến",
            "Chóng mặt",
            "Mệt mỏi",
            "Co thắt cơ trơn (co thắt tử cung, co thắt ruột)"
    ],
        "interactions": [
            "Triptans: CHỐNG CHỈ ĐỊNH (trong 24 giờ) - tăng nguy cơ co mạch nặng",
            "MAO inhibitors: CHỐNG CHỈ ĐỊNH (trong 14 ngày)",
            "Thuốc ức chế CYP3A4 (Ketoconazole, Clarithromycin) -> Tăng nồng độ dihydroergotamine, tăng nguy cơ tác dụng phụ",
            "SSRI/SNRI: tăng nguy cơ hội chứng serotonin (hiếm)"
    ],
        "pregnancy": "X (chống chỉ định)",
        "mechanism_of_action": """Dihydroergotamine là ergot alkaloid, tác động lên nhiều thụ thể: (1) 5-HT1B/1D receptors → co mạch mạch máu não và ức chế phóng thích chất trung gian gây viêm (CGRP, substance P), (2) Alpha-adrenergic receptors → co mạch, (3) Dopamine receptors → chống nôn. Dihydroergotamine có tác dụng mạnh và kéo dài hơn triptans, phù hợp cho migraine nặng hoặc status migrainosus. Tuy nhiên, có nhiều tác dụng phụ hơn triptans: co mạch mạch vành và mạch máu ngoại vi, buồn nôn, nôn. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai (co thắt tử cung).""",
        "monitoring": [
            "Đáp ứng lâm sàng (giảm đau migraine, triệu chứng)",
            "ECG, huyết áp liên tục - QUAN TRỌNG",
            "Tác dụng phụ tim mạch (đau ngực, nhồi máu cơ tim)",
            "Tác dụng phụ mạch máu ngoại vi (co thắt, hoại tử)",
            "Buồn nôn, nôn"
    ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH với triptans trong 24 giờ",
            "CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày",
            "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai",
            "NGUY CƠ CO MẠCH MẠCH VÀNH VÀ MẠCH MÁU NGOẠI VI NGHIÊM TRỌNG - theo dõi ECG, huyết áp liên tục",
            "Buồn nôn, nôn - phổ biến, có thể cần thuốc chống nôn trước khi dùng",
            "Dùng khi triptans không hiệu quả hoặc chống chỉ định",
            "Thận trọng ở bệnh nhân có nguy cơ tim mạch"
    ],
        "pharmacokinetics": {
            "half_life": "9 giờ",
            "onset": "15-30 phút (IM/IV), 30-60 phút (nasal)",
            "duration": "Kéo dài",
            "protein_binding": "93%",
            "clearance": "Gan: chuyển hóa (CYP3A4). Thận: thải trừ.",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": """NGUY CƠ CO MẠCH MẠCH VÀNH VÀ MẠCH MÁU NGOẠI VI NGHIÊM TRỌNG. CHỐNG CHỈ ĐỊNH với triptans trong 24 giờ. CHỐNG CHỈ ĐỊNH với MAO inhibitors trong 14 ngày. CHỐNG CHỈ ĐỊNH ở phụ nữ có thai. Buồn nôn, nôn - phổ biến.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Triptans (Sumatriptan, Rizatriptan, Zolmitriptan, Eletriptan, Almotriptan, Frovatriptan, Naratriptan)",
                    "mechanism": "Tác dụng cộng dồn co mạch",
                    "effect": "Tăng nguy cơ co mạch mạch vành và mạch máu ngoại vi nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng với triptans trong 24 giờ.",
                },
    {
                    "drug": "MAO inhibitors",
                    "mechanism": "Tăng nguy cơ tác dụng phụ",
                    "effect": "Tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng trong 14 ngày sau khi ngừng MAO inhibitors.",
                },
    {
                    "drug": "Thuốc ức chế CYP3A4 mạnh (Ketoconazole, Clarithromycin, Itraconazole)",
                    "mechanism": "Ức chế chuyển hóa dihydroergotamine",
                    "effect": "Tăng nồng độ dihydroergotamine, tăng nguy cơ tác dụng phụ nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH. Không dùng cùng.",
                }
                ],
            "moderate": [
    {
                    "drug": "SSRI, SNRI",
                    "mechanism": "Tăng nguy cơ hội chứng serotonin",
                    "effect": "Tăng nguy cơ hội chứng serotonin (hiếm)",
                    "management": "Thận trọng. Theo dõi dấu hiệu hội chứng serotonin.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "X (chống chỉ định)",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH ở phụ nữ có thai. Có thể gây co thắt tử cung và dị tật bẩm sinh.",
            "lactation": {
                "safety": "Contraindicated",
                "details": "Bài tiết vào sữa mẹ. Có thể gây tác dụng phụ nghiêm trọng ở trẻ.",
                "recommendation": "KHÔNG dùng khi cho con bú.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Dihydroergotamine chuyển hóa ở gan (CYP3A4). Suy gan nặng là chống chỉ định.",
        },
        "overdose_management": {
            "symptoms": [
                "Co mạch mạch vành nặng (đau ngực, nhồi máu cơ tim)",
                "Co mạch mạch máu ngoại vi nặng (hoại tử)",
                "Tăng huyết áp nặng",
                "Buồn nôn, nôn nặng",
                "Co thắt tử cung (ở phụ nữ có thai)"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Đánh giá đường thở, hô hấp, tuần hoàn - QUAN TRỌNG",
                "Theo dõi ECG, huyết áp liên tục - QUAN TRỌNG",
                "Điều trị co mạch nếu có (nitroglycerin, calcium channel blockers, phentolamine)",
                "Điều trị tăng huyết áp nếu có",
                "Hỗ trợ hô hấp nếu cần",
                "Điều trị hỗ trợ"
    ],
            "monitoring": "Theo dõi ECG, huyết áp liên tục (QUAN TRỌNG), ý thức, hô hấp, dấu hiệu hoại tử mạch máu ngoại vi",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "im": {
                "reconstitution": "Không cần pha",
                "injection_site": "Tiêm bắp",
                "notes": "1mg IM. Có thể lặp lại sau 1 giờ. Tối đa 3mg/24h.",
            },
            "iv": {
                "reconstitution": "Pha trong Normal saline hoặc D5W",
                "infusion_rate": "Tiêm chậm hoặc truyền trong 15-30 phút",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [],
                "notes": "0.5-1mg IV. Có thể lặp lại sau 1 giờ. Tối đa 3mg/24h. Theo dõi ECG, huyết áp liên tục.",
            },
            "nasal": {
                "preparation": "Lắc đều trước khi dùng",
                "technique": "Xịt 0.5mg vào mỗi lỗ mũi (tổng 1mg)",
                "notes": "0.5mg mỗi lỗ mũi (tổng 1mg). Có thể lặp lại sau 15 phút. Tối đa 4mg/24h.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Migranal (Dihydroergotamine)",
                "UpToDate - Dihydroergotamine: Drug information",
                "AHS Guidelines - Acute Migraine Treatment"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "vascular"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Blood pressure", "Cardiac symptoms", "Vascular symptoms"],
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "AHS Guidelines - Acute Migraine Treatment",
        ],
    },
}
