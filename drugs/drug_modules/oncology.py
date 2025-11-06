"""
Oncology Medications
Active module - contains all oncology drug data
"""

ONCOLOGY_DRUGS = {
"Cisplatin": {
        "group": "Oncology - Platinum Compound",
        "vietnamese_name": "Cisplatin, Platinol",
        "administration": ["IV"],
        "indications": [
            "Ung thư phổi (NSCLC, SCLC)",
            "Ung thư đầu cổ",
            "Ung thư tinh hoàn",
            "Ung thư buồng trứng",
            "Ung thư bàng quang",
            "Ung thư cổ tử cung"
        ],
        "contraindications": [
            "Dị ứng cisplatin",
            "Suy thận nặng (CrCl <60)",
            "Giảm thính lực",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "50-100mg/m² IV mỗi 3-4 tuần",
            "adult_weekly": "20-30mg/m² IV mỗi tuần",
            "adult_daily": "15-20mg/m² IV x 5 ngày (mỗi 3-4 tuần)",
            "notes": "Truyền với nước muối sinh lý (NaCl 0.9%), cần pre-hydration và post-hydration"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Không dùng hoặc giảm liều 50-75%"
        },
        "side_effects": [
            "Độc thận (phổ biến và nghiêm trọng - cần hydration)",
            "Nôn mửa nặng (thường xảy ra)",
            "Giảm thính lực (có thể vĩnh viễn)",
            "Độc thần kinh ngoại biên (tê bì, dị cảm)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Rụng tóc",
            "Hạ magne máu (phổ biến)",
            "Độc tim (hiếm)"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Furosemide: tăng độc thận",
            "Phenytoin: giảm nồng độ phenytoin",
            "Thuốc độc thận khác: tránh dùng đồng thời"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Cisplatin là hợp chất platinum gây liên kết chéo (cross-linking) DNA, đặc biệt giữa các base guanine và adenine. Liên kết chéo này ngăn chặn quá trình sao chép và phiên mã DNA, dẫn đến tổn thương DNA và chết tế bào. Cisplatin tạo thành các adduct với DNA, kích hoạt các con đường tín hiệu dẫn đến apoptosis. Tác dụng trên nhiều loại ung thư, đặc biệt hiệu quả với ung thư tinh hoàn, buồng trứng, phổi, đầu cổ. Có độc tính cao, đặc biệt là độc thận và độc thần kinh",
        "monitoring": [
            "Creatinine, BUN, điện giải trước và sau mỗi chu kỳ (độc thận là độc tính phổ biến nhất và nghiêm trọng)",
            "Lượng nước tiểu trong và sau truyền (đảm bảo >100ml/giờ)",
            "Chức năng thận (CrCl) trước mỗi chu kỳ - giảm liều nếu CrCl <60",
            "Thính lực (audiometry) trước và định kỳ - giảm thính lực có thể vĩnh viễn",
            "Dấu hiệu độc thần kinh ngoại biên: tê bì, dị cảm, yếu cơ (có thể tiến triển)",
            "Công thức máu (CBC) trước mỗi chu kỳ - myelosuppression",
            "Magne máu (hạ magne phổ biến, cần bổ sung)",
            "Dấu hiệu nôn mửa (nặng, cần antiemetic mạnh)",
            "Chức năng tim (ECG) nếu có triệu chứng (độc tim hiếm)"
        ],
        "precautions": [
            "PHẢI có pre-hydration và post-hydration đầy đủ (1-2L NS trước và sau) để giảm độc thận",
            "Truyền với NaCl 0.9% (không dùng D5W) để tăng thải trừ",
            "THEO DÕI CHẶT CHẼ chức năng thận - giảm liều hoặc ngừng nếu creatinine tăng",
            "Không dùng nếu CrCl <60 (trừ khi không có lựa chọn khác)",
            "Tránh dùng cùng aminoglycosides, furosemide (tăng độc thận)",
            "Theo dõi thính lực - ngừng nếu giảm thính lực tiến triển",
            "Dùng antiemetic mạnh (ondansetron, aprepitant) trước và sau truyền",
            "Bổ sung magne nếu hạ magne máu",
            "Theo dõi độc thần kinh - có thể tiến triển sau khi ngừng thuốc",
            "Thận trọng ở bệnh nhân cao tuổi, suy thận, suy tim (tăng nguy cơ độc tính)",
            "Không dùng trong thai kỳ (dị tật thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "30-100 giờ (rất dài, do gắn với protein và mô)",
            "onset": "Nhanh (vài giờ)",
            "duration": "Dài (tác dụng kéo dài)",
            "protein_binding": ">90% (rất cao)",
            "clearance": "Thận (chủ yếu, thải trừ qua nước tiểu), một phần gắn với mô (half-life dài)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch pha: bảo quản ở nhiệt độ phòng, dùng trong 20 giờ. Không đông lạnh",
        "black_box_warnings": "Độc thận có thể nghiêm trọng và tích lũy - cần hydration đầy đủ và theo dõi chức năng thận. Giảm thính lực có thể vĩnh viễn. Độc thần kinh ngoại biên có thể tiến triển. Myelosuppression có thể nặng. Chống chỉ định trong thai kỳ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides (gentamicin, tobramycin, amikacin)",
                    "mechanism": "Tăng độc thận tích lũy",
                    "effect": "Tăng nguy cơ suy thận cấp, độc thận nặng",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận chặt chẽ."
                },
                {
                    "drug": "Furosemide, Thiazides",
                    "mechanism": "Tăng độc thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng cùng. Nếu cần lợi tiểu, dùng mannitol hoặc theo dõi chặt chẽ."
                },
                {
                    "drug": "Thuốc độc thận khác (vancomycin, amphotericin B)",
                    "mechanism": "Tăng độc thận tích lũy",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận chặt chẽ."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin",
                    "mechanism": "Cisplatin có thể giảm hấp thu phenytoin",
                    "effect": "Giảm nồng độ phenytoin, tăng nguy cơ co giật",
                    "management": "Theo dõi nồng độ phenytoin. Tăng liều phenytoin nếu cần."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nguy cơ chảy máu",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Nephrotoxic drugs (NSAIDs, ACE inhibitors)",
                    "mechanism": "Tăng độc thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi chức năng thận."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Suy thận nặng (CrCl <60)",
                "Giảm thính lực nặng",
                "Có thai",
                "Đang cho con bú",
                "Dị ứng cisplatin hoặc platinum compounds",
                "Giảm bạch cầu/tiểu cầu nặng"
            ],
            "tương_đối": [
                "Suy thận nhẹ đến trung bình (CrCl 30-60) - giảm liều 25-50%",
                "Giảm thính lực nhẹ - theo dõi sát",
                "Suy gan nặng - thận trọng",
                "Bệnh tim - tăng nguy cơ độc tim",
                "Người cao tuổi - tăng nguy cơ độc tính",
                "Đã dùng cisplatin trước đây - tích lũy độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Cisplatin gây dị tật thai nhi, chậm phát triển, tử vong thai nhi. Cần test thai trước khi điều trị. Sử dụng biện pháp tránh thai hiệu quả trong và sau điều trị (ít nhất 6 tháng).",
            "lactation": {
                "safety": "Incompatible",
                "details": "Cisplatin bài tiết vào sữa mẹ. Không an toàn cho trẻ bú mẹ. Có thể gây độc tính nghiêm trọng ở trẻ.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng điều trị."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi hoặc giảm liều nhẹ",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Cisplatin chủ yếu thải trừ qua thận, không phụ thuộc nhiều vào chức năng gan. Tuy nhiên, suy gan có thể ảnh hưởng đến chuyển hóa và protein binding."
        },
        "overdose_management": {
            "symptoms": [
                "Suy thận cấp nặng (tăng creatinine, BUN, giảm lượng nước tiểu)",
                "Giảm thính lực nặng, điếc",
                "Độc thần kinh ngoại biên nặng (tê bì, mất cảm giác)",
                "Myelosuppression nặng (giảm bạch cầu, tiểu cầu)",
                "Nôn mửa nặng",
                "Hạ magne máu nặng",
                "Độc tim (rối loạn nhịp, suy tim)",
                "Suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Ngừng truyền ngay lập tức",
                "Hydration đầy đủ và mạnh (2-3L NS) để tăng thải trừ",
                "Theo dõi chức năng thận chặt chẽ (creatinine, BUN, lượng nước tiểu)",
                "Điều trị suy thận cấp: Truyền dịch, mannitol, furosemide (thận trọng)",
                "Lọc máu (hemodialysis) nếu suy thận nặng (hiệu quả hạn chế do gắn với protein)",
                "Bổ sung magne nếu hạ magne máu",
                "Điều trị myelosuppression: G-CSF, truyền máu/tiểu cầu nếu cần",
                "Điều trị nôn mửa: Antiemetics mạnh (ondansetron, aprepitant)",
                "Theo dõi thính lực (audiometry)",
                "Điều trị hỗ trợ: Chống nhiễm trùng, chống chảy máu"
            ],
            "monitoring": "Creatinine, BUN, lượng nước tiểu, công thức máu, thính lực, dấu hiệu độc thần kinh, magne máu, ECG, huyết áp"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A",
                "timing": "N/A"
            },
            "iv": {
                "reconstitution": "Pha với NS 0.9% để nồng độ 0.5-1mg/mL. Không dùng D5W (không ổn định)",
                "infusion_rate": "Truyền 50-100mg/m² trong 1-2 giờ. Không quá 100mg/phút",
                "compatibility": ["NS 0.9%"],
                "incompatibility": ["D5W", "Dung dịch chứa clorua", "Các thuốc khác"],
                "notes": "PHẢI có pre-hydration (1-2L NS trước) và post-hydration (1-2L NS sau) để giảm độc thận. Truyền với NS 0.9% để tăng thải trừ. Theo dõi lượng nước tiểu (đảm bảo >100ml/giờ)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Platinol (cisplatin)",
                "UpToDate - Cisplatin: Drug information",
                "NCCN Guidelines - Cancer treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Carboplatin": {
        "group": "Oncology - Platinum Compound",
        "vietnamese_name": "Carboplatin, Paraplatin",
        "administration": ["IV"],
        "indications": [
            "Ung thư buồng trứng",
            "Ung thư phổi (NSCLC)",
            "Ung thư đầu cổ",
            "Ung thư cổ tử cung",
            "Ung thư tinh hoàn"
        ],
        "contraindications": [
            "Dị ứng carboplatin hoặc platinum compounds",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_calvert": "AUC 4-6 mg/mL x min IV (tính theo GFR)",
            "adult_fixed": "300-400mg/m² IV mỗi 4 tuần",
            "adult_weekly": "100mg/m² IV mỗi tuần",
            "notes": "Dùng công thức Calvert: Dose (mg) = AUC x (GFR + 25). Ít độc thận hơn cisplatin"
        },
        "renal_adjustment": {
            "normal": "Tính theo GFR trong công thức Calvert",
            "30_60": "Giảm AUC hoặc liều 25-50%",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu (myelosuppression - phổ biến hơn cisplatin)",
            "Nôn mửa (ít hơn cisplatin)",
            "Độc thận (ít hơn cisplatin nhưng vẫn có)",
            "Rụng tóc (ít)",
            "Độc thần kinh (ít hơn cisplatin)",
            "Phản ứng dị ứng (hiếm)",
            "Hạ magne máu"
        ],
        "interactions": [
            "Aminoglycosides: tăng độc thận",
            "Thuốc độc thận: tránh dùng đồng thời",
            "Phenytoin: giảm nồng độ phenytoin"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Carboplatin là hợp chất platinum tương tự cisplatin, gây liên kết chéo DNA và ngăn chặn quá trình sao chép DNA. Cơ chế tác dụng giống cisplatin nhưng có cấu trúc hóa học khác (thay nhóm amin bằng cyclobutanedicarboxylate). Tác dụng trên nhiều loại ung thư tương tự cisplatin. Ưu điểm: ít độc thận và độc thần kinh hơn cisplatin, nhưng gây myelosuppression nhiều hơn. Liều được tính theo AUC (Area Under Curve) dựa trên GFR để đảm bảo hiệu quả và giảm độc tính",
        "monitoring": [
            "Creatinine, BUN, GFR trước mỗi chu kỳ (để tính liều theo công thức Calvert)",
            "Công thức máu (CBC) trước và sau mỗi chu kỳ - myelosuppression là độc tính phổ biến nhất",
            "Chức năng thận (CrCl) - cần để tính liều chính xác",
            "Dấu hiệu nhiễm trùng (do giảm bạch cầu)",
            "Dấu hiệu chảy máu (do giảm tiểu cầu)",
            "Dấu hiệu nôn mửa (ít hơn cisplatin nhưng vẫn có)",
            "Chức năng thận (độc thận ít hơn cisplatin nhưng vẫn cần theo dõi)",
            "Magne máu (hạ magne phổ biến)"
        ],
        "precautions": [
            "Dùng công thức Calvert để tính liều: Dose (mg) = AUC x (GFR + 25) - đảm bảo hiệu quả và giảm độc tính",
            "AUC thường dùng: 4-6 mg/mL x min (tùy phác đồ)",
            "THEO DÕI CHẶT CHẼ myelosuppression (giảm bạch cầu, tiểu cầu) - là độc tính phổ biến nhất",
            "Có thể cần hỗ trợ G-CSF nếu giảm bạch cầu nặng",
            "Có thể cần truyền tiểu cầu nếu giảm tiểu cầu nặng",
            "Ít cần hydration như cisplatin (ít độc thận hơn) nhưng vẫn nên truyền dịch đầy đủ",
            "Dùng antiemetic trước và sau truyền (ít nôn hơn cisplatin)",
            "Bổ sung magne nếu hạ magne máu",
            "Thận trọng ở bệnh nhân suy thận (cần điều chỉnh liều theo GFR)",
            "Theo dõi nhiễm trùng và chảy máu (do myelosuppression)",
            "Không dùng trong thai kỳ (dị tật thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "2-6 giờ (ngắn hơn cisplatin)",
            "onset": "Nhanh",
            "duration": "Dài (tác dụng kéo dài)",
            "protein_binding": "Thấp (khác với cisplatin)",
            "clearance": "Thận (chủ yếu, thải trừ nhanh hơn cisplatin)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Dung dịch pha: bảo quản ở nhiệt độ phòng, dùng trong 8 giờ. Không đông lạnh",
        "black_box_warnings": "Myelosuppression có thể nặng (giảm bạch cầu, tiểu cầu) - theo dõi chặt chẽ. Nhiễm trùng và chảy máu có thể xảy ra. Chống chỉ định trong thai kỳ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Aminoglycosides",
                    "mechanism": "Tăng độc thận",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận chặt chẽ."
                },
                {
                    "drug": "Thuốc độc thận khác",
                    "mechanism": "Tăng độc thận tích lũy",
                    "effect": "Tăng nguy cơ suy thận cấp",
                    "management": "Tránh dùng cùng. Nếu bắt buộc, giảm liều và theo dõi chức năng thận."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenytoin",
                    "mechanism": "Carboplatin có thể giảm nồng độ phenytoin",
                    "effect": "Giảm nồng độ phenytoin, tăng nguy cơ co giật",
                    "management": "Theo dõi nồng độ phenytoin. Tăng liều phenytoin nếu cần."
                },
                {
                    "drug": "Nephrotoxic drugs (NSAIDs, ACE inhibitors)",
                    "mechanism": "Tăng độc thận",
                    "effect": "Tăng nguy cơ suy thận",
                    "management": "Thận trọng. Theo dõi chức năng thận."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Có thai",
                "Đang cho con bú",
                "Dị ứng carboplatin hoặc platinum compounds",
                "Giảm bạch cầu/tiểu cầu nặng"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể, điều chỉnh công thức Calvert",
                "Suy gan nặng - thận trọng",
                "Người cao tuổi - tăng nguy cơ myelosuppression",
                "Đã dùng platinum compounds trước đây - tăng nguy cơ phản ứng dị ứng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Carboplatin gây dị tật thai nhi, chậm phát triển, tử vong thai nhi. Cần test thai trước khi điều trị. Sử dụng biện pháp tránh thai hiệu quả trong và sau điều trị (ít nhất 6 tháng).",
            "lactation": {
                "safety": "Incompatible",
                "details": "Carboplatin bài tiết vào sữa mẹ. Không an toàn cho trẻ bú mẹ. Có thể gây độc tính nghiêm trọng ở trẻ.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng điều trị."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Không đổi hoặc giảm liều nhẹ",
            "severe": "Thận trọng, có thể giảm liều",
            "notes": "Carboplatin chủ yếu thải trừ qua thận, không phụ thuộc nhiều vào chức năng gan. Liều được tính theo GFR (công thức Calvert)."
        },
        "overdose_management": {
            "symptoms": [
                "Myelosuppression nặng (giảm bạch cầu, tiểu cầu, thiếu máu)",
                "Nhiễm trùng (do giảm bạch cầu)",
                "Chảy máu (do giảm tiểu cầu)",
                "Suy thận cấp (ít hơn cisplatin nhưng vẫn có)",
                "Nôn mửa",
                "Hạ magne máu"
            ],
            "antidote": "Không có antidote đặc hiệu. Điều trị hỗ trợ",
            "treatment": [
                "Ngừng truyền ngay lập tức",
                "Theo dõi công thức máu chặt chẽ (myelosuppression là độc tính chính)",
                "Điều trị myelosuppression: G-CSF nếu giảm bạch cầu nặng, truyền tiểu cầu nếu giảm tiểu cầu nặng, truyền máu nếu thiếu máu",
                "Điều trị nhiễm trùng: Kháng sinh phổ rộng nếu có nhiễm trùng",
                "Điều trị chảy máu: Truyền tiểu cầu, hỗ trợ đông máu",
                "Theo dõi chức năng thận (creatinine, BUN, lượng nước tiểu)",
                "Bổ sung magne nếu hạ magne máu",
                "Điều trị nôn mửa: Antiemetics (ondansetron, aprepitant)",
                "Hydration đầy đủ để tăng thải trừ"
            ],
            "monitoring": "Công thức máu (CBC), chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, magne máu"
        },
        "reversal_agents": {
            "available": False,
            "agents": []
        },
        "administration_instructions": {
            "oral": {
                "with_food": "N/A",
                "timing": "N/A"
            },
            "iv": {
                "reconstitution": "Pha với D5W hoặc NS để nồng độ 0.5-2mg/mL",
                "infusion_rate": "Truyền trong 15-60 phút. Tốc độ phụ thuộc liều và phác đồ",
                "compatibility": ["D5W", "NS"],
                "incompatibility": ["Các thuốc khác"],
                "notes": "Dùng công thức Calvert để tính liều: Dose (mg) = AUC x (GFR + 25). Ít cần hydration như cisplatin nhưng vẫn nên truyền dịch đầy đủ. Theo dõi công thức máu chặt chẽ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Paraplatin (carboplatin)",
                "UpToDate - Carboplatin: Drug information",
                "NCCN Guidelines - Cancer treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Oxaliplatin": {
        "group": "Oncology - Platinum Compound",
        "vietnamese_name": "Oxaliplatin, Eloxatin",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (adjuvant và metastatic)",
            "Ung thư dạ dày",
            "Ung thư tụy"
        ],
        "contraindications": [
            "Dị ứng oxaliplatin hoặc platinum compounds",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Suy thận nặng (CrCl <30)",
            "Suy gan nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_folfox": "85mg/m² IV mỗi 2 tuần (phối hợp với 5-FU và leucovorin)",
            "adult_single": "85-130mg/m² IV mỗi 2-3 tuần",
            "notes": "Truyền 2-6 giờ. Tránh lạnh (độc lạnh - cold-induced neuropathy)"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều 25-50%"
        },
        "side_effects": [
            "Độc lạnh (cold-induced neuropathy - tê, cảm giác như bị điện giật khi tiếp xúc lạnh)",
            "Độc thần kinh ngoại biên (tê bì, mất cảm giác)",
            "Nôn mửa",
            "Tiêu chảy",
            "Giảm bạch cầu, tiểu cầu",
            "Phản ứng dị ứng (hiếm)",
            "Độc gan (tăng transaminase)"
        ],
        "interactions": [
            "Thuốc độc thận: thận trọng",
            "Phenytoin: có thể giảm nồng độ phenytoin"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Oxaliplatin là platinum compound, tạo ra các phức hợp platinum-DNA (cross-links), gây đứt gãy DNA và ngăn cản quá trình sao chép và phiên mã DNA. Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh, gây độc tế bào và chết tế bào ung thư. Oxaliplatin có cơ chế tương tự cisplatin và carboplatin nhưng có độc tính khác biệt (độc lạnh, độc thần kinh ngoại biên). Thuốc hiệu quả với ung thư đại trực tràng, đặc biệt khi dùng kết hợp với 5-FU và leucovorin (FOLFOX protocol)",
        "monitoring": [
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ",
            "Chức năng thận (creatinine, eGFR) trước mỗi chu kỳ",
            "Chức năng gan (ALT, AST) trước mỗi chu kỳ",
            "Dấu hiệu độc lạnh (tê, cảm giác như bị điện giật khi tiếp xúc lạnh) - phổ biến",
            "Dấu hiệu độc thần kinh ngoại biên (tê bì, mất cảm giác) - tích lũy",
            "Dấu hiệu phản ứng dị ứng (phát ban, khó thở) - hiếm",
            "Theo dõi extravasation khi truyền"
        ],
        "precautions": [
            "Tránh tiếp xúc với lạnh trong 3-7 ngày sau truyền (tránh độc lạnh)",
            "Không uống nước lạnh, không chạm vào đồ vật lạnh",
            "Mặc ấm, đeo găng tay, tất để tránh lạnh",
            "Theo dõi độc thần kinh ngoại biên (có thể tích lũy và kéo dài)",
            "Giảm liều hoặc ngừng nếu độc thần kinh nặng",
            "Giảm liều 25-50% nếu suy thận (CrCl <30-60)",
            "Truyền trong 2-6 giờ",
            "Có thể gây phản ứng dị ứng (hiếm - cần theo dõi)"
        ],
        "pharmacokinetics": {
            "half_life": "40 giờ (dài)",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Kéo dài (tích lũy)",
            "protein_binding": ">90%",
            "clearance": "Thận (thải trừ chủ yếu), không chuyển hóa"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": "Có thể gây độc lạnh nặng (cold-induced neuropathy) - tránh tiếp xúc với lạnh trong 3-7 ngày sau truyền. Có thể gây độc thần kinh ngoại biên tích lũy và kéo dài",
        "drug_interactions": {
            "major": [],
            "moderate": [
                {
                    "drug": "Thuốc độc thận (Aminoglycosides, Vancomycin, Amphotericin B)",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn làm tăng nguy cơ suy thận cấp.",
                    "effect": "Tăng nguy cơ suy thận cấp, độc thận nghiêm trọng",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi chức năng thận chặt chẽ. Duy trì đủ dịch."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "Oxaliplatin có thể giảm nồng độ phenytoin trong máu.",
                    "effect": "Giảm nồng độ phenytoin, giảm hiệu quả chống co giật",
                    "management": "Theo dõi nồng độ phenytoin. Có thể cần tăng liều phenytoin."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng oxaliplatin hoặc platinum compounds",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Đang cho con bú - chống chỉ định"
            ],
            "tương_đối": [
                "Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục",
                "Suy thận nặng (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ",
                "Suy gan nặng - thận trọng, có thể cần giảm liều",
                "Bệnh nhân có tiền sử độc thần kinh - tăng nguy cơ độc thần kinh nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Oxaliplatin gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Oxaliplatin bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng oxaliplatin. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Oxaliplatin không chuyển hóa qua gan, thải trừ chủ yếu qua thận. Tuy nhiên, suy gan có thể ảnh hưởng đến chức năng tổng thể và khả năng chịu đựng điều trị."
        },
        "overdose_management": {
            "symptoms": [
                "Độc lạnh nặng (tê, cảm giác như bị điện giật khi tiếp xúc lạnh)",
                "Độc thần kinh ngoại biên nặng (tê bì, mất cảm giác)",
                "Nôn mửa nặng",
                "Tiêu chảy nặng",
                "Giảm bạch cầu, tiểu cầu nặng",
                "Phản ứng dị ứng nặng"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay oxaliplatin",
                "Tránh tiếp xúc với lạnh (quan trọng)",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng thận, chức năng gan",
                "Điều trị nôn mửa (ondansetron, granisetron)",
                "Điều trị tiêu chảy (loperamide, bù dịch)",
                "Theo dõi và điều trị phản ứng dị ứng nếu có"
            ],
            "monitoring": "CBC, chức năng thận, chức năng gan, dấu hiệu độc lạnh, dấu hiệu độc thần kinh, dấu hiệu nhiễm trùng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không có dạng uống (chỉ có IV)"
            },
            "iv": {
                "reconstitution": "Pha với D5W (không dùng NS - có thể làm tăng độc tính) theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 2-6 giờ",
                "compatibility": ["D5W"],
                "incompatibility": ["NS", "NaCl"],
                "notes": "KHÔNG dùng NS hoặc NaCl để pha (có thể làm tăng độc tính). Chỉ dùng D5W. Truyền trong 2-6 giờ. Tránh lạnh khi truyền và sau truyền."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Oxaliplatin (Eloxatin)",
                "UpToDate - Oxaliplatin Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    "5-Fluorouracil": {
        "group": "Oncology - Antimetabolite",
        "vietnamese_name": "5-Fluorouracil, 5-FU, Fluorouracil",
        "administration": ["IV"],
        "indications": [
            "Ung thư đại trực tràng (adjuvant và metastatic)",
            "Ung thư dạ dày",
            "Ung thư đầu cổ",
            "Ung thư tụy",
            "Ung thư vú",
            "Ung thư da (topical)"
        ],
        "contraindications": [
            "Dị ứng 5-FU",
            "Thiếu hụt DPD (dihydropyrimidine dehydrogenase)",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_bolus": "400-600mg/m² IV bolus ngày 1, sau đó 400-600mg/m²/ngày x 4 ngày (mỗi 4 tuần)",
            "adult_infusion": "1000mg/m²/ngày IV infusion x 4-5 ngày (mỗi 4 tuần)",
            "adult_weekly": "500-600mg/m² IV mỗi tuần",
            "adult_topical": "5% cream bôi 2 lần/ngày",
            "notes": "Phối hợp với leucovorin để tăng hiệu quả. Cần test DPD nếu có thể"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều 25%",
            "under_30": "Thận trọng, giảm liều 25-50%"
        },
        "side_effects": [
            "Loét miệng (stomatitis - phổ biến)",
            "Tiêu chảy (phổ biến, có thể nặng)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Ban da",
            "Rụng tóc",
            "Độc tim (hiếm nhưng nguy hiểm)",
            "Rối loạn thần kinh (hiếm)",
            "Tăng bilirubin"
        ],
        "interactions": [
            "Leucovorin: tăng hiệu quả và độc tính",
            "Methotrexate: tăng độc tính",
            "Warfarin: tăng nguy cơ chảy máu",
            "Phenytoin: tăng nồng độ phenytoin"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "5-Fluorouracil (5-FU) là antimetabolite, chuyển hóa thành 5-fluorodeoxyuridine monophosphate (FdUMP) và 5-fluorouridine triphosphate (FUTP). FdUMP ức chế enzyme thymidylate synthase (TS), ngăn cản tổng hợp thymidine (thành phần DNA), dẫn đến thiếu hụt DNA và gây chết tế bào. FUTP tích hợp vào RNA, gây rối loạn tổng hợp protein. Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh (ung thư), gây độc tế bào. Hiệu quả tăng khi dùng kèm leucovorin (folinic acid) do tăng ức chế TS",
        "monitoring": [
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ (theo dõi giảm bạch cầu, tiểu cầu)",
            "Chức năng gan (ALT, AST, bilirubin) trước và trong điều trị",
            "Dấu hiệu loét miệng (stomatitis) - phổ biến, có thể nặng",
            "Dấu hiệu tiêu chảy - phổ biến, có thể nặng (cần điều trị sớm)",
            "Dấu hiệu độc tim (đau ngực, khó thở, rối loạn nhịp) - hiếm nhưng nguy hiểm",
            "Test DPD (dihydropyrimidine dehydrogenase) trước điều trị nếu có thể (thiếu hụt DPD gây độc tính nặng)",
            "Dấu hiệu nhiễm trùng (sốt, ớn lạnh) do giảm bạch cầu"
        ],
        "precautions": [
            "Test DPD trước điều trị nếu có thể (thiếu hụt DPD gây độc tính nặng, có thể tử vong)",
            "Giảm liều hoặc ngừng nếu có loét miệng nặng hoặc tiêu chảy nặng",
            "Dùng kèm leucovorin để tăng hiệu quả (nhưng cũng tăng độc tính)",
            "Theo dõi sát công thức máu (nguy cơ giảm bạch cầu, tiểu cầu cao)",
            "Tránh dùng nếu thiếu hụt DPD nặng",
            "Có thể gây độc tim (hiếm - cần theo dõi triệu chứng)",
            "Tương tác với warfarin (tăng nguy cơ chảy máu)",
            "Giảm liều 25-50% nếu suy thận"
        ],
        "pharmacokinetics": {
            "half_life": "10-20 phút (ngắn)",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "4-6 giờ (tác dụng sinh học)",
            "protein_binding": "Minimal",
            "clearance": "Gan (chuyển hóa qua DPD - dihydropyrimidine dehydrogenase), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": "Thiếu hụt DPD (dihydropyrimidine dehydrogenase) có thể gây độc tính nặng và tử vong. Nên test DPD trước điều trị nếu có thể. Theo dõi sát độc tính và ngừng ngay nếu có dấu hiệu độc tính nặng",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Methotrexate",
                    "mechanism": "Cả hai đều là antimetabolite, tác dụng cộng dồn làm tăng độc tính tủy xương và niêm mạc.",
                    "effect": "Tăng nguy cơ giảm bạch cầu, tiểu cầu, loét miệng, tiêu chảy nghiêm trọng",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi CBC và dấu hiệu độc tính chặt chẽ. Có thể cần giảm liều hoặc tránh dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Warfarin",
                    "mechanism": "5-FU có thể ức chế chuyển hóa warfarin, tăng nồng độ warfarin trong máu.",
                    "effect": "Tăng tác dụng chống đông, tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR chặt chẽ khi bắt đầu hoặc ngừng 5-FU. Có thể cần giảm liều warfarin."
                },
                {
                    "drug": "Phenytoin",
                    "mechanism": "5-FU có thể ức chế chuyển hóa phenytoin, tăng nồng độ phenytoin trong máu.",
                    "effect": "Tăng nồng độ phenytoin, tăng độc tính phenytoin",
                    "management": "Theo dõi nồng độ phenytoin và dấu hiệu độc tính. Có thể cần giảm liều phenytoin."
                }
            ],
            "minor": [
                {
                    "drug": "Leucovorin",
                    "mechanism": "Leucovorin tăng hiệu quả của 5-FU bằng cách tăng ức chế thymidylate synthase, nhưng cũng tăng độc tính.",
                    "effect": "Tăng hiệu quả và độc tính của 5-FU",
                    "management": "Dùng kèm để tăng hiệu quả, nhưng cần theo dõi độc tính chặt chẽ hơn."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng 5-FU",
                "Thiếu hụt DPD (dihydropyrimidine dehydrogenase) nặng - chống chỉ định tuyệt đối, có thể gây tử vong",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Đang cho con bú - chống chỉ định"
            ],
            "tương_đối": [
                "Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục",
                "Suy thận (CrCl <30) - giảm liều 25-50%, theo dõi chặt chẽ",
                "Suy gan - thận trọng, có thể cần giảm liều",
                "Bệnh nhân cao tuổi - tăng nguy cơ độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. 5-FU gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "5-FU bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng 5-FU. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "5-FU chuyển hóa chủ yếu qua gan (DPD - dihydropyrimidine dehydrogenase). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Loét miệng nặng (stomatitis)",
                "Tiêu chảy nặng, mất nước",
                "Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)",
                "Độc tim (hiếm)",
                "Rối loạn thần kinh (hiếm)",
                "Tăng bilirubin"
            ],
            "antidote": "Uridine triacetate (Vistogard) - antidote đặc hiệu cho quá liều 5-FU do thiếu hụt DPD",
            "treatment": [
                "Ngừng ngay 5-FU",
                "Nếu có thiếu hụt DPD và quá liều: dùng uridine triacetate (Vistogard) càng sớm càng tốt",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng gan, chức năng thận",
                "Điều trị loét miệng (súc miệng, thuốc giảm đau)",
                "Điều trị tiêu chảy (loperamide, bù dịch)",
                "Theo dõi và điều trị độc tim nếu có"
            ],
            "monitoring": "CBC mỗi ngày, chức năng gan, chức năng thận, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu độc tim"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Uridine triacetate (Vistogard)",
                    "indication": "Quá liều 5-FU do thiếu hụt DPD hoặc quá liều do lỗi dùng thuốc",
                    "dose": "10g PO x 3 lần/ngày x 5 ngày (bắt đầu càng sớm càng tốt)",
                    "notes": "Antidote đặc hiệu cho quá liều 5-FU. Hiệu quả nhất khi dùng trong vòng 96 giờ sau quá liều."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không có dạng uống (chỉ có IV và topical)"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Bolus: tiêm trực tiếp. Infusion: truyền trong 4-24 giờ tùy phác đồ",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Bolus: 400-600mg/m² tiêm trực tiếp. Infusion: 1000mg/m²/ngày truyền trong 4-24 giờ. Theo dõi extravasation."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - 5-Fluorouracil",
                "UpToDate - 5-Fluorouracil Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    "Methotrexate": {
        "group": "Oncology - Antimetabolite (Antifolate)",
        "vietnamese_name": "Methotrexate, MTX, Amethopterin",
        "administration": ["PO", "IV", "IM", "SC", "IT"],
        "indications": [
            "Bệnh bạch cầu cấp (leukemia)",
            "U lympho (lymphoma)",
            "U nguyên bào nuôi (choriocarcinoma)",
            "Ung thư đầu cổ",
            "Ung thư phổi",
            "Viêm khớp dạng thấp (liều thấp)",
            "Vẩy nến (liều thấp)"
        ],
        "contraindications": [
            "Dị ứng methotrexate",
            "Suy thận nặng",
            "Suy gan nặng",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Loét dạ dày tá tràng hoạt động",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_cancer_high": "50-250mg/m² IV (cần folinic acid rescue)",
            "adult_cancer_moderate": "10-50mg/m² IV/IM/PO",
            "adult_ra_psoriasis": "7.5-25mg PO x 1 lần/tuần",
            "adult_it": "12-15mg IT (theo dõi chặt chẽ)",
            "notes": "Liều cao (>50mg/m²) cần folinic acid rescue sau 24 giờ. Uống nhiều nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Không dùng hoặc giảm liều đáng kể, theo dõi sát"
        },
        "side_effects": [
            "Giảm bạch cầu, tiểu cầu, thiếu máu (myelosuppression - nghiêm trọng)",
            "Loét miệng (stomatitis)",
            "Tiêu chảy",
            "Độc gan (tăng transaminase, xơ gan)",
            "Độc phổi (viêm phổi kẽ - hiếm nhưng nguy hiểm)",
            "Độc thận (với liều cao)",
            "Rụng tóc",
            "Phát ban"
        ],
        "interactions": [
            "Probenecid: tăng độc tính methotrexate",
            "NSAID: tăng độc tính",
            "Penicillin: tăng độc tính",
            "Trimethoprim-Sulfamethoxazole: tăng độc tính",
            "Folinic acid: giải độc (rescue therapy)"
        ],
        "pregnancy": "X - Chống chỉ định tuyệt đối",
        "mechanism_of_action": "Antimetabolite, folic acid antagonist. Ức chế enzyme dihydrofolate reductase (DHFR), ngăn cản chuyển đổi dihydrofolate thành tetrahydrofolate (THF). THF cần thiết cho tổng hợp purine và thymidine (DNA, RNA). Ức chế tổng hợp DNA và RNA → ức chế sự phát triển và phân chia tế bào. Tác động mạnh lên tế bào phân chia nhanh (tế bào ung thư, tế bào miễn dịch, tế bào niêm mạc, tế bào tủy xương). Được dùng trong điều trị ung thư (liều cao), viêm khớp dạng thấp, vảy nến (liều thấp), và các bệnh tự miễn khác.",
        "monitoring": [
            "Công thức máu (WBC, platelet, hemoglobin) - giảm bạch cầu, giảm tiểu cầu, thiếu máu - QUAN TRỌNG",
            "Chức năng gan (ALT, AST, bilirubin, albumin) - độc tính gan, xơ gan",
            "Chức năng thận (creatinine, eGFR) - độc tính thận",
            "X-quang phổi (xơ phổi - hiếm nhưng nguy hiểm)",
            "Nồng độ methotrexate trong máu (nếu dùng liều cao)",
            "Dấu hiệu nhiễm trùng (do giảm bạch cầu)",
            "Dấu hiệu chảy máu (do giảm tiểu cầu)",
            "Dấu hiệu độc tính niêm mạc (loét miệng, tiêu chảy)"
        ],
        "precautions": [
            "Độc tính nghiêm trọng - phải theo dõi chặt chẽ",
            "PHẢI dùng folic acid để giảm độc tính (5-10mg/tuần, không dùng cùng ngày với methotrexate)",
            "Giảm bạch cầu, giảm tiểu cầu, thiếu máu - theo dõi công thức máu mỗi 1-4 tuần",
            "Độc tính gan - có thể gây xơ gan, kiểm tra chức năng gan định kỳ",
            "Độc tính thận - uống nhiều nước, kiểm tra chức năng thận",
            "Không dùng ở suy thận nặng",
            "Không dùng ở suy gan",
            "Tương tác với NSAID, aspirin → tăng nồng độ methotrexate, tăng độc tính",
            "Tương tác với trimethoprim-sulfamethoxazole → tăng độc tính",
            "Không dùng ở phụ nữ có thai (gây dị tật thai nhi) - dùng biện pháp tránh thai",
            "Liều thấp (viêm khớp, vảy nến): 7.5-25mg/tuần, liều cao (ung thư): 100mg/m² trở lên",
            "Ngừng nếu có dấu hiệu độc tính nghiêm trọng"
        ],
        "pharmacokinetics": {
            "half_life": "3-10 giờ (liều thấp), 8-15 giờ (liều cao)",
            "onset": "Vài giờ đến vài ngày",
            "duration": "Dài (nhiều ngày, tích lũy)",
            "protein_binding": "50-60%",
            "metabolism": "Một phần trong gan, một phần bị polyglutamylation trong tế bào (tích lũy)",
            "clearance": "Chủ yếu qua thận (80-90%), cần điều chỉnh thận"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (20-25°C), tránh ẩm, tránh ánh sáng. Dung dịch tiêm: bảo quản ở nhiệt độ phòng, tránh ánh sáng.",
        "black_box_warnings": "Độc tính nghiêm trọng, có thể tử vong. Giảm bạch cầu, giảm tiểu cầu, và thiếu máu có thể nặng. Độc tính gan có thể gây xơ gan. Độc tính thận có thể gây suy thận cấp. Phải theo dõi công thức máu và chức năng gan, thận định kỳ. Không dùng ở phụ nữ có thai (gây dị tật thai nhi).",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Probenecid",
                    "mechanism": "Probenecid ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate trong máu.",
                    "effect": "Tăng nồng độ methotrexate đáng kể, tăng độc tính (giảm bạch cầu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, giảm liều methotrexate 50-75% và theo dõi chặt chẽ công thức máu, chức năng gan, thận."
                },
                {
                    "drug": "NSAID (Ibuprofen, Naproxen, Diclofenac, Aspirin)",
                    "mechanism": "NSAID ức chế bài tiết ống thận của methotrexate, làm giảm thải trừ và tăng nồng độ methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính nghiêm trọng (giảm bạch cầu, độc gan, độc thận)",
                    "management": "TRÁNH DÙNG đồng thời, đặc biệt với liều cao methotrexate. Nếu dùng liều thấp (RA, psoriasis), thận trọng và theo dõi chặt chẽ. Có thể dùng acetaminophen thay thế."
                },
                {
                    "drug": "Trimethoprim-Sulfamethoxazole",
                    "mechanism": "Cả hai đều là folic acid antagonists, tác dụng cộng dồn làm tăng độc tính.",
                    "effect": "Tăng độc tính nghiêm trọng (giảm bạch cầu, thiếu máu megaloblastic)",
                    "management": "TRÁNH DÙNG đồng thời. Nếu bắt buộc, theo dõi chặt chẽ công thức máu và bổ sung folic acid."
                }
            ],
            "moderate": [
                {
                    "drug": "Penicillin, Ampicillin",
                    "mechanism": "Penicillin có thể ức chế bài tiết ống thận của methotrexate.",
                    "effect": "Tăng nồng độ methotrexate, tăng độc tính",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi công thức máu và chức năng gan, thận."
                },
                {
                    "drug": "Folic acid (nếu dùng cùng ngày)",
                    "mechanism": "Folic acid đối kháng tác dụng của methotrexate, giảm hiệu quả điều trị.",
                    "effect": "Giảm hiệu quả điều trị methotrexate",
                    "management": "KHÔNG dùng folic acid cùng ngày với methotrexate. Dùng folic acid vào ngày khác (5-10mg/tuần) để giảm độc tính mà không giảm hiệu quả."
                }
            ],
            "minor": [
                {
                    "drug": "Acetaminophen",
                    "mechanism": "Acetaminophen có thể tăng độc tính gan khi dùng với methotrexate.",
                    "effect": "Tăng nguy cơ độc gan",
                    "management": "Thận trọng, tránh dùng liều cao acetaminophen. Theo dõi chức năng gan."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng methotrexate",
                "Có thai (gây dị tật thai nhi, sảy thai)",
                "Đang cho con bú",
                "Suy thận nặng (CrCl <30)",
                "Suy gan nặng",
                "Giảm bạch cầu/tiểu cầu nặng",
                "Loét dạ dày tá tràng hoạt động"
            ],
            "tương_đối": [
                "Suy thận (CrCl 30-60: giảm liều 25-50%)",
                "Suy gan nhẹ-trung bình (theo dõi chức năng gan)",
                "Nhiễm trùng đang hoạt động (ức chế miễn dịch)",
                "Bệnh phổi mạn tính (nguy cơ xơ phổi)"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "X",
            "pregnancy_details": "Methotrexate chống chỉ định tuyệt đối trong thai kỳ. Gây dị tật thai nhi nghiêm trọng (dị tật hệ thần kinh, sọ mặt, chi), sảy thai, và tử vong thai nhi. Phụ nữ trong độ tuổi sinh đẻ PHẢI dùng biện pháp tránh thai hiệu quả trong và sau khi dùng methotrexate ít nhất 3 tháng (hoặc 1 chu kỳ ovulatory sau liều cuối). Nam giới cũng nên dùng biện pháp tránh thai trong và sau khi dùng ít nhất 3 tháng.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Methotrexate bài tiết vào sữa mẹ ở nồng độ đáng kể. Chống chỉ định khi cho con bú. Có thể gây độc tính nghiêm trọng cho trẻ bú mẹ (giảm bạch cầu, độc gan, độc thận).",
                "recommendation": "KHÔNG dùng khi cho con bú. Ngừng cho con bú hoặc ngừng methotrexate."
            }
        },
        "hepatic_adjustment": {
            "mild": "Thận trọng, theo dõi chức năng gan. Có thể cần giảm liều nhẹ.",
            "moderate": "Giảm liều 25-50%. Theo dõi chức năng gan chặt chẽ.",
            "severe": "Chống chỉ định hoặc thận trọng tối đa. Nguy cơ độc gan cao, có thể gây suy gan.",
            "notes": "Methotrexate chuyển hóa một phần qua gan và tích lũy trong gan. Suy gan làm tăng nguy cơ độc tính gan, xơ gan. Theo dõi ALT, AST, bilirubin, albumin định kỳ. Ngừng nếu có dấu hiệu độc gan."
        },
        "overdose_management": {
            "symptoms": [
                "Giảm bạch cầu, giảm tiểu cầu, thiếu máu nặng (myelosuppression)",
                "Loét miệng, tiêu chảy nặng (mucositis)",
                "Độc gan (tăng ALT/AST, vàng da, suy gan)",
                "Độc thận (tăng creatinine, suy thận cấp)",
                "Độc phổi (khó thở, xơ phổi)",
                "Nhiễm trùng nặng (do giảm bạch cầu)",
                "Chảy máu (do giảm tiểu cầu)"
            ],
            "antidote": "Folinic acid (leucovorin) - giải độc methotrexate. Dùng càng sớm càng tốt, tốt nhất trong vòng 24 giờ.",
            "treatment": [
                "Ngừng methotrexate ngay lập tức",
                "Dùng folinic acid (leucovorin) ngay: 10-15mg/m² mỗi 6 giờ cho đến khi nồng độ methotrexate <0.05 micromol/L. Liều folinic acid = liều methotrexate hoặc cao hơn.",
                "Tăng cường thủy phân (uống nhiều nước, truyền dịch) để tăng thải trừ qua thận",
                "Kiềm hóa nước tiểu (sodium bicarbonate) để tăng thải trừ methotrexate",
                "Theo dõi công thức máu, chức năng gan, thận chặt chẽ",
                "Điều trị nhiễm trùng nếu có (kháng sinh phổ rộng)",
                "Truyền tiểu cầu, hồng cầu nếu cần",
                "Theo dõi nồng độ methotrexate trong máu",
                "Có thể cần lọc máu (hemodialysis) nếu suy thận nặng"
            ],
            "monitoring": "Công thức máu mỗi ngày, chức năng gan/thận, nồng độ methotrexate, dấu hiệu nhiễm trùng, chảy máu. Theo dõi ít nhất 1-2 tuần."
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Folinic acid (Leucovorin)",
                    "mechanism": "Folinic acid là dạng hoạt động của folic acid, bỏ qua bước ức chế bởi methotrexate, cung cấp tetrahydrofolate cho tế bào bình thường.",
                    "indication": "Quá liều methotrexate, đặc biệt liều cao (>50mg/m²)",
                    "dosage": "10-15mg/m² IV/PO mỗi 6 giờ cho đến khi nồng độ methotrexate <0.05 micromol/L. Liều folinic acid thường bằng hoặc cao hơn liều methotrexate.",
                    "notes": "Dùng càng sớm càng tốt, tốt nhất trong vòng 24 giờ sau liều methotrexate. Tiếp tục cho đến khi nồng độ methotrexate về bình thường."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn. Uống với thức ăn có thể giảm kích ứng dạ dày.",
                "timing": "Liều thấp (RA, psoriasis): uống 1 lần/tuần vào cùng ngày mỗi tuần. Liều cao (ung thư): theo chỉ định. Uống nhiều nước (2-3L/ngày) để tăng thải trừ qua thận."
            },
            "iv": {
                "reconstitution": "Pha với D5W hoặc Normal saline theo hướng dẫn. Liều cao cần pha loãng đúng cách.",
                "infusion_rate": "Truyền trong 30-60 phút (liều thấp) hoặc theo chỉ định (liều cao). Không truyền nhanh.",
                "compatibility": ["D5W", "Normal saline"],
                "incompatibility": ["Không trộn với các thuốc khác"],
                "notes": "Liều cao (>50mg/m²) cần folinic acid rescue sau 24 giờ. Uống nhiều nước hoặc truyền dịch để tăng thải trừ. Kiềm hóa nước tiểu nếu cần."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Methotrexate (Trexall, Rheumatrex)",
                "American College of Rheumatology Guidelines - Methotrexate use",
                "UpToDate - Methotrexate drug information",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th ed)",
                "Lexicomp Online - Methotrexate Monograph"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "A - Dựa trên FDA drug labels, ACR guidelines, và dữ liệu lâm sàng từ nhiều nguồn"
        }
    },
    "Cyclophosphamide": {
        "group": "Oncology - Alkylating Agent",
        "vietnamese_name": "Cyclophosphamide, Endoxan, Cytoxan",
        "administration": ["PO", "IV"],
        "indications": [
            "U lympho (lymphoma)",
            "Bệnh bạch cầu",
            "Ung thư vú",
            "Ung thư buồng trứng",
            "Bệnh tự miễn (lupus, vasculitis, liều thấp)"
        ],
        "contraindications": [
            "Dị ứng cyclophosphamide",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Suy thận nặng",
            "Suy gan nặng",
            "Viêm bàng quang chảy máu",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_cancer_high": "500-1000mg/m² IV mỗi 3-4 tuần",
            "adult_cancer_moderate": "50-200mg/m² PO/IV mỗi ngày",
            "adult_autoimmune": "1-2mg/kg PO mỗi ngày hoặc 500-750mg/m² IV mỗi tháng",
            "notes": "Uống nhiều nước (2-3L/ngày) để phòng viêm bàng quang. Có thể dùng mesna để bảo vệ"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Giảm liều 25-50%",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Viêm bàng quang chảy máu (hemorrhagic cystitis - phổ biến, nguy hiểm)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Buồn nôn, nôn",
            "Rụng tóc",
            "Vô sinh (nam và nữ)",
            "Ung thư thứ phát (hiếm)",
            "Độc tim (với liều cao)",
            "Hội chứng lysis khối u"
        ],
        "interactions": [
            "Allopurinol: tăng độc tính",
            "Phenobarbital: tăng chuyển hóa",
            "Succinylcholine: kéo dài tác dụng",
            "Mesna: bảo vệ chống viêm bàng quang"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Cyclophosphamide là prodrug alkylating agent, được chuyển hóa ở gan thành các chất hoạt động (phosphoramide mustard và acrolein). Phosphoramide mustard gây liên kết chéo DNA (cross-linking), ngăn chặn quá trình sao chép DNA và dẫn đến tổn thương DNA, chết tế bào. Acrolein gây độc cho bàng quang (hemorrhagic cystitis). Tác dụng: điều trị ung thư (lymphoma, leukemia, ung thư vú, buồng trứng) và bệnh tự miễn (lupus, vasculitis) ở liều thấp hơn. Có tác dụng ức chế miễn dịch mạnh",
        "monitoring": [
            "Công thức máu (CBC) trước và sau mỗi chu kỳ - myelosuppression (giảm bạch cầu, tiểu cầu)",
            "Dấu hiệu viêm bàng quang chảy máu: tiểu máu, đau khi tiểu, tiểu nhiều lần (RẤT QUAN TRỌNG)",
            "Lượng nước tiểu (đảm bảo >2-3L/ngày để phòng viêm bàng quang)",
            "Chức năng thận (creatinine, BUN) - điều chỉnh liều khi suy thận",
            "Chức năng gan (ALT, AST) - cần gan hoạt động để chuyển hóa thành chất hoạt động",
            "Dấu hiệu nhiễm trùng (do giảm bạch cầu)",
            "Dấu hiệu chảy máu (do giảm tiểu cầu)",
            "Dấu hiệu hội chứng lysis khối u: tăng uric acid, kali, phosphate (với liều cao)",
            "Dấu hiệu độc tim: nhịp tim nhanh, suy tim (với liều cao)",
            "Uric acid (tăng nguy cơ gout, hội chứng lysis khối u)"
        ],
        "precautions": [
            "UỐNG NHIỀU NƯỚC (2-3L/ngày) để phòng viêm bàng quang chảy máu - đây là độc tính phổ biến và nguy hiểm",
            "NGỪNG NGAY nếu có tiểu máu hoặc dấu hiệu viêm bàng quang",
            "Có thể dùng mesna (sodium 2-mercaptoethanesulfonate) để bảo vệ bàng quang khi dùng liều cao",
            "Mesna liều: 20% liều cyclophosphamide, dùng trước, 4 giờ, và 8 giờ sau cyclophosphamide",
            "Theo dõi chặt chẽ myelosuppression - có thể cần hỗ trợ G-CSF hoặc truyền máu",
            "Dùng allopurinol để phòng tăng uric acid (hội chứng lysis khối u)",
            "Thận trọng ở bệnh nhân suy gan (cần gan để chuyển hóa thành chất hoạt động)",
            "Thận trọng ở bệnh nhân suy thận (giảm liều)",
            "Có thể gây vô sinh (nam và nữ) - tư vấn trước khi điều trị",
            "Có thể gây ung thư thứ phát (hiếm, với liều cao)",
            "Theo dõi nhiễm trùng và chảy máu (do myelosuppression)",
            "Không dùng trong thai kỳ (dị tật thai nhi)"
        ],
        "pharmacokinetics": {
            "half_life": "3-12 giờ (phụ thuộc vào chuyển hóa)",
            "onset": "Chậm (cần chuyển hóa thành chất hoạt động)",
            "duration": "Dài (tác dụng kéo dài)",
            "protein_binding": "10-20% (thấp)",
            "clearance": "Gan (chuyển hóa thành chất hoạt động qua CYP2B6, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ẩm, tránh ánh sáng. Viên nang: bảo quản ở nhiệt độ phòng. Dung dịch IV: bảo quản ở nhiệt độ phòng, dùng trong 24 giờ. Không đông lạnh",
        "black_box_warnings": "Viêm bàng quang chảy máu có thể nghiêm trọng - cần uống nhiều nước (2-3L/ngày) và dùng mesna khi cần. Myelosuppression có thể nặng, dẫn đến nhiễm trùng và chảy máu. Có thể gây vô sinh vĩnh viễn. Có thể gây ung thư thứ phát. Chống chỉ định trong thai kỳ",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Allopurinol",
                    "mechanism": "Tăng độc tính của cyclophosphamide",
                    "effect": "Tăng nguy cơ độc tính, đặc biệt myelosuppression",
                    "management": "Thận trọng. Giảm liều cyclophosphamide hoặc ngừng allopurinol nếu có thể."
                },
                {
                    "drug": "Phenobarbital, Rifampin",
                    "mechanism": "Cảm ứng CYP450, tăng chuyển hóa cyclophosphamide",
                    "effect": "Tăng chuyển hóa thành chất hoạt động, tăng độc tính",
                    "management": "Thận trọng. Theo dõi độc tính chặt chẽ. Có thể cần điều chỉnh liều."
                }
            ],
            "moderate": [
                {
                    "drug": "Succinylcholine",
                    "mechanism": "Cyclophosphamide ức chế cholinesterase",
                    "effect": "Kéo dài tác dụng succinylcholine",
                    "management": "Thận trọng khi gây mê. Giảm liều succinylcholine hoặc dùng thuốc khác."
                },
                {
                    "drug": "Warfarin",
                    "mechanism": "Có thể tăng nguy cơ chảy máu",
                    "effect": "Tăng INR, tăng nguy cơ chảy máu",
                    "management": "Theo dõi INR thường xuyên. Điều chỉnh liều warfarin nếu cần."
                }
            ],
            "minor": [
                {
                    "drug": "Mesna",
                    "mechanism": "Bảo vệ chống viêm bàng quang",
                    "effect": "Giảm nguy cơ viêm bàng quang chảy máu",
                    "management": "Dùng kèm khi dùng liều cao. Liều: 20% liều cyclophosphamide."
                }
            ]
        },
        "contraindications": {
            "tuyệt_đối": [
                "Viêm bàng quang chảy máu hoạt động",
                "Có thai",
                "Đang cho con bú",
                "Dị ứng cyclophosphamide",
                "Giảm bạch cầu/tiểu cầu nặng"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể",
                "Suy gan nặng - thận trọng (cần gan để chuyển hóa thành chất hoạt động)",
                "Nhiễm trùng hoạt động - tăng nguy cơ",
                "Bệnh tim - tăng nguy cơ độc tim",
                "Người cao tuổi - tăng nguy cơ độc tính",
                "Đã dùng cyclophosphamide trước đây - tích lũy độc tính"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Cyclophosphamide gây dị tật thai nhi, chậm phát triển, tử vong thai nhi. Cần test thai trước khi điều trị. Sử dụng biện pháp tránh thai hiệu quả trong và sau điều trị (ít nhất 6-12 tháng). Có thể gây vô sinh vĩnh viễn (nam và nữ).",
            "lactation": {
                "safety": "Incompatible",
                "details": "Cyclophosphamide bài tiết vào sữa mẹ. Không an toàn cho trẻ bú mẹ. Có thể gây độc tính nghiêm trọng, myelosuppression ở trẻ.",
                "recommendation": "Không dùng khi cho con bú. Ngừng cho con bú hoặc ngừng điều trị."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể giảm liều nhẹ",
            "severe": "Tránh dùng hoặc dùng liều rất thấp dưới sự giám sát chặt chẽ",
            "notes": "Cyclophosphamide là prodrug, cần gan để chuyển hóa thành chất hoạt động (phosphoramide mustard). Suy gan làm giảm chuyển hóa, giảm hiệu quả. Tuy nhiên, suy gan nặng có thể làm giảm clearance, tăng độc tính."
        },
        "overdose_management": {
            "symptoms": [
                "Viêm bàng quang chảy máu nặng (tiểu máu, đau bụng dưới)",
                "Myelosuppression nặng (giảm bạch cầu, tiểu cầu, thiếu máu)",
                "Nhiễm trùng nặng (do giảm bạch cầu)",
                "Chảy máu (do giảm tiểu cầu)",
                "Hội chứng lysis khối u (tăng uric acid, kali, phosphate)",
                "Độc tim (rối loạn nhịp, suy tim)",
                "Suy thận cấp",
                "Suy hô hấp"
            ],
            "antidote": "Không có antidote đặc hiệu. Mesna không phải antidote nhưng có thể giúp bảo vệ bàng quang",
            "treatment": [
                "Ngừng thuốc ngay lập tức",
                "UỐNG NHIỀU NƯỚC (3-4L/ngày) hoặc truyền dịch đầy đủ để phòng viêm bàng quang",
                "Mesna ngay lập tức (20% liều cyclophosphamide) nếu chưa dùng, sau đó mỗi 4 giờ",
                "Theo dõi sát nước tiểu (dấu hiệu viêm bàng quang chảy máu)",
                "Điều trị viêm bàng quang: Mesna, truyền dịch, có thể cần đặt catheter",
                "Theo dõi công thức máu chặt chẽ",
                "Điều trị myelosuppression: G-CSF, truyền máu/tiểu cầu nếu cần",
                "Điều trị nhiễm trùng: Kháng sinh phổ rộng",
                "Điều trị hội chứng lysis khối u: Allopurinol, hydration, rasburicase nếu cần",
                "Theo dõi chức năng thận, điện giải",
                "Điều trị hỗ trợ: Chống nôn, truyền dịch, theo dõi tim mạch"
            ],
            "monitoring": "Nước tiểu (hematuria), công thức máu (CBC), chức năng thận, uric acid, kali, phosphate, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, ECG"
        },
        "reversal_agents": {
            "available": False,
            "agents": ["Mesna (bảo vệ bàng quang, không phải antidote)"]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể dùng với hoặc không có thức ăn. Dùng với thức ăn có thể giảm kích ứng dạ dày",
                "timing": "Uống nhiều nước (2-3L/ngày) trước, trong và sau khi uống để phòng viêm bàng quang. Uống vào buổi sáng để tăng lượng nước tiểu ban ngày."
            },
            "iv": {
                "reconstitution": "Pha với D5W hoặc NS để nồng độ 1-20mg/mL",
                "infusion_rate": "Truyền trong 30-60 phút. Tốc độ phụ thuộc liều",
                "compatibility": ["D5W", "NS"],
                "incompatibility": ["Các thuốc khác"],
                "notes": "UỐNG NHIỀU NƯỚC (2-3L/ngày) trước, trong và sau truyền để phòng viêm bàng quang. Dùng mesna khi dùng liều cao (20% liều cyclophosphamide, dùng trước, 4 giờ, và 8 giờ sau). Theo dõi lượng nước tiểu (đảm bảo >2L/ngày)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Cytoxan (cyclophosphamide)",
                "UpToDate - Cyclophosphamide: Drug information",
                "NCCN Guidelines - Cancer treatment",
                "Goodman & Gilman's The Pharmacological Basis of Therapeutics"
            ],
            "last_updated": "2024-12-19",
            "evidence_level": "High - Multiple RCTs and systematic reviews"
        }
    },
    "Ifosfamide": {
        "group": "Oncology - Alkylating Agent",
        "vietnamese_name": "Ifosfamide, Ifex",
        "administration": ["IV"],
        "indications": [
            "Ung thư tinh hoàn",
            "U lympho",
            "Sarcoma mô mềm",
            "Ung thư xương",
            "Ung thư phổi (một số loại)"
        ],
        "contraindications": [
            "Dị ứng ifosfamide",
            "Suy thận nặng",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Viêm bàng quang chảy máu",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "1200-2000mg/m² IV x 3-5 ngày (mỗi 3-4 tuần)",
            "adult_high": "3000-5000mg/m² IV x 1-3 ngày (với mesna)",
            "notes": "Luôn dùng kèm mesna để bảo vệ bàng quang. Uống nhiều nước"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, giảm liều 25-50%",
            "under_30": "Thận trọng, giảm liều đáng kể"
        },
        "side_effects": [
            "Viêm bàng quang chảy máu (nguy hiểm - cần mesna)",
            "Độc thần kinh trung ương (lú lẫn, co giật - với liều cao)",
            "Giảm bạch cầu, tiểu cầu",
            "Buồn nôn, nôn",
            "Rụng tóc",
            "Độc thận",
            "Vô sinh"
        ],
        "interactions": [
            "Mesna: bảo vệ chống viêm bàng quang (bắt buộc)",
            "Phenobarbital: tăng chuyển hóa",
            "Cisplatin: tăng độc thận"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Ifosfamide là alkylating agent (nitrogen mustard), chuyển hóa trong gan thành các chất hoạt động (4-hydroxyifosfamide, aldophosphamide, isophosphoramide mustard). Các chất này gắn vào DNA, tạo ra cross-links DNA-DNA và DNA-protein, gây đứt gãy DNA và ngăn cản quá trình sao chép DNA. Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh, gây độc tế bào và chết tế bào ung thư. Acrolein (sản phẩm chuyển hóa) gây độc bàng quang (hemorrhagic cystitis), cần dùng kèm mesna để bảo vệ",
        "monitoring": [
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ và giữa các chu kỳ",
            "Chức năng thận (creatinine, eGFR) trước mỗi chu kỳ",
            "Chức năng gan (ALT, AST, bilirubin) trước mỗi chu kỳ",
            "Nước tiểu (hematuria, proteinuria) - theo dõi viêm bàng quang chảy máu",
            "Dấu hiệu viêm bàng quang chảy máu (đái máu, đau bụng dưới) - nguy hiểm",
            "Dấu hiệu độc thần kinh trung ương (lú lẫn, co giật, hôn mê) - với liều cao",
            "Điện giải (Na, K) nếu có độc thần kinh trung ương",
            "Theo dõi lượng nước tiểu (đảm bảo >100ml/giờ)"
        ],
        "precautions": [
            "LUÔN dùng kèm mesna để bảo vệ bàng quang (bắt buộc)",
            "Uống nhiều nước và truyền dịch đầy đủ (đảm bảo >2L/ngày)",
            "Theo dõi sát nước tiểu (dấu hiệu viêm bàng quang chảy máu)",
            "Ngừng ngay nếu có viêm bàng quang chảy máu nặng",
            "Có thể gây độc thần kinh trung ương với liều cao (lú lẫn, co giật - cần điều trị)",
            "Giảm liều 25-50% nếu suy thận (CrCl 30-60)",
            "Tránh dùng với các thuốc độc thận (cisplatin)",
            "Có thể gây vô sinh (cần tư vấn trước điều trị)",
            "Mesna phải được dùng đúng liều và thời điểm (trước, trong, và sau ifosfamide)"
        ],
        "pharmacokinetics": {
            "half_life": "3-15 giờ (tùy thuộc vào liều)",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Kéo dài (tích lũy)",
            "protein_binding": "<20%",
            "clearance": "Gan (chuyển hóa chủ yếu qua CYP2B6, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": "Có thể gây viêm bàng quang chảy máu nặng và nguy hiểm tính mạng. LUÔN phải dùng kèm mesna để bảo vệ bàng quang. Có thể gây độc thần kinh trung ương nặng (lú lẫn, co giật, hôn mê) với liều cao",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cisplatin",
                    "mechanism": "Cả hai đều có độc tính thận, tác dụng cộng dồn làm tăng nguy cơ suy thận cấp và độc thận nghiêm trọng.",
                    "effect": "Tăng nguy cơ suy thận cấp, độc thận nghiêm trọng",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi chức năng thận chặt chẽ. Duy trì đủ dịch. Có thể cần giảm liều hoặc tránh dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Phenobarbital",
                    "mechanism": "Phenobarbital cảm ứng CYP450, làm tăng chuyển hóa ifosfamide, giảm nồng độ ifosfamide trong máu.",
                    "effect": "Giảm nồng độ ifosfamide, giảm hiệu quả điều trị",
                    "management": "Theo dõi đáp ứng điều trị. Có thể cần tăng liều ifosfamide."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng ifosfamide",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Đang cho con bú - chống chỉ định",
                "Viêm bàng quang chảy máu nặng - chống chỉ định cho đến khi hồi phục"
            ],
            "tương_đối": [
                "Suy thận nặng (CrCl <30) - giảm liều đáng kể, theo dõi chặt chẽ",
                "Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục",
                "Suy gan - thận trọng, có thể cần giảm liều",
                "Bệnh nhân có tiền sử độc thần kinh trung ương - tăng nguy cơ độc thần kinh nặng"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Ifosfamide gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Ifosfamide bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng ifosfamide. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Ifosfamide chuyển hóa chủ yếu qua gan (CYP2B6, CYP3A4). Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ."
        },
        "overdose_management": {
            "symptoms": [
                "Viêm bàng quang chảy máu nặng (đái máu, đau bụng dưới)",
                "Độc thần kinh trung ương nặng (lú lẫn, co giật, hôn mê)",
                "Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)",
                "Suy thận cấp",
                "Nôn mửa nặng"
            ],
            "antidote": "Mesna (nếu chưa dùng) - bảo vệ bàng quang",
            "treatment": [
                "Ngừng ngay ifosfamide",
                "Nếu chưa dùng mesna: dùng mesna ngay để bảo vệ bàng quang",
                "Truyền dịch đầy đủ (đảm bảo >2L/ngày, >100ml/giờ)",
                "Theo dõi nước tiểu (hematuria, proteinuria)",
                "Điều trị viêm bàng quang chảy máu nếu có (mesna, truyền dịch, có thể cần đặt ống thông)",
                "Điều trị độc thần kinh trung ương nếu có (methylene blue, thiamine, có thể cần điều trị co giật)",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng thận, chức năng gan"
            ],
            "monitoring": "CBC, chức năng thận, chức năng gan, nước tiểu (hematuria), dấu hiệu độc thần kinh trung ương, lượng nước tiểu"
        },
        "reversal_agents": {
            "available": True,
            "agents": [
                {
                    "name": "Mesna",
                    "indication": "Bảo vệ bàng quang chống viêm bàng quang chảy máu do ifosfamide",
                    "dose": "20% liều ifosfamide IV trước, trong, và sau ifosfamide (tổng 60% liều ifosfamide)",
                    "notes": "Bắt buộc phải dùng kèm với ifosfamide. Mesna gắn với acrolein (sản phẩm chuyển hóa độc của ifosfamide) trong nước tiểu, bảo vệ bàng quang."
                }
            ]
        },
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không có dạng uống (chỉ có IV)"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 1-4 giờ",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "1200-2000mg/m² IV x 3-5 ngày (mỗi 3-4 tuần). LUÔN dùng kèm mesna (20% liều ifosfamide IV trước, trong, và sau ifosfamide). Truyền dịch đầy đủ (đảm bảo >2L/ngày, >100ml/giờ). Truyền trong 1-4 giờ."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Ifosfamide (Ifex)",
                "UpToDate - Ifosfamide Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    "Doxorubicin": {
        "group": "Oncology - Anthracycline",
        "vietnamese_name": "Doxorubicin, Adriamycin",
        "administration": ["IV"],
        "indications": [
            "Ung thư vú",
            "U lympho",
            "Bệnh bạch cầu",
            "Sarcoma mô mềm",
            "Ung thư buồng trứng",
            "Ung thư phổi (SCLC)"
        ],
        "contraindications": [
            "Dị ứng doxorubicin",
            "Suy tim nặng",
            "Bệnh tim tiềm ẩn",
            "Giảm bạch cầu/tiểu cầu nặng",
            "Có thai",
            "Đang cho con bú"
        ],
        "dosage": {
            "adult_standard": "60-75mg/m² IV mỗi 3 tuần",
            "adult_weekly": "20-30mg/m² IV mỗi tuần",
            "adult_cardiac_risk": "Giảm liều hoặc dùng liposomal doxorubicin",
            "notes": "Tổng liều tích lũy tối đa: 450-550mg/m² (nguy cơ độc tim). Dùng phác đồ 3 tuần"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Thận trọng, có thể giảm liều",
            "under_30": "Thận trọng, giảm liều"
        },
        "side_effects": [
            "Độc tim (suy tim, rối loạn nhịp - tích lũy, không hồi phục)",
            "Giảm bạch cầu, tiểu cầu (myelosuppression)",
            "Rụng tóc (phổ biến)",
            "Buồn nôn, nôn",
            "Loét miệng",
            "Da đỏ, đau khi truyền (extravasation - nguy hiểm)",
            "Nước tiểu đỏ (bình thường, không phải máu)",
            "Vô sinh"
        ],
        "interactions": [
            "Cyclophosphamide: tăng độc tim",
            "Trastuzumab: tăng độc tim",
            "Paclitaxel: có thể tăng độc tính",
            "Các anthracyclines khác: tăng độc tim"
        ],
        "pregnancy": "D - Chống chỉ định",
        "mechanism_of_action": "Doxorubicin là anthracycline, gắn vào DNA và ức chế enzyme topoisomerase II, ngăn cản quá trình sửa chữa DNA và gây đứt gãy DNA. Thuốc tạo ra các gốc tự do (free radicals) gây stress oxy hóa, tổn thương màng tế bào và DNA. Doxorubicin tích lũy trong ty thể, gây tổn thương ty thể và dẫn đến độc tim (cardiotoxicity). Thuốc tác động chủ yếu lên tế bào đang phân chia nhanh, gây độc tế bào và chết tế bào ung thư. Độc tim là do tích lũy liều (dose-dependent) và có thể không hồi phục",
        "monitoring": [
            "Chức năng tim trước mỗi chu kỳ (echo, MUGA scan - đo EF)",
            "Điện tâm đồ (ECG) trước và trong điều trị",
            "Tổng liều tích lũy (tối đa 450-550mg/m² để tránh độc tim)",
            "Công thức máu toàn phần (CBC) trước mỗi chu kỳ",
            "Chức năng gan (ALT, AST, bilirubin) trước mỗi chu kỳ",
            "Dấu hiệu suy tim (khó thở, phù, mệt mỏi) - có thể xảy ra muộn",
            "Theo dõi extravasation khi truyền (da đỏ, đau - nguy hiểm)",
            "Nước tiểu đỏ (bình thường, không phải máu)"
        ],
        "precautions": [
            "Theo dõi chặt chẽ tổng liều tích lũy (tối đa 450-550mg/m²)",
            "Đo EF trước mỗi chu kỳ nếu có nguy cơ độc tim cao",
            "Ngừng nếu EF giảm >10-15% hoặc có dấu hiệu suy tim",
            "Tránh extravasation khi truyền (có thể gây hoại tử da)",
            "Có thể dùng liposomal doxorubicin để giảm độc tim",
            "Tránh dùng với các thuốc khác gây độc tim (cyclophosphamide, trastuzumab)",
            "Độc tim có thể xảy ra muộn (sau nhiều năm) - cần theo dõi lâu dài",
            "Có thể gây vô sinh (cần tư vấn trước điều trị)"
        ],
        "pharmacokinetics": {
            "half_life": "20-48 giờ (dài)",
            "onset": "1-2 tuần (tác dụng lâm sàng)",
            "duration": "Kéo dài (tích lũy trong mô)",
            "protein_binding": ">90%",
            "clearance": "Gan (chuyển hóa), thận (thải trừ - chậm)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu. Bảo vệ khỏi ánh sáng",
        "black_box_warnings": "Có thể gây độc tim nặng và suy tim không hồi phục. Tổng liều tích lũy tối đa: 450-550mg/m². Theo dõi chức năng tim trước mỗi chu kỳ. Độc tim có thể xảy ra muộn (sau nhiều năm)",
        "drug_interactions": {
            "major": [
                {
                    "drug": "Cyclophosphamide",
                    "mechanism": "Cả hai đều gây độc tim, tác dụng cộng dồn làm tăng nguy cơ suy tim nghiêm trọng.",
                    "effect": "Tăng nguy cơ độc tim, suy tim không hồi phục",
                    "management": "Thận trọng khi dùng đồng thời. Giảm tổng liều tích lũy của cả hai thuốc. Theo dõi chức năng tim chặt chẽ."
                },
                {
                    "drug": "Trastuzumab",
                    "mechanism": "Cả hai đều gây độc tim, tác dụng cộng dồn làm tăng nguy cơ suy tim nghiêm trọng.",
                    "effect": "Tăng nguy cơ độc tim, suy tim không hồi phục",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi chức năng tim chặt chẽ. Có thể cần giảm liều hoặc tránh dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Paclitaxel",
                    "mechanism": "Có thể tăng độc tính của doxorubicin.",
                    "effect": "Tăng độc tính tổng thể",
                    "management": "Thận trọng khi dùng đồng thời. Theo dõi độc tính chặt chẽ."
                },
                {
                    "drug": "Các anthracyclines khác (Daunorubicin, Epirubicin, Idarubicin)",
                    "mechanism": "Cả hai đều gây độc tim tích lũy, tác dụng cộng dồn.",
                    "effect": "Tăng nguy cơ độc tim, suy tim",
                    "management": "Tính tổng liều tích lũy của tất cả anthracyclines. Giảm tổng liều tích lũy tối đa."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng doxorubicin",
                "Suy tim nặng - chống chỉ định tuyệt đối",
                "Có thai - chống chỉ định tuyệt đối, gây dị tật thai nhi (category D)",
                "Đang cho con bú - chống chỉ định"
            ],
            "tương_đối": [
                "Bệnh tim tiềm ẩn - thận trọng, theo dõi chức năng tim chặt chẽ",
                "Tổng liều tích lũy >450-550mg/m² - nguy cơ độc tim cao, nên ngừng",
                "Giảm bạch cầu/tiểu cầu nặng - trì hoãn điều trị cho đến khi hồi phục",
                "Suy gan - thận trọng, có thể cần giảm liều",
                "Suy thận - thận trọng, có thể cần giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "D",
            "pregnancy_details": "Chống chỉ định trong thai kỳ. Doxorubicin gây dị tật thai nhi, sẩy thai, và tử vong thai nhi. Không dùng trong thai kỳ trừ khi lợi ích vượt trội rõ ràng so với nguy cơ.",
            "lactation": {
                "safety": "Incompatible",
                "details": "Doxorubicin bài tiết vào sữa mẹ. Thuốc có thể gây độc tính nghiêm trọng cho trẻ sơ sinh.",
                "recommendation": "Không cho con bú khi dùng doxorubicin. Ngừng cho con bú hoặc ngừng thuốc."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, giảm liều 25-50%",
            "severe": "Thận trọng, giảm liều 50-75%",
            "notes": "Doxorubicin chuyển hóa chủ yếu qua gan. Suy gan làm giảm chuyển hóa, tăng nồng độ và độc tính. Theo dõi chức năng gan và độc tính chặt chẽ. Có thể cần giảm liều đáng kể ở suy gan."
        },
        "overdose_management": {
            "symptoms": [
                "Suy tim cấp (khó thở, phù, mệt mỏi)",
                "Rối loạn nhịp tim",
                "Giảm bạch cầu, tiểu cầu nặng (nhiễm trùng, chảy máu)",
                "Loét miệng nặng",
                "Nôn mửa nặng",
                "Extravasation (da đỏ, đau - nguy hiểm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng ngay doxorubicin",
                "Nếu có extravasation: ngừng truyền ngay, không rút kim, chườm lạnh, tham khảo phẫu thuật",
                "Điều trị suy tim: furosemide, ACE inhibitor, beta-blocker nếu cần",
                "Theo dõi và điều trị rối loạn nhịp tim",
                "Supportive care: bù dịch, điều trị nhiễm trùng, truyền máu nếu cần",
                "Theo dõi CBC, chức năng tim, chức năng gan",
                "Điều trị nôn mửa (ondansetron, granisetron)"
            ],
            "monitoring": "Chức năng tim (echo, ECG), CBC, chức năng gan, dấu hiệu nhiễm trùng, dấu hiệu chảy máu, dấu hiệu extravasation"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không có dạng uống (chỉ có IV)"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Truyền trong 15-30 phút (bolus) hoặc 1-4 giờ (infusion)",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "Bolus: 60-75mg/m² truyền trong 15-30 phút. Infusion: có thể truyền trong 1-4 giờ để giảm độc tính. QUAN TRỌNG: Theo dõi extravasation chặt chẽ (có thể gây hoại tử da). Bảo vệ khỏi ánh sáng."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Doxorubicin (Adriamycin)",
                "UpToDate - Doxorubicin Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    "Granisetron": {
        "group": "Oncology - Anti-emetic (5-HT3 Antagonist)",
        "vietnamese_name": "Granisetron, Kytril",
        "administration": ["PO", "IV"],
        "indications": [
            "Phòng và điều trị nôn do hóa trị",
            "Phòng nôn sau phẫu thuật",
            "Nôn do xạ trị"
        ],
        "contraindications": [
            "Dị ứng granisetron hoặc 5-HT3 antagonists"
        ],
        "dosage": {
            "adult_iv": "1mg IV x 1 lần trước hóa trị hoặc 0.01mg/kg IV",
            "adult_po": "1-2mg PO x 1 lần trước hóa trị, có thể lặp lại sau 12 giờ",
            "adult_prevention": "1-2mg PO x 1-2 lần/ngày",
            "notes": "Có thể dùng 30 phút - 1 giờ trước hóa trị"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu (phổ biến)",
            "Táo bón",
            "Chóng mặt",
            "Mệt mỏi",
            "Tăng transaminase (hiếm)",
            "QT kéo dài (hiếm)"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định (tăng tác dụng)",
            "Các 5-HT3 antagonists khác: không nên dùng đồng thời"
        ],
        "pregnancy": "B - Thận trọng",
        "mechanism_of_action": "Granisetron là 5-HT3 receptor antagonist, ức chế chọn lọc receptor serotonin type 3 (5-HT3) ở cả ngoại vi (dây thần kinh phế vị trong ruột) và trung ương (vùng chemoreceptor trigger zone - CTZ). Thuốc ngăn cản serotonin gắn vào receptor 5-HT3, giảm kích thích gây nôn từ hóa trị và xạ trị. Granisetron có ái lực cao với receptor 5-HT3 và tác dụng kéo dài, hiệu quả trong phòng và điều trị nôn do hóa trị, đặc biệt với các thuốc gây nôn mạnh (cisplatin, doxorubicin)",
        "monitoring": [
            "Đáp ứng điều trị (giảm nôn, buồn nôn)",
            "Dấu hiệu đau đầu (phổ biến)",
            "Dấu hiệu táo bón (phổ biến)",
            "Điện tâm đồ (ECG) nếu có nguy cơ QT kéo dài (hiếm)",
            "Chức năng gan nếu dùng lâu dài (tăng transaminase - hiếm)"
        ],
        "precautions": [
            "Dùng 30 phút - 1 giờ trước hóa trị để đạt hiệu quả tối đa",
            "Có thể dùng IV hoặc PO",
            "Có thể dùng kết hợp với corticosteroid (dexamethasone) để tăng hiệu quả",
            "Tránh dùng với apomorphine (chống chỉ định)",
            "Không nên dùng đồng thời với các 5-HT3 antagonists khác",
            "Có thể gây QT kéo dài (hiếm - cần theo dõi nếu có nguy cơ)",
            "Có thể dùng trong thai kỳ (category B - thận trọng)"
        ],
        "pharmacokinetics": {
            "half_life": "3-5 giờ (IV), 6-9 giờ (PO)",
            "onset": "1-3 phút (IV), 30-60 phút (PO)",
            "duration": "24 giờ",
            "protein_binding": "65%",
            "clearance": "Gan (chuyển hóa qua CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Apomorphine",
                    "mechanism": "Granisetron ức chế 5-HT3 receptor, có thể tăng tác dụng của apomorphine, gây hạ huyết áp nghiêm trọng.",
                    "effect": "Tăng tác dụng apomorphine, hạ huyết áp nghiêm trọng, nguy cơ tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng đồng thời."
                }
            ],
            "moderate": [
                {
                    "drug": "Các 5-HT3 antagonists khác (Ondansetron, Palonosetron)",
                    "mechanism": "Cả hai đều ức chế 5-HT3 receptor, không có lợi ích bổ sung.",
                    "effect": "Không tăng hiệu quả, có thể tăng tác dụng phụ",
                    "management": "Không nên dùng đồng thời. Chọn một trong hai."
                }
            ],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng granisetron hoặc 5-HT3 antagonists"
            ],
            "tương_đối": [
                "Bệnh nhân có tiền sử QT kéo dài - thận trọng, theo dõi ECG",
                "Suy gan - thận trọng, có thể cần giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần. Không có bằng chứng dị tật thai nhi, nhưng dữ liệu còn hạn chế. Dùng với thận trọng.",
            "lactation": {
                "safety": "Caution",
                "details": "Granisetron bài tiết vào sữa mẹ ở nồng độ thấp. Chưa có đủ dữ liệu về an toàn cho trẻ sơ sinh.",
                "recommendation": "Thận trọng khi cho con bú. Có thể dùng nếu lợi ích vượt trội nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Granisetron chuyển hóa chủ yếu qua gan (CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Táo bón nặng",
                "Chóng mặt",
                "QT kéo dài (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Supportive care",
                "Theo dõi ECG nếu có QT kéo dài",
                "Điều trị táo bón nếu cần"
            ],
            "monitoring": "ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Có thể uống với hoặc không thức ăn",
                "timing": "Uống 30 phút - 1 giờ trước hóa trị"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Tiêm trực tiếp hoặc truyền trong 5 phút",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "1mg IV x 1 lần trước hóa trị hoặc 0.01mg/kg IV. Có thể tiêm trực tiếp hoặc truyền trong 5 phút."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Granisetron (Kytril)",
                "UpToDate - Granisetron Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
    "Palonosetron": {
        "group": "Oncology - Anti-emetic (5-HT3 Antagonist)",
        "vietnamese_name": "Palonosetron, Aloxi",
        "administration": ["IV"],
        "indications": [
            "Phòng nôn do hóa trị (ngắn và trung hạn)",
            "Phòng nôn sau phẫu thuật"
        ],
        "contraindications": [
            "Dị ứng palonosetron hoặc 5-HT3 antagonists"
        ],
        "dosage": {
            "adult_chemotherapy": "0.25mg IV x 1 lần trước hóa trị",
            "adult_surgery": "0.075mg IV x 1 lần trước gây mê",
            "notes": "Tác dụng dài (48-72 giờ), chỉ cần 1 liều"
        },
        "renal_adjustment": {
            "normal": "Không đổi",
            "30_60": "Không đổi",
            "under_30": "Không đổi"
        },
        "side_effects": [
            "Đau đầu",
            "Táo bón",
            "Chóng mặt",
            "Mệt mỏi",
            "QT kéo dài (hiếm)"
        ],
        "interactions": [
            "Apomorphine: chống chỉ định"
        ],
        "pregnancy": "B - Thận trọng",
        "mechanism_of_action": "Palonosetron là 5-HT3 receptor antagonist thế hệ 2, ức chế chọn lọc receptor serotonin type 3 (5-HT3) ở cả ngoại vi và trung ương. Palonosetron có ái lực cao hơn và thời gian bán thải dài hơn so với các 5-HT3 antagonists thế hệ 1 (ondansetron, granisetron), cho phép dùng 1 liều duy nhất để phòng nôn trong 48-72 giờ. Thuốc ngăn cản serotonin gắn vào receptor 5-HT3, giảm kích thích gây nôn từ hóa trị. Palonosetron đặc biệt hiệu quả với hóa trị gây nôn trung hạn (delayed nausea)",
        "monitoring": [
            "Đáp ứng điều trị (giảm nôn, buồn nôn)",
            "Dấu hiệu đau đầu (phổ biến)",
            "Dấu hiệu táo bón (phổ biến)",
            "Điện tâm đồ (ECG) nếu có nguy cơ QT kéo dài (hiếm)",
            "Chức năng gan nếu dùng lâu dài"
        ],
        "precautions": [
            "Dùng 30 phút trước hóa trị để đạt hiệu quả tối đa",
            "Chỉ cần dùng 1 liều (tác dụng kéo dài 48-72 giờ)",
            "Có thể dùng kết hợp với corticosteroid (dexamethasone) để tăng hiệu quả",
            "Tránh dùng với apomorphine (chống chỉ định)",
            "Có thể gây QT kéo dài (hiếm - cần theo dõi nếu có nguy cơ)",
            "Có thể dùng trong thai kỳ (category B - thận trọng)",
            "Tác dụng dài hơn so với ondansetron và granisetron"
        ],
        "pharmacokinetics": {
            "half_life": "40 giờ (rất dài)",
            "onset": "5 phút (IV)",
            "duration": "48-72 giờ (rất dài)",
            "protein_binding": "62%",
            "clearance": "Gan (chuyển hóa qua CYP2D6, CYP3A4), thận (thải trừ)"
        },
        "storage": "Bảo quản ở nhiệt độ phòng (15-30°C), tránh ánh sáng. Bảo quản ở tủ lạnh (2-8°C) nếu yêu cầu",
        "black_box_warnings": None,
        "drug_interactions": {
            "major": [
                {
                    "drug": "Apomorphine",
                    "mechanism": "Palonosetron ức chế 5-HT3 receptor, có thể tăng tác dụng của apomorphine, gây hạ huyết áp nghiêm trọng.",
                    "effect": "Tăng tác dụng apomorphine, hạ huyết áp nghiêm trọng, nguy cơ tử vong",
                    "management": "CHỐNG CHỈ ĐỊNH - không dùng đồng thời."
                }
            ],
            "moderate": [],
            "minor": []
        },
        "contraindications": {
            "tuyệt_đối": [
                "Dị ứng palonosetron hoặc 5-HT3 antagonists"
            ],
            "tương_đối": [
                "Bệnh nhân có tiền sử QT kéo dài - thận trọng, theo dõi ECG",
                "Suy gan - thận trọng, có thể cần giảm liều"
            ]
        },
        "pregnancy_lactation": {
            "fda_category": "B",
            "pregnancy_details": "Có thể dùng trong thai kỳ nếu cần. Không có bằng chứng dị tật thai nhi, nhưng dữ liệu còn hạn chế. Dùng với thận trọng.",
            "lactation": {
                "safety": "Caution",
                "details": "Palonosetron bài tiết vào sữa mẹ ở nồng độ thấp. Chưa có đủ dữ liệu về an toàn cho trẻ sơ sinh.",
                "recommendation": "Thận trọng khi cho con bú. Có thể dùng nếu lợi ích vượt trội nguy cơ."
            }
        },
        "hepatic_adjustment": {
            "mild": "Không đổi",
            "moderate": "Thận trọng, có thể cần giảm liều",
            "severe": "Thận trọng, giảm liều 25-50%",
            "notes": "Palonosetron chuyển hóa chủ yếu qua gan (CYP2D6, CYP3A4). Suy gan có thể làm giảm chuyển hóa, tăng nồng độ và tác dụng phụ."
        },
        "overdose_management": {
            "symptoms": [
                "Đau đầu nặng",
                "Táo bón nặng",
                "Chóng mặt",
                "QT kéo dài (hiếm)"
            ],
            "antidote": "Không có antidote đặc hiệu",
            "treatment": [
                "Ngừng thuốc",
                "Supportive care",
                "Theo dõi ECG nếu có QT kéo dài",
                "Điều trị táo bón nếu cần"
            ],
            "monitoring": "ECG, dấu hiệu lâm sàng"
        },
        "reversal_agents": None,
        "administration_instructions": {
            "oral": {
                "with_food": "Không áp dụng",
                "timing": "Không có dạng uống (chỉ có IV)"
            },
            "iv": {
                "reconstitution": "Pha với NS hoặc D5W theo hướng dẫn nhà sản xuất",
                "infusion_rate": "Tiêm trực tiếp hoặc truyền trong 30 giây",
                "compatibility": ["NS", "D5W"],
                "incompatibility": [],
                "notes": "0.25mg IV x 1 lần trước hóa trị hoặc 0.075mg IV x 1 lần trước gây mê. Tiêm trực tiếp hoặc truyền trong 30 giây. Chỉ cần 1 liều (tác dụng kéo dài 48-72 giờ)."
            }
        },
        "references": {
            "primary_sources": [
                "FDA Drug Label - Palonosetron (Aloxi)",
                "UpToDate - Palonosetron Drug Information",
                "Goodman & Gilman's Pharmacological Basis of Therapeutics, 14th ed"
            ],
            "last_updated": "2025-01-15",
            "evidence_level": "High (FDA-approved, extensive clinical data)"
        }
    },
}

__all__ = ['ONCOLOGY_DRUGS']
