"""Oncology Medications - Monoclonal Antibodies and Antibody-Drug Conjugates
Active module - contains targeted therapy mAbs and ADCs for cancer treatment"""

# Monoclonal Antibodies and Antibody-Drug Conjugates for Oncology

MONOCLONAL_ANTIBODIES_ADCS_DRUGS = {
    "Daratumumab": {
        "group": "Oncology - Anti-CD38 Monoclonal Antibody",
        "vietnamese_name": "Daratumumab, Darzalex",
        "administration": ["IV", "SC"],
        "indications": [
            "Multiple myeloma - newly diagnosed",
            "Multiple myeloma - relapsed/refractory",
            "AL amyloidosis - relapsed/refractory"
        ],
        "contraindications": [
            "Dị ứng daratumumab hoặc bất kỳ thành phần nào"
        ],
        "dosage": {
            "adult_iv": "16mg/kg IV mỗi tuần x 8 tuần, sau đó mỗi 2 tuần x 16 tuần, sau đó mỗi 4 tuần",
            "adult_sc": "1800mg SC mỗi tuần x 8 tuần, sau đó mỗi 2 tuần x 16 tuần, sau đó mỗi 4 tuần",
            "notes": "Truyền tĩnh mạch hoặc tiêm dưới da. Cần premedication để giảm phản ứng truyền. Dùng kết hợp với các thuốc khác (lenalidomide, bortezomib, pomalidomide)."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến, có thể nghiêm trọng",
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến",
            "Giảm bạch cầu lympho (lymphopenia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, viêm phổi) - phổ biến",
            "Mệt mỏi",
            "Buồn nôn",
            "Tiêu chảy",
            "Tăng nguy cơ nhiễm trùng nặng (bao gồm nhiễm trùng cơ hội)"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Vaccine sống: chống chỉ định trong và sau điều trị"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Daratumumab là kháng thể đơn dòng kháng CD38 (human monoclonal antibody). "
            "CD38 là kháng nguyên bề mặt trên tế bào plasma (plasma cells) và tế bào myeloma, "
            "cũng có trên một số tế bào miễn dịch khác. "
            "Trong multiple myeloma, tế bào myeloma biểu hiện CD38 ở mức độ cao. "
            "Daratumumab gắn với CD38 trên tế bào myeloma → kích hoạt complement-dependent cytotoxicity (CDC), "
            "antibody-dependent cell-mediated cytotoxicity (ADCC), và antibody-dependent cellular phagocytosis (ADCP) → "
            "tiêu diệt tế bào myeloma. "
            "Daratumumab cũng có thể ức chế hoạt động của CD38 (một enzyme có vai trò trong chuyển hóa), "
            "gây ức chế tăng sinh tế bào myeloma. "
            "Dẫn đến: giảm số lượng tế bào myeloma, cải thiện đáp ứng điều trị, và kéo dài thời gian sống trong multiple myeloma. "
            "Daratumumab được dùng để điều trị multiple myeloma (newly diagnosed và relapsed/refractory), "
            "thường dùng kết hợp với các thuốc khác (lenalidomide, bortezomib, pomalidomide, dexamethasone)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng bạch cầu lympho - theo dõi lymphopenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Đáp ứng điều trị (M-protein, free light chains, bone marrow biopsy)"
        ],
        "precautions": [
            "PHẢN ỨNG TRUYỀN - phổ biến và có thể nghiêm trọng, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm tế bào miễn dịch",
            "Cần hoàn thành tất cả vaccine trước khi bắt đầu điều trị (ít nhất 4-6 tuần trước)",
            "CHỐNG CHỈ ĐỊNH vaccine sống trong và sau điều trị (ít nhất 3-6 tháng sau liều cuối)",
            "Ngừng daratumumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân có tiền sử nhiễm trùng tái phát",
            "Dạng SC: ít phản ứng truyền hơn dạng IV"
        ],
        "pharmacokinetics": {
            "half_life": "~18 ngày (dài, cho phép dùng 1-4 tuần một lần)",
            "onset": "Giảm tế bào myeloma trong vòng vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1κ monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C hoặc 15 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "NGUY CƠ PHẢN ỨNG TRUYỀN - có thể nghiêm trọng và đe dọa tính mạng. "
            "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. "
            "Theo dõi chặt chẽ trong và sau truyền. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng daratumumab nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Vaccine sống (MMR, varicella, zoster, yellow fever, BCG)",
                    "mechanism": "Daratumumab làm giảm đáp ứng miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng từ vaccine sống",
                    "management": "CHỐNG CHỈ ĐỊNH dùng vaccine sống trong và sau điều trị. Hoãn vaccine sống ít nhất 3-6 tháng sau liều cuối."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao, lenalidomide, bortezomib)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng",
                    "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng daratumumab hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Tiền sử nhiễm trùng tái phát",
                "Tiền sử phản ứng truyền nặng với các mAbs khác",
                "Suy giảm miễn dịch nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Daratumumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ phản ứng truyền nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Giảm bạch cầu/tiểu cầu nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay nếu có phản ứng nặng",
                "Điều trị phản ứng truyền: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)"
            ],
            "monitoring": "Phản ứng truyền, dấu hiệu nhiễm trùng, số lượng tế bào máu, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch với tốc độ tăng dần (bắt đầu 50ml/h, tăng đến 200ml/h nếu dung nạp tốt).",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền."
            },
            "sc": {
                "reconstitution": "Dùng trực tiếp từ ống tiêm đã pha sẵn.",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "injection_technique": "Tiêm dưới da (SC), không tiêm vào cơ hoặc tĩnh mạch.",
                "notes": "Dạng SC: ít phản ứng truyền hơn dạng IV. Cần premedication trước mỗi liều."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Daratumumab (Darzalex)",
                "UpToDate - Daratumumab: Drug information",
                "Lexicomp - Daratumumab monograph",
                "NCCN Guidelines - Multiple Myeloma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in multiple myeloma"
        }
    },

    "Brentuximab vedotin": {
        "group": "Oncology - Antibody-Drug Conjugate (ADC)",
        "vietnamese_name": "Brentuximab vedotin, Adcetris",
        "administration": ["IV"],
        "indications": [
            "Hodgkin lymphoma - relapsed/refractory",
            "Hodgkin lymphoma - frontline (kết hợp với AVD)",
            "Anaplastic large cell lymphoma (ALCL) - relapsed/refractory",
            "Cutaneous T-cell lymphoma (CTCL) - relapsed/refractory",
            "Peripheral T-cell lymphoma (PTCL) - frontline"
        ],
        "contraindications": [
            "Dị ứng brentuximab vedotin hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "1.8mg/kg IV mỗi 3 tuần (tối đa 180mg)",
            "adult_weekly": "1.2mg/kg IV mỗi tuần x 3 tuần, sau đó nghỉ 1 tuần (chu kỳ 4 tuần)",
            "notes": "Truyền tĩnh mạch trong 30 phút. Cần premedication để giảm phản ứng truyền. Dùng kết hợp với các thuốc khác trong một số phác đồ."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Bệnh lý thần kinh ngoại biên (peripheral neuropathy) - phổ biến, có thể nghiêm trọng",
            "Mệt mỏi",
            "Buồn nôn",
            "Tiêu chảy",
            "Sốt",
            "Nhiễm trùng (nhiễm trùng đường hô hấp trên, viêm phổi) - phổ biến",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Hội chứng giải phóng cytokine (cytokine release syndrome) - hiếm nhưng nghiêm trọng"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Thuốc gây độc thần kinh (vincristine, cisplatin): tăng nguy cơ bệnh lý thần kinh",
            "Strong CYP3A4 inhibitors: tăng nồng độ monomethyl auristatin E (MMAE), tăng độc tính",
            "Strong CYP3A4 inducers: giảm nồng độ MMAE, giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": (
            "Brentuximab vedotin là antibody-drug conjugate (ADC) gồm: "
            "(1) kháng thể đơn dòng kháng CD30 (chimeric monoclonal antibody), "
            "(2) linker (valine-citrulline dipeptide), và "
            "(3) payload (monomethyl auristatin E - MMAE, một chất ức chế microtubule). "
            "CD30 là kháng nguyên bề mặt trên tế bào Reed-Sternberg trong Hodgkin lymphoma và tế bào T trong ALCL. "
            "Brentuximab vedotin gắn với CD30 trên tế bào ung thư → được nội bào hóa (internalization) vào tế bào → "
            "linker bị cắt bởi protease (cathepsin B) trong lysosome → giải phóng MMAE → "
            "MMAE ức chế microtubule polymerization → ngăn cản phân chia tế bào → gây chết tế bào ung thư. "
            "Dẫn đến: tiêu diệt tế bào ung thư biểu hiện CD30, cải thiện đáp ứng điều trị, và kéo dài thời gian sống. "
            "Brentuximab vedotin được dùng để điều trị Hodgkin lymphoma và T-cell lymphoma, "
            "đặc biệt hiệu quả ở bệnh nhân relapsed/refractory. "
            "MMAE cũng có thể được giải phóng vào máu và gây độc tính toàn thân (đặc biệt bệnh lý thần kinh ngoại biên)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "Bệnh lý thần kinh ngoại biên - theo dõi triệu chứng (tê, ngứa ran, yếu, đau)",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Đáp ứng điều trị (CT scan, PET scan)"
        ],
        "precautions": [
            "BỆNH LÝ THẦN KINH NGOẠI BIÊN - phổ biến và có thể nghiêm trọng, cần theo dõi và điều chỉnh liều",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm bạch cầu",
            "Giảm liều hoặc ngừng thuốc nếu bệnh lý thần kinh ngoại biên nặng (grade 3-4)",
            "Thận trọng khi dùng với thuốc gây độc thần kinh (vincristine, cisplatin)",
            "Thận trọng khi dùng với strong CYP3A4 inhibitors hoặc inducers",
            "Ngừng brentuximab vedotin nếu có nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~4-6 ngày (ADC), ~3-4 ngày (MMAE)",
            "onset": "Giảm tế bào ung thư trong vòng vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "ADC: IgG1 monoclonal antibody, MMAE: ~70%",
            "metabolism": "ADC: chuyển hóa qua RES, MMAE: chuyển hóa qua CYP3A4",
            "clearance": "ADC: không phụ thuộc gan thận đáng kể, MMAE: phụ thuộc gan (CYP3A4)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C hoặc 8 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "BỆNH LÝ THẦN KINH NGOẠI BIÊN - có thể nghiêm trọng và không hồi phục. "
            "Cần theo dõi triệu chứng và điều chỉnh liều hoặc ngừng thuốc nếu nặng. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng brentuximab vedotin nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa MMAE, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt bệnh lý thần kinh ngoại biên)",
                    "management": "Thận trọng. Có thể cần giảm liều brentuximab vedotin."
                },
                {
                    "drug": "Thuốc gây độc thần kinh (vincristine, cisplatin, paclitaxel)",
                    "mechanism": "Tăng độc tính thần kinh",
                    "effect": "Tăng nguy cơ bệnh lý thần kinh ngoại biên nghiêm trọng",
                    "management": "Thận trọng. Theo dõi triệu chứng thần kinh chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa MMAE, giảm nồng độ",
                    "effect": "Giảm hiệu quả brentuximab vedotin",
                    "management": "Thận trọng. Có thể cần tăng liều brentuximab vedotin."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng brentuximab vedotin hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử bệnh lý thần kinh ngoại biên nặng",
                "Tiền sử nhiễm trùng tái phát",
                "Suy gan nặng - giảm chuyển hóa MMAE, tăng độc tính",
                "Suy thận nặng - giảm thải trừ, tăng độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Tránh dùng trong thai kỳ. Nếu cần dùng, thông báo rõ ràng về nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Tránh dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "MMAE chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ MMAE, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ bệnh lý thần kinh ngoại biên nặng",
                "Tăng nguy cơ giảm bạch cầu/tiểu cầu nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Theo dõi bệnh lý thần kinh ngoại biên chặt chẽ",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Bệnh lý thần kinh ngoại biên, số lượng tế bào máu, chức năng gan, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 30 phút.",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Brentuximab vedotin (Adcetris)",
                "UpToDate - Brentuximab vedotin: Drug information",
                "Lexicomp - Brentuximab vedotin monograph",
                "NCCN Guidelines - Hodgkin Lymphoma"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in Hodgkin and T-cell lymphoma"
        }
    },

    "Trastuzumab deruxtecan": {
        "group": "Oncology - Antibody-Drug Conjugate (ADC)",
        "vietnamese_name": "Trastuzumab deruxtecan, Enhertu",
        "administration": ["IV"],
        "indications": [
            "Ung thư vú HER2+ - unresectable hoặc metastatic",
            "Ung thư vú HER2-low - unresectable hoặc metastatic",
            "Ung thư dạ dày HER2+ - unresectable hoặc metastatic",
            "Ung thư phổi không tế bào nhỏ (NSCLC) HER2-mutant - unresectable hoặc metastatic"
        ],
        "contraindications": [
            "Dị ứng trastuzumab deruxtecan hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "5.4mg/kg IV mỗi 3 tuần",
            "adult_her2_low": "5.4mg/kg IV mỗi 3 tuần",
            "notes": "Truyền tĩnh mạch trong 30-90 phút. Cần premedication để giảm phản ứng truyền. Điều chỉnh liều theo độc tính."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Buồn nôn - phổ biến",
            "Mệt mỏi - phổ biến",
            "Nôn - phổ biến",
            "Rụng tóc - phổ biến",
            "Táo bón - phổ biến",
            "Tiêu chảy - phổ biến",
            "Giảm cảm giác ngon miệng - phổ biến",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Bệnh lý phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng nghiêm trọng, có thể gây tử vong",
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Nhiễm trùng - phổ biến"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Strong CYP3A4 inhibitors: tăng nồng độ deruxtecan, tăng độc tính",
            "Strong CYP3A4 inducers: giảm nồng độ deruxtecan, giảm hiệu quả"
        ],
        "pregnancy": "D",
        "mechanism_of_action": (
            "Trastuzumab deruxtecan là antibody-drug conjugate (ADC) gồm: "
            "(1) trastuzumab (kháng thể đơn dòng kháng HER2, humanized monoclonal antibody), "
            "(2) linker (tetrapeptide-based, cleavable), và "
            "(3) payload (deruxtecan - DXd, một chất ức chế topoisomerase I). "
            "HER2 (human epidermal growth factor receptor 2) là thụ thể tyrosine kinase trên tế bào ung thư vú, dạ dày, và phổi. "
            "Trastuzumab deruxtecan gắn với HER2 trên tế bào ung thư → được nội bào hóa (internalization) vào tế bào → "
            "linker bị cắt bởi protease trong lysosome → giải phóng deruxtecan → "
            "deruxtecan ức chế topoisomerase I → gây đứt gãy DNA → gây chết tế bào ung thư. "
            "Deruxtecan cũng có thể khuếch tán vào các tế bào lân cận (bystander effect), "
            "tiêu diệt cả tế bào ung thư không biểu hiện HER2. "
            "Dẫn đến: tiêu diệt tế bào ung thư HER2+, cải thiện đáp ứng điều trị, và kéo dài thời gian sống. "
            "Trastuzumab deruxtecan được dùng để điều trị ung thư vú HER2+ và HER2-low, "
            "ung thư dạ dày HER2+, và ung thư phổi HER2-mutant, "
            "đặc biệt hiệu quả ở bệnh nhân đã điều trị trước đó với trastuzumab và các thuốc khác. "
            "Deruxtecan cũng có thể được giải phóng vào máu và gây độc tính toàn thân (đặc biệt bệnh lý phổi kẽ)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "BỆNH LÝ PHỔI KẼ (ILD) - theo dõi triệu chứng (khó thở, ho, sốt, đau ngực)",
            "Chức năng phổi (X-quang ngực, CT scan ngực) - nếu có triệu chứng ILD",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Đáp ứng điều trị (CT scan, PET scan)"
        ],
        "precautions": [
            "BỆNH LÝ PHỔI KẼ (ILD) - hiếm nhưng nghiêm trọng, có thể gây tử vong, cần theo dõi chặt chẽ",
            "Ngừng trastuzumab deruxtecan ngay nếu nghi ngờ ILD và đánh giá",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm bạch cầu",
            "Giảm liều hoặc ngừng thuốc nếu giảm bạch cầu/tiểu cầu nặng (grade 3-4)",
            "Thận trọng khi dùng với strong CYP3A4 inhibitors hoặc inducers",
            "Ngừng trastuzumab deruxtecan nếu có nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~5.7 ngày (ADC), ~5.8 ngày (deruxtecan)",
            "onset": "Giảm tế bào ung thư trong vòng vài tuần",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "ADC: IgG1 monoclonal antibody, deruxtecan: ~97%",
            "metabolism": "ADC: chuyển hóa qua RES, deruxtecan: chuyển hóa qua CYP3A4",
            "clearance": "ADC: không phụ thuộc gan thận đáng kể, deruxtecan: phụ thuộc gan (CYP3A4)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 24 giờ ở 2-8°C hoặc 4 giờ ở nhiệt độ phòng.",
        "black_box_warnings": (
            "BỆNH LÝ PHỔI KẼ (ILD) - có thể nghiêm trọng và đe dọa tính mạng. "
            "Có báo cáo tử vong do ILD. "
            "Cần theo dõi triệu chứng (khó thở, ho, sốt, đau ngực) và chức năng phổi. "
            "Ngừng trastuzumab deruxtecan ngay nếu nghi ngờ ILD và đánh giá. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng trastuzumab deruxtecan nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa deruxtecan, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt bệnh lý phổi kẽ)",
                    "management": "Thận trọng. Có thể cần giảm liều trastuzumab deruxtecan."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa deruxtecan, giảm nồng độ",
                    "effect": "Giảm hiệu quả trastuzumab deruxtecan",
                    "management": "Thận trọng. Có thể cần tăng liều trastuzumab deruxtecan."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng trastuzumab deruxtecan hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử bệnh lý phổi kẽ - tăng nguy cơ ILD",
                "Tiền sử nhiễm trùng tái phát",
                "Suy gan nặng - giảm chuyển hóa deruxtecan, tăng độc tính",
                "Suy thận nặng - giảm thải trừ, tăng độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Tránh dùng trong thai kỳ. Nếu cần dùng, thông báo rõ ràng về nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Tránh dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "Deruxtecan chuyển hóa ở gan qua CYP3A4. Suy gan làm giảm chuyển hóa, tăng nồng độ deruxtecan, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ bệnh lý phổi kẽ nặng",
                "Tăng nguy cơ giảm bạch cầu/tiểu cầu nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Đánh giá bệnh lý phổi kẽ (X-quang ngực, CT scan ngực)",
                "Điều trị ILD nếu có (corticosteroid, hỗ trợ hô hấp nếu cần)",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Bệnh lý phổi kẽ, số lượng tế bào máu, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 30-90 phút (tùy liều).",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền, đặc biệt dấu hiệu bệnh lý phổi kẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trastuzumab deruxtecan (Enhertu)",
                "UpToDate - Trastuzumab deruxtecan: Drug information",
                "Lexicomp - Trastuzumab deruxtecan monograph",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in HER2+ and HER2-low breast cancer"
        }
    },

    "Sacituzumab govitecan": {
        "group": "Oncology - Antibody-Drug Conjugate (ADC)",
        "vietnamese_name": "Sacituzumab govitecan, Trodelvy",
        "administration": ["IV"],
        "indications": [
            "Ung thư vú triple-negative (TNBC) - unresectable hoặc metastatic",
            "Ung thư vú hormone receptor-positive (HR+) - unresectable hoặc metastatic",
            "Ung thư bàng quang (urothelial carcinoma) - unresectable hoặc metastatic"
        ],
        "contraindications": [
            "Dị ứng sacituzumab govitecan hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "10mg/kg IV ngày 1 và 8 của chu kỳ 21 ngày",
            "notes": "Truyền tĩnh mạch trong 3 giờ. Cần premedication để giảm phản ứng truyền. Điều chỉnh liều theo độc tính."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "Thận trọng, có thể cần giảm liều"
        },
        "side_effects": [
            "Giảm bạch cầu trung tính (neutropenia) - phổ biến, có thể nghiêm trọng",
            "Giảm hemoglobin (anemia) - phổ biến",
            "Giảm tiểu cầu (thrombocytopenia) - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến, có thể nghiêm trọng",
            "Mệt mỏi - phổ biến",
            "Nôn - phổ biến",
            "Rụng tóc - phổ biến",
            "Táo bón - phổ biến",
            "Giảm cảm giác ngon miệng - phổ biến",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Bệnh lý phổi kẽ (interstitial lung disease - ILD) - hiếm nhưng nghiêm trọng",
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Nhiễm trùng - phổ biến"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Strong CYP3A4 inhibitors: tăng nồng độ SN-38, tăng độc tính",
            "Strong CYP3A4 inducers: giảm nồng độ SN-38, giảm hiệu quả",
            "Strong UGT1A1 inhibitors: tăng nồng độ SN-38, tăng độc tính"
        ],
        "pregnancy": "D",
        "mechanism_of_action": (
            "Sacituzumab govitecan là antibody-drug conjugate (ADC) gồm: "
            "(1) sacituzumab (kháng thể đơn dòng kháng Trop-2, humanized monoclonal antibody), "
            "(2) linker (CL2A, cleavable), và "
            "(3) payload (govitecan - SN-38, một chất ức chế topoisomerase I, là chất chuyển hóa hoạt động của irinotecan). "
            "Trop-2 (trophoblast cell-surface antigen 2) là kháng nguyên bề mặt trên tế bào ung thư vú, bàng quang, và các ung thư khác. "
            "Sacituzumab govitecan gắn với Trop-2 trên tế bào ung thư → được nội bào hóa (internalization) vào tế bào → "
            "linker bị cắt bởi protease trong lysosome → giải phóng SN-38 → "
            "SN-38 ức chế topoisomerase I → gây đứt gãy DNA → gây chết tế bào ung thư. "
            "SN-38 cũng có thể khuếch tán vào các tế bào lân cận (bystander effect), "
            "tiêu diệt cả tế bào ung thư không biểu hiện Trop-2. "
            "Dẫn đến: tiêu diệt tế bào ung thư biểu hiện Trop-2, cải thiện đáp ứng điều trị, và kéo dài thời gian sống. "
            "Sacituzumab govitecan được dùng để điều trị ung thư vú triple-negative và HR+, "
            "và ung thư bàng quang, đặc biệt hiệu quả ở bệnh nhân đã điều trị trước đó. "
            "SN-38 cũng có thể được giải phóng vào máu và gây độc tính toàn thân (đặc biệt tiêu chảy và giảm bạch cầu)."
        ),
        "monitoring": [
            "Số lượng bạch cầu trung tính (ANC) - theo dõi neutropenia",
            "Số lượng tiểu cầu - theo dõi thrombocytopenia",
            "Hemoglobin - theo dõi anemia",
            "TIÊU CHẢY - theo dõi triệu chứng và mức độ nghiêm trọng",
            "Bệnh lý phổi kẽ (ILD) - theo dõi triệu chứng (khó thở, ho, sốt, đau ngực)",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)",
            "Đáp ứng điều trị (CT scan, PET scan)"
        ],
        "precautions": [
            "TIÊU CHẢY - phổ biến và có thể nghiêm trọng, cần điều trị sớm (loperamide, atropine/diphenoxylate)",
            "BỆNH LÝ PHỔI KẼ (ILD) - hiếm nhưng nghiêm trọng, cần theo dõi chặt chẽ",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do giảm bạch cầu",
            "Giảm liều hoặc ngừng thuốc nếu giảm bạch cầu/tiểu cầu nặng (grade 3-4)",
            "Giảm liều hoặc ngừng thuốc nếu tiêu chảy nặng (grade 3-4)",
            "Thận trọng khi dùng với strong CYP3A4 hoặc UGT1A1 inhibitors hoặc inducers",
            "Ngừng sacituzumab govitecan nếu có nhiễm trùng nặng"
        ],
        "pharmacokinetics": {
            "half_life": "~11.7 giờ (ADC), ~12.4 giờ (SN-38)",
            "onset": "Giảm tế bào ung thư trong vòng vài tuần",
            "duration": "Trung bình (do half-life trung bình)",
            "protein_binding": "ADC: IgG1 monoclonal antibody, SN-38: ~95%",
            "metabolism": "ADC: chuyển hóa qua RES, SN-38: chuyển hóa qua CYP3A4 và UGT1A1",
            "clearance": "ADC: không phụ thuộc gan thận đáng kể, SN-38: phụ thuộc gan (CYP3A4, UGT1A1)"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 4 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "TIÊU CHẢY - có thể nghiêm trọng. Cần điều trị sớm (loperamide, atropine/diphenoxylate). "
            "Giảm liều hoặc ngừng thuốc nếu tiêu chảy nặng. "
            "BỆNH LÝ PHỔI KẼ (ILD) - có thể nghiêm trọng và đe dọa tính mạng. "
            "Cần theo dõi triệu chứng và chức năng phổi. "
            "NGUY CƠ NHIỄM TRÙNG NẶNG - bao gồm nhiễm trùng cơ hội. "
            "Ngừng sacituzumab govitecan nếu có nhiễm trùng nặng."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, itraconazole, clarithromycin, ritonavir)",
                    "mechanism": "Ức chế chuyển hóa SN-38, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt tiêu chảy và giảm bạch cầu)",
                    "management": "Thận trọng. Có thể cần giảm liều sacituzumab govitecan."
                },
                {
                    "drug": "Strong UGT1A1 inhibitors",
                    "mechanism": "Ức chế chuyển hóa SN-38, tăng nồng độ",
                    "effect": "Tăng độc tính (đặc biệt tiêu chảy và giảm bạch cầu)",
                    "management": "Thận trọng. Có thể cần giảm liều sacituzumab govitecan."
                }
            ],
            "moderate": [
                {
                    "drug": "Strong CYP3A4 inducers (rifampin, carbamazepine, phenytoin)",
                    "mechanism": "Tăng chuyển hóa SN-38, giảm nồng độ",
                    "effect": "Giảm hiệu quả sacituzumab govitecan",
                    "management": "Thận trọng. Có thể cần tăng liều sacituzumab govitecan."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng sacituzumab govitecan hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử tiêu chảy nặng - tăng nguy cơ tiêu chảy",
                "Tiền sử bệnh lý phổi kẽ - tăng nguy cơ ILD",
                "Tiền sử nhiễm trùng tái phát",
                "Suy gan nặng - giảm chuyển hóa SN-38, tăng độc tính",
                "Suy thận nặng - giảm thải trừ, tăng độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Có thể gây hại cho thai nhi. Tránh dùng trong thai kỳ. Nếu cần dùng, thông báo rõ ràng về nguy cơ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Tránh dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, có thể cần giảm liều hoặc tránh dùng",
            "notes": "SN-38 chuyển hóa ở gan qua CYP3A4 và UGT1A1. Suy gan làm giảm chuyển hóa, tăng nồng độ SN-38, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ tiêu chảy nặng",
                "Tăng nguy cơ bệnh lý phổi kẽ nặng",
                "Tăng nguy cơ giảm bạch cầu/tiểu cầu nặng",
                "Tăng nguy cơ nhiễm trùng",
                "Tăng men gan nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay",
                "Điều trị tiêu chảy: loperamide, atropine/diphenoxylate, bù nước và điện giải",
                "Đánh giá bệnh lý phổi kẽ (X-quang ngực, CT scan ngực) nếu có triệu chứng",
                "Điều trị ILD nếu có (corticosteroid, hỗ trợ hô hấp nếu cần)",
                "Hỗ trợ tế bào máu nếu cần (G-CSF, truyền tiểu cầu, truyền máu)",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có",
                "Theo dõi chức năng gan"
            ],
            "monitoring": "Tiêu chảy, bệnh lý phổi kẽ, số lượng tế bào máu, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 3 giờ.",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền, đặc biệt dấu hiệu tiêu chảy và bệnh lý phổi kẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sacituzumab govitecan (Trodelvy)",
                "UpToDate - Sacituzumab govitecan: Drug information",
                "Lexicomp - Sacituzumab govitecan monograph",
                "NCCN Guidelines - Breast Cancer"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in triple-negative breast cancer"
        }
    },

    "Teprotumumab": {
        "group": "Oncology - Anti-IGF-1R Monoclonal Antibody",
        "vietnamese_name": "Teprotumumab, Tepezza",
        "administration": ["IV"],
        "indications": [
            "Bệnh mắt do tuyến giáp (thyroid eye disease - TED) - active, moderate to severe"
        ],
        "contraindications": [
            "Dị ứng teprotumumab hoặc bất kỳ thành phần nào",
            "Đang có nhiễm trùng nặng"
        ],
        "dosage": {
            "adult_standard": "10mg/kg IV liều đầu, sau đó 20mg/kg IV mỗi 3 tuần x 7 liều (tổng 8 liều)",
            "notes": "Truyền tĩnh mạch trong 90 phút. Cần premedication để giảm phản ứng truyền."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Không cần chỉnh liều"
        },
        "side_effects": [
            "Phản ứng truyền (infusion-related reactions) - phổ biến",
            "Co thắt cơ (muscle spasms) - phổ biến",
            "Rụng tóc - phổ biến",
            "Mệt mỏi - phổ biến",
            "Buồn nôn - phổ biến",
            "Tiêu chảy - phổ biến",
            "Tăng đường huyết - phổ biến",
            "Giảm thính lực (hearing loss) - phổ biến, có thể không hồi phục",
            "Tăng men gan (ALT, AST) - có thể nghiêm trọng",
            "Nhiễm trùng - phổ biến"
        ],
        "interactions": [
            "Thuốc ức chế miễn dịch khác: tăng nguy cơ nhiễm trùng",
            "Insulin, thuốc hạ đường huyết: tăng đường huyết, có thể cần điều chỉnh liều"
        ],
        "pregnancy": "C",
        "mechanism_of_action": (
            "Teprotumumab là kháng thể đơn dòng kháng IGF-1R (insulin-like growth factor-1 receptor, human monoclonal antibody). "
            "IGF-1R là thụ thể tyrosine kinase trên tế bào, có vai trò trong tăng sinh tế bào, biệt hóa, và chuyển hóa. "
            "Trong bệnh mắt do tuyến giáp (TED), có sự kích hoạt quá mức của IGF-1R trên tế bào fibroblast và tế bào mỡ trong hốc mắt, "
            "dẫn đến tăng sinh mô, viêm, và phù nề, gây lồi mắt (proptosis), nhìn đôi (diplopia), và các triệu chứng khác. "
            "Teprotumumab gắn với IGF-1R → ức chế tín hiệu IGF-1R → "
            "giảm tăng sinh tế bào fibroblast và tế bào mỡ → giảm viêm và phù nề trong hốc mắt. "
            "Dẫn đến: giảm lồi mắt, cải thiện nhìn đôi, và cải thiện các triệu chứng khác của TED. "
            "Teprotumumab được dùng để điều trị TED active, moderate to severe, "
            "là thuốc đầu tiên được FDA phê duyệt đặc biệt cho TED. "
            "Teprotumumab có thể gây tăng đường huyết do ức chế tín hiệu insulin/IGF-1."
        ),
        "monitoring": [
            "Đáp ứng điều trị: lồi mắt (proptosis), nhìn đôi (diplopia), các triệu chứng khác",
            "Đường huyết - theo dõi tăng đường huyết",
            "Thính lực - theo dõi giảm thính lực (có thể không hồi phục)",
            "Chức năng gan (ALT, AST) - theo dõi tăng men gan",
            "Phản ứng truyền (infusion-related reactions) - theo dõi trong và sau truyền",
            "Dấu hiệu nhiễm trùng (sốt, ho, khó thở, tiểu buốt, v.v.)"
        ],
        "precautions": [
            "GIẢM THÍNH LỰC - phổ biến và có thể không hồi phục, cần theo dõi thính lực định kỳ",
            "TĂNG ĐƯỜNG HUYẾT - phổ biến, có thể cần điều chỉnh liều insulin hoặc thuốc hạ đường huyết",
            "PHẢN ỨNG TRUYỀN - phổ biến, cần premedication (corticosteroid, antihistamine, acetaminophen)",
            "NGUY CƠ NHIỄM TRÙNG - tăng nguy cơ nhiễm trùng do ức chế miễn dịch",
            "Ngừng teprotumumab nếu có nhiễm trùng nặng",
            "Thận trọng ở bệnh nhân đái tháo đường - tăng đường huyết",
            "Thận trọng ở bệnh nhân có tiền sử giảm thính lực"
        ],
        "pharmacokinetics": {
            "half_life": "~20 ngày (dài, cho phép dùng mỗi 3 tuần)",
            "onset": "Cải thiện triệu chứng trong vòng vài tuần đến vài tháng",
            "duration": "Dài (do half-life dài)",
            "protein_binding": "IgG1 monoclonal antibody",
            "metabolism": "Chuyển hóa qua hệ thống reticuloendothelial (RES)",
            "clearance": "Không phụ thuộc gan thận đáng kể"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh, tránh ánh sáng. Dung dịch pha loãng: dùng trong 4 giờ ở nhiệt độ phòng hoặc 24 giờ ở 2-8°C.",
        "black_box_warnings": (
            "GIẢM THÍNH LỰC - có thể không hồi phục. "
            "Cần theo dõi thính lực định kỳ. "
            "Ngừng teprotumumab nếu có giảm thính lực nghiêm trọng. "
            "TĂNG ĐƯỜNG HUYẾT - có thể nghiêm trọng. "
            "Cần theo dõi đường huyết và điều chỉnh liều insulin hoặc thuốc hạ đường huyết nếu cần."
        ),
        "drug_interactions": {
            "major": [
                {
                    "drug": "Insulin, thuốc hạ đường huyết (metformin, sulfonylureas)",
                    "mechanism": "Teprotumumab gây tăng đường huyết",
                    "effect": "Có thể cần tăng liều insulin hoặc thuốc hạ đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ. Điều chỉnh liều insulin hoặc thuốc hạ đường huyết nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc ức chế miễn dịch khác (corticosteroid liều cao)",
                    "mechanism": "Tăng ức chế miễn dịch",
                    "effect": "Tăng nguy cơ nhiễm trùng nặng",
                    "management": "Thận trọng. Theo dõi chặt chẽ dấu hiệu nhiễm trùng."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng teprotumumab hoặc bất kỳ thành phần nào",
                "Đang có nhiễm trùng nặng"
            ],
            "tương_đối": [
                "Tiền sử giảm thính lực - tăng nguy cơ giảm thính lực",
                "Đái tháo đường - tăng nguy cơ tăng đường huyết",
                "Tiền sử nhiễm trùng tái phát"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu hạn chế. Có thể dùng trong thai kỳ khi lợi ích vượt trội nguy cơ. Theo dõi chặt chẽ.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Kháng thể lớn, hấp thu qua đường tiêu hóa trẻ có thể hạn chế.",
                "recommendation": "Cân nhắc ngừng cho bú hoặc không dùng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Teprotumumab chuyển hóa qua RES, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng nguy cơ giảm thính lực",
                "Tăng đường huyết nặng",
                "Tăng nguy cơ phản ứng truyền nặng",
                "Tăng nguy cơ nhiễm trùng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ.",
            "treatment": [
                "Ngừng truyền ngay nếu có phản ứng nặng",
                "Điều trị phản ứng truyền: corticosteroid, antihistamine, epinephrine nếu cần",
                "Theo dõi thính lực chặt chẽ",
                "Theo dõi đường huyết và điều chỉnh liều insulin nếu cần",
                "Theo dõi dấu hiệu nhiễm trùng chặt chẽ",
                "Điều trị nhiễm trùng nếu có"
            ],
            "monitoring": "Thính lực, đường huyết, phản ứng truyền, dấu hiệu nhiễm trùng, dấu hiệu sinh tồn"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha loãng trong NaCl 0.9% hoặc Dextrose 5% theo hướng dẫn hãng.",
                "infusion_rate": "Truyền tĩnh mạch trong 90 phút.",
                "compatibility": ["NaCl 0.9%", "Dextrose 5%"],
                "incompatibility": ["Không pha với các thuốc khác."],
                "notes": "Cần premedication (corticosteroid, antihistamine, acetaminophen) trước mỗi liều. Theo dõi chặt chẽ trong và sau truyền, đặc biệt dấu hiệu giảm thính lực và tăng đường huyết."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Teprotumumab (Tepezza)",
                "UpToDate - Teprotumumab: Drug information",
                "Lexicomp - Teprotumumab monograph",
                "ATA Guidelines - Thyroid Eye Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved, large RCTs showing benefit in thyroid eye disease"
        }
    }
}

__all__ = ['MONOCLONAL_ANTIBODIES_ADCS_DRUGS']

