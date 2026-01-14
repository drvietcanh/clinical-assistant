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
}
