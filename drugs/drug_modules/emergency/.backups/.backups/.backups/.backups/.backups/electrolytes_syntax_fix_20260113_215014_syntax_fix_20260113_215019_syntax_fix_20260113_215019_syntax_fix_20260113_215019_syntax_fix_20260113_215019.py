"""Emergency Medications - Electrolytes
Calcium chloride, Magnesium sulfate for emergency use"""

ELECTROLYTES_DRUGS = {
    "Calcium chloride": {
        "group": "Emergency - Electrolyte",
        "vietnamese_name": "Calcium chloride, CaCl2",
        "administration": ["IV"],
        "indications": [
            "Hạ calci máu cấp tính có triệu chứng",
            "Ngộ độc calcium channel blocker",
            "Ngộ độc magnesium sulfate",
            "Tăng kali máu nặng (bảo vệ tim)",
            "Ngộ độc hydrofluoric acid"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Suy thận nặng với tăng calci máu",
            "Sỏi thận calci",
            "Dùng với digoxin (tăng nguy cơ loạn nhịp)"
        ],
        "dosage": {
            "adult_hypocalcemia": "1g (10ml 10%) IV chậm trong 10-20 phút, có thể lặp lại",
            "adult_hyperkalemia": "1g (10ml 10%) IV chậm trong 2-5 phút để bảo vệ tim",
            "adult_ccb_overdose": "1-3g IV chậm, có thể lặp lại",
            "pediatric_hypocalcemia": "20mg/kg (0.2ml/kg 10%) IV chậm",
            "pediatric_hyperkalemia": "20mg/kg (0.2ml/kg 10%) IV chậm trong 2-5 phút",
            "notes": "1g CaCl2 = 13.6 mEq Ca2+. Truyền CHẬM, theo dõi ECG. Không trộn với bicarbonate hoặc phosphate."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều, theo dõi calci máu"
        },
        "side_effects": [
            "Nóng bỏng tại chỗ tiêm (phải truyền vào tĩnh mạch lớn)",
            "Hoại tử nếu tiêm ngoài mạch",
            "Tăng calci máu (quá liều)",
            "Loạn nhịp tim (đặc biệt với digoxin)",
            "Buồn nôn, nôn",
            "Sỏi thận (dùng kéo dài)"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ loạn nhịp tim nghiêm trọng",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Bicarbonate, Phosphate: tạo kết tủa - không trộn",
            "Ceftriaxone: tạo kết tủa (đặc biệt ở trẻ sơ sinh)"
        ],
        "pregnancy": "C - An toàn trong cấp cứu",
        "mechanism_of_action": "Calcium chloride cung cấp calcium ion (Ca2+) trực tiếp vào máu. Ca2+ tham gia vào nhiều chức năng sinh học: đông máu (cần thiết cho cascade đông máu), co cơ (bao gồm cơ tim và cơ trơn), dẫn truyền thần kinh, và giải phóng hormone. Trong hạ calci máu: bổ sung Ca2+ thiếu hụt. Trong tăng kali máu: Ca2+ ổn định màng tế bào tim, giảm nguy cơ loạn nhịp tim do tăng kali máu. Trong ngộ độc calcium channel blocker: Ca2+ đối kháng tác dụng chẹn kênh calci, có thể đảo ngược tác dụng. Calcium chloride có hàm lượng Ca2+ cao hơn calcium gluconate (1g CaCl2 = 13.6 mEq vs 1g Ca gluconate = 4.65 mEq).",
        "monitoring": [
            "ECG liên tục (theo dõi loạn nhịp tim, đặc biệt với digoxin)",
            "Nồng độ calcium trong máu (ionized calcium) - theo dõi tăng calci máu",
            "Dấu hiệu tại chỗ tiêm (nóng bỏng, hoại tử nếu tiêm ngoài mạch)",
            "Nhịp tim, huyết áp",
            "Dấu hiệu tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ"
        ],
        "precautions": [
            "PHẢI truyền vào tĩnh mạch lớn (tránh tĩnh mạch ngoại vi - gây nóng bỏng, hoại tử)",
            "Truyền CHẬM (10-20 phút cho 1g) - không truyền nhanh (tăng nguy cơ loạn nhịp tim)",
            "KHÔNG trộn với bicarbonate hoặc phosphate (tạo kết tủa)",
            "KHÔNG trộn với ceftriaxone (tạo kết tủa, đặc biệt nguy hiểm ở trẻ sơ sinh)",
            "Theo dõi ECG liên tục (nguy cơ loạn nhịp tim, đặc biệt với digoxin)",
            "Thận trọng với digoxin (tăng nguy cơ loạn nhịp tim nghiêm trọng)",
            "Theo dõi nồng độ calcium trong máu (tránh tăng calci máu)",
            "Dùng ngắn hạn (không dùng kéo dài - tăng nguy cơ sỏi thận)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (calcium là ion, không có half-life như thuốc)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "2-3 giờ (tác dụng lâm sàng)",
            "protein_binding": "Khoảng 40-50% gắn với albumin",
            "clearance": "Thận: bài tiết qua nước tiểu. Xương: lưu trữ dài hạn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Kiểm tra hạn sử dụng.",
        "black_box_warnings": "KHÔNG trộn với ceftriaxone - có thể tạo kết tủa tử vong, đặc biệt ở trẻ sơ sinh. Truyền CHẬM - truyền nhanh có thể gây loạn nhịp tim, đặc biệt với digoxin.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Calcium tăng tác dụng của digoxin trên tim, tăng nguy cơ loạn nhịp tim nghiêm trọng.",
                    "effect": "Tăng nguy cơ loạn nhịp tim nghiêm trọng, có thể tử vong",
                    "management": "TRÁNH DÙNG nếu có thể. Nếu bắt buộc, theo dõi ECG liên tục, theo dõi nồng độ digoxin. Dùng liều thấp nhất có thể."
                },
                {
                    "drug": "Ceftriaxone",
                    "mechanism": "Calcium chloride tạo phức hợp không hòa tan với ceftriaxone, gây kết tủa.",
                    "effect": "Kết tủa trong phổi, thận, có thể tử vong (đặc biệt ở trẻ sơ sinh)",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không trộn hoặc truyền cùng. Cách ít nhất 48 giờ giữa ceftriaxone và calcium chloride."
                }
            ],
            "moderate": [
                {
                    "drug": "Thiazide diuretics",
                    "mechanism": "Thiazide giảm bài tiết calcium, kết hợp với bổ sung calcium, dẫn đến tăng calci máu.",
                    "effect": "Tăng nguy cơ tăng calci máu, sỏi thận",
                    "management": "Theo dõi nồng độ calcium trong máu chặt chẽ. Có thể cần giảm liều calcium."
                },
                {
                    "drug": "Bicarbonate, Phosphate",
                    "mechanism": "Tạo phức hợp không hòa tan, gây kết tủa.",
                    "effect": "Kết tủa, tắc nghẽn mạch máu",
                    "management": "KHÔNG trộn. Truyền riêng biệt, cách thời gian."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng calci máu (hypercalcemia)",
                "Dùng với digoxin (tăng nguy cơ loạn nhịp tim nghiêm trọng) - tránh nếu có thể",
                "Trộn với ceftriaxone (kết tủa tử vong)"
            ],
            "tương_đối": [
                "Suy thận nặng - tăng nguy cơ tăng calci máu",
                "Sỏi thận calci - tăng nguy cơ tái phát",
                "Bệnh sarcoidosis - tăng nhạy cảm với calcium"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Calcium chloride có thể được dùng trong cấp cứu khi cần thiết. Hạ calci máu trong thai kỳ có thể nguy hiểm cho cả mẹ và thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Calcium chloride bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú với liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Calcium không chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần",
                "Loạn nhịp tim (đặc biệt với digoxin)",
                "Sỏi thận",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và giảm calci máu.",
            "treatment": [
                "Ngừng calcium chloride ngay lập tức",
                "Truyền dịch muối đẳng trương (0.9% NaCl) để tăng bài tiết calcium",
                "Furosemide (lợi tiểu) để tăng bài tiết calcium (sau khi đã bù dịch)",
                "Calcitonin nếu tăng calci máu nặng",
                "Bisphosphonates (pamidronate, zoledronate) nếu tăng calci máu nặng",
                "Theo dõi ECG liên tục (loạn nhịp tim)",
                "Hemodialysis nếu tăng calci máu rất nặng"
            ],
            "monitoring": "ECG, nồng độ calcium trong máu, creatinine, dấu hiệu lâm sàng."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ 10% (10ml = 1g). Không cần pha.",
                "infusion_rate": "Truyền CHẬM trong 10-20 phút cho 1g. Không truyền nhanh hơn.",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [
                    "Ceftriaxone - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (kết tủa tử vong)",
                    "Bicarbonate - tạo kết tủa",
                    "Phosphate - tạo kết tủa"
                ],
                "notes": "PHẢI truyền vào tĩnh mạch lớn (tránh tĩnh mạch ngoại vi). Truyền CHẬM (10-20 phút). Theo dõi ECG liên tục. KHÔNG trộn với ceftriaxone, bicarbonate, hoặc phosphate."
            }
        },
        "references": {
            "primary_sources": [
                "ACLS Guidelines - Hyperkalemia Management",
                "UpToDate - Calcium chloride drug information",
                "FDA Drug Label - Calcium chloride",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên ACLS guidelines và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Calcium Levels"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - Hyperkalemia Management",
            "FDA Drug Label - Calcium chloride",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
    
    "Calcium chloride": {
        "group": "Emergency - Electrolyte",
        "vietnamese_name": "Calcium chloride, CaCl2",
        "administration": ["IV"],
        "indications": [
            "Hạ calci máu cấp tính có triệu chứng",
            "Tăng kali máu nặng (bảo vệ tim)",
            "Ngộ độc calcium channel blocker",
            "Ngộ độc magnesium sulfate",
            "Ngộ độc hydrofluoric acid"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Suy thận nặng với tăng calci máu",
            "Sỏi thận calci",
            "Digitalis toxicity (tăng nguy cơ rối loạn nhịp)"
        ],
        "dosage": {
            "adult_hypocalcemia": "1g (10ml 10% solution) IV chậm trong 5-10 phút, có thể lặp lại",
            "adult_hyperkalemia": "1g IV chậm trong 5-10 phút",
            "adult_max": "3g trong 24 giờ",
            "notes": "Chứa nhiều calci hơn calcium gluconate (3x). Chỉ dùng IV, không dùng IM/SC (gây hoại tử)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng",
            "under_30": "Thận trọng (tăng nguy cơ tăng calci máu)"
        },
        "side_effects": [
            "Kích ứng mạch máu (phổ biến, có thể gây viêm tĩnh mạch)",
            "Hoại tử mô (nếu tiêm ngoài mạch)",
            "Tăng calci máu (nếu dùng quá liều)",
            "Rối loạn nhịp tim (nếu dùng với digitalis)",
            "Hạ huyết áp (hiếm)"
        ],
        "interactions": [
            "Digitalis: tăng nguy cơ rối loạn nhịp tim",
            "Sodium bicarbonate: kết tủa (CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI)",
            "Phosphate: kết tủa"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Calcium chloride cung cấp calci ion hóa (Ca2+). Calci cần thiết cho: (1) Co bóp cơ tim (tăng lực co bóp), (2) Dẫn truyền thần kinh, (3) Đông máu, (4) Chức năng cơ. Trong hạ calci máu: bổ sung calci. Trong tăng kali máu: bảo vệ tim khỏi tác dụng độc của kali (ổn định màng tế bào). Trong ngộ độc calcium channel blocker: đối kháng tác dụng. Đặc điểm: chứa nhiều calci hơn calcium gluconate (3x), chỉ dùng IV, kích ứng mạch máu mạnh hơn calcium gluconate.",
        "monitoring": [
            "Calci máu (ionized calcium) - quan trọng",
            "Kali máu (nếu dùng cho tăng kali máu)",
            "ECG (rối loạn nhịp tim, đặc biệt nếu dùng với digitalis)",
            "Dấu hiệu kích ứng mạch máu (đỏ, đau tại chỗ tiêm)",
            "Dấu hiệu tăng calci máu: mệt mỏi, buồn nôn, táo bón"
        ],
        "precautions": [
            "Kích ứng mạch máu - phổ biến, có thể gây viêm tĩnh mạch",
            "Chỉ dùng IV, không dùng IM/SC (gây hoại tử mô)",
            "Truyền CHẬM (5-10 phút) để giảm kích ứng",
            "Thận trọng với digitalis (tăng nguy cơ rối loạn nhịp)",
            "KHÔNG trộn với sodium bicarbonate (kết tủa tử vong)",
            "Chứa nhiều calci hơn calcium gluconate (3x)",
            "Theo dõi calci máu chặt chẽ"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (electrolyte)",
            "onset": "Ngay lập tức sau khi tiêm IV",
            "duration": "Phụ thuộc liều và tình trạng bệnh nhân",
            "protein_binding": "50% (ionized calcium)",
            "clearance": "Thận (thải trừ qua nước tiểu), xương (lắng đọng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "KHÔNG trộn với sodium bicarbonate - kết tủa tử vong. Chỉ dùng IV, không dùng IM/SC - gây hoại tử mô.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sodium bicarbonate",
                    "mechanism": "Kết tủa calcium carbonate",
                    "effect": "Kết tủa tử vong, tắc mạch",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không trộn hoặc truyền cùng."
                },
                {
                    "drug": "Digitalis (digoxin, digitoxin)",
                    "mechanism": "Calci tăng tác dụng của digitalis trên tim",
                    "effect": "Tăng nguy cơ rối loạn nhịp tim nghiêm trọng",
                    "management": "Thận trọng. Theo dõi ECG sát. Tránh dùng cùng nếu có thể."
                }
            ],
            "moderate": [
                {
                    "drug": "Phosphate",
                    "mechanism": "Kết tủa calcium phosphate",
                    "effect": "Kết tủa, giảm hiệu quả cả hai",
                    "management": "Tránh trộn hoặc truyền cùng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng calci máu",
                "Suy thận nặng với tăng calci máu",
                "Sỏi thận calci",
                "Digitalis toxicity",
                "Dùng với sodium bicarbonate (kết tủa tử vong)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - tăng nguy cơ tăng calci máu",
                "Dùng với digitalis - tăng nguy cơ rối loạn nhịp"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Calci cần thiết cho thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Calci bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Calci không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu: mệt mỏi, buồn nôn, táo bón, nhịp tim chậm",
                "Rối loạn nhịp tim",
                "Kích ứng mạch máu nặng",
                "Hoại tử mô (nếu tiêm ngoài mạch)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị tăng calci máu.",
            "treatment": [
                "Ngừng ngay calcium chloride",
                "Truyền dịch muối đẳng trương",
                "Furosemide để tăng bài tiết calci",
                "Calcitonin nếu tăng calci máu nặng",
                "Theo dõi calci máu, ECG liên tục"
            ],
            "monitoring": "Calci máu (ionized calcium), ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Dùng trực tiếp dung dịch 10% (1g/10ml).",
                "infusion_rate": "Truyền CHẬM trong 5-10 phút. Không truyền nhanh hơn.",
                "compatibility": ["D5W", "Normal saline (0.9% NaCl)"],
                "incompatibility": [
                    "Sodium bicarbonate - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (kết tủa tử vong)",
                    "Phosphate - kết tủa",
                    "Catecholamines - bất hoạt"
                ],
                "notes": "QUAN TRỌNG: 1) Chỉ dùng IV, không dùng IM/SC (gây hoại tử mô), 2) Truyền CHẬM (5-10 phút), 3) KHÔNG trộn với sodium bicarbonate (kết tủa tử vong), 4) Chứa nhiều calci hơn calcium gluconate (3x)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Calcium Chloride Injection",
                "ACLS Guidelines 2020 - American Heart Association",
                "UpToDate - Calcium: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên ACLS guidelines và dữ liệu lâm sàng"
        }
    },
    
    "Calcium gluconate": {
        "group": "Emergency - Electrolyte",
        "vietnamese_name": "Calcium gluconate, Ca gluconate",
        "administration": ["IV"],
        "indications": [
            "Hạ calci máu cấp tính có triệu chứng",
            "Tăng kali máu nặng (bảo vệ tim)",
            "Ngộ độc calcium channel blocker",
            "Ngộ độc magnesium sulfate",
            "Ngộ độc hydrofluoric acid"
        ],
        "contraindications": [
            "Tăng calci máu",
            "Suy thận nặng với tăng calci máu",
            "Sỏi thận calci",
            "Dùng với digoxin (tăng nguy cơ loạn nhịp)"
        ],
        "dosage": {
            "adult_hypocalcemia": "1-3g (10-30ml 10%) IV chậm trong 10-20 phút, có thể lặp lại",
            "adult_hyperkalemia": "1-3g (10-30ml 10%) IV chậm trong 2-5 phút để bảo vệ tim",
            "adult_ccb_overdose": "1-3g IV chậm, có thể lặp lại",
            "pediatric_hypocalcemia": "30-100mg/kg (0.3-1ml/kg 10%) IV chậm",
            "pediatric_hyperkalemia": "30-100mg/kg (0.3-1ml/kg 10%) IV chậm trong 2-5 phút",
            "notes": "1g Ca gluconate = 4.65 mEq Ca2+ (ít hơn CaCl2: 13.6 mEq). Có thể truyền vào tĩnh mạch ngoại vi (ít gây nóng bỏng hơn CaCl2). Truyền CHẬM, theo dõi ECG. Không trộn với bicarbonate hoặc phosphate."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều, theo dõi calci máu"
        },
        "side_effects": [
            "Nóng bỏng tại chỗ tiêm (ít hơn CaCl2, có thể truyền vào tĩnh mạch ngoại vi)",
            "Hoại tử nếu tiêm ngoài mạch",
            "Tăng calci máu (quá liều)",
            "Loạn nhịp tim (đặc biệt với digoxin)",
            "Buồn nôn, nôn",
            "Sỏi thận (dùng kéo dài)"
        ],
        "interactions": [
            "Digoxin: tăng nguy cơ loạn nhịp tim nghiêm trọng",
            "Thiazide diuretics: tăng nguy cơ tăng calci máu",
            "Bicarbonate, Phosphate: tạo kết tủa - không trộn",
            "Ceftriaxone: tạo kết tủa (đặc biệt ở trẻ sơ sinh)"
        ],
        ',
        "pregnancy": "C - An toàn trong cấp cứu",
        ',
        "mechanism_of_action": "Calcium gluconate cung cấp calcium ion (Ca2+) trực tiếp vào máu. Ca2+ tham gia vào nhiều chức năng sinh học: đông máu (cần thiết cho cascade đông máu), co cơ (bao gồm cơ tim và cơ trơn), dẫn truyền thần kinh, và giải phóng hormone. Trong hạ calci máu: bổ sung Ca2+ thiếu hụt. Trong tăng kali máu: Ca2+ ổn định màng tế bào tim, giảm nguy cơ loạn nhịp tim do tăng kali máu. Trong ngộ độc calcium channel blocker: Ca2+ đối kháng tác dụng chẹn kênh calci, có thể đảo ngược tác dụng. Calcium gluconate có hàm lượng Ca2+ thấp hơn calcium chloride (1g Ca gluconate = 4.65 mEq vs 1g CaCl2 = 13.6 mEq), nhưng ít gây nóng bỏng tại chỗ tiêm hơn, có thể truyền vào tĩnh mạch ngoại vi.",
        "monitoring": [
            "ECG liên tục (theo dõi loạn nhịp tim, đặc biệt với digoxin)",
            "Nồng độ calcium trong máu (ionized calcium) - theo dõi tăng calci máu",
            "Dấu hiệu tại chỗ tiêm (nóng bỏng, hoại tử nếu tiêm ngoài mạch)",
            "Nhịp tim, huyết áp",
            "Dấu hiệu tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ"
        ],
        "precautions": [
            "Có thể truyền vào tĩnh mạch ngoại vi (ít gây nóng bỏng hơn CaCl2), nhưng vẫn ưu tiên tĩnh mạch lớn",
            "Truyền CHẬM (10-20 phút cho 1-3g) - không truyền nhanh (tăng nguy cơ loạn nhịp tim)",
            "KHÔNG trộn với bicarbonate hoặc phosphate (tạo kết tủa)",
            "KHÔNG trộn với ceftriaxone (tạo kết tủa, đặc biệt nguy hiểm ở trẻ sơ sinh)",
            "Theo dõi ECG liên tục (nguy cơ loạn nhịp tim, đặc biệt với digoxin)",
            "Thận trọng với digoxin (tăng nguy cơ loạn nhịp tim nghiêm trọng)",
            "Theo dõi nồng độ calcium trong máu (tránh tăng calci máu)",
            "Dùng ngắn hạn (không dùng kéo dài - tăng nguy cơ sỏi thận)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (calcium là ion, không có half-life như thuốc)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "2-3 giờ (tác dụng lâm sàng)",
            "protein_binding": "Khoảng 40-50% gắn với albumin",
            "clearance": "Thận: bài tiết qua nước tiểu. Xương: lưu trữ dài hạn."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Kiểm tra hạn sử dụng.",
        "black_box_warnings": "KHÔNG trộn với ceftriaxone - có thể tạo kết tủa tử vong, đặc biệt ở trẻ sơ sinh. Truyền CHẬM - truyền nhanh có thể gây loạn nhịp tim, đặc biệt với digoxin.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Calcium tăng tác dụng của digoxin trên tim, tăng nguy cơ loạn nhịp tim nghiêm trọng.",
                    "effect": "Tăng nguy cơ loạn nhịp tim nghiêm trọng, có thể tử vong",
                    "management": "TRÁNH DÙNG nếu có thể. Nếu bắt buộc, theo dõi ECG liên tục, theo dõi nồng độ digoxin. Dùng liều thấp nhất có thể."
                },
                {
                    "drug": "Ceftriaxone",
                    "mechanism": "Calcium gluconate tạo phức hợp không hòa tan với ceftriaxone, gây kết tủa.",
                    "effect": "Kết tủa trong phổi, thận, có thể tử vong (đặc biệt ở trẻ sơ sinh)",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không trộn hoặc truyền cùng. Cách ít nhất 48 giờ giữa ceftriaxone và calcium gluconate."
                }
            ],
            "moderate": [
                {
                    "drug": "Thiazide diuretics",
                    "mechanism": "Thiazide giảm bài tiết calcium, kết hợp với bổ sung calcium, dẫn đến tăng calci máu.",
                    "effect": "Tăng nguy cơ tăng calci máu, sỏi thận",
                    "management": "Theo dõi nồng độ calcium trong máu chặt chẽ. Có thể cần giảm liều calcium."
                },
                {
                    "drug": "Bicarbonate, Phosphate",
                    "mechanism": "Tạo phức hợp không hòa tan, gây kết tủa.",
                    "effect": "Kết tủa, tắc nghẽn mạch máu",
                    "management": "KHÔNG trộn. Truyền riêng biệt, cách thời gian."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng calci máu (hypercalcemia)",
                "Dùng với digoxin (tăng nguy cơ loạn nhịp tim nghiêm trọng) - tránh nếu có thể",
                "Trộn với ceftriaxone (kết tủa tử vong)"
            ],
            "tương_đối": [
                "Suy thận nặng - tăng nguy cơ tăng calci máu",
                "Sỏi thận calci - tăng nguy cơ tái phát",
                "Bệnh sarcoidosis - tăng nhạy cảm với calcium"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Calcium gluconate có thể được dùng trong cấp cứu khi cần thiết. Hạ calci máu trong thai kỳ có thể nguy hiểm cho cả mẹ và thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Calcium gluconate bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú với liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Calcium không chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng calci máu: buồn nôn, nôn, táo bón, yếu cơ, rối loạn tâm thần",
                "Loạn nhịp tim (đặc biệt với digoxin)",
                "Sỏi thận",
                "Suy thận cấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và giảm calci máu.",
            "treatment": [
                "Ngừng calcium gluconate ngay lập tức",
                "Truyền dịch muối đẳng trương (0.9% NaCl) để tăng bài tiết calcium",
                "Furosemide (lợi tiểu) để tăng bài tiết calcium (sau khi đã bù dịch)",
                "Calcitonin nếu tăng calci máu nặng",
                "Bisphosphonates (pamidronate, zoledronate) nếu tăng calci máu nặng",
                "Theo dõi ECG liên tục (loạn nhịp tim)",
                "Hemodialysis nếu tăng calci máu rất nặng"
            ],
            "monitoring": "ECG, nồng độ calcium trong máu, creatinine, dấu hiệu lâm sàng."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Dùng trực tiếp từ lọ 10% (10ml = 1g). Không cần pha.",
                "infusion_rate": "Truyền CHẬM trong 10-20 phút cho 1-3g. Không truyền nhanh hơn.",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [
                    "Ceftriaxone - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (kết tủa tử vong)",
                    "Bicarbonate - tạo kết tủa",
                    "Phosphate - tạo kết tủa"
                ],
                "notes": "Có thể truyền vào tĩnh mạch ngoại vi (ít gây nóng bỏng hơn CaCl2), nhưng vẫn ưu tiên tĩnh mạch lớn. Truyền CHẬM (10-20 phút). Theo dõi ECG liên tục. KHÔNG trộn với ceftriaxone, bicarbonate, hoặc phosphate."
            }
        },
        "references": {
            "primary_sources": [
                "ACLS Guidelines - Hyperkalemia Management",
                "UpToDate - Calcium gluconate drug information",
                "FDA Drug Label - Calcium gluconate",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên ACLS guidelines và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["ECG", "Calcium Levels"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - Hyperkalemia Management",
            "FDA Drug Label - Calcium gluconate",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
    
    "Demeclocycline": {
        "group": "Emergency - Electrolyte (Tetracycline Antibiotic)",
        "vietnamese_name": "Demeclocycline, Declomycin",
        "administration": ["PO"],
        "indications": [
            "SIADH (Syndrome of Inappropriate Antidiuretic Hormone) - off-label",
            "Nhiễm khuẩn do vi khuẩn nhạy cảm (ít dùng)",
            "Mụn trứng cá (ít dùng)"
        ],
        "contraindications": [
            "Dị ứng demeclocycline hoặc tetracyclines",
            "Mang thai (category D)",
            "Trẻ em <8 tuổi (nguy cơ răng vàng, xương)",
            "Suy thận nặng"
        ],
        "dosage": {
            "adult_siadh": "300-600mg PO 2-4 lần/ngày",
            "adult_infection": "150mg PO 4 lần/ngày hoặc 300mg PO 2 lần/ngày",
            "notes": "Tetracycline antibiotic. Dùng cho SIADH (gây diabetes insipidus nephrogenic). Ít dùng cho nhiễm khuẩn (có thuốc tốt hơn)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (tăng nguy cơ độc tính thận)"
        },
        "side_effects": [
            "Nhạy cảm với ánh nắng (phổ biến)",
            "Răng vàng (nếu dùng khi <8 tuổi hoặc mang thai)",
            "Xương vàng (nếu dùng khi <8 tuổi hoặc mang thai)",
            "Buồn nôn, nôn",
            "Tiêu chảy",
            "Độc tính thận (nếu suy thận)",
            "Tăng BUN (do tác dụng antianabolic)"
        ],
        "interactions": [
            "Calcium, magnesium, aluminum, iron: giảm hấp thu demeclocycline",
            "Warfarin: tăng INR",
            "Oral contraceptives: giảm hiệu quả"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Demeclocycline là tetracycline antibiotic, ức chế tổng hợp protein vi khuẩn bằng cách gắn với 30S ribosomal subunit. Tác dụng với nhiều vi khuẩn Gram-dương và Gram-âm. Đặc điểm: gây diabetes insipidus nephrogenic (do ức chế tác dụng của ADH trên thận) → dùng cho SIADH (off-label). Ít dùng cho nhiễm khuẩn (có thuốc tốt hơn). Nguy cơ răng vàng, xương vàng nếu dùng khi <8 tuổi hoặc mang thai.",
        "monitoring": [
            "Natri máu (nếu dùng cho SIADH) - quan trọng",
            "Osmolality máu (nếu dùng cho SIADH)",
            "Chức năng thận (creatinine, BUN) - quan trọng",
            "Dấu hiệu nhạy cảm với ánh nắng",
            "Dấu hiệu độc tính thận (nếu suy thận)"
        ],
        "precautions": [
            "SIADH - dùng off-label, gây diabetes insipidus nephrogenic",
            "Nhạy cảm với ánh nắng - TRÁNH ánh nắng mặt trời, dùng kem chống nắng",
            "Răng vàng, xương vàng - CHỐNG CHỈ ĐỊNH khi <8 tuổi hoặc mang thai",
            "Độc tính thận - CHỐNG CHỈ ĐỊNH ở suy thận nặng",
            "Cách thời gian ít nhất 2 giờ với calcium, magnesium, aluminum, iron (giảm hấp thu)",
            "Thận trọng với warfarin (tăng INR)",
            "Giảm hiệu quả oral contraceptives"
        ],
        "pharmacokinetics": {
            "half_life": "10-17 giờ",
            "onset": "Vài ngày (SIADH)",
            "duration": "6-12 giờ (dùng 2-4 lần/ngày)",
            "protein_binding": "41-50%",
            "clearance": "Gan (chuyển hóa một phần), thận (thải trừ một phần). Tích lũy ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "CHỐNG CHỈ ĐỊNH khi <8 tuổi (nguy cơ răng vàng, xương vàng). CHỐNG CHỈ ĐỊNH khi mang thai (category D). Độc tính thận ở suy thận nặng.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium, Magnesium, Aluminum, Iron",
                    "mechanism": "Tạo phức hợp không hòa tan",
                    "effect": "Giảm hấp thu demeclocycline đáng kể (50-90%)",
                    "management": "Cách thời gian ít nhất 2 giờ."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể ức chế chuyển hóa warfarin",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Thận trọng. Theo dõi INR thường xuyên."
                }
            ],
            "moderate": [
                {
                    "drug": "Oral contraceptives",
                    "mechanism": "Giảm hấp thu hoặc chuyển hóa",
                    "effect": "Giảm hiệu quả oral contraceptives",
                    "management": "Sử dụng biện pháp tránh thai bổ sung."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng demeclocycline hoặc tetracyclines",
                "Mang thai (category D)",
                "Trẻ em <8 tuổi (nguy cơ răng vàng, xương vàng)",
                "Suy thận nặng (CrCl <30)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - thận trọng, giảm liều",
                "Dùng với calcium, magnesium, aluminum, iron - cách thời gian ít nhất 2 giờ"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - CHỐNG CHỈ ĐỊNH trong thai kỳ. Có nguy cơ răng vàng, xương vàng ở thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Demeclocycline bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Demeclocycline chuyển hóa một phần qua gan. Suy gan có thể làm giảm chuyển hóa."
        },
        "overdose_management": {
            "symptoms": [
                "Buồn nôn, nôn nặng",
                "Tiêu chảy nặng",
                "Độc tính thận (nếu suy thận)",
                "Nhạy cảm với ánh nắng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay demeclocycline",
                "Rửa dạ dày nếu uống trong vòng 1-2 giờ",
                "Than hoạt tính",
                "Điều trị độc tính thận nếu có",
                "Theo dõi chức năng thận, natri máu"
            ],
            "monitoring": "Chức năng thận, natri máu, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không có thức ăn. Uống với thức ăn có thể giảm buồn nôn.",
                "timing": "Dùng 2-4 lần/ngày. Cách thời gian ít nhất 2 giờ với calcium, magnesium, aluminum, iron. QUAN TRỌNG: TRÁNH ánh nắng mặt trời, dùng kem chống nắng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Declomycin (demeclocycline)",
                "UpToDate - Demeclocycline: Drug information",
                "UpToDate - Treatment of SIADH"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["hepatic", "renal", "dermatologic"],
            "qt_prolongation": False,
            "hepatotoxicity": True,
            "nephrotoxicity": True,
            "requires_monitoring": ["LFT", "RFT", "Photosensitivity"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "IDSA Guidelines - SIADH Treatment"
        ]
    },
    
    "Magnesium oxide": {
        "group": "Emergency - Electrolyte (Magnesium Supplement)",
        "vietnamese_name": "Magnesium oxide, MgO",
        "administration": ["PO"],
        "indications": [
            "Hạ magnesi máu nhẹ đến trung bình",
            "Táo bón",
            "Khó tiêu (antacid)"
        ],
        "contraindications": [
            "Tăng magnesi máu",
            "Suy thận nặng",
            "Block nhĩ thất",
            "Tắc ruột"
        ],
        "dosage": {
            "adult_hypomagnesemia": "400-800mg PO 1-3 lần/ngày",
            "adult_constipation": "400-800mg PO 1-2 lần/ngày",
            "adult_antacid": "400-800mg PO khi cần",
            "notes": "Bổ sung magnesi. Dạng PO, hấp thu kém (chỉ 4%). Tác dụng nhuận tràng (do không hấp thu)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (tăng nguy cơ tăng magnesi máu)",
            "under_30": "CHỐNG CHỈ ĐỊNH (nguy cơ tăng magnesi máu)"
        },
        "side_effects": [
            "Tiêu chảy (phổ biến, do không hấp thu)",
            "Tăng magnesi máu (nếu dùng quá liều hoặc suy thận)",
            "Buồn nôn",
            "Đau bụng"
        ],
        "interactions": [
            "Tetracyclines: giảm hấp thu tetracyclines",
            "Quinolones: giảm hấp thu quinolones",
            "Bisphosphonates: giảm hấp thu bisphosphonates"
        ],
        "pregnancy": "B",
        "mechanism_of_action": "Magnesium oxide cung cấp magnesi (Mg²⁺). Magnesi cần thiết cho: (1) Hoạt động enzyme (ATP, DNA, RNA synthesis), (2) Dẫn truyền thần kinh, (3) Co bóp cơ, (4) Điều hòa calci. Trong hạ magnesi máu: bổ sung magnesi. Đặc điểm: dạng PO, hấp thu kém (chỉ 4%), tác dụng nhuận tràng (do không hấp thu, giữ nước trong ruột), ít hiệu quả hơn magnesium sulfate IV cho hạ magnesi máu nặng.",
        "monitoring": [
            "Magnesi máu - quan trọng",
            "Dấu hiệu tiêu chảy (phổ biến)",
            "Dấu hiệu tăng magnesi máu (nếu dùng quá liều hoặc suy thận): yếu cơ, buồn nôn, block nhĩ thất"
        ],
        "precautions": [
            "TIÊU CHẢY - phổ biến do không hấp thu, giữ nước trong ruột",
            "Hấp thu kém (chỉ 4%) - ít hiệu quả hơn magnesium sulfate IV cho hạ magnesi máu nặng",
            "Thận trọng ở suy thận (tăng nguy cơ tăng magnesi máu)",
            "Cách thời gian ít nhất 2 giờ với tetracyclines, quinolones, bisphosphonates (giảm hấp thu)",
            "Theo dõi magnesi máu nếu dùng lâu dài"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (electrolyte)",
            "onset": "Vài giờ (tiêu chảy), vài ngày (bổ sung magnesi)",
            "duration": "Phụ thuộc liều",
            "protein_binding": "Không áp dụng",
            "clearance": "Hấp thu kém (chỉ 4%), phần lớn thải qua phân. Nếu hấp thu: thận (thải trừ qua nước tiểu)."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Tăng magnesi máu nếu dùng quá liều hoặc suy thận - nguy hiểm. Tiêu chảy - phổ biến.",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Tetracyclines (doxycycline, minocycline)",
                    "mechanism": "Tạo phức hợp không hòa tan",
                    "effect": "Giảm hấp thu tetracyclines",
                    "management": "Cách thời gian ít nhất 2 giờ."
                },
                {
                    "drug": "Quinolones (ciprofloxacin, levofloxacin)",
                    "mechanism": "Tạo phức hợp không hòa tan",
                    "effect": "Giảm hấp thu quinolones",
                    "management": "Cách thời gian ít nhất 2 giờ."
                },
                {
                    "drug": "Bisphosphonates (alendronate, risedronate)",
                    "mechanism": "Tạo phức hợp không hòa tan",
                    "effect": "Giảm hấp thu bisphosphonates",
                    "management": "Cách thời gian ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng magnesi máu",
                "Suy thận nặng (CrCl <30)",
                "Block nhĩ thất",
                "Tắc ruột"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - tăng nguy cơ tăng magnesi máu",
                "Tiêu chảy - có thể làm nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Category B - an toàn hơn category C. Magnesi cần thiết cho thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Magnesi bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Magnesi không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tiêu chảy nặng",
                "Tăng magnesi máu: yếu cơ, buồn nôn, block nhĩ thất, suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị tăng magnesi máu: calcium gluconate IV.",
            "treatment": [
                "Ngừng ngay magnesium oxide",
                "Nếu tăng magnesi máu: Calcium gluconate IV (đối kháng magnesi)",
                "Nếu block nhĩ thất: Atropine, pacemaker nếu cần",
                "Nếu suy hô hấp: Hỗ trợ hô hấp",
                "Theo dõi magnesi máu, ECG liên tục"
            ],
            "monitoring": "Magnesi máu, ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "preparation": "Dạng viên nén hoặc bột.",
                "dosing": "400-800mg PO 1-3 lần/ngày. Cách thời gian ít nhất 2 giờ với tetracyclines, quinolones, bisphosphonates.",
                "notes": "Bổ sung magnesi. Tiêu chảy phổ biến (do không hấp thu). Hấp thu kém (chỉ 4%)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Magnesium Oxide",
                "UpToDate - Magnesium: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": False,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": [],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum magnesium", "Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "KDIGO Guidelines - Electrolyte Management"
        ]
    },
    
    "Magnesium sulfate": {
        "group": "Emergency - Electrolyte",
        "vietnamese_name": "Magnesium sulfate, MgSO4",
        "administration": ["IV", "IM"],
        "indications": [
            "Hạ magie máu có triệu chứng",
            "Torsades de pointes",
            "Eclampsia / Tiền sản giật nặng",
            "Hen phế quản nặng (IV)",
            "Ngộ độc digitalis (một phần)",
            "Động kinh do hạ magie máu"
        ],
        "contraindications": [
            "Tăng magie máu",
            "Block nhĩ thất độ 2-3",
            "Suy thận nặng (CrCl <30) - tích lũy",
            "Nhược cơ nặng"
        ],
        "dosage": {
            "adult_hypomagnesemia": "1-2g IV trong 10-20 phút, sau đó 1g mỗi 6 giờ hoặc truyền liên tục 1-2g/giờ",
            "adult_torsades": "1-2g IV bolus trong 2-5 phút, có thể lặp lại",
            "adult_eclampsia": "4-6g IV bolus, sau đó 1-2g/giờ truyền liên tục",
            "adult_asthma": "2g IV trong 20 phút",
            "pediatric_hypomagnesemia": "25-50mg/kg IV trong 10-20 phút",
            "pediatric_torsades": "25-50mg/kg IV bolus trong 2-5 phút",
            "notes": "1g MgSO4 = 8.1 mEq Mg2+. Truyền CHẬM. Theo dõi phản xạ gân xương và hô hấp."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 50%",
            "under_30": "Tránh dùng hoặc giảm liều mạnh (tích lũy, tăng nguy cơ độc tính)"
        },
        "side_effects": [
            "Nóng bỏng tại chỗ tiêm",
            "Hạ huyết áp (truyền nhanh)",
            "Ức chế hô hấp (quá liều)",
            "Block nhĩ thất (quá liều)",
            "Yếu cơ, mất phản xạ gân xương",
            "Buồn nôn, nôn",
            "Tăng magie máu (quá liều)"
        ],
        "interactions": [
            "Neuromuscular blockers: tăng tác dụng (ức chế hô hấp)",
            "Digoxin: có thể tăng block nhĩ thất",
            "Calcium channel blockers: tăng tác dụng",
            "Aminoglycosides: tăng nguy cơ ức chế thần kinh cơ"
        ],
        "pregnancy": "A - An toàn trong eclampsia",
        "mechanism_of_action": "Magnesium sulfate cung cấp magnesium ion (Mg2+) trực tiếp vào máu. Mg2+ là cofactor cho hơn 300 enzyme, tham gia vào quá trình chuyển hóa năng lượng, tổng hợp protein, và chức năng thần kinh-cơ. Trong hạ magie máu: bổ sung Mg2+ thiếu hụt. Trong torsades de pointes: Mg2+ ổn định màng tế bào tim, giảm nguy cơ loạn nhịp. Trong eclampsia: Mg2+ ức chế giải phóng acetylcholine ở synap thần kinh-cơ, giảm co giật. Trong hen phế quản: Mg2+ giãn cơ trơn phế quản (cơ chế chưa rõ ràng).",
        "monitoring": [
            "Phản xạ gân xương (mất phản xạ = dấu hiệu quá liều sớm)",
            "Hô hấp (ức chế hô hấp = dấu hiệu quá liều nặng)",
            "Nồng độ magie trong máu (mục tiêu: 4-6 mg/dL cho eclampsia, 2-3 mg/dL cho hạ magie máu)",
            "ECG (block nhĩ thất, rối loạn nhịp)",
            "Huyết áp (hạ huyết áp khi truyền nhanh)",
            "Dấu hiệu tại chỗ tiêm (nóng bỏng)"
        ],
        "precautions": [
            "Truyền CHẬM (10-20 phút cho 1-2g) - truyền nhanh gây hạ huyết áp",
            "Theo dõi phản xạ gân xương (mất phản xạ = dấu hiệu quá liều sớm)",
            "Theo dõi hô hấp (ức chế hô hấp = dấu hiệu quá liều nặng)",
            "Thận trọng ở suy thận (tích lũy, tăng nguy cơ độc tính)",
            "Thận trọng với neuromuscular blockers (tăng tác dụng)",
            "Chuẩn bị sẵn calcium gluconate/calcium chloride (antidote cho quá liều)",
            "Trong eclampsia: theo dõi sát phản xạ, hô hấp, nồng độ magie máu"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (magnesium là ion)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "4-6 giờ (tác dụng lâm sàng)",
            "protein_binding": "Khoảng 30% gắn với protein",
            "clearance": "Thận: bài tiết qua nước tiểu (chủ yếu). Tích lũy ở suy thận."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng.",
        "black_box_warnings": "Truyền CHẬM - truyền nhanh có thể gây hạ huyết áp, ức chế hô hấp. Theo dõi phản xạ gân xương và hô hấp. Chuẩn bị sẵn calcium (antidote).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Neuromuscular blockers (Succinylcholine, Rocuronium, Vecuronium)",
                    "mechanism": "Magnesium tăng tác dụng của neuromuscular blockers, ức chế giải phóng acetylcholine.",
                    "effect": "Tăng ức chế thần kinh-cơ, kéo dài tác dụng, tăng nguy cơ ức chế hô hấp",
                    "management": "Giảm liều neuromuscular blocker 25-50%. Theo dõi hô hấp chặt chẽ. Có thể cần hỗ trợ hô hấp."
                }
            ],
            "moderate": [
                {
                    "drug": "Digoxin",
                    "mechanism": "Magnesium có thể tăng block nhĩ thất do digoxin.",
                    "effect": "Tăng block nhĩ thất, tăng nguy cơ loạn nhịp",
                    "management": "Thận trọng. Theo dõi ECG chặt chẽ. Có thể cần điều chỉnh liều digoxin."
                },
                {
                    "drug": "Calcium channel blockers",
                    "mechanism": "Cả hai đều ảnh hưởng đến kênh calci, tác dụng cộng dồn.",
                    "effect": "Tăng tác dụng chẹn kênh calci, tăng nguy cơ hạ huyết áp, block nhĩ thất",
                    "management": "Thận trọng. Theo dõi huyết áp và ECG."
                }
            ],
            "minor": [
                {
                    "drug": "Aminoglycosides",
                    "mechanism": "Cả hai đều có thể ức chế thần kinh-cơ.",
                    "effect": "Tăng nguy cơ ức chế thần kinh-cơ",
                    "management": "Thận trọng. Theo dõi hô hấp."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng magie máu (hypermagnesemia)",
                "Block nhĩ thất độ 2-3",
                "Nhược cơ nặng (myasthenia gravis)"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - tích lũy, tăng nguy cơ độc tính",
                "Suy thận trung bình (CrCl 30-60) - thận trọng, giảm liều",
                "Dùng với neuromuscular blockers - tăng tác dụng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "A",
            "pregnancy_details": "Magnesium sulfate an toàn và là thuốc chuẩn trong điều trị eclampsia và tiền sản giật nặng. Được sử dụng rộng rãi trong sản khoa để phòng ngừa và điều trị co giật do eclampsia.",
            "lactation": {
                "safety": "Compatible",
                "details": "Magnesium sulfate bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú với liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Magnesium không chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Mất phản xạ gân xương (dấu hiệu sớm)",
                "Ức chế hô hấp (dấu hiệu nặng)",
                "Block nhĩ thất, rối loạn nhịp tim",
                "Hạ huyết áp",
                "Yếu cơ, liệt cơ",
                "Hôn mê (quá liều rất nặng)"
            ],
            "antidote": "Calcium gluconate hoặc calcium chloride (đối kháng tác dụng của magnesium)",
            "treatment": [
                "Ngừng magnesium sulfate ngay lập tức",
                "Calcium gluconate 1-3g IV hoặc calcium chloride 1g IV (antidote)",
                "Hỗ trợ hô hấp (thở máy nếu cần)",
                "Truyền dịch nếu hạ huyết áp",
                "Hemodialysis nếu quá liều rất nặng và suy thận",
                "Theo dõi phản xạ, hô hấp, ECG, huyết áp liên tục"
            ],
            "monitoring": "Phản xạ gân xương, hô hấp, ECG, huyết áp, nồng độ magie trong máu. Theo dõi ít nhất 4-6 giờ."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Calcium gluconate / Calcium chloride",
                    "mechanism": "Calcium đối kháng tác dụng của magnesium tại synap thần kinh-cơ.",
                    "indication": "Quá liều magnesium gây ức chế hô hấp, mất phản xạ",
                    "dose": "Calcium gluconate 1-3g IV hoặc Calcium chloride 1g IV",
                    "notes": "Antidote đặc hiệu cho quá liều magnesium. Dùng ngay khi có dấu hiệu ức chế hô hấp."
                }
            ]
        },
        "administration_instructions": {
            "oral": None,
            "iv": {
                "reconstitution": "Pha 1-2g trong 50-100ml D5W hoặc Normal saline.",
                "infusion_rate": "Truyền CHẬM trong 10-20 phút cho 1-2g. Không truyền nhanh hơn.",
                "compatibility": ["D5W", "Normal saline (0.9% NaCl)"],
                "incompatibility": [
                    "Calcium (tạo kết tủa nếu trộn, nhưng có thể truyền riêng biệt)",
                    "Bicarbonate - tạo kết tủa"
                ],
                "notes": "Truyền CHẬM (10-20 phút). Theo dõi phản xạ gân xương và hô hấp. Chuẩn bị sẵn calcium (antidote)."
            },
            "im": {
                "reconstitution": "Dùng trực tiếp từ lọ. Tiêm sâu vào cơ.",
                "injection_site": "Tiêm sâu vào cơ (gluteus maximus hoặc vastus lateralis)",
                "notes": "Tiêm IM có thể gây đau tại chỗ. Hấp thu chậm hơn IV."
            }
        },
        "references": {
            "primary_sources": [
                "ACLS Guidelines - Torsades de Pointes Management",
                "ACOG Guidelines - Eclampsia Management",
                "UpToDate - Magnesium sulfate drug information",
                "FDA Drug Label - Magnesium sulfate",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên ACLS/ACOG guidelines và dữ liệu lâm sàng"
        }
    },
    
    "Pamidronate": {
        "group": "Emergency - Electrolyte (Bisphosphonate)",
        "vietnamese_name": "Pamidronate, Aredia",
        "administration": ["IV"],
        "indications": [
            "Tăng calci máu do ung thư",
            "Ung thư xương (metastatic bone disease)",
            "Bệnh Paget xương"
        ],
        "contraindications": [
            "Hạ calci máu",
            "Suy thận nặng (CrCl <30)",
            "Dị ứng pamidronate hoặc bisphosphonates",
            "Mang thai"
        ],
        "dosage": {
            "adult_hypercalcemia": "60-90mg IV truyền trong 2-4 giờ",
            "adult_bone_metastases": "90mg IV truyền trong 2-4 giờ mỗi 3-4 tuần",
            "adult_paget": "30mg IV truyền trong 2-4 giờ mỗi ngày x 3 ngày",
            "notes": "Bisphosphonate thế hệ 1, ức chế hủy xương. Truyền CHẬM trong 2-4 giờ. Cần bổ sung calci và vitamin D."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <30)"
        },
        "side_effects": [
            "Sốt, ớn lạnh (phổ biến trong 24-48 giờ đầu)",
            "Đau cơ, đau xương",
            "Hạ calci máu (phổ biến, cần bổ sung calci và vitamin D)",
            "Hạ phospho máu",
            "Suy thận cấp (hiếm nhưng nguy hiểm)",
            "Hoại tử xương hàm (ONJ) - hiếm nhưng nguy hiểm",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng nguy cơ hạ calci máu",
            "Loop diuretics: tăng nguy cơ hạ calci máu",
            "Nephrotoxic drugs: tăng nguy cơ suy thận"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Pamidronate là bisphosphonate thế hệ 1, ức chế hủy xương bằng cách: (1) Ức chế enzyme farnesyl pyrophosphate synthase trong tế bào hủy xương (osteoclasts), (2) Gây apoptosis tế bào hủy xương, (3) Giảm hoạt động hủy xương. Kết quả: giảm hủy xương, tăng mật độ xương, giảm calci máu. Được dùng cho tăng calci máu do ung thư, ung thư xương, bệnh Paget xương. Đặc điểm: bisphosphonate thế hệ 1 (yếu hơn zoledronic acid), tác dụng kéo dài (3-4 tuần), nguy cơ suy thận và hoại tử xương hàm.",
        "monitoring": [
            "Calci máu - quan trọng (hạ calci máu phổ biến)",
            "Phospho máu (hạ phospho máu)",
            "Chức năng thận (creatinine, eGFR) - quan trọng (nguy cơ suy thận)",
            "Dấu hiệu sốt, ớn lạnh (phổ biến trong 24-48 giờ đầu)",
            "Dấu hiệu hoại tử xương hàm (đau hàm, sưng, chảy mủ) - hiếm nhưng nguy hiểm",
            "ECG (rối loạn nhịp tim, hiếm)"
        ],
        "precautions": [
            "HẠ CALCI MÁU - phổ biến, cần bổ sung calci và vitamin D",
            "Suy thận cấp - hiếm nhưng nguy hiểm, theo dõi chức năng thận",
            "Hoại tử xương hàm (ONJ) - hiếm nhưng nguy hiểm, đặc biệt ở bệnh nhân ung thư, dùng steroid",
            "Truyền CHẬM trong 2-4 giờ (không nhanh hơn)",
            "Bổ sung calci và vitamin D trước và sau khi dùng",
            "Thận trọng với aminoglycosides, loop diuretics (tăng nguy cơ hạ calci máu)",
            "Thận trọng với nephrotoxic drugs (tăng nguy cơ suy thận)",
            "Không dùng khi mang thai (category D)"
        ],
        "pharmacokinetics": {
            "half_life": "27 giờ (ngắn hơn zoledronic acid)",
            "onset": "24-48 giờ (giảm calci máu)",
            "duration": "3-4 tuần",
            "protein_binding": "54%",
            "clearance": "Thận (chủ yếu, bài tiết nguyên dạng), xương (gắn với xương, thải trừ chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Suy thận cấp - hiếm nhưng nguy hiểm. Hoại tử xương hàm (ONJ) - hiếm nhưng nguy hiểm. Hạ calci máu - phổ biến, cần bổ sung calci và vitamin D. Không dùng khi mang thai (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Cả hai đều gây hạ calci máu",
                    "effect": "Tăng nguy cơ hạ calci máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi calci máu chặt chẽ. Bổ sung calci nếu cần."
                },
                {
                    "drug": "Loop diuretics (furosemide, bumetanide)",
                    "mechanism": "Tăng bài tiết calci qua thận",
                    "effect": "Tăng nguy cơ hạ calci máu",
                    "management": "Thận trọng. Theo dõi calci máu. Bổ sung calci nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Nephrotoxic drugs (aminoglycosides, vancomycin, NSAIDs)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Hạ calci máu",
                "Suy thận nặng (CrCl <30)",
                "Dị ứng pamidronate hoặc bisphosphonates",
                "Mang thai (category D)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình (CrCl 30-60) - thận trọng, có thể giảm liều",
                "Dùng với aminoglycosides, loop diuretics - tăng nguy cơ hạ calci máu",
                "Dùng với nephrotoxic drugs - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - CHỐNG CHỈ ĐỊNH trong thai kỳ. Có nguy cơ dị tật thai nhi và ảnh hưởng đến sự phát triển xương của thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Pamidronate bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Pamidronate không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ calci máu nặng: co giật, tetany, rối loạn nhịp tim",
                "Hạ phospho máu nặng",
                "Suy thận cấp",
                "Sốt, ớn lạnh nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hạ calci máu.",
            "treatment": [
                "Điều trị hạ calci máu: Calcium gluconate hoặc calcium chloride IV",
                "Điều trị hạ phospho máu: Bổ sung phosphate",
                "Điều trị suy thận cấp: Truyền dịch, có thể cần lọc máu",
                "Điều trị sốt: Acetaminophen, NSAIDs",
                "Theo dõi calci, phospho máu, chức năng thận liên tục"
            ],
            "monitoring": "Calci máu, phospho máu, chức năng thận, ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 60-90mg trong 250-500ml Normal saline hoặc D5W.",
                "infusion_rate": "Truyền CHẬM trong 2-4 giờ. Không nhanh hơn.",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [
                    "Calcium (calcium gluconate, calcium chloride) - không trộn",
                    "Các cation khác - không trộn"
                ],
                "notes": "QUAN TRỌNG: 1) Truyền CHẬM trong 2-4 giờ (không nhanh hơn), 2) Bổ sung calci và vitamin D trước và sau khi dùng, 3) Theo dõi chức năng thận chặt chẽ, 4) Theo dõi calci máu chặt chẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Aredia (pamidronate)",
                "UpToDate - Pamidronate: Drug information",
                "ASCO Guidelines - Hypercalcemia of malignancy"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal", "dental"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Serum calcium", "Serum phosphate", "Renal function", "Dental exam"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "ASCO Guidelines - Hypercalcemia of Malignancy",
            "FDA Black Box Warning - Osteonecrosis of Jaw"
        ]
    },
    "Potassium phosphate": {
        "group": "Emergency - Electrolyte (Phosphate Supplement)",
        "vietnamese_name": "Potassium phosphate, K2HPO4, KH2PO4",
        "administration": ["IV"],
        "indications": [
            "Hạ phospho máu",
            "Hạ phospho máu nặng",
            "Hạ kali máu kèm hạ phospho máu"
        ],
        "contraindications": [
            "Tăng phospho máu",
            "Tăng kali máu",
            "Suy thận nặng",
            "Tăng calci máu",
            "Dùng với calcium"
        ],
        "dosage": {
            "adult_iv": "0.16-0.32 mmol/kg IV truyền trong 2-6 giờ",
            "notes": "Bổ sung phosphate và kali. Dùng cho hạ phospho máu kèm hạ kali máu. Truyền CHẬM (2-6 giờ) để tránh hạ calci máu và tăng kali máu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (tăng nguy cơ tăng phospho và kali máu)",
            "under_30": "CHỐNG CHỈ ĐỊNH (nguy cơ tăng phospho và kali máu)"
        },
        "side_effects": [
            "Hạ calci máu (phổ biến, do kết tủa với calci)",
            "Tăng kali máu (nếu dùng quá liều)",
            "Tăng phospho máu (nếu dùng quá liều)",
            "Rối loạn nhịp tim (nếu hạ calci máu hoặc tăng kali máu)",
            "Co giật (nếu hạ calci máu nặng)"
        ],
        "interactions": [
            "Calcium: kết tủa (CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI)",
            "Magnesium: kết tủa",
            "ACE inhibitors, ARBs: tăng nguy cơ tăng kali máu"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Potassium phosphate cung cấp phosphate (PO4³⁻) và kali (K⁺). Phosphate cần thiết cho tổng hợp ATP, cấu trúc xương, đệm pH. Kali cần thiết cho dẫn truyền thần kinh, co bóp cơ. Trong hạ phospho máu kèm hạ kali máu: bổ sung cả hai. Đặc điểm: kết tủa với calci (gây hạ calci máu), tăng kali máu nếu dùng quá liều, cần truyền CHẬM (2-6 giờ), thận trọng ở suy thận.",
        "monitoring": [
            "Phospho máu - quan trọng",
            "Kali máu - quan trọng (tăng kali máu nếu dùng quá liều)",
            "Calci máu - quan trọng (hạ calci máu phổ biến do kết tủa)",
            "ECG (rối loạn nhịp tim nếu hạ calci máu hoặc tăng kali máu)",
            "Chức năng thận (creatinine, eGFR) - quan trọng",
            "Dấu hiệu hạ calci máu: tetany, co giật",
            "Dấu hiệu tăng kali máu: yếu cơ, rối loạn nhịp tim"
        ],
        "precautions": [
            "HẠ CALCI MÁU - phổ biến do kết tủa với calci, theo dõi calci máu chặt chẽ",
            "TĂNG KALI MÁU - nếu dùng quá liều, theo dõi kali máu chặt chẽ",
            "KHÔNG trộn với calcium (kết tủa tử vong)",
            "Truyền CHẬM (2-6 giờ) để giảm hạ calci máu và tăng kali máu",
            "Thận trọng ở suy thận (tăng nguy cơ tăng phospho và kali máu)",
            "Theo dõi calci, kali, và phospho máu chặt chẽ",
            "Bổ sung calci nếu hạ calci máu",
            "Thận trọng với ACE inhibitors, ARBs (tăng nguy cơ tăng kali máu)"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (electrolyte)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Phụ thuộc liều và tình trạng bệnh nhân",
            "protein_binding": "Không áp dụng",
            "clearance": "Thận (thải trừ qua nước tiểu), xương (lắng đọng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "KHÔNG trộn với calcium - kết tủa tử vong. Hạ calci máu - phổ biến, theo dõi calci máu chặt chẽ. Tăng kali máu - nếu dùng quá liều, theo dõi kali máu chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium (calcium gluconate, calcium chloride)",
                    "mechanism": "Kết tủa calcium phosphate",
                    "effect": "Kết tủa tử vong, tắc mạch, hạ calci máu",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không trộn hoặc truyền cùng."
                },
                {
                    "drug": "ACE inhibitors, ARBs (lisinopril, losartan)",
                    "mechanism": "Giảm bài tiết kali qua thận",
                    "effect": "Tăng nguy cơ tăng kali máu",
                    "management": "Thận trọng. Theo dõi kali máu chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Magnesium",
                    "mechanism": "Kết tủa magnesium phosphate",
                    "effect": "Kết tủa, giảm hiệu quả cả hai",
                    "management": "Tránh trộn hoặc truyền cùng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng phospho máu",
                "Tăng kali máu",
                "Suy thận nặng (CrCl <30)",
                "Tăng calci máu",
                "Dùng với calcium (kết tủa tử vong)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - tăng nguy cơ tăng phospho và kali máu",
                "Dùng với ACE inhibitors, ARBs - tăng nguy cơ tăng kali máu"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Phosphate và kali cần thiết cho thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Phosphate và kali bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Phosphate và kali không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng phospho máu: mệt mỏi, buồn nôn, ngứa",
                "Tăng kali máu: yếu cơ, rối loạn nhịp tim",
                "Hạ calci máu nặng: tetany, co giật, rối loạn nhịp tim",
                "Kết tủa (nếu trộn với calcium)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hạ calci máu: calcium gluconate IV. Điều trị tăng kali máu: calcium gluconate, insulin+glucose, kayexalate.",
            "treatment": [
                "Ngừng ngay potassium phosphate",
                "Nếu hạ calci máu: Calcium gluconate hoặc calcium chloride IV",
                "Nếu tăng kali máu: Calcium gluconate (bảo vệ tim), insulin+glucose, kayexalate",
                "Nếu tăng phospho máu: Truyền dịch, có thể cần lọc máu",
                "Điều trị co giật: Benzodiazepines",
                "Theo dõi calci, kali, phospho máu, ECG liên tục"
            ],
            "monitoring": "Calci máu, kali máu, phospho máu, ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 0.16-0.32 mmol/kg trong 250-500ml Normal saline hoặc D5W.",
                "infusion_rate": "Truyền CHẬM trong 2-6 giờ. Không nhanh hơn.",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [
                    "Calcium (calcium gluconate, calcium chloride) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (kết tủa tử vong)",
                    "Magnesium - kết tủa",
                    "Aluminum - kết tủa"
                ],
                "notes": "QUAN TRỌNG: 1) Truyền CHẬM trong 2-6 giờ (không nhanh hơn), 2) KHÔNG trộn với calcium (kết tủa tử vong), 3) Theo dõi calci, kali, và phospho máu chặt chẽ, 4) Bổ sung calci nếu hạ calci máu."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Potassium Phosphate Injection",
                "UpToDate - Phosphate: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum potassium", "Serum phosphate", "Serum calcium", "ECG", "Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "KDIGO Guidelines - Electrolyte Management",
            "FDA Black Box Warning - Precipitation with Calcium"
        ]
    },
    
    "Sodium bicarbonate": {
        "group": "Emergency - Electrolyte",
        "vietnamese_name": "Sodium bicarbonate, NaHCO3, Baking soda",
        "administration": ["IV", "PO"],
        "indications": [
            "Tăng kali máu nặng (nếu có toan chuyển hóa)",
            "Toan chuyển hóa nặng (pH <7.1)",
            "Ngộ độc salicylate (aspirin)",
            "Ngộ độc tricyclic antidepressant",
            "Ngộ độc methanol, ethylene glycol (một phần)",
            "Ngộ độc barbiturate (một phần)"
        ],
        "contraindications": [
            "Kiềm chuyển hóa",
            "Phù phổi cấp",
            "Hạ kali máu nặng (có thể làm nặng)",
            "Suy thận nặng với phù (tăng natri, tăng thể tích)"
        ],
        "dosage": {
            "adult_hyperkalemia": "50-100 mEq IV bolus trong 5-10 phút, có thể lặp lại",
            "adult_metabolic_acidosis": "1-2 mEq/kg IV bolus, sau đó truyền liên tục theo base deficit",
            "adult_salicylate_poisoning": "150 mEq trong 1L D5W, truyền 200ml/giờ",
            "pediatric_hyperkalemia": "1-2 mEq/kg IV bolus trong 5-10 phút",
            "pediatric_metabolic_acidosis": "1-2 mEq/kg IV bolus, sau đó truyền liên tục",
            "notes": "1 mEq NaHCO3 = 84mg. Truyền CHẬM. Theo dõi pH, kali máu, natri máu. Không trộn với calcium."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều",
            "under_30": "Thận trọng, giảm liều, theo dõi natri máu và thể tích"
        },
        "side_effects": [
            "Tăng natri máu (hypernatremia)",
            "Phù (tăng thể tích)",
            "Kiềm chuyển hóa (nếu quá liều)",
            "Hạ kali máu (do dịch chuyển K+ vào tế bào)",
            "Hạ calci máu (do tăng gắn với protein)",
            "Co giật (nếu tăng natri máu nhanh)",
            "Phù phổi cấp (nếu tăng thể tích nhanh)"
        ],
        "interactions": [
            "Calcium: tạo kết tủa - không trộn",
            "Catecholamines (epinephrine, norepinephrine): bất hoạt trong môi trường kiềm",
            "Thiazide diuretics: tăng nguy cơ kiềm chuyển hóa",
            "Lithium: tăng thải trừ lithium, giảm nồng độ"
        ],
        ',
        "pregnancy": "C - An toàn trong cấp cứu",
        ',
        "mechanism_of_action": "Sodium bicarbonate cung cấp bicarbonate ion (HCO3-) và natri ion (Na+) vào máu. HCO3- là base, trung hòa acid (H+), tăng pH máu. Trong toan chuyển hóa: HCO3- + H+ → H2CO3 → H2O + CO2 (thở ra), tăng pH. Trong tăng kali máu: kiềm hóa máu → dịch chuyển K+ từ ngoại bào vào nội bào → giảm kali máu. Trong ngộ độc salicylate: kiềm hóa nước tiểu → tăng thải trừ salicylate qua thận. ĐẶC ĐIỂM: (1) Base mạnh, trung hòa acid, (2) Dịch chuyển K+ vào tế bào (giảm kali máu), (3) Tăng natri và thể tích (nguy cơ phù), (4) Truyền CHẬM, (5) Theo dõi pH, kali, natri máu.",
        "monitoring": [
            "pH máu (mục tiêu: 7.35-7.45, không quá 7.5)",
            "Kali máu (có thể giảm do dịch chuyển vào tế bào)",
            "Natri máu (có thể tăng do Na+ trong NaHCO3)",
            "Thể tích dịch (nguy cơ phù, phù phổi)",
            "ECG (theo dõi loạn nhịp tim, đặc biệt với hạ kali máu)",
            "Dấu hiệu phù phổi cấp (khó thở, ran ẩm)"
        ],
        "precautions": [
            "Truyền CHẬM (5-10 phút cho bolus) - truyền nhanh gây tăng natri máu nhanh, co giật",
            "Theo dõi pH máu (không quá 7.5 - nguy cơ kiềm chuyển hóa)",
            "Theo dõi kali máu (có thể giảm do dịch chuyển vào tế bào)",
            "Theo dõi natri máu (có thể tăng do Na+ trong NaHCO3)",
            "Thận trọng ở bệnh nhân suy tim, phù (tăng natri, tăng thể tích)",
            "KHÔNG trộn với calcium (tạo kết tủa)",
            "KHÔNG trộn với catecholamines (bất hoạt trong môi trường kiềm)",
            "Chỉ dùng trong toan chuyển hóa nặng (pH <7.1) hoặc tăng kali máu nặng với toan"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (bicarbonate là ion)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "2-4 giờ (tác dụng lâm sàng)",
            "protein_binding": "Không áp dụng",
            "clearance": "Thận: bài tiết qua nước tiểu. Phổi: CO2 thở ra."
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Kiểm tra hạn sử dụng.",
        "black_box_warnings": "Truyền CHẬM - truyền nhanh có thể gây tăng natri máu nhanh, co giật, phù phổi cấp. KHÔNG trộn với calcium - tạo kết tủa. Theo dõi pH, kali, natri máu chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium (calcium chloride, calcium gluconate)",
                    "mechanism": "Tạo phức hợp không hòa tan, gây kết tủa.",
                    "effect": "Kết tủa, tắc nghẽn mạch máu",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI: Không trộn hoặc truyền cùng. Truyền riêng biệt, cách thời gian."
                },
                {
                    "drug": "Catecholamines (epinephrine, norepinephrine, dopamine)",
                    "mechanism": "Bất hoạt catecholamines trong môi trường kiềm.",
                    "effect": "Giảm tác dụng của catecholamines, giảm hiệu quả điều trị sốc",
                    "management": "KHÔNG trộn. Truyền riêng biệt. Nếu cần dùng cùng, truyền qua đường khác hoặc cách thời gian."
                }
            ],
            "moderate": [
                {
                    "drug": "Thiazide diuretics",
                    "mechanism": "Cả hai đều có thể gây kiềm chuyển hóa.",
                    "effect": "Tăng nguy cơ kiềm chuyển hóa",
                    "management": "Theo dõi pH máu chặt chẽ. Có thể cần giảm liều sodium bicarbonate."
                },
                {
                    "drug": "Lithium",
                    "mechanism": "Sodium bicarbonate tăng thải trừ lithium qua thận.",
                    "effect": "Giảm nồng độ lithium, giảm hiệu quả điều trị",
                    "management": "Theo dõi nồng độ lithium. Có thể cần tăng liều lithium."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Kiềm chuyển hóa (alkalosis)",
                "Trộn với calcium (kết tủa tử vong)",
                "Phù phổi cấp"
            ],
            "tương_đối": [
                "Hạ kali máu nặng - có thể làm nặng",
                "Suy thận nặng với phù - tăng natri, tăng thể tích",
                "Suy tim - tăng thể tích, tăng gánh tim"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Sodium bicarbonate có thể được dùng trong cấp cứu khi cần thiết. Toan chuyển hóa nặng trong thai kỳ có thể nguy hiểm cho cả mẹ và thai nhi. Có thể dùng khi lợi ích vượt quá nguy cơ.",
            "lactation": {
                "safety": "Compatible",
                "details": "Sodium bicarbonate bài tiết vào sữa mẹ ở nồng độ thấp. An toàn khi cho con bú với liều điều trị.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không cần điều chỉnh liều",
            "moderate": "Không cần điều chỉnh liều",
            "severe": "Không cần điều chỉnh liều",
            "notes": "Sodium bicarbonate không chuyển hóa ở gan. Suy gan không ảnh hưởng đáng kể."
        },
        "overdose_management": {
            "symptoms": [
                "Kiềm chuyển hóa: co giật, tetany, rối loạn tâm thần",
                "Tăng natri máu: co giật, hôn mê",
                "Phù phổi cấp: khó thở, ran ẩm",
                "Hạ kali máu: yếu cơ, loạn nhịp tim"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ và điều chỉnh rối loạn điện giải.",
            "treatment": [
                "Ngừng sodium bicarbonate ngay lập tức",
                "Truyền dịch muối đẳng trương (0.9% NaCl) nếu tăng natri máu",
                "Bổ sung kali nếu hạ kali máu",
                "Điều trị kiềm chuyển hóa: truyền dịch muối, có thể dùng acid (HCl) nếu nặng",
                "Điều trị phù phổi cấp: furosemide, hỗ trợ hô hấp",
                "Theo dõi pH, kali, natri máu, ECG liên tục"
            ],
            "monitoring": "pH máu, kali máu, natri máu, ECG, dấu hiệu lâm sàng, thể tích dịch."
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "preparation": "Dạng viên nén hoặc bột.",
                "dosing": "325-650mg PO 1-4 lần/ngày (điều trị toan nhẹ, khó tiêu).",
                "notes": "Dạng PO chủ yếu dùng cho khó tiêu, toan nhẹ. Dạng IV dùng cho cấp cứu."
            },
            "iv": {
                "reconstitution": "Pha 50-100 mEq trong 50-100ml D5W hoặc Normal saline.",
                "infusion_rate": "Truyền CHẬM trong 5-10 phút cho bolus. Không truyền nhanh hơn.",
                "compatibility": ["D5W", "Normal saline (0.9% NaCl)"],
                "incompatibility": [
                    "Calcium (calcium chloride, calcium gluconate) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (kết tủa tử vong)",
                    "Catecholamines (epinephrine, norepinephrine, dopamine) - bất hoạt trong môi trường kiềm"
                ],
                "notes": "Truyền CHẬM (5-10 phút cho bolus). Theo dõi pH, kali, natri máu chặt chẽ. KHÔNG trộn với calcium hoặc catecholamines."
            }
        },
        "references": {
            "primary_sources": [
                "ACLS Guidelines - Hyperkalemia Management",
                "UpToDate - Sodium bicarbonate drug information",
                "FDA Drug Label - Sodium bicarbonate",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A - Dựa trên ACLS guidelines và dữ liệu lâm sàng"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["metabolic"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["pH", "Electrolytes", "ECG"]
        },
        "guideline_tags": [
            "ACLS Guidelines 2020 - Hyperkalemia Management",
            "FDA Drug Label - Sodium bicarbonate",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
    
    "Sodium phosphate": {
        "group": "Emergency - Electrolyte (Phosphate Supplement)",
        "vietnamese_name": "Sodium phosphate, Na2HPO4, NaH2PO4",
        "administration": ["IV", "PO"],
        "indications": [
            "Hạ phospho máu",
            "Hạ phospho máu nặng",
            "Chuẩn bị đại tràng (bowel preparation) - dạng PO"
        ],
        "contraindications": [
            "Tăng phospho máu",
            "Suy thận nặng",
            "Tăng calci máu",
            "Tắc ruột (dạng PO)"
        ],
        "dosage": {
            "adult_iv": "0.16-0.32 mmol/kg IV truyền trong 2-6 giờ",
            "adult_po": "1-2 gói PO với nước (cho chuẩn bị đại tràng)",
            "notes": "Bổ sung phosphate. Dạng IV cho hạ phospho máu. Dạng PO cho chuẩn bị đại tràng. Truyền CHẬM (2-6 giờ) để tránh hạ calci máu."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng (tăng nguy cơ tăng phospho máu)",
            "under_30": "CHỐNG CHỈ ĐỊNH (nguy cơ tăng phospho máu)"
        },
        "side_effects": [
            "Hạ calci máu (phổ biến, do kết tủa với calci)",
            "Tăng phospho máu (nếu dùng quá liều)",
            "Rối loạn nhịp tim (nếu hạ calci máu nặng)",
            "Co giật (nếu hạ calci máu nặng)",
            "Tiêu chảy (dạng PO)"
        ],
        "interactions": [
            "Calcium: kết tủa (CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI)",
            "Magnesium: kết tủa",
            "Aluminum: kết tủa"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Sodium phosphate cung cấp phosphate (PO4³⁻). Phosphate cần thiết cho: (1) Tổng hợp ATP (năng lượng tế bào), (2) Cấu trúc xương và răng, (3) Đệm pH máu, (4) Chức năng tế bào. Trong hạ phospho máu: bổ sung phosphate. Đặc điểm: kết tủa với calci (gây hạ calci máu), cần truyền CHẬM (2-6 giờ), thận trọng ở suy thận (tăng nguy cơ tăng phospho máu).",
        "monitoring": [
            "Phospho máu - quan trọng",
            "Calci máu - quan trọng (hạ calci máu phổ biến do kết tủa)",
            "ECG (rối loạn nhịp tim nếu hạ calci máu)",
            "Chức năng thận (creatinine, eGFR) - quan trọng",
            "Dấu hiệu hạ calci máu: tetany, co giật, rối loạn nhịp tim"
        ],
        "precautions": [
            "HẠ CALCI MÁU - phổ biến do kết tủa với calci, theo dõi calci máu chặt chẽ",
            "KHÔNG trộn với calcium (kết tủa tử vong)",
            "Truyền CHẬM (2-6 giờ) để giảm hạ calci máu",
            "Thận trọng ở suy thận (tăng nguy cơ tăng phospho máu)",
            "Theo dõi calci và phospho máu chặt chẽ",
            "Bổ sung calci nếu hạ calci máu"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (electrolyte)",
            "onset": "Ngay lập tức sau khi truyền IV",
            "duration": "Phụ thuộc liều và tình trạng bệnh nhân",
            "protein_binding": "Không áp dụng",
            "clearance": "Thận (thải trừ qua nước tiểu), xương (lắng đọng)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "KHÔNG trộn với calcium - kết tủa tử vong. Hạ calci máu - phổ biến, theo dõi calci máu chặt chẽ.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Calcium (calcium gluconate, calcium chloride)",
                    "mechanism": "Kết tủa calcium phosphate",
                    "effect": "Kết tủa tử vong, tắc mạch, hạ calci máu",
                    "management": "CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI. Không trộn hoặc truyền cùng."
                },
                {
                    "drug": "Magnesium",
                    "mechanism": "Kết tủa magnesium phosphate",
                    "effect": "Kết tủa, giảm hiệu quả cả hai",
                    "management": "Tránh trộn hoặc truyền cùng."
                }
            ],
            "moderate": [
                {
                    "drug": "Aluminum",
                    "mechanism": "Kết tủa aluminum phosphate",
                    "effect": "Kết tủa, giảm hiệu quả cả hai",
                    "management": "Tránh trộn hoặc truyền cùng."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tăng phospho máu",
                "Suy thận nặng (CrCl <30)",
                "Tăng calci máu",
                "Dùng với calcium (kết tủa tử vong)",
                "Tắc ruột (dạng PO)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình - tăng nguy cơ tăng phospho máu",
                "Dùng với magnesium, aluminum - tránh"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Phosphate cần thiết cho thai nhi.",
            "lactation": {
                "safety": "Compatible",
                "details": "Phosphate bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Phosphate không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Tăng phospho máu: mệt mỏi, buồn nôn, ngứa",
                "Hạ calci máu nặng: tetany, co giật, rối loạn nhịp tim",
                "Kết tủa (nếu trộn với calcium)"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hạ calci máu: calcium gluconate IV.",
            "treatment": [
                "Ngừng ngay sodium phosphate",
                "Nếu hạ calci máu: Calcium gluconate hoặc calcium chloride IV",
                "Nếu tăng phospho máu: Truyền dịch, có thể cần lọc máu",
                "Điều trị co giật: Benzodiazepines",
                "Theo dõi calci, phospho máu, ECG liên tục"
            ],
            "monitoring": "Calci máu, phospho máu, ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 0.16-0.32 mmol/kg trong 250-500ml Normal saline hoặc D5W.",
                "infusion_rate": "Truyền CHẬM trong 2-6 giờ. Không nhanh hơn.",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [
                    "Calcium (calcium gluconate, calcium chloride) - CHỐNG CHỈ ĐỊNH TUYỆT ĐỐI (kết tủa tử vong)",
                    "Magnesium - kết tủa",
                    "Aluminum - kết tủa"
                ],
                "notes": "QUAN TRỌNG: 1) Truyền CHẬM trong 2-6 giờ (không nhanh hơn), 2) KHÔNG trộn với calcium (kết tủa tử vong), 3) Theo dõi calci và phospho máu chặt chẽ, 4) Bổ sung calci nếu hạ calci máu."
            },
            "oral": {
                "preparation": "Pha 1-2 gói trong nước.",
                "dosing": "1-2 gói PO với nước (cho chuẩn bị đại tràng).",
                "notes": "Dùng cho chuẩn bị đại tràng. Uống với nhiều nước."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Sodium Phosphate Injection",
                "UpToDate - Phosphate: Drug information"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["cardiac", "renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum phosphate", "Serum calcium", "ECG", "Renal function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "KDIGO Guidelines - Electrolyte Management",
            "FDA Black Box Warning - Precipitation with Calcium"
        ]
    },
    
    "Sodium polystyrene sulfonate": {
        "group": "Emergency - Electrolyte (Potassium Binder)",
        "vietnamese_name": "Sodium polystyrene sulfonate, Kayexalate, Resonium",
        "administration": ["PO", "Rectal"],
        "indications": [
            "Tăng kali máu",
            "Tăng kali máu mạn tính"
        ],
        "contraindications": [
            "Tắc ruột",
            "Giảm nhu động ruột",
            "Hạ kali máu",
            "Tăng natri máu nặng",
            "Suy tim nặng (do tăng natri)"
        ],
        "dosage": {
            "adult_po": "15-30g PO 1-4 lần/ngày với nước hoặc sorbitol",
            "adult_rectal": "30-50g thụt trực tràng, giữ 30-60 phút, rửa sạch sau đó",
            "notes": "Kayexalate là nhựa trao đổi ion, gắn kali trong ruột và thải qua phân. Tác dụng chậm (vài giờ)."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Táo bón (phổ biến, có thể nặng)",
            "Buồn nôn, nôn",
            "Tăng natri máu (do trao đổi Na+ với K+)",
            "Hoại tử ruột (hiếm nhưng nguy hiểm, đặc biệt với sorbitol)",
            "Tắc ruột (nếu táo bón nặng)"
        ],
        "interactions": [
            "Laxatives (sorbitol): tăng nguy cơ hoại tử ruột",
            "Cation (calcium, magnesium): giảm hiệu quả kayexalate"
        ],
        "pregnancy": "C",
        "mechanism_of_action": "Sodium polystyrene sulfonate (Kayexalate) là nhựa trao đổi ion. Trong ruột, natri (Na+) từ kayexalate trao đổi với kali (K+) từ cơ thể, gắn kali và thải qua phân. Giảm kali máu bằng cách tăng bài tiết kali qua phân (không qua thận). Đặc điểm: tác dụng chậm (vài giờ), không dùng cho cấp cứu, nguy cơ táo bón và hoại tử ruột (đặc biệt với sorbitol).",
        "monitoring": [
            "Kali máu - quan trọng (tác dụng chậm)",
            "Natri máu (tăng natri do trao đổi)",
            "Dấu hiệu táo bón (phổ biến, có thể nặng)",
            "Dấu hiệu hoại tử ruột: đau bụng nặng, nôn, sốt (hiếm nhưng nguy hiểm)"
        ],
        "precautions": [
            "TÁO BÓN - phổ biến, có thể nặng, cần dùng với sorbitol hoặc thuốc nhuận tràng",
            "Hoại tử ruột - hiếm nhưng nguy hiểm, đặc biệt với sorbitol, theo dõi dấu hiệu",
            "Tác dụng chậm (vài giờ) - không dùng cho cấp cứu",
            "Tăng natri máu - do trao đổi Na+ với K+",
            "Thận trọng ở suy tim (tăng natri có thể làm nặng)",
            "Dùng với nước hoặc sorbitol để giảm táo bón",
            "Tránh dùng với cation (calcium, magnesium) - giảm hiệu quả"
        ],
        "pharmacokinetics": {
            "half_life": "Không áp dụng (không hấp thu)",
            "onset": "Vài giờ (chậm)",
            "duration": "Vài giờ đến vài ngày",
            "protein_binding": "Không áp dụng (không hấp thu)",
            "clearance": "Không hấp thu, thải qua phân"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm",
        "black_box_warnings": "Nguy cơ hoại tử ruột, đặc biệt với sorbitol. Nguy cơ táo bón nặng. Tác dụng chậm - không dùng cho cấp cứu.",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Sorbitol (laxative)",
                    "mechanism": "Tăng nguy cơ hoại tử ruột",
                    "effect": "Hoại tử ruột, có thể tử vong",
                    "management": "Thận trọng. Theo dõi dấu hiệu hoại tử ruột."
                }
            ],
            "moderate": [
                {
                    "drug": "Cation (calcium, magnesium)",
                    "mechanism": "Cạnh tranh với kali trong trao đổi ion",
                    "effect": "Giảm hiệu quả kayexalate",
                    "management": "Tránh dùng cùng. Cách thời gian ít nhất 2 giờ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Tắc ruột",
                "Giảm nhu động ruột",
                "Hạ kali máu",
                "Tăng natri máu nặng",
                "Suy tim nặng (do tăng natri)"
            ],
            "tương_đối": [
                "Suy tim nhẹ đến trung bình - tăng natri có thể làm nặng",
                "Táo bón - có thể làm nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "C",
            "pregnancy_details": "Category C - có nguy cơ cho thai nhi. Không hấp thu.",
            "lactation": {
                "safety": "Compatible",
                "details": "Không hấp thu, không bài tiết vào sữa mẹ.",
                "recommendation": "Có thể dùng khi cho con bú."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Không hấp thu, không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Táo bón nặng",
                "Tắc ruột",
                "Hoại tử ruột: đau bụng nặng, nôn, sốt",
                "Hạ kali máu (nếu dùng quá liều)",
                "Tăng natri máu"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay kayexalate",
                "Nếu táo bón: thuốc nhuận tràng, thụt tháo",
                "Nếu hoại tử ruột: cấp cứu phẫu thuật",
                "Điều trị hạ kali máu nếu có",
                "Điều trị tăng natri máu nếu có",
                "Theo dõi kali, natri máu"
            ],
            "monitoring": "Kali máu, natri máu, dấu hiệu táo bón, hoại tử ruột"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "preparation": "Pha 15-30g trong nước hoặc sorbitol.",
                "dosing": "15-30g PO 1-4 lần/ngày với nước hoặc sorbitol.",
                "notes": "Dùng với nước hoặc sorbitol để giảm táo bón. Tránh dùng với cation (calcium, magnesium)."
            },
            "rectal": {
                "preparation": "Pha 30-50g trong nước.",
                "technique": "Thụt trực tràng, giữ 30-60 phút, rửa sạch sau đó.",
                "notes": "Dùng cho bệnh nhân không thể uống. Giữ 30-60 phút, rửa sạch sau đó."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Kayexalate (sodium polystyrene sulfonate)",
                "UpToDate - Treatment of hyperkalemia",
                "KDIGO Guidelines - Chronic Kidney Disease"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["gastrointestinal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": False,
            "requires_monitoring": ["Serum potassium", "Serum sodium", "Bowel function"]
        },
        "guideline_tags": [
            "FDA Drug Information",
            "UpToDate Drug Information",
            "KDIGO Guidelines - Hyperkalemia Management",
            "FDA Black Box Warning - Intestinal Necrosis"
        ]
    },
    
    "Zoledronic acid": {
        "group": "Emergency - Electrolyte (Bisphosphonate)",
        "vietnamese_name": "Zoledronic acid, Zometa, Reclast",
        "administration": ["IV"],
        "indications": [
            "Tăng calci máu do ung thư",
            "Loãng xương (osteoporosis)",
            "Bệnh Paget xương",
            "Ung thư xương (metastatic bone disease)"
        ],
        "contraindications": [
            "Hạ calci máu",
            "Suy thận nặng (CrCl <35)",
            "Dị ứng zoledronic acid hoặc bisphosphonates",
            "Mang thai"
        ],
        "dosage": {
            "adult_hypercalcemia": "4mg IV truyền trong 15 phút",
            "adult_osteoporosis": "5mg IV truyền trong 15 phút mỗi 12 tháng",
            "adult_paget": "5mg IV truyền trong 15 phút",
            "notes": "Bisphosphonate, ức chế hủy xương. Truyền CHẬM trong 15 phút. Cần bổ sung calci và vitamin D."
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "CHỐNG CHỈ ĐỊNH (CrCl <35)"
        },
        "side_effects": [
            "Sốt, ớn lạnh (phổ biến trong 24-48 giờ đầu)",
            "Đau cơ, đau xương",
            "Hạ calci máu (phổ biến, cần bổ sung calci và vitamin D)",
            "Hạ phospho máu",
            "Suy thận cấp (hiếm nhưng nguy hiểm)",
            "Hoại tử xương hàm (ONJ) - hiếm nhưng nguy hiểm",
            "Rối loạn nhịp tim (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng nguy cơ hạ calci máu",
            "Loop diuretics: tăng nguy cơ hạ calci máu",
            "Nephrotoxic drugs: tăng nguy cơ suy thận"
        ],
        "pregnancy": "D - CHỐNG CHỈ ĐỊNH",
        "mechanism_of_action": "Zoledronic acid là bisphosphonate thế hệ 3, ức chế hủy xương bằng cách: (1) Ức chế enzyme farnesyl pyrophosphate synthase trong tế bào hủy xương (osteoclasts), (2) Gây apoptosis tế bào hủy xương, (3) Giảm hoạt động hủy xương. Kết quả: giảm hủy xương, tăng mật độ xương, giảm calci máu. Được dùng cho tăng calci máu do ung thư, loãng xương, bệnh Paget xương. Đặc điểm: tác dụng mạnh, tác dụng kéo dài (12 tháng), nguy cơ suy thận và hoại tử xương hàm.",
        "monitoring": [
            "Calci máu - quan trọng (hạ calci máu phổ biến)",
            "Phospho máu (hạ phospho máu)",
            "Chức năng thận (creatinine, eGFR) - quan trọng (nguy cơ suy thận)",
            "Dấu hiệu sốt, ớn lạnh (phổ biến trong 24-48 giờ đầu)",
            "Dấu hiệu hoại tử xương hàm (đau hàm, sưng, chảy mủ) - hiếm nhưng nguy hiểm",
            "ECG (rối loạn nhịp tim, hiếm)"
        ],
        "precautions": [
            "HẠ CALCI MÁU - phổ biến, cần bổ sung calci và vitamin D",
            "Suy thận cấp - hiếm nhưng nguy hiểm, theo dõi chức năng thận",
            "Hoại tử xương hàm (ONJ) - hiếm nhưng nguy hiểm, đặc biệt ở bệnh nhân ung thư, dùng steroid",
            "Truyền CHẬM trong 15 phút (không nhanh hơn)",
            "Bổ sung calci và vitamin D trước và sau khi dùng",
            "Thận trọng với aminoglycosides, loop diuretics (tăng nguy cơ hạ calci máu)",
            "Thận trọng với nephrotoxic drugs (tăng nguy cơ suy thận)",
            "Không dùng khi mang thai (category D)"
        ],
        "pharmacokinetics": {
            "half_life": "146 giờ (rất dài, do gắn với xương)",
            "onset": "24-48 giờ (giảm calci máu)",
            "duration": "12 tháng (loãng xương)",
            "protein_binding": "22%",
            "clearance": "Thận (chủ yếu, bài tiết nguyên dạng), xương (gắn với xương, thải trừ chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng",
        "black_box_warnings": "Suy thận cấp - hiếm nhưng nguy hiểm. Hoại tử xương hàm (ONJ) - hiếm nhưng nguy hiểm. Hạ calci máu - phổ biến, cần bổ sung calci và vitamin D. Không dùng khi mang thai (category D).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Cả hai đều gây hạ calci máu",
                    "effect": "Tăng nguy cơ hạ calci máu nghiêm trọng",
                    "management": "Thận trọng. Theo dõi calci máu chặt chẽ. Bổ sung calci nếu cần."
                },
                {
                    "drug": "Loop diuretics (furosemide, bumetanide)",
                    "mechanism": "Tăng bài tiết calci qua thận",
                    "effect": "Tăng nguy cơ hạ calci máu",
                    "management": "Thận trọng. Theo dõi calci máu. Bổ sung calci nếu cần."
                }
            ],
            "moderate": [
                {
                    "drug": "Nephrotoxic drugs (aminoglycosides, vancomycin, NSAIDs)",
                    "mechanism": "Tác dụng cộng dồn",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Thận trọng. Theo dõi chức năng thận chặt chẽ."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Hạ calci máu",
                "Suy thận nặng (CrCl <35)",
                "Dị ứng zoledronic acid hoặc bisphosphonates",
                "Mang thai (category D)"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình (CrCl 35-60) - thận trọng, có thể giảm liều",
                "Dùng với aminoglycosides, loop diuretics - tăng nguy cơ hạ calci máu",
                "Dùng với nephrotoxic drugs - tăng nguy cơ suy thận"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Category D - CHỐNG CHỈ ĐỊNH trong thai kỳ. Có nguy cơ dị tật thai nhi và ảnh hưởng đến sự phát triển xương của thai nhi.",
            "lactation": {
                "safety": "Compatible with monitoring",
                "details": "Zoledronic acid bài tiết vào sữa mẹ ở nồng độ thấp.",
                "recommendation": "Có thể dùng khi cho con bú với theo dõi."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi",
            "severe": "Không đổi",
            "notes": "Zoledronic acid không chuyển hóa qua gan. Không cần điều chỉnh liều ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Hạ calci máu nặng: co giật, tetany, rối loạn nhịp tim",
                "Hạ phospho máu nặng",
                "Suy thận cấp",
                "Sốt, ớn lạnh nặng"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hạ calci máu.",
            "treatment": [
                "Điều trị hạ calci máu: Calcium gluconate hoặc calcium chloride IV",
                "Điều trị hạ phospho máu: Bổ sung phosphate",
                "Điều trị suy thận cấp: Truyền dịch, có thể cần lọc máu",
                "Điều trị sốt: Acetaminophen, NSAIDs",
                "Theo dõi calci, phospho máu, chức năng thận liên tục"
            ],
            "monitoring": "Calci máu, phospho máu, chức năng thận, ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "iv": {
                "reconstitution": "Pha 4-5mg trong 100ml Normal saline hoặc D5W.",
                "infusion_rate": "Truyền CHẬM trong 15 phút. Không nhanh hơn.",
                "compatibility": ["Normal saline (0.9% NaCl)", "D5W"],
                "incompatibility": [
                    "Calcium (calcium gluconate, calcium chloride) - không trộn",
                    "Các cation khác - không trộn"
                ],
                "notes": "QUAN TRỌNG: 1) Truyền CHẬM trong 15 phút (không nhanh hơn), 2) Bổ sung calci và vitamin D trước và sau khi dùng, 3) Theo dõi chức năng thận chặt chẽ, 4) Theo dõi calci máu chặt chẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Zometa, Reclast (zoledronic acid)",
                "UpToDate - Zoledronic acid: Drug information",
                "ASCO Guidelines - Hypercalcemia of malignancy"
            ],
            "last_updated": "2025-02-05",
            "evidence_level": "A"
        },
        "risk_flags": {
            "high_alert": True,
            "narrow_therapeutic_index": False,
            "bleeding_risk": False,
            "organ_toxicity": ["renal"],
            "qt_prolongation": False,
            "hepatotoxicity": False,
            "nephrotoxicity": True,
            "requires_monitoring": ["Calcium Levels", "Phosphorus Levels", "RFT", "ECG"]
        },
        "guideline_tags": [
            "FDA Drug Label - Zometa, Reclast (zoledronic acid)",
            "ASCO Guidelines - Hypercalcemia of malignancy",
            "ISMP High Alert Medications - Emergency Medications"
        ]
    },
    
}

__all__ = ['ELECTROLYTES_DRUGS']





















