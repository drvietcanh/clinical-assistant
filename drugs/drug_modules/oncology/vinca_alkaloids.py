"""Oncology Medications - Vinca Alkaloids
Active module - contains vinca alkaloid chemotherapy drugs"""

# Vinca Alkaloids

VINCA_ALKALOIDS_DRUGS = {
    "Vincristine": {
        "group": "Oncology - Vinca Alkaloid",
        "vietnamese_name": "Vincristine, Oncovin",
        "administration": ["IV"],
        "indications": [
            "Bệnh bạch cầu cấp (acute leukemia)",
            "U lympho (lymphoma)",
            "Ung thư tế bào nhỏ phổi (small cell lung cancer)",
            "Sarcoma mô mềm",
            "U nguyên bào thần kinh (neuroblastoma)",
            "U Wilms (Wilms tumor)"
        ],
        "contraindications": [
            "Dị ứng vincristine hoặc bất kỳ thành phần nào",
            "Độc thần kinh ngoại biên nặng đang hoạt động",
            "Bệnh Charcot-Marie-Tooth",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "1.4mg/m² IV (tối đa 2mg) mỗi tuần",
            "adult_weekly": "1.4mg/m² IV mỗi tuần",
            "pediatric": "1.5-2mg/m² IV mỗi tuần (tối đa 2mg)",
            "notes": "Truyền tĩnh mạch trong 1 phút. KHÔNG được truyền vào tủy sống (intrathecal) - GÂY TỬ VONG. Vincristine có độc tính thần kinh ngoại biên rất cao."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không cần điều chỉnh đáng kể",
            "under_30": "Thận trọng, không cần điều chỉnh liều"
        },
        "side_effects": [
            "Độc thần kinh ngoại biên (tê bì, dị cảm, yếu cơ) - RẤT PHỔ BIẾN, tích lũy, có thể không hồi phục",
            "Táo bón (có thể nặng, liệt ruột) - phổ biến",
            "Độc thần kinh tự chủ (hạ huyết áp, bí tiểu) - phổ biến",
            "Rụng tóc - phổ biến",
            "Hội chứng SIADH (hạ natri máu) - hiếm",
            "Co giật - hiếm",
            "Giảm bạch cầu, tiểu cầu (myelosuppression) - ít hơn các thuốc khác",
            "Buồn nôn, nôn - nhẹ đến trung bình"
        ],
        "interactions": [
            "L-asparaginase: tăng độc tính thần kinh (dùng vincristine trước L-asparaginase)",
            "Azole antifungals (itraconazole, fluconazole): tăng độc tính thần kinh",
            "CYP3A4 inhibitors: tăng nồng độ vincristine",
            "CYP3A4 inducers: giảm nồng độ vincristine"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Vincristine là vinca alkaloid, ức chế quá trình phân chia tế bào (mitosis) bằng cách gắn với tubulin, ngăn cản quá trình polymer hóa tubulin thành microtubules. Microtubules là cấu trúc quan trọng cho quá trình phân chia tế bào (spindle formation), vận chuyển nội bào, và duy trì hình dạng tế bào. Bằng cách ức chế hình thành microtubules, vincristine ngăn chặn quá trình phân chia tế bào ở giai đoạn metaphase, dẫn đến chết tế bào. Vincristine tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. ĐẶC ĐIỂM: (1) Vinca alkaloid, ức chế mitosis, (2) Độc thần kinh ngoại biên - RẤT PHỔ BIẾN, tích lũy, có thể không hồi phục, (3) Táo bón - phổ biến, có thể nặng (liệt ruột), (4) KHÔNG được truyền vào tủy sống (intrathecal) - GÂY TỬ VONG, (5) Myelosuppression ít hơn các thuốc khác, (6) Tương tác với L-asparaginase và azole antifungals.",
        "monitoring": [
            "Độc thần kinh ngoại biên - QUAN TRỌNG (tê bì, dị cảm tay chân, yếu cơ) - RẤT PHỔ BIẾN, tích lũy",
            "Táo bón - phổ biến, có thể nặng (liệt ruột) - theo dõi sát",
            "Độc thần kinh tự chủ (hạ huyết áp, bí tiểu) - phổ biến",
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ (myelosuppression ít hơn các thuốc khác)",
            "Chức năng gan (ALT, AST) trước và trong điều trị",
            "Natri máu (hội chứng SIADH - hiếm)",
            "Dấu hiệu co giật - hiếm"
        ],
        "precautions": [
            "ĐỘC THẦN KINH NGOẠI BIÊN - RẤT PHỔ BIẾN, tích lũy, có thể không hồi phục - giảm liều hoặc ngừng nếu nặng",
            "TÁO BÓN - phổ biến, có thể nặng (liệt ruột) - dùng thuốc nhuận tràng dự phòng, theo dõi sát",
            "KHÔNG ĐƯỢC TRUYỀN VÀO TỦY SỐNG (INTRATHECAL) - GÂY TỬ VONG - dán nhãn rõ ràng, để riêng",
            "Tương tác với L-asparaginase (tăng độc tính thần kinh - dùng vincristine trước L-asparaginase)",
            "Tương tác với azole antifungals (tăng độc tính thần kinh)",
            "Tương tác với CYP3A4 inhibitors/inducers (ảnh hưởng nồng độ vincristine)",
            "Myelosuppression ít hơn các thuốc khác (ưu điểm)",
            "Theo dõi natri máu (hội chứng SIADH - hiếm)"
        ],
        "pharmacokinetics": {
            "half_life": "85 giờ (rất dài)",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Dài (tích lũy)",
            "protein_binding": "75%",
            "metabolism": "Gan (CYP3A4)",
            "clearance": "Gan (chủ yếu), thận (một phần)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: bảo quản ở nhiệt độ phòng, dùng trong 24 giờ.",
        "black_box_warnings": "KHÔNG ĐƯỢC TRUYỀN VÀO TỦY SỐNG (INTRATHECAL) - GÂY TỬ VONG. Độc thần kinh ngoại biên RẤT PHỔ BIẾN, tích lũy, có thể không hồi phục. Táo bón phổ biến, có thể nặng (liệt ruột).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "L-asparaginase",
                    "mechanism": "L-asparaginase làm giảm clearance vincristine, tăng nồng độ và độc tính",
                    "effect": "Tăng độc tính thần kinh ngoại biên nghiêm trọng",
                    "management": "Dùng vincristine trước L-asparaginase (ít nhất 12-24 giờ). Theo dõi độc thần kinh chặt chẽ."
                },
                {
                    "drug": "Azole Antifungals (Itraconazole, Fluconazole, Voriconazole)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ vincristine",
                    "effect": "Tăng nồng độ vincristine, tăng độc tính thần kinh",
                    "management": "Thận trọng. Có thể cần giảm liều vincristine. Theo dõi độc thần kinh chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 Inhibitors (Ketoconazole, Ritonavir, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ vincristine",
                    "effect": "Tăng nồng độ vincristine, tăng độc tính",
                    "management": "Thận trọng. Có thể cần giảm liều vincristine."
                },
                {
                    "drug": "CYP3A4 Inducers (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, giảm nồng độ vincristine",
                    "effect": "Giảm nồng độ vincristine, giảm hiệu quả",
                    "management": "Thận trọng. Có thể cần tăng liều vincristine."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng vincristine hoặc bất kỳ thành phần nào",
                "Có thai - CHỐNG CHỈ ĐỊNH (category D)",
                "Đang cho con bú - CHỐNG CHỈ ĐỊNH",
                "Độc thần kinh ngoại biên nặng đang hoạt động - trì hoãn điều trị",
                "Bệnh Charcot-Marie-Tooth - CHỐNG CHỈ ĐỊNH (tăng nguy cơ độc thần kinh nặng)"
            ],
            "tương_đối": [
                "Độc thần kinh ngoại biên trung bình - giảm liều hoặc trì hoãn",
                "Suy gan nặng - thận trọng (chuyển hóa qua gan)",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc thần kinh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Vincristine phân loại D - chống chỉ định trong thai kỳ. Vincristine gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Vincristine bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng vincristine. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều 25%",
            "severe": "Thận trọng, giảm liều 50%",
            "notes": "Vincristine chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Độc thần kinh ngoại biên nặng (tê bì, dị cảm, yếu cơ, liệt)",
                "Táo bón nặng, liệt ruột",
                "Độc thần kinh tự chủ nặng (hạ huyết áp, bí tiểu)",
                "Hội chứng SIADH (hạ natri máu)",
                "Co giật",
                "Giảm bạch cầu, tiểu cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay vincristine",
                "Điều trị táo bón/liệt ruột: thuốc nhuận tràng, thụt tháo, có thể cần giải phóng ruột",
                "Điều trị hạ huyết áp: truyền dịch, vasopressor nếu cần",
                "Điều trị bí tiểu: đặt ống thông tiểu nếu cần",
                "Điều trị hạ natri máu (SIADH): hạn chế nước, có thể cần hypertonic saline nếu nặng",
                "Điều trị co giật: benzodiazepine, phenytoin nếu cần",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng gan, natri máu"
            ],
            "monitoring": "CBC, chức năng gan, natri máu, dấu hiệu độc thần kinh, dấu hiệu táo bón/liệt ruột, dấu hiệu hạ huyết áp, dấu hiệu bí tiểu, dấu hiệu co giật"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W. Nồng độ cuối: 0.01-1mg/ml. KHÔNG được truyền vào tủy sống (intrathecal) - GÂY TỬ VONG.",
                "infusion_rate": "Truyền tĩnh mạch trong 1 phút. KHÔNG được truyền vào tủy sống (intrathecal) - GÂY TỬ VONG.",
                "compatibility": ["NS", "D5W"],
                "incompatibility": ["Không pha với các thuốc khác"],
                "notes": "QUAN TRỌNG: 1) KHÔNG ĐƯỢC TRUYỀN VÀO TỦY SỐNG (INTRATHECAL) - GÂY TỬ VONG, 2) Dán nhãn rõ ràng, để riêng, 3) Độc thần kinh ngoại biên - RẤT PHỔ BIẾN, 4) Táo bón - phổ biến, dùng thuốc nhuận tràng dự phòng, 5) Tương tác với L-asparaginase và azole antifungals."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vincristine (Oncovin)",
                "UpToDate - Vincristine: Drug Information",
                "NCCN Guidelines - Leukemia, Lymphoma",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - FDA-approved, extensive clinical data, widely used"
        }
    },
}

__all__ = ['VINCA_ALKALOIDS_DRUGS']

