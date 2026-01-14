"""
Obstetrics and Gynecology Medications
Hormone replacement therapy
"""
from typing import Dict, Any

HORMONE_REPLACEMENT_DRUGS: Dict[str, Dict[str, Any]] = {
    "Estradiol":     {
        "group": "Obstetrics/Gynecology - Estrogen Replacement Therapy",
        "vietnamese_name": "Estradiol, Estrace, Climara",
        "administration": [
            "PO",
            "Transdermal",
            "Vaginal"
    ],
        "indications": [
            "Điều trị triệu chứng mãn kinh (hot flashes, night sweats, vaginal dryness)",
            "Phòng ngừa loãng xương (osteoporosis) ở phụ nữ mãn kinh",
            "Điều trị suy buồng trứng (ovarian failure)",
            "Điều trị thiếu hụt estrogen (hypoestrogenism)",
            "Điều trị khô âm đạo (vaginal atrophy)"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng estradiol",
                "Ung thư vú hiện tại hoặc tiền sử",
                "Ung thư nội mạc tử cung hiện tại hoặc tiền sử",
                "Ung thư gan hiện tại hoặc tiền sử",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim)",
                "Tăng huyết áp không kiểm soát",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân",
                "Đã mang thai (suspected or confirmed)"
    ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tăng huyết áp kiểm soát tốt - thận trọng",
                "Đái tháo đường - thận trọng",
                "Migraine - thận trọng",
                "Bệnh túi mật - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng"
    ],
        },
        "dosage": {
            "adult_menopause_po": "1-2mg PO x 1 lần/ngày",
            "adult_menopause_transdermal": "0.025-0.1mg/ngày qua patch, thay mỗi 3-7 ngày tùy chế phẩm",
            "adult_vaginal_atrophy": "0.5-2g cream hoặc 10-25mcg tablet đặt âm đạo x 1 lần/ngày trong 2 tuần, sau đó 2-3 lần/tuần",
            "notes": """Estradiol là estrogen replacement therapy. Nhiều chế phẩm và đường dùng. Dùng liều thấp nhất hiệu quả. Nếu còn tử cung, cần dùng kết hợp với progestin để giảm nguy cơ ung thư nội mạc tử cung.""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể",
        },
        "side_effects": {
            "phổ_biến": [
                "Đau đầu",
                "Buồn nôn",
                "Đau vú",
                "Chảy máu âm đạo bất thường (breakthrough bleeding)",
                "Chuột rút bụng",
                "Đầy hơi",
                "Tăng cân nhẹ",
                "Giữ nước"
    ],
            "nghiêm_trọng": [
                "Ung thư vú - tăng nguy cơ",
                "Ung thư nội mạc tử cung - tăng nguy cơ (nếu dùng đơn độc không có progestin)",
                "Huyết khối tĩnh mạch sâu (DVT) - tăng nguy cơ",
                "Thuyên tắc phổi (PE) - tăng nguy cơ",
                "Đột quỵ (stroke) - tăng nguy cơ",
                "Nhồi máu cơ tim (MI) - tăng nguy cơ",
                "Bệnh túi mật (gallbladder disease) - tăng nguy cơ",
                "Bệnh gan (viêm gan, u máu gan) - hiếm"
    ],
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
    ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ estradiol"
    ],
        },
"pregnancy": "X - CHỐNG CHỈ ĐỊNH nếu đã mang thai",
        "mechanism_of_action": """Estradiol là estrogen tự nhiên. Bổ sung estrogen cho phụ nữ mãn kinh hoặc thiếu hụt estrogen. Tác dụng: (1) Giảm triệu chứng mãn kinh (hot flashes, night sweats), (2) Cải thiện khô âm đạo, (3) Phòng ngừa loãng xương, (4) Cải thiện tình trạng da và tóc. ĐẶC ĐIỂM: (1) Nhiều chế phẩm và đường dùng (PO, transdermal, vaginal), (2) Dùng liều thấp nhất hiệu quả, (3) Nếu còn tử cung, cần dùng kết hợp với progestin, (4) Nguy cơ ung thư vú, huyết khối tĩnh mạch, đột quỵ - tăng nguy cơ, (5) Nguy cơ ung thư nội mạc tử cung nếu dùng đơn độc không có progestin.""",
        "monitoring": [
            "Triệu chứng mãn kinh (hot flashes, night sweats, vaginal dryness)",
            "Huyết áp - định kỳ",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, đau ngực, khó thở) - NGUY HIỂM",
            "Dấu hiệu đột quỵ (yếu liệt, nói khó, nhìn mờ) - NGUY HIỂM",
            "Dấu hiệu nhồi máu cơ tim (đau ngực, khó thở) - NGUY HIỂM",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)",
            "Mật độ xương (nếu dùng để phòng ngừa loãng xương)"
    ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh tim mạch nặng",
                "Dùng liều thấp nhất hiệu quả - QUAN TRỌNG",
                "Nếu còn tử cung, cần dùng kết hợp với progestin để giảm nguy cơ ung thư nội mạc tử cung",
                "Nguy cơ ung thư vú - tăng nguy cơ, cần khám vú định kỳ",
                "Nguy cơ huyết khối tĩnh mạch (DVT, PE) - tăng nguy cơ",
                "Nguy cơ đột quỵ, nhồi máu cơ tim - tăng nguy cơ",
                "Nguy cơ ung thư nội mạc tử cung nếu dùng đơn độc không có progestin - tăng nguy cơ",
                "Nguy cơ bệnh túi mật - tăng nguy cơ"
    ],
            "khác": [
                "Chảy máu âm đạo bất thường - phổ biến trong vài tháng đầu, thường giảm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân có tiền sử bệnh túi mật"
    ],
        },
        "pharmacokinetics": {
            "half_life": "PO: 13-20 giờ; Transdermal: phụ thuộc patch",
            "onset": "Vài tuần",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "37%",
            "metabolism": "Gan (CYP3A4, CYP1A2)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Patch: bảo quản trong túi kín.",
        "black_box_warnings": """Nguy cơ ung thư vú, huyết khối tĩnh mạch (DVT, PE), đột quỵ, nhồi máu cơ tim. CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh tim mạch nặng. Dùng liều thấp nhất hiệu quả trong thời gian ngắn nhất cần thiết.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa estradiol",
                    "effect": "Giảm nồng độ estradiol, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều estradiol.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa estradiol",
                    "effect": "Tăng nồng độ estradiol, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng estradiol",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư nội mạc tử cung hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư gan hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh tim mạch nặng (bệnh mạch vành, đột quỵ, nhồi máu cơ tim) - CHỐNG CHỈ ĐỊNH",
                "Tăng huyết áp không kiểm soát - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - CHỐNG CHỈ ĐỊNH",
                "Đã mang thai - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tăng huyết áp kiểm soát tốt - thận trọng",
                "Đái tháo đường - thận trọng",
                "Migraine - thận trọng",
                "Bệnh túi mật - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": """Estradiol là thuốc phân loại X. CHỐNG CHỈ ĐỊNH nếu đã mang thai. Nếu mang thai khi đang dùng, ngừng ngay và tư vấn bác sĩ.""",
            "lactation": {
                "safety": "Compatible with Caution",
                "details": """Estradiol bài tiết vào sữa mẹ ở nồng độ thấp. Có thể ảnh hưởng đến sản xuất sữa và trẻ bú mẹ. Không khuyến cáo dùng khi cho con bú.""",
                "recommendation": "Không khuyến cáo dùng khi cho con bú. Cân nhắc ngừng cho con bú hoặc ngừng thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": """Estradiol chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng.""",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Chảy máu âm đạo nặng",
                "Chóng mặt, mệt mỏi"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay estradiol",
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất"
    ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất cho đến khi hồi phục.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn. Có thể uống không thức ăn.",
                "timing": "1-2mg PO x 1 lần/ngày. Uống đều đặn.",
                "notes": """QUAN TRỌNG: 1) Dùng liều thấp nhất hiệu quả, 2) Nếu còn tử cung, cần dùng kết hợp với progestin, 3) Nguy cơ ung thư vú, huyết khối tĩnh mạch, đột quỵ.""",
            },
            "transdermal": {
                "preparation": "Patch estradiol.",
                "application": "Dán patch lên vùng da sạch, khô (bụng, mông, đùi). Thay patch mỗi 3-7 ngày tùy chế phẩm.",
                "dosing": "0.025-0.1mg/ngày tùy chế phẩm.",
                "notes": """QUAN TRỌNG: 1) Dùng liều thấp nhất hiệu quả, 2) Nếu còn tử cung, cần dùng kết hợp với progestin, 3) Thay patch đúng lịch.""",
            },
            "vaginal": {
                "preparation": "Cream hoặc tablet estradiol.",
                "application": """Đặt cream hoặc tablet vào âm đạo. 0.5-2g cream hoặc 10-25mcg tablet x 1 lần/ngày trong 2 tuần, sau đó 2-3 lần/tuần.""",
                "notes": """QUAN TRỌNG: 1) Dùng cho khô âm đạo, 2) Hấp thu toàn thân tối thiểu, 3) Ít nguy cơ tác dụng phụ toàn thân hơn PO/transdermal.""",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Estradiol (Estrace, Climara)",
                "ACOG Practice Bulletin - Hormone Therapy",
                "NAMS (North American Menopause Society) Guidelines",
                "UpToDate - Estradiol: Drug Information",
                "Medscape - Estradiol Drug Reference"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/NAMS guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"oncologic": "Black Box Warning - Endometrial cancer (if unopposed), breast cancer risk", "cardiovascular": "Black Box Warning - Cardiovascular events (stroke, MI, DVT, PE)", "neurological": "Black Box Warning - Dementia (in women ≥65 years)", "hepatic": "Hepatotoxicity (rare), hepatic hemangioma (rare)", "gastrointestinal": "Gallbladder disease"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Breast cancer (mammography recommended)", "Black Box Warning - Endometrial cancer (if unopposed, need progestin)", "Black Box Warning - Cardiovascular events (DVT, PE, stroke, MI signs)", "Black Box Warning - Dementia (in women ≥65 years)", "Blood pressure", "Vaginal bleeding (abnormal bleeding)", "Hepatic function (hepatotoxicity risk)"],
            "look_alike_sound_alike": ["Estradiol", "Estradiol"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Endometrial Cancer (if unopposed)",
            "FDA Black Box Warning - Cardiovascular Events (stroke, MI, DVT, PE)",
            "FDA Black Box Warning - Dementia (in women ≥65 years)",
            "ACOG Practice Bulletin - Hormone Therapy",
            "NAMS Guidelines - Hormone Therapy",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

    "Progesterone":     {
        "group": "Obstetrics/Gynecology - Progestin Replacement Therapy",
        "vietnamese_name": "Progesterone, Prometrium, Crinone",
        "administration": [
            "PO",
            "Vaginal",
            "IM"
    ],
        "indications": [
            "Điều trị thiếu hụt progesterone (hypoprogesteronism)",
            "Hỗ trợ giai đoạn hoàng thể (luteal phase support) trong thụ tinh trong ống nghiệm (IVF)",
            "Dự phòng sẩy thai tái phát do thiếu hụt progesterone",
            "Điều hòa kinh nguyệt (menstrual regulation)",
            "Điều trị rong kinh (menorrhagia)",
            "Kết hợp với estrogen trong hormone replacement therapy (HRT) để giảm nguy cơ ung thư nội mạc tử cung"
    ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng progesterone",
                "Ung thư vú hiện tại hoặc tiền sử",
                "Ung thư nội mạc tử cung hiện tại (trừ điều trị ung thư)",
                "Ung thư gan hiện tại hoặc tiền sử",
                "Bệnh gan nặng (viêm gan cấp, suy gan)",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân"
    ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Đái tháo đường - thận trọng",
                "Trầm cảm - thận trọng (có thể làm nặng)"
    ],
        },
        "dosage": {
            "adult_luteal_support_po": "200-300mg PO x 2-3 lần/ngày trong 12-14 ngày",
            "adult_luteal_support_vaginal": "90-200mg gel hoặc 100-200mg suppository đặt âm đạo x 2-3 lần/ngày trong 12-14 ngày",
            "adult_ivf_support": "Theo phác đồ IVF, thường 200mg gel đặt âm đạo x 2-3 lần/ngày hoặc 200-300mg PO x 2-3 lần/ngày",
            "adult_hrt": "200mg PO x 1 lần/ngày trong 12-14 ngày mỗi tháng (kết hợp với estrogen)",
            "notes": """Progesterone là progestin tự nhiên. Nhiều chế phẩm và đường dùng. Dùng liều thấp nhất hiệu quả. Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân hơn).""",
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Không cần điều chỉnh đáng kể",
        },
        "side_effects": {
            "phổ_biến": [
                "Buồn ngủ, mệt mỏi - phổ biến (đặc biệt với PO)",
                "Chóng mặt",
                "Đau đầu",
                "Buồn nôn",
                "Đau vú",
                "Chảy máu âm đạo bất thường (breakthrough bleeding)",
                "Thay đổi tâm trạng",
                "Tăng cân nhẹ"
    ],
            "nghiêm_trọng": [
                "Ung thư vú - tăng nguy cơ nhẹ",
                "Huyết khối tĩnh mạch sâu (DVT) - hiếm",
                "Thuyên tắc phổi (PE) - hiếm",
                "Bệnh gan (viêm gan, u máu gan) - hiếm"
    ],
        },
        "interactions": {
            "giảm_hiệu_quả": [
                "Thuốc cảm ứng CYP3A4 (rifampin, carbamazepine, phenytoin, St. John's Wort)"
    ],
            "tăng_nguy_cơ": [
                "Thuốc ức chế CYP3A4 (ketoconazole, ritonavir): tăng nồng độ progesterone"
    ],
        },
"pregnancy": "B - An toàn trong thai kỳ (dùng cho hỗ trợ giai đoạn hoàng thể)",
        "mechanism_of_action": """Progesterone là progestin tự nhiên. Tác dụng: (1) Chuẩn bị niêm mạc tử cung (endometrium) cho thai làm tổ, (2) Duy trì thai kỳ sớm (hỗ trợ giai đoạn hoàng thể), (3) Ức chế co bóp tử cung, (4) Giảm nguy cơ ung thư nội mạc tử cung khi dùng kết hợp với estrogen trong HRT. ĐẶC ĐIỂM: (1) Nhiều chế phẩm và đường dùng (PO, vaginal, IM), (2) Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân), (3) Buồn ngủ, mệt mỏi phổ biến với PO, (4) An toàn trong thai kỳ (category B), (5) Dùng kết hợp với estrogen trong HRT để giảm nguy cơ ung thư nội mạc tử cung.""",
        "monitoring": [
            "Triệu chứng (buồn ngủ, mệt mỏi, chóng mặt)",
            "Chảy máu âm đạo bất thường",
            "Dấu hiệu ung thư vú (khối u vú, thay đổi da vú)",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, đau ngực, khó thở) - hiếm",
            "Tình trạng thai (nếu dùng cho hỗ trợ giai đoạn hoàng thể)"
    ],
        "precautions": {
            "quan_trọng": [
                "CHỐNG CHỈ ĐỊNH ở ung thư vú, huyết khối tĩnh mạch, bệnh gan nặng",
                "Dùng liều thấp nhất hiệu quả",
                "Buồn ngủ, mệt mỏi phổ biến với PO - tránh lái xe hoặc vận hành máy móc",
                "Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân)",
                "Có thể gây trầm cảm - cần theo dõi sát",
                "Nguy cơ ung thư vú - tăng nguy cơ nhẹ"
    ],
            "khác": [
                "Chảy máu âm đạo bất thường - phổ biến, thường giảm",
                "Thận trọng ở bệnh nhân dùng thuốc cảm ứng CYP3A4 (có thể giảm hiệu quả)",
                "Thận trọng ở bệnh nhân có tiền sử trầm cảm"
    ],
        },
        "pharmacokinetics": {
            "half_life": "PO: 16-18 giờ; Vaginal: phụ thuộc chế phẩm",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (cần dùng liên tục)",
            "protein_binding": "96-99%",
            "metabolism": "Gan (CYP3A4, CYP2C19)",
            "clearance": "Gan, thận (bài tiết qua nước tiểu và phân)",
        },
        "storage": """Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Một số chế phẩm cần bảo quản trong tủ lạnh.""",
        "black_box_warnings": "Cần xem xét black box warnings",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Thuốc cảm ứng CYP3A4 (Rifampin, Carbamazepine, Phenytoin, St. John's Wort)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa progesterone",
                    "effect": "Giảm nồng độ progesterone, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều progesterone.",
                }
                ],
            "moderate": [
    {
                    "drug": "Thuốc ức chế CYP3A4 (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa progesterone",
                    "effect": "Tăng nồng độ progesterone, tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Theo dõi tác dụng phụ.",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng progesterone",
                "Ung thư vú hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Ung thư nội mạc tử cung hiện tại (trừ điều trị ung thư) - CHỐNG CHỈ ĐỊNH",
                "Ung thư gan hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Bệnh gan nặng (viêm gan cấp, suy gan) - CHỐNG CHỈ ĐỊNH",
                "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) hiện tại hoặc tiền sử - CHỐNG CHỈ ĐỊNH",
                "Xuất huyết âm đạo bất thường chưa rõ nguyên nhân - CHỐNG CHỈ ĐỊNH"
    ],
            "tương_đối": [
                "Bệnh gan nhẹ - thận trọng",
                "Tiền sử gia đình ung thư vú - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Đái tháo đường - thận trọng",
                "Trầm cảm - thận trọng (có thể làm nặng)"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": """Progesterone là thuốc phân loại B. An toàn trong thai kỳ. Được dùng rộng rãi cho hỗ trợ giai đoạn hoàng thể trong thụ tinh trong ống nghiệm (IVF) và dự phòng sẩy thai tái phát.""",
            "lactation": {
                "safety": "Compatible",
                "details": """Progesterone bài tiết vào sữa mẹ ở nồng độ thấp. Không có báo cáo về tác dụng phụ đáng kể ở trẻ bú mẹ.""",
                "recommendation": "Có thể dùng khi cho con bú. Nồng độ trong sữa mẹ thấp và không gây tác dụng phụ ở trẻ bú mẹ.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Thận trọng. Chuyển hóa qua gan có thể giảm, tăng nồng độ và nguy cơ tác dụng phụ.",
            "severe": "CHỐNG CHỈ ĐỊNH. Chuyển hóa qua gan giảm đáng kể, tăng nguy cơ bệnh gan và tác dụng phụ nặng.",
            "notes": """Progesterone chuyển hóa qua gan. Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và nguy cơ bệnh gan, tác dụng phụ nặng.""",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn ngủ nặng",
                "Chóng mặt nặng",
                "Chảy máu âm đạo nặng"
    ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay progesterone",
                "Nếu buồn ngủ nặng:",
                "  - Theo dõi sát",
                "  - Tránh lái xe hoặc vận hành máy móc",
                "Nếu chảy máu âm đạo nặng:",
                "  - Theo dõi lượng máu mất",
                "  - Điều trị hỗ trợ nếu cần",
                "Theo dõi: Dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần"
    ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn, lượng máu mất, tình trạng tinh thần cho đến khi hồi phục.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với thức ăn để giảm buồn nôn và tăng hấp thu.",
                "timing": "200-300mg PO x 2-3 lần/ngày. Uống đều đặn.",
                "notes": """QUAN TRỌNG: 1) Uống với thức ăn, 2) Buồn ngủ, mệt mỏi phổ biến - tránh lái xe, 3) Dùng liều thấp nhất hiệu quả.""",
            },
            "vaginal": {
                "preparation": "Gel hoặc suppository progesterone.",
                "application": "Đặt gel hoặc suppository vào âm đạo. 90-200mg gel hoặc 100-200mg suppository x 2-3 lần/ngày.",
                "notes": """QUAN TRỌNG: 1) Đường âm đạo thường được ưa chuộng cho hỗ trợ giai đoạn hoàng thể (ít tác dụng phụ toàn thân), 2) Đặt đều đặn.""",
            },
            "im": {
                "reconstitution": "Dùng dung dịch sẵn có.",
                "injection_site": "Tiêm sâu vào cơ lớn (mông, đùi).",
                "timing": "Theo phác đồ, thường 50-100mg IM mỗi ngày hoặc cách ngày.",
                "notes": "QUAN TRỌNG: 1) Tiêm đúng lịch, 2) Thường dùng cho hỗ trợ giai đoạn hoàng thể.",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Progesterone (Prometrium, Crinone)",
                "ACOG Practice Bulletin - Progesterone Supplementation",
                "ASRM (American Society for Reproductive Medicine) Guidelines",
                "UpToDate - Progesterone: Drug Information",
                "Medscape - Progesterone Drug Reference"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - Dựa trên FDA drug labels, ACOG/ASRM guidelines, và dữ liệu lâm sàng từ nhiều nguồn",
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"oncologic": "Black Box Warning - Breast cancer risk (slight increase)", "cardiovascular": "Black Box Warning - Cardiovascular events (stroke, MI, DVT, PE)", "neurological": "Black Box Warning - Dementia (in women ≥65 years)", "hepatic": "Hepatotoxicity (rare), hepatic hemangioma (rare)", "psychiatric": "Depression (may worsen)"},
            "qt_prolongation": False,
            "hepatotoxicity": "Rare",
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Breast cancer (mammography recommended)", "Black Box Warning - Cardiovascular events (DVT, PE, stroke, MI signs)", "Black Box Warning - Dementia (in women ≥65 years)", "Vaginal bleeding (abnormal bleeding)", "Mental status (depression risk)", "Hepatic function (hepatotoxicity risk)"],
            "look_alike_sound_alike": ["Progesterone", "Progesterone"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Cardiovascular Events (stroke, MI, DVT, PE)",
            "FDA Black Box Warning - Dementia (in women ≥65 years)",
            "ACOG Practice Bulletin - Progesterone Supplementation",
            "ASRM Guidelines - Luteal Phase Support",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

}

__all__ = ['HORMONE_REPLACEMENT_DRUGS']
