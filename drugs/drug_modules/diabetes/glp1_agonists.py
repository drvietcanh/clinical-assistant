"""
GLP-1 Receptor Agonists (Thuốc chủ vận thụ thể GLP-1)
Nhóm thuốc tiêm cho đái tháo đường type 2, có lợi ích giảm cân và tim mạch.
"""

GLP1_AGONISTS_DRUGS = {
    "Liraglutide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Liraglutide, Victoza, Saxenda",
        "brand_names": {
            "common": [
                "Victoza (ĐTĐ)",
                "Saxenda (Giảm cân)"
    ],
            "vietnam": [
                "Victoza 6mg/ml"
    ],
        },
        "administration": [
            "SC (Tiêm dưới da)"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm cân (Saxenda 3mg) - Chỉ định riêng",
            "Giảm nguy cơ biến cố tim mạch ở bệnh nhân đái tháo đường type 2 có bệnh tim mạch"
    ],
        "contraindications": [
            "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
            "Tiền sử viêm tụy cấp",
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường"
    ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với liraglutide hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        },
        "dosage": {
            "dm_t2": """Khởi đầu 0.6mg SC x 1 lần/ngày x 1 tuần, sau đó tăng lên 1.2mg x 1 lần/ngày. Có thể tăng lên 1.8mg nếu cần.""",
            "weight_loss": "Saxenda: Khởi đầu 0.6mg, tăng dần mỗi tuần đến 3mg x 1 lần/ngày.",
            "notes": "Tiêm dưới da (bụng, đùi, cánh tay) mỗi ngày, cùng giờ. Tăng liều từ từ để giảm buồn nôn.",
        },
        "side_effects": [
            "Buồn nôn, nôn (Rất phổ biến ~40%, giảm dần sau vài tuần)",
            "Tiêu chảy",
            "Táo bón",
            "Đau bụng",
            "Giảm cân (Tác dụng mong muốn, ~3-5kg)",
            "Viêm tụy cấp (Hiếm nhưng nghiêm trọng)",
            "Tăng nhịp tim nhẹ"
    ],
        "interactions": [
            "Insulin, Sulfonylurea: Tăng nguy cơ hạ đường huyết (cần giảm liều).",
            "Thuốc uống: Làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống."
    ],
        "mechanism_of_action": """Chủ vận thụ thể GLP-1 (Glucagon-Like Peptide-1): Tăng tiết insulin phụ thuộc glucose, giảm tiết glucagon, làm chậm làm rỗng dạ dày, tăng cảm giác no → Giảm đường huyết và giảm cân. Lợi ích tim mạch: Giảm biến cố tim mạch lớn (LEADER trial).""",
        "monitoring": [
            "Đường huyết (HbA1c, glucose máu)",
            "Cân nặng (giảm cân là tác dụng mong muốn)",
            "Dấu hiệu viêm tụy (đau bụng dữ dội, buồn nôn, nôn)",
            "Nhịp tim",
            "Dấu hiệu hạ đường huyết (nếu dùng với insulin/SU)"
    ],
        "precautions": [
            "Buồn nôn rất phổ biến - Tăng liều từ từ, uống thuốc chống nôn nếu cần",
            "Nguy cơ viêm tụy - Ngừng thuốc nếu nghi ngờ viêm tụy",
            "Nguy cơ ung thư tuyến giáp tủy (MTC) - Chống chỉ định nếu có tiền sử MTC hoặc MEN 2",
            "Giảm liều insulin/sulfonylurea khi bắt đầu dùng",
            "Lợi ích giảm cân và tim mạch lớn",
            "Tiêm mỗi ngày - Tuân thủ điều trị có thể khó"
    ],
        "black_box_warnings": """Nguy cơ ung thư tuyến giáp tủy (MTC) ở động vật thí nghiệm. Chống chỉ định ở bệnh nhân có tiền sử MTC hoặc MEN 2.""",
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
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
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "GLP-1 agonists thải trừ một phần qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Semaglutide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Semaglutide, Ozempic, Wegovy, Rybelsus",
        "brand_names": {
            "common": [
                "Ozempic (ĐTĐ - tiêm)",
                "Wegovy (Giảm cân - tiêm)",
                "Rybelsus (ĐTĐ - uống)"
    ],
            "vietnam": [
                "Ozempic 0.25/0.5/1mg",
                "Rybelsus 3/7/14mg"
    ],
        },
        "administration": [
            "SC (Tiêm dưới da - Ozempic, Wegovy)",
            "PO (Uống - Rybelsus)"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm cân (Wegovy 2.4mg) - Chỉ định riêng",
            "Giảm nguy cơ biến cố tim mạch"
    ],
        "dosage": {
            "dm_t2_injection": """Ozempic: Khởi đầu 0.25mg SC x 1 lần/tuần x 4 tuần, sau đó 0.5mg x 1 lần/tuần. Có thể tăng lên 1mg hoặc 2mg nếu cần.""",
            "dm_t2_oral": "Rybelsus: Khởi đầu 3mg PO x 1 lần/sáng x 30 ngày, sau đó 7mg. Có thể tăng lên 14mg.",
            "weight_loss": "Wegovy: Tăng dần từ 0.25mg đến 2.4mg x 1 lần/tuần.",
            "notes": "Tiêm 1 lần/tuần (tiện lợi hơn Liraglutide). Rybelsus: Uống lúc đói, với ít nước, chờ 30 phút mới ăn.",
        },
        "side_effects": [
            "Buồn nôn, nôn (Phổ biến nhưng ít hơn Liraglutide)",
            "Tiêu chảy, táo bón",
            "Đau bụng",
            "Giảm cân (Mạnh hơn Liraglutide, ~5-10kg)",
            "Viêm tụy cấp (Hiếm)",
            "Tăng nhịp tim nhẹ"
    ],
        "mechanism_of_action": """Tương tự Liraglutide nhưng tác dụng kéo dài hơn (tiêm 1 lần/tuần). Lợi ích tim mạch: Giảm biến cố tim mạch lớn (SUSTAIN-6 trial). Giảm cân mạnh hơn Liraglutide.""",
        "monitoring": [
            "Đường huyết, cân nặng",
            "Dấu hiệu viêm tụy",
            "Nhịp tim"
    ],
        "precautions": [
            "Tương tự Liraglutide",
            "Rybelsus (dạng uống): Phải uống lúc đói, chờ 30 phút mới ăn (hấp thu kém)",
            "Giảm cân mạnh - Rất phổ biến hiện nay (Ozempic, Wegovy)"
    ],
        "black_box_warnings": "Nguy cơ ung thư tuyến giáp tủy (MTC). Chống chỉ định nếu có tiền sử MTC hoặc MEN 2.",
        "contraindications": [
            "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
            "Tiền sử viêm tụy cấp",
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với semaglutide hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        },
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
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
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "GLP-1 agonists thải trừ một phần qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Dulaglutide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Dulaglutide, Trulicity",
        "brand_names": {
            "common": [
                "Trulicity"
    ],
            "vietnam": [
                "Trulicity 0.75/1.5mg"
    ],
        },
        "administration": [
            "SC (Tiêm dưới da)"
    ],
        "indications": [
            "Đái tháo đường type 2",
            "Giảm nguy cơ biến cố tim mạch"
    ],
        "dosage": {
            "dm_t2": "Khởi đầu 0.75mg SC x 1 lần/tuần. Có thể tăng lên 1.5mg, 3mg, hoặc 4.5mg nếu cần.",
            "notes": "Tiêm 1 lần/tuần. Bút tiêm sẵn (pre-filled pen) - Tiện lợi.",
        },
        "side_effects": [
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Đau bụng",
            "Giảm cân",
            "Viêm tụy (Hiếm)"
    ],
        "mechanism_of_action": "Tương tự các GLP-1 RA khác. Lợi ích tim mạch (REWIND trial). Bút tiêm sẵn tiện lợi.",
        "monitoring": [
            "Đường huyết, cân nặng",
            "Dấu hiệu viêm tụy"
    ],
        "black_box_warnings": "Nguy cơ ung thư tuyến giáp tủy (MTC).",
        "contraindications": [],
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
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
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "GLP-1 agonists thải trừ một phần qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
    "Exenatide":     {
        "group": "Diabetes - GLP-1 Receptor Agonist",
        "vietnamese_name": "Exenatide, Byetta, Bydureon",
        "brand_names": {
            "common": [
                "Byetta (2 lần/ngày)",
                "Bydureon (1 lần/tuần)"
    ],
            "vietnam": [
                "Byetta 5/10mcg"
    ],
        },
        "administration": [
            "SC"
    ],
        "indications": [
            "Đái tháo đường type 2"
    ],
        "dosage": {
            "dm_t2_byetta": """Byetta: Khởi đầu 5mcg SC x 2 lần/ngày (trước bữa sáng và tối), sau 1 tháng tăng lên 10mcg x 2 lần/ngày.""",
            "dm_t2_bydureon": "Bydureon: 2mg SC x 1 lần/tuần.",
            "notes": "Byetta: Tiêm 2 lần/ngày (ít tiện lợi hơn). Bydureon: 1 lần/tuần.",
        },
        "side_effects": [
            "Buồn nôn, nôn (Rất phổ biến)",
            "Tiêu chảy",
            "Hạ đường huyết (nếu dùng với SU)",
            "Viêm tụy (Hiếm)"
    ],
        "mechanism_of_action": """GLP-1 RA đầu tiên. Tác dụng tương tự các GLP-1 RA khác nhưng ít được dùng hơn do phải tiêm 2 lần/ngày (Byetta).""",
        "monitoring": [
            "Đường huyết",
            "Dấu hiệu viêm tụy"
    ],
        "contraindications": [
            "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
            "Tiền sử viêm tụy cấp",
            "Đái tháo đường type 1",
            "Nhiễm toan ceton đái tháo đường"
        ],
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tiền sử ung thư tuyến giáp tủy (MTC) hoặc hội chứng u nội tiết đa tuyến type 2 (MEN 2)",
                "Tiền sử viêm tụy cấp",
                "Đái tháo đường type 1",
                "Nhiễm toan ceton do đái tháo đường",
                "Dị ứng với exenatide hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Suy thận - thận trọng, có thể cần giảm liều",
                "Suy gan - thận trọng, theo dõi chức năng gan",
                "Bệnh nhân cao tuổi - tăng nguy cơ buồn nôn, mất nước",
                "Bệnh nhân có bệnh dạ dày - tăng nguy cơ buồn nôn, nôn",
                "Phụ nữ có thai - không có dữ liệu đầy đủ về an toàn"
            ]
        },
        "interactions": [],
        "pregnancy": "C - Nguy cơ không thể loại trừ. Không khuyến nghị trong thai kỳ",
        "precautions": [],
        "pharmacokinetics": {
        },
        "storage": "",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Insulin, Sulfonylureas",
                    "mechanism": "GLP-1 agonists tăng tiết insulin, có thể tăng nguy cơ hạ đường huyết",
                    "effect": "Tăng nguy cơ hạ đường huyết",
                    "management": "Giảm liều insulin hoặc sulfonylurea khi bắt đầu GLP-1 agonist. Theo dõi đường huyết chặt chẽ."
                }
            ],
            "minor": [
                {
                    "drug": "Thuốc uống (nói chung)",
                    "mechanism": "GLP-1 agonists làm chậm làm rỗng dạ dày, có thể ảnh hưởng hấp thu thuốc uống",
                    "effect": "Có thể giảm hấp thu hoặc làm chậm tác dụng của thuốc uống",
                    "management": "Theo dõi tác dụng của thuốc uống. Có thể cần điều chỉnh liều hoặc thời gian uống."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "GLP-1 agonists có thể ảnh hưởng nhẹ đến chuyển hóa warfarin",
                    "effect": "Có thể thay đổi INR nhẹ",
                    "management": "Theo dõi INR khi bắt đầu hoặc thay đổi liều GLP-1 agonist."
                }
            ]
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
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Có thể dùng nhưng thận trọng. Theo dõi chức năng thận.",
            "under_30": "Thận trọng, có thể cần giảm liều. GLP-1 agonists thải trừ qua thận một phần.",
            "dialysis": "Thận trọng. Không có dữ liệu đầy đủ về an toàn ở bệnh nhân lọc máu.",
            "notes": "GLP-1 agonists thải trừ một phần qua thận. Suy thận có thể làm tăng nồng độ thuốc. Cần theo dõi chức năng thận và điều chỉnh liều nếu cần."
        },
        "overdose_management": {
            "symptoms": [],
            "antidote": "",
            "treatment": [],
            "monitoring": "",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị quá liều chủ yếu là hỗ trợ: ngừng thuốc, điều chỉnh đường huyết nếu hạ đường huyết, điều trị viêm tụy nếu có."
        },
        "administration_instructions": {
        },
        "references": {
            "primary_sources": [],
            "last_updated": "",
            "evidence_level": "",
        },
    },
}
