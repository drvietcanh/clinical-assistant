"""
Potassium-Competitive Acid Blockers (PCAB)
Nhóm thuốc mới ức chế acid dạ dày - Thế hệ sau PPI
Vonoprazan, Tegoprazan
"""

PCAB_DRUGS = {
    "Tegoprazan":     {
        "group": "Gastrointestinal - Potassium-Competitive Acid Blocker (PCAB)",
        "vietnamese_name": "Tegoprazan",
        "administration": [
            "PO"
    ],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD (Gastroesophageal Reflux Disease)",
            "Điều trị nhiễm H. pylori (kết hợp với kháng sinh)"
    ],
        "contraindications": [
            "Dị ứng với tegoprazan",
            "Có thai (chưa có dữ liệu đầy đủ)",
            "Cho con bú (chưa có dữ liệu đầy đủ)"
    ],
        "dosage": {
            "adult_po_ulcer": "50mg x 1 lần/ngày",
            "adult_po_gerd": "50mg x 1 lần/ngày",
            "adult_po_hpylori": "50mg x 2 lần/ngày (kết hợp với amoxicillin + clarithromycin)",
            "notes": """Uống với hoặc không có thức ăn. Đang trong giai đoạn 3 thử nghiệm lâm sàng, dự kiến phê duyệt Q4 2025.""",
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Buồn nôn",
            "Phát ban"
    ],
        "interactions": [
            "Ít tương tác với CYP450 hơn PPI",
            "Có thể tương tác với warfarin (theo dõi INR)",
            "Có thể ảnh hưởng đến hấp thu các thuốc cần môi trường acid"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Potassium-Competitive Acid Blocker (PCAB). Ức chế H+/K+-ATPase (proton pump) bằng cách cạnh tranh với kali tại vị trí gắn, dẫn đến ức chế tiết acid dạ dày nhanh chóng và mạnh mẽ hơn PPI. Tương tự vonoprazan nhưng đang trong quá trình phát triển.""",
        "monitoring": [
            "Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng",
            "LFT (AST, ALT) nếu dùng kéo dài",
            "Mg2+ máu (nếu dùng kéo dài >3 tháng)",
            "Vitamin B12 (nếu dùng kéo dài >2 năm)"
    ],
        "precautions": [
            "Có thể uống với hoặc không có thức ăn",
            "Đang trong giai đoạn 3 thử nghiệm lâm sàng",
            "Dự kiến phê duyệt Q4 2025",
            "Thận trọng ở bệnh nhân suy gan, suy thận",
            "Tăng nguy cơ viêm phổi, C. difficile colitis khi dùng kéo dài"
    ],
        "pharmacokinetics": {
            "half_life": "~9-12 giờ (ước tính)",
            "onset": "Nhanh hơn PPI",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "clearance": "Gan (CYP3A4)",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Chưa có (đang trong quá trình phát triển)",
        "drug_interactions": {
            "major": [],
            "moderate": [
    {
                    "drug": "Ketoconazole, Itraconazole",
                    "mechanism": "PCAB tăng pH dạ dày, giảm hấp thu azole antifungals",
                    "effect": "Giảm nồng độ azole antifungals",
                    "management": "Cách thời gian ít nhất 2 giờ.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa có dữ liệu đầy đủ. Chỉ dùng nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "overdose_management": {
            "symptoms": [
                "Cần đánh giá lâm sàng"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Triệu chứng: Buồn nôn, nôn, đau bụng. Điều trị: Hỗ trợ, rửa dạ dày nếu mới uống."
    ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn và triệu chứng",
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với hoặc không có thức ăn. Nuốt nguyên viên, không nhai hoặc nghiền.",
                "timing": "Theo chỉ định của bác sĩ",
            },
            "iv": {
                "reconstitution": "N/A",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống",
            },
        },
        "references": {
            "primary_sources": [
                "Clinical Trials (Phase 3), Cinclus Pharma Q3 2025 Report"
    ],
            "last_updated": "",
            "evidence_level": "",
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Magnesium (long-term use)"],
            },
            "guideline_tags": [
                "ACG 2017 GERD Guidelines",
                "FDA - Long-term PPI use monitoring",
            ]
    },
    "Vonoprazan":     {
        "group": "Gastrointestinal - Potassium-Competitive Acid Blocker (PCAB)",
        "vietnamese_name": "Vonoprazan, Voquezna",
        "administration": [
            "PO"
    ],
        "indications": [
            "Loét dạ dày tá tràng",
            "GERD (Gastroesophageal Reflux Disease)",
            "Điều trị nhiễm H. pylori (kết hợp với kháng sinh)",
            "Phòng ngừa loét do stress",
            "Zollinger-Ellison syndrome"
    ],
        "contraindications": [
            "Dị ứng với vonoprazan",
            "Có thai (chưa có dữ liệu đầy đủ)",
            "Cho con bú (chưa có dữ liệu đầy đủ)"
    ],
        "dosage": {
            "adult_po_ulcer": "20mg x 1 lần/ngày",
            "adult_po_gerd": "20mg x 1 lần/ngày",
            "adult_po_hpylori": "20mg x 2 lần/ngày (kết hợp với amoxicillin + clarithromycin)",
            "adult_po_maintenance": "10mg x 1 lần/ngày",
            "notes": "Uống với hoặc không có thức ăn. Không cần uống trước bữa ăn như PPI.",
        },
        "side_effects": [
            "Nhức đầu",
            "Tiêu chảy",
            "Đau bụng",
            "Buồn nôn",
            "Phát ban",
            "Tăng men gan (hiếm)"
    ],
        "interactions": [
            "Ít tương tác với CYP450 hơn PPI",
            "Có thể tương tác với warfarin (theo dõi INR)",
            "Có thể ảnh hưởng đến hấp thu các thuốc cần môi trường acid (ketoconazole, itraconazole)"
    ],
        "pregnancy": "C",
        "mechanism_of_action": """Potassium-Competitive Acid Blocker (PCAB). Ức chế H+/K+-ATPase (proton pump) bằng cách cạnh tranh với kali tại vị trí gắn, dẫn đến ức chế tiết acid dạ dày nhanh chóng và mạnh mẽ hơn PPI. Khác với PPI (ức chế không thuận nghịch), PCAB ức chế thuận nghịch nhưng hiệu quả hơn và tác dụng nhanh hơn.""",
        "monitoring": [
            "Đáp ứng lâm sàng: giảm triệu chứng đau, ợ nóng",
            "LFT (AST, ALT) nếu dùng kéo dài",
            "Mg2+ máu (nếu dùng kéo dài >3 tháng)",
            "Vitamin B12 (nếu dùng kéo dài >2 năm)",
            "Dấu hiệu nhiễm trùng: tăng nguy cơ viêm phổi, C. difficile colitis"
    ],
        "precautions": [
            "Có thể uống với hoặc không có thức ăn (khác với PPI cần uống trước bữa ăn)",
            "Ưu điểm so với PPI: Tác dụng nhanh hơn, không cần uống trước bữa ăn, ít tương tác với CYP450",
            "Thận trọng ở bệnh nhân suy gan nặng",
            "Thận trọng ở bệnh nhân suy thận (không cần chỉnh liều nhưng monitor)",
            "Tăng nguy cơ viêm phổi, C. difficile colitis (đặc biệt ở người già, suy giảm miễn dịch)",
            "Có thể tăng nguy cơ gãy xương khi dùng kéo dài (tương tự PPI)"
    ],
        "pharmacokinetics": {
            "half_life": "9 giờ (dài hơn PPI)",
            "onset": "Nhanh hơn PPI (tác dụng trong vài giờ)",
            "duration": "24 giờ",
            "protein_binding": ">99%",
            "clearance": "Gan (CYP3A4) - ít tương tác hơn PPI",
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": """Có thể tăng nguy cơ gãy xương hông, cổ tay, cột sống khi dùng lâu dài (≥1 năm). Nguy cơ nhiễm C. difficile tăng. Giảm hấp thu vitamin B12 và magnesium khi dùng lâu dài.""",
        "drug_interactions": {
            "major": [
    {
                    "drug": "Atazanavir (HIV protease inhibitor)",
                    "mechanism": "PCAB làm tăng pH dạ dày, giảm hấp thu atazanavir (cần môi trường acid)",
                    "effect": "Giảm nồng độ atazanavir, giảm hiệu quả điều trị HIV",
                    "management": "CHỐNG CHỈ ĐỊNH dùng cùng. Không dùng vonoprazan với atazanavir.",
                }
                ],
            "moderate": [
    {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "PCAB tăng pH dạ dày, giảm hấp thu azole antifungals (cần môi trường acid)",
                    "effect": "Giảm nồng độ azole antifungals, giảm hiệu quả",
                    "management": "Cách thời gian ít nhất 2 giờ. Hoặc dùng IV azole nếu có thể.",
                },
    {
                    "drug": "Warfarin",
                    "mechanism": "Vonoprazan ít ức chế CYP450 hơn PPI, nhưng vẫn có thể tương tác nhẹ",
                    "effect": "Có thể tăng INR nhẹ",
                    "management": "Theo dõi INR thường xuyên.",
                }
                ],
            "minor": [],
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Chưa có dữ liệu đầy đủ về sử dụng trong thai kỳ. Chỉ dùng nếu lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết có bài tiết vào sữa mẹ hay không. Thận trọng khi cho con bú.",
                "recommendation": "Thận trọng khi cho con bú.",
            },
        },
        "overdose_management": {
            "symptoms": [
                "Cần đánh giá lâm sàng"
    ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Triệu chứng: Buồn nôn, nôn, đau bụng. Điều trị: Hỗ trợ, rửa dạ dày nếu mới uống. Không có chất đối kháng đặc hiệu."
    ],
            "monitoring": "Theo dõi dấu hiệu sinh tồn và triệu chứng",
        },
        "administration_instructions": {
            "oral": {
                "with_food": """Uống với hoặc không có thức ăn. Không cần uống trước bữa ăn như PPI. Nuốt nguyên viên, không nhai hoặc nghiền.""",
                "timing": "Theo chỉ định của bác sĩ",
            },
            "iv": {
                "reconstitution": "N/A",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống",
            },
        },
        "references": {
            "primary_sources": [
                "FDA Label (Voquezna), UpToDate - Vonoprazan, ACG Guidelines 2024 - H. pylori Treatment"
    ],
            "last_updated": "",
            "evidence_level": "",
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan.",
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
        },
            "risk_flags": {
                "high_alert": False,
                "narrow_therapeutic_index": False,
                "bleeding_risk": False,
                "organ_toxicity": [],
                "qt_prolongation": False,
                "hepatotoxicity": False,
                "nephrotoxicity": False,
                "requires_monitoring": ["Magnesium (long-term use)"],
            },
            "guideline_tags": [
                "ACG 2017 GERD Guidelines",
                "FDA - Long-term PPI use monitoring",
            ]
    },
}

