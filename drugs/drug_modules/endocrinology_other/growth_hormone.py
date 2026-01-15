"""
Endocrinology_Other - Growth_Hormone
"""

from typing import Dict, Any

ENDOCRINOLOGY_OTHER_GROWTH_HORMONE_DRUGS: Dict[str, Dict[str, Any]] = {
    "Voxzogo": {
        "group": "Endocrinology - C-type Natriuretic Peptide Analog",
        "vietnamese_name": "Vosoritide, Voxzogo",
        "administration": ["SC"],
        "indications": [
            "Cải thiện tăng trưởng ở trẻ em từ 5 tuổi trở lên bị achondroplasia với epiphyses mở"
        ],
        "contraindications": [
            "Dị ứng vosoritide hoặc bất kỳ thành phần nào",
            "Epiphyses đã đóng (không còn khả năng tăng trưởng)"
        ],
        "dosage": {
            "pediatric_5_18": "15 mcg/kg SC x 1 lần/ngày",
            "notes": "Tiêm dưới da hàng ngày. Liều dựa trên cân nặng. FDA phê duyệt 11/19/2021. Chỉ dùng cho trẻ em từ 5 tuổi trở lên với epiphyses mở."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nôn - phổ biến",
            "Đau khớp - phổ biến",
            "Giảm huyết áp - phổ biến",
            "Đau đầu - phổ biến",
            "Mệt mỏi - phổ biến",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Không có tương tác dược động học quan trọng",
            "Có thể tương tác với các thuốc hạ huyết áp"
        ],
        "pregnancy": "N/A (chỉ dùng cho trẻ em)",
        "mechanism_of_action": "Vosoritide là C-type natriuretic peptide (CNP) analog. CNP là một peptide tự nhiên có vai trò quan trọng trong sự phát triển xương. Trong achondroplasia, đột biến FGFR3 (fibroblast growth factor receptor 3) → tăng signaling FGFR3 → ức chế sự phát triển xương → chậm tăng trưởng. Vosoritide gắn với thụ thể natriuretic peptide B (NPR-B) → kích hoạt signaling pathway → ức chế FGFR3 signaling → giảm ức chế sự phát triển xương → tăng tăng trưởng. Dẫn đến: cải thiện tốc độ tăng trưởng ở trẻ em bị achondroplasia. Vosoritide được FDA phê duyệt 11/19/2021 để cải thiện tăng trưởng ở trẻ em từ 5 tuổi trở lên bị achondroplasia với epiphyses mở.",
        "monitoring": [
            "Tốc độ tăng trưởng (chiều cao) - đánh giá mỗi 3-6 tháng",
            "Huyết áp - giảm huyết áp phổ biến, theo dõi định kỳ",
            "Tình trạng epiphyses (X-ray) - chỉ dùng khi epiphyses mở",
            "Phản ứng tại chỗ tiêm",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "CHỈ DÙNG cho trẻ em từ 5 tuổi trở lên với epiphyses mở - không dùng khi epiphyses đã đóng",
            "Giảm huyết áp - phổ biến, theo dõi huyết áp định kỳ",
            "Phản ứng tại chỗ tiêm - phổ biến, thay đổi vị trí tiêm mỗi lần",
            "Cần tiêm hàng ngày - tuân thủ điều trị quan trọng",
            "Theo dõi tốc độ tăng trưởng định kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "~0.5 giờ",
            "onset": "Vài tuần đến vài tháng (tăng trưởng)",
            "duration": "Ngắn (cần dùng hàng ngày)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua neutral endopeptidase (NEP)",
            "clearance": "Thải trừ qua thận"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 3 tháng.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần lưu ý chỉ dùng cho trẻ em từ 5 tuổi trở lên với epiphyses mở.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc hạ huyết áp",
                    "mechanism": "Vosoritide có thể gây giảm huyết áp",
                    "effect": "Tăng nguy cơ hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng vosoritide hoặc bất kỳ thành phần nào",
                "Epiphyses đã đóng"
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Huyết áp thấp - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "N/A",
            "pregnancy_details": "Chỉ dùng cho trẻ em từ 5 tuổi trở lên. Không áp dụng cho phụ nữ có thai.",
            "lactation": {
                "safety": "N/A",
                "details": "Chỉ dùng cho trẻ em từ 5 tuổi trở lên.",
                "recommendation": "Không áp dụng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Vosoritide chuyển hóa qua NEP, không phụ thuộc gan đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ huyết áp nặng",
                "Phản ứng tại chỗ tiêm nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng vosoritide",
                "Điều trị hạ huyết áp nếu cần",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, huyết áp, phản ứng tại chỗ tiêm"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng tiêm sẵn (pre-filled pen)",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "notes": "Tiêm dưới da hàng ngày, 15 mcg/kg. Có thể tự tiêm sau khi được hướng dẫn. Bảo quản trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Vosoritide (Voxzogo)",
                "FDA Approval Date: 11/19/2021",
                "FDA-approved use: To improve growth in children five years of age and older with achondroplasia and open epiphyses",
                "UpToDate - Vosoritide: Drug information",
                "Lexicomp - Vosoritide monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 11/19/2021"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Growth rate (height) - every 3-6 months", "Blood pressure (periodically)", "Epiphyseal status (X-ray)", "Injection site reactions"]
        },
        "guideline_tags": [
            "FDA Drug Information - Vosoritide (Voxzogo)"
        ],
        "last_updated": "2025-02-18"
    },

    "Skytrofa": {
        "group": "Endocrinology - Long-Acting Growth Hormone",
        "vietnamese_name": "Lonapegsomatropin, Skytrofa",
        "administration": ["SC"],
        "indications": [
            "Điều trị chậm tăng trưởng do thiếu hụt hormone tăng trưởng nội sinh ở trẻ em từ 1 tuổi trở lên"
        ],
        "contraindications": [
            "Dị ứng lonapegsomatropin hoặc bất kỳ thành phần nào",
            "Khối u ác tính đang hoạt động",
            "Bệnh lý võng mạc tiểu đường tăng sinh (proliferative diabetic retinopathy)",
            "Đóng epiphyses (không còn khả năng tăng trưởng)"
        ],
        "dosage": {
            "pediatric_1_18": "0.24 mg/kg SC x 1 lần/tuần",
            "notes": "Tiêm dưới da mỗi tuần. Liều dựa trên cân nặng. FDA phê duyệt 8/25/2021. Dạng long-acting, chỉ cần tiêm 1 lần/tuần thay vì hàng ngày như growth hormone thông thường."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Phản ứng tại chỗ tiêm (đau, đỏ, sưng) - phổ biến",
            "Nhức đầu - phổ biến",
            "Nôn - phổ biến",
            "Đau khớp - phổ biến",
            "Tăng đường huyết - phổ biến",
            "Giảm đường huyết - hiếm",
            "Tăng áp lực nội sọ (intracranial hypertension) - hiếm nhưng nghiêm trọng",
            "Slipped capital femoral epiphysis (SCFE) - hiếm nhưng nghiêm trọng",
            "Dị ứng (hiếm)"
        ],
        "interactions": [
            "Glucocorticoid: có thể làm giảm hiệu quả của growth hormone",
            "Estrogen, testosterone: có thể ảnh hưởng đến hiệu quả",
            "Cyclosporine: có thể tăng nồng độ cyclosporine"
        ],
        "pregnancy": "N/A (chỉ dùng cho trẻ em)",
        "mechanism_of_action": "Lonapegsomatropin là growth hormone (somatropin) dạng long-acting, được gắn với một polymer để kéo dài thời gian tác dụng. Growth hormone là hormone quan trọng cho sự phát triển xương, cơ, và các mô khác. Trong thiếu hụt growth hormone, trẻ em chậm tăng trưởng. Lonapegsomatropin bổ sung growth hormone → kích thích sự phát triển xương, cơ → tăng tăng trưởng. Dạng long-acting cho phép tiêm 1 lần/tuần thay vì hàng ngày như growth hormone thông thường. Dẫn đến: cải thiện tốc độ tăng trưởng ở trẻ em thiếu hụt growth hormone. Lonapegsomatropin được FDA phê duyệt 8/25/2021 để điều trị chậm tăng trưởng do thiếu hụt hormone tăng trưởng nội sinh ở trẻ em từ 1 tuổi trở lên.",
        "monitoring": [
            "Tốc độ tăng trưởng (chiều cao) - đánh giá mỗi 3-6 tháng",
            "Đường huyết - tăng đường huyết phổ biến, giảm đường huyết hiếm",
            "Tình trạng epiphyses (X-ray) - chỉ dùng khi epiphyses mở",
            "Dấu hiệu tăng áp lực nội sọ (đau đầu, buồn nôn, nôn, rối loạn thị giác) - hiếm nhưng nghiêm trọng",
            "Dấu hiệu SCFE (đau hông, khập khiễng) - hiếm nhưng nghiêm trọng",
            "Phản ứng tại chỗ tiêm",
            "Chức năng tuyến giáp (TSH, T4) - growth hormone có thể ảnh hưởng"
        ],
        "precautions": [
            "CHỈ DÙNG cho trẻ em từ 1 tuổi trở lên với epiphyses mở - không dùng khi epiphyses đã đóng",
            "Tăng áp lực nội sọ - hiếm nhưng nghiêm trọng, theo dõi dấu hiệu (đau đầu, buồn nôn, nôn, rối loạn thị giác)",
            "SCFE - hiếm nhưng nghiêm trọng, theo dõi dấu hiệu (đau hông, khập khiễng)",
            "Tăng đường huyết - phổ biến, theo dõi đường huyết",
            "Giảm đường huyết - hiếm, đặc biệt ở trẻ em tiểu đường type 1",
            "Khối u ác tính - chống chỉ định ở khối u ác tính đang hoạt động",
            "Bệnh lý võng mạc tiểu đường tăng sinh - chống chỉ định",
            "Cần tiêm mỗi tuần - tuân thủ điều trị quan trọng",
            "Theo dõi tốc độ tăng trưởng định kỳ"
        ],
        "pharmacokinetics": {
            "half_life": "~25-30 giờ (dài hơn growth hormone thông thường ~3-4 giờ)",
            "onset": "Vài tuần đến vài tháng (tăng trưởng)",
            "duration": "1 tuần (dùng 1 lần/tuần)",
            "protein_binding": "Không rõ",
            "metabolism": "Chuyển hóa qua gan và thận",
            "clearance": "Thải trừ qua thận"
        },
        "storage": "Bảo quản trong tủ lạnh (2-8°C), tránh đông lạnh. Có thể để ở nhiệt độ phòng (≤25°C) tối đa 4 tuần.",
        "black_box_warnings": "Không có black box warning. Tuy nhiên, cần lưu ý nguy cơ tăng áp lực nội sọ, SCFE, và tăng đường huyết.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Glucocorticoid (prednisone, dexamethasone)",
                    "mechanism": "Glucocorticoid ức chế tác dụng của growth hormone",
                    "effect": "Giảm hiệu quả của lonapegsomatropin",
                    "management": "Thận trọng. Có thể cần tăng liều lonapegsomatropin."
                },
                {
                    "drug": "Cyclosporine",
                    "mechanism": "Growth hormone có thể ảnh hưởng đến chuyển hóa cyclosporine",
                    "effect": "Tăng nồng độ cyclosporine",
                    "management": "Thận trọng. Theo dõi nồng độ cyclosporine."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng lonapegsomatropin hoặc bất kỳ thành phần nào",
                "Khối u ác tính đang hoạt động",
                "Bệnh lý võng mạc tiểu đường tăng sinh",
                "Đóng epiphyses"
            ],
            "tương_đối": [
                "Suy thận nặng - thận trọng",
                "Tiểu đường - thận trọng, theo dõi đường huyết",
                "Tiền sử khối u - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "N/A",
            "pregnancy_details": "Chỉ dùng cho trẻ em từ 1 tuổi trở lên. Không áp dụng cho phụ nữ có thai.",
            "lactation": {
                "safety": "N/A",
                "details": "Chỉ dùng cho trẻ em từ 1 tuổi trở lên.",
                "recommendation": "Không áp dụng."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, dữ liệu hạn chế",
            "notes": "Lonapegsomatropin chuyển hóa qua gan và thận."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng đường huyết nặng",
                "Tăng áp lực nội sọ nặng",
                "Phản ứng tại chỗ tiêm nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng lonapegsomatropin",
                "Điều trị tăng đường huyết nếu cần",
                "Điều trị tăng áp lực nội sọ nếu cần",
                "Điều trị hỗ trợ"
            ],
            "monitoring": "Dấu hiệu sinh tồn, đường huyết, dấu hiệu tăng áp lực nội sọ, phản ứng tại chỗ tiêm"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "sc": {
                "reconstitution": "Dạng tiêm sẵn (pre-filled pen)",
                "injection_site": "Vùng bụng, đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần.",
                "notes": "Tiêm dưới da mỗi tuần, 0.24 mg/kg. Có thể tự tiêm sau khi được hướng dẫn. Bảo quản trong tủ lạnh, để ở nhiệt độ phòng 30 phút trước khi tiêm."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lonapegsomatropin (Skytrofa)",
                "FDA Approval Date: 8/25/2021",
                "FDA-approved use: To treat short stature due to inadequate secretion of endogenous growth hormone",
                "UpToDate - Lonapegsomatropin: Drug information",
                "Lexicomp - Lonapegsomatropin monograph"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA-approved 8/25/2021"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["Neurological (intracranial hypertension)", "Musculoskeletal (SCFE)"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Growth rate (height) - every 3-6 months", "Blood glucose (periodically)", "Epiphyseal status (X-ray)", "Signs of intracranial hypertension - CRITICAL", "Signs of SCFE - CRITICAL", "Injection site reactions", "Thyroid function (TSH, T4)"]
        },
    "Ngenla": {
                "group": "FDA Approved 2023",
                "vietnamese_name": "Somatrogon, Ngenla",
                "administration": [
                        "PO",
                ],
                "indications": [
                        "To treat growth failure due to inadequate secretion of endogenous growth hormone",
                ],
                "contraindications": [
                        "Dị ứng somatrogon hoặc bất kỳ thành phần nào",
                ],
                "dosage": {
                        "adult_standard": "Theo chỉ định của bác sĩ",
                        "notes": "FDA phê duyệt 2023. To treat growth failure due to inadequate secretion of endogenous growth hormone",
                },
                "renal_adjustment": {
                        "normal": "Không cần chỉnh liều",
                        "30_60": "Thận trọng",
                        "under_30": "Thận trọng, dữ liệu hạn chế",
                },
                "side_effects": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "interactions": [
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pregnancy": "C",
                "mechanism_of_action": "Somatrogon được FDA phê duyệt 2023 để to treat growth failure due to inadequate secretion of endogenous growth hormone. Cần bổ sung thông tin chi tiết về cơ chế tác dụng.",
                "monitoring": [
                        "Theo dõi đáp ứng điều trị",
                        "Theo dõi tác dụng phụ",
                ],
                "precautions": [
                        "Dị ứng somatrogon",
                        "Cần bổ sung thông tin từ tài liệu FDA",
                ],
                "pharmacokinetics": {
                        "half_life": "Cần bổ sung",
                        "onset": "Cần bổ sung",
                        "duration": "Cần bổ sung",
                        "protein_binding": "Cần bổ sung",
                        "metabolism": "Cần bổ sung",
                        "clearance": "Cần bổ sung",
                },
                "storage": "Bảo quản theo hướng dẫn của nhà sản xuất",
                "black_box_warnings": "Cần kiểm tra tài liệu FDA",
                "drug_interactions": {
                        "major": [],
                        "moderate": [],
                        "minor": [],
                },
                "contraindications_detail": {
                        "tuyệt_đối": [
                                "Dị ứng somatrogon hoặc bất kỳ thành phần nào",
                        ],
                        "tương_đối": [],
                },
                "pregnancy_lactation": {
                        "fda_category": "C",
                        "pregnancy_details": "Cần bổ sung thông tin từ tài liệu FDA",
                        "lactation": {
                                "safety": "Unknown",
                                "details": "Chưa biết có bài tiết vào sữa mẹ hay không",
                                "recommendation": "Thận trọng khi cho con bú",
                        },
                },
                "hepatic_adjustment": {
                        "mild": "Không đổi",
                        "moderate": "Thận trọng",
                        "severe": "Thận trọng, dữ liệu hạn chế",
                        "notes": "Cần bổ sung thông tin từ tài liệu FDA",
                },
                "overdose_management": {
                        "symptoms": [
                                "Cần bổ sung",
                        ],
                        "antidote": "Không có antidote đặc hiệu",
                        "treatment": [
                                "Điều trị hỗ trợ",
                        ],
                        "monitoring": "Theo dõi dấu hiệu sinh tồn",
                },
                "reversal_agents": {
                        "available": False,
                        "agents": [],
                },
                "administration_instructions": {
                        "oral": {
                                "with_food": "Cần bổ sung",
                                "timing": "Cần bổ sung",
                        },
                },
                "references": {
                        "primary_sources": [
                                "FDA Drug Label - Somatrogon (Ngenla)",
                                "FDA Approval Date: 2023",
                                "FDA-approved use: To treat growth failure due to inadequate secretion of endogenous growth hormone",
                        ],
                        "last_updated": "2026-01-15",
                        "evidence_level": "A - FDA-approved 2023",
                },
                "risk_flags": {
                        "high_alert": False,
                        "narrow_therapeutic_index": False,
                        "bleeding_risk": False,
                        "organ_toxicity": [],
                        "qt_prolongation": False,
                        "hepatotoxicity": False,
                        "nephrotoxicity": False,
                        "requires_monitoring": [
                                "Clinical response",
                                "Adverse effects",
                        ],
                },
                "guideline_tags": [
                        "FDA Drug Information - Somatrogon (Ngenla)",
                ],
                "last_updated": "2026-01-15",
        },
        "guideline_tags": [
            "FDA Drug Information - Lonapegsomatropin (Skytrofa)"
        ],
        "last_updated": "2025-02-18"
    }
}

__all__ = ['ENDOCRINOLOGY_OTHER_GROWTH_HORMONE_DRUGS']
