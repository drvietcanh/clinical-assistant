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

    "Ticagrelor": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Ticagrelor, Brilinta",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp (ACS)",
            "Sau nhồi máu cơ tim",
            "Sau đặt stent",
            "Dự phòng thứ phát đột quỵ/TIA (ở bệnh nhân có nguy cơ cao)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Tiền sử xuất huyết nội sọ",
            "Suy gan nặng",
            "Dị ứng ticagrelor",
            "Dùng với liều >100mg aspirin/ngày (tăng nguy cơ chảy máu)"
        ],
        "dosage": {
            "adult_loading": "180mg x 1 lần",
            "adult_maintenance": "90mg x 2 lần/ngày",
            "adult_stroke_prevention": "90mg x 2 lần/ngày (với aspirin 75-100mg/ngày)",
            "notes": "Dùng kèm aspirin 75-100mg/ngày (không dùng >100mg/ngày). Dùng 2 lần/ngày. Uống với hoặc không thức ăn."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng (dữ liệu hạn chế)"
        },
        "side_effects": [
            "Chảy máu (phổ biến, có thể nặng)",
            "Khó thở (dyspnea) - 10-20% bệnh nhân, thường nhẹ",
            "Chóng mặt",
            "Nhức đầu",
            "Chảy máu mũi",
            "Vết bầm tím",
            "Nhịp tim chậm (bradycardia) - hiếm"
        ],
        "interactions": [
            "Aspirin >100mg/ngày: tăng nguy cơ chảy máu",
            "CYP3A4 inhibitors mạnh: tăng nồng độ ticagrelor",
            "CYP3A4 inducers: giảm nồng độ ticagrelor",
            "Digoxin: có thể tăng nồng độ digoxin"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Ticagrelor là P2Y12 receptor antagonist có thể đảo ngược (reversible), ức chế thụ thể P2Y12 trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP, giảm kết tập tiểu cầu. Khác với clopidogrel (ức chế không hồi phục) và prasugrel (ức chế không hồi phục), ticagrelor ức chế có thể đảo ngược. Tác dụng nhanh hơn clopidogrel, hiệu quả hơn clopidogrel trong ACS. Đặc điểm: ức chế tái hấp thu adenosine, có thể gây khó thở và nhịp tim chậm. Chuyển hóa qua CYP3A4.",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu, chảy máu nội sọ) - QUAN TRỌNG",
            "Khó thở (dyspnea) - 10-20% bệnh nhân, thường nhẹ, không cần ngừng thuốc",
            "Công thức máu nếu nghi ngờ chảy máu nặng",
            "Nhịp tim (có thể gây nhịp tim chậm)",
            "Nồng độ digoxin nếu đang dùng (ticagrelor có thể tăng nồng độ digoxin)"
        ],
        "precautions": [
            "NGUY CƠ CHẢY MÁU - cao hơn clopidogrel, đặc biệt khi dùng với aspirin >100mg/ngày. CHỈ dùng với aspirin 75-100mg/ngày.",
            "Khó thở (dyspnea) - 10-20% bệnh nhân, thường nhẹ, không cần ngừng thuốc. Giải thích cho bệnh nhân trước khi dùng.",
            "Dùng kèm aspirin 75-100mg/ngày: DAPT 12 tháng sau ACS/stent (hoặc theo hướng dẫn)",
            "Ngừng 5-7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không ngừng đột ngột sau stent (nguy cơ huyết khối stent)",
            "TRÁNH dùng với CYP3A4 inhibitors mạnh (ketoconazole, clarithromycin, ritonavir) - tăng nồng độ ticagrelor",
            "TRÁNH dùng với CYP3A4 inducers mạnh (rifampin, carbamazepine, phenytoin) - giảm nồng độ ticagrelor",
            "Thận trọng ở suy gan nặng (chống chỉ định)",
            "Uống với hoặc không thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "7-9 giờ",
            "onset": "30 phút - 2 giờ (nhanh hơn clopidogrel)",
            "duration": "q12h (dùng 2 lần/ngày)",
            "protein_binding": ">99%",
            "metabolism": "Chuyển hóa qua CYP3A4 (chủ yếu), CYP3A5",
            "clearance": "Chủ yếu qua gan (chuyển hóa), một phần qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỈ dùng với aspirin 75-100mg/ngày. Dùng với aspirin >100mg/ngày làm tăng nguy cơ chảy máu. Không ngừng ticagrelor sớm sau đặt stent - nguy cơ huyết khối stent và tử vong do tim. Chảy máu có thể đe dọa tính mạng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin >100mg/ngày",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "CHỐNG CHỈ ĐỊNH dùng với aspirin >100mg/ngày. CHỈ dùng với aspirin 75-100mg/ngày."
                },
                {
                    "drug": "CYP3A4 inhibitors mạnh (Ketoconazole, Itraconazole, Voriconazole, Clarithromycin, Ritonavir, Saquinavir, Nelfinavir)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa ticagrelor",
                    "effect": "Tăng nồng độ ticagrelor đáng kể, tăng nguy cơ chảy máu",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, giảm liều ticagrelor hoặc theo dõi chặt chẽ dấu hiệu chảy máu."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa ticagrelor",
                    "effect": "Giảm nồng độ ticagrelor, giảm hiệu quả",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, có thể cần tăng liều ticagrelor hoặc thay bằng clopidogrel/prasugrel."
                },
                {
                    "drug": "Digoxin",
                    "mechanism": "Ticagrelor ức chế P-glycoprotein, tăng hấp thu digoxin",
                    "effect": "Tăng nồng độ digoxin, tăng nguy cơ độc tính",
                    "management": "Theo dõi nồng độ digoxin. Giảm liều digoxin nếu cần."
                },
                {
                    "drug": "Simvastatin, Lovastatin (liều cao >40mg/ngày)",
                    "mechanism": "Cả hai đều chuyển hóa qua CYP3A4, tác dụng cạnh tranh",
                    "effect": "Có thể tăng nồng độ statin nhẹ, tăng nguy cơ tiêu cơ vân",
                    "management": "Thận trọng. Giảm liều statin hoặc dùng statin khác (pravastatin, rosuvastatin). Theo dõi CK, dấu hiệu đau cơ."
                }
            ],
            "minor": [
                {
                    "drug": "CYP3A4 inhibitors nhẹ (Diltiazem, Verapamil)",
                    "mechanism": "Ức chế nhẹ CYP3A4",
                    "effect": "Tăng nhẹ nồng độ ticagrelor",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Tiền sử xuất huyết nội sọ - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Dị ứng ticagrelor",
                "Dùng với aspirin >100mg/ngày - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (tăng nguy cơ chảy máu)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, dữ liệu hạn chế",
                "Suy gan trung bình - thận trọng",
                "Dùng với CYP3A4 inhibitors mạnh - tăng nồng độ ticagrelor, tăng nguy cơ chảy máu",
                "Dùng với CYP3A4 inducers mạnh - giảm nồng độ ticagrelor, giảm hiệu quả",
                "Bệnh nhân có nguy cơ chảy máu cao - thận trọng",
                "Bệnh nhân có tiền sử khó thở nặng - thận trọng (ticagrelor có thể gây khó thở)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Ticagrelor phân loại C - thận trọng trong thai kỳ. Các nghiên cứu trên động vật cho thấy một số nguy cơ. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể tăng nguy cơ chảy máu thai nhi, chảy máu nhau thai. Cân nhắc lợi ích/nguy cơ. Nếu cần dùng: theo dõi sát thai nhi và dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Ticagrelor bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
            "notes": "Ticagrelor chuyển hóa chủ yếu qua gan (CYP3A4, CYP3A5). Suy gan nặng là chống chỉ định tuyệt đối. Suy gan trung bình cần thận trọng và có thể cần giảm liều."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng chảy máu: Chảy máu nặng, có thể đe dọa tính mạng (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật)",
                "Triệu chứng hô hấp: Khó thở nặng (do ức chế tái hấp thu adenosine)",
                "Triệu chứng tim mạch: Nhịp tim chậm (do ức chế tái hấp thu adenosine)",
                "Triệu chứng thần kinh: Chóng mặt, nhức đầu"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay ticagrelor",
                "Điều trị chảy máu nặng:",
                "  - Truyền tiểu cầu nếu cần (nhưng hiệu quả hạn chế do ticagrelor ức chế có thể đảo ngược)",
                "  - Truyền máu nếu mất máu nặng",
                "  - Điều trị chảy máu dạ dày ruột: PPI, nội soi nếu cần",
                "  - Điều trị chảy máu nội sọ: phẫu thuật nếu cần",
                "  - Theo dõi dấu hiệu chảy máu chặt chẽ",
                "Điều trị khó thở nếu có:",
                "  - Hỗ trợ hô hấp nếu cần",
                "  - Oxy nếu cần",
                "  - Theo dõi SpO2",
                "Điều trị nhịp tim chậm nếu có:",
                "  - Theo dõi ECG",
                "  - Atropine nếu cần",
                "  - Pacing nếu cần",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lưu ý: Ticagrelor ức chế có thể đảo ngược, tác dụng sẽ giảm dần sau khi ngừng (half-life 7-9 giờ)"
            ],
            "monitoring": "Theo dõi dấu hiệu chảy máu (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật), dấu hiệu hô hấp (khó thở, SpO2), nhịp tim (nhịp tim chậm), dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có chảy máu nặng."
        },
        "reversal_agents": {
            "available": False,
            "agents": ["Truyền tiểu cầu có thể giúp một phần (nhưng hiệu quả hạn chế do ticagrelor ức chế có thể đảo ngược)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 2 lần/ngày (q12h), thường 90mg x 2 lần/ngày. Uống đều đặn, cách đều nhau trong ngày (12 giờ). Không bỏ liều. QUAN TRỌNG: Dùng kèm aspirin 75-100mg/ngày (KHÔNG dùng >100mg/ngày)."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "adolescents": "≥18 tuổi: Liều người lớn. 180mg x 1 lần (loading), sau đó 90mg x 2 lần/ngày (maintenance).",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho ACS/stent ở trẻ ≥18 tuổi. Dùng kèm aspirin 75-100mg/ngày. Theo dõi dấu hiệu chảy máu, khó thở."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi có thể nhạy cảm hơn với tác dụng phụ (chảy máu, khó thở). Suy gan, suy thận phổ biến hơn.",
            "dose_adjustment": "Không cần điều chỉnh liều ở suy thận. Thận trọng ở suy gan (chống chỉ định ở suy gan nặng).",
            "monitoring": "Theo dõi dấu hiệu chảy máu chặt chẽ (nguy cơ cao hơn). Theo dõi khó thở (có thể gây lo lắng ở người cao tuổi). Theo dõi nhịp tim (có thể gây nhịp tim chậm)."
        },
        "brand_names": {
            "vietnam": ["Brilinta", "Ticagrelor", "Ticagrelor Stada"],
            "common": ["Brilinta", "Ticagrelor"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "50,000 - 150,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Ticagrelor generic thường rẻ hơn (50,000-100,000 VND/viên 90mg). Brilinta (brand) thường đắt hơn (100,000-150,000 VND/viên 90mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Brilinta (ticagrelor)",
                "UpToDate - Ticagrelor: Drug information",
                "PLATO Study - The New England Journal of Medicine (2009) - Ticagrelor vs Clopidogrel trong ACS",
                "THALES Study - The New England Journal of Medicine (2020) - Ticagrelor trong đột quỵ",
                "American Heart Association/American College of Cardiology guidelines - Antiplatelet therapy"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Multiple large RCTs (PLATO, THALES) and extensive clinical experience"
        }
    },

    "Prasugrel": {
        "group": "Cardiovascular - Antiplatelet (P2Y12 Inhibitor)",
        "vietnamese_name": "Prasugrel, Effient",
        "administration": ["PO"],
        "indications": [
            "Hội chứng mạch vành cấp (ACS) với PCI",
            "Sau nhồi máu cơ tim với PCI",
            "Sau đặt stent (đặc biệt drug-eluting stent)"
        ],
        "contraindications": [
            "Chảy máu đang hoạt động",
            "Tiền sử xuất huyết nội sọ hoặc TIA",
            "Suy gan nặng",
            "Dị ứng prasugrel",
            "Tuổi ≥75 tuổi (trừ trường hợp đặc biệt - tăng nguy cơ chảy máu)",
            "Cân nặng <60kg (tăng nguy cơ chảy máu)"
        ],
        "dosage": {
            "adult_loading": "60mg x 1 lần",
            "adult_maintenance": "10mg x 1 lần/ngày",
            "adult_low_weight": "5mg x 1 lần/ngày (nếu cân nặng <60kg)",
            "adult_elderly": "5mg x 1 lần/ngày (nếu tuổi ≥75 tuổi)",
            "notes": "Dùng kèm aspirin 75-100mg/ngày. Dùng 1 lần/ngày. Mạnh hơn clopidogrel, nhưng tăng nguy cơ chảy máu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Thận trọng (dữ liệu hạn chế)"
        },
        "side_effects": [
            "Chảy máu (phổ biến, có thể nặng) - cao hơn clopidogrel",
            "Chảy máu nội sọ (hiếm nhưng nguy hiểm)",
            "Chảy máu dạ dày ruột",
            "Chảy máu mũi",
            "Vết bầm tím",
            "Thiếu máu",
            "Chóng mặt",
            "Nhức đầu"
        ],
        "interactions": [
            "Aspirin: tăng nguy cơ chảy máu (nhưng có chỉ định)",
            "Warfarin: tăng nguy cơ chảy máu",
            "NSAIDs: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Prasugrel là prodrug, chuyển hóa thành chất chuyển hóa hoạt tính bởi CYP3A4 và CYP2B6 (và các CYP khác). Ức chế không hồi phục thụ thể P2Y12 trên tiểu cầu, ngăn chặn kích hoạt tiểu cầu bởi ADP, giảm kết tập tiểu cầu. Khác với clopidogrel: prasugrel chuyển hóa nhanh hơn và hiệu quả hơn, ít phụ thuộc vào đa hình CYP2C19. Mạnh hơn clopidogrel, nhưng tăng nguy cơ chảy máu, đặc biệt ở người cao tuổi (≥75 tuổi) và cân nặng thấp (<60kg).",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu, chảy máu nội sọ) - QUAN TRỌNG",
            "Công thức máu nếu nghi ngờ chảy máu nặng (thiếu máu, giảm tiểu cầu)",
            "Dấu hiệu chảy máu nội sọ (đau đầu, thay đổi ý thức, yếu liệt) - đặc biệt quan trọng",
            "Dấu hiệu chảy máu dạ dày ruột (phân đen, nôn ra máu)"
        ],
        "precautions": [
            "NGUY CƠ CHẢY MÁU - cao hơn clopidogrel, đặc biệt ở người cao tuổi (≥75 tuổi) và cân nặng thấp (<60kg). Giảm liều xuống 5mg/ngày ở những bệnh nhân này.",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân có tiền sử xuất huyết nội sọ hoặc TIA - tăng nguy cơ chảy máu nội sọ",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân tuổi ≥75 tuổi (trừ trường hợp đặc biệt) - tăng nguy cơ chảy máu",
            "CHỐNG CHỈ ĐỊNH ở bệnh nhân cân nặng <60kg (trừ trường hợp đặc biệt) - tăng nguy cơ chảy máu",
            "Dùng kèm aspirin 75-100mg/ngày: DAPT 12 tháng sau PCI/stent (hoặc theo hướng dẫn)",
            "Ngừng 7 ngày trước phẫu thuật lớn (nếu có thể)",
            "Không ngừng đột ngột sau stent (nguy cơ huyết khối stent)",
            "Mạnh hơn clopidogrel, nhưng tăng nguy cơ chảy máu - cân nhắc lợi ích/nguy cơ",
            "Uống với hoặc không thức ăn"
        ],
        "pharmacokinetics": {
            "half_life": "Prasugrel: 7 giờ; Metabolite hoạt tính: 3.7 giờ (nhưng tác dụng kéo dài do ức chế không hồi phục)",
            "onset": "30 phút - 4 giờ (nhanh hơn clopidogrel)",
            "duration": "q24h (dùng 1 lần/ngày), nhưng tác dụng kéo dài 5-10 ngày sau khi ngừng (do ức chế không hồi phục)",
            "protein_binding": "98%",
            "metabolism": "Chuyển hóa qua CYP3A4, CYP2B6, CYP2C9, CYP2C19 (ít phụ thuộc CYP2C19 hơn clopidogrel)",
            "clearance": "Chủ yếu qua thận (68%), một phần qua phân (27%)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở bệnh nhân có tiền sử xuất huyết nội sọ hoặc TIA - tăng nguy cơ chảy máu nội sọ. CHỐNG CHỈ ĐỊNH ở bệnh nhân tuổi ≥75 tuổi (trừ trường hợp đặc biệt) - tăng nguy cơ chảy máu. CHỐNG CHỈ ĐỊNH ở bệnh nhân cân nặng <60kg (trừ trường hợp đặc biệt) - tăng nguy cơ chảy máu. Không ngừng prasugrel sớm sau đặt stent - nguy cơ huyết khối stent và tử vong do tim. Chảy máu có thể đe dọa tính mạng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng ức chế kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "Thận trọng. Dùng kèm aspirin 75-100mg/ngày là chỉ định (DAPT), nhưng theo dõi dấu hiệu chảy máu chặt chẽ. TRÁNH dùng với NSAIDs nếu có thể."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "TRÁNH DÙNG đồng thời nếu có thể. Nếu bắt buộc, theo dõi dấu hiệu chảy máu chặt chẽ. Thường TRÁNH dùng chung (trừ chỉ định đặc biệt)."
                }
            ],
            "moderate": [
                {
                    "drug": "CYP3A4 inhibitors mạnh (Ketoconazole, Itraconazole, Clarithromycin)",
                    "mechanism": "Ức chế CYP3A4, giảm chuyển hóa prasugrel",
                    "effect": "Có thể tăng nồng độ prasugrel, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                },
                {
                    "drug": "CYP3A4 inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng CYP3A4, tăng chuyển hóa prasugrel",
                    "effect": "Có thể giảm nồng độ prasugrel, giảm hiệu quả",
                    "management": "Thận trọng. Theo dõi hiệu quả. Có thể cần tăng liều prasugrel hoặc thay bằng clopidogrel/ticagrelor."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Chảy máu đang hoạt động - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Tiền sử xuất huyết nội sọ hoặc TIA - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (tăng nguy cơ chảy máu nội sọ)",
                "Suy gan nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Dị ứng prasugrel",
                "Tuổi ≥75 tuổi - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (trừ trường hợp đặc biệt - tăng nguy cơ chảy máu)",
                "Cân nặng <60kg - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (trừ trường hợp đặc biệt - tăng nguy cơ chảy máu)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - thận trọng, dữ liệu hạn chế",
                "Suy gan trung bình - thận trọng",
                "Bệnh nhân có nguy cơ chảy máu cao - thận trọng",
                "Dùng với warfarin - tăng nguy cơ chảy máu",
                "Dùng với NSAIDs - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Prasugrel phân loại B - an toàn trong thai kỳ. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể tăng nguy cơ chảy máu thai nhi, chảy máu nhau thai. Cân nhắc lợi ích/nguy cơ. Nếu cần dùng: theo dõi sát thai nhi và dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Prasugrel và chất chuyển hóa bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
            "notes": "Prasugrel chuyển hóa chủ yếu qua gan (CYP3A4, CYP2B6, CYP2C9, CYP2C19). Suy gan nặng là chống chỉ định tuyệt đối. Suy gan trung bình cần thận trọng và có thể cần giảm liều."
        },
        "overdose_management": {
            "symptoms": [
                "Triệu chứng chảy máu: Chảy máu nặng, có thể đe dọa tính mạng (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật)",
                "Triệu chứng thần kinh: Chóng mặt, nhức đầu",
                "Triệu chứng thiếu máu: Mệt mỏi, khó thở, da xanh"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều trị triệu chứng.",
            "treatment": [
                "Ngừng ngay prasugrel",
                "Điều trị chảy máu nặng:",
                "  - Truyền tiểu cầu nếu cần (nhưng hiệu quả hạn chế do prasugrel ức chế không hồi phục)",
                "  - Truyền máu nếu mất máu nặng",
                "  - Điều trị chảy máu dạ dày ruột: PPI, nội soi nếu cần",
                "  - Điều trị chảy máu nội sọ: phẫu thuật nếu cần",
                "  - Theo dõi dấu hiệu chảy máu chặt chẽ",
                "Điều trị thiếu máu nếu có:",
                "  - Truyền máu nếu cần",
                "  - Theo dõi Hct, Hb",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lưu ý: Prasugrel ức chế không hồi phục, tác dụng kéo dài 5-10 ngày sau khi ngừng"
            ],
            "monitoring": "Theo dõi dấu hiệu chảy máu (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật), công thức máu (thiếu máu, giảm tiểu cầu), dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có chảy máu nặng (tác dụng kéo dài 5-10 ngày sau khi ngừng)."
        },
        "reversal_agents": {
            "available": False,
            "agents": ["Truyền tiểu cầu có thể giúp một phần (nhưng hiệu quả hạn chế do prasugrel ức chế không hồi phục)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Không ảnh hưởng đáng kể đến hấp thu.",
                "timing": "Uống 1 lần/ngày, thường 10mg x 1 lần/ngày (hoặc 5mg nếu tuổi ≥75 tuổi hoặc cân nặng <60kg). Uống đúng giờ mỗi ngày. Không bỏ liều. QUAN TRỌNG: Dùng kèm aspirin 75-100mg/ngày. Giảm liều xuống 5mg/ngày ở bệnh nhân tuổi ≥75 tuổi hoặc cân nặng <60kg."
            },
            "iv": {
                "reconstitution": "Không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng uống"
            }
        },
        "pediatric_dosing": {
            "neonates": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "infants": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "children": "Không khuyến cáo cho trẻ <18 tuổi (dữ liệu hạn chế).",
            "adolescents": "≥18 tuổi: Liều người lớn. 60mg x 1 lần (loading), sau đó 10mg x 1 lần/ngày (maintenance). Giảm xuống 5mg/ngày nếu cân nặng <60kg.",
            "notes": "Dữ liệu hạn chế ở trẻ em. Chỉ dùng cho ACS/PCI ở trẻ ≥18 tuổi. Dùng kèm aspirin 75-100mg/ngày. Giảm liều xuống 5mg/ngày nếu cân nặng <60kg. Theo dõi dấu hiệu chảy máu chặt chẽ."
        },
        "geriatric_dosing": {
            "considerations": "Người cao tuổi (≥75 tuổi) có nguy cơ chảy máu cao hơn. CHỐNG CHỈ ĐỊNH ở tuổi ≥75 tuổi (trừ trường hợp đặc biệt). Nếu dùng: giảm liều xuống 5mg/ngày.",
            "dose_adjustment": "CHỐNG CHỈ ĐỊNH ở tuổi ≥75 tuổi (trừ trường hợp đặc biệt). Nếu dùng: giảm liều xuống 5mg/ngày. Không cần điều chỉnh liều ở suy thận.",
            "monitoring": "Theo dõi dấu hiệu chảy máu chặt chẽ (nguy cơ cao hơn ở người cao tuổi). Theo dõi công thức máu (thiếu máu, giảm tiểu cầu)."
        },
        "brand_names": {
            "vietnam": ["Effient", "Prasugrel", "Prasugrel Stada"],
            "common": ["Effient", "Prasugrel"]
        },
        "cost_estimate": {
            "unit": "VND",
            "range": "60,000 - 200,000 VND/viên (tùy hàm lượng và thương hiệu)",
            "note": "Giá thay đổi theo thương hiệu và nhà thuốc. Prasugrel generic thường rẻ hơn (60,000-120,000 VND/viên 10mg). Effient (brand) thường đắt hơn (120,000-200,000 VND/viên 10mg)."
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Effient (prasugrel)",
                "UpToDate - Prasugrel: Drug information",
                "TRITON-TIMI 38 Study - The New England Journal of Medicine (2007) - Prasugrel vs Clopidogrel trong ACS",
                "American Heart Association/American College of Cardiology guidelines - Antiplatelet therapy"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "High - Large RCT (TRITON-TIMI 38) and extensive clinical experience"
        }
    },
    
    "Fondaparinux": {
        "group": "Cardiovascular - Anticoagulant (Factor Xa Inhibitor)",
        "vietnamese_name": "Fondaparinux, Arixtra",
        "administration": ["SC"],
        "indications": [
            "Phòng ngừa huyết khối tĩnh mạch sâu (DVT) sau phẫu thuật hông/gối",
            "Điều trị DVT",
            "Điều trị thuyên tắc phổi (PE)",
            "Hội chứng mạch vành cấp (ACS) - không ST chênh lên"
        ],
        "contraindications": [
            "Dị ứng fondaparinux",
            "Chảy máu đang hoạt động",
            "Thiếu hụt antithrombin III nặng",
            "Suy thận nặng (CrCl <30)",
            "Có thai",
            "Cân nặng <50kg (tăng nguy cơ chảy máu)"
        ],
        "dosage": {
            "adult_dvt_pe_treatment": "5-10mg SC x 1 lần/ngày (theo cân nặng)",
            "adult_dvt_pe_prophylaxis": "2.5mg SC x 1 lần/ngày",
            "adult_acs": "2.5mg SC x 1 lần/ngày",
            "weight_based": "<50kg: không dùng; 50-100kg: 7.5mg/ngày; >100kg: 10mg/ngày",
            "notes": "Tiêm dưới da, không tiêm vào cơ. Không cần theo dõi aPTT/PTT (không ảnh hưởng)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể cần giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (tích lũy, tăng nguy cơ chảy máu)"
        },
        "side_effects": [
            "Chảy máu (phổ biến, có thể nặng)",
            "Giảm tiểu cầu (hiếm)",
            "Thiếu máu",
            "Phản ứng tại chỗ tiêm (đau, sưng, bầm tím)",
            "Tăng men gan (hiếm)"
        ],
        "interactions": [
            "Thuốc chống đông khác: tăng nguy cơ chảy máu",
            "Thuốc chống kết tập tiểu cầu: tăng nguy cơ chảy máu",
            "NSAID: tăng nguy cơ chảy máu"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Fondaparinux là synthetic pentasaccharide, ức chế chọn lọc factor Xa. Fondaparinux gắn với antithrombin III (ATIII), làm tăng khả năng ức chế factor Xa của ATIII. Ức chế factor Xa → giảm chuyển đổi prothrombin thành thrombin → giảm hình thành fibrin → giảm hình thành huyết khối. Fondaparinux không ức chế thrombin trực tiếp (khác với heparin). Tác dụng dài (17 giờ), dùng 1 lần/ngày. Không cần theo dõi aPTT/PTT (không ảnh hưởng đến các xét nghiệm đông máu thông thường).",
        "monitoring": [
            "Dấu hiệu chảy máu (chảy máu chân răng, chảy máu mũi, vết bầm tím, phân đen, nôn ra máu) - QUAN TRỌNG",
            "Công thức máu (Hct, Hb, tiểu cầu) nếu nghi ngờ chảy máu",
            "Chức năng thận (creatinine, eGFR) - CHỐNG CHỈ ĐỊNH ở CrCl <30",
            "Cân nặng - CHỐNG CHỈ ĐỊNH ở cân nặng <50kg",
            "Dấu hiệu phản ứng tại chỗ tiêm (đau, sưng, bầm tím)"
        ],
        "precautions": [
            "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy, tăng nguy cơ chảy máu",
            "CHỐNG CHỈ ĐỊNH ở cân nặng <50kg - tăng nguy cơ chảy máu",
            "NGUY CƠ CHẢY MÁU - theo dõi dấu hiệu chảy máu chặt chẽ",
            "Tiêm dưới da, không tiêm vào cơ (tăng nguy cơ chảy máu)",
            "Không cần theo dõi aPTT/PTT (không ảnh hưởng)",
            "Thận trọng ở suy thận trung bình (CrCl 30-60) - có thể cần giảm liều",
            "Tránh dùng với thuốc chống đông khác, thuốc chống kết tập tiểu cầu, NSAID (tăng nguy cơ chảy máu)",
            "Không có antidote đặc hiệu - điều trị hỗ trợ nếu chảy máu nặng",
            "Thời gian bán thải dài (17 giờ) - tác dụng kéo dài sau khi ngừng"
        ],
        "pharmacokinetics": {
            "half_life": "17 giờ (dài)",
            "onset": "2-3 giờ",
            "duration": "24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "94%",
            "metabolism": "Không chuyển hóa (bài tiết nguyên dạng qua thận)",
            "clearance": "Thận: bài tiết nguyên dạng (100%). Không chuyển hóa. Tích lũy ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Dạng ống tiêm: bảo quản trong bao bì kín.",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH ở suy thận nặng (CrCl <30) - tích lũy, tăng nguy cơ chảy máu nghiêm trọng. CHỐNG CHỈ ĐỊNH ở cân nặng <50kg - tăng nguy cơ chảy máu. Chảy máu nặng có thể dẫn đến tử vong. Không có antidote đặc hiệu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Thuốc chống đông khác (heparin, LMWH, warfarin, DOAC)",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nghiêm trọng",
                    "management": "TRÁNH DÙNG ĐỒNG THỜI. Nếu chuyển từ heparin/LMWH sang fondaparinux: ngừng heparin/LMWH trước khi bắt đầu fondaparinux."
                },
                {
                    "drug": "Thuốc chống kết tập tiểu cầu (aspirin, clopidogrel, ticagrelor, prasugrel)",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu và kết tập tiểu cầu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ. Có thể cần giảm liều một trong hai thuốc."
                },
                {
                    "drug": "NSAID (ibuprofen, naproxen, diclofenac)",
                    "mechanism": "NSAID ức chế kết tập tiểu cầu và gây loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu, đặc biệt chảy máu dạ dày ruột",
                    "management": "Thận trọng. Tránh dùng đồng thời nếu có thể. Nếu cần: dùng liều thấp, cân nhắc dùng PPI, theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng fondaparinux",
                "Chảy máu đang hoạt động - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI",
                "Suy thận nặng (CrCl <30) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (tích lũy, tăng nguy cơ chảy máu)",
                "Cân nặng <50kg - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (tăng nguy cơ chảy máu)",
                "Thiếu hụt antithrombin III nặng - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (giảm hiệu quả)"
            ],
            "tương_đối": [
                "Suy thận trung bình (CrCl 30-60) - thận trọng, có thể cần giảm liều",
                "Có thai (category B) - thận trọng",
                "Dùng với thuốc chống đông khác - tăng nguy cơ chảy máu",
                "Dùng với thuốc chống kết tập tiểu cầu - tăng nguy cơ chảy máu",
                "Dùng với NSAID - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Fondaparinux là FDA category B. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Không có nghiên cứu đầy đủ trên phụ nữ có thai. Có thể tăng nguy cơ chảy máu thai nhi, chảy máu nhau thai. Cân nhắc lợi ích/nguy cơ. Nếu cần dùng: theo dõi sát thai nhi và dấu hiệu chảy máu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Fondaparinux bài tiết vào sữa mẹ ở nồng độ thấp. Nồng độ trong máu trẻ bú mẹ thường rất thấp. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Fondaparinux không chuyển hóa ở gan, bài tiết nguyên dạng qua thận. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nặng (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật)",
                "Thiếu máu (mệt mỏi, khó thở, da xanh)",
                "Giảm tiểu cầu (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu. Protamine sulfate KHÔNG đảo ngược fondaparinux (khác với heparin/LMWH).",
            "treatment": [
                "Ngừng ngay fondaparinux",
                "Điều trị chảy máu nặng:",
                "  - Truyền máu nếu mất máu nặng",
                "  - Điều trị chảy máu dạ dày ruột: PPI, nội soi nếu cần",
                "  - Điều trị chảy máu nội sọ: phẫu thuật nếu cần",
                "  - Theo dõi dấu hiệu chảy máu chặt chẽ",
                "Điều trị thiếu máu nếu có:",
                "  - Truyền máu nếu cần",
                "  - Theo dõi Hct, Hb",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lưu ý: Fondaparinux có half-life dài (17 giờ), tác dụng kéo dài sau khi ngừng. Không có antidote đặc hiệu."
            ],
            "monitoring": "Theo dõi dấu hiệu chảy máu (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật), công thức máu (thiếu máu, giảm tiểu cầu), dấu hiệu sinh tồn trong ít nhất 24-48 giờ. Theo dõi lâu hơn nếu có chảy máu nặng (half-life 17 giờ)."
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Protamine sulfate KHÔNG đảo ngược fondaparinux (khác với heparin/LMWH). Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng."
        },
        "administration_instructions": {
            "oral": None,
            "sc": {
                "technique": "Tiêm dưới da (subcutaneous), thường ở bụng (cách rốn ít nhất 5cm), đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần. KHÔNG tiêm vào cơ (tăng nguy cơ chảy máu).",
                "timing": "Tiêm 1 lần/ngày, cùng giờ mỗi ngày. Liều: 2.5-10mg tùy chỉ định và cân nặng.",
                "after_use": "Không xoa bóp vị trí tiêm (tăng nguy cơ chảy máu).",
                "notes": "Tiêm dưới da, không tiêm vào cơ. Thay đổi vị trí tiêm mỗi lần. Không xoa bóp vị trí tiêm."
            },
            "iv": {
                "reconstitution": "Fondaparinux chỉ có dạng SC, không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng tiêm dưới da (SC)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Arixtra (fondaparinux)",
                "UpToDate - Fondaparinux: Drug information",
                "Lexicomp - Fondaparinux monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, multiple RCTs, clinical guidelines"
        }
    },
    "Enoxaparin": {
        "group": "Cardiovascular - Anticoagulant (Low Molecular Weight Heparin)",
        "vietnamese_name": "Enoxaparin, Lovenox, Clexane",
        "administration": ["SC"],
        "indications": [
            "Phòng ngừa DVT/PE sau phẫu thuật",
            "Điều trị DVT/PE",
            "Điều trị hội chứng mạch vành cấp (NSTEMI, STEMI)",
            "Phòng ngừa DVT/PE ở bệnh nhân nằm liệt giường"
        ],
        "contraindications": [
            "Dị ứng heparin, LMWH, hoặc pork products",
            "Chảy máu đang hoạt động",
            "Giảm tiểu cầu do heparin (HIT) - hiện tại hoặc tiền sử",
            "Suy thận nặng (CrCl <30) - tăng nguy cơ tích lũy"
        ],
        "dosage": {
            "adult_dvt_pe_treatment": "1mg/kg SC x 2 lần/ngày HOẶC 1.5mg/kg SC x 1 lần/ngày",
            "adult_dvt_pe_prophylaxis": "40mg SC x 1 lần/ngày",
            "adult_acs": "1mg/kg SC x 2 lần/ngày (kết hợp với aspirin)",
            "adult_surgery_prophylaxis": "40mg SC x 1 lần/ngày (bắt đầu 12 giờ trước phẫu thuật)",
            "adult_max": "Không có liều tối đa cố định, điều chỉnh theo cân nặng và chỉ định",
            "notes": "Liều điều chỉnh theo cân nặng. Không cần theo dõi aPTT thường xuyên (khác với heparin). Theo dõi anti-Xa nếu cần."
        },
        "side_effects": [
            "Chảy máu (nặng có thể tử vong)",
            "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm",
            "Tăng ALT/AST (hiếm)",
            "Phản ứng tại chỗ tiêm (đỏ, sưng, đau)",
            "Loãng xương (với dùng dài ngày)"
        ],
        "interactions": [
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Antiplatelets: tăng nguy cơ chảy máu",
            "Warfarin: tăng nguy cơ chảy máu (dùng chung trong quá trình chuyển đổi)",
            "Thrombolytics: tăng nguy cơ chảy máu nặng"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Enoxaparin là low molecular weight heparin (LMWH), ức chế yếu tố Xa và yếu tố IIa (thrombin) thông qua antithrombin III. Khác với heparin không phân đoạn, enoxaparin ưu tiên ức chế yếu tố Xa hơn yếu tố IIa (tỷ lệ 3:1 đến 4:1), có tác dụng dự đoán được hơn, ít gây HIT hơn, và không cần theo dõi aPTT thường xuyên. Tác dụng: phòng ngừa và điều trị DVT/PE, điều trị hội chứng mạch vành cấp. Tác dụng phụ: chảy máu (nặng có thể tử vong), giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm.",
        "monitoring": [
            "Dấu hiệu chảy máu: chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật",
            "Công thức máu (tiểu cầu) - giảm tiểu cầu do heparin (HIT), đặc biệt ngày 5-14",
            "Anti-Xa activity - nếu cần (thường không cần, trừ trường hợp đặc biệt: suy thận, béo phì, mang thai)",
            "Creatinine, CrCl - suy thận tăng nguy cơ tích lũy",
            "ALT/AST - tăng men gan hiếm"
        ],
        "precautions": [
            "Chảy máu - nguy hiểm, có thể tử vong, theo dõi dấu hiệu chảy máu chặt chẽ",
            "Giảm tiểu cầu do heparin (HIT) - hiếm nhưng nguy hiểm, thường xảy ra ngày 5-14, ngừng ngay nếu nghi ngờ",
            "Suy thận (CrCl <30) - tăng nguy cơ tích lũy, giảm liều hoặc tránh dùng",
            "Tiêm dưới da - không tiêm vào cơ, thay đổi vị trí tiêm mỗi lần, không xoa bóp vị trí tiêm",
            "Tránh dùng với aspirin/NSAID, antiplatelets - tăng nguy cơ chảy máu",
            "Chuyển đổi sang warfarin - dùng chung enoxaparin và warfarin trong quá trình chuyển đổi, theo dõi INR và dấu hiệu chảy máu",
            "Protamine sulfate - có thể đảo ngược một phần tác dụng enoxaparin (không hoàn toàn như heparin)"
        ],
        "pharmacokinetics": {
            "half_life": "4-5 giờ",
            "onset": "1-2 giờ (SC)",
            "duration": "12-24 giờ (tùy liều)",
            "protein_binding": "Minimal",
            "clearance": "Thận: bài tiết chủ yếu qua thận. Gan: chuyển hóa một phần. Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Không đông lạnh. Dạng tiêm: bảo quản trong bao bì kín.",
        "black_box_warnings": "Chảy máu nặng có thể dẫn đến tử vong. Giảm tiểu cầu do heparin (HIT) có thể gây huyết khối nặng và tử vong. Ngừng ngay nếu nghi ngờ HIT.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aspirin, NSAIDs (ibuprofen, naproxen)",
                    "mechanism": "Aspirin/NSAIDs ức chế kết tập tiểu cầu và gây loét dạ dày",
                    "effect": "Tăng nguy cơ chảy máu nặng, đặc biệt chảy máu dạ dày ruột",
                    "management": "TRÁNH DÙNG CHUNG nếu có thể. Nếu cần: dùng liều thấp aspirin (75-100mg), cân nhắc dùng PPI, theo dõi dấu hiệu chảy máu chặt chẽ."
                },
                {
                    "drug": "Antiplatelets (Clopidogrel, Ticagrelor, Prasugrel)",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu nặng",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ. Thường dùng trong ACS (kết hợp với aspirin)."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Dùng chung trong quá trình chuyển đổi sang warfarin. Theo dõi INR và dấu hiệu chảy máu chặt chẽ. Ngừng enoxaparin khi INR đạt mục tiêu."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng heparin, LMWH, hoặc pork products",
                "Chảy máu đang hoạt động",
                "Giảm tiểu cầu do heparin (HIT) - hiện tại hoặc tiền sử",
                "Suy thận nặng (CrCl <30) - tăng nguy cơ tích lũy"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60) - tăng nguy cơ tích lũy, giảm liều hoặc theo dõi anti-Xa",
                "Béo phì - có thể cần điều chỉnh liều, theo dõi anti-Xa",
                "Mang thai - có thể dùng nhưng cần theo dõi anti-Xa",
                "Dùng với aspirin/NSAID, antiplatelets - tăng nguy cơ chảy máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Enoxaparin là FDA category B. Các nghiên cứu trên động vật không cho thấy nguy cơ gây dị tật thai nhi. Có thể dùng trong thai kỳ, đặc biệt khi cần chống đông (ví dụ: van tim cơ học, huyết khối). Có thể tăng nguy cơ chảy máu thai nhi, chảy máu nhau thai. Theo dõi anti-Xa nếu cần. Cân nhắc lợi ích/nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Enoxaparin bài tiết vào sữa mẹ ở nồng độ rất thấp. Không hấp thu qua đường tiêu hóa, nồng độ trong máu trẻ bú mẹ thường không đáng kể. Không có báo cáo về tác dụng phụ nghiêm trọng ở trẻ bú mẹ.",
                "recommendation": "Có thể dùng khi cho con bú. Theo dõi trẻ nếu có dấu hiệu bất thường."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Thận trọng, theo dõi tác dụng phụ",
            "notes": "Enoxaparin chuyển hóa một phần ở gan. Suy gan ít ảnh hưởng đến nồng độ enoxaparin."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% hoặc theo dõi anti-Xa",
            "under_30": "Giảm liều 50% hoặc tránh dùng, theo dõi anti-Xa",
            "notes": "Enoxaparin bài tiết chủ yếu qua thận. Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy và tác dụng phụ (chảy máu)."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nặng (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật)",
                "Thiếu máu (mệt mỏi, khó thở, da xanh)",
                "Giảm tiểu cầu (hiếm)"
            ],
            "antidote": "Protamine sulfate - 1mg protamine cho mỗi 1mg enoxaparin (tối đa 100mg protamine). Lưu ý: Protamine chỉ đảo ngược một phần tác dụng enoxaparin (không hoàn toàn như heparin).",
            "treatment": [
                "Ngừng ngay enoxaparin",
                "Protamine sulfate: 1mg protamine cho mỗi 1mg enoxaparin (tối đa 100mg protamine), tiêm tĩnh mạch chậm (không quá 5mg/phút)",
                "Điều trị chảy máu nặng:",
                "  - Truyền máu nếu mất máu nặng",
                "  - Điều trị chảy máu dạ dày ruột: PPI, nội soi nếu cần",
                "  - Điều trị chảy máu nội sọ: phẫu thuật nếu cần",
                "  - Theo dõi dấu hiệu chảy máu chặt chẽ",
                "Điều trị thiếu máu nếu có:",
                "  - Truyền máu nếu cần",
                "  - Theo dõi Hct, Hb",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lưu ý: Protamine chỉ đảo ngược một phần tác dụng enoxaparin. Có thể cần điều trị hỗ trợ thêm."
            ],
            "monitoring": "Theo dõi dấu hiệu chảy máu (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật), công thức máu (thiếu máu, giảm tiểu cầu), dấu hiệu sinh tồn trong ít nhất 24 giờ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Protamine sulfate",
                    "dose": "1mg protamine cho mỗi 1mg enoxaparin (tối đa 100mg protamine)",
                    "route": "IV",
                    "notes": "Protamine chỉ đảo ngược một phần tác dụng enoxaparin (không hoàn toàn như heparin). Tiêm tĩnh mạch chậm (không quá 5mg/phút)."
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "sc": {
                "technique": "Tiêm dưới da (subcutaneous), thường ở bụng (cách rốn ít nhất 5cm), đùi, hoặc cánh tay. Thay đổi vị trí tiêm mỗi lần. KHÔNG tiêm vào cơ (tăng nguy cơ chảy máu).",
                "timing": "Tiêm 1-2 lần/ngày tùy chỉ định. Liều điều chỉnh theo cân nặng. Tiêm cùng giờ mỗi ngày.",
                "after_use": "Không xoa bóp vị trí tiêm (tăng nguy cơ chảy máu).",
                "notes": "Tiêm dưới da, không tiêm vào cơ. Thay đổi vị trí tiêm mỗi lần. Không xoa bóp vị trí tiêm."
            },
            "iv": {
                "reconstitution": "Enoxaparin chỉ có dạng SC, không có dạng IV",
                "infusion_rate": "N/A",
                "compatibility": [],
                "incompatibility": [],
                "notes": "Chỉ có dạng tiêm dưới da (SC)"
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Lovenox (enoxaparin)",
                "UpToDate - Enoxaparin: Drug information",
                "Lexicomp - Enoxaparin monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, multiple RCTs, clinical guidelines"
        }
    },
    "Rivaroxaban": {
        "group": "Cardiovascular - Anticoagulant (Direct Factor Xa Inhibitor - DOAC)",
        "vietnamese_name": "Rivaroxaban, Xarelto",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Phòng ngừa DVT/PE sau phẫu thuật thay khớp gối/háng",
            "Điều trị DVT/PE",
            "Phòng ngừa tái phát DVT/PE"
        ],
        "contraindications": [
            "Dị ứng",
            "Chảy máu đang hoạt động",
            "Suy thận nặng (CrCl <15)",
            "Bệnh gan nặng (Child-Pugh C)",
            "Mang thai"
        ],
        "dosage": {
            "adult_afib": "20mg x 1 lần/ngày (với bữa ăn), giảm xuống 15mg x 1 lần/ngày nếu CrCl 15-50",
            "adult_dvt_pe_treatment": "15mg x 2 lần/ngày x 21 ngày, sau đó 20mg x 1 lần/ngày",
            "adult_dvt_pe_prophylaxis": "10mg x 1 lần/ngày",
            "adult_surgery_prophylaxis": "10mg x 1 lần/ngày (bắt đầu 6-10 giờ sau phẫu thuật)",
            "adult_max": "20mg/ngày",
            "notes": "DOAC (Direct Oral Anticoagulant). Uống với bữa ăn để tăng hấp thu. Không cần theo dõi INR. Điều chỉnh liều theo CrCl."
        },
        "side_effects": [
            "Chảy máu (nặng có thể tử vong)",
            "Buồn nôn",
            "Tăng ALT/AST (hiếm)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Antiplatelets: tăng nguy cơ chảy máu",
            "CYP3A4/P-gp inhibitors mạnh (ketoconazole, ritonavir): tăng nồng độ rivaroxaban",
            "CYP3A4/P-gp inducers mạnh (rifampin, carbamazepine): giảm nồng độ rivaroxaban"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Rivaroxaban là direct factor Xa inhibitor (DOAC), ức chế trực tiếp yếu tố Xa, ngăn chặn sự hình thành thrombin và cục máu đông. Khác với warfarin, rivaroxaban không cần antithrombin III, có tác dụng dự đoán được, không cần theo dõi INR, và ít tương tác thuốc hơn. Tác dụng: phòng ngừa đột quỵ trong rung nhĩ, phòng ngừa và điều trị DVT/PE. Tác dụng phụ: chảy máu (nặng có thể tử vong).",
        "monitoring": [
            "Dấu hiệu chảy máu: chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật",
            "Creatinine, CrCl - điều chỉnh liều theo CrCl",
            "ALT/AST - tăng men gan hiếm",
            "Không cần theo dõi INR (khác với warfarin)"
        ],
        "precautions": [
            "Chảy máu - nguy hiểm, có thể tử vong, theo dõi dấu hiệu chảy máu chặt chẽ",
            "Suy thận (CrCl 15-50) - giảm liều, tránh dùng nếu CrCl <15",
            "Bệnh gan nặng (Child-Pugh C) - tránh dùng",
            "Uống với bữa ăn - tăng hấp thu, đặc biệt liều 15-20mg",
            "Tránh dùng với CYP3A4/P-gp inhibitors mạnh - tăng nồng độ rivaroxaban, tăng nguy cơ chảy máu",
            "Tránh dùng với CYP3A4/P-gp inducers mạnh - giảm nồng độ rivaroxaban, giảm hiệu quả",
            "Chuyển đổi từ warfarin - ngừng warfarin, bắt đầu rivaroxaban khi INR <3.0",
            "Chuyển đổi sang warfarin - giảm liều rivaroxaban 50%, bắt đầu warfarin, theo dõi INR"
        ],
        "pharmacokinetics": {
            "half_life": "5-9 giờ (trẻ), 11-13 giờ (già)",
            "onset": "2-4 giờ (PO)",
            "duration": "12-24 giờ",
            "protein_binding": "92-95%",
            "clearance": "Gan: chuyển hóa qua CYP3A4, CYP2J2. Thận: bài tiết một phần nguyên dạng (33%) và metabolites. Cần điều chỉnh liều ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Chảy máu nặng có thể dẫn đến tử vong. Không có antidote đặc hiệu (trước khi có andexanet alfa). Ngừng ngay trước phẫu thuật có nguy cơ chảy máu cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4/P-gp inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế chuyển hóa và bài tiết rivaroxaban, tăng nồng độ rivaroxaban",
                    "effect": "Tăng nồng độ rivaroxaban, tăng nguy cơ chảy máu",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: giảm liều rivaroxaban 50% hoặc tránh dùng."
                },
                {
                    "drug": "CYP3A4/P-gp inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng chuyển hóa và bài tiết rivaroxaban, giảm nồng độ rivaroxaban",
                    "effect": "Giảm nồng độ rivaroxaban, giảm hiệu quả",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: tăng liều rivaroxaban hoặc chuyển sang warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng rivaroxaban hoặc các thành phần khác",
                "Chảy máu đang hoạt động",
                "Suy thận nặng (CrCl <15) - tăng nguy cơ tích lũy",
                "Bệnh gan nặng (Child-Pugh C) - tăng nguy cơ chảy máu",
                "Mang thai - nguy cơ dị tật thai nhi, chảy máu thai nhi"
            ],
            "tương_đối": [
                "Suy thận (CrCl 15-50) - giảm liều",
                "Bệnh gan (Child-Pugh A, B) - thận trọng",
                "Dùng với CYP3A4/P-gp inhibitors mạnh - tránh dùng hoặc giảm liều",
                "Dùng với CYP3A4/P-gp inducers mạnh - tránh dùng hoặc tăng liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Rivaroxaban là FDA category X. Có nguy cơ dị tật thai nhi và chảy máu thai nhi. CHỐNG CHỈ ĐỊNH trong thai kỳ. Nếu có thai khi đang dùng: ngừng ngay, tư vấn di truyền.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết rivaroxaban có bài tiết vào sữa mẹ hay không. Không nên dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần: ngừng cho con bú hoặc chuyển sang thuốc khác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "CHỐNG CHỈ ĐỊNH (Child-Pugh C)",
            "notes": "Rivaroxaban chuyển hóa ở gan qua CYP3A4, CYP2J2. Suy gan nặng (Child-Pugh C) làm tăng nguy cơ chảy máu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50% (tùy chỉ định)",
            "15_30": "Giảm liều 50% hoặc tránh dùng",
            "under_15": "CHỐNG CHỈ ĐỊNH",
            "notes": "Rivaroxaban bài tiết một phần qua thận (33% nguyên dạng). Suy thận làm giảm thải trừ, tăng nguy cơ tích lũy và tác dụng phụ (chảy máu)."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nặng (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật)",
                "Thiếu máu (mệt mỏi, khó thở, da xanh)"
            ],
            "antidote": "Andexanet alfa (Andexxa) - antidote đặc hiệu cho factor Xa inhibitors. Liều: 400-800mg IV bolus, sau đó truyền liên tục. Nếu không có: điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay rivaroxaban",
                "Andexanet alfa (nếu có): 400-800mg IV bolus, sau đó truyền liên tục",
                "Điều trị chảy máu nặng:",
                "  - Truyền máu nếu mất máu nặng",
                "  - Điều trị chảy máu dạ dày ruột: PPI, nội soi nếu cần",
                "  - Điều trị chảy máu nội sọ: phẫu thuật nếu cần",
                "  - Theo dõi dấu hiệu chảy máu chặt chẽ",
                "Điều trị thiếu máu nếu có:",
                "  - Truyền máu nếu cần",
                "  - Theo dõi Hct, Hb",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lưu ý: Half-life 5-13 giờ, tác dụng kéo dài sau khi ngừng."
            ],
            "monitoring": "Theo dõi dấu hiệu chảy máu (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật), công thức máu (thiếu máu), dấu hiệu sinh tồn trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Andexanet alfa (Andexxa)",
                    "dose": "400-800mg IV bolus, sau đó truyền liên tục",
                    "route": "IV",
                    "notes": "Antidote đặc hiệu cho factor Xa inhibitors (rivaroxaban, apixaban, edoxaban). Có thể đảo ngược tác dụng chống đông."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Uống với bữa ăn để tăng hấp thu, đặc biệt liều 15-20mg. Liều 10mg có thể uống không cần thức ăn.",
                "timing": "Uống 1-2 lần/ngày tùy chỉ định. Uống cùng thời điểm mỗi ngày. Không bỏ liều."
            },
            "im": None,
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Xarelto (rivaroxaban)",
                "UpToDate - Rivaroxaban: Drug information",
                "Lexicomp - Rivaroxaban monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, multiple RCTs, clinical guidelines"
        }
    },
    "Apixaban": {
        "group": "Cardiovascular - Anticoagulant (Direct Factor Xa Inhibitor - DOAC)",
        "vietnamese_name": "Apixaban, Eliquis",
        "administration": ["PO"],
        "indications": [
            "Phòng ngừa đột quỵ trong rung nhĩ không do van tim",
            "Phòng ngừa DVT/PE sau phẫu thuật thay khớp gối/háng",
            "Điều trị DVT/PE",
            "Phòng ngừa tái phát DVT/PE"
        ],
        "contraindications": [
            "Dị ứng",
            "Chảy máu đang hoạt động",
            "Bệnh gan nặng (Child-Pugh C)"
        ],
        "dosage": {
            "adult_afib": "5mg x 2 lần/ngày, giảm xuống 2.5mg x 2 lần/ngày nếu có ≥2 yếu tố: tuổi ≥80, cân nặng ≤60kg, Cr ≥1.5mg/dL",
            "adult_dvt_pe_treatment": "10mg x 2 lần/ngày x 7 ngày, sau đó 5mg x 2 lần/ngày",
            "adult_dvt_pe_prophylaxis": "2.5mg x 2 lần/ngày",
            "adult_surgery_prophylaxis": "2.5mg x 2 lần/ngày (bắt đầu 12-24 giờ sau phẫu thuật)",
            "adult_max": "10mg/ngày",
            "notes": "DOAC (Direct Oral Anticoagulant). Uống với hoặc không có thức ăn. Không cần theo dõi INR. Điều chỉnh liều theo tuổi, cân nặng, Cr."
        },
        "side_effects": [
            "Chảy máu (nặng có thể tử vong)",
            "Buồn nôn",
            "Tăng ALT/AST (hiếm)",
            "Phản ứng dị ứng (hiếm)"
        ],
        "interactions": [
            "Aspirin/NSAID: tăng nguy cơ chảy máu",
            "Antiplatelets: tăng nguy cơ chảy máu",
            "CYP3A4/P-gp inhibitors mạnh (ketoconazole, ritonavir): tăng nồng độ apixaban",
            "CYP3A4/P-gp inducers mạnh (rifampin, carbamazepine): giảm nồng độ apixaban"
        ],
        "pregnancy": "X",
        "mechanism_of_action": "Apixaban là direct factor Xa inhibitor (DOAC), ức chế trực tiếp yếu tố Xa, ngăn chặn sự hình thành thrombin và cục máu đông. Khác với warfarin, apixaban không cần antithrombin III, có tác dụng dự đoán được, không cần theo dõi INR, và ít tương tác thuốc hơn. Tác dụng: phòng ngừa đột quỵ trong rung nhĩ, phòng ngừa và điều trị DVT/PE. Tác dụng phụ: chảy máu (nặng có thể tử vong).",
        "monitoring": [
            "Dấu hiệu chảy máu: chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật",
            "Creatinine - điều chỉnh liều theo Cr (kết hợp với tuổi, cân nặng)",
            "ALT/AST - tăng men gan hiếm",
            "Không cần theo dõi INR (khác với warfarin)"
        ],
        "precautions": [
            "Chảy máu - nguy hiểm, có thể tử vong, theo dõi dấu hiệu chảy máu chặt chẽ",
            "Bệnh gan nặng (Child-Pugh C) - tránh dùng",
            "Điều chỉnh liều theo tuổi, cân nặng, Cr - giảm liều nếu có ≥2 yếu tố: tuổi ≥80, cân nặng ≤60kg, Cr ≥1.5mg/dL",
            "Tránh dùng với CYP3A4/P-gp inhibitors mạnh - tăng nồng độ apixaban, tăng nguy cơ chảy máu",
            "Tránh dùng với CYP3A4/P-gp inducers mạnh - giảm nồng độ apixaban, giảm hiệu quả",
            "Chuyển đổi từ warfarin - ngừng warfarin, bắt đầu apixaban khi INR <2.0",
            "Chuyển đổi sang warfarin - giảm liều apixaban 50%, bắt đầu warfarin, theo dõi INR"
        ],
        "pharmacokinetics": {
            "half_life": "12 giờ",
            "onset": "1-3 giờ (PO)",
            "duration": "12-24 giờ",
            "protein_binding": "87%",
            "clearance": "Gan: chuyển hóa qua CYP3A4. Thận: bài tiết một phần nguyên dạng (25%) và metabolites. Cần điều chỉnh liều ở suy thận nặng."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nén: bảo quản trong bao bì kín.",
        "black_box_warnings": "Chảy máu nặng có thể dẫn đến tử vong. Không có antidote đặc hiệu (trước khi có andexanet alfa). Ngừng ngay trước phẫu thuật có nguy cơ chảy máu cao.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "CYP3A4/P-gp inhibitors mạnh (Ketoconazole, Itraconazole, Ritonavir)",
                    "mechanism": "Ức chế chuyển hóa và bài tiết apixaban, tăng nồng độ apixaban",
                    "effect": "Tăng nồng độ apixaban, tăng nguy cơ chảy máu",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: giảm liều apixaban 50% hoặc tránh dùng."
                },
                {
                    "drug": "CYP3A4/P-gp inducers mạnh (Rifampin, Carbamazepine, Phenytoin)",
                    "mechanism": "Cảm ứng chuyển hóa và bài tiết apixaban, giảm nồng độ apixaban",
                    "effect": "Giảm nồng độ apixaban, giảm hiệu quả",
                    "management": "TRÁNH DÙNG CHUNG. Nếu bắt buộc: tăng liều apixaban hoặc chuyển sang warfarin."
                }
            ],
            "moderate": [
                {
                    "drug": "Aspirin, NSAIDs",
                    "mechanism": "Tác dụng hiệp đồng ức chế đông máu",
                    "effect": "Tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi dấu hiệu chảy máu chặt chẽ."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng apixaban hoặc các thành phần khác",
                "Chảy máu đang hoạt động",
                "Bệnh gan nặng (Child-Pugh C) - tăng nguy cơ chảy máu",
                "Mang thai - nguy cơ dị tật thai nhi, chảy máu thai nhi"
            ],
            "tương_đối": [
                "Bệnh gan (Child-Pugh A, B) - thận trọng",
                "Suy thận nặng - điều chỉnh liều",
                "Dùng với CYP3A4/P-gp inhibitors mạnh - tránh dùng hoặc giảm liều",
                "Dùng với CYP3A4/P-gp inducers mạnh - tránh dùng hoặc tăng liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Apixaban là FDA category X. Có nguy cơ dị tật thai nhi và chảy máu thai nhi. CHỐNG CHỈ ĐỊNH trong thai kỳ. Nếu có thai khi đang dùng: ngừng ngay, tư vấn di truyền.",
            "lactation": {
                "safety": "Unknown",
                "details": "Chưa biết apixaban có bài tiết vào sữa mẹ hay không. Không nên dùng khi cho con bú.",
                "recommendation": "Tránh dùng khi cho con bú. Nếu cần: ngừng cho con bú hoặc chuyển sang thuốc khác."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, theo dõi tác dụng phụ",
            "severe": "CHỐNG CHỈ ĐỊNH (Child-Pugh C)",
            "notes": "Apixaban chuyển hóa ở gan qua CYP3A4. Suy gan nặng (Child-Pugh C) làm tăng nguy cơ chảy máu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Điều chỉnh liều theo tuổi, cân nặng, Cr",
            "under_30": "Điều chỉnh liều theo tuổi, cân nặng, Cr",
            "notes": "Apixaban bài tiết một phần qua thận (25% nguyên dạng). Suy thận nặng cần điều chỉnh liều (kết hợp với tuổi, cân nặng)."
        },
        "overdose_management": {
            "symptoms": [
                "Chảy máu nặng (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật)",
                "Thiếu máu (mệt mỏi, khó thở, da xanh)"
            ],
            "antidote": "Andexanet alfa (Andexxa) - antidote đặc hiệu cho factor Xa inhibitors. Liều: 400-800mg IV bolus, sau đó truyền liên tục. Nếu không có: điều trị hỗ trợ.",
            "treatment": [
                "Ngừng ngay apixaban",
                "Andexanet alfa (nếu có): 400-800mg IV bolus, sau đó truyền liên tục",
                "Điều trị chảy máu nặng:",
                "  - Truyền máu nếu mất máu nặng",
                "  - Điều trị chảy máu dạ dày ruột: PPI, nội soi nếu cần",
                "  - Điều trị chảy máu nội sọ: phẫu thuật nếu cần",
                "  - Theo dõi dấu hiệu chảy máu chặt chẽ",
                "Điều trị thiếu máu nếu có:",
                "  - Truyền máu nếu cần",
                "  - Theo dõi Hct, Hb",
                "Theo dõi dấu hiệu sinh tồn: Huyết áp, nhịp tim, nhịp thở, SpO2",
                "Lưu ý: Half-life 12 giờ, tác dụng kéo dài sau khi ngừng."
            ],
            "monitoring": "Theo dõi dấu hiệu chảy máu (chảy máu dạ dày ruột, chảy máu nội sọ, chảy máu sau phẫu thuật), công thức máu (thiếu máu), dấu hiệu sinh tồn trong ít nhất 24-48 giờ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Andexanet alfa (Andexxa)",
                    "dose": "400-800mg IV bolus, sau đó truyền liên tục",
                    "route": "IV",
                    "notes": "Antidote đặc hiệu cho factor Xa inhibitors (rivaroxaban, apixaban, edoxaban). Có thể đảo ngược tác dụng chống đông."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn.",
                "timing": "Uống 2 lần/ngày (sáng và tối). Uống cùng thời điểm mỗi ngày. Không bỏ liều."
            },
            "im": None,
            "iv": None
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Eliquis (apixaban)",
                "UpToDate - Apixaban: Drug information",
                "Lexicomp - Apixaban monograph",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - FDA-approved, multiple RCTs, clinical guidelines"
        }
    }

}

__all__ = ['ANTICOAGULANTS']
