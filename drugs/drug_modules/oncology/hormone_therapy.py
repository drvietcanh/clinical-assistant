"""Oncology Medications - Hormone Therapy
Active module - contains hormone therapy drugs for cancer treatment"""

# Hormone Therapy Drugs

HORMONE_THERAPY_DRUGS = {
    "Abiraterone": {
        "group": "Oncology - CYP17 Inhibitor (Androgen Synthesis Inhibitor)",
        "vietnamese_name": "Abiraterone, Zytiga",
        "administration": ["PO"],
        "indications": [
            "Ung thư tuyến tiền liệt (prostate cancer) - castration-resistant, metastatic",
            "Ung thư tuyến tiền liệt - castration-sensitive, metastatic"
        ],
        "contraindications": [
            "Dị ứng abiraterone",
            "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
            "Suy tim nặng - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_standard": "1000mg PO x 1 lần/ngày (với prednisone 5mg PO x 2 lần/ngày)",
            "notes": "Uống khi đói (1 giờ trước hoặc 2 giờ sau bữa ăn). PHẢI dùng kèm prednisone để giảm tác dụng phụ."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Giữ nước, phù - phổ biến",
            "Tăng huyết áp - phổ biến",
            "Hạ kali máu (hypokalemia) - phổ biến, có thể nặng",
            "Độc tim (suy tim, rối loạn nhịp) - phổ biến, NGUY HIỂM",
            "Tăng men gan (ALT, AST) - phổ biến",
            "Mệt mỏi - phổ biến"
        ],
        "interactions": [
            "CYP3A4 inhibitors: tăng nồng độ abiraterone",
            "CYP3A4 inducers: giảm nồng độ abiraterone",
            "Thức ăn: tăng hấp thu 10 lần - PHẢI uống khi đói"
        ],
        "pregnancy": "Không áp dụng (chỉ dùng cho nam giới)",
        "mechanism_of_action": "Abiraterone là CYP17 inhibitor, ức chế enzyme CYP17 trong tuyến thượng thận và tế bào ung thư tuyến tiền liệt. CYP17 chuyển đổi pregnenolone/progesterone thành DHEA/androstenedione → testosterone/DHT. Ức chế CYP17 → ngăn chặn tổng hợp androgen → giảm testosterone và DHT → giảm tăng sinh tế bào ung thư tuyến tiền liệt.",
        "monitoring": [
            "Chức năng tim (LVEF) - QUAN TRỌNG, trước điều trị và mỗi 3 tháng",
            "Kali máu - QUAN TRỌNG, trước điều trị và mỗi 2 tuần trong 3 tháng đầu",
            "Huyết áp - mỗi chu kỳ",
            "Chức năng gan (ALT, AST) - trước điều trị và mỗi 2 tuần trong 3 tháng đầu",
            "PSA - đánh giá đáp ứng điều trị"
        ],
        "precautions": [
            "ĐỘC TIM - phổ biến, NGUY HIỂM - theo dõi chức năng tim chặt chẽ",
            "HẠ KALI MÁU - phổ biến, có thể nặng - theo dõi kali máu chặt chẽ",
            "PHẢI DÙNG KÈM PREDNISONE - để giảm tác dụng phụ",
            "UỐNG KHI ĐÓI - QUAN TRỌNG (thức ăn tăng hấp thu 10 lần)",
            "CHỐNG CHỈ ĐỊNH ở suy gan nặng và suy tim nặng"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "Vài tuần đến vài tháng",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": "99%",
            "metabolism": "Gan (CYP3A4, SULT2A1)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "ĐỘC TIM - phổ biến và NGUY HIỂM. HẠ KALI MÁU - phổ biến và có thể nặng. TĂNG MEN GAN - phổ biến. CHỐNG CHỈ ĐỊNH ở suy gan nặng và suy tim nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ abiraterone",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều abiraterone 50%."
                },
                {
                    "drug": "Thức ăn",
                    "mechanism": "Tăng hấp thu abiraterone 10 lần",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "PHẢI uống khi đói (1 giờ trước hoặc 2 giờ sau bữa ăn)."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng abiraterone",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH",
                "Suy tim nặng - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Suy tim trung bình - tăng nguy cơ độc tim",
                "Hạ kali máu nền - tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "Không áp dụng",
            "pregnancy_details": "Abiraterone chỉ dùng cho nam giới. Không áp dụng cho phụ nữ có thai.",
            "lactation": {
                "safety": "Không áp dụng",
                "details": "Abiraterone chỉ dùng cho nam giới. Không áp dụng cho phụ nữ cho con bú.",
                "recommendation": "Không áp dụng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH",
            "notes": "Abiraterone chuyển hóa qua gan. CHỐNG CHỈ ĐỊNH ở suy gan nặng."
        },
        "overdose_management": {
            "symptoms": [
                "Độc tim nặng",
                "Hạ kali máu nặng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay abiraterone",
                "Điều trị suy tim nếu có",
                "Bổ sung kali nếu hạ kali máu nặng",
                "Supportive care"
            ],
            "monitoring": "Chức năng tim, kali máu, chức năng gan"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống khi đói (1 giờ trước hoặc 2 giờ sau bữa ăn). QUAN TRỌNG: thức ăn tăng hấp thu 10 lần.",
                "timing": "1000mg PO x 1 lần/ngày (với prednisone 5mg PO x 2 lần/ngày).",
                "notes": "QUAN TRỌNG: 1) Uống khi đói, 2) PHẢI dùng kèm prednisone, 3) Độc tim - phổ biến, NGUY HIỂM, 4) Hạ kali máu - phổ biến, có thể nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Abiraterone (Zytiga)",
                "UpToDate - Abiraterone: Drug Information",
                "NCCN Guidelines - Prostate Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, effective for castration-resistant prostate cancer"
        }
    },

    "Anastrozole": {
        "group": "Oncology - Aromatase Inhibitor",
        "vietnamese_name": "Anastrozole, Arimidex",
        "administration": ["PO"],
        "indications": [
            "Ung thư vú (breast cancer) - ER-positive, postmenopausal, adjuvant và metastatic"
        ],
        "contraindications": [
            "Dị ứng anastrozole",
            "Phụ nữ premenopausal - CHỐNG CHỈ ĐỊNH (không hiệu quả)",
            "Có thai - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_adjuvant": "1mg PO x 1 lần/ngày (5-10 năm)",
            "adult_metastatic": "1mg PO x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. CHỈ dùng cho phụ nữ postmenopausal."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Bốc hỏa - phổ biến",
            "Đau khớp, đau cơ - phổ biến",
            "Loãng xương (osteoporosis) - phổ biến, NGUY HIỂM",
            "Gãy xương - phổ biến, NGUY HIỂM",
            "Tăng cholesterol - phổ biến",
            "Mệt mỏi - phổ biến"
        ],
        "interactions": [
            "Estrogen: đối kháng tác dụng",
            "Tamoxifen: giảm nồng độ anastrozole"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Anastrozole là aromatase inhibitor, ức chế enzyme aromatase chuyển đổi androgen thành estrogen. Ở phụ nữ postmenopausal, estrogen chủ yếu được sản xuất từ androgen qua aromatase. Ức chế aromatase → giảm estrogen → giảm tăng sinh tế bào ung thư vú ER-positive.",
        "monitoring": [
            "Mật độ xương (BMD) - QUAN TRỌNG, đo trước điều trị và mỗi 1-2 năm",
            "Dấu hiệu gãy xương",
            "Lipid profile (cholesterol) - mỗi 6-12 tháng",
            "Xác nhận postmenopausal status trước điều trị"
        ],
        "precautions": [
            "LOÃNG XƯƠNG - phổ biến, NGUY HIỂM - đo BMD định kỳ, bổ sung calcium và vitamin D",
            "CHỈ DÙNG CHO PHỤ NỮ POSTMENOPAUSAL - không hiệu quả ở premenopausal",
            "TRÁNH DÙNG với estrogen và tamoxifen"
        ],
        "pharmacokinetics": {
            "half_life": "50 giờ",
            "onset": "Vài tuần đến vài tháng",
            "duration": "Dài (dùng hàng ngày, 5-10 năm)",
            "protein_binding": "40%",
            "metabolism": "Gan",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "LOÃNG XƯƠNG - phổ biến và NGUY HIỂM. Đo BMD trước điều trị và mỗi 1-2 năm. Bổ sung calcium và vitamin D. CHỈ DÙNG CHO PHỤ NỮ POSTMENOPAUSAL.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Estrogen (HRT)",
                    "mechanism": "Đối kháng tác dụng anastrozole",
                    "effect": "Giảm hiệu quả điều trị",
                    "management": "TRÁNH DÙNG estrogen."
                },
                {
                    "drug": "Tamoxifen",
                    "mechanism": "Giảm nồng độ anastrozole",
                    "effect": "Giảm hiệu quả",
                    "management": "TRÁNH DÙNG đồng thời."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng anastrozole",
                "Phụ nữ premenopausal - CHỐNG CHỈ ĐỊNH",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)"
            ],
            "tương_đối": [
                "Loãng xương nặng - tăng nguy cơ gãy xương"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Anastrozole phân loại D - chống chỉ định trong thai kỳ. CHỈ dùng cho phụ nữ postmenopausal.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Anastrozole bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Anastrozole chuyển hóa qua gan. Suy gan có thể làm tăng nồng độ và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Loãng xương nặng",
                "Gãy xương",
                "Tăng cholesterol nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay anastrozole",
                "Điều trị loãng xương: bổ sung calcium và vitamin D, bisphosphonate",
                "Điều trị gãy xương: phẫu thuật nếu cần"
            ],
            "monitoring": "BMD, dấu hiệu gãy xương, lipid profile"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn.",
                "timing": "1mg PO x 1 lần/ngày. Dùng 5-10 năm trong adjuvant therapy.",
                "notes": "QUAN TRỌNG: 1) CHỈ dùng cho phụ nữ postmenopausal, 2) Loãng xương - phổ biến, NGUY HIỂM, 3) Đo BMD định kỳ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Anastrozole (Arimidex)",
                "UpToDate - Anastrozole: Drug Information",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, effective for ER-positive postmenopausal breast cancer"
        }
    },

    "Enzalutamide": {
        "group": "Oncology - Androgen Receptor Antagonist",
        "vietnamese_name": "Enzalutamide, Xtandi",
        "administration": ["PO"],
        "indications": [
            "Ung thư tuyến tiền liệt (prostate cancer) - castration-resistant, metastatic",
            "Ung thư tuyến tiền liệt - castration-resistant, non-metastatic"
        ],
        "contraindications": [
            "Dị ứng enzalutamide",
            "Co giật không kiểm soát - CHỐNG CHỈ ĐỊNH"
        ],
        "dosage": {
            "adult_standard": "160mg PO x 1 lần/ngày",
            "notes": "Uống với hoặc không thức ăn. Enzalutamide là androgen receptor antagonist."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh",
            "under_30": "Thận trọng"
        },
        "side_effects": [
            "Mệt mỏi - phổ biến",
            "Co giật (seizures) - phổ biến, NGUY HIỂM",
            "Đau đầu - phổ biến",
            "Chóng mặt - phổ biến",
            "Tăng huyết áp - phổ biến",
            "Độc tim - hiếm nhưng NGUY HIỂM",
            "Rối loạn nhịp tim - phổ biến"
        ],
        "interactions": [
            "CYP2C8 inhibitors: tăng nồng độ enzalutamide",
            "Warfarin: tăng nguy cơ chảy máu - theo dõi INR"
        ],
        "pregnancy": "X - Chống chỉ định",
        "mechanism_of_action": "Enzalutamide là androgen receptor antagonist. Gắn với androgen receptor → ngăn chặn androgen gắn với receptor → ức chế kích hoạt AR → ngăn chặn tín hiệu tăng sinh → giảm tăng sinh tế bào ung thư tuyến tiền liệt.",
        "monitoring": [
            "Co giật - QUAN TRỌNG (phổ biến, NGUY HIỂM)",
            "Chức năng tim - theo dõi định kỳ",
            "Huyết áp - mỗi chu kỳ",
            "ECG - theo dõi định kỳ",
            "INR nếu dùng với warfarin",
            "PSA - đánh giá đáp ứng điều trị"
        ],
        "precautions": [
            "CO GIẬT - phổ biến, NGUY HIỂM - CHỐNG CHỈ ĐỊNH ở co giật không kiểm soát",
            "Độc tim - hiếm nhưng NGUY HIỂM",
            "Tương tác với warfarin (theo dõi INR)",
            "Không lái xe nếu có chóng mặt hoặc co giật"
        ],
        "pharmacokinetics": {
            "half_life": "5.8 ngày (rất dài)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "Dài (dùng hàng ngày)",
            "protein_binding": "97-98%",
            "metabolism": "Gan (CYP2C8, CYP3A4)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "CO GIẬT - phổ biến và NGUY HIỂM. CHỐNG CHỈ ĐỊNH ở co giật không kiểm soát. Không lái xe nếu có co giật.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP2C8 Inhibitors (Gemfibrozil)",
                    "mechanism": "Ức chế CYP2C8, tăng nồng độ enzalutamide",
                    "effect": "Tăng nguy cơ tác dụng phụ",
                    "management": "Thận trọng. Có thể cần giảm liều enzalutamide."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tăng tác dụng chống đông",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng enzalutamide",
                "Co giật không kiểm soát - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Tiền sử co giật - tăng nguy cơ",
                "Bệnh tim - tăng nguy cơ độc tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Enzalutamide phân loại X - chống chỉ định tuyệt đối. Chỉ dùng cho nam giới.",
            "lactation": {
                "safety": "Không áp dụng",
                "details": "Enzalutamide chỉ dùng cho nam giới.",
                "recommendation": "Không áp dụng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Enzalutamide chuyển hóa qua gan. Suy gan có thể làm tăng nồng độ và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Co giật nặng",
                "Độc tim nặng",
                "Tăng huyết áp nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay enzalutamide",
                "Điều trị co giật: benzodiazepine, phenytoin",
                "Điều trị suy tim nếu có",
                "Supportive care"
            ],
            "monitoring": "Dấu hiệu co giật, chức năng tim, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn.",
                "timing": "160mg PO x 1 lần/ngày.",
                "notes": "QUAN TRỌNG: 1) Co giật - phổ biến, NGUY HIỂM, 2) CHỐNG CHỈ ĐỊNH ở co giật không kiểm soát, 3) Không lái xe nếu có co giật."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Enzalutamide (Xtandi)",
                "UpToDate - Enzalutamide: Drug Information",
                "NCCN Guidelines - Prostate Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, effective for castration-resistant prostate cancer"
        }
    },
    "Tamoxifen": {
        "group": "Oncology - Selective Estrogen Receptor Modulator (SERM)",
        "vietnamese_name": "Tamoxifen, Nolvadex",
        "administration": ["PO"],
        "indications": [
            "Ung thư vú (breast cancer) - ER-positive, adjuvant và metastatic",
            "Phòng ngừa ung thư vú ở phụ nữ có nguy cơ cao",
            "Ung thư vú ở nam giới (ER-positive)"
        ],
        "contraindications": [
            "Dị ứng tamoxifen hoặc bất kỳ thành phần nào",
            "Có thai - CHỐNG CHỈ ĐỊNH",
            "Đang cho con bú - CHỐNG CHỈ ĐỊNH",
            "Huyết khối tĩnh mạch sâu (DVT) hoặc thuyên tắc phổi (PE) đang hoạt động"
        ],
        "dosage": {
            "adult_adjuvant": "20mg PO x 1 lần/ngày (5-10 năm)",
            "adult_metastatic": "20-40mg PO x 1 lần/ngày",
            "adult_prevention": "20mg PO x 1 lần/ngày (5 năm)",
            "notes": "Uống với hoặc không thức ăn. Tamoxifen là SERM, ức chế estrogen receptor trong mô vú nhưng có tác dụng giống estrogen ở xương và tử cung."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Bốc hỏa (hot flashes) - phổ biến",
            "Đổ mồ hôi đêm - phổ biến",
            "Khô âm đạo - phổ biến",
            "Tăng nguy cơ huyết khối tĩnh mạch (DVT, PE) - phổ biến, NGUY HIỂM",
            "Tăng nguy cơ ung thư nội mạc tử cung (endometrial cancer) - phổ biến, NGUY HIỂM",
            "Đột quỵ - hiếm nhưng NGUY HIỂM",
            "Đục thủy tinh thể - phổ biến",
            "Tăng triglyceride - phổ biến",
            "Mệt mỏi - phổ biến",
            "Trầm cảm - phổ biến"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu - theo dõi INR",
            "CYP2D6 inhibitors (paroxetine, fluoxetine): giảm hiệu quả tamoxifen",
            "Estrogen: đối kháng tác dụng tamoxifen"
        ],
        "pregnancy": "D",
        "mechanism_of_action": "Tamoxifen là selective estrogen receptor modulator (SERM). Tamoxifen gắn với estrogen receptor (ER) trong mô vú → ngăn chặn estrogen gắn với ER → ức chế tín hiệu estrogen → giảm tăng sinh tế bào ung thư vú ER-positive. Tuy nhiên, tamoxifen có tác dụng khác nhau ở các mô khác: (1) Mô vú: ức chế estrogen (antagonist), (2) Xương: tác dụng giống estrogen (agonist) - bảo vệ xương, (3) Tử cung: tác dụng giống estrogen (agonist) - tăng nguy cơ ung thư nội mạc tử cung, (4) Gan: tác dụng giống estrogen (agonist) - tăng nguy cơ huyết khối. Tamoxifen được chuyển hóa thành endoxifen (chất hoạt động) bởi CYP2D6.",
        "monitoring": [
            "Khám phụ khoa và siêu âm tử cung mỗi năm - QUAN TRỌNG (tăng nguy cơ ung thư nội mạc tử cung)",
            "Dấu hiệu huyết khối tĩnh mạch (đau chân, sưng chân, khó thở, đau ngực) - QUAN TRỌNG",
            "Dấu hiệu đột quỵ (yếu nửa người, nói khó, nhìn mờ) - hiếm nhưng NGUY HIỂM",
            "Dấu hiệu xuất huyết âm đạo bất thường - cần đánh giá ngay",
            "Khám mắt định kỳ (đục thủy tinh thể) - mỗi 1-2 năm",
            "Lipid profile (triglyceride) - mỗi 6-12 tháng",
            "INR nếu dùng với warfarin"
        ],
        "precautions": [
            "TĂNG NGUY CƠ HUYẾT KHỐI TĨNH MẠCH (DVT, PE) - phổ biến, NGUY HIỂM - ngừng ngay nếu có dấu hiệu",
            "TĂNG NGUY CƠ UNG THƯ NỘI MẠC TỬ CUNG - phổ biến, NGUY HIỂM - khám phụ khoa và siêu âm tử cung mỗi năm",
            "Tương tác với CYP2D6 inhibitors (paroxetine, fluoxetine) - giảm hiệu quả tamoxifen, tránh dùng",
            "Tương tác với warfarin (tăng nguy cơ chảy máu - theo dõi INR)",
            "Dùng 5-10 năm trong adjuvant therapy"
        ],
        "pharmacokinetics": {
            "half_life": "5-7 ngày (rất dài)",
            "onset": "Vài tuần đến vài tháng",
            "duration": "Dài (dùng hàng ngày, 5-10 năm)",
            "protein_binding": "99%",
            "metabolism": "Gan (CYP2D6 → endoxifen, CYP3A4, CYP2C9, CYP2C19)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "TĂNG NGUY CƠ HUYẾT KHỐI TĨNH MẠCH (DVT, PE) - phổ biến và NGUY HIỂM. TĂNG NGUY CƠ UNG THƯ NỘI MẠC TỬ CUNG - phổ biến và NGUY HIỂM. Khám phụ khoa và siêu âm tử cung mỗi năm.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tamoxifen ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "CYP2D6 Inhibitors (Paroxetine, Fluoxetine)",
                    "mechanism": "Ức chế CYP2D6, giảm chuyển hóa tamoxifen thành endoxifen",
                    "effect": "Giảm hiệu quả điều trị tamoxifen",
                    "management": "TRÁNH DÙNG với CYP2D6 inhibitors mạnh. Xem xét chuyển sang aromatase inhibitor."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng tamoxifen",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)",
                "Đang cho con bú - CHỐNG CHỈ ĐỊNH",
                "Huyết khối tĩnh mạch đang hoạt động - CHỐNG CHỈ ĐỊNH"
            ],
            "tương_đối": [
                "Tiền sử huyết khối tĩnh mạch - tăng nguy cơ",
                "Tiền sử ung thư nội mạc tử cung - tăng nguy cơ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Tamoxifen phân loại D - chống chỉ định trong thai kỳ. Gây dị tật thai nhi. Phụ nữ PHẢI dùng biện pháp tránh thai hiệu quả.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Tamoxifen bài tiết vào sữa mẹ. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Tamoxifen chuyển hóa qua gan. Suy gan có thể làm tăng nồng độ và độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Huyết khối tĩnh mạch nặng",
                "Xuất huyết âm đạo nặng",
                "Đột quỵ"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay tamoxifen",
                "Điều trị huyết khối: thuốc chống đông",
                "Đánh giá phụ khoa nếu xuất huyết âm đạo",
                "Điều trị đột quỵ theo phác đồ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, dấu hiệu huyết khối, dấu hiệu xuất huyết, dấu hiệu đột quỵ"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không thức ăn.",
                "timing": "20mg PO x 1 lần/ngày. Dùng 5-10 năm trong adjuvant therapy.",
                "notes": "QUAN TRỌNG: 1) Tăng nguy cơ huyết khối tĩnh mạch và ung thư nội mạc tử cung, 2) Khám phụ khoa mỗi năm, 3) Tương tác với CYP2D6 inhibitors (tránh dùng)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Tamoxifen (Nolvadex)",
                "UpToDate - Tamoxifen: Drug Information",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, revolutionized ER-positive breast cancer treatment"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": "High (with warfarin)",
            "organ_toxicity": {"oncologic": "Black Box Warning - Uterine malignancy (endometrial cancer)", "cardiovascular": "Black Box Warning - Thromboembolic events (DVT, PE, stroke)", "ophthalmic": "Cataracts (common)", "metabolic": "Hypertriglyceridemia", "psychiatric": "Depression (common)"},
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Black Box Warning - Uterine malignancy (gynecologic exam and ultrasound annually)", "Black Box Warning - Thromboembolic events (DVT, PE, stroke signs)", "Vaginal bleeding (abnormal bleeding - evaluate immediately)", "Ophthalmic exam (cataracts, every 1-2 years)", "Lipid panel (triglycerides, every 6-12 months)", "PT/INR (if used with warfarin)", "CYP2D6 inhibitors (avoid - reduces efficacy)"],
            "look_alike_sound_alike": ["Tamoxifen", "Toremifene"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Uterine Malignancy (endometrial cancer)",
            "FDA Black Box Warning - Thromboembolic Events (DVT, PE, stroke)",
            "NCCN Guidelines - Breast Cancer",
            "ASCO Guidelines - Breast Cancer",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },

}

__all__ = ['HORMONE_THERAPY_DRUGS']
