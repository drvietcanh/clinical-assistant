"""
Bone and Joint Supplements (Thuốc bổ sung xương khớp)
Glucosamine, Chondroitin, MSM, Calcium/Vitamin D combinations
"""

BONE_JOINT_SUPPLEMENTS = {
    "Glucosamine": {
        "group": "Rheumatology - Joint Supplement (Glucosamine)",
        "vietnamese_name": "Glucosamine, Glucosamine sulfate, Glucosamine hydrochloride",
        "brand_names": {
            "common": [
                "Glucosamine sulfate",
                "Glucosamine HCl"
            ],
            "vietnam": [
                "Glucosamine Orihiro 1500mg",
                "Glucosamine Stada",
                "Glucosamine 500mg",
                "Viên uống Glucosamine"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau khớp, cứng khớp",
            "Hỗ trợ tái tạo sụn khớp",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với glucosamine hoặc động vật có vỏ (shellfish)",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)",
            "Bệnh nhân tiểu đường (có thể ảnh hưởng đường huyết)"
        ],
        "dosage": {
            "adult_osteoarthritis": "1500mg PO mỗi ngày, chia 1-3 lần, uống với thức ăn",
            "maintenance": "1000-1500mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Nên dùng kết hợp với chondroitin để tăng hiệu quả. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (thường gặp)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng động vật có vỏ)",
            "Tăng đường huyết (ở bệnh nhân tiểu đường)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc tiểu đường: có thể ảnh hưởng đường huyết - theo dõi đường huyết",
            "Thuốc hóa trị (doxorubicin, etoposide): có thể giảm hiệu quả"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Glucosamine là một amino monosaccharide, là thành phần tự nhiên của glycosaminoglycans "
            "trong sụn khớp và dịch khớp. Glucosamine sulfate được chuyển hóa thành các thành phần "
            "của proteoglycans và glycosaminoglycans, là các phân tử quan trọng trong cấu trúc sụn. "
            "Glucosamine có thể: (1) Kích thích tổng hợp proteoglycans và collagen trong sụn, "
            "(2) Ức chế các enzyme phá hủy sụn (collagenase, phospholipase A2), "
            "(3) Giảm viêm và đau khớp, (4) Cải thiện chức năng khớp. "
            "Tuy nhiên, bằng chứng lâm sàng về hiệu quả còn tranh cãi, một số nghiên cứu cho thấy "
            "hiệu quả vừa phải trong viêm khớp xương, một số nghiên cứu khác không thấy hiệu quả rõ ràng."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 4-8 tuần)",
            "Đường huyết (ở bệnh nhân tiểu đường)",
            "INR (nếu dùng với warfarin)",
            "Chức năng gan (nếu dùng kéo dài)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân, có thể không hiệu quả ở một số bệnh nhân",
            "Thận trọng ở bệnh nhân tiểu đường - theo dõi đường huyết",
            "Thận trọng ở bệnh nhân dị ứng động vật có vỏ (glucosamine thường chiết xuất từ vỏ tôm, cua)",
            "Có thể mất 4-8 tuần để thấy hiệu quả",
            "Nên dùng kết hợp với chondroitin để tăng hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Khoảng 15 giờ",
            "onset": "Hiệu quả có thể xuất hiện sau 4-8 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa ở gan, thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Glucosamine có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu glucosamine. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tiểu đường (metformin, insulin, sulfonylureas)",
                    "mechanism": "Glucosamine có thể ảnh hưởng đến chuyển hóa glucose",
                    "effect": "Có thể tăng hoặc giảm đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ, điều chỉnh liều thuốc tiểu đường nếu cần."
                },
                {
                    "drug": "Thuốc hóa trị (doxorubicin, etoposide)",
                    "mechanism": "Glucosamine có thể giảm hiệu quả của một số thuốc hóa trị",
                    "effect": "Giảm hiệu quả điều trị ung thư",
                    "management": "Thận trọng. Cân nhắc ngừng glucosamine trong quá trình hóa trị."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glucosamine hoặc động vật có vỏ (shellfish)"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân tiểu đường - có thể ảnh hưởng đường huyết",
                "Suy thận nặng - dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Không khuyến cáo",
            "notes": "Glucosamine chuyển hóa ở gan"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Tăng đường huyết (ở bệnh nhân tiểu đường)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng glucosamine",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi đường huyết nếu cần"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 1-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Nên dùng kết hợp với chondroitin."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine and Chondroitin for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Cochrane Review - Glucosamine for osteoarthritis"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (common)",
                "metabolic": "Hyperglycemia risk (in diabetes patients)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Blood glucose (in diabetes patients)",
                "INR (if co-administered with warfarin)",
                "Joint pain/stiffness (efficacy assessment after 4-8 weeks)",
                "Allergic reactions (especially in shellfish allergy)"
            ],
            "look_alike_sound_alike": ["Glucosamine", "Glucosamine sulfate", "Glucosamine HCl"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements",
            "Cochrane Review - Glucosamine"
        ],
        "last_updated": "2025-01-20"
    },

    "Chondroitin": {
        "group": "Rheumatology - Joint Supplement (Chondroitin)",
        "vietnamese_name": "Chondroitin, Chondroitin sulfate",
        "brand_names": {
            "common": [
                "Chondroitin sulfate",
                "Chondroitin sodium"
            ],
            "vietnam": [
                "Chondroitin 400mg",
                "Chondroitin Stada",
                "Viên uống Chondroitin"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau khớp, cứng khớp",
            "Hỗ trợ tái tạo sụn khớp",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với chondroitin",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)"
        ],
        "dosage": {
            "adult_osteoarthritis": "800-1200mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "maintenance": "800-1200mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Nên dùng kết hợp với glucosamine để tăng hiệu quả. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (ít gặp hơn glucosamine)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc chống đông khác: có thể tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Chondroitin sulfate là một glycosaminoglycan, là thành phần tự nhiên của sụn khớp, "
            "xương và các mô liên kết. Chondroitin có thể: (1) Kích thích tổng hợp proteoglycans "
            "và collagen trong sụn, (2) Ức chế các enzyme phá hủy sụn (hyaluronidase, elastase, "
            "collagenase), (3) Tăng sản xuất dịch khớp, cải thiện bôi trơn khớp, "
            "(4) Giảm viêm và đau khớp, (5) Cải thiện chức năng khớp. "
            "Chondroitin thường được dùng kết hợp với glucosamine để tăng hiệu quả. "
            "Bằng chứng lâm sàng về hiệu quả còn tranh cãi, một số nghiên cứu cho thấy hiệu quả "
            "vừa phải trong viêm khớp xương, đặc biệt khi kết hợp với glucosamine."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 4-8 tuần)",
            "INR (nếu dùng với warfarin hoặc thuốc chống đông khác)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân dùng thuốc chống đông - theo dõi INR và dấu hiệu chảy máu",
            "Có thể mất 4-8 tuần để thấy hiệu quả",
            "Nên dùng kết hợp với glucosamine để tăng hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 4-8 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Chondroitin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu chondroitin. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc chống đông khác (heparin, enoxaparin, dabigatran, rivaroxaban)",
                    "mechanism": "Chondroitin có thể tăng tác dụng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với chondroitin"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Suy thận nặng - dữ liệu hạn chế",
                "Bệnh nhân dùng thuốc chống đông - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Chondroitin không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng chondroitin",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Nên dùng kết hợp với glucosamine."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine and Chondroitin for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Cochrane Review - Chondroitin for osteoarthritis"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (less common than glucosamine)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "INR (if co-administered with warfarin) - CRITICAL",
                "Bleeding signs (if co-administered with anticoagulants) - CRITICAL",
                "Joint pain/stiffness (efficacy assessment after 4-8 weeks)",
                "Allergic reactions (rare)"
            ],
            "look_alike_sound_alike": ["Chondroitin", "Chondroitin sulfate"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements",
            "Cochrane Review - Chondroitin"
        ],
        "last_updated": "2025-01-20"
    },

    "Glucosamine + Chondroitin": {
        "group": "Rheumatology - Joint Supplement (Combination)",
        "vietnamese_name": "Glucosamine + Chondroitin, Triple Flex",
        "brand_names": {
            "common": [
                "Glucosamine + Chondroitin",
                "Triple Flex"
            ],
            "vietnam": [
                "Glucosamine + Chondroitin 500/400mg",
                "Triple Flex Nature Made",
                "Viên uống Glucosamine Chondroitin"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau khớp, cứng khớp",
            "Hỗ trợ tái tạo sụn khớp",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với glucosamine, chondroitin hoặc động vật có vỏ",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)",
            "Bệnh nhân tiểu đường (glucosamine có thể ảnh hưởng đường huyết)"
        ],
        "dosage": {
            "adult_osteoarthritis": "Glucosamine 1500mg + Chondroitin 1200mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "alternative": "Glucosamine 1000mg + Chondroitin 800mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Kết hợp glucosamine và chondroitin có thể hiệu quả hơn dùng đơn độc. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (thường gặp)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng động vật có vỏ)",
            "Tăng đường huyết (ở bệnh nhân tiểu đường, do glucosamine)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc tiểu đường: có thể ảnh hưởng đường huyết - theo dõi đường huyết",
            "Thuốc chống đông khác: có thể tăng nguy cơ chảy máu"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Kết hợp glucosamine và chondroitin có tác dụng hiệp đồng trong hỗ trợ sức khỏe khớp. "
            "Glucosamine: kích thích tổng hợp proteoglycans và collagen trong sụn, ức chế các enzyme "
            "phá hủy sụn. Chondroitin: kích thích tổng hợp proteoglycans, ức chế các enzyme phá hủy "
            "sụn, tăng sản xuất dịch khớp. Tác dụng hiệp đồng: (1) Tăng tổng hợp và giảm phá hủy sụn, "
            "(2) Cải thiện bôi trơn khớp, (3) Giảm viêm và đau khớp, (4) Cải thiện chức năng khớp. "
            "Một số nghiên cứu cho thấy kết hợp glucosamine và chondroitin có thể hiệu quả hơn dùng đơn độc."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 4-8 tuần)",
            "Đường huyết (ở bệnh nhân tiểu đường)",
            "INR (nếu dùng với warfarin)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân tiểu đường - theo dõi đường huyết",
            "Thận trọng ở bệnh nhân dị ứng động vật có vỏ",
            "Thận trọng ở bệnh nhân dùng thuốc chống đông - theo dõi INR và dấu hiệu chảy máu",
            "Có thể mất 4-8 tuần để thấy hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Glucosamine: ~15 giờ; Chondroitin: không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 4-8 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cả glucosamine và chondroitin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tiểu đường (metformin, insulin, sulfonylureas)",
                    "mechanism": "Glucosamine có thể ảnh hưởng đến chuyển hóa glucose",
                    "effect": "Có thể tăng hoặc giảm đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ, điều chỉnh liều thuốc tiểu đường nếu cần."
                },
                {
                    "drug": "Thuốc chống đông khác (heparin, enoxaparin, dabigatran, rivaroxaban)",
                    "mechanism": "Chondroitin có thể tăng tác dụng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glucosamine, chondroitin hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân tiểu đường - glucosamine có thể ảnh hưởng đường huyết",
                "Suy thận nặng - dữ liệu hạn chế",
                "Bệnh nhân dùng thuốc chống đông - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Không khuyến cáo",
            "notes": "Glucosamine chuyển hóa ở gan, chondroitin không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Tăng đường huyết (ở bệnh nhân tiểu đường)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi đường huyết nếu cần"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Kết hợp có thể hiệu quả hơn dùng đơn độc."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine and Chondroitin for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "GAIT Study - Glucosamine/Chondroitin Arthritis Intervention Trial"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (common)",
                "metabolic": "Hyperglycemia risk (in diabetes patients, due to glucosamine)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Blood glucose (in diabetes patients)",
                "INR (if co-administered with warfarin) - CRITICAL",
                "Bleeding signs (if co-administered with anticoagulants) - CRITICAL",
                "Joint pain/stiffness (efficacy assessment after 4-8 weeks)",
                "Allergic reactions (especially in shellfish allergy)"
            ],
            "look_alike_sound_alike": ["Glucosamine + Chondroitin", "Triple Flex"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements",
            "GAIT Study - Glucosamine/Chondroitin"
        ],
        "last_updated": "2025-01-20"
    },

    "MSM (Methylsulfonylmethane)": {
        "group": "Rheumatology - Joint Supplement (MSM)",
        "vietnamese_name": "MSM, Methylsulfonylmethane",
        "brand_names": {
            "common": [
                "MSM",
                "Methylsulfonylmethane"
            ],
            "vietnam": [
                "MSM 1000mg",
                "MSM Stada",
                "Viên uống MSM"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau khớp, cứng khớp",
            "Hỗ trợ giảm viêm khớp",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với MSM",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)"
        ],
        "dosage": {
            "adult_osteoarthritis": "1500-3000mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "maintenance": "1000-2000mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Có thể dùng kết hợp với glucosamine và chondroitin. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (ít gặp)",
            "Đau đầu",
            "Mất ngủ (hiếm)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "MSM (Methylsulfonylmethane) là một hợp chất chứa lưu huỳnh tự nhiên, có trong nhiều loại thực phẩm. "
            "MSM có thể: (1) Giảm viêm khớp bằng cách ức chế các cytokine gây viêm (TNF-α, IL-1, IL-6), "
            "(2) Giảm đau khớp, (3) Cải thiện tính linh hoạt của khớp, (4) Hỗ trợ sửa chữa mô sụn. "
            "MSM cung cấp lưu huỳnh, là thành phần quan trọng của collagen và các mô liên kết. "
            "Bằng chứng lâm sàng về hiệu quả còn hạn chế, một số nghiên cứu nhỏ cho thấy hiệu quả vừa phải "
            "trong việc giảm đau và cải thiện chức năng khớp ở bệnh nhân viêm khớp xương."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 2-4 tuần)",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Có thể mất 2-4 tuần để thấy hiệu quả",
            "Có thể dùng kết hợp với glucosamine và chondroitin",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 2-4 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với MSM"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Suy thận nặng - dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "MSM không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng MSM",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Có thể dùng kết hợp với glucosamine và chondroitin."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - MSM for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Journal of Alternative and Complementary Medicine - MSM studies"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "C - Bằng chứng lâm sàng hạn chế, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (uncommon)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Joint pain/stiffness (efficacy assessment after 2-4 weeks)",
                "Allergic reactions (rare)"
            ],
            "look_alike_sound_alike": ["MSM", "Methylsulfonylmethane"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    },

    "Calcium + Vitamin D3": {
        "group": "Rheumatology - Bone Health Supplement (Calcium + Vitamin D)",
        "vietnamese_name": "Calcium + Vitamin D3, Canxi + Vitamin D3",
        "brand_names": {
            "common": [
                "Calcium + Vitamin D3",
                "Calcium Carbonate + Cholecalciferol"
            ],
            "vietnam": [
                "Calcium + D3 500/200IU",
                "Calcium + D3 600/400IU",
                "Calcium + D3 Stada",
                "Canxi + Vitamin D3"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Bổ sung calci và vitamin D cho sức khỏe xương",
            "Dự phòng và điều trị loãng xương",
            "Hỗ trợ điều trị thiếu calci và vitamin D",
            "Hỗ trợ sức khỏe xương ở phụ nữ mãn kinh, người cao tuổi"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Tăng calci niệu",
            "Sỏi thận do calci",
            "Suy thận nặng",
            "Dị ứng với calci hoặc vitamin D"
        ],
        "dosage": {
            "adult_bone_health": "Calcium 1000-1200mg + Vitamin D3 400-800IU PO mỗi ngày, chia 1-2 lần, uống với thức ăn",
            "adult_osteoporosis": "Calcium 1200-1500mg + Vitamin D3 800-1000IU PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "elderly": "Calcium 1200mg + Vitamin D3 800-1000IU PO mỗi ngày",
            "notes": "Nên uống với thức ăn để tăng hấp thu. Không uống quá 500-600mg calci mỗi lần để tối ưu hấp thu. Uống cách xa các thuốc khác ít nhất 2 giờ."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, theo dõi calci máu",
            "under_30": "Không khuyến cáo, nguy cơ tăng calci máu"
        },
        "side_effects": [
            "Táo bón (thường gặp, đặc biệt với calcium carbonate)",
            "Đầy hơi, khó chịu dạ dày",
            "Tăng calci máu (nếu dùng quá liều)",
            "Tăng calci niệu, sỏi thận (nếu dùng quá liều)",
            "Buồn nôn, nôn (hiếm)"
        ],
        "interactions": [
            "Bisphosphonates, denosumab: calci giảm hấp thu - dùng cách xa ít nhất 30 phút",
            "Tetracyclines, quinolones: calci giảm hấp thu - dùng cách xa ít nhất 2 giờ",
            "Levothyroxine: calci giảm hấp thu - dùng cách xa ít nhất 4 giờ",
            "Sắt: calci giảm hấp thu sắt - dùng cách xa ít nhất 2 giờ",
            "Digoxin: tăng calci máu có thể tăng độc tính digoxin",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu"
        ],
        "pregnancy": "A - An toàn khi dùng với liều khuyến cáo",
        "mechanism_of_action": (
            "Calcium: là khoáng chất quan trọng nhất cho sức khỏe xương, chiếm khoảng 99% calci trong cơ thể "
            "nằm trong xương và răng. Calci cần thiết cho: (1) Hình thành và duy trì xương, răng, "
            "(2) Co cơ, dẫn truyền thần kinh, đông máu, (3) Chức năng tim mạch. "
            "Vitamin D3 (Cholecalciferol): là dạng hoạt động của vitamin D, cần thiết cho: "
            "(1) Hấp thu calci từ ruột, (2) Tái hấp thu calci ở thận, (3) Khoáng hóa xương, "
            "(4) Điều hòa nồng độ calci và phospho trong máu. Vitamin D3 được chuyển hóa thành "
            "calcitriol (1,25-dihydroxyvitamin D3) ở thận, là dạng hoạt động. "
            "Kết hợp calci và vitamin D3 có tác dụng hiệp đồng: vitamin D3 tăng hấp thu calci, "
            "cả hai cùng hỗ trợ sức khỏe xương và dự phòng loãng xương."
        ),
        "monitoring": [
            "Calci máu (đặc biệt khi dùng liều cao hoặc suy thận)",
            "Calci niệu (nếu có nguy cơ sỏi thận)",
            "25-hydroxyvitamin D (nếu thiếu vitamin D)",
            "Creatinine, eGFR (nếu suy thận)"
        ],
        "precautions": [
            "QUAN TRỌNG: Không uống quá 500-600mg calci mỗi lần để tối ưu hấp thu",
            "Uống với thức ăn để tăng hấp thu",
            "Uống cách xa các thuốc khác ít nhất 2 giờ (đặc biệt bisphosphonates, tetracyclines, quinolones, levothyroxine, sắt)",
            "Thận trọng ở bệnh nhân suy thận - nguy cơ tăng calci máu",
            "Thận trọng ở bệnh nhân sỏi thận - nguy cơ tăng calci niệu",
            "Thận trọng khi dùng với thiazide diuretics - tăng nguy cơ tăng calci máu",
            "Calcium carbonate: cần acid dạ dày để hấp thu tốt, nên uống với thức ăn",
            "Calcium citrate: có thể uống lúc đói, hấp thu tốt hơn ở người giảm acid dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Calcium: không áp dụng; Vitamin D3: ~2-3 tuần",
            "onset": "Tác dụng trên xương: vài tháng đến vài năm",
            "duration": "Cần dùng liên tục để duy trì sức khỏe xương",
            "protein_binding": "Calcium: ~40-50%; Vitamin D3: gắn với protein vận chuyển",
            "clearance": "Calcium: thải qua thận và phân; Vitamin D3: chuyển hóa ở gan và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Bisphosphonates (alendronate, risedronate, ibandronate)",
                    "mechanism": "Calci tạo phức hợp không hòa tan với bisphosphonates, giảm hấp thu",
                    "effect": "Giảm hấp thu bisphosphonates, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 30 phút. Uống bisphosphonate trước, sau đó mới uống calci."
                },
                {
                    "drug": "Denosumab",
                    "mechanism": "Calci có thể ảnh hưởng đến hấp thu denosumab",
                    "effect": "Có thể giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 30 phút."
                },
                {
                    "drug": "Tetracyclines (doxycycline, minocycline)",
                    "mechanism": "Calci tạo phức hợp không hòa tan với tetracyclines, giảm hấp thu",
                    "effect": "Giảm hấp thu tetracyclines, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 2 giờ."
                },
                {
                    "drug": "Quinolones (ciprofloxacin, levofloxacin)",
                    "mechanism": "Calci tạo phức hợp không hòa tan với quinolones, giảm hấp thu",
                    "effect": "Giảm hấp thu quinolones, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 2 giờ."
                },
                {
                    "drug": "Levothyroxine",
                    "mechanism": "Calci giảm hấp thu levothyroxine",
                    "effect": "Giảm hấp thu levothyroxine, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 4 giờ."
                }
            ],
            "moderate": [
                {
                    "drug": "Sắt (iron supplements)",
                    "mechanism": "Calci giảm hấp thu sắt",
                    "effect": "Giảm hấp thu sắt, giảm hiệu quả",
                    "management": "Dùng cách xa ít nhất 2 giờ."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Tăng calci máu có thể tăng độc tính digoxin",
                    "effect": "Tăng nguy cơ độc tính digoxin",
                    "management": "Theo dõi calci máu và nồng độ digoxin."
                },
                {
                    "drug": "Thiazide diuretics (hydrochlorothiazide, chlorthalidone)",
                    "mechanism": "Thiazide giảm thải calci qua thận, calci bổ sung tăng calci máu",
                    "effect": "Tăng nguy cơ tăng calci máu",
                    "management": "Theo dõi calci máu chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Tăng calci máu",
                "Tăng calci niệu",
                "Sỏi thận do calci",
                "Dị ứng với calci hoặc vitamin D"
            ],
            "tương_đối": [
                "Suy thận nặng - nguy cơ tăng calci máu",
                "Bệnh nhân dùng thiazide diuretics - tăng nguy cơ tăng calci máu",
                "Bệnh nhân sarcoidosis - tăng nhạy cảm với vitamin D"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "An toàn khi dùng với liều khuyến cáo. Calci và vitamin D cần thiết cho phát triển xương thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "An toàn khi cho con bú. Calci và vitamin D bài tiết vào sữa mẹ ở nồng độ thấp, cần thiết cho phát triển xương trẻ sơ sinh.",
                "recommendation": "Có thể dùng khi cho con bú với liều khuyến cáo."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Thận trọng với vitamin D (chuyển hóa ở gan)",
            "notes": "Vitamin D3 chuyển hóa ở gan thành 25-hydroxyvitamin D3"
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu (buồn nôn, nôn, yếu cơ, rối loạn nhịp tim, sỏi thận)",
                "Tăng calci niệu, sỏi thận",
                "Táo bón nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng calci và vitamin D",
                "Bù dịch (saline IV) để tăng thải calci qua thận",
                "Furosemide (loop diuretic) để tăng thải calci",
                "Calcitonin hoặc bisphosphonate nếu tăng calci máu nặng",
                "Điều trị sỏi thận nếu có"
            ],
            "monitoring": "Calci máu, calci niệu, chức năng thận, ECG, dấu hiệu sinh tồn"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tăng hấp thu",
                "timing": "Uống 1-3 lần/ngày, không quá 500-600mg calci mỗi lần. Uống cách xa các thuốc khác ít nhất 2 giờ.",
                "notes": "QUAN TRỌNG: Không uống quá 500-600mg calci mỗi lần để tối ưu hấp thu. Uống cách xa bisphosphonates ít nhất 30 phút, tetracyclines/quinolones/levothyroxine/sắt ít nhất 2-4 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "NOF Guidelines - Calcium and Vitamin D for Bone Health",
                "IOM - Dietary Reference Intakes for Calcium and Vitamin D",
                "Endocrine Society - Vitamin D Deficiency Guidelines"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "A - Khuyến cáo mạnh cho sức khỏe xương"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "renal": "Hypercalcemia, hypercalciuria, kidney stones (if overdose)",
                "gastrointestinal": "Constipation (common, especially with calcium carbonate)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Serum calcium (especially with high doses or renal impairment)",
                "Urine calcium (if kidney stone risk)",
                "25-hydroxyvitamin D (if vitamin D deficiency)",
                "Renal function (creatinine, eGFR - if renal impairment)",
                "Drug interactions (bisphosphonates, tetracyclines, quinolones, levothyroxine, iron - take at least 2-4 hours apart)"
            ],
            "look_alike_sound_alike": ["Calcium + Vitamin D3", "Calcium Carbonate + Cholecalciferol"]
        },
        "guideline_tags": [
            "NOF Guidelines - Calcium and Vitamin D for Bone Health",
            "IOM - Dietary Reference Intakes",
            "Endocrine Society - Vitamin D Deficiency Guidelines",
            "WHO Essential Medicines List"
        ],
        "last_updated": "2025-01-20"
    },

    "Glucosamine + MSM": {
        "group": "Rheumatology - Joint Supplement (Combination - Glucosamine + MSM)",
        "vietnamese_name": "Glucosamine + MSM, Glucosamine HCl + Methylsulfonylmethane",
        "brand_names": {
            "common": [
                "Glucosamine + MSM",
                "Kirkland Glucosamine HCl 1500mg With MSM"
            ],
            "vietnam": [
                "Glucosamine + MSM 1500/1500mg",
                "Kirkland Glucosamine + MSM",
                "Viên uống Glucosamine MSM"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau nhức, sưng viêm khớp",
            "Hỗ trợ phục hồi sụn khớp",
            "Tăng độ đàn hồi và linh hoạt cho khớp",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với glucosamine, MSM hoặc động vật có vỏ",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)",
            "Bệnh nhân tiểu đường (glucosamine có thể ảnh hưởng đường huyết)"
        ],
        "dosage": {
            "adult_osteoarthritis": "Glucosamine 1500mg + MSM 1500mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "alternative": "Glucosamine 1000mg + MSM 1000mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Kết hợp glucosamine và MSM có tác dụng hiệp đồng: glucosamine hỗ trợ tái tạo sụn, MSM giảm viêm và đau. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (thường gặp)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng động vật có vỏ)",
            "Tăng đường huyết (ở bệnh nhân tiểu đường, do glucosamine)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc tiểu đường: có thể ảnh hưởng đường huyết - theo dõi đường huyết"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Kết hợp glucosamine và MSM có tác dụng hiệp đồng trong hỗ trợ sức khỏe khớp. "
            "Glucosamine: kích thích tổng hợp proteoglycans và collagen trong sụn, ức chế các enzyme "
            "phá hủy sụn, hỗ trợ tái tạo sụn khớp. MSM (Methylsulfonylmethane): giảm viêm khớp bằng cách "
            "ức chế các cytokine gây viêm (TNF-α, IL-1, IL-6), giảm đau khớp, cải thiện tính linh hoạt "
            "của khớp, cung cấp lưu huỳnh cho collagen và mô liên kết. Tác dụng hiệp đồng: "
            "(1) Glucosamine tái tạo sụn, MSM giảm viêm và đau, (2) Cải thiện chức năng khớp nhanh hơn "
            "so với dùng đơn độc, (3) Hỗ trợ toàn diện cho sức khỏe khớp."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 2-4 tuần)",
            "Đường huyết (ở bệnh nhân tiểu đường)",
            "INR (nếu dùng với warfarin)",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân tiểu đường - theo dõi đường huyết",
            "Thận trọng ở bệnh nhân dị ứng động vật có vỏ",
            "Có thể mất 2-4 tuần để thấy hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Glucosamine: ~15 giờ; MSM: không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 2-4 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Glucosamine có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tiểu đường (metformin, insulin, sulfonylureas)",
                    "mechanism": "Glucosamine có thể ảnh hưởng đến chuyển hóa glucose",
                    "effect": "Có thể tăng hoặc giảm đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ, điều chỉnh liều thuốc tiểu đường nếu cần."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glucosamine, MSM hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân tiểu đường - glucosamine có thể ảnh hưởng đường huyết",
                "Suy thận nặng - dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Không khuyến cáo",
            "notes": "Glucosamine chuyển hóa ở gan, MSM không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Tăng đường huyết (ở bệnh nhân tiểu đường)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi đường huyết nếu cần"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Kết hợp có tác dụng hiệp đồng."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine and MSM for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Journal of Alternative and Complementary Medicine - MSM studies"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (common)",
                "metabolic": "Hyperglycemia risk (in diabetes patients, due to glucosamine)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Blood glucose (in diabetes patients)",
                "INR (if co-administered with warfarin) - CRITICAL",
                "Joint pain/stiffness (efficacy assessment after 2-4 weeks)",
                "Allergic reactions (especially in shellfish allergy)"
            ],
            "look_alike_sound_alike": ["Glucosamine + MSM", "Kirkland Glucosamine + MSM"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    },

    "Glucosamine + Chondroitin + MSM": {
        "group": "Rheumatology - Joint Supplement (Combination - Triple)",
        "vietnamese_name": "Glucosamine + Chondroitin + MSM, Triple Flex",
        "brand_names": {
            "common": [
                "Glucosamine + Chondroitin + MSM",
                "Triple Flex",
                "Triple Flex Nature Made"
            ],
            "vietnam": [
                "Glucosamine + Chondroitin + MSM 1500/1200/1500mg",
                "Triple Flex Nature Made",
                "Viên uống Triple Flex"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau nhức, sưng viêm khớp",
            "Hỗ trợ phục hồi và tái tạo sụn khớp",
            "Tăng độ đàn hồi và linh hoạt cho khớp",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với glucosamine, chondroitin, MSM hoặc động vật có vỏ",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)",
            "Bệnh nhân tiểu đường (glucosamine có thể ảnh hưởng đường huyết)"
        ],
        "dosage": {
            "adult_osteoarthritis": "Glucosamine 1500mg + Chondroitin 1200mg + MSM 1500mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "alternative": "Glucosamine 1000mg + Chondroitin 800mg + MSM 1000mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Kết hợp ba thành phần có tác dụng hiệp đồng mạnh: glucosamine và chondroitin tái tạo sụn, MSM giảm viêm và đau. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (thường gặp)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng động vật có vỏ)",
            "Tăng đường huyết (ở bệnh nhân tiểu đường, do glucosamine)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc tiểu đường: có thể ảnh hưởng đường huyết - theo dõi đường huyết",
            "Thuốc chống đông khác: có thể tăng nguy cơ chảy máu (do chondroitin)"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Kết hợp glucosamine, chondroitin và MSM có tác dụng hiệp đồng mạnh trong hỗ trợ sức khỏe khớp. "
            "Glucosamine: kích thích tổng hợp proteoglycans và collagen trong sụn, ức chế các enzyme phá hủy sụn. "
            "Chondroitin: kích thích tổng hợp proteoglycans, ức chế các enzyme phá hủy sụn, tăng sản xuất dịch khớp, "
            "cải thiện bôi trơn khớp. MSM: giảm viêm khớp bằng cách ức chế các cytokine gây viêm, giảm đau khớp, "
            "cải thiện tính linh hoạt của khớp, cung cấp lưu huỳnh cho collagen. Tác dụng hiệp đồng: "
            "(1) Glucosamine và chondroitin tái tạo và bảo vệ sụn, (2) MSM giảm viêm và đau, "
            "(3) Cải thiện chức năng khớp toàn diện và nhanh hơn so với dùng đơn độc, "
            "(4) Hỗ trợ toàn diện cho sức khỏe khớp từ nhiều góc độ."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 2-4 tuần)",
            "Đường huyết (ở bệnh nhân tiểu đường)",
            "INR (nếu dùng với warfarin)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân tiểu đường - theo dõi đường huyết",
            "Thận trọng ở bệnh nhân dị ứng động vật có vỏ",
            "Thận trọng ở bệnh nhân dùng thuốc chống đông - theo dõi INR và dấu hiệu chảy máu",
            "Có thể mất 2-4 tuần để thấy hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Glucosamine: ~15 giờ; Chondroitin: không rõ; MSM: không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 2-4 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cả glucosamine và chondroitin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tiểu đường (metformin, insulin, sulfonylureas)",
                    "mechanism": "Glucosamine có thể ảnh hưởng đến chuyển hóa glucose",
                    "effect": "Có thể tăng hoặc giảm đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ, điều chỉnh liều thuốc tiểu đường nếu cần."
                },
                {
                    "drug": "Thuốc chống đông khác (heparin, enoxaparin, dabigatran, rivaroxaban)",
                    "mechanism": "Chondroitin có thể tăng tác dụng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glucosamine, chondroitin, MSM hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân tiểu đường - glucosamine có thể ảnh hưởng đường huyết",
                "Suy thận nặng - dữ liệu hạn chế",
                "Bệnh nhân dùng thuốc chống đông - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Không khuyến cáo",
            "notes": "Glucosamine chuyển hóa ở gan, chondroitin và MSM không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Tăng đường huyết (ở bệnh nhân tiểu đường)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi đường huyết nếu cần"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Kết hợp ba thành phần có tác dụng hiệp đồng mạnh."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine, Chondroitin and MSM for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Triple Flex Nature Made - Product Information"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (common)",
                "metabolic": "Hyperglycemia risk (in diabetes patients, due to glucosamine)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Blood glucose (in diabetes patients)",
                "INR (if co-administered with warfarin) - CRITICAL",
                "Bleeding signs (if co-administered with anticoagulants) - CRITICAL",
                "Joint pain/stiffness (efficacy assessment after 2-4 weeks)",
                "Allergic reactions (especially in shellfish allergy)"
            ],
            "look_alike_sound_alike": ["Glucosamine + Chondroitin + MSM", "Triple Flex"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    },

    "Glucosamine + Chondroitin + Hyaluronic Acid": {
        "group": "Rheumatology - Joint Supplement (Combination - Move Free)",
        "vietnamese_name": "Glucosamine + Chondroitin + Hyaluronic Acid, Move Free",
        "brand_names": {
            "common": [
                "Glucosamine + Chondroitin + Hyaluronic Acid",
                "Move Free Joint Health",
                "Move Free Advanced"
            ],
            "vietnam": [
                "Move Free Joint Health",
                "Glucosamine + Chondroitin + Hyaluronic Acid",
                "Viên uống Move Free"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Giảm sưng, đau nhức xương khớp",
            "Tăng cường khả năng vận động",
            "Hỗ trợ tái tạo mô sụn khớp",
            "Cải thiện bôi trơn khớp"
        ],
        "contraindications": [
            "Dị ứng với glucosamine, chondroitin, hyaluronic acid hoặc động vật có vỏ",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)",
            "Bệnh nhân tiểu đường (glucosamine có thể ảnh hưởng đường huyết)"
        ],
        "dosage": {
            "adult_osteoarthritis": "Glucosamine 1500mg + Chondroitin 1200mg + Hyaluronic Acid 10-20mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "alternative": "Theo hướng dẫn của nhà sản xuất (có thể khác nhau tùy sản phẩm)",
            "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Kết hợp ba thành phần có tác dụng hiệp đồng: glucosamine và chondroitin tái tạo sụn, hyaluronic acid cải thiện bôi trơn khớp. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (thường gặp)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng động vật có vỏ)",
            "Tăng đường huyết (ở bệnh nhân tiểu đường, do glucosamine)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc tiểu đường: có thể ảnh hưởng đường huyết - theo dõi đường huyết",
            "Thuốc chống đông khác: có thể tăng nguy cơ chảy máu (do chondroitin)"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Kết hợp glucosamine, chondroitin và hyaluronic acid có tác dụng hiệp đồng trong hỗ trợ sức khỏe khớp. "
            "Glucosamine: kích thích tổng hợp proteoglycans và collagen trong sụn, ức chế các enzyme phá hủy sụn. "
            "Chondroitin: kích thích tổng hợp proteoglycans, ức chế các enzyme phá hủy sụn, tăng sản xuất dịch khớp. "
            "Hyaluronic Acid: là thành phần chính của dịch khớp (synovial fluid), có tác dụng bôi trơn khớp, "
            "giảm ma sát, hấp thụ sốc, cung cấp chất dinh dưỡng cho sụn. Tác dụng hiệp đồng: "
            "(1) Glucosamine và chondroitin tái tạo và bảo vệ sụn, (2) Hyaluronic acid cải thiện bôi trơn khớp "
            "và giảm ma sát, (3) Cải thiện chức năng khớp toàn diện, (4) Hỗ trợ toàn diện cho sức khỏe khớp."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 4-8 tuần)",
            "Đường huyết (ở bệnh nhân tiểu đường)",
            "INR (nếu dùng với warfarin)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân tiểu đường - theo dõi đường huyết",
            "Thận trọng ở bệnh nhân dị ứng động vật có vỏ",
            "Thận trọng ở bệnh nhân dùng thuốc chống đông - theo dõi INR và dấu hiệu chảy máu",
            "Có thể mất 4-8 tuần để thấy hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Glucosamine: ~15 giờ; Chondroitin: không rõ; Hyaluronic Acid: không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 4-8 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cả glucosamine và chondroitin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tiểu đường (metformin, insulin, sulfonylureas)",
                    "mechanism": "Glucosamine có thể ảnh hưởng đến chuyển hóa glucose",
                    "effect": "Có thể tăng hoặc giảm đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ, điều chỉnh liều thuốc tiểu đường nếu cần."
                },
                {
                    "drug": "Thuốc chống đông khác (heparin, enoxaparin, dabigatran, rivaroxaban)",
                    "mechanism": "Chondroitin có thể tăng tác dụng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glucosamine, chondroitin, hyaluronic acid hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân tiểu đường - glucosamine có thể ảnh hưởng đường huyết",
                "Suy thận nặng - dữ liệu hạn chế",
                "Bệnh nhân dùng thuốc chống đông - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Không khuyến cáo",
            "notes": "Glucosamine chuyển hóa ở gan, chondroitin và hyaluronic acid không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Tăng đường huyết (ở bệnh nhân tiểu đường)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi đường huyết nếu cần"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Kết hợp ba thành phần có tác dụng hiệp đồng."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine, Chondroitin and Hyaluronic Acid for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Move Free Joint Health - Product Information"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (common)",
                "metabolic": "Hyperglycemia risk (in diabetes patients, due to glucosamine)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Blood glucose (in diabetes patients)",
                "INR (if co-administered with warfarin) - CRITICAL",
                "Bleeding signs (if co-administered with anticoagulants) - CRITICAL",
                "Joint pain/stiffness (efficacy assessment after 4-8 weeks)",
                "Allergic reactions (especially in shellfish allergy)"
            ],
            "look_alike_sound_alike": ["Glucosamine + Chondroitin + Hyaluronic Acid", "Move Free"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    },

    "Glucosamine + Chondroitin + MSM + Vitamin C": {
        "group": "Rheumatology - Joint Supplement (Combination - Cosamin DS)",
        "vietnamese_name": "Glucosamine + Chondroitin + MSM + Vitamin C, Cosamin DS",
        "brand_names": {
            "common": [
                "Glucosamine + Chondroitin + MSM + Vitamin C",
                "Cosamin DS Joint Health",
                "Cosamin DS"
            ],
            "vietnam": [
                "Cosamin DS Joint Health",
                "Glucosamine + Chondroitin + MSM + Vitamin C",
                "Viên uống Cosamin DS"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị thoái hóa khớp, viêm khớp",
            "Tăng độ đàn hồi của sụn khớp",
            "Giảm đau nhức xương khớp",
            "Duy trì độ bền và sự linh hoạt của hệ vận động",
            "Hỗ trợ tái tạo mô sụn khớp"
        ],
        "contraindications": [
            "Dị ứng với glucosamine, chondroitin, MSM, vitamin C hoặc động vật có vỏ",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)",
            "Bệnh nhân tiểu đường (glucosamine có thể ảnh hưởng đường huyết)",
            "Bệnh nhân sỏi thận (vitamin C liều cao có thể tăng nguy cơ sỏi thận)"
        ],
        "dosage": {
            "adult_osteoarthritis": "Glucosamine 1500mg + Chondroitin 1200mg + MSM 1500mg + Vitamin C 60-100mg PO mỗi ngày, chia 2-3 lần, uống với thức ăn",
            "alternative": "Theo hướng dẫn của nhà sản xuất (có thể khác nhau tùy sản phẩm)",
            "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Kết hợp bốn thành phần có tác dụng hiệp đồng: glucosamine và chondroitin tái tạo sụn, MSM giảm viêm, vitamin C hỗ trợ tổng hợp collagen. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, dữ liệu hạn chế",
            "under_30": "Không khuyến cáo, dữ liệu hạn chế, vitamin C liều cao có thể tăng nguy cơ sỏi thận"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (thường gặp)",
            "Ợ nóng, tiêu chảy",
            "Đau đầu, chóng mặt",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng động vật có vỏ)",
            "Tăng đường huyết (ở bệnh nhân tiểu đường, do glucosamine)",
            "Sỏi thận (vitamin C liều cao, hiếm)"
        ],
        "interactions": [
            "Warfarin: có thể tăng nguy cơ chảy máu - theo dõi INR",
            "Thuốc tiểu đường: có thể ảnh hưởng đường huyết - theo dõi đường huyết",
            "Thuốc chống đông khác: có thể tăng nguy cơ chảy máu (do chondroitin)",
            "Estrogen: vitamin C có thể tăng nồng độ estrogen",
            "Aluminum-containing antacids: vitamin C tăng hấp thu aluminum"
        ],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Kết hợp glucosamine, chondroitin, MSM và vitamin C có tác dụng hiệp đồng mạnh trong hỗ trợ sức khỏe khớp. "
            "Glucosamine: kích thích tổng hợp proteoglycans và collagen trong sụn, ức chế các enzyme phá hủy sụn. "
            "Chondroitin: kích thích tổng hợp proteoglycans, ức chế các enzyme phá hủy sụn, tăng sản xuất dịch khớp. "
            "MSM: giảm viêm khớp bằng cách ức chế các cytokine gây viêm, giảm đau khớp, cải thiện tính linh hoạt của khớp. "
            "Vitamin C: là cofactor quan trọng cho tổng hợp collagen, tăng cường sức mạnh của mô liên kết, "
            "chống oxy hóa, bảo vệ sụn khỏi tổn thương do gốc tự do. Tác dụng hiệp đồng: "
            "(1) Glucosamine và chondroitin tái tạo và bảo vệ sụn, (2) MSM giảm viêm và đau, "
            "(3) Vitamin C hỗ trợ tổng hợp collagen và chống oxy hóa, (4) Cải thiện chức năng khớp toàn diện."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 2-4 tuần)",
            "Đường huyết (ở bệnh nhân tiểu đường)",
            "INR (nếu dùng với warfarin)",
            "Dấu hiệu chảy máu (nếu dùng với thuốc chống đông)",
            "Chức năng thận, sỏi thận (nếu dùng vitamin C liều cao)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân tiểu đường - theo dõi đường huyết",
            "Thận trọng ở bệnh nhân dị ứng động vật có vỏ",
            "Thận trọng ở bệnh nhân dùng thuốc chống đông - theo dõi INR và dấu hiệu chảy máu",
            "Thận trọng ở bệnh nhân sỏi thận - vitamin C liều cao có thể tăng nguy cơ sỏi thận",
            "Có thể mất 2-4 tuần để thấy hiệu quả",
            "Uống với thức ăn để giảm kích ứng dạ dày"
        ],
        "pharmacokinetics": {
            "half_life": "Glucosamine: ~15 giờ; Chondroitin: không rõ; MSM: không rõ; Vitamin C: ~16 giờ",
            "onset": "Hiệu quả có thể xuất hiện sau 2-4 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Cả glucosamine và chondroitin có thể tăng tác dụng chống đông của warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Thuốc tiểu đường (metformin, insulin, sulfonylureas)",
                    "mechanism": "Glucosamine có thể ảnh hưởng đến chuyển hóa glucose",
                    "effect": "Có thể tăng hoặc giảm đường huyết",
                    "management": "Theo dõi đường huyết chặt chẽ, điều chỉnh liều thuốc tiểu đường nếu cần."
                },
                {
                    "drug": "Thuốc chống đông khác (heparin, enoxaparin, dabigatran, rivaroxaban)",
                    "mechanism": "Chondroitin có thể tăng tác dụng chống đông",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Estrogen",
                    "mechanism": "Vitamin C có thể tăng nồng độ estrogen",
                    "effect": "Tăng tác dụng phụ của estrogen",
                    "management": "Thận trọng. Theo dõi tác dụng phụ của estrogen."
                },
                {
                    "drug": "Aluminum-containing antacids",
                    "mechanism": "Vitamin C tăng hấp thu aluminum",
                    "effect": "Tăng nguy cơ độc tính aluminum",
                    "management": "Dùng cách xa ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với glucosamine, chondroitin, MSM, vitamin C hoặc động vật có vỏ"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân tiểu đường - glucosamine có thể ảnh hưởng đường huyết",
                "Bệnh nhân sỏi thận - vitamin C liều cao có thể tăng nguy cơ sỏi thận",
                "Suy thận nặng - dữ liệu hạn chế",
                "Bệnh nhân dùng thuốc chống đông - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng",
            "severe": "Không khuyến cáo",
            "notes": "Glucosamine chuyển hóa ở gan, chondroitin, MSM và vitamin C không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Tăng đường huyết (ở bệnh nhân tiểu đường)",
                "Sỏi thận (vitamin C liều cao)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi đường huyết nếu cần",
                "Điều trị sỏi thận nếu có"
            ],
            "monitoring": "Triệu chứng lâm sàng, đường huyết, chức năng thận"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2-3 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Kết hợp bốn thành phần có tác dụng hiệp đồng mạnh."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Glucosamine, Chondroitin, MSM and Vitamin C for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Cosamin DS Joint Health - Product Information"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng còn tranh cãi, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": True,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (common)",
                "metabolic": "Hyperglycemia risk (in diabetes patients, due to glucosamine)",
                "renal": "Kidney stones risk (with high-dose vitamin C)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Blood glucose (in diabetes patients)",
                "INR (if co-administered with warfarin) - CRITICAL",
                "Bleeding signs (if co-administered with anticoagulants) - CRITICAL",
                "Renal function, kidney stones (with high-dose vitamin C)",
                "Joint pain/stiffness (efficacy assessment after 2-4 weeks)",
                "Allergic reactions (especially in shellfish allergy)"
            ],
            "look_alike_sound_alike": ["Glucosamine + Chondroitin + MSM + Vitamin C", "Cosamin DS"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    },

    "Diacerein": {
        "group": "Rheumatology - Osteoarthritis Medication (Diacerein)",
        "vietnamese_name": "Diacerein, Diacetylrhein",
        "brand_names": {
            "common": [
                "Diacerein",
                "Artrodar",
                "Artrodar 50mg"
            ],
            "vietnam": [
                "Diacerein 50mg",
                "Artrodar 50mg",
                "Viên nang Diacerein"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Điều trị viêm khớp xương (osteoarthritis)",
            "Giảm đau và cứng khớp trong viêm khớp xương",
            "Cải thiện chức năng khớp",
            "Làm chậm tiến triển viêm khớp xương"
        ],
        "contraindications": [
            "Dị ứng với diacerein hoặc anthraquinone",
            "Suy thận nặng (CrCl <30 ml/min)",
            "Suy gan nặng",
            "Trẻ em dưới 15 tuổi",
            "Phụ nữ có thai và cho con bú"
        ],
        "dosage": {
            "adult_osteoarthritis": "50mg PO 2 lần/ngày (sáng và tối), uống với thức ăn",
            "elderly": "50mg PO 2 lần/ngày, có thể giảm xuống 50mg 1 lần/ngày nếu không dung nạp",
            "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Cần dùng liên tục ít nhất 3-6 tháng để thấy hiệu quả rõ ràng. Uống với thức ăn để giảm kích ứng dạ dày."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Thận trọng, cân nhắc giảm liều",
            "under_30": "Chống chỉ định nếu CrCl <30 ml/min"
        },
        "side_effects": [
            "Tiêu chảy (rất thường gặp, đặc biệt trong vài tuần đầu)",
            "Đau bụng, khó chịu dạ dày",
            "Buồn nôn, nôn",
            "Đổi màu nước tiểu (màu vàng/cam - vô hại)",
            "Phát ban da (hiếm)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Laxatives: tăng nguy cơ tiêu chảy",
            "Thuốc độc gan: tăng nguy cơ độc gan"
        ],
        "pregnancy": "C - Tránh dùng trong thai kỳ",
        "mechanism_of_action": (
            "Diacerein là một anthraquinone, được chuyển hóa thành rhein (dạng hoạt động). "
            "Cơ chế tác dụng: (1) Ức chế interleukin-1β (IL-1β), một cytokine gây viêm quan trọng "
            "trong viêm khớp xương, (2) Ức chế các enzyme phá hủy sụn (matrix metalloproteinases), "
            "(3) Giảm sản xuất các chất gây viêm và đau, (4) Bảo vệ sụn khớp khỏi tổn thương, "
            "(5) Có thể làm chậm tiến triển viêm khớp xương. Diacerein có tác dụng chậm nhưng kéo dài, "
            "khác với NSAIDs (tác dụng nhanh nhưng không bảo vệ sụn). Diacerein được coi là "
            "disease-modifying osteoarthritis drug (DMOAD) - thuốc làm thay đổi tiến triển bệnh."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 2-4 tuần)",
            "Tiêu chảy (rất thường gặp, đặc biệt trong vài tuần đầu)",
            "Chức năng gan (men gan) nếu dùng kéo dài",
            "Chức năng thận (creatinine, eGFR)"
        ],
        "precautions": [
            "QUAN TRỌNG: Tiêu chảy rất thường gặp, đặc biệt trong vài tuần đầu - thường tự hết sau vài tuần",
            "Nếu tiêu chảy nặng hoặc kéo dài, có thể giảm liều hoặc ngừng thuốc",
            "Uống với thức ăn để giảm kích ứng dạ dày",
            "Đổi màu nước tiểu (màu vàng/cam) là bình thường, không nguy hiểm",
            "Cần dùng liên tục ít nhất 3-6 tháng để thấy hiệu quả rõ ràng",
            "Không dùng nếu CrCl <30 ml/min",
            "Thận trọng ở bệnh nhân suy gan"
        ],
        "pharmacokinetics": {
            "half_life": "Diacerein: ~4 giờ; Rhein (metabolite): ~10 giờ",
            "onset": "Hiệu quả có thể xuất hiện sau 2-4 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Rhein: ~99%",
            "clearance": "Chuyển hóa ở gan thành rhein, thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Laxatives",
                    "mechanism": "Cả hai đều có thể gây tiêu chảy",
                    "effect": "Tăng nguy cơ tiêu chảy nặng",
                    "management": "Thận trọng. Tránh dùng đồng thời nếu có thể."
                },
                {
                    "drug": "Thuốc độc gan (paracetamol liều cao, isoniazid, methotrexate)",
                    "mechanism": "Cộng gộp độc tính trên gan",
                    "effect": "Tăng nguy cơ độc gan",
                    "management": "Thận trọng. Theo dõi men gan."
                }
            ],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với diacerein hoặc anthraquinone",
                "Suy thận nặng (CrCl <30 ml/min)",
                "Suy gan nặng",
                "Trẻ em dưới 15 tuổi",
                "Phụ nữ có thai và cho con bú"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, cân nhắc giảm liều",
                "Suy gan trung bình - thận trọng",
                "Tiền sử tiêu chảy mạn tính - tăng nguy cơ tiêu chảy"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Tránh dùng trong thai kỳ. Dữ liệu an toàn hạn chế.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Không khuyến cáo dùng khi cho con bú.",
                "recommendation": "Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Thận trọng, theo dõi men gan",
            "severe": "Chống chỉ định",
            "notes": "Diacerein chuyển hóa ở gan thành rhein"
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Đau bụng, buồn nôn, nôn",
                "Tăng men gan"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng diacerein",
                "Điều trị tiêu chảy: bù dịch, điện giải",
                "Điều trị hỗ trợ triệu chứng",
                "Theo dõi men gan nếu cần"
            ],
            "monitoring": "Triệu chứng lâm sàng, men gan, chức năng thận"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để giảm kích ứng dạ dày",
                "timing": "Uống 2 lần/ngày (sáng và tối), cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 2-4 tuần. Tiêu chảy rất thường gặp trong vài tuần đầu, thường tự hết. Cần dùng liên tục ít nhất 3-6 tháng."
            }
        },
        "references": {
            "primary_sources": [
                "EMA - Diacerein Product Information",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Cochrane Review - Diacerein for osteoarthritis"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "B - Bằng chứng lâm sàng vừa phải, hiệu quả trong viêm khớp xương"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "CRITICAL - Diarrhea (very common, especially in first few weeks)",
                "hepatic": "Hepatotoxicity (rare, monitor liver function)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "CRITICAL - Diarrhea (very common in first few weeks, usually self-limiting) - CRITICAL",
                "Liver function (ALT, AST - if long-term use)",
                "Renal function (creatinine, eGFR - contraindicated if CrCl <30 ml/min)",
                "Joint pain/stiffness (efficacy assessment after 2-4 weeks)",
                "Urine color change (yellow/orange - harmless)"
            ],
            "look_alike_sound_alike": ["Diacerein", "Diacetylrhein", "Artrodar"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "EMA - Diacerein Product Information",
            "Cochrane Review - Diacerein"
        ],
        "last_updated": "2025-01-20"
    },

    "Hyaluronic Acid (Oral)": {
        "group": "Rheumatology - Joint Supplement (Hyaluronic Acid)",
        "vietnamese_name": "Hyaluronic Acid, Acid Hyaluronic, Sodium Hyaluronate",
        "brand_names": {
            "common": [
                "Hyaluronic Acid",
                "Sodium Hyaluronate",
                "HA Supplement"
            ],
            "vietnam": [
                "Hyaluronic Acid 100mg",
                "Acid Hyaluronic",
                "Viên uống Hyaluronic Acid"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Cải thiện bôi trơn khớp",
            "Giảm đau khớp, cứng khớp",
            "Hỗ trợ sức khỏe da và mắt (tác dụng phụ)",
            "Cải thiện chức năng vận động khớp"
        ],
        "contraindications": [
            "Dị ứng với hyaluronic acid",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)"
        ],
        "dosage": {
            "adult_osteoarthritis": "100-200mg PO mỗi ngày, uống với thức ăn",
            "alternative": "50-100mg PO mỗi ngày",
            "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Hyaluronic acid đường uống có thể được hấp thu và phân bố đến khớp. Uống với thức ăn để tăng hấp thu."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (ít gặp)",
            "Đau đầu",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Hyaluronic acid (HA) là một glycosaminoglycan tự nhiên, là thành phần chính của dịch khớp "
            "(synovial fluid) và sụn khớp. HA có tác dụng: (1) Bôi trơn khớp, giảm ma sát giữa các bề mặt khớp, "
            "(2) Hấp thụ sốc, bảo vệ khớp khỏi tổn thương, (3) Cung cấp chất dinh dưỡng cho sụn, "
            "(4) Giữ nước trong khớp, duy trì độ đàn hồi của sụn, (5) Có thể giảm viêm và đau khớp. "
            "Trong viêm khớp xương, nồng độ và chất lượng HA trong dịch khớp giảm, dẫn đến giảm bôi trơn "
            "và tăng ma sát. Bổ sung HA đường uống có thể được hấp thu và phân bố đến khớp, "
            "mặc dù bằng chứng lâm sàng về hiệu quả còn hạn chế so với tiêm nội khớp."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 4-8 tuần)",
            "Dấu hiệu dị ứng"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Bằng chứng lâm sàng về hiệu quả đường uống còn hạn chế so với tiêm nội khớp",
            "Có thể mất 4-8 tuần để thấy hiệu quả",
            "Uống với thức ăn để tăng hấp thu"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 4-8 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "Không rõ",
            "clearance": "Chuyển hóa và thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với hyaluronic acid"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Suy thận nặng - dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Hyaluronic acid không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng hyaluronic acid",
                "Điều trị hỗ trợ triệu chứng"
            ],
            "monitoring": "Triệu chứng lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn để tăng hấp thu",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Bằng chứng lâm sàng về hiệu quả đường uống còn hạn chế."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Hyaluronic Acid for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Journal of Orthopaedic Research - Oral HA studies"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "C - Bằng chứng lâm sàng hạn chế, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (uncommon)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Joint pain/stiffness (efficacy assessment after 4-8 weeks)",
                "Allergic reactions (rare)"
            ],
            "look_alike_sound_alike": ["Hyaluronic Acid", "Sodium Hyaluronate", "HA Supplement"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    },

    "Collagen Type 2 (Undenatured)": {
        "group": "Rheumatology - Joint Supplement (Collagen Type 2)",
        "vietnamese_name": "Collagen Type 2, Undenatured Collagen Type 2, UC-II",
        "brand_names": {
            "common": [
                "Collagen Type 2",
                "Undenatured Collagen Type 2",
                "UC-II"
            ],
            "vietnam": [
                "Collagen Type 2 40mg",
                "UC-II",
                "Viên uống Collagen Type 2"
            ],
        },
        "administration": ["PO"],
        "indications": [
            "Hỗ trợ điều trị viêm khớp xương (osteoarthritis)",
            "Hỗ trợ điều trị viêm khớp dạng thấp (rheumatoid arthritis)",
            "Giảm đau khớp, cứng khớp",
            "Cải thiện chức năng vận động khớp",
            "Hỗ trợ sức khỏe sụn khớp"
        ],
        "contraindications": [
            "Dị ứng với collagen hoặc thịt gà",
            "Phụ nữ có thai và cho con bú (dữ liệu an toàn hạn chế)"
        ],
        "dosage": {
            "adult_osteoarthritis": "40mg PO mỗi ngày, uống với nước lạnh, lúc đói hoặc với thức ăn",
            "alternative": "Theo hướng dẫn của nhà sản xuất (có thể khác nhau tùy sản phẩm)",
            "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Undenatured collagen type 2 (UC-II) được cho là hoạt động qua cơ chế miễn dịch, tạo dung nạp miễn dịch. Uống với nước lạnh, có thể uống lúc đói hoặc với thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không cần chỉnh liều",
            "30_60": "Không cần chỉnh liều",
            "under_30": "Thận trọng, dữ liệu hạn chế"
        },
        "side_effects": [
            "Buồn nôn, khó chịu dạ dày (ít gặp)",
            "Đau đầu",
            "Phản ứng dị ứng (đặc biệt ở người dị ứng thịt gà)",
            "Phản ứng miễn dịch (hiếm, có thể gây đau khớp tạm thời)"
        ],
        "interactions": [],
        "pregnancy": "C - Dữ liệu an toàn hạn chế, tránh dùng trừ khi lợi ích vượt trội nguy cơ",
        "mechanism_of_action": (
            "Collagen type 2 là thành phần chính của sụn khớp, chiếm khoảng 50-60% protein trong sụn. "
            "Undenatured collagen type 2 (UC-II) là collagen type 2 chưa bị biến tính (denatured), "
            "giữ nguyên cấu trúc ba chiều. Cơ chế tác dụng được đề xuất: (1) Oral tolerance - "
            "khi uống UC-II, hệ miễn dịch nhận diện và tạo dung nạp miễn dịch với collagen type 2, "
            "giảm phản ứng tự miễn tấn công sụn khớp, (2) Giảm viêm khớp bằng cách điều hòa miễn dịch, "
            "(3) Bảo vệ sụn khớp khỏi tổn thương do miễn dịch, (4) Có thể kích thích tái tạo sụn. "
            "UC-II khác với collagen thủy phân (hydrolyzed collagen) - UC-II hoạt động qua cơ chế miễn dịch, "
            "trong khi collagen thủy phân cung cấp amino acid để tổng hợp collagen mới. "
            "Bằng chứng lâm sàng về hiệu quả còn hạn chế, một số nghiên cứu cho thấy hiệu quả vừa phải."
        ),
        "monitoring": [
            "Triệu chứng đau khớp, cứng khớp (đánh giá hiệu quả sau 4-8 tuần)",
            "Dấu hiệu dị ứng (đặc biệt ở người dị ứng thịt gà)",
            "Phản ứng miễn dịch (có thể gây đau khớp tạm thời)"
        ],
        "precautions": [
            "Hiệu quả có thể khác nhau giữa các cá nhân",
            "Thận trọng ở bệnh nhân dị ứng thịt gà (UC-II thường chiết xuất từ sụn gà)",
            "Có thể mất 4-8 tuần để thấy hiệu quả",
            "Một số bệnh nhân có thể có phản ứng miễn dịch tạm thời (đau khớp tăng nhẹ) trong vài tuần đầu",
            "Uống với nước lạnh, có thể uống lúc đói hoặc với thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "Không rõ",
            "onset": "Hiệu quả có thể xuất hiện sau 4-8 tuần",
            "duration": "Cần dùng liên tục để duy trì hiệu quả",
            "protein_binding": "N/A (protein)",
            "clearance": "Tiêu hóa và hấp thu một phần, phần còn lại thải qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng, tránh nhiệt độ cao",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [],
            "minor": []
        },
        "contraindications_detail": {
            "tuyệt_đối": [
                "Dị ứng với collagen hoặc thịt gà"
            ],
            "tương_đối": [
                "Phụ nữ có thai và cho con bú - dữ liệu an toàn hạn chế",
                "Bệnh nhân rối loạn miễn dịch - có thể ảnh hưởng đến phản ứng miễn dịch",
                "Suy thận nặng - dữ liệu hạn chế"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Dữ liệu an toàn hạn chế. Tránh dùng trừ khi lợi ích vượt trội nguy cơ.",
            "lactation": {
                "safety": "Caution",
                "details": "Chưa rõ bài tiết vào sữa mẹ. Dữ liệu an toàn hạn chế.",
                "recommendation": "Thận trọng. Cân nhắc lợi ích-nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần chỉnh liều",
            "moderate": "Không cần chỉnh liều",
            "severe": "Không cần chỉnh liều",
            "notes": "Collagen type 2 không chuyển hóa qua gan đáng kể"
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn, tiêu chảy",
                "Đau bụng",
                "Phản ứng dị ứng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng collagen type 2",
                "Điều trị hỗ trợ triệu chứng",
                "Điều trị phản ứng dị ứng nếu có"
            ],
            "monitoring": "Triệu chứng lâm sàng, dấu hiệu dị ứng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống lúc đói hoặc với thức ăn",
                "timing": "Uống 1 lần/ngày, với nước lạnh, cùng giờ mỗi ngày",
                "notes": "Hiệu quả có thể xuất hiện sau 4-8 tuần. Uống với nước lạnh. Một số bệnh nhân có thể có phản ứng miễn dịch tạm thời trong vài tuần đầu."
            }
        },
        "references": {
            "primary_sources": [
                "NIH - Collagen Type 2 for Osteoarthritis",
                "OARSI Guidelines - Osteoarthritis Treatment",
                "Journal of International Medical Research - UC-II studies"
            ],
            "last_updated": "2025-01-20",
            "evidence_level": "C - Bằng chứng lâm sàng hạn chế, hiệu quả vừa phải"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "icu_critical_care_only": False,
            "bleeding_risk": False,
            "organ_toxicity": {
                "gastrointestinal": "Mild - Nausea, stomach upset (uncommon)",
                "immunologic": "Immune reaction (rare, may cause temporary joint pain)"
            },
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": [
                "Joint pain/stiffness (efficacy assessment after 4-8 weeks)",
                "Allergic reactions (especially in chicken allergy) - CRITICAL",
                "Immune reactions (may cause temporary joint pain in first few weeks)"
            ],
            "look_alike_sound_alike": ["Collagen Type 2", "Undenatured Collagen Type 2", "UC-II"]
        },
        "guideline_tags": [
            "OARSI Guidelines - Osteoarthritis Treatment",
            "NIH - Dietary Supplements"
        ],
        "last_updated": "2025-01-20"
    }
}

__all__ = ["BONE_JOINT_SUPPLEMENTS"]
