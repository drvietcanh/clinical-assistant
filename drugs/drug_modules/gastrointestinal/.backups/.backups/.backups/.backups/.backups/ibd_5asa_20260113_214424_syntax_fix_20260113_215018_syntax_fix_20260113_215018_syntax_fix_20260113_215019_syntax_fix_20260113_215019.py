"""Gastrointestinal Drugs - 5-ASA for IBD
Mesalazine (Mesalamine) and Sulfasalazine for ulcerative colitis and Crohn's colitis"""

IBD_5ASA_DRUGS = {
    "Mesalazine": {
        "group": "Gastrointestinal - 5-ASA (Aminosalicylate)",
        "vietnamese_name": "Mesalazine (Mesalamine), Salofalk, Pentasa, Asacol",
        "administration": ["PO", "PR"],  # PR = suppository/enema
        "indications": [
            "Viêm loét đại tràng (ulcerative colitis) mức độ nhẹ đến trung bình - cảm ứng và duy trì lui bệnh",
            "Bệnh Crohn ở đại tràng (Crohn's colitis) mức độ nhẹ",
            "Phòng ngừa tái phát viêm loét đại tràng sau lui bệnh",
        ],
        "contraindications": [
            "Dị ứng mesalazine, 5-ASA, hoặc salicylates khác (aspirin)",
            "Suy thận nặng (CrCl <30 ml/phút)",
            "Suy gan nặng",
        ],
        "dosage": {
            "uc_induction_oral": "2.4–4.8 g/ngày PO chia 2–3 lần, tùy mức độ nặng và chế phẩm (giải phóng ở đại tràng/đoạn xa)",
            "uc_maintenance_oral": "1.2–2.4 g/ngày PO chia 1–2 lần",
            "uc_distal_proctitis_pr": "Suppository 500–1000 mg PR x 1–2 lần/ngày",
            "uc_left_sided_colitis_enema": "Enema 1–4 g PR x 1 lần/ngày, thường buổi tối",
            "notes": (
                "Liều và tần suất phụ thuộc chế phẩm (pH-dependent vs controlled-release). "
                "UC nhẹ–trung bình: ưu tiên phối hợp đường uống + tại chỗ (suppository/enema) nếu tổn thương đoạn xa. "
                "Duy trì: dùng liều thấp nhất còn kiểm soát được triệu chứng, thường 1.2–2.4 g/ngày."
            ),
        },
        "renal_adjustment": {
            "normal": "Không đổi, nhưng cần theo dõi creatinine định kỳ (mỗi 3–6 tháng)",
            "30_60": "Thận trọng, cân nhắc giảm liều và theo dõi chặt chức năng thận",
            "under_30": "Tránh dùng (nguy cơ độc thận tăng rõ)",
        },
        "side_effects": [
            "Đau bụng, đầy hơi",
            "Buồn nôn, nôn",
            "Đau đầu",
            "Phát ban, ngứa",
            "Tăng men gan nhẹ",
            "Độc thận kẽ (interstitial nephritis) hiếm nhưng quan trọng",
            "Giảm bạch cầu, thiếu máu tán huyết (rất hiếm, thường gặp hơn với sulfasalazine)",
        ],
        "interactions": [
            "NSAID: tăng nhẹ nguy cơ độc thận",
            "Azathioprine/6-MP: tăng nguy cơ giảm bạch cầu (cộng hưởng ức chế tủy)",
        ],
        ',
        "pregnancy": "B",
        ',
        "mechanism_of_action": (
            "Mesalazine (5-aminosalicylic acid, 5-ASA) là thuốc chống viêm tại chỗ ở niêm mạc ruột, đặc biệt là đại tràng. "
            "Cơ chế chính: ức chế tổng hợp prostaglandin và leukotriene (COX và LOX), "
            "quét gốc tự do, ức chế hoạt hóa NF-κB và sản xuất cytokine tiền viêm (TNF-α, IL-1, IL-6). "
            "Tác dụng tập trung tại lòng và niêm mạc ruột do thuốc được phóng thích chậm và ít hấp thu toàn thân. "
            "Hiệu quả cao trong viêm loét đại tràng nhẹ–trung bình, đặc biệt với tổn thương đoạn xa khi dùng dạng suppository/enema."
        ),
        "monitoring": [
            "Triệu chứng lâm sàng: đau bụng, tiêu chảy, máu trong phân, tần suất đi ngoài",
            "Công thức máu (CBC): thiếu máu, giảm bạch cầu (ít gặp nhưng cần theo dõi định kỳ)",
            "Chức năng thận (creatinin, eGFR) trước điều trị, sau 3 tháng, sau đó mỗi 6–12 tháng (nguy cơ interstitial nephritis)",
            "Men gan (ALT, AST) định kỳ",
        ],
        "precautions": [
            "Kiểm tra creatinin và eGFR trước khi bắt đầu, sau 3 tháng, rồi mỗi 6–12 tháng",
            "Ngừng thuốc nếu xuất hiện suy thận mới hoặc xấu đi không giải thích được",
            "Thận trọng ở bệnh nhân có tiền sử dị ứng aspirin/salicylate",
            "Có thể đổi sang chế phẩm khác (pH-dependent vs controlled-release) nếu không dung nạp tốt",
            "Dạng suppository/enema: hướng dẫn bệnh nhân giữ thuốc trong trực tràng/đại tràng càng lâu càng tốt (ít nhất 30–60 phút, lý tưởng qua đêm)",
        ],
        "pharmacokinetics": {
            "half_life": "5–10 giờ (tùy chế phẩm; hấp thu toàn thân hạn chế)",
            "onset": "Vài ngày đến vài tuần (cải thiện triệu chứng rõ sau 2–4 tuần)",
            "duration": "Cần dùng liên tục để duy trì lui bệnh",
            "protein_binding": "43–50%",
            "clearance": "Thận (dưới dạng không đổi và chuyển hóa), một phần qua gan (acetyl hóa thành N-acetyl-5-ASA)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15–30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Azathioprine/6-mercaptopurine",
                    "mechanism": "Cộng hưởng độc tính lên tủy xương và có thể tăng nguy cơ độc tính gan/thận.",
                    "effect": "Tăng nguy cơ giảm bạch cầu, thiếu máu, tăng men gan.",
                    "management": "Theo dõi CBC và men gan chặt khi phối hợp; điều chỉnh liều thiopurine nếu cần.",
                },
                {
                    "drug": "NSAID",
                    "mechanism": "Cộng hưởng nguy cơ độc thận.",
                    "effect": "Tăng nguy cơ suy thận cấp hoặc mạn.",
                    "management": "Hạn chế NSAID nếu có thể; nếu phải dùng, theo dõi creatinin thường xuyên.",
                },
            ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng mesalazine/5-ASA hoặc salicylates khác",
                "Suy thận nặng (CrCl <30 ml/phút)",
                "Suy gan nặng",
            ],
            "tương_đối": [
                "Tiền sử bệnh thận mạn (cần theo dõi creatinin sát sao)",
                "Tiền sử viêm tụy do 5-ASA (hiếm) – nếu tái phát phải ngừng vĩnh viễn",
            ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": (
                "Mesalazine được xem là an toàn tương đối trong thai kỳ (category B). "
                "Duy trì lui bệnh IBD trong thai kỳ quan trọng hơn nguy cơ lý thuyết từ thuốc. "
                "Thường được khuyến cáo TIẾP TỤC trong thai kỳ để tránh bùng phát IBD."
            ),
            "lactation": {
                "safety": "Compatible",
                "details": "Một lượng nhỏ mesalazine và chất chuyển hóa vào sữa mẹ; nhìn chung an toàn, nhưng hiếm khi gây tiêu chảy ở trẻ.",
                "recommendation": "Có thể cho con bú; nếu trẻ tiêu chảy kéo dài, cân nhắc đổi thuốc.",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, không cần chỉnh liều.",
            "moderate": "Thận trọng, theo dõi men gan định kỳ.",
            "severe": "Tránh dùng nếu không thật cần thiết.",
            "notes": "Phần lớn tác dụng tại chỗ ở ruột; tuy nhiên, suy gan nặng có thể ảnh hưởng chuyển hóa và tăng độc tính.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn",
                "Đau bụng, tiêu chảy",
                "Nhức đầu, chóng mặt",
                "Triệu chứng giống salicylate (rất hiếm, liều rất cao): ù tai, tăng thông khí",
            ],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, điều trị triệu chứng (bù dịch, điện giải).",
                "Cân nhắc than hoạt nếu uống liều rất lớn và đến sớm.",
                "Theo dõi chức năng thận và gan.",
            ],
            "monitoring": "Theo dõi triệu chứng, creatinin, men gan; theo dõi nước tiểu.",
        },
        "reversal_agents": {"available": False, "agents": [], "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có độc tính thận hoặc phản ứng dị ứng nghiêm trọng."},
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống cùng hoặc không cùng thức ăn; uống với nhiều nước.",
                "timing": "Chia 2–3 lần/ngày, tùy chế phẩm; uống đều mỗi ngày ngay cả khi hết triệu chứng để duy trì lui bệnh.",
            },
            "rectal": {
                "notes": "Đặt suppository hoặc bơm enema khi trực tràng/đại tràng trống (sau đi ngoài). Giữ thuốc càng lâu càng tốt, lý tưởng qua đêm.",
            },
        },
        "references": {
            "primary_sources": [
                "ACG Ulcerative Colitis Guidelines",
                "ECCO Guidelines on Inflammatory Bowel Disease",
                "UpToDate - Aminosalicylates (5-ASA) in the treatment of IBD",
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - guideline-recommended first-line therapy in mild-moderate UC",
        },
             "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},

    "Sulfasalazine":     {
        "group": "Gastrointestinal - 5-ASA (Aminosalicylate prodrug) + Sulfonamide",
        "vietnamese_name": "Sulfasalazine, Salazopyrin",
        "administration": [
            "PO"
    ],
        "indications": [
            "Viêm loét đại tràng (ulcerative colitis) mức độ nhẹ đến trung bình",
            "Bệnh Crohn ở đại tràng (Crohn's colitis) – hiệu quả kém hơn mesalazine",
            "Viêm khớp dạng thấp (dạng DMARD, ngoài tiêu hóa)"
    ],
        "contraindications": [
            "Dị ứng sulfonamide (sulfamide) hoặc salicylate",
            "Suy gan nặng",
            "Suy thận nặng",
            "Thiếu men G6PD (nguy cơ tán huyết)"
    ],
        "dosage": {
            "uc_induction": "3–4 g/ngày PO chia 3–4 lần, tăng dần trong vài ngày–tuần để giảm tác dụng phụ tiêu hóa",
            "uc_maintenance": "2 g/ngày PO chia 2–4 lần",
            "ra": "2–3 g/ngày PO chia 2–3 lần (ngoài chỉ định tiêu hóa)",
            "notes": """Bắt đầu với liều thấp (500 mg x 1–2 lần/ngày), tăng dần mỗi 3–7 ngày tới liều đích để cải thiện dung nạp. Khuyến cáo dùng cùng acid folic 1 mg/ngày (sulfasalazine giảm hấp thu folate).""",
        },
        "renal_adjustment": {
            "normal": "Không đổi, nhưng theo dõi creatinin định kỳ.",
            "30_60": "Giảm liều 25–50% và tăng khoảng cách liều; theo dõi creatinin, BUN.",
            "under_30": "Tránh dùng nếu có thể; nếu buộc phải dùng, phải theo dõi rất sát.",
        },
        "side_effects": [
            "Buồn nôn, nôn, chán ăn",
            "Đau bụng, tiêu chảy",
            "Nhức đầu, chóng mặt",
            "Phát ban, mày đay (dị ứng sulfonamide)",
            "Thiếu máu tán huyết (đặc biệt ở người thiếu G6PD)",
            "Giảm bạch cầu (leukopenia), giảm tiểu cầu (hiếm nhưng quan trọng)",
            "Tăng men gan",
            "Nước tiểu và da có thể hơi vàng/cam (vô hại)"
    ],
        "interactions": [
            "Folate/acid folic: cần bổ sung để phòng thiếu hụt do sulfasalazine giảm hấp thu folate",
            "Warfarin: có thể tăng tác dụng chống đông (gắn protein và chuyển hóa)"
    ],
        "pregnancy": "B",
        "mechanism_of_action": """Sulfasalazine là prodrug gồm sulfapyridine + 5-ASA (mesalazine) gắn với nhau qua liên kết azo. Tại đại tràng, vi khuẩn phân cắt liên kết azo → giải phóng 5-ASA (tác dụng chống viêm tại chỗ) và sulfapyridine (nhiều tác dụng phụ toàn thân). 5-ASA: ức chế COX/LOX, giảm prostaglandin/leukotriene, quét gốc tự do, ức chế NF-κB và cytokine tiền viêm. Sulfapyridine: mang đặc tính sulfonamide, liên quan đến nhiều tác dụng phụ (dị ứng, tán huyết, giảm bạch cầu).""",
        "monitoring": [
            "Công thức máu (CBC) trước điều trị, sau 2–4 tuần, rồi mỗi 3 tháng trong năm đầu, sau đó mỗi 6–12 tháng (theo dõi thiếu máu, giảm bạch cầu, giảm tiểu cầu)",
            "Chức năng gan (ALT, AST) định kỳ",
            "Chức năng thận (creatinin, eGFR)",
            "Triệu chứng lâm sàng UC: đau bụng, tiêu chảy, máu trong phân"
    ],
        "precautions": [
            "Bắt đầu liều thấp và tăng dần để giảm buồn nôn, đau bụng",
            "Bổ sung acid folic (thường 1 mg/ngày) để phòng thiếu hụt folate",
            "Sàng lọc thiếu men G6PD nếu có thể, đặc biệt ở nhóm nguy cơ cao",
            "Ngừng thuốc ngay nếu xuất hiện phát ban nặng, sốt, đau họng (nghi ngờ giảm bạch cầu hoặc hội chứng quá mẫn)",
            "Thận trọng ở người có tiền sử dị ứng sulfonamide"
    ],
        "pharmacokinetics": {
            "half_life": "7–15 giờ (tùy thành phần; sulfapyridine kéo dài hơn)",
            "onset": "Vài tuần (cải thiện UC thường sau 2–4 tuần)",
            "duration": "Hiệu quả duy trì nếu dùng đều hàng ngày",
            "protein_binding": "Rất cao đối với sulfapyridine (~90%)",
            "clearance": "Gan (acetyl hóa, hydroxyl hóa) và thận (thải trừ dưới dạng không đổi và chuyển hóa)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15–30°C), tránh ẩm, tránh ánh sáng.",
        "black_box_warnings": "Không có",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Warfarin",
                    "mechanism": "Cạnh tranh gắn protein và ảnh hưởng chuyển hóa warfarin.",
                    "effect": "Có thể tăng INR và nguy cơ chảy máu.",
                    "management": "Theo dõi INR chặt khi bắt đầu/ngừng; điều chỉnh liều warfarin nếu cần.",
                }
                ],
            "moderate": [
    {
                    "drug": "Folate/acid folic",
                    "mechanism": "Sulfasalazine giảm hấp thu folate.",
                    "effect": "Nguy cơ thiếu máu do thiếu folate nếu không bổ sung.",
                    "management": "Bổ sung acid folic thường quy (ví dụ 1 mg/ngày).",
                }
                ],
            "minor": [],
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng sulfonamide hoặc salicylate",
                "Thiếu men G6PD nặng (nguy cơ thiếu máu tán huyết)",
                "Suy gan nặng",
                "Suy thận nặng"
    ],
            "tương_đối": [
                "Tiền sử phản ứng quá mẫn với sulfonamide",
                "Thiếu folate",
                "Tiền sử bệnh máu (thiếu máu, giảm bạch cầu, giảm tiểu cầu)"
    ],
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": """Sulfasalazine nhìn chung an toàn trong thai kỳ (category B) và được sử dụng rộng rãi cho UC. Do giảm hấp thu folate, cần bổ sung acid folic liều cao hơn (ít nhất 2 mg/ngày) trước và trong thai kỳ.""",
            "lactation": {
                "safety": "",
                "details": "",
                "recommendation": "",
            },
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi men gan.",
            "moderate": "Giảm liều và theo dõi chặt; cân nhắc thuốc khác nếu men gan tăng.",
            "severe": "Tránh dùng.",
            "notes": "Sulfasalazine được chuyển hóa nhiều ở gan; suy gan làm tăng nguy cơ độc tính.",
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, đau bụng",
                "Chóng mặt, nhức đầu",
                "Triệu chứng tán huyết (đặc biệt nếu thiếu G6PD): mệt, vàng da, nước tiểu sẫm"
    ],
            "antidote": "Không có antidote đặc hiệu; điều trị hỗ trợ.",
            "treatment": [
                "Ngừng thuốc, điều trị triệu chứng.",
                "Bù dịch, điện giải.",
                "Theo dõi CBC, men gan, chức năng thận.",
                "Truyền máu nếu tán huyết nặng."
    ],
            "monitoring": "Theo dõi CBC, men gan, creatinin, dấu hiệu tán huyết.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": """Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Ngừng thuốc ngay nếu có tán huyết, độc tính thận, hoặc phản ứng dị ứng nghiêm trọng.""",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống cùng thức ăn để giảm kích ứng dạ dày và buồn nôn.",
                "timing": "Chia nhiều lần trong ngày; bắt đầu liều thấp và tăng dần mỗi vài ngày để cải thiện dung nạp.",
            },
        },
        "references": {
            "primary_sources": [
                "ACG Ulcerative Colitis Guidelines",
                "ECCO Guidelines on Inflammatory Bowel Disease",
                "UpToDate - Sulfasalazine in the treatment of IBD and RA",
                "Lexicomp - Sulfasalazine monograph"
    ],
            "last_updated": "2025-02-18",
            "evidence_level": "High - guideline-supported therapy in mild-moderate UC",
        },
    },
}

__all__ = ["IBD_5ASA_DRUGS"]


