"""Respiratory Medications
Active module - fixed-dose combination inhalers (ICS/LABA, LAMA/LABA, SAMA/SABA)"""

COMBINATION_INHALERS_DRUGS = {
    "Budesonide/Formoterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Budesonide/Formoterol, Symbicort",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát + cắt cơn theo GINA: SMART/MART)",
            "COPD có nhiều đợt cấp (ICS/LABA)",
        ],
        "contraindications": [
            "Dị ứng với budesonide, formoterol hoặc bất kỳ thành phần nào",
            "Hen phế quản cấp (không dùng đơn độc để cắt cơn nếu không theo phác đồ SMART/MART)",
        ],
        "dosage": {
            "adult_asthma_maintenance": "160/4.5mcg: 2 hít x 2 lần/ngày (sáng, tối)",
            "adult_asthma_smart": "160/4.5mcg: 1-2 hít x 1-2 lần/ngày duy trì + 1 hít khi cần, tối đa 12 hít/ngày",
            "adult_copd": "160/4.5mcg: 2 hít x 2 lần/ngày",
            "notes": "Dùng đều đặn hàng ngày. Trong phác đồ SMART/MART, có thể dùng thêm để cắt cơn nhẹ thay SABA.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Hấp thu toàn thân ít từ dạng hít. Không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Nấm miệng (do ICS)",
            "Khàn tiếng",
            "Ho, kích ứng họng",
            "Tim đập nhanh, run cơ (do LABA)",
            "Đau đầu",
        ],
        "interactions": [
            "Ritonavir, ketoconazole, itraconazole: tăng nồng độ budesonide",
            "Beta-blocker: đối kháng tác dụng formoterol",
            "Theophylline: tăng tác dụng phụ tim mạch",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Phối hợp ICS (budesonide) kháng viêm tại chỗ và LABA (formoterol) giãn phế quản kéo dài, khởi phát nhanh. Dùng vừa để kiểm soát vừa để cắt cơn (SMART/MART).",
        "monitoring": [
            "Triệu chứng hen/COPD, số lần cơn cấp, nhu cầu SABA",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, run cơ",
        ],
        "precautions": [
            "Súc miệng sau khi dùng để tránh nấm miệng.",
            "Không dùng LABA đơn độc cho hen – luôn đi kèm ICS.",
            "Trong phác đồ SMART/MART: cần hướng dẫn rõ cho bệnh nhân về tối đa số hít/ngày.",
        ],
        "pharmacokinetics": {
            "half_life": "Budesonide: 2-3 giờ; Formoterol: 10 giờ",
            "onset": "Formoterol: 1-3 phút (khởi phát nhanh); Budesonide: vài giờ",
            "duration": "Formoterol: 12 giờ; Budesonide: tác dụng tại chỗ kéo dài",
            "protein_binding": "Budesonide: 88-90%; Formoterol: 50-65%",
            "clearance": "Budesonide: chuyển hóa gan (CYP3A4) thành chất không hoạt tính, thải qua thận; Formoterol: chuyển hóa gan (CYP2D6, CYP2C19), thải qua thận và phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Ritonavir, ketoconazole, itraconazole",
                    "mechanism": "Ức chế CYP3A4, tăng chuyển hóa budesonide",
                    "effect": "Tăng nồng độ budesonide toàn thân, tăng nguy cơ ức chế HPA",
                    "management": "Thận trọng. Theo dõi dấu hiệu ức chế HPA. Có thể cần giảm liều."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng formoterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc. Có thể dùng beta-blockers chọn lọc tim mạch khi cần."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Tác dụng cộng dồn trên tim mạch",
                    "effect": "Tăng tác dụng phụ tim mạch (nhịp tim nhanh, run cơ)",
                    "management": "Thận trọng. Theo dõi nhịp tim, dấu hiệu lâm sàng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với budesonide, formoterol hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng đơn độc để cắt cơn nếu không theo phác đồ SMART/MART",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Budesonide và formoterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Budesonide và formoterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Budesonide và formoterol chuyển hóa qua gan (CYP3A4, CYP2D6, CYP2C19). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh, run cơ (do formoterol)",
                "Tăng đường huyết (do formoterol)",
                "Hạ kali máu (do formoterol)",
                "Ức chế HPA (nếu hấp thu nhiều budesonide)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của formoterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân hen",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu",
                "Theo dõi dấu hiệu ức chế HPA nếu hấp thu nhiều budesonide"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu ức chế HPA"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Có thể cần bổ sung corticosteroid nếu có suy thượng thận do ICS."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Lắc kỹ trước khi dùng. Thở ra hoàn toàn. Đặt ống hít vào miệng, bắt đầu hít sâu và chậm, đồng thời ấn nút. Giữ hơi 10 giây. Thở ra từ từ. Súc miệng sau khi dùng.",
                "timing": "2 lần/ngày (sáng, tối) hoặc theo phác đồ SMART/MART",
                "notes": "QUAN TRỌNG: 1) Súc miệng sau khi dùng để tránh nấm miệng, 2) Không dùng LABA đơn độc cho hen, 3) Trong phác đồ SMART/MART: tối đa 12 hít/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Symbicort (budesonide/formoterol)",
                "GINA Guidelines - Global Initiative for Asthma",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
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
         "black_box_warnings": None,
         "black_box_warnings": "Không có",
},
    "Fluticasone/Salmeterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Fluticasone/Salmeterol, Seretide, Advair",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD có nhiều đợt cấp",
        ],
        "contraindications": [
            "Dị ứng với fluticasone, salmeterol hoặc thành phần khác",
            "Hen phế quản cấp (không dùng để cắt cơn)",
        ],
        "dosage": {
            "adult_asthma": "250/50mcg: 1 hít x 2 lần/ngày; điều chỉnh theo mức độ hen",
            "adult_copd": "250/50mcg: 1 hít x 2 lần/ngày",
            "notes": "Không dùng để cắt cơn; cần SABA kèm theo.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Hấp thu toàn thân ít từ dạng hít. Không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Tim đập nhanh, run cơ (LABA)",
            "Đau đầu",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Ritonavir: tăng mạnh nồng độ fluticasone (tránh dùng)",
            "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
            "Beta-blocker: đối kháng tác dụng salmeterol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "ICS (fluticasone) kháng viêm + LABA (salmeterol) giãn phế quản kéo dài 12 giờ. Cải thiện kiểm soát hen/COPD khi đơn trị ICS hoặc LABA không đủ.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng LABA đơn độc cho hen.",
            "Tránh dùng với ritonavir nếu có thể.",
        ],
        "pharmacokinetics": {
            "half_life": "Fluticasone: 7.8 giờ; Salmeterol: 5.5 giờ",
            "onset": "Salmeterol: 10-20 phút; Fluticasone: vài giờ",
            "duration": "Salmeterol: 12 giờ; Fluticasone: tác dụng tại chỗ kéo dài",
            "protein_binding": "Fluticasone: 91%; Salmeterol: 96%",
            "clearance": "Fluticasone: chuyển hóa gan (CYP3A4) thành chất không hoạt tính, thải qua phân; Salmeterol: chuyển hóa gan (CYP3A4), thải qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng LABA đơn độc cho hen phế quản - luôn phải kết hợp với ICS. Tăng nguy cơ tử vong do hen khi dùng LABA không kèm ICS.",
             "drug_interactions": {
             "major": [],
             "moderate": [],
             "minor": [
                 {
                     "drug": "Ritonavir: tăng mạnh nồng độ fluticasone (tránh dùng)",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Beta-blocker: đối kháng tác dụng salmeterol",
                     "mechanism": "Tương tác lâm sàng"
                 }
             ]
         },
         "pregnancy_lactation": {
             "fda_category": "C",
             "pregnancy_details": "Category C - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
             "lactation": {
                 "safety": "Compatible with monitoring",
                 "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                 "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
             }
         },
         "hepatic_adjustment": {
             "mild": "Không đổi",
             "moderate": "Thận trọng",
             "severe": "Thận trọng, có thể giảm liều",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
         },
         "overdose_management": {
             "symptoms": [
                 "Cần tra cứu thêm thông tin về triệu chứng quá liều"
             ],
             "antidote": "Không có antidote đặc hiệu",
             "treatment": [
                 "Ngừng ngay thuốc",
                 "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                 "Than hoạt tính",
                 "Điều trị hỗ trợ và điều trị triệu chứng",
                 "Theo dõi dấu hiệu sinh tồn"
             ],
             "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
         },
         "reversal_agents": {
             "available": False,
             "agents": []
         },
         "administration_instructions": {},
         "references": {
             "primary_sources": [
                 "FDA Drug Label - Fluticasone/Salmeterol inhaler",
                 "UpToDate - Cần cập nhật"
             ],
             "last_updated": "2025-12-28",
             "evidence_level": "C - Cần tra cứu và cập nhật"
         },
},
    "Fluticasone/Umeclidinium/Vilanterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LAMA/LABA)",
        "vietnamese_name": "Fluticasone/Umeclidinium/Vilanterol, Trelegy Ellipta",
        "administration": ["Inhalation"],
        "indications": [
            "COPD nặng, nhiều đợt cấp (triple therapy)",
            "Hen phế quản không kiểm soát với ICS/LABA",
        ],
        "contraindications": [
            "Dị ứng với fluticasone, umeclidinium, vilanterol",
            "Dùng cùng ritonavir (tăng mạnh nồng độ fluticasone)",
        ],
        "dosage": {
            "adult_copd": "100/62.5/25mcg: 1 hít x 1 lần/ngày",
            "adult_asthma": "200/62.5/25mcg: 1 hít x 1 lần/ngày (tùy mức độ)",
            "notes": "Dùng đều đặn 1 lần/ngày; không dùng để cắt cơn.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "LAMA thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA)",
        ],
        "interactions": [
            "Ritonavir: chống chỉ định (tăng mạnh nồng độ fluticasone)",
            "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Phối hợp 3 trong 1: ICS (fluticasone) kháng viêm, LAMA (umeclidinium) và LABA (vilanterol) giãn phế quản kéo dài, tối ưu hóa kiểm soát COPD/hen nặng.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, tác dụng phụ anticholinergic",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng với ritonavir.",
        ],
        "pharmacokinetics": {
            "half_life": "Fluticasone: 7.8 giờ; Umeclidinium: 11 giờ; Vilanterol: 11 giờ",
            "onset": "Vilanterol: 5 phút; Umeclidinium: 5-15 phút; Fluticasone: vài giờ",
            "duration": "Cả ba: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Fluticasone: 91%; Umeclidinium: 89%; Vilanterol: 94%",
            "clearance": "Fluticasone: chuyển hóa gan (CYP3A4), thải qua phân; Umeclidinium: chuyển hóa gan (CYP2D6), thải qua phân và thận; Vilanterol: chuyển hóa gan (CYP3A4), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng với ritonavir do tăng mạnh nồng độ fluticasone gây tác dụng phụ nghiêm trọng. Không dùng LABA đơn độc cho hen phế quản.",
             "drug_interactions": {
             "major": [],
             "moderate": [],
             "minor": [
                 {
                     "drug": "Ritonavir: chống chỉ định (tăng mạnh nồng độ fluticasone)",
                     "mechanism": "Tương tác lâm sàng"
                 },
                 {
                     "drug": "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
                     "mechanism": "Tương tác lâm sàng"
                 }
             ]
         },
         "pregnancy_lactation": {
             "fda_category": "C",
             "pregnancy_details": "Category C - Cần tra cứu thêm thông tin chi tiết về sử dụng trong thai kỳ.",
             "lactation": {
                 "safety": "Compatible with monitoring",
                 "details": "Cần tra cứu thêm thông tin chi tiết về bài tiết vào sữa mẹ.",
                 "recommendation": "Thận trọng khi cho con bú, tra cứu thêm thông tin."
             }
         },
         "hepatic_adjustment": {
             "mild": "Không đổi",
             "moderate": "Thận trọng",
             "severe": "Thận trọng, có thể giảm liều",
             "notes": "Cần tra cứu thêm thông tin chi tiết về điều chỉnh liều ở suy gan."
         },
         "overdose_management": {
             "symptoms": [
                 "Cần tra cứu thêm thông tin về triệu chứng quá liều"
             ],
             "antidote": "Không có antidote đặc hiệu",
             "treatment": [
                 "Ngừng ngay thuốc",
                 "Rửa dạ dày nếu uống trong vòng 1-2 giờ (nếu phù hợp)",
                 "Than hoạt tính",
                 "Điều trị hỗ trợ và điều trị triệu chứng",
                 "Theo dõi dấu hiệu sinh tồn"
             ],
             "monitoring": "Theo dõi dấu hiệu sinh tồn, triệu chứng lâm sàng"
         },
         "reversal_agents": {
             "available": False,
             "agents": []
         },
         "administration_instructions": {},
         "references": {
             "primary_sources": [
                 "FDA Drug Label - Fluticasone/Umeclidinium/Vilanterol inhaler",
                 "UpToDate - Cần cập nhật"
             ],
             "last_updated": "2025-12-28",
             "evidence_level": "C - Cần tra cứu và cập nhật"
         },
},
    "Ipratropium/Salbutamol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (SAMA/SABA)",
        "vietnamese_name": "Ipratropium/Salbutamol, Combivent, Duoneb",
        "administration": ["Inhalation", "Nebulizer"],
        "indications": [
            "COPD đợt cấp",
            "Cơn hen nặng (kết hợp SABA + SAMA)",
        ],
        "contraindications": [
            "Dị ứng với ipratropium, atropine, salbutamol",
            "Glaucoma góc đóng, tăng nhãn áp nặng",
        ],
        "dosage": {
            "adult_inhaler": "1-2 puffs mỗi 4-6 giờ khi cần",
            "adult_nebulizer": "2.5mg salbutamol + 0.5mg ipratropium mỗi 4-6 giờ",
            "notes": "Thường dùng trong cấp cứu/đợt cấp; theo dõi sát nhịp tim và hô hấp.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Hấp thu toàn thân ít từ dạng hít. Không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Tim đập nhanh, run cơ (SABA)",
            "Khô miệng, đắng miệng (SAMA)",
            "Ho, kích ứng họng",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ khô miệng, bí tiểu",
            "Beta-blocker: giảm tác dụng salbutamol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Hiệp đồng SABA (salbutamol – kích thích beta-2) và SAMA (ipratropium – ức chế muscarinic), giãn phế quản mạnh trong đợt cấp COPD/hen.",
        "monitoring": [
            "Nhịp tim, huyết áp",
            "Đáp ứng phế quản, SpO2",
            "Dấu hiệu tăng nhãn áp nếu thuốc vào mắt",
        ],
        "precautions": [
            "Tránh thuốc vào mắt (nguy cơ tăng nhãn áp).",
            "Thận trọng ở bệnh nhân tim mạch, loạn nhịp.",
        ],
        "pharmacokinetics": {
            "half_life": "Ipratropium: 2 giờ; Salbutamol: 3.8 giờ",
            "onset": "Salbutamol: 5-15 phút; Ipratropium: 15-30 phút",
            "duration": "Salbutamol: 3-6 giờ; Ipratropium: 4-6 giờ",
            "protein_binding": "Ipratropium: <20%; Salbutamol: 10%",
            "clearance": "Ipratropium: thải trừ chủ yếu qua thận (dạng nguyên dạng); Salbutamol: chuyển hóa gan (sulfation), thải qua thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng salbutamol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                },
                {
                    "drug": "Anticholinergics khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu anticholinergic."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với ipratropium, atropine, salbutamol"
            ],
            "tương_đối": [
                "Glaucoma góc đóng - thận trọng",
                "Phì đại tuyến tiền liệt - thận trọng",
                "Bệnh tim mạch - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Ipratropium và salbutamol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Ipratropium và salbutamol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (salbutamol chuyển hóa qua gan)",
            "severe": "Thận trọng",
            "notes": "Salbutamol chuyển hóa qua gan (sulfation). Ipratropium thải trừ chủ yếu qua thận. Suy gan có thể ảnh hưởng đến salbutamol. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh, run cơ (do salbutamol)",
                "Khô miệng, bí tiểu (do ipratropium)",
                "Tăng đường huyết (do salbutamol)",
                "Hạ kali máu (do salbutamol)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của salbutamol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân hen/COPD",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu anticholinergic"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Lắc kỹ trước khi dùng. Thở ra hoàn toàn. Đặt ống hít vào miệng, bắt đầu hít sâu và chậm, đồng thời ấn nút. Giữ hơi 10 giây. Thở ra từ từ.",
                "timing": "3-4 lần/ngày khi cần (cho cơn cấp)",
                "notes": "Dùng cho COPD đợt cấp, cơn hen nặng. Không dùng thường quy, chỉ dùng khi cần."
            },
            "nebulizer": {
                "technique": "Pha trong Normal saline, phun sương qua máy phun sương",
                "timing": "3-4 lần/ngày khi cần",
                "notes": "Dùng cho COPD đợt cấp nặng, cơn hen nặng. Theo protocol cụ thể."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Combivent, Duoneb (ipratropium/salbutamol)",
                "GINA Guidelines - Global Initiative for Asthma",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
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
    "Tiotropium/Olodaterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (LAMA/LABA)",
        "vietnamese_name": "Tiotropium/Olodaterol, Spiolto Respimat, Stiolto Respimat",
        "administration": ["Inhalation"],
        "indications": [
            "COPD (phòng ngừa triệu chứng và đợt cấp)",
        ],
        "contraindications": [
            "Dị ứng với tiotropium, olodaterol",
            "Glaucoma góc đóng, phì đại tuyến tiền liệt nặng",
            "Hen phế quản cấp (không dùng để cắt cơn)",
        ],
        "dosage": {
            "adult_copd": "2 puffs (5/5mcg) x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày, không dùng để cắt cơn.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Tránh dùng hoặc theo dõi rất sát", "dialysis": "Thận trọng", "notes": "LAMA thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."},
        "side_effects": [
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA – hiếm)",
            "Ho, kích ứng họng",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ",
            "Beta-blocker: đối kháng tác dụng olodaterol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Kết hợp LAMA (tiotropium) và LABA (olodaterol) giúp giãn phế quản tối ưu và kéo dài 24 giờ cho COPD.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
            "Nhịp tim, huyết áp ở bệnh nhân có bệnh tim mạch",
        ],
        "precautions": [
            "Không dùng để cắt cơn; cần SABA dự phòng.",
            "Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
        ],
        "pharmacokinetics": {
            "half_life": "Tiotropium: 5-6 ngày (rất dài); Olodaterol: 22 giờ",
            "onset": "Olodaterol: 5 phút; Tiotropium: 30 phút",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Tiotropium: 72%; Olodaterol: 60%",
            "clearance": "Tiotropium: thải trừ chủ yếu qua thận (dạng nguyên dạng), một phần qua gan; Olodaterol: chuyển hóa gan (UGT, O-methylation), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Anticholinergics khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu anticholinergic."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng olodaterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với tiotropium, olodaterol",
                "Glaucoma góc đóng",
                "Hen phế quản cấp - không dùng để cắt cơn"
            ],
            "tương_đối": [
                "Phì đại tuyến tiền liệt nặng - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Tiotropium và olodaterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Tiotropium và olodaterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng (olodaterol chuyển hóa qua gan)",
            "severe": "Thận trọng",
            "notes": "Olodaterol chuyển hóa qua gan (UGT, O-methylation). Tiotropium thải trừ chủ yếu qua thận. Suy gan có thể ảnh hưởng đến olodaterol. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng, bí tiểu nặng (do tiotropium)",
                "Nhịp tim nhanh, run cơ (do olodaterol)",
                "Tăng nhãn áp (do tiotropium nếu vào mắt)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của olodaterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa mắt nếu thuốc vào mắt (nguy cơ tăng nhãn áp)",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu bí tiểu: đặt thông tiểu nếu cần",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân COPD"
            ],
            "monitoring": "Nhịp tim, huyết áp, dấu hiệu anticholinergic, nhãn áp nếu thuốc vào mắt"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Đặt ống hít vào miệng. Thở ra hoàn toàn. Bắt đầu hít sâu và chậm, đồng thời ấn nút. Giữ hơi 10 giây. Thở ra từ từ. QUAN TRỌNG: Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
                "timing": "1 lần/ngày (sáng hoặc tối)",
                "notes": "QUAN TRỌNG: 1) Dùng đều đặn 1 lần/ngày, không dùng để cắt cơn, 2) Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp), 3) Cần SABA dự phòng cho cơn cấp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Spiolto Respimat, Stiolto Respimat (tiotropium/olodaterol)",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
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
         "black_box_warnings": "Không có",
},
    "Umeclidinium/Vilanterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (LAMA/LABA)",
        "vietnamese_name": "Umeclidinium/Vilanterol, Anoro Ellipta",
        "administration": ["Inhalation"],
        "indications": [
            "COPD (phòng ngừa triệu chứng và đợt cấp)",
        ],
        "contraindications": [
            "Dị ứng với umeclidinium, vilanterol",
            "Glaucoma góc đóng, phì đại tuyến tiền liệt nặng",
        ],
        "dosage": {
            "adult_copd": "62.5/25mcg: 1 hít x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày, không dùng cho hen đơn độc.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "LAMA thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."},
        "side_effects": [
            "Khô miệng, bí tiểu",
            "Tim đập nhanh, run cơ",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ",
            "Beta-blocker: đối kháng tác dụng vilanterol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "LAMA (umeclidinium) + LABA (vilanterol) cho giãn phế quản kéo dài 24 giờ, cải thiện triệu chứng COPD.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
        ],
        "precautions": [
            "Không dùng cho hen phế quản nếu không có ICS kèm.",
            "Tránh thuốc vào mắt.",
        ],
        "pharmacokinetics": {
            "half_life": "Umeclidinium: 11 giờ; Vilanterol: 11 giờ",
            "onset": "Vilanterol: 5 phút; Umeclidinium: 5-15 phút",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Umeclidinium: 89%; Vilanterol: 94%",
            "clearance": "Umeclidinium: chuyển hóa gan (CYP2D6), thải qua phân và thận; Vilanterol: chuyển hóa gan (CYP3A4), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Anticholinergics khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu anticholinergic."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng vilanterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                },
                {
                    "drug": "Strong CYP3A4 inhibitors (ketoconazole, ritonavir)",
                    "mechanism": "Ức chế CYP3A4, tăng chuyển hóa vilanterol",
                    "effect": "Tăng nồng độ vilanterol toàn thân (ít quan trọng về mặt lâm sàng do hấp thu tối thiểu)",
                    "management": "Thận trọng. Theo dõi tác dụng phụ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với umeclidinium, vilanterol",
                "Glaucoma góc đóng"
            ],
            "tương_đối": [
                "Phì đại tuyến tiền liệt nặng - thận trọng",
                "Bệnh tim mạch - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Umeclidinium và vilanterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Umeclidinium và vilanterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Umeclidinium và vilanterol chuyển hóa qua gan (CYP2D6, CYP3A4). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng, bí tiểu nặng (do umeclidinium)",
                "Nhịp tim nhanh, run cơ (do vilanterol)",
                "Tăng đường huyết (do vilanterol)",
                "Hạ kali máu (do vilanterol)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của vilanterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu bí tiểu: đặt thông tiểu nếu cần",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân COPD",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu anticholinergic"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Có thể cần bổ sung corticosteroid nếu có suy thượng thận do ICS."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Đặt ống hít Ellipta vào miệng. Thở ra hoàn toàn. Bắt đầu hít sâu và chậm, đồng thời kéo thanh trượt. Giữ hơi 10 giây. Thở ra từ từ.",
                "timing": "1 lần/ngày (sáng hoặc tối)",
                "notes": "QUAN TRỌNG: 1) Dùng đều đặn 1 lần/ngày, không dùng để cắt cơn, 2) Cần SABA dự phòng cho cơn cấp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Anoro Ellipta (umeclidinium/vilanterol)",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
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
         "black_box_warnings": "Không có",
},
    "Fluticasone/Vilanterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Fluticasone/Vilanterol, Breo Ellipta",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD có nhiều đợt cấp (ICS/LABA)",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với fluticasone, vilanterol hoặc bất kỳ thành phần nào",
                "Dùng cùng ritonavir (tăng mạnh nồng độ fluticasone)"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng để cắt cơn",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "dosage": {
            "adult_asthma": "100/25mcg hoặc 200/25mcg: 1 hít x 1 lần/ngày",
            "adult_copd": "100/25mcg: 1 hít x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày; không dùng để cắt cơn. Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Hấp thu toàn thân ít từ dạng hít. Không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Tim đập nhanh, run cơ (LABA - hiếm)",
            "Đau đầu",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Ritonavir: chống chỉ định (tăng mạnh nồng độ fluticasone)",
            "Ketoconazole/itraconazole: tăng nồng độ fluticasone",
            "Beta-blocker: đối kháng tác dụng vilanterol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "ICS (fluticasone) kháng viêm + LABA (vilanterol) giãn phế quản kéo dài 24 giờ. Cải thiện kiểm soát hen/COPD khi đơn trị ICS hoặc LABA không đủ. Ưu điểm: dùng 1 lần/ngày.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng LABA đơn độc cho hen.",
            "TRÁNH DÙNG với ritonavir.",
            "Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Fluticasone: 7.8 giờ; Vilanterol: 11 giờ",
            "onset": "Vilanterol: 5 phút; Fluticasone: vài giờ",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Fluticasone: 91%; Vilanterol: 94%",
            "clearance": "Fluticasone: chuyển hóa gan (CYP3A4), thải qua phân; Vilanterol: chuyển hóa gan (CYP3A4), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "TRÁNH DÙNG với ritonavir do tăng mạnh nồng độ fluticasone gây tác dụng phụ nghiêm trọng. Không dùng LABA đơn độc cho hen phế quản.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ritonavir",
                    "mechanism": "Ức chế CYP3A4, tăng đáng kể nồng độ fluticasone",
                    "effect": "Tăng nguy cơ ức chế trục HPA nghiêm trọng, hội chứng Cushing, suy thượng thận",
                    "management": "CHỐNG CHỈ ĐỊNH với ritonavir. Nếu cần dùng, xem xét thuốc thay thế (budesonide/formoterol)."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ fluticasone",
                    "effect": "Tăng nguy cơ tác dụng toàn thân, ức chế HPA",
                    "management": "Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều fluticasone."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng vilanterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với fluticasone, vilanterol hoặc bất kỳ thành phần nào",
                "Dùng cùng ritonavir - chống chỉ định tuyệt đối"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng để cắt cơn",
                "Dùng với ketoconazole, itraconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Fluticasone và vilanterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Fluticasone và vilanterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Fluticasone và vilanterol chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh, run cơ (do vilanterol)",
                "Tăng đường huyết (do vilanterol)",
                "Hạ kali máu (do vilanterol)",
                "Ức chế HPA (nếu hấp thu nhiều fluticasone)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của vilanterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân hen",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu",
                "Theo dõi dấu hiệu ức chế HPA nếu hấp thu nhiều fluticasone"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu ức chế HPA"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Có thể cần bổ sung corticosteroid nếu có suy thượng thận do ICS."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Đặt ống hít Ellipta vào miệng. Thở ra hoàn toàn. Bắt đầu hít sâu và chậm, đồng thời kéo thanh trượt. Giữ hơi 10 giây. Thở ra từ từ. Súc miệng sau khi dùng.",
                "timing": "1 lần/ngày (sáng hoặc tối)",
                "notes": "QUAN TRỌNG: 1) Súc miệng sau khi dùng để tránh nấm miệng, 2) Không dùng LABA đơn độc cho hen, 3) TRÁNH DÙNG với ritonavir, 4) Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Breo Ellipta (fluticasone/vilanterol)",
                "GINA Guidelines - Global Initiative for Asthma",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA approved, multiple RCTs"
        }
    },
    "Mometasone/Indacaterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Mometasone/Indacaterol, Atectura Breezhaler",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát, phòng ngừa)",
            "COPD có nhiều đợt cấp (ICS/LABA)",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với mometasone, indacaterol hoặc bất kỳ thành phần nào",
                "Dùng cùng ritonavir (tăng mạnh nồng độ mometasone)"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng để cắt cơn",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "dosage": {
            "adult_asthma": "160/150mcg: 1 hít x 1 lần/ngày",
            "adult_copd": "160/150mcg: 1 hít x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày; không dùng để cắt cơn. Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Hấp thu toàn thân ít từ dạng hít. Không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Tim đập nhanh, run cơ (LABA - hiếm)",
            "Đau đầu",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Ritonavir: chống chỉ định (tăng mạnh nồng độ mometasone)",
            "Ketoconazole/itraconazole: tăng nồng độ mometasone",
            "Beta-blocker: đối kháng tác dụng indacaterol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "ICS (mometasone) kháng viêm + LABA (indacaterol) giãn phế quản kéo dài 24 giờ. Cải thiện kiểm soát hen/COPD khi đơn trị ICS hoặc LABA không đủ. Ưu điểm: dùng 1 lần/ngày.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng LABA đơn độc cho hen.",
            "TRÁNH DÙNG với ritonavir.",
            "Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Mometasone: 5 giờ; Indacaterol: 40-56 giờ",
            "onset": "Indacaterol: 5 phút; Mometasone: vài giờ",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Mometasone: 98-99%; Indacaterol: 94-96%",
            "clearance": "Mometasone: chuyển hóa gan (CYP3A4), thải qua phân; Indacaterol: chuyển hóa gan (CYP3A4, UGT1A1), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "TRÁNH DÙNG với ritonavir do tăng mạnh nồng độ mometasone gây tác dụng phụ nghiêm trọng. Không dùng LABA đơn độc cho hen phế quản.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ritonavir",
                    "mechanism": "Ức chế CYP3A4, tăng đáng kể nồng độ mometasone",
                    "effect": "Tăng nguy cơ ức chế trục HPA nghiêm trọng, hội chứng Cushing, suy thượng thận",
                    "management": "CHỐNG CHỈ ĐỊNH với ritonavir. Nếu cần dùng, xem xét thuốc thay thế (budesonide/formoterol)."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ mometasone",
                    "effect": "Tăng nguy cơ tác dụng toàn thân, ức chế HPA",
                    "management": "Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều mometasone."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng indacaterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với mometasone, indacaterol hoặc bất kỳ thành phần nào",
                "Dùng cùng ritonavir - chống chỉ định tuyệt đối"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng để cắt cơn",
                "Dùng với ketoconazole, itraconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Mometasone và indacaterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Mometasone và indacaterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Mometasone và indacaterol chuyển hóa qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh, run cơ (do indacaterol)",
                "Tăng đường huyết (do indacaterol)",
                "Hạ kali máu (do indacaterol)",
                "Ức chế HPA (nếu hấp thu nhiều mometasone)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của indacaterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân hen",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu",
                "Theo dõi dấu hiệu ức chế HPA nếu hấp thu nhiều mometasone"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu ức chế HPA"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Có thể cần bổ sung corticosteroid nếu có suy thượng thận do ICS."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Đặt ống hít Breezhaler vào miệng. Thở ra hoàn toàn. Hít mạnh và sâu. Giữ hơi 10 giây. Thở ra từ từ. Súc miệng sau khi dùng.",
                "timing": "1 lần/ngày (sáng hoặc tối)",
                "notes": "QUAN TRỌNG: 1) Súc miệng sau khi dùng để tránh nấm miệng, 2) Không dùng LABA đơn độc cho hen, 3) TRÁNH DÙNG với ritonavir, 4) Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Atectura Breezhaler (mometasone/indacaterol)",
                "GINA Guidelines - Global Initiative for Asthma",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA approved, multiple RCTs"
        }
    },
    "Budesonide/Glycopyrronium/Formoterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LAMA/LABA)",
        "vietnamese_name": "Budesonide/Glycopyrronium/Formoterol, Trimbow",
        "administration": ["Inhalation"],
        "indications": [
            "COPD nặng, nhiều đợt cấp (triple therapy)",
            "Hen phế quản không kiểm soát với ICS/LABA",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với budesonide, glycopyrronium, formoterol hoặc bất kỳ thành phần nào",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt nặng gây bí tiểu"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng để cắt cơn",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "dosage": {
            "adult_copd": "160/50/9mcg: 2 hít x 2 lần/ngày",
            "adult_asthma": "160/50/9mcg: 2 hít x 2 lần/ngày (tùy mức độ)",
            "notes": "Dùng đều đặn 2 lần/ngày; không dùng để cắt cơn. Triple therapy cho COPD nặng.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "LAMA thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."},
        "side_effects": [
            "Nấm miệng, khàn tiếng (ICS)",
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA - hiếm)",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Ritonavir, ketoconazole, itraconazole: tăng nồng độ budesonide",
            "Beta-blocker: đối kháng tác dụng formoterol",
            "Anticholinergics khác: tăng tác dụng phụ anticholinergic",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Phối hợp 3 trong 1: ICS (budesonide) kháng viêm, LAMA (glycopyrronium) và LABA (formoterol) giãn phế quản kéo dài, tối ưu hóa kiểm soát COPD/hen nặng.",
        "monitoring": [
            "Triệu chứng hen/COPD, FEV1",
            "Nấm miệng, tác dụng phụ anticholinergic",
            "Nhịp tim, huyết áp",
        ],
        "precautions": [
            "Súc miệng sau khi dùng.",
            "Không dùng với ritonavir nếu có thể.",
            "Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
            "Triple therapy cho COPD nặng, nhiều đợt cấp.",
        ],
        "pharmacokinetics": {
            "half_life": "Budesonide: 2-3 giờ; Glycopyrronium: 12-15 giờ; Formoterol: 10 giờ",
            "onset": "Formoterol: 1-3 phút; Glycopyrronium: 5-15 phút; Budesonide: vài giờ",
            "duration": "Cả ba: 12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Budesonide: 88-90%; Glycopyrronium: <10%; Formoterol: 50-65%",
            "clearance": "Budesonide: chuyển hóa gan (CYP3A4), thải qua thận; Glycopyrronium: chuyển hóa gan (CYP2D6), thải qua phân và thận; Formoterol: chuyển hóa gan (CYP2D6, CYP2C19), thải qua thận và phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng với ritonavir do tăng mạnh nồng độ budesonide gây tác dụng phụ nghiêm trọng. Không dùng LABA đơn độc cho hen phế quản.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Ritonavir",
                    "mechanism": "Ức chế CYP3A4, tăng đáng kể nồng độ budesonide",
                    "effect": "Tăng nguy cơ ức chế trục HPA nghiêm trọng",
                    "management": "TRÁNH DÙNG với ritonavir. Nếu cần dùng, giảm liều budesonide đáng kể hoặc xem xét thuốc thay thế."
                }
            ],
            "moderate": [
                {
                    "drug": "Ketoconazole, Itraconazole, Posaconazole",
                    "mechanism": "Ức chế CYP3A4, tăng nồng độ budesonide",
                    "effect": "Tăng nguy cơ tác dụng toàn thân, ức chế HPA",
                    "management": "Thận trọng, theo dõi tác dụng toàn thân. Có thể cần giảm liều budesonide."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng formoterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                },
                {
                    "drug": "Anticholinergics khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu anticholinergic."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với budesonide, glycopyrronium, formoterol",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt nặng gây bí tiểu"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng để cắt cơn",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Budesonide, glycopyrronium và formoterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Budesonide, glycopyrronium và formoterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Budesonide, glycopyrronium và formoterol chuyển hóa qua gan (CYP3A4, CYP2D6, CYP2C19). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng, bí tiểu nặng (do glycopyrronium)",
                "Nhịp tim nhanh, run cơ (do formoterol)",
                "Tăng nhãn áp (do glycopyrronium nếu vào mắt)",
                "Ức chế HPA (nếu hấp thu nhiều budesonide)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của formoterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa mắt nếu thuốc vào mắt (nguy cơ tăng nhãn áp)",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu bí tiểu: đặt thông tiểu nếu cần",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân hen/COPD",
                "Theo dõi dấu hiệu ức chế HPA nếu hấp thu nhiều budesonide"
            ],
            "monitoring": "Nhịp tim, huyết áp, dấu hiệu anticholinergic, nhãn áp nếu thuốc vào mắt, dấu hiệu ức chế HPA"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Lắc kỹ trước khi dùng. Thở ra hoàn toàn. Đặt ống hít vào miệng, bắt đầu hít sâu và chậm, đồng thời ấn nút. Giữ hơi 10 giây. Thở ra từ từ. Súc miệng sau khi dùng. QUAN TRỌNG: Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
                "timing": "2 lần/ngày (sáng, tối)",
                "notes": "QUAN TRỌNG: 1) Súc miệng sau khi dùng để tránh nấm miệng, 2) Không dùng LABA đơn độc cho hen, 3) TRÁNH DÙNG với ritonavir, 4) Tránh để thuốc vào mắt, 5) Triple therapy cho COPD nặng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Trimbow (budesonide/glycopyrronium/formoterol)",
                "GINA Guidelines - Global Initiative for Asthma",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA approved, multiple RCTs"
        }
    },
    "Aclidinium/Formoterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (LAMA/LABA)",
        "vietnamese_name": "Aclidinium/Formoterol, Duaklir Genuair",
        "administration": ["Inhalation"],
        "indications": [
            "COPD (phòng ngừa triệu chứng và đợt cấp)",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với aclidinium, formoterol hoặc bất kỳ thành phần nào",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt nặng gây bí tiểu",
                "Hen phế quản cấp (không dùng để cắt cơn)"
            ],
            "tương_đối": [
                "Phì đại tuyến tiền liệt - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "dosage": {
            "adult_copd": "400/12mcg: 1 hít x 2 lần/ngày",
            "notes": "Dùng đều đặn 2 lần/ngày, không dùng để cắt cơn.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "LAMA thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."},
        "side_effects": [
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA - hiếm)",
            "Ho, kích ứng họng",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ anticholinergic",
            "Beta-blocker: đối kháng tác dụng formoterol",
            "Theophylline: tăng tác dụng phụ tim mạch",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "LAMA (aclidinium) + LABA (formoterol) cho giãn phế quản kéo dài, cải thiện triệu chứng COPD. Formoterol có tác dụng nhanh (1-3 phút) nên có thể dùng để cắt cơn nhẹ, nhưng vẫn nên dùng SABA cho cơn cấp.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
            "Nhịp tim, huyết áp ở bệnh nhân có bệnh tim mạch",
        ],
        "precautions": [
            "Không dùng để cắt cơn; cần SABA dự phòng.",
            "Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
            "Formoterol có tác dụng nhanh (1-3 phút) nhưng vẫn nên dùng SABA cho cơn cấp.",
        ],
        "pharmacokinetics": {
            "half_life": "Aclidinium: 5-8 giờ; Formoterol: 10 giờ",
            "onset": "Formoterol: 1-3 phút; Aclidinium: 5-15 phút",
            "duration": "Cả hai: 12 giờ (dùng 2 lần/ngày)",
            "protein_binding": "Aclidinium: <10%; Formoterol: 50-65%",
            "clearance": "Aclidinium: chuyển hóa gan (CYP2D6, CYP3A4), thải qua phân và thận; Formoterol: chuyển hóa gan (CYP2D6, CYP2C19), thải qua thận và phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng LABA đơn độc cho hen phế quản. Không dùng để cắt cơn cấp.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Anticholinergics khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu anticholinergic."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng formoterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Tác dụng cộng dồn trên tim mạch",
                    "effect": "Tăng tác dụng phụ tim mạch (nhịp tim nhanh, run cơ)",
                    "management": "Thận trọng. Theo dõi nhịp tim, dấu hiệu lâm sàng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với aclidinium, formoterol",
                "Glaucoma góc đóng",
                "Hen phế quản cấp - không dùng để cắt cơn"
            ],
            "tương_đối": [
                "Phì đại tuyến tiền liệt nặng - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Aclidinium và formoterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Aclidinium và formoterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Aclidinium và formoterol chuyển hóa qua gan (CYP2D6, CYP3A4, CYP2C19). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng, bí tiểu nặng (do aclidinium)",
                "Nhịp tim nhanh, run cơ (do formoterol)",
                "Tăng nhãn áp (do aclidinium nếu vào mắt)",
                "Tăng đường huyết (do formoterol)",
                "Hạ kali máu (do formoterol)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của formoterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa mắt nếu thuốc vào mắt (nguy cơ tăng nhãn áp)",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu bí tiểu: đặt thông tiểu nếu cần",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân COPD",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu anticholinergic, nhãn áp nếu thuốc vào mắt"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Đặt ống hít Genuair vào miệng. Thở ra hoàn toàn. Bắt đầu hít sâu và chậm, đồng thời ấn nút. Giữ hơi 10 giây. Thở ra từ từ. QUAN TRỌNG: Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
                "timing": "2 lần/ngày (sáng, tối)",
                "notes": "QUAN TRỌNG: 1) Dùng đều đặn 2 lần/ngày, không dùng để cắt cơn, 2) Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp), 3) Cần SABA dự phòng cho cơn cấp."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Duaklir Genuair (aclidinium/formoterol)",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA approved, multiple RCTs"
        }
    },
    "Glycopyrronium/Indacaterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (LAMA/LABA)",
        "vietnamese_name": "Glycopyrronium/Indacaterol, Ultibro Breezhaler",
        "administration": ["Inhalation"],
        "indications": [
            "COPD (phòng ngừa triệu chứng và đợt cấp)",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với glycopyrronium, indacaterol hoặc bất kỳ thành phần nào",
                "Glaucoma góc đóng",
                "Phì đại tuyến tiền liệt nặng gây bí tiểu",
                "Hen phế quản cấp (không dùng để cắt cơn)"
            ],
            "tương_đối": [
                "Phì đại tuyến tiền liệt - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "dosage": {
            "adult_copd": "50/110mcg: 1 hít x 1 lần/ngày",
            "notes": "Dùng đều đặn 1 lần/ngày, không dùng để cắt cơn. Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Thận trọng", "under_30": "Thận trọng", "dialysis": "Thận trọng", "notes": "LAMA thải trừ một phần qua thận. Suy thận có thể tăng nguy cơ tích lũy."},
        "side_effects": [
            "Khô miệng, bí tiểu (LAMA)",
            "Tim đập nhanh, run cơ (LABA - hiếm)",
            "Ho, kích ứng họng",
            "Nhiễm trùng đường hô hấp trên",
        ],
        "interactions": [
            "Anticholinergics khác: tăng tác dụng phụ anticholinergic",
            "Beta-blocker: đối kháng tác dụng indacaterol",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "LAMA (glycopyrronium) + LABA (indacaterol) cho giãn phế quản kéo dài 24 giờ, cải thiện triệu chứng COPD. Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        "monitoring": [
            "Triệu chứng COPD, FEV1",
            "Dấu hiệu bí tiểu, tăng nhãn áp",
            "Nhịp tim, huyết áp ở bệnh nhân có bệnh tim mạch",
        ],
        "precautions": [
            "Không dùng để cắt cơn; cần SABA dự phòng.",
            "Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
            "Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị.",
        ],
        "pharmacokinetics": {
            "half_life": "Glycopyrronium: 12-15 giờ; Indacaterol: 40-56 giờ",
            "onset": "Indacaterol: 5 phút; Glycopyrronium: 5-15 phút",
            "duration": "Cả hai: 24 giờ (dùng 1 lần/ngày)",
            "protein_binding": "Glycopyrronium: <10%; Indacaterol: 94-96%",
            "clearance": "Glycopyrronium: chuyển hóa gan (CYP2D6), thải qua phân và thận; Indacaterol: chuyển hóa gan (CYP3A4, UGT1A1), thải qua phân và thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng LABA đơn độc cho hen phế quản. Không dùng để cắt cơn cấp.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Anticholinergics khác",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng tác dụng phụ anticholinergic (khô miệng, bí tiểu)",
                    "management": "Thận trọng. Theo dõi dấu hiệu anticholinergic."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng indacaterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với glycopyrronium, indacaterol",
                "Glaucoma góc đóng",
                "Hen phế quản cấp - không dùng để cắt cơn"
            ],
            "tương_đối": [
                "Phì đại tuyến tiền liệt nặng - thận trọng",
                "Bệnh tim mạch - thận trọng",
                "Suy thận nặng - thận trọng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Glycopyrronium và indacaterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Glycopyrronium và indacaterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Glycopyrronium và indacaterol chuyển hóa qua gan (CYP2D6, CYP3A4, UGT1A1). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Khô miệng, bí tiểu nặng (do glycopyrronium)",
                "Nhịp tim nhanh, run cơ (do indacaterol)",
                "Tăng nhãn áp (do glycopyrronium nếu vào mắt)",
                "Tăng đường huyết (do indacaterol)",
                "Hạ kali máu (do indacaterol)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của indacaterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Rửa mắt nếu thuốc vào mắt (nguy cơ tăng nhãn áp)",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu bí tiểu: đặt thông tiểu nếu cần",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân COPD",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu anticholinergic, nhãn áp nếu thuốc vào mắt"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Physostigmine có thể đối kháng tác dụng anticholinergic nhưng thận trọng."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Đặt ống hít Breezhaler vào miệng. Thở ra hoàn toàn. Hít mạnh và sâu. Giữ hơi 10 giây. Thở ra từ từ. QUAN TRỌNG: Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp).",
                "timing": "1 lần/ngày (sáng hoặc tối)",
                "notes": "QUAN TRỌNG: 1) Dùng đều đặn 1 lần/ngày, không dùng để cắt cơn, 2) Tránh để thuốc vào mắt (nguy cơ tăng nhãn áp), 3) Cần SABA dự phòng cho cơn cấp, 4) Ưu điểm: dùng 1 lần/ngày tăng tuân thủ điều trị."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ultibro Breezhaler (glycopyrronium/indacaterol)",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA approved, multiple RCTs"
        }
    },
    "Beclomethasone/Formoterol inhaler": {
        "group": "Respiratory - Fixed-dose Combination (ICS/LABA)",
        "vietnamese_name": "Beclomethasone/Formoterol, Fostair",
        "administration": ["Inhalation"],
        "indications": [
            "Hen phế quản (kiểm soát + cắt cơn theo GINA: SMART/MART)",
            "COPD có nhiều đợt cấp (ICS/LABA)",
        ],
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với beclomethasone, formoterol hoặc bất kỳ thành phần nào",
                "Hen phế quản cấp (không dùng đơn độc để cắt cơn nếu không theo phác đồ SMART/MART)"
            ],
            "tương_đối": [
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "dosage": {
            "adult_asthma_maintenance": "100/6mcg: 2 hít x 2 lần/ngày (sáng, tối)",
            "adult_asthma_smart": "100/6mcg: 1-2 hít x 1-2 lần/ngày duy trì + 1 hít khi cần, tối đa 8 hít/ngày",
            "adult_copd": "100/6mcg: 2 hít x 2 lần/ngày",
            "notes": "Dùng đều đặn hàng ngày. Trong phác đồ SMART/MART, có thể dùng thêm để cắt cơn nhẹ thay SABA.",
        },
        "renal_adjustment": {"normal": "Không đổi", "30_60": "Không đổi", "under_30": "Không đổi", "dialysis": "Không đổi", "notes": "Hấp thu toàn thân ít từ dạng hít. Không cần điều chỉnh liều ở suy thận."},
        "side_effects": [
            "Nấm miệng (do ICS)",
            "Khàn tiếng",
            "Ho, kích ứng họng",
            "Tim đập nhanh, run cơ (do LABA)",
            "Đau đầu",
        ],
        "interactions": [
            "Ritonavir, ketoconazole, itraconazole: tăng nồng độ beclomethasone",
            "Beta-blocker: đối kháng tác dụng formoterol",
            "Theophylline: tăng tác dụng phụ tim mạch",
        ],
        "pregnancy": "C",
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "organ_toxicity": {},
            "icu_critical_care_only": False,
            "look_alike_sound_alike": []
        },
        "guideline_tags": [
            "GINA Guidelines (Global Initiative for Asthma)",
            "GOLD Guidelines (Global Initiative for Chronic Obstructive Lung Disease)"
        ],
        "mechanism_of_action": "Phối hợp ICS (beclomethasone) kháng viêm tại chỗ và LABA (formoterol) giãn phế quản kéo dài, khởi phát nhanh. Dùng vừa để kiểm soát vừa để cắt cơn (SMART/MART).",
        "monitoring": [
            "Triệu chứng hen/COPD, số lần cơn cấp, nhu cầu SABA",
            "Nấm miệng, khàn tiếng",
            "Nhịp tim, run cơ",
        ],
        "precautions": [
            "Súc miệng sau khi dùng để tránh nấm miệng.",
            "Không dùng LABA đơn độc cho hen – luôn đi kèm ICS.",
            "Trong phác đồ SMART/MART: cần hướng dẫn rõ cho bệnh nhân về tối đa số hít/ngày.",
        ],
        "pharmacokinetics": {
            "half_life": "Beclomethasone: 15 giờ (trong phổi), 2-3 giờ (toàn thân); Formoterol: 10 giờ",
            "onset": "Formoterol: 1-3 phút (khởi phát nhanh); Beclomethasone: vài giờ",
            "duration": "Formoterol: 12 giờ; Beclomethasone: tác dụng tại chỗ kéo dài",
            "protein_binding": "Beclomethasone: 87%; Formoterol: 50-65%",
            "clearance": "Beclomethasone: chuyển hóa gan (CYP3A4) thành chất không hoạt tính, thải qua thận; Formoterol: chuyển hóa gan (CYP2D6, CYP2C19), thải qua thận và phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng trực tiếp, tránh ẩm. Không bảo quản trong tủ lạnh. Để xa tầm tay trẻ em. Kiểm tra hạn sử dụng trước khi dùng.",
        "black_box_warnings": "Không dùng LABA đơn độc cho hen phế quản - luôn phải kết hợp với ICS. Tăng nguy cơ tử vong do hen khi dùng LABA không kèm ICS.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Ritonavir, ketoconazole, itraconazole",
                    "mechanism": "Ức chế CYP3A4, tăng chuyển hóa beclomethasone",
                    "effect": "Tăng nồng độ beclomethasone toàn thân, tăng nguy cơ ức chế HPA",
                    "management": "Thận trọng. Theo dõi dấu hiệu ức chế HPA. Có thể cần giảm liều."
                },
                {
                    "drug": "Beta-blockers",
                    "mechanism": "Đối kháng tác dụng formoterol",
                    "effect": "Giảm hiệu quả giãn phế quản",
                    "management": "Thận trọng. Tránh beta-blockers không chọn lọc. Có thể dùng beta-blockers chọn lọc tim mạch khi cần."
                },
                {
                    "drug": "Theophylline",
                    "mechanism": "Tác dụng cộng dồn trên tim mạch",
                    "effect": "Tăng tác dụng phụ tim mạch (nhịp tim nhanh, run cơ)",
                    "management": "Thận trọng. Theo dõi nhịp tim, dấu hiệu lâm sàng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng với beclomethasone, formoterol hoặc bất kỳ thành phần nào"
            ],
            "tương_đối": [
                "Hen phế quản cấp - không dùng đơn độc để cắt cơn nếu không theo phác đồ SMART/MART",
                "Dùng với ritonavir, ketoconazole - thận trọng (tăng nguy cơ ức chế HPA)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Beclomethasone và formoterol có thể ảnh hưởng đến thai nhi. Hấp thu toàn thân từ dạng hít: tối thiểu, giảm nguy cơ.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Beclomethasone và formoterol bài tiết vào sữa mẹ ở nồng độ thấp. Hấp thu toàn thân từ dạng hít: tối thiểu.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng",
            "notes": "Beclomethasone và formoterol chuyển hóa qua gan (CYP3A4, CYP2D6, CYP2C19). Suy gan có thể làm giảm chuyển hóa. Tuy nhiên, hấp thu toàn thân từ dạng hít: tối thiểu, nên ít ảnh hưởng."
        },
        "overdose_management": {
            "symptoms": [
                "Nhịp tim nhanh, run cơ (do formoterol)",
                "Tăng đường huyết (do formoterol)",
                "Hạ kali máu (do formoterol)",
                "Ức chế HPA (nếu hấp thu nhiều beclomethasone)"
            ],
            "antidote": "Không có antidote đặc hiệu. Beta-blockers (selective) có thể đối kháng một phần tác dụng của formoterol.",
            "treatment": [
                "Ngừng ngay thuốc",
                "Theo dõi nhịp tim, huyết áp",
                "Nếu nhịp tim nhanh nặng: beta-blockers (selective) nếu cần, nhưng thận trọng ở bệnh nhân hen",
                "Nếu hạ kali máu: bổ sung kali",
                "Theo dõi đường huyết, kali máu",
                "Theo dõi dấu hiệu ức chế HPA nếu hấp thu nhiều beclomethasone"
            ],
            "monitoring": "Nhịp tim, huyết áp, đường huyết, kali máu, dấu hiệu ức chế HPA"
        },
        "reversal_agents": {
            "available": False,
            "agents": [],
            "notes": "Không có antidote đặc hiệu. Điều trị chủ yếu là hỗ trợ và điều trị triệu chứng. Có thể cần bổ sung corticosteroid nếu có suy thượng thận do ICS."
        },
        "administration_instructions": {
            "inhalation": {
                "technique": "Lắc kỹ trước khi dùng. Thở ra hoàn toàn. Đặt ống hít vào miệng, bắt đầu hít sâu và chậm, đồng thời ấn nút. Giữ hơi 10 giây. Thở ra từ từ. Súc miệng sau khi dùng.",
                "timing": "2 lần/ngày (sáng, tối) hoặc theo phác đồ SMART/MART",
                "notes": "QUAN TRỌNG: 1) Súc miệng sau khi dùng để tránh nấm miệng, 2) Không dùng LABA đơn độc cho hen, 3) Trong phác đồ SMART/MART: tối đa 8 hít/ngày."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Fostair (beclomethasone/formoterol)",
                "GINA Guidelines - Global Initiative for Asthma",
                "GOLD Guidelines - Global Initiative for Chronic Obstructive Lung Disease"
            ],
            "last_updated": "2025-02-18",
            "evidence_level": "A - FDA approved, multiple RCTs"
        }
    }
}

__all__ = ["COMBINATION_INHALERS_DRUGS"]


