"""Sex Hormones - Androgens, Estrogens, Progestins"""

SEX_HORMONES_DRUGS = {
    "Testosterone": {
        "group": "Endocrinology - Androgen (Sex Hormone)",
        "vietnamese_name": "Testosterone, Testosteron",
        "administration": ["IM", "Topical", "Transdermal", "PO"],
        "indications": [
            "Suy sinh dục nam (hypogonadism)",
            "Thiếu hụt testosterone",
            "Chậm dậy thì ở nam",
            "Loãng xương ở nam (do thiếu testosterone)",
            "Thiếu máu do suy thận (kết hợp với erythropoietin)"
        ],
        "contraindications": [
            "Ung thư tuyến tiền liệt",
            "Ung thư vú ở nam",
            "Suy tim nặng",
            "Bệnh gan nặng",
            "Có thai (phụ nữ)"
        ],
        "dosage": {
            "adult_im_cypionate": "50-400mg IM mỗi 2-4 tuần",
            "adult_im_enanthate": "50-400mg IM mỗi 2-4 tuần",
            "adult_transdermal_patch": "2.5-7.5mg/ngày (patch)",
            "adult_topical_gel": "25-100mg/ngày (gel 1%)",
            "adult_po": "Không khuyến cáo (chuyển hóa nhanh ở gan)",
            "notes": "Điều chỉnh liều theo nồng độ testosterone trong máu. Mục tiêu: 400-1000 ng/dL"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Tăng huyết áp",
            "Giữ nước, phù",
            "Tăng cân",
            "Mụn trứng cá",
            "Rụng tóc (hói đầu)",
            "Tăng kích thước tuyến tiền liệt",
            "Tăng nguy cơ huyết khối",
            "Rối loạn lipid máu",
            "Ngưng thở khi ngủ",
            "Tăng nguy cơ bệnh tim mạch (còn tranh cãi)",
            "Ức chế sản xuất testosterone tự nhiên (khi ngừng)"
        ],
        "interactions": [
            "Warfarin: có thể tăng tác dụng chống đông",
            "Insulin: có thể cần điều chỉnh liều insulin",
            "Corticosteroid: tăng giữ nước"
        ],
        "pregnancy": "X - Chống chỉ định ở phụ nữ có thai",
        "mechanism_of_action": "Testosterone là hormone sinh dục nam chính (androgen), được sản xuất chủ yếu ở tinh hoàn. Testosterone gắn với androgen receptor trong tế bào, sau đó di chuyển vào nhân và gắn vào androgen response elements (ARE) trên DNA, kích hoạt biểu hiện gen. Dẫn đến: phát triển và duy trì đặc tính sinh dục nam (giọng nói trầm, râu, cơ bắp), tăng khối lượng cơ, tăng mật độ xương, tăng ham muốn tình dục, tăng sản xuất hồng cầu, và ảnh hưởng đến tâm trạng và năng lượng. Testosterone cũng được chuyển đổi thành dihydrotestosterone (DHT) bởi 5-alpha-reductase (mạnh hơn testosterone) và estradiol bởi aromatase (có thể gây nữ hóa). Được dùng để thay thế testosterone thiếu hụt trong suy sinh dục nam.",
        "monitoring": [
            "Nồng độ testosterone trong máu (mục tiêu: 400-1000 ng/dL) - kiểm tra 6-12 tuần sau khi bắt đầu hoặc điều chỉnh liều",
            "PSA (prostate-specific antigen) - mỗi 3-6 tháng (tăng nguy cơ ung thư tuyến tiền liệt)",
            "Hematocrit, hemoglobin - testosterone tăng sản xuất hồng cầu, có thể gây đa hồng cầu",
            "Lipid máu (cholesterol, triglyceride) - testosterone có thể ảnh hưởng đến lipid",
            "Huyết áp - testosterone có thể tăng huyết áp",
            "Cân nặng, dấu hiệu phù - giữ nước",
            "Dấu hiệu ung thư tuyến tiền liệt (tiểu khó, tiểu nhiều lần, tiểu máu)",
            "Dấu hiệu ung thư vú ở nam (u vú, chảy dịch núm vú)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở ung thư tuyến tiền liệt - testosterone có thể làm nặng ung thư",
            "CHỐNG CHỈ ĐỊNH ở ung thư vú ở nam - testosterone có thể làm nặng ung thư",
            "Theo dõi PSA thường xuyên (mỗi 3-6 tháng) - tăng nguy cơ ung thư tuyến tiền liệt",
            "Theo dõi hematocrit - testosterone tăng sản xuất hồng cầu, có thể gây đa hồng cầu (hematocrit >54%)",
            "Nếu hematocrit >54%: ngừng testosterone tạm thời hoặc trích máu (phlebotomy)",
            "Thận trọng ở bệnh nhân suy tim (giữ nước → phù, suy tim nặng)",
            "Thận trọng ở bệnh nhân tăng huyết áp (có thể tăng huyết áp)",
            "Thận trọng ở bệnh nhân ngưng thở khi ngủ (testosterone có thể làm nặng)",
            "Dạng uống không khuyến cáo (chuyển hóa nhanh ở gan, độc gan)",
            "Dạng IM: tiêm sâu vào cơ, thay đổi vị trí tiêm",
            "Dạng gel/transdermal: tránh tiếp xúc với phụ nữ và trẻ em (có thể hấp thu qua da)",
            "Khi ngừng: có thể ức chế sản xuất testosterone tự nhiên, cần theo dõi"
        ],
        "pharmacokinetics": {
            "half_life": "8 ngày (IM cypionate/enanthate), 2-4 giờ (PO - không dùng)",
            "onset": "2-4 tuần (IM), vài giờ (transdermal)",
            "duration": "2-4 tuần (IM), 24 giờ (transdermal)",
            "protein_binding": "98% (gắn với sex hormone-binding globulin, SHBG)",
            "metabolism": "Gan (CYP3A4) - chuyển hóa thành DHT (5-alpha-reductase) và estradiol (aromatase)",
            "clearance": "Gan (chuyển hóa), thận (bài tiết metabolites)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ánh sáng. Dạng gel/transdermal: bảo quản ở nhiệt độ phòng, tránh nhiệt độ cao.",
        "black_box_warnings": "Có thể gây ung thư tuyến tiền liệt. Có thể gây đa hồng cầu (hematocrit >54%), tăng nguy cơ huyết khối. Có thể gây tổn thương gan (dạng uống).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Testosterone có thể ảnh hưởng đến đông máu và chuyển hóa warfarin.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc điều chỉnh liều testosterone. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Insulin, Oral hypoglycemics",
                    "mechanism": "Testosterone có thể ảnh hưởng đến chuyển hóa glucose.",
                    "effect": "Có thể cần điều chỉnh liều insulin hoặc thuốc hạ đường huyết",
                    "management": "Theo dõi đường huyết khi bắt đầu hoặc điều chỉnh liều testosterone."
                },
                {
                    "drug": "Corticosteroid",
                    "mechanism": "Cả hai đều gây giữ natri và nước, tác dụng cộng dồn.",
                    "effect": "Tăng giữ nước, tăng phù, tăng huyết áp",
                    "management": "Theo dõi cân nặng, dấu hiệu phù, huyết áp. Có thể cần giảm liều một trong hai thuốc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Ung thư tuyến tiền liệt - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (testosterone có thể làm nặng ung thư)",
                "Ung thư vú ở nam - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Có thai (phụ nữ) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (có thể gây dị tật thai nhi nam)",
                "Suy tim nặng - giữ nước có thể làm nặng suy tim"
            ],
            "tương_đối": [
                "Bệnh gan nặng - testosterone chuyển hóa ở gan, có thể độc gan (đặc biệt dạng uống)",
                "Suy tim nhẹ-trung bình - thận trọng, theo dõi cân nặng và dấu hiệu phù",
                "Tăng huyết áp - thận trọng, theo dõi huyết áp",
                "Ngưng thở khi ngủ - testosterone có thể làm nặng",
                "Đa hồng cầu - testosterone tăng sản xuất hồng cầu",
                "Rối loạn lipid máu - testosterone có thể ảnh hưởng đến lipid"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Testosterone phân loại X - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI ở phụ nữ có thai. Testosterone có thể gây dị tật thai nhi nam (nữ hóa bộ phận sinh dục ngoài). Phụ nữ có thai không được dùng testosterone.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Testosterone bài tiết vào sữa mẹ. Có thể ảnh hưởng đến trẻ sơ sinh. Không dùng khi cho con bú.",
                "recommendation": "Không dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi chức năng gan",
            "moderate": "Thận trọng, có thể cần giảm liều. Theo dõi chức năng gan chặt chẽ.",
            "severe": "CHỐNG CHỈ ĐỊNH hoặc thận trọng tối đa. Testosterone chuyển hóa ở gan, có thể độc gan. Dạng uống đặc biệt nguy hiểm.",
            "notes": "Testosterone chuyển hóa chủ yếu ở gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Dạng uống đặc biệt nguy hiểm ở suy gan (độc gan). Dạng IM hoặc transdermal an toàn hơn ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng huyết áp nặng",
                "Đa hồng cầu (hematocrit >54%) - tăng nguy cơ huyết khối",
                "Phù nặng, suy tim",
                "Tăng kích thước tuyến tiền liệt, tiểu khó",
                "Mụn trứng cá nặng",
                "Rụng tóc",
                "Tổn thương gan (dạng uống)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng testosterone",
                "Nếu đa hồng cầu (hematocrit >54%): trích máu (phlebotomy) để giảm hematocrit",
                "Nếu tăng huyết áp: thuốc hạ huyết áp nếu cần",
                "Nếu phù/suy tim: lợi tiểu (furosemide), hạn chế dịch",
                "Nếu tổn thương gan: điều trị hỗ trợ gan",
                "Theo dõi PSA, hematocrit, huyết áp, chức năng gan"
            ],
            "monitoring": "Huyết áp, hematocrit, PSA, chức năng gan, cân nặng, dấu hiệu phù trong ít nhất 2-4 tuần."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A - dạng uống không khuyến cáo (chuyển hóa nhanh ở gan, độc gan)",
                "timing": "N/A - dạng uống không khuyến cáo"
            },
            "im": {
                "reconstitution": "Dùng trực tiếp từ lọ. Lắc kỹ trước khi dùng.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus, vastus lateralis). Thay đổi vị trí tiêm mỗi lần.",
                "notes": "Tiêm sâu vào cơ. Thay đổi vị trí tiêm mỗi lần để tránh teo cơ. Liều: 50-400mg IM mỗi 2-4 tuần tùy loại (cypionate, enanthate)."
            },
            "transdermal": {
                "technique": "Dán patch lên da sạch, khô (bụng, đùi, lưng). Thay patch mỗi 24 giờ. Tránh vùng có vết thương.",
                "after_use": "Rửa tay sau khi dán patch. Tránh tiếp xúc với phụ nữ và trẻ em.",
                "frequency": "Thay patch mỗi 24 giờ. Liều: 2.5-7.5mg/ngày."
            },
            "topical": {
                "technique": "Bôi gel lên da sạch, khô (cánh tay, vai, bụng). Để khô 5 phút trước khi mặc quần áo. Rửa tay sau khi bôi.",
                "after_use": "Rửa tay kỹ sau khi bôi. Tránh tiếp xúc với phụ nữ và trẻ em (có thể hấp thu qua da).",
                "frequency": "Bôi 1 lần/ngày. Liều: 25-100mg/ngày (gel 1%)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Testosterone",
                "Endocrine Society Guidelines - Testosterone Therapy in Men",
                "UpToDate - Testosterone: Drug Information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên FDA drug labels, guidelines, và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": None,
            "organ_toxicity": {"oncologic": "Black Box Warning - Prostate cancer risk", "cardiovascular": "Black Box Warning - Venous thromboembolism (DVT, PE), cardiovascular events", "hematologic": "Black Box Warning - Polycythemia (hematocrit >54%)", "hepatic": "Hepatotoxicity (especially oral form)", "cardiovascular_other": "Heart failure exacerbation (fluid retention)"},
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": ["PSA (Black Box Warning - prostate cancer risk, every 3-6 months)", "Hematocrit (Black Box Warning - polycythemia, stop if >54%)", "Black Box Warning - Venous thromboembolism signs (DVT, PE)", "Black Box Warning - Cardiovascular events", "Blood pressure (hypertension risk)", "Lipid panel (dyslipidemia risk)", "Hepatic function (hepatotoxicity risk, especially oral form)", "Testosterone levels (target 400-1000 ng/dL)"],
            "look_alike_sound_alike": ["Testosterone", "Testosterone"]
        },
        "guideline_tags": [
            "FDA Black Box Warning - Prostate Cancer Risk",
            "FDA Black Box Warning - Venous Thromboembolism (DVT, PE)",
            "FDA Black Box Warning - Cardiovascular Events",
            "FDA Black Box Warning - Polycythemia (hematocrit >54%)",
            "Endocrine Society Guidelines - Testosterone Therapy in Men",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-02-18"
    },
}

__all__ = ['SEX_HORMONES_DRUGS']
