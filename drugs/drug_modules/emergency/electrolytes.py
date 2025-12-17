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
        }
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
    }
}

__all__ = ['ELECTROLYTES_DRUGS']



















