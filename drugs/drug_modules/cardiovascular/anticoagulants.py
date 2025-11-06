"""
Anticoagulants and Antiplatelets
"""

ANTICOAGULANTS = {
    "Warfarin": {
        "group": "Cardiovascular - Anticoagulant (Vitamin K Antagonist)",
        "vietnamese_name": "Warfarin, Coumadin",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ",
            "Huyết khối tĩnh mạch sâu (DVT)",
            "Thuyên tắc phổi (PE)",
            "Sau phẫu thuật tim mạch",
            "Thay van tim cơ học"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Có thai (3 tháng đầu và cuối)",
            "Bệnh gan nặng",
            "Không tuân thủ điều trị"
        ],
        "dosage": {
            "adult_loading": "5-10mg x 1 lần/ngày x 2-3 ngày",
            "adult_maintenance": "2-10mg x 1 lần/ngày (theo INR)",
            "target_inr": "2.0-3.0 (hầu hết), 2.5-3.5 (van tim cơ học)",
            "notes": "Theo dõi INR thường xuyên, điều chỉnh liều theo INR"
        },
        "side_effects": [
            "Chảy máu (nặng có thể tử vong)",
            "Hoại tử da (hiếm, ngày 3-10)",
            "Dị tật thai nhi",
            "Tăng nguy cơ loãng xương"
        ],
        "interactions": [
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Metronidazole: tăng tác dụng warfarin",
            "Vitamin K: giảm tác dụng",
            "Nhiều thuốc khác (xem interaction checker)"
        ],
        "pregnancy": "X - Chống chỉ định (trừ trường hợp đặc biệt)",
        "mechanism_of_action": "Ức chế enzyme vitamin K epoxide reductase, giảm tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X)",
        "monitoring": [
            "INR mỗi 1-4 tuần khi ổn định, thường xuyên hơn khi mới bắt đầu hoặc thay đổi liều",
            "INR mỗi 2-3 ngày trong tuần đầu",
            "Công thức máu (Hct, Hb) nếu nghi ngờ chảy máu",
            "Theo dõi dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím)"
        ],
        "precautions": [
            "Uống cùng thời điểm mỗi ngày",
            "Tránh thay đổi đột ngột chế độ ăn (vitamin K)",
            "Giữ chế độ ăn ổn định vitamin K",
            "Tránh rượu (tăng nguy cơ chảy máu)",
            "Thông báo bác sĩ trước khi phẫu thuật",
            "Theo dõi hoại tử da (ngày 3-10, thường ở bệnh nhân thiếu protein C)"
        ],
        "pharmacokinetics": {
            "half_life": "40 giờ (dài)",
            "onset": "24-72 giờ",
            "duration": "2-5 ngày sau khi ngừng",
            "protein_binding": "99%",
            "clearance": "Gan (CYP2C9, CYP1A2)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng",
        "black_box_warnings": "Chảy máu nặng có thể dẫn đến tử vong. Cần theo dõi INR chặt chẽ. Hoại tử da hiếm nhưng nguy hiểm",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin, NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Aspirin/NSAIDs ức chế kết tập tiểu cầu và gây loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu nặng, đặc biệt chảy máu dạ dày ruột",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: dùng liều thấp aspirin (75-100mg), cân nhắc dùng PPI, theo dõi dấu hiệu chảy máu chặt chẽ."
                },
                {
                    "drug": "Amiodarone",
                    "mechanism": "Amiodarone ức chế CYP2C9 (chuyển hóa warfarin), tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông mạnh, tăng INR, tăng nguy cơ chảy máu nặng",
                    "management": "GIẢM LIỀU WARFARIN 30-50% ngay khi bắt đầu amiodarone. Theo dõi INR thường xuyên (mỗi 1-2 tuần đầu). Có thể cần giảm liều warfarin thêm."
                },
                {
                    "drug": "Metronidazole, Fluconazole, Ketoconazole",
                    "mechanism": "Ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông, tăng INR",
                    "management": "Giảm liều warfarin 30-50%. Theo dõi INR thường xuyên. Tăng liều warfarin khi ngừng các thuốc này."
                },
                {
                    "drug": "Rifampin",
                    "mechanism": "Rifampin tăng chuyển hóa warfarin (CYP2C9 induction)",
                    "effect": "Giảm tác dụng chống đông, giảm INR",
                    "management": "Tăng liều warfarin khi bắt đầu rifampin. Giảm liều warfarin khi ngừng rifampin. Theo dõi INR thường xuyên."
                }
            ],
            "moderate": [
                {
                    "drug": "Clopidogrel, Ticagrelor, Prasugrel",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ. Thường TRÁNH dùng chung (trừ chỉ định đặc biệt)."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline, paroxetine)",
                    "mechanism": "SSRIs ức chế kết tập tiểu cầu nhẹ, có thể ức chế CYP2C9",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Antibiotics (sulfamethoxazole-trimethoprim, ciprofloxacin)",
                    "mechanism": "Ức chế CYP2C9, tăng nồng độ warfarin",
                    "effect": "Tăng tác dụng chống đông",
                    "management": "Theo dõi INR thường xuyên. Có thể cần giảm liều warfarin tạm thời."
                },
                {
                    "drug": "Vitamin K",
                    "mechanism": "Đối kháng với warfarin (tăng tổng hợp yếu tố đông máu)",
                    "effect": "Giảm tác dụng chống đông, giảm INR",
                    "management": "Thận trọng với chế độ ăn giàu vitamin K (rau xanh). Giữ chế độ ăn ổn định. Nếu cần đối kháng: Vitamin K IV hoặc PO."
                },
                {
                    "drug": "Statins (simvastatin, atorvastatin)",
                    "mechanism": "Có thể ức chế CYP2C9 nhẹ",
                    "effect": "Tăng tác dụng chống đông nhẹ",
                    "management": "Thận trọng. Theo dõi INR."
                }
            ],
            "minor": [
                {
                    "drug": "Acetaminophen (liều cao >2g/ngày)",
                    "mechanism": "Có thể ức chế CYP2C9",
                    "effect": "Tăng tác dụng chống đông nhẹ",
                    "management": "Thận trọng với liều cao. Theo dõi INR."
                },
                {
                    "drug": "Omeprazole",
                    "mechanism": "Có thể ức chế CYP2C9 nhẹ",
                    "effect": "Tăng tác dụng chống đông nhẹ",
                    "management": "Thận trọng. Theo dõi INR."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Có thai (3 tháng đầu và cuối - category X)",
                "Bệnh gan nặng (Child-Pugh C)",
                "Thiếu protein C hoặc S bẩm sinh (tăng nguy cơ hoại tử da)",
                "Không tuân thủ điều trị"
            ],
            "tương_đối": [
                "Bệnh gan nhẹ-trung bình (thận trọng, theo dõi chức năng gan)",
                "Suy thận nặng (thận trọng)",
                "Người già (>75 tuổi - tăng nguy cơ chảy máu)",
                "Tiền sử loét dạ dày tá tràng (tăng nguy cơ chảy máu)",
                "Đang dùng aspirin/NSAIDs (tăng nguy cơ chảy máu)",
                "Rối loạn đông máu (hemophilia, von Willebrand disease)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI trong thai kỳ (trừ trường hợp van tim cơ học - lợi ích vượt trội nguy cơ). Warfarin đi qua nhau thai và có thể gây dị tật thai nhi (warfarin embryopathy: hypoplastic nose, chondrodysplasia punctata), chảy máu thai nhi, chảy máu nhau thai, sẩy thai, và tử vong thai nhi. Nguy cơ cao nhất trong 3 tháng đầu (dị tật) và 3 tháng cuối (chảy máu). Nếu đang dùng warfarin và có thai: ngừng ngay và chuyển sang heparin/LMWH.",
            "lactation": {
                "safety": "Compatible",
                "details": "Warfarin bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp (do protein binding 99%). Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (warfarin chuyển hóa qua gan)",
            "severe": "TRÁNH DÙNG (Child-Pugh C) hoặc thận trọng (nếu bắt buộc), theo dõi chức năng gan và INR chặt chẽ",
            "notes": "Warfarin chuyển hóa qua gan (CYP2C9, CYP1A2). Suy gan làm giảm tổng hợp yếu tố đông máu và có thể ảnh hưởng đến chuyển hóa warfarin. Bắt buộc theo dõi chức năng gan và INR chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
                "Chảy máu nặng (xuất huyết nội sọ, xuất huyết tiêu hóa, chảy máu nội tạng)",
                "INR tăng cao (>5.0)",
                "Hoại tử da (hiếm, ngày 3-10, thường ở bệnh nhân thiếu protein C)"
            ],
            "antidote": "Vitamin K (phytomenadione) - ANTIDOTE",
            "treatment": [
                "NGỪNG WARFARIN NGAY LẬP TỨC",
                "Đánh giá mức độ chảy máu: Nếu chảy máu nặng hoặc INR >10: Vitamin K + Fresh Frozen Plasma (FFP) hoặc Prothrombin Complex Concentrate (PCC)",
                "Nếu INR 4.5-10, không chảy máu: Giảm liều warfarin hoặc bỏ 1-2 liều, theo dõi INR",
                "Nếu INR >10, không chảy máu: Vitamin K 1-5mg PO, theo dõi INR",
                "Nếu chảy máu nhẹ: Vitamin K 1-2mg PO, theo dõi INR",
                "Nếu chảy máu nặng: Vitamin K 5-10mg IV + FFP hoặc PCC + hỗ trợ hô hấp và tuần hoàn",
                "Theo dõi INR thường xuyên (mỗi 6-12 giờ khi chảy máu nặng)",
                "Điều trị nguyên nhân chảy máu nếu có"
            ],
            "monitoring": "INR (mỗi 6-12 giờ khi chảy máu nặng), công thức máu (Hct, Hb, tiểu cầu), dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu), chức năng thận, gan, ý thức"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Vitamin K (Phytomenadione)",
                    "mechanism": "Kích thích tổng hợp các yếu tố đông máu phụ thuộc vitamin K (II, VII, IX, X)",
                    "indication": "INR tăng cao (>5.0) hoặc chảy máu do warfarin",
                    "dose": "PO: 1-5mg (INR >10, không chảy máu). IV: 5-10mg (chảy máu nặng). Tác dụng sau 6-12 giờ (PO) hoặc 1-2 giờ (IV)."
                },
                {
                    "name": "Fresh Frozen Plasma (FFP)",
                    "mechanism": "Cung cấp các yếu tố đông máu",
                    "indication": "Chảy máu nặng do warfarin",
                    "dose": "10-15ml/kg IV. Tác dụng ngay lập tức."
                },
                {
                    "name": "Prothrombin Complex Concentrate (PCC)",
                    "mechanism": "Cung cấp nồng độ cao các yếu tố đông máu II, VII, IX, X",
                    "indication": "Chảy máu nặng do warfarin (ưu tiên hơn FFP)",
                    "dose": "25-50 units/kg IV. Tác dụng ngay lập tức."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, CÙNG THỜI ĐIỂM mỗi ngày (ví dụ: 6 giờ tối). Rất quan trọng để duy trì nồng độ ổn định. KHÔNG bỏ liều. Nếu quên: uống ngay khi nhớ, nhưng không uống gấp đôi. Giữ chế độ ăn ổn định (vitamin K)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Coumadin (warfarin)",
                "UpToDate - Warfarin: Drug information",
                "WARCEF Study - New England Journal of Medicine (2012)",
                "RE-LY Study - New England Journal of Medicine (2009) - So sánh warfarin với dabigatran",
                "American Heart Association/American College of Cardiology guidelines - Anticoagulation"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Extensive clinical experience and multiple large RCTs (WARCEF, RE-LY) in anticoagulation"
        }
    },

    "Aspirin": {
        "group": "Cardiovascular - Antiplatelet",
        "vietnamese_name": "Aspirin, Acetylsalicylic acid",
        "administration": ["PO"],
        "indications": [
            "Dự phòng nhồi máu cơ tim",
            "Dự phòng đột quỵ",
            "Sau đặt stent",
            "Đau, sốt, viêm",
            "Viêm khớp dạng thấp"
        ],
        "contraindications": [
            "Loét dạ dày tá tràng đang hoạt động",
            "Chảy máu đang hoạt động",
            "Dị ứng aspirin",
            "Trẻ em <12 tuổi (hội chứng Reye)"
        ],
        "dosage": {
            "adult_cardioprotective": "75-100mg x 1 lần/ngày",
            "adult_pain": "325-650mg mỗi 4-6 giờ",
            "adult_arthritis": "325-650mg x 4 lần/ngày",
            "notes": "Liều thấp (75-100mg) cho dự phòng tim mạch"
        },
        "side_effects": [
            "Chảy máu dạ dày",
            "Loét dạ dày tá tràng",
            "Chảy máu nói chung",
            "Ù tai (liều cao)",
            "Co thắt phế quản (ở bệnh nhân hen)"
        ],
        "interactions": [
            "Warfarin: tăng nguy cơ chảy máu nặng",
            "NSAID khác: tăng nguy cơ chảy máu dạ dày",
            "ACE inhibitor: giảm hiệu quả hạ huyết áp"
        ],
        "pregnancy": "C - D trong 3 tháng cuối",
        "mechanism_of_action": "Ức chế không hồi phục enzyme cyclooxygenase (COX-1), ức chế kết tập tiểu cầu và tổng hợp prostaglandin. Với liều cao: giảm đau, hạ sốt, kháng viêm",
        "monitoring": [
            "Dấu hiệu chảy máu (phân đen, nôn ra máu, chảy máu chân răng)",
            "Hemoglobin nếu nghi ngờ chảy máu",
            "Chức năng thận nếu dùng lâu dài",
            "Ù tai nếu dùng liều cao (dấu hiệu độc tính)"
        ],
        "precautions": [
            "Dùng với thức ăn hoặc sau ăn để giảm kích ứng dạ dày",
            "Cân nhắc dùng PPI nếu có nguy cơ loét dạ dày",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không dùng cho trẻ <12 tuổi (hội chứng Reye)",
            "Không dùng với rượu (tăng nguy cơ chảy máu dạ dày)"
        ],
        "pharmacokinetics": {
            "half_life": "2-3 giờ (liều thấp), 15-20 giờ (liều cao)",
            "onset": "30 phút",
            "duration": "7-10 ngày (tiểu cầu, liều thấp), 4-6 giờ (giảm đau)",
            "protein_binding": "50-80%",
            "clearance": "Gan (thủy phân) và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng nguy cơ chảy máu, đặc biệt chảy máu dạ dày ruột. Nguy cơ tăng ở người già và dùng chung với thuốc khác",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: theo dõi INR và dấu hiệu chảy máu chặt chẽ."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAIDs cũng ức chế COX-1 và gây loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu dạ dày ruột, loét dạ dày tá tràng",
                    "management": "Thận trọng. Cân nhắc dùng PPI. Theo dõi dấu hiệu chảy máu dạ dày. Tránh dùng lâu dài cùng."
                },
                {
                    "drug": "Clopidogrel, Ticagrelor, Prasugrel",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu (nhưng có chỉ định trong DAPT sau ACS/stent)",
                    "management": "Dùng kèm sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn). Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "ACE inhibitors, ARBs",
                    "mechanism": "Aspirin có thể giảm hiệu quả hạ huyết áp của ACE/ARB (ức chế prostaglandin)",
                    "effect": "Giảm hiệu quả hạ huyết áp",
                    "management": "Thận trọng. Theo dõi huyết áp. Thường không cần điều chỉnh (lợi ích dự phòng tim mạch của aspirin)."
                },
                {
                    "drug": "Corticosteroids (prednisone, hydrocortisone)",
                    "mechanism": "Corticosteroids cũng gây loét dạ dày",
                    "effect": "Tăng nguy cơ loét dạ dày tá tràng",
                    "management": "Cân nhắc dùng PPI. Theo dõi dấu hiệu loét dạ dày."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline)",
                    "mechanism": "SSRIs ức chế kết tập tiểu cầu nhẹ",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Methotrexate",
                    "mechanism": "Aspirin giảm thải trừ methotrexate",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng. Theo dõi chức năng thận, công thức máu. Có thể cần giảm liều methotrexate."
                }
            ],
            "minor": [
                {
                    "drug": "Acetaminophen",
                    "mechanism": "Có thể tăng nguy cơ chảy máu nhẹ",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng với liều cao. Theo dõi dấu hiệu chảy máu."
                },
                {
                    "drug": "Ginkgo biloba",
                    "mechanism": "Ginkgo ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Loét dạ dày tá tràng đang hoạt động",
                "Chảy máu đang hoạt động",
                "Dị ứng aspirin (phản ứng nghiêm trọng: phù mạch, sốc phản vệ)",
                "Trẻ em <12 tuổi (hội chứng Reye - nguy hiểm tính mạng)",
                "Hemophilia, von Willebrand disease (rối loạn đông máu)"
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng (tăng nguy cơ tái phát)",
                "Suy gan nặng (tăng nguy cơ chảy máu)",
                "Suy thận nặng (thận trọng)",
                "Hen phế quản (có thể gây co thắt phế quản - aspirin-sensitive asthma)",
                "Người già (>75 tuổi - tăng nguy cơ chảy máu)",
                "Đang dùng warfarin hoặc thuốc chống đông khác (tăng nguy cơ chảy máu)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C (D trong 3 tháng cuối)",
            "pregnancy_details": "Có thể dùng khi cần thiết trong 3 tháng đầu và giữa. Tránh dùng trong 3 tháng cuối (category D) - có thể gây đóng sớm ống động mạch, chảy máu thai nhi, chảy máu nhau thai, kéo dài chuyển dạ, tăng nguy cơ chảy máu sau sinh. Nếu cần dùng trong 3 tháng cuối: dùng liều thấp (75-100mg) và theo dõi sát.",
            "lactation": {
                "safety": "Compatible",
                "details": "Aspirin bài tiết vào sữa mẹ ở nồng độ thấp. Với liều thấp (75-100mg): an toàn. Với liều cao: có thể gây hội chứng Reye ở trẻ (hiếm).",
                "recommendation": "Có thể dùng liều thấp (75-100mg) khi cho con bú. Tránh liều cao. Theo dõi trẻ nếu có dấu hiệu chảy máu hoặc hội chứng Reye."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (tăng nguy cơ chảy máu)",
            "severe": "TRÁNH DÙNG hoặc thận trọng (nếu bắt buộc), theo dõi chức năng gan và dấu hiệu chảy máu chặt chẽ",
            "notes": "Aspirin chuyển hóa qua gan. Suy gan làm giảm tổng hợp yếu tố đông máu và có thể ảnh hưởng đến chuyển hóa aspirin. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Ù tai, mất thính giác",
                "Buồn nôn, nôn",
                "Chóng mặt",
                "Lú lẫn",
                "Sốt",
                "Thở nhanh",
                "Nhiễm toan chuyển hóa",
                "Hạ đường huyết",
                "Co giật",
                "Hôn mê",
                "Chảy máu (đặc biệt dạ dày ruột)",
                "Suy thận cấp",
                "Tử vong"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: bù dịch, điện giải, điều chỉnh toan",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị nhiễm toan chuyển hóa: Sodium bicarbonate IV (nếu pH <7.2)",
                "Điều trị hạ đường huyết: Glucose IV",
                "Điều trị co giật: Benzodiazepines (lorazepam, diazepam)",
                "Hỗ trợ hô hấp và tuần hoàn nếu cần",
                "Theo dõi điện giải, glucose, chức năng thận, công thức máu",
                "Theo dõi ít nhất 12-24 giờ"
            ],
            "monitoring": "Điện giải, glucose, khí máu (pH, bicarbonate), chức năng thận (creatinine, BUN), công thức máu (Hct, Hb, tiểu cầu), chức năng gan, ý thức, dấu hiệu chảy máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Nên uống với thức ăn hoặc sau ăn để giảm kích ứng dạ dày. Uống với nhiều nước.",
                "timing": "Liều thấp (75-100mg): Uống 1 lần/ngày, cùng giờ mỗi ngày. Liều cao (đau, viêm): Uống 3-4 lần/ngày, cách nhau 4-6 giờ. KHÔNG ngừng đột ngột nếu dùng lâu dài (có thể tăng nguy cơ biến cố tim mạch)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV thông thường",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aspirin",
                "UpToDate - Aspirin: Drug information",
                "ANTITHROMBOTIC Trialists' Collaboration - The Lancet (2002) - Aspirin trong dự phòng tim mạch",
                "CHARISMA Study - New England Journal of Medicine (2006)",
                "American Heart Association/American College of Cardiology guidelines - Antiplatelet therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (ANTITHROMBOTIC, CHARISMA) and extensive clinical experience in cardiovascular prevention"
        }
    },

    "Clopidogrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Clopidogrel, Plavix",
        "administration": ["PO"],
        "indications": [
            "Sau nhồi máu cơ tim",
            "Sau đặt stent",
            "Hội chứng mạch vành cấp",
            "Đột quỵ/TIA",
            "Bệnh động mạch ngoại biên"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Loét dạ dày tá tràng nặng",
            "Dị ứng"
        ],
        "dosage": {
            "adult_loading": "300-600mg x 1 lần",
            "adult_maintenance": "75mg x 1 lần/ngày",
            "notes": "Dùng kèm aspirin sau ACS/stent (dual antiplatelet therapy)"
        },
        "side_effects": [
            "Chảy máu",
            "Giảm tiểu cầu",
            "Tăng nguy cơ xuất huyết",
            "Ban xuất huyết giảm tiểu cầu huyết khối (TTP) - hiếm"
        ],
        "interactions": [
            "Omeprazole: giảm hiệu quả clopidogrel",
            "Aspirin: tăng nguy cơ chảy máu (nhưng có chỉ định)",
            "Warfarin: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Clopidogrel là prodrug, chuyển hóa thành chất chuyển hóa hoạt tính bởi CYP2C19 (và các CYP khác). Ức chế không hồi phục thụ thể P2Y12 trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP, giảm kết tập tiểu cầu",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
            "Công thức máu nếu nghi ngờ giảm tiểu cầu",
            "Xét nghiệm chức năng tiểu cầu (nếu cần - để đánh giá hiệu quả)",
            "Lưu ý: Một số bệnh nhân có thể kháng clopidogrel do đa hình CYP2C19"
        ],
        "precautions": [
            "Tránh dùng với PPIs mạnh (omeprazole, esomeprazole) - giảm hiệu quả do ức chế CYP2C19",
            "Có thể dùng với pantoprazole, lansoprazole (ít ức chế CYP2C19 hơn)",
            "Dùng kèm aspirin sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn)",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không ngừng đột ngột sau stent (nguy cơ huyết khối stent)",
            "Một số bệnh nhân kháng clopidogrel: xem xét thay bằng ticagrelor hoặc prasugrel"
        ],
        "pharmacokinetics": {
            "half_life": "Clopidogrel: 6 giờ; Metabolite hoạt tính: 30 phút (nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "2-8 giờ (sau loading dose 300-600mg)",
            "duration": "5-10 ngày (cho đến khi tiểu cầu mới được tạo ra)",
            "protein_binding": "98%",
            "clearance": "Gan (chuyển hóa qua CYP2C19, CYP3A4, CYP2B6, CYP1A2)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Không ngừng clopidogrel sớm sau đặt stent (đặc biệt drug-eluting stent) - nguy cơ huyết khối stent và tử vong do tim. Chảy máu có thể đe dọa tính mạng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Omeprazole, Esomeprazole",
                    "mechanism": "Omeprazole/esomeprazole ức chế CYP2C19 (enzyme chuyển hóa clopidogrel thành chất hoạt tính)",
                    "effect": "Giảm hiệu quả clopidogrel mạnh (giảm 40-50% tác dụng), tăng nguy cơ biến cố tim mạch",
                    "management": "TRÁNH DÙNG CHUNG. Thay bằng pantoprazole, lansoprazole (ít ức chế CYP2C19 hơn) hoặc H2 blockers (ranitidine, famotidine)."
                },
                {
                    "drug": "Aspirin",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu (nhưng có chỉ định trong DAPT sau ACS/stent)",
                    "management": "Dùng kèm sau ACS/stent: DAPT 12 tháng (hoặc theo hướng dẫn). Theo dõi dấu hiệu chảy máu chặt chẽ. Cân nhắc dùng PPI (pantoprazole, lansoprazole)."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: theo dõi INR và dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Fluconazole, Voriconazole",
                    "mechanism": "Ức chế CYP2C19, giảm chuyển hóa clopidogrel",
                    "effect": "Giảm hiệu quả clopidogrel",
                    "management": "Thận trọng. Theo dõi hiệu quả. Có thể cần tăng liều clopidogrel hoặc thay bằng ticagrelor/prasugrel."
                },
                {
                    "drug": "Ciprofloxacin, Fluoroquinolones",
                    "mechanism": "Có thể ức chế CYP2C19 nhẹ",
                    "effect": "Giảm hiệu quả clopidogrel nhẹ",
                    "management": "Thận trọng. Theo dõi hiệu quả."
                },
                {
                    "drug": "NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "NSAIDs gây loét dạ dày, tăng nguy cơ chảy máu",
                    "effect": "Tăng nguy cơ chảy máu dạ dày ruột",
                    "management": "Thận trọng. Cân nhắc dùng PPI. Theo dõi dấu hiệu chảy máu dạ dày."
                },
                {
                    "drug": "SSRIs (fluoxetine, sertraline)",
                    "mechanism": "SSRIs ức chế kết tập tiểu cầu nhẹ",
                    "effect": "Tăng nguy cơ chảy máu nhẹ",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ],
            "minor": [
                {
                    "drug": "Atorvastatin (liều cao)",
                    "mechanism": "Có thể ức chế CYP3A4 nhẹ",
                    "effect": "Giảm hiệu quả clopidogrel nhẹ (không rõ ràng)",
                    "management": "Thận trọng. Theo dõi hiệu quả."
                },
                {
                    "drug": "Ginkgo biloba",
                    "mechanism": "Ginkgo ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động",
                "Loét dạ dày tá tràng nặng đang hoạt động",
                "Dị ứng clopidogrel (phản ứng nghiêm trọng: phù mạch, sốc phản vệ)",
                "Hemophilia, von Willebrand disease (rối loạn đông máu)"
            ],
            "tương_đối": [
                "Tiền sử loét dạ dày tá tràng (tăng nguy cơ chảy máu)",
                "Suy gan nặng (tăng nguy cơ chảy máu)",
                "Suy thận nặng (thận trọng)",
                "Người già (>75 tuổi - tăng nguy cơ chảy máu)",
                "Đang dùng warfarin hoặc thuốc chống đông khác (tăng nguy cơ chảy máu)",
                "Đa hình CYP2C19 poor metabolizer (giảm hiệu quả - xem xét thay bằng ticagrelor/prasugrel)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng khi cần thiết. Clopidogrel đi qua nhau thai. Không có dữ liệu đầy đủ về an toàn trong thai kỳ. Có thể tăng nguy cơ chảy máu thai nhi, chảy máu nhau thai. Cân nhắc lợi ích/nguy cơ. Nếu cần dùng: theo dõi sát thai nhi và dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible (có thể)",
                "details": "Clopidogrel bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu chảy máu."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (clopidogrel chuyển hóa qua gan)",
            "severe": "Thận trọng (nếu bắt buộc), theo dõi chức năng gan và dấu hiệu chảy máu chặt chẽ",
            "notes": "Clopidogrel chuyển hóa qua gan (CYP2C19, CYP3A4, CYP2B6, CYP1A2) thành chất hoạt tính. Suy gan có thể ảnh hưởng đến chuyển hóa. Thận trọng ở bệnh nhân suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu)",
                "Chảy máu nặng (xuất huyết nội sọ, xuất huyết tiêu hóa, chảy máu nội tạng)",
                "Giảm tiểu cầu",
                "Ban xuất huyết giảm tiểu cầu huyết khối (TTP) - hiếm nhưng nguy hiểm"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ: truyền tiểu cầu (nếu chảy máu nặng), hỗ trợ hô hấp và tuần hoàn",
            "treatment": [
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị chảy máu nặng: Truyền tiểu cầu (nếu cần), Fresh Frozen Plasma (FFP), hỗ trợ hô hấp và tuần hoàn",
                "Theo dõi công thức máu (Hct, Hb, tiểu cầu), dấu hiệu chảy máu",
                "Theo dõi ít nhất 5-10 ngày (do tác dụng kéo dài 5-10 ngày cho đến khi tiểu cầu mới được tạo ra)"
            ],
            "monitoring": "Công thức máu (Hct, Hb, tiểu cầu), dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu), chức năng thận, gan, ý thức"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, cùng giờ mỗi ngày. Loading dose: 300-600mg x 1 lần (sau ACS/stent). Maintenance: 75mg x 1 lần/ngày. KHÔNG ngừng đột ngột sau stent (nguy cơ huyết khối stent). Nếu cần ngừng: ngừng 5-7 ngày trước phẫu thuật lớn."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Plavix (clopidogrel)",
                "UpToDate - Clopidogrel: Drug information",
                "CURE Study - New England Journal of Medicine (2001) - Clopidogrel trong ACS",
                "CREDO Study - JAMA (2002) - Clopidogrel sau PCI",
                "American Heart Association/American College of Cardiology guidelines - Antiplatelet therapy"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple large RCTs (CURE, CREDO) and extensive clinical experience in cardiovascular disease"
        }
    },

}

__all__ = ['ANTICOAGULANTS']
